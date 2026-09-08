#!/usr/bin/env python3
"""Crop the SceneGuard architecture panel from a paper PDF.

The crop removes surrounding page text, the figure caption, and excess margins.
It does not alter pixels inside the architecture panel.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Source paper PDF.")
    parser.add_argument("--output", type=Path, required=True, help="Output PNG path.")
    parser.add_argument(
        "--page",
        type=int,
        default=4,
        help="One-indexed PDF page containing the architecture panel.",
    )
    parser.add_argument(
        "--crop",
        type=float,
        nargs=4,
        metavar=("X0", "Y0", "X1", "Y1"),
        default=(39.0, 35.0, 573.0, 135.0),
        help="Crop rectangle in PDF points.",
    )
    parser.add_argument("--scale", type=float, default=3.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.page < 1:
        raise ValueError("--page must be one-indexed and greater than zero.")
    if args.scale <= 0:
        raise ValueError("--scale must be greater than zero.")

    document = pymupdf.open(args.input)
    if args.page > document.page_count:
        raise ValueError(
            f"Requested page {args.page}, but the PDF has {document.page_count} pages."
        )

    page = document[args.page - 1]
    crop = pymupdf.Rect(*args.crop) & page.rect
    if crop.is_empty:
        raise ValueError("The crop rectangle does not intersect the selected page.")

    pixmap = page.get_pixmap(
        matrix=pymupdf.Matrix(args.scale, args.scale),
        clip=crop,
        alpha=False,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(args.output)
    print(
        f"Saved {args.output} ({pixmap.width} × {pixmap.height}px); "
        f"page {args.page}, crop {tuple(args.crop)}, scale {args.scale}."
    )


if __name__ == "__main__":
    main()
