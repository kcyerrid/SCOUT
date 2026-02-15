---
entity_type: threat_actor
actor_name: "Stealth Falcon"
common_name: "Stealth Falcon"
actor_id: "G0038"
actor_type: "Targeted cyber espionage / spyware operator focused on political and strategic targets; suspected UAE-linked (unconfirmed)"
aliases: ["FruityArmor","Project Raven"]
country_of_origin: "United Arab Emirates (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2012-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Surveillance"]
objectives: ["Conduct targeted surveillance against political and civil society targets","Collect credentials and local data for intelligence value","Maintain stealthy access via encrypted C2 and modular post-compromise tooling","Exploit high-value opportunities (including use of zero-days, reported)"]
victimology_summary: "Stealth Falcon (MITRE ATT&CK G0038) is a threat group reported active since at least 2012, known for targeted spyware operations against Emirati journalists, activists, and dissidents, with broader Middle East–focused espionage activity. Multiple public sources describe overlaps and circumstantial indicators consistent with UAE-aligned interests, but public attribution to a confirmed sponsor remains unproven. Reporting documents evolving toolchains over time, including PowerShell-based implants (Citizen Lab), a Windows backdoor leveraging BITS for C2 (ESET, 2019), the Deadglyph backdoor (ESET, 2023), and a 2025 intrusion chain attributed to Stealth Falcon exploiting CVE-2025-33053 to deliver a custom implant (Check Point Research)."
target_sectors: ["Civil society / human rights","Journalism / media","Government","Defense"]
target_regions: ["United Arab Emirates","Middle East","Turkey","Qatar (reported telemetry)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Win32/StealthFalcon]]","[[30_CIPHER/05_Malware/Deadglyph]]","[[30_CIPHER/05_Malware/Horus Agent]]","[[30_CIPHER/05_Malware/Apollo]]"]
tools: ["[[30_CIPHER/05_Malware/PowerShell]]","[[30_CIPHER/05_Malware/Windows Management Instrumentation]]","[[30_CIPHER/05_Malware/Mythic]]","[[30_CIPHER/05_Malware/Background Intelligent Transfer Service]]","[[30_CIPHER/05_Malware/WebDAV]]"]
infrastructure: ["[[Targeted spearphishing lures]]","[[Macro-enabled document delivery]]","[[Malicious URL shortener / link profiling]]","[[HTTPS C2]]","[[Encrypted C2 channel]]","[[Modular backdoor modules]]","[[WebDAV-hosted payload staging]]","[[BITS-based C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]]","[[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]","[[20_Entities/07_TTPs/T1555.004 - Credentials from Password Stores: Windows Credential Manager]]","[[20_Entities/07_TTPs/T1005 - Data from Local System]]","[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1057 - Process Discovery]]","[[20_Entities/07_TTPs/T1012 - Query Registry]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]","[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]","[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Stealth Falcon (G0038) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0038/","Citizen Lab — Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents (2016-05-29): https://citizenlab.org/2016/05/stealth-falcon/","ESET Research — ESET discovered an undocumented backdoor used by the infamous Stealth Falcon group (2019-09-09): https://www.welivesecurity.com/2019/09/09/backdoor-stealth-falcon-group/","ESET Research — Stealth Falcon preying over Middle Eastern skies with Deadglyph (2023-09-22): https://www.welivesecurity.com/en/eset-research/stealth-falcon-preying-middle-eastern-skies-deadglyph/","Check Point Research — Stealth Falcon’s Exploit of Microsoft Zero Day Vulnerability (CVE-2025-33053) (2025-06-10): https://research.checkpoint.com/2025/stealth-falcon-zero-day/","Reuters Investigates — Project Raven (series hub) (2019-01-30): https://www.reuters.com/investigates/section/usa-raven/"]
tags: ["threat-actor","stealth-falcon","g0038","fruityarmor","project-raven","spyware","middle-east","uae-suspected"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

# Stealth Falcon

## 1. BLUF / Executive Summary
Stealth Falcon (MITRE ATT&CK **G0038**) is a long-running spyware and cyber-espionage operator active since at least **2012**, best known for targeted surveillance against **Emirati journalists, activists, and dissidents** and for broader **Middle East–focused** espionage. Public reporting describes ongoing toolchain evolution across the 2012–2025 period, including PowerShell-centric implant activity documented by Citizen Lab (2016), a Windows backdoor leveraging BITS for stealthy C2 (ESET, 2019), the **Deadglyph** backdoor (ESET, 2023), and a 2025 campaign attributed to Stealth Falcon exploiting **CVE-2025-33053** to deliver a custom implant (**Horus Agent**) built for the **Mythic** framework (Check Point Research, 2025). Circumstantial evidence suggests possible UAE alignment, but public sources generally stop short of confirmed sponsor attribution.

## 2. Attribution Notes
- MITRE describes Stealth Falcon as targeting Emirati dissidents and notes **circumstantial** indicators that may suggest a UAE linkage, while emphasizing the link is **not confirmed**.
- Citizen Lab’s 2016 reporting details the group’s early-to-mid period operations and target set consistent with UAE political context.
- ESET’s 2019 and 2023 reporting attributes specific malware families (**Win32/StealthFalcon**, **Deadglyph**) to Stealth Falcon with high confidence based on technical overlaps and victimology.
- Reuters’ 2019 “Project Raven” reporting is frequently discussed as relevant context for UAE-associated cyber surveillance; overlap assertions remain analytic and should be treated cautiously unless explicitly evidenced per-case.

## 3. Motivations & Objectives
- **Espionage and surveillance:** obtain sensitive communications, documents, and credentials from politically and strategically relevant targets.
- **Access development:** sustain stealthy footholds long enough to stage additional modules and collection tooling.
- **Operational agility:** incorporate advanced tradecraft and, in at least one reported case, leverage a Windows zero-day to increase success against hardened targets.

## 4. Targeting Profile
- **Primary victim profile (reported):** Emirati dissidents, activists, journalists, and associated civil society figures.
- **Secondary victim profile (reported):** government and defense-adjacent entities in the Middle East region; at least one publicly described attempted intrusion targeted a defense organization in Turkey (2025).
- **Geographic emphasis:** UAE and broader Middle East, with spillover or regionally linked targets (e.g., Turkey; Qatar-associated telemetry in ESET’s reporting context).

## 5. Tradecraft Overview
- **Targeted spearphishing and social engineering:** Citizen Lab describes macro-enabled document lures and tailored pretexting against specific individuals.
- **Scripted post-compromise operations:** MITRE highlights PowerShell usage and WMI-backed scripting for execution and data collection ([[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]], [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]], [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]).
- **Credential collection focus:** MITRE documents credential harvesting from password stores including browsers and Windows credential mechanisms ([[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]] and sub-techniques).
- **Encrypted communications:** MITRE notes encrypted C2 traffic and standard web protocol use for C2 ([[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]], [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]).
- **Persistence and discovery:** MITRE documents scheduled task-based persistence and common discovery behaviors (process, system, user/owner, network configuration) consistent with reconnaissance and operational staging.
- **Evolving malware toolchains:** ESET documents distinct backdoor families over time (Win32/StealthFalcon; Deadglyph), and Check Point Research describes a 2025 intrusion chain delivering a custom implant (Horus Agent), indicating sustained development and modernization.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]]
- [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]
- [[20_Entities/07_TTPs/T1555.004 - Credentials from Password Stores: Windows Credential Manager]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1012 - Query Registry]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Win32/StealthFalcon]] — ESET-named Windows backdoor family (2019) attributed to Stealth Falcon; reported to use Windows background transfer mechanisms as part of its C2 approach.
- [[30_CIPHER/05_Malware/Deadglyph]] — sophisticated modular backdoor (ESET, 2023) attributed with high confidence to Stealth Falcon.
- [[30_CIPHER/05_Malware/Horus Agent]] — custom implant described by Check Point Research (2025) as delivered in a Stealth Falcon-attributed operation.
- [[30_CIPHER/05_Malware/Apollo]] — previously used customized implant referenced as a predecessor to Horus Agent in Check Point Research’s reporting.
- [[30_CIPHER/05_Malware/PowerShell]] and [[30_CIPHER/05_Malware/Windows Management Instrumentation]] — execution/collection ecosystem components emphasized in MITRE’s Stealth Falcon technique notes.
- [[30_CIPHER/05_Malware/Mythic]] — framework referenced by Check Point Research as the platform targeted by/for the Horus Agent build (tooling context for the 2025 campaign).
- [[30_CIPHER/05_Malware/Background Intelligent Transfer Service]] — Windows component referenced by ESET (2019) in the group’s C2 design.
- [[30_CIPHER/05_Malware/WebDAV]] — staging/hosting mechanism referenced by Check Point Research (2025) in the Stealth Falcon-attributed intrusion chain.

