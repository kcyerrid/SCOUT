---
entity_type: threat_actor
actor_name: "Naikon"
common_name: "Naikon"
actor_id: "G0019"
actor_type: "State-linked cyber espionage (attributed in public reporting)"
aliases: ["Lotus Panda", "Hellsing", "ITG06"]
country_of_origin: "China (attributed in public reporting)"
suspected_sponsors: ["People’s Liberation Army (PLA) Unit 78020 (attributed in public reporting)"]
attribution_confidence: "Medium"
first_seen: "2010-01"
last_seen: ""
status: "Active (reported historically; recent activity reported 2019–2021)"
motivations: ["Espionage", "Information theft"]
objectives: ["Geopolitical and strategic intelligence collection across Southeast Asia/APAC", "Long-term access into government and related organizations", "Collection of sensitive documents and credentials from targeted networks"]
victimology_summary: "Naikon (MITRE ATT&CK G0019) is assessed in public reporting as a state-sponsored cyber espionage group attributed to PLA Unit 78020. Reporting describes operations since at least 2010 primarily against government, military, and civil organizations in Southeast Asia, and against international bodies such as UNDP and ASEAN. Technical reporting also describes activity from 2019–2021 using newer backdoors (e.g., Aria-body, Nebulae, RainyDay) and delivery chains involving spearphishing, exploit builder tooling (RoyalRoad), and DLL search order hijacking/side-loading."
target_sectors: ["Government", "Military", "Civil organizations", "International organizations"]
target_regions: ["Southeast Asia", "Asia-Pacific (APAC)"]
related_groups: ["APT30 (shares characteristics; not an exact match)"]
malware: ["[[30_CIPHER/05_Malware/Aria-body]]", "[[30_CIPHER/05_Malware/Nebulae]]", "[[30_CIPHER/05_Malware/RainyDay]]", "[[30_CIPHER/05_Malware/RARSTONE]]", "[[30_CIPHER/05_Malware/SslMM]]", "[[30_CIPHER/05_Malware/Sys10]]", "[[30_CIPHER/05_Malware/WinMM]]", "[[30_CIPHER/05_Malware/HDoor]]"]
tools: ["[[30_CIPHER/05_Malware/RoyalRoad]]", "[[30_CIPHER/05_Malware/PsExec]]", "[[30_CIPHER/05_Malware/netsh]]", "[[30_CIPHER/05_Malware/Net]]", "[[30_CIPHER/05_Malware/Ping]]", "[[30_CIPHER/05_Malware/ftp]]", "[[30_CIPHER/05_Malware/Tasklist]]", "[[30_CIPHER/05_Malware/Systeminfo]]", "[[30_CIPHER/05_Malware/schtasks]]", "[[30_CIPHER/05_Malware/WMIC]]", "[[30_CIPHER/05_Malware/LadonGo]]"]
infrastructure: ["[[Spearphishing Attachment]]", "[[Decoy Documents]]", "[[RoyalRoad Exploit Builder]]", "[[Word Startup Add-ins]]", "[[DLL Search Order Hijacking]]", "[[C2 over HTTP]]", "[[Encrypted Channel]]", "[[Domain Generation Algorithms]]", "[[Proxy Infrastructure]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]", "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]", "[[20_Entities/07_TTPs/T1137.006 - Office Application Startup: Add-ins]]", "[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]", "[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]", "[[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]", "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]", "[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]", "[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]", "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]", "[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]", "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]", "[[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]", "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0019): Naikon (Last modified 2025-04-25)","Bitdefender (2021-04-23): NAIKON – Traces from a Military Cyber-Espionage Operation (PDF)","Bitdefender Labs (2021-04-28): New Nebulae Backdoor Linked with the NAIKON Group","Check Point Research (2020-05-07): Naikon APT: Cyber Espionage Reloaded","Kaspersky Securelist (2015-05-14): The Naikon APT","ThreatConnect (2015-07): Project CameraShy / Naikon (Unit 78020 attribution)"]
tags: ["threat-actor", "apt", "cyber-espionage", "china", "naikon", "lotus-panda", "hellsing", "mitre-g0019"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Naikon

## 1. BLUF / Executive Summary
Naikon (MITRE ATT&CK **G0019**) is a state-linked cyber espionage actor attributed in public reporting to **PLA Unit 78020**, with activity reported since at least **2010** and a longstanding focus on **Southeast Asia/APAC** government and related targets. Public reporting highlights sustained intelligence collection, spearphishing-led access, and a tooling ecosystem that includes multiple custom backdoors (e.g., [[30_CIPHER/05_Malware/Aria-body]], [[30_CIPHER/05_Malware/Nebulae]], [[30_CIPHER/05_Malware/RainyDay]]) and tradecraft such as [[Word Startup Add-ins]] and [[DLL Search Order Hijacking]].

## 2. Attribution Notes
Naikon is assessed by MITRE ATT&CK as state-sponsored and attributed to a PLA technical reconnaissance bureau/unit (**Unit 78020**) based on public reporting. Third-party reporting has attempted to tie Naikon activity to specific organizational structures within that unit; however, open-source attribution remains inherently probabilistic and should be treated conservatively when making policy or legal determinations.

## 3. Motivations & Objectives
Naikon is consistently described as espionage-motivated, prioritizing **geopolitical and strategic intelligence** across Southeast Asia/APAC. Objectives center on sustained access to government and adjacent organizations, enabling long-term collection of sensitive documents and operational information.

## 4. Targeting Profile
Naikon’s victimology is reported as heavily concentrated in **Southeast Asia/APAC**, targeting **government, military, and civil organizations**, with reporting also describing targeting of international bodies such as **ASEAN** and **UNDP**. Target selection patterns appear aligned to geopolitical collection requirements rather than broad opportunistic compromise.

## 5. Tradecraft Overview
Naikon tradecraft is characterized in public reporting by:
- [[Spearphishing Attachment]] delivery and user-driven execution consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- Use of exploit-builder workflows (notably [[RoyalRoad Exploit Builder]]) to place loaders as Word add-ins in startup paths, consistent with [[20_Entities/07_TTPs/T1137.006 - Office Application Startup: Add-ins]].
- Execution flow hijacking/side-loading consistent with [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]].
- Post-compromise discovery and lateral enablement using native and common admin utilities (e.g., WMI, scheduled tasks, discovery commands), consistent with multiple ATT&CK techniques listed by MITRE for this group.
- Defense evasion via masquerading of tasks/services and filenames/locations, consistent with [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]] and [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1137.006 - Office Application Startup: Add-ins]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]

