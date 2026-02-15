---
entity_type: mitre_technique

technique_id: "T1673"
subtechnique_id: ""
technique_name: "Virtual Machine Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - ESXi
  - Linux
  - Windows
  - macOS
datasources:
  - "Command Execution (DC0064)"
  - "Process Creation (DC0032)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "G1048 - UNC3886"
associated_malware:
  - "S1096 - Cheerscrypt"
  - "S1242 - Qilin"
  - "S1217 - VIRTUALPITA"
associated_campaigns: []
related_techniques:
  - "T1059.012 - Command and Scripting Interpreter: Hypervisor CLI"
  - "T1489 - Service Stop"
  - "T1486 - Data Encrypted for Impact"

detection_priority:
  - High

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
Virtual Machine Discovery (T1673) is adversary enumeration of virtual machines (VMs) to identify targets for subsequent actions. In hypervisor environments (notably ESXi), discovery may precede disruptive operations (e.g., stopping VM-related services or encrypting VM files).

## 2. Technical Overview
Key behaviors include execution of hypervisor/virtualization management tooling to list guests:
- **ESXi**: `esxcli vm process list`, `vim-cmd vmsvc/getallvms` (and related host tooling).
- **Linux**: `virsh list`, queries of libvirt/qemu artifacts, VirtualBox/VMware tooling where installed.
- **Windows/macOS**: PowerShell Hyper-V `Get-VM`, virtualization product CLIs (e.g., VirtualBox tooling) when present.

Defender focus: these commands are typically constrained to admin workflows; **unexpected invocation** is a strong signal, especially on ESXi/hypervisor management planes.

## 3. Subtechnique Considerations
- No sub-techniques.

## 4. Procedure Examples
Representative ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S1096 - Cheerscrypt|Cheerscrypt (S1096)]] leveraged `esxcli vm process list` to gather running VM lists.
- [[30_CIPHER/05_Malware/S1242 - Qilin|Qilin (S1242)]] can detect virtual machine environments.
- [[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886 (G1048)]] used scripts to enumerate ESXi hypervisors and guest VMs.
- [[30_CIPHER/05_Malware/S1217 - VIRTUALPITA|VIRTUALPITA (S1217)]] can target specific guest VMs for script execution.

## 5. Detection Guidance
High-signal detections:
- **Hypervisor command detection**: alert on VM listing commands issued by non-standard users or from unusual parent processes/sessions.
- **Session provenance**: correlate with new SSH/management logins, rare source IPs, or abnormal session timing.
- **Behavior sequencing**:
  - VM discovery → VM power operations / service stop → encryption/impact behaviors
- **Asset-based controls**:
  - treat ESXi and hypervisor management nodes as **Tier 0/critical** and apply stricter alerting thresholds.

### Data Source Notes
MITRE Detection Strategy (DET0199) highlights monitoring for hypervisor management commands that enumerate VMs:
- **Command Execution (DC0064)**: command audit telemetry for `esxcli`, `vim-cmd`, `virsh`, virtualization CLIs.
- **Process Creation (DC0032)**: process launch telemetry where available (EDR/host auditing).
- On ESXi/network management planes, ensure **command accounting** and **auth/session logs** are centralized.

## 6. Response Guidance
1. Confirm whether the command aligns with a legitimate maintenance window and known admin identity.
2. Verify **authentication path**: who logged in, from where, and whether MFA/conditional access was satisfied.
3. Immediately assess for follow-on actions:
   - service stop, VM power operations, datastore encryption/write activity.
4. If suspicious:
   - isolate management access, rotate privileged credentials/keys,
   - disable untrusted sessions and restrict management-plane ingress,
   - preserve logs (ESXi shell history where applicable, auth logs, EDR telemetry).

## 7. Related ATT&CK Content
- Tactic folder link:
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1673 - Virtual Machine Discovery|T1673]]

- Related technique references:
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059.012 - Command and Scripting Interpreter - Hypervisor CLI|T1059.012]]
  - [[20_Entities/07_TTPs/TA0040 - Impact/T1489 - Service Stop|T1489]]
  - [[20_Entities/07_TTPs/TA0040 - Impact/T1486 - Data Encrypted for Impact|T1486]]

## 8. SOC Relevance
- Strong signal in hypervisor environments due to **low baseline frequency** of VM listing commands.
- Highly relevant for ransomware-prevention monitoring on ESXi and virtualization stacks.
- Ideal for tiered alerting: suspicious on endpoints, **critical** on hypervisors.

## 9. Threat Actor Usage
Observed in ATT&CK procedure examples:
- [[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886 (G1048)]]

## 10. Campaign Usage
- No campaign entries captured in this note.

## 11. Malware Usage
Observed in ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S1096 - Cheerscrypt|Cheerscrypt (S1096)]]
- [[30_CIPHER/05_Malware/S1242 - Qilin|Qilin (S1242)]]
- [[30_CIPHER/05_Malware/S1217 - VIRTUALPITA|VIRTUALPITA (S1217)]]

## 12. Mitigations
- Restrict hypervisor management access (jump hosts, network segmentation, MFA, allowlists).
- Disable or tightly control ESXi Shell/SSH where possible; monitor and alert when enabled.
- Apply least privilege for virtualization admins; separate duties and use just-in-time access.
- Maintain immutable/offline backups and monitor datastore write patterns.

## 13. Testing & Validation
- Validate that hypervisor command execution telemetry is collected and searchable.
- Create detections for:
  - VM enumeration commands outside approved admin toolchains
  - enumeration followed by disruptive actions within defined windows
- Reference safe testing content:
  - https://www.atomicredteam.io/atomic-red-team/atomics/T1673

## 14. References
- MITRE. (2025). Virtual Machine Discovery (T1673). MITRE ATT&CK. https://attack.mitre.org/techniques/T1673/
- MITRE. (2025). Detection Strategy for Virtual Machine Discovery (DET0199). MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0199/
- CrowdStrike. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. CrowdStrike Blog. https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/
- Atomic Red Team. (n.d.). T1673: Virtual Machine Discovery. https://www.atomicredteam.io/atomic-red-team/atomics/T1673

## 15. Notes
- Treat hypervisor VM discovery as a “stop-the-line” alert in environments with limited admin population.
- Ensure command accounting and admin session attribution are reliable (shared accounts severely degrade detection/IR).
