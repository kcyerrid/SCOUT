---
entity_type: threat_actor
actor_name: "Putter Panda"
common_name: "Putter Panda"
actor_id: "G0024"
actor_type: "State-linked cyber espionage (attributed)"
aliases: ["APT2","MSUpdater","PLA Unit 61486","TG-6952","Sulphur","Group 36","SearchFire","4HCrew"]
country_of_origin: "China (attributed)"
suspected_sponsors: ["People’s Liberation Army (PLA) Unit 61486 / 12th Bureau, 3rd Department (attributed)"]
attribution_confidence: "Medium"
first_seen: "2007-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Strategic intelligence collection","Information theft"]
objectives: ["Initial access via targeted phishing and document exploitation","Establish persistence and maintain access","Collect and exfiltrate sensitive data from targeted organizations"]
victimology_summary: "Putter Panda (MITRE ATT&CK G0024) is a China-attributed cyber espionage threat actor publicly linked to PLA Unit 61486 in multiple sources. Reporting commonly describes targeting of defense, aerospace/satellite, communications/space technology, research, and government-adjacent organizations, with a notable focus on U.S. and European entities."
target_sectors: ["Defense","Aerospace","Satellite/Space technology","Telecommunications/Communications technology","Research & academia","Government (reported)","Technology (hardware/software)"]
target_regions: ["United States","Europe"]
related_groups: ["APT1 (reported infrastructure/tool overlap)"]
malware: ["[[30_CIPHER/05_Malware/4H RAT]]","[[30_CIPHER/05_Malware/3PARA RAT]]","[[30_CIPHER/05_Malware/httpclient]]","[[30_CIPHER/05_Malware/pngdowner]]"]
tools: []
infrastructure: ["[[Spearphishing Attachment]]","[[Spearphishing Link]]","[[Compromised Web Infrastructure]]","[[Staging Servers]]","[[Dynamic DNS]]","[[HTTP C2]]","[[Encrypted C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]","[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]","[[20_Entities/07_TTPs/T1055.001 - Process Injection: Dynamic-link Library Injection]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1057 - Process Discovery]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]","[[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1552.001 - Unsecured Credentials: Credentials In Files]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Putter Panda (G0024): https://attack.mitre.org/groups/G0024/","CrowdStrike — Hat-tribution to PLA Unit 61486 (2014-06-09): https://www.crowdstrike.com/en-us/blog/hat-tribution-pla-unit-61486/","Council on Foreign Relations — Cyber Operations Tracker: Putter Panda (2014-06): https://www.cfr.org/cyber-operations/2014/06/10/putter-panda/","BlackBerry Research — Puttering into the Future… (2016-01-12): https://blogs.blackberry.com/en/2016/01/puttering-into-the-future","ETDA Threat Group Cards — Putter Panda, APT 2: https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Putter+Panda%2C+APT+2"]
tags: ["threat-actor","putter-panda","apt2","msupdater","g0024","china","cyber-espionage","aerospace","defense","satellite"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Putter Panda

## 1. BLUF / Executive Summary
Putter Panda (MITRE ATT&CK **G0024**) is a China-attributed cyber espionage threat actor publicly linked in multiple sources to **PLA Unit 61486**. Reporting commonly describes sustained targeting of **defense**, **aerospace/satellite**, **communications/space technology**, **research**, and **government-adjacent** entities, with emphasis on **U.S.** and **European** victimology. Publicly documented tradecraft includes targeted phishing and exploit-enabled delivery, custom malware families, persistence via common Windows autostart mechanisms, and web-protocol C2 with encrypted communications.

## 2. Attribution Notes
- MITRE ATT&CK describes Putter Panda as a Chinese threat group attributed to **Unit 61486** of the PLA’s broader intelligence apparatus.
- Public attribution narratives are largely sourced to private-sector reporting and OSINT-based analysis; this note treats state linkage as **attributed** rather than legally established.
- Some sources discuss overlap or proximity with other China-attributed clusters (including reported infrastructure/tool overlap with APT1), but these overlaps do not necessarily imply identical operators.

## 3. Motivations & Objectives
- **Motivation:** Espionage and strategic intelligence collection.
- **Objectives:** Gain initial access via socially engineered delivery and document exploitation; establish persistence; perform discovery to orient operators; collect and exfiltrate sensitive information relevant to targeted sectors (technology, aerospace/satellite, defense, research).

## 4. Targeting Profile
- **Sectors:** Defense contractors, aerospace/satellite and space-related technology, communications/telecom-adjacent technology, research organizations, and government-related targets (reported).
- **Regions:** Strong emphasis in public reporting on the **United States** and **Europe**, including space/satellite technology ecosystems.

## 5. Tradecraft Overview
- **Initial access:** Targeted phishing (attachments and links) and exploit-enabled document delivery (reported).
- **Persistence:** Use of Windows autostart extensibility points consistent with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]].
- **Defense evasion:** Attempts to degrade endpoint/security tooling consistent with [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]].
- **Obfuscation:** Encoded/encrypted payload artifacts consistent with [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]].
- **Post-compromise:** Discovery and operator enablement consistent with [[20_Entities/07_TTPs/T1057 - Process Discovery]], [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]], and [[20_Entities/07_TTPs/T1082 - System Information Discovery]].
- **C2:** Web-protocol communications and encrypted channels consistent with [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] and [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1055.001 - Process Injection: Dynamic-link Library Injection]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- [[20_Entities/07_TTPs/T1552.001 - Unsecured Credentials: Credentials In Files]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/4H RAT]] — malware family reported by MITRE as used by Putter Panda since at least 2007.
- [[30_CIPHER/05_Malware/3PARA RAT]] — MITRE-associated RAT linked to Putter Panda reporting.
- [[30_CIPHER/05_Malware/httpclient]] — MITRE-associated tooling reported in Putter Panda activity.
- [[30_CIPHER/05_Malware/pngdowner]] — MITRE-associated tooling reported in Putter Panda activity.
- Tools: none added beyond what authoritative public reporting explicitly associates.

