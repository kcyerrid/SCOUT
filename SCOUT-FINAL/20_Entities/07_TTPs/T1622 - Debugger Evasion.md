---
entity_type: mitre_technique
technique_id: "T1622"
subtechnique_id: ""
technique_name: "Debugger Evasion"
tactic:
  - "TA0005 - Defense Evasion"
  - "TA0007 - Discovery"
platforms:
  - "Linux"
  - "Windows"
  - "macOS"
datasources:
  - "Process Creation (DC0032)"
  - "OS API Execution (DC0021)"
  - "File Access (DC0055)"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1087 - AsyncRAT|AsyncRAT]]"
  - "[[30_CIPHER/05_Malware/S1070 - Black Basta|Black Basta]]"
  - "[[30_CIPHER/05_Malware/S1039 - Bumblebee|Bumblebee]]"
  - "[[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]"
  - "[[30_CIPHER/05_Malware/S1066 - DarkTortilla|DarkTortilla]]"
  - "[[30_CIPHER/05_Malware/S0694 - DRATzarus|DRATzarus]]"
  - "[[30_CIPHER/05_Malware/S1160 - Latrodectus|Latrodectus]]"
  - "[[30_CIPHER/05_Malware/S1202 - LockBit 3.0|LockBit 3.0]]"
  - "[[30_CIPHER/05_Malware/S1213 - Lumma Stealer|Lumma Stealer]]"
  - "[[30_CIPHER/05_Malware/S1060 - Mafalda|Mafalda]]"
  - "[[30_CIPHER/05_Malware/S1145 - Pikabot|Pikabot]]"
  - "[[30_CIPHER/05_Malware/S0013 - PlugX|PlugX]]"
  - "[[30_CIPHER/05_Malware/S1228 - PUBLOAD|PUBLOAD]]"
  - "[[30_CIPHER/05_Malware/S1130 - Raspberry Robin|Raspberry Robin]]"
  - "[[30_CIPHER/05_Malware/S0240 - ROKRAT|ROKRAT]]"
  - "[[30_CIPHER/05_Malware/S1018 - Saint Bot|Saint Bot]]"
  - "[[30_CIPHER/05_Malware/S1200 - StealBit|StealBit]]"
  - "[[30_CIPHER/05_Malware/S1183 - StrelaStealer|StrelaStealer]]"
  - "[[30_CIPHER/05_Malware/S0595 - ThiefQuest|ThiefQuest]]"
  - "[[30_CIPHER/05_Malware/S1239 - TONESHELL|TONESHELL]]"
  - "[[30_CIPHER/05_Malware/S1207 - XLoader|XLoader]]"
associated_campaigns:
  - "C0022 - Operation Dream Job"
related_techniques: []
detection_priority:
  - Medium
detection_maturity: ""
threat_score: 3
created: 2026-01-06
updated: 2026-01-06
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

## 1. Summary
Adversaries attempt to detect and avoid debuggers to hinder dynamic analysis and incident response, often altering execution flow, suppressing functionality, or exiting when analysis artifacts are present.

## 2. Technical Overview
Debugger evasion is a class of anti-analysis behaviors where malware checks for indicators of a debugged process or analysis environment and reacts to reduce visibility. Common approaches include:
- **Debugger presence checks** (e.g., Windows APIs that reveal debugging state; Linux `/proc` checks; macOS `ptrace`/`sysctl` checks).
- **Artifact discovery** (searching for common debugger process names, windows/titles, or tool installations).
- **Exception/flow manipulation** (structured exception handling, deliberate faults, or timing checks) to confuse debuggers.
- **Debugger “flooding”** (generating large volumes of debug output/events to overwhelm analysis tooling).

Operational impact:
- Reduced forensic signal from sandboxes and detonation systems
- Conditional execution that only triggers in “real” environments
- Increased dwell time due to slower reverse engineering and triage

## 3. Subtechnique Considerations
No sub-techniques.

## 4. Procedure Examples
Observed in ATT&CK procedure examples (representative set from the technique page):
- [[30_CIPHER/05_Malware/S1087 - AsyncRAT|AsyncRAT]] uses debugger-detection functions.
- [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]] checks the `BeingDebugged` flag in the PEB.
- [[30_CIPHER/05_Malware/S1066 - DarkTortilla|DarkTortilla]] detects debuggers and profiler-related environment conditions.
- [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]] includes debug strings and uses Windows debugger-check APIs.
- Campaign reference: **C0022 - Operation Dream Job** used tools leveraging Windows debugger-check calls.
- Additional malware in ATT&CK examples includes: [[30_CIPHER/05_Malware/S1145 - Pikabot|Pikabot]], [[30_CIPHER/05_Malware/S0013 - PlugX|PlugX]], [[30_CIPHER/05_Malware/S1130 - Raspberry Robin|Raspberry Robin]], [[30_CIPHER/05_Malware/S0595 - ThiefQuest|ThiefQuest]], and others listed in this note’s metadata.

