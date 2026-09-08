# SceneGuard web demo assets

This directory intentionally contains no audio samples yet.

Before publishing a sample, record:

- source dataset and utterance ID;
- speaker/sample attribution required by the source license;
- noise source, scene category, and redistribution terms;
- exact SceneGuard configuration;
- whether the baseline and protected variants are derived from the same clean sample;
- any displayed per-sample metrics and the script that computed them.

LibriTTS is distributed under CC BY 4.0 and requires attribution. TAU Urban
Acoustic Scenes 2022 Mobile has non-commercial restrictions; its audio must not
be copied into this MIT-licensed repository without an explicit, separately
documented redistribution review.

Use `scripts/export_sceneguard_web_assets.py` with a private input manifest to
generate web-sized PCM WAV files, waveform images, mel spectrograms, and a
public manifest.
