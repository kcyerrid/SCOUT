---
entity_type: mitre_technique

technique_id: "T1135"
subtechnique_id: ""
technique_name: "Network Share Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "DC0032 - Process Creation"
  - "DC0082 - Network Connection Creation"
  - "DC0048 - Named Pipe Metadata"
  - "DC0064 - Command Execution"
  - "DC0021 - OS API Execution"
  - "DC0078 - Network Traffic Flow"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
  - "[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]"
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]"
  - "[[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec]]"
associated_campaigns:
  - "C0015"
  - "C0049 - Leviathan Australian Intrusions"
related_techniques:
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1018 - Remote System Discovery|T1018]]"
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1083 - File and Directory Discovery|T1083]]"
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1046 - Network Service Discovery|T1046]]"

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
Network Share Discovery (T1135) captures adversary behavior used to enumerate shared folders/drives across hosts (commonly SMB shares), often as a precursor to targeted collection, lateral movement planning, or ransomware impact.

## 2. Technical Overview
Common patterns:
- **Host-level share enumeration**: queries for local shares (e.g., enumerating exported SMB shares) and remote shares on other hosts.
- **Network fan-out**: rapid SMB/RPC connections to many internal hosts (ports **445/139**) to probe share availability, sometimes via RPC calls that enumerate shares.
- **Tooling and methods**:
  - Windows-native utilities and scripting (e.g., share listing via built-in commands or PowerShell SMB modules).
  - SMB client tooling on Linux/macOS that lists available shares.
  - API/RPC-based enumeration (e.g., calls consistent with share enumeration behavior), which can be harder to see without deeper telemetry.

Operational intent:
- Identify file servers, departmental shares, backup locations, and high-value repositories.
- Discover administrative shares (e.g., default admin shares) to assess lateral movement paths.
- Build target lists for follow-on **share traversal, file discovery, staging, or encryption**.

## 3. Subtechnique Considerations
No sub-techniques for T1135.

## 4. Procedure Examples
Examples from ATT&CK procedure references include:
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]] using share discovery commands to enumerate available shares (including administrative shares).
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]] using share discovery as part of reconnaissance.
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]] enumerating non-hidden shares via Windows networking APIs.
- [[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec]] enumerating shares and permissions in targeted environments.
- Campaign references such as **C0015** and **C0049 - Leviathan Australian Intrusions** featuring share enumeration during intrusion activity.

## 5. Detection Guidance
High-signal detection focuses on **(a) share enumeration execution** plus **(b) SMB/RPC fan-out** and **(c) follow-on file access**.

Recommended analytics:
1. **Burst share discovery + SMB fan-out (Windows)**
   - Process/script launches share discovery behavior → **multiple SMB connections** to distinct internal hosts within a short window.
   - Enrich with user context (non-admin, unusual workstation, suspicious parent process, remote logon).
2. **RPC/API share enumeration (Windows)**
   - Detect RPC activity consistent with share enumeration (where available), especially from atypical processes.
3. **Linux/macOS share enumeration tools**
   - Process creation for SMB enumeration utilities followed by **connections to 445/139** to multiple hosts.
4. **Ransomware-context correlation**
   - Share discovery shortly before mass file access, remote service creation, or encryption-like I/O.

Suggested pivot and enrichment:
- Account/session lineage, interactive vs service context, source host role (user workstation vs management server).
- Lateral movement precursors (remote admin tooling, remote execution artifacts).
- Share access events (e.g., object access on file servers) following discovery.

### 5.1 Data Source Notes
Prioritize these data components:
- **DC0032 Process Creation**: creation of share discovery-related processes and scripting hosts.
- **DC0064 Command Execution**: PowerShell and shell command telemetry with arguments indicative of share listing.
- **DC0082 Network Connection Creation / DC0078 Network Traffic Flow**: SMB connection bursts to many hosts; identify fan-out patterns.
- **DC0048 Named Pipe Metadata**: SMB/RPC named pipe usage tied to share enumeration workflows (where collected).
- **DC0021 OS API Execution**: ETW/RPC visibility for share-enumeration API usage (environment-dependent).

## 6. Response Guidance
Triage steps:
1. Confirm the initiating user/process and **parent process chain** (interactive shell, script host, remote admin tool, scheduled task).
2. Enumerate targets: destination hosts and ports, SMB sessions established, and any authentication anomalies.
3. Check follow-on behavior:
   - Share traversal, file discovery, staging, large copy operations, or encryption-like file modifications.
   - Lateral movement actions (remote service creation, remote execution).
4. Containment:
   - Isolate affected endpoints if fan-out is anomalous.
   - Temporarily restrict SMB egress from workstations where feasible; reset/disable suspicious accounts; invalidate tokens/sessions.
5. Hunt:
   - Look for similar fan-out from other hosts/users in the same time window.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1018 - Remote System Discovery|T1018]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1083 - File and Directory Discovery|T1083]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1046 - Network Service Discovery|T1046]]

## 8. SOC Relevance
- **High value** for early intrusion detection and ransomware pre-impact hunting.
- Strong correlation opportunities:
  - share discovery → remote authentication spikes → file server object access → lateral movement / impact.
- Works well with thresholding and allowlists for known inventory/management systems.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]: share discovery to map accessible administrative and non-administrative shares.
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]: network share enumeration as part of reconnaissance and targeting.
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]]: discovery of connected network shares.

## 10. Campaign Usage
- **C0015**: referenced use of PowerView/ShareFinder-style discovery to identify open shares.
- **C0049 - Leviathan Australian Intrusions**: referenced scanning/enumeration of remote network shares in victim environments.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]: enumerating accessible shares using Windows networking APIs.
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]: querying shared drives locally as discovery.
- [[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec]]: enumerating shared folders and permissions.

## 12. Mitigations
- **M1028 Operating System Configuration** (ATT&CK mitigation):
  - Reduce unnecessary shares; enforce least privilege on share ACLs.
  - Restrict/monitor administrative shares and remote administration channels.
  - Network segmentation and host firewall rules to limit SMB exposure (especially from user workstations).

## 13. Testing & Validation
- Validate detections in a controlled environment using benign share enumeration activity and confirm:
  - Process + command telemetry captures the enumerator.
  - Network telemetry captures SMB fan-out and IPC$ / share listing patterns where applicable.
  - Thresholds differentiate IT inventory tooling from unexpected endpoints.
- Recommended test content:
  - Atomic Red Team T1135 test cases (where available) mapped to your EDR/SIEM data model.

## 14. References
- MITRE ATT&CK. (n.d.). *Network Share Discovery (T1135)*. https://attack.mitre.org/techniques/T1135/
- MITRE ATT&CK. (n.d.). *Behavior-chain detection for T1135 Network Share Discovery across Windows, Linux, and macOS (DET0182)*. https://attack.mitre.org/detectionstrategies/DET0182/
- SwiftOnSecurity. (n.d.). *Sysmon documentation*. https://learn.microsoft.com/sysinternals/downloads/sysmon
- Atomic Red Team. (n.d.). *Atomic tests for T1135*. https://atomicredteam.io/atomic-red-team/atomics/T1135/

## 15. Notes
- Baseline and allowlist legitimate inventory/scanner hosts and IT admin scripts; T1135 is frequently noisy in environments with heavy SMB management tooling.
- Consider separate thresholds for workstation vs server initiators; workstation-originated SMB fan-out is often higher risk.
