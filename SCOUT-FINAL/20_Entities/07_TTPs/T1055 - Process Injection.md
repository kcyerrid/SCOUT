---
entity_type: mitre_technique

technique_id: "T1055"
subtechnique_id: ""
technique_name: "Process Injection"

tactic:
  - Defense Evasion
  - Privilege Escalation

platforms:
  - Windows
  - Linux
  - macOS

datasources:
  - Process Creation
  - OS API Execution
  - Memory
  - Security Event Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1106"
  - "T1059"
  - "T1134"

detection_priority:
  - High
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - defense-evasion
  - privilege-escalation
  - process-injection
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Process Injection (T1055)

## 1. Summary
Process Injection describes adversaries **injecting malicious code into the memory space of a legitimate process**. By executing within a trusted process context, attackers can evade defenses, escalate privileges, and maintain stealthy execution.

T1055 is commonly used to:
- Evade endpoint detection and antivirus controls
- Execute malicious payloads under trusted process identities
- Maintain persistence and conceal malicious activity
- Facilitate credential access and lateral movement

---

## 2. Technical Overview
Process injection abuses operating system mechanisms that allow processes to interact with one another’s memory. Adversaries perform injection by:
- Allocating memory within a target process
- Writing malicious payloads into that memory
- Executing the payload via remote threads or APCs

Common techniques include:
- DLL injection
- Process hollowing
- Thread hijacking
- Reflective code loading

Artifacts often include:
- Memory regions with executable permissions
- API calls indicative of injection behavior
- Legitimate processes exhibiting anomalous behavior

---

## 3. Subtechnique Considerations
T1055 includes multiple subtechniques that vary by injection method. Considerations include:
- Injection technique affects detectability
- Some subtechniques require elevated privileges
- Injection often pairs with process discovery and token abuse
- Detection relies heavily on memory and API telemetry

Process injection remains a cornerstone of modern malware tradecraft.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Injecting shellcode into system processes
- Hollowing benign executables to host malicious code
- Using injection to persist across security restarts
- Pairing injection with credential dumping tools

These actions typically occur after initial execution.

---

## 5. Detection Guidance
Detection strategies should focus on:
- Monitoring suspicious memory allocation and execution patterns
- Detecting API call sequences associated with injection
- Identifying trusted processes exhibiting unexpected network or file activity
- Alerting on executable memory regions created at runtime

### Data Source Notes
- **Memory telemetry**: Essential for detecting in-memory payloads
- **API monitoring**: Required to identify injection behavior
- **Process telemetry**: Enables behavioral correlation

---

## 6. Response Guidance
When suspected:
1. Identify injected processes and isolate affected systems
2. Capture memory images for forensic analysis
3. Terminate malicious processes where safe
4. Investigate for follow-on activity such as credential access
5. Harden endpoint defenses against injection techniques

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1134 - Access Token Manipulation|T1134]]

---

## 8. SOC Relevance
T1055 is highly relevant in:
- Enterprise endpoint environments
- Sophisticated malware and APT campaigns
- Intrusions seeking stealth and longevity

Injection often enables attackers to bypass traditional detection controls.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Advanced persistent threats
- Ransomware operators
- Commodity malware families

Usage reflects its effectiveness and versatility.

---

## 10. Campaign Usage
Observed in:
- Targeted enterprise intrusions
- Long-term espionage campaigns
- Malware delivery and execution chains

---

## 11. Malware Usage
Malware leveraging process injection includes:
- Credential dumpers
- Post-exploitation frameworks
- Stealthy backdoors and loaders

---

## 12. Mitigations
Recommended mitigations:
- Use EDR with memory inspection capabilities
- Restrict use of high-risk APIs
- Enable exploit mitigation features
- Monitor and block anomalous inter-process interactions
- Apply least privilege principles

---

## 13. Testing & Validation
Validation approaches:
- Use Atomic Red Team tests for T1055
- Conduct red team exercises focused on injection detection
- Validate memory scanning and behavioral detections
- Review alert fidelity and false positives

---

## 14. References
MITRE ATT&CK. (2024). *Process Injection (T1055)*.  
https://attack.mitre.org/techniques/T1055/

Microsoft. (2023). *Windows process injection techniques*.  
https://learn.microsoft.com/windows/security/threat-protection

Elastic Security Labs. (2022). *Detecting process injection techniques*.  
https://www.elastic.co/security-labs

---

## 15. Notes
- Process injection is a foundational malware technique
- Memory visibility is critical for reliable detection
- Correlation across telemetry sources improves detection accuracy
