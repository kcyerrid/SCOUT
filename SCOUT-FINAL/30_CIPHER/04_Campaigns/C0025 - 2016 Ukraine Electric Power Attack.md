---
entity_type: campaign

campaign_name: "2016 Ukraine Electric Power Attack"
campaign_id: "C0025"
aliases: []

description: "Sandworm Team operation targeting Ukrainian electric utilities; involved Industroyer/CRASHOVERRIDE (Crash Override) capabilities to disrupt power operations."

attribution:
  attributed:
    - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|G0034 - Sandworm Team]]"
  suspected: []
  attribution_confidence: "high"

first_observed: "2016-12"
last_observed: "2016-12"
campaign_status: "inactive"

primary_objectives:
  - "Operational disruption (electric grid)"
secondary_objectives:
  - "Credential access"
  - "Lateral movement into ICS environments"

target_sectors:
  - "Energy (electric utilities)"
target_regions:
  - "Ukraine"
target_technologies:
  - "ICS/SCADA"
  - "Windows"

initial_access_vectors:
  - "Enterprise compromise with pivot into ICS network (reported in analyses)"
  - "Use of legitimate credentials and remote services (reported)"

key_ttp_themes:
  - "ICS disruption tooling"
  - "Credential theft + lateral movement"
  - "Masquerading and defense impairment"

associated_ttps:
  - "T1003.001 - LSASS Memory"
  - "T1562.002 - Disable Windows Event Logging"
  - "T1021.002 - SMB/Windows Admin Shares"
  - "T1018 - Remote System Discovery"
  - "T1047 - Windows Management Instrumentation"
  - "T1036.005 - Match Legitimate Resource Name or Location"
  - "T1036.008 - Masquerade File Type"
  - "T1027.002 - Software Packing"
  - "T0807 - Command-Line Interface"
  - "T0886 - Remote Services"

malware_families:
  - "[[30_CIPHER/05_Malware/S0604 - Industroyer|Industroyer (S0604)]]"

tools_used: []
infrastructure_patterns:
  - "Pivoting from IT to OT/ICS environments"
  - "Remote services into ICS networks"

risk_level: "critical"
impact_assessment: "Disruption of electric utility operations; risk of safety and service interruption in critical infrastructure."

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0025/"
  - "https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/"
  - "https://www.dragos.com/blog/crashoverride-anatomy-of-an-attack/"
  - "https://www.dragos.com/resource/crashoverride-analysis-of-the-threat-to-electric-grid-operations/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# 2016 Ukraine Electric Power Attack (C0025)

## 1. Executive Summary
The **2016 Ukraine Electric Power Attack** is attributed to **[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|G0034 - Sandworm Team]]** and is notable for the use of **[[30_CIPHER/05_Malware/S0604 - Industroyer|Industroyer (S0604)]]** (aka CRASHOVERRIDE) to support disruption activity against electric utility operations.

## 2. Attribution & Victimology
- **Attributed actor:** [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|G0034 - Sandworm Team]]
- **Victim profile:** Ukrainian electric utilities / ICS environments

## 3. Malware & Tooling (Atomic Links)
- [[30_CIPHER/05_Malware/S0604 - Industroyer|Industroyer (S0604)]]

## 4. Associated MITRE ATT&CK Techniques (Flat TTP Links)
- [[T1003.001 - LSASS Memory]]
- [[T1562.002 - Disable Windows Event Logging]]
- [[T1021.002 - SMB/Windows Admin Shares]]
- [[T1018 - Remote System Discovery]]
- [[T1047 - Windows Management Instrumentation]]
- [[T1036.005 - Match Legitimate Resource Name or Location]]
- [[T1036.008 - Masquerade File Type]]
- [[T1027.002 - Software Packing]]
- [[T0807 - Command-Line Interface]]
- [[T0886 - Remote Services]]

## 5. Infrastructure & Access Patterns
- Reported pivot from IT foothold into OT/ICS segments
- Remote services and valid credentials used for movement and execution

## 6. Timeline of Campaign Activity (Chronos + Markdown)
```chronos
- [2016-12-17] Attack timeframe reported around this date range; disruption activity observed.
- [2017-06-12] Public disclosure: ESET publishes Industroyer analysis.
```

| Date | Event |
|---|---|
| 2016-12-17 | Attack timeframe reported around this date range; disruption activity observed. |
| 2017-06-12 | Public disclosure: ESET publishes Industroyer analysis. |

## 7. Detection & Hunting Ideas
- Alert on abnormal service creation/modification and suspicious ImagePath changes.
- Hunt for WMI + SMB admin share execution patterns in ICS-adjacent networks.
- Monitor for event log disabling and credential dumping tooling behaviors.

## 8. References (APA)
- Cherepanov, A. (2017, June 12). *Win32/Industroyer: A new threat for industrial control systems*. WeLiveSecurity. https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/
- Slowik, J. (2018, October 12). *Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE*. Dragos. https://www.dragos.com/blog/crashoverride-anatomy-of-an-attack/
- Dragos. (2017, June 13). *CRASHOVERRIDE: Analysis of the Threat to Electric Grid Operations*. https://www.dragos.com/resource/crashoverride-analysis-of-the-threat-to-electric-grid-operations/
- MITRE ATT&CK. (n.d.). *Campaign C0025: 2016 Ukraine Electric Power Attack*. https://attack.mitre.org/campaigns/C0025/