## 5. Detection Guidance
Debugger evasion is often best detected by correlating low-level telemetry (API calls, file access, process behavior) with execution context.
- Watch for processes calling known debugger-detection APIs shortly after start, especially when followed by early termination or behavior suppression.
- Detect “tool discovery” patterns: scanning for debugger-related strings/processes/windows, and file/registry probes for installed analysis tools.
- Correlate anti-debug actions with other suspicious signals (unsigned binaries, unusual parent processes, network beacons, persistence attempts).

Practical detection approaches:
- **Windows**: telemetry for API execution patterns (where available), suspicious sequences of debug-related API calls, and suspicious module loads used for introspection.
- **Linux**: monitor file reads of `/proc/self/status` with focus on fields associated with tracing/debugging.
- **macOS**: detect `ptrace` and related calls used to deny or detect debugging; correlate with suspicious process ancestry.

Alert enrichment tips:
- Add “analysis evasion” context when you see fast process exit after anti-debug checks.
- Include execution chain (parent/command line) and code-signing reputation in the alert payload.

### Data Source Notes
Required/strongly recommended telemetry:
- **Process Creation (DC0032)**: to identify suspicious binaries and early termination patterns; correlate with parent process and command line.
- **OS API Execution (DC0021)**: where supported (e.g., ETW/unified logging) to detect debug-related API calls.
- **File Access (DC0055)**: especially for Linux `/proc` inspection and macOS extension paths in broader anti-analysis behaviors.

## 6. Response Guidance
1. **Preserve execution artifacts**: capture process tree, loaded modules, memory (if possible), and early-exit binaries.
2. **Triage behavior suppression**: compare observed behavior in endpoint vs. detonation environment; consider that sandbox runs may be incomplete.
3. **Hunt for follow-on**: look for staged payloads that may only execute after environment checks succeed.
4. **Containment**: isolate host if correlated with other malicious activity; block hash/cert/IOC as appropriate.
5. **Analysis strategy**: consider instrumented detonation with anti-evasion controls (without relying solely on sandbox verdicts).

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1622 - Debugger Evasion|T1622]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1622 - Debugger Evasion|T1622]]

## 8. SOC Relevance
Moderate-to-high relevance in malware triage pipelines: debugger evasion can explain “no behavior” detonations, short-lived processes, and inconsistent sandbox outcomes. It is also a useful pivot when suspicious binaries appear inert.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]

## 10. Campaign Usage
- C0022 - Operation Dream Job

## 11. Malware Usage
See `associated_malware` in frontmatter for the full list of software referenced in ATT&CK procedure examples for this technique.

## 12. Mitigations
MITRE notes this technique is difficult to prevent with purely preventive controls because it abuses legitimate system features. Focus on:
- Robust endpoint telemetry coverage (API/file/process)
- Threat hunting playbooks for anti-analysis patterns
- Rapid isolation and triage workflows for suspicious binaries that exhibit early termination

## 13. Testing & Validation
Safe validation ideas (lab):
- Execute a benign test program that performs debugger-detection checks and confirm your telemetry captures the relevant API/file access signals.
- Validate correlation logic: “debug-check API call(s)” + “process exit within short interval” + “unsigned/untrusted binary” raises an alert.
- Ensure Linux/macOS controls capture `/proc` reads and `ptrace` usage for non-standard processes.

## 14. References
- MITRE ATT&CK. (n.d.). *Debugger Evasion (T1622)*. https://attack.mitre.org/techniques/T1622/
- MITRE ATT&CK. (2025, October 21). *Detection Strategy for Debugger Evasion (DET0371)*. https://attack.mitre.org/detectionstrategies/DET0371/
- Apriorit. (2024, June 4). *Anti Debugging Protection Techniques with Examples*. https://www.apriorit.com/dev-blog/anti-debugging-protection-techniques

## 15. Notes
- Consider treating debugger-evasion detections as “analysis risk modifiers” that increase priority when paired with other indicators (persistence, C2, credential access).