## 7. Malware & Tools Used
**Malware / backdoors (MITRE- and vendor-reported)**
- [[30_CIPHER/05_Malware/Aria-body]]
- [[30_CIPHER/05_Malware/Nebulae]]
- [[30_CIPHER/05_Malware/RainyDay]]
- [[30_CIPHER/05_Malware/RARSTONE]]
- [[30_CIPHER/05_Malware/SslMM]]
- [[30_CIPHER/05_Malware/Sys10]]
- [[30_CIPHER/05_Malware/WinMM]]
- [[30_CIPHER/05_Malware/HDoor]]

**Tools / utilities (MITRE- and vendor-reported)**
- [[30_CIPHER/05_Malware/RoyalRoad]]
- [[30_CIPHER/05_Malware/LadonGo]]
- [[30_CIPHER/05_Malware/PsExec]]
- [[30_CIPHER/05_Malware/netsh]]
- [[30_CIPHER/05_Malware/Net]]
- [[30_CIPHER/05_Malware/Ping]]
- [[30_CIPHER/05_Malware/ftp]]
- [[30_CIPHER/05_Malware/Tasklist]]
- [[30_CIPHER/05_Malware/Systeminfo]]
- [[30_CIPHER/05_Malware/schtasks]]
- [[30_CIPHER/05_Malware/WMIC]]

