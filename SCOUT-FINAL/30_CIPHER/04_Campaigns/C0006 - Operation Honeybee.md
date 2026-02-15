---
entity_type: campaign

campaign_name: "Operation Honeybee"
campaign_id: "C0006"
aliases: []
tlp_classification: "TLP:CLEAR"

associated_threat_actors: []
suspected_threat_actors: []
attribution_confidence: "2-medium"
confidence_notes: "Researchers assessed likely Korean-speaking operators based on metadata and lure artifacts; no definitive group attribution."

first_observed: "2017-08"
last_observed: "2018-02"
campaign_status: "historic"

primary_objectives:
  - "Initial Access"
  - "Execution"
  - "Collection"
  - "Exfiltration"
secondary_objectives:
  - "Persistence"
  - "Defense Evasion"
  - "Privilege Escalation"

target_sectors:
  - "Humanitarian aid organizations"
  - "Inter-Korean affairs organizations"
target_regions:
  - "South Korea"
  - "Vietnam"
  - "Singapore"
  - "Japan"
  - "Indonesia"
  - "Argentina"
  - "Canada"
target_technologies:
  - "Windows"
  - "Microsoft Office (macro/doc delivery)"

initial_access_vectors:
  - "Malicious Office documents / macro-enabled execution"

associated_ttps:
  - "T1548.002 - Bypass User Account Control"
  - "T1583.001 - Domains"
  - "T1583.004 - Server"
  - "T1071.002 - File Transfer Protocols"
  - "T1560.001 - Archive via Utility"
  - "T1059.003 - Windows Command Shell"
  - "T1059.005 - Visual Basic"
  - "T1543.003 - Windows Service"
  - "T1005 - Data from Local System"
  - "T1074.001 - Local Data Staging"
  - "T1140 - Deobfuscate/Decode Files or Information"
  - "T1585.002 - Email Accounts"
  - "T1041 - Exfiltration Over C2 Channel"
  - "T1083 - File and Directory Discovery"
  - "T1574.011 - Services Registry Permissions Weakness"
  - "T1070.004 - File Deletion"
  - "T1105 - Ingress Tool Transfer"
  - "T1036 - Masquerading"
  - "T1036.005 - Match Legitimate Resource Name or Location"
  - "T1112 - Modify Registry"
  - "T1106 - Native API"
  - "T1027.013 - Encrypted/Encoded File"
  - "T1588.004 - Digital Certificates"
  - "T1057 - Process Discovery"
  - "T1553.002 - Code Signing"
  - "T1082 - System Information Discovery"
  - "T1569.002 - Service Execution"
  - "T1204.002 - Malicious File"

malware_families:
  - "[[30_CIPHER/05_Malware/S0464 - SYSCON|SYSCON (S0464)]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0106 - cmd|cmd (S0106)]]"
  - "[[30_CIPHER/05_Malware/S0075 - Reg|Reg (S0075)]]"
  - "[[30_CIPHER/05_Malware/S0096 - Systeminfo|Systeminfo (S0096)]]"
  - "[[30_CIPHER/05_Malware/S0057 - Tasklist|Tasklist (S0057)]]"

infrastructure_patterns:
  - "Registered domains and control servers"
  - "Possible FTP-based C2 capability"
  - "Use of stolen digital signing certificate(s) reported"

notable_victims: []
related_incidents: []

risk_level: "Medium"
impact_assessment: "Targeted document-driven intrusion with service-based persistence and data staging/exfiltration patterns."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0006/"
  - "https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Operation Honeybee (C0006)

## 1. Executive Summary
**Operation Honeybee** targeted humanitarian aid and inter-Korean affairs organizations from at least late 2017 through early 2018, beginning with South Korea and expanding to multiple countries. Reporting assessed likely Korean-speaking operators based on metadata in lures/executables.

## 2. Technical Overview
Observed tradecraft includes:
- Malicious documents and macro-driven execution.
- Service-based persistence and service hijacking behaviors.
- Staged local collection and compression prior to exfiltration.
- Use of trust subversion (reported stolen digital signature) to increase execution success.

## 3. Associated MITRE ATT&CK Techniques
- [[T1548.002 - Bypass User Account Control]]
- [[T1583.001 - Domains]]
- [[T1583.004 - Server]]
- [[T1071.002 - File Transfer Protocols]]
- [[T1560.001 - Archive via Utility]]
- [[T1059.003 - Windows Command Shell]]
- [[T1059.005 - Visual Basic]]
- [[T1543.003 - Windows Service]]
- [[T1005 - Data from Local System]]
- [[T1074.001 - Local Data Staging]]
- [[T1140 - Deobfuscate/Decode Files or Information]]
- [[T1585.002 - Email Accounts]]
- [[T1041 - Exfiltration Over C2 Channel]]
- [[T1083 - File and Directory Discovery]]
- [[T1574.011 - Services Registry Permissions Weakness]]
- [[T1070.004 - File Deletion]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1036 - Masquerading]]
- [[T1036.005 - Match Legitimate Resource Name or Location]]
- [[T1112 - Modify Registry]]
- [[T1106 - Native API]]
- [[T1027.013 - Encrypted/Encoded File]]
- [[T1588.004 - Digital Certificates]]
- [[T1057 - Process Discovery]]
- [[T1553.002 - Code Signing]]
- [[T1082 - System Information Discovery]]
- [[T1569.002 - Service Execution]]
- [[T1204.002 - Malicious File]]

## 4. Malware & Tooling (Atomic Links)
**Malware Families**
- [[30_CIPHER/05_Malware/S0464 - SYSCON|SYSCON (S0464)]]

**Tools Used**
- [[30_CIPHER/05_Malware/S0106 - cmd|cmd (S0106)]]
- [[30_CIPHER/05_Malware/S0075 - Reg|Reg (S0075)]]
- [[30_CIPHER/05_Malware/S0096 - Systeminfo|Systeminfo (S0096)]]
- [[30_CIPHER/05_Malware/S0057 - Tasklist|Tasklist (S0057)]]

## 5. Timeline (Chronos)
```chronos
- [2017-08] First observed timeframe begins (MITRE reporting window)
- [2018-02] Last observed timeframe ends (MITRE reporting window)
- [2018-03-02] McAfee publishes primary “Operation Honeybee” report
- [2022-09-16] MITRE ATT&CK creates campaign entry (C0006)
- [2024-04-11] MITRE ATT&CK updates campaign entry (C0006)
```

## 6. Timeline of Campaign Activity (Markdown)
| Date | Event |
|---|---|
| 2017-08 | First observed timeframe begins (MITRE reporting window) |
| 2018-02 | Last observed timeframe ends (MITRE reporting window) |
| 2018-03-02 | McAfee publishes primary “Operation Honeybee” report |
| 2022-09-16 | MITRE ATT&CK creates campaign entry (C0006) |
| 2024-04-11 | MITRE ATT&CK updates campaign entry (C0006) |

## 7. Defensive Recommendations
- Enforce and monitor **macro policies**; alert on Office spawning script interpreters.
- Watch for **new/modified Windows services** and suspicious service DLL loading paths.
- Detect suspicious **tasklist/systeminfo** output redirection and staged archive creation before exfiltration.

## 8. References (APA)
- McAfee. (2018, March 2). *McAfee uncovers Operation Honeybee, a malicious document campaign targeting humanitarian aid groups*. https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/
- MITRE ATT&CK. (n.d.). *Operation Honeybee (Campaign C0006)*. Retrieved 2026-01-02, from https://attack.mitre.org/campaigns/C0006/
