---
entity_type: "threat_actor"
actor_name: "Ke3chang"
common_name: "Ke3chang"
actor_id: "G0004"
actor_type: "Nation-state / cyber espionage (attributed)"
aliases: ["APT15", "Mirage", "Vixen Panda", "GREF", "Playful Dragon", "RoyalAPT", "NICKEL", "Nylon Typhoon"]
country_of_origin: "China (attributed)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2010-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Strategic intelligence collection", "Diplomatic intelligence collection", "Long-term access and persistence"]
victimology_summary: "MITRE ATT&CK describes Ke3chang as a China-attributed espionage group targeting oil, government, diplomatic, military, and NGO entities across Central/South America, the Caribbean, Europe, and North America since at least 2010."
target_sectors: ["Oil and Gas", "Government", "Diplomatic", "Military", "Non-Governmental Organizations (NGOs)"]
target_regions: ["Central America", "South America", "Caribbean", "Europe", "North America"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/MirageFox]]", "[[30_CIPHER/05_Malware/Neoichor]]", "[[30_CIPHER/05_Malware/Okrum]]"]
tools: ["[[30_CIPHER/05_Malware/Mimikatz]]", "[[30_CIPHER/05_Malware/spwebmember]]", "[[30_CIPHER/05_Malware/Net]]", "[[30_CIPHER/05_Malware/ipconfig]]", "[[30_CIPHER/05_Malware/netstat]]", "[[30_CIPHER/05_Malware/Ping]]", "[[30_CIPHER/05_Malware/Systeminfo]]", "[[30_CIPHER/05_Malware/Tasklist]]"]
infrastructure: ["[[Operational Relay Box Network]]", "[[ORB Network]]", "[[Virtual Private Server]]", "[[Multi-hop Proxy]]", "[[Botnet Relay]]", "[[HTTP C2]]", "[[DNS C2]]", "[[VPN Access]]", "[[Stolen VPN Certificates]]", "[[Microsoft Exchange]]", "[[Microsoft SharePoint]]", "[[Windows Admin Shares]]"]
ttps: ["[[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]", "[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]", "[[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]", "[[20_Entities/07_TTPs/T1583.005 - Acquire Infrastructure: Botnet]]", "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]", "[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]", "[[20_Entities/07_TTPs/T1560 - Archive Collected Data]]", "[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]", "[[20_Entities/07_TTPs/T1119 - Automated Collection]]", "[[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]", "[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]", "[[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]]", "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]", "[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]", "[[20_Entities/07_TTPs/T1213.002 - Data from Information Repositories: Sharepoint]]", "[[20_Entities/07_TTPs/T1005 - Data from Local System]]", "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]", "[[20_Entities/07_TTPs/T1587.001 - Develop Capabilities: Malware]]", "[[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]", "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]", "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]", "[[20_Entities/07_TTPs/T1133 - External Remote Services]]", "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]", "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]", "[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]", "[[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override]]", "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]", "[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]", "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]", "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]", "[[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]", "[[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]", "[[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]", "[[20_Entities/07_TTPs/T1069.002 - Permission Groups Discovery: Domain Groups]]", "[[20_Entities/07_TTPs/T1057 - Process Discovery]]", "[[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]", "[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]", "[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]", "[[20_Entities/07_TTPs/T1558.001 - Steal or Forge Kerberos Tickets: Golden Ticket]]", "[[20_Entities/07_TTPs/T1082 - System Information Discovery]]", "[[20_Entities/07_TTPs/T1614.001 - System Location Discovery: System Language Discovery]]", "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]", "[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]", "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]", "[[20_Entities/07_TTPs/T1007 - System Service Discovery]]", "[[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]", "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]", "[[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0004): Ke3chang (last modified 2025-04-04)","Mandiant (2014-11-12): OPERATION 'KE3CHANG' — Targeted Attacks Against Ministries of Foreign Affairs","Microsoft MSTIC (2021-12-06): NICKEL targeting government organizations across Latin America and Europe","ESET WeLiveSecurity (2019-07-18): Okrum—Ke3chang group targets diplomatic missions","Google Cloud (2024-05-22): ORB networks used by China-nexus actors (SPACEHOP Activity context)"]
tags: ["threat-actor", "apt", "china", "cyber-espionage", "ke3chang", "apt15", "nickel", "nylon-typhoon", "mitre-g0004"]
---

