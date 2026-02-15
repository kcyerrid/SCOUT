---
entity_type: campaign

campaign_name: "FunnyDream"
campaign_id: "C0007"
aliases: []
tlp_classification: "TLP:CLEAR"

associated_threat_actors: []
suspected_threat_actors:
  - "TAG-16 (non-MITRE designation; infrastructure overlap reported)"
attribution_confidence: "2-medium"
confidence_notes: "Suspected Chinese cyber espionage; multiple reports cite Chinoxy use and infrastructure overlap with TAG-16."

first_observed: "2018-07"
last_observed: "2020-11"
campaign_status: "historic"

primary_objectives:
  - "Espionage"
  - "Discovery"
  - "Collection"
secondary_objectives:
  - "Ingress Tool Transfer"
  - "Remote Administration"

target_sectors:
  - "Government"
  - "Foreign organizations"
target_regions:
  - "Malaysia"
  - "Philippines"
  - "Taiwan"
  - "Vietnam"
  - "Southeast Asia (broader)"
target_technologies:
  - "Windows"
  - "Internal networks (mapping / remote command execution)"

initial_access_vectors:
  - "Malware/tool deployment post-compromise (per reporting)"

associated_ttps:
  - "T1583.001 - Domains"
  - "T1560.001 - Archive via Utility"
  - "T1059.003 - Windows Command Shell"
  - "T1059.005 - Visual Basic"
  - "T1585.002 - Email Accounts"
  - "T1105 - Ingress Tool Transfer"
  - "T1588.001 - Malware"
  - "T1588.002 - Tool"
  - "T1057 - Process Discovery"
  - "T1018 - Remote System Discovery"
  - "T1082 - System Information Discovery"
  - "T1016 - System Network Configuration Discovery"
  - "T1049 - System Network Connections Discovery"
  - "T1047 - Windows Management Instrumentation"

malware_families:
  - "[[30_CIPHER/05_Malware/S1041 - Chinoxy|Chinoxy (S1041)]]"
  - "[[30_CIPHER/05_Malware/S1044 - FunnyDream|FunnyDream (S1044)]]"
  - "[[30_CIPHER/05_Malware/S1043 - ccf32|ccf32 (S1043)]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S1050 - PcShare|PcShare (S1050)]]"
  - "[[30_CIPHER/05_Malware/S0100 - ipconfig|ipconfig (S0100)]]"
  - "[[30_CIPHER/05_Malware/S0104 - netstat|netstat (S0104)]]"
  - "[[30_CIPHER/05_Malware/S0096 - Systeminfo|Systeminfo (S0096)]]"
  - "[[30_CIPHER/05_Malware/S0057 - Tasklist|Tasklist (S0057)]]"

infrastructure_patterns:
  - "Registered domains and email-account supported registration"
  - "Reported infra overlap with TAG-16-linked activity"

notable_victims: []
related_incidents: []

risk_level: "High"
impact_assessment: "Regional espionage with remote execution tooling, discovery at scale, and custom backdoors used for persistence and component deployment."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0007/"
  - "https://www.bitdefender.com/blog/labs/dissecting-a-chinese-apt-targeting-south-eastern-asian-government-institutions/"
  - "https://securelist.com/apt-trends-report-q1-2020/96826/"
  - "https://www.recordedfuture.com/blog/chinese-state-sponsored-cyber-espionage-expansion-power-influence-southeast-asia"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# FunnyDream (C0007)

## 1. Executive Summary
**FunnyDream** is a suspected Chinese cyber-espionage campaign targeting government and foreign organizations across Southeast Asia. Reporting links activity to Chinese-speaking operators through use of **Chinoxy** and notes infrastructure overlap with **TAG-16**.

## 2. Technical Overview
Commonly reported elements:
- Custom backdoors (**Chinoxy**, **FunnyDream**) and collection component (**ccf32**).
- Tooling includes a modified **PcShare** remote administration tool.
- Discovery and network mapping using built-in utilities and WMI-based remote command execution.

