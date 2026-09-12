---
layout: project
title: Infrared–Visible Multimodal Object Detection
subtitle: Adaptive RGB–IR Fusion under Changing Visual Conditions
date: 2026-05-01 00:00:00 +0800
category: research
selected: true
detail_page: true
permalink: /projects/infrared-visible/
advanced_project: true
project_page_style: true
project_page_script: true
project_theme: rgbir
project_type: Multimodal Perception · Object Detection
description: An RGB–infrared object detection project investigating whether lightweight adaptive modality weighting can dynamically balance visual and thermal information under changing scene conditions.
og_type: article
og_image: /assets/images/projects/infrared-visible/concept-overview.png
cover: /assets/images/projects/infrared-visible/concept-overview.png
cover_fit: contain
hero_figure: /assets/images/projects/infrared-visible/concept-overview.svg
hero_figure_alt: Visible and infrared images enter adaptive fusion, then a detector outputs boxes, classes, and scores
abstract: >-
  An RGB–infrared object detection project investigating whether lightweight adaptive modality weighting can dynamically balance visual and thermal information under changing scene conditions.
summary: >-
  Adaptive RGB–IR fusion for object detection: multimodal beats unimodal, but learned weighting is not universally better.
authors:
- Rui Sang
pub: "SAT301 Final Year Project, Xi’an Jiaotong-Liverpool University"
pub_date: "May 2026"
pub_last: "· Supervised by Dr. Xiaohui Zhu"
hero_links:
  Qualitative Demo:
    url: "#qualitative-demo"
    target: _self
    icon: fas fa-images
section_nav:
- id: problem
  label: Problem
- id: motivation
  label: Motivation
- id: input
  label: Input
- id: architecture
  label: Model
- id: innovation
  label: Innovation
- id: output
  label: Output
- id: metrics
  label: Metrics
- id: results
  label: Results
- id: qualitative-demo
  label: Demo
- id: limitations
  label: Limits
---

<section class="project-section" id="problem">
  <div class="section-kicker">1 · Problem</div>
  <h2>Should RGB and infrared always contribute equally?</h2>
  <p class="section-intro">The technical question on this page is narrower than “does fusion help?”. It asks whether a multimodal detector can learn <em>when</em> to trust visible or infrared information.</p>
  <div class="modality-grid">
    <div class="modality-card modality-card-visible">
      <div class="overview-label">Visible</div>
      <h3>Texture, colour, boundaries</h3>
      <p>Useful in well-lit scenes, but the signal can degrade under low light, glare, rain, or haze.</p>
    </div>
    <div class="modality-card modality-card-infrared">
      <div class="overview-label">Infrared</div>
      <h3>Thermal contrast</h3>
      <p>Often stronger in low light, but it carries less texture, less colour, and weaker fine detail.</p>
    </div>
  </div>
  <div class="question-banner">Visible and infrared are complementary. Equal contribution is a convenient assumption, not a law.</div>
</section>

<section class="project-section" id="motivation">
  <div class="section-kicker">2 · Motivation</div>
  <h2>Learn a modality preference instead of fixing one</h2>
  <p class="section-intro">If the two sensors are not equally reliable in every scene, a detector that always mixes them 1:1 may waste a trustworthy channel or over-trust a degraded one. The project therefore tests whether a lightweight weighting rule can move with the input.</p>
  <div class="overview-grid">
    <div class="overview-card">
      <div class="overview-label">Question</div>
      <h3>Can the model learn when to trust RGB or IR?</h3>
      <p>The page is organised around this one question, not around platform reproduction or dataset migration.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Hypothesis</div>
      <h3>Reliability is scene-dependent</h3>
      <p>Visible cues should matter more when texture is intact; thermal cues should matter more when visible contrast collapses.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Test</div>
      <h3>Fix the detector, change the mix</h3>
      <p>Static weights, a dynamic gate, and a conservative residual gate are compared against default multimodal fusion.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Expectation</div>
      <h3>Not a guaranteed win</h3>
      <p>If default fusion is already strong, adaptive weighting may only appear when modality quality becomes uneven.</p>
    </div>
  </div>