## 8. Infrastructure Patterns
- [[Targeted spearphishing lures]] with [[Macro-enabled document delivery]] and tailored pretexts (Citizen Lab; consistent follow-on reporting).
- [[Malicious URL shortener / link profiling]] used to profile targets and stage follow-on actions (Citizen Lab).
- [[HTTPS C2]] combined with [[Encrypted C2 channel]] for command and data transfer (MITRE technique notes).
- [[BITS-based C2]] leveraging native Windows transfer services for stealth and resilience (ESET, 2019).
- [[WebDAV-hosted payload staging]] as part of a Windows exploitation chain attributed to the actor (Check Point Research, 2025).
- [[Modular backdoor modules]] delivered or activated dynamically (ESET, 2023), enabling capability expansion with reduced on-disk footprint.

## 9. Campaign History
- **2012–2016 (publicly documented):** Citizen Lab reports a multi-year campaign targeting Emirati dissidents and associated civil society figures, including macro-enabled lure activity and PowerShell-centric implant behavior (published 2016-05-29).
- **2019-01-30 (context reporting):** Reuters publishes “Project Raven” investigation series focused on UAE cyber surveillance operations; frequently discussed alongside Stealth Falcon/target overlap claims in subsequent commentary.
- **2019-09-09:** ESET reports an undocumented Windows backdoor (Win32/StealthFalcon) attributed to Stealth Falcon, with observed victims spanning multiple countries including UAE and diplomatic-context targeting (reporting scope).
- **2023-09-22:** ESET publishes analysis of **Deadglyph**, a sophisticated backdoor attributed to Stealth Falcon and used for espionage against a Middle East governmental entity.
- **2025-03 (observed) / 2025-06-10 (published):** Check Point Research reports a Stealth Falcon-attributed attempted intrusion against a defense organization in Turkey leveraging **CVE-2025-33053**, patched by Microsoft on **2025-06-10**, delivering **Horus Agent** (and describing it as an evolution from **Apollo**).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Treat Stealth Falcon as a **highly targeted** threat: prioritize protection of at-risk user populations (executives, comms staff, journalists, policy teams) and their endpoints, identities, and cloud accounts.
- Strengthen controls for **phishing and lure execution** pathways, especially macro-enabled and shortcut-driven delivery patterns in high-risk user groups; emphasize rapid containment and forensic readiness over broad-based blocking alone.
- Increase visibility into **credential access** behaviors tied to password stores and browser credential harvesting, aligned to [[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]] and sub-techniques.
- Maintain detection and response maturity for **PowerShell and WMI** abuse in user contexts, aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]] and [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]].
- Prioritize timely patching and risk-based exposure review for **high-impact Windows vulnerabilities** when credible in-the-wild exploitation is reported, given public reporting of a Stealth Falcon-attributed zero-day chain in 2025.

