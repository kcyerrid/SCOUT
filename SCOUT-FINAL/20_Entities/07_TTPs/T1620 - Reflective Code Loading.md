---
entity_type: mitre_technique

technique_id: "T1620"
subtechnique_id: ""
technique_name: "Reflective Code Loading"

tactic:
  - Defense Evasion
  - Execution

platforms:
  - Windows
  - Linux
  - macOS

datasources:
  - Process Creation
  - API Monitoring
  - Memory Analysis
  - EDR Telemetry
  - Endpoint Security Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1055"
  - "T1106"
  - "T1027"
  - "T1059"

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
  - execution
  - defense-evasion
  - reflective-loading
  - memory
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Reflective Code Loading (T1620)

## 1. Summary
Reflective Code Loading describes adversaries **loading executable code directly into a process’s memory without relying on the operating system’s standard loader mechanisms**. This enables execution without writing payloads to disk, significantly reducing forensic artifacts and bypassing file-based detection controls.

Adversaries use this technique to:
- Execute payloads without touching disk
- Evade signature-based and file integrity controls
- Inject or run malware stealthily in memory
- Bypass traditional process creation monitoring

---

## 2. Technical Overview
Reflective code loading involves manually mapping executable code into memory and resolving dependencies without using standard APIs like `LoadLibrary`. Common characteristics include:
- Parsing Portable Executable (PE) headers in memory
- Resolving imports and relocations manually
- Invoking entry points directly
- Executing shellcode or DLL payloads from memory

This technique is often implemented via:
- Custom loaders
- Exploitation frameworks
- Memory injection utilities
- Living-off-the-land binaries abusing native APIs

Artifacts include:
- Memory regions with executable permissions not backed by files
- Unusual API call sequences (e.g., memory allocation + execution)
- Execution chains without corresponding disk artifacts

---

## 3. Subtechnique Considerations
Key considerations for T1620:
- Often combined with **Process Injection (T1055)**
- Common in post-exploitation frameworks
- Detection requires memory visibility
- Disk-based controls provide little coverage

Reflective loading is a cornerstone of **fileless malware operations**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Loading a DLL from memory into a trusted process
- Executing shellcode delivered over the network
- Using custom loaders embedded in scripts or binaries
- Reflectively loading payloads staged by other techniques

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **memory behavior and abnormal API usage**:
- Monitor memory regions with executable permissions not backed by files
- Detect suspicious API call chains (allocate → write → execute)
- Identify reflective loading patterns in EDR telemetry
- Correlate execution with absence of corresponding disk writes

### Data Source Notes
- **Memory analysis**: Identify in-memory-only payloads
- **API monitoring**: Detect non-standard loader behavior
- **EDR telemetry**: Correlate memory execution with parent processes

Common false positives:
- Legitimate in-memory loading by security tools
- Software using custom loaders or packers

Tuning guidance:
- Baseline legitimate reflective loading behavior
- Elevate alerts when reflective loading follows initial access

---

## 6. Response Guidance
When suspected:
1. Capture memory snapshots for analysis
2. Identify parent and injected processes
3. Terminate affected processes where appropriate
4. Hunt for similar in-memory behaviors across endpoints
5. Review initial access vectors and staging techniques

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1055 - Process Injection|T1055]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]

---

## 8. SOC Relevance
T1620 is critical because:
- Payloads never touch disk
- Traditional antivirus may miss execution entirely
- Detection requires advanced telemetry and analysis

SOC teams must rely on **behavioral and memory-based detection**.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threat groups
- Ransomware affiliates
- Red team and post-exploitation frameworks

---

## 10. Campaign Usage
Observed in:
- Fileless malware campaigns
- Post-exploitation stages of intrusions
- Memory-resident loader operations

---

## 11. Malware Usage
Associated with:
- In-memory loaders
- Fileless malware
- Post-exploitation toolkits

---

## 12. Mitigations
Recommended mitigations:
- Enable EDR memory protection features
- Restrict execution permissions in memory
- Monitor suspicious API usage
- Harden systems against initial access

---

## 13. Testing & Validation
Validation approaches:
- Use benign reflective loading tests in lab
- Validate alerts on in-memory execution
- Test SOC response to fileless malware scenarios
- Ensure memory telemetry is retained

Include:
- Preconditions: EDR memory monitoring enabled
- Required roles/tools: SOC, DFIR, EDR platform
- Expected outcomes: detection of reflective loading
- Success criteria: alerting without disk artifacts

---

## 14. References
MITRE ATT&CK. (2025). *Reflective Code Loading (T1620)*.  
https://attack.mitre.org/techniques/T1620/

Elastic Security Labs. (2024). *Detecting reflective loaders*.  
https://www.elastic.co/security-labs

Microsoft. (2024). *Memory-based attack detection*.  
https://learn.microsoft.com/security/

---

## 15. Notes
- Reflective loading is foundational to fileless attacks.
- Memory telemetry is non-negotiable.
- Disk-centric detection models are insufficient.
