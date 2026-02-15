---
entity_type: threat_actor
actor_name: "Cobalt Group"
common_name: "Cobalt Group"
actor_id: "G0080"
actor_type: "Cybercrime / Financially motivated"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2016"
last_seen: ""
status: "Active (reported)"
motivations: ["Financial gain"]
objectives: ["Monetization via ATM, card processing, payment, and SWIFT targeting","Credential theft and access maintenance","Operational security through proxying, tunneling, and log removal"]
victimology_summary: "Cobalt Group is described in ATT&CK as financially motivated and primarily targeting financial institutions since at least 2016, including intrusions aimed at stealing money by targeting ATM systems, card processing/payment systems, and SWIFT systems, with primary targeting in Eastern Europe, Central Asia, and Southeast Asia."
target_sectors: ["Financial services","Banking"]
target_regions: ["Eastern Europe","Central Asia","Southeast Asia"]
related_groups: ["[[30_CIPHER/03_Threat_Actors/G0008 - Carbanak|Carbanak]]","[[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7]]"]
malware: ["[[30_CIPHER/05_Malware/S0284 - More_eggs|More_eggs]]","[[30_CIPHER/05_Malware/S0646 - SpicyOmelette|SpicyOmelette]]"]
tools: ["[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]","[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]","[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]","[[30_CIPHER/05_Malware/S0195 - SDelete|SDelete]]"]
infrastructure: ["[[Spearphishing]]","[[Proxy/Tunneling]]","[[RDP and SMB Remote Services]]","[[ATM / payment environment targeting]]"]
ttps: ["[[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1037.001 - Boot or Logon Initialization Scripts: Logon Script]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]","[[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]","[[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]","[[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]","[[20_Entities/07_TTPs/T1572 - Protocol Tunneling]]","[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]","[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1055 - Process Injection]]","[[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]","[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]","[[20_Entities/07_TTPs/T1010 - Application Window Discovery]]","[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]","[[20_Entities/07_TTPs/T1016.001 - System Network Configuration Discovery: Internet Connection Discovery]]","[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]","[[20_Entities/07_TTPs/T1007 - System Service Discovery]]","[[20_Entities/07_TTPs/T1124 - System Time Discovery]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0080 Cobalt Group - https://attack.mitre.org/groups/G0080/","MITRE ATT&CK - S0154 Cobalt Strike - https://attack.mitre.org/software/S0154/","MITRE ATT&CK - S0284 More_eggs - https://attack.mitre.org/software/S0284/","MITRE ATT&CK - S0029 PsExec - https://attack.mitre.org/software/S0029/","MITRE ATT&CK - S0195 SDelete - https://attack.mitre.org/software/S0195/","MITRE ATT&CK - S0646 SpicyOmelette - https://attack.mitre.org/software/S0646/","MITRE ATT&CK - S0002 Mimikatz - https://attack.mitre.org/software/S0002/","Group-IB - Secrets of Cobalt - https://www.group-ib.com/blog/cobalt/","MITRE ATT&CK - G0008 Carbanak (linkage note) - https://attack.mitre.org/groups/G0008/"]
tags: ["scout","threat-actor","mitre-g0080","cobalt-group","financial-crime","banking"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
Cobalt Group (G0080) is described in ATT&CK as a **financially motivated** threat group targeting **financial institutions** since at least **2016**, including intrusions aimed at stealing money by targeting **ATM systems**, **card processing/payment systems**, and **SWIFT systems**. ATT&CK documents a mature intrusion playbook spanning phishing-driven access, credential and token abuse, remote service operations (RDP/SMB), proxy/tunneling, and tooling commonly seen in financially motivated intrusions (e.g., [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]], [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]).

## 2. Attribution Notes
ATT&CK provides a financial motivation and victimology profile but does not provide a definitive sponsor attribution in the group summary. This note treats country attribution as **unknown/low confidence**.

## 3. Motivations & Objectives
- Financial theft through compromise of banking/payment/ATM infrastructure
- Maintain operational access and move laterally within enterprise and payment networks
- Reduce detection and impede investigation via proxying/tunneling and log clearance

