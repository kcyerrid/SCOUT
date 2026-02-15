---
entity_type: mitre_technique
technique_id: T1072
subtechnique_id: ""
technique_name: Software Deployment Tools
tactic:
  - TA0002 - Execution
  - TA0008 - Lateral Movement
platforms:
  - Linux
  - Network Devices
  - SaaS
  - Windows
  - macOS
datasources:
  - Process Creation (DC0032)
  - Application Log Content (DC0038)
  - Command Execution (DC0064)
  - Network Traffic Flow (DC0078)
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]"
  - "[[30_CIPHER/03_Threat_Actors/G1051 - Medusa Group|Medusa Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]"
  - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]"
  - "[[30_CIPHER/03_Threat_Actors/G0091 - Silence|Silence]]"
  - "[[30_CIPHER/03_Threat_Actors/G0028 - Threat Group-1314|Threat Group-1314]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1053 - AvosLocker|AvosLocker]]"
  - "[[S0041 - Wiper|Wiper]]"
associated_campaigns:
  - C0018 - C0018
related_techniques: []
detection_priority:
  - High
detection_maturity: ""
threat_score: 5
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

# T1072 - Software Deployment Tools

## 1. Summary
Adversaries may abuse centralized software deployment and endpoint management platforms (on-prem, cloud, and network-device management) to execute commands at scale and pivot across environments. This is high-impact “management-plane” abuse: a single compromise can translate into broad remote execution, rapid ransomware deployment, or coordinated destructive actions.

## 2. Technical Overview
Software Deployment Tools covers adversary use of legitimate deployment/configuration systems (e.g., endpoint management suites, orchestration/config management, cloud run-command services, and network device managers) to:
- **Execute code remotely** (often as **SYSTEM/root** or a privileged agent context)
- **Push binaries/scripts** to many endpoints simultaneously
- **Abuse trusted channels** (signed agents, allowed admin consoles, standard management ports)
- **Blend into admin operations** (scheduled maintenance windows, expected parent processes/services)

Common defender-relevant behaviors:
- Execution initiated by known management agents **outside normal windows** or **targeting atypical hosts**
- Use of deployment consoles or APIs from **unusual admin accounts**, **unusual source IPs**, or **unusual org/tenant contexts**
- Sudden burst of remote executions, package pushes, or configuration changes inconsistent with baseline

## 3. Subtechnique Considerations
This technique has **no sub-techniques**. Model granularity instead via:
- **Control plane type** (on-prem endpoint management vs. cloud run-command vs. network device manager)
- **Execution context** (SYSTEM/root agent vs. user context)
- **Target scope** (single OU/site vs. enterprise-wide, cross-tenant/cross-subscription)

## 4. Procedure Examples
Observed usage examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]] compromised a management/deployment system (McAfee ePO) to distribute malware as a deployment task.
- Campaign **C0018** used a legitimate deployment tool (PDQ Deploy) to move [[30_CIPHER/05_Malware/S1053 - AvosLocker|AvosLocker]] and tools across a network.
- [[30_CIPHER/03_Threat_Actors/G1051 - Medusa Group|Medusa Group]] used software deployment/management solutions (e.g., BigFix, PDQ Deploy) to deploy encryption payloads.
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]] used commercially available remote execution tooling consistent with management-plane style deployment.
- [[30_CIPHER/03_Threat_Actors/G0028 - Threat Group-1314|Threat Group-1314]] used an endpoint management platform (Altiris) for lateral movement.
- [[S0041 - Wiper|Wiper]] was assessed as distributed via a patch management system tied to commonly deployed security software.

## 5. Detection Guidance
Prioritize detections that treat management-plane execution as **high-signal** unless strongly baselined.

High-value detection themes:
- **Parent/launcher anomalies**: Management agents spawning unusual children (e.g., PowerShell/cmd, shells, scripting hosts) or launching from non-standard paths.
- **Timing anomalies**: Deployment executions outside approved maintenance windows or change windows.
- **Scope anomalies**: Large fan-out pushes, first-time targeting of sensitive tiers (DCs, management servers, build agents, hypervisors).
- **Identity anomalies**: New/rare admin accounts, MFA-bypassed sessions, non-interactive service principals used unusually, or privilege changes preceding pushes.
- **Source anomalies**: Console/API calls from new IP ranges, unmanaged devices, TOR/VPN egress, or unusual geolocation.
- **Content anomalies**: Unsigned/unapproved packages, scripts with suspicious arguments, or payload hashes not seen in software catalog.

Recommended correlation (examples):
- Deployment-tool log entries **→** endpoint process creation on multiple hosts within a short window
- Deployment-tool activity **→** immediate disablement of security controls or service stop events
- Deployment-tool activity **→** rapid staging of binaries in shared working directories, temp paths, or agent cache locations

