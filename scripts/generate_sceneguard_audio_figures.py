#!/usr/bin/env python3
"""Render waveform + mel-spectrogram panels for the SceneGuard SNR audio demo."""

from __future__ import annotations

import wave
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

SOURCE_DIR = Path("assets/images/projects/sceneguard")
OUTPUT_DIR = SOURCE_DIR / "audio"
CASES = [
    ("snr25", "机场背景混音_轻度_SNR25dB.wav"),
    ("snr20", "机场背景混音_中度_SNR20dB.wav"),
    ("snr15", "机场背景混音_较明显_SNR15dB.wav"),
]

INK = "#24343B"
TEAL = "#2A7F86"
LINE = "#DFE7EA"
MUTED = "#62747E"

N_FFT = 2048
HOP = 512
N_MELS = 96
F_MAX = 12000


def load(path: Path) -> tuple[np.ndarray, int]:
    with wave.open(str(path)) as handle:
        rate = handle.getframerate()
        frames = handle.readframes(handle.getnframes())
        channels = handle.getnchannels()
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    if channels > 1:
        audio = audio.reshape(-1, channels).mean(axis=1)
    return audio, rate


def hz_to_mel(hz: np.ndarray) -> np.ndarray:
    return 2595.0 * np.log10(1.0 + hz / 700.0)


def mel_to_hz(mel: np.ndarray) -> np.ndarray:
    return 700.0 * (10.0 ** (mel / 2595.0) - 1.0)


def mel_filterbank(rate: int) -> np.ndarray:
    bins = np.fft.rfftfreq(N_FFT, 1.0 / rate)
    points = mel_to_hz(np.linspace(hz_to_mel(np.array(0.0)), hz_to_mel(np.array(F_MAX)), N_MELS + 2))
    bank = np.zeros((N_MELS, bins.size), dtype=np.float32)
    for i in range(N_MELS):
        lo, mid, hi = points[i], points[i + 1], points[i + 2]
        rising = (bins - lo) / (mid - lo)
        falling = (hi - bins) / (hi - mid)
        bank[i] = np.clip(np.minimum(rising, falling), 0.0, None)
    return bank


def mel_db(audio: np.ndarray, rate: int) -> np.ndarray:
    window = np.hanning(N_FFT).astype(np.float32)
    count = 1 + (audio.size - N_FFT) // HOP
    frames = np.lib.stride_tricks.as_strided(
        audio, shape=(count, N_FFT), strides=(audio.strides[0] * HOP, audio.strides[0])
    )
    power = np.abs(np.fft.rfft(frames * window, axis=1)) ** 2
    mel = mel_filterbank(rate) @ power.T
    return 10.0 * np.log10(np.maximum(mel, 1e-10))


def render(stem: str, audio: np.ndarray, rate: int, vmax: float) -> None:
    fig, (wave_ax, mel_ax) = plt.subplots(
        2, 1, figsize=(4.4, 3.2), gridspec_kw={"height_ratios": [1, 2.2], "hspace": 0.12}
    )
    fig.set_facecolor("white")
    t = np.arange(audio.size) / rate
    step = max(1, audio.size // 6000)
    wave_ax.plot(t[::step], audio[::step], color=TEAL, linewidth=0.5)
    wave_ax.set_xlim(0, t[-1])
    wave_ax.set_ylim(-1, 1)
    wave_ax.axis("off")

    mel = mel_db(audio, rate)
    mel_ax.imshow(
        mel, origin="lower", aspect="auto", cmap="magma",
        vmin=vmax - 80, vmax=vmax, extent=[0, t[-1], 0, N_MELS],
    )
    mel_ax.set_yticks([])
    mel_ax.set_xlabel("Time (s)", color=MUTED, fontsize=7)
    mel_ax.tick_params(axis="x", colors=MUTED, labelsize=7, length=2)
    for spine in mel_ax.spines.values():
        spine.set_visible(False)
    fig.savefig(OUTPUT_DIR / f"airport-{stem}.png", dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    loaded = {stem: load(SOURCE_DIR / name) for stem, name in CASES}
    vmax = max(float(mel_db(a, r).max()) for a, r in loaded.values())
    for stem, (audio, rate) in loaded.items():
        render(stem, audio, rate, vmax)
        rms = float(np.sqrt(np.mean(audio**2)))
        print(f"{stem}: {audio.size / rate:.1f}s, RMS {20 * np.log10(rms):.1f} dBFS")


if __name__ == "__main__":
    main()