# Ke3chang

## 1. BLUF / Executive Summary
Ke3chang (MITRE ATT&CK **G0004**) is a China-attributed cyber espionage threat group assessed in public reporting as active since at least 2010, with targeting that includes oil, government, diplomatic, military, and NGO entities across Central/South America, the Caribbean, Europe, and North America. Public reporting and ATT&CK documentation associate Ke3chang with a mix of credential theft, long-term persistence, and multiple malware families such as [[30_CIPHER/05_Malware/Neoichor]], [[30_CIPHER/05_Malware/MirageFox]], and [[30_CIPHER/05_Malware/Okrum]].

## 2. Attribution Notes
- MITRE ATT&CK attributes Ke3chang to actors operating out of China and maps multiple associated tracking names including APT15, Mirage, Vixen Panda, NICKEL, and Nylon Typhoon.
- Naming/cluster overlap across vendors is common for this ecosystem; attribution should be grounded in convergent evidence (victimology + TTPs + malware/infrastructure), not aliases alone.
- ATT&CK also links a campaign entry (“SPACEHOP Activity”) to Ke3chang, with reporting describing ORB-style relay infrastructure and activity observed through at least May 2024.

## 3. Motivations & Objectives
- **Motivation:** Strategic intelligence collection aligned with cyber espionage.
- **Objectives (reported):** Access to diplomatic/government information, sensitive operational data, and long-term footholds for ongoing collection.

## 4. Targeting Profile
- **Sectors (reported):** Oil, government, diplomatic entities (including foreign affairs), military organizations, and NGOs.
- **Regions (reported):** Central/South America, the Caribbean, Europe, and North America; Microsoft reporting also emphasizes government targeting in Latin America and Europe under the NICKEL designation.

## 5. Tradecraft Overview
- **Initial access & expansion:** Public-facing application exploitation (including [[Microsoft Exchange]] and [[Microsoft SharePoint]]) consistent with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]] and follow-on access via [[VPN Access]] with compromised accounts and [[Stolen VPN Certificates]] (reported).
- **Collection & exfiltration patterns:** Scheduled collection and exfiltration behaviors consistent with [[20_Entities/07_TTPs/T1119 - Automated Collection]] and [[20_Entities/07_TTPs/T1020 - Automated Exfiltration]], with compression/encryption prior to transfer (reported) consistent with [[20_Entities/07_TTPs/T1560 - Archive Collected Data]] and [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]].
- **Credential access & lateral movement:** Credential dumping (including use of [[30_CIPHER/05_Malware/Mimikatz]]) consistent with the [[20_Entities/07_TTPs/T1003.* - OS Credential Dumping]] family; lateral movement via [[Windows Admin Shares]] consistent with [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]].
- **C2 & relay:** Use of [[HTTP C2]] and [[DNS C2]] is documented; ATT&CK also describes chains of compromised network devices and multi-hop relays consistent with [[Operational Relay Box Network]] / [[ORB Network]] and [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server]]
- [[20_Entities/07_TTPs/T1583.005 - Acquire Infrastructure: Botnet]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
- [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1119 - Automated Collection]]
- [[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
- [[20_Entities/07_TTPs/T1213.002 - Data from Information Repositories: Sharepoint]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1587.001 - Develop Capabilities: Malware]]
- [[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]
- [[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]
- [[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]
- [[20_Entities/07_TTPs/T1069.002 - Permission Groups Discovery: Domain Groups]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1558.001 - Steal or Forge Kerberos Tickets: Golden Ticket]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1614.001 - System Location Discovery: System Language Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1007 - System Service Discovery]]
- [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]]

## 7. Malware & Tools Used
- **Malware (ATT&CK software associated with Ke3chang):**
  - [[30_CIPHER/05_Malware/MirageFox]]
  - [[30_CIPHER/05_Malware/Neoichor]]
  - [[30_CIPHER/05_Malware/Okrum]]
- **Tools (ATT&CK software associated with Ke3chang, including built-ins and third-party utilities):**
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/spwebmember]]
  - [[30_CIPHER/05_Malware/Net]]
  - [[30_CIPHER/05_Malware/ipconfig]]
  - [[30_CIPHER/05_Malware/netstat]]
  - [[30_CIPHER/05_Malware/Ping]]
  - [[30_CIPHER/05_Malware/Systeminfo]]
  - [[30_CIPHER/05_Malware/Tasklist]]

