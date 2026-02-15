---
entity_type: threat_actor
actor_name: "Velvet Chollima"
common_name: "Kimsuky"
actor_id: "G0094"
actor_type: "North Korea-based cyber espionage threat group (often vendor-tracked as Velvet Chollima) focused on Korean Peninsula foreign policy, national security, nuclear policy, and sanctions-related intelligence (reported)"
aliases: ["Kimsuky","Black Banshee","Emerald Sleet","THALLIUM","APT43","TA427","Springtail"]
country_of_origin: "North Korea"
suspected_sponsors: ["North Korean government"]
attribution_confidence: "High"
first_seen: "2012-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Strategic intelligence collection aligned to DPRK foreign policy and national security priorities (reported)","Credential harvesting and email account compromise to enable follow-on access and spearphishing (reported)","Long-term access to government, policy, research, and related organizations for sustained collection (reported)"]
victimology_summary: "Velvet Chollima is a widely used vendor name for activity that MITRE ATT&CK tracks as Kimsuky (G0094), a North Korea-based cyber espionage group active since at least 2012. Public reporting describes initial emphasis on South Korean government agencies, think tanks, and subject-matter experts, with later expansion to targets including the United Nations and organizations across government, education, business services, and manufacturing sectors in the United States, Japan, Russia, and Europe."
target_sectors: ["Government","Think tanks","Academia / research","International organizations (e.g., United Nations; reported)","Education","Business services","Manufacturing","Media / journalism (reported)","NGO / policy research (reported)"]
target_regions: ["South Korea","United States","Japan","Russia","Europe"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/AppleSeed]]","[[30_CIPHER/05_Malware/BabyShark]]","[[30_CIPHER/05_Malware/Brave Prince]]","[[30_CIPHER/05_Malware/CSPY Downloader]]","[[30_CIPHER/05_Malware/GoBear]]","[[30_CIPHER/05_Malware/Amadey]]","[[30_CIPHER/05_Malware/TRANSLATEXT]]"]
tools: ["[[30_CIPHER/05_Malware/PHProxy]]","[[30_CIPHER/05_Malware/QuickZip]]","[[30_CIPHER/05_Malware/GREASE]]","[[30_CIPHER/05_Malware/Dropbox]]","[[30_CIPHER/05_Malware/Blogspot]]","[[30_CIPHER/05_Malware/GitHub]]"]
infrastructure: ["[[Look-alike domains]]","[[Domain spoofing]]","[[Compromised legitimate websites]]","[[Malicious browser extension]]","[[Dead drop resolver]]","[[Third-party web services for C2]]","[[Cloud storage staging]]","[[Fast flux DNS]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]","[[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]","[[20_Entities/07_TTPs/T1098.007 - Account Manipulation: Additional Local or Domain Groups]]","[[20_Entities/07_TTPs/T1078.003 - Valid Accounts: Local Accounts]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1185 - Browser Session Hijacking]]","[[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]","[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]","[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]","[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]","[[20_Entities/07_TTPs/T1119 - Automated Collection]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Kimsuky (G0094) (Last Modified 2025-11-12): https://attack.mitre.org/groups/G0094/","CISA — North Korean Advanced Persistent Threat Focus: Kimsuky (AA20-301A) (2020-10-27): https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a","CISA (PDF) — TLP-WHITE_AA20-301A_North_Korean_APT_Focus_Kimsuky (2020-10-27): https://www.cisa.gov/sites/default/files/publications/TLP-WHITE_AA20-301A_North_Korean_APT_Focus_Kimsuky.pdf","Microsoft Learn — How Microsoft names threat actors (Updated 2025-11-07): https://learn.microsoft.com/en-us/unified-secops/microsoft-threat-actor-naming","CrowdStrike — VELVET CHOLLIMA adversary profile (access-limited): https://www.crowdstrike.com/adversaries/velvet-chollima/","Cybereason Nocturnus — Back to the Future: Inside the Kimsuky KGH Spyware Suite: https://www.cybereason.com/blog/research/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite","NETSCOUT ASERT — STOLEN PENCIL Campaign Targets Academia (2018-12-05): https://www.netscout.com/blog/asert/stolen-pencil-campaign-targets-academia","Broadcom/Symantec Threat Hunter Team — Springtail: New Linux Backdoor Added to Toolkit (2024-05-16): https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage","Mandiant (Google Cloud) — APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations (2023-03-28): https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage"]
tags: ["threat-actor","velvet-chollima","kimsuky","g0094","dprk-nexus","cyber-espionage","phishing","credential-harvesting"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Velvet Chollima

## 1. BLUF / Executive Summary
Velvet Chollima is a commonly used name for activity that MITRE ATT&CK tracks as **Kimsuky (G0094)**, a **North Korea-based** cyber espionage actor active since at least **2012**. Public reporting characterizes the group as a persistent collector focused on Korean Peninsula foreign policy and national security topics, using **credential harvesting, spearphishing, and modular malware/tooling** with resilient use of **third-party services** for staging and command-and-control.

## 2. Attribution Notes
- In open reporting, “Velvet Chollima” is an **alias label** used by some vendors; MITRE consolidates this activity under **Kimsuky (G0094)** and lists Velvet Chollima as an associated name.
- Microsoft’s naming guidance associates **Emerald Sleet** with older names including **THALLIUM** and **VELVET CHOLLIMA**, reflecting vendor taxonomy rather than separate organizations.
- Public reporting also uses **APT43** for overlapping/related activity sets; treat these as **tracking labels** that may not perfectly align across sources.

## 3. Motivations & Objectives
- **Espionage**: intelligence collection aligned to DPRK strategic interests (policy, sanctions, nuclear issues, Korea-related national security topics).
- **Operational objectives**: compromise email accounts and credentials to enable follow-on spearphishing, internal access, and long-term collection from policy and research ecosystems.

## 4. Targeting Profile
- **Primary focus (reported):** South Korean government agencies, think tanks, and subject-matter experts.
- **Expanded targeting (reported):** international organizations (including the UN), plus government, education, business services, and manufacturing organizations in the U.S., Japan, Russia, and Europe.
- **Persona-heavy targeting:** victims often include individuals whose access or expertise can be leveraged for broader collection.

## 5. Tradecraft Overview
- **Spearphishing and social engineering** are recurring access vectors, often paired with account compromise to improve credibility and reach ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]).
- **Script-centric execution** using PowerShell, Windows command shell, and VBScript is documented in ATT&CK mapping and public advisories ([[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]).
- **Credential and browser data theft** is a notable theme, including ATT&CK-mapped browser session hijacking behavior ([[20_Entities/07_TTPs/T1185 - Browser Session Hijacking]]).
- **Resilient C2 and staging** via web protocols, mail protocols, and third-party web services (including dead-drop patterns) appear repeatedly in reporting ([[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]).
- **Operational packaging** such as archiving prior to exfiltration and obfuscation/encoding is common in mapped techniques ([[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]; [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]).

## 6. MITRE ATT&CK Mapping
- Initial Access / Execution
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
  - [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
  - [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- Resource Development / Infrastructure
  - [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
  - [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]
  - [[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]
- Persistence / Privilege / Account Operations
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
  - [[20_Entities/07_TTPs/T1098.007 - Account Manipulation: Additional Local or Domain Groups]]
  - [[20_Entities/07_TTPs/T1078.003 - Valid Accounts: Local Accounts]]
  - [[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]
- Command and Control
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]
  - [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]
  - [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]
- Collection / Exfiltration
  - [[20_Entities/07_TTPs/T1185 - Browser Session Hijacking]]
  - [[20_Entities/07_TTPs/T1119 - Automated Collection]]
  - [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
  - [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- Execution
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
  - [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]

## 7. Malware & Tools Used
- Actor-associated malware families and loaders documented in MITRE ATT&CK (representative):
  - [[30_CIPHER/05_Malware/AppleSeed]]
  - [[30_CIPHER/05_Malware/BabyShark]]
  - [[30_CIPHER/05_Malware/Brave Prince]]
  - [[30_CIPHER/05_Malware/CSPY Downloader]]
  - [[30_CIPHER/05_Malware/GoBear]]
  - [[30_CIPHER/05_Malware/TRANSLATEXT]]
- Commodity/adjacent malware observed in Kimsuky operations per MITRE mapping:
  - [[30_CIPHER/05_Malware/Amadey]]
- Tools/utility concepts referenced in ATT&CK mapping and major public reporting (representative):
  - [[30_CIPHER/05_Malware/PHProxy]] (used in modified form in reported activity)
  - [[30_CIPHER/05_Malware/QuickZip]] (archiving utility referenced in ATT&CK technique notes)
  - [[30_CIPHER/05_Malware/GREASE]] (tool name referenced in ATT&CK technique notes)
  - [[30_CIPHER/05_Malware/Dropbox]]
  - [[30_CIPHER/05_Malware/Blogspot]]
  - [[30_CIPHER/05_Malware/GitHub]]

## 8. Infrastructure Patterns
- [[Look-alike domains]] and [[Domain spoofing]] for lure credibility and credential capture.
- [[Third-party web services for C2]] including blogging platforms and code repositories, aligned to ATT&CK-mapped web service usage.
- [[Cloud storage staging]] for payload hosting and/or data transfer (reported).
- [[Dead drop resolver]] patterns where public web content is used to retrieve configuration or tasking.
- [[Malicious browser extension]] use has been described in public reporting for specific campaigns (e.g., STOLEN PENCIL).
- [[Fast flux DNS]] / dynamic resolution behaviors appear in ATT&CK technique mapping.

## 9. Campaign History
- **2012+** — MITRE reports Kimsuky activity since at least 2012, initially focused on South Korea-based targets and later expanding internationally.
- **2014** — Public reporting (as summarized by MITRE) assesses the group was responsible for the Korea Hydro & Nuclear Power Co. compromise.
- **2018** — **Operation STOLEN PENCIL** described in public reporting and referenced by MITRE; associated reporting highlights browser-extension-based infection themes.
- **2019** — MITRE references **Operation Kabar Cobra** and **Operation Smoke Screen** as notable campaigns.
- **2023–2025** — Public reporting highlights continued evolution, including broader toolsets and infrastructure patterns; MITRE also notes observed use of commercial LLMs in 2023 for activities such as scripting and reconnaissance (as a reporting note, not a standalone signature).

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Prioritize controls against spearphishing, credential theft, and account takeover aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]].
- Increase monitoring for abnormal scripting activity and LOLBin-style execution aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]] and related interpreter techniques.
- Improve visibility for browser/session credential exposure aligned to [[20_Entities/07_TTPs/T1185 - Browser Session Hijacking]] and downstream exfiltration patterns.
- Treat third-party platforms used for command-and-control or staging as investigative pivots aligned to [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]] and [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]].
- Harden and monitor for persistence via registry autoruns consistent with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]].

## 12. Analyst Notes
- “Velvet Chollima” should be treated as an **alias** for the **G0094** cluster in most analytic contexts; when correlating vendor reports, validate whether the scope aligns to Kimsuky/THALLIUM/Em​erald Sleet/APT43 labeling.
- Reported overlaps with other DPRK clusters are frequently described as potential ad hoc collaboration or resource sharing; avoid assuming a single monolithic organization.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Kimsuky (G0094): https://attack.mitre.org/groups/G0094/
- CISA Advisory — AA20-301A (Kimsuky): https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a
- Microsoft Learn — Threat actor naming: https://learn.microsoft.com/en-us/unified-secops/microsoft-threat-actor-naming
- NETSCOUT ASERT — STOLEN PENCIL: https://www.netscout.com/blog/asert/stolen-pencil-campaign-targets-academia
- Broadcom/Symantec — Springtail (Kimsuky-linked): https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage
- Mandiant — APT43 report landing page: https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage

## 14. References
1. MITRE ATT&CK. “Kimsuky (G0094).” Last Modified 2025-11-12. https://attack.mitre.org/groups/G0094/
2. Cybersecurity and Infrastructure Security Agency (CISA). “North Korean Advanced Persistent Threat Focus: Kimsuky (AA20-301A).” 2020-10-27. https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a
3. CISA (PDF). “TLP-WHITE_AA20-301A_North_Korean_APT_Focus_Kimsuky.” 2020-10-27. https://www.cisa.gov/sites/default/files/publications/TLP-WHITE_AA20-301A_North_Korean_APT_Focus_Kimsuky.pdf
4. Microsoft Learn. “How Microsoft names threat actors.” Updated 2025-11-07. https://learn.microsoft.com/en-us/unified-secops/microsoft-threat-actor-naming
5. NETSCOUT ASERT. “STOLEN PENCIL Campaign Targets Academia.” 2018-12-05. https://www.netscout.com/blog/asert/stolen-pencil-campaign-targets-academia
6. Broadcom/Symantec Threat Hunter Team. “Springtail: New Linux Backdoor Added to Toolkit.” 2024-05-16. https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage
7. Cybereason Nocturnus. “Back to the Future: Inside the Kimsuky KGH Spyware Suite.” https://www.cybereason.com/blog/research/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite
8. CrowdStrike. “VELVET CHOLLIMA.” https://www.crowdstrike.com/adversaries/velvet-chollima/
9. Mandiant (Google Cloud). “APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations.” 2023-03-28. https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage
