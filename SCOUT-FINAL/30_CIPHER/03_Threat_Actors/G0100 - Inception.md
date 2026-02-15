---
entity_type: threat_actor
actor_name: "Inception"
common_name: "Inception"
actor_id: "G0100"
actor_type: "Cyberespionage"
aliases:
  - "Inception Framework"
  - "Cloud Atlas"
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2014-01-01"
last_seen: ""
status: "Active"
motivations:
  - "Espionage"
objectives:
  - "Initial access via phishing and exploit chains"
  - "Stealthy execution and cleanup"
  - "Credential and data collection"
victimology_summary: "Cyberespionage group active since at least 2014, historically targeting Russia and other regions, with observed campaigns against European targets using Office vulnerabilities and PowerShell-based backdoors."
target_sectors: []
target_regions:
  - "Russia"
  - "Europe"
  - "Global"
related_groups: []
ttps:
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001]]"
  - "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link|T1204.001]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001]]"
  - "[[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver|T1102.001]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell|T1059.001]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell|T1059.003]]"
  - "[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic|T1059.005]]"
  - "[[20_Entities/07_TTPs/T1059.006 - Command and Scripting Interpreter: Python|T1059.006]]"
  - "[[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32|T1218.010]]"
  - "[[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override|T1036.002]]"
  - "[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion|T1070.004]]"
  - "[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing|T1553.002]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol|T1021.001]]"
  - "[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares|T1021.002]]"
malware:
  - "[[30_CIPHER/05_Malware/LaZagne]]"
  - "[[30_CIPHER/05_Malware/PowerShower]]"
  - "[[30_CIPHER/05_Malware/VBShower]]"
tools: []
infrastructure:
  - "Use of web services and web protocols for staging/C2 patterns"
  - "Signed or legitimate-looking artifacts and proxy execution via system binaries"
references:
  - "https://attack.mitre.org/groups/G0100/"
  - "https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/"
  - "https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/"
mitre_version: "18.0"
attack_spec_version: "3.2"
created: 2026-01-06
last_modified: 2026-01-06
tags:
  - scout
  - threat-actor
  - mitre
  - group
  - G0100
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. BLUF / Executive Summary
Inception (a.k.a. Cloud Atlas / Inception Framework) is a cyberespionage group active since at least 2014. Detection should focus on **phishing-led execution**, **PowerShell backdoors**, **signed/trust-abuse**, and **living-off-the-land proxy execution** (e.g., Regsvr32).

## 2. Attribution Notes
- Public reporting documents activity against Russian and European targets, including observed attacks in October 2018 using Office vulnerabilities and a PowerShell backdoor (PowerShower).

## 3. Motivations & Objectives
- Espionage-driven access and collection.
- Objectives include stealthy persistence/execution, credential enablement, and operational cleanup.

## 4. Targeting Profile
- Historical targeting includes Russia; documented activity includes European targets; broader/global victim set is reported.

## 5. Tradecraft Overview
- Delivery through spearphishing and user-driven execution paths.
- Multi-language scripting (VB, PowerShell, Python) and staged payload delivery.
- Defensive evasion via masquerading and file deletion cleanup.

## 6. MITRE ATT&CK Mapping
- Initial Access / Execution: [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001]], [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link|T1204.001]]
- C2 / Staging: [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001]], [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver|T1102.001]], [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105]]
- Scripting: [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell|T1059.001]], [[20_Entities/07_TTPs/T1059.006 - Command and Scripting Interpreter: Python|T1059.006]]
- Proxy execution / trust: [[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32|T1218.010]], [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing|T1553.002]]
- Evasion/cleanup: [[20_Entities/07_TTPs/T1036.002 - Masquerading: Right-to-Left Override|T1036.002]], [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion|T1070.004]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/PowerShower]] (PowerShell backdoor)
- [[30_CIPHER/05_Malware/VBShower]]
- [[30_CIPHER/05_Malware/LaZagne]] (credential recovery tooling used in reported activity)

## 8. Infrastructure Patterns
- Web-based staging/C2 and use of public web services in resolver-style patterns.
- Reliance on trusted/legitimate-seeming binaries and signed artifacts to reduce suspicion.

## 9. Campaign History
- Documented activity since at least 2014; notable reporting includes “Cloud Atlas” tradecraft and later Europe-targeting campaigns.

## 10. Known Indicators
- Maintain case-specific IOCs: lure URLs, redirect chains, hosting, payload hashes, and signing certificate metadata (when applicable).

## 11. Defensive Recommendations
1. **Phishing telemetry:** correlate email → browser → Office → script engine chains; prioritize “download then execute” patterns.
2. **PowerShell detections:** script block logging, AMSI hits, encoded/obfuscated commands, and suspicious download cradles.
3. **Regsvr32 monitoring:** unusual regsvr32 invocations (remote URLs, uncommon arguments, parent process anomalies).
4. **Code signing controls:** flag newly observed/rare signers; detect execution from user-writable paths even when signed.
5. **Cleanup signals:** file deletion bursts after execution + short-lived artifacts in temp/user profile directories.

## 12. Analyst Notes
- Inception reporting spans years; expect tooling refresh while retaining core behaviors (script-based backdoors + proxy execution + web staging).

## 13. Further Reading / External Resources
- Palo Alto Networks Unit 42. (2018, November 5). *Inception Attackers Target Europe with Year-old Office Vulnerability.* https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/
- Kaspersky. (2014, December 10). *Cloud Atlas: RedOctober APT is back in style.* https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/

## 14. References
- MITRE ATT&CK. (n.d.). *Inception (G0100).* Retrieved 2026-01-06, from https://attack.mitre.org/groups/G0100/
- Palo Alto Networks Unit 42. (2018, November 5). *Inception Attackers Target Europe with Year-old Office Vulnerability.* https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/
- Kaspersky. (2014, December 10). *Cloud Atlas: RedOctober APT is back in style.* https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/
