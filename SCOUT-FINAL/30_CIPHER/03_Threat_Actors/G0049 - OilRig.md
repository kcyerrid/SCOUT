---
entity_type: threat_actor
actor_name: "OilRig"
common_name: "OilRig"
actor_id: "G0049"
actor_type: "Iran-linked cyber espionage threat group targeting Middle Eastern and international organizations (reported)"
aliases: ["APT34","Helix Kitten","Earth Simnavaz","COBALT GYPSY","IRN2","Evasive Serpens","Hazel Sandstorm","EUROPIUM","ITG13","Crambus","TA452"]
country_of_origin: "Iran"
suspected_sponsors: ["Iranian government"]
attribution_confidence: "High"
first_seen: "2014-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Collect sensitive information from targeted organizations (reported)","Establish durable access using script-heavy tooling and multiple persistence options (reported)","Leverage trusted relationships and compromise adjacent entities to reach primary targets (reported)","Maintain resilient C2 using DNS/HTTP and regularly refreshed infrastructure (reported)"]
victimology_summary: "OilRig (MITRE ATT&CK G0049) is a suspected Iranian threat group active since at least 2014 that has targeted Middle Eastern and international victims across sectors including financial, government, energy, chemical, and telecommunications. Public reporting and MITRE describe a campaign history that includes spearphishing and web-based lures, extensive scripting (PowerShell/VBS/batch), use of custom backdoors and downloaders, and at times exploitation of trusted relationships/supply-chain style access. Recent public reporting includes campaigns tracked as Outer Space (2021) and Juicy Mix (2022), with tooling that leverages cloud services and Exchange-related access paths."
target_sectors: ["Government","Financial services","Energy","Telecommunications","Chemical","Technology (reported)"]
target_regions: ["Middle East","International (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/BONDUPDATER]]","[[30_CIPHER/05_Malware/Helminth]]","[[30_CIPHER/05_Malware/POWRUNER]]","[[30_CIPHER/05_Malware/QUADAGENT]]","[[30_CIPHER/05_Malware/RGDoor]]","[[30_CIPHER/05_Malware/RDAT]]","[[30_CIPHER/05_Malware/PowerExchange]]","[[30_CIPHER/05_Malware/Mango]]","[[30_CIPHER/05_Malware/SideTwist]]","[[30_CIPHER/05_Malware/OopsIE]]","[[30_CIPHER/05_Malware/Solar]]","[[30_CIPHER/05_Malware/OilBooster]]","[[30_CIPHER/05_Malware/OilCheck]]","[[30_CIPHER/05_Malware/ODAgent]]","[[30_CIPHER/05_Malware/SEASHARPEE]]","[[30_CIPHER/05_Malware/SampleCheck5000]]","[[30_CIPHER/05_Malware/ISMInjector]]","[[30_CIPHER/05_Malware/ZeroCleare]]"]
tools: ["[[30_CIPHER/05_Malware/Mimikatz]]","[[30_CIPHER/05_Malware/LaZagne]]","[[30_CIPHER/05_Malware/PsExec]]","[[30_CIPHER/05_Malware/ngrok]]","[[30_CIPHER/05_Malware/certutil]]","[[30_CIPHER/05_Malware/Net]]","[[30_CIPHER/05_Malware/Reg]]","[[30_CIPHER/05_Malware/ftp]]","[[30_CIPHER/05_Malware/ipconfig]]","[[30_CIPHER/05_Malware/netstat]]","[[30_CIPHER/05_Malware/Systeminfo]]","[[30_CIPHER/05_Malware/Tasklist]]"]
infrastructure: ["[[Fake VPN portals]]","[[Conference registration lures]]","[[Job application lures]]","[[Domain and hosting churn]]","[[DNS-based C2]]","[[Web service C2]]","[[Exchange Web Services API abuse]]","[[Web shells]]","[[Cloud service-powered downloaders]]","[[Steganography-enabled C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]","[[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]","[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1110 - Brute Force]]","[[20_Entities/07_TTPs/T1115 - Clipboard Data]]","[[20_Entities/07_TTPs/T1119 - Automated Collection]]","[[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]","[[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]","[[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]","[[20_Entities/07_TTPs/T1505.004 - Server Software Component: IIS Components]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]","[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — OilRig (G0049) (Last Modified 2025-01-16): https://attack.mitre.org/groups/G0049/","ESET — OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes (2023-09-21): https://www.welivesecurity.com/2023/09/21/oilrig-outer-space-juicy-mix/","ESET — OilRig’s persistent attacks using cloud service-powered downloaders (2023-12-14): https://www.welivesecurity.com/2023/12/14/oilrig-persistent-attacks-cloud-service-powered-downloaders/","Trend Micro — Earth Simnavaz (aka APT34) Levies Advanced Cyberattacks Against Middle East (2024-10-11): https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html","Symantec Threat Hunter Team — Crambus: New Campaign Targets Middle Eastern Government (2023-10-19): https://www.security.com/threat-intelligence/crambus-middle-east-government","Check Point Research — Iran’s APT34 Returns with an Updated Arsenal (2021-04-08): https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/"]
tags: ["threat-actor","oilrig","g0049","iran-nexus","apt34","helix-kitten","cyber-espionage"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# OilRig

## 1. BLUF / Executive Summary
OilRig (**G0049**) is an Iran-linked cyber espionage threat actor active since at least **2014**, primarily associated with sustained operations in the **Middle East** with additional international targeting. Public reporting and MITRE describe recurring **spearphishing and web-lure** operations, extensive **PowerShell/VBScript/batch** usage, and a broad catalog of **custom malware** (downloaders, backdoors, and web-based implants). Recent public reporting includes campaigns **Outer Space (2021)** and **Juicy Mix (2022)** that highlight continued evolution of tooling and infrastructure, including cloud service–powered components.

## 2. Attribution Notes
- MITRE ATT&CK tracks the activity cluster as **OilRig (G0049)** and states it is suspected to work on behalf of the **Iranian government**, citing infrastructure and targeting alignment.
- Public tracking has historically split or labeled overlapping activity as **APT34** and **OilRig**; MITRE notes consolidation due to higher-confidence overlap.
- Multiple vendors track related subclusters/overlaps under different names (e.g., **Helix Kitten**, **Earth Simnavaz**, **Crambus**, **Hazel Sandstorm/EUROPIUM**), and naming can reflect vendor-specific clustering rather than strict separations.

## 3. Motivations & Objectives
- **Primary motivation:** espionage.
- **Objectives (reported):**
  - Collect sensitive information from targeted organizations (government and commercially sensitive sectors).
  - Establish repeatable access paths via email compromise, phishing, and credential theft.
  - Use trusted relationships and compromised infrastructure to reach higher-value targets.
  - Maintain resilient command-and-control using DNS/HTTP and refreshed infrastructure.

## 4. Targeting Profile
- **Geographic focus:** Middle East; additional international targeting reported.
- **Sectors (MITRE-reported):** financial, government, energy, chemical, telecommunications; technology/service providers have also appeared in reporting.
- **Victim type patterns:** organizations with strategic, governmental, or commercially sensitive information; environments where email and web infrastructure provide durable footholds.

## 5. Tradecraft Overview
- **Initial access:** spearphishing attachments and malicious links, including macro-enabled documents requiring user interaction ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]).
- **Credential and account-focused access:** compromise of email accounts used to facilitate follow-on phishing and internal access expansion ([[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]; [[20_Entities/07_TTPs/T1078 - Valid Accounts]]).
- **Execution style:** script-heavy workflows leveraging PowerShell, Windows command shell, and VBScript for staging and execution ([[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]; [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]).
- **C2 and infrastructure:** use of HTTP/DNS for command and control and frequent domain/infrastructure changes ([[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]; [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]).
- **Server-side footholds:** use of server component abuse patterns (IIS components/web shells) and Exchange-adjacent access paths reported in recent research ([[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]; [[20_Entities/07_TTPs/T1505.004 - Server Software Component: IIS Components]]).
- **Collection:** automated and browser-focused collection behaviors appear in modern campaign reporting ([[20_Entities/07_TTPs/T1119 - Automated Collection]]; [[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]).

## 6. MITRE ATT&CK Mapping
- Resource Development / Infrastructure
  - [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
  - [[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]]
- Initial Access / User Execution
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
  - [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- Execution
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
  - [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
- Persistence / Tasking
  - [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- Credential / Account Operations
  - [[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
  - [[20_Entities/07_TTPs/T1110 - Brute Force]]
- Discovery / Collection
  - [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]
  - [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
  - [[20_Entities/07_TTPs/T1115 - Clipboard Data]]
  - [[20_Entities/07_TTPs/T1119 - Automated Collection]]
  - [[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]
- Command and Control
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- Server-side Operations
  - [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]
  - [[20_Entities/07_TTPs/T1505.004 - Server Software Component: IIS Components]]
- Obfuscation
  - [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]

## 7. Malware & Tools Used
- Commonly cited custom malware families in OilRig reporting (MITRE and vendor reporting):
  - [[30_CIPHER/05_Malware/BONDUPDATER]]
  - [[30_CIPHER/05_Malware/Helminth]]
  - [[30_CIPHER/05_Malware/POWRUNER]]
  - [[30_CIPHER/05_Malware/QUADAGENT]]
  - [[30_CIPHER/05_Malware/RGDoor]]
  - [[30_CIPHER/05_Malware/RDAT]]
  - [[30_CIPHER/05_Malware/PowerExchange]]
  - [[30_CIPHER/05_Malware/Mango]]
  - [[30_CIPHER/05_Malware/SideTwist]]
  - [[30_CIPHER/05_Malware/OopsIE]]
  - [[30_CIPHER/05_Malware/Solar]]
  - [[30_CIPHER/05_Malware/OilBooster]]
  - [[30_CIPHER/05_Malware/OilCheck]]
  - [[30_CIPHER/05_Malware/ODAgent]]
  - [[30_CIPHER/05_Malware/SEASHARPEE]]
  - [[30_CIPHER/05_Malware/SampleCheck5000]]
  - [[30_CIPHER/05_Malware/ISMInjector]]
- Dual-use utilities and commercial tooling observed in OilRig intrusions (MITRE-reported):
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/LaZagne]]
  - [[30_CIPHER/05_Malware/PsExec]]
  - [[30_CIPHER/05_Malware/ngrok]]
  - [[30_CIPHER/05_Malware/certutil]]
  - [[30_CIPHER/05_Malware/Net]]
  - [[30_CIPHER/05_Malware/Reg]]
  - [[30_CIPHER/05_Malware/ftp]]
- Destructive collaboration noted in public reporting:
  - [[30_CIPHER/05_Malware/ZeroCleare]] (OilRig reported as collaborating on the destructive component in at least one incident described by MITRE-linked sources)

## 8. Infrastructure Patterns
- [[Fake VPN portals]] and similar credential-harvesting sites; also [[Conference registration lures]] and [[Job application lures]] used to attract victim interaction.
- [[Domain and hosting churn]] consistent with repeated campaign refresh cycles and infrastructure replacement.
- Mixed C2 channels: [[DNS-based C2]] and [[Web service C2]] appear in reporting.
- Server-side enablement patterns including [[Web shells]] and IIS-related components (reported).
- Modern delivery and staging described as [[Cloud service-powered downloaders]] in recent campaign reporting.
- Tradecraft that includes [[Steganography-enabled C2]] has been reported in OilRig-associated tooling.

## 9. Campaign History
- **2014+** — MITRE reports OilRig targeting Middle Eastern and international victims since at least 2014 across multiple strategic sectors.
- **2016–2018** — Public vendor reporting describes recurring spearphishing, custom backdoors, and evolving toolsets (referenced by MITRE).
- **2021 (Outer Space)** — Campaign tracked in public reporting and referenced by MITRE; highlights continued script-based delivery and C2 over web protocols.
- **2022 (Juicy Mix)** — Campaign tracked in public reporting and referenced by MITRE; associated with updated tooling and data-stealing components.
- **2023–2024** — Additional public reporting describes continued evolution, including cloud-service-powered components and Exchange-adjacent activity in some reporting.
- **2025-01-16** — MITRE ATT&CK entry for **OilRig (G0049)** updated (Last Modified date as posted by MITRE).

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Emphasize controls and detections for phishing-led access and user execution behaviors ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]).
- Monitor for script-heavy execution and suspicious scripting interpreter usage aligned to OilRig tradecraft ([[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]; [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]).
- Prioritize detection for DNS/HTTP-based C2 patterns and suspicious ingress tool transfer behaviors ([[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]; [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]).
- Harden and monitor internet-facing server components and email/web infrastructure where applicable, including web-shell and IIS component abuse patterns ([[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]; [[20_Entities/07_TTPs/T1505.004 - Server Software Component: IIS Components]]).
- Treat account compromise as a central risk: strengthen protections for email accounts and watch for anomalous login and account usage patterns ([[20_Entities/07_TTPs/T1586.002 - Compromise Accounts: Email Accounts]]; [[20_Entities/07_TTPs/T1078 - Valid Accounts]]).

## 12. Analyst Notes
- Naming varies widely across vendors; anchor this profile to **MITRE G0049** to reduce drift across aliases and subcluster labels.
- OilRig reporting spans multiple years and tool generations; incident scoping should identify which campaign era (e.g., 2016–2018 vs. Outer Space/Juicy Mix) best matches observed behavior.
- Some reporting ties OilRig to destructive operations via collaboration (e.g., ZeroCleare). Treat destructive capability/intent as context-dependent and avoid overgeneralizing across all OilRig activity.

## 13. Further Reading / External Resources
- MITRE ATT&CK — OilRig (G0049): https://attack.mitre.org/groups/G0049/
- ESET — OilRig’s Outer Space and Juicy Mix: https://www.welivesecurity.com/2023/09/21/oilrig-outer-space-juicy-mix/
- ESET — OilRig’s persistent attacks using cloud service-powered downloaders: https://www.welivesecurity.com/2023/12/14/oilrig-persistent-attacks-cloud-service-powered-downloaders/
- Trend Micro — Earth Simnavaz / OilRig reporting: https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html
- Symantec Threat Hunter Team — Crambus campaign reporting: https://www.security.com/threat-intelligence/crambus-middle-east-government
- Check Point Research — APT34 updated arsenal: https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/

## 14. References
1. MITRE ATT&CK. “OilRig (G0049).” Last Modified 2025-01-16. https://attack.mitre.org/groups/G0049/
2. ESET. “OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes.” 2023-09-21. https://www.welivesecurity.com/2023/09/21/oilrig-outer-space-juicy-mix/
3. ESET. “OilRig’s persistent attacks using cloud service-powered downloaders.” 2023-12-14. https://www.welivesecurity.com/2023/12/14/oilrig-persistent-attacks-cloud-service-powered-downloaders/
4. Trend Micro. “Earth Simnavaz (aka APT34) Levies Advanced Cyberattacks Against Middle East.” 2024-10-11. https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html
5. Symantec Threat Hunter Team. “Crambus: New Campaign Targets Middle Eastern Government.” 2023-10-19. https://www.security.com/threat-intelligence/crambus-middle-east-government
6. Check Point Research. “Iran’s APT34 Returns with an Updated Arsenal.” 2021-04-08. https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/
