---
entity_type: mitre_technique

technique_id: "T1005"
subtechnique_id: ""
technique_name: "Data from Local System"

tactic:
  - TA0009 - Collection
platforms:
  - ESXi
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group (G0047)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1028 - Action RAT|Action RAT (S1028)]]"
  - "[[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]]"
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

## 1. Summary
Adversaries may collect sensitive data from a compromised host’s local sources (file systems, configuration files, local databases, VM artifacts, logs, or other resident data) prior to exfiltration. This is a broad, high-frequency collection behavior that often accompanies discovery, staging, and exfiltration workflows.

## 2. Technical Overview
Common patterns include:
- **Recursive file enumeration + selective reads** (documents, credentials, configs, archives).
- **Targeted artifact collection** (VM files, browser profiles, keychains, SSH keys, local databases).
- **Use of native interpreters/CLIs** to access local storage (including network device CLIs).
- **Pre-exfil staging** (temporary directories, renamed archives) to consolidate data.

High-signal context:
- New or unusual processes reading many user directories.
- Large bursts of file reads followed by compression/staging and outbound transfer.

## 3. Subtechnique Considerations
- No subtechniques for this technique.
- When tuning, segment detections by environment:
  - **Endpoints vs. servers** (file types and access patterns differ).
  - **Network devices/ESXi** (CLI-driven collection and configuration pulls).

## 4. Procedure Examples
ATT&CK documents many examples; selected highlights:
- [[30_CIPHER/05_Malware/S1028 - Action RAT|Action RAT (S1028)]] can collect local data from infected machines.
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]] collected files from local victims.
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]] retrieved internal documents and used tooling (e.g., Forfiles) to stage documents before exfiltration.
- [[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]] crawls local drives and collects targeted document types.

## 5. Detection Guidance
ATT&CK provides a detection strategy for local data collection prior to exfiltration (DET0380), emphasizing recursive listings, targeted reads, and staging patterns.

Detection approaches:
- **Behavioral file-access detections**
  - Unusual processes performing high-volume reads across user profiles, shared folders, and sensitive paths.
  - Access to “high-value” file patterns (finance/hr/legal folders; credential/config directories).
- **Process + file correlation**
  - Script interpreters/shells spawning file enumeration utilities, followed by archive utilities or copy operations.
- **Timeboxed “collection bursts”**
  - Atypical surge in file read operations within a short window, especially post-compromise or after privilege escalation.

### Data Source Notes
Recommended telemetry:
- Endpoint EDR: process creation, command-line, parent/child chains, loaded modules.
- File system telemetry: file open/read events (where feasible), mass read indicators, archive creation.
- Security logs: access to protected directories, removable media mount events (where applicable).
- Network telemetry: outbound transfers that follow local collection/staging.

## 6. Response Guidance
1. **Containment**
   - Isolate impacted hosts if active collection is ongoing.
   - Disable/rotate suspected compromised accounts; revoke tokens/sessions.
2. **Scoping**
   - Identify accessed directories and file patterns; locate staging paths and newly created archives.
   - Correlate process trees with file access windows.
3. **Eradication**
   - Remove malicious tooling; close initial access vector; patch and harden.
4. **Recovery**
   - Deploy/expand telemetry for file-access and staging signals; add least-privilege controls for sensitive paths.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1005 - Data from Local System|T1005]]

## 8. SOC Relevance
- Extremely common across intrusions; prioritize **high-value targets** (servers, admin endpoints) and **high-signal tools** (shells, LOLBins, remote tooling).
- Strongest detections usually combine:
  - **Process context** + **file read patterns** + **subsequent staging/exfil** indicators.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1 (G0006)]]: local file collection.
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]: internal document retrieval and staging for exfiltration.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group (G0047)]]: collects files from infected systems and uploads to C2 (also uses related collection techniques).

## 10. Campaign Usage
- 

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1028 - Action RAT|Action RAT (S1028)]]: local data collection capability.
- [[30_CIPHER/05_Malware/S0128 - BADNEWS|BADNEWS (S0128)]]: targeted document crawling/collection.

## 12. Mitigations
- **M1057 - Data Loss Prevention:** restrict and alert on access to sensitive data; detect unencrypted sensitive data movement.
- **M1022 - Restrict File and Directory Permissions:** limit access to high-value folders and secrets.
- **M1030 - Network Segmentation:** reduce attacker reach to file servers and sensitive systems.
- **M1047 - Audit:** ensure robust endpoint logging and adequate retention for file/process telemetry.

## 13. Testing & Validation
- Validate with controlled scenarios:
  - Benign admin tooling vs. shell-driven mass enumeration + archive creation.
  - Confirm detections alert on “new process reading many user docs” patterns.
- Where available, leverage community tests:
  - https://github.com/redcanaryco/atomic-red-team

## 14. References
- MITRE ATT&CK. (n.d.). *Data from Local System (T1005)*. https://attack.mitre.org/techniques/T1005/
- MITRE ATT&CK. (n.d.). *Detection of Local Data Collection Prior to Exfiltration (DET0380)*. https://attack.mitre.org/detections/DET0380/
- Cisco. (2022-08-16). *show running-config - Cisco IOS Configuration Fundamentals Command Reference*. https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html

## 15. Notes
- 
