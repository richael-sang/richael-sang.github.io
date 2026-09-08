# SceneGuard Project Page Design Plan

## Design references

- [Clarity](https://shikun.io/projects/clarity): restrained technical panels, clear comparison displays, and readable mathematics.
- [Nerfies](https://nerfies.github.io/): compact academic hero, resource buttons, teaser-first hierarchy, and responsive diagrams.
- [Academic Project Page Template](https://eliahuhorwitz.github.io/Academic-project-page-template/): project SEO metadata, responsive media, and accessible action groups.
- [Academic Project Astro Template](https://research-template.roman.technology/): reusable figure, comparison, and mobile-stacking component patterns. The Astro stack itself will not be adopted.
- [De-AntiFake](https://de-antifake.github.io/samples): condition-oriented audio comparisons and demo-first organization.
- [VoiceBlock](https://interactiveaudiolab.github.io/project/voiceblock.html): concise research landing page with a separate path to deeper audio evidence.
- [Google SEANet](https://google-research.github.io/seanet/multimodal/speech/index.html): synchronized audio, waveform, spectrogram, and metric presentation.
- [AudioLDM](https://audioldm.github.io/) and [AudioLDM2](https://audioldm.github.io/audioldm2/): grouping many audio examples by task and progressively revealing secondary samples.
- [ClearMask](https://clear-mask.github.io/): direct clean/protected/synthesized comparison structure.

## Patterns to adopt

1. A concise academic hero with Paper, Code, and Audio Demo actions.
2. A four-card summary that explains input, output, goal, and core idea in under 30 seconds.
3. Neutral figure panels for the threat model, signal transformation, and system architecture.
4. Native, progressively loaded audio controls arranged as a responsive comparison matrix.
5. Offline-generated waveform and mel-spectrogram assets rather than browser-side signal processing.
6. Responsive result tables plus small native SVG/CSS visualizations.
7. Lightweight JavaScript for the precomputed SNR and robustness explorers.
8. A visible limitations section and explicit evidence labels.

## Patterns to avoid

- Framework migration, a separate visual theme, or large UI/chart dependencies.
- Autoplay, large public audio collections, or third-party dataset files without redistribution clearance.
- Decorative animation, oversized marketing claims, and cross-paper numerical comparisons.
- Treating SceneGuard as a newly trained neural architecture.
- Presenting repository README diagnostics as paper-verified results.
- Hiding the PESQ trade-off or implying full BERT-VITS2 fine-tuning or a human naturalness study.

## Adaptation to this site

- Extend the existing Jekyll `projects` collection and reusable `_layouts/project.html`.
- Add a reusable `project_advanced` flag, page-level CSS/JS hooks, and generic technical-page components.
- Keep Bootstrap 4, Lato/Raleway typography, the current navbar/footer, neutral cards, and existing breakpoints.
- Implement `/projects/sceneguard/` as `_projects/sceneguard.md`, then link it from Core Projects, Projects, and the SceneGuard publication entry.
- Use the existing KaTeX renderer for equations.
- Keep demo metadata in a small JSON manifest and provide an offline export helper; publish audio only after licensing and provenance review.

## Evidence policy

- **Paper-reported:** numerical claims transcribed from arXiv:2511.16114v1.
- **Repository implementation:** code paths and defaults visible in the public SceneGuard repository.
- **Not verified / future:** unavailable raw results, full TTS fine-tuning, human naturalness evidence, and adaptive-attack evaluation.

The page will label these categories instead of blending them.
