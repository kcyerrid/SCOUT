---
entity_type: threat_actor
actor_name: "Scarlet Mimic"
common_name: "Scarlet Mimic"
actor_id: "G0029"
actor_type: "Espionage-focused intrusion set (unattributed; suspected alignment with PRC interests per public reporting)"
aliases: []
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2012-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Surveillance / intelligence collection"]
objectives: ["Collect information on minority rights activists and associated networks","Maintain covert access via spearphishing and strategic web compromises","Expand collection from PCs to mobile devices (reported)"]
victimology_summary: "Scarlet Mimic (MITRE ATT&CK G0029) is a threat group primarily reported to target minority rights activists (notably Uyghur and Tibetan communities) and those interested in or supporting their causes. Public reporting states there is no direct evidence linking the activity to a government source, but assesses the motivations appear aligned with PRC interests. Reporting also describes targeting linked to government organizations in Russia and India responsible for tracking activist/terrorist activities. Tooling spans Windows, macOS, and Android, including the Windows backdoor [[30_CIPHER/05_Malware/FakeM]], macOS Trojan [[30_CIPHER/05_Malware/CallMe]], and Android spyware [[30_CIPHER/05_Malware/MobileOrder]]."
target_sectors: ["Civil society / NGOs","Minority rights activists","Activist supporters and researchers","Government (counter-terror / tracking units) (reported)"]
target_regions: ["Global (reported)","India (reported)","Russia (reported)"]
related_groups: ["Putter Panda (reported IP overlap; not concluded to be the same group)"]
malware: ["[[30_CIPHER/05_Malware/FakeM]]","[[30_CIPHER/05_Malware/CallMe]]","[[30_CIPHER/05_Malware/MobileOrder]]","[[30_CIPHER/05_Malware/Psylo]]","[[30_CIPHER/05_Malware/BrutishCommand]]","[[30_CIPHER/05_Malware/SkiBoot Loader]]","[[30_CIPHER/05_Malware/SubtractThis]]"]
tools: ["[[30_CIPHER/05_Malware/Tiny SHell]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Strategic Web Compromise]]","[[Decoy Documents]]","[[Self-Extracting RAR Archives]]","[[Right-to-Left Override]]","[[Protocol or Service Impersonation]]","[[Encrypted C2]]","[[Cross-platform malware]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override]]","[[20_Entities/07_TTPs/T1001.003 - Data Obfuscation: Protocol or Service Impersonation]]","[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]]","[[20_Entities/07_TTPs/T1059.004 - Command and Scripting Interpreter: Unix Shell]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]","[[20_Entities/07_TTPs/T1005 - Data from Local System]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1057 - Process Discovery]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Scarlet Mimic (G0029) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0029/","Palo Alto Networks Unit 42 — Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists (2016-01-24): https://unit42.paloaltonetworks.com/scarlet-mimic-years-long-espionage-targets-minority-activists/","MITRE ATT&CK — FakeM (S0076): https://attack.mitre.org/software/S0076/","MITRE ATT&CK — CallMe (S0077): https://attack.mitre.org/software/S0077/","MITRE ATT&CK — MobileOrder (S0079): https://attack.mitre.org/software/S0079/","Check Point Research — 7 Years of Scarlet Mimic’s Mobile Surveillance Campaign Targeting Uyghurs (2022-09-22): https://research.checkpoint.com/2022/never-truly-left-7-years-of-scarlet-mimics-mobile-surveillance-campaign-targeting-uyghurs/","Citizen Lab — Palo Alto Networks report on Scarlet Mimic cited Citizen Lab work (2016-01-28): https://citizenlab.ca/2016/01/citizen-lab-palo-alto-networks-scarlet-mimic/"]
tags: ["threat-actor","scarlet-mimic","g0029","minority-rights","uyghur","tibetan","surveillance","fakem","mobileorder"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Scarlet Mimic

## 1. BLUF / Executive Summary
Scarlet Mimic (MITRE ATT&CK **G0029**) is an espionage-focused intrusion set most prominently reported for targeting **Uyghur and Tibetan activists** and adjacent communities (supporters, researchers, and others interested in these causes). Public reporting states there is **no direct evidence** linking the activity to a government source, but assesses the motivations appear aligned with **PRC interests**. Reporting describes a multi-platform toolkit spanning **Windows** ([[30_CIPHER/05_Malware/FakeM]] and multiple loaders), **macOS** ([[30_CIPHER/05_Malware/CallMe]]), and **Android** ([[30_CIPHER/05_Malware/MobileOrder]]), with campaigns characterized by **spearphishing**, **strategic web compromises**, and extensive use of **decoy content**.

## 2. Attribution Notes
- Scarlet Mimic is tracked by MITRE as **G0029** and described as **not directly linked** to a government source, while noting motivation overlap with PRC positions on relevant targets.
- Public reporting notes **overlap in IP usage** with Putter Panda but explicitly does **not** conclude the groups are the same.
- Attribution in this note is therefore treated as **suspected alignment** rather than confirmed sponsorship.

## 3. Motivations & Objectives
- **Motivation:** Surveillance and intelligence collection related to minority rights activism and associated networks.
- **Objectives:** Gain access via [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] pathways; maintain covert command-and-control; collect and exfiltrate targeted information from endpoints and mobile devices; extend operational reach across platforms.

## 4. Targeting Profile
- **Primary targets:** Uyghur and Tibetan activists and those interested in or supporting their causes.
- **Additional reported targets:** Government organizations in Russia and India responsible for tracking activist/terrorist activity (reported in vendor research).
- **Target selection theme:** Individuals and entities with access to information relevant to minority rights communities and monitoring efforts.

## 5. Tradecraft Overview
- **Delivery:** Heavy use of [[Spearphishing Attachment]] with decoy documents and, in at least one publicly described period, a [[Strategic Web Compromise]] (watering-hole style) approach.
- **Execution:** Exploit-enabled documents (reported) consistent with [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]; also direct user-trick execution via archives/executables consistent with [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- **Masquerading:** Use of [[Right-to-Left Override]] in filenames consistent with [[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override]].
- **C2 / concealment:** [[30_CIPHER/05_Malware/FakeM]] is described with [[Protocol or Service Impersonation]] and encrypted communications behaviors reflected in ATT&CK software technique associations.
- **Cross-platform:** Reported evolution from PC-focused operations to mobile surveillance, with long-running Android spyware activity described in later research.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override]]
- [[20_Entities/07_TTPs/T1001.003 - Data Obfuscation: Protocol or Service Impersonation]]
- [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]]
- [[20_Entities/07_TTPs/T1059.004 - Command and Scripting Interpreter: Unix Shell]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/FakeM]] — Windows backdoor associated with Scarlet Mimic in public reporting; described as modular, including keylogging capability and C2 concealment behaviors (per ATT&CK software entry).
- [[30_CIPHER/05_Malware/CallMe]] — macOS Trojan associated with Scarlet Mimic; described as based on [[30_CIPHER/05_Malware/Tiny SHell]] (per ATT&CK software entry).
- [[30_CIPHER/05_Malware/MobileOrder]] — Android spyware associated with Scarlet Mimic; described as supporting broad device data collection and operator tasking (per ATT&CK software entry and follow-on research).
- [[30_CIPHER/05_Malware/BrutishCommand]] — loader family described in public reporting as used to decrypt/load FakeM.
- [[30_CIPHER/05_Malware/SkiBoot Loader]] — loader family described in public reporting as used to decrypt/load FakeM.
- [[30_CIPHER/05_Malware/SubtractThis]] — loader family referenced in public reporting as part of the broader tooling ecosystem.
- [[30_CIPHER/05_Malware/Psylo]] — Windows Trojan referenced in public reporting as part of the Scarlet Mimic tooling set.
- [[30_CIPHER/05_Malware/Tiny SHell]] — publicly available tool noted as the basis for CallMe in ATT&CK’s software description.

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] with [[Decoy Documents]] to reduce user suspicion post-execution.
- [[Strategic Web Compromise]] (watering-hole style) used in at least one publicly described operation window.
- [[Self-Extracting RAR Archives]] and filename [[Right-to-Left Override]] to disguise executable payloads.
- C2 concealment themes including [[Protocol or Service Impersonation]] and [[Encrypted C2]] behaviors (as reflected in ATT&CK software technique associations).

