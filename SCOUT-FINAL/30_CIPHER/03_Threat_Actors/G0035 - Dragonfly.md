---
entity_type: threat_actor
actor_name: "Dragonfly"
common_name: "Dragonfly"
actor_id: "G0035"
actor_type: "State-linked cyber espionage actor with sustained critical-infrastructure and ICS-adjacent targeting; supply-chain and credential-harvesting tradecraft"
aliases: ["Energetic Bear","Berserk Bear","Crouching Yeti","IRON LIBERTY","TG-4192","TEMP.Isotope","DYMALLOY","BROMINE","Ghost Blizzard"]
country_of_origin: "Russia"
suspected_sponsors: ["FSB Centre 16 (Unit 71330)"]
attribution_confidence: "High"
first_seen: "2010-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Strategic access development","Potential contingency access for future disruption (assessed by some reporting)"]
objectives: ["Gain and maintain access to energy and critical infrastructure environments (often via IT-to-OT adjacency)","Collect credentials and reconnaissance data related to industrial environments and ICS/SCADA ecosystems","Leverage supply-chain compromise and watering-hole activity to scale initial access","Enable follow-on access and persistence via web shells, valid accounts, and staged tooling"]
victimology_summary: "Dragonfly (MITRE ATT&CK G0035) is a Russia-linked cyber espionage group attributed in public reporting to Russia’s Federal Security Service (FSB) Centre 16. Active since at least 2010, Dragonfly has targeted defense and aviation, government entities, and organizations tied to industrial control systems (ICS) and critical infrastructure. Publicly described activity includes two commonly referenced phases—an earlier campaign (often associated with Havex/ICS supply-chain compromise) and later, more targeted activity (“Dragonfly 2.0”) emphasizing credential theft, watering-hole compromises, and access to operationally sensitive environments."
target_sectors: ["Energy (electric, oil & gas)","ICS/OT vendors and integrators","Critical infrastructure","Defense","Aviation","Government","Nuclear (reported)"]
target_regions: ["Europe","North America","Global"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Havex]]","[[30_CIPHER/05_Malware/Backdoor.Oldrea]]","[[30_CIPHER/05_Malware/Karagany]]","[[30_CIPHER/05_Malware/Goodor]]","[[30_CIPHER/05_Malware/Dorshel]]","[[30_CIPHER/05_Malware/Heriplor]]","[[30_CIPHER/05_Malware/MCMD]]"]
tools: ["[[30_CIPHER/05_Malware/PowerShell]]","[[30_CIPHER/05_Malware/PsExec]]","[[30_CIPHER/05_Malware/Mimikatz]]","[[30_CIPHER/05_Malware/CrackMapExec]]","[[30_CIPHER/05_Malware/Impacket]]","[[30_CIPHER/05_Malware/Hydra]]","[[30_CIPHER/05_Malware/Phishery]]","[[30_CIPHER/05_Malware/Shellter]]","[[30_CIPHER/05_Malware/ScreenUtil]]"]
infrastructure: ["[[Trojanized ICS software updates]]","[[Vendor app-store abuse]]","[[Watering-hole compromise]]","[[Strategic website compromise]]","[[Credential-harvesting redirectors]]","[[Malicious lookalike domains]]","[[VPS-based staging]]","[[Compromised legitimate servers for hosting]]","[[OWA/webmail server web shells]]","[[SMB-based C2 channel (reported)]]"]
ttps: ["[[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]","[[20_Entities/07_TTPs/T0862 - Supply Chain Compromise]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1598.002 - Phishing for Information: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T0817 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1221 - Template Injection]]","[[20_Entities/07_TTPs/T1187 - Forced Authentication]]","[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]","[[20_Entities/07_TTPs/T1210 - Exploitation of Remote Services]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.006 - Command and Scripting Interpreter: Python]]","[[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]","[[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]","[[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]","[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]","[[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Dragonfly (G0035) (Last Modified 2024-01-08): https://attack.mitre.org/groups/G0035/","U.S. DOJ — Four Russian Government Employees Charged… (Dragonfly/Havex; Dragonfly 2.0) (Press Release 2022-03-24, updated 2025-02-06): https://www.justice.gov/archives/opa/pr/four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting-critical","UK Government — Russia’s FSB malign activity: factsheet (FSB Centre 16; Energetic Bear/Dragonfly naming) (Updated 2023-12-07): https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/russias-fsb-malign-activity-factsheet","Broadcom/Symantec — Dragonfly: Western energy sector targeted by sophisticated attack group (Dragonfly 2.0) (2017-10-20): https://www.security.com/threat-intelligence/dragonfly-energy-sector-cyber-attacks","Secureworks — Resurgent IRON LIBERTY Targeting Energy Sector (2019-07-24): https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector","Virus Bulletin — The Baffling Berserk Bear: A Decade’s Activity Targeting Critical Infrastructure (2021-10-07): https://vblocalhost.com/uploads/VB2021-Slowik.pdf"]
tags: ["threat-actor","dragonfly","energetic-bear","berserk-bear","g0035","fsb","ics","supply-chain","watering-hole","credential-theft"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Dragonfly

## 1. BLUF / Executive Summary
Dragonfly (MITRE ATT&CK **G0035**) is a Russia-linked cyber espionage actor attributed in public reporting to **FSB Centre 16**. Since at least **2010**, Dragonfly has maintained a persistent focus on **critical infrastructure and ICS-adjacent ecosystems**, combining **supply-chain compromise**, **watering-hole/strategic web compromise**, and **credential-harvesting** tradecraft to obtain and maintain access. Public records frequently frame activity in two broad phases: an earlier campaign commonly associated with **Havex**-linked supply-chain activity and a later, more targeted phase (“Dragonfly 2.0”) emphasizing credential theft, remote access, and access to operationally sensitive environments.

## 2. Attribution Notes
- MITRE attributes Dragonfly to **Russia’s FSB Centre 16** and tracks the actor under **G0035**.
- UK government public attribution places **Energetic Bear / Berserk Bear / Dragonfly / IRON LIBERTY / TG-4192** naming within the **FSB Centre 16** umbrella.
- A U.S. Department of Justice press release (2022-03-24; updated 2025-02-06) describes two energy-sector campaign phases commonly referred to as **“Dragonfly” / “Havex” (2012–2014)** and **“Dragonfly 2.0” (2014–2017)**, reinforcing public-sector alignment and long-running operational continuity.

## 3. Motivations & Objectives
- **Primary:** Intelligence collection and strategic access development across energy and ICS-adjacent targets.
- **Operational:** Credential theft and reconnaissance of industrial environments, enabling deeper access to systems and identities relevant to OT/ICS operations.
- **Strategic (assessed in some reporting):** Maintain footholds that could enable future operational effects in crisis scenarios, even where observed activity is primarily reconnaissance-oriented.

## 4. Targeting Profile
- **Core sectors:** Energy (electric, oil & gas) and organizations that build, integrate, or support **ICS/SCADA** environments.
- **Additional sectors:** Defense and aviation, government entities, and related critical infrastructure stakeholders.
- **Geography:** Historically reported targeting emphasizes Europe and North America, with broader global exposure in large-scale compromises.

## 5. Tradecraft Overview
- **Supply-chain enablement:** Public reporting describes trojanized ICS-related software updates and placement of compromised installers in legitimate distribution channels (aligns to [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]] / [[20_Entities/07_TTPs/T0862 - Supply Chain Compromise]]).
- **Watering-hole and web compromise:** Strategic website compromise and credential-harvesting workflows are highlighted across multiple reporting streams (aligns to [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] / [[20_Entities/07_TTPs/T0817 - Drive-by Compromise]]).
- **Credential-centric access:** Techniques described include template injection and forced-authentication patterns to elicit credentials or hashes (aligns to [[20_Entities/07_TTPs/T1221 - Template Injection]] and [[20_Entities/07_TTPs/T1187 - Forced Authentication]]).
- **Post-compromise enterprise access:** MITRE documents web shells, remote services (notably RDP), valid account use, and staged tool transfer as recurring elements (aligns to [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]], [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]], [[20_Entities/07_TTPs/T1078 - Valid Accounts]], [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]).
- **Credential dumping and discovery:** MITRE documents multiple credential dumping sub-techniques plus discovery patterns consistent with domain-focused operations (aligns to [[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]], [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]], [[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]).
- **Operational security and cleanup:** MITRE notes log clearing and file deletion behaviors consistent with reducing forensic visibility (aligns to [[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]] and [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]).

