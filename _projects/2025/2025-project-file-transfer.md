---
title:          "Secure File Transfer System – Network Protocol Implementation"
date:           2024-11-15 00:01:00 +0800
selected:       true
pub:            "CAN201 - Computer Networks"
pub_date:       "2024"
abstract: >-
  This networking project implements a complete file transfer system from scratch, building a custom client-server application using Python socket programming. The system enables secure file uploads and downloads through a custom-designed communication protocol, demonstrating fundamental principles of network programming and distributed systems.


  The project features a user-friendly GUI client application built with Tkinter that connects to a server following the STEP (Simple Transfer and Exchange Protocol) specification. Users can authenticate, upload files of any size, download files, and manage their stored data through an intuitive interface. The system handles large files efficiently by breaking them into manageable blocks and includes real-time progress tracking during transfers.


  Security is built into every layer: user authentication with hashed passwords, token-based session management to maintain secure connections, and MD5 checksums to verify file integrity after transfers. The protocol includes error handling and status reporting to ensure reliable communication even under network instability.


  The implementation showcases low-level network programming concepts including socket creation and management, binary data serialization with JSON metadata, multi-threaded operations for responsive UI during network operations, and graceful connection handling with proper resource cleanup.


  Beyond just functioning code, this project required designing a complete protocol specification, implementing both client and server sides that correctly interpret the protocol, and ensuring robust error handling for various failure scenarios like network timeouts, file access errors, and authentication failures.
cover:          /assets/images/covers/project-file-transfer.png
authors:
- Rui Sang
- MingXuan Hu
- ZiQi Liu
- ZhiXin Li
- ZhengHao Zhou
links:
  Report: /assets/pdfs/projects/file-transfer/Report_Part_I.pdf
---

