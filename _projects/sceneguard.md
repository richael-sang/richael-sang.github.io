---
layout: project
title: SceneGuard
subtitle: Training-Time Voice Protection with Scene-Consistent Audible Background Noise
subtitle_zh: 用场景一致的可听背景噪声进行训练时语音保护
date: 2026-01-26 00:01:00 +0800
category: research
selected: true
detail_page: true
permalink: /projects/sceneguard/
advanced_project: true
bilingual: true
project_page_style: true
project_page_script: true
project_type: Voice Privacy · Audio ML
description: SceneGuard is a scene-conditioned audio protection pipeline that optimizes a temporal noise mask and gain to reduce speaker-identity similarity while preserving intelligibility.
citation_title: "SceneGuard: Training-Time Voice Protection with Scene-Consistent Audible Background Noise"
citation_publication_date: "2026-01-26"
paper_url: https://arxiv.org/pdf/2511.16114
og_type: article
og_image: /assets/images/projects/sceneguard/concept-overview.png
cover: /assets/images/projects/sceneguard/concept-overview.png
cover_fit: contain
hero_figure: /assets/images/projects/sceneguard/concept-overview.png
hero_figure_alt: Three-step SceneGuard concept showing original speech, scene-matched protection, and useful speech with reduced voice-cloning risk
hero_figure_alt_zh: SceneGuard 三步概念：原始语音、场景匹配保护、以及更难克隆但仍可懂的语音
pub: "AAAI-26 Workshop on Artificial Intelligence for Cyber Security (AICS)"
pub_date: "Accepted"
pub_date_zh: "已接收"
pub_last: "· First author"
pub_last_zh: "· 第一作者"
abstract: >-
  SceneGuard protects published speech by adding scene-matched audible noise whose timing and strength are optimized to reduce speaker-identity similarity while preserving intelligibility.
abstract_zh: >-
  SceneGuard 通过添加与录音场景匹配的可听噪声来保护已发布语音；噪声的时序与强度经过优化，以降低说话人身份相似度，同时尽量保持可懂度。
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
    label_zh: 音频演示
links:
  Paper: https://arxiv.org/pdf/2511.16114
  Code: https://github.com/richael-sang/SceneGuard
section_nav:
- id: overview
  label: Overview
  label_zh: 概览
- id: audio-demo
  label: Audio
  label_zh: 音频
- id: system-architecture
  label: Method
  label_zh: 方法
- id: main-results
  label: Results
  label_zh: 结果
- id: implementation
  label: Implementation
  label_zh: 实现
- id: limitations
  label: Limitations
  label_zh: 局限
---

