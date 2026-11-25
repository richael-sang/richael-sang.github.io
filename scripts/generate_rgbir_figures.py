#!/usr/bin/env python3
"""Generate RGB–IR project-page figures and compress verified demo plates."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image


NAVY = "#1E3A5F"
BLUE = "#3D7CC9"
BLUE_DEEP = "#2A5F9E"
BLUE_SOFT = "#7EACDC"
IR = "#E07A3D"
IR_SOFT = "#E8A06A"
PURPLE = "#7A4E9A"
PALE = "#F6F9FC"
PALE_BLUE = "#EEF4FB"
PALE_ORANGE = "#F8EDE4"
LINE = "#D4E2EF"
MUTED = "#5B6F82"
GREY = "#9AABBC"
WHITE = "#FFFFFF"

ADVANTAGE_ORDER = ["Visible", "Infrared", "Multimodal seed1", "Multimodal seed2"]
ABLATION_ORDER = [
    "Default multimodal",
    "Static 0.25",
    "Static 0.50",
    "Static 0.75",
    "Dynamic gate",
    "Residual gate",
]
CHALLENGE_ORDER = ["Equal fusion", "Dynamic weighting"]
CHALLENGE_METRICS = ["AP", "AP50", "AP75"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("assets/data/rgbir/figure-data.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("assets/images/projects/infrared-visible"))
    parser.add_argument("--preview-dir", type=Path)
    parser.add_argument("--pptx-media", type=Path, default=Path("reference_materials/rgbir-pptx-media"))
    parser.add_argument("--qual-source", type=Path, default=Path("reference_materials/rgbir-thesis-images/p35_2.png"))
    return parser.parse_args()


def configure_style() -> None:
    matplotlib.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.titleweight": 700,
            "axes.labelcolor": MUTED,
            "axes.edgecolor": LINE,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "svg.fonttype": "none",
            "svg.hashsalt": "rgbir-web-figures",
        }
    )


def load_data(path: Path) -> list[dict[str, str | float]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"figure", "condition", "metric", "value", "unit", "source"}
    if not rows or set(rows[0]) != required:
        raise ValueError(f"{path} must contain exactly these columns: {sorted(required)}")
    for row in rows:
        row["value"] = float(row["value"])
    return rows


def values(
    rows: list[dict[str, str | float]],
    figure: str,
    metric: str,
    order: list[str],
) -> list[float]:
    lookup = {
        str(row["condition"]): float(row["value"])
        for row in rows
        if row["figure"] == figure and row["metric"] == metric
    }
    missing = [condition for condition in order if condition not in lookup]
    if missing:
        raise ValueError(f"Missing {figure}/{metric} values for: {missing}")
    return [lookup[condition] for condition in order]


def save_figure(fig: plt.Figure, stem: str, output_dir: Path, preview_dir: Path | None, png: bool = False) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg_path = output_dir / f"{stem}.svg"
    fig.savefig(svg_path, format="svg", bbox_inches="tight", facecolor=WHITE, metadata={"Date": None, "Creator": "RGB-IR figure generator"})
    svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
    if png or preview_dir:
        target = (preview_dir or output_dir) / f"{stem}.png"
        if preview_dir:
            preview_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(target, dpi=200, bbox_inches="tight", facecolor=WHITE)
        if png and preview_dir:
            fig.savefig(output_dir / f"{stem}.png", dpi=200, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


def rounded(ax, xy, width, height, facecolor, edgecolor, lw=1.1, radius=0.08, z=2) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle=f"round,pad=0.012,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=lw,
        zorder=z,
    )
    ax.add_patch(patch)
    return patch


def arrow(ax, start, end, color=MUTED) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.15,
            color=color,
            zorder=3,
        )
    )


def make_concept(output_dir: Path, preview_dir: Path | None) -> None:
    fig, ax = plt.subplots(figsize=(10.8, 4.15))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.4)
    ax.axis("off")
    fig.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    rounded(ax, (0.25, 1.55), 2.35, 2.05, PALE_BLUE, BLUE, radius=0.12)
    rounded(ax, (0.25, 0.25), 2.35, 1.15, PALE_ORANGE, IR, radius=0.12)
    ax.text(1.43, 3.15, "Visible image", ha="center", color=BLUE_DEEP, fontsize=11, weight="bold")
    ax.text(1.43, 2.55, "texture · colour\nboundaries", ha="center", color=MUTED, fontsize=8.2)
    ax.text(1.43, 0.92, "Infrared image", ha="center", color=IR, fontsize=11, weight="bold")
    ax.text(1.43, 0.52, "thermal contrast", ha="center", color=MUTED, fontsize=8.2)

    arrow(ax, (2.7, 2.55), (3.45, 2.15), BLUE)
    arrow(ax, (2.7, 0.85), (3.45, 1.55), IR)

    rounded(ax, (3.5, 0.85), 3.2, 2.55, PALE, BLUE, radius=0.12)
    ax.text(5.1, 2.95, "Adaptive fusion", ha="center", color=NAVY, fontsize=12, weight="bold")
    ax.text(5.1, 2.35, r"$F = \alpha F_{\mathrm{vis}} + (1-\alpha) F_{\mathrm{ir}}$", ha="center", color=BLUE_DEEP, fontsize=10)
    ax.text(5.1, 1.7, "Learn when to trust\nvisible or infrared", ha="center", color=MUTED, fontsize=8.4)
    ax.text(5.1, 1.15, "α may change by scale / input", ha="center", color=PURPLE, fontsize=7.8)

    arrow(ax, (6.8, 2.1), (7.55, 2.1), BLUE)

    rounded(ax, (7.6, 0.85), 3.95, 2.55, PALE_BLUE, BLUE_DEEP, radius=0.12)
    ax.text(9.58, 2.95, "Object detection", ha="center", color=NAVY, fontsize=12, weight="bold")
    ax.text(9.58, 2.25, "boxes  ·  classes  ·  scores", ha="center", color=BLUE_DEEP, fontsize=9.5)
    ax.text(9.58, 1.45, "Not universally better.\nMore useful when modality\nreliability becomes uneven.", ha="center", color=MUTED, fontsize=8.2)

    ax.text(0.25, 4.15, "Visible + infrared  →  adaptive fusion  →  detection", ha="left", color=NAVY, fontsize=13, weight="bold")
    save_figure(fig, "concept-overview", output_dir, preview_dir, png=True)


def make_architecture(output_dir: Path, preview_dir: Path | None) -> None:
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    ax.set_xlim(0, 13.2)
    ax.set_ylim(0, 5.2)
    ax.axis("off")
    fig.set_facecolor(WHITE)

    stages = [
        (0.2, 3.15, 2.3, 1.35, "Visible image", "Visible features", PALE_BLUE, BLUE),
        (0.2, 0.7, 2.3, 1.35, "Infrared image", "Infrared features", PALE_ORANGE, IR),
        (3.3, 1.7, 2.55, 1.8, "Multimodal fusion", "feature-level combine", PALE, BLUE_DEEP),
        (6.55, 1.7, 2.35, 1.8, "Multi-scale\nfeatures", "FPN levels p2–p5", PALE_BLUE, BLUE),
        (9.55, 1.7, 3.35, 1.8, "DiffusionDet head", "boxes + classes + scores", PALE_BLUE, BLUE_DEEP),
    ]
    for x, y, w, h, title, sub, face, edge in stages:
        rounded(ax, (x, y), w, h, face, edge, radius=0.1)
        ax.text(x + w / 2, y + h * 0.66, title, ha="center", va="center", color=NAVY, fontsize=10.5, weight="bold")
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center", color=MUTED, fontsize=8)

    arrow(ax, (2.55, 3.75), (3.3, 2.85), BLUE)
    arrow(ax, (2.55, 1.35), (3.3, 2.25), IR)
    arrow(ax, (5.9, 2.6), (6.5, 2.6), BLUE)
    arrow(ax, (8.95, 2.6), (9.5, 2.6), BLUE)

    ax.text(4.58, 1.35, "E2E-MFD-HOD  ·  Detectron2  ·  DiffusionDet", ha="center", color=MUTED, fontsize=8.2)
    ax.text(0.2, 4.9, "Conceptual pipeline only — no unverified internal modules", ha="left", color=NAVY, fontsize=12.5, weight="bold")
    save_figure(fig, "architecture", output_dir, preview_dir)


def make_advantage(rows: list[dict[str, str | float]], output_dir: Path, preview_dir: Path | None) -> None:
    ap = values(rows, "advantage", "AP", ADVANTAGE_ORDER)
    colors = [BLUE, IR, BLUE_DEEP, BLUE_DEEP]
    fig, ax = plt.subplots(figsize=(9.6, 4.2), constrained_layout=True)
    fig.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)
    x = np.arange(len(ADVANTAGE_ORDER))
    bars = ax.bar(x, ap, color=colors, width=0.32, edgecolor="none")
    for bar, value in zip(bars, ap):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.7, f"{value:.2f}", ha="center", color=NAVY, fontsize=9)
    ax.set_xticks(x, ["Visible", "Infrared", "Multimodal\nseed 1", "Multimodal\nseed 2"])
    ax.set_ylim(0, 62)
    ax.set_ylabel("AP")
    ax.grid(axis="y", color=LINE, linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title("Combining RGB and infrared produces the strongest overall detector", loc="left", color=NAVY, fontsize=12.5)
    fig.text(0.99, 0.01, "Source: candidate-init official HOD results", ha="right", color=MUTED, fontsize=7)
    save_figure(fig, "multimodal-advantage", output_dir, preview_dir)


def make_ablation(rows: list[dict[str, str | float]], output_dir: Path, preview_dir: Path | None) -> None:
    ap = values(rows, "ablation", "AP", ABLATION_ORDER)
    default = ap[0]
    colors = [BLUE_DEEP if name == "Default multimodal" else GREY for name in ABLATION_ORDER]
    fig, ax = plt.subplots(figsize=(10.4, 4.55), constrained_layout=True)
    fig.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)
    y = np.arange(len(ABLATION_ORDER))
    bars = ax.barh(y, ap, color=colors, height=0.28)
    ax.axvline(default, color=BLUE, linestyle="--", linewidth=1)
    for bar, value in zip(bars, ap):
        delta = value - default
        label = f"{value:.2f}" if abs(delta) < 1e-6 else f"{value:.2f}  ({delta:+.2f})"
        ax.text(value + 0.06, bar.get_y() + bar.get_height() / 2, label, va="center", color=NAVY, fontsize=8)
    ax.set_xlim(50.8, 54.15)
    ax.set_yticks(y, ABLATION_ORDER)
    ax.invert_yaxis()
    ax.grid(axis="x", color=LINE, linewidth=0.7)
    ax.set_axisbelow(True)
    ax.set_xlabel("AP on the full benchmark")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title("Simple adaptive reweighting does not outperform default fusion", loc="left", color=NAVY, fontsize=12.5)
    fig.text(0.99, 0.01, "Source: full-benchmark fusion ablation", ha="right", color=MUTED, fontsize=7)
    save_figure(fig, "fusion-ablation", output_dir, preview_dir)


def make_preference(output_dir: Path, preview_dir: Path | None) -> None:
    fig, ax = plt.subplots(figsize=(10.6, 4.7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.3)
    ax.axis("off")
    fig.set_facecolor(WHITE)

    levels = [
        ("p5", "closer to balanced", 4.15, 7.7, PALE, PURPLE),
        ("p4", "closer to balanced", 3.55, 8.9, PALE_BLUE, BLUE_SOFT),
        ("p3", "more visible-oriented", 2.75, 10.5, PALE_BLUE, BLUE),
        ("p2", "more infrared-oriented", 1.75, 12.2, PALE_ORANGE, IR),
    ]
    for name, note, y, width, face, edge in levels:
        x = (12 - width) / 2
        rounded(ax, (x, y), width, 0.72, face, edge, radius=0.08)
        ax.text(6, y + 0.45, name, ha="center", color=NAVY, fontsize=12, weight="bold")
        ax.text(6, y + 0.16, note, ha="center", color=MUTED, fontsize=8.3)

    ax.text(0.3, 4.95, "Modality preference changes across feature scales", ha="left", color=NAVY, fontsize=13, weight="bold")
    ax.text(0.3, 0.85, "Dynamic-gate analysis. Preference is descriptive, not a causal claim.", ha="left", color=MUTED, fontsize=8.2)
    rounded(ax, (0.3, 0.2), 2.3, 0.42, PALE_ORANGE, IR, radius=0.06)
    ax.text(1.45, 0.4, "Infrared-leaning", ha="center", va="center", color=IR, fontsize=8, weight="bold")
    rounded(ax, (2.8, 0.2), 2.3, 0.42, PALE_BLUE, BLUE, radius=0.06)
    ax.text(3.95, 0.4, "Visible-leaning", ha="center", va="center", color=BLUE_DEEP, fontsize=8, weight="bold")
    rounded(ax, (5.3, 0.2), 2.3, 0.42, PALE, PURPLE, radius=0.06)
    ax.text(6.45, 0.4, "Near-balanced", ha="center", va="center", color=PURPLE, fontsize=8, weight="bold")
    save_figure(fig, "modality-preference", output_dir, preview_dir)


def make_challenge(rows: list[dict[str, str | float]], output_dir: Path, preview_dir: Path | None) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.15), constrained_layout=True)
    fig.set_facecolor(WHITE)
    for ax, metric in zip(axes, CHALLENGE_METRICS):
        vals = values(rows, "challenge", metric, CHALLENGE_ORDER)
        ax.set_facecolor(WHITE)
        bars = ax.bar([0, 1], vals, color=[GREY, BLUE], width=0.28)
        for bar, value in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, value + 0.35, f"{value:.2f}", ha="center", color=NAVY, fontsize=8.5, weight="bold")
        ax.set_xticks([0, 1], ["Equal", "Dynamic"])
        lo = min(vals) - 3
        ax.set_ylim(lo, max(vals) + 4)
        ax.set_title(metric, loc="left", color=NAVY)
        ax.grid(axis="y", color=LINE, linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ax.text(1, vals[1] - (max(vals) - lo) * 0.18, f"+{vals[1] - vals[0]:.2f}", ha="center", color=BLUE_DEEP, fontsize=8, weight="bold")
    fig.suptitle(
        "Supplementary challenge scenes: a modest positive signal under uneven conditions",
        x=0.01,
        ha="left",
        color=NAVY,
        fontsize=12.5,
        weight="bold",
    )
    fig.text(0.99, 0.01, "Automatically constructed subset — not an official benchmark", ha="right", color=MUTED, fontsize=7)
    save_figure(fig, "challenge-scenes", output_dir, preview_dir)


def _save_jpeg(image: Image.Image, dest: Path, width: int = 1280) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    rgb = image.convert("RGB")
    if rgb.width > width:
        ratio = width / rgb.width
        rgb = rgb.resize((width, max(1, int(rgb.height * ratio))), Image.Resampling.LANCZOS)
    rgb.save(dest, format="JPEG", quality=86, optimize=True)


def _trim_letterbox(image: Image.Image, threshold: int = 248) -> Image.Image:
    arr = np.asarray(image.convert("L"))
    mask = arr < threshold
    if not mask.any():
        return image
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    return image.crop((int(cols[0]), int(rows[0]), int(cols[-1]) + 1, int(rows[-1]) + 1))


def _strip_white_caption(image: Image.Image) -> Image.Image:
    arr = np.asarray(image.convert("L"))
    row_white = (arr > 245).mean(axis=1)
    header_end = 0
    limit = max(8, int(len(row_white) * 0.22))
    for index, share in enumerate(row_white[:limit]):
        if share > 0.72:
            header_end = index
    if header_end > 8:
        image = image.crop((0, header_end + 1, image.width, image.height))
    return _trim_letterbox(image)


def export_demo_assets(pptx_media: Path, qual_source: Path, output_dir: Path) -> None:
    demo_dir = output_dir / "demo"
    pair_visible = Image.open(pptx_media / "image3.png")
    pair_infrared = Image.open(pptx_media / "image4.png")
    _save_jpeg(_strip_white_caption(pair_visible), demo_dir / "pair-visible.jpg")
    _save_jpeg(_strip_white_caption(pair_infrared), demo_dir / "pair-infrared.jpg")

    if not qual_source.exists():
        return
    plate = Image.open(qual_source)
    # Verified 2x3 qualitative plate from the thesis figure.
    boxes = {
        "rain-visible": (0, 140, 1024, 816),
        "rain-equal": (1040, 140, 2064, 816),
        "rain-dynamic": (2080, 140, 3104, 816),
        "lowlight-visible": (0, 976, 1024, 1652),
        "lowlight-equal": (1040, 976, 2064, 1652),
        "lowlight-dynamic": (2080, 976, 3104, 1652),
    }
    for name, box in boxes.items():
        _save_jpeg(_strip_white_caption(plate.crop(box)), demo_dir / f"{name}.jpg")
    _save_jpeg(_strip_white_caption(pair_infrared), demo_dir / "lowlight-infrared.jpg")


def main() -> None:
    args = parse_args()
    configure_style()
    rows = load_data(args.data)
    make_concept(args.output_dir, args.preview_dir)
    make_architecture(args.output_dir, args.preview_dir)
    make_advantage(rows, args.output_dir, args.preview_dir)
    make_ablation(rows, args.output_dir, args.preview_dir)
    make_preference(args.output_dir, args.preview_dir)
    make_challenge(rows, args.output_dir, args.preview_dir)
    export_demo_assets(args.pptx_media, args.qual_source, args.output_dir)
    print(f"Generated RGB–IR figures in {args.output_dir}.")


if __name__ == "__main__":
    main()
