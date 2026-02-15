---
entity_type: threat_actor
actor_name: "Leafminer"
common_name: "Leafminer"
actor_id: "G0077"
actor_type: "State-linked (suspected) / Espionage"
aliases: ["Raspite"]
country_of_origin: "Iran (reported)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2017"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Credential access","Collection from email and endpoints","Establish and maintain access to Middle East targets"]
victimology_summary: "Leafminer is described in ATT&CK as an Iranian threat group targeting government organizations and business entities in the Middle East since at least early 2017."
target_sectors: ["Government","Business (varied)"]
target_regions: ["Middle East"]
related_groups: []
malware: []
tools: ["[[30_CIPHER/05_Malware/S0349 - LaZagne|LaZagne]]","[[30_CIPHER/05_Malware/S0413 - MailSniper|MailSniper]]","[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]","[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]"]
infrastructure: ["[[Web Shell]]","[[HTTP/S C2]]","[[Password Spraying]]","[[Remote Email Collection]]"]
ttps: ["[[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying]]","[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]","[[20_Entities/07_TTPs/T1136.001 - Create Account: Local Account]]","[[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]]","[[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]","[[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]","[[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]","[[20_Entities/07_TTPs/T1003.005 - OS Credential Dumping: Cached Domain Credentials]]","[[20_Entities/07_TTPs/T1055.013 - Process Injection: Process Doppelgänging]]","[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]","[[20_Entities/07_TTPs/T1552.001 - Unsecured Credentials: Credentials In Files]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0077 Leafminer - https://attack.mitre.org/groups/G0077/","MITRE ATT&CK - S0349 LaZagne - https://attack.mitre.org/software/S0349/","MITRE ATT&CK - S0413 MailSniper - https://attack.mitre.org/software/S0413/","MITRE ATT&CK - S0002 Mimikatz - https://attack.mitre.org/software/S0002/","MITRE ATT&CK - S0029 PsExec - https://attack.mitre.org/software/S0029/","Symantec Threat Intelligence - Leafminer - https://www.security.com/threat-intelligence/leafminer-espionage-middle-east"]
tags: ["scout","threat-actor","mitre-g0077","leafminer","iran","middle-east"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
Leafminer (G0077), also referenced by the alias **Raspite**, is described in ATT&CK as an Iranian threat group targeting **government organizations and business entities in the Middle East** since at least **early 2017**. ATT&CK documents credential-focused tradecraft (password spraying, credential dumping, browser credential access), email collection, and use of common offensive tooling (e.g., [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]).

## 2. Attribution Notes
ATT&CK characterizes Leafminer as an **Iranian** threat group. This note treats country attribution as **medium confidence** (consistent with ATT&CK framing and public reporting), and avoids assumptions beyond cited sources.

## 3. Motivations & Objectives
- Espionage-oriented access against government and commercial targets in the Middle East
- Credential acquisition (spraying, dumping, browser/password store access) to expand access
- Email access/collection aligned to remote email collection behaviors

## 4. Targeting Profile
- **Regions:** Middle East
- **Sectors:** Government; business entities (varied)
- **Likely victim systems:** Windows endpoints and enterprise services supporting email and web applications

## 5. Tradecraft Overview
- Credential access and collection aligned to:
  - [[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying]]
  - [[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]] and [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]
  - [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]] (plus related LSASS/LSA/cached credential subtechniques listed in ATT&CK)
- Email collection aligned to [[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]
- Use of commodity tools obtained/used aligned to [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- Discovery and lateral expansion aligned to [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]] and [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying]]
- [[20_Entities/07_TTPs/T1555 - Credentials from Password Stores]]
- [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]
- [[20_Entities/07_TTPs/T1003.005 - OS Credential Dumping: Cached Domain Credentials]]
- [[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1552.001 - Unsecured Credentials: Credentials In Files]]
- [[20_Entities/07_TTPs/T1136.001 - Create Account: Local Account]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1055.013 - Process Injection: Process Doppelgänging]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]

## 7. Malware & Tools Used
- Tools (per ATT&CK software mapping):
  - [[30_CIPHER/05_Malware/S0349 - LaZagne|LaZagne]]
  - [[30_CIPHER/05_Malware/S0413 - MailSniper|MailSniper]]
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]
  - [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]

## 8. Infrastructure Patterns
- Likely credential-focused intrusion infrastructure (spraying endpoints, credential harvesting)
- [[HTTP/S C2]] and tooling delivery patterns consistent with [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- Web-facing compromise opportunities aligned with [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] (as documented)

## 9. Campaign History
- **2017–present (reported):** ATT&CK and public reporting describe activity beginning no later than early 2017.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Enforce phishing-resistant authentication and reduce password spraying exposure (rate-limits, MFA, conditional access).
- Monitor for credential access tradecraft:
  - LSASS access anomalies, suspicious credential dumping telemetry
  - Browser credential store access
  - Unusual remote email access patterns aligned to [[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]
- Alert on toolmarks:
  - Process/service creation consistent with [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]
  - Credential dump artifacts consistent with [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]

## 12. Analyst Notes
**Confidence:** Medium for country attribution (per ATT&CK description). Technique mappings and tools listed reflect ATT&CK documentation; validate specifics per incident.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0077/
- https://www.security.com/threat-intelligence/leafminer-espionage-middle-east

## 14. References
- MITRE ATT&CK. (2025). *Leafminer (G0077)*. https://attack.mitre.org/groups/G0077/
- Symantec Threat Intelligence. (2018, July 25). *Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions*. https://www.security.com/threat-intelligence/leafminer-espionage-middle-east
- MITRE ATT&CK. (2025). *LaZagne (S0349)*. https://attack.mitre.org/software/S0349/
- MITRE ATT&CK. (2025). *MailSniper (S0413)*. https://attack.mitre.org/software/S0413/
- MITRE ATT&CK. (2025). *Mimikatz (S0002)*. https://attack.mitre.org/software/S0002/
- MITRE ATT&CK. (2025). *PsExec (S0029)*. https://attack.mitre.org/software/S0029/
