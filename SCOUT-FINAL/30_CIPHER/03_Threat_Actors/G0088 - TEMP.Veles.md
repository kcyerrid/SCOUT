---
entity_type: threat_actor
actor_name: "TEMP.Veles"
common_name: "TEMP.Veles"
actor_id: "G0088"
actor_type: "Threat group (critical infrastructure / ICS-focused) (as described in ATT&CK)"
aliases: ["XENOTIME"]
country_of_origin: "Russia (as described by ATT&CK)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2014-10-01"
last_seen: ""
status: "Active (as of ATT&CK last modified 2024-04-17)"
motivations: ["Disruption","Espionage"]
objectives: ["Access and persistence in critical infrastructure environments","Credential capture and remote access enablement","Enablement of safety-system manipulation capability (as described in reporting)"]
victimology_summary: "TEMP.Veles is described in ATT&CK as a Russia-based threat group targeting critical infrastructure, observed utilizing TRITON-related activity and overlapping with Dragos-defined XENOTIME."
target_sectors: ["Critical Infrastructure","Industrial (ICS environments)"]
target_regions: []
related_groups: []
malware: ["[[30_CIPHER/05_Malware/TRITON|TRITON]]"]
tools: []
infrastructure: ["Remote access pathways into OT/ICS","Operational tooling staged and removed post-use","Non-standard port protocol use (per ATT&CK)"]
ttps: ["[[20_Entities/07_TTPs/T1573 - Encrypted Channel]]","[[20_Entities/07_TTPs/T1546.012 - Event Triggered Execution: Image File Execution Options Injection]]","[[20_Entities/07_TTPs/T1133 - External Remote Services]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]]","[[20_Entities/07_TTPs/T1056.003 - Input Capture: Web Portal Capture]]","[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]","[[20_Entities/07_TTPs/T1571 - Non-Standard Port]]","[[20_Entities/07_TTPs/T1027.005 - Obfuscated Files or Information: Indicator Removal from Tools]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0088 TEMP.Veles - https://attack.mitre.org/groups/G0088/","Mandiant (Google Cloud) - TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping - https://cloud.google.com/blog/topics/threat-intelligence/triton-actor-ttp-profile-custom-attack-tools-detections/"]
tags: ["scout","threat-actor","mitre-g0088","temp.veles","xenotime","ics","critical-infrastructure"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
TEMP.Veles (G0088) is described in ATT&CK as a Russia-based threat group targeting critical infrastructure and associated with TRITON-related activity. The actor’s documented behaviors emphasize persistence mechanisms, credential capture opportunities, encrypted communications, masquerading, and post-operation cleanup in environments that may include OT/ICS boundary systems.

## 2. Attribution Notes
- ATT&CK describes the group as Russia-based; attribution should be treated as **medium confidence** absent further corroboration in the specific investigation.
- Overlap is noted with Dragos-defined XENOTIME in ATT&CK narratives.

## 3. Motivations & Objectives
- **Disruption and/or espionage outcomes** enabled by sustained access into critical infrastructure environments.
- **Operational objectives:** gain foothold, persist, capture credentials, and reduce detection through cleanup and obfuscation.

## 4. Targeting Profile
- **Primary:** critical infrastructure environments (including OT-adjacent enterprise systems)
- **Victim profile:** organizations operating industrial safety and control processes (per ATT&CK context)

## 5. Tradecraft Overview
- **Encrypted communications:** [[20_Entities/07_TTPs/T1573 - Encrypted Channel]].
- **Persistence via OS mechanisms:** [[20_Entities/07_TTPs/T1546.012 - Event Triggered Execution: Image File Execution Options Injection]].
- **Remote access:** [[20_Entities/07_TTPs/T1133 - External Remote Services]].
- **Credential capture patterns:** [[20_Entities/07_TTPs/T1056.003 - Input Capture: Web Portal Capture]].
- **Evasion:** masquerading and indicator removal aligned to [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]], [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]], and [[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1546.012 - Event Triggered Execution: Image File Execution Options Injection]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1056.003 - Input Capture: Web Portal Capture]]
- [[20_Entities/07_TTPs/T1573 - Encrypted Channel]]
- [[20_Entities/07_TTPs/T1571 - Non-Standard Port]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- [[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]]
- [[20_Entities/07_TTPs/T1027.005 - Obfuscated Files or Information: Indicator Removal from Tools]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]

## 7. Malware & Tools Used
- Malware / frameworks (as described in ATT&CK and cited reporting):
  - [[30_CIPHER/05_Malware/TRITON|TRITON]]

## 8. Infrastructure Patterns
- **Remote-access paths** into enterprise systems that interface with OT/ICS environments.
- **Non-standard port usage** aligned to [[20_Entities/07_TTPs/T1571 - Non-Standard Port]].
- **Tool staging and rapid cleanup** aligned to indicator removal techniques.

## 9. Campaign History
- ATT&CK lists activity spanning at least **October 2014–January 2017** in campaign tables and ties TRITON-related activity to critical infrastructure targeting.

## 10. Known Indicators
No stable indicators included here. Treat artifacts (accounts, VPN/RDP usage, registry modifications, staged tools) as incident-specific.

## 11. Defensive Recommendations
- **Detect persistence:** monitor IFEO registry modifications (new debugger values, anomalous executables).
- **Credential capture:** watch for suspicious web portal credential interception and abnormal auth flows.
- **Cleanup behavior:** correlate file deletions and timestomping with prior suspicious tool execution; treat as high signal in admin contexts.
- **Network:** alert on protocol mismatches and non-standard ports in OT/ICS boundary segments.

## 12. Analyst Notes
**Confidence:** Medium overall; elevate confidence only when TRITON-related artifacts and ATT&CK-aligned behaviors converge with environment-specific evidence.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0088/
- https://cloud.google.com/blog/topics/threat-intelligence/triton-actor-ttp-profile-custom-attack-tools-detections/

## 14. References
- MITRE ATT&CK. (n.d.). *TEMP.Veles (G0088)*. https://attack.mitre.org/groups/G0088/
- Miller, S., Brubaker, N., Zafra, D. K., & Caban, D. (2019, April 10). *TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping*. https://cloud.google.com/blog/topics/threat-intelligence/triton-actor-ttp-profile-custom-attack-tools-detections/
