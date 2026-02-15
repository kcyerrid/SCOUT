---
entity_type: mitre_technique

technique_id: "T1033"
subtechnique_id: ""
technique_name: "System Owner/User Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources:
  - "Process Creation (DC0032)"
  - "Command Execution (DC0064)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "G0022 - APT3"
  - "G0050 - APT32"
  - "G0067 - APT37"
associated_malware:
  - "S0331 - Agent Tesla"
  - "S0534 - Bazar"
  - "S1025 - Amadey"
associated_campaigns: []
related_techniques:
  - "T1059.008 - Command and Scripting Interpreter: Network Device CLI"

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 2

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
System Owner/User Discovery (T1033) captures adversary attempts to identify the current user, logged-on users, or local account lists on endpoints and network devices. This enables environment-aware decision-making (e.g., privilege context verification, tailoring follow-on actions, targeting specific users).

## 2. Technical Overview
Common patterns include:
- **Local user context discovery**: `whoami`, `query user`, `w`, `who`, `id`, reading environment variables (e.g., `%USERNAME%`, `$USER`).
- **Account list enumeration**: OS tools/APIs to list local users (e.g., directory service queries on macOS/Linux).
- **Session/user presence checks**: enumerating interactive sessions and remote logins.
- **Network device user/session discovery**: device CLI commands (e.g., “show users”, “show ssh”) to identify active logins.

Key defender takeaway: this technique is often **early-stage** discovery and becomes higher signal when correlated with **remote access**, **privilege escalation**, **credential access**, or **lateral movement** activity.

## 3. Subtechnique Considerations
- No sub-techniques.

## 4. Procedure Examples
Representative ATT&CK procedure examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3 (G0022)]] executed `whoami` to verify elevated execution context.
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32 (G0050)]] collected usernames and executed `whoami` during victim profiling.
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]] collected the victim username as part of host profiling.

## 5. Detection Guidance
Prioritize detections that combine **process lineage + command intent + user context**:
- **Command-line hunting**: executions of `whoami`, `query user`, `net user`, `w`, `who`, `id`, `/etc/passwd` reads, macOS user listing commands, and network device “show users/show ssh”.
- **Suspicious parentage**: discovery spawned by Office, browsers, archive utilities, scripting engines, LOLBins, or newly dropped binaries.
- **Context anomalies**:
  - executed by **service accounts** that normally do not perform interactive discovery,
  - executed on **servers** with low admin interaction,
  - bursts across many hosts (automation-like discovery).
- **Network device correlation**: user/session discovery commands shortly after a new management-plane login, unusual source IPs, or outside change windows.

### Data Source Notes
MITRE Detection Strategy (DET0093) emphasizes:
- **Process Creation (DC0032)**:
  - Windows: Sysmon EID 1 / Security 4688 (where available)
  - Linux/macOS: auditd `execve` / process start telemetry
- **Command Execution (DC0064)**:
  - Windows PowerShell: 4103–4106 (module/script block where enabled)
- For network devices: management-plane audit logs/AAA (TACACS+/RADIUS), device command accounting, and configuration/session logs.

## 6. Response Guidance
Triage steps:
1. **Confirm legitimacy**: is this an expected admin workflow (IT scripts, compliance tooling)?
2. **Scope**: identify other hosts where the same actor/process executed similar discovery.
3. **Follow-on correlation**: within 5–30 minutes, look for:
   - remote execution, credential access attempts, new services/tasks, privilege escalation.
4. **Containment** (if suspicious): isolate host/account, revoke tokens/sessions, reset credentials where appropriate.
5. **Evidence capture**: process tree, full command line, script contents, and remote session provenance.

## 7. Related ATT&CK Content
- Tactic folder link:
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1033 - System Owner-User Discovery|T1033]]

- Related technique references (explicitly relevant):
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059.008 - Command and Scripting Interpreter - Network Device CLI|T1059.008]]

## 8. SOC Relevance
- **High-frequency technique** in real environments; detection value comes from **context and correlation**.
- Useful for **early intrusion detection** when paired with unusual initial access vectors, LOLBins, or persistence setup.
- Strong enrichment target for “**Discovery burst**” correlation rules.

## 9. Threat Actor Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3 (G0022)]]
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32 (G0050)]]
- [[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37 (G0067)]]

## 10. Campaign Usage
- No campaign entries captured in this note.

## 11. Malware Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]
- [[30_CIPHER/05_Malware/S0534 - Bazar|Bazar (S0534)]]
- [[30_CIPHER/05_Malware/S1025 - Amadey|Amadey (S1025)]]

## 12. Mitigations
Preventive controls are limited for discovery-by-design, but impact can be reduced:
- **Least privilege** and remove unnecessary local admin rights.
- Harden and monitor **remote administration** pathways (RDP/SSH/WMI/WinRM).
- Enforce **PowerShell** logging and constrained language mode where feasible.
- Centralize and alert on **network device command accounting** (AAA).

## 13. Testing & Validation
- Validate telemetry coverage for:
  - endpoint process creation + full command line
  - PowerShell logging (4104) where applicable
  - auditd exec telemetry on Linux/macOS
  - network device command accounting
- Use safe simulation/hunting validation such as Atomic Red Team references:
  - https://www.atomicredteam.io/atomic-red-team/atomics/T1033
- Create unit tests for detection logic to ensure:
  - allowlists for known admin tools,
  - alerts for unusual parents/users/time windows,
  - burst correlation works as intended.

## 14. References
- MITRE. (2025). System Owner/User Discovery (T1033). MITRE ATT&CK. https://attack.mitre.org/techniques/T1033/
- MITRE. (2025). Behavioral Detection of User Discovery via Local and Remote Enumeration (DET0093). MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0093/
- Cisco. (2024, August 28). Cisco IOS Security Command Reference: Commands S to Z (show users). Cisco. https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s5.html
- Atomic Red Team. (n.d.). T1033: System Owner/User Discovery. https://www.atomicredteam.io/atomic-red-team/atomics/T1033

## 15. Notes
- Consider separate detections for: (a) interactive host discovery, (b) remote user/session discovery, (c) network device user/session discovery.
- High signal when paired with “first-seen binary” or “post-exploitation framework” lineage.
