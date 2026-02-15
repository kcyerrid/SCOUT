---
entity_type: threat_actor
actor_name: "MuddyWater"
common_name: "MuddyWater"
actor_id: "G0069"
actor_type: "State-sponsored (espionage)"
aliases: ["Earth Vetala","MERCURY","Static Kitten","Seedworm","TEMP.Zagros","Mango Sandstorm","TA450"]
country_of_origin: "Iran"
suspected_sponsors: ["Iran Ministry of Intelligence and Security (MOIS) (assessed subordinate element)"]
attribution_confidence: "High"
first_seen: "2017-01-01"
last_seen: ""
status: "Active"
motivations: ["Espionage","Information theft"]
objectives: ["Enterprise intrusion and long-term access","Credential access and discovery","Data collection and exfiltration","Use of commodity tooling alongside bespoke implants"]
victimology_summary: "Cyber espionage group assessed in ATT&CK as a subordinate element within Iran's MOIS; targets government and private organizations across telecommunications, local government, defense, and oil/gas sectors across the Middle East, Asia, Africa, Europe, and North America since at least 2017."
target_sectors: ["Telecommunications","Local government","Defense","Oil and gas","Government","Private sector (multi-sector)"]
target_regions: ["Middle East","Asia","Africa","Europe","North America"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/POWERSTATS]]","[[30_CIPHER/05_Malware/STARWHALE]]","[[30_CIPHER/05_Malware/DCHSpy]]"]
tools: ["[[30_CIPHER/05_Malware/CrackMapExec]]","[[30_CIPHER/05_Malware/ConnectWise]]"]
infrastructure: ["[[Abuse of Web Services]]","[[HTTP C2]]","[[Phishing Delivery]]"]
ttps: ["[[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]","[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]","[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]","[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0069 MuddyWater - https://attack.mitre.org/groups/G0069/","MITRE ATT&CK - S0223 POWERSTATS - https://attack.mitre.org/software/S0223/","MITRE ATT&CK - S1037 STARWHALE - https://attack.mitre.org/software/S1037/","MITRE ATT&CK - S1243 DCHSpy - https://attack.mitre.org/software/S1243/","MITRE ATT&CK - S0488 CrackMapExec - https://attack.mitre.org/software/S0488/","MITRE ATT&CK - S0591 ConnectWise - https://attack.mitre.org/software/S0591/"]
tags: ["scout","threat-actor","mitre-g0069","iran","moi","espionage"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

## 1. BLUF / Executive Summary
MuddyWater (G0069) is an Iran-linked espionage actor assessed in ATT&CK as a subordinate element within the Ministry of Intelligence and Security (MOIS). Since at least 2017, it has targeted a broad range of sectors and regions, using a mix of bespoke malware and commodity tools, and leaning on web services and web protocols for delivery, staging, and command-and-control.

## 2. Attribution Notes
ATT&CK explicitly assesses MuddyWater as a subordinate element within Iran’s MOIS. Multiple associated tracking names (e.g., Mango Sandstorm, Seedworm, TEMP.Zagros) are listed as aliases/related clusters in public reporting referenced by ATT&CK.

## 3. Motivations & Objectives
- Strategic intelligence collection and long-term access
- Credential access and discovery to expand control of victim environments
- Data collection/exfiltration, often supported by common administrative and post-exploitation tooling

## 4. Targeting Profile
- **Sectors (reported):** telecommunications, local government, defense, oil and gas, and other private-sector targets
- **Regions (reported):** Middle East, Asia, Africa, Europe, North America

## 5. Tradecraft Overview
- Use of web services for distribution and operational support aligned to [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]].
- C2 and transfer patterns aligned to [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] and [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]].
- PowerShell-heavy execution aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]].
- Persistence via autoruns aligned to [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]].
- Enterprise discovery/administration aligned to [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]] and [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]].
- Data staging via built-in archiving aligned to [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/POWERSTATS]]
  - [[30_CIPHER/05_Malware/STARWHALE]]
  - [[30_CIPHER/05_Malware/DCHSpy]]
- Tools / dual-use:
  - [[30_CIPHER/05_Malware/CrackMapExec]]
  - [[30_CIPHER/05_Malware/ConnectWise]]

## 8. Infrastructure Patterns
- [[Abuse of Web Services]] for staging/distribution and communication
- [[HTTP C2]] and other [[Web Protocol C2]] patterns
- [[Phishing Delivery]] and tool distribution via file-sharing services (as described in ATT&CK technique narratives)

## 9. Campaign History
- **2017–present (reported):** Broad, multi-sector targeting across multiple continents; ATT&CK references multiple public and government-adjacent reports over time.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Improve visibility and governance around outbound web-service usage from endpoints/servers; focus on anomalous patterns rather than static IOCs.
- Strengthen monitoring of PowerShell and WMI usage in non-administrative contexts.
- Emphasize credential hygiene and rapid containment workflows for suspected compromise given repeated credential and discovery behaviors.

## 12. Analyst Notes
**Confidence:** High for attribution and general tradecraft due to ATT&CK’s explicit MOIS assessment and the breadth of referenced reporting; incident-to-incident tooling may vary.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0069/

## 14. References
- https://attack.mitre.org/groups/G0069/
- https://attack.mitre.org/software/S0223/
- https://attack.mitre.org/software/S1037/
- https://attack.mitre.org/software/S1243/
- https://attack.mitre.org/software/S0488/
- https://attack.mitre.org/software/S0591/
