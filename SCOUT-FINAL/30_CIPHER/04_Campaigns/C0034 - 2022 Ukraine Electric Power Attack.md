---
entity_type: campaign

campaign_name: "2022 Ukraine Electric Power Attack"
campaign_id: "C0034"
aliases:
  - "ELECTRUM (reporting label in public reporting)"
status: "inactive"
risk_level: "critical"

first_seen: "2022-06"
last_seen: "2022-10"

attribution:
  associated_threat_actors:
    - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team (G0034)]]"
  suspected_threat_actors: []
  attribution_confidence: "high"
  attribution_notes: "MITRE attributes the campaign to Sandworm Team."

targets:
  regions:
    - "Ukraine"
  sectors:
    - "Electric utility / energy"
    - "Critical Infrastructure"
  technologies:
    - "SCADA environments"
    - "OT/IT interconnected networks"
    - "MicroSCADA (referenced in reporting)"
    - "Linux persistence mechanisms (systemd)"

initial_access_vectors:
  - "Compromise of environment using custom tools and living-off-the-land techniques (per reporting)"
  - "Web shell placement on internet-facing server (Neo-REGEORG referenced)"

key_ttp_themes:
  - "Custom tooling + LOTL to access utility environment"
  - "Unauthorized command execution in SCADA"
  - "Wiper deployment in IT environment to support OT disruption"
  - "Persistence via system services and scheduled task mechanisms"

associated_malware:
  - "[[30_CIPHER/05_Malware/S0693 - CaddyWiper|CaddyWiper (S0693)]]"

associated_ttps:
  - "T1059.001 - PowerShell"
  - "T1543.002 - Systemd Service"
  - "T1485 - Data Destruction"
  - "T1484.001 - Group Policy Modification"
  - "T1570 - Lateral Tool Transfer"
  - "T1036.004 - Masquerade Task or Service"
  - "T1095 - Non-Application Layer Protocol"
  - "T1572 - Protocol Tunneling"
  - "T1053.005 - Scheduled Task"
  - "T1505.003 - Web Shell"
  - "T0895 - Autorun Image"
  - "T0807 - Command-Line Interface"
  - "T0853 - Scripting"
  - "T0894 - System Binary Proxy Execution"
  - "T0855 - Unauthorized Command Message"

impact_assessment:
  - "Electric power disruption via unauthorized SCADA commands"
  - "Destructive activity via wiper deployment in IT environment"

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0034/"
  - "https://www.mandiant.com/resources/blog/sandworm-disrupts-power-ukraine-operational-technology"
  - "https://www.dragos.com/blog/"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# 2022 Ukraine Electric Power Attack (C0034)

## 1. Executive Summary
**C0034** is a **Sandworm Team** campaign targeting a Ukrainian electric utility, combining **custom tooling**, **web shell access**, and **living-off-the-land** techniques to ultimately **send unauthorized commands from the SCADA system**, alongside **destructive wiper deployment** in the IT environment (notably **[[30_CIPHER/05_Malware/S0693 - CaddyWiper|CaddyWiper (S0693)]]**).

## 2. Campaign Overview
- **Timeframe:** 2022-06 to 2022-10  
- **Outcome:** OT disruption (unauthorized SCADA command messages) + IT destructive actions (wiping).  
- **Tradecraft:** persistence via system services, lateral tool transfer, and scheduled tasks (per reporting).

## 3. Linked Entities
### Threat Actor
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team (G0034)]]

### Malware / Software
- [[30_CIPHER/05_Malware/S0693 - CaddyWiper|CaddyWiper (S0693)]]

## 4. Timeline of Campaign Activity (Chronos)
```chronos
- [2022-06] First seen timeframe (per MITRE entry).
- [2022-10] Last seen timeframe (per MITRE entry).
- [2023-11-09] Public reporting describing Sandworm OT disruption and campaign details (reporting date).
- [2023-12-11] Additional vendor reporting on custom tooling and CaddyWiper usage (reporting date).
```

## 5. Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2022-06 | First seen timeframe (per MITRE entry) |
| 2022-10 | Last seen timeframe (per MITRE entry) |
| 2023-11-09 | Public reporting on Sandworm OT disruption campaign details |
| 2023-12-11 | Additional reporting on custom tools and CaddyWiper use |

## 6. MITRE ATT&CK Alignment (Observed TTPs)
- [[T1505.003 - Web Shell]]
- [[T1484.001 - Group Policy Modification]]
- [[T1053.005 - Scheduled Task]]
- [[T1485 - Data Destruction]]
- [[T1570 - Lateral Tool Transfer]]
- [[T0855 - Unauthorized Command Message]]

## 7. Defensive Considerations
1. **SCADA command monitoring:** alert on unusual command sequences and unauthorized use of SCADA scripting/interfaces.
2. **GPO abuse detection:** monitor for suspicious GPO creation/changes and timed execution artifacts.
3. **Wiper readiness:** ensure immutable backups, offline recovery paths, and rapid containment procedures.
4. **Web shell hunting:** inspect internet-facing servers and internal pivot points for web shell deployment.

## 8. References (APA)
- Dragos, Inc. (2023, December 11). *ELECTRUM Targeted Ukrainian Electric Entity Using Custom Tools and CaddyWiper Malware, October 2022.* Dragos. https://www.dragos.com/blog/  
- Proska, K., Wolfram, J., Wilson, J., Black, D., Lunden, K., Zafra, D. K., Brubaker, N., Mclellan, T., & Sistrunk, C. (2023, November 9). *Sandworm Disrupts Power in Ukraine Using a Novel Attack Against Operational Technology.* Mandiant. https://www.mandiant.com/resources/blog/sandworm-disrupts-power-ukraine-operational-technology  
- MITRE ATT&CK. (n.d.). *2022 Ukraine Electric Power Attack (C0034).* https://attack.mitre.org/campaigns/C0034/
