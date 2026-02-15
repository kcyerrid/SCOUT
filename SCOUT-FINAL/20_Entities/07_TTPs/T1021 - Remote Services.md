---
entity_type: mitre_technique

technique_id: "T1021"
subtechnique_id: ""
technique_name: "Remote Services"

tactic:
  - "TA0008 - Lateral Movement"
platforms:
  - ESXi
  - IaaS
  - Linux
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda]]"
  - "[[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear]]"
  - "[[30_CIPHER/03_Threat_Actors/G0102 - Wizard Spider|Wizard Spider]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1063 - Brute Ratel C4|Brute Ratel C4]]"
  - "[[30_CIPHER/05_Malware/S0437 - Kivars|Kivars]]"
  - "[[30_CIPHER/05_Malware/S1016 - MacMa|MacMa]]"
  - "[[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]]"
associated_campaigns: []
related_techniques: []

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

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

# T1021 - Remote Services

## 1. Summary
Remote Services (T1021) covers adversary use of legitimate remote-access services/protocols (e.g., RDP, SMB admin shares, DCOM, SSH, VNC, WinRM, cloud/hypervisor consoles) to move laterally by authenticating to remote systems with valid credentials and operating as the logged-on user.

## 2. Technical Overview
Attackers commonly:
- Obtain valid credentials (often domain or privileged local) and authenticate to remote services exposed internally (and sometimes externally).
- Use the remote session to execute commands, stage tools, access shares, or pivot further.
- Blend with administrative activity (IT/ops tools and normal remote management) to evade simplistic detection.

High-signal behaviors often include:
- First-time remote login for a user/host pair, especially into servers, DCs, hypervisors, or management planes.
- Remote logins from atypical source hosts/subnets, jump hosts, or non-interactive service accounts.
- Remote access followed by rapid post-auth activity (process execution, remote service creation, task scheduling, file staging, credential access, or outbound lateral connections).

## 3. Subtechnique Considerations
T1021 is best handled as a “container” technique in detections and investigations:
- Use subtechniques for protocol-specific coverage and tuning (ports, log sources, and expected admin workflows differ).
- For ESXi/IaaS scenarios, include management plane telemetry (vCenter/vSphere APIs, cloud console/bastion activity) alongside endpoint and network data.

Subtechniques under T1021:
- T1021.001 Remote Desktop Protocol
- T1021.002 SMB/Windows Admin Shares
- T1021.003 Distributed Component Object Model
- T1021.004 SSH
- T1021.005 VNC
- T1021.006 Windows Remote Management
- T1021.007 Cloud Services
- T1021.008 Direct Cloud VM Connections

## 4. Procedure Examples
Examples documented in ATT&CK include:
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda]] using remote scheduled tasks during lateral movement.
- [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear]] using valid credentials (often with common frameworks) to move laterally.
- [[30_CIPHER/05_Malware/S1063 - Brute Ratel C4|Brute Ratel C4]] leveraging RPC for lateral movement capability.
- [[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]] propagating via RPC-related mechanisms.
- [[30_CIPHER/03_Threat_Actors/G0102 - Wizard Spider|Wizard Spider]] using remote-service-enabled paths (e.g., WebDAV/remote file shares) to execute payloads.

## 5. Detection Guidance
Prioritize detections that correlate **remote authentication** with **post-auth actions**:
- “Remote service login → uncommon process execution” within a short window.
- “Remote service login → remote admin activity” (service creation, scheduled task, WMI/WinRM, PsExec-like patterns, remote share writes + execution).
- “Remote service login → outbound lateral connection” (pivot chaining).

Recommended analytic patterns:
- Baseline and alert on new/rare remote login relationships (user→target, source→target, protocol/service).
- Detect remote logins to privileged tiers (DCs, management servers, hypervisors) from non-admin workstations.
- Identify authentication anomalies (impossible travel, new device, unusual source subnet, sudden fan-out).

### 5.1. Data Source Notes
Practical telemetry for T1021 coverage typically includes:
- Authentication events (success/failure) on targets; explicit-credential usage where available.
- Remote service–specific logs (RDP/RDS logs, SSHD logs, SMB auditing, WinRM logs).
- Network telemetry (flow logs, firewall logs) for protocol ports and session metadata.
- Endpoint telemetry (process start, parent/child, remote execution artifacts) on the destination host.

