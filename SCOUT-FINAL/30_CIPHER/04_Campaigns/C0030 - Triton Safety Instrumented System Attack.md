---
entity_type: campaign

campaign_name: "Triton Safety Instrumented System Attack"
campaign_id: "C0030"
aliases:
  - "TRITON / TRISIS incident (SIS-focused)"
status: "inactive"
risk_level: "critical"

first_seen: "2017-06"
last_seen: "2017-08"

attribution:
  associated_threat_actors:
    - "[[30_CIPHER/03_Threat_Actors/G0088 - TEMP.Veles|TEMP.Veles (G0088)]]"
  suspected_threat_actors: []
  attribution_confidence: "high"
  attribution_notes: "MITRE associates the campaign with TEMP.Veles."

targets:
  regions:
    - "Middle East (reported petrochemical sector incident context)"
  sectors:
    - "Petrochemical / Industrial"
    - "Critical Infrastructure"
  technologies:
    - "Triconex Safety Instrumented Systems (SIS)"
    - "Industrial control environments (ICS/OT)"

initial_access_vectors:
  - "Post-compromise traversal into OT environment via remote services and poor segmentation (reported)"
  - "Credential capture and use of valid accounts"

key_ttp_themes:
  - "Targeted manipulation of safety controllers (SIS)"
  - "Credential access + tool acquisition"
  - "Masquerading and obfuscation"
  - "Remote services into OT environment"

associated_malware:
  - "[[30_CIPHER/05_Malware/S1009 - Triton|Triton (S1009)]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]"

associated_ttps:
  - "T1595 - Active Scanning"
  - "T1059.001 - PowerShell"
  - "T1587.001 - Malware"
  - "T1573 - Encrypted Channel"
  - "T1056.003 - Web Portal Capture"
  - "T1036.005 - Match Legitimate Resource Name or Location"
  - "T1027.005 - Indicator Removal from Tools"
  - "T1588.002 - Tool"
  - "T1003.001 - LSASS Memory"
  - "T1053.005 - Scheduled Task"
  - "T0830 - Adversary-in-the-Middle"
  - "T0807 - Command-Line Interface"
  - "T0872 - Indicator Removal on Host"
  - "T0867 - Lateral Tool Transfer"
  - "T0828 - Loss of Productivity and Revenue"
  - "T0843 - Program Download"
  - "T0886 - Remote Services"
  - "T0853 - Scripting"
  - "T0855 - Unauthorized Command Message"
  - "T0859 - Valid Accounts"

impact_assessment:
  - "Safety trip and plant shutdown attributed to SIS disruption/unsafe state"
  - "Potential for physical consequences in industrial operations"

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0030/"
  - "https://attack.mitre.org/software/S1009/"
  - "https://www.fireeye.com/blog/threat-research/2017/12/attackers_deploy_new_ics_attack_framework_triton.html"
  - "https://cloud.google.com/blog/topics/threat-intelligence/triton-actor-ttp-profile-custom-attack-tools-detections"
  - "https://www.eenews.net/articles/the-inside-story-of-the-worlds-most-dangerous-malware/"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Triton Safety Instrumented System Attack (C0030)

## 1. Executive Summary
**C0030** describes the **SIS-targeting TRITON incident**, attributed by MITRE to **[[30_CIPHER/03_Threat_Actors/G0088 - TEMP.Veles|TEMP.Veles (G0088)]]**, leveraging **[[30_CIPHER/05_Malware/S1009 - Triton|Triton (S1009)]]** to interact with **Triconex safety controllers**. The operation is notable for **high-consequence risk**: the incident was discovered after a **safety trip** caused by an issue in the malware and resulted in operational disruption.

## 2. Campaign Overview
- **Timeframe:** 2017-06 to 2017-08  
- **Objective:** Capability to interfere with safety systems (SIS) and industrial processes.  
- **Operational pattern:** Recon → tool use (PowerShell, Mimikatz) → credential capture → remote services into OT.

## 3. Linked Entities
### Threat Actor
- [[30_CIPHER/03_Threat_Actors/G0088 - TEMP.Veles|TEMP.Veles (G0088)]]

### Malware / Software
- [[30_CIPHER/05_Malware/S1009 - Triton|Triton (S1009)]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]

## 4. Timeline of Campaign Activity (Chronos)
```chronos
- [2017-06] Campaign first observed timeframe (reported).
- [2017-08] Campaign last observed timeframe (reported).
- [2017-12-14] Public disclosure of TRITON framework and operational disruption reporting (vendor publication date).
- [2018-06-07] Deep-dive technical analysis published (historical reference).
- [2019-03-07] Investigative reporting on incident context (historical reference).
```

## 5. Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2017-06 | First observed timeframe (reported) |
| 2017-08 | Last observed timeframe (reported) |
| 2017-12-14 | Public disclosure of TRITON attack framework |
| 2018-06-07 | Additional technical deep-dive published |
| 2019-03-07 | Investigative reporting on incident context |

## 6. MITRE ATT&CK Alignment (Observed TTPs)
- [[T1595 - Active Scanning]]
- [[T1059.001 - PowerShell]]
- [[T1003.001 - LSASS Memory]]
- [[T1053.005 - Scheduled Task]]
- [[T1056.003 - Web Portal Capture]]
- [[T1573 - Encrypted Channel]]
- [[T1036.005 - Match Legitimate Resource Name or Location]]
- [[T1027.005 - Indicator Removal from Tools]]
- [[T1588.002 - Tool]]
- [[T0886 - Remote Services]]
- [[T0855 - Unauthorized Command Message]]
- [[T0859 - Valid Accounts]]

## 7. Defensive Considerations
1. **OT segmentation & access control:** restrict and monitor remote services into OT; enforce jump-box hardening.
2. **SIS/OT telemetry:** alert on abnormal engineering workstation activity and unauthorized program downloads.
3. **Credential protections:** monitor for LSASS access and suspicious credential tooling.
4. **Incident readiness:** ensure safety systems have robust change control and integrity monitoring.

## 8. Analyst Notes
SIS-focused operations are rare and high-impact. Even “failed” attempts can create dangerous conditions or operational shutdowns. Prioritize **engineering network visibility** and **strict remote access governance**.

## 9. References (APA)
- Johnson, B., et al. (2017, December 14). *Attackers Deploy New ICS Attack Framework “TRITON” and Cause Operational Disruption to Critical Infrastructure.* FireEye. https://www.fireeye.com/blog/threat-research/2017/12/attackers_deploy_new_ics_attack_framework_triton.html  
- Miller, S., et al. (2019, April 10). *TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping.* Mandiant. https://cloud.google.com/blog/topics/threat-intelligence/triton-actor-ttp-profile-custom-attack-tools-detections  
- Sobczak, B. (2019, March 7). *The inside story of the world’s most dangerous malware.* E&E News. https://www.eenews.net/articles/the-inside-story-of-the-worlds-most-dangerous-malware/  
- MITRE ATT&CK. (n.d.). *Triton Safety Instrumented System Attack (C0030).* https://attack.mitre.org/campaigns/C0030/
