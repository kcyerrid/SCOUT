---
entity_type: threat_actor
actor_name: "The White Company"
common_name: "The White Company"
actor_id: "G0089"
actor_type: "Likely state-sponsored (espionage) (as described in ATT&CK)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2017-01-01"
last_seen: ""
status: "Unknown (as of ATT&CK last modified 2025-04-25)"
motivations: ["Espionage"]
objectives: ["Targeted compromise via malicious documents","Security product awareness and evasion","Maintain stealth through packing and post-compromise cleanup"]
victimology_summary: "The White Company (G0089) is described in ATT&CK as a likely state-sponsored actor that ran Operation Shaheen (2017–2018) targeting government and military organizations in Pakistan, using phishing lure documents and exploitation of Microsoft Word vulnerabilities."
target_sectors: ["Government","Military"]
target_regions: ["Pakistan"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/S0198 - NETWIRE|NETWIRE]]"]
tools: []
infrastructure: ["Phishing delivery infrastructure","Document-based initial access workflows","C2 over web protocols (via associated software)"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]","[[20_Entities/07_TTPs/T1124 - System Time Discovery]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0089 The White Company - https://attack.mitre.org/groups/G0089/","Cylance - White Company Operation Shaheen Report (PDF) - https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf"]
tags: ["scout","threat-actor","mitre-g0089","operation-shaheen","espionage","pakistan"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
The White Company (G0089) is described in ATT&CK as a likely state-sponsored actor that conducted Operation Shaheen (2017–2018) targeting government and military organizations in Pakistan. ATT&CK documents phishing with malicious Word attachments, client-side exploitation, payload packing, security product discovery, and malware self-deletion for stealth.

## 2. Attribution Notes
- ATT&CK uses “likely state-sponsored” language; maintain **medium confidence** unless corroborated by case evidence.
- Avoid attributing a sponsoring state beyond what ATT&CK and primary reporting state.

## 3. Motivations & Objectives
- **Primary:** espionage against government/military targets
- **Operational:** compromise endpoints through document workflows and reduce detection through obfuscation and cleanup

## 4. Targeting Profile
- **Sectors:** Government, Military
- **Region:** Pakistan
- **Campaign window:** 2017–2018 (Operation Shaheen) per ATT&CK

## 5. Tradecraft Overview
- **Delivery:** [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] with lure documents leading to [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- **Execution:** [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]] leveraging Word vulnerabilities (ATT&CK notes CVE-2012-0158).
- **Evasion:** [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]] and post-run cleanup [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]].
- **Pre-detonation checks:** [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]] and [[20_Entities/07_TTPs/T1124 - System Time Discovery]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]
- [[20_Entities/07_TTPs/T1124 - System Time Discovery]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0198 - NETWIRE|NETWIRE]]

## 8. Infrastructure Patterns
- **Phishing infrastructure:** staged email lures and attachment hosting.
- **C2 posture:** software-associated web protocol use (validate in telemetry).
- **Operational security:** deletion and packing behaviors to limit artifact longevity.

## 9. Campaign History
- **Operation Shaheen (2017–2018):** espionage campaign targeting Pakistani government and military organizations (per ATT&CK).

## 10. Known Indicators
No stable indicators included in this note. Prefer incident-derived IOCs and vendor-reported artifacts validated in your environment.

## 11. Defensive Recommendations
- Flag **Word exploit + unusual child process chains** (e.g., Word spawning script engines or suspicious binaries).
- Alert on **packed binaries** appearing shortly after document open events.
- Monitor **AV product enumeration** and **system time checks** in proximity to new binaries.
- Track **rapid post-execution file deletion** patterns for new artifacts in user-writable directories.

## 12. Analyst Notes
**Confidence:** Medium. ATT&CK provides a narrow but actionable slice of the actor’s tradecraft; expand with validated case telemetry and the referenced reporting.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0089/
- https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf

## 14. References
- MITRE ATT&CK. (n.d.). *The White Company (G0089)*. https://attack.mitre.org/groups/G0089/
- Cylance. (n.d.). *White Company Operation Shaheen Report* (PDF). https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf
