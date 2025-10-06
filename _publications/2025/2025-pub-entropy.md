---
title:          "An Entropy-Guided Curriculum Learning Strategy for Data-Efficient Acoustic Scene Classification under Domain Shift"
date:           2025-09-05 00:01:00 +0800
selected:       true
pub:            "Workshop on Detection and Classification of Acoustic Scenes and Events (DCASE Workshop)"
pub_date:       "2025"
abstract: >-
  Acoustic Scene Classification (ASC) faces challenges in generalizing across recording devices, particularly when labeled data is limited. The DCASE 2024 Challenge Task 1 highlights this issue by requiring models to learn from small labeled subsets recorded on a few devices. These models need to then generalize to recordings from previously unseen devices under strict complexity constraints. While techniques such as data augmentation and the use of pre-trained models are well-established for improving model generalization, optimizing the training strategy represents a complementary yet less-explored path that introduces no additional architectural complexity or inference overhead. Among various training strategies, curriculum learning offers a promising paradigm by structuring the learning process from easier to harder examples. In this work, we propose an entropy-guided curriculum learning strategy to address the domain shift problem in data-efficient ASC. Specifically, we quantify the uncertainty of device domain predictions for each training sample by computing the Shannon entropy of the device posterior probabilities estimated by an auxiliary domain classifier. Using entropy as a proxy for domain invariance, the curriculum begins with high-entropy samples and gradually incorporates low-entropy, domainspecific ones to facilitate the learning of generalizable representations. Experimental results on multiple DCASE 2024 ASC baselines demonstrate that our strategy effectively mitigates domain shift, particularly under limited labeled data conditions. Our strategy is architecture-agnostic and introduces no additional inference cost, making it easily integrable into existing ASC baselines and offering a practical solution to domain shift.
cover:          /assets/images/covers/pub-entropy.png
authors:
- Peihong Zhang*
- Yuxuan Liu*
- Zhixin Li
- Rui Sang
- Yiqiang Cai
- Yizhou Tan
- Shengchen Li
links:
  Paper: https://arxiv.org/pdf/2509.11168
---