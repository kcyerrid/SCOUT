---
entity_type: mitre_technique

technique_id: "T1124"
subtechnique_id: ""
technique_name: "System Time Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - ESXi
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources:
  - "Process Creation (DC0032)"
  - "Command Execution (DC0064)"
  - "OS API Execution (DC0021)"
  - "Module Load (DC0016)"
  - "Scheduled Job Creation (DC0001)"
  - "Scheduled Job Metadata (DC0005)"
  - "Process Metadata (DC0034)"
  - "User Account Authentication (DC0002)"
  - "File Creation (DC0039)"
  - "Process Access (DC0035)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "G0060 - BRONZE BUTLER"
  - "G0046 - FIN7"
  - "G0114 - Chimera"
associated_malware:
  - "S0331 - Agent Tesla"
  - "S0115 - Crimson"
  - "S0534 - Bazar"
associated_campaigns: []
related_techniques:
  - "T1053 - Scheduled Task/Job"
  - "T1614 - System Location Discovery"

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
System Time Discovery (T1124) is the collection of system time/time zone/uptime from local or remote systems. Adversaries use this to infer locale, coordinate operations, implement time bombs/delays, or support scheduling and conditional execution.

## 2. Technical Overview
Common behaviors:
- **Windows**: `net time \\host`, `w32tm /tz`, time-related API calls (e.g., GetTickCount) to obtain uptime.
- **Linux**: `date`, `timedatectl`, `hwclock`, reading `/etc/timezone` or `/proc/uptime`, direct syscalls (e.g., `time()`).
- **macOS**: `systemsetup -gettimezone`, system calls and time APIs.
- **Network Devices**: device CLI (e.g., `show clock detail`) to read time configuration.
- **ESXi**: `esxcli system clock get` to read time.

High signal scenarios:
- time discovery followed by **task creation**, **large sleep/delay**, or **conditional execution**.
- time discovery executed by **untrusted binaries** or unusual user contexts.

## 3. Subtechnique Considerations
- No sub-techniques.

## 4. Procedure Examples
Representative ATT&CK procedure examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER (G0060)]] used `net time` to check local time.
- [[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7 (G0046)]] used scripts to execute `net time`.
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]] collected timestamps/time information during profiling.

## 5. Detection Guidance
Detections should focus on **intent + sequencing**:
- **Direct time query commands** (platform-specific) with suspicious parents or rare prevalence.
- **Behavior chains**:
  - time discovery → scheduled task creation/modification (Windows Task Scheduler, cron/at) within a short window
  - time discovery → long sleep/delay APIs or loops
- **Remote time queries**: time discovery against multiple hosts can indicate automated recon.

### Data Source Notes
MITRE Detection Strategy (DET0151) provides a behavior-chain approach with broad telemetry coverage:
- **Process Creation (DC0032)**: 4688 / Sysmon EID 1 / auditd EXECVE
- **Command Execution (DC0064)**: PowerShell 4103–4106, shell command telemetry
- **OS API Execution (DC0021)**: API/syscall monitoring for time-related calls (use selectively due to cost)
- **Scheduled Job Creation/Metadata (DC0001/DC0005)**: TaskScheduler/cron signals for follow-on actions
- Additional enrichment: **Process Metadata (DC0034)**, **Module Load (DC0016)**, **File Creation (DC0039)**, **User Account Authentication (DC0002)**

## 6. Response Guidance
1. Determine if execution aligns with known maintenance tooling (NTP checks, monitoring agents).
2. Identify whether it is paired with scheduling/delay behavior (tasks, cron, large sleep).
3. Validate the initiating user/session (interactive admin vs. suspicious remote session).
4. If malicious:
   - contain host/account,
   - review follow-on persistence or execution chains,
   - collect process tree, scripts, and remote access telemetry.

## 7. Related ATT&CK Content
- Tactic folder link:
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1124 - System Time Discovery|T1124]]

- Related technique references:
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1053 - Scheduled Task-Job|T1053]]
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1614 - System Location Discovery|T1614]]

## 8. SOC Relevance
- Valuable as an **early-stage recon** indicator and as a **precursor** to time-based evasion or scheduled persistence.
- Best used as a **correlation feature** in broader detections rather than a standalone high-severity alert.

## 9. Threat Actor Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER (G0060)]]
- [[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7 (G0046)]]
- [[30_CIPHER/03_Threat_Actors/G0114 - Chimera|Chimera (G0114)]]

## 10. Campaign Usage
- No campaign entries captured in this note.

## 11. Malware Usage
Observed in ATT&CK procedure examples (representative):
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]
- [[30_CIPHER/05_Malware/S0115 - Crimson|Crimson (S0115)]]
- [[30_CIPHER/05_Malware/S0534 - Bazar|Bazar (S0534)]]

## 12. Mitigations
- Restrict and monitor remote administration (WMI/WinRM/SSH) and privileged scheduling interfaces.
- Enforce scripting controls and logging (PowerShell, shell auditing).
- Segment and monitor management-plane access to network devices and hypervisors.

## 13. Testing & Validation
- Validate detection chains: time query → scheduled job creation or delay.
- Ensure coverage for time-related commands on each platform in scope (Windows/Linux/macOS/ESXi/network devices).
- Reference safe testing content:
  - https://www.atomicredteam.io/atomic-red-team/atomics/T1124

## 14. References
- MITRE. (2025). System Time Discovery (T1124). MITRE ATT&CK. https://attack.mitre.org/techniques/T1124/
- MITRE. (2025). Behavior-chain, platform-aware detection strategy for T1124 System Time Discovery (DET0151). MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0151/
- ANY.RUN. (n.d.). Malware With Delayed Execution. ANY.RUN Blog. https://any.run/cybersecurity-blog/time-bombs-malware-with-delayed-execution/
- Atomic Red Team. (n.d.). T1124: System Time Discovery. https://www.atomicredteam.io/atomic-red-team/atomics/T1124

## 15. Notes
- Consider separate alerting tiers: (1) standalone time query (low), (2) time query + follow-on scheduling/delay (medium/high), (3) time query in intrusion chain with other TTPs (high).
