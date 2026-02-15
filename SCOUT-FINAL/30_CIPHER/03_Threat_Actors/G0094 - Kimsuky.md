---
entity_type: threat_actor
actor_name: "Kimsuky"
common_name: "Kimsuky"
actor_id: "G0094"
actor_type: "State-linked (cyber espionage)"
aliases:
  - "Black Banshee"
  - "Velvet Chollima"
  - "Emerald Sleet"
  - "THALLIUM"
  - "APT43"
  - "TA427"
  - "Springtail"
country_of_origin: "North Korea"
suspected_sponsors:
  - "North Korea (DPRK)"
attribution_confidence: "High"
first_seen: "2012-01-01"
last_seen: ""
status: "Active"

motivations:
  - "Espionage"
objectives:
  - "Information theft and strategic intelligence collection"
  - "Credential theft and email collection"
victimology_summary: "North Korea-based cyber espionage group active since at least 2012; has targeted South Korean government entities, think tanks, and individuals, and conducted campaigns against organizations in the US, Japan, Russia, Europe, and South Korea."
target_sectors: []
target_regions:
  - "South Korea"
  - "United States"
  - "Japan"
  - "Russia"
  - "Europe"

related_groups:
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]"

malware:
  - "[[30_CIPHER/05_Malware/S1025 - Amadey|Amadey]]"
  - "[[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed]]"
  - "[[30_CIPHER/05_Malware/S0414 - BabyShark|BabyShark]]"
  - "[[30_CIPHER/05_Malware/S0252 - Brave Prince|Brave Prince]]"
  - "[[30_CIPHER/05_Malware/S0527 - CSPY Downloader|CSPY Downloader]]"
  - "[[30_CIPHER/05_Malware/S0032 - gh0st RAT|gh0st RAT]]"
  - "[[30_CIPHER/05_Malware/S1197 - GoBear|GoBear]]"
  - "[[30_CIPHER/05_Malware/S0249 - Gold Dragon|Gold Dragon]]"
  - "[[30_CIPHER/05_Malware/S1198 - Gomir|Gomir]]"
  - "[[30_CIPHER/05_Malware/S0526 - KGH_SPY|KGH_SPY]]"
  - "[[30_CIPHER/05_Malware/S0353 - NOKKI|NOKKI]]"
  - "[[30_CIPHER/05_Malware/S0262 - QuasarRAT|QuasarRAT]]"
  - "[[30_CIPHER/05_Malware/S1196 - Troll Stealer|Troll Stealer]]"
tools:
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]"

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1583 - Acquire Infrastructure|T1583]]"
  - "[[20_Entities/07_TTPs/T1102.001 - Dead Drop Resolver|T1102.001]]"
  - "[[20_Entities/07_TTPs/T1557 - Adversary-in-the-Middle|T1557]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001]]"
  - "[[20_Entities/07_TTPs/T1071.002 - File Transfer Protocols|T1071.002]]"
  - "[[20_Entities/07_TTPs/T1071.003 - Mail Protocols|T1071.003]]"
  - "[[20_Entities/07_TTPs/T1547.001 - Registry Run Keys - Startup Folder|T1547.001]]"
  - "[[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001]]"
  - "[[20_Entities/07_TTPs/T1185 - Browser Session Hijacking|T1185]]"
  - "[[20_Entities/07_TTPs/T1555.003 - Credentials from Web Browsers|T1555.003]]"
  - "[[20_Entities/07_TTPs/T1114.002 - Remote Email Collection|T1114.002]]"

notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0094/"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a"
tags:
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0094"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Kimsuky (G0094) is a **North Korea-based** cyber espionage group active since at least **2012**, linked to multiple long-running campaigns and ongoing collection operations targeting South Korea and international entities. ATT&CK notes that in **2023** the group was observed using **commercial large language models** to assist with research, scripting, and social engineering.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0094
- **Associated names/clusters:** Black Banshee, Velvet Chollima, Emerald Sleet, THALLIUM, APT43, TA427, Springtail
- **Related grouping note in ATT&CK reporting:** Some researchers have grouped Kimsuky under broader DPRK umbrellas (e.g., [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]).
- **Confidence:** High (ATT&CK describes the group as North Korea-based).

## 3. Motivations & Objectives
- **Motivation:** Espionage.
- **Objectives:** Information theft (documents), credential theft, email collection, and sustained access to enable ongoing collection.

## 4. Targeting Profile
- **Primary targeting:** South Korean government entities, think tanks, and subject matter experts.
- **Additional targeting:** Organizations in the US, Japan, Russia, Europe, and South Korea.

## 5. Tradecraft Overview
Common behaviors reflected in ATT&CK technique examples:
- **Infrastructure acquisition** (domains, servers, web services) including spoofing targeted/trusted organizations.
- **Spearphishing and social engineering** with attachment-based lures and tailored filenames/extensions (including LNK lure examples in ATT&CK).
- **Web-service abuse** (dead drop resolvers; bidirectional comms via public platforms) and use of cloud services for hosting and exfil.
- **Credential access** via browser credential theft and session hijacking techniques.
- **Persistence** via Run keys/startup folder and service creation.
- **Email collection** and remote email access via IMAP-capable tooling (as described in ATT&CK).
- **Archive & encryption prior to exfil** (utility-based archiving; custom encryption noted in examples).
- **Operator enablement** noted in ATT&CK: observed using commercial LLMs for research/scripting/social engineering.

