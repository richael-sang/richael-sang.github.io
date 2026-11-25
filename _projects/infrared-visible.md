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
- id: overview
  label: Overview
  label_zh: 概览
- id: problem
  label: Problem & input
  label_zh: 问题与输入
- id: architecture
  label: Model & gate
  label_zh: 模型与门控
- id: training
  label: Training
  label_zh: 训练
- id: results
  label: Results
  label_zh: 结果
- id: qualitative-demo
  label: Demo
  label_zh: 演示
- id: next
  label: Next
  label_zh: 后续研究
---

<section class="project-section" id="overview">
  {% include i18n.html tag="div" class="section-kicker" en="1 · Overview" zh="1 · 项目概览" %}
  {% include i18n.html tag="h2" en="What I built, and what it achieved" zh="我做了什么，取得了什么结果" %}
  {% include i18n.html tag="p" class="section-intro" en="I reproduced an RGB–infrared detector on M3FD, integrated a lightweight modality gate into its fusion step, trained it end-to-end with detection supervision, and validated it through controlled ablations, gate diagnostics, and a challenge-scene benchmark." zh="我在 M3FD 上复现了 RGB–红外检测器，把轻量模态门控接入其融合步骤，用检测监督端到端训练，并通过受控消融、门控诊断和挑战场景评估进行验证。" %}
  <div class="stage-strip">
    <div class="stage-card"><b>01</b>{% include i18n.html tag="strong" en="Module integration" zh="模块接入" %}{% include i18n.html tag="span" en="Gate inserted at each FPN level of the fusion step" zh="在融合步骤的每个 FPN 层接入门控" %}</div>
    <div class="stage-card"><b>02</b>{% include i18n.html tag="strong" en="Model training" zh="模型训练" %}{% include i18n.html tag="span" en="Gate learned jointly with the detector" zh="门控与检测器联合学习" %}</div>
    <div class="stage-card"><b>03</b>{% include i18n.html tag="strong" en="Controlled ablation" zh="受控消融" %}{% include i18n.html tag="span" en="Same detector, only the fusion rule changes" zh="检测器不变，只改融合规则" %}</div>
    <div class="stage-card"><b>04</b>{% include i18n.html tag="strong" en="Gate diagnostics" zh="门控诊断" %}{% include i18n.html tag="span" en="Learned preference per pyramid level" zh="分析各金字塔层学到的偏好" %}</div>
    <div class="stage-card"><b>05</b>{% include i18n.html tag="strong" en="Challenge validation" zh="挑战场景验证" %}{% include i18n.html tag="span" en="Low light, rain, and haze subset" zh="低光、雨天、雾霾子集" %}</div>
  </div>
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="Multimodal vs visible-only" zh="多模态 vs 仅可见光" %}<strong>+4.5 AP</strong>{% include i18n.html tag="small" en="full M3FD test" zh="完整 M3FD 测试集" %}</div>
    <div>{% include i18n.html tag="span" en="Multimodal vs infrared-only" zh="多模态 vs 仅红外" %}<strong>+11.0 AP</strong>{% include i18n.html tag="small" en="full M3FD test" zh="完整 M3FD 测试集" %}</div>
    <div>{% include i18n.html tag="span" en="Dynamic gate vs equal fusion" zh="动态门控 vs 等权融合" %}<strong>+1.60 AP50</strong>{% include i18n.html tag="small" en="challenge subset" zh="挑战子集" %}</div>
    <div>{% include i18n.html tag="span" en="High-IoU detection" zh="高 IoU 检测" %}<strong>+5.1 AP75</strong>{% include i18n.html tag="small" en="same challenge protocol" zh="同一挑战子集协议" %}</div>
  </div>
</section>

