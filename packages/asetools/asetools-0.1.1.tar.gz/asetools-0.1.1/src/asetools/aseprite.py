"""
Load an Aseprite file
"""

import zlib
from io import BytesIO
from struct import unpack
from typing import BinaryIO, Optional, Union
from pathlib import Path

"""
Aseprite file format doc:

https://github.com/aseprite/aseprite/blob/master/docs/ase-file-specs.md

An aseprite image can be considered as a 2D array: layers are the rows and
frames are the columns.

The main class, AsepriteImage, contains both layers (a list of Layer instances)
and frames (a list of Frame instances). the Frame class contains Cels
instances. Cels are the individual cells of the array: the intersection of a
row and a column.
"""

MAGIC = 0xA5E0
FRAME_MAGIC = 0xF1FA

LAYER_CHUNK = 0x2004
CEL_CHUNK = 0x2005
PALETTE_CHUNK = 0x2019
SLICE_CHUNK = 0x2022

LINKED_CEL_TYPE = 1
COMPRESSED_IMAGE_CEL_TYPE = 2


class NotAsepriteFile(Exception):
    pass


class NotSupported(Exception):
    pass


class ChildLayerWithoutParent(Exception):
    pass


class Layer:
    def __init__(self, image: "AsepriteImage", name: str, child_level: int) -> None:
        self.image = image
        self.visible = True
        self.is_group = False
        self.name = name
        self.child_level = child_level
        self.parent: Optional[Layer] = None

    def is_really_visible(self) -> bool:
        if not self.visible:
            return False
        if self.parent is None:
            return True
        return self.parent.is_really_visible()


class Cel:
    def __init__(self, layer: Layer) -> None:
        self.layer = layer
        self.position = (0, 0)
        self.size = (0, 0)
        self.pixels = b""


class Slice:
    def __init__(self, name: str, pos: tuple[int, int], size: tuple[int, int]) -> None:
        self.name = name
        self.position = pos
        self.size = size


class Frame:
    def __init__(self, image: "AsepriteImage") -> None:
        self.image = image
        self.cels: list[Cel] = []

    def append_cel(self, layer: Layer) -> None:
        self.cels.append(Cel(layer))


RGBA = tuple[int, int, int, int]


class AsepriteImage:
    def __init__(self, filename: Union[str, Path]) -> None:
        self.palette: list[RGBA] = []
        self.size = (0, 0)
        self.frame_count = 0
        self.transparent_color = 0
        self.depth = 0
        self.color_count = 0
        self.layers: list[Layer] = []
        self.frames: list[Frame] = []
        self.slices: list[Slice] = []

        with open(str(filename), "rb") as fp:
            self.read_header(fp)
            for _ in range(self.frame_count):
                self.read_frame(fp)

    def read_header(self, fp: BinaryIO) -> None:
        data = fp.read(44)
        (
            file_size,
            magic,
            self.frame_count,
            width,
            height,
            self.depth,
            flags,
            speed,
            zero1,
            zero2,
            self.transparent_color,
            self.color_count,
            px_width,
            px_height,
            grid_x,
            grid_y,
            grid_width,
            grid_height,
        ) = unpack("<LHHHHHLHLLBxxxHBBhhHH", data)
        self.size = (width, height)
        if magic != MAGIC:
            raise NotAsepriteFile()
        if zero1 != 0 or zero2 != 0:
            raise NotAsepriteFile()
        # Skip padding
        fp.seek(128)

    def read_frame(self, fp: BinaryIO) -> None:
        data = fp.read(16)
        frame_size, magic, old_chunks, duration, new_chunks = unpack("<LHHHxxL", data)
        if magic != FRAME_MAGIC:
            raise NotAsepriteFile(f"Invalid frame magic ({magic})")
        chunk_count = old_chunks if old_chunks < 0xFFFF else new_chunks

        frame = Frame(self)
        self.frames.append(frame)
        if len(self.frames) > 1:
            for layer in self.layers:
                frame.append_cel(layer)
        for _ in range(chunk_count):
            self.read_chunk(fp)

    def read_chunk(self, fp: BinaryIO) -> None:
        chunk_size, chunk_type = unpack("<LH", fp.read(6))
        data = fp.read(chunk_size - 6)
        chunk_fp = BytesIO(data)
        if chunk_type == LAYER_CHUNK:
            self.read_layer_chunk(chunk_fp)
        elif chunk_type == CEL_CHUNK:
            self.read_cel_chunk(chunk_fp)
        elif chunk_type == PALETTE_CHUNK:
            self.read_palette_chunk(chunk_fp)
        elif chunk_type == SLICE_CHUNK:
            self.read_slice_chunk(chunk_fp)

    def set_layer_parent(self, child_layer: Layer) -> None:
        # The parent is the latest added layer whose child level is
        # child_level - 1
        wanted_child_level = child_layer.child_level - 1
        for layer in self.layers[::-1]:
            if layer.child_level == wanted_child_level:
                child_layer.parent = layer
                return
        raise ChildLayerWithoutParent(child_layer.name)

    def read_layer_chunk(self, fp: BinaryIO) -> None:
        flags, layer_type, child_level, blend_mode, opacity, layer_name_length = unpack(
            "<HHHxxxxHbxxxH", fp.read(18)
        )
        name = str(fp.read(), "utf-8")
        layer = Layer(self, name, child_level)
        layer.visible = bool(flags & 1)
        layer.is_group = layer_type == 1

        if child_level > 0:
            self.set_layer_parent(layer)

        self.layers.append(layer)
        # Create a matching cel in the first frame, so that read_cel_chunk has
        # a place to write
        self.frames[0].append_cel(layer)

    def read_cel_chunk(self, fp: BinaryIO) -> None:
        index, pos_x, pos_y, opacity, cel_type = unpack("<HhhBH", fp.read(9))
        fp.read(7)
        if cel_type == LINKED_CEL_TYPE:
            linked_frame_index = unpack("<H", fp.read(2))[0]
            linked_cel = self.frames[linked_frame_index].cels[index]
            self.frames[-1].cels[index] = linked_cel
        elif cel_type == COMPRESSED_IMAGE_CEL_TYPE:
            cel = self.frames[-1].cels[index]
            cel.position = [pos_x, pos_y]
            cel.size = unpack("<HH", fp.read(4))
            cel.pixels = zlib.decompress(fp.read())
        else:
            raise NotSupported(f"Unsupported cel_type {cel_type}")

    def read_palette_chunk(self, fp: BinaryIO) -> None:
        self.palette = [(0, 0, 0, 0)] * self.color_count
        size, first, last = unpack("<LLL", fp.read(12))
        fp.read(8)
        for idx in range(first, last + 1):
            flags, red, green, blue, alpha = unpack("<HBBBB", fp.read(6))
            if flags != 0:
                raise NotSupported("Named colors in palette")
            self.palette[idx] = (red, green, blue, alpha)
        self.palette[self.transparent_color] = (0, 0, 0, 0)

    def read_slice_chunk(self, fp: BinaryIO) -> None:
        count, flags, name_length = unpack("<LLxxxxH", fp.read(14))
        if count > 1:
            raise NotSupported("Multi-key slices")
        if flags != 0:
            raise NotSupported(f"Slice flags {flags}")
        name = str(fp.read(name_length), "utf-8")

        frame_number, x, y, width, height = unpack("<LllLL", fp.read(20))
        self.slices.append(Slice(name, (x, y), (width, height)))
