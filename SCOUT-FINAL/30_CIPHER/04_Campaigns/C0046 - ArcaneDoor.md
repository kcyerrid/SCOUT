---
entity_type: campaign
campaign_name: ArcaneDoor
campaign_id: C0046
first_seen: 2023-07
last_seen: 2024-04
suspected_attribution: State-sponsored (tracked as UAT4356 / STORM-1849)
associated_actors:
  - UAT4356 (Cisco tracking label)
  - STORM-1849 (tracking label)
associated_malware:
  - "[[30_CIPHER/05_Malware/S1188 - Line Runner|Line Runner (S1188)]]"
  - "[[30_CIPHER/05_Malware/S1186 - Line Dancer|Line Dancer (S1186)]]"
target_geography:
  - Global (gov/critical infrastructure focus)
target_sectors:
  - Government
  - Critical infrastructure
  - Perimeter/security appliances (VPN edge)
goals:
  - Espionage; perimeter persistence; device-level collection and exfiltration
intel_sources:
  - https://attack.mitre.org/campaigns/C0046/
  - https://blog.talosintelligence.com/arcanedoor/
  - https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns
---

# ArcaneDoor (C0046)

## Executive synopsis
A sophisticated campaign targeting Cisco (and other) network edge devices, delivering custom implants (Line Runner / Line Dancer) and enabling long-term access, traffic interception, data collection (including packet capture), and exfiltration. Public reporting assesses a state-sponsored operator (UAT4356 / STORM-1849).

## Timeline (high level)
- 2023-07: First observed activity
- 2024-04: Last observed activity window in campaign entry

## Initial access
- Abuse of WebVPN / clientless SSLVPN surfaces to achieve unauthorized code execution on targeted appliances (as described by authoring agencies).
- Follow-on persistence via Lua-based webshell/backdoor mechanisms.

## Tradecraft (ATT&CK highlights)
- Persistence / execution on appliance:
  - Boot/init scripts; Lua execution via legitimate-looking URIs
- Defense evasion:
  - Disable/modify logging (including syslog and command history)
  - Authentication process manipulation (AAA bypass/modification)
- Collection:
  - Automated collection of configs and packet captures
- Exfiltration:
  - Exfil over existing C2 channels / scripted export
- Network manipulation:
  - Adversary-in-the-middle style interception of HTTP flows on the device

## Malware / tooling
- Line Runner (S1188): persistent Lua webshell/backdoor leveraging device customization pathways
- Line Dancer (S1186): memory-resident loader enabling shellcode execution and deeper control

## IOC / artifact summary (starter set)
- HTTP patterns (reported examples):
  - Suspicious GETs to AnyConnect/WebVPN URIs with randomized query keys carrying URL-encoded Lua
  - POSTs to WebVPN endpoints with base64-encoded payload blobs (victim-specific gating values reported)
- Device behavior:
  - Unexpected packet capture session creation
  - Sudden logging disablement and config export artifacts

## Detection & hunting (practical)
- Edge telemetry:
  - Centralize ASA/FTD logs; alert on toggling of syslog/AAA changes and unusual WebVPN requests
- Network monitoring:
  - Detect anomalous HTTP request patterns to WebVPN endpoints with abnormal query entropy
- Response posture:
  - Treat suspected compromise as device integrity event; plan for evidence preservation + vendor-guided remediation

## Risks & implications
- Edge-device compromise undermines “trusted perimeter” assumptions and can enable credential capture, session hijacking, and stealthy exfiltration.
- Multi-layered persistence and logging impairment elevate dwell-time risk.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0046 - ArcaneDoor|ArcaneDoor (C0046)]]
- Malware: [[30_CIPHER/05_Malware/S1188 - Line Runner|Line Runner (S1188)]], [[30_CIPHER/05_Malware/S1186 - Line Dancer|Line Dancer (S1186)]]

## Recommended OSINT queries
- "C0046 ArcaneDoor Line Runner Line Dancer"
- "UAT4356 STORM-1849 Cisco ASA WebVPN Lua webshell"
- "cyber.gc.ca Cyber Activity Impacting CISCO ASA VPNs artifacts"
- "Talos ArcaneDoor indicators"

## Confidence
High on tradecraft and implant set (detailed multi-agency + vendor reporting). Medium on broader vendor scope and full targeting set (varies by reporting).

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