<section class="project-section" id="overview">
  {% include i18n.html tag="div" class="section-kicker" en="30-second overview" zh="30 秒概览" %}
  {% include i18n.html tag="h2" en="What SceneGuard does" zh="SceneGuard 做什么" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Input" zh="输入" %}
      {% include i18n.html tag="h3" en="Speech + scene context" zh="语音 + 场景上下文" %}
      {% include i18n.html tag="p" en="Speech \(x(t)\), an acoustic scene \(s\), and a scene-specific noise library \(\mathcal{N}_s\)." zh="语音 \(x(t)\)、声学场景 \(s\)，以及该场景对应的噪声库 \(\mathcal{N}_s\)。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Output" zh="输出" %}
      {% include i18n.html tag="h3" en="Protected speech" zh="受保护语音" %}
      {% include i18n.html tag="p" en="An audio signal \(x'(t)\) containing audible noise selected to match the recording context." zh="带有可听噪声的音频信号 \(x'(t)\)，噪声按录音场景选取。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Goal" zh="目标" %}
      {% include i18n.html tag="h3" en="Reduce speaker identity" zh="降低说话人身份信息" %}
      {% include i18n.html tag="p" en="Lower ECAPA speaker similarity while retaining speech intelligibility and practical usability." zh="降低 ECAPA 说话人相似度，同时尽量保持可懂度与可用性。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Core idea" zh="核心思路" %}
      {% include i18n.html tag="h3" en="Optimize placement + strength" zh="优化投放位置与强度" %}
      {% include i18n.html tag="p" en="Learn a temporal mask \(m(t)\) and global gain \(\gamma\) for a scene-matched noise sample." zh="为场景匹配噪声学习时间掩码 \(m(t)\) 与全局增益 \(\gamma\)。" %}
    </div>
  </div>
  <div class="evidence-note mt-3">
    {% include i18n.html tag="strong" en="Method in one line:" zh="一句话方法：" %}
    {% include i18n.html en="SceneGuard is a scene-conditioned audio protection pipeline with per-sample gradient-based mask and gain optimization—not a newly trained neural-network architecture." zh="SceneGuard 是按样本优化掩码与增益的场景条件音频保护流程，而不是新训练的神经网络架构。" %}
  </div>
</section>

<section class="project-section" id="audio-demo">
  {% include i18n.html tag="div" class="section-kicker" en="Interactive evidence" zh="交互证据" %}
  {% include i18n.html tag="h2" en="Audio demo" zh="音频演示" %}
  {% include i18n.html tag="p" class="section-intro" en="The comparison interface is ready for curated Clean / Baseline / SceneGuard samples, with matching waveforms and mel spectrograms." zh="对比界面已预留 Clean / Baseline / SceneGuard 样本位置，并配套波形图与 Mel 频谱。" %}
  {% include widgets/project_audio_matrix.html demo=site.data.sceneguard_audio %}
  <div class="evidence-note mt-3">
    {% include i18n.html en="No audio is embedded yet. The public repository contains no WAV examples, and the TAU noise dataset has non-commercial redistribution restrictions. No synthetic or untraceable sample has been substituted." zh="目前尚未嵌入音频。公开仓库没有 WAV 样例，且 TAU 噪声数据有非商业再分发限制。这里没有用无法追溯来源的合成样本代替。" %}
  </div>
</section>

<section class="project-section" id="threat-model">
  {% include i18n.html tag="div" class="section-kicker" en="Problem & threat model" zh="问题与威胁模型" %}
  {% include i18n.html tag="h2" en="Protecting speech before an attacker collects it" zh="在攻击者收集之前保护语音" %}
  <div class="threat-flow" role="img" aria-label="A user publishes protected speech, an attacker collects it, and attempts voice cloning">
    <div class="flow-node"><i class="fas fa-microphone" aria-hidden="true"></i>{% include i18n.html tag="strong" en="User publishes speech" zh="用户发布语音" %}{% include i18n.html tag="span" en="Protection is applied before release" zh="保护在发布前完成" %}</div>
    <div class="flow-arrow" aria-hidden="true">→</div>
    <div class="flow-node"><i class="fas fa-download" aria-hidden="true"></i>{% include i18n.html tag="strong" en="Attacker collects audio" zh="攻击者收集音频" %}{% include i18n.html tag="span" en="Black-box attacker does not know the defense" zh="黑盒攻击者不知道防御机制" %}</div>
    <div class="flow-arrow" aria-hidden="true">→</div>
    <div class="flow-node"><i class="fas fa-user-secret" aria-hidden="true"></i>{% include i18n.html tag="strong" en="Voice-cloning attempt" zh="尝试语音克隆" %}{% include i18n.html tag="span" en="Training-time or zero-shot use" zh="训练时或 zero-shot 使用" %}</div>
  </div>
  <div class="comparison-grid mt-4">
    <div class="comparison-card">
      {% include i18n.html tag="div" class="comparison-label" en="Conventional paradigm" zh="常见范式" %}
      {% include i18n.html tag="h3" en="Imperceptible perturbation" zh="不可感知扰动" %}
      {% include i18n.html tag="p" en="Prior proactive defenses often constrain perturbations to be difficult to hear, but such low-energy signals may be vulnerable to compression, filtering, or purification." zh="已有主动防御常把扰动限制为难以听见，但这类低能量信号可能容易被压缩、滤波或净化去掉。" %}
    </div>
    <div class="comparison-card comparison-card-accent">
      {% include i18n.html tag="div" class="comparison-label" en="SceneGuard design choice" zh="SceneGuard 的设计选择" %}
      {% include i18n.html tag="h3" en="Scene-matched audible protection" zh="场景匹配的可听保护" %}
      {% include i18n.html tag="p" en="SceneGuard trades strict imperceptibility for context-aware noise selection and tests whether protection persists under common preprocessing operations." zh="SceneGuard 用场景感知的噪声选择换取不再追求严格不可听，并检验保护是否能在常见预处理后仍然有效。" %}
    </div>
  </div>
  <p class="source-line"><span class="evidence-chip">Paper-described threat model</span> {% include i18n.html en="Full end-to-end BERT-VITS2 fine-tuning was not performed because of computational constraints; speaker-embedding degradation is used as a proxy, complemented by a zero-shot evaluation." zh="因计算资源限制，未做完整端到端 BERT-VITS2 微调；说话人嵌入退化作为代理指标，并辅以 zero-shot 评估。" %}</p>
</section>

<section class="project-section" id="input-output">
  {% include i18n.html tag="div" class="section-kicker" en="Signal transformation" zh="信号变换" %}
  {% include i18n.html tag="h2" en="Input → output" zh="输入 → 输出" %}
  <div class="equation-panel">
    $$x'(t) = x(t) + \gamma\,m(t)\odot n_k(t), \qquad n_k(t)\sim\mathcal{N}_s$$
  </div>
  <div class="symbol-grid">
    <div><code>x(t)</code>{% include i18n.html tag="span" en="clean input speech" zh="干净输入语音" %}</div>
    <div><code>s</code>{% include i18n.html tag="span" en="predicted or user-provided scene" zh="预测或用户指定的场景" %}</div>
    <div><code>n_k(t)</code>{% include i18n.html tag="span" en="noise sampled from the scene library" zh="从场景噪声库采样的噪声" %}</div>
    <div><code>m(t)</code>{% include i18n.html tag="span" en="temporal mask in \([0,1]^T\)" zh="时间掩码，取值 \([0,1]^T\)" %}</div>
    <div><code>γ</code>{% include i18n.html tag="span" en="global noise strength" zh="全局噪声强度" %}</div>
    <div><code>x'(t)</code>{% include i18n.html tag="span" en="protected speech output" zh="受保护语音输出" %}</div>
  </div>
</section>

<section class="project-section" id="system-architecture">
  {% include i18n.html tag="div" class="section-kicker" en="System architecture" zh="系统架构" %}
  {% include i18n.html tag="h2" en="Pretrained perception, per-sample optimization" zh="预训练感知模块，按样本优化" %}
  {% include i18n.html tag="p" class="section-intro" en="PANNs, ECAPA-TDNN, and Whisper are pretrained components. SceneGuard does not train them; gradients update only the temporal mask and global gain for each sample." zh="PANNs、ECAPA-TDNN 和 Whisper 都是预训练组件。SceneGuard 不训练它们；梯度只更新每个样本的时间掩码与全局增益。" %}
  <figure class="technical-figure technical-figure-borderless">
    <img src="{{ '/assets/images/projects/sceneguard/sceneguard.png' | relative_url }}" alt="SceneGuard architecture showing scene and noise selection, mask and gain optimization, protected speech generation, usability and robustness evaluation, and training-time and zero-shot attacks" data-alt-en="SceneGuard architecture showing scene and noise selection, mask and gain optimization, protected speech generation, usability and robustness evaluation, and training-time and zero-shot attacks" data-alt-zh="SceneGuard 架构：场景与噪声选择、掩码与增益优化、受保护语音生成，以及可用性、鲁棒性、训练时与 zero-shot 评估" loading="lazy">
  </figure>
</section>

<section class="project-section" id="why-optimization">
  {% include i18n.html tag="div" class="section-kicker" en="Ablation" zh="消融" %}
  {% include i18n.html tag="h2" en="Why optimize the mixture?" zh="为什么要优化混合过程？" %}
  <div class="comparison-grid">
    <div class="comparison-card">
      {% include i18n.html tag="div" class="comparison-label" en="Direct mixing" zh="直接混合" %}
      {% include i18n.html tag="h3" en="Fixed / unoptimized placement" zh="固定、未优化的投放" %}
      <div class="metric-large">2.8%</div>
      {% include i18n.html tag="div" class="metric-caption" en="paper-reported protection" zh="论文报告的保护强度" %}
      <div class="mini-bar"><span style="width: 35%"></span></div>
      <p>SIM 0.972 · STOI 0.989 · WER 3.2%</p>
    </div>
    <div class="comparison-card comparison-card-accent">
      <div class="comparison-label">SceneGuard</div>
      {% include i18n.html tag="h3" en="Learned mask + constrained gain" zh="学习掩码 + 受约束增益" %}
      <div class="metric-large">5.5%</div>
      {% include i18n.html tag="div" class="metric-caption" en="paper-reported protection" zh="论文报告的保护强度" %}
      <div class="mini-bar"><span style="width: 69%"></span></div>
      <p>SIM 0.945 · STOI 0.986 · WER 3.6%</p>
    </div>
  </div>
  <p class="source-line"><span class="evidence-chip">Paper Table 6</span> {% include i18n.html en="Optimization improves reported similarity degradation by 2.7 percentage points under the same SNR constraint, with a 0.003 STOI decrease and 0.4-point WER increase." zh="在相同 SNR 约束下，优化使报告的相似度下降提高 2.7 个百分点；STOI 仅下降 0.003，WER 上升 0.4 个百分点。" %}</p>
</section>

<section class="project-section" id="objective">
  {% include i18n.html tag="div" class="section-kicker" en="Optimization objective" zh="优化目标" %}
  {% include i18n.html tag="h2" en="What is actually optimized?" zh="实际优化了什么？" %}
  <div class="equation-panel">
    $$\mathcal{L}_{\mathrm{default}} =
    \lambda_{\mathrm{SIM}}\,\mathrm{cos}\!\left(e(x'),e(x)\right)
    + \lambda_{\mathrm{REG}}\left(\|\nabla m\|_2^2+\gamma^2\right)$$
    $$\text{subject to}\quad \mathrm{SNR}\!\left(x,\gamma m\odot n_k\right)\in[10,20]\ \mathrm{dB}$$
  </div>
  <div class="objective-list">
    <div>{% include i18n.html tag="strong" en="Speaker similarity" zh="说话人相似度" %}{% include i18n.html tag="span" en="Minimize cosine similarity between clean and protected ECAPA embeddings." zh="最小化干净语音与受保护语音 ECAPA 嵌入的余弦相似度。" %}</div>
    <div>{% include i18n.html tag="strong" en="Mask smoothness" zh="掩码平滑" %}{% include i18n.html tag="span" en="Penalize abrupt temporal changes that may create unstable or spiky masks." zh="惩罚可能导致掩码尖峰或不稳定的剧烈时间变化。" %}</div>
    <div>{% include i18n.html tag="strong" en="Energy penalty" zh="能量惩罚" %}{% include i18n.html tag="span" en="Regularize the global noise strength \(\gamma\)." zh="对全局噪声强度 \(\gamma\) 做正则。" %}</div>
    <div>{% include i18n.html tag="strong" en="SNR constraint" zh="SNR 约束" %}{% include i18n.html tag="span" en="Bound the paper’s default operating range to 10–20 dB." zh="将论文默认工作区间限制在 10–20 dB。" %}</div>
  </div>
  <details class="technical-details mt-3">
    <summary>{% include i18n.html en="General paper formulation and disabled terms" zh="论文一般形式与默认关闭项" %}</summary>
    <div class="equation-panel equation-panel-secondary">
      $$\mathcal{L}=\lambda_{\mathrm{SIM}}\mathcal{L}_{\mathrm{SIM}}
      +\lambda_{\mathrm{REG}}\mathcal{L}_{\mathrm{REG}}
      +\lambda_{\mathrm{ASR}}\mathcal{L}_{\mathrm{ASR}}
      +\lambda_{\mathrm{SCN}}\mathcal{L}_{\mathrm{SCN}}$$
    </div>
    {% include i18n.html tag="p" en="In the default experiments, \(\lambda_{\mathrm{ASR}}=0\) and \(\lambda_{\mathrm{SCN}}=0\). Scene consistency is introduced mainly by selecting noise from the scene-specific library; usability is enforced primarily through SNR and evaluated after optimization." zh="默认实验中 \(\lambda_{\mathrm{ASR}}=0\)、\(\lambda_{\mathrm{SCN}}=0\)。场景一致性主要靠从对应噪声库取样来引入；可用性主要靠 SNR 约束保证，并在优化后评估。" %}
  </details>
</section>

<section class="project-section" id="evaluation">
  {% include i18n.html tag="div" class="section-kicker" en="Evaluation framework" zh="评估框架" %}
  {% include i18n.html tag="h2" en="Four views of the protection–quality trade-off" zh="保护与质量权衡的四个视角" %}
  <div class="evaluation-grid">
    <div class="evaluation-card"><i class="fas fa-user-shield" aria-hidden="true"></i>{% include i18n.html tag="h3" en="Protection" zh="保护效果" %}<p><strong>Speaker Similarity (SIM) ↓</strong><br>{% include i18n.html en="Cosine similarity between speaker embeddings." zh="说话人嵌入之间的余弦相似度。" %}</p></div>
    <div class="evaluation-card"><i class="fas fa-comment-dots" aria-hidden="true"></i>{% include i18n.html tag="h3" en="Usability" zh="可用性" %}<p><strong>WER ↓ · STOI ↑ · PESQ ↑</strong><br>{% include i18n.html en="Transcription, intelligibility, and objective quality." zh="转写、可懂度与客观音质。" %}</p></div>
    <div class="evaluation-card"><i class="fas fa-filter" aria-hidden="true"></i>{% include i18n.html tag="h3" en="Robustness" zh="鲁棒性" %}<p><strong>SIM after preprocessing</strong><br>{% include i18n.html en="MP3, spectral subtraction, low-pass, and downsampling." zh="MP3、谱减、低通与降采样。" %}</p></div>
    <div class="evaluation-card"><i class="fas fa-bolt" aria-hidden="true"></i><h3>Zero-shot</h3><p><strong>SIM + success rate ↓</strong><br>{% include i18n.html en="Cloning with clean versus protected reference audio." zh="分别用干净参考与受保护参考做克隆。" %}</p></div>
  </div>
</section>

<section class="project-section" id="main-results">
  {% include i18n.html tag="div" class="section-kicker" en="Paper-reported results" zh="论文报告结果" %}
  {% include i18n.html tag="h2" en="Main comparison" zh="主要对比" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/sceneguard/main-results.svg' | relative_url }}" alt="Comparison of speaker similarity and word error rate for clean data, random noise, Gaussian noise, and SceneGuard" data-alt-en="Comparison of speaker similarity and word error rate for clean data, random noise, Gaussian noise, and SceneGuard" data-alt-zh="Clean、随机噪声、高斯噪声与 SceneGuard 在说话人相似度和词错误率上的对比" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div><span>SIM</span><strong>1.000 → 0.945</strong>{% include i18n.html tag="small" en="training-attack proxy comparison" zh="训练攻击代理对比" %}</div>
    <div><span>STOI</span><strong>0.986</strong><small>95% CI [0.980, 0.992]</small></div>
    <div><span>WER</span><strong>3.60%</strong>{% include i18n.html tag="small" en="usability evaluation" zh="可用性评估" %}</div>
    <div><span>Effect size</span><strong>2.18</strong>{% include i18n.html tag="small" en="Cohen’s d; paper reports p &lt; 10<sup>−15</sup>" zh="Cohen’s d；论文报告 p &lt; 10<sup>−15</sup>" %}</div>
  </div>
  <details class="technical-details result-table-details mt-4">
    <summary>{% include i18n.html en="View exact values from Paper Table 1" zh="查看 Paper Table 1 精确数值" %}</summary>
    <div class="table-responsive">
      <table class="table technical-table">
        <thead><tr><th>{% include i18n.html en="Training data" zh="训练数据" %}</th><th>SIM ↓</th><th>WER (%) ↓</th><th>PESQ ↑</th><th>STOI ↑</th></tr></thead>
        <tbody>
          <tr><td>Clean</td><td>1.000</td><td>0.00</td><td>4.64</td><td>1.00</td></tr>
          <tr><td>Random noise</td><td>0.965</td><td>5.82</td><td>1.85</td><td>0.97</td></tr>
          <tr><td>Gaussian noise</td><td>0.968</td><td>5.28</td><td>1.92</td><td>0.98</td></tr>
          <tr class="table-emphasis"><td>SceneGuard</td><td>0.945</td><td>2.77</td><td>2.22</td><td>0.99</td></tr>
        </tbody>
      </table>
    </div>
  </details>
  <div class="tradeoff-callout">
    {% include i18n.html tag="strong" en="Visible trade-off:" zh="可见权衡：" %}
    {% include i18n.html en="the separate usability evaluation reports PESQ 2.034 (95% CI [1.840, 2.233]), below the paper’s stated ideal threshold of 3.0. SceneGuard preserves high measured intelligibility, but not pristine perceptual quality." zh="单独的可用性评估报告 PESQ 为 2.034（95% CI [1.840, 2.233]），低于论文给出的理想阈值 3.0。SceneGuard 保持了较高的可懂度，但不是接近无损的感知音质。" %}
  </div>
  <p class="source-line"><span class="evidence-chip">Paper Tables 1–2</span> {% include i18n.html en="Table 1 reports WER 2.77% and PESQ 2.22; the separate usability summary reports WER 3.60% and PESQ 2.034. The paper does not document why the summaries differ, so they are shown separately." zh="Table 1 报告 WER 2.77%、PESQ 2.22；单独的可用性摘要报告 WER 3.60%、PESQ 2.034。论文未说明两组摘要为何不同，因此分开展示。" %}</p>
</section>

<section class="project-section" id="snr-explorer">
  {% include i18n.html tag="div" class="section-kicker" en="Interactive ablation" zh="交互消融" %}
  {% include i18n.html tag="h2" en="SNR trade-off explorer" zh="SNR 权衡查看器" %}
  {% include i18n.html tag="p" class="section-intro" en="Move across the four precomputed settings to inspect the reported protection–usability balance." zh="在四个预计算结果之间切换，查看论文报告的保护与可用性权衡。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/sceneguard/snr-tradeoff.svg' | relative_url }}" alt="SNR ablation showing that lower SNR increases protection but reduces STOI and increases word error rate" data-alt-en="SNR ablation showing that lower SNR increases protection but reduces STOI and increases word error rate" data-alt-zh="SNR 消融：更低 SNR 增强保护，但会降低 STOI 并提高词错误率" loading="lazy">
  </figure>
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
      <div>{% include i18n.html tag="span" en="Protection" zh="保护强度" %}<strong data-snr-protection>5.5%</strong></div>
      <div><span>SIM ↓</span><strong data-snr-sim>0.945</strong></div>
      <div><span>STOI ↑</span><strong data-snr-stoi>0.986</strong></div>
      <div><span>WER ↓</span><strong data-snr-wer>3.6%</strong></div>
    </div>
    <p class="small text-muted mb-0" id="snr-explorer-note">{% include i18n.html en="Visualization of paper-reported, precomputed ablation results—no model inference runs in the browser." zh="这是论文报告的预计算消融可视化，浏览器中不运行模型推理。" %}</p>
  </div>
</section>

<section class="project-section" id="robustness-explorer">
  {% include i18n.html tag="div" class="section-kicker" en="Preprocessing robustness" zh="预处理鲁棒性" %}
  {% include i18n.html tag="h2" en="Protection after common preprocessing" zh="常见预处理后的保护效果" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/sceneguard/robustness-results.svg' | relative_url }}" alt="Horizontal bar chart of speaker similarity after MP3 compression, spectral subtraction, low-pass filtering, and downsampling" data-alt-en="Horizontal bar chart of speaker similarity after MP3 compression, spectral subtraction, low-pass filtering, and downsampling" data-alt-zh="MP3 压缩、谱减、低通滤波与降采样后的说话人相似度条形图" loading="lazy">
  </figure>
  <p class="source-line"><span class="evidence-chip">Paper Table 3</span> {% include i18n.html en="Lower SIM indicates greater speaker-identity degradation. The public repository does not contain the per-sample files needed for independent recomputation." zh="更低的 SIM 表示说话人身份退化更强。公开仓库目前没有可供独立复算的逐样本文件。" %}</p>
</section>

<section class="project-section" id="zero-shot">
  {% include i18n.html tag="div" class="section-kicker" en="Zero-shot evaluation" zh="Zero-shot 评估" %}
  {% include i18n.html tag="h2" en="Protected reference audio lowers reported cloning similarity" zh="受保护参考音频会降低报告的克隆相似度" %}
  <div class="zero-shot-grid">
    <div class="zero-shot-card">{% include i18n.html tag="span" en="Clean reference" zh="干净参考" %}<strong>SIM 0.618</strong>{% include i18n.html tag="small" en="Attack success rate 20.0%" zh="攻击成功率 20.0%" %}</div>
    <div class="zero-shot-arrow" aria-hidden="true">→</div>
    <div class="zero-shot-card zero-shot-card-accent">{% include i18n.html tag="span" en="SceneGuard reference" zh="SceneGuard 参考" %}<strong>SIM 0.588</strong>{% include i18n.html tag="small" en="Attack success rate 13.3%" zh="攻击成功率 13.3%" %}</div>
  </div>
  <p class="source-line"><span class="evidence-chip">Paper Table 4</span> {% include i18n.html en="No publishable zero-shot synthesized audio or raw result file is present in the public repository, so this section reports metrics only." zh="公开仓库没有可发布的 zero-shot 合成音频或原始结果文件，因此本节只报告指标。" %}</p>
</section>

<section class="project-section" id="implementation">
  {% include i18n.html tag="div" class="section-kicker" en="Engineering view" zh="工程细节" %}
  {% include i18n.html tag="h2" en="Implementation details" zh="实现细节" %}
  <div class="table-responsive">
    <table class="table technical-table implementation-table">
      <tbody>
        <tr><th>{% include i18n.html en="Scene classifier" zh="场景分类器" %}</th><td>PANNs CNN14, pretrained on AudioSet</td></tr>
        <tr><th>{% include i18n.html en="Speaker encoder" zh="说话人编码器" %}</th><td>ECAPA-TDNN, 192-dimensional embeddings</td></tr>
        <tr><th>{% include i18n.html en="ASR evaluator" zh="ASR 评估器" %}</th><td>Whisper Base</td></tr>
        <tr><th>{% include i18n.html en="Referenced TTS architecture" zh="参考 TTS 架构" %}</th><td>{% include i18n.html en="BERT-VITS2; no full fine-tuning in the workshop experiment" zh="BERT-VITS2；workshop 实验中未做完整微调" %}</td></tr>
        <tr><th>{% include i18n.html en="Optimizer" zh="优化器" %}</th><td>Adam, learning rate 0.01</td></tr>
        <tr><th>{% include i18n.html en="Default optimization" zh="默认优化设置" %}</th><td>50 epochs, gradient clipping max norm 1.0</td></tr>
        <tr><th>{% include i18n.html en="Default SNR" zh="默认 SNR" %}</th><td>10–20 dB</td></tr>
        <tr><th>{% include i18n.html en="Reported runtime" zh="报告运行时间" %}</th><td>{% include i18n.html en="Approximately 10–15 s/sample on one RTX A6000" zh="单张 RTX A6000 上约 10–15 秒/样本" %}</td></tr>
        <tr><th>{% include i18n.html en="Speech / noise data" zh="语音 / 噪声数据" %}</th><td>LibriTTS; TAU Urban Acoustic Scenes 2022</td></tr>
        <tr><th>{% include i18n.html en="Noise library" zh="噪声库" %}</th><td>{% include i18n.html en="Approximately 50,000 three-second clips across 10 scene categories" zh="约 50,000 条 3 秒片段，覆盖 10 类场景" %}</td></tr>
        <tr><th>{% include i18n.html en="Training-attack split" zh="训练攻击划分" %}</th><td>{% include i18n.html en="100 training samples and 40 test samples" zh="100 条训练样本，40 条测试样本" %}</td></tr>
      </tbody>
    </table>
  </div>
  <div class="evidence-note">
    {% include i18n.html tag="strong" en="Repository status:" zh="仓库现状：" %}
    {% include i18n.html en="the public code contains the mixer, optimizer, metrics, and helper scripts, but does not currently include result CSVs, audio samples, checkpoints, or a complete PANNs / robustness / zero-shot reproduction pipeline." zh="公开代码包含 mixer、优化器、指标与辅助脚本，但目前没有结果 CSV、音频样本、checkpoint，也没有完整的 PANNs / 鲁棒性 / zero-shot 复现流程。" %}
  </div>
</section>

<section class="project-section" id="limitations">
  {% include i18n.html tag="div" class="section-kicker" en="Limitations" zh="局限" %}
  {% include i18n.html tag="h2" en="Evidence boundary" zh="证据边界" %}
  <div class="evidence-note">
    {% include i18n.html en="SceneGuard trades pristine audio quality for robust, audible protection (reported PESQ ≈ 2.03). The workshop evaluation uses speaker-embedding degradation as a proxy rather than full end-to-end TTS fine-tuning, and does not yet cover human listening studies or adaptive scene-aware attacks." zh="SceneGuard 用可听、更鲁棒的保护换取不再追求接近无损的音质（报告 PESQ ≈ 2.03）。workshop 评估用说话人嵌入退化作为代理，而不是完整端到端 TTS 微调，也尚未覆盖听感实验或自适应场景感知攻击。" %}
  </div>
</section>

<section class="project-section" id="reproducibility">
  {% include i18n.html tag="div" class="section-kicker" en="Reproducibility" zh="可复现性" %}
  {% include i18n.html tag="h2" en="Public pipeline" zh="公开流程" %}
  <div class="pipeline" aria-label="SceneGuard reproduction pipeline">
    {% include i18n.html tag="span" en="Build noise library" zh="构建噪声库" %}<i class="fas fa-angle-right" aria-hidden="true"></i>
    {% include i18n.html tag="span" en="Assign scene labels" zh="分配场景标签" %}<i class="fas fa-angle-right" aria-hidden="true"></i>
    {% include i18n.html tag="span" en="Generate protection" zh="生成保护" %}<i class="fas fa-angle-right" aria-hidden="true"></i>
    {% include i18n.html tag="span" en="Evaluate" zh="评估" %}
  </div>
  <div class="resource-list mt-4">
    <a href="https://github.com/richael-sang/SceneGuard" target="_blank" rel="noopener"><i class="fab fa-github" aria-hidden="true"></i><span>{% include i18n.html tag="strong" en="Source code" zh="源代码" %}{% include i18n.html tag="small" en="Public implementation and scripts" zh="公开实现与脚本" %}</span></a>
    <a href="https://github.com/richael-sang/SceneGuard/blob/main/ENVIRONMENT.yml" target="_blank" rel="noopener"><i class="fas fa-cube" aria-hidden="true"></i><span>{% include i18n.html tag="strong" en="Environment" zh="环境" %}{% include i18n.html tag="small" en="Conda dependency specification" zh="Conda 依赖说明" %}</span></a>
    <a href="https://github.com/richael-sang/SceneGuard/tree/main/scripts" target="_blank" rel="noopener"><i class="fas fa-terminal" aria-hidden="true"></i><span>{% include i18n.html tag="strong" en="Experiment scripts" zh="实验脚本" %}{% include i18n.html tag="small" en="Preparation, defense, evaluation, and figures" zh="数据准备、防御生成、评估与作图" %}</span></a>
  </div>
  <p class="source-line"><span class="evidence-chip">Evidence boundary</span> {% include i18n.html en="Paper tables are the source for the numerical results on this page. Values such as negative final speaker similarity and very low SNR variance from the README are excluded because their dataset/configuration cannot be traced to public artifacts." zh="本页数值以论文表格为准。README 中无法追溯到公开实验设置的结果（例如负的最终说话人相似度、极低 SNR 方差）未采用。" %}</p>
</section>

<section class="project-section" id="related-work">
  {% include i18n.html tag="div" class="section-kicker" en="Related work" zh="相关工作" %}
  {% include i18n.html tag="h2" en="Positioning" zh="定位" %}
  {% include i18n.html tag="p" en="SceneGuard sits alongside real-time speaker de-identification (VoiceBlock), imperceptible proactive protection (SafeSpeech), purification-aware protection research (De-AntiFake), and diffusion-based voice-cloning protection (VoiceCloak). Numerical cross-paper comparisons are intentionally omitted because threat models, datasets, cloning systems, and metrics differ." zh="SceneGuard 与实时说话人去标识（VoiceBlock）、不可感知主动保护（SafeSpeech）、面向净化的保护研究（De-AntiFake），以及基于扩散的语音克隆保护（VoiceCloak）处于同一问题脉络。由于威胁模型、数据、克隆系统和指标不同，这里不做跨论文数值对比。" %}
</section>
