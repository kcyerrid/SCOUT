---
entity_type: mitre_technique

technique_id: "T1069"
subtechnique_id: ""
technique_name: "Permission Groups Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - Containers
  - IaaS
  - Identity Provider
  - Linux
  - Office Suite
  - SaaS
  - Windows
  - macOS
datasources:
  - "DC0032 - Process Creation"
  - "DC0064 - Command Execution"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0335 - Carbon|Carbon]]"
  - "[[30_CIPHER/05_Malware/S0483 - IcedID|IcedID]]"
  - "[[30_CIPHER/05_Malware/S0623 - Siloscape|Siloscape]]"
associated_campaigns:
  - "C0024 - SolarWinds Compromise"
related_techniques:
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1069.001 - Permission Groups Discovery: Local Groups|T1069.001]]"
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1069.002 - Permission Groups Discovery: Domain Groups|T1069.002]]"
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1069.003 - Permission Groups Discovery: Cloud Groups|T1069.003]]"
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]"

detection_priority:
  - High

detection_maturity: "Established"
threat_score: 4

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
Permission Groups Discovery (T1069) covers attempts to enumerate group/role membership and permission group settings across endpoints and control planes (AD, local OS, SaaS/IdP, IaaS, and container platforms). This discovery helps adversaries identify privileged users/groups and target high-impact accounts and pathways.

## 2. Technical Overview
Common objectives:
- Identify “who is privileged” (admins, operators, service accounts).
- Map group membership for lateral movement targeting, privilege escalation planning, and defense evasion.

Common execution patterns:
- **Windows**: group enumeration via native tooling and scripting (local/domain), including PowerShell and built-in utilities.
- **Linux/macOS**: group membership queries using native commands and directory lookups.
- **Identity Provider / SaaS / Office Suite**: API-driven enumeration of directory roles/groups, often via administrative portals or Graph/API clients.
- **Containers / IaaS**: permission checks and role/group queries in orchestration or cloud control planes (e.g., listing roles, checking node/service permissions).

Analyst framing:
- “Group discovery” is often benign for IT operations—**context** (source host, principal, parent process, and timing) is critical.
- High-signal when coupled with adjacent behaviors: credential access, remote execution, role assignment, or suspicious authentication.

## 3. Subtechnique Considerations
T1069 has sub-techniques that change telemetry and context:
- **T1069.001 Local Groups**: endpoint-local admin/user group enumeration; strong precursor to privilege abuse and lateral movement.
- **T1069.002 Domain Groups**: AD domain group membership/permissions; often paired with DC queries and lateral movement planning.
- **T1069.003 Cloud Groups**: tenant role/group enumeration in IdP/SaaS; often paired with OAuth/app consent, role assignment, or mailbox/tenant changes.

## 4. Procedure Examples
Examples from ATT&CK procedure references include:
- [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]] using tooling to enumerate permissions associated with Windows groups.
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]] using group enumeration commands to map user groups and permissions.
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]] enumerating privileged virtualization/admin groups in targeted environments.
- [[30_CIPHER/05_Malware/S0623 - Siloscape|Siloscape]] checking Kubernetes node permissions (container context).
- **C0024 - SolarWinds Compromise** referencing group enumeration activity during intrusion operations.

## 5. Detection Guidance
Detection focus: group enumeration is typically a **discovery burst**. Prioritize behavioral correlation and anomaly detection.

Recommended analytics:
1. **Windows group enumeration burst**
   - Detect process creation and/or command/script telemetry indicative of group membership queries.
   - Elevate if:
     - performed by unusual users (non-admins querying high-privilege groups),
     - executed from endpoints not used for administration,
     - parent process is suspicious (macro, LOLBin chain, remote admin tool),
     - followed by lateral movement or credential access.
2. **Linux/macOS group enumeration**
   - Detect group membership command execution from remote sessions or unusual parents.
