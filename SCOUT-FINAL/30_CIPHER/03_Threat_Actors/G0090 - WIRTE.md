---
entity_type: threat_actor
actor_name: "WIRTE"
common_name: "WIRTE"
actor_id: "G0090"
actor_type: "Threat group (as described in ATT&CK)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2018-08-01"
last_seen: ""
status: "Active (as of ATT&CK last modified 2025-04-16)"
motivations: ["Espionage"]
objectives: ["Targeted intrusion across government and related sectors","Script-based execution and staged payload delivery","Defense evasion via masquerading and system checks"]
victimology_summary: "WIRTE (G0090) is described in ATT&CK as active since at least August 2018, targeting government, diplomatic, financial, military, legal, and technology organizations in the Middle East and Europe."
target_sectors: ["Government","Diplomatic","Financial","Military","Legal","Technology"]
target_regions: ["Middle East","Europe"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/S0679 - Ferocious|Ferocious]]"]
tools: []
infrastructure: ["HTTP-based C2","Script-delivered payload chains","Masquerading of dropped artifacts"]
ttps: ["[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0090 WIRTE - https://attack.mitre.org/groups/G0090/","Lab52 - WIRTE Group attacking the Middle East - https://lab52.io/blog/wirte-group-attacking-the-middle-east/","Kaspersky Securelist - WIRTE campaign in the Middle East - https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044"]
tags: ["scout","threat-actor","mitre-g0090","wirte","middle-east","europe","espionage"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
WIRTE (G0090) is described in ATT&CK as active since at least August 2018, targeting government, diplomatic, financial, military, legal, and technology organizations in the Middle East and Europe. ATT&CK documents HTTP-based communications, PowerShell/VBScript execution, base64 decoding, tool transfer, and masquerading. Associated software includes [[30_CIPHER/05_Malware/S0679 - Ferocious|Ferocious]].

## 2. Attribution Notes
- ATT&CK does not assert a specific sponsoring entity in the captured summary.
- Maintain **medium confidence** until corroborated by investigation evidence and supporting reporting.

## 3. Motivations & Objectives
- **Primary:** espionage-oriented targeting across government and adjacent sectors
- **Operational:** script-based execution, staged payload delivery, and evasion through artifact disguise and environment checks

## 4. Targeting Profile
- **Sectors:** government, diplomatic, financial, military, legal, technology
- **Regions:** Middle East and Europe

## 5. Tradecraft Overview
- **C2 communications:** [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]].
- **Execution:** [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]] and [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]].
- **Decode/obfuscation handling:** [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]] (ATT&CK notes base64 decoding).
- **Staging and retrieval:** [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- **Evasion/stealth:** [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0679 - Ferocious|Ferocious]]

## 8. Infrastructure Patterns
- **HTTP-based C2** aligned to [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]].
- **Script delivery chains** where PowerShell retrieves additional code, aligned to [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- **Masqueraded artifacts** (filenames/locations) aligned to [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]].

## 9. Campaign History
- **At least August 2018–present (reported in ATT&CK):** ongoing activity with targeting across Middle East and Europe.

## 10. Known Indicators
No stable indicators included here. Use incident-derived indicators from:
- proxy/DNS logs, endpoint process trees, script block logging, and dropped file metadata
- validated IOCs from the cited external reporting

## 11. Defensive Recommendations
- **PowerShell detections:** enable and hunt PowerShell Script Block Logging; alert on encoded commands and remote content retrieval.
- **VBScript detections:** monitor wscript/cscript executions, especially when spawned by Office or user-writable paths.
- **Ingress correlation:** tie network downloads to immediate script execution and new file writes.
- **Masquerade controls:** alert on suspicious binaries/scripts adopting names close to legitimate system files and appearing in unusual directories.

## 12. Analyst Notes
**Confidence:** Medium. ATT&CK provides strong behavioral anchors (HTTP + PS/VBS + decode + transfer + masquerade). Confirm exact payload chain and infrastructure in your telemetry.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0090/
- https://lab52.io/blog/wirte-group-attacking-the-middle-east/
- https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044

## 14. References
- MITRE ATT&CK. (n.d.). *WIRTE (G0090)*. https://attack.mitre.org/groups/G0090/
- Lab52. (n.d.). *WIRTE Group attacking the Middle East*. https://lab52.io/blog/wirte-group-attacking-the-middle-east/
- Kaspersky Securelist. (n.d.). *Public report on attacks in Middle East we attribute to WIRTE APT*. https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044
