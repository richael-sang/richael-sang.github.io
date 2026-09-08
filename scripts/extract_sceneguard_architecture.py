#!/usr/bin/env python3
"""Crop surrounding title and caption from the SceneGuard architecture image.

The crop removes the top title, bottom figure caption, and excess margins.
It does not alter pixels inside the architecture panel.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Source image.")
    parser.add_argument("--output", type=Path, required=True, help="Output PNG path.")
    parser.add_argument(
        "--crop",
        type=int,
        nargs=4,
        metavar=("X0", "Y0", "X1", "Y1"),
        default=(5, 74, 1019, 699),
        help="Crop rectangle in source-image pixels.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = Image.open(args.input).convert("RGB")
    x0, y0, x1, y1 = args.crop
    if not (0 <= x0 < x1 <= source.width and 0 <= y0 < y1 <= source.height):
        raise ValueError(
            f"Crop {tuple(args.crop)} is outside source dimensions "
            f"{source.width} × {source.height}."
        )

    cropped = source.crop((x0, y0, x1, y1))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(args.output, format="PNG", optimize=True)
    print(
        f"Saved {args.output} ({cropped.width} × {cropped.height}px); "
        f"crop {tuple(args.crop)} from {source.width} × {source.height}px."
    )


if __name__ == "__main__":
    main()
