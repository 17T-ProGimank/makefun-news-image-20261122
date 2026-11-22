#!/usr/bin/env python3
"""Entrypoint for the news-image-20261122 bounty.

Renders the front page for Sunday 22 November 2026 into
$MAKEFUN_OUTPUT_DIR/entry.png (1024x1024, deterministic).

Run locally:  python3 main.py
The drawing itself lives in draw_poster.py, imported from this directory.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import draw_poster  # noqa: E402


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    path = draw_poster.render(out_dir)
    print(f"entry written to {path}")


if __name__ == "__main__":
    main()
