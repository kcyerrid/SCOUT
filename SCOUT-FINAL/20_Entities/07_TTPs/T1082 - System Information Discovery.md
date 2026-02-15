---
entity_type: mitre_technique

technique_id: "T1082"
subtechnique_id: ""
technique_name: "System Information Discovery"

tactic:
  - TA0007 - Discovery
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
  - "[[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338]]"
  - "[[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]]"
  - "[[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]"
  - "[[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1028 - Action RAT|Action RAT]]"
  - "[[30_CIPHER/05_Malware/S0045 - ADVSTORESHELL|ADVSTORESHELL]]"
  - "[[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]]"
  - "[[30_CIPHER/05_Malware/S1167 - AcidPour|AcidPour]]"
associated_campaigns: []
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

# T1082 - System Information Discovery

## 1. Summary
Adversaries collect system information (e.g., OS version, hostname, architecture, hardware details) to profile a host, validate execution conditions, and guide follow-on behaviors such as payload selection, privilege escalation decisions, and targeting.

## 2. Technical Overview
System information discovery is performed via:
- **Native OS utilities** and APIs that reveal OS, hardware, and configuration details
- **Scripting** (PowerShell/WMI on Windows; shell commands on Linux/macOS)
- **Network device CLI** commands to determine device OS/version/hardware
- **Cloud APIs** in IaaS to enumerate instance/VM details (authenticated calls)

Common data collected:
- Hostname, domain/workgroup (where applicable)
- OS name/version/build, kernel version, patches/hotfix context
- CPU architecture, memory, disk, system model identifiers
- On hypervisors (e.g., ESXi): platform version and host identifiers

## 3. Subtechnique Considerations
- No sub-techniques.
- This technique is extremely common; detection value increases when you treat it as a **node in a behavior chain** rather than a standalone alert.

## 4. Procedure Examples
MITRE procedure examples include:
- Numerous malware families gathering OS/host identifiers (e.g., [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]], [[30_CIPHER/05_Malware/S1028 - Action RAT|Action RAT]]).
- Threat groups and operators collecting OS/system details post-compromise (e.g., [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338]], [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]], [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]] listed on the technique page).
- Linux/embedded targeting where system identification supports destructive operations (e.g., [[30_CIPHER/05_Malware/S1167 - AcidPour|AcidPour]] listed on the technique page).

## 5. Detection Guidance
Because this is common for admins and software installers, detections should emphasize **context**:

High-signal patterns:
- System info discovery from suspicious parent processes (Office → script host, browser → dropped binary).
- Discovery by **non-interactive accounts** or from endpoints that do not normally run inventory tooling.
- Repeated discovery across multiple hosts in a short period (automation consistent with post-compromise playbooks).

Behavior-chain analytics:
- System info discovery → credential access attempts → remote discovery/lateral movement
- System info discovery → security tool discovery → tampering/exclusions
- System info discovery → payload staging/execution shortly after

### Data Source Notes
Best telemetry:
- **Endpoint**: process creation, command line, parent/child lineage; script telemetry (PowerShell, shell).
- **Cloud**: audit logs for instance/VM describe/list calls.
- **Network devices**: CLI command auditing for version/system show commands.
- **ESXi**: SSH/session auditing and command telemetry where available.

## 6. Response Guidance
1. **Triage the initiating process**: signer, prevalence, and ancestry.
2. **Validate principal and host role**: admin jump host vs user workstation.
3. **Pivot to follow-on behaviors**: privilege escalation, credential access, remote execution attempts, defense evasion.
4. **Collect artifacts**: preserve process tree and script contents that performed discovery.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1082 - System Information Discovery|T1082]]

## 8. SOC Relevance
- Medium standalone value; high value when chained.
- Useful to time-bound “post-compromise initialization” phases for hunting and IR scoping.

## 9. Threat Actor Usage
Examples included on the technique page:
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338]]
- [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]]
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]
- [[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]

## 10. Campaign Usage
- Not pinned here; correlate to your incident’s compromise timeline.

## 11. Malware Usage
Examples included on the technique page:
- [[30_CIPHER/05_Malware/S1028 - Action RAT|Action RAT]]
- [[30_CIPHER/05_Malware/S0045 - ADVSTORESHELL|ADVSTORESHELL]]
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]]
- [[30_CIPHER/05_Malware/S1167 - AcidPour|AcidPour]]

## 12. Mitigations
Preventive controls are limited because discovery uses legitimate features. Focus on:
- Least privilege and scripting control hardening
- Strong endpoint logging (process + script)
- Cloud IAM least privilege (limit broad describe/list rights) and alerting on anomalous inventory calls

## 13. Testing & Validation
- Validate in a lab across platforms:
  - Windows (native inventory and PowerShell/WMI)
  - Linux/macOS (shell-based system info)
  - Cloud (describe/list instance APIs)
  - Network devices (show version/system)
- Confirm your detections capture:
  - parent process context
  - command-line arguments
  - identity + host role metadata

## 14. References
- MITRE ATT&CK. (n.d.). *System Information Discovery (T1082).* https://attack.mitre.org/techniques/T1082/
- MITRE ATT&CK. (n.d.). *System Discovery via Native and Remote Utilities (DET0525).* https://attack.mitre.org/detectionstrategies/DET0525/
- Microsoft. (n.d.). *systeminfo.* https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo

## 15. Notes
- Treat system information discovery as the “initialization step” in many intrusions—optimize detections around what it enables next.
