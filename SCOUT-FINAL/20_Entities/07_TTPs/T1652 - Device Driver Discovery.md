---
entity_type: mitre_technique
technique_id: "T1652"
subtechnique_id: ""
technique_name: "Device Driver Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "Linux"
  - "Windows"
  - "macOS"
datasources:
  - "Process Creation (DC0032)"
  - "Windows Registry Key Modification (DC0063)"
  - "Command Execution (DC0064)"
  - "File Access (DC0055)"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1051 - Medusa Group|Medusa Group]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0376 - HOPLIGHT|HOPLIGHT]]"
  - "[[30_CIPHER/05_Malware/S1139 - INC Ransomware|INC Ransomware]]"
  - "[[30_CIPHER/05_Malware/S0125 - Remsec|Remsec]]"
associated_campaigns: []
related_techniques: []
detection_priority:
  - Medium
detection_maturity: ""
threat_score: 2
created: 2026-01-06
updated: 2026-01-06
contributors: []
tags:
  - mitre
  - technique
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Adversaries enumerate installed device drivers (or kernel modules) to identify host characteristics, security tooling, and potential privilege escalation or evasion opportunities.

## 2. Technical Overview
Device driver discovery can provide insights such as:
- **Host role and hardware footprint** (e.g., printer drivers, specialized devices)
- **Defensive tooling** presence (EDR drivers, kernel sensors)
- **Potentially vulnerable drivers** that may be targeted for exploitation or abuse
- **Service/driver relationships** (Windows services associated with drivers)

Common discovery surfaces:
- **Windows**: native utilities and APIs for listing drivers; registry locations that enumerate driver/service entries.
- **Linux**: kernel modules visible via utilities and `/proc`/`/sys`.
- **macOS**: kernel extensions and related filesystem locations.

## 3. Subtechnique Considerations
No sub-techniques.

## 4. Procedure Examples
Observed in ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S0376 - HOPLIGHT|HOPLIGHT]] enumerated device drivers via registry locations.
- [[30_CIPHER/05_Malware/S1139 - INC Ransomware|INC Ransomware]] verified presence of specific drivers.
- [[30_CIPHER/03_Threat_Actors/G1051 - Medusa Group|Medusa Group]] queried drivers on victim devices using Windows driver listing capabilities.
- [[30_CIPHER/05_Malware/S0125 - Remsec|Remsec]] checked for active drivers of security products.

## 5. Detection Guidance
Driver discovery often appears as benign administrative behavior; detection should emphasize **context** and **chaining**:
- Unexpected driver enumeration by non-admin users, unusual parent processes, or post-compromise toolchains.
- Enumeration followed by attempts to disable defenses, load unsigned drivers, or exploit vulnerable drivers.

Recommended detection logic:
- Alert on suspicious invocation of driver enumeration utilities from atypical locations (temp paths) or from suspicious parent processes (office apps, script hosts, unusual services).
- Monitor registry access patterns consistent with scanning multiple driver/service keys in rapid succession.
- On Linux/macOS, detect unusual access to kernel module listings and repeated module-inspection commands by non-administrative contexts.

### Data Source Notes
Required/strongly recommended telemetry:
- **Process Creation (DC0032)**: to detect execution of driver/module inspection utilities and correlate parent/child lineage.
- **Windows Registry Key Modification (DC0063)**: used in practice to observe registry interactions around driver/service enumeration paths in Sysmon-style telemetry.
- **Command Execution (DC0064)**: Linux module inspection commands (e.g., module listing/inspection utilities) from audited exec events.
- **File Access (DC0055)**: reads of `/proc/modules`, `/sys/module/`, or macOS kernel extension paths.

## 6. Response Guidance
1. **Validate legitimacy**: confirm whether the initiating user/process is expected to perform driver inventory (IT ops, troubleshooting).
2. **Scope the activity**: identify which drivers/services/modules were queried; look for EDR/security-driver targeting.
3. **Hunt follow-on**: check for defense impairment, privilege escalation attempts, driver loading events, or kernel manipulation.
4. **Containment**: if suspicious, isolate endpoint and collect triage package (process tree, command lines, module lists, registry access logs).
5. **Hardening**: restrict driver installation/loading policies; enforce least privilege; ensure kernel-protection controls are enabled where applicable.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1652 - Device Driver Discovery|T1652]]

## 8. SOC Relevance
Moderate SOC relevance: valuable as supporting evidence of defense reconnaissance or privilege escalation preparation, particularly when focused on security-related drivers or paired with suspicious tooling.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1051 - Medusa Group|Medusa Group]]

## 10. Campaign Usage
No ATT&CK procedure examples list a specific campaign for this technique.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0376 - HOPLIGHT|HOPLIGHT]]
- [[30_CIPHER/05_Malware/S1139 - INC Ransomware|INC Ransomware]]
- [[30_CIPHER/05_Malware/S0125 - Remsec|Remsec]]

## 12. Mitigations
MITRE notes this technique cannot be easily prevented with preventive controls since it leverages standard OS features. Practical focus:
- Limit administrative access and audit driver/service inventory actions.
- Strengthen kernel protections and driver signing enforcement to reduce the value of driver reconnaissance.

## 13. Testing & Validation
Safe validation ideas (lab):
- Run driver/module inventory commands under a standard user vs. admin context; validate your telemetry and allowlisting behavior.
- Validate correlation: driver discovery followed by defense impairment attempts increases severity.
- Confirm Linux/macOS auditing captures module inspection and relevant file reads.

## 14. References
- MITRE ATT&CK. (n.d.). *Device Driver Discovery (T1652)*. https://attack.mitre.org/techniques/T1652/
- MITRE ATT&CK. (2025, October 21). *Detection Strategy for Device Driver Discovery (DET0579)*. https://attack.mitre.org/detectionstrategies/DET0579/
- Microsoft. (n.d.). *driverquery*. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/driverquery
- Cybersecurity and Infrastructure Security Agency. (2025, March 12). *#StopRansomware: Medusa Ransomware (AA25-071A)*. https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

## 15. Notes
- Treat focused enumeration of EDR/AV drivers as higher risk than broad system inventory in isolation.
