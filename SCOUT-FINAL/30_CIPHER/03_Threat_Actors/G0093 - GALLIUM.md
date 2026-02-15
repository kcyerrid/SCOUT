---
entity_type: threat_actor
actor_name: "GALLIUM"
common_name: "GALLIUM"
actor_id: "G0093"
actor_type: "State-linked (cyber espionage)"
aliases:
  - "Granite Typhoon"
country_of_origin: "China (likely)"
suspected_sponsors:
  - "China (likely state-sponsored)"
attribution_confidence: "Medium"
first_seen: "2012-01-01"
last_seen: ""
status: "Active"

motivations:
  - "Espionage"
objectives:
  - "Access and persistence within telecommunications providers and related sectors"
victimology_summary: "Likely Chinese state-sponsored group targeting telecommunications providers; activity reported since at least 2012 with victim organizations across multiple regions."
target_sectors:
  - "Telecommunications"
target_regions:
  - "Afghanistan"
  - "Australia"
  - "Bangladesh"
  - "India"
  - "Indonesia"
  - "Malaysia"
  - "Mongolia"
  - "Mozambique"
  - "Nepal"
  - "Philippines"
  - "Russia"
  - "Saudi Arabia"
  - "Sri Lanka"
  - "Thailand"
  - "United States"
  - "Vietnam"

related_groups: []

malware:
  - "[[30_CIPHER/05_Malware/S0564 - BlackMould|BlackMould]]"
  - "[[30_CIPHER/05_Malware/S1031 - PingPull|PingPull]]"
  - "[[30_CIPHER/05_Malware/S0012 - PoisonIvy|PoisonIvy]]"
  - "[[30_CIPHER/05_Malware/S0020 - China Chopper|China Chopper]]"
tools:
  - "[[30_CIPHER/05_Malware/S0110 - at|at]]"
  - "[[30_CIPHER/05_Malware/S0106 - cmd|cmd]]"
  - "[[30_CIPHER/05_Malware/S0040 - HTRAN|HTRAN]]"
  - "[[30_CIPHER/05_Malware/S0100 - ipconfig|ipconfig]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0590 - NBTscan|NBTscan]]"
  - "[[30_CIPHER/05_Malware/S0039 - Net|Net]]"
  - "[[30_CIPHER/05_Malware/S0097 - Ping|Ping]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]"
  - "[[30_CIPHER/05_Malware/S0075 - Reg|Reg]]"
  - "[[30_CIPHER/05_Malware/S0005 - Windows Credential Editor|Windows Credential Editor]]"

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190]]"
  - "[[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105]]"
  - "[[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001]]"
  - "[[20_Entities/07_TTPs/T1550.002 - Pass the Hash|T1550.002]]"
  - "[[20_Entities/07_TTPs/T1021.002 - SMB - Windows Admin Shares|T1021.002]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001]]"

notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0093/"
  - "https://www.microsoft.com/en-us/security/blog/2019/12/12/gallium-targeting-global-telecom/"
tags:
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0093"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
GALLIUM (G0093) is assessed in ATT&CK as a **likely Chinese state-sponsored** cyber espionage actor active since at least **2012**, primarily targeting **telecommunications providers** across a wide geographic footprint.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0093
- **Associated name/cluster:** Granite Typhoon
- **Confidence:** Medium (ATT&CK uses “likely” language regarding state sponsorship).

## 3. Motivations & Objectives
- **Motivation:** Espionage.
- **Objectives:** Long-term access to telecom environments; collection and operational leverage via provider networks.

## 4. Targeting Profile
- **Primary sector:** Telecommunications (with reporting indicating broader spillover in some research).
- **Geography:** Multi-region targeting across APAC, Middle East, Europe, Africa, and North America (see YAML target list).

## 5. Tradecraft Overview
Notable ATT&CK-mapped behaviors include:
- **Entry via exposed services** (public-facing application exploitation and web shell placement).
- **Payload transfer** and multi-stage tooling delivery.
- **Credential access** and alternate authentication (LSASS dumping; pass-the-hash).
- **Lateral movement** via SMB/admin shares and remote execution tooling (e.g., PsExec).
- **Reconnaissance** via common Windows utilities and discovery commands.
- **Proxying/tunneling** (e.g., HTRAN) to pivot and obscure operator origin.
- **Custom malware** families (e.g., BlackMould, PingPull) and legacy RAT usage (e.g., PoisonIvy).

## 6. MITRE ATT&CK Mapping (Key TTPs)
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190]] — Initial foothold via exploitation.
- [[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003]] — Web shell persistence/command execution on servers.
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105]] — Tooling staging and delivery.
- [[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001]] — Credential dumping.
- [[20_Entities/07_TTPs/T1550.002 - Pass the Hash|T1550.002]] — Alternate auth for movement.
- [[20_Entities/07_TTPs/T1021.002 - SMB - Windows Admin Shares|T1021.002]] — Lateral movement in Windows estates.
- [[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003]] — Command execution.
- [[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001]] — C2 patterns over web protocols.

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0564 - BlackMould|BlackMould]]
  - [[30_CIPHER/05_Malware/S1031 - PingPull|PingPull]]
  - [[30_CIPHER/05_Malware/S0012 - PoisonIvy|PoisonIvy]]
  - [[30_CIPHER/05_Malware/S0020 - China Chopper|China Chopper]]
- Tools/Utilities (ATT&CK Software mappings):
  - [[30_CIPHER/05_Malware/S0040 - HTRAN|HTRAN]]
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]
  - [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]
  - [[30_CIPHER/05_Malware/S0005 - Windows Credential Editor|Windows Credential Editor]]
  - Plus common Windows utilities: cmd, net, ping, ipconfig, reg, at, NBTscan.

## 8. Infrastructure Patterns
- Web-facing compromise paths (exposed apps → web shells).
- Use of proxy tooling and multi-hop staging common to long-dwell espionage.
- Likely segmentation-aware pivots within provider networks.

## 9. Campaign History
- Reporting includes multiple waves against telecommunications providers; ATT&CK references include Microsoft threat intelligence and additional vendor research.

## 10. Known Indicators
- Prioritize behavioral detections over static IOCs:
  - Web shell file writes and suspicious IIS/Apache child processes.
  - LSASS access patterns and credential dumping artifacts.
  - PsExec service creation and remote service execution.
  - HTRAN-like proxy process patterns and unusual internal proxying.

## 11. Defensive Recommendations
- Patch management and perimeter hardening for internet-facing services; WAF with robust web shell detection.
- Server telemetry: command-line capture, module loads, suspicious child process relationships from web servers.
- Credential protections: restrict admin credential reuse; enforce MFA for privileged access; monitor pass-the-hash indicators.
- Network detection: internal proxy/tunnel anomalies; lateral SMB admin share access spikes.

## 12. Analyst Notes
- Telecom environments often have high value and complex trust boundaries; focus detections on **server-side tradecraft** and **credential movement**.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0093/
- Microsoft Threat Intelligence: https://www.microsoft.com/en-us/security/blog/2019/12/12/gallium-targeting-global-telecom/

## 14. References
- MITRE ATT&CK. (n.d.). *GALLIUM (G0093).* https://attack.mitre.org/groups/G0093/
- Microsoft Threat Intelligence Center. (2019, December 12). *GALLIUM: Targeting global telecom.* Microsoft Security Blog. https://www.microsoft.com/en-us/security/blog/2019/12/12/gallium-targeting-global-telecom/