## 8. Infrastructure Patterns
- Reliance on [[Spearphishing Attachment]] and [[Spearphishing Link]] delivery aligned to targeted victim selection.
- Use of [[Compromised Web Infrastructure]] and [[Staging Servers]] to host or relay payload stages (reported conceptually across sources).
- Use of [[Dynamic DNS]] and frequently refreshed infrastructure patterns reported in public analysis.
- Predominantly [[HTTP C2]] with [[Encrypted C2]] characteristics reported for multiple malware families associated with the group.

## 9. Campaign History
- **2007 (reported):** Public reporting describes the group operating since at least 2007.
- **2014-06 (public exposure):** CrowdStrike publicly documented Putter Panda / Unit 61486 attribution and victimology emphasis on defense and satellite/aerospace ecosystems.
- **2014-06 (contextual summary):** CFR’s Cyber Operations Tracker summarized Putter Panda’s espionage targeting of U.S. technology (communications/space/aerospace), research, defense, and government sectors.
- **2016-01 (follow-on research):** Additional public reporting discussed continued evolution and reuse/adaptation patterns following public exposure of the group.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Strengthen protections against targeted phishing consistent with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and the group’s long-running reliance on tailored delivery (e.g., attachment/link risk controls and high-signal detections for suspicious user-driven execution).
- Emphasize telemetry and alerting for persistence and autostart creation events aligned to [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] correlated with anomalous inbound communications.
- Improve visibility for defense impairment attempts aligned to [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]] (unexpected security-tool interference should be treated as a high-severity correlation amplifier).
- Monitor for obfuscated payload artifacts aligned to [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]] and process injection behaviors aligned to [[20_Entities/07_TTPs/T1055.001 - Process Injection: Dynamic-link Library Injection]].
- Detect suspicious web-protocol beaconing aligned to [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] and encrypted channel usage aligned to [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]] when correlated with new persistence and discovery bursts.

## 12. Analyst Notes
- Alias sprawl is significant (APT2, MSUpdater, TG-6952, Sulphur, etc.). Treat cross-vendor mappings conservatively unless a source explicitly equates clusters.
- This profile intentionally avoids publishing live IOCs or operational specifics; consult the primary reports for incident-scoped validation and evidence handling.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Putter Panda (G0024): https://attack.mitre.org/groups/G0024/
- CrowdStrike — Hat-tribution to PLA Unit 61486 (2014-06-09): https://www.crowdstrike.com/en-us/blog/hat-tribution-pla-unit-61486/
- CFR — Cyber Operations Tracker: Putter Panda (2014-06): https://www.cfr.org/cyber-operations/2014/06/10/putter-panda/
- BlackBerry Research — Puttering into the Future… (2016-01-12): https://blogs.blackberry.com/en/2016/01/puttering-into-the-future
- ETDA Threat Group Cards — Putter Panda, APT 2: https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Putter+Panda%2C+APT+2

## 14. References
1. MITRE ATT&CK. “Putter Panda (G0024).” https://attack.mitre.org/groups/G0024/
2. CrowdStrike. “Hat-tribution to PLA Unit 61486.” (2014-06-09). https://www.crowdstrike.com/en-us/blog/hat-tribution-pla-unit-61486/
3. Council on Foreign Relations. “Cyber Operations Tracker: Putter Panda.” (2014-06). https://www.cfr.org/cyber-operations/2014/06/10/putter-panda/
4. BlackBerry Blog. “Puttering into the Future…” (2016-01-12). https://blogs.blackberry.com/en/2016/01/puttering-into-the-future
5. Electronic Transactions Development Agency (ETDA). “Threat Group Cards: Putter Panda, APT 2.” https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Putter+Panda%2C+APT+2
---