## 3. Associated MITRE ATT&CK Techniques
- [[T1583.001 - Domains]]
- [[T1560.001 - Archive via Utility]]
- [[T1059.003 - Windows Command Shell]]
- [[T1059.005 - Visual Basic]]
- [[T1585.002 - Email Accounts]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1588.001 - Malware]]
- [[T1588.002 - Tool]]
- [[T1057 - Process Discovery]]
- [[T1018 - Remote System Discovery]]
- [[T1082 - System Information Discovery]]
- [[T1016 - System Network Configuration Discovery]]
- [[T1049 - System Network Connections Discovery]]
- [[T1047 - Windows Management Instrumentation]]

## 4. Malware & Tooling (Atomic Links)
**Malware Families**
- [[30_CIPHER/05_Malware/S1041 - Chinoxy|Chinoxy (S1041)]]
- [[30_CIPHER/05_Malware/S1044 - FunnyDream|FunnyDream (S1044)]]
- [[30_CIPHER/05_Malware/S1043 - ccf32|ccf32 (S1043)]]

**Tools Used**
- [[30_CIPHER/05_Malware/S1050 - PcShare|PcShare (S1050)]]
- [[30_CIPHER/05_Malware/S0100 - ipconfig|ipconfig (S0100)]]
- [[30_CIPHER/05_Malware/S0104 - netstat|netstat (S0104)]]
- [[30_CIPHER/05_Malware/S0096 - Systeminfo|Systeminfo (S0096)]]
- [[30_CIPHER/05_Malware/S0057 - Tasklist|Tasklist (S0057)]]

## 5. Timeline (Chronos)
```chronos
- [2018-07] First observed timeframe begins (MITRE reporting window)
- [2020-11] Last observed timeframe ends (MITRE reporting window)
- [2020-04-30] Kaspersky GReAT publishes APT trends report (Q1 2020) referenced by MITRE
- [2020-11] Bitdefender publishes primary “FunnyDream” report
- [2021-12-08] Recorded Future (Insikt Group) publishes Southeast Asia espionage reporting referencing TAG-16
```

## 6. Timeline of Campaign Activity (Markdown)
| Date | Event |
|---|---|
| 2018-07 | First observed timeframe begins (MITRE reporting window) |
| 2020-11 | Last observed timeframe ends (MITRE reporting window) |
| 2020-04-30 | Kaspersky GReAT publishes APT trends report (Q1 2020) |
| 2020-11 | Bitdefender publishes primary “FunnyDream” report |
| 2021-12-08 | Recorded Future publishes Southeast Asia espionage reporting referencing TAG-16 |

## 7. Defensive Recommendations
- Detect creation/use of **RAR/7z** archives for staging (especially paired with exfil paths).
- Monitor for remote command execution patterns via **WMI** and scripted wmiexec-style behavior.
- Watch for anomalous network mapping using built-in tools (ipconfig/netstat) at scale across hosts.

## 8. References (APA)
- Bitdefender. (2020, November). *Dissecting a Chinese APT targeting South Eastern Asian government institutions*. https://www.bitdefender.com/blog/labs/dissecting-a-chinese-apt-targeting-south-eastern-asian-government-institutions/
- Insikt Group. (2021, December 8). *Chinese state-sponsored cyber espionage activity supports expansion of regional power and influence in Southeast Asia*. *Recorded Future*. https://www.recordedfuture.com/blog/chinese-state-sponsored-cyber-espionage-expansion-power-influence-southeast-asia
- Kaspersky Global Research & Analysis Team. (2020, April 30). *APT trends report Q1 2020*. https://securelist.com/apt-trends-report-q1-2020/96826/
- MITRE ATT&CK. (n.d.). *FunnyDream (Campaign C0007)*. Retrieved 2026-01-02, from https://attack.mitre.org/campaigns/C0007/
