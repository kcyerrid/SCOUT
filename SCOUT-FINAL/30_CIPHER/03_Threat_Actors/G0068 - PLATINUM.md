---
entity_type: threat_actor
actor_name: "PLATINUM"
common_name: "PLATINUM"
actor_id: "G0068"
actor_type: "Espionage-focused activity group (state-linked suspected)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2009-01-01"
last_seen: ""
status: "Active"
motivations: ["Espionage","Information theft"]
objectives: ["Targeted intrusion into government-related organizations","Credential collection","Long-term access and data theft"]
victimology_summary: "Activity group targeting government and related organizations in South and Southeast Asia since at least 2009, with documented use of drive-by compromise, spearphishing attachments, privilege escalation exploits, and custom backdoor families."
target_sectors: ["Government","Government-adjacent organizations"]
target_regions: ["South Asia","Southeast Asia"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/adbupd]]","[[30_CIPHER/05_Malware/Dipsind]]","[[30_CIPHER/05_Malware/JPIN]]"]
tools: []
infrastructure: ["[[Spearphishing Infrastructure]]","[[Drive-by Compromise]]","[[Covert C2 Channels]]"]
ttps: ["[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1056.004 - Input Capture: Credential API Hooking]]","[[20_Entities/07_TTPs/T1036 - Masquerading]]","[[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]]","[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]","[[20_Entities/07_TTPs/T1055 - Process Injection]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0068 PLATINUM - https://attack.mitre.org/groups/G0068/","MITRE ATT&CK - S0202 adbupd - https://attack.mitre.org/software/S0202/","MITRE ATT&CK - S0200 Dipsind - https://attack.mitre.org/software/S0200/","MITRE ATT&CK - S0201 JPIN - https://attack.mitre.org/software/S0201/"]
tags: ["scout","threat-actor","mitre-g0068","espionage"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

## 1. BLUF / Executive Summary
PLATINUM (G0068) is an espionage-focused activity group tracked for targeting government and related organizations in South and Southeast Asia since at least 2009. ATT&CK documents a mature intrusion lifecycle including spearphishing attachments, drive-by compromise, exploitation for privilege escalation, and custom backdoors such as [[30_CIPHER/05_Malware/JPIN]].

## 2. Attribution Notes
ATT&CK does not present a definitive public sponsor attribution in its high-level summary. This note treats PLATINUM as state-linked suspected based on the victimology and reporting base referenced by ATT&CK, while leaving sponsor fields unset.

## 3. Motivations & Objectives
- Espionage and strategic intelligence collection
- Credential access and keylogging to support persistence and lateral movement
- Long-term access to enable sustained collection from government-related targets

## 4. Targeting Profile
- **Regions (reported):** South Asia, Southeast Asia
- **Victim class (reported):** governments and related organizations

## 5. Tradecraft Overview
- Initial access via [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- Use of [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] in some operations (including vulnerable browser plugin targeting in referenced reporting).
- Privilege escalation through exploitation aligned to [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]].
- Collection via input capture aligned to [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1056.004 - Input Capture: Credential API Hooking]].
- Evasion through [[20_Entities/07_TTPs/T1036 - Masquerading]] and C2 mechanisms including [[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]] as described by ATT&CK’s technique entries.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1056.004 - Input Capture: Credential API Hooking]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1055 - Process Injection]]
- [[20_Entities/07_TTPs/T1036 - Masquerading]]
- [[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/adbupd]]
  - [[30_CIPHER/05_Malware/Dipsind]]
  - [[30_CIPHER/05_Malware/JPIN]]

## 8. Infrastructure Patterns
- [[Spearphishing Infrastructure]] for initial delivery
- [[Drive-by Compromise]] infrastructure for select victim populations
- [[Covert C2 Channels]] leveraging non-application-layer or atypical channels (as reflected in ATT&CK)

## 9. Campaign History
- **2009–present (reported):** Long-running, government-focused targeting in South and Southeast Asia (ATT&CK summary and referenced reporting).

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Strengthen email and attachment controls for high-risk government functions; prioritize detection of abnormal attachment-driven process trees.
- Improve visibility into credential theft and input-capture behaviors; emphasize endpoint telemetry and anomaly detection.
- Reduce client-side exploit exposure via timely patching and browser/plugin hardening.

## 12. Analyst Notes
**Confidence:** Medium. ATT&CK provides strong technique/tool grounding; sponsor attribution is intentionally conservative due to limited definitive public statements in the ATT&CK summary.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0068/

## 14. References
- https://attack.mitre.org/groups/G0068/
- https://attack.mitre.org/software/S0202/
- https://attack.mitre.org/software/S0200/
- https://attack.mitre.org/software/S0201/
