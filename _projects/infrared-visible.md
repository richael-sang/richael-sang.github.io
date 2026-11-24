---
layout: project
title: Infrared–Visible Multimodal Object Detection
title_zh: 红外–可见光多模态目标检测
subtitle: Adaptive RGB–IR Fusion under Changing Visual Conditions
subtitle_zh: 变化视觉条件下的自适应 RGB–红外融合
date: 2026-05-01 00:00:00 +0800
category: research
selected: true
detail_page: true
permalink: /projects/infrared-visible/
advanced_project: true
bilingual: true
project_page_style: true
project_page_script: true
project_theme: rgbir
project_type: Multimodal Perception · Object Detection
project_type_zh: 多模态感知 · 目标检测
description: An RGB–infrared object detection project investigating whether lightweight adaptive modality weighting can dynamically balance visual and thermal information under changing scene conditions.
og_type: article
og_image: /assets/images/projects/infrared-visible/concept.png
cover: /assets/images/projects/infrared-visible/concept.png
cover_fit: contain
hero_figure: /assets/images/projects/infrared-visible/concept.png
hero_figure_alt: Adaptive gating of RGB and infrared features into a weighted fused representation
hero_figure_alt_zh: 根据 RGB 与红外特征学习权重，再得到加权融合表示
abstract: >-
  An RGB–infrared object detection project investigating whether lightweight adaptive modality weighting can dynamically balance visual and thermal information under changing scene conditions.
abstract_zh: >-
  一项 RGB–红外目标检测研究：轻量自适应模态加权能否在变化场景中动态平衡可见光与热红外信息。
summary: >-
  Adaptive RGB–IR fusion for object detection: multimodal beats unimodal, but learned weighting is not universally better.
authors:
- Rui Sang
pub: "SAT301 Final Year Project, Xi’an Jiaotong-Liverpool University"
pub_date: "May 2026"
pub_date_zh: "2026 年 5 月"
pub_last: "· Supervised by Dr. Xiaohui Zhu"
pub_last_zh: "· 导师：朱晓辉博士"
hero_links:
  Qualitative Demo:
    url: "#qualitative-demo"
    target: _self
    icon: fas fa-images
    label_zh: 检测示例
section_nav:
- id: problem
  label: Problem
  label_zh: 问题
- id: motivation
  label: Motivation
  label_zh: 动机
- id: input
  label: Input
  label_zh: 输入
- id: architecture
  label: Model
  label_zh: 模型
- id: innovation
  label: Innovation
  label_zh: 创新
- id: output
  label: Output
  label_zh: 输出
- id: metrics
  label: Metrics
  label_zh: 指标
- id: results
  label: Results
  label_zh: 结果
- id: qualitative-demo
  label: Demo
  label_zh: 演示
---

<section class="project-section" id="problem">
  {% include i18n.html tag="div" class="section-kicker" en="1 · Problem" zh="1 · 问题" %}
  {% include i18n.html tag="h2" en="Should RGB and infrared always contribute equally?" zh="RGB 和红外是否应该始终等权贡献？" %}
  {% include i18n.html tag="p" class="section-intro" en="Visible and infrared are complementary, but they are not equally reliable in every scene. The question is whether a multimodal detector can learn <em>when</em> to trust each modality." zh="可见光与红外互补，但并非在每个场景都同样可靠。问题是：多模态检测器能否学会<em>何时</em>信任每一种模态。" %}
  <div class="modality-grid">
    <div class="modality-card modality-card-visible">
      {% include i18n.html tag="div" class="overview-label" en="Visible" zh="可见光" %}
      {% include i18n.html tag="h3" en="Texture, colour, boundaries" zh="纹理、颜色、边界" %}
      {% include i18n.html tag="p" en="Useful in well-lit scenes, but the signal can degrade under low light, glare, rain, or haze." zh="光照充足时很有用，但在低光、眩光、雨天或雾霾下信号会变差。" %}
    </div>
    <div class="modality-card modality-card-infrared">
      {% include i18n.html tag="div" class="overview-label" en="Infrared" zh="红外" %}
      {% include i18n.html tag="h3" en="Thermal contrast" zh="热对比" %}
      {% include i18n.html tag="p" en="Often stronger in low light, but it carries less texture, less colour, and weaker fine detail." zh="低光下通常更稳，但纹理、颜色和细结构更弱。" %}
    </div>
  </div>
  <div class="question-banner">{% include i18n.html en="Visible and infrared are complementary, so equal weighting is not always the right fusion rule." zh="可见光与红外互补，因此等权融合并不总是合适。" %}</div>
