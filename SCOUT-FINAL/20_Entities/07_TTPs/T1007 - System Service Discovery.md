---
entity_type: mitre_technique

technique_id: "T1007"
subtechnique_id: ""
technique_name: "System Service Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - Linux
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
  - "G0006 - APT1"
  - "G0018 - admin@338"
  - "G0143 - Aquatic Panda"
associated_malware:
  - "S0154 - Cobalt Strike"
  - "S0638 - Babuk"
  - "S0570 - BitPaymer"
associated_campaigns: []
related_techniques:
  - "T1053 - Scheduled Task/Job"

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 2

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

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
System Service Discovery (T1007) captures adversary enumeration of running services/daemons and service configurations. Attackers use the results to identify security tooling, discover high-value services, plan privilege escalation, or decide whether to proceed with deeper infection.

## 2. Technical Overview
Typical behaviors:
- **Windows**: `sc query`, `sc qc`, `net start`, `tasklist /svc`, PowerShell `Get-Service`, WMI queries for service objects.
- **Linux/macOS**: `systemctl list-units`, `service --status-all`, listing init scripts (e.g., `/etc/init.d`), launchctl queries on macOS.
- **Security product discovery**: targeted checks for EDR/AV service names and status.

Detection value increases when service discovery is:
- executed by **untrusted binaries**, LOLBins, or unusual parent processes,
- performed in **bursts** across multiple hosts,
- followed by **defense evasion**, credential access, or lateral movement.

## 3. Subtechnique Considerations
- No sub-techniques.

## 4. Procedure Examples
Representative ATT&CK procedure examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]] used `net start` to collect service information.
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]] used `net start` and `tasklist` to list services.
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda (G0143)]] attempted to discover third-party EDR services.
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]] can enumerate services on compromised hosts.

## 5. Detection Guidance
High-value detection patterns:
- **CLI service enumeration commands** with suspicious parentage or first-seen binaries.
- **PowerShell service enumeration** from non-admin users, odd hosts, or via remote sessions.
- **EDR/AV-specific checks**: repeated lookups for known security service names.
- **Correlation rules**:
  - service discovery + process injection tooling
  - service discovery + credential access attempts
  - service discovery + service stop/disable actions shortly after

### Data Source Notes
MITRE Detection Strategy (DET0483) highlights:
- **Process Creation (DC0032)**:
  - Windows: Security 4688; Sysmon EID 1 (if deployed)
  - Linux: auditd EXECVE/execve
  - macOS: process start telemetry (EDR) / audit frameworks
- **Command Execution (DC0064)**:
  - Windows: PowerShell 4103–4106 (where enabled)
- Ensure command-line capture is enabled; without it, distinguishing benign admin activity becomes difficult.

## 6. Response Guidance
Triage checklist:
1. Identify **what enumerated** (generic listing vs. targeted EDR/AV service names).
2. Validate **user context** (interactive admin vs. unexpected service account).
3. Review **process tree** and **download/drop activity** preceding discovery.
4. Hunt for **follow-on actions**:
   - disabling security tools, modifying services, persistence via service creation.
5. Contain and reset affected credentials/sessions if discovery is part of a broader intrusion chain.

## 7. Related ATT&CK Content
- Tactic folder link:
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1007 - System Service Discovery|T1007]]

- Related technique references:
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1053 - Scheduled Task-Job|T1053]]

## 8. SOC Relevance
- Useful for detecting **tooling reconnaissance** and **security product discovery**.
- Pairs well with endpoint baselining: service enumeration is common for IT, but rarely from **user-workstation malware lineage**.
- Strong signal on servers where routine admin access is limited/controlled.

## 9. Threat Actor Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda (G0143)]]

## 10. Campaign Usage
- No campaign entries captured in this note.

## 11. Malware Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]
- [[30_CIPHER/05_Malware/S0638 - Babuk|Babuk (S0638)]]
- [[30_CIPHER/05_Malware/S0570 - BitPaymer|BitPaymer (S0570)]]

## 12. Mitigations
- Reduce the value of service discovery by hardening:
  - restrict local admin rights and remote service management privileges,
  - enforce application control and script controls (PowerShell, WMI),
  - protect and monitor security tooling configurations.
- For Windows, consider restricting who can query/modify services remotely and monitor administrative shares/remote management.

## 13. Testing & Validation
- Validate detections for:
  - Windows service enumeration commands + PowerShell `Get-Service`
  - Linux `systemctl`/`service` enumeration
- Reference safe testing content:
  - https://www.atomicredteam.io/atomic-red-team/atomics/T1007
- Unit test correlation: discovery → follow-on (service modification, persistence, defense evasion) within defined windows.

## 14. References
- MITRE. (2025). System Service Discovery (T1007). MITRE ATT&CK. https://attack.mitre.org/techniques/T1007/
- MITRE. (2025). Detection of System Service Discovery Commands Across OS Platforms (DET0483). MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0483/
- Splunk. (n.d.). Breaking Down Linux.Gomir: Understanding this Backdoor’s TTPs. https://www.splunk.com/en_us/blog/security/breaking-down-linux-gomir-understanding-this-backdoors-ttps.html
- Atomic Red Team. (n.d.). T1007: System Service Discovery. https://www.atomicredteam.io/atomic-red-team/atomics/T1007

## 15. Notes
- Consider separate detections for “generic service listing” vs. “EDR/AV name probing”.
- Add allowlists for known IT tooling and management agents to reduce noise.
