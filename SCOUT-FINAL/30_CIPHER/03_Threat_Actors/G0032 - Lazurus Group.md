---
entity_type: threat_actor
actor_name: "Lazarus Group"
common_name: "Lazarus Group"
actor_id: "G0032"
actor_type: "State-sponsored cyber threat group; reported umbrella for multiple DPRK operators spanning espionage, destructive attacks, and financially motivated operations"
aliases: ["HIDDEN COBRA","Guardians of Peace","ZINC","Diamond Sleet","NICKEL ACADEMY","Labyrinth Chollima"]
country_of_origin: "North Korea (DPRK)"
suspected_sponsors: ["Reconnaissance General Bureau (RGB)"]
attribution_confidence: "Medium"
first_seen: "2009-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Financial gain","Sabotage/Disruption"]
objectives: ["Strategic intelligence collection against government/defense and high-value sectors","Revenue generation via financially motivated intrusions (reported across DPRK ecosystem)","Capability demonstration and destructive operations to impose cost and disruption (reported)","Long-term access and data theft via social engineering and multi-stage tooling"]
victimology_summary: "Lazarus Group (MITRE ATT&CK G0032) is widely reported as a DPRK state-sponsored cyber threat group attributed to the Reconnaissance General Bureau (RGB) and often treated as an umbrella label for multiple DPRK operators. Public reporting ties the group to a long history of cyber espionage, destructive activity (including the 2014 Sony Pictures destructive incident referenced in MITRE’s description), and financially motivated operations. MITRE tracks multiple Lazarus-linked campaigns (e.g., Operation Dream Job) and a broad malware/tool ecosystem spanning Windows, macOS, and cross-platform tradecraft, with repeated reliance on social engineering, staged malware delivery, and web-service-enabled command-and-control and exfiltration patterns."
target_sectors: ["Government","Defense/Aerospace","Critical infrastructure (reported)","Finance (reported)","Cryptocurrency/Blockchain ecosystem (reported)","IT & Security industry (targeted security researchers, reported)","Media/Entertainment (reported)"]
target_regions: ["Global"]
related_groups: ["APT38 (reported as financially motivated DPRK cluster)","BlueNoroff (reported as financially motivated DPRK cluster)","Stardust Chollima (reported)"]
malware: ["[[30_CIPHER/05_Malware/AppleJeus]]","[[30_CIPHER/05_Malware/AuditCred]]","[[30_CIPHER/05_Malware/BADCALL]]","[[30_CIPHER/05_Malware/Bankshot]]","[[30_CIPHER/05_Malware/BLINDINGCAN]]","[[30_CIPHER/05_Malware/Dtrack]]","[[30_CIPHER/05_Malware/FALLCHILL]]","[[30_CIPHER/05_Malware/HOPLIGHT]]","[[30_CIPHER/05_Malware/MagicRAT]]","[[30_CIPHER/05_Malware/HotCroissant]]","[[30_CIPHER/05_Malware/TAINTEDSCRIBE]]","[[30_CIPHER/05_Malware/ThreatNeedle]]"]
tools: ["[[30_CIPHER/05_Malware/Responder]]","[[30_CIPHER/05_Malware/netsh]]","[[30_CIPHER/05_Malware/RawDisk]]","[[30_CIPHER/05_Malware/route]]","[[30_CIPHER/05_Malware/DRATzarus]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Spearphishing Link]]","[[Spearphishing via Service]]","[[Fake recruiter personas]]","[[Social media personas]]","[[Weaponized open-source software]]","[[Compromised infrastructure]]","[[File hosting services]]","[[Cloud storage exfiltration]]","[[GitHub-based C2]]","[[Code signing abuse]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1566.003 - Phishing: Spearphishing via Service]]","[[20_Entities/07_TTPs/T1593.001 - Search Open Websites/Domains: Social Media]]","[[20_Entities/07_TTPs/T1585.001 - Establish Accounts: Social Media Accounts]]","[[20_Entities/07_TTPs/T1585.002 - Establish Accounts: Email Accounts]]","[[20_Entities/07_TTPs/T1656 - Impersonation]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1583.004 - Acquire Infrastructure: Server]]","[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]","[[20_Entities/07_TTPs/T1220 - XSL Script Processing]]","[[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32]]","[[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]","[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]","[[20_Entities/07_TTPs/T1036 - Masquerading]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay]]","[[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]","[[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1113 - Screen Capture]]","[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]","[[20_Entities/07_TTPs/T1485 - Data Destruction]]","[[20_Entities/07_TTPs/T1561.001 - Disk Wipe: Disk Content Wipe]]","[[20_Entities/07_TTPs/T1561.002 - Disk Wipe: Disk Structure Wipe]]","[[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Lazarus Group (G0032) (Last Modified 2025-10-24): https://attack.mitre.org/groups/G0032/","MITRE ATT&CK — Operation Dream Job (C0022): https://attack.mitre.org/campaigns/C0022/","Microsoft — Microsoft and Facebook disrupt ZINC/Lazarus; notes attribution to WannaCry and public gov attribution statements (2017-12-19): https://blogs.microsoft.com/on-the-issues/2017/12/19/microsoft-facebook-disrupt-zinc-malware-attack-protect-customers-internet-ongoing-cyberthreats/","Microsoft Security Blog — ZINC attacks against security researchers (ZINC later tracked as Diamond Sleet) (2021-01-28): https://www.microsoft.com/en-us/security/blog/2021/01/28/zinc-attacks-against-security-researchers/","Microsoft Security Blog — ZINC weaponizing open-source software (2022-09-29): https://www.microsoft.com/en-us/security/blog/2022/09/29/zinc-weaponizing-open-source-software/","CISA — AA21-048A: AppleJeus cryptocurrency trading platform malware (2021-04-15): https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-048a","Mandiant/Google Cloud — North Korea Leverages SaaS Provider in a Targeted Supply Chain Attack (UNC4899; TraderTraitor correspondence noted) (2023-07-24): https://cloud.google.com/blog/topics/threat-intelligence/north-korea-supply-chain","Mandiant/Google Cloud — Assessed Cyber Structure and Alignments of North Korea in 2023 (context on DPRK cyber units incl. APT38) (2023-10-10): https://cloud.google.com/blog/topics/threat-intelligence/north-korea-cyber-structure-alignment-2023"]
tags: ["threat-actor","lazarus","g0032","dprk","hidden-cobra","zinc","diamond-sleet","espionage","financially-motivated","destructive","supply-chain"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Lazarus Group

## 1. BLUF / Executive Summary
Lazarus Group (MITRE ATT&CK **G0032**) is a widely reported **DPRK state-sponsored** cyber threat group attributed to the **Reconnaissance General Bureau (RGB)** and frequently treated as an **umbrella label** encompassing multiple DPRK operators with overlapping infrastructure, personnel, and tooling. Public reporting and MITRE track Lazarus-linked activity across **espionage, destructive operations, and financially motivated intrusions**, with recurring tradecraft themes including **high-touch social engineering**, staged malware delivery, **web-service-enabled** command-and-control and exfiltration, and periodic use of destructive tooling.

## 2. Attribution Notes
- MITRE characterizes Lazarus as a **North Korean state-sponsored** group attributed to the **RGB**, while also noting the broader DPRK pattern of unit reorganization and shared resources that complicate operation-level attribution.
- Several ecosystems use different names for overlapping DPRK activity (e.g., **HIDDEN COBRA**, **ZINC/Diamond Sleet**, **Labyrinth Chollima**, **NICKEL ACADEMY**). Naming differences can reflect analytic methodology rather than discrete actors.
- Where reporting is ecosystem-specific (e.g., Mandiant UNC### tracks; Microsoft “Sleet” taxonomy), treat cross-mappings as **probabilistic** unless explicitly stated in primary sources.

## 3. Motivations & Objectives
- **Espionage:** Collection against government, defense/aerospace, and strategic sectors; persistent access and data theft.
- **Financial gain:** Revenue-generation operations reported across DPRK cyber activity, including cryptocurrency and financial targeting within the wider ecosystem.
- **Disruption / signaling:** Destructive events and wiper-like impacts reported in association with Lazarus-linked incidents.
- **Operational flexibility:** Ability to pivot from espionage to monetization (and vice versa) within the same targeting construct (noted in campaign reporting such as Operation Dream Job).

## 4. Targeting Profile
- **Global** victim set; commonly cited focus areas include:
  - Government, defense/aerospace, and critical infrastructure-adjacent organizations
  - Finance and cryptocurrency/blockchain organizations (reported)
  - IT and security community targets, including **security researchers** (reported by Microsoft)
  - Media/entertainment targets (reported; e.g., Sony Pictures destructive incident referenced by MITRE)
- **Victim selection** often aligns to DPRK strategic interests: intelligence value, disruption potential, or revenue opportunity.

## 5. Tradecraft Overview
- **Social engineering-led access:** Repeated use of spearphishing attachments/links and service-based approaches (e.g., professional networking platforms) consistent with “fake recruiter/job offer” narratives in public reporting and MITRE-tracked campaigns.
- **Multi-stage tooling ecosystem:** Broad malware set tracked by MITRE, including families used for backdoor access, collection, and operator tooling deployment (e.g., [[30_CIPHER/05_Malware/AppleJeus]], [[30_CIPHER/05_Malware/BLINDINGCAN]], [[30_CIPHER/05_Malware/Dtrack]], [[30_CIPHER/05_Malware/FALLCHILL]], [[30_CIPHER/05_Malware/HOPLIGHT]], [[30_CIPHER/05_Malware/MagicRAT]]).
- **Living-off-the-land + proxy execution:** Use of built-in Windows mechanisms and proxy execution patterns (e.g., [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]], [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]], [[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32]]) documented in MITRE’s mappings.
- **Web services in operations:** MITRE describes use of web services (including GitHub) for aspects of command-and-control or operational workflows (e.g., [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]).
- **Defense evasion + obfuscation:** Routine use of packing/obfuscation and masquerading behaviors (e.g., [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]], [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]], [[20_Entities/07_TTPs/T1036 - Masquerading]]).
- **Impact capability:** MITRE’s broader mappings include destructive/disk wipe behaviors via tooling like [[30_CIPHER/05_Malware/RawDisk]] aligned to [[20_Entities/07_TTPs/T1485 - Data Destruction]] and disk wipe sub-techniques.