</section>

<section class="project-section" id="input">
  <div class="section-kicker">3 · Input</div>
  <h2>A registered RGB–infrared pair</h2>
  <p class="section-intro">Each sample is a spatially aligned visible image and infrared image. The pair below is a night scene from the project materials: pedestrians that fade in RGB remain clear in IR.</p>
  <div class="paired-input-grid">
    <figure>
      <span class="plate-label plate-visible">Visible</span>
      <img src="{{ '/assets/images/projects/infrared-visible/demo/pair-visible.jpg' | relative_url }}" alt="Registered night-time visible image of a road scene" loading="lazy">
    </figure>
    <figure>
      <span class="plate-label plate-infrared">Infrared</span>
      <img src="{{ '/assets/images/projects/infrared-visible/demo/pair-infrared.jpg' | relative_url }}" alt="Registered night-time infrared image of the same road scene" loading="lazy">
    </figure>
  </div>
  <p class="source-line"><span class="evidence-chip">Paired input</span> Same camera geometry, two physical measurements. No extra metadata is required at inference beyond the image pair.</p>
</section>

<section class="project-section" id="architecture">
  <div class="section-kicker">4 · Model architecture</div>
  <h2>Two streams, one DiffusionDet head</h2>
  <p class="section-intro">The experimental framework is E2E-MFD-HOD on Detectron2 with a DiffusionDet detection head. The diagram stays conceptual: only the verified pipeline is shown.</p>
  <figure class="technical-figure technical-figure-borderless">
    <img src="{{ '/assets/images/projects/infrared-visible/architecture.svg' | relative_url }}" alt="Conceptual architecture from visible and infrared images through fusion, multi-scale features, and a DiffusionDet head" loading="lazy">
  </figure>
  <div class="pipeline" aria-label="Conceptual detection pipeline">
    <span>Visible features</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Infrared features</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Multimodal fusion</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Multi-scale features</span><i class="fas fa-angle-right" aria-hidden="true"></i>
    <span>Boxes + classes + scores</span>
  </div>
</section>

<section class="project-section" id="innovation">
  <div class="section-kicker">5 · Core innovation</div>
  <h2>Adaptive modality weighting</h2>
  <p class="section-intro">Instead of assuming equal RGB / IR importance, the fusion step learns a visible weight \(\alpha\) from features. \(\alpha\) may vary by feature level and by input.</p>
  <div class="fusion-formula">
    Fused feature \(= \alpha \times\) visible feature \(+ (1-\alpha) \times\) infrared feature
  </div>
  <div class="overview-grid">
    <div class="overview-card">
      <div class="overview-label">Experiment 1</div>
      <h3>Fixed static weighting</h3>
      <p>Manually set visible ratios to 0.25, 0.50, and 0.75.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Experiment 2</div>
      <h3>Lightweight dynamic gating</h3>
      <p>Predict \(\alpha\) from the two feature streams.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Experiment 3</div>
      <h3>Conservative residual gating</h3>
      <p>Keep the default fusion path and learn only a small correction.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Goal</div>
      <h3>Preference, not a hand-set mix</h3>
      <p>Ask the model to allocate trust instead of freezing it.</p>
    </div>
  </div>
  <div class="evidence-note mt-3">
    <strong>Secondary idea — modality-robust training.</strong>
    During training, one modality is mildly attenuated to simulate a degraded sensor. The aim is to reduce over-reliance on a single stream. This remains a supporting probe, not the main claim.
  </div>
</section>

<section class="project-section" id="output">
  <div class="section-kicker">6 · Output</div>
  <h2>Multiclass boxes, labels, and scores</h2>
  <div class="overview-grid">
    <div class="overview-card">
      <div class="overview-label">Boxes</div>
      <h3>Object bounding boxes</h3>
      <p>Horizontal detections on the aligned scene.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Labels</div>
      <h3>Category names</h3>
      <p>A multiclass vocabulary, including people and common vehicles.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Scores</div>
      <h3>Confidence</h3>
      <p>Each box carries a detector confidence used by AP.</p>
    </div>
    <div class="overview-card">
      <div class="overview-label">Task</div>
      <h3>Multiclass object detection</h3>
      <p>No extra heads beyond detection are claimed here.</p>
    </div>
  </div>
