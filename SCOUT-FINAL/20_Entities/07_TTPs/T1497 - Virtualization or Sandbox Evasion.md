---
entity_type: mitre_technique

technique_id: "T1497"
subtechnique_id: ""
technique_name: "Virtualization/Sandbox Evasion"

tactic:
  - "TA0005 - Defense Evasion"
  - "TA0007 - Discovery"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "Process Creation (DC0032)"
  - "Command Execution (DC0064)"
  - "Module Load (DC0016)"
  - "File Creation (DC0039)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "G1052 - Contagious Interview"
associated_malware:
  - "S0331 - Agent Tesla"
  - "S1039 - Bumblebee"
  - "S1070 - Black Basta"
associated_campaigns: []
related_techniques:
  - "T1497.001 - System Checks"
  - "T1497.002 - User Activity-Based Checks"
  - "T1497.003 - Time Based Evasion"

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

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
Virtualization/Sandbox Evasion (T1497) describes adversary behaviors used to detect or evade virtualized analysis environments and sandboxes. This includes checking for virtualization artifacts, assessing user activity signals, and using time-based delays/loops to outlast automated analysis windows.

## 2. Technical Overview
Common evasion categories:
- **Artifact checks**: probing for virtualization tooling, drivers, device identifiers, registry keys, MAC OUIs, process/service names, filesystem paths, or hardware identifiers indicative of VMs/sandboxes.
- **User activity heuristics**: checking whether the environment looks “real” (e.g., presence/absence of user documents, browsing artifacts, interaction patterns).
- **Time-based techniques**: delaying execution (sleep/loops), timing checks, or conditional triggers based on uptime/system time.

Defender view: direct “anti-VM” logic is often embedded in malware; detections rely on **observable side effects** (enumeration patterns, unusual queries, long sleeps) and correlation with other suspicious activity.

## 3. Subtechnique Considerations
T1497 has sub-techniques:
- **T1497.001 System Checks**: virtualization/sandbox artifact detection via hardware/software indicators.
- **T1497.002 User Activity-Based Checks**: validation of user-like artifacts or interaction signals.
- **T1497.003 Time Based Evasion**: delays/loops/time-bomb logic to evade short-lived analysis.

## 4. Procedure Examples
Representative ATT&CK procedure examples (non-exhaustive):
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]] performs anti-sandboxing/anti-virtualization checks.
- [[30_CIPHER/05_Malware/S1039 - Bumblebee|Bumblebee (S1039)]] performs anti-virtualization checks.
- [[30_CIPHER/05_Malware/S1070 - Black Basta|Black Basta (S1070)]] uses anti-analysis behaviors to hinder analysis/logging.
- [[30_CIPHER/03_Threat_Actors/G1052 - Contagious Interview|Contagious Interview (G1052)]] attempted to thwart container isolation by instructing victims to disable Docker/containers.

## 5. Detection Guidance
Because adversaries adapt quickly, focus on **high-level behaviors** and **correlation**:
- **Environment probing bursts**: short time windows with many host profiling queries (hardware, drivers, processes, services, registry, virtualization indicators).
- **Suspicious time-delay behavior**:
  - unusually long sleeps/delays from non-standard process lineages,
  - repeated timing checks (high-frequency time API usage) correlated with subsequent execution.
- **Anti-analysis tooling discovery**: checks for monitoring/debug tools and analysis artifacts.
- **Context-based alerting**:
  - first-seen binaries showing extensive profiling prior to payload execution,
  - sandbox-evasion checks paired with download/execution attempts.

### Data Source Notes
MITRE Detection Strategy (DET0046) emphasizes:
- **Process Creation (DC0032)**: suspicious utilities and scripts used for artifact checks
- **Command Execution (DC0064)**: shell/PowerShell commands used to query environment indicators
- **Module Load (DC0016)**: loads consistent with probing or anti-analysis behaviors (where observable)
- **File Creation (DC0039)**: creation of marker files or artifacts used to gate execution
- Combine with EDR enrichment for process lineage and prevalence scoring.

## 6. Response Guidance
1. Identify the suspected evasion mechanism (system checks vs. time-based vs. user-activity checks).
2. Correlate with other behaviors (download, injection, persistence, C2 attempts).
3. If confirmed suspicious:
   - isolate the host,
   - capture process memory and binaries for analysis,
   - expand hunting for similar samples (hashes, command-line patterns, lineage).
4. Review sandbox pipeline: confirm detonation windows, interaction simulation, and logging coverage.

## 7. Related ATT&CK Content
- Tactic folder links (multi-tactic technique):
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1497 - Virtualization-Sandbox Evasion|T1497]]
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1497 - Virtualization-Sandbox Evasion|T1497]]

- Sub-techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1497.001 - Virtualization-Sandbox Evasion - System Checks|T1497.001]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1497.002 - Virtualization-Sandbox Evasion - User Activity-Based Checks|T1497.002]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1497.003 - Virtualization-Sandbox Evasion - Time Based Evasion|T1497.003]]

## 8. SOC Relevance
- High relevance for malware triage pipelines and EDR detections.
- Often appears as “low-and-slow” pre-execution behavior; requires correlation to avoid false positives.
- Useful for prioritizing alerts: sandbox-evasion behaviors from new binaries should raise triage urgency.

## 9. Threat Actor Usage
Observed in ATT&CK procedure examples:
- [[30_CIPHER/03_Threat_Actors/G1052 - Contagious Interview|Contagious Interview (G1052)]]

## 10. Campaign Usage
- No campaign entries captured in this note.

## 11. Malware Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]
- [[30_CIPHER/05_Malware/S1039 - Bumblebee|Bumblebee (S1039)]]
- [[30_CIPHER/05_Malware/S1070 - Black Basta|Black Basta (S1070)]]

## 12. Mitigations
- Reduce reliance on single-layer sandboxing:
  - diversify detonation environments and extend analysis windows,
  - simulate user interaction where feasible,
  - use multi-engine/static + behavior + reputation correlation.
- Harden endpoints:
  - application control, attack surface reduction rules, script controls, and least privilege.
- Improve detection fidelity with EDR prevalence scoring and lineage-based policies.

## 13. Testing & Validation
- Validate that your pipeline can observe:
  - environment-probing command bursts,
  - long delay behavior and timing checks,
  - artifact probing patterns.
- Reference safe testing content:
  - https://www.atomicredteam.io/atomic-red-team/atomics/T1497
- Build regression tests for rules to ensure they survive common benign admin utilities and VM management tools.

## 14. References
- MITRE. (2025). Virtualization/Sandbox Evasion (T1497). MITRE ATT&CK. https://attack.mitre.org/techniques/T1497/
- MITRE. (2025). Detection Strategy for Virtualization/Sandbox Evasion (DET0046). MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0046/
- Picus Security. (2023, May 24). Virtualization/Sandbox Evasion - How Attackers Avoid Malware Analysis. https://www.picussecurity.com/resource/virtualization/sandbox-evasion-how-attackers-avoid-malware-analysis
- Unit 42. (n.d.). UPS: Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. https://unit42.paloaltonetworks.com/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/
- Atomic Red Team. (n.d.). T1497: Virtualization/Sandbox Evasion. https://www.atomicredteam.io/atomic-red-team/atomics/T1497

## 15. Notes
- Consider splitting alerts into: artifact-check burst, user-activity gating, and time-based delay/loop signals.
- Treat “anti-analysis + loader-like behavior” as higher risk than “generic VM artifact checks” in isolation.