## 6. MITRE ATT&CK Mapping
- Initial Access / Pre-compromise
  - [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]
  - [[20_Entities/07_TTPs/T0862 - Supply Chain Compromise]]
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1598.002 - Phishing for Information: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link]]
  - [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
  - [[20_Entities/07_TTPs/T0817 - Drive-by Compromise]]
  - [[20_Entities/07_TTPs/T1221 - Template Injection]]
  - [[20_Entities/07_TTPs/T1187 - Forced Authentication]]
  - [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
  - [[20_Entities/07_TTPs/T1210 - Exploitation of Remote Services]]
- Execution / Tooling
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.006 - Command and Scripting Interpreter: Python]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- Credential Access / Lateral Access
  - [[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]
  - [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]
  - [[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
  - [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
- Persistence / Defense Evasion
  - [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]
  - [[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]
  - [[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]
  - [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- Reconnaissance / Staging
  - [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
  - [[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]
  - [[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Havex]] — publicly referenced in U.S. DOJ reporting as the malware family used in the 2012–2014 phase; frequently discussed in ICS/SCADA supply-chain compromise context.
- [[30_CIPHER/05_Malware/Backdoor.Oldrea]] — tracked by MITRE as associated software for Dragonfly (commonly discussed alongside Havex reporting).
- [[30_CIPHER/05_Malware/Karagany]] — reported in energy-sector intrusion reporting (including “Dragonfly 2.0” coverage) as a backdoor used against targeted environments.
- [[30_CIPHER/05_Malware/Goodor]], [[30_CIPHER/05_Malware/Dorshel]], [[30_CIPHER/05_Malware/Heriplor]] — backdoors reported in vendor writeups covering Dragonfly activity and energy-sector targeting.
- [[30_CIPHER/05_Malware/MCMD]] — malware/tooling associated with IRON LIBERTY / Dragonfly-linked activity described in Secureworks reporting.
- Common operator tooling observed in reporting and/or MITRE technique narratives:
  - [[30_CIPHER/05_Malware/PowerShell]], [[30_CIPHER/05_Malware/PsExec]]
  - [[30_CIPHER/05_Malware/Mimikatz]], [[30_CIPHER/05_Malware/Impacket]], [[30_CIPHER/05_Malware/CrackMapExec]]
  - [[30_CIPHER/05_Malware/Hydra]], [[30_CIPHER/05_Malware/Phishery]]
  - [[30_CIPHER/05_Malware/Shellter]], [[30_CIPHER/05_Malware/ScreenUtil]]

## 8. Infrastructure Patterns
- [[Trojanized ICS software updates]] and [[Vendor app-store abuse]] to distribute malware through trusted channels.
- [[Watering-hole compromise]] / [[Strategic website compromise]] to reach engineers and ICS-adjacent personnel.
- [[Credential-harvesting redirectors]] and lookalike infrastructure (e.g., [[Malicious lookalike domains]]) to acquire valid access.
- [[VPS-based staging]] and [[Compromised legitimate servers for hosting]] to reduce attribution and blend with normal traffic.
- [[OWA/webmail server web shells]] used to sustain access and support follow-on tooling delivery.
- Reported use of [[SMB-based C2 channel (reported)]] in some activity narratives.

## 9. Campaign History
- **2010–2014 (reported):** Early Dragonfly activity widely described across vendor reporting and later synthesis work, featuring a blend of phishing, watering-hole compromise, and supply-chain tradecraft; commonly associated with [[30_CIPHER/05_Malware/Havex]] narratives.
- **2012–2014 (per U.S. DOJ framing):** Campaign phase commonly referred to as “Dragonfly” or “Havex,” involving supply-chain compromise of ICS/SCADA manufacturers and trojanized updates.
- **2014–2017 (per U.S. DOJ framing):** “Dragonfly 2.0” phase characterized as more targeted, with spearphishing and watering-hole activity aimed at specific energy-sector entities and personnel.
- **2015–2017 (vendor reporting emphasis):** Symantec describes renewed activity (“Dragonfly 2.0”) including credential harvesting, trojanized software, and access into operationally sensitive contexts.
- **2016–2018+ (reported):** Secureworks describes resurgent IRON LIBERTY / Dragonfly-linked activity using a mix of new and old techniques and tooling in energy-sector contexts.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Treat Dragonfly as an **ICS-adjacent threat** even when detections appear “pure IT”: prioritize security governance at IT/OT boundaries and protect identities and hosts used by engineers, integrators, and vendors.
- Emphasize prevention and detection for **supply-chain exposure** (third-party software distribution paths, vendor portals, and update workflows) given repeated reporting of trojanized software distribution.
- Strengthen defenses against **credential harvesting** and identity compromise scenarios, especially in environments where webmail and remote access services represent high-value entry points.
- Maintain high confidence monitoring around behaviors aligned to web shells, remote access, valid accounts, and credential dumping, with special attention to environments supporting critical services.

## 12. Analyst Notes
- Public naming varies heavily (Dragonfly/Energetic Bear/Berserk Bear/IRON LIBERTY/TG-4192). This note treats these as overlapping labels for a commonly described activity cluster and anchors identity to **MITRE G0035**.
- Some public reporting discusses “potential for sabotage” based on proximity to operational systems; open reporting more consistently supports **espionage and access development** rather than confirmed disruptive outcomes.
- When correlating incidents, prefer government attributions and primary vendor research over secondary summaries due to frequent alias overlap and campaign-phase labeling differences.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Dragonfly (G0035): https://attack.mitre.org/groups/G0035/
- U.S. DOJ — Dragonfly/Havex & Dragonfly 2.0 indictment summary (press release): https://www.justice.gov/archives/opa/pr/four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting-critical
- UK Government — Russia’s FSB malign activity: factsheet (FSB Centre 16): https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/russias-fsb-malign-activity-factsheet
- Broadcom/Symantec — Dragonfly 2.0 energy-sector reporting: https://www.security.com/threat-intelligence/dragonfly-energy-sector-cyber-attacks
- Secureworks — Resurgent IRON LIBERTY Targeting Energy Sector: https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector
- Virus Bulletin — The Baffling Berserk Bear (timeline and synthesis): https://vblocalhost.com/uploads/VB2021-Slowik.pdf

## 14. References
1. MITRE ATT&CK. “Dragonfly (G0035).” (Last Modified 2024-01-08). https://attack.mitre.org/groups/G0035/
2. U.S. Department of Justice. “Four Russian Government Employees Charged in Two Historical Hacking Campaigns Targeting Critical Infrastructure Worldwide.” (2022-03-24; updated 2025-02-06). https://www.justice.gov/archives/opa/pr/four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting-critical
3. UK Government (FCDO). “Russia’s FSB malign activity: factsheet.” (Updated 2023-12-07). https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/russias-fsb-malign-activity-factsheet
4. Broadcom/Symantec (Security.com). “Dragonfly: Western energy sector targeted by sophisticated attack group.” (2017-10-20). https://www.security.com/threat-intelligence/dragonfly-energy-sector-cyber-attacks
5. Secureworks. “Resurgent IRON LIBERTY Targeting Energy Sector.” (2019-07-24). https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector
6. Virus Bulletin. “The Baffling Berserk Bear: A Decade’s Activity Targeting Critical Infrastructure.” (2021-10-07). https://vblocalhost.com/uploads/VB2021-Slowik.pdf
---
