---
entity_type: mitre_technique
technique_id: "T1083"
subtechnique_id: ""
technique_name: "File and Directory Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "ESXi"
  - "Linux"
  - "Network Devices"
  - "Windows"
  - "macOS"
datasources:
  - "DC0032 - Process Creation"
  - "DC0039 - File Creation"
  - "DC0055 - File Access"
  - "DC0064 - Command Execution"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338]]"
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1087"
  - "T1018"
  - "T1518"
detection_priority:
  - "Medium"
detection_maturity: ""
threat_score: 3
created: 2026-01-06
updated: 2026-01-06
contributors: []
tags:
  - "mitre"
  - "technique"
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
File and Directory Discovery is adversary enumeration of file systems (paths, files, permissions, metadata) to understand the environment, locate sensitive data, identify security tooling/configs, and stage follow-on actions (collection, credential theft, ransomware targeting, lateral movement prep).

## 2. Technical Overview
Adversaries commonly:
- Enumerate directories recursively to map user profiles, application directories, shared mounts, and config locations.
- Query for file metadata (timestamps, size, attributes) and permission boundaries to determine accessible targets.
- Target high-value locations: user home directories, browser/credential stores, SSH keys, cloud creds, scripts, backups, and log/config directories.
- Use native tooling (shell built-ins, OS utilities), API calls, or malware features to list and filter filesystem objects.

Typical behaviors (defender lens):
- Bursty recursive traversal (many path touches in short windows)
- Discovery aligned with privilege context changes (post-UAC elevation, post-credential access, post-lateral movement)
- Unusual parent/child process lineage (office apps → cmd/shell → enumeration utilities)
- Enumeration of atypical paths for the host role (e.g., DCs enumerating user download folders)

## 3. Subtechnique Considerations
None (no sub-techniques).

## 4. Procedure Examples
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338]] used multiple directory listing commands on Windows after exploitation to inventory files and directories for follow-on actions.
- Malware families may enumerate files/directories to locate specific targets (e.g., storage device paths on Linux for destructive actions) and to identify encryption candidates prior to ransomware activity.

## 5. Detection Guidance
Prioritize detections that combine **process lineage + bursty filesystem interaction + sensitive path targeting**.

High-signal detection ideas:
- **Recursive enumeration commands** (Windows: directory traversal patterns; Linux/macOS: `find`/`locate`-like behavior) executed by unusual users, from unusual parents, or outside baseline admin tooling.
- **Sensitive directory targeting**: credential/config locations, browser extension storage, key material directories, backup/config paths, etc.
- **Cross-telemetry correlation**: process start → repeated file access patterns → optional file creation (staging lists) and/or network activity shortly after.

### Data Source Notes
Minimum telemetry to support robust detection:
- **DC0032 – Process Creation**: command line, parent process, user, integrity level.
- **DC0055 – File Access**: repeated opens/reads across many directories; depth of traversal.
- **DC0039 – File Creation**: creation of “inventory” outputs (e.g., redirected listings into temp files).
- **DC0064 – Command Execution** (where available): CLI auditing on ESXi/network devices.

## 6. Response Guidance
1. Scope impact: identify the principal, host, and time window; look for concurrent privilege escalation, credential access, or lateral movement.
2. Triage paths touched: determine if the enumeration targeted credential stores, admin scripts, backups, or security tooling.
3. Contain if suspicious: isolate host or restrict session; invalidate credentials if discovery aligns with credential store access.
4. Hunt laterally: search for the same process/command patterns across the fleet; check for similar traversal bursts.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1083 - File and Directory Discovery|T1083]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1018 - Remote System Discovery|T1018]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1518 - Software Discovery|T1518]]

## 8. SOC Relevance
- **High prevalence** in intrusions; noisy if done by admins/scripts—tuning is essential.
- **Best SOC value** comes from *contextual detection*: unusual user/host role + recursion + sensitive paths + follow-on behaviors (staging/exfil/ransomware).

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0018 - admin@338|admin@338]]: directory listing to survey hosts and identify files of interest.

## 10. Campaign Usage
None noted.

## 11. Malware Usage
Common malware behaviors include enumerating:
- user/home directories for documents and browser data
- configuration locations for secrets
- file attributes to decide what to encrypt or steal

## 12. Mitigations
- Reduce standing privileges; enforce least privilege on sensitive directories.
- Harden and monitor remote administration channels (to reduce interactive discovery by adversaries).
- Centralize and protect credential/config secrets (vaulting, tight ACLs).
- Maintain allowlists for legitimate inventory tooling and schedule-based baselines.

## 13. Testing & Validation
Safe validation steps:
- Execute benign directory listings under controlled accounts and compare telemetry to baseline.
- Simulate recursion bursts (e.g., enumerating a large directory tree) and verify:
  - process creation visibility with full command line
  - file access coverage in sensitive paths
  - alert suppression for known-good admin tooling
- Confirm detection logic distinguishes:
  - admin inventory scripts (known signer/path, scheduled task lineage)
  - interactive low-priv enumeration (more suspicious)

## 14. References
- MITRE ATT&CK. (n.d.). *File and Directory Discovery (T1083).* https://attack.mitre.org/techniques/T1083/
- MITRE ATT&CK. (2025). *Recursive Enumeration of Files and Directories Across Privilege Contexts (DET0370).* https://attack.mitre.org/detectionstrategies/DET0370/

## 15. Notes
- Tuning tip: build baselines by **host role** (server vs workstation vs DC) and **parent process** (explorer vs admin console vs EDR tooling).
