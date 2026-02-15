---
entity_type: threat_actor
actor_name: "Axiom"
common_name: "Axiom"
actor_id: "G0001"
actor_type: "Nation-state / cyber espionage (suspected)"
aliases: ["Group 72"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2008-01"
last_seen: ""
status: "Unknown"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Intellectual property theft", "Strategic intelligence collection"]
victimology_summary: "Axiom is publicly described as a suspected Chinese cyber-espionage group targeting aerospace, defense, government, manufacturing, and media. Reporting highlights web-based initial access (including watering-hole and exploitation), credential access, and long-term persistence using multiple RAT families."
target_sectors: ["Aerospace", "Defense", "Government", "Manufacturing", "Media"]
target_regions: ["United States", "Japan", "Taiwan", "South Korea"]
related_groups: ["Winnti Group"]
malware: ["[[30_CIPHER/05_Malware/Derusbi]]", "[[30_CIPHER/05_Malware/gh0st RAT]]", "[[30_CIPHER/05_Malware/Hikit]]", "[[30_CIPHER/05_Malware/Hydraq]]", "[[30_CIPHER/05_Malware/PlugX]]", "[[30_CIPHER/05_Malware/PoisonIvy]]", "[[30_CIPHER/05_Malware/Zox]]"]
tools: []
infrastructure: ["[[Dynamic DNS]]", "[[Virtual Private Server]]", "[[Compromised Botnet Proxies]]", "[[Watering Hole]]", "[[SQL Injection]]"]
ttps: ["[[20_Entities/07_TTPs/T1583.002 - Acquire Infrastructure: DNS Server]]", "[[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]", "[[20_Entities/07_TTPs/T1560 - Archive Collected Data]]", "[[20_Entities/07_TTPs/T1584.005 - Compromise Infrastructure: Botnet]]", "[[20_Entities/07_TTPs/T1005 - Data from Local System]]", "[[20_Entities/07_TTPs/T1001.002 - Data Obfuscation: Steganography]]", "[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]", "[[20_Entities/07_TTPs/T1546.008 - Event Triggered Execution: Accessibility Features]]", "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]", "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]", "[[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]", "[[20_Entities/07_TTPs/T1566 - Phishing]]", "[[20_Entities/07_TTPs/T1563.002 - Remote Service Session Hijacking: RDP Hijacking]]", "[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]", "[[20_Entities/07_TTPs/T1553 - Subvert Trust Controls]]", "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0001): Axiom","Cisco Talos (2014-10-14): Threat Spotlight: Group 72","Novetta (archived): Operation SMN / Executive Summary PDF","Kaspersky Securelist (2013-04-11): Winnti. More than just a game","Kaspersky Securelist: Games are over"]
tags: ["threat-actor", "apt", "china", "cyber-espionage", "axiom", "group-72", "mitre-g0001"]
---

# Axiom

## 1. BLUF / Executive Summary
Axiom (MITRE ATT&CK **G0001**, also tracked as **Group 72**) is a suspected Chinese cyber-espionage actor assessed in public reporting as active since at least 2008. Open reporting associates the group with high-value strategic and intellectual property targeting across aerospace, defense, government, manufacturing, and media, using web-based access paths (including [[Watering Hole]] and [[SQL Injection]]), credential theft, and persistent access via multiple RAT families (e.g., [[30_CIPHER/05_Malware/Hikit]], [[30_CIPHER/05_Malware/Derusbi]], [[30_CIPHER/05_Malware/PlugX]]).

## 2. Attribution Notes
- Public sources consistently characterize Axiom as **suspected China-linked** and **espionage-motivated**, but attribution language remains probabilistic.
- MITRE notes reporting that suggests **some overlap** between Axiom and [[Winnti Group]], while also indicating they appear **distinct** based on publicly reported TTPs and targeting.
- “Axiom” and “Group 72” should be treated as **tracking designations**; incident attribution should be based on converging evidence (tradecraft + malware + infrastructure) rather than name-only claims.

## 3. Motivations & Objectives
- **Primary motivation:** Strategic intelligence collection and long-term access consistent with cyber espionage.
- **Primary objectives:** Acquisition of sensitive information (including IP), operational intelligence, and privileged network access to high-value organizations.

## 4. Targeting Profile
- **Sectors:** Aerospace, defense, government, manufacturing, and media are repeatedly cited in authoritative public reporting.
- **Geography:** Reporting highlights targets largely in the [[United States]], [[Japan]], [[Taiwan]], and [[South Korea]], with a focus on organizations holding valuable IP and strategic information.

## 5. Tradecraft Overview
- **Initial access:** Combination of [[Watering Hole]] activity and exploitation, including [[SQL Injection]] aligned to [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]] and [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]].
- **Credential access & privilege:** Use patterns consistent with [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- **Persistence & remote access:** Reliance on multiple malware families (RATs/rootkit-capable tooling) and remote access via RDP behaviors consistent with [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]] and [[20_Entities/07_TTPs/T1563.002 - Remote Service Session Hijacking: RDP Hijacking]].
- **Operational enablement:** Use of [[Dynamic DNS]] and [[Virtual Private Server]] infrastructure, plus [[Compromised Botnet Proxies]] for routing and operational resilience.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583.002 - Acquire Infrastructure: DNS Server]]
- [[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]
- [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]
- [[20_Entities/07_TTPs/T1584.005 - Compromise Infrastructure: Botnet]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1001.002 - Data Obfuscation: Steganography]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1546.008 - Event Triggered Execution: Accessibility Features]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]
- [[20_Entities/07_TTPs/T1566 - Phishing]]
- [[20_Entities/07_TTPs/T1563.002 - Remote Service Session Hijacking: RDP Hijacking]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1553 - Subvert Trust Controls]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]

