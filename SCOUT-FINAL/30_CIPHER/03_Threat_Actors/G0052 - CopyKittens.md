---
entity_type: threat_actor
actor_name: "CopyKittens"
common_name: "CopyKittens"
actor_id: "G0052"
actor_type: "Iranian cyber espionage threat group (reported)"
aliases: ["Slayer Kitten","DEV-0588"]
country_of_origin: "Iran"
suspected_sponsors: []
attribution_confidence: "High"
first_seen: "2013-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Foreign intelligence collection against strategic targets (reported)","Long-term access and collection via web compromise, phishing, and custom tooling (reported)","Data collection and exfiltration including via DNS-based channels (reported)"]
victimology_summary: "CopyKittens (MITRE ATT&CK G0052) is an Iran-linked cyber espionage group reported active since at least 2013. Reporting describes targeting across Israel, Saudi Arabia, Turkey, the United States, Jordan, and Germany, including government and foreign affairs entities, academia, defense-related organizations and contractors, municipal authorities, large IT companies, and (at times) United Nations employees. Public reporting highlights the 2017 campaign Operation Wilted Tulip, which documented watering-hole activity, malicious document delivery, and multiple self-developed tools alongside widely available offensive frameworks."
target_sectors: ["Government (including foreign affairs; reported)","Academia / research (reported)","Defense companies and subcontractors (reported)","Municipal authorities (reported)","Information technology companies (reported)","Media / news websites (compromised as watering holes; reported)","International organizations (e.g., UN employees; reported)"]
target_regions: ["Israel","Saudi Arabia","Turkey","United States","Jordan","Germany"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Matryoshka]]","[[30_CIPHER/05_Malware/TDTESS]]"]
tools: ["[[30_CIPHER/05_Malware/Vminst]]","[[30_CIPHER/05_Malware/NetSrv]]","[[30_CIPHER/05_Malware/ZPP]]","[[30_CIPHER/05_Malware/Cobalt Strike]]","[[30_CIPHER/05_Malware/Empire]]","[[30_CIPHER/05_Malware/Metasploit]]","[[30_CIPHER/05_Malware/Mimikatz]]","[[30_CIPHER/05_Malware/BeEF]]","[[30_CIPHER/05_Malware/sqlmap]]","[[30_CIPHER/05_Malware/Acunetix]]","[[30_CIPHER/05_Malware/Havij]]","[[30_CIPHER/05_Malware/AirVPN]]"]
infrastructure: ["[[Watering hole]]","[[Compromised legitimate websites]]","[[Malicious JavaScript injection]]","[[Spoofed domains]]","[[DNS-based C2]]","[[DNS-based data exfiltration]]","[[Stolen code-signing certificate]]","[[Commercial VPN service]]","[[Offshore hosting]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]","[[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1090 - Proxy]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]","[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]","[[20_Entities/07_TTPs/T1560.003 - Archive Collected Data: Archive via Custom Method]]","[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]"]
notable_claims: ["Operation Wilted Tulip reporting describes a mixed toolset of self-developed implants and widely available frameworks (reported)","Reporting describes DNS being used for command-and-control and (in some cases) data exfiltration (reported)"]
intel_sources: ["MITRE ATT&CK — CopyKittens (G0052) (Last Modified 2024-11-17): https://attack.mitre.org/groups/G0052/","ClearSky & Trend Micro (PDF) — Operation Wilted Tulip: Exposing a cyber espionage apparatus (2017-07): https://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf","ClearSky — Report: The CopyKittens are targeting Israelis (2015-11-23): https://www.clearskysec.com/report-the-copykittens-are-targeting-israelis/","Microsoft Security Blog — Exposing POLONIUM activity and infrastructure (mentions AirVPN overlap and tracks CopyKittens as DEV-0588) (2022-06-02): https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/","SecurityWeek — Iranian ‘CopyKittens’ Conduct Foreign Espionage (2017-07-25): https://www.securityweek.com/iranian-copykittens-conduct-foreign-espionage/"]
tags: ["threat-actor","copykittens","g0052","iran-nexus","cyber-espionage","watering-hole","dns-c2"]
created: "2025-12-28"
last_modified: "2025-12-28"
---

# CopyKittens

