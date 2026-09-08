#!/usr/bin/env python3
"""Generate SceneGuard web figures from the paper-reported data manifest."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


NAVY = "#234E5A"
TEAL = "#2F8F87"
SEA = "#70BDB4"
SKY = "#8EC8D3"
PALE_BLUE = "#EAF5F7"
PALE_MINT = "#E7F5F0"
PALEST = "#F7FBFB"
LINE = "#C8DFE1"
MUTED = "#667C83"
GREY = "#9AABAF"
WHITE = "#FFFFFF"

METHOD_ORDER = ["Clean", "Random noise", "Gaussian noise", "SceneGuard"]
SNR_ORDER = ["5–10 dB", "10–20 dB", "15–25 dB", "20–30 dB"]
ROBUSTNESS_ORDER = [
    "None",
    "MP3 128 kbps",
    "MP3 64 kbps",
    "Spectral subtraction",
    "Low-pass 3400 Hz",
    "Downsample 8 kHz",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=Path("assets/data/sceneguard/figure-data.csv"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("assets/images/projects/sceneguard"),
    )
    parser.add_argument(
        "--preview-dir",
        type=Path,
        help="Optional directory for PNG QA previews.",
    )
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
            "svg.hashsalt": "sceneguard-web-figures",
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


def save_figure(
    fig: plt.Figure,
    stem: str,
    output_dir: Path,
    preview_dir: Path | None,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg_path = output_dir / f"{stem}.svg"
    fig.savefig(
        svg_path,
        format="svg",
        bbox_inches="tight",
        facecolor=WHITE,
        metadata={"Date": None, "Creator": "SceneGuard figure generator"},
    )
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n",
        encoding="utf-8",
    )
    if preview_dir:
        preview_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(
            preview_dir / f"{stem}.png",
            dpi=180,
            bbox_inches="tight",
            facecolor=WHITE,
        )
    plt.close(fig)


def make_main_results(
    rows: list[dict[str, str | float]],
    output_dir: Path,
    preview_dir: Path | None,
) -> None:
    sim = values(rows, "main", "Speaker similarity", METHOD_ORDER)
    wer = values(rows, "main", "WER", METHOD_ORDER)
    colors = [GREY, SKY, SKY, TEAL]
    y = np.arange(len(METHOD_ORDER))

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    fig.set_facecolor(WHITE)

    ax = axes[0]
    ax.set_facecolor(PALEST)
    ax.scatter(sim, y, s=90, c=colors, zorder=3)
    for yi, value in zip(y, sim):
        ax.text(value - 0.002, yi - 0.22, f"{value:.3f}", ha="right", color=NAVY)
    ax.axvline(1.0, color=LINE, linestyle="--", linewidth=1)
    ax.set_xlim(0.9, 1.005)
    ax.set_yticks(y, METHOD_ORDER)
    ax.invert_yaxis()
    ax.grid(axis="x", color=LINE, linewidth=0.7, alpha=0.8)
    ax.set_title("Speaker similarity  ↓", loc="left", color=NAVY)
    ax.set_xlabel("Lower indicates stronger identity degradation")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)

    ax = axes[1]
    ax.set_facecolor(PALEST)
    bars = ax.barh(y, wer, color=colors, height=0.55)
    for bar, value in zip(bars, wer):
        ax.text(value + 0.12, bar.get_y() + bar.get_height() / 2, f"{value:.2f}%", va="center", color=NAVY)
    ax.set_xlim(0, 6.5)
    ax.set_yticks(y, METHOD_ORDER)
    ax.invert_yaxis()
    ax.grid(axis="x", color=LINE, linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    ax.set_title("Word error rate  ↓", loc="left", color=NAVY)
    ax.set_xlabel("Lower indicates better transcription")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)

    fig.suptitle(
        "SceneGuard improves protection while keeping WER below noise baselines",
        x=0.01,
        ha="left",
        color=NAVY,
        fontsize=13,
        weight="bold",
    )
    fig.text(0.99, 0.005, "Source: workshop paper, Table 1", ha="right", color=MUTED, fontsize=7)
    save_figure(fig, "main-results", output_dir, preview_dir)


def make_snr_tradeoff(
    rows: list[dict[str, str | float]],
    output_dir: Path,
    preview_dir: Path | None,
) -> None:
    protection = values(rows, "snr", "Protection", SNR_ORDER)
    stoi = values(rows, "snr", "STOI", SNR_ORDER)
    wer = values(rows, "snr", "WER", SNR_ORDER)
    x = np.arange(len(SNR_ORDER))
    metric_rows = [
        ("Protection  ↑", protection, (0, 9), "{:.1f}%", TEAL),
        ("STOI  ↑", stoi, (0.93, 1.005), "{:.3f}", SEA),
        ("WER  ↓", wer, (0, 9), "{:.1f}%", SKY),
    ]

    fig, axes = plt.subplots(3, 1, figsize=(10.5, 6.2), sharex=True, constrained_layout=True)
    for ax, (title, data, ylim, formatter, color) in zip(axes, metric_rows):
        ax.set_facecolor(PALEST)
        ax.axvspan(0.72, 1.28, color=PALE_MINT, zorder=0)
        ax.plot(x, data, color=color, linewidth=2.2, marker="o", markersize=6)
        for xi, value in zip(x, data):
            ax.text(xi, value + (ylim[1] - ylim[0]) * 0.07, formatter.format(value), ha="center", color=NAVY, fontsize=8)
        ax.set_ylim(*ylim)
        ax.set_ylabel(title, rotation=0, ha="right", va="center", labelpad=28, color=NAVY, weight="bold")
        ax.grid(axis="y", color=LINE, linewidth=0.7)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)

    axes[-1].set_xticks(x, SNR_ORDER)
    axes[-1].set_xlabel("Configured SNR range")
    axes[0].text(1, 8.55, "paper default", ha="center", color=TEAL, fontsize=8, weight="bold")
    fig.suptitle(
        "Lower SNR strengthens protection but reduces usability",
        x=0.01,
        ha="left",
        color=NAVY,
        fontsize=13,
        weight="bold",
    )
    fig.text(0.99, 0.005, "Source: workshop paper, Table 5", ha="right", color=MUTED, fontsize=7)
    save_figure(fig, "snr-tradeoff", output_dir, preview_dir)


def make_robustness(
    rows: list[dict[str, str | float]],
    output_dir: Path,
    preview_dir: Path | None,
) -> None:
    sim = values(rows, "robustness", "Speaker similarity", ROBUSTNESS_ORDER)
    y = np.arange(len(ROBUSTNESS_ORDER))
    colors = [GREY, SKY, SKY, SEA, TEAL, NAVY]

    fig, ax = plt.subplots(figsize=(10.5, 4.8), constrained_layout=True)
    ax.set_facecolor(PALEST)
    bars = ax.barh(y, sim, color=colors, height=0.58)
    ax.axvline(sim[0], color=MUTED, linestyle="--", linewidth=1, label="No preprocessing")
    for bar, value in zip(bars, sim):
        ax.text(
            value + 0.015,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.3f}",
            va="center",
            color=NAVY,
            fontsize=8,
        )
    ax.set_xlim(0, 1.02)
    ax.set_yticks(y, ROBUSTNESS_ORDER)
    ax.invert_yaxis()
    ax.grid(axis="x", color=LINE, linewidth=0.7)
    ax.set_axisbelow(True)
    ax.set_xlabel("Speaker similarity (lower indicates stronger protection)")
    ax.set_title(
        "Protection persists after common audio preprocessing",
        loc="left",
        color=NAVY,
        fontsize=13,
    )
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(loc="lower right", fontsize=8)
    fig.text(0.99, 0.005, "Source: workshop paper, Table 3", ha="right", color=MUTED, fontsize=7)
    save_figure(fig, "robustness-results", output_dir, preview_dir)


def main() -> None:
    args = parse_args()
    configure_style()
    rows = load_data(args.data)
    make_main_results(rows, args.output_dir, args.preview_dir)
    make_snr_tradeoff(rows, args.output_dir, args.preview_dir)
    make_robustness(rows, args.output_dir, args.preview_dir)
    print(f"Generated SceneGuard SVG figures in {args.output_dir}.")


if __name__ == "__main__":
    main()
