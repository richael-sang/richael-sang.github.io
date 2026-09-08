---
layout: project
title: SceneGuard
subtitle: Training-Time Voice Protection with Scene-Consistent Audible Background Noise
date: 2026-01-26 00:01:00 +0800
category: research
selected: true
detail_page: true
permalink: /projects/sceneguard/
advanced_project: true
project_page_style: true
project_page_script: true
project_type: Voice Privacy · Audio ML
description: SceneGuard is a scene-conditioned audio protection pipeline that optimizes a temporal noise mask and gain to reduce speaker-identity similarity while preserving intelligibility.
citation_title: "SceneGuard: Training-Time Voice Protection with Scene-Consistent Audible Background Noise"
citation_publication_date: "2026-01-26"
paper_url: https://arxiv.org/pdf/2511.16114
og_type: article
og_image: /assets/images/projects/sceneguard/cover.svg
cover: /assets/images/projects/sceneguard/cover.svg
pub: "AAAI-26 Workshop on Artificial Intelligence for Cyber Security (AICS)"
pub_date: "Accepted"
pub_last: "· First author"
abstract: >-
  SceneGuard protects published speech by adding scene-matched audible noise whose timing and strength are optimized to reduce speaker-identity similarity while preserving intelligibility.
summary: >-
  Per-sample optimization of a temporal mask and noise gain for scene-conditioned, training-time voice protection.
authors:
- Rui Sang
- Yuxuan Liu
hero_links:
  Paper:
    url: https://arxiv.org/pdf/2511.16114
    target: _blank
    icon: fas fa-file-pdf
  Code:
    url: https://github.com/richael-sang/SceneGuard
    target: _blank
    icon: fab fa-github
  Audio Demo:
    url: "#audio-demo"
    target: _self
    icon: fas fa-headphones
links:
  Paper: https://arxiv.org/pdf/2511.16114
  Code: https://github.com/richael-sang/SceneGuard
section_nav:
- id: overview
  label: Overview
- id: audio-demo
  label: Audio
- id: system-architecture
  label: Method
- id: main-results
  label: Results
- id: implementation
  label: Implementation
- id: limitations
  label: Limitations
---

