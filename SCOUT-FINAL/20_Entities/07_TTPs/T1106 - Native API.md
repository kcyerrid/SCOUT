---
entity_type: mitre_technique

technique_id: "T1106"
subtechnique_id: ""
technique_name: "Native API"

tactic: ["Execution"]
platforms: ["windows", "linux", "macos"]
datasources: ["Process Execution", "API Call Tracing", "Kernel Logs", "Authentication Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059", "T1027", "T1204", "T1569"]

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

# Native API (T1106)

## 1. Summary
Native API describes adversary execution of malicious functionality through direct invocation of operating system APIs rather than higher-level command interpreters or utilities. By interacting directly with native APIs, adversaries can execute code, create processes, manipulate memory, and interact with the operating system in a stealthier manner.

This technique is frequently used to evade security controls that focus on command-line activity or known binaries.

---

## 2. Technical Overview
Operating systems expose native APIs that allow programs to perform low-level system operations.

Adversaries abuse Native APIs to:
- Create processes without invoking common utilities
- Inject code into other processes
- Manipulate memory and threads
- Interact with system services and kernel objects

Examples include Windows Native APIs (e.g., `NtCreateProcess`, `NtWriteVirtualMemory`) and POSIX system calls on Unix-like systems. Artifacts are often limited to low-level process and memory activity.

---

## 3. Subtechnique Considerations
T1106 does not define subtechniques. Variations are primarily based on:
- Operating system (Windows vs. Unix-like)
- User-mode vs. kernel-mode interaction
- Use of undocumented or less-monitored APIs

Detection difficulty increases as adversaries move closer to kernel-level interaction.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Using custom loaders that invoke native APIs directly
- Creating processes without spawning common interpreters
- Injecting payloads into trusted system processes
- Avoiding command-line artifacts entirely

Analysts may observe suspicious process creation or memory manipulation without typical parent-child relationships.

---

## 5. Detection Guidance
Detection should focus on behavioral indicators:
- Process creation without corresponding command-line artifacts
- Suspicious memory allocation and thread creation
- API call patterns inconsistent with normal application behavior
- Execution originating from unsigned or untrusted binaries

Kernel-level telemetry and EDR instrumentation significantly improve detection capability.

### Data Source Notes
- **Process Execution:** Useful but often incomplete alone
- **API Tracing:** High value but requires advanced tooling
- **Kernel Logs:** Provide deep visibility when available

---

## 6. Response Guidance
When Native API abuse is suspected:
- Isolate affected systems immediately
- Capture memory dumps for analysis
- Identify injected processes and malicious loaders
- Review persistence and privilege escalation opportunities

Preserve low-level telemetry and memory artifacts for forensic investigation.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]  
  [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1204 - User Execution|T1204]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1569 - System Services|T1569]]

---

## 8. SOC Relevance
Native API abuse represents a high-skill execution technique commonly used by advanced threat actors and sophisticated malware. SOC teams often struggle to detect this behavior without EDR or kernel-level telemetry.

---

## 9. Threat Actor Usage
This technique is used by:
- Advanced persistent threat groups
- Sophisticated ransomware operators
- Custom malware loaders and post-exploitation frameworks

Confidence in targeted but high-impact usage is high.

---

## 10. Campaign Usage
Native API execution has appeared in:
- Advanced espionage campaigns
- Stealthy ransomware deployment operations
- Long-dwell enterprise intrusions

---

## 11. Malware Usage
Malware and tooling leveraging Native API execution include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0129 - PlugX|PlugX]]
- [[30_CIPHER/05_Malware/S0466 - Cobalt Strike Beacon|Cobalt Strike Beacon]]

---

## 12. Mitigations
Effective mitigations include:
- Deploying EDR solutions with behavioral detection
- Enforcing code signing and application control
- Monitoring for anomalous process and memory activity
- Applying least-privilege principles
- Hardening endpoint configurations

---

## 13. Testing & Validation
Validation approaches include:
- Red team testing with custom loaders
- Purple team simulations of in-memory execution
- Review of alerts tied to memory injection and API abuse

Successful validation results in detection of unauthorized Native API usage.

---

## 14. References
MITRE ATT&CK. (2024). *Native API (T1106)*.  
https://attack.mitre.org/techniques/T1106/

Microsoft. (2023). *Windows Native API documentation*.  
https://learn.microsoft.com/en-us/windows/win32/apiindex/windows-api-list

Elastic. (2023). *Detecting memory-based attacks*.  
https://www.elastic.co/security-labs/detecting-memory-threats

---

## 15. Notes
- Native API abuse often overlaps with defense evasion
- Detection requires deep telemetry and behavioral analysis
- Memory forensics is critical for investigation
