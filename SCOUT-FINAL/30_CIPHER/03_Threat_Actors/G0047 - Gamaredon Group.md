---
entity_type: threat_actor
actor_name: "Gamaredon Group"
common_name: "Gamaredon Group"
actor_id: "G0047"
actor_type: "Russia-linked cyber espionage threat group focused primarily on Ukrainian government and related entities (reported)"
aliases: ["Shuckworm","Armageddon","Primitive Bear","IRON TILDEN","ACTINIUM","DEV-0157","Aqua Blizzard"]
country_of_origin: "Russia"
suspected_sponsors: ["Russian Federal Security Service (FSB) Center 18"]
attribution_confidence: "High"
first_seen: "2013-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Collect sensitive information from Ukrainian government and related sectors (reported)","Maintain access via repeated reinfection and high-volume spearphishing (reported)","Spread within target environments via shared content, removable media, and document/template abuse (reported)","Operate resilient C2 using frequently changing infrastructure and third-party services (reported)"]
victimology_summary: "Gamaredon Group (MITRE ATT&CK G0047) is a suspected Russian cyber espionage actor assessed active since at least 2013 and heavily focused on Ukraine, including government, military, law enforcement, judiciary, NGOs, and non-profits. Public reporting notes Ukrainian government attribution of Gamaredon activity to Russia’s FSB Center 18 (operating out of occupied Crimea) and multiple vendors describe persistent, noisy operations characterized by spearphishing at scale, frequent tool iteration/obfuscation, and resilient infrastructure patterns."
target_sectors: ["Government","Military","Law enforcement","Judiciary","Non-profit","NGO","Public administration"]
target_regions: ["Ukraine","NATO-related entities (reported, limited attempts)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Pteranodon]]","[[30_CIPHER/05_Malware/PowerPunch]]","[[30_CIPHER/05_Malware/QuietSieve]]","[[30_CIPHER/05_Malware/Remcos]]"]
tools: ["[[30_CIPHER/05_Malware/Reg]]","[[30_CIPHER/05_Malware/Ping]]"]
infrastructure: ["[[Fast flux DNS]]","[[Dynamic DNS]]","[[Cloudflare tunnels]]","[[Telegram/Telegraph-based resolution]]","[[GitHub-hosted staging]]","[[Non-standard ports]]","[[Domain churn]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]","[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1102 - Web Service]]","[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]","[[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1221 - Template Injection]]","[[20_Entities/07_TTPs/T1534 - Internal Spearphishing]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1112 - Modify Registry]]","[[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]","[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]","[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]","[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1119 - Automated Collection]]","[[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1005 - Data from Local System]]","[[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive]]","[[20_Entities/07_TTPs/T1025 - Data from Removable Media]]","[[20_Entities/07_TTPs/T1568 - Dynamic Resolution]]","[[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]","[[20_Entities/07_TTPs/T1571 - Non-Standard Port]]","[[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]]","[[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta]]","[[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]","[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]","[[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]","[[20_Entities/07_TTPs/T1480 - Execution Guardrails]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Gamaredon Group (G0047) (Last Modified 2025-10-24): https://attack.mitre.org/groups/G0047/","Microsoft Security Blog — ACTINIUM targets Ukrainian organizations (2022-02-04): https://www.microsoft.com/en-us/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/","ESET Research — Cyberespionage the Gamaredon way (white paper PDF) (2024-09-26): https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf","Palo Alto Networks Unit 42 — Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine (2022-12-20): https://unit42.paloaltonetworks.com/gamaredon-trident-ursa/","VMware Carbon Black / Symantec Threat Hunter Team — Shuckworm Targets Foreign Military Mission Based in Ukraine (2025-04-10): https://www.security.com/threat-intelligence/shuckworm-targets-foreign-military-mission-ukraine","Cisco Talos — Gamaredon campaign abuses LNK files to distribute Remcos backdoor (2025-03-28): https://blog.talosintelligence.com/gamaredon-lnk-remcos/"]
tags: ["threat-actor","gamaredon","g0047","russia-nexus","cyber-espionage","ukraine","shuckworm","armageddon"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Gamaredon Group

## 1. BLUF / Executive Summary
Gamaredon Group (**G0047**) is a Russia-linked cyber espionage threat actor primarily associated with long-running, high-volume operations against **Ukrainian government and related entities** since at least **2013**. Public reporting cites **Ukrainian government attribution** to Russia’s **FSB Center 18**, and multiple vendors describe the actor as persistent and operationally “noisy,” with rapid tool iteration/obfuscation and resilient C2/infrastructure practices.

## 2. Attribution Notes
- MITRE ATT&CK tracks the cluster as **Gamaredon Group (G0047)** and documents sustained Ukraine-focused targeting and a broad TTP set.
- Microsoft (tracking as **ACTINIUM / DEV-0157**, later mapped into its naming taxonomy) describes consistent targeting of Ukrainian organizations and notes public Ukrainian attribution to the FSB.
- ESET reporting aligns the cluster to SSU attribution (FSB Center 18) and characterizes sustained activity with extensive tool churn and infrastructure resilience.

## 3. Motivations & Objectives
- **Primary motivation:** espionage-driven intelligence collection.
- **Objectives (reported):** gain and maintain access to Ukrainian governmental environments; spread via internal targeting and shared content; automate collection and exfiltration; sustain C2 through infrastructure churn and third-party services.

## 4. Targeting Profile
- **Primary:** Ukrainian governmental institutions and adjacent sectors (military, law enforcement, judiciary, NGOs).
- **Secondary (reported/episodic):** limited attempts against NATO-related government institutions (reported in vendor research), with Ukraine remaining the dominant focus.

## 5. Tradecraft Overview
- **Spearphishing at scale** with user-driven execution and attachment/lure workflows ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]).
- **Document/template abuse and propagation** via macro/template mechanisms and shared content dynamics ([[20_Entities/07_TTPs/T1221 - Template Injection]]; [[20_Entities/07_TTPs/T1534 - Internal Spearphishing]]).
- **Script-heavy post-compromise tradecraft** emphasizing PowerShell/VB/command shell ([[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]; [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]).
- **Persistence & host modifications** including registry-based persistence and scheduled tasks ([[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]; [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]).
- **C2 resilience** using domain churn, dynamic resolution and fast-flux patterns, and leveraging web services/third parties ([[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]; [[20_Entities/07_TTPs/T1102 - Web Service]]).
- **Automated collection/exfiltration** behaviors documented in ATT&CK mapping ([[20_Entities/07_TTPs/T1119 - Automated Collection]]; [[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]).

## 6. MITRE ATT&CK Mapping
- Resource Development / Infrastructure
  - [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
  - [[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]
  - [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]
- Initial Access / Execution
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
  - [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
  - [[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta]]
  - [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]
- Persistence / Defense Evasion / Discovery
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
  - [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
  - [[20_Entities/07_TTPs/T1112 - Modify Registry]]
  - [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]
  - [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
  - [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]
  - [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]
  - [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
  - [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]
  - [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- Collection / Exfiltration
  - [[20_Entities/07_TTPs/T1119 - Automated Collection]]
  - [[20_Entities/07_TTPs/T1005 - Data from Local System]]
  - [[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive]]
  - [[20_Entities/07_TTPs/T1025 - Data from Removable Media]]
  - [[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]
  - [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- Command and Control
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1102 - Web Service]]
  - [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]
  - [[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]
  - [[20_Entities/07_TTPs/T1568 - Dynamic Resolution]]
  - [[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]
  - [[20_Entities/07_TTPs/T1571 - Non-Standard Port]]
  - [[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol]]
  - [[20_Entities/07_TTPs/T1480 - Execution Guardrails]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
  - [[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]

## 7. Malware & Tools Used
- Primary malware/tooling families noted in MITRE and major vendor reporting:
  - [[30_CIPHER/05_Malware/Pteranodon]] (MITRE software associated with Gamaredon)
  - [[30_CIPHER/05_Malware/PowerPunch]] (MITRE software associated with Gamaredon)
  - [[30_CIPHER/05_Malware/QuietSieve]] (MITRE software associated with Gamaredon)
  - [[30_CIPHER/05_Malware/Remcos]] (commodity RAT observed in Gamaredon-associated activity in MITRE mapping)
- Common utilities referenced in MITRE mapping (legitimate binaries used as part of activity):
  - [[30_CIPHER/05_Malware/Reg]]
  - [[30_CIPHER/05_Malware/Ping]]

## 8. Infrastructure Patterns
- [[Domain churn]] with recurring registration/rotation for staging and C2.
- [[Dynamic DNS]] and [[Fast flux DNS]] patterns used to complicate blocking and tracking.
- [[Cloudflare tunnels]] / web-service-mediated C2 acquisition and shielding (reported in MITRE technique notes and vendor reporting).
- [[Telegram/Telegraph-based resolution]] where third-party content is used to reveal or retrieve C2 endpoints (reported in MITRE technique notes).
- [[GitHub-hosted staging]] and similar third-party web service usage for payload hosting or staging (reported in MITRE technique notes).
- [[Non-standard ports]] and mixed protocol choices for C2 (reported in MITRE technique notes).

## 9. Campaign History
- **2013+** — Widely reported start of sustained Ukraine-focused operations (MITRE; multiple vendors).
- **2021-11** — Public Ukrainian attribution of Gamaredon activity to **FSB Center 18** (as summarized by MITRE and vendors).
- **2022-02-04** — Microsoft publishes research on **ACTINIUM (Gamaredon)** targeting Ukrainian organizations and references Ukrainian attribution.
- **2022–2023** — ESET documents toolset evolution and multiple access/propagation pathways used during this period (white paper).
- **2025-03 / 2025-04** — Additional public reporting describes continued campaigns and evolving delivery of commodity tooling (e.g., Remcos) and operational adjustments.
- **2025-10-24** — MITRE ATT&CK entry for **G0047** updated (Last Modified date as posted by MITRE).

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Prioritize detection and response for **phishing-led access** and post-compromise **script execution** patterns consistent with Gamaredon’s documented tradecraft ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]).
- Treat **document/template abuse and internal propagation** as high-risk behaviors in Ukrainian-facing environments ([[20_Entities/07_TTPs/T1221 - Template Injection]]; [[20_Entities/07_TTPs/T1534 - Internal Spearphishing]]).
- Increase scrutiny for **registry-based persistence and configuration tampering** aligned to ATT&CK-mapped behaviors ([[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]; [[20_Entities/07_TTPs/T1112 - Modify Registry]]).
- Monitor for **C2 resilience indicators** such as dynamic resolution/fast-flux patterns and web-service-mediated C2 behaviors ([[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]; [[20_Entities/07_TTPs/T1102 - Web Service]]).
- Assume repeated intrusion attempts; operationally plan for **rapid reinfection** and high-frequency tooling changes as documented in multiple public sources.

## 12. Analyst Notes
- Gamaredon has extensive aliasing across vendors; anchoring to **G0047** reduces naming drift (e.g., Shuckworm, ACTINIUM, Primitive Bear).
- Public descriptions consistently emphasize **high operational tempo** and **frequent tool changes/obfuscation**, suggesting detection strategies should emphasize behavior over static signatures.
- Some reporting highlights third-party services (Cloudflare/Telegram/GitHub) in the actor’s operational patterns; interpret these as **tradecraft enablers** rather than unique identifiers.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Gamaredon Group (G0047): https://attack.mitre.org/groups/G0047/
- Microsoft Security Blog — ACTINIUM targets Ukrainian organizations (Gamaredon): https://www.microsoft.com/en-us/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/
- ESET (PDF) — Cyberespionage the Gamaredon way: https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf
- Unit 42 — Gamaredon/Trident Ursa reporting: https://unit42.paloaltonetworks.com/gamaredon-trident-ursa/
- Cisco Talos — Gamaredon LNK → Remcos reporting: https://blog.talosintelligence.com/gamaredon-lnk-remcos/

## 14. References
1. MITRE ATT&CK. “Gamaredon Group (G0047).” Last Modified 2025-10-24. https://attack.mitre.org/groups/G0047/
2. Microsoft Security Blog. “ACTINIUM targets Ukrainian organizations.” 2022-02-04. https://www.microsoft.com/en-us/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/
3. ESET Research (PDF). “Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023.” 2024-09-26. https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf
4. Palo Alto Networks Unit 42. “Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine.” 2022-12-20. https://unit42.paloaltonetworks.com/gamaredon-trident-ursa/
5. VMware Carbon Black / Symantec Threat Hunter Team. “Shuckworm Targets Foreign Military Mission Based in Ukraine.” 2025-04-10. https://www.security.com/threat-intelligence/shuckworm-targets-foreign-military-mission-ukraine
6. Cisco Talos. “Gamaredon campaign abuses LNK files to distribute Remcos backdoor.” 2025-03-28. https://blog.talosintelligence.com/gamaredon-lnk-remcos/