<section class="project-section" id="problem">
  {% include i18n.html tag="div" class="section-kicker" en="2 · Problem and input" zh="2 · 问题与输入" %}
  {% include i18n.html tag="h2" en="Why fusion should be dynamic" zh="为什么融合需要动态调整" %}
  {% include i18n.html tag="p" class="section-intro" en="Visible and infrared images are complementary, but neither is reliable in every scene. A detector that always mixes them 1:1 can waste a trustworthy channel or over-trust a degraded one." zh="可见光与红外互补，但都不是在每个场景都可靠。始终 1:1 混合的检测器，可能浪费可信的通道，或过度信任已经退化的通道。" %}
  <div class="modality-grid">
    <div class="modality-card modality-card-visible">
      {% include i18n.html tag="div" class="overview-label" en="Visible" zh="可见光" %}
      {% include i18n.html tag="h3" en="Texture, colour, boundaries" zh="纹理、颜色、边界" %}
      {% include i18n.html tag="p" en="Strong in well-lit scenes; degrades under low light, glare, rain, or haze." zh="光照充足时很强；在低光、眩光、雨天或雾霾下会退化。" %}
    </div>
    <div class="modality-card modality-card-infrared">
      {% include i18n.html tag="div" class="overview-label" en="Infrared" zh="红外" %}
      {% include i18n.html tag="h3" en="Thermal contrast" zh="热对比" %}
      {% include i18n.html tag="p" en="Stable in low light, but carries less texture, colour, and fine detail." zh="低光下更稳定，但纹理、颜色和细节更弱。" %}
    </div>
  </div>
  {% include i18n.html tag="p" class="section-intro mt-4" en="Each sample is a registered visible–infrared pair. In the night scene below, pedestrians that fade in RGB remain clear in IR." zh="每个样本都是一对已配准的可见光–红外图像。下图夜景中，RGB 里几乎看不见的行人在红外中仍然清楚。" %}
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
  <div class="question-banner">{% include i18n.html en="Can the detector learn, from the input itself, how much to trust each modality?" zh="检测器能否根据输入本身，学会该信任哪种模态、信任多少？" %}</div>
</section>

