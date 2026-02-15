---
entity_type: threat_actor
name: "Sowbug"
actor_id: "G0054"
aliases: ["Sowbug"]
description: "Sowbug is a threat group associated with targeted cyber-espionage activity against government and diplomatic organizations, with publicly reported activity spanning South America and Southeast Asia."
first_seen: "2015-01-01"
last_seen: ""
suspected_country: ""
suspected_region: ""
suspected_sponsors: []
motivations: ["Espionage"]
objectives: ["Collection of foreign policy and diplomatic information"]
target_regions: ["South America", "Southeast Asia"]
target_countries: ["Argentina", "Brazil", "Ecuador", "Peru", "Brunei", "Malaysia"]
target_sectors: ["Government", "Diplomacy / Foreign Affairs"]
malware: ["[[30_CIPHER/05_Malware/Felismus]]", "[[30_CIPHER/05_Malware/Starloader]]"]
tools: []
infrastructure_patterns: ["[[HTTP-based C2]]", "[[Masquerading as legitimate software]]", "[[Archive staging for collection/exfiltration]]", "[[Long-dwell access]]"]
ttps: ["[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]", "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]", "[[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive]]", "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]", "[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]", "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]", "[[20_Entities/07_TTPs/T1135 - Network Share Discovery]]", "[[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]", "[[20_Entities/07_TTPs/T1082 - System Information Discovery]]", "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]", "[[20_Entities/07_TTPs/T1132.001 - Data Encoding: Standard Encoding]]", "[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]", "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]", "[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]", "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]", "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]", "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]"]
created: "2025-12-28"
last_updated: "2025-12-28"
intel_sources: ["MITRE ATT&CK - Sowbug (G0054): https://attack.mitre.org/groups/G0054/", "MITRE ATT&CK - Felismus (S0171): https://attack.mitre.org/software/S0171/", "MITRE ATT&CK - Starloader (S0188): https://attack.mitre.org/software/S0188/", "Dark Reading (2017-11-07) - South America the Target of 'Sowbug' Cyber Espionage Group: https://www.darkreading.com/cyberattacks-data-breaches/south-america-the-target-of-sowbug-cyber-espionage-group", "CyberScoop (2017-11-07) - Previously unknown cyber-espionage group has successfully hacked in South America since 2015: https://cyberscoop.com/previously-unknown-cyber-espionage-group-successfully-hacked-south-america-since-2015/", "LevelBlue (2017-04-25) - The Felismus RAT: Powerful Threat, Mysterious Purpose: https://levelblue.com/blogs/security-essentials/the-felismus-rat-powerful-threat-mysterious-purpose", "Silicon UK (2017-11-07) - Sowbug Hacking Group Targets South America & Asian Governments: https://www.silicon.co.uk/security/sowbug-hacking-group-224423", "SC Media (2017-11-07) - Sowbug APT uses Felismus backdoor to for cyberespionage operations: https://www.scworld.com/news/sowbug-apt-uses-felismus-backdoor-to-for-cyberespionage-operations"]
tags: ["threat-actor", "apt", "espionage", "government-targeting"]
---

## 1. BLUF / Executive Summary
Sowbug ([[MITRE ATT&CK G0054]]) is assessed in public reporting as a targeted cyber-espionage threat group active since at least 2015, with a victimology centered on government and diplomatic entities in South America and Southeast Asia. Reporting links Sowbug to the modular backdoor [[30_CIPHER/05_Malware/Felismus]] and a loader component [[30_CIPHER/05_Malware/Starloader]], alongside tradecraft consistent with document discovery/collection, credential access, and stealth through [[Masquerading as legitimate software]].

## 2. Attribution Notes
Public sources characterize Sowbug as having “nation-state-like” capability and a victimology aligned to strategic intelligence requirements, but do not provide a definitive public attribution to a specific government or sponsor.
- Attribution to a named state: **Not supported** in the cited public sources.
- Confidence note: **Low** for sponsor attribution; **High** for victimology and tooling linkages documented by MITRE ATT&CK and contemporary reporting.

## 3. Motivations & Objectives
- Primary motivation: **Espionage** (foreign policy / diplomatic intelligence collection).
- Likely operational objectives (as reflected in public reporting): targeted collection of documents and access to systems that hold diplomatic or foreign-ministry information, with an emphasis on sustained access (months-long dwell time described in reporting).

## 4. Targeting Profile
**Regions:** South America; Southeast Asia  
**Countries called out in public reporting:** Argentina, Brazil, Ecuador, Peru, Brunei, Malaysia  
**Sectors:** Government; diplomatic/foreign affairs institutions; foreign ministries and related bodies