</section>

<section class="project-section" id="metrics">
  <div class="section-kicker">7 · Metrics</div>
  <h2>AP, and only AP</h2>
  <p class="section-intro">The report uses standard COCO-style detection metrics. Hover or focus a card for the short definition used on this page.</p>
  <div class="metric-tooltip-grid">
    <div class="metric-tip" tabindex="0" title="Mean Average Precision averaged over IoU thresholds from 0.50 to 0.95.">
      <strong>AP</strong>
      <span>Primary score. Average precision across IoU thresholds 0.50–0.95.</span>
    </div>
    <div class="metric-tip" tabindex="0" title="Average Precision at a single IoU threshold of 0.50.">
      <strong>AP50</strong>
      <span>Loose localisation. A prediction counts if IoU is at least 0.50.</span>
    </div>
    <div class="metric-tip" tabindex="0" title="Average Precision at a single IoU threshold of 0.75.">
      <strong>AP75</strong>
      <span>Stricter boxes. A prediction counts if IoU is at least 0.75.</span>
    </div>
    <div class="metric-tip" tabindex="0" title="Average Precision computed independently for each object category.">
      <strong>Per-class AP</strong>
      <span>Same AP, one value per category. Used to see which classes move.</span>
    </div>
  </div>
</section>

<section class="project-section" id="results">
  <div class="section-kicker">8 · Results</div>
  <h2>Four readings of the same question</h2>

  <h3 class="mt-4">Result 1 — Multimodal advantage</h3>
  <p class="section-intro">On the candidate-init official route, combining RGB and infrared produces the strongest overall detector. Two multimodal seeds stay within 0.33 AP of each other.</p>
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/multimodal-advantage.svg' | relative_url }}" alt="Bar chart comparing visible-only, infrared-only, and two multimodal seeds" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div><span>Visible</span><strong>48.66</strong><small>AP</small></div>
    <div><span>Infrared</span><strong>42.20</strong><small>AP</small></div>
    <div><span>Multimodal seed 1</span><strong>53.19</strong><small>AP</small></div>
    <div><span>Multimodal seed 2</span><strong>53.52</strong><small>AP</small></div>
  </div>
  <p class="source-line"><span class="evidence-chip">Key message</span> Combining RGB and infrared produces the strongest overall detector.</p>

  <h3 class="mt-5">Result 2 — Full-benchmark fusion ablation</h3>
  <p class="section-intro">Once the default multimodal detector is strong, simple adaptive reweighting does not beat it on the full benchmark. The negative result is part of the answer.</p>
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/fusion-ablation.svg' | relative_url }}" alt="Horizontal bar chart of default multimodal fusion versus static and gated alternatives" loading="lazy">
  </figure>
  <details class="technical-details result-table-details mt-3">
    <summary>Exact full-benchmark AP values</summary>
    <div class="table-responsive">
      <table class="table technical-table">
        <thead><tr><th>Method</th><th>AP</th><th>AP50</th></tr></thead>
        <tbody>
          <tr class="table-emphasis"><td>Default multimodal</td><td>53.1935</td><td>82.3669</td></tr>
          <tr><td>Static 0.25</td><td>52.1932</td><td>—</td></tr>
          <tr><td>Static 0.50</td><td>52.8243</td><td>—</td></tr>
          <tr><td>Static 0.75</td><td>52.8200</td><td>—</td></tr>
          <tr><td>Dynamic gate</td><td>52.9163</td><td>—</td></tr>
          <tr><td>Residual gate</td><td>53.1922</td><td>—</td></tr>
        </tbody>
      </table>
    </div>
  </details>
  <p class="source-line"><span class="evidence-chip">Key message</span> Simple adaptive reweighting does not outperform the strong default fusion on the full benchmark.</p>

  <h3 class="mt-5">Result 3 — Learned modality preference</h3>
  <p class="section-intro">The dynamic gate still changes its preference across the feature pyramid. That is a behavioural observation, not a causal proof that the gate “understands” weather or lighting.</p>
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/modality-preference.svg' | relative_url }}" alt="Feature-pyramid diagram showing infrared-leaning p2, visible-leaning p3, and more balanced p4 and p5" loading="lazy">
  </figure>
  <p class="source-line"><span class="evidence-chip">Key interpretation</span> Modality preference changes across feature scales. Causality is not claimed.</p>

  <h3 class="mt-5">Result 4 — Supplementary challenge-scene evaluation</h3>
  <p class="section-intro">This split is automatically constructed from image statistics. It is <strong>not</strong> an official benchmark. It only asks whether adaptive fusion looks more useful when modality quality is more uneven.</p>
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/challenge-scenes.svg' | relative_url }}" alt="Bar charts of AP, AP50, and AP75 for equal fusion versus dynamic weighting on the challenge subset" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div><span>Equal fusion</span><strong>70.91</strong><small>AP · 94.83 AP50 · 80.18 AP75</small></div>
    <div><span>Dynamic weighting</span><strong>71.70</strong><small>AP · 96.43 AP50 · 85.27 AP75</small></div>
    <div><span>Δ AP</span><strong>+0.79</strong><small>modest overall gain</small></div>
    <div><span>Δ AP75</span><strong>+5.09</strong><small>largest reported movement</small></div>
  </div>
  <div class="tradeoff-callout mt-3">
    <strong>How to read this.</strong>
    Adaptive fusion shows a positive signal when modality quality becomes more uneven under difficult visual conditions. The subset is automatically constructed and does not replace the full-benchmark conclusion.
  </div>
