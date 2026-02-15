---
entity_type: mitre_technique

technique_id: "T1129"
subtechnique_id: ""
technique_name: "Shared Modules"

tactic: ["Execution"]
platforms: ["windows", "linux", "macos"]
datasources: ["Process Execution", "Image Load", "File Creation", "Registry", "Authentication Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059", "T1106", "T1574", "T1027"]

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

# Shared Modules (T1129)

## 1. Summary
Shared Modules describes adversary execution of malicious code by loading shared libraries into a running process. By abusing legitimate module-loading mechanisms (e.g., DLLs on Windows or shared objects on Unix-like systems), adversaries can execute payloads in the context of trusted processes, often reducing visibility and bypassing simple application controls.

This technique is commonly used for stealthy execution, defense evasion, and as a precursor to persistence or privilege escalation.

---

## 2. Technical Overview
Operating systems support shared modules to enable code reuse:
- **Windows:** Dynamic-link libraries (DLLs)
- **Linux/macOS:** Shared objects (`.so`, `.dylib`)

Adversaries may:
- Load malicious libraries into benign processes
- Abuse search order hijacking to force loading of attacker-controlled modules
- Inject modules into running processes
- Leverage legitimate plugin or extension mechanisms

Artifacts include module load events, file creation of shared libraries, registry or configuration changes affecting load paths, and process execution telemetry.

---

## 3. Subtechnique Considerations
T1129 does not define subtechniques but overlaps operationally with related techniques:
- DLL search order hijacking
- Library injection
- Plugin abuse

Detection approaches must consider OS-specific loading behavior and legitimate application use of shared modules.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Dropping a malicious DLL alongside a legitimate executable
- Abusing writable directories in application load paths
- Loading shared objects via custom loaders
- Injecting modules into long-lived or privileged processes

Analysts may observe unexpected module loads by trusted binaries.

---

## 5. Detection Guidance
Detection should focus on:
- Unusual or unsigned modules loaded by trusted processes
- Module loads from user-writable or temporary directories
- Processes loading modules with anomalous names or hashes
- Changes to environment variables or registry keys influencing load paths

High-fidelity detection benefits from image-load telemetry and code-signing validation.

### Data Source Notes
- **Image Load:** High value for identifying malicious modules
- **Process Execution:** Provides execution context
- **Registry / Config:** Useful for detecting path manipulation

---

## 6. Response Guidance
When malicious shared module activity is suspected:
- Identify and remove the malicious library
- Isolate affected systems if privileged processes are involved
- Review for persistence mechanisms tied to module loading
- Validate integrity of affected applications and binaries

Preserve loaded module artifacts and process memory for forensic analysis.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]  
  [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1574 - Hijack Execution Flow|T1574]]  
  [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]

---

## 8. SOC Relevance
Shared module abuse is a high-risk execution technique because it often executes within trusted processes. SOC teams without module load visibility may miss this activity entirely.

---

## 9. Threat Actor Usage
This technique is used by:
- Advanced persistent threat groups
- Sophisticated ransomware operators
- Custom malware developers

Confidence in targeted but impactful usage is high.

---

## 10. Campaign Usage
Shared module execution has appeared in:
- Stealthy post-exploitation campaigns
- Long-dwell enterprise intrusions
- Malware loader and injector operations

---

## 11. Malware Usage
Malware and tooling leveraging shared modules include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0129 - PlugX|PlugX]]
- [[30_CIPHER/05_Malware/S0501 - Backdoor.DLL Loaders|Backdoor.DLL Loaders]]

---

## 12. Mitigations
Effective mitigations include:
- Enforcing code signing and application control
- Monitoring and restricting writable directories in load paths
- Deploying EDR with image-load telemetry
- Applying least-privilege principles
- Hardening application search path configurations

---

## 13. Testing & Validation
Validation approaches include:
- Atomic Red Team tests for DLL/shared object loading
- Purple team simulations of search order hijacking
- Review of alerts for anomalous module loads

Successful validation results in detection of unauthorized shared module execution.

---

## 14. References
MITRE ATT&CK. (2024). *Shared Modules (T1129)*.  
https://attack.mitre.org/techniques/T1129/

Microsoft. (2023). *Dynamic-link library security*.  
https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security

Elastic. (2023). *Detecting malicious DLL loading*.  
https://www.elastic.co/security-labs/detecting-malicious-dll-loading

---

## 15. Notes
- Image-load telemetry is essential for detection
- Shared module abuse often overlaps with execution flow hijacking
- Trusted process context significantly increases impact