## 8. Infrastructure Patterns
- Use of [[Virtual Private Server]] nodes for control systems and relay management has been reported in the SPACEHOP context.
- Use of [[Operational Relay Box Network]] / [[ORB Network]] constructs (chains of compromised network devices) consistent with [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]].
- Mixed [[HTTP C2]] and [[DNS C2]] patterns (reported for specific malware families), supporting resilient communications.
- Enterprise access patterns involving compromised or stolen credentials for [[VPN Access]] and cloud account access consistent with [[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]].

## 9. Campaign History
- **2010 (reported):** MITRE ATT&CK assesses Ke3chang activity dating to at least 2010 with multi-region targeting.
- **2014 (reporting):** Public reporting describes “Operation Ke3chang” targeting ministries of foreign affairs and related diplomatic entities.
- **2019 (reporting):** ESET reporting details Ke3chang-linked diplomatic targeting and documents updated activity tied to [[30_CIPHER/05_Malware/Okrum]].
- **2021 (reporting):** Microsoft MSTIC reports NICKEL (associated with Ke3chang) targeting government organizations across Latin America and Europe.
- **2019–2024 (campaign in ATT&CK):** ATT&CK lists “SPACEHOP Activity” as associated with Ke3chang (first seen January 2019; last seen May 2024), emphasizing ORB-style relays and exploitation activity in reporting.

## 10. Known Indicators
No stable public indicators are included in this note due to infrastructure churn, long time horizons, and the risk of stale or repurposed artifacts.

## 11. Defensive Recommendations
- Prioritize monitoring for activity patterns consistent with exploitation of public-facing collaboration/messaging infrastructure (e.g., [[Microsoft Exchange]] / [[Microsoft SharePoint]]) in line with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]].
- Maintain strong detection coverage for credential access and post-compromise credential use patterns consistent with [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Treat relay-heavy command-and-control and traffic proxying consistent with [[Operational Relay Box Network]] / [[ORB Network]] and [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]] as high-signal when correlated with victimology and associated malware families.

## 12. Analyst Notes
- **Attribution confidence:** Medium (strong ATT&CK mapping and multiple reputable reports; however, alias overlap and ecosystem clustering can complicate strict boundary definition).
- **Analytic caution:** Ke3chang is linked to many associated names (APT15, NICKEL, etc.); use a case-by-case convergence approach (TTPs + malware + infra + victimology).
- **Coverage note:** ATT&CK lists a broad technique set for Ke3chang; this should be treated as “observed across reporting” rather than implying every technique appears in every incident.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Ke3chang (G0004)  
  https://attack.mitre.org/groups/G0004/
- ESET WeLiveSecurity — Okrum: Ke3chang group targets diplomatic missions (2019-07-18)  
  https://www.welivesecurity.com/2019/07/18/okrum-ke3chang-targets-diplomatic-missions/
- Microsoft Security Blog (MSTIC) — NICKEL targeting government organizations across Latin America and Europe (2021-12-06)  
  https://www.microsoft.com/en-us/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe/
- Google Cloud — ORB networks used by China-nexus cyber espionage actors (SPACEHOP context) (2024-05-22)  
  https://cloud.google.com/blog/topics/threat-intelligence/ioc-extinction-china-nexus-cyber-espionage-orb-networks

## 14. References
- MITRE ATT&CK. “Ke3chang (G0004).” (Last modified 2025-04-04)  
  https://attack.mitre.org/groups/G0004/
- ESET. “Okrum: Ke3chang group targets diplomatic missions.” (2019-07-18)  
  https://www.welivesecurity.com/2019/07/18/okrum-ke3chang-targets-diplomatic-missions/
- Microsoft MSTIC. “NICKEL targeting government organizations across Latin America and Europe.” (2021-12-06)  
  https://www.microsoft.com/en-us/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe/
- Google Cloud Threat Intelligence. “IOC Extinction? China-Nexus Cyber Espionage Actors Use ORB Networks to Raise Cost on Defenders.” (2024-05-22)  
  https://cloud.google.com/blog/topics/threat-intelligence/ioc-extinction-china-nexus-cyber-espionage-orb-networks