## 5. Tradecraft Overview
Observed tradecraft themes across MITRE ATT&CK entries and reporting include:
- **Focused collection** behavior (e.g., searching for specific document types and time-scoped collections).
- **Credential access and monitoring** behavior consistent with credential dumping and keylogging.
- **Stealth and persistence enablers** through [[Masquerading as legitimate software]] and modular tooling (notably [[30_CIPHER/05_Malware/Felismus]]).
- **C2 over common protocols** (notably web protocols for [[30_CIPHER/05_Malware/Felismus]]), aligned with [[HTTP-based C2]] patterns.

## 6. MITRE ATT&CK Mapping
Techniques publicly associated with Sowbug and/or its linked software include:

**Collection / Staging**
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]

**Execution**
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]

**Credential Access**
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]

**Discovery**
- [[20_Entities/07_TTPs/T1135 - Network Share Discovery]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]

**Defense Evasion**
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]

**Command and Control**
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1132.001 - Data Encoding: Standard Encoding]]
- [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]

## 7. Malware & Tools Used
**Malware (publicly linked)**
- [[30_CIPHER/05_Malware/Felismus]] — modular backdoor/RAT associated with Sowbug; described as capable of remote command execution and modular extension.
- [[30_CIPHER/05_Malware/Starloader]] — loader component observed loading Felismus and associated tooling.

**Tools**
- No distinct tool names beyond the above malware components are consistently named across the cited sources in a way that is stable and broadly corroborated.

## 8. Infrastructure Patterns
Commonly described infrastructure/tradecraft patterns include:
- [[HTTP-based C2]] leveraging common web protocols (consistent with blending into normal traffic).
- [[Masquerading as legitimate software]] to reduce suspicion and extend dwell time.
- [[Archive staging for collection/exfiltration]] consistent with bundling and staging collected documents prior to transfer.
- [[Long-dwell access]] (months-scale persistence referenced in reporting).

## 9. Campaign History
- **2015-01-01 (at least):** Public reporting and MITRE ATT&CK describe activity dating to at least early 2015, with targeting against government entities in South America and Southeast Asia.
- **2017-03-01 (reported timeframe):** Reporting describes Symantec becoming aware of related activity in early 2017, with links to Felismus emerging in public narratives.
- **2017-11-07:** Multiple outlets publish coverage of Sowbug following Symantec reporting; victimology emphasizes foreign policy/diplomatic targets in South America and Southeast Asia.

## 10. Known Indicators
No indicators (domains, IPs, hashes, or other live IOCs) are included in this note.

## 11. Defensive Recommendations
- Prioritize detections and hunts aligned to the mapped behaviors: document discovery/collection, unusual archive creation/staging, and suspicious use of command shell execution consistent with post-compromise activity.
- Strengthen monitoring for [[Masquerading as legitimate software]] behaviors (unexpected process lineage, signed-binary lookalikes, anomalous installation/update artifacts).
- Increase visibility for credential access patterns associated with [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]] and [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] through endpoint telemetry and credential access auditing.
- Baseline and alert on anomalous outbound web traffic patterns consistent with [[HTTP-based C2]], especially from systems not expected to generate sustained or automated web protocol traffic.

## 12. Analyst Notes
- Sponsor attribution remains **unresolved** in the referenced public sources; treat claims of state backing as speculative unless supported by additional government advisories or legal actions.
- The strongest, most stable anchors for this actor profile are MITRE ATT&CK’s group/software entries and contemporaneous reporting that reiterates the same victimology and timeline.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0054/
- MITRE ATT&CK Software (Felismus): https://attack.mitre.org/software/S0171/
- MITRE ATT&CK Software (Starloader): https://attack.mitre.org/software/S0188/
- Dark Reading coverage (2017-11-07): https://www.darkreading.com/cyberattacks-data-breaches/south-america-the-target-of-sowbug-cyber-espionage-group
- CyberScoop coverage (2017-11-07): https://cyberscoop.com/previously-unknown-cyber-espionage-group-successfully-hacked-south-america-since-2015/
- LevelBlue background on Felismus (2017-04-25): https://levelblue.com/blogs/security-essentials/the-felismus-rat-powerful-threat-mysterious-purpose

## 14. References
1. https://attack.mitre.org/groups/G0054/
2. https://attack.mitre.org/software/S0171/
3. https://attack.mitre.org/software/S0188/
4. https://www.darkreading.com/cyberattacks-data-breaches/south-america-the-target-of-sowbug-cyber-espionage-group
5. https://cyberscoop.com/previously-unknown-cyber-espionage-group-successfully-hacked-south-america-since-2015/
6. https://levelblue.com/blogs/security-essentials/the-felismus-rat-powerful-threat-mysterious-purpose
7. https://www.silicon.co.uk/security/sowbug-hacking-group-224423
8. https://www.scworld.com/news/sowbug-apt-uses-felismus-backdoor-to-for-cyberespionage-operations
