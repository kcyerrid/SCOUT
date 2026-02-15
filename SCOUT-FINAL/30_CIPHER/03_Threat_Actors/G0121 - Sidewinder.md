---
entity_type: threat_actor
actor_name: "Sidewinder"
common_name: "Sidewinder"
actor_id: "G0121"
actor_type: ""
aliases:
  - "T-APT-04"
  - "Rattlesnake"
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: ""
first_seen: ""
last_seen: ""
status: ""

motivations: []
objectives: []
victimology_summary: "APT tracked as Sidewinder (a.k.a. T-APT-04 / Rattlesnake) that uses spearphishing, client-side exploitation, scripted loaders, DLL side-loading, and HTTP-based C2 with automated collection and exfiltration behaviors."
target_sectors: []
target_regions: []

related_groups: []

malware: []
tools: []

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1119 - Automated Collection|T1119 - Automated Collection]]"
  - "[[20_Entities/07_TTPs/T1020 - Automated Exfiltration|T1020 - Automated Exfiltration]]"
  - "[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder|T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell|T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic|T1059.005 - Command and Scripting Interpreter: Visual Basic]]"
  - "[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript|T1059.007 - Command and Scripting Interpreter: JavaScript]]"
  - "[[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging|T1074.001 - Data Staged: Local Data Staging]]"
  - "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]"
  - "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]"
  - "[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001 - Hijack Execution Flow: DLL]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange|T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location|T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation|T1027.010 - Obfuscated Files or Information: Command Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File|T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]"
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link|T1566.002 - Phishing: Spearphishing Link]]"
  - "[[20_Entities/07_TTPs/T1598.002 - Phishing for Information: Spearphishing Attachment|T1598.002 - Phishing for Information: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link|T1598.003 - Phishing for Information: Spearphishing Link]]"
  - "[[20_Entities/07_TTPs/T1057 - Process Discovery|T1057 - Process Discovery]]"
  - "[[20_Entities/07_TTPs/T1518 - Software Discovery|T1518 - Software Discovery]]"
  - "[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery|T1518.001 - Software Discovery: Security Software Discovery]]"
  - "[[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta|T1218.005 - System Binary Proxy Execution: Mshta]]"
  - "[[20_Entities/07_TTPs/T1082 - System Information Discovery|T1082 - System Information Discovery]]"
  - "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]"
  - "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery|T1033 - System Owner/User Discovery]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0121/"
  - "https://www.mitre.org/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0121"
  - "apt"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Sidewinder (G0121) (also tracked as **T-APT-04** and **Rattlesnake**) is an APT with observed tradecraft centered on **spearphishing**, **client-side exploitation**, and **scripted loaders** (PowerShell/VBScript/JavaScript). ATT&CK examples show **DLL side-loading**, **HTTP-based C2**, **automated collection/exfiltration**, and broad host discovery, with multiple phishing-for-information workflows leading to credential harvesting.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0121
- **Aliases:** T-APT-04, Rattlesnake (per ATT&CK)
- **Sponsor/country:** Not explicitly stated on the ATT&CK Group page.

## 3. Motivations & Objectives
- Not explicitly stated on the ATT&CK Group page; operational objectives inferred from ATT&CK behaviors include initial access, credential harvesting, collection, and exfiltration.

## 4. Targeting Profile
- Targeting varies by campaign; ATT&CK examples emphasize tailored spearphishing and credential harvesting workflows.

## 5. Tradecraft Overview
- **Delivery/initial access:** Spearphishing attachments and links; credential-harvesting phishing-for-information.
- **Execution:** Scripted loaders across PowerShell/VBScript/JavaScript; DDE-enabled execution patterns in examples.
- **Persistence:** Registry Run Keys / Startup Folder.
- **Defense awareness:** Enumerates installed software/AV; checks SecurityCenter2 service in examples.
- **Collection & exfil:** Automated collection with local staging and automated exfiltration; HTTP used for C2.
- **Evasion/obfuscation:** Base64 and encrypted/encoded payloads; command obfuscation.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link|T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1598.002 - Phishing for Information: Spearphishing Attachment|T1598.002 - Phishing for Information: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link|T1598.003 - Phishing for Information: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell|T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic|T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript|T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001 - Hijack Execution Flow: DLL]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1119 - Automated Collection|T1119 - Automated Collection]]
- [[20_Entities/07_TTPs/T1020 - Automated Exfiltration|T1020 - Automated Exfiltration]]
- [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging|T1074.001 - Data Staged: Local Data Staging]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder|T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange|T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location|T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation|T1027.010 - Obfuscated Files or Information: Command Obfuscation]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File|T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1518 - Software Discovery|T1518 - Software Discovery]]
- [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery|T1518.001 - Software Discovery: Security Software Discovery]]
- [[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta|T1218.005 - System Binary Proxy Execution: Mshta]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery|T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery|T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery|T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]

## 7. Malware & Tools Used
- ATT&CK techniques cite multiple loaders and payload workflows; specific software (S####) was not captured in the extracted material for this note. Add MITRE Software mappings after correlating to the relevant campaign/tooling.

## 8. Infrastructure Patterns
- HTTP C2 via [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]].
- Credential harvesting pages (phishing-for-information), plus staging/exfil endpoints referenced in automated exfiltration examples.

## 9. Campaign History
- ATT&CK documents multiple Sidewinder campaigns via technique examples; campaign naming is not standardized on the Group page.

## 10. Known Indicators
- Prefer behavior-led pivots:
  - Spearphishing attachments/links → credential harvesting pages.
  - Script loader execution (PowerShell/VBScript/JS) with base64/encrypted blobs.
  - Persistence via Run Keys; staged data in temp folders.
  - Mshta execution for payload launch; DLL side-loading via renamed legitimate binaries.

## 11. Defensive Recommendations
- **Email:** Tight controls on attachment types; detonate suspicious documents; block known risky content chains.
- **Endpoint:** Script-block logging, PowerShell transcription; alert on mshta misuse and DDE-related patterns.
- **Identity:** Monitor credential-harvested logins; enforce phishing-resistant MFA.
- **Network:** Detect unusual outbound HTTP from non-browser processes; flag exfil patterns (burst uploads, automation).

## 12. Analyst Notes
- High-signal detections: [[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta|T1218.005 - System Binary Proxy Execution: Mshta]], [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001 - Hijack Execution Flow: DLL]], plus phishing-for-information workflows.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0121/

## 14. References
- MITRE ATT&CK. (n.d.). *Sidewinder (G0121).* https://attack.mitre.org/groups/G0121/

## 15. Notes
- Add campaign-specific malware/tool notes once you bind observed hashes/domains to known Sidewinder clusters.
