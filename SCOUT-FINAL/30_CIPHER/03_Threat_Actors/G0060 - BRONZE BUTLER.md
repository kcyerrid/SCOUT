---
entity_type: threat_actor
actor_name: "BRONZE BUTLER"
common_name: "BRONZE BUTLER"
actor_id: "G0060"
actor_type: "State-sponsored (espionage)"
aliases: ["REDBALDKNIGHT","Tick"]
country_of_origin: "China (likely)"
suspected_sponsors: []
attribution_confidence: "Medium-High"
first_seen: "2008-01-01"
last_seen: ""
status: "Active"
motivations: ["Espionage","Information theft"]
objectives: ["Collection of sensitive organizational data","Long-term access in targeted environments"]
victimology_summary: "Primarily targets Japanese organizations; reporting highlights government and select high-tech and industrial sectors."
target_sectors: ["Government","Biotechnology","Electronics manufacturing","Industrial chemistry"]
target_regions: ["Japan"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/ABK]]","[[30_CIPHER/05_Malware/Avenger]]","[[30_CIPHER/05_Malware/BBK]]","[[30_CIPHER/05_Malware/build_downer]]"]
tools: []
infrastructure: ["HTTP C2","Dead drop resolvers","Watering hole sites","File shares"]
ttps: ["[[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]","[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]","[[20_Entities/07_TTPs/T1080 - Taint Shared Content]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0060 BRONZE BUTLER - https://attack.mitre.org/groups/G0060/","MITRE ATT&CK - S0469 ABK - https://attack.mitre.org/software/S0469/","MITRE ATT&CK - S0473 Avenger - https://attack.mitre.org/software/S0473/","MITRE ATT&CK - S0470 BBK - https://attack.mitre.org/software/S0470/","MITRE ATT&CK - S0471 build_downer - https://attack.mitre.org/software/S0471/"]
tags: ["scout","threat-actor","mitre-g0060","espionage","japan-targeting"]
created: "2026-01-01"
last_modified: "2026-01-01"
---

## 1. BLUF / Executive Summary
BRONZE BUTLER (G0060) is an espionage-focused threat actor with likely China-linked origins, active since at least 2008. Public reporting highlights sustained targeting of Japanese organizations—particularly government and select industrial and high-technology sectors—using multi-stage tooling and common enterprise intrusion techniques.

## 2. Attribution Notes
MITRE ATT&CK assesses “likely Chinese origins.” The actor is also tracked under the names Tick and REDBALDKNIGHT in public reporting. Exact overlaps between vendor clusters should be treated conservatively when correlating incidents.

## 3. Motivations & Objectives
- Intelligence collection and information theft from strategic Japanese targets
- Establish and maintain long-lived footholds to enable ongoing collection

## 4. Targeting Profile
- **Primary region (reported):** Japan  
- **Sectors (reported):** government, biotech, electronics manufacturing, industrial chemistry

## 5. Tradecraft Overview
- Spearphishing and user-driven execution appear repeatedly in public reporting.
- Uses a family of downloaders and staged payload delivery to support persistence and collection.
- Leverages common Windows execution and persistence mechanisms and HTTP-based C2 patterns.
- Documented use of web-service “dead drop” style indirection and shared-content tainting patterns.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]
- [[20_Entities/07_TTPs/T1080 - Taint Shared Content]]
- [[20_Entities/07_TTPs/T1550.003 - Use Alternate Authentication Material: Pass the Ticket]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1053.002 - Scheduled Task/Job: At]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/ABK]]
  - [[30_CIPHER/05_Malware/Avenger]]
  - [[30_CIPHER/05_Malware/BBK]]
  - [[30_CIPHER/05_Malware/build_downer]]

## 8. Infrastructure Patterns
- [[HTTP C2]] patterns consistent with web-protocol blending
- [[Dead Drop Resolvers]] leveraging legitimate web services for redirection/indirection
- [[Watering Hole Sites]] / drive-by style entry points (reported historically)
- [[Tainted Shared Content]] on file shares to prompt execution

## 9. Campaign History
- **2008–present (reported):** Long-running espionage activity with recurring Japan-focused targeting.
- **2019–present (reported):** ATT&CK software tracking includes multiple downloaders associated with BRONZE BUTLER operations.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Strengthen phishing resilience (email security controls + user-risk reduction) and monitor for suspicious attachment execution chains.
- Harden Windows privilege boundaries and monitor for UAC bypass artifacts and abnormal elevation patterns.
- Increase visibility into persistence vectors (Run keys, scheduled tasks) and investigate deviations from baseline.
- Monitor for suspicious outbound HTTP/S traffic patterns and “dead drop” style beaconing to popular web services.

## 12. Analyst Notes
**Confidence:** Medium-high for victimology and tradecraft at a high level (per ATT&CK). Lower confidence for fine attribution granularity beyond “likely” origin statements.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0060/

## 14. References
- https://attack.mitre.org/groups/G0060/
- https://attack.mitre.org/software/S0469/
- https://attack.mitre.org/software/S0473/
- https://attack.mitre.org/software/S0470/
- https://attack.mitre.org/software/S0471/
