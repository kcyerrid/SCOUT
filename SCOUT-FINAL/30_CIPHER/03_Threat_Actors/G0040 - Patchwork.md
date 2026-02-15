---
entity_type: threat_actor
actor_name: "Patchwork"
common_name: "Patchwork"
actor_id: "G0040"
actor_type: "Cyber espionage threat group; circumstantial evidence suggests pro-Indian/India-linked interests (unconfirmed)"
aliases: ["Hangover Group","Dropping Elephant","Chinastrats","MONSOON","Operation Hangover"]
country_of_origin: "India (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2015-12-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Conduct intelligence collection against diplomatic/government-adjacent targets","Initial access via spearphishing and watering-hole activity","Exploit client-side vulnerabilities through malicious documents","Persist and stage collection with lightweight tooling and malware modules","Use signed malware (including self-signed certificates) to increase trust and reduce detection"]
victimology_summary: "Patchwork (MITRE ATT&CK G0040) is a cyber espionage group first publicly observed in December 2015. The group has not been definitively attributed, though MITRE notes circumstantial evidence suggesting it may be a pro-Indian or Indian entity. Reporting ties Patchwork to sustained targeting of diplomatic and government-related organizations, with campaigns documented across South Asia and (in 2018) spearphishing activity targeting U.S. think tanks. Public sources describe frequent reuse of publicly available code and off-the-shelf tooling alongside custom malware, including [[30_CIPHER/05_Malware/BADNEWS]] (S0128), [[30_CIPHER/05_Malware/BackConfig]] (S0475), [[30_CIPHER/05_Malware/AutoIt backdoor]] (S0129), and [[30_CIPHER/05_Malware/NDiskMonitor]] (S0272)."
target_sectors: ["Government","Diplomacy / foreign affairs","Think tanks","International affairs NGOs (reported)"]
target_regions: ["South Asia","United States (think tanks, reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/BADNEWS]]","[[30_CIPHER/05_Malware/BackConfig]]","[[30_CIPHER/05_Malware/AutoIt backdoor]]","[[30_CIPHER/05_Malware/NDiskMonitor]]"]
tools: ["[[30_CIPHER/05_Malware/PowerSploit]]","[[30_CIPHER/05_Malware/QuasarRAT]]","[[30_CIPHER/05_Malware/Meterpreter]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Spearphishing Link]]","[[Watering hole delivery]]","[[Exploit-laden Office documents]]","[[DDE-based execution]]","[[Dead drop resolver]]","[[BITS-based payload delivery]]","[[Self-signed code-signing]]","[[DLL side-loading]]","[[Tracking pixels / web bugs]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1197 - BITS Jobs]]","[[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]","[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1587.002 - Develop Capabilities: Code Signing Certificates]]","[[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]","[[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Patchwork (G0040) (Last Modified 2025-10-21): https://attack.mitre.org/groups/G0040/","MITRE ATT&CK — BADNEWS (S0128) (Last Modified 2025-04-25): https://attack.mitre.org/software/S0128/","MITRE ATT&CK — BackConfig (S0475) (Last Modified 2025-04-16): https://attack.mitre.org/software/S0475/","MITRE ATT&CK — AutoIt backdoor (S0129) (Last Modified 2025-04-25): https://attack.mitre.org/software/S0129/","MITRE ATT&CK — NDiskMonitor (S0272) (Last Modified 2025-04-25): https://attack.mitre.org/software/S0272/","Forcepoint Security Labs — MONSOON: Analysis of an APT Campaign (2016-08-08) (PDF): https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf","Trend Micro — Untangling the Patchwork Cyberespionage Group (2017-12-11) (PDF): https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf","Palo Alto Networks Unit 42 — Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent (2018-03-07): https://unit42.paloaltonetworks.com/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/","Volexity — Patchwork APT Group Targets US Think Tanks (2018-06-07): https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/"]
tags: ["threat-actor","patchwork","g0040","dropping-elephant","hangover-group","monsoon","cyber-espionage","south-asia"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Patchwork

## 1. BLUF / Executive Summary
Patchwork (MITRE ATT&CK **G0040**) is a cyber espionage threat group first observed publicly in **December 2015**. MITRE assesses attribution as **unconfirmed**, with circumstantial indicators suggesting possible pro-Indian/India-linked interests. Public reporting describes persistent targeting of **diplomatic and government-related** entities, with documented activity spanning **South Asia** and (in 2018) spearphishing campaigns targeting **U.S. think tanks**. Operations commonly leverage **spearphishing**, **watering holes**, and **malicious document exploitation**, alongside a mix of custom malware and repurposed tooling, including [[30_CIPHER/05_Malware/BADNEWS]], [[30_CIPHER/05_Malware/BackConfig]], [[30_CIPHER/05_Malware/AutoIt backdoor]], and [[30_CIPHER/05_Malware/NDiskMonitor]].

## 2. Attribution Notes
- **Definitive sponsor attribution is not public.** MITRE notes Patchwork has not been definitively attributed, while indicating circumstantial evidence consistent with pro-Indian/India-linked interests.
- Patchwork is associated in public nomenclature with several overlapping labels/campaign framings (e.g., **Dropping Elephant**, **MONSOON**, **Operation Hangover**). Treat these as **tracking-name overlaps** unless a given source explicitly equates them.

## 3. Motivations & Objectives
- **Espionage-driven collection** against targets relevant to diplomacy, government policy, and strategic affairs.
- **Stealthy access and continuity:** favor delivery chains that blend into normal user workflows (email lures, document opens, browser visits) and enable repeated re-entry.
- **Operational pragmatism:** documented reuse of code from public sources and incorporation of common tools where effective.

## 4. Targeting Profile
- **Primary sectors (reported):** diplomatic entities, government agencies, and organizations adjacent to foreign affairs.
- **Geographic focus (reported):** South Asia; additional, time-bounded reporting of targeting against U.S. think tanks (March–April 2018).
- **Target selection pattern:** campaign themes and lures frequently align to geopolitical and regional security topics.

## 5. Tradecraft Overview
- **Initial access via targeted messaging:** [[Spearphishing Attachment]] and [[Spearphishing Link]] are repeatedly documented, including use of embedded tracking links (web bugs) to identify opened messages.
- **Client-side exploitation:** malicious documents delivering exploits aligned to [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]; multiple CVEs have been referenced in public reporting in connection with Patchwork activity.
- **Living-off-the-land + commodity tooling:** use of scripting and common frameworks, including [[30_CIPHER/05_Malware/PowerSploit]] and references to reverse-shell tooling (e.g., [[30_CIPHER/05_Malware/Meterpreter]]) in MITRE’s group entry context.
- **C2 resilience and concealment:** use of [[Dead drop resolver]] patterns (e.g., hiding encoded C2 locations in comments on legitimate websites) and background transfer mechanisms such as [[BITS-based payload delivery]].
- **Trust subversion:** signed malware has been reported, including self-signed certificates crafted to resemble legitimate vendors.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]
- [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]
- [[20_Entities/07_TTPs/T1119 - Automated Collection]]
- [[20_Entities/07_TTPs/T1197 - BITS Jobs]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]
- [[20_Entities/07_TTPs/T1132.001 - Data Encoding: Standard Encoding]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]
- [[20_Entities/07_TTPs/T1587.002 - Develop Capabilities: Code Signing Certificates]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]
- [[T1680 - Local Storage Discovery]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1112 - Modify Registry]]
- [[20_Entities/07_TTPs/T1027.001 - Obfuscated Files or Information: Binary Padding]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1027.005 - Obfuscated Files or Information: Indicator Removal from Tools]]
- [[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/BADNEWS]] — backdoor associated with Patchwork campaigns; reported to use web content (e.g., RSS/forums/blogs) for C2 and support automated collection and staging behaviors (MITRE S0128; Forcepoint/Trend Micro/Unit 42 reporting lineage).
- [[30_CIPHER/05_Malware/BackConfig]] — custom trojan with a plugin architecture attributed to Patchwork (MITRE S0475; Unit 42).
- [[30_CIPHER/05_Malware/AutoIt backdoor]] — malware associated with the MONSOON campaign framing and used in Patchwork-linked reporting contexts (MITRE S0129; Forcepoint).
- [[30_CIPHER/05_Malware/NDiskMonitor]] — custom .NET backdoor described as unique to Patchwork in public reporting (MITRE S0272; Trend Micro).
- [[30_CIPHER/05_Malware/PowerSploit]] — open-source PowerShell offensive framework referenced in Patchwork tradecraft (MITRE G0040 and S0194 context).
- [[30_CIPHER/05_Malware/QuasarRAT]] — open-source RAT referenced by MITRE as an example of Patchwork obtaining and using open-source tooling (MITRE G0040).
- [[30_CIPHER/05_Malware/Meterpreter]] — referenced in MITRE’s Patchwork entry in the context of reverse-shell activity.

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] and [[Spearphishing Link]] delivery, including [[Tracking pixels / web bugs]] to measure engagement and prioritize follow-up.
- [[Watering hole delivery]] used to seed exploit-bearing content for initial victims (documented in MITRE’s group entry references).
- [[Dead drop resolver]] approach for C2 indirection and resilience, including encoded/obfuscated pointers on legitimate websites.
- [[BITS-based payload delivery]] to download additional stages with reduced user friction and potentially lower visibility.
- [[Self-signed code-signing]] and signed malware patterns (including spoofed vendor identities) to influence trust decisions.
- [[DLL side-loading]] and other hijack-execution-flow methods to load payloads under legitimate signed binaries.