## 6. Response Guidance
When suspected Remote Services lateral movement is detected:
- Contain: isolate affected hosts (especially jump points), restrict lateral management ports temporarily if feasible.
- Credential actions: disable/reset suspected accounts; rotate local admin passwords; investigate MFA bypass gaps.
- Scope: enumerate other targets accessed by the same account/source; look for fan-out.
- Persistence check: validate services, scheduled tasks, new accounts, and remote management configuration changes.
- Harden: remove unnecessary exposure (internal and internet), enforce gateways/bastions, and tighten segmentation.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021 - Remote Services|T1021]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.001 - Remote Desktop Protocol|T1021.001]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.002 - SMB/Windows Admin Shares|T1021.002]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.003 - Distributed Component Object Model|T1021.003]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.004 - SSH|T1021.004]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.005 - VNC|T1021.005]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.006 - Windows Remote Management|T1021.006]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.007 - Cloud Services|T1021.007]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1021.008 - Direct Cloud VM Connections|T1021.008]]

## 8. SOC Relevance
Common SOC pivots:
- Source host identity (jump host vs. workstation), user identity, and privilege tier.
- Protocol/service used and whether it is expected for that user/team.
- Time-to-action after login (rapid post-auth activity is high signal).
- Repeated failures followed by success; authentication from new device; unusual geography/VPN.

High-value enrichment:
- Asset criticality (DC/hypervisor/management plane), account role, and normal admin tooling patterns.
- Known maintenance windows and sanctioned remote admin paths (gateways, bastions).

## 9. Threat Actor Usage
Documented examples include:
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda|Aquatic Panda]]
- [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear]]
- [[30_CIPHER/03_Threat_Actors/G0102 - Wizard Spider|Wizard Spider]]

## 10. Campaign Usage
- None explicitly captured in this note (see ATT&CK technique/subtechnique procedure examples for campaign-specific mappings).

## 11. Malware Usage
Documented examples include:
- [[30_CIPHER/05_Malware/S1063 - Brute Ratel C4|Brute Ratel C4]]
- [[30_CIPHER/05_Malware/S0437 - Kivars|Kivars]]
- [[30_CIPHER/05_Malware/S1016 - MacMa|MacMa]]
- [[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]]

## 12. Mitigations
ATT&CK-listed mitigations for T1021 include:
- M1047 Audit: assess systems, permissions, and insecure configurations.
- M1042 Disable or Remove Feature or Program: disable unnecessary remote service types (including direct cloud VM connections); on ESXi consider lockdown mode.
- M1035 Limit Access to Resource Over Network: reduce unnecessary access to file shares/hypervisors/sensitive systems; use gateways/bastions where appropriate.
- M1032 Multi-factor Authentication: enforce MFA for remote service logons where feasible.
- M1027 Password Policies: enforce strong, unique passwords; avoid local admin password reuse.
- M1018 User Account Management: limit who can use remote services and constrain high-risk accounts.

## 13. Testing & Validation
Safe validation ideas:
- Baseline-building: identify legitimate admin remote paths (jump hosts, gateways) and expected accounts.
- Detection simulation (authorized): generate benign remote logins using standard tools and confirm telemetry (auth logs + network sessions).
- ATT&CK-aligned tests: use controlled emulation frameworks/tests to validate alert logic without deploying malware.

## 14. References
- MITRE. (n.d.). *Remote Services (T1021)*. MITRE ATT&CK. https://attack.mitre.org/techniques/T1021/
- Broadcom. (2025, February 12). *Enabling or disabling Lockdown mode on an ESXi host*. https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html
- Microsoft. (2025, January 15). *Remove administrative shares - Windows Server*. https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/remove-administrative-shares
- CISA. (2025, June 4). *Internet Exposure Reduction Guidance*. https://www.cisa.gov/resources-tools/resources/exposure-reduction
- Red Canary. (n.d.). *Atomic Red Team (ART)*. GitHub. https://github.com/redcanaryco/atomic-red-team

## 15. Notes
- Treat remote management plane access (vCenter/vSphere, cloud consoles, bastions) as privileged-tier telemetry; ensure it is ingested and correlated with endpoint/network activity.
- Tuning tip: separate “interactive admin” (RDP/SSH) from “file staging” (SMB shares) and “remote object activation” (DCOM) to reduce noise.