</section>

<section class="project-section" id="motivation">
  {% include i18n.html tag="div" class="section-kicker" en="2 · Motivation" zh="2 · 动机" %}
  {% include i18n.html tag="h2" en="Learn a modality preference instead of fixing one" zh="学习模态偏好，而不是手工固定权重" %}
  {% include i18n.html tag="p" class="section-intro" en="If the two sensors are not equally reliable in every scene, a detector that always mixes them 1:1 may waste a trustworthy channel or over-trust a degraded one. The project therefore tests whether a lightweight weighting rule can move with the input." zh="如果两个传感器并非在每个场景都同样可靠，始终 1:1 混合可能会浪费可信通道，或过度信任已经退化的通道。因此本项目检验轻量加权规则能否随输入变化。" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Question" zh="问题" %}
      {% include i18n.html tag="h3" en="Can the model learn when to trust RGB or IR?" zh="模型能否学会何时信任 RGB 或红外？" %}
      {% include i18n.html tag="p" en="The experiments change only the fusion rule, keeping the detector and evaluation protocol fixed." zh="实验只改变融合规则，检测器与评估协议保持不变。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Hypothesis" zh="假设" %}
      {% include i18n.html tag="h3" en="Reliability is scene-dependent" zh="可靠性随场景变化" %}
      {% include i18n.html tag="p" en="Visible cues should matter more when texture is intact; thermal cues should matter more when visible contrast collapses." zh="纹理完整时可见光应更重要；可见光对比崩溃时热红外应更重要。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Test" zh="检验" %}
      {% include i18n.html tag="h3" en="Fix the detector, change the mix" zh="固定检测器，只改混合方式" %}
      {% include i18n.html tag="p" en="Static weights, a dynamic gate, and a conservative residual gate are compared against default multimodal fusion." zh="将静态权重、动态门控和保守残差门控与默认多模态融合对比。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Expectation" zh="预期" %}
      {% include i18n.html tag="h3" en="When it may help" zh="何时可能有用" %}
      {% include i18n.html tag="p" en="If default fusion is already strong, adaptive weighting may matter mainly when modality quality becomes uneven." zh="若默认融合已经很强，自适应加权可能主要在模态质量更不均匀时起作用。" %}
    </div>
  </div>
</section>

<section class="project-section" id="input">
  {% include i18n.html tag="div" class="section-kicker" en="3 · Input" zh="3 · 输入" %}
  {% include i18n.html tag="h2" en="A registered RGB–infrared pair" zh="一对已配准的 RGB–红外图像" %}
  {% include i18n.html tag="p" class="section-intro" en="Each sample is a spatially aligned visible image and infrared image. In the night scene below, pedestrians that fade in RGB remain clear in IR." zh="每个样本都是空间对齐的可见光图与红外图。下图夜景中，RGB 里几乎看不见的行人在红外中仍然清楚。" %}
  <div class="paired-input-grid">
    <figure>
      {% include i18n.html tag="span" class="plate-label plate-visible" en="Visible" zh="可见光" %}
      <img src="{{ '/assets/images/projects/infrared-visible/demo/pair-visible.jpg' | relative_url }}" alt="Registered night-time visible image of a road scene" data-alt-en="Registered night-time visible image of a road scene" data-alt-zh="已配准的夜间可见光道路图像" loading="lazy">
    </figure>
    <figure>
      {% include i18n.html tag="span" class="plate-label plate-infrared" en="Infrared" zh="红外" %}
      <img src="{{ '/assets/images/projects/infrared-visible/demo/pair-infrared.jpg' | relative_url }}" alt="Registered night-time infrared image of the same road scene" data-alt-en="Registered night-time infrared image of the same road scene" data-alt-zh="同一道路场景的已配准夜间红外图像" loading="lazy">
    </figure>
  </div>
</section>

<section class="project-section" id="architecture">
  {% include i18n.html tag="div" class="section-kicker" en="4 · Model architecture" zh="4 · 模型结构" %}
  {% include i18n.html tag="h2" en="Two streams, one DiffusionDet head" zh="双流特征，一个 DiffusionDet 检测头" %}
  {% include i18n.html tag="p" class="section-intro" en="The experimental framework is E2E-MFD-HOD on Detectron2, with a DiffusionDet detection head." zh="实验框架是 Detectron2 上的 E2E-MFD-HOD，检测头为 DiffusionDet。" %}
  <figure class="technical-figure technical-figure-borderless">
    <img src="{{ '/assets/images/projects/infrared-visible/architecture.png' | relative_url }}" alt="RGB and infrared streams, adaptive fusion options, DiffusionDet head, and detection outputs" data-alt-en="RGB and infrared streams, adaptive fusion options, DiffusionDet head, and detection outputs" data-alt-zh="RGB 与红外双流、自适应融合选项、DiffusionDet 检测头与检测输出" loading="lazy">
  </figure>
</section>

<section class="project-section" id="innovation">
  {% include i18n.html tag="div" class="section-kicker" en="5 · Core innovation" zh="5 · 核心创新" %}
  {% include i18n.html tag="h2" en="Adaptive modality weighting" zh="自适应模态加权" %}
  {% include i18n.html tag="p" class="section-intro" en="Instead of assuming equal RGB / IR importance, the fusion step learns a visible weight \(\alpha\) from features. \(\alpha\) may vary by feature level and by input." zh="融合步不再假设 RGB / 红外同等重要，而是从特征中学习可见光权重 \(\alpha\)。\(\alpha\) 可以随特征层和输入变化。" %}
  <div class="fusion-formula">
    {% include i18n.html en="Fused feature \(= \alpha \times\) visible feature \(+ (1-\alpha) \times\) infrared feature" zh="融合特征 \(= \alpha \times\) 可见光特征 \(+ (1-\alpha) \times\) 红外特征" %}
  </div>
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Experiment 1" zh="实验 1" %}
      {% include i18n.html tag="h3" en="Fixed static weighting" zh="固定静态加权" %}
      {% include i18n.html tag="p" en="Manually set visible ratios to 0.25, 0.50, and 0.75." zh="把可见光比例手工设为 0.25、0.50 和 0.75。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Experiment 2" zh="实验 2" %}
      {% include i18n.html tag="h3" en="Lightweight dynamic gating" zh="轻量动态门控" %}
      {% include i18n.html tag="p" en="Predict \(\alpha\) from the two feature streams." zh="由两路特征预测 \(\alpha\)。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Experiment 3" zh="实验 3" %}
      {% include i18n.html tag="h3" en="Conservative residual gating" zh="保守残差门控" %}
      {% include i18n.html tag="p" en="Keep the default fusion path and learn only a small correction." zh="保留默认融合路径，只学习一个小修正。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Goal" zh="目标" %}
      {% include i18n.html tag="h3" en="Learned preference" zh="学习得到的偏好" %}
      {% include i18n.html tag="p" en="The model allocates visible and infrared weight from features rather than using a fixed ratio." zh="模型根据特征分配可见光与红外权重，而不是使用固定比例。" %}
    </div>
  </div>
  <div class="evidence-note mt-3">
    {% include i18n.html tag="strong" en="Also explored: modality-robust training." zh="同时探索：模态稳健训练。" %}
    {% include i18n.html en="During training, one modality is mildly attenuated to simulate a degraded sensor and reduce over-reliance on a single stream." zh="训练时轻微衰减其中一个模态，以模拟传感器退化，并减少对单一通路的过度依赖。" %}
  </div>
</section>

<section class="project-section" id="output">
  {% include i18n.html tag="div" class="section-kicker" en="6 · Output" zh="6 · 输出" %}
  {% include i18n.html tag="h2" en="Multiclass boxes, labels, and scores" zh="多类检测框、类别与分数" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Boxes" zh="检测框" %}
      {% include i18n.html tag="h3" en="Object bounding boxes" zh="目标边界框" %}
      {% include i18n.html tag="p" en="Horizontal detections on the aligned scene." zh="对齐场景上的水平检测框。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Labels" zh="类别" %}
      {% include i18n.html tag="h3" en="Category names" zh="类别名称" %}
      {% include i18n.html tag="p" en="A multiclass vocabulary, including people and common vehicles." zh="多类词表，包括行人和常见车辆。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Scores" zh="分数" %}
      {% include i18n.html tag="h3" en="Confidence" zh="置信度" %}
      {% include i18n.html tag="p" en="Each box carries a detector confidence used by AP." zh="每个框带有检测置信度，用于计算 AP。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Task" zh="任务" %}
      {% include i18n.html tag="h3" en="Multiclass object detection" zh="多类目标检测" %}
      {% include i18n.html tag="p" en="The output of the system is a standard detection result." zh="系统输出为标准目标检测结果。" %}
    </div>
  </div>
</section>

<section class="project-section" id="metrics">
  {% include i18n.html tag="div" class="section-kicker" en="7 · Metrics" zh="7 · 指标" %}
  {% include i18n.html tag="h2" en="Detection metrics" zh="检测指标" %}
  {% include i18n.html tag="p" class="section-intro" en="Results are reported with standard COCO-style detection metrics." zh="结果按标准 COCO 风格检测指标报告。" %}
  <div class="metric-tooltip-grid">
    <div class="metric-tip" tabindex="0" title="Mean Average Precision averaged over IoU thresholds from 0.50 to 0.95.">
      <strong>AP</strong>
      {% include i18n.html tag="span" en="Primary score. Average precision across IoU thresholds 0.50–0.95." zh="主指标。在 IoU 0.50–0.95 上平均的精度。" %}
    </div>
    <div class="metric-tip" tabindex="0" title="Average Precision at a single IoU threshold of 0.50.">
      <strong>AP50</strong>
      {% include i18n.html tag="span" en="Loose localisation. A prediction counts if IoU is at least 0.50." zh="较松的定位。IoU 至少 0.50 即计入。" %}
    </div>
    <div class="metric-tip" tabindex="0" title="Average Precision at a single IoU threshold of 0.75.">
      <strong>AP75</strong>
      {% include i18n.html tag="span" en="Stricter boxes. A prediction counts if IoU is at least 0.75." zh="更严的框。IoU 至少 0.75 才计入。" %}
    </div>
    <div class="metric-tip" tabindex="0" title="Average Precision computed independently for each object category.">
      {% include i18n.html tag="strong" en="Per-class AP" zh="逐类 AP" %}
      {% include i18n.html tag="span" en="Average precision computed separately for each object category." zh="按每个目标类别分别计算的平均精度。" %}
    </div>
  </div>
</section>

<section class="project-section" id="results">
  {% include i18n.html tag="div" class="section-kicker" en="8 · Results" zh="8 · 结果" %}
  {% include i18n.html tag="h2" en="Main findings" zh="主要发现" %}

  {% include i18n.html tag="h3" class="mt-4" en="Result 1 — Multimodal advantage" zh="结果 1 — 多模态优势" %}
  {% include i18n.html tag="p" class="section-intro" en="Combining RGB and infrared produces the strongest overall detector. Two multimodal seeds stay within 0.33 AP of each other." zh="结合 RGB 与红外得到最强的整体检测器。两个多模态随机种子相差不超过 0.33 AP。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/multimodal-advantage.svg' | relative_url }}" alt="Bar chart comparing visible-only, infrared-only, and two multimodal seeds" data-alt-en="Bar chart comparing visible-only, infrared-only, and two multimodal seeds" data-alt-zh="可见光、红外与两个多模态种子的 AP 柱状图" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="Visible" zh="可见光" %}<strong>48.66</strong><small>AP</small></div>
    <div>{% include i18n.html tag="span" en="Infrared" zh="红外" %}<strong>42.20</strong><small>AP</small></div>
    <div>{% include i18n.html tag="span" en="Multimodal seed 1" zh="多模态种子 1" %}<strong>53.19</strong><small>AP</small></div>
    <div>{% include i18n.html tag="span" en="Multimodal seed 2" zh="多模态种子 2" %}<strong>53.52</strong><small>AP</small></div>
  </div>
  <p class="source-line"><span class="evidence-chip">{% include i18n.html en="Key message" zh="要点" %}</span> {% include i18n.html en="Combining RGB and infrared produces the strongest overall detector." zh="结合 RGB 与红外得到最强的整体检测器。" %}</p>

  {% include i18n.html tag="h3" class="mt-5" en="Result 2 — Full-benchmark fusion ablation" zh="结果 2 — 全基准融合消融" %}
  {% include i18n.html tag="p" class="section-intro" en="Once the default multimodal detector is strong, simple adaptive reweighting does not improve it on the full benchmark." zh="默认多模态检测器已经较强时，简单自适应再加权在全基准上没有进一步提升。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/fusion-ablation.svg' | relative_url }}" alt="Horizontal bar chart of default multimodal fusion versus static and gated alternatives" data-alt-en="Horizontal bar chart of default multimodal fusion versus static and gated alternatives" data-alt-zh="默认多模态融合与静态、门控方案的水平柱状图" loading="lazy">
  </figure>
  <details class="technical-details result-table-details mt-3">
    <summary>{% include i18n.html en="Exact full-benchmark AP values" zh="全基准 AP 精确值" %}</summary>
    <div class="table-responsive">
      <table class="table technical-table">
        <thead><tr><th>{% include i18n.html en="Method" zh="方法" %}</th><th>AP</th><th>AP50</th></tr></thead>
        <tbody>
          <tr class="table-emphasis"><td>{% include i18n.html en="Default multimodal" zh="默认多模态" %}</td><td>53.1935</td><td>82.3669</td></tr>
          <tr><td>{% include i18n.html en="Static 0.25" zh="静态 0.25" %}</td><td>52.1932</td><td>—</td></tr>
          <tr><td>{% include i18n.html en="Static 0.50" zh="静态 0.50" %}</td><td>52.8243</td><td>—</td></tr>
          <tr><td>{% include i18n.html en="Static 0.75" zh="静态 0.75" %}</td><td>52.8200</td><td>—</td></tr>
          <tr><td>{% include i18n.html en="Dynamic gate" zh="动态门控" %}</td><td>52.9163</td><td>—</td></tr>
          <tr><td>{% include i18n.html en="Residual gate" zh="残差门控" %}</td><td>53.1922</td><td>—</td></tr>
        </tbody>
      </table>
    </div>
  </details>
  <p class="source-line"><span class="evidence-chip">{% include i18n.html en="Key message" zh="要点" %}</span> {% include i18n.html en="Simple adaptive reweighting does not outperform the strong default fusion on the full benchmark." zh="简单自适应再加权在全基准上没有超过较强的默认融合。" %}</p>

  {% include i18n.html tag="h3" class="mt-5" en="Result 3 — Learned modality preference" zh="结果 3 — 学到的模态偏好" %}
  {% include i18n.html tag="p" class="section-intro" en="The dynamic gate still changes its preference across the feature pyramid: p2 is more infrared-oriented, p3 is more visible-oriented, and p4 / p5 stay closer to balanced." zh="动态门控在特征金字塔各层上的偏好并不相同：p2 更偏红外，p3 更偏可见光，p4 / p5 更接近平衡。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/modality-preference.png' | relative_url }}" alt="Feature-pyramid diagram showing infrared-leaning p2, visible-leaning p3, and more balanced p4 and p5" data-alt-en="Feature-pyramid diagram showing infrared-leaning p2, visible-leaning p3, and more balanced p4 and p5" data-alt-zh="特征金字塔：p2 更偏红外，p3 更偏可见光，p4 与 p5 更接近平衡" loading="lazy">
  </figure>
  <p class="source-line"><span class="evidence-chip">{% include i18n.html en="Observation" zh="观察" %}</span> {% include i18n.html en="Modality preference changes across feature scales." zh="模态偏好随特征尺度变化。" %}</p>

  {% include i18n.html tag="h3" class="mt-5" en="Result 4 — Supplementary challenge-scene evaluation" zh="结果 4 — 补充性挑战场景评估" %}
  {% include i18n.html tag="p" class="section-intro" en="On an automatically constructed hard-scene subset, adaptive fusion shows a modest gain when modality quality is more uneven. This subset is not an official benchmark." zh="在自动构造的困难场景子集上，当模态质量更不均匀时，自适应融合出现小幅提升。该子集不是官方基准。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/challenge-scenes.svg' | relative_url }}" alt="Bar charts of AP, AP50, and AP75 for equal fusion versus dynamic weighting on the challenge subset" data-alt-en="Bar charts of AP, AP50, and AP75 for equal fusion versus dynamic weighting on the challenge subset" data-alt-zh="挑战子集上 equal fusion 与动态加权的 AP、AP50、AP75 柱状图" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="Equal fusion" zh="等权融合" %}<strong>70.91</strong><small>AP · 94.83 AP50 · 80.18 AP75</small></div>
    <div>{% include i18n.html tag="span" en="Dynamic weighting" zh="动态加权" %}<strong>71.70</strong><small>AP · 96.43 AP50 · 85.27 AP75</small></div>
    <div><span>Δ AP</span><strong>+0.79</strong>{% include i18n.html tag="small" en="modest overall gain" zh="整体增益有限" %}</div>
    <div><span>Δ AP75</span><strong>+5.09</strong>{% include i18n.html tag="small" en="largest reported movement" zh="报告中最大的变动" %}</div>
  </div>
  <div class="tradeoff-callout mt-3">
    {% include i18n.html en="Adaptive fusion is more promising when visual conditions make the two modalities uneven, but this does not replace the full-benchmark result." zh="当视觉条件使两种模态更不均匀时，自适应融合更有前景，但不能取代全基准结果。" %}
  </div>
</section>

<section class="project-section" id="qualitative-demo">
  {% include i18n.html tag="div" class="section-kicker" en="9 · Qualitative demo" zh="9 · 检测示例" %}
  {% include i18n.html tag="h2" en="Visible, infrared, equal fusion, dynamic fusion" zh="可见光、红外、等权融合、动态融合" %}
  {% include i18n.html tag="p" class="section-intro" en="Compare detections under low light and rain." zh="对比低光与雨天条件下的检测结果。" %}
  <div data-rgbir-demo='{{ site.data.rgbir_demo.cases | jsonify }}' data-rgbir-initial="low-light">
    <div class="rgbir-demo-tabs" role="tablist" aria-label="Scene condition">
      {% for item in site.data.rgbir_demo.cases %}
      {% assign demo_case_id = item[0] %}
      {% assign demo_case = item[1] %}
      <button type="button" data-rgbir-case="{{ demo_case_id }}" aria-pressed="{% if demo_case_id == 'low-light' %}true{% else %}false{% endif %}">{% include i18n.html en=demo_case.label zh=demo_case.label_zh %}</button>
      {% endfor %}
    </div>
    <div class="rgbir-demo-grid">
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-visible" en="Visible" zh="可见光" %}
        <div data-rgbir-pane="visible">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-infrared" en="Infrared" zh="红外" %}
        <div data-rgbir-pane="infrared">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-equal" en="Equal fusion" zh="等权融合" %}
        <div data-rgbir-pane="equal">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <figcaption class="small text-muted mt-2 mb-0" data-caption></figcaption>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-dynamic" en="Dynamic fusion" zh="动态融合" %}
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
</section>
