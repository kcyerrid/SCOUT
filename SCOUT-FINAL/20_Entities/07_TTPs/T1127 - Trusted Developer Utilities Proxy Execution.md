---
entity_type: mitre_technique

technique_id: "T1127"
subtechnique_id: ""
technique_name: "Trusted Developer Utilities Proxy Execution"

tactic:
  - Defense Evasion
platforms:
  - Windows
datasources:
  - Process Creation
  - Module Load
  - File Creation
  - Network Connection Creation
  - Process Metadata

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - T1127.001
  - T1127.002
  - T1127.003

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
Adversaries may abuse trusted, signed developer utilities to execute attacker-controlled code while appearing to run legitimate tooling, often bypassing application control and reputation-based defenses (including Smart App Control scenarios). These executions frequently occur on endpoints that are not developer workstations and may quickly chain into scripting/LOLBins and network activity.

## 2. Technical Overview
**Core idea:** execute malicious payloads “through” a trusted developer tool.

Key characteristics:
- **Trusted parent process**: a signed developer utility launches or loads attacker-controlled logic.
- **Context mismatch**: developer tooling observed on non-dev hosts (users, servers) or outside normal build hours.
- **Behavior chaining**: immediate follow-on actions that are atypical for development flows:
  - spawning high-risk children (PowerShell, cmd, rundll32, regsvr32, wscript, mshta)
  - loading unsigned/user-writable DLLs
  - writing and executing payloads from user-writable directories
  - initiating outbound network connections shortly after tool start

## 3. Subtechnique Considerations
This is a parent technique with multiple sub-techniques, each with distinct telemetry:
- **MSBuild (T1127.001):** build engine running inline tasks/project logic.
- **ClickOnce (T1127.002):** deployment/activation chain via dfsvc.exe/dfshim.dll and related artifacts.
- **JamPlus (T1127.003):** build utility executing scripts via `.jam` build files.

When possible, detect at the sub-technique level for higher signal and lower false positives.

## 4. Procedure Examples
MITRE ATT&CK does not enumerate specific CTI procedure examples on the parent technique page.

## 5. Detection Guidance
Use a **behavior-chain** approach:

- **Non-dev context detection**
  - Alert when known developer utilities run on endpoints outside your “dev/build host” inventory.
  - Differentiate “developer hosts” vs. “general endpoints” in asset identity.

- **High-risk child process chains**
  - Developer utility → PowerShell/cmd/rundll32/regsvr32/wscript/mshta is high signal outside build pipelines.

- **Unsigned module load + user-writable execution**
  - Utility loads unsigned/user-writable DLLs or drops artifacts into `%TEMP%`, `%APPDATA%`, user profile, public folders, OneDrive sync paths.

- **Immediate network egress**
  - Parent utility starts and rapidly generates outbound connections (especially to rare domains/IPs).

### Data Source Notes
**MITRE Detection Strategy (DET0172 / AN0488) log sources:**
- Process Creation — Security 4688
- Module Load — Sysmon 7
- File Creation — Sysmon 11
- Network Connection Creation — Sysmon 3/22
- Process Metadata — AppLocker audit/blocks (developer utilities executing outside policy)

## 6. Response Guidance
1. **Triage**
   - Identify the developer utility executable, command line, parent chain, and host role (dev vs non-dev).
   - Determine payload lineage: what files were created, what children spawned, what network destinations were contacted.

2. **Contain**
   - Isolate affected host(s) if chaining indicates execution + egress.
   - Temporarily block the abused utility via application control where feasible (or scope to non-dev endpoints).

3. **Eradicate & recover**
   - Remove dropped artifacts and persistence discovered during follow-on investigation.
   - Enforce WDAC/AppLocker baselines by host role; limit developer utilities to approved endpoints and pipelines.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1127.001 - Trusted Developer Utilities Proxy Execution - MSBuild|T1127.001]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1127.002 - Trusted Developer Utilities Proxy Execution - ClickOnce|T1127.002]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1127.003 - Trusted Developer Utilities Proxy Execution - JamPlus|T1127.003]]

## 8. SOC Relevance
High:
- Strong correlation of signed/trusted process abuse with execution chains that evade allowlisting controls.
- Well-suited to correlation analytics (process + module load + file write + net egress).
- Best results when combined with strong asset role classification (dev vs non-dev).

## 9. Threat Actor Usage
No specific threat actor mappings are listed on the parent technique page.

## 10. Campaign Usage
No specific campaign mappings are listed on the parent technique page.

## 11. Malware Usage
No specific malware/software mappings are listed on the parent technique page.

## 12. Mitigations
- **Disable or Remove Feature or Program (M1042):** remove unneeded developer utilities in environments that don’t require them.
- **Execution Prevention (M1038):** block or restrict developer utilities with application control (WDAC/AppLocker) when not required.
- **Restrict Web-Based Content (M1021):** reduce ability to install/execute content from the internet via these utilities where applicable.

## 13. Testing & Validation
- Inventory developer utilities and classify allowed endpoints (build/dev hosts).
- Generate benign test executions on:
  - a dev host (expected/allowed), and
  - a non-dev host (should alert/block),
  then validate correlation alerts for suspicious child spawn, unsigned module load, file write, and egress.
- Confirm AppLocker/WDAC policy logging is ingested (audit + block events).

## 14. References
- MITRE. (2025, October 24). *Trusted Developer Utilities Proxy Execution (T1127).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1127/
- MITRE. (2025, October 21). *Behavior-chain, platform-aware detection strategy for T1127 Trusted Developer Utilities Proxy Execution (Windows) (DET0172).* MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0172/
- Desimone, J. (2024, August 6). *Dismantling Smart App Control.* Elastic Security Labs. https://www.elastic.co/security-labs/dismantling-smart-app-control

## 15. Notes
- Treat “developer utility on non-dev endpoint” as a high-signal enrichment feature.
- Maintain and regularly update an allowlist of legitimate parent orchestrators (CI/CD agents) to reduce noise.
