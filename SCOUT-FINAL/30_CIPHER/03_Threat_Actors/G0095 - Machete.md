---
entity_type: threat_actor
actor_name: "Machete"
common_name: "Machete"
actor_id: "G0095"
actor_type: "Cyber espionage"
aliases:
  - "APT-C-43"
  - "El Machete"
country_of_origin: "Unknown (suspected Spanish-speaking)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2010-01-01"
last_seen: ""
status: "Active"

motivations:
  - "Espionage"
objectives:
  - "Collection and exfiltration of sensitive information from targeted institutions"
victimology_summary: "Suspected Spanish-speaking cyber espionage group active since at least 2010, primarily targeting government institutions in Latin America (especially Venezuela), with additional activity against entities in the US, Europe, Russia, and parts of Asia."
target_sectors:
  - "Government"
target_regions:
  - "Latin America"
  - "Venezuela"
  - "United States"
  - "Europe"
  - "Russia"
  - "Asia"

related_groups: []

malware:
  - "[[30_CIPHER/05_Malware/S0409 - Machete|Machete]]"
tools: []

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment|T1566.001]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105]]"
  - "[[20_Entities/07_TTPs/T1113 - Screen Capture|T1113]]"
  - "[[20_Entities/07_TTPs/T1125 - Video Capture|T1125]]"
  - "[[20_Entities/07_TTPs/T1140 - Deobfuscate - Decode Files or Information|T1140]]"
  - "[[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001]]"
  - "[[20_Entities/07_TTPs/T1218.011 - Rundll32|T1218.011]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190]]"

notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0095/"
  - "https://www.welivesecurity.com/2016/06/15/sharpening-machete-cyberespionage/"
tags:
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0095"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Machete (G0095) is a suspected Spanish-speaking cyber espionage group active since at least **2010**, primarily targeting **government institutions in Latin America** (notably Venezuela), with additional targeting across the US, Europe, Russia, and parts of Asia. ATT&CK maps the group to the Machete malware family (S0409).

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0095
- **Associated names/clusters:** APT-C-43, El Machete
- **Confidence:** Medium (ATT&CK characterizes as “suspected” and describes regional/linguistic indicators).

## 3. Motivations & Objectives
- **Motivation:** Espionage.
- **Objectives:** Document and information theft with exfiltration; operational monitoring via screen/video capture.

## 4. Targeting Profile
- **Primary sector:** Government.
- **Primary regions:** Latin America (especially Venezuela).
- **Additional regions:** US, Europe, Russia, parts of Asia.

## 5. Tradecraft Overview
ATT&CK technique examples indicate:
- **Spearphishing attachment** delivery and user-driven execution.
- **Execution** via Windows command shell and LOLBin-style utilities (e.g., rundll32).
- **C2 over web protocols** (and FTP noted for Machete in ATT&CK technique references).
- **Tool transfer** for staging follow-on payloads.
- **Collection/monitoring** via screen capture and video capture.
- **Obfuscation/decode** steps and archival prior to exfiltration.

## 6. MITRE ATT&CK Mapping (Key TTPs)
- [[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment|T1566.001]] — Attachment-based initial access.
- [[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003]] — Command execution.
- [[20_Entities/07_TTPs/T1218.011 - Rundll32|T1218.011]] — Signed binary proxy execution behavior.
- [[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001]] — Web protocol-based C2.
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105]] — Payload staging.
- [[20_Entities/07_TTPs/T1113 - Screen Capture|T1113]] / [[20_Entities/07_TTPs/T1125 - Video Capture|T1125]] — Monitoring/collection.
- [[20_Entities/07_TTPs/T1140 - Deobfuscate - Decode Files or Information|T1140]] — Decode steps.
- [[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001]] — Archiving prior to exfiltration.
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190]] — Included in ATT&CK technique mapping for the group.

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0409 - Machete|Machete]]

## 8. Infrastructure Patterns
- C2 over standard protocols with emphasis on web traffic; ATT&CK technique references note FTP usage associated with the group’s malware in some reporting.

## 9. Campaign History
- Activity reported since at least 2010; primary geographic focus in Latin America with broader international targeting per ATT&CK description.

## 10. Known Indicators
- Maintain campaign-specific IOCs separately. High-yield pivots:
  - Spearphishing attachments leading to cmd/rundll32 execution.
  - Unusual capture activity (screen/video capture) on endpoints.
  - Archiving operations immediately preceding outbound communications.

## 11. Defensive Recommendations
- Email hardening: attachment isolation, detonation, and user execution controls.
- Endpoint controls: monitor rundll32 usage with suspicious DLL paths; command-line logging for cmd activity.
- Network controls: alert on anomalous outbound web/FTP patterns from user endpoints; restrict where feasible.
- Data loss prevention: detect staged archives and unusual upload activity following collection spikes.

## 12. Analyst Notes
- Capture-focused tradecraft (screen/video) can be a high-signal differentiator when correlated with suspicious execution chains.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0095/
- ESET Research (commonly cited in ATT&CK mapping): https://www.welivesecurity.com/2016/06/15/sharpening-machete-cyberespionage/

## 14. References
- MITRE ATT&CK. (n.d.). *Machete (G0095).* https://attack.mitre.org/groups/G0095/
- ESET Research. (2016, June 15). *Sharpening the Machete: cyberespionage in Latin America.* WeLiveSecurity. https://www.welivesecurity.com/2016/06/15/sharpening-machete-cyberespionage/