## 9. Campaign History
- **2015-12 (first observed):** MITRE records Patchwork as first observed in December 2015 and links early activity to diplomatic/government-related targeting.
- **2016 (MONSOON reporting window):** Forcepoint documents an ongoing espionage campaign (MONSOON) tracked since May 2016, described as starting in December 2015 and still active as of mid-2016; MITRE associates MONSOON/Operation Hangover naming with Patchwork tracking.
- **2017-12:** Trend Micro publishes analysis highlighting Patchwork’s continued evolution and reliance on a mix of custom malware and repurposed/off-the-shelf components.
- **2018-03 to 2018-04:** Volexity reports multiple spearphishing campaigns attributed to Patchwork targeting U.S. think tanks.
- **2018-03-07:** Unit 42 reports Patchwork continuing to deliver updated [[30_CIPHER/05_Malware/BADNEWS]] payloads against targets in the Indian subcontinent and documents additional tradecraft patterns (e.g., weaponized documents and background delivery behaviors).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize defenses against **targeted phishing** and **document-based intrusion chains**, especially for high-risk user populations (policy, foreign affairs, executive, and research roles).
- Emphasize detection for **script execution** and **signed-but-untrusted binaries**, including anomalous signing patterns and certificate provenance concerns aligned to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]].
- Build visibility for **background transfer and staged payload delivery** behaviors consistent with [[20_Entities/07_TTPs/T1197 - BITS Jobs]] and [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- Monitor for **C2 indirection** and web-service dead-drop behaviors aligned to [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]], especially where legitimate web properties are used as pointers.
- Maintain strong hygiene for **client-side exploit exposure** (rapid patching, hardening of Office execution paths, and layered endpoint protections) given repeated public reporting of exploitation-driven delivery.

