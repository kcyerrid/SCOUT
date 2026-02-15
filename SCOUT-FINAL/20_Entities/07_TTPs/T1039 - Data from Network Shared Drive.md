---
entity_type: mitre_technique

technique_id: "T1039"
subtechnique_id: ""
technique_name: "Data from Network Shared Drive"

tactic:
  - TA0009 - Collection
platforms:
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
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group (G0047)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]]"
  - "[[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay (S0458)]]"
associated_campaigns:
  - "C0015"
related_techniques: []

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
Adversaries may collect sensitive files from network-accessible shared drives (e.g., SMB/CIFS, NFS, file servers, administrative shares) that are reachable from a compromised host. This often occurs after discovery of shares and before staging/exfiltration.

## 2. Technical Overview
Observable behaviors commonly include:
- **Mounting or mapping shares** from endpoints/servers, then browsing/copying targeted content.
- **Abuse of administrative shares** (e.g., C$, ADMIN$) or centrally hosted file servers.
- **Scripted collection** using shells, interpreters, or dual-use utilities that enumerate and copy in bulk.
- **Follow-on staging** to local temp paths or centralized staging hosts.

High-signal context:
- Unusual share access by non-file-management processes (e.g., scripting engines).
- New access patterns from hosts/users that do not typically interact with file servers.
- Large read/copy bursts from shares followed by outbound network activity.

## 3. Subtechnique Considerations
- No subtechniques for this technique.
- Consider environment-specific baselining:
  - Workstations with legitimate mapped drives vs. servers that should rarely mount user shares.
  - Service accounts used for backups/IT jobs (common source of false positives).

## 4. Procedure Examples
Examples documented in ATT&CK include:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]] collected files from network shared drives.
- [[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]] crawls mapped drives and collects targeted document types.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group (G0047)]] malware collected Microsoft Office documents from mapped network drives.
- [[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay (S0458)]] can collect data from network drives and stage it for exfiltration.
- Campaign: **C0015** involved collecting files from network shared drives prior to encryption activity.

## 5. Detection Guidance
ATT&CK provides a detection strategy for this technique (DET0410) that emphasizes monitoring access to network shares followed by unusual read/copy operations.

Practical detection ideas:
- **Share access by unusual processes**
  - PowerShell/script interpreters, certutil, LOLBins, or unexpected binaries accessing SMB/NFS mounts.
- **Anomalous access patterns**
  - New client host accessing a share; off-hours access; sudden expansion in file types/paths accessed.
- **Bulk copy signals**
  - Many file reads/copies from a share in a short time; large total bytes read; rapid traversal of directories.
- **Sequence detections**
  - Share enumeration → bulk read/copy → archive creation → egress spike.

### Data Source Notes
Recommended telemetry:
- File server logs (SMB/NFS access logs, object access auditing).
- Endpoint EDR on clients and file servers (process + network connections to file server ports).
- Authentication logs (Kerberos/NTLM, service account use, lateral auth anomalies).
- Network telemetry (SMB session creation, data transfer volumes).

## 6. Response Guidance
1. **Containment**
   - Restrict access to impacted shares; disable suspicious accounts; enforce temporary allowlists.
2. **Scoping**
   - Identify which shares and paths were accessed; enumerate files touched; determine whether staging occurred.
3. **Eradication**
   - Remove attacker tooling and persistence; remediate credential compromise that enabled share access.
4. **Hardening**
   - Least privilege on shares, separate admin shares, enforce SMB signing where appropriate, and improve auditing.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1039 - Data from Network Shared Drive|T1039]]

## 8. SOC Relevance
- High relevance in ransomware/extortion and espionage workflows (file server data concentration).
- Strongest signals come from:
  - **Unusual principal** + **unusual process** + **bulk share access** + **staging/exfil follow-on**.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]: documented file collection from shares.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group (G0047)]]: mapped drive document collection.

## 10. Campaign Usage
- C0015: collected files from network shared drives prior to network encryption activity.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]]: crawls mapped drives to collect documents.
- [[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay (S0458)]]: collects from network drives and stages for exfiltration.

## 12. Mitigations
- Preventive controls are limited because this technique abuses normal file-sharing features; prioritize:
  - Least privilege and segmentation for shares
  - Strong authentication controls and monitoring
  - Enhanced auditing and anomaly detection on file servers

## 13. Testing & Validation
- Validate alerts against:
  - Legitimate backup/IT tooling vs. ad-hoc bulk copy by shells/scripts.
  - Access to admin shares from non-admin endpoints.
- Community tests (where available):
  - https://github.com/redcanaryco/atomic-red-team

## 14. References
- MITRE ATT&CK. (n.d.). *Data from Network Shared Drive (T1039)*. https://attack.mitre.org/techniques/T1039/
- MITRE ATT&CK. (n.d.). *Detection Strategy for Data from Network Shared Drive (DET0410)*. https://attack.mitre.org/detections/DET0410/
- NSA, CISA, FBI, & NCSC. (2021-07). *Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments* (Cybersecurity Advisory). https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF

## 15. Notes
- 