## 4. Targeting Profile
- **Sectors:** Banking / financial services
- **Regions:** Eastern Europe, Central Asia, Southeast Asia (per ATT&CK summary)
- **High-value systems:** ATM management servers, payment processing systems, SWIFT-connected infrastructure, identity services enabling privileged access

## 5. Tradecraft Overview
- Initial access aligned to:
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
  - Exploit-assisted execution aligned to [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- Execution and staging aligned to:
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
  - [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- Credential and access abuse aligned to:
  - [[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]
  - [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]
- Lateral movement and remote ops aligned to:
  - [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
  - [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
  - Tooling consistent with [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]
- OPSEC/Defense evasion aligned to:
  - [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]] / [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]
  - [[20_Entities/07_TTPs/T1572 - Protocol Tunneling]]
  - [[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1037.001 - Boot or Logon Initialization Scripts: Logon Script]]
- [[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]
- [[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]
- [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]
- [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]
- [[20_Entities/07_TTPs/T1572 - Protocol Tunneling]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1055 - Process Injection]]
- [[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]
- [[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1010 - Application Window Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1016.001 - System Network Configuration Discovery: Internet Connection Discovery]]
- [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1007 - System Service Discovery]]
- [[20_Entities/07_TTPs/T1124 - System Time Discovery]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]

## 7. Malware & Tools Used
- Malware (per ATT&CK software mapping on the group page):
  - [[30_CIPHER/05_Malware/S0284 - More_eggs|More_eggs]]
  - [[30_CIPHER/05_Malware/S0646 - SpicyOmelette|SpicyOmelette]]
- Tools (per ATT&CK software mapping on the group page):
  - [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]
  - [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]
  - [[30_CIPHER/05_Malware/S0195 - SDelete|SDelete]]

## 8. Infrastructure Patterns
- Spearphishing delivery infrastructure and staged payload hosting
- Proxy and tunneling layers to mediate operator access and reduce attribution
- Remote administration via RDP/SMB and tool-based lateral movement (e.g., PsExec-like patterns)

## 9. Campaign History
- **2016–present (reported):** ATT&CK describes primary targeting of financial institutions since at least 2016 and notes continued activity after a reported arrest in early 2018.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Prioritize detections tied to high-signal financial intrusion tradecraft:
  - Unusual RDP + SMB admin share usage (especially outside normal admin patterns)
  - PsExec-like remote service creation and suspicious service binaries
  - Proxy/tunneling artifacts and anomalous DNS-based C2 behavior
  - Event log clearing attempts and use of secure deletion tooling (e.g., SDelete)
- Segment and monitor payment/ATM/SWIFT-adjacent networks; enforce privileged access workflows and hardened jump hosts.
- Implement robust credential protection (LSASS protections where applicable, strong MFA, tiered admin) and alert on pass-the-hash indicators.

## 12. Analyst Notes
**Confidence:** High for victimology and techniques listed (explicit in ATT&CK). Low for actor origin attribution. Related-group links reflect ATT&CK’s linkage note in the Carbanak group entry.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0080/
- https://www.group-ib.com/blog/cobalt/
- https://attack.mitre.org/groups/G0008/

## 14. References
- MITRE ATT&CK. (2025). *Cobalt Group (G0080)*. https://attack.mitre.org/groups/G0080/
- Group-IB. (2017, August 15). *Secrets of Cobalt*. https://www.group-ib.com/blog/cobalt/
- MITRE ATT&CK. (2025). *Carbanak (G0008)*. https://attack.mitre.org/groups/G0008/
- MITRE ATT&CK. (2025). *Cobalt Strike (S0154)*. https://attack.mitre.org/software/S0154/
- MITRE ATT&CK. (2025). *More_eggs (S0284)*. https://attack.mitre.org/software/S0284/
- MITRE ATT&CK. (2025). *SpicyOmelette (S0646)*. https://attack.mitre.org/software/S0646/
- MITRE ATT&CK. (2025). *Mimikatz (S0002)*. https://attack.mitre.org/software/S0002/
- MITRE ATT&CK. (2025). *PsExec (S0029)*. https://attack.mitre.org/software/S0029/
- MITRE ATT&CK. (2025). *SDelete (S0195)*. https://attack.mitre.org/software/S0195/