3. **Control-plane group enumeration (IdP/SaaS/IaaS)**
   - Cloud/IdP audit events showing group/role listing APIs by principals with unusual device/geo/client app.
   - Correlate with risky changes (role assignment, app consent, token abuse, mailbox rules, new access keys).
4. **Container permission checks**
   - Detect permission enumeration of cluster roles and node/service permissions, especially from compromised workloads or newly created service accounts.

### 5.1 Data Source Notes
Prioritize:
- **DC0032 Process Creation**: group enumeration tooling and scripting engines.
- **DC0064 Command Execution**: PowerShell ScriptBlock/module logging; shell command telemetry capturing arguments used to query groups.

## 6. Response Guidance
1. Confirm whether the initiating principal is expected to perform group enumeration (admin workstation, IT tooling).
2. Validate the execution chain:
   - parent process, script origin, remote session indicators, scheduled tasks.
3. Determine scope:
   - which groups were enumerated (especially high-privilege groups), volume/cadence, and whether enumeration crossed hosts/tenants.
4. Correlate with follow-on actions:
   - new privileged sessions, role changes, credential access, remote execution.
5. Contain:
   - revoke suspicious sessions/tokens, reset credentials, and apply conditional access restrictions if control-plane related.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1069.001 - Permission Groups Discovery: Local Groups|T1069.001]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1069.002 - Permission Groups Discovery: Domain Groups|T1069.002]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1069.003 - Permission Groups Discovery: Cloud Groups|T1069.003]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]

## 8. SOC Relevance
- High relevance: maps directly to privilege pathway discovery and is frequently seen before privilege escalation or lateral movement.
- Best used as part of behavior chains:
  - group discovery → credential access attempts → privileged auth → remote execution.
- Especially valuable for cloud/IdP where enumeration may be stealthy and fast.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]]: enumerating group permissions on Windows.
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]: enumerating Windows user groups and permissions.
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]: enumerating privileged virtualization/admin groups.

## 10. Campaign Usage
- **C0024 - SolarWinds Compromise**: referenced group discovery activity during intrusion operations.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0335 - Carbon|Carbon]]: using group enumeration commands in host discovery.
- [[30_CIPHER/05_Malware/S0483 - IcedID|IcedID]]: identifying membership context (e.g., workgroup/domain indicators) as part of discovery.
- [[30_CIPHER/05_Malware/S0623 - Siloscape|Siloscape]]: checking Kubernetes permissions.

## 12. Mitigations
This technique is generally **not easily mitigated** preventively because it can rely on legitimate system and directory features.
Defender-focused controls:
- Enforce least privilege and reduce standing privileges; monitor access to high-privilege group membership data.
- Harden and monitor admin tooling usage (PowerShell logging, constrained language mode where appropriate, endpoint allowlisting).
- Apply strong identity security controls (MFA, conditional access, privileged access workstations, just-in-time access).

## 13. Testing & Validation
- Validate visibility for:
  - endpoint group enumeration commands and PowerShell telemetry,
  - control-plane group/role listing events in IdP/SaaS/IaaS,
  - correlation with privilege changes and remote execution.
- Recommended test content:
  - Atomic Red Team T1069 tests (and sub-technique tests where available) mapped to your telemetry sources.

## 14. References
- MITRE ATT&CK. (n.d.). *Permission Groups Discovery (T1069)*. https://attack.mitre.org/techniques/T1069/
- MITRE ATT&CK. (n.d.). *Behavioral Detection of Permission Groups Discovery (DET0179)*. https://attack.mitre.org/detectionstrategies/DET0179/
- Atomic Red Team. (n.d.). *Atomic tests for T1069*. https://atomicredteam.io/atomic-red-team/atomics/T1069/
- Microsoft. (n.d.). *PowerShell logging and protections*. https://learn.microsoft.com/powershell/scripting/learn/ps101/02-help-system

## 15. Notes
- Treat enumeration of **high-privilege groups** (domain admins, local admins, tenant/global admins, cluster-admin roles) as higher risk, especially from non-admin endpoints or unusual identities.
