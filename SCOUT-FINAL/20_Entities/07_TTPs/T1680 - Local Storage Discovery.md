---
entity_type: mitre_technique
technique_id: "T1680"
subtechnique_id: ""
technique_name: "Local Storage Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "Windows"
  - "macOS"
datasources:
  - "DC0032 - Process Creation"
  - "DC0064 - Command Execution"
  - "DC0002 - User Account Authentication"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false
associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: []
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
Local Storage Discovery is adversary enumeration of local disks/volumes/drives and their attributes (size, free space, volume IDs/serials, mount points). This supports decisions like what/where to encrypt, staging strategy, targeting large data stores, and identifying host roles.

## 2. Technical Overview
Common behaviors across platforms:
- Windows: enumerate logical disks and drive mappings; query drive types/attributes via built-ins, WMI, or APIs.
- Linux: enumerate block devices/partitions and mount points; query filesystem type, free space, and device identifiers.
- macOS: enumerate disks and volumes and their mount paths.
- ESXi: enumerate connected storage, datastores, and VM disk files.
- IaaS: enumerate attached volumes/disks via provider tooling (AWS/GCP/Azure volume listings).

Defender-relevant signals:
- Storage discovery from non-admin contexts or unusual automation accounts
- Disk/volume enumeration preceding file discovery bursts, credential access, or ransomware behaviors
- On ESXi: unexpected interactive sessions followed by storage enumeration

## 3. Subtechnique Considerations
None (no sub-techniques).

## 4. Procedure Examples
Common patterns include enumerating:
- drive letters/mount points
- volume IDs/serials
- total/free space
- datastore inventories (virtualization)

## 5. Detection Guidance
Detection is most effective when combining **process telemetry** with **context**:
- Identify disk enumeration utilities executed outside baseline maintenance windows.
- Track sequences such as: login/authentication event → shell execution → storage discovery commands → rapid file discovery or encryption-like file operations.
- On Linux/macOS, emphasize non-interactive shells and unusual parent processes.

### Data Source Notes
- **DC0032 – Process Creation**: watch for processes executing disk enumeration utilities and related arguments.
- **DC0064 – Command Execution**: command-line auditing (Linux auditd EXECVE; macOS unified logs; ESXi shell command logging).
- **DC0002 – User Account Authentication**: correlate unexpected remote admin sessions (e.g., SSH) with immediate storage enumeration on ESXi.

## 6. Response Guidance
1. Confirm whether the account/session is expected to perform storage inventory on the host.
2. If suspicious, pivot to adjacent behaviors:
   - file discovery and file access spikes
   - privilege escalation attempts
   - remote service usage or lateral movement
3. For ESXi/IaaS, check for parallel activity across multiple hosts (volume discovery can be systematic for ransomware prep).

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1680 - Local Storage Discovery|T1680]]

## 8. SOC Relevance
- Often moderate-signal alone, but becomes **high value** when correlated with:
  - file discovery and mass file modification
  - backups/software discovery
  - disabling defenses or shadow copy tampering (ransomware tradecraft)

## 9. Threat Actor Usage
Not specified.

## 10. Campaign Usage
None noted.

## 11. Malware Usage
Not specified.

## 12. Mitigations
Preventive controls are limited; prioritize:
- least privilege for management utilities
- strong monitoring of admin sessions on virtualization and cloud control planes
- segmentation and hardening of hypervisor management interfaces

## 13. Testing & Validation
- Execute benign storage enumeration on each platform in a test environment and validate:
  - process creation capture (with command lines)
  - command execution auditing (where supported)
  - correlation with authentication/session telemetry on ESXi
- Validate tuning by allowing known inventory/monitoring tools and flagging non-standard parents/users.

## 14. References
- MITRE ATT&CK. (n.d.). *Local Storage Discovery (T1680).* https://attack.mitre.org/techniques/T1680/
- MITRE ATT&CK. (2025). *Local Storage Discovery via Drive Enumeration and Filesystem Probing (DET0188).* https://attack.mitre.org/detectionstrategies/DET0188/

## 15. Notes
- Consider role-based baselines: virtualization hosts, database servers, and file servers will have different “normal” storage enumeration profiles than endpoints.
