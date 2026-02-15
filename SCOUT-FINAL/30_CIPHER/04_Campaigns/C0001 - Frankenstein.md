---
entity_type: campaign

campaign_name: "Frankenstein"
campaign_id: "C0001"
aliases: []
tlp_classification: "TLP:CLEAR"

associated_threat_actors: []
suspected_threat_actors: []
attribution_confidence: "1-low"
confidence_notes: "Unattributed activity; described as moderately sophisticated and highly resourceful, relying on open-source tooling."

first_observed: "2019-01"
last_observed: "2019-04"
campaign_status: "historic"

primary_objectives:
  - "Initial Access"
  - "Execution"
  - "Collection"
  - "Exfiltration"
secondary_objectives:
  - "Defense Evasion"
  - "Discovery"
  - "Persistence"

target_sectors:
  - "Unknown (highly-targeted)"
target_regions:
  - "Unknown"
target_technologies:
  - "Windows"
  - "Microsoft Office"

initial_access_vectors:
  - "Spearphishing Attachment"
  - "Template Injection"
  - "Client-side Exploitation"

associated_ttps:
  - "T1071.001 - Web Protocols"
  - "T1119 - Automated Collection"
  - "T1020 - Automated Exfiltration"
  - "T1059.001 - PowerShell"
  - "T1059.003 - Windows Command Shell"
  - "T1059.005 - Visual Basic"
  - "T1005 - Data from Local System"
  - "T1140 - Deobfuscate/Decode Files or Information"
  - "T1573.001 - Symmetric Cryptography"
  - "T1041 - Exfiltration Over C2 Channel"
  - "T1203 - Exploitation for Client Execution"
  - "T1105 - Ingress Tool Transfer"
  - "T1036.004 - Masquerade Task or Service"
  - "T1027.010 - Command Obfuscation"
  - "T1588.002 - Tool"
  - "T1566.001 - Spearphishing Attachment"
  - "T1057 - Process Discovery"
  - "T1053.005 - Scheduled Task"
  - "T1518.001 - Security Software Discovery"
  - "T1082 - System Information Discovery"
  - "T1016 - System Network Configuration Discovery"
  - "T1033 - System Owner/User Discovery"
  - "T1221 - Template Injection"
  - "T1127.001 - MSBuild"
  - "T1204.002 - Malicious File"
  - "T1497.001 - System Checks"
  - "T1047 - Windows Management Instrumentation"

malware_families: []
tools_used:
  - "[[30_CIPHER/05_Malware/S0363 - Empire|Empire (S0363)]]"

infrastructure_patterns:
  - "Web-based C2"
  - "Use of public tooling and staged components"

notable_victims: []
related_incidents: []

risk_level: "Medium"
impact_assessment: "Credential and data theft potential through staged collection and automated exfiltration behaviors."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0001/"
  - "https://blog.talosintelligence.com/frankenstein-campaign/"
  - "https://www.bleepingcomputer.com/news/security/attackers-stitch-together-frankenstein-campaign-using-free-tools/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Frankenstein (C0001)

## 1. Executive Summary
**Frankenstein** is a highly-targeted intrusion campaign observed in early 2019. Reporting describes the operators as moderately sophisticated and “resourceful,” assembling a toolchain from multiple open-source components and leveraging **[[30_CIPHER/05_Malware/S0363 - Empire|Empire (S0363)]]** to support post-compromise activity.

## 2. Technical Overview
Frankenstein tradecraft emphasizes modular staging and “cobbled together” components:
- Initial access via phishing and document-based delivery paths.
- Execution via scripting (PowerShell, Windows command shell, VB) and build/proxy execution mechanisms.
- Collection and exfiltration automation, including web-protocol C2 and encrypted channels.

## 3. Associated MITRE ATT&CK Techniques
- [[T1071.001 - Web Protocols]]
- [[T1119 - Automated Collection]]
- [[T1020 - Automated Exfiltration]]
- [[T1059.001 - PowerShell]]
- [[T1059.003 - Windows Command Shell]]
- [[T1059.005 - Visual Basic]]
- [[T1005 - Data from Local System]]
- [[T1140 - Deobfuscate/Decode Files or Information]]
- [[T1573.001 - Symmetric Cryptography]]
- [[T1041 - Exfiltration Over C2 Channel]]
- [[T1203 - Exploitation for Client Execution]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1036.004 - Masquerade Task or Service]]
- [[T1027.010 - Command Obfuscation]]
- [[T1588.002 - Tool]]
- [[T1566.001 - Spearphishing Attachment]]
- [[T1057 - Process Discovery]]
- [[T1053.005 - Scheduled Task]]
- [[T1518.001 - Security Software Discovery]]
- [[T1082 - System Information Discovery]]
- [[T1016 - System Network Configuration Discovery]]
- [[T1033 - System Owner/User Discovery]]
- [[T1221 - Template Injection]]
- [[T1127.001 - MSBuild]]
- [[T1204.002 - Malicious File]]
- [[T1497.001 - System Checks]]
- [[T1047 - Windows Management Instrumentation]]

## 4. Malware & Tooling
**Tools Used**
- [[30_CIPHER/05_Malware/S0363 - Empire|Empire (S0363)]]

## 5. Infrastructure & Operational Patterns
- Web-protocol command and control with encrypted/obfuscated command and data flows.
- Staged tool transfer and modular payload assembly to reduce unique on-disk artifacts.

## 6. Timeline (Chronos)
```chronos
- [2019-01] First observed activity timeframe begins (campaign reporting)
- [2019-04] Last observed activity timeframe ends (campaign reporting)
- [2019-06-04] Public reporting: Talos publishes analysis of “Frankenstein” campaign
- [2019-06-04] Public reporting: BleepingComputer summary coverage of Talos findings
- [2022-09-07] MITRE ATT&CK creates campaign entry (C0001)
```

## 7. Timeline of Campaign Activity (Markdown)
| Date | Event |
|---|---|
| 2019-01 | First observed activity timeframe begins (campaign reporting) |
| 2019-04 | Last observed activity timeframe ends (campaign reporting) |
| 2019-06-04 | Talos publishes “Frankenstein campaign” analysis |
| 2019-06-04 | BleepingComputer publishes coverage of the campaign |
| 2022-09-07 | MITRE ATT&CK creates campaign entry (C0001) |

## 8. Defensive Recommendations
- Prioritize detections for **template injection** and unusual Office remote template fetches.
- Alert on **Empire**-like staging behaviors: script-heavy execution, ingress tool transfer, scheduled tasks.
- Correlate **process discovery + security software discovery** shortly after user execution events.

## 9. Analyst Notes
Frankenstein is a good “composition” case: defenders should focus on **behavioral chains** (phish → script exec → staging → C2) rather than single-file signatures.

## 10. References (APA)
- Cisco Talos. (2019, June 4). *It’s alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign*. https://blog.talosintelligence.com/frankenstein-campaign/
- MITRE ATT&CK. (n.d.). *Frankenstein (Campaign C0001)*. Retrieved 2026-01-02, from https://attack.mitre.org/campaigns/C0001/
- Gatlan, S. (2019, June 4). *Attackers stitch together Frankenstein campaign using free tools*. *BleepingComputer*. https://www.bleepingcomputer.com/news/security/attackers-stitch-together-frankenstein-campaign-using-free-tools/
