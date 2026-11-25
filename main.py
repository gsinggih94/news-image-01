#!/usr/bin/env python3
"""news-image-20261124 entry: copy the front-page image to the output dir.

The image (entry.png, beside this file) is a 1024x1024 newspaper front
page summing up Tuesday 24 November 2026: Nvidia reinstates Jensen
Huang (+31%), Ukraine hits a Russian warship in Libya, Trump lands in
the Philippines, 12,000 flee a Manchester concert, and the US loses its
measles-free status, plus a footer strip of further news.

Runs with the standard library only, no network, no clock, no random
input: the same input bytes always produce the same output bytes.
"""
import os
import shutil
import sys

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        head = f.read(8)
    if head != PNG_MAGIC and not head.startswith(JPEG_MAGIC):
        print("entry.png is not a PNG or JPEG", file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print("entry.png is over 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    with open(src, "rb") as f:
        before = f.read()
    with open(dst, "rb") as f:
        after = f.read()
    if before != after:
        print("copied bytes differ from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