## 9. Campaign History
- **~2012 (reported):** Unit 42 reported the attacks began “over four years” before the 2016 publication date (i.e., at least early-2012 activity).
- **2013 (reported):** Unit 42 describes Scarlet Mimic activity publicly exposed in 2013 (earlier FakeM coverage) and references a watering-hole/strategic web compromise event in that period.
- **2015 (reported):** Unit 42 describes “most recent” attacks identified in 2015 and notes expansion from PCs toward mobile targeting in the observed evolution.
- **2016-01-24:** Unit 42 publishes the consolidated Scarlet Mimic report, linking Windows, macOS, and Android toolchains via infrastructure and victimology.
- **2015–2022 (reported):** Check Point Research describes a multi-year MobileOrder surveillance campaign targeting Uyghurs, assessing continuity with Scarlet Mimic based on code/infrastructure/victimology overlaps.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Emphasize controls against targeted phishing aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and user-driven execution aligned to [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]], with special attention to archive-based delivery and deceptive filenames.
- Improve detection of masquerading patterns aligned to [[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override]] in attachment workflows and downloaded content.
- Maintain visibility into suspicious egress and encrypted channel behaviors aligned to [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]] and abnormal data movement aligned to [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]].
- Include mobile threat considerations where relevant to your risk model; Scarlet Mimic reporting includes Android surveillance tooling with broad collection capabilities.