### 5.1. Data Source Notes
Minimum telemetry for useful coverage:
- **Process Creation (DC0032)**  
  - Windows: Security 4688 / Sysmon process creation (where available) on endpoints and management servers  
  - Linux/macOS: auditd execve / unified logs to capture agent-spawned execution
- **Application Log Content (DC0038)**  
  - Endpoint management suite logs (SCCM/Intune/MDM/orchestration server logs), job history, package/task metadata
  - Network device manager logs for config pushes/reboots/firmware updates
- **Command Execution (DC0064)**  
  - Cloud control plane audit logs (e.g., run-command invocations) with actor identity, target set, payload details
- **Network Traffic Flow (DC0078)**  
  - Flows from management servers to endpoints (fan-out spikes), unusual east-west deployment traffic

## 6. Response Guidance
1. **Contain the management plane first**: isolate/disable the deployment platform’s ability to push tasks (pause agents, revoke API keys/tokens, disable distribution points) while preserving evidence.
2. **Credential and token reset**: rotate privileged accounts/service principals tied to the tool; enforce MFA; revoke sessions.
3. **Scope and impact assessment**: identify all tasks/jobs executed in the suspicious window; enumerate targeted endpoints; collect executed payload hashes and command lines.
4. **Endpoint triage**: prioritize high-value tiers and hosts that received pushes; look for secondary persistence and credential theft immediately following pushes.
5. **Hardening & recovery**: rebuild/restore the management server(s) from known-good backups; validate configuration integrity and admin RBAC; re-onboard agents with verified packages only.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0002 - Execution/T1072 - Software Deployment Tools|T1072]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1072 - Software Deployment Tools|T1072]]

## 8. SOC Relevance
- **High-fidelity hunting**: “management agent → shell/scripting child process” on endpoints is often a strong anomaly.
- **Ransomware early warning**: many enterprise-wide encryptions rely on rapid software-push or run-command primitives.
- **Detection engineering leverage**: baselining approved deployment workflows (who/what/when/where) materially reduces false positives while preserving strong signal.

## 9. Threat Actor Usage
Known to be used by (examples from ATT&CK procedure observations):
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]
- [[30_CIPHER/03_Threat_Actors/G1051 - Medusa Group|Medusa Group]]
- [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]
- [[30_CIPHER/03_Threat_Actors/G0091 - Silence|Silence]]
- [[30_CIPHER/03_Threat_Actors/G0028 - Threat Group-1314|Threat Group-1314]]

## 10. Campaign Usage
- **C0018 - C0018** (month-long ransomware intrusion culminating in AvosLocker deployment)

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1053 - AvosLocker|AvosLocker]]
- [[S0041 - Wiper|Wiper]]

## 12. Mitigations
- **M1015 – Active Directory Configuration**: enforce isolation/privilege separation for management systems via directory policy and governance.
- **M1033 – Limit Software Installation**: restrict/approve third-party management suites; minimize where high-privilege deployment tools are deployed.
- **M1032 – Multi-factor Authentication**: require MFA for all management plane/admin console access and privileged APIs.
- **M1030 – Network Segmentation**: segment management infrastructure and restrict agent/control traffic to necessary paths only.
- **M1027 – Password Policies**: ensure credentials used to access deployment systems are unique and not reused broadly.
- **M1026 – Privileged Account Management**: tightly control and audit accounts with deployment permissions.
- **M1029 – Remote Data Storage**: protect signing keys/certs; avoid co-locating sensitive signing material with deployment systems.
- **M1051 – Update Software**: patch deployment systems and dependencies to reduce takeover risk.
- **M1018 – User Account Management**: govern third-party and service accounts; continuous review/deprovisioning.
- **M1017 – User Training**: enforce strict approval and change control policies for deployments.

## 13. Testing & Validation
- Validate detections using safe simulations that mimic **management-plane initiated execution**:
  - Use a lab deployment tool to trigger benign script execution on test endpoints and verify: logging, correlation, alert routing, and response playbooks.
  - Confirm visibility across: management server logs, endpoint process creation, and cloud audit events (where applicable).
  - Ensure detections distinguish approved maintenance windows vs. ad-hoc pushes.

## 14. References
- MITRE. (n.d.). *Software Deployment Tools (T1072).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1072/
- MITRE. (2025, October 21). *Detection of Adversary Abuse of Software Deployment Tools (DET0223).* MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0223/
- Neal, C., & Venere, G. (2022, June 21). *Avos ransomware group expands with new attack arsenal.* Cisco Talos Intelligence. https://blog.talosintelligence.com/avoslocker-new-arsenal/
- Cybersecurity and Infrastructure Security Agency. (2025, March 12). *#StopRansomware: Medusa Ransomware (AA25-071A).* https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a

## 15. Notes
- Treat **new administrative principals** gaining deployment permissions as a detection pivot.
- Consider guardrails: “deployment-tool actions require ticket/change ID” where feasible, and alert on missing/invalid change linkage.
