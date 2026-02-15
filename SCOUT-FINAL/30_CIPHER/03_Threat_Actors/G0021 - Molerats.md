---
entity_type: threat_actor
actor_name: "Molerats"
common_name: "MoleRats"
actor_id: "G0021"
actor_type: "Politically motivated cyber espionage"
aliases: ["Operation Molerats","Gaza Cybergang","Gaza Cybergang Group1","Gaza Hacking Team","TA402","Extreme Jackal","ALUMINUM SARATOGA"]
country_of_origin: "Palestinian Territories / Gaza (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2012-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Political objectives","Information theft"]
objectives: ["Intelligence collection against regional political and security targets","Credential and document theft","Host reconnaissance and data exfiltration"]
victimology_summary: "Molerats (G0021), also tracked under labels including Gaza Cybergang and TA402, is an Arabic-language, politically motivated threat actor active since at least 2012. Public reporting describes primary targeting across the Middle East and North Africa (MENA), with additional victimology in Europe and the United States. Campaigns are commonly phishing-led, with multi-stage delivery chains and a malware ecosystem that includes multiple .NET and Windows backdoors (e.g., DustySky, Spark, DropBook, SharpStage, MoleNet, and LastConn), as well as periodic use of commodity tooling."
target_sectors: ["Government","Diplomatic (embassies)","Telecommunications","Education","Media","Civil society (journalists, activists, political personnel)","Defense/Aerospace (reported)","Financial institutions (reported)"]
target_regions: ["Middle East","North Africa","Palestinian Territories","Israel","Egypt","Saudi Arabia","United Arab Emirates","Iraq","Turkey","Europe","United States"]
related_groups: ["APT-C-23 (Arid Viper) (reported overlap in some campaigns)"]
malware: ["[[30_CIPHER/05_Malware/DustySky]]","[[30_CIPHER/05_Malware/Spark]]","[[30_CIPHER/05_Malware/DropBook]]","[[30_CIPHER/05_Malware/SharpStage]]","[[30_CIPHER/05_Malware/MoleNet]]","[[30_CIPHER/05_Malware/PoisonIvy]]","[[30_CIPHER/05_Malware/LastConn]]","[[30_CIPHER/05_Malware/Pierogi]]"]
tools: ["[[30_CIPHER/05_Malware/BrowserPasswordDump]]","[[30_CIPHER/05_Malware/Enigma Protector]]"]
infrastructure: ["[[Spearphishing attachments]]","[[Spearphishing links]]","[[Staged payload delivery]]","[[RAR/ZIP delivery]]","[[Paste sites staging]]","[[Public file-hosting staging]]","[[Disposable emails/domains]]","[[Cloud/web service abuse]]"]
ttps: ["[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]","[[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]","[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1027.015 - Obfuscated Files or Information: Compression]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1057 - Process Discovery]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1218.007 - System Binary Proxy Execution: Msiexec]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Molerats (G0021) (Last Modified 2024-11-17)","ClearSky (2016-01) — Operation DustySky (PDF)","Kaspersky Securelist (2019-04-10) — Gaza Cybergang Group1, Operation SneakyPastes","Palo Alto Networks Unit 42 (2020-03-03) — Molerats Delivers Spark Backdoor","Cybereason Nocturnus (2020-12-09) — Molerats in the Cloud (PDF)","Proofpoint (2021-06-17) — New TA402 (Molerats) Malware Targets Governments in the Middle East"]
tags: ["threat-actor","molerats","mole-rats","g0021","gaza-cybergang","ta402","middle-east","politically-motivated","espionage"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Molerats

## 1. BLUF / Executive Summary
Molerats (MITRE ATT&CK **G0021**) is an Arabic-language, politically motivated cyber espionage actor operating since at least 2012. Reporting consistently places its primary victimology in the **MENA region**, with additional targeting documented in **Europe** and the **United States**. Campaigns are commonly **phishing-led** and use multi-stage delivery chains that culminate in Windows/.NET backdoors (notably [[30_CIPHER/05_Malware/DustySky]] and [[30_CIPHER/05_Malware/Spark]]), with periodic evolution into cloud/web-service-abusing tooling (e.g., [[30_CIPHER/05_Malware/DropBook]]).

## 2. Attribution Notes
- MITRE ATT&CK characterizes Molerats as Arabic-speaking and politically motivated, with long-running activity since 2012.
- Vendor and research reporting frequently uses the “Gaza Cybergang” framing and describes targeting patterns aligned to Palestinian and broader regional political issues; public sources vary in how they segment “Gaza Cybergang” into sub-groups/campaign clusters (e.g., “Group1” ≈ MoleRats in some reporting).
- Sponsorship attribution is not consistently established in primary public advisories; this note remains conservative on sponsor claims.

## 3. Motivations & Objectives
- **Motivations:** Politically aligned espionage and information theft.
- **Objectives:** Steal sensitive documents and credentials from targeted entities; conduct host reconnaissance; sustain access long enough to enable collection and exfiltration.

## 4. Targeting Profile
- **Regions:** Predominantly MENA (including the Palestinian Territories), with additional documented targeting in Europe and the United States.
- **Sectors/communities frequently cited:** Government and diplomatic entities (including embassies), education, media outlets, journalists/activists/political personnel, and government-adjacent organizations. Some reporting also describes telecom, and episodic targeting outside the actor’s “typical” set.

## 5. Tradecraft Overview
- **Initial access:** Email-borne phishing using attachments and links (often requiring user interaction such as enabling content or opening an archive).
- **Multi-stage delivery:** Use of staged payload retrieval and chained stages to extend infrastructure longevity and reduce single-point detections.
- **Living-off-the-web staging:** Use of paste sites and common file hosting / web services as intermediate distribution or comms channels (reported in some campaigns).
- **Persistence:** Common persistence via Startup folder / Registry Run Keys and scheduled tasks in some observed activity.
- **Evasion/obfuscation:** Use of compression, deobfuscation/decoding routines, and (in some cases) packers; selective execution guardrails have been reported (e.g., regional keyboard/locale checks).
- **Credential access:** Reported use of browser credential dumping via publicly available tools.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1027.015 - Obfuscated Files or Information: Compression]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- [[20_Entities/07_TTPs/T1218.007 - System Binary Proxy Execution: Msiexec]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]