## 8. Infrastructure Patterns
- Reliance on [[Spearphishing Attachment]] with [[Decoy Documents]] aligned to target-country context.
- Delivery chains featuring [[RoyalRoad Exploit Builder]] and persistence via [[Word Startup Add-ins]].
- Execution via [[DLL Search Order Hijacking]] / side-loading in abused legitimate applications.
- C2 patterns reported using [[C2 over HTTP]] and encrypted communications, with some tooling described as supporting [[Domain Generation Algorithms]] and [[Proxy Infrastructure]].

## 9. Campaign History
- **2010–2015 (reported):** Long-running activity against Southeast Asian government and civil/military organizations documented in major public reporting, including South China Sea–focused victimology.
- **2015-07 (public research):** Public research projects described Naikon infrastructure and linked the activity to PLA Unit 78020 (attribution claim; corroborated by other public summaries but still an OSINT judgment).
- **2019–2021 (reported):** Vendor reporting described renewed/continued espionage activity against Asian military/government targets, including use of [[30_CIPHER/05_Malware/Aria-body]] loaders and newer backdoors such as [[30_CIPHER/05_Malware/Nebulae]] and [[30_CIPHER/05_Malware/RainyDay]].
- **2020 (reported):** Additional research described Naikon-attributed operations using RoyalRoad-based delivery and add-in placement, indicating ongoing evolution rather than a static toolchain.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize controls and detections aligned to spearphishing-delivered intrusions (especially attachment-led delivery) consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]].
- Strengthen monitoring for Office startup persistence and suspicious add-in placement consistent with [[20_Entities/07_TTPs/T1137.006 - Office Application Startup: Add-ins]].
- Increase visibility for DLL search order hijacking/side-loading patterns consistent with [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]] when correlated with abnormal process lineage and unsigned/unexpected DLL loads.
- Monitor for high-signal combinations of discovery + lateral enablement behaviors (e.g., WMI, scheduled tasks, remote discovery) consistent with the ATT&CK mappings documented for Naikon.
- Treat masquerading of services/tasks and legitimate-name imitation as a correlation amplifier rather than a standalone indicator, consistent with [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]] and [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]].

## 12. Analyst Notes
- Naikon is sometimes cross-referenced with the label “Lotus Panda” and described as sharing characteristics with APT30; sources emphasize these are **not exact matches**, so entity resolution should retain uncertainty.
- Some tradecraft elements in this note are derived from ATT&CK technique citations and vendor reverse-engineering; treat them as “reported/observed in specific operations,” not universal invariants across all Naikon activity.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Naikon (G0019): https://attack.mitre.org/groups/G0019/
- Kaspersky Securelist — The Naikon APT (2015-05-14): https://securelist.com/the-naikon-apt/69953/
- Check Point Research — Naikon APT: Cyber Espionage Reloaded (2020-05-07): https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/
- Bitdefender (PDF) — NAIKON: Traces from a Military Cyber-Espionage Operation (2021-04-23): https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf
- Bitdefender Labs — New Nebulae Backdoor Linked with the NAIKON Group (2021-04-28): https://www.bitdefender.com/en-us/blog/labs/new-nebulae-backdoor-linked-with-the-naikon-group
- ThreatConnect — Project CameraShy (Naikon / Unit 78020) landing page (2015): https://threatconnect.com/resource/project-camerashy-closing-the-aperture-on-chinas-unit-78020/

## 14. References
- MITRE ATT&CK. “Naikon (G0019).” (Last modified 2025-04-25). https://attack.mitre.org/groups/G0019/
- Kaspersky Securelist. “The Naikon APT.” (2015-05-14). https://securelist.com/the-naikon-apt/69953/
- Check Point Research. “Naikon APT: Cyber Espionage Reloaded.” (2020-05-07). https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/
- Bitdefender. “NAIKON – Traces from a Military Cyber-Espionage Operation.” (2021-04-23, PDF). https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf
- Bitdefender Labs. “New Nebulae Backdoor Linked with the NAIKON Group.” (2021-04-28). https://www.bitdefender.com/en-us/blog/labs/new-nebulae-backdoor-linked-with-the-naikon-group
- ThreatConnect. “Project CameraShy: Closing the Aperture on China’s Unit 78020.” (2015). https://threatconnect.com/resource/project-camerashy-closing-the-aperture-on-chinas-unit-78020/
