---
entity_type: campaign

campaign_name: "AvosLocker Ransomware Intrusion (C0018)"
campaign_id: "C0018"

associated_actors: []
suspected_actors: []

attribution_confidence: "2-medium"
confidence_notes: "Public reporting provides detailed technical tradecraft but does not name a definitive threat actor; activity is treated as an unidentified ransomware intrusion aligned to AvosLocker deployment."

first_observed: "2022-02"
last_observed: "2022-03"
campaign_status: "concluded"

primary_objectives: ["extortion"]
secondary_objectives: ["data_theft", "impact"]

target_sectors: ["unknown"]
target_regions: ["unknown"]
target_technologies: ["VMware Horizon UAG", "Windows", "RDP", "PowerShell"]

initial_access_vectors: ["exploit_public_facing_application"]
key_ttp_themes: ["log4shell_exploitation", "tool_staging", "rdp_lateral_movement", "ransomware_deployment"]

malware_families:
  - "[[30_CIPHER/05_Malware/S1053 - AvosLocker|S1053 - AvosLocker]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|S0154 - Cobalt Strike]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|S0002 - Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0633 - Sliver|S0633 - Sliver]]"
  - "[[30_CIPHER/05_Malware/S0108 - netsh|S0108 - netsh]]"
  - "[[30_CIPHER/05_Malware/S0097 - Ping|S0097 - Ping]]"

infrastructure_patterns: ["http_c2", "tool_download_staging"]
notable_victims: []
related_incidents: []

risk_level: "high"
impact_assessment: "Ransomware intrusion culminating in enterprise-wide file encryption using AvosLocker; tradecraft includes exploitation of exposed services, extensive tool staging, and lateral movement via RDP."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0018/"
  - "https://blog.talosintelligence.com/avos-ransomware-group-expands-with-new-attack-arsenal/"
  - "https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa/"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-284a"

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
**C0018** is a month-long ransomware intrusion (Feb–Mar 2022) that resulted in deployment of **[[30_CIPHER/05_Malware/S1053 - AvosLocker|S1053 - AvosLocker]]**. Public reporting describes initial access via an **exposed server**, follow-on staging of multiple open-source and commercial tools, and eventual ransomware execution for impact.

---

## Attribution Assessment
The intrusion is attributed to **unidentified actors**; confidence is **medium** because the technical chain is well described, but actor identity is not conclusively established in the cited sources.

---

## Objectives & Intent
- **Primary:** extortion via file encryption (impact)
- **Secondary:** possible data theft / positioning and internal control prior to detonation

---

## Targeting Analysis
### Technologies / Platforms Targeted
- **VMware Horizon Unified Access Gateway** (Log4Shell-era exploitation cited)
- Windows domain environments
- RDP-enabled workflows and lateral movement paths
- PowerShell for execution and automation

---

## Campaign Tradecraft
### High-Level Tradecraft Summary
Actors exploited exposed infrastructure, then **downloaded and staged tooling** (credential dumping, C2 frameworks, scanners, remote access utilities) before pushing ransomware across the environment (including via deployment tooling).

---

## MITRE ATT&CK Alignment
### Techniques Observed
- [[T1071.001 - Web Protocols]]
- [[T1059.001 - PowerShell]]
- [[T1486 - Data Encrypted for Impact]]
- [[T1190 - Exploit Public-Facing Application]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1570 - Lateral Tool Transfer]]
- [[T1036 - Masquerading]]
- [[T1036.005 - Match Legitimate Resource Name or Location]]
- [[T1046 - Network Service Discovery]]
- [[T1571 - Non-Standard Port]]
- [[T1027.010 - Command Obfuscation]]
- [[T1588.002 - Tool]]
- [[T1219.002 - Remote Desktop Software]]
- [[T1021.001 - Remote Desktop Protocol]]
- [[T1072 - Software Deployment Tools]]
- [[T1218.011 - Rundll32]]
- [[T1016 - System Network Configuration Discovery]]
- [[T1033 - System Owner/User Discovery]]
- [[T1047 - Windows Management Instrumentation]]

### Notable Tradecraft Characteristics
- Exploitation of exposed edge infrastructure followed by **aggressive tool staging**
- Lateral movement and administration heavily reliant on **RDP** and scripted execution
- Obfuscation of PowerShell (base64) and masquerading of payload filenames

---

## Malware & Tooling
### Malware Families
- [[30_CIPHER/05_Malware/S1053 - AvosLocker|S1053 - AvosLocker]]

### Tools (COTS / Open-Source / LOLBins)
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|S0154 - Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0633 - Sliver|S0633 - Sliver]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|S0002 - Mimikatz]]
- [[30_CIPHER/05_Malware/S0108 - netsh|S0108 - netsh]]
- [[30_CIPHER/05_Malware/S0097 - Ping|S0097 - Ping]]

---

## Infrastructure & Operational Patterns
- HTTP-based C2 noted in reporting
- Tool download and staging prior to impact execution
- Port opening for RDP connectivity observed

---

## Timeline of Campaign Activity (Chronos)
```chronos
- [2022-02]: Initial access and foothold established via exposed server / edge infrastructure.
- [2022-02]: Tooling staged (credential dumping, C2 frameworks, scanners, remote access utilities).
- [2022-03]: AvosLocker deployed to encrypt files for impact (intrusion culmination).
- [2022-05-01]: Incident response analysis published describing tradecraft and tooling.
- [2022-06-21]: Vendor reporting published on Avos ransomware group expansion and arsenal.
- [2023-10-11]: CISA advisory published on AvosLocker ransomware activity and TTPs.
```

## Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2022-02 | Initial access via exposed server / edge infrastructure |
| 2022-02 | Tool staging and internal movement preparation |
| 2022-03 | AvosLocker deployed for file encryption |
| 2022-05-01 | Incident response analysis published |
| 2022-06-21 | Vendor blog published on AvosLocker arsenal |
| 2023-10-11 | CISA advisory published on AvosLocker activity |

---

## Defensive Considerations
- Patch and continuously validate exposure posture of **edge services** (e.g., Horizon UAG).
- Detect obfuscated PowerShell and suspicious encoded command-lines.
- Monitor for unusual RDP enablement/port opening and mass remote admin actions.
- Alert on deployment tooling used to distribute binaries at scale.

---

## Analyst Notes
This intrusion highlights a common modern ransomware workflow: edge exploitation → rapid tool staging → credential access → lateral movement → distributed encryption.

---

## References (APA)
- MITRE ATT&CK. (2025, April 21). *C0018 (Campaign)*. Retrieved 2026-01-03 from https://attack.mitre.org/campaigns/C0018/
- Costa, F. (2022, May 1). *RaaS AvosLocker Incident Response Analysis*. LinkedIn. Retrieved 2026-01-03 from https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa/
- Venere, G., & Neal, C. (2022, June 21). *Avos ransomware group expands with new attack arsenal*. Cisco Talos. Retrieved 2026-01-03 from https://blog.talosintelligence.com/avos-ransomware-group-expands-with-new-attack-arsenal/
- Cybersecurity and Infrastructure Security Agency. (2023, October 11). *#StopRansomware: AvosLocker Ransomware (AA23-284A)*. Retrieved 2026-01-03 from https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-284a