## 12. Analyst Notes
- Attribution remains **circumstantial** in public sources; keep analytic language conservative and distinguish “suspected” from “confirmed.”
- Patchwork is frequently characterized by **code reuse** and **repurposed tools**, which can increase false-positive overlap with unrelated activity; prefer multi-factor correlation (victimology + infrastructure + malware lineage) over single-artifact matches.
- The MONSOON / Operation Hangover naming is commonly used across sources; treat these as **tracking conventions** unless a source explicitly equates the actor sets.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Patchwork (G0040): https://attack.mitre.org/groups/G0040/
- Forcepoint — MONSOON: Analysis of an APT Campaign (PDF): https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf
- Trend Micro — Untangling the Patchwork Cyberespionage Group (PDF): https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf
- Unit 42 — Patchwork Continues to Deliver BADNEWS: https://unit42.paloaltonetworks.com/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/
- Volexity — Patchwork Targets US Think Tanks: https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/

## 14. References
1. MITRE ATT&CK. “Patchwork (G0040).” (Last Modified 2025-10-21). https://attack.mitre.org/groups/G0040/
2. Forcepoint Security Labs. “MONSOON – Analysis of an APT Campaign.” (2016-08-08) (PDF). https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf
3. Trend Micro. “Untangling the Patchwork Cyberespionage Group.” (2017-12-11) (PDF). https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf
4. Palo Alto Networks Unit 42. “Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent.” (2018-03-07). https://unit42.paloaltonetworks.com/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/
5. Volexity. “Patchwork APT Group Targets US Think Tanks.” (2018-06-07). https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/
6. MITRE ATT&CK. “BADNEWS (S0128).” (Last Modified 2025-04-25). https://attack.mitre.org/software/S0128/
7. MITRE ATT&CK. “BackConfig (S0475).” (Last Modified 2025-04-16). https://attack.mitre.org/software/S0475/
8. MITRE ATT&CK. “AutoIt backdoor (S0129).” (Last Modified 2025-04-25). https://attack.mitre.org/software/S0129/
9. MITRE ATT&CK. “NDiskMonitor (S0272).” (Last Modified 2025-04-25). https://attack.mitre.org/software/S0272/
