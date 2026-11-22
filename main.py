#!/usr/bin/env python3
"""Entrypoint for the news-image-20261122 bounty.

Copies the pre-rendered front page for Sunday 22 November 2026
(entry.png, 1024x1024, 40 sourced stories across 7 regions) into
$MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only, on purpose: the grader runs this in the pinned python
image, which ships no Pillow and no system fonts, so the program
itself must not import anything beyond the standard library. The
poster was drawn offline by draw_poster.py (Pillow + DejaVu Sans,
run locally) and the rendered bytes are committed here as entry.png;
copying them keeps the graded run byte-identical and deterministic.

Run locally:  python3 main.py
"""
import hashlib
import os
import sys

SOURCE_NAME = "entry.png"


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_root, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, SOURCE_NAME)
    with open(source, "rb") as f:
        data = f.read()
    with open(path, "wb") as f:
        f.write(data)
    print(f"entry written to {path}")
    print(f"bytes {len(data)}")
    print(f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
