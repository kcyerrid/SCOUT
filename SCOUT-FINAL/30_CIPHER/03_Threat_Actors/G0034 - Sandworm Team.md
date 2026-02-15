---
entity_type: threat_actor
actor_name: "Sandworm Team"
common_name: "Sandworm Team"
actor_id: "G0034"
actor_type: "State-sponsored destructive threat group (GRU Unit 74455 / GTsST); conducts cyber sabotage, espionage, and disruptive operations"
aliases: ["APT44","Voodoo Bear","Telebots","ELECTRUM","IRON VIKING","Seashell Blizzard","IRIDIUM","FROZENBARENTS","BlackEnergy (Group)","Quedagh"]
country_of_origin: "Russia"
suspected_sponsors: ["GRU (Russia) — Main Center for Special Technologies (GTsST), Unit 74455"]
attribution_confidence: "High"
first_seen: "2009-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Sabotage/Disruption","Espionage","Strategic signaling"]
objectives: ["Disrupt and degrade critical infrastructure and essential services (notably energy/ICS environments)","Conduct destructive operations (wipers and other impact tooling) against priority targets","Support Russian strategic objectives through cyber-enabled coercion and destabilization","Maintain access for follow-on operations via opportunistic initial access and handoff to specialized teams (reported)"]
victimology_summary: "Sandworm Team (MITRE ATT&CK G0034) is a destructive threat group attributed to Russia’s GRU Unit 74455 (GTsST) and assessed active since at least 2009. Public reporting and government attributions tie Sandworm to high-impact operations including Ukraine power grid attacks (2015, 2016, and later intrusions), the globally disruptive NotPetya event (2017), the Olympic Destroyer disruption (2018), and other operations targeting government, election-related, and international organizations. More recent reporting highlights continued activity during Russia’s war against Ukraine, including disruptive/OT-focused operations and mobile malware targeting Android devices used by Ukrainian military personnel, as well as multiyear global access operations linked to a Sandworm subgroup."
target_sectors: ["Energy/Electric utilities","Critical infrastructure","Government","Defense","International organizations","Telecommunications (reported)","Logistics/transportation (reported)","IT service providers and perimeter device ecosystems (reported)"]
target_regions: ["Ukraine (primary historical focus)","Europe","Global"]
related_groups: ["APT28 (GRU Unit 26165) (reported operational assistance in some cases)"]
malware: ["[[30_CIPHER/05_Malware/BlackEnergy]]","[[30_CIPHER/05_Malware/KillDisk]]","[[30_CIPHER/05_Malware/Industroyer]]","[[30_CIPHER/05_Malware/Industroyer2]]","[[30_CIPHER/05_Malware/NotPetya]]","[[30_CIPHER/05_Malware/Olympic Destroyer]]","[[30_CIPHER/05_Malware/Cyclops Blink]]","[[30_CIPHER/05_Malware/VPNFilter]]","[[30_CIPHER/05_Malware/CaddyWiper]]","[[30_CIPHER/05_Malware/Infamous Chisel]]","[[30_CIPHER/05_Malware/AcidRain]]","[[30_CIPHER/05_Malware/AcidPour]]","[[30_CIPHER/05_Malware/Bad Rabbit]]"]
tools: ["[[30_CIPHER/05_Malware/PowerShell]]","[[30_CIPHER/05_Malware/Windows Command Shell]]","[[30_CIPHER/05_Malware/Windows Management Instrumentation]]","[[30_CIPHER/05_Malware/Mimikatz]]","[[30_CIPHER/05_Malware/GOGETTER]]","[[30_CIPHER/05_Malware/Neo-REGEORG]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Drive-by Compromise]]","[[Exploit Public-Facing Application]]","[[Compromised software supply chain]]","[[Router/perimeter device botnet]]","[[Operational technology targeting]]","[[Wiper-based disruption]]","[[Mobile malware targeting]]","[[Dynamic infrastructure acquisition]]","[[Leased servers and resellers]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]","[[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]","[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]","[[20_Entities/07_TTPs/T1562.002 - Impair Defenses: Disable Windows Event Logging]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]","[[20_Entities/07_TTPs/T1485 - Data Destruction]]","[[20_Entities/07_TTPs/T1561.001 - Disk Wipe: Disk Content Wipe]]","[[20_Entities/07_TTPs/T1561.002 - Disk Wipe: Disk Structure Wipe]]","[[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]","[[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]","[[20_Entities/07_TTPs/T1570 - Lateral Tool Transfer]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Sandworm Team (G0034) (Last Modified 2024-12-04): https://attack.mitre.org/groups/G0034/","U.S. DOJ — Six Russian GRU Officers Charged… (2020-10-19): https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and","UK Government — Profile: GRU cyber and hybrid threat operations (Sandworm/APT44 as Unit 74455/GTsST): https://www.gov.uk/government/publications/profile-gru-cyber-and-hybrid-threat-operations/profile-gru-cyber-and-hybrid-threat-operations","MITRE ATT&CK — 2015 Ukraine Electric Power Attack (C0028): https://attack.mitre.org/campaigns/C0028/","MITRE ATT&CK — 2016 Ukraine Electric Power Attack (C0025): https://attack.mitre.org/campaigns/C0025/","MITRE ATT&CK — 2022 Ukraine Electric Power Attack (C0034): https://attack.mitre.org/campaigns/C0034/","CISA/NCSC/NSA/FBI — AA22-054A: Cyclops Blink replaces VPNFilter (2022-02-23): https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-054a","CISA — Infamous Chisel Malware Analysis Report (AR23-243A) (2023-08-31): https://www.cisa.gov/news-events/analysis-reports/ar23-243a","NSA — Government agencies report Infamous Chisel; reiterates Sandworm attribution to GRU/GTsST (2023-08-31): https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3511738/government-agencies-report-new-russian-malware-targets-ukrainian-military/","ESET — Industroyer2: Industroyer reloaded (2022-04-12): https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/","Microsoft Threat Intelligence — The BadPilot campaign (Seashell Blizzard subgroup) (2025-02-12): https://www.microsoft.com/en-us/security/blog/2025/02/12/the-badpilot-campaign-seashell-blizzard-subgroup-conducts-multiyear-global-access-operation/"]
tags: ["threat-actor","sandworm","g0034","apt44","voodoo-bear","telebots","gru","unit-74455","destructive","ics","ukraine","notpetya","industroyer","cyclops-blink"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Sandworm Team

## 1. BLUF / Executive Summary
Sandworm Team (MITRE ATT&CK **G0034**) is a Russia-linked, GRU Unit **74455 (GTsST)** threat group with a long record of **destructive and disruptive cyber operations**, including multiple **Ukraine power grid intrusions**, the **NotPetya** global outbreak (2017), and **Olympic Destroyer** (2018). Government attributions and indictments strongly support the Unit 74455 linkage, and open reporting indicates continued activity during Russia’s war against Ukraine, including **wiper operations**, **perimeter device compromises**, and **mobile-focused malware** targeting Android devices in a military context.

## 2. Attribution Notes
- MITRE attributes Sandworm Team to Russia’s **GRU Main Center for Special Technologies (GTsST), Unit 74455**, citing U.S. DOJ and UK government sources.
- The U.S. DOJ (2020-10-19) charged six GRU Unit 74455 officers in connection with multiple operations publicly associated with Sandworm (including the 2015/2016 Ukraine power events, NotPetya, Olympic Destroyer, and Georgia-related activity).
- Vendor taxonomies vary; Microsoft tracks overlapping activity under names including **Seashell Blizzard** (and previously **IRIDIUM**) and has described subgroup-level roles (e.g., an initial access subgroup).

## 3. Motivations & Objectives
- **Strategic disruption and coercion:** degrade critical services and impose operational costs (especially in Ukraine).
- **Operational/strategic espionage:** access and situational awareness within government, critical infrastructure, and international organizations.
- **Signaling and shaping effects:** high-visibility disruptive actions consistent with state strategic objectives.

## 4. Targeting Profile
- **Primary:** Ukrainian energy and broader Ukrainian state/critical infrastructure ecosystems.
- **Secondary/global:** international organizations and events (e.g., Olympics), election-related targets (reported), and global spillover effects from destructive campaigns.
- **Environments of note:** OT/ICS-adjacent networks and supporting IT layers; perimeter network devices; mobile endpoints in a military operating context (reported for Infamous Chisel).

## 5. Tradecraft Overview
- **Initial access diversity:** historical reporting includes spearphishing and drive-by activity; more recent reporting highlights opportunistic exploitation and infrastructure scanning behavior consistent with sustained initial access operations.
- **Impact tooling specialization:** repeated use of **wipers/destructive malware** across campaigns (e.g., KillDisk lineage, CaddyWiper; AcidRain/AcidPour in broader disruptive contexts).
- **ICS/OT capability:** multiple Ukraine power grid incidents demonstrate intent and capability to interfere with operational processes, including use of ICS-specific tooling (e.g., Industroyer/Industroyer2-related activity).
- **Infrastructure pragmatism:** use of acquired/leased infrastructure and rapid operationalization; perimeter device targeting to gain durable footholds outside typical endpoint controls.
- **Subgroup model (reported):** reporting describes role separation (initial access vs. follow-on exploitation/impact), enabling operational scale and adaptability.

## 6. MITRE ATT&CK Mapping
- Initial Access
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
  - [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
  - [[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]
- Execution / C2 / Movement
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]
  - [[20_Entities/07_TTPs/T1570 - Lateral Tool Transfer]]
- Persistence / Evasion
  - [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
  - [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
  - [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]
  - [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
  - [[20_Entities/07_TTPs/T1562.002 - Impair Defenses: Disable Windows Event Logging]]
- Credential Access
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
  - [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- Impact / Supply Chain
  - [[20_Entities/07_TTPs/T1485 - Data Destruction]]
  - [[20_Entities/07_TTPs/T1561.001 - Disk Wipe: Disk Content Wipe]]
  - [[20_Entities/07_TTPs/T1561.002 - Disk Wipe: Disk Structure Wipe]]
  - [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/BlackEnergy]] and [[30_CIPHER/05_Malware/KillDisk]] — associated with the 2015 Ukraine power disruption campaign (MITRE campaign tracking).
- [[30_CIPHER/05_Malware/Industroyer]] — associated with the 2016 Ukraine power disruption campaign (MITRE campaign tracking).
- [[30_CIPHER/05_Malware/Industroyer2]] — ICS-capable malware reported in the attempted 2022 Ukraine power incident response work (ESET/CERT-UA collaboration reporting).
- [[30_CIPHER/05_Malware/CaddyWiper]] — wiper associated with the 2022 Ukraine electric power attack campaign (MITRE campaign tracking).
- [[30_CIPHER/05_Malware/NotPetya]] and [[30_CIPHER/05_Malware/Olympic Destroyer]] — cited in U.S. DOJ’s 2020 indictment context and MITRE’s Sandworm profile as major operations attributed to Unit 74455-linked officers.
- [[30_CIPHER/05_Malware/Cyclops Blink]] — malware framework described by US/UK partners as replacing [[30_CIPHER/05_Malware/VPNFilter]] and attributed to Sandworm.
- [[30_CIPHER/05_Malware/Infamous Chisel]] — Android-focused malware suite assessed by US/UK partners as associated with Sandworm activity.
- [[30_CIPHER/05_Malware/AcidRain]] / [[30_CIPHER/05_Malware/AcidPour]] — destructive tooling associated with Sandworm in public reporting and MITRE software associations.
- Commonly observed operator utilities and components (where tied to MITRE/campaign documentation): [[30_CIPHER/05_Malware/PowerShell]], [[30_CIPHER/05_Malware/Windows Command Shell]], [[30_CIPHER/05_Malware/Windows Management Instrumentation]], [[30_CIPHER/05_Malware/Mimikatz]].

## 8. Infrastructure Patterns
- [[Compromised software supply chain]] as an access multiplier (widely discussed in NotPetya context; referenced in government/industry reporting and MITRE’s Sandworm narrative).
- [[Router/perimeter device botnet]] tradecraft and long-lived footholds at the network edge (e.g., [[30_CIPHER/05_Malware/Cyclops Blink]] as described in joint advisories).
- [[Operational technology targeting]] where IT access is leveraged to impact OT/ICS processes (Ukraine power incidents tracked by MITRE; OT/ICS-focused reporting across multiple years).
- [[Mobile malware targeting]] for field-operating Android devices (Infamous Chisel reporting).
- [[Dynamic infrastructure acquisition]] and [[Leased servers and resellers]] to support campaigns and reduce traceability (noted in MITRE’s group-level technique narratives).

## 9. Campaign History
- **2015-12 to 2016-01:** [[2015 Ukraine Electric Power Attack]] (MITRE **C0028**) — BlackEnergy/KillDisk-associated disruption of Ukrainian power operations.
- **2016-12:** [[2016 Ukraine Electric Power Attack]] (MITRE **C0025**) — Industroyer-associated disruption of Ukrainian power distribution substations.
- **2017-06 (reported):** [[30_CIPHER/05_Malware/NotPetya]] — widely attributed destructive outbreak with global impact; cited in U.S. DOJ’s Unit 74455 indictment context.
- **2018-02 (reported):** [[30_CIPHER/05_Malware/Olympic Destroyer]] — disruption of systems supporting the PyeongChang Winter Olympics; cited in U.S. DOJ’s indictment context.
- **2022-02 (reported):** ViaSat KA-SAT incident linkage and edge-device disruption narratives associated with Sandworm in public reporting and MITRE software associations (e.g., [[30_CIPHER/05_Malware/AcidRain]]).
- **2022-06 to 2022-10:** [[2022 Ukraine Electric Power Attack]] (MITRE **C0034**) — campaign description includes [[30_CIPHER/05_Malware/CaddyWiper]] and other tooling in an OT/ICS intrusion context.
- **2022-04 (reported):** [[30_CIPHER/05_Malware/Industroyer2]] reported in response to a Ukraine energy provider incident (ESET/CERT-UA reporting).
- **2022-02 onward (reported):** [[30_CIPHER/05_Malware/Cyclops Blink]] described as replacing [[30_CIPHER/05_Malware/VPNFilter]] (joint advisory).
- **2023-08 (reported):** [[30_CIPHER/05_Malware/Infamous Chisel]] malware analysis and attribution statements from US/UK partners.
- **2024–2025 (reported):** Microsoft describes a multiyear global initial access operation linked to a **Seashell Blizzard** subgroup, indicating continued Sandworm-linked operational reach beyond Ukraine.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Treat Sandworm as both an **IT** and **OT/ICS** risk: ensure governance bridges IT security monitoring with OT safety/availability requirements, and prioritize resilience against disruptive outcomes.
- Prioritize hardening and visibility for **edge/perimeter devices** and remote access surfaces given repeated Sandworm-linked activity targeting network infrastructure and public-facing systems.
- Increase detection emphasis on **impact precursors** (staging for destructive actions) and post-compromise behaviors that commonly precede disruption, including obfuscation, persistence, and lateral movement patterns.
- For organizations supporting Ukraine-adjacent or high-tension geopolitical contexts, incorporate **wiper/disruption** scenarios into continuity planning and executive-level risk discussions.

## 12. Analyst Notes
- Sandworm’s “brand” spans multiple vendor naming schemes (APT44, Voodoo Bear, Telebots, Seashell Blizzard). Mapping should be explicitly documented per-source when operationally relevant.
- Where incident-level claims are made (e.g., Viasat tooling), prefer government advisories and primary vendor incident writeups; avoid over-aggregating ecosystem-adjacent activity without explicit linkage.
- The group’s history shows credible **escalation potential** (sabotage/disruption) even when observed activity appears focused on access or espionage.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Sandworm Team (G0034): https://attack.mitre.org/groups/G0034/
- U.S. DOJ — GRU Unit 74455 indictment press release (2020-10-19): https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and
- UK Government — Profile: GRU cyber and hybrid threat operations (Unit 74455/GTsST): https://www.gov.uk/government/publications/profile-gru-cyber-and-hybrid-threat-operations/profile-gru-cyber-and-hybrid-threat-operations
- CISA — AA22-054A (Cyclops Blink): https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-054a
- CISA — AR23-243A (Infamous Chisel): https://www.cisa.gov/news-events/analysis-reports/ar23-243a
- ESET — Industroyer2 analysis: https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/
- Microsoft — BadPilot / Seashell Blizzard subgroup report: https://www.microsoft.com/en-us/security/blog/2025/02/12/the-badpilot-campaign-seashell-blizzard-subgroup-conducts-multiyear-global-access-operation/

## 14. References
1. MITRE ATT&CK. “Sandworm Team (G0034).” (Last Modified 2024-12-04). https://attack.mitre.org/groups/G0034/
2. U.S. Department of Justice. “Six Russian GRU Officers Charged in Connection with Worldwide Deployment of Destructive Malware and Other Disruptive Actions in Cyberspace.” (2020-10-19). https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and
3. UK Government. “Profile: GRU cyber and hybrid threat operations.” (Accessed 2025-12-25). https://www.gov.uk/government/publications/profile-gru-cyber-and-hybrid-threat-operations/profile-gru-cyber-and-hybrid-threat-operations
4. MITRE ATT&CK. “2015 Ukraine Electric Power Attack (C0028).” https://attack.mitre.org/campaigns/C0028/
5. MITRE ATT&CK. “2016 Ukraine Electric Power Attack (C0025).” https://attack.mitre.org/campaigns/C0025/
6. MITRE ATT&CK. “2022 Ukraine Electric Power Attack (C0034).” https://attack.mitre.org/campaigns/C0034/
7. CISA. “AA22-054A: New Sandworm Malware Cyclops Blink Replaces VPNFilter.” (2022-02-23). https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-054a
8. CISA. “AR23-243A: Infamous Chisel Malware Analysis Report.” (2023-08-31). https://www.cisa.gov/news-events/analysis-reports/ar23-243a
9. NSA. “Government Agencies Report New Russian Malware Targets Ukrainian Military.” (2023-08-31). https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3511738/government-agencies-report-new-russian-malware-targets-ukrainian-military/
10. ESET. “Industroyer2: Industroyer reloaded.” (2022-04-12). https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/
11. Microsoft Threat Intelligence. “The BadPilot campaign: Seashell Blizzard subgroup conducts multiyear global access operation.” (2025-02-12). https://www.microsoft.com/en-us/security/blog/2025/02/12/the-badpilot-campaign-seashell-blizzard-subgroup-conducts-multiyear-global-access-operation/
---
