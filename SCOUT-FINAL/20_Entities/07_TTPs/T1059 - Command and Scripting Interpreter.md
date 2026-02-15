---
entity_type: mitre_technique

technique_id: "T1059"
subtechnique_id: ""
technique_name: "Command and Scripting Interpreter"

tactic: ["Execution"]
platforms: ["windows", "linux", "macos", "network", "cloud"]
datasources: ["Process Execution", "Command-Line Parameters", "Script Execution Logs", "Authentication Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059.001", "T1059.002", "T1059.003", "T1059.004", "T1059.005", "T1059.006", "T1059.007", "T1059.008", "T1059.009", "T1106"]

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

# Command and Scripting Interpreter (T1059)

## 1. Summary
Command and Scripting Interpreter describes adversary execution of commands or scripts through native operating system interpreters. These interpreters provide direct access to system functionality and are widely available across platforms, making them a foundational execution mechanism in nearly all intrusion chains.

This technique enables rapid execution, automation, and post-exploitation flexibility while often blending into legitimate administrative activity.

---

## 2. Technical Overview
Operating systems include built-in interpreters designed for system administration and automation.

Common interpreters abused by adversaries include:
- PowerShell
- Windows Command Shell
- Unix shells (bash, sh, zsh)
- Scripting languages such as Python, JavaScript, and Visual Basic
- Network device and cloud-native CLIs

Adversaries may execute scripts inline, load scripts from disk, or retrieve and execute code from remote locations. Artifacts include process creation events, command-line arguments, script execution logs, and child process spawning.

---

## 3. Subtechnique Considerations
T1059 contains multiple subtechniques reflecting interpreter-specific implementations:
- PowerShell
- Windows Command Shell
- Unix Shell
- Python
- JavaScript
- Visual Basic
- Network Device CLI
- Cloud API

Detection strategies must be tailored to each interpreter’s logging capabilities and normal usage patterns.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Executing encoded or obfuscated commands
- Launching interpreters to download and execute payloads
- Using scripting languages for in-memory execution
- Chaining interpreter commands to automate attack workflows

Analysts may observe interpreter processes spawning suspicious child processes or accessing the network.

---

## 5. Detection Guidance
Detection should focus on behavioral anomalies:
- Interpreter execution by unexpected parent processes
- Suspicious or encoded command-line arguments
- Script execution from user-writable or temporary directories
- Network connections initiated by interpreter processes

High-fidelity detection relies on command-line logging and script block visibility.

### Data Source Notes
- **Process Execution:** Primary detection source
- **Command-Line Parameters:** Critical for identifying obfuscation
- **Script Logs:** Provide high-confidence behavioral insight

---

## 6. Response Guidance
When malicious interpreter usage is suspected:
- Capture full command-line and script content
- Isolate affected hosts if execution is confirmed
- Identify follow-on payloads or persistence mechanisms
- Review credential exposure and lateral movement indicators

Preserve process and script execution artifacts for forensic analysis.

---

## 7. Related ATT&CK Content
- Subtechniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.001 - PowerShell|T1059.001]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.002 - AppleScript|T1059.002]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.003 - Windows Command Shell|T1059.003]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.004 - Unix Shell|T1059.004]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.005 - Visual Basic|T1059.005]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.006 - Python|T1059.006]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.007 - JavaScript|T1059.007]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.008 - Network Device CLI|T1059.008]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.009 - Cloud API|T1059.009]]

- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]

---

## 8. SOC Relevance
Command and scripting interpreters are among the most frequently observed execution mechanisms in enterprise intrusions. SOCs must differentiate between benign administrative usage and malicious activity through behavioral context rather than simple allow/block logic.

---

## 9. Threat Actor Usage
This technique is used by:
- Ransomware operators
- Advanced persistent threat groups
- Initial access brokers
- Commodity malware families

Confidence in ubiquitous usage is extremely high.

---

## 10. Campaign Usage
Interpreter-based execution appears in:
- Initial access and post-exploitation phases
- Automated ransomware deployment campaigns
- Long-dwell espionage operations

---

## 11. Malware Usage
Malware and tooling heavily reliant on interpreters include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]

---

## 12. Mitigations
Effective mitigations include:
- Restricting interpreter usage via policy
- Enabling enhanced command-line and script logging
- Blocking encoded or obfuscated command execution
- Applying least-privilege principles
- Monitoring interpreter network activity

---

## 13. Testing & Validation
Validation approaches include:
- Atomic Red Team tests for interpreter execution
- Purple team simulations across multiple interpreters
- Review of alerts tied to command-line anomalies

Successful validation results in detection of unauthorized interpreter use.

---

## 14. References
MITRE ATT&CK. (2024). *Command and Scripting Interpreter (T1059)*.  
https://attack.mitre.org/techniques/T1059/

Microsoft. (2023). *PowerShell security best practices*.  
https://learn.microsoft.com/en-us/powershell/scripting/security/overview

Elastic. (2023). *Detecting malicious command-line activity*.  
https://www.elastic.co/security-labs/detecting-malicious-command-line-activity

---

## 15. Notes
- Interpreter abuse is foundational to most attack chains
- Obfuscation is the primary detection challenge
- Interpreter telemetry should be considered high priority
