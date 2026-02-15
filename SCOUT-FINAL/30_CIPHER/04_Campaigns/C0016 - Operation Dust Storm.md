---
entity_type: campaign

campaign_name: "Operation Dust Storm"
campaign_id: "C0016"

associated_actors: []
suspected_actors: []

attribution_confidence: "1-low"
confidence_notes: "Public reporting attributes Operation Dust Storm to an unidentified espionage-focused cluster; no definitive public attribution to a named threat group."

first_observed: "2010-01"
last_observed: "2016-02"
campaign_status: "concluded"

primary_objectives: ["espionage"]
secondary_objectives: ["data_theft"]

target_sectors: ["government", "critical_infrastructure", "telecommunications", "manufacturing"]
target_regions: ["Japan", "South Korea", "United States", "Europe", "Middle East"]
target_technologies: ["Windows", "Android", "Internet Explorer", "web servers"]

initial_access_vectors: ["watering_hole", "spearphishing", "exploit"]
key_ttp_themes: ["web_compromise", "credential_theft", "lateral_movement", "mobile_compromise"]

malware_families: []
tools_used:
  - "[[30_CIPHER/05_Malware/S0001 - Shiva|S0001 - Shiva]]"
  - "[[30_CIPHER/05_Malware/S0110 - at|S0110 - at]]"

infrastructure_patterns: ["watering_hole_sites", "staged_download_servers"]
notable_victims: []
related_incidents: []

risk_level: "medium"
impact_assessment: "Multi-year espionage activity with broad regional targeting and repeated intrusion opportunities via web compromise and exploitation; impact depends on victim environment sensitivity."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0016/"
  - "https://www.cylance.com/en-us/resources/reports/operation-dust-storm.html"
  - "https://www.securityweek.com/operation-dust-storm-cyber-espionage-campaign-targets-japan/"
  - "https://exchange.xforce.ibmcloud.com/collection/Operation-Dust-Storm-Report-9c4f0ab24a5af1b99a97f7034b506498"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
**Operation Dust Storm (C0016)** is a long-running cyber espionage campaign first observed in **January 2010** and last observed in **February 2016**. Public reporting describes broad targeting, including organizations in Japan and other regions, with activity spanning both enterprise environments and mobile ecosystems. The campaign is notable for its **web compromise / watering-hole** component and its mix of tooling across platforms.  
Primary reference: MITRE ATT&CK campaign entry. 

---

## Attribution Assessment
No definitive public attribution to a named threat actor is provided in widely cited sources; confidence remains **low** due to reliance on open reporting and limited victim-side forensic detail.

---

## Objectives & Intent
**Primary:** espionage / intelligence collection  
**Secondary:** credential theft and operational access maintenance

---

## Targeting Analysis
### Sectors Targeted
- Government and public sector entities
- Critical infrastructure-related organizations (per public reporting)
- Telecommunications / manufacturing (reported across victims)

### Regions Targeted
- Strong emphasis on **Japan**, with additional activity reported in other regions.

### Technologies / Platforms Targeted
- Windows endpoints and servers
- Web infrastructure (watering holes / compromised sites)
- Mobile (Android-targeting components reported)

---

## Campaign Tradecraft
### High-Level Tradecraft Summary
Operation Dust Storm leveraged **watering-hole compromises**, exploitation, and multi-stage payload delivery to establish access. Follow-on behavior included credential access, lateral movement, and persistence using both custom malware and built-in OS capabilities.

---

## MITRE ATT&CK Alignment
### Techniques Observed
- [[T1053.002 - At]]
- [[T1059.003 - Windows Command Shell]]
- [[T1068 - Exploitation for Privilege Escalation]]
- [[T1071.001 - Web Protocols]]
- [[T1082 - System Information Discovery]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1110 - Brute Force]]
- [[T1190 - Exploit Public-Facing Application]]
- [[T1203 - Exploitation for Client Execution]]
- [[T1210 - Exploitation of Remote Services]]
- [[T1222.001 - Windows File and Directory Permissions Modification]]
- [[T1505.003 - Web Shell]]
- [[T1543.003 - Windows Service]]
- [[T1550.003 - Pass the Ticket]]
- [[T1557.001 - LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1560.001 - Archive via Utility]]
- [[T1562.001 - Disable or Modify Tools]]
- [[T1573.001 - Symmetric Cryptography]]
- [[T1587.001 - Malware]]
- [[T1611 - Escape to Host]]

### Notable Tradecraft Characteristics
- Emphasis on **watering-hole** driven initial access and follow-on exploitation.
- Use of built-in scheduling/command execution (e.g., **at**).

---

## Malware & Tooling
### Malware Families / Software
- [[30_CIPHER/05_Malware/S0001 - Shiva|S0001 - Shiva]] (reported usage in the campaign context)
- [[30_CIPHER/05_Malware/S0110 - at|S0110 - at]] (abused for scheduling / execution)

### Tools (LOLBins / Native)
- Task scheduling via **at**
- Shell execution via **cmd.exe**

---

## Infrastructure & Operational Patterns
- Compromised web properties used as **watering holes**
- Staging servers for payload delivery (varies by victim set)

---

## Timeline of Campaign Activity (Chronos)
```chronos
- [2010-01]: Earliest public observation of Operation Dust Storm activity.
- [2014-02]: Public reporting highlights watering-hole/exploit activity used to compromise targets.
- [2015-01]: Reporting indicates continued targeting with evolving tooling and infrastructure.
- [2016-02]: Last publicly reported observation of campaign activity.
- [2016-02-23]: Public report(s) describing Operation Dust Storm published.
```

## Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2010-01 | Earliest public observation of Operation Dust Storm activity |
| 2014-02 | Watering-hole / exploit activity reported in campaign coverage |
| 2015-01 | Continued targeting with evolving tooling and infrastructure |
| 2016-02 | Last publicly reported observation of campaign activity |
| 2016-02-23 | Public reporting released describing Operation Dust Storm |

---

## Notable Victims & Impact
Public reporting emphasizes espionage impact; victim-specific details vary by source and are often anonymized.

---

## Defensive Considerations
- Monitor for anomalous **webshell** placement and suspicious IIS/Apache execution chains.
- Alert on unusual **task scheduling** activity (including `at`) and unexpected service creation.
- Harden and monitor externally exposed web applications; prioritize patching and WAF telemetry.

---

## Analyst Notes
Operation Dust Storm illustrates how **web compromise + exploitation** can sustain multi-year access against diverse targets. Detection typically requires correlating web telemetry with endpoint behavior and credential access patterns.

---

## References (APA)
- MITRE ATT&CK. (2024, April 11). *Operation Dust Storm (C0016)*. Retrieved 2026-01-03 from https://attack.mitre.org/campaigns/C0016/
- Gross, J. (2016, February 23). *Operation Dust Storm* [Report]. Cylance. Retrieved 2026-01-03 from https://www.cylance.com/en-us/resources/reports/operation-dust-storm.html
- SecurityWeek. (2016, February 23). *Operation Dust Storm cyber espionage campaign targets Japan*. Retrieved 2026-01-03 from https://www.securityweek.com/operation-dust-storm-cyber-espionage-campaign-targets-japan/
- IBM X-Force Exchange. (n.d.). *Operation Dust Storm Report* [Collection]. Retrieved 2026-01-03 from https://exchange.xforce.ibmcloud.com/collection/Operation-Dust-Storm-Report-9c4f0ab24a5af1b99a97f7034b506498