<section class="project-section" id="architecture">
  {% include i18n.html tag="div" class="section-kicker" en="3 · Model and gate" zh="3 · 模型与门控" %}
  {% include i18n.html tag="h2" en="Two streams, one gated fusion, one DiffusionDet head" zh="双流特征、门控融合、DiffusionDet 检测头" %}
  {% include i18n.html tag="p" class="section-intro" en="The framework is E2E-MFD-HOD on Detectron2 with a DiffusionDet head. Only the fusion step between the two FPN streams is changed." zh="实验框架是 Detectron2 上的 E2E-MFD-HOD，检测头为 DiffusionDet。只改动两路 FPN 特征之间的融合步骤。" %}
  <figure class="technical-figure technical-figure-borderless">
    <img src="{{ '/assets/images/projects/infrared-visible/architecture.png' | relative_url }}" alt="RGB and infrared streams, adaptive fusion options, DiffusionDet head, and detection outputs" data-alt-en="RGB and infrared streams, adaptive fusion options, DiffusionDet head, and detection outputs" data-alt-zh="RGB 与红外双流、自适应融合选项、DiffusionDet 检测头与检测输出" loading="lazy">
  </figure>

  {% include i18n.html tag="h3" class="mt-5" en="How the lightweight gate works" zh="轻量门控如何工作" %}
  {% include i18n.html tag="p" class="section-intro" en="<strong>The gate predicts an input-dependent modality weight at each feature level, allowing the detector to adjust the contribution of RGB and infrared features.</strong>" zh="<strong>门控根据当前两路特征，在不同特征层预测模态权重，动态调整可见光与红外信息的贡献。</strong>" %}
  {% include figure_slot.html class="technical-figure technical-figure-borderless diagram-figure" src="/assets/images/projects/infrared-visible/lightweight_gate_mechanism.svg" label="Gate" ratio="1118 / 464" alt_en="Visible and infrared features are pooled to predict a weight, which then rescales the full feature maps before fusion" alt_zh="可见光与红外特征经池化预测权重，再对完整特征图加权后融合" %}
  <div class="math-panel">
    <span class="evidence-chip">{% include i18n.html en="Scale-matched illustration" zh="尺度保持示意" %}</span>
    <div class="math-block">\[\alpha_l = g_l\big(F_v^l,\, F_i^l\big)\]</div>
    <div class="math-block">\[F_f^l = 2\left[\alpha_l \odot F_v^l + (1-\alpha_l) \odot F_i^l\right]\]</div>
  </div>
  <ul class="math-notes">
    <li>{% include i18n.html en="\(\alpha_l\) is the relative weight of visible features; \(1-\alpha_l\) is the relative weight of infrared." zh="\(\alpha_l\) 表示可见光的相对权重；\(1-\alpha_l\) 表示红外的相对权重。" %}</li>
    <li>{% include i18n.html en="The weight changes with the input and with the feature level \(l\)." zh="权重随输入和特征层 \(l\) 变化。" %}</li>
    <li>{% include i18n.html en="The factor 2 keeps the equal-weight case at the same magnitude as default feature addition." zh="系数 2 使等权状态与默认的特征相加保持相同幅值。" %}</li>
  </ul>
  <details class="technical-details mt-3">
    <summary>{% include i18n.html en="Gate implementation details" zh="门控实现细节" %}</summary>
    <div class="details-body">
      <div class="math-block">\[\alpha_l = \sigma\!\Big(W_2\,\operatorname{ReLU}\big(W_1\,[\operatorname{GAP}(F_v^l);\,\operatorname{GAP}(F_i^l)] + b_1\big) + b_2\Big)\]</div>
      <div class="table-responsive">
        <table class="table technical-table">
          <thead><tr><th>{% include i18n.html en="Operation" zh="操作" %}</th><th>{% include i18n.html en="Example tensor shape" zh="示例张量形状" %}</th></tr></thead>
          <tbody>
            <tr><td>{% include i18n.html en="Two FPN features" zh="两路 FPN 特征" %}</td><td>\(B\times256\times H_l\times W_l\) {% include i18n.html en="each" zh="各一份" %}</td></tr>
            <tr><td>{% include i18n.html en="Global average pooling" zh="分别全局平均池化" %}</td><td>\(B\times256\) {% include i18n.html en="each" zh="各一份" %}</td></tr>
            <tr><td>{% include i18n.html en="Concatenation" zh="拼接" %}</td><td>\(B\times512\)</td></tr>
            <tr><td>Linear + ReLU</td><td>\(B\times32\)</td></tr>
            <tr><td>Linear + Sigmoid</td><td>\(B\times1\)</td></tr>
            <tr><td>{% include i18n.html en="Broadcast weight" zh="广播权重" %}</td><td>\(B\times1\times1\times1\)</td></tr>
            <tr class="table-emphasis"><td>{% include i18n.html en="Fused feature" zh="融合结果" %}</td><td>\(B\times256\times H_l\times W_l\)</td></tr>
          </tbody>
        </table>
      </div>
      {% include i18n.html tag="p" en="<strong>This example uses one scalar gate per image and feature level</strong>: all spatial positions in a level share the same weight. The pooled vectors only produce the weight; the full feature maps keep their spatial layout and are what the detector sees." zh="<strong>此示例为每张图像、每个特征层生成一个标量权重</strong>，同层各空间位置共享该权重。池化向量只用于生成权重；真正被加权并送入检测器的是保留空间结构的完整特征图。" %}
      {% include i18n.html tag="p" en="Illustrative configuration: 512 → 32 → 1; approximately 16.4K parameters per level, or 65.8K across four independent gates (p2–p5), a negligible addition to the detector." zh="示例配置：512 → 32 → 1；每层约 16.4K 参数，四个独立门控（p2–p5）共约 65.8K，相对检测器几乎可以忽略。" %}
    </div>
  </details>

  {% include i18n.html tag="h3" class="mt-5" en="Fusion variants compared" zh="对比的融合方式" %}
  <div class="overview-grid overview-grid-3">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Static" zh="静态" %}
      {% include i18n.html tag="h3" en="Fixed visible ratio" zh="固定可见光比例" %}
      {% include i18n.html tag="p" en="\(\alpha\) set by hand to 0.25, 0.50, or 0.75." zh="\(\alpha\) 手工设为 0.25、0.50 或 0.75。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Dynamic" zh="动态" %}
      {% include i18n.html tag="h3" en="Lightweight gate" zh="轻量门控" %}
      {% include i18n.html tag="p" en="\(\alpha_l\) predicted from the two feature streams at every level." zh="在每一层由两路特征预测 \(\alpha_l\)。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Residual" zh="残差" %}
      {% include i18n.html tag="h3" en="Conservative correction" zh="保守修正" %}
      {% include i18n.html tag="p" en="Keeps the default fusion path and learns only a small correction." zh="保留默认融合路径，只学习一个小修正。" %}
    </div>
  </div>
