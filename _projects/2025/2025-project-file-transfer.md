---
title:          "Secure File Transfer System – Network Protocol Implementation"
date:           2024-11-15 00:01:00 +0800
selected:       true
pub:            "CAN201 - Computer Networks"
pub_date:       "2024"
abstract: >-
  This networking project implements a secure file transfer system from scratch using Python socket programming. The application follows a custom-designed communication protocol (STEP), which defines command structures, status responses, and how JSON metadata is transmitted alongside the binary file stream. The system features a multi-threaded Tkinter GUI client that remains responsive and does not freeze during lengthy network operations.

  The client provides an intuitive interface for user authentication, file management, and real-time progress tracking for large file transfers. Security is a core component, incorporating hashed passwords, token-based sessions for persistent login, and MD5 checksums to verify file integrity after transit. This project showcases low-level network programming, from designing a complete protocol specification to implementing robust error handling for various network failure scenarios.
cover:          /assets/images/covers/project-file-transfer.png
authors:
- Rui Sang
- Mingxuan Hu
- Ziqi Liu
- Zhixin Li
- Zhenghao Zhou
links:
  Code: https://github.com/richael-sang/Network-Protocol-Implementation
  Report: /assets/pdfs/projects/file-transfer/Report_Part_I.pdf
---

