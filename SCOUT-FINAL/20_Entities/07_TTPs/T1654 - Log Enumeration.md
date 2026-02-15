---
entity_type: mitre_technique
technique_id: "T1654"
subtechnique_id: ""
technique_name: "Log Enumeration"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "Windows"
  - "macOS"
datasources:
  - "DC0032 - Process Creation"
  - "DC0055 - File Access"
  - "DC0064 - Command Execution"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]"
  - "[[30_CIPHER/03_Threat_Actors/G1023 - APT5|APT5]]"
  - "[[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]]"
associated_campaigns: []
related_techniques:
  - "T1087"
  - "T1518"
  - "T1018"
detection_priority:
  - "High"
detection_maturity: ""
threat_score: 4
created: 2026-01-06
updated: 2026-01-06
contributors: []
tags:
  - "mitre"
  - "technique"
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Log Enumeration is adversary discovery of system/service logs (local or centralized) to extract insights such as authentication events, security tooling presence, operational context, and incident response activity. It can also precede log theft, tampering, or defensive evasion.

## 2. Technical Overview
Adversaries may:
- Use native OS utilities and scripting to read/export event logs (Windows) or review text-based logs (Linux/macOS/ESXi).
- Enumerate centralized logging/SIEM sources to understand detections and response actions.
- In cloud environments, use provider logging services/APIs to retrieve audit histories and operational logs.

Defender-relevant behavioral signals:
- First-time or unusual usage of log utilities by a user/host
- Access to security/authentication channels from non-admin contexts
- Log export followed by archive creation, staging, or outbound transfer
- Correlation with other recon actions (account discovery, software discovery, remote system discovery)

## 3. Subtechnique Considerations
None (no sub-techniques).

## 4. Procedure Examples
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]] used Windows log enumeration utilities/PowerShell to search for successful logons.
- [[30_CIPHER/03_Threat_Actors/G1023 - APT5|APT5]] used tooling to parse and extract information from VPN logs.
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda]] enumerated authentication-related logs in Linux environments.
- [[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]] enumerated system log information.

## 5. Detection Guidance
Design detections around:
- **Process + command context**: log utilities and scripts (and their arguments) from unusual processes/users.
- **Sensitive channel targeting**: Windows Security/System channels, authentication logs, hypervisor host logs.
- **Export/collection sequences**: enumeration → file creation/export → compression → network transfer.

Practical detection patterns:
- Windows:
  - executions of log utilities or event log cmdlets by non-admin accounts
  - enumeration of Security channel or high-value providers outside baseline
- Linux/macOS/ESXi:
  - repeated access to `/var/log/` (or platform-specific log paths) across multiple files in short time windows
- Cloud/IaaS:
  - high-frequency log retrieval calls across multiple instances/resources

### Data Source Notes
- **DC0032 – Process Creation**: command-line visibility for log utilities and PowerShell execution.
- **DC0055 – File Access**: file open/read patterns against sensitive log paths/channels.
- **DC0064 – Command Execution**: shell/command auditing (auditd/unified logs/ESXi CLI logging) and cloud API call logging where applicable.

## 6. Response Guidance
1. Validate legitimacy: is the operator an admin/troubleshooter and is there a ticket/change window?
2. Identify scope: which logs were accessed (security/auth/VPN/EDR/SIEM) and whether export occurred.
3. Pivot: search for data staging and exfil behaviors immediately following enumeration.
4. Containment: if adversarial, restrict session and rotate credentials; consider blocking further log access/export for that principal.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1654 - Log Enumeration|T1654]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1518 - Software Discovery|T1518]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1018 - Remote System Discovery|T1018]]

## 8. SOC Relevance
- **High**: strong recon indicator with direct defensive implications.
- Often appears in:
  - hands-on-keyboard intrusions
  - pre-ransomware prep (environment understanding and response evasion)
  - “living off the land” tradecraft (PowerShell + native tools)

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]: log enumeration for successful logons.
- [[30_CIPHER/03_Threat_Actors/G1023 - APT5|APT5]]: parsing/extracting VPN logs.
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda]]: Linux authentication log enumeration.

## 10. Campaign Usage
None noted.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]]: enumerates infected system log information.

## 12. Mitigations
- Restrict log access/export to privileged roles where feasible.
- Protect centralized logging infrastructure with strict RBAC and alerting on bulk exports.
- Ensure strong auditing is enabled for event log access and PowerShell/script execution.

## 13. Testing & Validation
- Controlled tests:
  - enumerate logs with native tools under a standard user vs admin and confirm telemetry.
  - simulate “enumerate then export” and validate correlation rules.
- Validate tuning:
  - allowlist known IT troubleshooting scripts and EDR agents
  - alert on anomalous parents, unusual hosts, and high-volume/bulk access patterns

## 14. References
- MITRE ATT&CK. (n.d.). *Log Enumeration (T1654).* https://attack.mitre.org/techniques/T1654/
- MITRE ATT&CK. (2025). *Detection Strategy for Log Enumeration (DET0255).* https://attack.mitre.org/detectionstrategies/DET0255/
- MITRE ATT&CK. (n.d.). *DUSTTRAP (S1159).* https://attack.mitre.org/software/S1159/

## 15. Notes
- High-value correlation: log enumeration + credential access or remote discovery is often a reliable precursor to escalation or lateral movement.
