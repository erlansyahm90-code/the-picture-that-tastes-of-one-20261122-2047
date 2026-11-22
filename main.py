"""Copy the entry picture to the output directory and verify it.

The picture itself lives in assets/entry.png next to this script. This
program only copies that file and checks the result, so it needs no
network and no image data embedded in the code.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def png_dimensions(path):
    """Return (width, height) of a PNG file, or None if it is not a PNG."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "assets", "entry.png")
    if not os.path.isfile(source):
        print(f"error: missing source image: {source}", file=sys.stderr)
        return 1
    source_size = os.path.getsize(source)
    if source_size > MAX_BYTES:
        print(f"error: source image is {source_size} bytes, over the "
              f"{MAX_BYTES} byte limit — shrink assets/entry.png first",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)

    size = os.path.getsize(target)
    dimensions = png_dimensions(target)
    if dimensions is None:
        print("error: output is not a valid PNG file", file=sys.stderr)
        return 1
    width, height = dimensions
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"error: output is {width}x{height}, "
              f"over the {MAX_DIMENSION}x{MAX_DIMENSION} limit",
              file=sys.stderr)
        return 1
    if size > MAX_BYTES:
        print(f"error: output is {size} bytes, over the "
              f"{MAX_BYTES} byte limit", file=sys.stderr)
        return 1

    print(f"wrote {target}: PNG {width}x{height}, {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
