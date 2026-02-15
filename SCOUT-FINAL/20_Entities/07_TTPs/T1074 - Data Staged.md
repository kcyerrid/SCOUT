---
entity_type: mitre_technique

technique_id: "T1074"
subtechnique_id: ""
technique_name: "Data Staged"

tactic:
  - TA0009 - Collection
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
  - "[[30_CIPHER/03_Threat_Actors/G1032 - INC Ransom|INC Ransom (G1032)]]"
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider (G1015)]]"
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon (G1017)]]"
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1074.001"
  - "T1074.002"

detection_priority:
  - High

detection_maturity: ""
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
Adversaries may stage collected data in a central location (local or remote) prior to exfiltration. Staging reduces the number of outbound connections needed and can help evade detections by consolidating data before transfer.

## 2. Technical Overview
Common staging behaviors:
- **Centralizing data** into a single directory, share, or host prior to exfiltration.
- **Combining/sequencing** with compression or archiving to reduce file counts and size.
- **Using “quiet” directories** (temp, system-like paths) or attacker-created directories.
- **Cloud environments:** staging within a specific instance/VM before transfer out of the environment.

Defender-observable patterns:
- Creation of new directories that rapidly receive many copied files.
- Large archives appearing shortly after a period of file/share access.
- Copy/robocopy/rsync-like activity to staging locations.

## 3. Subtechnique Considerations
This technique has subtechniques:
- **T1074.001 - Local Data Staging:** staging on the same host where collection occurs.
- **T1074.002 - Remote Data Staging:** staging on a different internal system (e.g., file server, admin share, remote host).

Detection should explicitly differentiate:
- Local temp staging vs. lateral movement to a remote staging node (authentication and network telemetry become critical for remote staging).

## 4. Procedure Examples
Examples documented in ATT&CK include:
- [[30_CIPHER/03_Threat_Actors/G1032 - INC Ransom|INC Ransom (G1032)]] staged data on compromised hosts prior to exfiltration.
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider (G1015)]] staged data in a centralized database prior to exfiltration.
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon (G1017)]] has staged collected data prior to exfiltration.

## 5. Detection Guidance
ATT&CK provides a detection strategy for this technique (DET0014) emphasizing file access/copy patterns and staging directory creation.

Detection opportunities:
- **New staging directory patterns**
  - Newly created directories with rapid file writes from disparate source paths.
  - Staging directories in unusual locations (system temp, obscure system folders, user profile subfolders not used by apps).
- **Archiving + staging sequences**
  - File copy bursts followed by archive creation in the same directory tree.
- **Remote staging indicators**
  - Lateral auth events to file servers/admin shares, then large write volumes to remote paths.
- **Cloud staging indicators**
  - New VM/instance used primarily as a data aggregation node (high inbound copy, then outbound egress).

### Data Source Notes
Recommended telemetry:
- Endpoint EDR: process creation, command lines for copy/archive utilities, file creation bursts.
- File system telemetry: directory creation + large write volumes, archive creation events.
- Network telemetry: SMB/NFS write patterns, internal transfer volumes, subsequent egress.
- Identity telemetry: authentication to shares/servers used for remote staging.

## 6. Response Guidance
1. **Containment**
   - Isolate suspected staging hosts; block outbound egress from staging nodes.
   - Disable compromised accounts used to access staging locations.
2. **Scoping**
   - Identify staging directories, file manifests, and archive outputs; enumerate source systems involved.
   - Determine whether staged data left the environment (proxy/firewall logs, cloud egress logs).
3. **Eradication**
   - Remove attacker tooling and persistence; remediate lateral movement paths enabling remote staging.
4. **Hardening**
   - Restrict write access to sensitive shares; monitor for new high-volume write paths.
   - Apply least privilege and conditional access for admin shares and file servers.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1074 - Data Staged|T1074]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1074.001 - Local Data Staging|T1074.001]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1074.002 - Remote Data Staging|T1074.002]]

## 8. SOC Relevance
- High relevance for ransomware/extortion and large-scale theft.
- Often a reliable “bridge” signal between collection and exfiltration; use it to trigger:
  - targeted hunts for archives,
  - egress monitoring,
  - rapid containment actions.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1032 - INC Ransom|INC Ransom (G1032)]]: host-based staging prior to exfiltration.
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider (G1015)]]: centralized database staging prior to exfiltration.
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon (G1017)]]: staging as part of broader collection/exfil workflows.

## 10. Campaign Usage
- 

## 11. Malware Usage
- 

## 12. Mitigations
- Preventive mitigations are limited since staging can use normal OS features; prioritize:
  - Least privilege for write access on shares and sensitive directories
  - Network segmentation and monitoring of internal transfer paths
  - Robust logging/auditing on file servers and high-value endpoints

## 13. Testing & Validation
- Validate detections using:
  - Simulated “copy many files into a new directory” and “create archive in staging dir” sequences.
  - Remote staging tests that include lateral auth + large SMB writes.
- Community tests (where available):
  - https://github.com/redcanaryco/atomic-red-team

## 14. References
- MITRE ATT&CK. (n.d.). *Data Staged (T1074)*. https://attack.mitre.org/techniques/T1074/
- MITRE ATT&CK. (n.d.). *Detection Strategy for Data Staged (DET0014)*. https://attack.mitre.org/detections/DET0014/
- Huntress. (2023-08-11). *Investigating New INC Ransom Group Activity*. https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity

## 15. Notes
- 
