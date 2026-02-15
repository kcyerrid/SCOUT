---
entity_type: threat_actor
actor_name: "Orangeworm"
common_name: "Orangeworm"
actor_id: "G0071"
actor_type: ""
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Unknown"
first_seen: ""
last_seen: ""
status: "Unknown"
motivations: ["Corporate espionage"]
objectives: ["Targeted compromise of healthcare organizations","Long-term access and internal propagation via Windows network shares","Collection of system/network context to support lateral movement and persistence"]
victimology_summary: "Orangeworm (G0071) is documented in ATT&CK as targeting healthcare sector organizations across the United States, Europe, and Asia since at least 2015, likely for corporate espionage. ATT&CK directly associates Orangeworm activity with the Kwampirs malware family and documents HTTP-based command-and-control and SMB/ADMIN$ share propagation behaviors."
target_sectors: ["Healthcare"]
target_regions: ["United States","Europe","Asia"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/S0236 - Kwampirs|Kwampirs]]"]
tools: []
infrastructure: ["[[HTTP C2]]","[[SMB/ADMIN$ propagation]]"]
ttps: ["[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0071 Orangeworm - https://attack.mitre.org/groups/G0071/","MITRE ATT&CK - S0236 Kwampirs - https://attack.mitre.org/software/S0236/"]
tags: ["scout","threat-actor","mitre-g0071","healthcare","espionage"]
created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Orangeworm (G0071) is a healthcare-focused intrusion set documented by ATT&CK, associated with [[30_CIPHER/05_Malware/S0236 - Kwampirs|Kwampirs]]. Reported tradecraft emphasizes **high-signal lateral movement via administrative SMB shares** and **web-protocol C2**, making it especially relevant for Windows-centric enterprise monitoring and detection engineering.

## 2. Attribution Notes
ATT&CK describes Orangeworm’s targeting and intent as likely corporate espionage. Attribution to a specific sponsor is not asserted in ATT&CK; treat any third-party attribution beyond ATT&CK as unconfirmed unless separately validated.

## 3. Motivations & Objectives
- Corporate espionage against healthcare organizations
- Establish and maintain persistent access in enterprise Windows environments
- Propagate internally using administrative shares and remote services

## 4. Targeting Profile
- **Victim themes:** healthcare sector organizations
- **Regions:** United States, Europe, Asia (as summarized in ATT&CK)

## 5. Tradecraft Overview
- **C2 channeling:** HTTP-based communications aligned to [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]].
- **Propagation / lateral movement:** copying payloads across open/admin shares aligned to [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0236 - Kwampirs|Kwampirs]]

## 8. Infrastructure Patterns
- [[HTTP C2]] with enterprise web-proxy visibility (proxy logs, EDR network telemetry)
- [[SMB/ADMIN$ propagation]] across ADMIN$/C$/D$ style administrative shares

## 9. Campaign History
- **Since at least 2015 (ATT&CK):** sustained healthcare targeting with tooling mapped to Kwampirs.

## 10. Known Indicators
This note does not include stable, copy/paste IOCs. Prefer behavior-based detections and incident-specific enrichment.

## 11. Defensive Recommendations
- Prioritize monitoring for **remote share write activity** to ADMIN$/C$/Windows paths from non-admin management systems.
- Detect uncommon SMB lateral movement chains (workstation-to-workstation admin share usage) and correlate with service creation or remote execution telemetry.
- Baseline outbound HTTP(S) beaconing from hosts that also show SMB share propagation indicators.

## 12. Analyst Notes
**Confidence:** Medium–High for behaviors explicitly mapped in ATT&CK; validate environment-specific propagation paths and tooling variants during investigations.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0071/
- https://attack.mitre.org/software/S0236/

## 14. References
- MITRE ATT&CK. (n.d.). *Orangeworm (G0071).* https://attack.mitre.org/groups/G0071/
- MITRE ATT&CK. (n.d.). *Kwampirs (S0236).* https://attack.mitre.org/software/S0236/
