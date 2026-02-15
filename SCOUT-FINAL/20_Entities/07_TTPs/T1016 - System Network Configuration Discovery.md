---
entity_type: mitre_technique
technique_id: "T1016"
subtechnique_id: ""
technique_name: "System Network Configuration Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - ESXi
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
  - "[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]"
  - "[[30_CIPHER/05_Malware/S0552 - AdFind|AdFind (S0552)]]"
  - "[[30_CIPHER/05_Malware/S0099 - Arp|Arp (S0099)]]"
associated_campaigns: []
related_techniques:
  - "T1016.001"
  - "T1016.002"
detection_priority:
  - Medium
detection_maturity: ""
threat_score: 3
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
System Network Configuration Discovery covers adversary attempts to enumerate network configuration details (IP/MAC, routes, interfaces, DNS/DHCP settings, gateway/WINS, etc.) on endpoints, hypervisors (ESXi), and network devices.

## 2. Technical Overview
Common patterns:
- **Windows/macOS/Linux**: local utilities that report interfaces, routing tables, ARP cache, and resolver configuration.
- **Network devices**: CLI commands that show interface configuration and routes.
- **ESXi**: management CLIs (e.g., esxcli) to enumerate NICs and IP configuration.

This discovery frequently supports lateral movement planning, target selection (e.g., domain vs. workgroup), proxy/redirector detection, and understanding segmentation.

## 3. Subtechnique Considerations
This technique includes sub-techniques that often present different detection surfaces:
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1016.001 - System Network Configuration Discovery: Internet Connection Discovery|T1016.001]] (connectivity checks)
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1016.002 - System Network Configuration Discovery: Wi-Fi Discovery|T1016.002]] (wireless profiles/passwords; higher sensitivity)

## 4. Procedure Examples
Examples observed in public reporting include:
- **[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]** using OS utilities to gather network configuration details.
- **[[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]** using configuration discovery following exploitation.
- Malware such as **[[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]** enumerating network-related settings.

## 5. Detection Guidance
Treat this as a **baseline-noisy** technique; detections should emphasize:
- **Unusual parent/child** chains (Office app → cmd/shell → network discovery utility)
- **First-seen binaries** or execution from user-writable paths performing discovery
- **Burst behavior**: multiple discovery commands executed in rapid sequence (“discovery stack”)

Recommended detection pivots:
- Process creation telemetry for known network-discovery binaries/CLIs and their arguments.
- Scripting telemetry (PowerShell script block/logging) when network discovery cmdlets are invoked.
- Remote execution context: discovery run via PsExec/WMI/WinRM/SSH from non-admin endpoints.

### Data Source Notes
Commonly leveraged telemetry:
- Process creation + command line
- Command execution (PowerShell, bash/zsh history/audit)
- Network device CLI audit logs (where available)
- Hypervisor management logs (ESXi)

## 6. Response Guidance
1. **Confirm intent**: correlate discovery with authentication events, remote tooling, or suspicious process lineage.
2. **Scope across hosts**: identify other endpoints running similar discovery bursts from the same account/device.
3. **Hunt follow-on**: lateral movement attempts, service enumeration, SMB/RDP probing, credential access.

## 7. Related ATT&CK Content
- This technique: [[20_Entities/07_TTPs/TA0007 - Discovery/T1016 - System Network Configuration Discovery|T1016]]
- Sub-techniques:
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1016.001 - System Network Configuration Discovery: Internet Connection Discovery|T1016.001]]
  - [[20_Entities/07_TTPs/TA0007 - Discovery/T1016.002 - System Network Configuration Discovery: Wi-Fi Discovery|T1016.002]]

## 8. SOC Relevance
- Common in both benign admin activity and adversary recon—**context is everything**.
- High value when paired with: suspicious remote exec, unusual account context, or subsequent lateral movement.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338 (G0018)]]

## 10. Campaign Usage
- None listed.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]
- [[30_CIPHER/05_Malware/S0552 - AdFind|AdFind (S0552)]]
- [[30_CIPHER/05_Malware/S0099 - Arp|Arp (S0099)]]

## 12. Mitigations
Preventing discovery is difficult; focus on:
- Restricting unnecessary local admin rights and remote management exposure
- Application control for untrusted binaries and scripts
- Logging coverage (process + script) and SIEM correlations for discovery bursts

## 13. Testing & Validation
- Atomic Red Team test: https://www.atomicredteam.io/atomic-red-team/atomics/T1016  
Validate:
- Command-line capture for network discovery utilities
- Correlation logic that reduces noise (e.g., discovery burst + suspicious ancestry)

## 14. References
- MITRE ATT&CK. (n.d.). *System Network Configuration Discovery (T1016)*. https://attack.mitre.org/techniques/T1016/  
- CISA. (n.d.). *Eviction Strategies: System Network Configuration Discovery (T1016)*. https://www.cisa.gov/eviction-strategies-tool/info-attack/T1016  
- Atomic Red Team. (n.d.). *T1016 – System Network Configuration Discovery*. https://www.atomicredteam.io/atomic-red-team/atomics/T1016  

## 15. Notes
- Tune detections with allowlists for sanctioned IT tooling (SCCM, fleet scripts, endpoint health checks).
- Escalate when discovery is performed by new/unsigned binaries or immediately after suspicious initial execution.
