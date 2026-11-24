---
layout: project
title: Multimodal SOP Inspection for Industrial Assembly Video
title_zh: 工业装配视频的多模态 SOP 检测
subtitle: VLM Evidence, Multi-frame Verification, and State-driven Scheduling
subtitle_zh: VLM 视觉证据、多帧校验与状态驱动调度
date: 2026-08-01 00:00:00 +0800
category: internship
selected: false
detail_page: true
back_to_home: true
permalink: /projects/bosch-sop/
advanced_project: true
bilingual: true
project_page_style: true
project_page_script: true
project_theme: bosch
project_type: Internship · Multimodal Video Inspection
project_type_zh: 实习项目 · 多模态视频检测
description: A vision-language-model workflow that checks whether each step of a manual assembly procedure is supported by visual evidence, and reports the exact missing screw position or label.
og_type: article
og_image: /assets/images/projects/bosch-sop/01_sop_concept.png
cover: /assets/images/projects/bosch-sop/01_sop_concept.png
cover_fit: contain
hero_figure: /assets/images/projects/bosch-sop/01_sop_concept.png
hero_figure_slot: true
hero_figure_alt: An assembly video turned into a five-step checklist, with one missing screw position flagged
hero_figure_alt_zh: 装配视频被转换为五步检查清单，其中一个缺失的螺丝位置被标出
abstract: >-
  A vision-language-model workflow that checks whether each step of a manual assembly procedure is supported by visual evidence, and reports the exact missing screw position or label instead of a single OK / NG verdict.
abstract_zh: >-
  一套基于视觉语言模型的检测工作流：逐步检查人工装配流程的每一步是否有视觉证据支持，并指出具体缺失的螺丝位置或标签，而不只给出一个 OK / NG 结论。
summary: >-
  VLM-based SOP inspection for assembly video: structured evidence, multi-frame verification, and state-driven calls.
authors:
- Rui Sang
pub: "Bosch China Software Center (BCSC), Wuxi"
pub_date: "May – Aug. 2026"
pub_date_zh: "2026 年 5 月 – 8 月"
pub_last: "· Multimodal and Machine Learning Algorithm Intern"
pub_last_zh: "· 多模态与机器学习算法实习生"
hero_links:
  Results:
    url: "#results"
    target: _self
    icon: fas fa-chart-bar
    label_zh: 结果
section_nav:
- id: background
  label: Background
  label_zh: 项目背景
- id: architecture
  label: Architecture
  label_zh: 系统架构
- id: challenges
  label: Challenges & solutions
  label_zh: 难点与方法
- id: optimisation
  label: Optimisation
  label_zh: 优化思路
- id: results
  label: Results
  label_zh: 优化结果
---

<section class="project-section" id="background">
  {% include i18n.html tag="div" class="section-kicker" en="1 · Background" zh="1 · 项目背景" %}
  {% include i18n.html tag="h2" en="A finished-looking part can still be missing a step" zh="看起来已经完成的工件，仍可能漏了一步" %}
  {% include i18n.html tag="p" class="section-intro" en="A manual assembly station follows a fixed procedure. At the end of a video the part has been carried away, yet one screw or one label may never have been installed. The goal is a per-step evidence record that says which requirement is supported and which position is missing." zh="人工装配工位遵循固定流程。视频结束时工件已经被移走，但可能有一颗螺丝或一张标签始终没有装上。目标是建立逐步的证据记录：哪项要求得到支持，哪个位置缺失。" %}
  <div class="stage-strip">
    <div class="stage-card"><b>S1</b>{% include i18n.html tag="strong" en="Place cover" zh="放置盖板" %}{% include i18n.html tag="span" en="Correct metal cover on the target workbench" zh="正确的金属盖板位于目标工作台" %}</div>
    <div class="stage-card"><b>S2</b>{% include i18n.html tag="strong" en="Black box" zh="安装黑盒" %}{% include i18n.html tag="span" en="Mounted on the upper-right of the placed cover" zh="位于已放置盖板的右上区域" %}</div>
    <div class="stage-card"><b>S3</b>{% include i18n.html tag="strong" en="Four screws" zh="四颗螺丝" %}{% include i18n.html tag="span" en="Each of four positions completed separately" zh="四个孔位分别完成" %}</div>
    <div class="stage-card"><b>S4</b>{% include i18n.html tag="strong" en="Two labels" zh="两张标签" %}{% include i18n.html tag="span" en="Center and side labels each attached" zh="center 与 side 标签分别贴附" %}</div>
    <div class="stage-card"><b>S5</b>{% include i18n.html tag="strong" en="Removal" zh="移除工件" %}{% include i18n.html tag="span" en="Cover leaves and the workbench is visible again" zh="盖板离开，工作台恢复可见" %}</div>
  </div>
  <p class="source-line"><span class="evidence-chip">{% include i18n.html en="Setup" zh="条件" %}</span> {% include i18n.html en="6 regression videos · Qwen3.5-27B-FP16 · ~1 fps sampling · output: OK / NG with the exact missing screw position or label" zh="6 条回归视频 · Qwen3.5-27B-FP16 · 约 1 fps 采样 · 输出：OK / NG 及具体缺失的螺丝位置或标签" %}</p>
  <div class="question-banner">{% include i18n.html en="Reaching the next step does not mean the previous step passed." zh="进入下一步，不代表上一步已经合格。" %}</div>
