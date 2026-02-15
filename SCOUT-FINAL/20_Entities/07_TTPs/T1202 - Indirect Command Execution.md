---
entity_type: mitre_technique

technique_id: "T1202"
subtechnique_id: ""
technique_name: "Indirect Command Execution"

tactic:
  - Execution

platforms:
  - Windows
  - Linux
  - macOS

datasources:
  - Process Creation
  - Command-Line Parameters
  - Script Execution
  - OS API Execution
  - EDR Telemetry

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1059"
  - "T1106"
  - "T1218"
  - "T1036"

detection_priority:
  - Medium
  - High

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - execution
  - indirect-execution
  - living-off-the-land
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Indirect Command Execution (T1202)

## 1. Summary
Indirect Command Execution describes adversaries **executing commands through intermediaries** rather than invoking command interpreters directly. By leveraging trusted system utilities, APIs, or execution chains, attackers evade detections that focus on direct command-line or scripting activity.

Attackers use this technique to:
- Bypass command-line–based detections
- Blend malicious activity into legitimate system behavior
- Leverage trusted binaries to proxy execution
- Reduce forensic clarity of execution origin

---

## 2. Technical Overview
Instead of directly executing a command interpreter (e.g., `cmd`, `powershell`, `bash`), adversaries abuse:

- System utilities that accept commands or scripts as input
- APIs that spawn processes indirectly
- Application features that evaluate or execute embedded commands
- Execution chains where one process causes another to run

Common characteristics:
- The initiating process may not appear malicious
- Commands may not appear directly in command-line logs
- Execution may occur via callbacks, configuration files, or embedded logic

Typical indicators:
- Trusted binaries spawning unexpected child processes
- Execution without visible command-line context
- Anomalous process ancestry chains

---

## 3. Subtechnique Considerations
T1202 has no subtechniques but often overlaps with:
- **Command and Scripting Interpreter (T1059)**
- **Native API Execution (T1106)**
- **Signed Binary Proxy Execution (T1218)**

Indirect execution is especially effective in environments with **string- or process-name–based detections**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Using trusted utilities to execute embedded commands
- Triggering execution via configuration files or parameters
- Leveraging application scripting or plugin functionality
- Chaining benign processes to obscure execution source

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **behavioral context and execution chains**:
- Monitor trusted binaries spawning unexpected children
- Alert on anomalous parent–child process relationships
- Detect execution without corresponding user interaction
- Correlate execution with suspicious file or network activity

### Data Source Notes
- **Process creation telemetry**: Primary detection source
- **EDR lineage tracking**: Identify indirect execution paths
- **Script and API logs**: Provide supporting context

Common false positives:
- Legitimate automation tools
- Software installers or updaters
- Administrative management scripts

Tuning guidance:
- Baseline normal execution chains per host role
- Increase severity when indirect execution follows initial access

---

## 6. Response Guidance
When suspected:
1. Identify the initiating process and execution chain
2. Determine what command or payload was ultimately executed
3. Correlate execution with file, network, and identity telemetry
4. Investigate for follow-on execution or persistence
5. Expand scope for similar indirect execution patterns

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1218 - Signed Binary Proxy Execution|T1218]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1036 - Masquerading|T1036]]

---

## 8. SOC Relevance
T1202 explains execution events where:
- Malicious commands are not directly visible
- Trusted binaries are abused as execution proxies
- Detection coverage appears bypassed despite activity

This technique is critical for **behavior-based detection engineering**.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threats
- Red teams and post-exploitation operators
- Adversaries relying on living-off-the-land techniques

---

## 10. Campaign Usage
Observed in:
- Initial access and post-exploitation phases
- Stealth-focused intrusions
- Campaigns targeting environments with strict application controls

---

## 11. Malware Usage
Associated with:
- Loaders and droppers
- Fileless malware
- Post-exploitation frameworks
- LOLBin-abusing toolchains

---

## 12. Mitigations
Recommended mitigations:
- Monitor and restrict abuse of trusted system utilities
- Apply application control and allowlisting
- Use EDR solutions with full process lineage visibility
- Harden systems against misuse of execution-capable features

---

## 13. Testing & Validation
Validation approaches:
- Simulate indirect execution using benign tools
- Validate alerts on anomalous execution chains
- Test SOC workflows for proxy execution scenarios
- Ensure detections are not solely command-line dependent

---

## 14. References
MITRE ATT&CK. (2025). *Indirect Command Execution (T1202)*.  
https://attack.mitre.org/techniques/T1202/

MITRE. (2024). *ATT&CK Execution techniques overview*.  
https://attack.mitre.org/tactics/TA0002/

Elastic Security Labs. (2023). *Detecting living-off-the-land abuse*.  
https://www.elastic.co/security-labs

---

## 15. Notes
- Indirect execution targets detection assumptions.
- Process lineage is more reliable than command strings.
- Treat trusted binaries behaving unexpectedly as suspicious.
