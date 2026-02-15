---
entity_type: mitre_technique

technique_id: "T1216"
subtechnique_id: ""
technique_name: "System Script Proxy Execution"

tactic:
  - Defense Evasion
platforms:
  - Windows
datasources:
  - Process Creation
  - Command Execution
  - Module Load
  - Process Access
  - File Creation

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - T1216.001
  - T1216.002

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

created: 2026-01-06
updated: 2026-01-06

contributors:
  - Praetorian
  - Wes Hurd
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
System Script Proxy Execution is a defense-evasion technique where adversaries leverage trusted/signed scripts (often Microsoft-provided or default Windows scripts) to **proxy execution** of malicious content. The trusted parent can help bypass application control, reputation-based defenses, and some signature validation assumptions—especially when defenders focus on “unknown binaries” rather than **signed script hosts and their arguments**.

## 2. Technical Overview
**Core idea:** Use a trusted script (and often a trusted interpreter such as `wscript.exe`/`cscript.exe`) as the **execution wrapper** so the observable “parent” appears legitimate.

Defender-relevant behaviors:
- **Signed Microsoft script usage** in contexts that don’t align with endpoint role (non-admin workstation, non-IT user, etc.)
- Script hosts (`wscript.exe`, `cscript.exe`) executing scripts from:
  - non-standard paths
  - user-writable locations
  - recently written/rarely executed scripts
- **Proxy indicators in command line** (e.g., arguments that reference external content, embedded secondary interpreters, or suspicious delimiters)
- Rapid follow-on behaviors after proxy execution:
  - child process spawning (LOLBins, interpreters)
  - payload staging and execution from user-writable paths
  - unusual module loads
  - suspicious process access events (credential theft / injection adjacency)

Primary subtechniques in ATT&CK:
- **T1216.001 PubPrn**: scriptlet/remote payload proxying patterns
- **T1216.002 SyncAppvPublishingServer**: proxying embedded PowerShell via a Microsoft VBScript used in App-V workflows

## 3. Subtechnique Considerations
This parent technique is broad; detections should generally be **implemented at subtechnique granularity** to reduce false positives:
- **PubPrn** tends to be network-reachable / remote payload proxy behavior and is frequently high-signal in modern environments.
- **SyncAppvPublishingServer** is typically rare unless App-V is in use; it often includes **embedded PowerShell** in command line, which can be scored for obfuscation/encoding.

## 4. Procedure Examples
MITRE ATT&CK does not enumerate specific CTI procedure examples on the parent technique page (procedure examples may appear under sub-techniques instead).

## 5. Detection Guidance
Build detections around **(a) script host lineage** and **(b) argument-level semantics**, then correlate with **post-execution behaviors**.

High-signal detection patterns:
- **Unusual signed-script execution** (first-seen on host/user; rare across fleet)
- `wscript.exe`/`cscript.exe` executing **Microsoft-supplied scripts** with anomalous parameters
- **Signed parent → unsigned child** correlation (payload execution initiated by a signed script chain)
- **Script host spawning**:
  - command interpreters or scripting engines
  - binaries from user-writable directories
- **Short-window correlation (0–30 minutes)**:
  - script host execution → child process spawn + file creation + suspicious network egress

Tuning / reduction of noise:
- Maintain allowlists for legitimate enterprise scripts and IT automation tooling.
- Baseline by endpoint role (developer, IT admin workstation, kiosk, standard user).

### Data Source Notes
Minimum telemetry to support high-fidelity detections:
- **Process Creation**: parent/child chain and full command line for `wscript.exe`, `cscript.exe`, and invoked scripts
- **Command Execution**: script block / command line visibility (where available) for secondary interpreters launched via the script
- **Module Load**: suspicious/unsigned loads in script host or immediate children
- **Process Access**: suspicious handle access indicative of injection or credential theft follow-on
- **File Creation**: payload drops and scriptlet staging linked to the proxy execution window

## 6. Response Guidance
1. **Triage**
   - Capture full process tree (script host + script path + arguments + children).
   - Determine script provenance (signed Microsoft/default script vs newly introduced file).
2. **Contain**
   - If suspicious children and egress are present, isolate host and block active sessions.
   - Temporarily block abused script(s) or execution paths via application control if operationally safe.
3. **Investigate**
   - Retrieve referenced artifacts (scripts, downloaded content, child payloads) and compute hashes.
   - Expand scope: hunt for same command-line patterns across the fleet.
4. **Harden**
   - Restrict unnecessary signed scripts and script hosts on non-admin endpoints.
   - Enforce strong application control and reduce “living off the land” surface area.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1216 - System Script Proxy Execution|T1216]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1216.001 - System Script Proxy Execution: PubPrn|T1216.001]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1216.002 - System Script Proxy Execution: SyncAppvPublishingServer|T1216.002]]

## 8. SOC Relevance
**High** for Windows environments:
- Common bypass theme: **trusted parent process** and “signed utility” blending
- Strong signal when paired with:
  - argument-based detections (proxy indicators)
  - post-execution correlation (drop + execute, LOLBin chain, egress)
- Ideal for correlation rules rather than single-event alerts

## 9. Threat Actor Usage
No specific threat actor mappings are listed on the parent technique page.

## 10. Campaign Usage
No specific campaign mappings are listed on the parent technique page.

## 11. Malware Usage
No specific malware/software mappings are listed on the parent technique page.

## 12. Mitigations
- **M1038 – Execution Prevention**: Use application control to block execution of signed scripts that are not required in your environment, and constrain script hosts where feasible (especially on standard user endpoints).

## 13. Testing & Validation
Defender-safe validation ideas:
- Verify EDR/Sysmon captures full command lines for `wscript.exe`/`cscript.exe` and script paths.
- Validate detections fire on:
  - rare Microsoft script execution across endpoints
  - suspicious parameter patterns (proxy indicators)
  - signed script host → suspicious child process + file creation correlation
- Confirm playbooks capture required artifacts (script file, child payloads, network destinations).

## 14. References
- MITRE ATT&CK. (n.d.). *System Script Proxy Execution (T1216).* https://attack.mitre.org/techniques/T1216/
- MITRE ATT&CK. (2025, October 21). *Detection of Script-Based Proxy Execution via Signed Microsoft Utilities (DET0466).* https://attack.mitre.org/detectionstrategies/DET0466/
- LOLBAS Project. (n.d.). *LOLBAS – Living Off The Land Binaries, Scripts and Libraries.* https://lolbas-project.github.io/

## 15. Notes
- Treat “signed script execution on non-admin endpoints” as a policy violation candidate.
- Prefer **argument-aware** analytics plus **behavior-chain** correlation to minimize false positives.