## 7. Malware & Tools Used
- **Malware (RATs / backdoors) publicly associated with Axiom:**
  - [[30_CIPHER/05_Malware/Derusbi]]
  - [[30_CIPHER/05_Malware/gh0st RAT]]
  - [[30_CIPHER/05_Malware/Hikit]]
  - [[30_CIPHER/05_Malware/Hydraq]]
  - [[30_CIPHER/05_Malware/PlugX]]
  - [[30_CIPHER/05_Malware/PoisonIvy]]
  - [[30_CIPHER/05_Malware/Zox]]
- **Tools:** No specific distinct tooling names (beyond malware families) are consistently enumerated in the core authoritative sources cited in this note.

## 8. Infrastructure Patterns
- [[Dynamic DNS]] acquisition and use aligned to [[20_Entities/07_TTPs/T1583.002 - Acquire Infrastructure: DNS Server]].
- [[Virtual Private Server]] hosting aligned to [[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]].
- [[Compromised Botnet Proxies]] aligned to [[20_Entities/07_TTPs/T1584.005 - Compromise Infrastructure: Botnet]] for proxying/relay.
- Web-access patterns aligned with [[Watering Hole]] and [[SQL Injection]] activity.
- Use of [[Digital Certificates]] themes aligned to [[20_Entities/07_TTPs/T1553 - Subvert Trust Controls]] (as described in public reporting).

## 9. Campaign History
- **≥2008:** Public reporting (as summarized by MITRE ATT&CK) indicates targeting activity dating back to at least 2008.
- **2014:** “Operation SMN” public reporting and associated industry actions describe disruption-focused efforts and detailed characterization of Group 72/Axiom tradecraft and malware usage.
- **Ongoing/continuity:** Public reporting acknowledges name/cluster overlaps in the broader China-linked ecosystem (notably comparisons to [[Winnti Group]]), but available sources vary on the extent of shared infrastructure or personnel.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize detection and response for [[Watering Hole]] exposure and public-facing application compromise risk consistent with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]].
- Emphasize visibility for credential theft and post-compromise access patterns consistent with [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Maintain high confidence triage paths for activity associated with the malware families listed in this note (e.g., [[30_CIPHER/05_Malware/Hikit]], [[30_CIPHER/05_Malware/Derusbi]], [[30_CIPHER/05_Malware/PlugX]]) when corroborated by matching TTPs and infrastructure patterns.

## 12. Analyst Notes
- **Attribution confidence:** Medium (strong public reporting and ATT&CK mapping, but “suspected” language persists; overlaps with adjacent clusters increase misattribution risk).
- **Key analytic risk:** Ecosystem overlap narratives (e.g., with [[Winnti Group]]) can cause label drift; treat “Axiom” as a cluster definition bounded by corroborated TTP + malware + infrastructure evidence.
- **Indicator discipline:** Avoid relying on static IOCs for long-lived espionage clusters; infrastructure is frequently replaced or repurposed.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Axiom (G0001)  
  https://attack.mitre.org/groups/G0001/
- Cisco Talos — Threat Spotlight: Group 72 (Axiom)  
  https://blogs.cisco.com/security/talos/threat-spotlight-group-72
- Novetta (archived) — Executive Summary (Operation SMN)  
  https://web.archive.org/web/20230115144216/https://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf
- Kaspersky Securelist — Winnti. More than just a game  
  https://securelist.com/winnti-more-than-just-a-game/37029/
- Kaspersky Securelist — Games are over  
  https://securelist.com/games-are-over/70991/
- Lawfare — Axiom — A Chinese APT  
  https://www.lawfaremedia.org/article/axiom-chinese-apt

## 14. References
- MITRE ATT&CK. “Axiom (G0001).”  
  https://attack.mitre.org/groups/G0001/
- Cisco Talos. “Threat Spotlight: Group 72.” (2014-10-14)  
  https://blogs.cisco.com/security/talos/threat-spotlight-group-72
- Novetta (archived via Internet Archive). “Operation SMN — Executive Summary.”  
  https://web.archive.org/web/20230115144216/https://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf
- Kaspersky Securelist. “Winnti. More than just a game.” (2013-04-11)  
  https://securelist.com/winnti-more-than-just-a-game/37029/
- Kaspersky Securelist. “Games are over.”  
  https://securelist.com/games-are-over/70991/
- Lawfare. “Axiom — A Chinese APT.” (2014-10-28)  
  https://www.lawfaremedia.org/article/axiom-chinese-apt
