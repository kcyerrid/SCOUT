---
entity_type: mitre_technique

technique_id: "T1560"
subtechnique_id: ""
technique_name: "Archive Collected Data"

tactic:
  - "TA0009 - Collection"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "Process Creation (DC0032)"
  - "File Creation (DC0039)"
  - "Module Load (DC0016)"
  - "Command Execution (DC0064)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0037 - FIN6|FIN6]]"
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]]"
  - "[[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed]]"
  - "[[30_CIPHER/05_Malware/S0642 - BADFLICK|BADFLICK]]"
associated_campaigns: []
related_techniques: []

detection_priority:
  - High

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
Adversaries may compress and/or encrypt collected data prior to exfiltration to reduce size, obfuscate contents, and evade content inspection. This technique is commonly observed immediately before exfiltration, and often coincides with staging activity in temporary/user-writable directories.

## 2. Technical Overview
**What it is:** Packaging (compression) and/or protecting (encryption/encoding) collected artifacts—documents, logs, dumps, database extracts—into archives or encrypted blobs for transport.

**Common defender-relevant behaviors:**
- Execution of archiving/encryption tooling (native or third-party) followed by creation of new archive/container files.
- Archive output written to staging paths: user profile folders, `%TEMP%`, `/tmp`, `/var/tmp`, hidden or newly created directories.
- Sudden appearance of large `.zip/.rar/.7z/.cab/.tar.*` outputs or high-entropy files shortly before outbound transfers.
- Parent/child anomalies (e.g., Office/browser processes spawning archivers; service accounts performing interactive-like compression).

**Why it matters:** Archive creation is often a “last-mile” step in the collection→staging→exfil chain; it is usually higher-signal than many discovery events, especially when correlated with subsequent network egress.

## 3. Subtechnique Considerations
Archive Collected Data can be implemented via:
- **[[20_Entities/07_TTPs/TA0009 - Collection/T1560.001 - Archive via Utility|T1560.001]]** (utilities like `zip`, `tar`, `7z`, `rar`, `makecab`, `certutil` encoding)
- **[[20_Entities/07_TTPs/TA0009 - Collection/T1560.002 - Archive via Library|T1560.002]]** (libraries like zlib/libzip used inside malware/scripts)
- **[[20_Entities/07_TTPs/TA0009 - Collection/T1560.003 - Archive via Custom Method|T1560.003]]** (custom routines such as XOR/stream ciphers, bespoke containers)

Detection strategy and telemetry requirements differ significantly by subtechnique; prioritize building coverage for utilities first (most observable), then library/custom (more behavioral).

## 4. Procedure Examples
Examples documented by ATT&CK include:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]] compressing collected documents prior to exfiltration.
- [[30_CIPHER/03_Threat_Actors/G0037 - FIN6|FIN6]] compressing collected logs before staging/exfiltration.
- Malware families compressing and/or encrypting outputs prior to transfer (e.g., [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]]).

## 5. Detection Guidance
Model detection around **correlation** (tool execution → archive creation → egress), not single events.

**High-signal analytics patterns (MITRE DET0526):**
- Correlate creation of archive files with nearby process execution of compression/encryption utilities (Windows/macOS) or command execution (Linux).
- Detect suspicious archiving utilities invoked from unusual parents or user contexts.
- Identify archive creation in staging directories, especially shortly before outbound network events.
- Flag use of encryption switches / password-protection usage (where command line is visible) and creation of high-entropy archives.

### 5.1 Data Source Notes
Primary data components for DET0526:
- **Process Creation (DC0032)**: Windows Security 4688, Sysmon Event 1, macOS unified logs (process exec)
- **File Creation (DC0039)**: Sysmon Event 11, auditd file create/write, macOS fs usage/unified logs
- **Module Load (DC0016)**: Sysmon Event 7 / platform equivalents (notably crypto/compression libs)
- **Command Execution (DC0064)**: auditd execve for Linux command-line tools

**Telemetry tips:**
- Ensure command-line capture for process creation where possible (Windows 4688 w/ command line, Sysmon, EDR).
- Capture file hashes/size/paths for new archives; size thresholds reduce noise.
- Add staging-path allow/deny lists and business-approved archivers to reduce false positives.

## 6. Response Guidance
1. **Scope the archive(s):** Identify created archive files, paths, sizes, and timestamps; preserve copies and hashes.
2. **Attribute the creator:** Determine process tree, user context, parent process, and execution source (interactive vs service).
3. **Assess intent:** Check if archive creation is followed by outbound connections, uploads, or removable media writes.
4. **Contain:** Isolate host if exfil is suspected; block associated egress destinations and revoke exposed credentials.
5. **Hunt laterally:** Search for similar archive artifacts and tool executions across endpoints in the same time window.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1560 - Archive Collected Data|T1560]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1560.001 - Archive via Utility|T1560.001]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1560.002 - Archive via Library|T1560.002]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1560.003 - Archive via Custom Method|T1560.003]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1074 - Data Staged|T1074]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1074.002 - Remote Data Staging|T1074.002]]

## 8. SOC Relevance
**Primary use-cases:**
- Pre-exfiltration staging detection and early containment.
- Insider-risk / data loss investigations (archive creation + unusual destination).
- Ransomware and extortion operations (archive-and-steal patterns).

**Prioritization cues:**
- Unusual parent process + archive created in staging path + subsequent network egress.
- Archive creation by privileged/service accounts outside maintenance windows.
- Password-protected/encrypted archives created shortly before external transfer.

## 9. Threat Actor Usage
ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]
- [[30_CIPHER/03_Threat_Actors/G0037 - FIN6|FIN6]]
- [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]

## 10. Campaign Usage
No specific campaigns are enumerated on the ATT&CK T1560 technique page (use subtechnique pages for campaign-level examples where available).

## 11. Malware Usage
ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]]
- [[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed]]
- [[30_CIPHER/05_Malware/S0642 - BADFLICK|BADFLICK]]

## 12. Mitigations
- **M1047 – Audit:** Conduct periodic scans and inventorying to identify unauthorized archiving/encryption utilities and suspicious use in endpoints/servers.

## 13. Testing & Validation
- Execute controlled, authorized tests mapped to T1560 to validate:
  - Process creation visibility (command line capture).
  - File creation telemetry for archive/container outputs.
  - Correlation rules (exec → archive create → outbound).
- Use Atomic Red Team tests for T1560 to verify alerting and triage playbooks.

## 14. References
- MITRE ATT&CK. (2025, October 24). *Archive Collected Data (T1560).* https://attack.mitre.org/techniques/T1560/
- MITRE ATT&CK. (2025, October 21). *Detect Archiving and Encryption of Collected Data (DET0526).* https://attack.mitre.org/detectionstrategies/DET0526/
- Red Canary. (n.d.). *Atomic Red Team: T1560 – Archive Collected Data.* https://www.atomicredteam.io/atomic-red-team/atomics/T1560

## 15. Notes
- Treat archive creation as a **correlation problem**: the strongest signal emerges when paired with staging paths and subsequent egress.
- For deeper coverage, build dedicated detections for each subtechnique (utility/library/custom) due to different telemetry surfaces.
