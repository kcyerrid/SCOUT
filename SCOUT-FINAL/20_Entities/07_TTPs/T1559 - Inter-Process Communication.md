---
entity_type: mitre_technique

technique_id: "T1559"
subtechnique_id: ""
technique_name: "Inter-Process Communication"

tactic: ["Execution"]
platforms: ["windows", "linux", "macos"]
datasources: ["Process Execution", "IPC Logs", "Named Pipe Events", "Socket Communication", "Authentication Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059", "T1106", "T1047", "T1021"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-17"
updated: "2025-12-17"

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

# Inter-Process Communication (T1559)

## 1. Summary
Inter-Process Communication (IPC) describes adversaries executing code by abusing mechanisms that allow processes to communicate with one another. Instead of launching a new process directly, attackers interact with or inject commands into an existing process through supported IPC channels.

This technique enables stealthy execution, frequently bypassing application allowlisting, parent–child process controls, and simplistic execution monitoring.

---

## 2. Technical Overview
Modern operating systems provide multiple IPC mechanisms, including:
- **Windows:** Named pipes, COM/DCOM, RPC, ALPC
- **Linux/macOS:** Unix domain sockets, signals, shared memory, message queues
- **Cross-platform:** Local TCP/UDP sockets

Adversaries leverage IPC to:
- Send commands to already-running processes
- Trigger execution paths in trusted services
- Control malware components split across multiple processes
- Execute payloads without spawning new executables

Artifacts include IPC handle creation, pipe connections, socket communication, and anomalous inter-process signaling.

---

## 3. Subtechnique Considerations
T1559 includes subtechniques that specify IPC mechanisms (e.g., DCOM, Named Pipes).

Key considerations include:
- IPC activity often appears benign without context
- Legitimate software frequently uses IPC extensively
- Visibility varies widely depending on OS and tooling
- Abuse often overlaps with lateral movement or privilege escalation

Detection requires behavioral baselining and correlation across multiple telemetry sources.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Using named pipes to send commands to malware loaders
- Leveraging COM/DCOM objects to execute code remotely
- Communicating with injected processes via IPC channels
- Triggering execution through service-based IPC interfaces

Analysts may observe unusual IPC activity between unrelated processes.

---

## 5. Detection Guidance
Detection should focus on:
- IPC connections between uncommon process pairs
- Named pipes or sockets created by non-standard processes
- IPC usage shortly followed by suspicious behavior
- Repeated IPC communication patterns indicative of C2-like control

EDR tools with IPC telemetry significantly improve detection fidelity.

### Data Source Notes
- **Named Pipe Events:** High value on Windows
- **Socket Communication:** Useful on Unix-like systems
- **Process Execution:** Provides context but may miss IPC-only execution

---

## 6. Response Guidance
When malicious IPC usage is suspected:
- Identify communicating processes and their roles
- Isolate affected endpoints if execution is confirmed
- Capture memory of involved processes
- Review persistence mechanisms leveraging IPC

Preserve IPC artifacts and execution telemetry for forensic analysis.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1047 - Windows Management Instrumentation|T1047]]  
  [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021 - Remote Services|T1021]]

---

## 8. SOC Relevance
IPC abuse is a common blind spot for many SOCs due to limited telemetry and high noise levels. It is frequently used by advanced adversaries to evade detection and maintain stealthy control over compromised systems.

---

## 9. Threat Actor Usage
This technique is used by:
- Advanced persistent threat groups
- Sophisticated ransomware operators
- Custom malware frameworks

Confidence in targeted but high-impact usage is high.

---

## 10. Campaign Usage
Inter-process communication abuse has appeared in:
- Stealthy post-exploitation campaigns
- Long-dwell enterprise intrusions
- Modular malware deployment operations

---

## 11. Malware Usage
Malware and tooling leveraging IPC include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0129 - PlugX|PlugX]]
- [[30_CIPHER/05_Malware/S0663 - ShadowPad|ShadowPad]]

---

## 12. Mitigations
Effective mitigations include:
- Deploying EDR with IPC visibility
- Restricting unnecessary IPC interfaces
- Enforcing least-privilege process execution
- Monitoring and alerting on anomalous IPC patterns
- Hardening service and COM/DCOM configurations

---

## 13. Testing & Validation
Validation approaches include:
- Atomic Red Team tests for IPC abuse
- Purple team simulations of named pipe and COM execution
- Review of alerts tied to anomalous IPC activity

Successful validation results in detection of unauthorized execution via IPC.

---

## 14. References
MITRE ATT&CK. (2024). *Inter-Process Communication (T1559)*.  
https://attack.mitre.org/techniques/T1559/

Microsoft. (2023). *Windows inter-process communication overview*.  
https://learn.microsoft.com/en-us/windows/win32/ipc/interprocess-communications

Elastic. (2023). *Detecting malicious named pipe activity*.  
https://www.elastic.co/security-labs/detecting-malicious-named-pipes

---

## 15. Notes
- IPC-based execution is difficult to detect without EDR
- Process relationship context is critical
- Frequently combined with lateral movement techniques
