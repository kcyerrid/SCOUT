---
entity_type: threat_actor
actor_name: "NEODYMIUM"
common_name: "NEODYMIUM"
actor_id: "G0055"
actor_type: "Microsoft-tracked activity group associated with targeted surveillance/espionage using [[30_CIPHER/05_Malware/Wingbird]] (FinFisher-like) and exploitation of Adobe Flash zero-day CVE-2016-4117 via spearphishing (reported)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2016-05-01"
last_seen: ""
status: "Unknown (public reporting concentrated in 2016)"
motivations: ["Espionage","Surveillance"]
objectives: ["Targeted collection against specific individuals (reported)","Initial compromise via spearphishing attachments delivering embedded exploit content (reported)","Establish persistence and covert access on individual endpoints using [[30_CIPHER/05_Malware/Wingbird]] (reported)"]
victimology_summary: "NEODYMIUM (G0055) is a Microsoft-tracked activity group publicly described in relation to a May 2016 campaign that heavily targeted Turkish victims and other individuals in Europe. Reporting ties NEODYMIUM to the backdoor [[30_CIPHER/05_Malware/Wingbird]], assessed by MITRE as resembling commercial spyware [[30_CIPHER/05_Malware/FinFisher]] (FinFisher/FinSpy lineage). MITRE notes NEODYMIUM shows similarities to [[PROMETHIUM]] based on overlapping victim and campaign characteristics and is reportedly closely associated with [[BlackOasis]] operations, though public evidence does not confirm these names are direct aliases."
target_sectors: []
target_regions: ["Turkey","Europe"]
related_groups: ["PROMETHIUM","BlackOasis"]
malware: ["[[30_CIPHER/05_Malware/Wingbird]]","[[30_CIPHER/05_Malware/FinFisher]]"]
tools: []
infrastructure: ["[[Spearphishing attachment]]","[[Embedded Adobe Flash exploit in Office document]]","[[Exploitation of CVE-2016-4117]]","[[Staged component download]]","[[Service-based persistence]]","[[DLL side-loading]]","[[Process injection]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]","[[20_Entities/07_TTPs/T1547.008 - Boot or Logon Autostart Execution: LSASS Driver]]","[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]","[[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]","[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]","[[20_Entities/07_TTPs/T1055 - Process Injection]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]"]
notable_claims: ["Microsoft observed NEODYMIUM using the Adobe Flash zero-day CVE-2016-4117 in early May 2016 in parallel with PROMETHIUM activity (reported)","MITRE describes [[30_CIPHER/05_Malware/Wingbird]] as appearing to be a version of commercial spyware [[30_CIPHER/05_Malware/FinFisher]] and used by NEODYMIUM (reported)","MITRE notes a close reported association with [[BlackOasis]] operations, but states evidence of direct aliasing is not identified"]
intel_sources: ["MITRE ATT&CK — NEODYMIUM (G0055) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0055/","MITRE ATT&CK — Wingbird (S0176) (Last Modified 2025-04-25): https://attack.mitre.org/software/S0176/","Microsoft Security Blog — Twin zero-day attacks: PROMETHIUM and NEODYMIUM target individuals in Europe (2016-12-14): https://www.microsoft.com/en-us/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/","Microsoft Download Center (PDF) — Microsoft Security Intelligence Report Volume 21 (2016-12-14): https://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_Parallel_Zero-day_Attacks_English.pdf","Microsoft Security Intelligence — Backdoor:Win32/Wingbird.A!dha (Published 2016-12-07; Updated 2017-11-27): https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor%3AWin32%2FWingbird.A%21dha","CyberScoop — Middle Eastern hacking group is using FinFisher malware to conduct international espionage (2017-10-16): https://www.cyberscoop.com/middle-eastern-hacking-group-using-finfisher-malware-conduct-international-espionage/"]
tags: ["threat-actor","neodymium","g0055","targeted-surveillance","cyber-espionage","microsoft-activity-group","wingbird","finfisher"]
created: "2025-12-28"
last_modified: "2025-12-28"
---

# NEODYMIUM

## 1. BLUF / Executive Summary
NEODYMIUM (**G0055**) is a Microsoft-tracked activity group publicly associated with a **May 2016** campaign that **heavily targeted Turkish victims** and other **individuals in Europe**. Open reporting ties the activity to the backdoor [[30_CIPHER/05_Malware/Wingbird]], which MITRE describes as resembling commercial surveillance software [[30_CIPHER/05_Malware/FinFisher]]. Reporting highlights initial access via **spearphishing attachments** delivering an embedded **Adobe Flash zero-day exploit (CVE-2016-4117)** leading to installation of Wingbird on individual endpoints.

## 2. Attribution Notes
- **Attribution basis:** MITRE’s NEODYMIUM (G0055) and Wingbird (S0176) entries, plus Microsoft’s public research describing the May 2016 campaign and toolchain.
- **Sponsor / country attribution:** not established in the cited sources; this note does **not** assign a state sponsor.
- **Related activity:** MITRE notes similarities with [[PROMETHIUM]] and reports NEODYMIUM is closely associated with [[BlackOasis]] operations, while also stating that evidence of direct aliasing is not identified.

## 3. Motivations & Objectives
- **Motivation (reported):** targeted collection and surveillance against individuals (espionage-oriented rather than broad criminal monetization).
- **Objectives (reported):**
  - Compromise specific individuals via tailored delivery.
  - Establish persistent access on endpoints using [[30_CIPHER/05_Malware/Wingbird]].
  - Maintain stealth and operational security through common persistence and injection patterns.