</section>

<section class="project-section" id="architecture">
  {% include i18n.html tag="div" class="section-kicker" en="2 · System architecture" zh="2 · 系统架构" %}
  {% include i18n.html tag="h2" en="A state-driven inspection loop" zh="状态驱动的检测闭环" %}
  {% include i18n.html tag="p" class="section-intro" en="Every sample runs one loop through five layers: input, VLM evidence, verification, state and scheduling, and reporting. The design choices behind the loop are below." zh="每个采样时刻沿五层走一次闭环：输入、VLM 证据、校验、状态与调度、报告。闭环背后的设计取舍如下。" %}
  {% include figure_slot.html src="/assets/images/projects/bosch-sop/02_inspection_workflow.png" label="Fig. 2" ratio="16 / 9" alt_en="Five-layer inspection loop from video input to defect report" alt_zh="从视频输入到缺陷报告的五层检测闭环" %}
  <div class="overview-grid overview-grid-2 mt-4">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Separation" zh="职责分离" %}
      {% include i18n.html tag="h3" en="The VLM observes, the code decides" zh="VLM 负责观察，程序负责判断" %}
      {% include i18n.html tag="p" en="The model only returns timestamped evidence fields. Whether a step passes is decided by verifiers and the state machine, so every verdict can be explained." zh="模型只返回带时间戳的证据字段；某一步是否合格由校验器和状态机决定，因此每个结论都能解释。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="One model" zh="一个模型" %}
      {% include i18n.html tag="h3" en="Four tasks, one endpoint" zh="四类任务，共用一个服务" %}
      {% include i18n.html tag="p" en="main, screw, label, and removal share the same Qwen3.5-27B service and differ only in prompt, image crop, and output schema. No extra models are trained." zh="main、screw、label、removal 共用同一个 Qwen3.5-27B 服务，只在 prompt、图像裁剪与输出契约上不同，无需额外训练模型。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Two states" zh="两套状态" %}
      {% include i18n.html tag="h3" en="Phase moves on, defects stay" zh="阶段可推进，缺陷会保留" %}
      {% include i18n.html tag="p" en="The observed phase and the compliance checklist are tracked separately, so one missed screw never blocks the checks on labels and removal." zh="观察阶段与合规清单分开维护，漏一颗螺丝不会卡住后面的标签和移除检查。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Feedback" zh="反馈" %}
      {% include i18n.html tag="h3" en="State chooses the next call" zh="由状态决定下一次调用" %}
      {% include i18n.html tag="p" en="The scheduler uses the current state to pick the next task, crop, and call frequency. This is what later makes the cost savings possible." zh="调度器根据当前状态选择下一次的任务、裁剪区域和调用频率，这也是后续降低调用成本的基础。" %}
    </div>
  </div>
</section>

<section class="project-section" id="challenges">
  {% include i18n.html tag="div" class="section-kicker" en="3 · Challenges and solutions" zh="3 · 项目难点与解决方法" %}
  {% include i18n.html tag="h2" en="Four challenges, four design decisions" zh="四个难点，四项设计决策" %}
  {% include i18n.html tag="p" class="section-intro" en="Each challenge below maps to one layer of the system and the method used to address it." zh="下面每个难点都对应系统中的一层，以及针对它的解决方法。" %}
  <div class="challenge-block" id="evidence">
  {% include i18n.html tag="h3" class="challenge-title" en="3.1 · Look-alike objects → structured evidence" zh="3.1 · 相似负例 → 结构化证据" %}
  <div class="evidence-note mt-3">{% include i18n.html tag="strong" en="Challenge." zh="难点：" %} {% include i18n.html en="A pre-existing black bracket looks like the black box, a printer label looks like an attached label, and a visible drill looks like a finished screw." zh="原有黑色支架像黑盒，打印机出纸像已贴标签，看到电钻像螺丝已装好。" %}</div>
  {% include i18n.html tag="h4" class="solution-title" en="The model reports evidence; the verifier decides" zh="模型只报告证据，结论由校验器决定" %}
  {% include i18n.html tag="p" class="section-intro" en="Instead of asking the model whether a step is done, each prompt splits the question into separate fields: object, spatial relation, action cue, and static result. Downstream code can then control how these fields combine." zh="不直接问模型某一步是否完成，而是把问题拆成独立字段：对象、空间关系、动作线索和静态结果。下游代码再控制这些字段如何组合。" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Main" zh="Main" %}
      {% include i18n.html tag="h3" en="Global scene" zh="全局场景" %}
      {% include i18n.html tag="p" en="Cover location, black box relative to the cover, and phase hints. The cover box anchors every later crop." zh="盖板位置、黑盒与盖板的关系、阶段提示。盖板框是后续所有裁剪的空间锚点。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Screw" zh="Screw" %}
      {% include i18n.html tag="h3" en="Four named positions" zh="四个命名孔位" %}
      {% include i18n.html tag="p" en="Tool, bit contact, fastening cue, action position, and static installed-screw evidence are separate fields." zh="工具、钻头接触、拧紧线索、动作位置和静态螺丝证据是相互独立的字段。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Label" zh="Label" %}
      {% include i18n.html tag="h3" en="Being attached vs attached" zh="正在贴 vs 已贴上" %}
      {% include i18n.html tag="p" en="Center and side labels are judged independently; printer output and hand-held labels do not count." zh="center 与 side 标签独立判断；打印机出纸和手中的标签不计入。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Removal" zh="Removal" %}
      {% include i18n.html tag="h3" en="Gone, not just hidden" zh="真正离开，而非被挡住" %}
      {% include i18n.html tag="p" en="Cover presence, confirmed removal, workbench visibility, and restoration are reported separately." zh="盖板存在、确认移除、工作台可见、工作台恢复分别报告。" %}
    </div>
  </div>
  <div class="table-responsive mt-3">
    <table class="table technical-table">
      <thead><tr><th>{% include i18n.html en="Screw field" zh="螺丝字段" %}</th><th>{% include i18n.html en="Answers" zh="回答的问题" %}</th><th>{% include i18n.html en="Does not prove" zh="不能单独证明" %}</th></tr></thead>
      <tbody>
        <tr><td><code>drill_visible</code></td><td>{% include i18n.html en="Is the tool visible?" zh="工具是否可见" %}</td><td>{% include i18n.html en="That an installation happened" zh="发生了安装" %}</td></tr>
        <tr><td><code>drill_bit_touching_hole</code></td><td>{% include i18n.html en="Is the bit on a hole?" zh="钻头是否接触孔位" %}</td><td>{% include i18n.html en="That fastening finished" zh="拧紧已完成" %}</td></tr>
        <tr><td><code>action_position</code></td><td>{% include i18n.html en="Which position is the action at?" zh="动作发生在哪个位置" %}</td><td>{% include i18n.html en="That this position is complete" zh="该位置已完成" %}</td></tr>
        <tr><td><code>post_screw_visible_positions</code></td><td>{% include i18n.html en="Which positions show an installed screw?" zh="哪些位置可见已装螺丝" %}</td><td>{% include i18n.html en="Immunity to reflections" zh="不受反光干扰" %}</td></tr>
      </tbody>
    </table>
  </div>
  </div>
  <div class="challenge-block" id="verification">
  {% include i18n.html tag="h3" class="challenge-title" en="3.2 · Unstable single frames → multi-frame verification" zh="3.2 · 单帧不稳定 → 多帧校验" %}
  <div class="evidence-note mt-3">{% include i18n.html tag="strong" en="Challenge." zh="难点：" %} {% include i18n.html en="Screws and labels are small and often hidden by hands, tools, or reflections; a single frame can be wrong, and repeated frames can double-count." zh="螺丝和标签很小，常被手、工具或反光遮挡；单帧可能出错，重复帧还会导致重复计数。" %}</div>
  {% include i18n.html tag="h4" class="solution-title" en="Separate what was seen from what is compliant" zh="把“看到了什么”和“是否合格”分开" %}
  {% include i18n.html tag="p" class="section-intro" en="A single observation can be wrong, occluded, or ambiguous. Observations are aggregated into evidence state, and only then into compliance state used by the report." zh="单次观察可能出错、被遮挡或位置不确定。观察先聚合为证据状态，再形成用于报告的合规状态。" %}
  {% include figure_slot.html src="/assets/images/projects/bosch-sop/03_temporal_screw_evidence.png" label="Fig. 3" ratio="16 / 7" alt_en="Observation, evidence state, and compliance state for the four screw positions" alt_zh="四个螺丝位置的观察、证据状态与合规状态" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Screws" zh="螺丝" %}
      {% include i18n.html tag="h3" en="Count positions, not positives" zh="按位置计数，而不是累计正例" %}
      {% include i18n.html tag="p" en="Evidence is kept per position. Repeated hits on one hole add support, never a new screw. Missing positions are the four minus the confirmed set." zh="证据按孔位维护。同一孔位重复命中只增加支持，不会多出一颗螺丝。缺失位置 = 四个孔位减去已确认集合。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Static rescue" zh="静态补查" %}
      {% include i18n.html tag="h3" en="Bounded by the S3 window" zh="限定在 S3 窗口内" %}
      {% include i18n.html tag="p" en="A later clear frame may confirm a screw hidden during the action, but only inside the screw stage; once labelling starts, new screw evidence stops counting." zh="稍后清晰的静态帧可以补认动作中被遮挡的螺丝，但只在螺丝阶段内；开始贴标后不再计入新的螺丝证据。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Labels" zh="标签" %}
      {% include i18n.html tag="h3" en="No permanent OR-latch" zh="避免一次正例永久锁定" %}
      {% include i18n.html tag="p" en="Locking a label as done after a single positive frame lets one false positive survive forever; candidates are separated from confirmations." zh="一帧为真就永久锁定完成，会让一次误检无法纠正；因此把候选与确认分开。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Removal" zh="移除" %}
      {% include i18n.html tag="h3" en="Early stop, NG kept" zh="早停，但保留 NG" %}
      {% include i18n.html tag="p" en="Reliable removal ends the cycle and skips the idle tail, without overwriting earlier missing items." zh="可靠确认移除后结束本轮观察、跳过尾部空帧，但不覆盖之前的缺失项。" %}
    </div>
  </div>

  {% include i18n.html tag="h3" class="mt-4" en="Walkthrough — the upper-right screw is missing" zh="推演 — 漏装右上螺丝" %}
  <ol class="walkthrough">
    <li><strong>{% include i18n.html en="Part in place" zh="工件就位" %}</strong>{% include i18n.html en="Cover and black-box relation confirmed; the cover box becomes the spatial anchor." zh="盖板与黑盒关系得到确认；盖板框成为空间锚点。" %}</li>
    <li><strong>{% include i18n.html en="Three screws" zh="前三颗螺丝" %}</strong>{% include i18n.html en="Action cues and static results appear per position; repeated frames do not raise the count." zh="动作线索与静态结果按位置出现；重复帧不增加计数。" %}</li>
    <li class="is-flag"><strong>{% include i18n.html en="Upper-right is blurred" zh="右上位置模糊" %}</strong>{% include i18n.html en="A possible action near the hole, no visible result: kept as a candidate, not completed." zh="孔位附近有疑似动作，但看不到结果：保留为候选，不判为完成。" %}</li>
    <li><strong>{% include i18n.html en="Labelling starts" zh="开始贴标" %}</strong>{% include i18n.html en="The screw window closes with upper-right still unconfirmed; observation moves on to labels." zh="螺丝窗口关闭，右上仍未确认；观察转入标签阶段。" %}</li>
    <li class="is-flag"><strong>{% include i18n.html en="Labels, removal, report" zh="标签、移除、报告" %}</strong>{% include i18n.html en="Later steps are still checked; the report lists the missing upper-right screw." zh="后续步骤照常检查；报告列出缺失的右上螺丝。" %}</li>
  </ol>
  <div class="tradeoff-callout mt-2">
    {% include i18n.html en="The observed phase and the compliance checklist are kept apart. Otherwise a single missed screw would block the system from ever checking the labels." zh="观察阶段与合规清单分开维护。否则漏一颗螺丝就会让系统卡住，永远查不到后面的标签。" %}
  </div>
  </div>
  <div class="challenge-block" id="scheduling">
  {% include i18n.html tag="h3" class="challenge-title" en="3.3 · Out-of-stage false positives → state-driven gating" zh="3.3 · 阶段外误报 → 按状态调用" %}
  <div class="evidence-note mt-3">{% include i18n.html tag="strong" en="Challenge." zh="难点：" %} {% include i18n.html en="Running every task on every frame wastes calls and lets label or screw checks fire in the wrong stage." zh="每帧都跑全部任务既浪费调用，又会让标签或螺丝检查在错误阶段误报。" %}</div>
  {% include i18n.html tag="h4" class="solution-title" en="Call only what the current state needs" zh="只调用当前状态需要的检测" %}
  {% include i18n.html tag="p" class="section-intro" en="Calling all four tasks on every sample costs requests and invites out-of-stage false positives. Stage gating decides which tasks are eligible at each sample." zh="每个采样都调用四类任务，既浪费请求，又会制造阶段外误报。阶段门控决定每个采样时刻哪些任务有资格调用。" %}
  <div class="overview-grid overview-grid-3">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Gating" zh="门控" %}
      {% include i18n.html tag="h3" en="Eligibility by stage" zh="按阶段决定调用资格" %}
      {% include i18n.html tag="p" en="Screw, label, and removal checks are collected according to stage, strong signals, visibility, and lock state." zh="螺丝、标签、移除检查根据阶段、强信号、可见性和锁定状态决定是否收集。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Rule-based" zh="规则式" %}
      {% include i18n.html tag="h3" en="Explicit and inspectable" zh="显式、可检查" %}
      {% include i18n.html tag="p" en="Every call or skip is logged with its reason, so request savings can be traced back to the schedule." zh="每次调用或跳过都记录原因，请求节省可以追溯到具体调度规则。" %}
    </div>
  </div>
  </div>
  <div class="challenge-block" id="input">
  {% include i18n.html tag="h3" class="challenge-title" en="3.4 · Silently corrupted inputs → input integrity checks" zh="3.4 · 输入悄悄出错 → 输入完整性校验" %}
  <div class="evidence-note mt-3">{% include i18n.html tag="strong" en="Challenge." zh="难点：" %} {% include i18n.html en="A wrong crop or a preprocessing step that silently falls back corrupts every rule built on top of it." zh="裁错区域或预处理静默回退，会让上层所有规则都建立在错误证据上。" %}</div>
  {% include i18n.html tag="h4" class="solution-title" en="Verify the pixels the model actually receives" zh="核对模型实际收到的像素" %}
  {% include i18n.html tag="p" class="section-intro" en="A wrong crop silently corrupts every rule built on top of it, so preprocessing is treated as part of perception and logged like a model call." zh="裁错区域会让上层所有规则都建立在错误证据上，因此预处理被视为感知的一部分，并像模型调用一样记录。" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Time" zh="时间" %}
      {% include i18n.html tag="h3" en="Video time, not wall time" zh="视频时间而非运行时间" %}
      {% include i18n.html tag="p" en="Evidence is stamped with the video timestamp and frame index; processing latency is measured on a separate clock." zh="证据以视频时间戳与帧号标记；处理延迟用另一套时钟单独统计。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Geometry" zh="几何" %}
      {% include i18n.html tag="h3" en="Cover-relative work zone" zh="以盖板为参照的工作区" %}
      {% include i18n.html tag="p" en="An early design used four small fixed boxes; a strip anchored to the cover tolerates small shifts and keeps tool-contact context." zh="早期用四个固定小框；以盖板为参照的长条工作区能容忍轻微偏移，并保留工具接触上下文。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Encoding" zh="编码" %}
      {% include i18n.html tag="h3" en="Resize, JPEG, Base64 are different" zh="缩放、JPEG、Base64 不是一回事" %}
      {% include i18n.html tag="p" en="Resizing changes what the model sees, JPEG quality changes bytes, Base64 only wraps them. Each is checked on its own." zh="缩放改变模型看到的内容，JPEG 质量改变字节数，Base64 只是封装。三者分别检查。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Case" zh="案例" %}
      {% include i18n.html tag="h3" en="Enabled is not applied" zh="开启不等于生效" %}
      {% include i18n.html tag="p" en="Compression was switched on, but image reads failed on a non-ASCII path and the code fell back to the original image. The fix was to check real payload size, not the config flag." zh="压缩配置已开启，但在中文路径下读图失败，代码回退到原图。解决思路是检查实际载荷大小，而不是配置开关。" %}
    </div>
  </div>
  </div>
</section>

<section class="project-section" id="optimisation">
  {% include i18n.html tag="div" class="section-kicker" en="4 · Optimisation approach" zh="4 · 优化思路与方法" %}
  {% include i18n.html tag="h2" en="Cut cost without giving up a single defect" zh="降低成本，但不放过任何一个缺陷" %}
  {% include i18n.html tag="p" class="section-intro" en="Optimisation is framed as a constrained problem: reduce requests and run time while defect escapes and false rejects stay unchanged on the regression set." zh="优化被定义为带约束的问题：在回归集上缺陷漏放与误拒保持不变的前提下，减少请求数与运行时间。" %}

  {% include i18n.html tag="h3" class="mt-4" en="How each change is measured" zh="每项改动怎样衡量" %}
  {% include i18n.html tag="p" class="section-intro" en="NG (defective) videos are the positive class. A correct NG verdict with the wrong defect is not a success." zh="以 NG（缺陷）视频为正类。判成 NG 但缺陷类型报错，不算成功。" %}
  <div class="metric-tooltip-grid">
    <div class="metric-tip">
      {% include i18n.html tag="strong" en="Defect escape" zh="缺陷漏放率" %}
      {% include i18n.html tag="span" en="FN / (TP + FN). Defective parts passed as OK." zh="FN / (TP + FN)。缺陷件被判为 OK 的比例。" %}
    </div>
    <div class="metric-tip">
      {% include i18n.html tag="strong" en="False reject" zh="正常品误拒率" %}
      {% include i18n.html tag="span" en="FP / (FP + TN). Good parts flagged as NG." zh="FP / (FP + TN)。正常件被判为 NG 的比例。" %}
    </div>
    <div class="metric-tip">
      {% include i18n.html tag="strong" en="Exact defect set" zh="缺陷集合完全匹配" %}
      {% include i18n.html tag="span" en="The predicted set of missing screws and labels equals the true set." zh="预测的缺失螺丝与标签集合与真实集合完全一致。" %}
    </div>
    <div class="metric-tip">
      {% include i18n.html tag="strong" en="Requests & latency" zh="请求与延迟" %}
      {% include i18n.html tag="span" en="Logical vs raw requests, p50 / p95 latency, and wall time per video." zh="逻辑调用与实际请求、p50 / p95 延迟，以及每条视频的总耗时。" %}
    </div>
  </div>

  {% include i18n.html tag="h3" class="mt-5" en="Method 1 — M1 sparse main scheduling" zh="方法 1 — M1 稀疏 main 调度" %}
  {% include i18n.html tag="p" class="section-intro" en="Once the cover and black box are confirmed, the global main call no longer needs to run on every sample. M1 widens the main stride by stage, while event triggers and a maximum gap keep the stage estimate fresh." zh="盖板与黑盒确认后，全局 main 无需每个采样都调用。M1 按阶段放宽 main 的调用步长，同时用事件触发和最大间隔保证阶段估计不过期。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/bosch-sop/m1-schedule.svg' | relative_url }}" alt="Main stride per stage: every sample in S1 and S2, every 2 in S3 and S4, every 3 in S5, with maximum gaps" data-alt-en="Main stride per stage: every sample in S1 and S2, every 2 in S3 and S4, every 3 in S5, with maximum gaps" data-alt-zh="各阶段 main 调用步长：S1、S2 每次采样，S3、S4 每 2 次，S5 每 3 次，并标注最大间隔" loading="lazy">
  </figure>
  <div class="overview-grid overview-grid-2">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Forced main" zh="强制 main" %}
      {% include i18n.html tag="h3" en="Events override the stride" zh="事件优先于步长" %}
      {% include i18n.html tag="p" en="Key positives, FSM changes, stage transitions, verifier conflicts, and the final report all force a global look." zh="关键正例、状态机变化、阶段转场、校验冲突和生成报告前都会强制一次全局观察。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Max gap" zh="最大间隔" %}
      {% include i18n.html tag="h3" en="Never stale for long" zh="不会长期使用过期信息" %}
      {% include i18n.html tag="p" en="A cap on the time since the last main call bounds how long the stage estimate can go unrefreshed." zh="限制距上次 main 的最长时间，使阶段估计不会长时间得不到更新。" %}
    </div>
  </div>

  {% include i18n.html tag="h3" class="mt-5" en="Methods 2–4 — Prompt, client, and concurrency" zh="方法 2–4 — Prompt、客户端与并发" %}
  <div class="overview-grid overview-grid-3">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Prompt" zh="Prompt" %}
      {% include i18n.html tag="h3" en="Slim the removal prompt" zh="精简 removal prompt" %}
      {% include i18n.html tag="p" en="Shorter instructions and output fields to cut decode time on the removal check." zh="缩短指令与输出字段，降低 removal 检查的生成耗时。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Client" zh="客户端" %}
      {% include i18n.html tag="h3" en="Shared client and warmup" zh="共享客户端与预热" %}
      {% include i18n.html tag="p" en="Reuse one HTTP client and warm the connection before the first request." zh="复用同一个 HTTP 客户端，并在首次请求前预热连接。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Concurrency" zh="并发" %}
      {% include i18n.html tag="h3" en="Parallel requests" zh="并行请求" %}
      {% include i18n.html tag="p" en="Send two task requests at once and compare tail latency against sequential calls." zh="同时发送两个任务请求，与串行调用比较尾延迟。" %}
    </div>
  </div>
  <div class="tradeoff-callout mt-3">
    {% include i18n.html en="Every change is compared against a same-round baseline, changes one factor at a time, and is adopted only if the full-system regression keeps every defect report intact." zh="每项改动都与同轮基线对照，一次只改一个因素，只有全系统回归保证缺陷报告完整时才会采用。" %}
  </div>
</section>

<section class="project-section" id="results">
  {% include i18n.html tag="div" class="section-kicker" en="5 · Optimisation results and final outcome" zh="5 · 优化结果与最终效果" %}
  {% include i18n.html tag="h2" en="~20% fewer global VLM calls, zero verdict changes" zh="全局 VLM 调用减少近 20%，检测结论零变化" %}
  {% include i18n.html tag="p" class="section-intro" en="State-driven scheduling removed redundant model calls without losing a single defect: every final verdict and every key check survived the cut." zh="状态驱动调度砍掉了冗余的模型调用，同时没有漏掉任何一个缺陷：所有最终判断与关键检查点全部保留。" %}
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="Global main calls" zh="全局 main 调用" %}<strong>−19.6%</strong><small>112 → 90</small></div>
    <div>{% include i18n.html tag="span" en="Total VLM requests" zh="VLM 总请求" %}<strong>−38</strong>{% include i18n.html tag="small" en="per regression round · −15.8%" zh="每轮回归 · −15.8%" %}</div>
    <div>{% include i18n.html tag="span" en="Final verdicts" zh="最终判断" %}<strong>100%</strong>{% include i18n.html tag="small" en="6 / 6 preserved" zh="6 / 6 全部保持" %}</div>
    <div>{% include i18n.html tag="span" en="Key checks" zh="关键检查点" %}<strong>14 / 14</strong>{% include i18n.html tag="small" en="zero regressions" zh="零回退" %}</div>
  </div>

  {% include i18n.html tag="h3" class="mt-5" en="Result 1 — Sparse main scheduling cuts calls at no accuracy cost" zh="结果 1 — 稀疏 main 调度：降调用，不降准确性" %}
  {% include i18n.html tag="p" class="section-intro" en="In a same-round comparison on all six regression videos, M1 removed 38 requests per round, 22 of them global main calls, while every OK / NG verdict and all 14 key checks stayed exactly the same." zh="在全部六条回归视频的同轮对照中，M1 每轮少发 38 次请求，其中 22 次是全局 main 调用；所有 OK / NG 判断与 14 个关键检查点保持完全一致。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/bosch-sop/request-reduction.svg' | relative_url }}" alt="Requests before and after M1: total 240 to 202, main 112 to 90, non-main 128 to 112" data-alt-en="Requests before and after M1: total 240 to 202, main 112 to 90, non-main 128 to 112" data-alt-zh="M1 前后的请求数：总计 240 到 202，main 112 到 90，非 main 128 到 112" loading="lazy">
  </figure>
  <p class="source-line"><span class="evidence-chip">{% include i18n.html en="Headroom" zh="后续空间" %}</span> {% include i18n.html en="In the OK video, 14 main calls were triggered by verifier conflicts; separating verdict-changing conflicts from minor ones is the next lever for further savings." zh="OK 视频中有 14 次 main 由校验冲突触发；区分会改变结论的冲突与轻微不一致，是进一步降低调用的下一个抓手。" %}</p>

  {% include i18n.html tag="h3" class="mt-5" en="Result 2 — Regression gating: aggressive speed-ups, zero risky adoptions" zh="结果 2 — 回归把关：大胆提速，零风险上线" %}
  {% include i18n.html tag="p" class="section-intro" en="Module-level speed-ups of up to 36.6% were identified and measured, then gated by full-system regression. Two failed the full-system check, one of them missing key defects in two rounds, and both were blocked before adoption." zh="识别并测量了最高 36.6% 的模块级提速，再交由全系统回归把关。其中两项未通过全系统回归（一项连续两轮漏掉关键缺陷），均在采用前被拦下。" %}
  <figure class="data-figure">
    <img src="{{ '/assets/images/projects/bosch-sop/optimisation-outcomes.svg' | relative_url }}" alt="Reported time reductions of three optimisation attempts and their regression outcomes" data-alt-en="Reported time reductions of three optimisation attempts and their regression outcomes" data-alt-zh="三项优化尝试的时间降幅及其回归结果" loading="lazy">
  </figure>
  <div class="result-highlight-grid">
    <div>{% include i18n.html tag="span" en="Removal module latency" zh="removal 模块延迟" %}<strong>−36.6%</strong><small>2.950 → 1.870 s</small></div>
    <div>{% include i18n.html tag="span" en="Removal output length" zh="removal 输出长度" %}<strong>−46%</strong>{% include i18n.html tag="small" en="prompt slimming" zh="prompt 精简" %}</div>
    <div>{% include i18n.html tag="span" en="End-to-end wall time" zh="端到端总耗时" %}<strong>−32%</strong>{% include i18n.html tag="small" en="best single round" zh="最佳单轮" %}</div>
    <div>{% include i18n.html tag="span" en="Risky speed-ups blocked" zh="拦下的风险方案" %}<strong>2 / 2</strong>{% include i18n.html tag="small" en="caught by regression" zh="均由回归发现" %}</div>
  </div>
  <details class="technical-details result-table-details mt-3">
    <summary>{% include i18n.html en="Optimisation log" zh="优化记录" %}</summary>
    <div class="table-responsive">
      <table class="table technical-table">
        <thead><tr><th>{% include i18n.html en="Change" zh="改动" %}</th><th>{% include i18n.html en="Measured effect" zh="测得效果" %}</th><th>{% include i18n.html en="Decision" zh="决定" %}</th></tr></thead>
        <tbody>
          <tr class="table-emphasis"><td>{% include i18n.html en="M1 sparse main" zh="M1 稀疏 main" %}</td><td>{% include i18n.html en="Requests 240 → 202, main 112 → 90, verdicts kept" zh="请求 240 → 202，main 112 → 90，结论保持" %}</td><td>{% include i18n.html en="Adopted" zh="采用" %}</td></tr>
          <tr><td>{% include i18n.html en="Removal prompt slimming" zh="removal prompt 精简" %}</td><td>{% include i18n.html en="Output −46%, module latency 2.950 → 1.870 s" zh="输出 −46%，模块延迟 2.950 → 1.870 秒" %}</td><td>{% include i18n.html en="Blocked: system regression failed" zh="拦下：系统回归未通过" %}</td></tr>
          <tr><td>{% include i18n.html en="Sparse main + removal slimming" zh="稀疏 main + removal 精简" %}</td><td>{% include i18n.html en="Wall time −32% in one round" zh="单轮总耗时 −32%" %}</td><td>{% include i18n.html en="Blocked: key defects missed in two rounds" zh="拦下：两轮均漏掉关键缺陷" %}</td></tr>
          <tr><td>{% include i18n.html en="Shared client + warmup" zh="共享客户端 + 预热" %}</td><td>{% include i18n.html en="Wall time −11.7% in one round" zh="单轮总耗时 −11.7%" %}</td><td>{% include i18n.html en="Promising, under further validation" zh="有潜力，继续验证中" %}</td></tr>
          <tr><td>{% include i18n.html en="Concurrency of 2" zh="并发数 2" %}</td><td>{% include i18n.html en="Tail latency worse" zh="尾延迟变差" %}</td><td>{% include i18n.html en="Not adopted" zh="未采用" %}</td></tr>
        </tbody>
      </table>
    </div>
  </details>
  <div class="tradeoff-callout mt-3">
    {% include i18n.html en="Every optimisation was accepted only if it kept the defect report intact: speed was never traded for a missed screw or label." zh="每项优化都必须保证缺陷报告完整才会被采用：从不以漏掉一颗螺丝或一张标签为代价换取速度。" %}
  </div>

  {% include i18n.html tag="h3" class="mt-5" en="Final outcome" zh="最终效果" %}
  <div class="overview-grid">
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Verdicts" zh="判断" %}
      {% include i18n.html tag="h3" en="6 / 6 videos match the expected report" zh="6 / 6 条视频与预期报告一致" %}
      {% include i18n.html tag="p" en="OK runs pass; defective runs are flagged NG with the right error codes." zh="OK 流程通过；缺陷流程判为 NG，并给出对应错误码。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Localisation" zh="定位" %}
      {% include i18n.html tag="h3" en="Exact missing item" zh="精确到缺失项" %}
      {% include i18n.html tag="p" en="Reports which screw position or which label is missing, with evidence timestamps." zh="报告具体缺失的螺丝位置或标签类型，并附证据时间戳。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Cost" zh="成本" %}
      {% include i18n.html tag="h3" en="~20% fewer global calls" zh="全局调用减少近 20%" %}
      {% include i18n.html tag="p" en="Sparse main scheduling is adopted in the final pipeline with no loss in key checks." zh="稀疏 main 调度进入最终流程，关键检查点无损失。" %}
    </div>
    <div class="overview-card">
      {% include i18n.html tag="div" class="overview-label" en="Traceability" zh="可追溯" %}
      {% include i18n.html tag="h3" en="Every decision is logged" zh="每个决策都有记录" %}
      {% include i18n.html tag="p" en="Each call, skip, verifier decision, and state change can be traced back from the report." zh="每次调用、跳过、校验结论与状态变化都能从报告回溯。" %}
    </div>
  </div>
</section>
