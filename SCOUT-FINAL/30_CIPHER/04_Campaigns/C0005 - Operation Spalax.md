---
entity_type: campaign

campaign_name: "Operation Spalax"
campaign_id: "C0005"
aliases: []
tlp_classification: "TLP:CLEAR"

associated_threat_actors: []
suspected_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0099 - APT-C-36|APT-C-36 (G0099)]]"
attribution_confidence: "1-low"
confidence_notes: "Reporting noted some IoC/infrastructure overlaps with past campaigns (including one attributed to APT-C-36), but treated Operation Spalax as separate, unattributed activity."

first_observed: "2019-11"
last_observed: "2021-01"
campaign_status: "historic"

primary_objectives:
  - "Initial Access"
  - "Execution"
  - "Persistence"
secondary_objectives:
  - "Defense Evasion"
  - "Command and Control"

target_sectors:
  - "Government (Colombia)"
  - "Energy"
  - "Metallurgical industries"
target_regions:
  - "Colombia"
target_technologies:
  - "Windows"
  - "Email"
  - "Web hosting services"

initial_access_vectors:
  - "Spearphishing Attachment"
  - "Spearphishing Link"

associated_ttps:
  - "T1583.001 - Domains"
  - "T1059 - Command and Scripting Interpreter"
  - "T1140 - Deobfuscate/Decode Files or Information"
  - "T1568 - Dynamic Resolution"
  - "T1027.002 - Software Packing"
  - "T1027.003 - Steganography"
  - "T1027.013 - Encrypted/Encoded File"
  - "T1588.001 - Malware"
  - "T1588.002 - Tool"
  - "T1566.001 - Spearphishing Attachment"
  - "T1566.002 - Spearphishing Link"
  - "T1608.001 - Upload Malware"
  - "T1218.011 - Rundll32"
  - "T1204.001 - Malicious Link"
  - "T1204.002 - Malicious File"
  - "T1497 - Virtualization/Sandbox Evasion"
  - "T1102 - Web Service"

malware_families:
  - "[[30_CIPHER/05_Malware/S0332 - Remcos|Remcos (S0332)]]"
  - "[[30_CIPHER/05_Malware/S0385 - njRAT|njRAT (S0385)]]"
tools_used: []

infrastructure_patterns:
  - "Dynamic DNS services (e.g., DuckDNS/DNSExit)"
  - "Legitimate file hosting for payload staging (e.g., OneDrive/MediaFire)"
  - "High-volume domain registration"

notable_victims: []
related_incidents: []

risk_level: "High"
impact_assessment: "Commodity malware at scale with extensive infra registration and evasion-ready droppers increases likelihood of repeated intrusions."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0005/"
  - "https://www.welivesecurity.com/2021/01/21/operation-spalax-targeted-malware-attacks-colombia/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Operation Spalax (C0005)

## 1. Executive Summary
**Operation Spalax** targeted Colombian government and private sector organizations (notably energy and metallurgical). Operators distributed **commodity malware** via phishing themes (COVID-19, banking, law enforcement) and relied on **dynamic DNS** plus legitimate hosting for staging.

## 2. Technical Overview
Operational highlights:
- Large-scale domain registration and dynamic DNS usage.
- Installer scripting (NSIS) and multi-layer packing/obfuscation including encoded payloads and steganography-like techniques.
- Payload staging in common web services (cloud storage / file sharing) and execution via trusted binaries (e.g., rundll32).

## 3. Associated MITRE ATT&CK Techniques
- [[T1583.001 - Domains]]
- [[T1059 - Command and Scripting Interpreter]]
- [[T1140 - Deobfuscate/Decode Files or Information]]
- [[T1568 - Dynamic Resolution]]
- [[T1027.002 - Software Packing]]
- [[T1027.003 - Steganography]]
- [[T1027.013 - Encrypted/Encoded File]]
- [[T1588.001 - Malware]]
- [[T1588.002 - Tool]]
- [[T1566.001 - Spearphishing Attachment]]
- [[T1566.002 - Spearphishing Link]]
- [[T1608.001 - Upload Malware]]
- [[T1218.011 - Rundll32]]
- [[T1204.001 - Malicious Link]]
- [[T1204.002 - Malicious File]]
- [[T1497 - Virtualization/Sandbox Evasion]]
- [[T1102 - Web Service]]

## 4. Malware & Tooling (Atomic Links)
**Malware Families**
- [[30_CIPHER/05_Malware/S0332 - Remcos|Remcos (S0332)]]
- [[30_CIPHER/05_Malware/S0385 - njRAT|njRAT (S0385)]]

## 5. Timeline (Chronos)
```chronos
- [2019-11] First observed timeframe begins (MITRE reporting window)
- [2021-01] Last observed timeframe ends (MITRE reporting window)
- [2021-01-21] ESET/WeLiveSecurity publishes primary “Operation Spalax” report
- [2022-09-16] MITRE ATT&CK creates campaign entry (C0005)
- [2024-04-11] MITRE ATT&CK updates campaign entry (C0005)
```

## 6. Timeline of Campaign Activity (Markdown)
| Date | Event |
|---|---|
| 2019-11 | First observed timeframe begins (MITRE reporting window) |
| 2021-01 | Last observed timeframe ends (MITRE reporting window) |
| 2021-01-21 | ESET/WeLiveSecurity publishes primary “Operation Spalax” report |
| 2022-09-16 | MITRE ATT&CK creates campaign entry (C0005) |
| 2024-04-11 | MITRE ATT&CK updates campaign entry (C0005) |

## 7. Defensive Recommendations
- Detect **high-volume domain registrations** + **dynamic DNS** associations in telemetry.
- Monitor downloads from **legitimate file hosts** followed by execution via **rundll32**.
- Hunt for droppers performing **sandbox/VM checks** before payload decode/execute.

## 8. References (APA)
- MITRE ATT&CK. (n.d.). *Operation Spalax (Campaign C0005)*. Retrieved 2026-01-02, from https://attack.mitre.org/campaigns/C0005/
- Porolli, M. (2021, January 21). *Operation Spalax: Targeted malware attacks in Colombia*. *WeLiveSecurity (ESET)*. https://www.welivesecurity.com/2021/01/21/operation-spalax-targeted-malware-attacks-colombia/
