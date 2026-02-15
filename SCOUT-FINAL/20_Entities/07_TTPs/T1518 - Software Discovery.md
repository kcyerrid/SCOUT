---
entity_type: mitre_technique

technique_id: "T1518"
subtechnique_id: ""
technique_name: "Software Discovery"

tactic:
  - TA0007 - Discovery
platforms:
  - ESXi
  - IaaS
  - Linux
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER]]"
  - "[[30_CIPHER/03_Threat_Actors/G0069 - MuddyWater|MuddyWater]]"
  - "[[30_CIPHER/03_Threat_Actors/G0081 - Tropic Trooper|Tropic Trooper]]"
  - "[[30_CIPHER/03_Threat_Actors/G0112 - Windshift|Windshift]]"
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0534 - Bazar|Bazar]]"
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]"
  - "[[30_CIPHER/05_Malware/S0384 - Dridex|Dridex]]"
  - "[[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]"
associated_campaigns:
  - "C0044 - Juicy Mix"
  - "C0016 - Operation Dust Storm"
  - "C0014 - Operation Wocao"
related_techniques:
  - "T1518.001"
  - "T1518.002"

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

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

# T1518 - Software Discovery

## 1. Summary
Adversaries enumerate installed software (and sometimes versions) to understand the environment, identify defensive controls, locate tooling they can abuse (e.g., deployment/management agents), and tailor follow-on actions such as privilege escalation attempts or lateral movement.

## 2. Technical Overview
Software discovery commonly leverages:
- **Windows**: Registry and WMI/PowerShell-based inventory; product/service enumeration; application install paths.
- **Linux**: package manager queries and filesystem inspection for installed packages/binaries.
- **macOS**: application bundle enumeration and system inventory tooling.
- **ESXi/IaaS**: host/instance inventory via platform tooling or cloud APIs (when applicable).

Discovery outputs typically include:
- Application names, versions, install paths
- Installed management/deployment tooling (high-value for lateral movement)
- Indicators of security tooling (expanded in sub-techniques)

## 3. Subtechnique Considerations
- Use **T1518.001** when the intent is clearly focused on **security tooling/sensors/configurations**.
- Use **T1518.002** when the intent is clearly focused on **backup products/configurations** (often pre-impact for ransomware/extortion).
- Parent **T1518** is appropriate when the enumeration appears broad/non-specific (general software inventory).

## 4. Procedure Examples
Commonly observed patterns include:
- Inventorying installed applications via registry/WMI or directory listing prior to deploying additional payloads or selecting exploitation paths.
- Using post-exploitation frameworks’ profiling modules (e.g., [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]) to collect application/version details.
- Threat actors and malware families reported performing software discovery in MITRE procedure examples include [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]] and [[30_CIPHER/05_Malware/S0534 - Bazar|Bazar]] (among many others on the technique page).

## 5. Detection Guidance
Key idea: detect **inventory behavior** when it occurs from **unusual processes**, **unusual principals**, or **unusual hosts**, and when it is **sequenced** with intrusion activity.

High-signal heuristics:
- Software inventory queries launched from **office/browsers/script hosts**, newly dropped binaries, or unsigned/rare executables.
- **Burst enumeration**: rapid queries across multiple inventory sources (registry + services + filesystem), or repeated inventory on a timer.
- Enumeration focused on **deployment/management tooling** (potential lateral movement amplifier).

Detection engineering patterns:
- Correlate **process creation + command line** with known inventory utilities and scripting engines.
- Look for **WMI/PowerShell** inventory patterns followed quickly by credential access, privilege escalation, or remote execution.
- In cloud contexts, flag unusual **Describe/List** API activity that inventories instances/agents from non-management principals.

### Data Source Notes
Telemetry that usually matters most:
- **Endpoint**: process creation, command line, parent/child lineage; PowerShell logging; WMI provider activity (as available in EDR).
- **Windows**: registry access telemetry (EDR) and service/process enumeration behaviors.
- **Linux/macOS**: shell/process exec and package manager invocation logging.
- **Cloud**: audit logs for inventory-related API calls.

## 6. Response Guidance
1. **Validate legitimacy**: is this host/user a known IT inventory workflow?
2. **Scope and sequence**: identify what was enumerated and what happened immediately before/after.
3. **Hunt follow-ons**: privilege escalation attempts, defense evasion, credential access, and lateral movement from the same principal/host.
4. **Contain if suspicious**: isolate endpoint, preserve telemetry/artifacts, and rotate credentials if chaining indicates compromise.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1518 - Software Discovery|T1518]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1518.001 - Software Discovery: Security Software Discovery|T1518.001]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1518.002 - Software Discovery: Backup Software Discovery|T1518.002]]

## 8. SOC Relevance
- High value as an early/mid-stage **environment mapping** signal, especially when paired with initial access artifacts or suspicious execution chains.
- Tuning is essential due to overlap with legitimate inventory and IT management.

## 9. Threat Actor Usage
Examples included on the technique page:
- [[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER]]
- [[30_CIPHER/03_Threat_Actors/G0069 - MuddyWater|MuddyWater]]
- [[30_CIPHER/03_Threat_Actors/G0081 - Tropic Trooper|Tropic Trooper]]
- [[30_CIPHER/03_Threat_Actors/G0112 - Windshift|Windshift]]
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]

## 10. Campaign Usage
Examples included on the technique page:
- C0044 - Juicy Mix
- C0016 - Operation Dust Storm
- C0014 - Operation Wocao

## 11. Malware Usage
Examples included on the technique page:
- [[30_CIPHER/05_Malware/S0534 - Bazar|Bazar]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0384 - Dridex|Dridex]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]

## 12. Mitigations
Preventive controls are limited because discovery abuses common system features. Focus on:
- Application control and least privilege (reduce attacker ability to run discovery tooling broadly)
- Strong endpoint telemetry coverage (process + script logging)
- Harden/administer remote management and software deployment tooling (reduce lateral movement amplification)

## 13. Testing & Validation
- Validate detections in a lab by generating:
  - broad software inventory from a standard user context
  - the same from a sanctioned IT inventory host/account
- Ensure analytics correctly weigh:
  - **host role**, **principal**, **process ancestry**, and **behavior chaining**

## 14. References
- MITRE ATT&CK. (n.d.). *Software Discovery (T1518).* https://attack.mitre.org/techniques/T1518/
- Red Canary. (n.d.). *Atomic Red Team: T1518 - Software Discovery.* https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1518
- MITRE ATT&CK. (n.d.). *Multi-Platform Software Discovery Behavior Chain (DET0392).* https://attack.mitre.org/detectionstrategies/DET0392/

## 15. Notes
- Treat discovery of **deployment/management agents** and **environment-wide inventory tools** as higher-risk than generic application listing.
