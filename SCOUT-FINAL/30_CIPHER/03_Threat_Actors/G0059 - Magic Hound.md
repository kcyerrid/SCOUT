---
entity_type: threat_actor
actor_name: "Magic Hound"
common_name: "Magic Hound"
actor_id: "G0059"
actor_type: "State-sponsored (espionage)"
aliases: ["TA453","COBALT ILLUSION","Charming Kitten","ITG18","Phosphorus","Newscaster","APT35","Mint Sandstorm"]
country_of_origin: "Iran"
suspected_sponsors: ["Islamic Revolutionary Guard Corps (IRGC) (likely)"]
attribution_confidence: "High"
first_seen: "2014-01-01"
last_seen: ""
status: "Active"
motivations: ["Espionage","Strategic intelligence collection"]
objectives: ["Credential access","Email and document collection","Long-term access to target environments"]
victimology_summary: "Targets reported include government and military personnel, academics, journalists, and international organizations across Europe, the United States, and the Middle East."
target_sectors: ["Government","Military / Defense","Academia","Media / Journalism","International organizations"]
target_regions: ["Middle East","Europe","United States"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/CharmPower]]","[[30_CIPHER/05_Malware/DownPaper]]","[[30_CIPHER/05_Malware/PowerLess]]"]
tools: ["[[30_CIPHER/05_Malware/Impacket]]","[[30_CIPHER/05_Malware/FRP]]"]
infrastructure: ["Phishing domains","Compromised domains","Web services","Cloud storage"]
ttps: ["[[20_Entities/07_TTPs/T1087.003 - Account Discovery: Email Account]]","[[20_Entities/07_TTPs/T1098.002 - Account Manipulation: Additional Email Delegate Permissions]]","[[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0059 Magic Hound - https://attack.mitre.org/groups/G0059/","MITRE ATT&CK - S0674 CharmPower - https://attack.mitre.org/software/S0674/","MITRE ATT&CK - S0186 DownPaper - https://attack.mitre.org/software/S0186/","MITRE ATT&CK - S1012 PowerLess - https://attack.mitre.org/software/S1012/","MITRE ATT&CK - S0357 Impacket - https://attack.mitre.org/software/S0357/","MITRE ATT&CK - S1144 FRP - https://attack.mitre.org/software/S1144/"]
tags: ["scout","threat-actor","mitre-g0059","espionage","iran"]
created: "2026-01-01"
last_modified: "2026-01-01"
---

## 1. BLUF / Executive Summary
Magic Hound (G0059) is an Iran-linked cyber espionage activity cluster assessed to run long-term, resource-intensive operations. Public reporting emphasizes complex social engineering and credential-focused intrusion chains to access email, documents, and strategic information across government-adjacent and high-value individual targets.

## 2. Attribution Notes
MITRE ATT&CK describes Magic Hound as Iranian-sponsored and likely operating on behalf of the IRGC. The actor is also tracked under multiple widely used aliases (e.g., TA453, APT35, Phosphorus, Charming Kitten), reflecting overlaps in vendor tracking and analytic methodologies.

## 3. Motivations & Objectives
- Strategic intelligence collection (espionage)
- Targeted credential theft and mailbox access to support downstream collection
- Durable access to victim communications and documents

## 4. Targeting Profile
- **Regions (reported):** Middle East, Europe, United States  
- **Victim types (reported):** government and military personnel, academics, journalists, international organizations  
- **Sectors (reported):** government, defense, academia, media, international organizations

## 5. Tradecraft Overview
- Heavy reliance on **social engineering** and **targeted phishing** to obtain credentials and user execution.
- Use of **email-focused account manipulation** to expand mailbox visibility and collection.
- Operational emphasis on **discovery**, **persistence**, and **encrypted communications** to maintain access and reduce detection.
- Use of both **custom malware** and **publicly available tooling** in post-compromise activity.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1087.003 - Account Discovery: Email Account]]
- [[20_Entities/07_TTPs/T1098.002 - Account Manipulation: Additional Email Delegate Permissions]]
- [[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1573 - Encrypted Channel]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/CharmPower]]
  - [[30_CIPHER/05_Malware/DownPaper]]
  - [[30_CIPHER/05_Malware/PowerLess]]
- Tools / dual-use:
  - [[30_CIPHER/05_Malware/Impacket]]
  - [[30_CIPHER/05_Malware/FRP]]

## 8. Infrastructure Patterns
- [[Phishing Domains]] and fraudulent lookalike domains aligned to specific targets
- [[Compromised Domains]] used to host lures or redirect infrastructure
- [[Web Services]] (including cloud and hosted services) used for staging and/or C2 support
- [[Encrypted Proxies]] / tunneling tooling to route traffic

## 9. Campaign History
- **2014–present (reported):** Ongoing espionage operations with repeated emphasis on persona-driven outreach and phishing.
- **2022–present (reported):** Continued use of modular PowerShell-based malware families and commodity tooling in enterprise intrusions (as reflected in ATT&CK software tracking).

## 10. Known Indicators
No public, stable indicators are included in this note (to preserve operational safety and because IOCs rapidly age).

## 11. Defensive Recommendations
- Harden email identity and access: enforce phishing-resistant MFA where possible; monitor suspicious delegate/permission changes.
- Improve detection for script-heavy tradecraft: PowerShell logging and alerting for abnormal execution chains.
- Reduce exposure of public-facing services; prioritize patching for widely exploited classes of vulnerabilities.
- Monitor for anomalous mailbox access patterns, impossible travel, and abnormal token/session behavior.

## 12. Analyst Notes
**Confidence:** High for broad characterization and attribution framing (per ATT&CK); medium for fine-grained operational details, which vary by source and campaign. Alias overlap across vendors should be treated carefully when correlating incidents.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0059/
- MITRE ATT&CK Software (examples): https://attack.mitre.org/software/S0674/ | https://attack.mitre.org/software/S1012/

## 14. References
- https://attack.mitre.org/groups/G0059/
- https://attack.mitre.org/software/S0674/
- https://attack.mitre.org/software/S0186/
- https://attack.mitre.org/software/S1012/
- https://attack.mitre.org/software/S0357/
- https://attack.mitre.org/software/S1144/
