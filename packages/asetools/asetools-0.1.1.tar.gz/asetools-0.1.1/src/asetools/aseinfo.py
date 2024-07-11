"""
Display info about an aseprite file
"""

import argparse
import json

from typing import Any

from asetools.aseprite import AsepriteImage, Layer, Slice


def print_text(image: AsepriteImage) -> None:
    print(f"size={image.size[0]}x{image.size[1]}")
    print(f"depth={image.depth}")
    print(f"color_count={image.color_count}")
    print(f"frame_count={image.frame_count}")
    print(f"transparent_color={image.transparent_color}")
    print("# layers")
    for idx, layer in reversed(list(enumerate(image.layers))):
        print(f"{idx}: {layer.name:40} visible={layer.visible} group={layer.is_group}")
    print("# palette (RGBA)")
    for idx, color in enumerate(image.palette):
        r, g, b, a = color
        print(f"{idx:3}: #{r:02x}{b:02x}{g:02x}{a:02x}")
    print("# slices")
    for slice_ in image.slices:
        print(f"{slice_.name:40} pos={slice_.position} size={slice_.size}")


def create_layer_dict(layer: Layer) -> dict[str, Any]:
    return {
        "name": layer.name,
        "visible": layer.visible,
        "is_group": layer.is_group,
    }


def create_slice_dict(slice: Slice) -> dict[str, Any]:
    return {
        "name": slice.name,
        "position": slice.position,
        "size": slice.size,
    }


def print_json(image: AsepriteImage) -> None:
    dct = {
        "size": image.size,
        "depth": image.depth,
        "color_count": image.color_count,
        "frame_count": image.frame_count,
        "transparent_color": image.transparent_color,
        "palette": [f"#{r:02x}{b:02x}{g:02x}{a:02x}" for r, g, b, a in image.palette],
        "layers": [create_layer_dict(x) for x in image.layers],
        "slices": [create_slice_dict(x) for x in image.slices],
    }
    print(json.dumps(dct))


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    parser.add_argument("-j", "--json", action="store_true", help="JSON output")
    parser.add_argument("ase_file")

    args = parser.parse_args()

    image = AsepriteImage(args.ase_file)

    if args.json:
        print_json(image)
    else:
        print_text(image)

    return 0
