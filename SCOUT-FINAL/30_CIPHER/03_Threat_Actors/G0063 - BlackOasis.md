---
entity_type: threat_actor
actor_name: "BlackOasis"
common_name: "BlackOasis"
actor_id: "G0063"
actor_type: "State-linked (suspected espionage)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2017-08-08"
last_seen: ""
status: "Active"
motivations: ["Espionage","Surveillance"]
objectives: ["Collection on individuals and organizations of political/strategic interest","Device compromise and monitoring","Access to communications and documents"]
victimology_summary: "Reporting describes targeting of prominent individuals and entities including UN-related figures, activists, opposition bloggers, regional journalists/correspondents, and think tanks; public coverage highlights use of commercial spyware (FinFisher) in targeted operations."
target_sectors: ["International organizations","Media / Journalism","Civil society / NGOs","Think tanks"]
target_regions: ["Middle East","International / UN-affiliated"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/FinFisher]]"]
tools: []
infrastructure: ["[[Spearphishing Infrastructure]]","[[Exploit Documents]]","[[Commercial Spyware Deployment]]"]
ttps: ["[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0063 BlackOasis - https://attack.mitre.org/groups/G0063/","Kaspersky Securelist (2017-10-16) - Targeted attacks leveraging CVE-2017-11292; BlackOasis background and targeting - https://securelist.com/blackoasis-apt-and-new-targeted-attacks-leveraging-zero-day-exploit/82732/","CyberScoop (2017-10-16) - Reporting on FinFisher use linked to BlackOasis activity - https://www.cyberscoop.com/middle-eastern-hacking-group-using-finfisher-malware-conduct-international-espionage/"]
tags: ["scout","threat-actor","mitre-g0063","espionage","commercial-spyware"]
created: "2026-01-01"
last_modified: "2026-01-01"
---

## 1. BLUF / Executive Summary
BlackOasis (G0063) is a Middle East–linked espionage cluster described in public reporting as leveraging targeted delivery and commercial spyware (**[[30_CIPHER/05_Malware/FinFisher]]**) to surveil individuals and organizations of political and strategic interest. Reporting highlights selective victim targeting (UN-linked and civil society figures) and operations that included exploit-driven initial access.

## 2. Attribution Notes
MITRE ATT&CK characterizes BlackOasis as a Middle Eastern threat group and notes it is believed to be a customer of Gamma Group (maker of FinFisher). Microsoft’s tracking name NEODYMIUM is described as closely associated with BlackOasis operations, but ATT&CK notes that alias equivalence has not been conclusively established.

## 3. Motivations & Objectives
- Espionage and surveillance of high-interest individuals/organizations
- Covert collection of communications and sensitive documents
- Use of commercial intrusion capabilities to reduce bespoke development burden

## 4. Targeting Profile
- **Victim themes (reported):** UN-related figures, activists, opposition bloggers, regional journalists/correspondents, think tanks
- **Region (reported):** Middle East with international-facing target sets

## 5. Tradecraft Overview
- **Highly selective targeting** consistent with strategic collection requirements.
- **Exploit-enabled compromise** described in public research (including an exploit chain associated with CVE-2017-11292 in 2017 reporting).
- **Commercial spyware usage** (FinFisher) to support surveillance workflows and collection.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]

## 7. Malware & Tools Used
- Malware / spyware:
  - [[30_CIPHER/05_Malware/FinFisher]]

## 8. Infrastructure Patterns
- [[Spearphishing Infrastructure]] aligned to specific personas and target communities
- [[Exploit Documents]] used to trigger client-side execution for initial access (reported)
- [[Commercial Spyware Deployment]] patterns consistent with third-party tooling ecosystems

## 9. Campaign History
- **2017-08 to 2017-10 (reported):** Public reporting details BlackOasis background and targeted operations leveraging a then-current exploit chain and FinFisher deployment.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Prioritize protection for high-risk individuals and executive/communications staff (phishing-resistant MFA, hardened endpoints, rapid patching).
- Implement exploit mitigation controls and application hardening for document/PDF workflows.
- Enhance monitoring for signs of commercial surveillance tooling and anomalous endpoint behavior associated with targeted intrusion attempts.

## 12. Analyst Notes
**Confidence:** Medium. Targeting narrative and commercial spyware linkage are supported by reputable reporting, but precise sponsor attribution is not established publicly with high confidence.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0063/
- https://securelist.com/blackoasis-apt-and-new-targeted-attacks-leveraging-zero-day-exploit/82732/

## 14. References
- https://attack.mitre.org/groups/G0063/
- https://securelist.com/blackoasis-apt-and-new-targeted-attacks-leveraging-zero-day-exploit/82732/
- https://www.cyberscoop.com/middle-eastern-hacking-group-using-finfisher-malware-conduct-international-espionage/