</section>

<section class="project-section" id="training">
  {% include i18n.html tag="div" class="section-kicker" en="4 · Training" zh="4 · 训练过程与损失" %}
  {% include i18n.html tag="h2" en="How the model learns modality weights" zh="模型如何学会分配模态权重" %}
  {% include i18n.html tag="p" class="section-intro" en="<strong>The gate is trained through detection supervision. Classification and localisation errors propagate through the fused features to update the gating network.</strong> Over training, it learns the modality split that is most useful for detection." zh="<strong>门控通过检测监督学习。分类与定位误差经融合特征反向传播，更新门控参数</strong>，使模型逐渐学会对当前检测任务更有用的模态分配。" %}
  {% include figure_slot.html class="technical-figure technical-figure-borderless diagram-figure" src="/assets/images/projects/infrared-visible/detection_supervised_gate_training.svg" label="Training" ratio="1119 / 421" alt_en="Forward pass from inputs to detections, and the training-only backward path from the detection loss through the head and fused features into the gate" alt_zh="从输入到检测结果的前向计算，以及仅在训练时从检测损失经检测头、融合特征回到门控的反向传播路径" %}
  <div class="evidence-note mt-3">
    {% include i18n.html tag="strong" en="Inference requires only a forward pass to generate the weights." zh="推理时只需一次前向计算即可生成权重。" %}
    {% include i18n.html en="The gate adapts to each new image without any retraining." zh="门控会针对每张新图像自动调整，无需重新训练。" %}
  </div>

  {% include i18n.html tag="h3" class="mt-5" en="Detection loss" zh="检测损失" %}
  <div class="math-panel">
    <div class="math-block">\[\mathcal{L}_{\mathrm{det}} = \lambda_{\mathrm{cls}}\,\mathcal{L}_{\mathrm{cls}} + \lambda_{L1}\,\mathcal{L}_{L1} + \lambda_{\mathrm{GIoU}}\,\mathcal{L}_{\mathrm{GIoU}}\]</div>
  </div>
  <div class="overview-grid overview-grid-3">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Classification" zh="分类" %}
      {% include i18n.html tag="h3" en="What is it?" zh="是什么" %}
      {% include i18n.html tag="p" en="Predicts the object class and separates objects from background." zh="判断目标类别，区分目标与背景。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="L1 regression" zh="L1 回归" %}
      {% include i18n.html tag="h3" en="Where exactly?" zh="坐标多准" %}
      {% include i18n.html tag="p" en="Reduces the coordinate gap between predicted and ground-truth boxes." zh="减小预测框与真实框的坐标差。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="GIoU" zh="GIoU" %}
      {% include i18n.html tag="h3" en="How well does it overlap?" zh="重叠多好" %}
      {% include i18n.html tag="p" en="Improves the geometric overlap between predicted and ground-truth boxes." zh="改善预测框与真实框的几何重叠。" %}
    </div>
  </div>
  {% include i18n.html tag="p" class="source-line" en="Intermediate detection stages also receive supervision to support progressive box refinement." zh="中间检测阶段同样接受监督，以支持检测框的逐步细化。" %}
  <details class="technical-details mt-3">
    <summary>{% include i18n.html en="Auxiliary image-fusion branch" zh="辅助图像融合分支" %}</summary>
    <div class="details-body">
      <div class="math-block">\[\mathcal{L}_{\mathrm{total}} = \mathcal{L}_{\mathrm{det}} + \lambda_{\mathrm{fusion}}\,\mathcal{L}_{\mathrm{fusion}}\]</div>
      {% include i18n.html tag="p" en="The image-fusion term comes from the E2E-MFD baseline framework and follows its configuration. The gate adds no separate loss: it is learned entirely from the existing objective." zh="图像融合项来自 E2E-MFD 基线框架，按其配置使用。门控没有额外损失项，完全从已有目标中学习。" %}
    </div>
  </details>

  {% include i18n.html tag="h3" class="mt-5" en="Training pipeline" zh="训练流程" %}
  <ol class="walkthrough">
    <li><strong>{% include i18n.html en="Data preparation" zh="数据准备" %}</strong>{% include i18n.html en="Pair checks, synchronised geometric transforms for both modalities, and box-coordinate handling." zh="配对检查、两种模态同步几何变换、检测框坐标处理。" %}</li>
    <li><strong>{% include i18n.html en="Baseline training" zh="基线训练" %}</strong>{% include i18n.html en="Visible-only, infrared-only, and multimodal runs; initialisation and evaluation checked against released weights." zh="仅可见光、仅红外与多模态三组训练；对照官方权重检查初始化与评估。" %}</li>
    <li><strong>{% include i18n.html en="Module integration" zh="模块接入" %}</strong>{% include i18n.html en="Gate parameters, gradients, and output ranges checked before long runs." zh="长时间训练前检查门控参数、梯度和输出范围。" %}</li>
    <li><strong>{% include i18n.html en="Model optimisation" zh="模型优化" %}</strong>{% include i18n.html en="Fusion and detection trained jointly through classification and localisation supervision." zh="通过分类与定位监督联合训练融合与检测。" %}</li>
    <li><strong>{% include i18n.html en="Controlled evaluation" zh="受控评估" %}</strong>{% include i18n.html en="Detector and evaluator fixed; only the fusion rule differs between runs." zh="固定检测器与评估器，各组之间只有融合规则不同。" %}</li>
  </ol>
  <details class="technical-details mt-3">
    <summary>{% include i18n.html en="Training configuration" zh="训练配置" %}</summary>
    <div class="table-responsive">
      <table class="table technical-table">
        <tbody>
          <tr><td>{% include i18n.html en="Framework" zh="框架" %}</td><td>{% include i18n.html en="E2E-MFD-HOD · Detectron2 · DiffusionDet" zh="E2E-MFD-HOD · Detectron2 · DiffusionDet" %}</td></tr>
          <tr><td>{% include i18n.html en="Dataset" zh="数据集" %}</td><td>{% include i18n.html en="M3FD, official split: 2,940 trainval / 1,260 test" zh="M3FD 官方划分：2,940 训练验证 / 1,260 测试" %}</td></tr>
          <tr><td>{% include i18n.html en="Initialisation" zh="初始化" %}</td><td>{% include i18n.html en="Candidate DiffusionDet checkpoint (candidate-init)" zh="候选 DiffusionDet 检查点（candidate-init）" %}</td></tr>
          <tr><td>{% include i18n.html en="Schedule" zh="训练长度" %}</td><td>{% include i18n.html en="15,000 iterations, with periodic evaluation" zh="15,000 次迭代，期间定期评估" %}</td></tr>
          <tr><td>{% include i18n.html en="Reproducibility" zh="可复现性" %}</td><td>{% include i18n.html en="Two seeds for the multimodal baseline; best-vs-final checkpoint gap checked" zh="多模态基线跑两个种子；检查最佳与最终检查点的差距" %}</td></tr>
          <tr><td>{% include i18n.html en="Challenge fine-tuning" zh="挑战子集微调" %}</td><td>{% include i18n.html en="Both methods from the same multimodal checkpoint; 361 train / 138 test images" zh="两种方法从同一多模态检查点出发；361 张训练 / 138 张测试" %}</td></tr>
          <tr><td>{% include i18n.html en="Evaluation" zh="评估" %}</td><td>{% include i18n.html en="Official M3FD HOD evaluator; AP, AP50, AP75, per-class AP" zh="官方 M3FD HOD 评估器；AP、AP50、AP75、逐类 AP" %}</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</section>

<section class="project-section" id="results">
  {% include i18n.html tag="div" class="section-kicker" en="5 · Results and ablation" zh="5 · 实验结果与消融" %}
  {% include i18n.html tag="h2" en="Where adaptive fusion pays off" zh="自适应融合在哪里见效" %}
  <p class="source-line metric-line"><span class="evidence-chip">{% include i18n.html en="Metrics" zh="指标" %}</span> {% include i18n.html en="<strong>AP</strong> averages precision over IoU 0.50–0.95 · <strong>AP50</strong> counts a box at IoU ≥ 0.50 · <strong>AP75</strong> requires IoU ≥ 0.75, i.e. tighter boxes." zh="<strong>AP</strong>：IoU 0.50–0.95 上的平均精度 · <strong>AP50</strong>：IoU ≥ 0.50 即计入 · <strong>AP75</strong>：IoU ≥ 0.75 才计入，即框更准。" %}</p>

  {% include i18n.html tag="h3" class="mt-4" en="Result 1 — Dynamic gating wins on hard scenes" zh="结果 1 — 困难场景中动态门控胜出" %}
  {% include i18n.html tag="p" class="section-intro" en="When visual conditions make the two modalities uneven, the dynamic gate beats equal fusion on every headline metric, with the largest gain on tight, high-IoU boxes." zh="当视觉条件让两种模态质量不均时，动态门控在全部主要指标上超过等权融合，其中高 IoU 的精确定位提升最大。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/challenge-scenes.svg' | relative_url }}" alt="Bar charts of AP, AP50, and AP75 for equal fusion versus dynamic weighting on the challenge subset" data-alt-en="Bar charts of AP, AP50, and AP75 for equal fusion versus dynamic weighting on the challenge subset" data-alt-zh="挑战子集上等权融合与动态加权的 AP、AP50、AP75 柱状图" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="AP75" zh="AP75" %}<strong>+5.09</strong><small>80.18 → 85.27</small></div>
    <div>{% include i18n.html tag="span" en="AP50" zh="AP50" %}<strong>+1.60</strong><small>94.83 → 96.43</small></div>
    <div>{% include i18n.html tag="span" en="AP" zh="AP" %}<strong>+0.79</strong><small>70.91 → 71.70</small></div>
    <div>{% include i18n.html tag="span" en="Motorcycle AP" zh="摩托车 AP" %}<strong>+8.86</strong><small>59.60 → 68.47</small></div>
  </div>
  <p class="source-line"><span class="evidence-chip">{% include i18n.html en="Protocol" zh="协议" %}</span> {% include i18n.html en="<strong>Both methods were fine-tuned from the same multimodal checkpoint on 361 challenge-training images and evaluated on 138 challenge-test images.</strong> The subset is built automatically from brightness, contrast, entropy, haze, and low-light signals." zh="<strong>两种方法从同一多模态检查点出发，在 361 张挑战训练图上微调，并在 138 张挑战测试图上评估。</strong>子集根据亮度、对比度、熵、雾霾和低光信号自动构造。" %}</p>

  {% include i18n.html tag="h3" class="mt-5" en="Result 2 — Two modalities beat one" zh="结果 2 — 双模态显著优于单模态" %}
  {% include i18n.html tag="p" class="section-intro" en="On the full M3FD test set, combining RGB and infrared lifts AP by 4.5 over visible-only and by 11.0 over infrared-only, and two independent seeds agree within 0.33 AP." zh="在完整 M3FD 测试集上，RGB 与红外结合比仅可见光高 4.5 AP，比仅红外高 11.0 AP，两个独立种子相差不超过 0.33 AP。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/multimodal-advantage.svg' | relative_url }}" alt="Bar chart comparing visible-only, infrared-only, and two multimodal seeds" data-alt-en="Bar chart comparing visible-only, infrared-only, and two multimodal seeds" data-alt-zh="可见光、红外与两个多模态种子的 AP 柱状图" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="Visible" zh="可见光" %}<strong>48.66</strong><small>AP</small></div>
    <div>{% include i18n.html tag="span" en="Infrared" zh="红外" %}<strong>42.20</strong><small>AP</small></div>
    <div>{% include i18n.html tag="span" en="Multimodal seed 1" zh="多模态种子 1" %}<strong>53.19</strong><small>AP</small></div>
    <div>{% include i18n.html tag="span" en="Multimodal seed 2" zh="多模态种子 2" %}<strong>53.52</strong><small>AP</small></div>
  </div>

  {% include i18n.html tag="h3" class="mt-5" en="Result 3 — Full-benchmark ablation" zh="结果 3 — 完整测试集消融" %}
  {% include i18n.html tag="p" class="section-intro" en="On the full benchmark, where most scenes are easy, the strong default fusion (53.19 AP) stays on top and the dynamic gate reaches 52.92 AP. Adaptive weighting matters most when modality quality becomes uneven, which motivates more explicit supervision of modality utility." zh="在以普通场景为主的完整测试集上，较强的默认融合（53.19 AP）仍然最好，动态门控为 52.92 AP。自适应加权主要在模态质量不均时发挥作用，这也促使我进一步研究更明确的模态效用监督。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/fusion-ablation.svg' | relative_url }}" alt="Horizontal bar chart of default multimodal fusion versus static and gated alternatives" data-alt-en="Horizontal bar chart of default multimodal fusion versus static and gated alternatives" data-alt-zh="默认多模态融合与静态、门控方案的水平柱状图" loading="lazy">
  </figure>
  <details class="technical-details result-table-details mt-3">
    <summary>{% include i18n.html en="Exact full-benchmark AP values" zh="完整测试集 AP 精确值" %}</summary>
    <div class="table-responsive">
      <table class="table technical-table">
        <thead><tr><th>{% include i18n.html en="Method" zh="方法" %}</th><th>AP</th><th>AP50</th></tr></thead>
        <tbody>
          <tr class="table-emphasis"><td>{% include i18n.html en="Default multimodal" zh="默认多模态" %}</td><td>53.19</td><td>82.37</td></tr>
          <tr><td>{% include i18n.html en="Static 0.25" zh="静态 0.25" %}</td><td>52.19</td><td>80.86</td></tr>
          <tr><td>{% include i18n.html en="Static 0.50" zh="静态 0.50" %}</td><td>52.82</td><td>82.03</td></tr>
          <tr><td>{% include i18n.html en="Static 0.75" zh="静态 0.75" %}</td><td>52.82</td><td>81.92</td></tr>
          <tr><td>{% include i18n.html en="Dynamic gate" zh="动态门控" %}</td><td>52.92</td><td>81.55</td></tr>
          <tr><td>{% include i18n.html en="Residual gate" zh="残差门控" %}</td><td>53.19</td><td>82.25</td></tr>
        </tbody>
      </table>
    </div>
  </details>

  {% include i18n.html tag="h3" class="mt-5" en="Result 4 — What the gate learned" zh="结果 4 — 门控学到了什么" %}
  {% include i18n.html tag="p" class="section-intro" en="The learned weights are structured, not random: p2 leans towards infrared, p3 towards visible, and p4 / p5 stay closer to balanced." zh="学到的权重有结构而非随机：p2 偏红外，p3 偏可见光，p4 / p5 更接近平衡。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/infrared-visible/modality-preference.png' | relative_url }}" alt="Feature-pyramid diagram showing infrared-leaning p2, visible-leaning p3, and more balanced p4 and p5" data-alt-en="Feature-pyramid diagram showing infrared-leaning p2, visible-leaning p3, and more balanced p4 and p5" data-alt-zh="特征金字塔：p2 更偏红外，p3 更偏可见光，p4 与 p5 更接近平衡" loading="lazy">
  </figure>
  <div class="tradeoff-callout mt-3">
    {% include i18n.html en="<strong>Different feature levels learned different modality preferences, motivating more targeted supervision of modality contribution.</strong>" zh="<strong>不同特征层学到了不同的模态偏好，这促使我对模态贡献做更有针对性的监督。</strong>" %}
  </div>
</section>

<section class="project-section" id="qualitative-demo">
  {% include i18n.html tag="div" class="section-kicker" en="6 · Qualitative demo" zh="6 · 定性示例" %}
  {% include i18n.html tag="h2" en="Aligned inputs and detector comparison" zh="对齐输入与检测器对比" %}
  <div data-rgbir-demo='{{ site.data.rgbir_demo.cases | jsonify }}' data-rgbir-initial="low-light">
    <div class="rgbir-demo-tabs" role="tablist" aria-label="Scene condition">
      {% for item in site.data.rgbir_demo.cases %}
      {% assign demo_case_id = item[0] %}
      {% assign demo_case = item[1] %}
      <button type="button" data-rgbir-case="{{ demo_case_id }}" aria-pressed="{% if demo_case_id == 'low-light' %}true{% else %}false{% endif %}">{% include i18n.html en=demo_case.label zh=demo_case.label_zh %}</button>
      {% endfor %}
    </div>
    {% include i18n.html tag="div" class="rgbir-demo-row-label" en="Inputs" zh="输入" %}
    <div class="rgbir-demo-grid" data-rgbir-row>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-visible" en="RGB input + ground truth" zh="RGB 输入 + 真值框" %}
        <div data-rgbir-pane="visible">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-infrared" en="Aligned infrared input" zh="对齐的红外输入" %}
        <div data-rgbir-pane="infrared">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
    </div>
    {% include i18n.html tag="div" class="rgbir-demo-row-label" en="Detector predictions" zh="检测器预测" %}
    <div class="rgbir-demo-grid" data-rgbir-row>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-equal" en="Equal-fusion detector" zh="等权融合检测器" %}
        <div data-rgbir-pane="equal">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
      <figure>
        {% include i18n.html tag="span" class="plate-label plate-dynamic" en="Dynamic-gating detector" zh="动态门控检测器" %}
        <div data-rgbir-pane="dynamic">
          <img alt="" loading="lazy" hidden>
          <div class="rgbir-empty" data-empty hidden></div>
          <div class="rgbir-stats" data-stats hidden></div>
        </div>
      </figure>
    </div>
    <p class="rgbir-demo-note mt-3" data-rgbir-note></p>
  </div>
</section>

<section class="project-section" id="next">
  {% include i18n.html tag="div" class="section-kicker" en="7 · Next" zh="7 · 后续研究" %}
  <div class="future-card">
    <div class="future-card-meta">
      <span class="evidence-chip">{% include i18n.html en="Planned research" zh="计划中的研究" %}</span>
      <span class="future-venue">{% include i18n.html en="Target venue: Information Fusion" zh="目标期刊：Information Fusion" %}</span>
    </div>
    {% include i18n.html tag="h2" en="Next: object-level modality utility supervision" zh="下一步：对象级模态效用监督" %}
    {% include i18n.html tag="p" en="The current lightweight gate learns modality preferences per feature level. Next, I plan to study object-level modality utility: measure how the classification and localisation losses of the same object change when one modality is removed or attenuated, and use those changes to supervise a spatial gate. The experiments will isolate the contributions of utility supervision, object-level granularity, and degradation training, while tracking both detection gains and inference cost." zh="当前轻量门控学习的是不同特征层的模态偏好。下一步，我计划研究对象级模态效用：比较移除或削弱某一路后，同一目标的分类和定位损失如何变化，并用这些变化监督空间门控。实验将分别验证效用监督、对象级粒度和退化训练的贡献，同时评估检测收益与推理开销。" %}
    <ul class="future-list">
      <li>{% include i18n.html en="Original gate vs utility-supervised gate." zh="原门控与效用监督门控的对照。" %}</li>
      <li>{% include i18n.html en="Concatenation, standard attention, and the new method under identical settings." zh="拼接、普通注意力与新方法的同条件比较。" %}</li>
      <li>{% include i18n.html en="Normal scenes and single-modality degradation tests." zh="正常场景与单模态退化测试。" %}</li>
      <li>{% include i18n.html en="Multiple datasets, multiple seeds, and latency evaluation." zh="多数据集、多种子及延迟评估。" %}</li>
    </ul>
  </div>
</section>
