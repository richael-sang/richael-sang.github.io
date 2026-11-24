#!/usr/bin/env python3
"""Generate data figures for the Bosch multimodal SOP inspection page."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


INK = "#2A1F3D"
VIOLET = "#6B4FA0"
VIOLET_DEEP = "#4A3373"
LAVENDER = "#9C84C9"
LAVENDER_SOFT = "#CDBFE6"
BASE = "#C7C2CF"
SLATE = "#6F7F8F"
MUTED = "#625A6E"
LINE = "#E2DAF0"
WHITE = "#FFFFFF"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("assets/images/projects/bosch-sop"))
    return parser.parse_args()


def configure_style() -> None:
    matplotlib.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 9,
            "axes.labelcolor": MUTED,
            "axes.edgecolor": LINE,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "svg.fonttype": "none",
            "svg.hashsalt": "bosch-sop-web-figures",
        }
    )


def save(fig: plt.Figure, path: Path) -> None:
    fig.savefig(path, format="svg", facecolor=WHITE, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def request_reduction(out: Path) -> None:
    groups = ["Total raw requests", "Main requests", "Non-main requests"]
    baseline = np.array([240, 112, 128])
    m1 = np.array([202, 90, 112])
    y = np.arange(len(groups))[::-1]
    h = 0.3

    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.barh(y + h / 2, baseline, height=h, color=BASE, label="Before · dense main")
    ax.barh(y - h / 2, m1, height=h, color=VIOLET, label="After · M1 sparse main")
    for yi, b, m in zip(y, baseline, m1):
        ax.text(b + 3, yi + h / 2, f"{b}", va="center", fontsize=8.5, color=MUTED)
        ax.text(m + 3, yi - h / 2, f"{m}", va="center", fontsize=8.5, color=VIOLET_DEEP, fontweight="bold")
        ax.text(264, yi + 0.07, f"−{b - m} calls", va="center", ha="left", fontsize=10.5,
                color=VIOLET_DEEP, fontweight="bold")
        ax.text(264, yi - 0.2, f"−{(b - m) / b * 100:.1f}%", va="center", ha="left", fontsize=8.5,
                color=MUTED)
    ax.set_yticks(y, groups)
    ax.tick_params(axis="y", length=0, labelsize=9, labelcolor=INK)
    ax.set_xlim(0, 305)
    ax.set_xticks([0, 50, 100, 150, 200, 250])
    ax.set_xlabel("Requests in the same regression round (six videos)")
    ax.grid(axis="x", color=LINE, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, 1.2), ncol=2, frameon=False, fontsize=8.5,
              handlelength=1.2, columnspacing=1.6)
    save(fig, out / "request-reduction.svg")


def m1_schedule(out: Path) -> None:
    stages = ["S1 · Cover", "S2 · Black box", "S3 · Screws", "S4 · Labels", "S5 · Removal"]
    stride = [1, 1, 2, 2, 3]
    max_gap = [None, None, 2.5, 2.5, 3.5]
    colors = [LAVENDER_SOFT, LAVENDER_SOFT, LAVENDER, LAVENDER, VIOLET]
    x = np.arange(len(stages))

    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.bar(x, stride, width=0.42, color=colors)
    for xi, s, g in zip(x, stride, max_gap):
        top = s + 0.08
        if g is not None:
            ax.text(xi, top, f"max gap {g} s", ha="center", va="bottom", fontsize=7.8, color=MUTED)
            top += 0.3
        ax.text(xi, top, f"every {s}" if s > 1 else "every sample", ha="center", va="bottom",
                fontsize=8.5, color=INK, fontweight="bold")
    ax.set_xticks(x, stages)
    ax.tick_params(axis="x", length=0, labelsize=8.8, labelcolor=INK)
    ax.set_ylim(0, 3.9)
    ax.set_yticks([0, 1, 2, 3])
    ax.set_ylabel("Main stride (samples)")
    ax.grid(axis="y", color=LINE, linewidth=0.6)
    ax.set_axisbelow(True)
    save(fig, out / "m1-schedule.svg")


def optimisation_outcomes(out: Path) -> None:
    rows = [
        ("Removal prompt slimming", "module latency, 2.950 → 1.870 s", 36.6, "Rejected · system regression failed", LAVENDER),
        ("Sparse main + removal slimming", "wall time, single round", 32.0, "Rejected · key defects missed in two rounds", LAVENDER),
        ("Shared client + warmup", "wall time, single round", 11.7, "Kept as signal · not yet stable", SLATE),
    ]
    y = np.arange(len(rows))[::-1]

    fig, ax = plt.subplots(figsize=(6.8, 2.3))
    for yi, (name, unit, value, verdict, color) in zip(y, rows):
        ax.barh(yi, value, height=0.32, color=color)
        ax.text(value + 0.8, yi, f"−{value:.1f}%", va="center", fontsize=9, color=INK, fontweight="bold")
        ax.text(48, yi, verdict, va="center", ha="left", fontsize=8.3,
                color=VIOLET_DEEP if color == LAVENDER else SLATE)
    ax.set_yticks(y, [f"{name}\n{unit}" for name, unit, *_ in rows])
    ax.tick_params(axis="y", length=0, labelsize=8.4, labelcolor=INK)
    ax.set_xlim(0, 90)
    ax.set_xticks([0, 10, 20, 30, 40])
    ax.spines["bottom"].set_bounds(0, 40)
    ax.set_xlabel("Reported time reduction (%)", loc="left")
    ax.grid(axis="x", color=LINE, linewidth=0.6)
    ax.set_axisbelow(True)
    save(fig, out / "optimisation-outcomes.svg")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    configure_style()
    request_reduction(args.output_dir)
    m1_schedule(args.output_dir)
    optimisation_outcomes(args.output_dir)


if __name__ == "__main__":
    main()
