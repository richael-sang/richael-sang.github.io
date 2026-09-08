#!/usr/bin/env python3
"""Export curated SceneGuard audio comparisons for the Jekyll project page.

The private input manifest must contain explicitly selected, publishable files:

{
  "samples": [{
    "id": "sample-01",
    "label": "Sample 01",
    "scene": "airport",
    "source": "LibriTTS utterance ...",
    "license": "CC BY 4.0",
    "attribution": "...",
    "variants": {
      "clean": "/private/path/clean.wav",
      "baseline": "/private/path/baseline.wav",
      "sceneguard": "/private/path/sceneguard.wav"
    }
  }]
}

The script does not download datasets, create synthetic examples, or infer
missing variants. It writes web-sized PCM WAV files, waveform PNGs, mel
spectrogram PNGs, and a JSON asset manifest.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

CONDITIONS = ("clean", "baseline", "sceneguard")


def load_audio_dependencies() -> None:
    global librosa, plt, np, sf
    try:
        import librosa
        import librosa.display
        import matplotlib.pyplot as plt
        import numpy as np
        import soundfile as sf
    except ImportError as error:
        raise SystemExit(
            "Missing audio dependencies. Activate the SceneGuard environment "
            "or install librosa, matplotlib, numpy, and soundfile."
        ) from error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export licensed SceneGuard demo audio and visual assets."
    )
    parser.add_argument("--input-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--public-base",
        default="/assets/audio/projects/sceneguard",
        help="URL prefix written to the generated manifest.",
    )
    parser.add_argument("--sample-rate", type=int, default=16000)
    parser.add_argument("--peak-limit", type=float, default=0.98)
    parser.add_argument(
        "--allow-noncommercial",
        action="store_true",
        help="Required when a sample manifest declares a non-commercial license.",
    )
    return parser.parse_args()


def safe_id(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "-", value.strip()).strip("-").lower()
    if not cleaned:
        raise ValueError("Every sample requires a non-empty, filename-safe id.")
    return cleaned


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("samples"), list):
        raise ValueError("Input manifest must contain a 'samples' array.")
    return data


def validate_sample(sample: dict[str, Any], allow_noncommercial: bool) -> None:
    required = ("id", "label", "scene", "source", "license", "attribution", "variants")
    missing = [key for key in required if not sample.get(key)]
    if missing:
        raise ValueError(f"Sample {sample.get('id', '<unknown>')} missing: {missing}")

    license_name = str(sample["license"]).lower()
    if "non-commercial" in license_name or "noncommercial" in license_name:
        if not allow_noncommercial:
            raise ValueError(
                f"Sample {sample['id']} is marked non-commercial. "
                "Review redistribution terms, then pass --allow-noncommercial."
            )

    variants = sample["variants"]
    for condition in CONDITIONS:
        source = Path(variants.get(condition, ""))
        if not source.is_file():
            raise FileNotFoundError(
                f"Sample {sample['id']} has no readable {condition} file: {source}"
            )


def prepare_audio(path: Path, sample_rate: int, peak_limit: float) -> np.ndarray:
    audio, source_rate = sf.read(path, always_2d=True, dtype="float32")
    mono = np.mean(audio, axis=1)
    if source_rate != sample_rate:
        mono = librosa.resample(
            mono, orig_sr=source_rate, target_sr=sample_rate, res_type="kaiser_best"
        )

    peak = float(np.max(np.abs(mono))) if mono.size else 0.0
    if peak > peak_limit:
        mono = mono * (peak_limit / peak)
    return mono.astype(np.float32)


def save_waveform(audio: np.ndarray, sample_rate: int, path: Path) -> None:
    times = np.arange(audio.size) / sample_rate
    fig, axis = plt.subplots(figsize=(8, 1.8), dpi=160)
    axis.plot(times, audio, color="#315a75", linewidth=0.65)
    axis.set_xlim(0, times[-1] if times.size else 1)
    axis.set_ylim(-1, 1)
    axis.set_xlabel("Time (s)")
    axis.set_ylabel("Amplitude")
    axis.grid(alpha=0.18, linewidth=0.5)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def save_mel(audio: np.ndarray, sample_rate: int, path: Path) -> None:
    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate,
        n_fft=1024,
        hop_length=256,
        n_mels=80,
        fmin=40,
        fmax=sample_rate // 2,
        power=2.0,
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)
    fig, axis = plt.subplots(figsize=(8, 2.2), dpi=160)
    image = librosa.display.specshow(
        mel_db,
        sr=sample_rate,
        hop_length=256,
        x_axis="time",
        y_axis="mel",
        cmap="magma",
        ax=axis,
    )
    axis.set_xlabel("Time (s)")
    axis.set_ylabel("Mel frequency")
    fig.colorbar(image, ax=axis, format="%+2.0f dB", pad=0.01)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def export_sample(
    sample: dict[str, Any],
    output_dir: Path,
    public_base: str,
    sample_rate: int,
    peak_limit: float,
) -> dict[str, Any]:
    sample_id = safe_id(str(sample["id"]))
    sample_dir = output_dir / sample_id
    sample_dir.mkdir(parents=True, exist_ok=True)

    public_variants: dict[str, dict[str, str]] = {}
    for condition in CONDITIONS:
        audio = prepare_audio(
            Path(sample["variants"][condition]), sample_rate, peak_limit
        )
        audio_path = sample_dir / f"{condition}.wav"
        waveform_path = sample_dir / f"{condition}-waveform.png"
        mel_path = sample_dir / f"{condition}-mel.png"

        sf.write(audio_path, audio, sample_rate, subtype="PCM_16")
        save_waveform(audio, sample_rate, waveform_path)
        save_mel(audio, sample_rate, mel_path)

        prefix = f"{public_base.rstrip('/')}/{sample_id}"
        public_variants[condition] = {
            "audio": f"{prefix}/{audio_path.name}",
            "waveform": f"{prefix}/{waveform_path.name}",
            "mel": f"{prefix}/{mel_path.name}",
        }

    return {
        "id": sample_id,
        "label": sample["label"],
        "scene": sample["scene"],
        "source": sample["source"],
        "license": sample["license"],
        "attribution": sample["attribution"],
        "variants": public_variants,
    }


def main() -> None:
    args = parse_args()
    load_audio_dependencies()
    if not 0 < args.peak_limit <= 1:
        raise ValueError("--peak-limit must be in (0, 1].")

    manifest = load_manifest(args.input_manifest)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    exported = []
    for sample in manifest["samples"]:
        validate_sample(sample, args.allow_noncommercial)
        exported.append(
            export_sample(
                sample,
                args.output_dir,
                args.public_base,
                args.sample_rate,
                args.peak_limit,
            )
        )

    public_manifest = {
        "status": "ready" if exported else "pending",
        "sample_rate": args.sample_rate,
        "conditions": list(CONDITIONS),
        "samples": exported,
    }
    output_manifest = args.output_dir / "manifest.json"
    output_manifest.write_text(
        json.dumps(public_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Exported {len(exported)} sample(s) to {args.output_dir}")
    print(f"Manifest: {output_manifest}")


if __name__ == "__main__":
    main()