## 6. MITRE ATT&CK Mapping
- Initial Access & Social Engineering
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
  - [[20_Entities/07_TTPs/T1566.003 - Phishing: Spearphishing via Service]]
  - [[20_Entities/07_TTPs/T1593.001 - Search Open Websites/Domains: Social Media]]
  - [[20_Entities/07_TTPs/T1656 - Impersonation]]
- Infrastructure & Execution
  - [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
  - [[20_Entities/07_TTPs/T1583.004 - Acquire Infrastructure: Server]]
  - [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
  - [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
  - [[20_Entities/07_TTPs/T1220 - XSL Script Processing]]
  - [[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32]]
  - [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]
- Persistence & Defense Evasion
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
  - [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
  - [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]
  - [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
  - [[20_Entities/07_TTPs/T1036 - Masquerading]]
- Credential Access & Lateral Movement
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
  - [[20_Entities/07_TTPs/T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay]]
  - [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]
  - [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]
- C2 & Exfiltration
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]
  - [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
  - [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]
- Collection & Impact
  - [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
  - [[20_Entities/07_TTPs/T1113 - Screen Capture]]
  - [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
  - [[20_Entities/07_TTPs/T1485 - Data Destruction]]
  - [[20_Entities/07_TTPs/T1561.001 - Disk Wipe: Disk Content Wipe]]
  - [[20_Entities/07_TTPs/T1561.002 - Disk Wipe: Disk Structure Wipe]]
- Supply Chain (reported across DPRK ecosystem; use carefully at operation level)
  - [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]

## 7. Malware & Tools Used
**Malware families (MITRE-tracked for G0032)**
- [[30_CIPHER/05_Malware/AppleJeus]] — trojanized cryptocurrency/trading application malware family tracked by MITRE and described in CISA reporting.
- [[30_CIPHER/05_Malware/BLINDINGCAN]], [[30_CIPHER/05_Malware/FALLCHILL]], [[30_CIPHER/05_Malware/Dtrack]], [[30_CIPHER/05_Malware/HOPLIGHT]] — representative Lazarus-linked backdoors/tooling tracked by MITRE for the group.
- [[30_CIPHER/05_Malware/MagicRAT]] — MITRE notes exclusive association with Lazarus operations in 2022.
- Additional MITRE-listed families frequently cited in Lazarus-linked reporting include [[30_CIPHER/05_Malware/Bankshot]], [[30_CIPHER/05_Malware/BADCALL]], [[30_CIPHER/05_Malware/AuditCred]], [[30_CIPHER/05_Malware/ThreatNeedle]], [[30_CIPHER/05_Malware/TAINTEDSCRIBE]], and [[30_CIPHER/05_Malware/HotCroissant]].

**Tools / utilities (MITRE-tracked and campaign-reported)**
- [[30_CIPHER/05_Malware/Responder]] — credential interception/relay tooling referenced in MITRE’s campaign mapping (noting it as obtained/used in Operation Dream Job context).
- [[30_CIPHER/05_Malware/netsh]], [[30_CIPHER/05_Malware/route]] — built-in utilities cited in MITRE’s group/software mappings as part of observed activity.
- [[30_CIPHER/05_Malware/RawDisk]] — destructive-enabling tooling referenced by MITRE mappings.

## 8. Infrastructure Patterns
- [[Fake recruiter personas]] and outreach via [[Social media personas]] consistent with Microsoft reporting on ZINC/Diamond Sleet social engineering against security researchers.
- Use of [[Weaponized open-source software]] and trojanized installers as initial footholds (reported by Microsoft).
- Reliance on [[File hosting services]] and [[Web services]] (including GitHub-referenced workflows) for staging, payload retrieval, or operational communications (MITRE notes).
- Frequent use of [[Cloud storage exfiltration]] patterns in specific campaigns (e.g., Operation Dream Job references exfiltration to cloud storage).
- Regular use of [[Compromised infrastructure]] and short-lived infrastructure segments to support delivery and C2.

## 9. Campaign History
- **2009–present (reported):** MITRE reports Lazarus active since at least 2009, with broad operational scope and multiple overlapping units.
- **2014-11 (reported):** MITRE’s group description references a destructive incident against Sony Pictures (Operation Blockbuster context).
- **2017-05 (reported):** Microsoft publicly associated ZINC/Lazarus with WannaCry and noted government attribution statements to North Korea (contextual, not a full incident dossier in this note).
- **2018–present (reported):** CISA reporting describes AppleJeus-themed operations using trojanized cryptocurrency trading platforms since at least 2018.
- **2019-09 to 2020-08 (MITRE Campaign):** [[Operation Dream Job]] (C0022) — Lazarus-linked espionage operation targeting defense/aerospace/government and other sectors, with at least one case of attempted monetization (MITRE).
- **2020–2022 (reported):** Microsoft documents ZINC/Diamond Sleet targeting security researchers and later weaponizing legitimate open-source tools as part of social engineering chains.
- **2023 (reported across DPRK ecosystem):** Mandiant describes a DPRK-nexus supply chain event involving a cryptocurrency-focused actor (UNC4899) and notes correspondence to “TraderTraitor” reporting; attribution to Lazarus specifically varies by vendor taxonomy, and should be treated as ecosystem-adjacent unless a source explicitly equates clusters.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Reduce exposure to social-engineering-led access: prioritize controls and user resilience for [[20_Entities/07_TTPs/T1566.003 - Phishing: Spearphishing via Service]] and recruiter/persona-driven lures, including heightened scrutiny of unsolicited “opportunity” outreach.
- Improve detection for suspicious system-binary proxy execution patterns aligned to [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]] and [[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32]] when correlated with new binaries or unusual persistence.
- Monitor for web-service abuse and cloud exfiltration patterns aligned to [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]] and [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]].
- Treat obfuscation and masquerading clusters (e.g., [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]] and [[20_Entities/07_TTPs/T1036 - Masquerading]]) as higher-risk when combined with social engineering entry points.
- Include impact readiness in playbooks: destructive outcomes aligned to [[20_Entities/07_TTPs/T1485 - Data Destruction]] and disk wipe techniques should be explicitly considered in incident response planning.

## 12. Analyst Notes
- Lazarus is frequently used as an umbrella label; operation-level precision often requires mapping to the specific sub-cluster (e.g., Microsoft “Sleet” nomenclature, Mandiant UNC tracking, and other vendor taxonomies).
- This note emphasizes **MITRE-tracked** associations for defensibility and avoids asserting contested one-to-one equivalences between all DPRK clusters and Lazarus without explicit primary-source statements.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Lazarus Group (G0032): https://attack.mitre.org/groups/G0032/
- MITRE ATT&CK — Operation Dream Job (C0022): https://attack.mitre.org/campaigns/C0022/
- Microsoft Security Blog — ZINC attacks against security researchers (2021-01-28): https://www.microsoft.com/en-us/security/blog/2021/01/28/zinc-attacks-against-security-researchers/
- Microsoft Security Blog — ZINC weaponizing open-source software (2022-09-29): https://www.microsoft.com/en-us/security/blog/2022/09/29/zinc-weaponizing-open-source-software/
- CISA — AA21-048A AppleJeus advisory (2021-04-15): https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-048a
- Mandiant/Google Cloud — DPRK supply chain attack (2023-07-24): https://cloud.google.com/blog/topics/threat-intelligence/north-korea-supply-chain

## 14. References
1. MITRE ATT&CK. “Lazarus Group (G0032).” (Last Modified 2025-10-24). https://attack.mitre.org/groups/G0032/
2. MITRE ATT&CK. “Operation Dream Job (C0022).” https://attack.mitre.org/campaigns/C0022/
3. Microsoft. “Microsoft and Facebook disrupt ZINC malware attack…” (2017-12-19). https://blogs.microsoft.com/on-the-issues/2017/12/19/microsoft-facebook-disrupt-zinc-malware-attack-protect-customers-internet-ongoing-cyberthreats/
4. Microsoft Security Blog. “ZINC attacks against security researchers.” (2021-01-28). https://www.microsoft.com/en-us/security/blog/2021/01/28/zinc-attacks-against-security-researchers/
5. Microsoft Security Blog. “ZINC weaponizing open-source software.” (2022-09-29). https://www.microsoft.com/en-us/security/blog/2022/09/29/zinc-weaponizing-open-source-software/
6. CISA. “AA21-048A: AppleJeus: Analysis of North Korea’s Cryptocurrency Trading Platform Malware.” (2021-04-15). https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-048a
7. Mandiant (Google Cloud). “North Korea Leverages SaaS Provider in a Targeted Supply Chain Attack.” (2023-07-24). https://cloud.google.com/blog/topics/threat-intelligence/north-korea-supply-chain
8. Mandiant (Google Cloud). “Assessed Cyber Structure and Alignments of North Korea in 2023.” (2023-10-10). https://cloud.google.com/blog/topics/threat-intelligence/north-korea-cyber-structure-alignment-2023
---