</section>

<section class="project-section" id="qualitative-demo">
  <div class="section-kicker">9 · Qualitative demo</div>
  <h2>Visible, infrared, equal fusion, dynamic fusion</h2>
  <p class="section-intro">Switch condition. Only plates that exist in the source materials are shown. Glare and failure-case images were not available, so those tabs stay empty rather than being filled with substitutes.</p>
  <div data-rgbir-demo='{{ site.data.rgbir_demo.cases | jsonify }}' data-rgbir-initial="low-light">
    <div class="rgbir-demo-tabs" role="tablist" aria-label="Scene condition">
      {% for item in site.data.rgbir_demo.cases %}
      <button type="button" data-rgbir-case="{{ item[0] }}" aria-pressed="{% if item[0] == 'low-light' %}true{% else %}false{% endif %}">{{ item[1].label }}</button>
      {% endfor %}
    </div>
    <div class="rgbir-demo-grid">
      <figure>
        <span class="plate-label plate-visible">Visible</span>
        <div data-rgbir-pane="visible">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        <span class="plate-label plate-infrared">Infrared</span>
        <div data-rgbir-pane="infrared">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        <span class="plate-label plate-equal">Equal fusion</span>
        <div data-rgbir-pane="equal">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        <span class="plate-label plate-dynamic">Dynamic fusion</span>
        <div data-rgbir-pane="dynamic">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
    </div>
    <p class="source-line mt-3" data-rgbir-note></p>
  </div>
  <p class="source-line"><span class="evidence-chip">Evidence boundary</span> {{ site.data.rgbir_demo.note_default }} Green / red boxes on the plates come from the original qualitative package. Counts are shown only when those plates report them.</p>
</section>

<section class="project-section" id="limitations">
  <div class="section-kicker">10 · Limitations</div>
  <h2>What the results do not say</h2>
  <div class="objective-list">
    <div><strong>Full benchmark</strong><span>Dynamic fusion does not improve the full benchmark relative to default multimodal fusion.</span></div>
    <div><strong>Challenge subset</strong><span>The hard-scene split is automatically constructed and is not an official benchmark.</span></div>
    <div><strong>Effect size</strong><span>Some gains are modest, especially the +0.79 AP movement on the challenge subset.</span></div>
    <div><strong>Data provenance</strong><span>The raw dataset and split provenance are currently being revalidated.</span></div>
  </div>
</section>
