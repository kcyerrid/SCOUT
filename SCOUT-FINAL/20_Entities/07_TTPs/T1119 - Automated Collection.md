---
entity_type: mitre_technique

technique_id: "T1119"
subtechnique_id: ""
technique_name: "Automated Collection"

tactic:
  - "TA0009 - Collection"
platforms:
  - IaaS
  - Linux
  - Office Suite
  - SaaS
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1030 - Agrius|Agrius]]"
  - "[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]]"
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0125 - HAFNIUM|HAFNIUM]]"
  - "[[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0363 - Empire|Empire]]"
  - "[[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]]"
  - "[[30_CIPHER/05_Malware/S1213 - Lumma Stealer|Lumma Stealer]]"
associated_campaigns: []
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
Adversaries use **Automated Collection** to repeatedly gather targeted data (files, user data, cloud artifacts) using scripts, native utilities, cloud APIs, or automation frameworks. The value is scale: once criteria are defined (paths, extensions, object types), collection runs continuously or in bursts—often preceding staging/exfiltration.

## 2. Technical Overview
Common implementation patterns:
- **Host-based scripting/automation**: scheduled tasks/cron/launch agents invoking shell, PowerShell, or scripting runtimes to enumerate and copy files on an interval.
- **Native “collection primitives”**: command-line utilities to list/search/copy, plus compression/encoding for staging.
- **Cloud API-driven collection**: programmatic access to mailbox/drive/storage via service APIs (e.g., graph/drive/storage APIs) using non-interactive clients.
- **RAT-integrated automation**: remote access tools provide built-in jobing or “module loops” to continuously harvest.

Operationally, this technique often chains with discovery (to identify what to collect), staging (compress/encrypt/encode), and exfiltration.

## 3. Subtechnique Considerations
- **No sub-techniques** (Enterprise).

## 4. Procedure Examples
Representative ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1030 - Agrius|Agrius]] used a custom tool to query SQL databases and extract PII.
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]] used batch scripting to automate discovery and store results for later retrieval.
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]] used tooling to gather/compress multiple documents from victim networks.
- [[30_CIPHER/03_Threat_Actors/G0125 - HAFNIUM|HAFNIUM]] leveraged Graph/API access to collect data from cloud services (e.g., mail/drive/share).
- [[30_CIPHER/05_Malware/S0363 - Empire|Empire]] supports automated system/user data collection modules.
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]] can automate collection of cloud artifacts (e.g., templates/reports/credential reports).
(ATT&CK lists many additional group/software examples on the technique page.)

## 5. Detection Guidance
Key detection opportunities hinge on identifying **automation** + **repeatability** + **scope**.

Behavioral signals:
- **Repeated file access** across user/profile directories in a short time window (especially many extensions/types).
- **Burst collection** followed by staging actions (archive/encrypt/encode) and outbound transfer.
- **Scripting engines** spawning file utilities at cadence (cron/schtasks/launchd).
- **Non-interactive cloud access** from atypical user agents (CLI/Python/PowerShell) performing high-volume drive/mail/storage reads.
- **RAT job loops** producing periodic IO spikes without user interaction.

Analytic starting points:
- “**Automation cadence**” detections: same command pattern repeating every N minutes (parent/child, arguments, targets).
- “**Wide fan-out**” detections: one process enumerating/reading many files across disparate directories rapidly.
- “**Cloud read spikes**” detections: sudden increase in object/file/message reads by a principal, role, or token that historically does not.

### 5.1 Data Source Notes
- ATT&CK v18+ expresses detection as **Detection Strategies/Analytics** and **Data Components**; populate `datasources` from your ATT&CK STIX/ADM pipeline if your vault requires explicit data source names.
- Ensure telemetry coverage for:
  - Process execution lineage (parent/child), command lines
  - File access and file read metadata at scale
  - Scheduling/automation artifacts (task/cron/launch agents)
  - Cloud audit logs for object/file/mail access (principal, user agent, token type, source IP, volume)

## 6. Response Guidance
1. **Triage scope**: identify the initiating process/user/token, recurrence schedule, and breadth of accessed locations/objects.
2. **Contain**: isolate host/session or revoke cloud tokens/refresh tokens; disable suspicious automation entries (tasks/cron/agents).
3. **Hunt for staging/exfil**: search for new archives, temp staging directories, or outbound transfers adjacent in time.
4. **Credential hygiene (cloud)**: rotate potentially exposed keys/tokens; review OAuth grants and service principals used for programmatic access.
5. **Eradicate**: remove scripts/modules and persistence; validate no re-creation via GPO/MDM/management tooling.

## 7. Related ATT&CK Content
- Primary:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1119 - Automated Collection|T1119]]

## 8. SOC Relevance
High SOC value due to:
- Frequent presence in real intrusions (collection is a prerequisite for monetization/espionage).
- Good detection leverage when you baseline normal file/API access volumes and automate anomaly rules.
- Strong correlation across telemetry domains (endpoint + cloud + network) when attackers scale collection.

## 9. Threat Actor Usage
Notable ATT&CK-listed examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G1030 - Agrius|Agrius]], [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]], [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]], [[30_CIPHER/03_Threat_Actors/G0125 - HAFNIUM|HAFNIUM]], [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]].

## 10. Campaign Usage
ATT&CK lists campaign usage on the technique page where applicable.

## 11. Malware Usage
Notable ATT&CK-listed examples (non-exhaustive):
- [[30_CIPHER/05_Malware/S0363 - Empire|Empire]], [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]], [[30_CIPHER/05_Malware/S1213 - Lumma Stealer|Lumma Stealer]].

## 12. Mitigations
ATT&CK provides mitigations for this technique; align controls to reduce automated harvesting:
- Harden and monitor automation primitives (scheduled tasks/cron/launch agents), and restrict scripting where feasible.
- Apply least privilege for file access and cloud storage/mail permissions; prefer short-lived tokens.
- Increase auditing around bulk reads and suspicious user agents.
(Refer to the ATT&CK technique page for the authoritative mitigation list.)

## 13. Testing & Validation
- Validate endpoint visibility by simulating benign “bulk file read” patterns (controlled test directories) and confirming:
  - process lineage + command lines
  - file access telemetry volume and performance
- Validate cloud visibility by performing controlled high-volume reads in a test tenant and confirming:
  - audit log completeness (principal, user agent, IP, object count)
  - alert thresholds for anomalous volume and new user agents

## 14. References
- MITRE ATT&CK. (2025, October 24). *Automated Collection (T1119)*. https://attack.mitre.org/techniques/T1119/
- Mandiant Intelligence. (2023, September 14). *Why Are You Texting Me? UNC3944 Leverages SMS Phishing Campaigns for SIM Swapping, Ransomware, Extortion, and Notoriety.* https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware
- Or Chechik, Tom Fakterman, Daniel Frank, & Assaf Dahan. (2023, November 6). *Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors.* https://unit42.paloaltonetworks.com/agrius-targeting-israel/

## 15. Notes
- Populate `datasources` from ATT&CK STIX/ADM if your vault enforces explicit data source naming.
- Prioritize detections that combine **automation cadence** + **bulk access** + **staging/exfil adjacency**.