## 1. BLUF / Executive Summary
CopyKittens (**G0052**) is an Iran-linked cyber espionage group reported active since at least **2013**, associated with **Operation Wilted Tulip** and a broader set of campaigns targeting strategic organizations across the Middle East and select Western countries. Public reporting emphasizes **watering-hole activity**, **spearphishing with malicious documents/links**, and a toolchain blending **self-developed malware** (e.g., [[30_CIPHER/05_Malware/TDTESS]], [[30_CIPHER/05_Malware/Matryoshka]]) with widely available offensive tooling (e.g., [[30_CIPHER/05_Malware/Cobalt Strike]], [[30_CIPHER/05_Malware/Metasploit]], [[30_CIPHER/05_Malware/Empire]]).

## 2. Attribution Notes
- MITRE ATT&CK tracks CopyKittens as **G0052** and describes it as an Iranian cyber espionage group, citing ClearSky/Trend Micro reporting and earlier research.
- Some vendors and datasets refer to CopyKittens as **“Slayer Kitten”**; Microsoft has tracked related observations under **DEV-0588** in at least one public write-up (naming differences reflect taxonomy, not necessarily distinct organizations).
- Sponsorship is not conclusively established in the cited sources; the profile is treated as **Iran-linked / state-aligned** based on victimology and tradecraft characterization in reporting.

## 3. Motivations & Objectives
- **Motivation:** espionage / intelligence collection.
- **Objectives (reported):**
  - Collect sensitive information from diplomatic, policy, defense-adjacent, and research targets.
  - Maintain access and scale collection through compromised web infrastructure and repeated phishing waves.
  - Use DNS-mediated communications in support of command-and-control and, in some cases, exfiltration.

## 4. Targeting Profile
- **Geographies (reported):** Israel, Saudi Arabia, Turkey, United States, Jordan, Germany.
- **Sectors (reported):** foreign affairs and government organizations, academia, defense companies/contractors, municipal authorities, large IT companies, and UN-affiliated individuals.
- **Enabling targets (reported):** media/news and general websites were compromised and weaponized as **watering holes** to reach downstream victims.

