---
entity_type: mitre_technique

technique_id: "T1025"
subtechnique_id: ""
technique_name: "Data from Removable Media"

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
  - "[[30_CIPHER/03_Threat_Actors/G0040 - Patchwork|Patchwork (G0040)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed (S0622)]]"
  - "[[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]]"
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

## 1. Summary
Adversaries may search and collect data from removable media connected to compromised systems (USB storage, external drives, optical media). This technique can support offline transfer, collection from air-gapped segments, or opportunistic theft of sensitive documents.

## 2. Technical Overview
Common behaviors:
- **Detection of device insertion** followed by enumeration of new volumes/mount points.
- **File search + selective copy** based on extensions/keywords or directory targets.
- **Automated collection** triggered by device events (mount/attach) rather than interactive browsing.
- **Staging on host** (e.g., temp directories) before exfiltration or later retrieval.

High-signal context:
- Office/document file access shortly after USB insertion by non-user-facing processes.
- Bulk copy operations to hidden/temp directories.
- Repeated USB access across multiple hosts by the same account or process lineage.

## 3. Subtechnique Considerations
- No subtechniques for this technique.
- Tuning depends heavily on workstation norms (developers/IT commonly use USB storage); prioritize:
  - Privileged endpoints, jump boxes, and sensitive servers where removable media should be rare.
  - Correlation with suspicious process execution or recent compromise indicators.

## 4. Procedure Examples
ATT&CK documents examples including:
- [[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed (S0622)]] can find and collect data from removable media devices.
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]] backdoor behavior may collect entire contents of an inserted USB device.
- [[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]] copies files with certain extensions from USB devices.

## 5. Detection Guidance
ATT&CK provides a detection strategy for removable media collection (DET0511), focusing on mount events followed by enumeration/copy/compress actions.

Detection ideas:
- **Device event → suspicious process chain**
  - USB mount/attach events followed by scripting engines, shells, or uncommon binaries accessing the new volume.
- **Bulk file access patterns**
  - Rapid traversal of directories and copying of many documents immediately after insertion.
- **Staging indicators**
  - Creation of archives or collections in temp locations following removable media access.
- **Policy violation detections**
  - Any removable media mount on systems with “no USB storage” policy should be high severity.

### Data Source Notes
Recommended telemetry:
- OS device/mount events (Windows removable storage events; macOS/Linux mount logs).
- EDR process telemetry and file access signals (where available).
- DLP/endpoint control logs for USB policy enforcement.
- File creation events for archives/staged bundles.

## 6. Response Guidance
1. **Containment**
   - Isolate the host if active collection is suspected; preserve removable media if available.
   - Disable/rotate credentials if compromise is confirmed.
2. **Investigation**
   - Identify which volumes were accessed and what was copied/staged.
   - Collect artifacts of staging directories and created archives; timeline device insertion to file operations.
3. **Eradication**
   - Remove malware/tooling; remediate initial access vector.
4. **Hardening**
   - Enforce removable media controls, endpoint device control, and DLP rules.
   - Increase monitoring on sensitive endpoints for USB mount + bulk file reads.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1025 - Data from Removable Media|T1025]]

## 8. SOC Relevance
- Useful indicator for:
  - Insider-threat-like behaviors (mass copy to USB)
  - Malware that opportunistically steals files from newly mounted drives
  - Air-gap bridging scenarios
- Highest confidence detections typically rely on **device attach + abnormal process/file activity** correlation.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]: documented USB content collection behavior.

## 10. Campaign Usage
- 

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed (S0622)]]: removable media data collection.
- [[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]]: copies targeted files from USB devices.

## 12. Mitigations
- **M1057 - Data Loss Prevention:** restrict access to sensitive data and detect unencrypted sensitive data movement.
- Enforce device control policies for removable storage (allowlist/denylist, read-only modes).
- Limit local admin privileges that can disable device controls.

## 13. Testing & Validation
- Test detections by:
  - Inserting removable media on a test endpoint and validating alerts for “device attach → bulk copy by shell/script”.
  - Verifying policy-based blocks are logged and centralized.
- Community tests (where available):
  - https://github.com/redcanaryco/atomic-red-team

## 14. References
- MITRE ATT&CK. (n.d.). *Data from Removable Media (T1025)*. https://attack.mitre.org/techniques/T1025/
- MITRE ATT&CK. (n.d.). *Detection of Data Access and Collection from Removable Media (DET0511)*. https://attack.mitre.org/detections/DET0511/
- Trend Micro. (2017-12). *Untangling the Patchwork Cyberespionage Group* (tech brief). https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf

## 15. Notes
- 