## 12. Analyst Notes
- Scarlet Mimic attribution is best treated as **unattributed with suspected PRC-aligned motivations**; multiple reputable sources explicitly avoid claiming direct state linkage.
- Overlap with other China-attributed clusters (e.g., reported IP overlap with Putter Panda) should be handled cautiously and does not imply equivalence.
- Publicly available reporting contains extensive historical indicators; this note intentionally excludes IOCs to remain SCOUT-compliant and avoid operationalizing stale data.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Scarlet Mimic (G0029): https://attack.mitre.org/groups/G0029/
- Unit 42 — Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists (2016-01-24): https://unit42.paloaltonetworks.com/scarlet-mimic-years-long-espionage-targets-minority-activists/
- MITRE ATT&CK — FakeM (S0076): https://attack.mitre.org/software/S0076/
- MITRE ATT&CK — CallMe (S0077): https://attack.mitre.org/software/S0077/
- MITRE ATT&CK — MobileOrder (S0079): https://attack.mitre.org/software/S0079/
- Check Point Research — 7 Years of Scarlet Mimic’s Mobile Surveillance Campaign Targeting Uyghurs (2022-09-22): https://research.checkpoint.com/2022/never-truly-left-7-years-of-scarlet-mimics-mobile-surveillance-campaign-targeting-uyghurs/
- Citizen Lab — Context on civil society targeting referenced by Scarlet Mimic reporting (2016-01-28): https://citizenlab.ca/2016/01/citizen-lab-palo-alto-networks-scarlet-mimic/

## 14. References
1. MITRE ATT&CK. “Scarlet Mimic (G0029).” (Last Modified 2025-04-25). https://attack.mitre.org/groups/G0029/
2. Palo Alto Networks Unit 42. “Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists.” (2016-01-24). https://unit42.paloaltonetworks.com/scarlet-mimic-years-long-espionage-targets-minority-activists/
3. MITRE ATT&CK. “FakeM (S0076).” https://attack.mitre.org/software/S0076/
4. MITRE ATT&CK. “CallMe (S0077).” https://attack.mitre.org/software/S0077/
5. MITRE ATT&CK. “MobileOrder (S0079).” https://attack.mitre.org/software/S0079/
6. Check Point Research. “7 Years of Scarlet Mimic’s Mobile Surveillance Campaign Targeting Uyghurs.” (2022-09-22). https://research.checkpoint.com/2022/never-truly-left-7-years-of-scarlet-mimics-mobile-surveillance-campaign-targeting-uyghurs/
7. Citizen Lab. “Citizen Lab cited in report on malware campaign against Tibetan, Uyghur activists.” (2016-01-28). https://citizenlab.ca/2016/01/citizen-lab-palo-alto-networks-scarlet-mimic/
---
