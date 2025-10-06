---
title:          "Intelligent Network Traffic Control – Software-Defined Networking"
date:           2024-12-13 00:01:00 +0800
selected:       true
pub:            "CAN201 - Computer Networks"
pub_date:       "2024"
abstract: >-
  This project explores the power of Software-Defined Networking (SDN) by building an intelligent traffic control system that can dynamically redirect network flows. In modern cloud infrastructure and data centers, the ability to programmatically control how data travels through networks is crucial for optimizing performance, balancing loads, and ensuring service reliability.


  Using Mininet to create a virtual network environment, we constructed a realistic topology with a client, two servers, and an SDN-enabled switch. This setup simulates real-world scenarios where multiple servers handle user requests and traffic needs intelligent routing decisions.


  The heart of the project is two custom SDN controller applications built with the Ryu framework. The first implements standard forwarding where traffic flows directly to its intended destination. The second demonstrates intelligent redirection, where the controller can transparently route traffic to an alternative server based on programmable logic—useful for scenarios like load balancing when one server becomes overloaded, or failover when a primary server goes down.


  Through performance testing, we measured and compared network latency under both modes, revealing the tradeoffs between direct routing and intelligent redirection. The results provide insights into how SDN can optimize network performance while maintaining the flexibility to adapt to changing conditions.


  This project showcases SDN's practical applications in building smarter, more adaptable networks. Beyond the technical implementation, it demonstrates understanding of how network architecture decisions impact user experience and system reliability—knowledge directly applicable to designing modern cloud services and distributed systems.
cover:          /assets/images/covers/project-sdn-traffic.png
authors:
- Rui Sang
- MingXuan Hu
- ZiQi Liu
- ZhiXin Li
- ZhengHao Zhou
links:
  Code: https://github.com/richael-sang/Software-Defined-Networking
  Report: /assets/pdfs/projects/sdn-traffic/Report_Part_II.pdf
---

