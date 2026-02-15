---
entity_type: mitre_technique
technique_id: "T1049"
subtechnique_id: ""
technique_name: "System Network Connections Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - ESXi
  - IaaS
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources: []
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]"
associated_campaigns: []
related_techniques:
  - "T1016"
  - "T1046"
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
System Network Connections Discovery involves enumerating active or historical network connections/sessions on a host (or, in some contexts, connected systems/services in cloud virtual networks or network devices). This can reveal pivot targets, admin shares, RDP sessions, listening services, and active C2 channels.

## 2. Technical Overview
Common behaviors:
- Listing active TCP/UDP connections and listening sockets.
- Enumerating SMB sessions and mapped resources (Windows).
- On macOS/Linux, listing open network handles/sockets via system utilities.
- On network devices, using CLI to display sockets/sessions.
- In cloud/IaaS, mapping virtual network connectivity and attached resources.

This technique often appears during internal recon and before lateral movement or staging.

## 3. Subtechnique Considerations
- N/A (no sub-techniques).
- Detection approaches should differ by platform:
  - **Windows**: focus on suspicious discovery commands/cmdlets and session enumeration.
  - **Linux/macOS**: focus on socket/process inspection tools executed from unusual contexts.
  - **Network devices**: rely on CLI audit logs and privileged session monitoring.
  - **ESXi/IaaS**: track management CLI usage and cloud audit trails.

## 4. Procedure Examples
- **[[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]** used local enumeration to display network connections after exploitation.
- **[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]** used commands to list network connections/resources.
- **[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]** has used network connection enumeration as part of reconnaissance.
- Tooling such as **[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]** can generate session/connection visibility from compromised hosts.

## 5. Detection Guidance
Core detection strategy: identify **enumeration tooling** + **suspicious lineage**.

High-value detections:
- Network connection enumeration executed by **rare or unsigned binaries**, or by shells spawned from user-facing apps.
- **Burst recon**: multiple enumeration commands within a short time window (connections + routes + ARP + shares).
- Enumeration executed in the context of **remote administration** (WMI/WinRM/SSH) from unusual source hosts.

Correlations that increase fidelity:
- Enumeration immediately followed by authentication events to remote hosts (SMB/RDP/WinRM).
- Enumeration followed by service creation, scheduled tasks, or remote tool transfer.

### Data Source Notes
Telemetry commonly required:
- Process creation + command line
- PowerShell logging (Windows) for network connection cmdlets
- Network device CLI audit logs (device-side)
- ESXi and cloud audit logs (management actions)
- EDR socket/process telemetry when available

## 6. Response Guidance
1. **Validate process origin**: signer, path, prevalence, and whether executed interactively or remotely.
2. **Pivot to lateral movement**: review subsequent logons, remote service usage, and internal scanning.
3. **Contain** suspicious tooling and block hashes/paths; consider isolating affected endpoints if recon is part of an active intrusion.
4. **Preserve evidence**: capture volatile context (process tree, network connections) and relevant logs.

## 7. Related ATT&CK Content
- This technique: [[20_Entities/07_TTPs/TA0007 - Discovery/T1049 - System Network Connections Discovery|T1049]]
- Related discovery: [[20_Entities/07_TTPs/TA0007 - Discovery/T1016 - System Network Configuration Discovery|T1016]]

## 8. SOC Relevance
- Common admin activity exists, but suspicious contexts (new binaries, odd parents, remote execution) make it a strong hunting pivot.
- Particularly useful for identifying staging before lateral movement or identifying active C2.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]

## 10. Campaign Usage
- None listed.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]

## 12. Mitigations
- Limit local admin and restrict remote management exposure.
- Application control to prevent execution of unauthorized recon tooling.
- Centralized logging for process + script + admin session activity.

## 13. Testing & Validation
- Atomic Red Team test: https://www.atomicredteam.io/atomic-red-team/atomics/T1049  
Validate:
- Capture of process + command-line telemetry for connection enumeration
- Correlation rules (enumeration → lateral movement indicators)

## 14. References
- MITRE ATT&CK. (n.d.). *System Network Connections Discovery (T1049)*. https://attack.mitre.org/techniques/T1049/  
- Splunk Threat Research Team. (2025). *Network Connection Discovery With Netstat* (analytic). https://research.splunk.com/endpoint/2cf5cc25-f39a-436d-a790-4857e5995ede/  
- Atomic Red Team. (n.d.). *T1049 – System Network Connections Discovery*. https://www.atomicredteam.io/atomic-red-team/atomics/T1049  

## 15. Notes
- Keep an allowlist for legitimate troubleshooting tools; alert on atypical usage patterns (non-IT endpoints, odd ancestry, high-frequency bursts).