## 4. Targeting Profile
- **Primary geography (reported):** Turkey.
- **Additional geography (reported):** Europe (individual targets outside Turkey noted in Microsoft reporting).
- **Target type (reported):** individuals, with targets described as not necessarily sharing a single common organizational affiliation.

## 5. Tradecraft Overview
- **Initial access:** spearphishing attachments delivering Office documents embedding Flash exploit content aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]].
- **Privilege enablement:** exploitation used to elevate payload execution aligned to [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]] (as described in Wingbird tradecraft).
- **Persistence & execution:** service-based persistence and related mechanisms aligned to [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]], [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]], and autostart execution aligned to [[20_Entities/07_TTPs/T1547.008 - Boot or Logon Autostart Execution: LSASS Driver]].
- **Defense evasion & stealth:** DLL side-loading and process injection aligned to [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]] and [[20_Entities/07_TTPs/T1055 - Process Injection]], plus cleanup aligned to [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]].
- **Discovery:** security software and system information checks aligned to [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]] and [[20_Entities/07_TTPs/T1082 - System Information Discovery]].

## 6. MITRE ATT&CK Mapping
- Delivery / Execution
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
  - [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- Privilege Escalation
  - [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]
- Persistence / Service Abuse
  - [[20_Entities/07_TTPs/T1547.008 - Boot or Logon Autostart Execution: LSASS Driver]]
  - [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
  - [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]
- Defense Evasion / Execution Flow
  - [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]
  - [[20_Entities/07_TTPs/T1055 - Process Injection]]
  - [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- Discovery
  - [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]
  - [[20_Entities/07_TTPs/T1082 - System Information Discovery]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Wingbird]] — backdoor used by NEODYMIUM in the May 2016 campaign (per MITRE/Microsoft).
- [[30_CIPHER/05_Malware/FinFisher]] — commercial spyware family Wingbird is assessed to resemble (per MITRE description).

## 8. Infrastructure Patterns
- [[Spearphishing attachment]] delivery with [[Embedded Adobe Flash exploit in Office document]].
- [[Exploitation of CVE-2016-4117]] as an initial compromise enabler in the May 2016 campaign (reported).
- [[Staged component download]] behavior described at a high level as retrieving additional components prior to full payload deployment (reported).
- Persistence patterns emphasizing [[Service-based persistence]] with [[DLL side-loading]] and [[Process injection]].

## 9. Campaign History
- **2016-05 (reported):** NEODYMIUM campaign observed leveraging the Adobe Flash zero-day **CVE-2016-4117** to install [[30_CIPHER/05_Malware/Wingbird]] on targeted individuals.
- **2016-12-14:** Microsoft publishes public research describing NEODYMIUM and PROMETHIUM’s parallel use of the same Flash zero-day in the same region.
- **2017-11-27 (reported update date):** Microsoft’s malware description for Wingbird is updated, providing additional public characterization of the threat.
- **2018-01-16 / 2025-04-25:** MITRE ATT&CK creation and later modification dates for the NEODYMIUM/Wingbird entries indicate ongoing curation rather than new activity.

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Emphasize controls and detections for spearphishing-delivered exploit documents aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]].
- Monitor for service creation and suspicious service execution aligned to [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]] and [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]] in combination with unusual endpoint behaviors.
- Increase detection coverage for injection and side-loading patterns aligned to [[20_Entities/07_TTPs/T1055 - Process Injection]] and [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]].
- Treat evidence of file self-deletion/cleanup aligned to [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]] as a potential post-compromise signal when correlated with other anomalies.
- Baseline and alert on atypical security product discovery checks aligned to [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]].

## 12. Analyst Notes
- NEODYMIUM is best handled as a **campaign-defined activity group** with limited public visibility beyond the 2016 reporting window; avoid overstating continuity or scope without additional corroboration.
- The reported association with [[BlackOasis]] should be treated as **related/overlapping operations** rather than confirmed aliasing, consistent with MITRE’s caution.
- Because the activity is described as targeting **individual endpoints**, endpoint-focused telemetry and user-centric risk controls are especially relevant.

## 13. Further Reading / External Resources
- MITRE ATT&CK — NEODYMIUM (G0055): https://attack.mitre.org/groups/G0055/
- MITRE ATT&CK — Wingbird (S0176): https://attack.mitre.org/software/S0176/
- Microsoft Security Blog — Twin zero-day attacks (2016-12-14): https://www.microsoft.com/en-us/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/
- Microsoft Security Intelligence Report Volume 21 (PDF): https://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_Parallel_Zero-day_Attacks_English.pdf

## 14. References
1. MITRE ATT&CK. “NEODYMIUM (G0055).” Last Modified 2025-04-25. https://attack.mitre.org/groups/G0055/
2. MITRE ATT&CK. “Wingbird (S0176).” Last Modified 2025-04-25. https://attack.mitre.org/software/S0176/
3. Microsoft Defender Security Research Team. “Twin zero-day attacks: PROMETHIUM and NEODYMIUM target individuals in Europe.” 2016-12-14. https://www.microsoft.com/en-us/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/
4. Anthe, C. et al. Microsoft. “Microsoft Security Intelligence Report Volume 21: Parallel Zero-day Attacks.” 2016-12-14 (PDF). https://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_Parallel_Zero-day_Attacks_English.pdf
5. Microsoft Security Intelligence. “Backdoor:Win32/Wingbird.A!dha threat description.” Published 2016-12-07; Updated 2017-11-27. https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor%3AWin32%2FWingbird.A%21dha
6. Bing, Chris. CyberScoop. “Middle Eastern hacking group is using FinFisher malware to conduct international espionage.” 2017-10-16. https://www.cyberscoop.com/middle-eastern-hacking-group-using-finfisher-malware-conduct-international-espionage/