## 7. Malware & Tools Used
**Malware / implants (representative, per public reporting and ATT&CK software associations)**
- [[30_CIPHER/05_Malware/DustySky]] (aka “NeD Worm” in some reporting)
- [[30_CIPHER/05_Malware/Spark]]
- [[30_CIPHER/05_Malware/DropBook]]
- [[30_CIPHER/05_Malware/SharpStage]]
- [[30_CIPHER/05_Malware/MoleNet]]
- [[30_CIPHER/05_Malware/PoisonIvy]]
- [[30_CIPHER/05_Malware/LastConn]]
- [[30_CIPHER/05_Malware/Pierogi]]

**Tools / supporting utilities (reported)**
- [[30_CIPHER/05_Malware/BrowserPasswordDump]]
- [[30_CIPHER/05_Malware/Enigma Protector]] (packer reported in some Spark-related activity)

## 8. Infrastructure Patterns
- Recurrent [[Spearphishing attachments]] and [[Spearphishing links]] delivering [[RAR/ZIP delivery]] or document-based lures.
- [[Disposable emails/domains]] used to support campaign infrastructure (reported in some operations).
- Use of [[Paste sites staging]] and [[Public file-hosting staging]] to distribute intermediate stages (reported in some campaigns).
- [[Cloud/web service abuse]] for staging and/or comms in certain campaigns (reported by multiple vendors).

## 9. Campaign History
- **2012 (at least):** MITRE ATT&CK reports Molerats operating since 2012.
- **2015–2016:** “Operation DustySky” reporting describes phishing-led intrusions delivering DustySky/NeD Worm against regional and international targets.
- **2018–2019:** Kaspersky’s “Operation SneakyPastes” describes “Gaza Cybergang Group1 (MoleRATs)” using paste sites and chained stages to deliver RAT capabilities, with a broad victim set including embassies and political personnel.
- **2019–2020:** Unit 42 reports phishing activity delivering [[30_CIPHER/05_Malware/Spark]] and highlights continued development and operationalization.
- **2020–2021:** Cybereason describes “Molerats in the Cloud” campaigns leveraging new backdoors and abuse of cloud platforms; Proofpoint reports TA402 (Molerats) distributing [[30_CIPHER/05_Malware/LastConn]] against government/government-adjacent targets tied to regional geopolitics.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Reduce exposure to phishing-driven initial access consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]] through layered email controls, attachment/link risk reduction, and strong endpoint visibility.
- Improve detection for user-driven execution chains consistent with [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]] and [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]] (especially archive-based delivery and “enable content” social engineering themes).
- Monitor persistence signals consistent with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]] when correlated with inbound phishing activity.
- Track tool-transfer and staging behaviors consistent with [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]] and obfuscation patterns consistent with [[20_Entities/07_TTPs/T1027.015 - Obfuscated Files or Information: Compression]] and [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]].
- Watch for browser credential access patterns consistent with [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]] and treat it as a high-severity correlation amplifier in targeted environments.

## 12. Analyst Notes
- Public reporting uses multiple overlapping labels (Molerats, Gaza Cybergang, TA402) and sometimes partitions activity into “sub-groups.” Maintain conservative entity resolution unless you have campaign-level clustering evidence.
- This note intentionally omits IOCs and step-by-step tradecraft details; consult the original reports for technical appendices when required for incident-specific validation.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Molerats (G0021): https://attack.mitre.org/groups/G0021/
- ClearSky — Operation DustySky (2016-01, PDF): https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf
- Kaspersky Securelist — Gaza Cybergang Group1, Operation SneakyPastes (2019-04-10): https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/
- Palo Alto Networks Unit 42 — Molerats Delivers Spark Backdoor (2020-03-03): https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/
- Cybereason — Molerats in the Cloud (2020-12-09, PDF): https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf
- Proofpoint — New TA402 (Molerats) Malware Targets Governments in the Middle East (2021-06-17): https://www.proofpoint.com/us/blog/threat-insight/new-ta402-molerats-malware-targets-governments-middle-east

## 14. References
- MITRE ATT&CK. “Molerats (G0021).” (Last Modified 2024-11-17). https://attack.mitre.org/groups/G0021/
- ClearSky. “Operation DustySky.” (2016-01, PDF). https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf
- Kaspersky GReAT (Securelist). “Gaza Cybergang Group1, operation SneakyPastes.” (2019-04-10). https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/
- Palo Alto Networks Unit 42. “Molerats Delivers Spark Backdoor to Government and Telecommunications Organizations.” (2020-03-03). https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/
- Cybereason Nocturnus Team. “MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign.” (2020-12-09, PDF). https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf
- Proofpoint. “New TA402 Molerats Malware Targets Governments in the Middle East.” (2021-06-17). https://www.proofpoint.com/us/blog/threat-insight/new-ta402-molerats-malware-targets-governments-middle-east
---