<section class="project-section" id="overview">
  <div class="section-kicker">30-second overview</div>
  <h2>What SceneGuard does</h2>
  <div class="overview-grid">
    <div class="overview-card">
      <div class="overview-label">Input</div>
      <h3>Speech + scene context</h3>
      <p>Speech \(x(t)\), an acoustic scene \(s\), and a scene-specific noise library \(\mathcal{N}_s\).</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Output</div>
      <h3>Protected speech</h3>
      <p>An audio signal \(x'(t)\) containing audible noise selected to match the recording context.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Goal</div>
      <h3>Reduce speaker identity</h3>
      <p>Lower ECAPA speaker similarity while retaining speech intelligibility and practical usability.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Core idea</div>
      <h3>Optimize placement + strength</h3>
      <p>Learn a temporal mask \(m(t)\) and global gain \(\gamma\) for a scene-matched noise sample.</p>
    </div>
  </div>
  <div class="evidence-note mt-3">
    <strong>Method in one line:</strong> SceneGuard is a scene-conditioned audio protection pipeline with per-sample gradient-based mask and gain optimization—not a newly trained neural-network architecture.
  </div>
</section>

<section class="project-section" id="audio-demo">
  <div class="section-kicker">Interactive evidence</div>
  <h2>Audio demo</h2>
  <p class="section-intro">The comparison interface is ready for curated Clean / Baseline / SceneGuard samples, with matching waveforms and mel spectrograms.</p>
  {% include widgets/project_audio_matrix.html demo=site.data.sceneguard_audio %}
  <div class="evidence-note mt-3">
    No audio is embedded yet. The public repository contains no WAV examples, and the TAU noise dataset has non-commercial redistribution restrictions. No synthetic or untraceable sample has been substituted.
  </div>
</section>

<section class="project-section" id="threat-model">
  <div class="section-kicker">Problem &amp; threat model</div>
  <h2>Protecting speech before an attacker collects it</h2>
  <div class="threat-flow" role="img" aria-label="A user publishes protected speech, an attacker collects it, and attempts voice cloning">
    <div class="flow-node"><i class="fas fa-microphone" aria-hidden="true"></i><strong>User publishes speech</strong><span>Protection is applied before release</span></div>
    <div class="flow-arrow" aria-hidden="true">→</div>
    <div class="flow-node"><i class="fas fa-download" aria-hidden="true"></i><strong>Attacker collects audio</strong><span>Black-box attacker does not know the defense</span></div>
    <div class="flow-arrow" aria-hidden="true">→</div>
    <div class="flow-node"><i class="fas fa-user-secret" aria-hidden="true"></i><strong>Voice-cloning attempt</strong><span>Training-time or zero-shot use</span></div>
  </div>
  <div class="comparison-grid mt-4">
    <div class="comparison-card">
      <div class="comparison-label">Conventional paradigm</div>
      <h3>Imperceptible perturbation</h3>
      <p>Prior proactive defenses often constrain perturbations to be difficult to hear, but such low-energy signals may be vulnerable to compression, filtering, or purification.</p>
    </div>
    <div class="comparison-card comparison-card-accent">
      <div class="comparison-label">SceneGuard design choice</div>
      <h3>Scene-matched audible protection</h3>
      <p>SceneGuard trades strict imperceptibility for context-aware noise selection and tests whether protection persists under common preprocessing operations.</p>
    </div>
  </div>
  <p class="source-line"><span class="evidence-chip">Paper-described threat model</span> Full end-to-end BERT-VITS2 fine-tuning was not performed because of computational constraints; speaker-embedding degradation is used as a proxy, complemented by a zero-shot evaluation.</p>
</section>

<section class="project-section" id="input-output">
  <div class="section-kicker">Signal transformation</div>
  <h2>Input → output</h2>
  <div class="equation-panel">
    $$x'(t) = x(t) + \gamma\,m(t)\odot n_k(t), \qquad n_k(t)\sim\mathcal{N}_s$$
  </div>
  <div class="symbol-grid">
    <div><code>x(t)</code><span>clean input speech</span></div>
    <div><code>s</code><span>predicted or user-provided scene</span></div>
    <div><code>n_k(t)</code><span>noise sampled from the scene library</span></div>
    <div><code>m(t)</code><span>temporal mask in \([0,1]^T\)</span></div>
    <div><code>γ</code><span>global noise strength</span></div>
    <div><code>x'(t)</code><span>protected speech output</span></div>
  </div>
</section>

<section class="project-section" id="system-architecture">
  <div class="section-kicker">System architecture</div>
  <h2>Pretrained perception, per-sample optimization</h2>
  <p class="section-intro">PANNs, ECAPA-TDNN, and Whisper are pretrained components. SceneGuard does not train them; gradients update only the temporal mask and global gain for each sample.</p>
  <figure class="technical-figure technical-figure-borderless">
    <img src="{{ '/assets/images/projects/sceneguard/system-architecture.png' | relative_url }}" alt="SceneGuard architecture showing scene and noise selection, mask and gain optimization, protected speech generation, usability and robustness evaluation, and training-time and zero-shot attacks" loading="lazy">
  </figure>
</section>

<section class="project-section" id="why-optimization">
  <div class="section-kicker">Ablation</div>
  <h2>Why optimize the mixture?</h2>
  <div class="comparison-grid">
    <div class="comparison-card">
      <div class="comparison-label">Direct mixing</div>
      <h3>Fixed / unoptimized placement</h3>
      <div class="metric-large">2.8%</div>
      <div class="metric-caption">paper-reported protection</div>
      <div class="mini-bar"><span style="width: 35%"></span></div>
      <p>SIM 0.972 · STOI 0.989 · WER 3.2%</p>
    </div>
    <div class="comparison-card comparison-card-accent">
      <div class="comparison-label">SceneGuard</div>
      <h3>Learned mask + constrained gain</h3>
      <div class="metric-large">5.5%</div>
      <div class="metric-caption">paper-reported protection</div>
      <div class="mini-bar"><span style="width: 69%"></span></div>
      <p>SIM 0.945 · STOI 0.986 · WER 3.6%</p>
    </div>
  </div>
  <p class="source-line"><span class="evidence-chip">Paper Table 6</span> Optimization improves reported similarity degradation by 2.7 percentage points under the same SNR constraint, with a 0.003 STOI decrease and 0.4-point WER increase.</p>
</section>

<section class="project-section" id="objective">
  <div class="section-kicker">Optimization objective</div>
  <h2>What is actually optimized?</h2>
  <div class="equation-panel">
    $$\mathcal{L}_{\mathrm{default}} =
    \lambda_{\mathrm{SIM}}\,\mathrm{cos}\!\left(e(x'),e(x)\right)
    + \lambda_{\mathrm{REG}}\left(\|\nabla m\|_2^2+\gamma^2\right)$$
    $$\text{subject to}\quad \mathrm{SNR}\!\left(x,\gamma m\odot n_k\right)\in[10,20]\ \mathrm{dB}$$
  </div>
  <div class="objective-list">
    <div><strong>Speaker similarity</strong><span>Minimize cosine similarity between clean and protected ECAPA embeddings.</span></div>
    <div><strong>Mask smoothness</strong><span>Penalize abrupt temporal changes that may create unstable or spiky masks.</span></div>
    <div><strong>Energy penalty</strong><span>Regularize the global noise strength \(\gamma\).</span></div>
    <div><strong>SNR constraint</strong><span>Bound the paper’s default operating range to 10–20 dB.</span></div>
  </div>
  <details class="technical-details mt-3">
    <summary>General paper formulation and disabled terms</summary>
    <div class="equation-panel equation-panel-secondary">
      $$\mathcal{L}=\lambda_{\mathrm{SIM}}\mathcal{L}_{\mathrm{SIM}}
      +\lambda_{\mathrm{REG}}\mathcal{L}_{\mathrm{REG}}
      +\lambda_{\mathrm{ASR}}\mathcal{L}_{\mathrm{ASR}}
      +\lambda_{\mathrm{SCN}}\mathcal{L}_{\mathrm{SCN}}$$
    </div>
    <p>In the default experiments, \(\lambda_{\mathrm{ASR}}=0\) and \(\lambda_{\mathrm{SCN}}=0\). Scene consistency is introduced mainly by selecting noise from the scene-specific library; usability is enforced primarily through SNR and evaluated after optimization.</p>
  </details>
</section>

<section class="project-section" id="evaluation">
  <div class="section-kicker">Evaluation framework</div>
  <h2>Four views of the protection–quality trade-off</h2>
  <div class="evaluation-grid">
    <div class="evaluation-card"><i class="fas fa-user-shield" aria-hidden="true"></i><h3>Protection</h3><p><strong>Speaker Similarity (SIM) ↓</strong><br>Cosine similarity between speaker embeddings.</p></div>
    <div class="evaluation-card"><i class="fas fa-comment-dots" aria-hidden="true"></i><h3>Usability</h3><p><strong>WER ↓ · STOI ↑ · PESQ ↑</strong><br>Transcription, intelligibility, and objective quality.</p></div>
    <div class="evaluation-card"><i class="fas fa-filter" aria-hidden="true"></i><h3>Robustness</h3><p><strong>SIM after preprocessing</strong><br>MP3, spectral subtraction, low-pass, and downsampling.</p></div>
    <div class="evaluation-card"><i class="fas fa-bolt" aria-hidden="true"></i><h3>Zero-shot</h3><p><strong>SIM + success rate ↓</strong><br>Cloning with clean versus protected reference audio.</p></div>
  </div>
</section>

<section class="project-section" id="main-results">
  <div class="section-kicker">Paper-reported results</div>
  <h2>Main comparison</h2>
  <div class="result-highlight-grid">
    <div><span>SIM</span><strong>1.000 → 0.945</strong><small>training-attack proxy comparison</small></div>
    <div><span>STOI</span><strong>0.986</strong><small>95% CI [0.980, 0.992]</small></div>
    <div><span>WER</span><strong>3.60%</strong><small>usability evaluation</small></div>
    <div><span>Effect size</span><strong>2.18</strong><small>Cohen’s d; paper reports p &lt; 10<sup>−15</sup></small></div>
  </div>
  <div class="table-responsive mt-4">
    <table class="table technical-table">
      <caption>Training-attack proxy comparison reported in Table 1 of the workshop paper.</caption>
      <thead><tr><th>Training data</th><th>SIM ↓</th><th>WER (%) ↓</th><th>PESQ ↑</th><th>STOI ↑</th></tr></thead>
      <tbody>
        <tr><td>Clean</td><td>1.000</td><td>0.00</td><td>4.64</td><td>1.00</td></tr>
        <tr><td>Random noise</td><td>0.965</td><td>5.82</td><td>1.85</td><td>0.97</td></tr>
        <tr><td>Gaussian noise</td><td>0.968</td><td>5.28</td><td>1.92</td><td>0.98</td></tr>
        <tr class="table-emphasis"><td>SceneGuard</td><td>0.945</td><td>2.77</td><td>2.22</td><td>0.99</td></tr>
      </tbody>
    </table>
  </div>
  <div class="tradeoff-callout">
    <strong>Visible trade-off:</strong> the separate usability evaluation reports PESQ 2.034 (95% CI [1.840, 2.233]), below the paper’s stated ideal threshold of 3.0. SceneGuard preserves high measured intelligibility, but not pristine perceptual quality.
  </div>
  <p class="source-line"><span class="evidence-chip">Paper Tables 1–2</span> Table 1 reports WER 2.77% and PESQ 2.22; the separate usability summary reports WER 3.60% and PESQ 2.034. The paper does not document why the summaries differ, so they are shown separately.</p>
</section>

<section class="project-section" id="snr-explorer">
  <div class="section-kicker">Interactive ablation</div>
  <h2>SNR trade-off explorer</h2>
  <p class="section-intro">Move across the four precomputed settings to inspect the reported protection–usability balance.</p>
  <div class="explorer" data-snr-explorer>
    <label for="snr-range"><strong>SNR range:</strong> <span data-snr-label>10–20 dB</span></label>
    <input id="snr-range" type="range" min="0" max="3" step="1" value="1"
      data-labels="5–10 dB|10–20 dB|15–25 dB|20–30 dB"
      data-sim="0.921|0.945|0.968|0.982"
      data-protection="7.9|5.5|3.2|1.8"
      data-stoi="0.942|0.986|0.993|0.997"
      data-wer="8.2|3.6|1.8|0.9"
      aria-describedby="snr-explorer-note">
    <div class="range-labels" aria-hidden="true"><span>5–10</span><span>10–20</span><span>15–25</span><span>20–30 dB</span></div>
    <div class="explorer-metrics" aria-live="polite">
      <div><span>Protection</span><strong data-snr-protection>5.5%</strong></div>
      <div><span>SIM ↓</span><strong data-snr-sim>0.945</strong></div>
      <div><span>STOI ↑</span><strong data-snr-stoi>0.986</strong></div>
      <div><span>WER ↓</span><strong data-snr-wer>3.6%</strong></div>
    </div>
    <p class="small text-muted mb-0" id="snr-explorer-note">Visualization of paper-reported, precomputed ablation results—no model inference runs in the browser.</p>
  </div>
</section>

<section class="project-section" id="robustness-explorer">
  <div class="section-kicker">Preprocessing robustness</div>
  <h2>Robustness explorer</h2>
  <div class="explorer" data-robustness-explorer>
    <div class="robustness-controls" role="group" aria-label="Select an audio preprocessing condition">
      <button type="button" class="active" data-label="No countermeasure" data-sim="0.937">None</button>
      <button type="button" data-label="MP3 at 128 kbps" data-sim="0.901">MP3 128</button>
      <button type="button" data-label="MP3 at 64 kbps" data-sim="0.899">MP3 64</button>
      <button type="button" data-label="Spectral subtraction" data-sim="0.745">Spectral subtraction</button>
      <button type="button" data-label="Low-pass at 3400 Hz" data-sim="0.704">Low-pass</button>
      <button type="button" data-label="Downsampled to 8 kHz" data-sim="0.688">Downsample</button>
    </div>
    <div class="robustness-display" aria-live="polite">
      <div><span data-robustness-label>No countermeasure</span><strong>SIM <span data-robustness-sim>0.937</span></strong></div>
      <div class="robustness-track"><span data-robustness-bar style="width: 93.7%"></span></div>
      <small>Lower SIM indicates greater speaker-identity degradation in the paper’s evaluation.</small>
    </div>
    <p class="small text-muted mb-0 mt-3"><span class="evidence-chip">Paper Table 3</span> The public repository does not contain the underlying per-sample robustness CSVs or audio needed for independent recomputation.</p>
  </div>
</section>

<section class="project-section" id="zero-shot">
  <div class="section-kicker">Zero-shot evaluation</div>
  <h2>Protected reference audio lowers reported cloning similarity</h2>
  <div class="zero-shot-grid">
    <div class="zero-shot-card"><span>Clean reference</span><strong>SIM 0.618</strong><small>Attack success rate 20.0%</small></div>
    <div class="zero-shot-arrow" aria-hidden="true">→</div>
    <div class="zero-shot-card zero-shot-card-accent"><span>SceneGuard reference</span><strong>SIM 0.588</strong><small>Attack success rate 13.3%</small></div>
  </div>
  <p class="source-line"><span class="evidence-chip">Paper Table 4</span> No publishable zero-shot synthesized audio or raw result file is present in the public repository, so this section reports metrics only.</p>
</section>

<section class="project-section" id="implementation">
  <div class="section-kicker">Engineering view</div>
  <h2>Implementation details</h2>
  <div class="table-responsive">
    <table class="table technical-table implementation-table">
      <tbody>
        <tr><th>Scene classifier</th><td>PANNs CNN14, pretrained on AudioSet</td></tr>
        <tr><th>Speaker encoder</th><td>ECAPA-TDNN, 192-dimensional embeddings</td></tr>
        <tr><th>ASR evaluator</th><td>Whisper Base</td></tr>
        <tr><th>Referenced TTS architecture</th><td>BERT-VITS2; no full fine-tuning in the workshop experiment</td></tr>
        <tr><th>Optimizer</th><td>Adam, learning rate 0.01</td></tr>
        <tr><th>Default optimization</th><td>50 epochs, gradient clipping max norm 1.0</td></tr>
        <tr><th>Default SNR</th><td>10–20 dB</td></tr>
        <tr><th>Reported runtime</th><td>Approximately 10–15 s/sample on one RTX A6000</td></tr>
        <tr><th>Speech / noise data</th><td>LibriTTS; TAU Urban Acoustic Scenes 2022</td></tr>
        <tr><th>Noise library</th><td>Approximately 50,000 three-second clips across 10 scene categories</td></tr>
        <tr><th>Training-attack split</th><td>100 training samples and 40 test samples</td></tr>
      </tbody>
    </table>
  </div>
  <div class="evidence-note">
    <strong>Repository status:</strong> the public code contains the mixer, optimizer, metrics, and helper scripts, but does not currently include result CSVs, audio samples, checkpoints, or a complete PANNs / robustness / zero-shot reproduction pipeline.
  </div>
</section>

<section class="project-section" id="limitations">
  <div class="section-kicker">Limitations</div>
  <h2>What the current evidence does not establish</h2>
  <div class="limitations-list">
    <div><span>01</span><div><h3>Audible protection</h3><p>The method is not suitable when pristine audio is required, such as studio recording or professional voice production.</p></div></div>
    <div><span>02</span><div><h3>Perceptual quality</h3><p>PESQ is approximately 2.03 in the usability evaluation, below the paper’s stated ideal target of 3.0.</p></div></div>
    <div><span>03</span><div><h3>Adaptive attacks</h3><p>Scene-aware source separation and attackers explicitly adapted to SceneGuard have not been comprehensively evaluated.</p></div></div>
    <div><span>04</span><div><h3>Training-time evidence</h3><p>Full end-to-end TTS fine-tuning was not performed in the workshop experiment because of computational constraints; embedding degradation is used as a proxy.</p></div></div>
    <div><span>05</span><div><h3>Scene consistency</h3><p>No dedicated human naturalness or scene-matching listening study is reported. The noise is scene-matched by construction, not perceptually validated by listeners.</p></div></div>
  </div>
</section>

<section class="project-section" id="reproducibility">
  <div class="section-kicker">Reproducibility</div>
  <h2>Public pipeline</h2>
  <div class="pipeline" aria-label="SceneGuard reproduction pipeline">
    <span>Build noise library</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Assign scene labels</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Generate protection</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Evaluate</span>
  </div>
  <div class="resource-list mt-4">
    <a href="https://github.com/richael-sang/SceneGuard" target="_blank" rel="noopener"><i class="fab fa-github" aria-hidden="true"></i><span><strong>Source code</strong><small>Public implementation and scripts</small></span></a>
    <a href="https://github.com/richael-sang/SceneGuard/blob/main/ENVIRONMENT.yml" target="_blank" rel="noopener"><i class="fas fa-cube" aria-hidden="true"></i><span><strong>Environment</strong><small>Conda dependency specification</small></span></a>
    <a href="https://github.com/richael-sang/SceneGuard/tree/main/scripts" target="_blank" rel="noopener"><i class="fas fa-terminal" aria-hidden="true"></i><span><strong>Experiment scripts</strong><small>Preparation, defense, evaluation, and figures</small></span></a>
  </div>
  <p class="source-line"><span class="evidence-chip">Evidence boundary</span> Paper tables are the source for the numerical results on this page. Values such as negative final speaker similarity and very low SNR variance from the README are excluded because their dataset/configuration cannot be traced to public artifacts.</p>
</section>

<section class="project-section" id="related-work">
  <div class="section-kicker">Related work</div>
  <h2>Positioning</h2>
  <p>SceneGuard sits alongside real-time speaker de-identification (VoiceBlock), imperceptible proactive protection (SafeSpeech), purification-aware protection research (De-AntiFake), and diffusion-based voice-cloning protection (VoiceCloak). Numerical cross-paper comparisons are intentionally omitted because threat models, datasets, cloning systems, and metrics differ.</p>
</section>
