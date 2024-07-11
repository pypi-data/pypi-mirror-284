# Asetools

[Aseprite][] is a wonderful pixelart tool. Unfortunately its license is not OSI compliant, even if the source code is available. This makes it complicated to rely on the tool being available everywhere it's needed. This is a problem for CI servers or open-source application stores like F-Droid.

Asetools are open-source command-line tools to work with Aseprite images.

[Aseprite]: https://aseprite.com

## Tools

### asesplit

The `asesplit` tool turns .ase images into .png. It can extract individual layers and/or slices, trim and rotate them.

<!-- [[[cog
from subprocess import run
p = run(["asesplit", "--help"], check=True, capture_output=True, text=True)
print(f"```\n{p.stdout}```")
]]] -->
```
usage: asesplit [-h] [--split-layers] [--split-slices] [--trim]
                [--rotate ANGLE] [--dry-run]
                ase_file format

Turn an Aseprite file into one or several png files.

positional arguments:
  ase_file
  format          Define the name of the generated files. Supported keywords:
                  {title}, {layer}, {frame}, {slice}

options:
  -h, --help      show this help message and exit
  --split-layers
  --split-slices
  --trim
  --rotate ANGLE  Rotate image by ANGLE degrees counter-clockwise
  --dry-run
```
<!-- [[[end]]] -->

### aseinfo

The `aseinfo` tool gives you information about the content of a .ase file.

<!-- [[[cog
from subprocess import run
p = run(["aseinfo", "--help"], check=True, capture_output=True, text=True)
print(f"```\n{p.stdout}```")
]]] -->
```
usage: aseinfo [-h] [-j] ase_file

Display info about an aseprite file

positional arguments:
  ase_file

options:
  -h, --help  show this help message and exit
  -j, --json  JSON output
```
<!-- [[[end]]] -->

## Installation

The recommended way to install is using [pipx][].

```
pipx install asetools
```

[pipx]: https://pipx.pypa.io/stable/

## Tests

You can run tests using `pytest`. Just run `pytest` in this directory.

## Warning

Asetools works well for me: it has been used for years now in [Pixel Wheels](https://agateau.com/projects/pixelwheels), but its support for .ase files is limited to the subset of Aseprite features I use. In particular, it currently only supports sprites with a color palette.