## 5. Tradecraft Overview
- **Watering-hole delivery** via injected JavaScript on compromised strategic websites ([[Watering hole]]; [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]).
- **Phishing-based delivery** using both malicious attachments and links; earlier reporting describes document-based lures with user prompts/macros and embedded executables ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]).
- **Client exploitation** in document workflows reported in Operation Wilted Tulip (e.g., Office exploitation themes) ([[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]).
- **Post-exploitation and operator tradecraft** includes PowerShell-centric operations and hiding PowerShell windows ([[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]; [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]).
- **Living-off-the-land / proxy execution** patterns reported via rundll32-based loading of tooling (including lateral movement tooling and commercial frameworks) ([[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]).
- **Credential and access enablement** is supported by reporting of tools like [[30_CIPHER/05_Malware/Mimikatz]] and web exploitation tooling in support of infrastructure compromise.
- **Data handling** includes archival/compression utilities (including a custom compressor described as ZPP) and reported encryption/packing prior to transfer ([[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]; [[20_Entities/07_TTPs/T1560.003 - Archive Collected Data: Archive via Custom Method]]).
- **DNS use** as a notable operational characteristic (C2 and, in some reporting, exfiltration) ([[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]).

## 6. MITRE ATT&CK Mapping
- Initial Access / Delivery
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
  - [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
  - [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- Execution / Scripting
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- Defense Evasion / Tradecraft
  - [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]
  - [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]
  - [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- Command and Control / Infrastructure
  - [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
  - [[20_Entities/07_TTPs/T1090 - Proxy]]
- Resource Development / Tooling
  - [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- Collection / Packaging
  - [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
  - [[20_Entities/07_TTPs/T1560.003 - Archive Collected Data: Archive via Custom Method]]

## 7. Malware & Tools Used
- Custom / actor-associated malware and components (reported):
  - [[30_CIPHER/05_Malware/Matryoshka]] (multi-stage framework described in early reporting)
  - [[30_CIPHER/05_Malware/TDTESS]] (backdoor described in Operation Wilted Tulip)
  - [[30_CIPHER/05_Malware/Vminst]] (lateral movement tooling described in Operation Wilted Tulip)
  - [[30_CIPHER/05_Malware/NetSrv]] (loader described in Operation Wilted Tulip)
  - [[30_CIPHER/05_Malware/ZPP]] (file compression utility described in Operation Wilted Tulip)
- Widely available / third-party tooling referenced in reporting:
  - [[30_CIPHER/05_Malware/Cobalt Strike]]
  - [[30_CIPHER/05_Malware/Empire]]
  - [[30_CIPHER/05_Malware/Metasploit]]
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/BeEF]]
  - [[30_CIPHER/05_Malware/sqlmap]]
  - [[30_CIPHER/05_Malware/Acunetix]]
  - [[30_CIPHER/05_Malware/Havij]]
  - [[30_CIPHER/05_Malware/AirVPN]]

## 8. Infrastructure Patterns
- [[Compromised legitimate websites]] used as [[Watering hole]] delivery points (including news/general sites) with [[Malicious JavaScript injection]].
- [[Spoofed domains]] and attacker-built web properties used for link-based delivery and reconnaissance/fingerprinting themes (reported).
- [[DNS-based C2]] and reported [[DNS-based data exfiltration]] as a notable channel characteristic in multiple write-ups.
- [[Stolen code-signing certificate]] usage reported for signing at least one executable.
- Use of [[Commercial VPN service]] (e.g., [[30_CIPHER/05_Malware/AirVPN]]) cited as an operational choice in public reporting.

## 9. Campaign History
- **2013-01-01 (at least)** — MITRE ATT&CK reports CopyKittens operating since at least 2013.
- **2014-08 (at least)** — Early public reporting describes targeting of Israeli diplomats and academic researchers.
- **2017-01 to 2017-07 (reported)** — Operation Wilted Tulip reporting documents web compromise/watering-hole activity and malicious document delivery, including use of multiple custom tools and commodity frameworks.

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Prioritize defenses against **watering-hole** and web compromise exposure aligned to [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] (web integrity monitoring, rapid remediation of compromised web assets, and browser hardening).
- Reduce document-based attack risk aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]] (macro risk reduction and timely patching of document-handling components).
- Increase detection and response readiness for script-heavy operations aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]] and hidden execution patterns aligned to [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]].
- Monitor for suspicious proxy/VPN usage patterns aligned to [[20_Entities/07_TTPs/T1090 - Proxy]] in combination with other anomaly signals (authentication, endpoint telemetry, and unusual administrative activity).
- Enhance visibility into DNS anomalies aligned to [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]] (unusual query volume, rare domains, and atypical DNS request patterns correlated with endpoint behavior).
- Treat unexpected code-signing trust events as high-signal, aligning review processes to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]].

## 12. Analyst Notes
- CopyKittens reporting frequently emphasizes a **mixed toolset**: bespoke components used alongside widely available offensive tools, which can complicate attribution if analysts over-weight commodity tooling.
- Naming varies across vendors and time (e.g., “Slayer Kitten,” “DEV-0588”); use **G0052** as the stable cross-reference anchor when normalizing data.
- Public reporting is strongest around the 2014–2017 window; lack of recent public detail should be treated as a visibility gap rather than a definitive indication of inactivity.

## 13. Further Reading / External Resources
- MITRE ATT&CK — CopyKittens (G0052): https://attack.mitre.org/groups/G0052/
- ClearSky & Trend Micro (PDF) — Operation Wilted Tulip: https://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf
- ClearSky — The CopyKittens are targeting Israelis (2015): https://www.clearskysec.com/report-the-copykittens-are-targeting-israelis/
- Microsoft Security Blog — POLONIUM report (mentions AirVPN overlap and DEV-0588 label) (2022): https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/
- SecurityWeek — CopyKittens foreign espionage summary (2017): https://www.securityweek.com/iranian-copykittens-conduct-foreign-espionage/

## 14. References
1. MITRE ATT&CK. “CopyKittens (G0052).” Last Modified 2024-11-17. https://attack.mitre.org/groups/G0052/
2. ClearSky Cyber Security & Trend Micro (PDF). “Operation Wilted Tulip: Exposing a cyber espionage apparatus.” 2017-07. https://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf
3. ClearSky Cyber Security. “Report: The CopyKittens are targeting Israelis.” 2015-11-23. https://www.clearskysec.com/report-the-copykittens-are-targeting-israelis/
4. Microsoft Security Blog. “Exposing POLONIUM activity and infrastructure targeting Israeli organizations.” 2022-06-02. https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/
5. SecurityWeek. “Iranian ‘CopyKittens’ Conduct Foreign Espionage.” 2017-07-25. https://www.securityweek.com/iranian-copykittens-conduct-foreign-espionage/
