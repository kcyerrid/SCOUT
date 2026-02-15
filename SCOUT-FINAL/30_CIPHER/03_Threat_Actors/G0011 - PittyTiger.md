---
entity_type: threat_actor
actor_name: "PittyTiger"
common_name: "PittyTiger"
actor_id: "G0011"
actor_type: "Cyber espionage (suspected China-nexus; possibly mercenary)"
aliases: ["Pitty Panda", "APT24", "Temp.Pittytiger"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2011-01"
last_seen: ""
status: "Unknown"
motivations: ["Information theft", "Espionage"]
objectives: ["Sustain command-and-control using multiple malware families", "Credential theft and access enablement", "Targeted data theft against high-value organizations"]
victimology_summary: "PittyTiger (MITRE ATT&CK G0011) is assessed in public reporting as a China-linked intrusion set active since at least 2011. Reporting describes targeting of private-sector organizations (notably defense and telecommunications) and at least one government entity, with observed activity affecting targets in Taiwan and Europe. The actor is characterized by use of multiple RAT families and credential-focused tradecraft; some reporting suggests the group may be opportunistic and potentially operating as a mercenary capability."
target_sectors: ["Defense", "Telecommunications", "Government", "Web development"]
target_regions: ["Taiwan", "Europe"]
related_groups: ["APT 5 / Keyhole Panda (reported overlap)"]
malware: ["[[30_CIPHER/05_Malware/gh0st RAT]]", "[[30_CIPHER/05_Malware/Lurid]]", "[[30_CIPHER/05_Malware/PoisonIvy]]", "[[30_CIPHER/05_Malware/Paladin RAT]]", "[[30_CIPHER/05_Malware/Leo RAT]]", "[[30_CIPHER/05_Malware/pgift]]", "[[30_CIPHER/05_Malware/Pitty]]"]
tools: ["[[30_CIPHER/05_Malware/Mimikatz]]", "[[30_CIPHER/05_Malware/gsecdump]]"]
infrastructure: ["[[Command and Control]]", "[[Remote Access Trojan]]", "[[Spearphishing]]", "[[Credential Theft]]"]
ttps: ["[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]", "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (G0011): PittyTiger (Last modified 2025-04-25)","ETDA Threat Group Cards: PittyTiger, Pitty Panda (Last change 2025-08-16)","SecurityWeek (2014-08-01): \"Pitty Tiger\" Threat Actors Possibly Active Since 2008: FireEye"]
tags: ["threat-actor", "apt", "china", "espionage", "pittytiger", "pitty-panda", "mitre-g0011"]
---

# PittyTiger

## 1. BLUF / Executive Summary
PittyTiger (MITRE ATT&CK **G0011**, also reported as **Pitty Panda**) is a suspected China-nexus threat group associated with cyber espionage and information theft, active since at least **2011**. Public reporting describes targeted activity against private-sector organizations—especially **defense** and **telecommunications**—and at least one government entity, with observed targeting in **Taiwan** and **Europe**. The cluster is characterized by use of multiple RAT families for command-and-control and credential acquisition to sustain access.

## 2. Attribution Notes
- **MITRE framing:** MITRE ATT&CK assesses PittyTiger as “believed to operate out of China” and highlights the actor’s use of multiple malware types to maintain C2.
- **Alias variance:** “Pitty Panda” is used in some tracking; “APT24” also appears in some public catalogs. These labels can be inconsistent across vendors and should be treated as *potentially overlapping* rather than automatically equivalent.
- **Mercenary hypothesis:** Some reporting (summarized in public actor cards) suggests PittyTiger may be opportunistic and potentially operates as a service for private-sector competitors; this remains less definitive than the China-nexus assessment and should be treated cautiously.

## 3. Motivations & Objectives
- **Motivations:** Espionage and information theft.
- **Objectives:** Maintain persistent access through multiple RAT toolchains, acquire credentials for access enablement, and exfiltrate sensitive information from high-value organizations.

## 4. Targeting Profile
- **Primary sectors reported:** Defense and telecommunications; also at least one government target and “web development” noted in public actor card summaries.
- **Geography reported:** Taiwan and Europe are explicitly cited in public actor-card summaries; broader scope is not consistently enumerated in the most authoritative public sources.

## 5. Tradecraft Overview
- **Credential-focused access:** Public reporting and MITRE technique mapping emphasize credential acquisition and use of legitimate credentials consistent with [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- **Tool acquisition and use:** MITRE notes PittyTiger obtained and used tools such as [[30_CIPHER/05_Malware/Mimikatz]] and [[30_CIPHER/05_Malware/gsecdump]], aligning with [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]].
- **Multi-RAT operations:** Reporting describes shifting among multiple RAT families (including variants associated with [[30_CIPHER/05_Malware/gh0st RAT]] and [[30_CIPHER/05_Malware/PoisonIvy]]) as part of sustained C2 and remote operator control.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]

## 7. Malware & Tools Used
- **Malware / RATs (reported):**
  - [[30_CIPHER/05_Malware/gh0st RAT]]
  - [[30_CIPHER/05_Malware/Lurid]]
  - [[30_CIPHER/05_Malware/PoisonIvy]]
  - [[30_CIPHER/05_Malware/Paladin RAT]]
  - [[30_CIPHER/05_Malware/Leo RAT]]
  - [[30_CIPHER/05_Malware/pgift]]
  - [[30_CIPHER/05_Malware/Pitty]]
- **Tools (reported):**
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/gsecdump]]

## 8. Infrastructure Patterns
- Use of [[Remote Access Trojan]] families for [[Command and Control]] and interactive access across campaigns.
- Reliance on [[Spearphishing]]-style delivery described in public reporting (high-level), with follow-on credential use consistent with [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Malware/tool diversity and rotation as an operational pattern to sustain access while varying artifacts.

## 9. Campaign History
- **2011 (reported):** “Operation ‘The Eye of the Tiger’” is cited in public actor-card summaries as an early named operation associated with the cluster.
- **2014 (reported):** Public reporting describes spearphishing activity against a French company and multi-language lures; actor-card summaries note discovery of an active C2 server during mid-2014 analysis.
- **2008 (possible earlier activity):** A FireEye analysis summarized in journalism suggests PittyTiger activity may extend back to 2008, including historical association with RAT usage; this is less consistently documented than the “since at least 2011” baseline.

## 10. Known Indicators
No stable public indicators are included in this note. IOC handling should be incident-specific and validated against current, authoritative reporting.

## 11. Defensive Recommendations
- Increase monitoring and response readiness for credential abuse patterns consistent with [[20_Entities/07_TTPs/T1078 - Valid Accounts]] in high-value environments (defense, telecom, and adjacent supply chains).
- Treat detections of widely used post-exploitation tools (e.g., [[30_CIPHER/05_Malware/Mimikatz]] / [[30_CIPHER/05_Malware/gsecdump]]) as higher-signal when correlated with PittyTiger-aligned victimology and concurrent RAT activity.
- Maintain strong controls around user-driven infection vectors (e.g., email-borne lure exposure) and prioritize rapid containment of RAT footholds to prevent follow-on credential theft and lateral enablement.

## 12. Analyst Notes
- **Attribution confidence:** Medium (MITRE China-nexus assessment + multiple public summaries; limited direct, easily accessible primary reporting in this workflow due to source availability constraints).
- **Label management:** Keep “PittyTiger” (G0011) as the primary cluster key and track “Pitty Panda/APT24” as aliases with explicit provenance to avoid accidental merges with unrelated “APT24” usage in other taxonomies.
- **Overlap caveat:** Reported overlap with “APT 5 / Keyhole Panda” appears in public actor-card summaries and should be treated as a potential analytic linkage requiring corroboration by malware lineage and victimology.

## 13. Further Reading / External Resources
- MITRE ATT&CK — PittyTiger (G0011)  
  https://attack.mitre.org/groups/G0011/
- ETDA Threat Group Cards — PittyTiger, Pitty Panda (last change 2025-08-16)  
  https://apt.etda.or.th/cgi-bin/showcard.cgi?g=PittyTiger%2C+Pitty+Panda
- SecurityWeek — “Pitty Tiger” Threat Actors Possibly Active Since 2008: FireEye (2014-08-01)  
  https://www.securityweek.com/pitty-tiger-threat-actors-possibly-active-2008-fireeye/

## 14. References
- MITRE ATT&CK. “PittyTiger (G0011).” (Last modified 2025-04-25)  
  https://attack.mitre.org/groups/G0011/
- Electronic Transactions Development Agency (ETDA). “Threat Group Cards: PittyTiger, Pitty Panda.” (Last change 2025-08-16)  
  https://apt.etda.or.th/cgi-bin/showcard.cgi?g=PittyTiger%2C+Pitty+Panda
- SecurityWeek. “'Pitty Tiger' Threat Actors Possibly Active Since 2008: FireEye.” (2014-08-01)  
  https://www.securityweek.com/pitty-tiger-threat-actors-possibly-active-2008-fireeye/
