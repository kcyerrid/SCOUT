---
entity_type: threat_actor
actor_name: "Rancor"
common_name: "Rancor"
actor_id: "G0075"
actor_type: ""
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Unknown"
first_seen: ""
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Initial access via spearphishing attachments","Establish persistence via scheduled tasks and WMI event subscriptions","Stage and execute custom malware families for access and collection"]
victimology_summary: "Rancor (G0075) is documented in ATT&CK as conducting targeted activity with initial access via spearphishing attachments and persistence through Windows-native mechanisms (scheduled tasks and WMI event subscriptions). ATT&CK maps Rancor to custom malware families [[30_CIPHER/05_Malware/S0254 - PLAINTEE|PLAINTEE]] and [[30_CIPHER/05_Malware/S0255 - DDKONG|DDKONG]] and to use of certutil for tool transfer."
target_sectors: []
target_regions: ["Southeast Asia"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/S0254 - PLAINTEE|PLAINTEE]]","[[30_CIPHER/05_Malware/S0255 - DDKONG|DDKONG]]"]
tools: ["certutil"]
infrastructure: ["[[Phishing]]","[[HTTP C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1218.007 - System Binary Proxy Execution: Msiexec]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0075 Rancor - https://attack.mitre.org/groups/G0075/","MITRE ATT&CK - S0254 PLAINTEE - https://attack.mitre.org/software/S0254/","MITRE ATT&CK - S0255 DDKONG - https://attack.mitre.org/software/S0255/","MITRE ATT&CK - S0160 certutil - https://attack.mitre.org/software/S0160/"]
tags: ["scout","threat-actor","mitre-g0075","espionage","southeast-asia"]
created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Rancor (G0075) is an espionage-oriented threat actor documented by ATT&CK with a strong emphasis on **phishing-based initial access** and **Windows persistence** via scheduled tasks and WMI event subscriptions. ATT&CK maps Rancor to the custom malware families [[30_CIPHER/05_Malware/S0254 - PLAINTEE|PLAINTEE]] and [[30_CIPHER/05_Malware/S0255 - DDKONG|DDKONG]], plus living-off-the-land enablement using certutil and msiexec.

## 2. Attribution Notes
ATT&CK provides technique and software mappings for Rancor. Sponsorship attribution is not asserted in this note unless explicitly documented by ATT&CK or primary research sources you choose to lock in.

## 3. Motivations & Objectives
- Espionage-driven access and collection
- Maintain persistence using built-in Windows scheduling/eventing features
- Download/execute additional payloads after initial foothold

## 4. Targeting Profile
- **Victim themes:** targeted attacks reported against Southeast Asian interests (supported by ATT&CK-linked public reporting)
- **Sectors/regions:** populate from internal intelligence if maintained

## 5. Tradecraft Overview
- **Initial access:** spearphishing attachment aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and user execution aligned to [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- **Persistence:** scheduled tasks aligned to [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]] and WMI event subscriptions aligned to [[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]].
- **Tool transfer/execution:** msiexec proxy execution aligned to [[20_Entities/07_TTPs/T1218.007 - System Binary Proxy Execution: Msiexec]] and ingress transfer aligned to [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- **C2:** HTTP aligned to [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1218.007 - System Binary Proxy Execution: Msiexec]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0254 - PLAINTEE|PLAINTEE]]
  - [[30_CIPHER/05_Malware/S0255 - DDKONG|DDKONG]]
- Tools / LOLBins:
  - [[30_CIPHER/05_Malware/S0160 - certutil|certutil]] *(software/utility entity; adjust path if you store tools separately)*

## 8. Infrastructure Patterns
- [[Phishing]] delivery with document/macro or script execution chains
- [[HTTP C2]] with proxy/DNS visibility and endpoint network telemetry

## 9. Campaign History
ATT&CK maintains software and technique mappings for Rancor; campaign delineation is not captured in this note. Add internal campaign notes if you track them.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Alert on WMI event subscription creation and suspicious MOF compilation chains.
- Detect scheduled task creation where the task target is a user-writable path or launches script interpreters.
- Correlate msiexec network retrieval with immediate execution and follow-on persistence.
- Monitor certutil usage patterns consistent with file retrieval/transfer in user contexts.

## 12. Analyst Notes
**Confidence:** Medium for ATT&CK mappings. Validate delivery tooling (document types, macro/VBS usage) and persistence objects during incident response.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0075/
- https://attack.mitre.org/software/S0254/
- https://attack.mitre.org/software/S0255/

## 14. References
- MITRE ATT&CK. (n.d.). *Rancor (G0075).* https://attack.mitre.org/groups/G0075/
- MITRE ATT&CK. (n.d.). *PLAINTEE (S0254).* https://attack.mitre.org/software/S0254/
- MITRE ATT&CK. (n.d.). *DDKONG (S0255).* https://attack.mitre.org/software/S0255/
- MITRE ATT&CK. (n.d.). *certutil (S0160).* https://attack.mitre.org/software/S0160/
