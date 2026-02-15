---
entity_type: threat_actor
actor_name: "BlackTech"
common_name: "BlackTech"
actor_id: "G0098"
actor_type: "Cyberespionage (suspected state-sponsored)"
aliases:
  - "Palmerworm"
country_of_origin: "China (suspected)"
suspected_sponsors:
  - "Chinese state (suspected)"
attribution_confidence: "Medium"
first_seen: "2010-01-01"
last_seen: ""
status: "Active"
motivations:
  - "Espionage"
objectives:
  - "Long-term access to strategic targets"
  - "Credential acquisition and reuse"
  - "Collection and exfiltration of sensitive data"
victimology_summary: "Cyberespionage group active since at least 2010 targeting organizations in East Asia (especially Taiwan, Japan, and Hong Kong), including government, technology, media, and other sectors."
target_sectors:
  - "Government"
  - "Technology"
  - "Media"
target_regions:
  - "Taiwan"
  - "Japan"
  - "Hong Kong"
  - "East Asia"
related_groups: []
ttps:
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190]]"
  - "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution|T1203]]"
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001]]"
  - "[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link|T1566.002]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell|T1059.003]]"
  - "[[20_Entities/07_TTPs/T1003 - OS Credential Dumping|T1003]]"
  - "[[20_Entities/07_TTPs/T1110 - Brute Force|T1110]]"
  - "[[20_Entities/07_TTPs/T1555 - Credentials from Password Stores|T1555]]"
  - "[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001]]"
  - "[[20_Entities/07_TTPs/T1021.004 - Remote Services: SSH|T1021.004]]"
  - "[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing|T1553.002]]"
  - "[[20_Entities/07_TTPs/T1560 - Archive Collected Data|T1560]]"
malware:
  - "[[30_CIPHER/05_Malware/Flagpro]]"
  - "[[30_CIPHER/05_Malware/Kivars]]"
tools: []
infrastructure:
  - "Abuse of legitimate remote access services and credential reuse"
  - "DLL execution flow hijacking for stealth/persistence"
  - "Staging + archival prior to exfiltration"
references:
  - "https://attack.mitre.org/groups/G0098/"
  - "https://www.trendmicro.com/en_us/research/17/f/following-trail-blacktech-cyber-espionage-campaigns.html"
mitre_version: "18.0"
attack_spec_version: "3.2"
created: 2026-01-06
last_modified: 2026-01-06
tags:
  - scout
  - threat-actor
  - mitre
  - group
  - G0098
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. BLUF / Executive Summary
BlackTech is a suspected China-linked cyberespionage group focused on East Asia. Detection engineering should prioritize **credential operations**, **remote service access**, and **trust/loader tradecraft** (e.g., DLL flow hijacking and signed/legitimate-looking artifacts).

## 2. Attribution Notes
- Public reporting and ATT&CK characterize BlackTech as a cyberespionage group active since at least 2010, with targeting emphasis in Taiwan, Japan, and Hong Kong.

## 3. Motivations & Objectives
- **Espionage:** long-term access and intelligence collection.
- **Operational objectives:** credential access, stealthy execution/persistence, and controlled exfiltration.

## 4. Targeting Profile
- **Regions:** Taiwan, Japan, Hong Kong (broader East Asia).
- **Sectors:** government and strategic private sector targets (including technology and media).

## 5. Tradecraft Overview
- Exploitation and phishing for initial access.
- Emphasis on credential theft/reuse to enable remote access and lateral movement.
- Use of execution flow hijacking for stealth.

## 6. MITRE ATT&CK Mapping
- Initial Access: [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190]], [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution|T1203]], [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001]]
- Credential Access: [[20_Entities/07_TTPs/T1003 - OS Credential Dumping|T1003]], [[20_Entities/07_TTPs/T1555 - Credentials from Password Stores|T1555]], [[20_Entities/07_TTPs/T1110 - Brute Force|T1110]]
- Defense Evasion / Execution: [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001]]
- Lateral Movement / Remote Ops: [[20_Entities/07_TTPs/T1021.004 - Remote Services: SSH|T1021.004]]
- Collection/Exfil Prep: [[20_Entities/07_TTPs/T1560 - Archive Collected Data|T1560]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Flagpro]]
- [[30_CIPHER/05_Malware/Kivars]]

## 8. Infrastructure Patterns
- Remote administration over standard services; credential reuse is a key enabling dependency.
- Loader/persistence patterns consistent with DLL-related execution flow manipulation.

## 9. Campaign History
- Multiple espionage campaigns documented in public reporting across East Asia.

## 10. Known Indicators
- Track per-incident IOCs (C2 domains, loader hashes, signed binaries, lateral movement source hosts) with time-bounds; BlackTech infrastructure is expected to rotate.

## 11. Defensive Recommendations
1. **Remote access controls:** strict SSH admin segmentation; MFA where applicable; monitor auth from unusual sources.
2. **Credential telemetry:** LSASS access, credential store reads, and password-store access patterns; correlate with new remote sessions.
3. **DLL load monitoring:** alert on unusual DLL search order activity and unsigned/unexpected DLL loads by signed binaries.
4. **Archive/exfil staging:** watch for bulk archiving in user profile/temp paths preceding outbound connections.

## 12. Analyst Notes
- DLL-based flow hijacking is often high-signal when paired with unusual parent-child chains and new persistence artifacts.

## 13. Further Reading / External Resources
- Trend Micro. (2017). *The Trail of BlackTech’s Cyber Espionage Campaigns.* https://www.trendmicro.com/en_us/research/17/f/following-trail-blacktech-cyber-espionage-campaigns.html

## 14. References
- MITRE ATT&CK. (n.d.). *BlackTech (G0098).* Retrieved 2026-01-06, from https://attack.mitre.org/groups/G0098/
- Trend Micro. (2017). *The Trail of BlackTech’s Cyber Espionage Campaigns.* https://www.trendmicro.com/en_us/research/17/f/following-trail-blacktech-cyber-espionage-campaigns.html