## 12. Analyst Notes
- “Project Raven” is widely referenced in the same target narrative space as Stealth Falcon; however, many public discussions are inferential. Maintain strict case-by-case evidence standards before asserting equivalence.
- Stealth Falcon’s public tooling record shows continued modernization and modularity (PowerShell era → BITS-enabled backdoor → Deadglyph modular backdoor → 2025 custom implant framework), supporting an assessment of sustained resourcing.
- Keep ATT&CK mapping conservative and anchored to MITRE’s Stealth Falcon entry to avoid over-attribution of techniques described in vendor malware deep dives where group-level linkage may vary by campaign.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Stealth Falcon (G0038): https://attack.mitre.org/groups/G0038/
- Citizen Lab — Stealth Falcon (2016 report): https://citizenlab.org/2016/05/stealth-falcon/
- ESET Research — Win32/StealthFalcon backdoor (2019): https://www.welivesecurity.com/2019/09/09/backdoor-stealth-falcon-group/
- ESET Research — Deadglyph backdoor (2023): https://www.welivesecurity.com/en/eset-research/stealth-falcon-preying-middle-eastern-skies-deadglyph/
- Check Point Research — CVE-2025-33053 / Horus Agent report (2025): https://research.checkpoint.com/2025/stealth-falcon-zero-day/
- Reuters Investigates — Project Raven series hub (2019): https://www.reuters.com/investigates/section/usa-raven/

## 14. References
1. MITRE ATT&CK. “Stealth Falcon (G0038).” (Last Modified 2025-04-25). https://attack.mitre.org/groups/G0038/
2. Citizen Lab. “Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents.” (2016-05-29). https://citizenlab.org/2016/05/stealth-falcon/
3. ESET Research. “ESET discovered an undocumented backdoor used by the infamous Stealth Falcon group.” (2019-09-09). https://www.welivesecurity.com/2019/09/09/backdoor-stealth-falcon-group/
4. ESET Research. “Stealth Falcon preying over Middle Eastern skies with Deadglyph.” (2023-09-22). https://www.welivesecurity.com/en/eset-research/stealth-falcon-preying-middle-eastern-skies-deadglyph/
5. Check Point Research. “Stealth Falcon’s Exploit of Microsoft Zero Day Vulnerability (CVE-2025-33053).” (2025-06-10). https://research.checkpoint.com/2025/stealth-falcon-zero-day/
6. Reuters Investigates. “Project Raven” (series hub). (2019-01-30). https://www.reuters.com/investigates/section/usa-raven/
---