## 6. MITRE ATT&CK Mapping (Key TTPs)
- [[20_Entities/07_TTPs/T1583 - Acquire Infrastructure|T1583]] — Domains/servers/web services acquired for operations.
- [[20_Entities/07_TTPs/T1102.001 - Dead Drop Resolver|T1102.001]] — Retrieval of tasks/configs from public content sources.
- [[20_Entities/07_TTPs/T1557 - Adversary-in-the-Middle|T1557]] — Modified proxy tooling to inspect victim web traffic.
- [[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001]] — HTTP-based C2 patterns.
- [[20_Entities/07_TTPs/T1071.002 - File Transfer Protocols|T1071.002]] — FTP used for malware download in ATT&CK examples.
- [[20_Entities/07_TTPs/T1071.003 - Mail Protocols|T1071.003]] — Email used for exfil/C2 behaviors (ATT&CK examples).
- [[20_Entities/07_TTPs/T1547.001 - Registry Run Keys - Startup Folder|T1547.001]] — Persistence via autostart.
- [[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001]] — Execution and automation (including Invoke-Mimikatz usage in ATT&CK examples).
- [[20_Entities/07_TTPs/T1185 - Browser Session Hijacking|T1185]] — Session theft/form grabbing described in ATT&CK.
- [[20_Entities/07_TTPs/T1555.003 - Credentials from Web Browsers|T1555.003]] — Browser credential theft (extensions + password dumping tools in examples).
- [[20_Entities/07_TTPs/T1114.002 - Remote Email Collection|T1114.002]] — Mail crawling and IMAP collection tooling.

## 7. Malware & Tools Used
- Malware (ATT&CK Software mappings):
  - [[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed]]
  - [[30_CIPHER/05_Malware/S0414 - BabyShark|BabyShark]]
  - [[30_CIPHER/05_Malware/S0252 - Brave Prince|Brave Prince]]
  - [[30_CIPHER/05_Malware/S0527 - CSPY Downloader|CSPY Downloader]]
  - [[30_CIPHER/05_Malware/S0032 - gh0st RAT|gh0st RAT]]
  - [[30_CIPHER/05_Malware/S1197 - GoBear|GoBear]]
  - [[30_CIPHER/05_Malware/S0249 - Gold Dragon|Gold Dragon]]
  - [[30_CIPHER/05_Malware/S1198 - Gomir|Gomir]]
  - [[30_CIPHER/05_Malware/S0526 - KGH_SPY|KGH_SPY]]
  - [[30_CIPHER/05_Malware/S0353 - NOKKI|NOKKI]]
  - [[30_CIPHER/05_Malware/S0262 - QuasarRAT|QuasarRAT]]
  - [[30_CIPHER/05_Malware/S1196 - Troll Stealer|Troll Stealer]]
  - [[30_CIPHER/05_Malware/S1025 - Amadey|Amadey]]
- Tools:
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]
  - [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]

## 8. Infrastructure Patterns
- Use of **public web services** (blogs, repositories) as dead drops and C2 adjuncts.
- Cloud storage leveraged for payload hosting and data upload/download.
- Domain spoofing of trusted entities and services.

## 9. Campaign History
ATT&CK highlights multiple notable campaigns (including operations in 2018–2019) and continuing evolution, with 2023 observations including the use of commercial LLMs in support roles.

## 10. Known Indicators
- Treat IOCs as campaign-specific; prioritize behaviors:
  - Lookalike/spoofed domains and targeting infrastructure acquisition patterns.
  - Browser extension anomalies and credential theft indicators.
  - Unusual outbound HTTP/FTP/mail traffic from hosts not expected to use those channels.
  - Archive/encryption staging before exfil; suspicious utility usage in user context.

## 11. Defensive Recommendations
- Email security: isolate risky attachment formats; enforce link rewriting/detonation; train for tailored lure patterns.
- Browser controls: restrict extensions via policy; monitor extension installs; audit credential store access.
- Network controls: restrict outbound FTP/mail from endpoints; monitor to public blog/repo platforms for C2-like patterns.
- Endpoint controls: PowerShell logging and constrained execution; detect persistence via Run keys and suspicious service creation.
- Data protection: monitor for rapid document harvesting and staging directories; DLP alerts on exfil channels.

## 12. Analyst Notes
- High-signal detection opportunities: **web-service dead drops**, **AitM proxying**, and **browser credential/session theft**.
- Track “benign” cloud/web platforms used as operational infrastructure; false positives can be controlled with allowlists + context.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0094/
- CISA Alert (referenced in ATT&CK): https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a

## 14. References
- MITRE ATT&CK. (n.d.). *Kimsuky (G0094).* https://attack.mitre.org/groups/G0094/
- CISA, FBI, & CNMF. (2020, October 27). *AA20-301A: North Korean state-sponsored cyber actors use social engineering techniques to gain initial access.* https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a
