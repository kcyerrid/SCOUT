---
entity_type: mitre_technique
technique_id: "T1046"
subtechnique_id: ""
technique_name: "Network Service Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "Containers"
  - "IaaS"
  - "Linux"
  - "Network Devices"
  - "Windows"
  - "macOS"
datasources:
  - "DC0032 - Process Creation"
  - "DC0082 - Network Connection Creation"
  - "DC0078 - Network Traffic Flow"
  - "DC0085 - Network Traffic Content"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
  - "[[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]"
  - "[[30_CIPHER/03_Threat_Actors/G0098 - BlackTech|BlackTech]]"
  - "[[30_CIPHER/03_Threat_Actors/G1043 - BlackByte|BlackByte]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1180 - BlackByte Ransomware|BlackByte Ransomware]]"
associated_campaigns: []
related_techniques:
  - "T1018"
detection_priority:
  - "High"
detection_maturity: ""
threat_score: 4
created: 2026-01-06
updated: 2026-01-06
contributors: []
tags:
  - "mitre"
  - "technique"
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Network Service Discovery is adversary identification of services running on remote hosts or network infrastructure (open ports, exposed services, banners, protocols). It supports targeting for exploitation, lateral movement planning, credential abuse, and identifying high-value systems.

## 2. Technical Overview
Common discovery methods:
- Port/service scanning and probing across subnets (TCP/UDP), including version and banner discovery.
- Wordlist or vulnerability scanning to identify known-exploitable services.
- mDNS/Bonjour-based discovery on macOS environments to find advertised services.
- In cloud or containerized environments, probing services within VPCs/namespaces and enumerating reachable endpoints.

Defender-relevant signals:
- Rapid sequential connections to many ports/hosts from a single process
- Repeated connection failures (SYN scans, refused ports) consistent with scanning rather than application use
- Scanning utilities executed from endpoints that are not authorized scanners
- Container namespace traffic probing that differs from typical service-to-service patterns

## 3. Subtechnique Considerations
None (no sub-techniques).

## 4. Procedure Examples
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]] used malware to conduct port scans on specified subnets.
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]] used scanning frameworks and custom scanners for network scanning.
- [[30_CIPHER/03_Threat_Actors/G1043 - BlackByte|BlackByte]] used tools to enumerate network services in victim environments.
- [[30_CIPHER/05_Malware/S1180 - BlackByte Ransomware|BlackByte Ransomware]] performed discovery of remote systems/services prior to launching payloads.

## 5. Detection Guidance
Core detection goal: identify **enumeration behavior** distinct from normal client/server usage.

Recommended detection logic:
- **Process-to-network correlation**
  - Join process creation telemetry to outbound connection telemetry.
  - Flag processes that connect to N unique destinations/ports within a short time window.
- **Rate + breadth thresholds**
  - Unique destination IP count, unique destination port count, failed-connection ratio.
- **Environmental allowlisting**
  - Maintain approved scanner inventory (hosts, accounts, tools, time windows).
  - Flag scanner-like behavior from non-scanner hosts.

### Data Source Notes
- **DC0032 – Process Creation**: identify scanner processes and suspicious parents/paths.
- **DC0082 – Network Connection Creation**: endpoint connection telemetry to measure scan breadth and rates.
- **DC0078 – Network Traffic Flow**: NetFlow/NSM for scan-like traffic patterns (SYN bursts, UDP probes).
- **DC0085 – Network Traffic Content**: protocol fingerprints (e.g., mDNS queries, service probes) and payload indicators.

## 6. Response Guidance
1. Identify the scanning process, user, and host; verify if it is an authorized scanner or IT activity.
2. Scope the scan: targets, ports, duration, and whether it focused on known sensitive services.
3. Hunt follow-on behavior: exploit attempts, credential abuse, remote service usage, lateral movement.
4. Contain if malicious: block scanning host, restrict egress, isolate container namespace, and reset compromised creds if discovery is internal.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1046 - Network Service Discovery|T1046]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1018 - Remote System Discovery|T1018]]

## 8. SOC Relevance
- **High**: foundational recon step that frequently precedes exploitation/lateral movement.
- Best detections are behavior-based and tuned to the environment’s legitimate scanning patterns.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]: subnet scanning via malware.
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]: use of scanning tools and custom scanners.
- [[30_CIPHER/03_Threat_Actors/G0098 - BlackTech|BlackTech]]: scanning utilities for target identification.
- [[30_CIPHER/03_Threat_Actors/G1043 - BlackByte|BlackByte]]: network service enumeration in victim environments.

## 10. Campaign Usage
None noted.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1180 - BlackByte Ransomware|BlackByte Ransomware]]: discovery of remote systems/services prior to payload launch.

## 12. Mitigations
- Restrict and monitor administrative scanning tools; use jump hosts and dedicated scanner networks.
- Network segmentation to limit reachability of sensitive services.
- Egress controls and anomaly detection to reduce internal scanning impact.
- Harden exposed services (patching, MFA, least privilege) to reduce utility of discovered attack surface.

## 13. Testing & Validation
- Safe validation:
  - Run authorized scanning from a known scanner host; ensure allowlists prevent false positives.
  - Simulate low-rate scanning from a non-scanner endpoint (in a lab) and validate thresholds and joins.
  - Test mDNS discovery on macOS and confirm visibility in both endpoint logs and NSM.

## 14. References
- MITRE ATT&CK. (n.d.). *Network Service Discovery (T1046).* https://attack.mitre.org/techniques/T1046/
- MITRE ATT&CK. (2025). *Behavioral Detection Strategy for Network Service Discovery Across Platforms (DET0376).* https://attack.mitre.org/detectionstrategies/DET0376/
- MITRE ATT&CK. (n.d.). *BlackByte Ransomware (S1180).* https://attack.mitre.org/software/S1180/

## 15. Notes
- Strongest SOC signal: **non-scanner endpoint** performing broad, fast connection attempts paired with a suspicious new/unsigned binary or unusual parent process.
