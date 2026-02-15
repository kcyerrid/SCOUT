---
entity_type: mitre_technique

technique_id: "T1047"
subtechnique_id: ""
technique_name: "Windows Management Instrumentation"

tactic: ["Execution"]
platforms: ["windows"]
datasources: ["WMI Events", "Process Execution", "Authentication Logs", "PowerShell Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059", "T1021", "T1106"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-16"
updated: "2025-12-16"

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

# Windows Management Instrumentation (T1047)

## 1. Summary
Windows Management Instrumentation (WMI) is abused by adversaries to execute commands and payloads on local or remote Windows systems. Because WMI is a legitimate administrative framework commonly used for system management, its malicious use can blend into normal administrative activity, making detection challenging.

WMI is frequently leveraged for stealthy execution, lateral movement preparation, and automation of malicious tasks.

---

## 2. Technical Overview
WMI enables interaction with Windows systems through CIM objects and namespaces. Adversaries commonly use:
- `wmic.exe`
- PowerShell WMI cmdlets
- COM-based WMI interfaces
- Remote WMI execution over DCOM

Execution may occur locally or remotely and often does not require dropping files to disk. Artifacts include WMI event logs, process creation spawned by `wmiprvse.exe`, and authentication events tied to remote WMI access.

---

## 3. Subtechnique Considerations
T1047 does not currently define subtechniques. Variations are primarily based on:
- Local vs. remote execution
- CLI vs. PowerShell-based invocation
- Use of permanent vs. temporary WMI event subscriptions

Permanent subscriptions significantly increase detection complexity.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Executing remote commands via `wmic /node`
- Creating WMI event subscriptions to trigger payload execution
- Using WMI to launch PowerShell or native binaries
- Leveraging WMI as part of lateral movement chains

Analysts may observe command execution without traditional service creation or scheduled task artifacts.

---

## 5. Detection Guidance
Detection should focus on:
- Process creation originating from `wmiprvse.exe`
- Remote WMI connections from non-administrative hosts
- Creation of WMI event filters and consumers
- Use of `wmic.exe` outside approved administrative workflows

Correlation between authentication logs, process execution, and WMI-specific telemetry is essential.

### Data Source Notes
- **WMI Logs:** High-fidelity but often disabled by default
- **Process Execution:** Critical for identifying child processes
- **Authentication Logs:** Useful for identifying remote execution

---

## 6. Response Guidance
When malicious WMI activity is suspected:
- Identify and remove malicious WMI subscriptions
- Isolate affected hosts if remote execution occurred
- Review credential exposure and lateral movement scope
- Rotate credentials used for WMI access

Preserve WMI repository data and endpoint logs for forensic analysis.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]  
  [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021 - Remote Services|T1021]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]

---

## 8. SOC Relevance
WMI abuse is common in both ransomware and advanced intrusion campaigns due to its stealth and flexibility. SOC teams often lack sufficient WMI logging, making proactive configuration critical.

---

## 9. Threat Actor Usage
This technique is used by:
- Ransomware operators
- Advanced persistent threat groups
- Post-exploitation frameworks

Confidence in widespread usage is high.

---

## 10. Campaign Usage
WMI has been observed in:
- Ransomware intrusion chains
- Lateral movement preparation campaigns
- Long-dwell enterprise compromises

---

## 11. Malware Usage
Malware and tooling leveraging WMI include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]

---

## 12. Mitigations
Effective mitigations include:
- Restricting WMI access to required administrators
- Enabling detailed WMI logging
- Monitoring for abnormal remote WMI usage
- Network segmentation to limit lateral access
- Endpoint protection policies for LOLbin abuse

---

## 13. Testing & Validation
Validation approaches include:
- Atomic Red Team tests for WMI execution
- Purple team simulations using remote WMI
- Review of `wmiprvse.exe` child process alerts

Successful validation results in detection of anomalous WMI-based execution.

---

## 14. References
MITRE ATT&CK. (2024). *Windows Management Instrumentation (T1047)*.  
https://attack.mitre.org/techniques/T1047/

Microsoft. (2023). *Securing Windows Management Instrumentation*.  
https://learn.microsoft.com/en-us/windows/win32/wmisdk/securing-wmi

Mandiant. (2022). *Detecting WMI abuse in enterprise environments*.  
https://www.mandiant.com/resources/blog/detecting-wmi-abuse

---

## 15. Notes
- WMI logging is frequently disabled in production
- Permanent event subscriptions are high-risk artifacts
- WMI often appears alongside PowerShell abuse
