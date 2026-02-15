---
entity_type: mitre_technique

technique_id: "T1218"
subtechnique_id: ""
technique_name: "Signed Binary Proxy Execution"

tactic:
  - Defense Evasion
  - Execution

platforms:
  - Windows
  - macOS

datasources:
  - Process Creation
  - Command-Line Parameters
  - Module Load
  - File Creation
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
  - "T1553"
  - "T1036"
  - "T1106"

detection_priority:
  - High
  - Critical

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - execution
  - defense-evasion
  - signed-binary
  - lolbins
  - proxy-execution
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Signed Binary Proxy Execution (T1218)

## 1. Summary
Signed Binary Proxy Execution describes adversaries **abusing legitimate, signed operating system binaries to proxy the execution of malicious code or commands**. Because these binaries are trusted and commonly present, their misuse can evade application allowlisting, reduce alerting, and blend malicious activity into normal system behavior.

Adversaries use this technique to:
- Execute malicious payloads using trusted binaries
- Bypass application control and allowlisting
- Reduce detection by blending into legitimate activity
- Proxy execution without dropping obvious malicious binaries

---

## 2. Technical Overview
Operating systems ship with numerous **signed binaries** that can execute scripts, load DLLs, or invoke other code. Adversaries abuse these capabilities by:
- Passing malicious arguments to trusted executables
- Leveraging binaries that load external content or scripts
- Using built-in utilities to execute or download payloads
- Abusing binaries that proxy execution into other processes

Common characteristics:
- Execution originates from a signed system binary
- Command-line arguments reveal abnormal behavior
- Payloads may reside in user-writable locations
- No custom executable may be dropped initially

Indicators include:
- Unusual command-line usage of signed binaries
- Signed binaries executing from non-standard contexts
- Execution chains where trusted binaries spawn suspicious children

---

## 3. Subtechnique Considerations
T1218 includes multiple subtechniques focused on specific binaries (e.g., `mshta`, `rundll32`, `installutil`, `regsvr32`). Key considerations:
- Behavior varies significantly by binary
- Detection must be argument- and context-aware
- Legitimate use is common, increasing false positive risk
- Abuse often occurs early in the intrusion chain

Signed binary proxy execution enables **stealthy initial and follow-on execution**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Using signed utilities to load and execute malicious scripts
- Invoking trusted binaries to run attacker-controlled DLLs
- Proxying execution through installers or system utilities
- Leveraging signed binaries to bypass application controls

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **behavioral context and argument analysis**:
- Monitor command-line arguments of signed binaries
- Alert on signed binaries executing content from user-writable paths
- Detect unusual parent/child process relationships
- Correlate signed binary execution with network or file activity

### Data Source Notes
- **Process creation**: Critical for command-line inspection
- **Module load**: Detect DLLs loaded by signed binaries
- **EDR telemetry**: Correlate execution with downstream behavior

Common false positives:
- Legitimate administrative or scripting activity
- Software installation or update processes

Tuning guidance:
- Baseline normal usage patterns per environment
- Elevate alerts when execution context deviates from baseline

---

## 6. Response Guidance
When suspected:
1. Inspect command-line arguments and execution context
2. Identify payloads or scripts executed by the signed binary
3. Quarantine or remove malicious content
4. Hunt for additional signed binary abuse
5. Review application control effectiveness

---

## 7. Related ATT&CK Content
- Technique:
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1218 - Signed Binary Proxy Execution|T1218]]

- Related techniques:
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553 - Subvert Trust Controls|T1553]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1036 - Masquerading|T1036]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]

---

## 8. SOC Relevance
T1218 is critical because:
- Trusted binaries are rarely blocked outright
- Abuse blends into legitimate system activity
- Detection requires deep visibility into execution context

SOC teams must monitor **how trusted binaries are used**, not just that they run.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threat actors
- Initial access and post-exploitation operators
- Malware seeking low-friction execution paths

---

## 10. Campaign Usage
Observed in:
- Phishing-driven initial access campaigns
- Living-off-the-land attack chains
- Application control bypass operations

---

## 11. Malware Usage
Associated with:
- Loaders and droppers
- Fileless malware frameworks
- Post-exploitation tooling leveraging LOLBins

---

## 12. Mitigations
Recommended mitigations:
- Restrict execution of high-risk signed binaries
- Enforce application control with argument inspection
- Monitor and alert on abnormal usage patterns
- Apply least-privilege principles to execution contexts

---

## 13. Testing & Validation
Validation approaches:
- Simulate abuse of signed binaries in a lab
- Validate alerts on abnormal arguments and execution chains
- Test application control bypass scenarios
- Exercise SOC playbooks for LOLBin abuse

Include:
- Preconditions: command-line logging enabled
- Required roles/tools: SOC, EDR, endpoint engineering
- Expected outcomes: detection of proxy execution
- Success criteria: alerting prior to payload execution

---

## 14. References
MITRE ATT&CK. (2025). *Signed Binary Proxy Execution (T1218).*  
https://attack.mitre.org/techniques/T1218/

LOLBAS Project. (2024). *Signed binary abuse techniques*.  
https://lolbas-project.github.io/

Microsoft. (2024). *Detecting living-off-the-land attacks*.  
https://learn.microsoft.com/security/

---

## 15. Notes
- Trust is contextual, not absolute.
- Signed binaries are powerful attack primitives.
- Argument-level visibility is essential.
