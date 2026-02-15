---
entity_type: mitre_technique

technique_id: "T1091"
subtechnique_id: ""
technique_name: "Replication Through Removable Media"

tactic:
  - "TA0008 - Lateral Movement"
  - "TA0001 - Initial Access"
platforms:
  - Windows
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1007 - Aoqin Dragon|Aoqin Dragon]]"
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0012 - Darkhotel|Darkhotel]]"
  - "[[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7]]"
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G1014 - LuminousMoth|LuminousMoth]]"
  - "[[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]"
  - "[[30_CIPHER/03_Threat_Actors/G0081 - Tropic Trooper|Tropic Trooper]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0092 - Agent.btz|Agent.btz]]"
  - "[[30_CIPHER/05_Malware/S1074 - ANDROMEDA|ANDROMEDA]]"
  - "[[30_CIPHER/05_Malware/S0023 - CHOPSTICK|CHOPSTICK]]"
  - "[[30_CIPHER/05_Malware/S0608 - Conficker|Conficker]]"
  - "[[30_CIPHER/05_Malware/S0115 - Crimson|Crimson]]"
  - "[[30_CIPHER/05_Malware/S0062 - DustySky|DustySky]]"
  - "[[30_CIPHER/05_Malware/S0143 - Flame|Flame]]"
  - "[[30_CIPHER/05_Malware/S0132 - H1N1|H1N1]]"
  - "[[30_CIPHER/05_Malware/S1230 - HIUPAN|HIUPAN]]"
  - "[[30_CIPHER/05_Malware/S0385 - njRAT|njRAT]]"
  - "[[30_CIPHER/05_Malware/S0013 - PlugX|PlugX]]"
  - "[[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]"
  - "[[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay]]"
  - "[[30_CIPHER/05_Malware/S1130 - Raspberry Robin|Raspberry Robin]]"
  - "[[30_CIPHER/05_Malware/S0028 - SHIPSHAPE|SHIPSHAPE]]"
  - "[[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]]"
  - "[[30_CIPHER/05_Malware/S0130 - Unknown Logger|Unknown Logger]]"
  - "[[30_CIPHER/05_Malware/S0386 - Ursnif|Ursnif]]"
  - "[[30_CIPHER/05_Malware/S0452 - USBferry|USBferry]]"
  - "[[30_CIPHER/05_Malware/S0136 - USBStealer|USBStealer]]"
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

# T1091 - Replication Through Removable Media

## 1. Summary
Adversaries may move onto systems—potentially including disconnected or air-gapped networks—by copying malware to removable media and triggering execution when the media is inserted into another system. This can support **Initial Access** and **Lateral Movement**, including via Autorun behaviors or user execution of disguised binaries.

## 2. Technical Overview
Common attacker behaviors include:
- Writing malicious files onto removable media (USB drives, external storage) to propagate between systems.
- Abusing Autorun-related behaviors (where enabled) or tricking users into launching a malicious file that resembles legitimate content.
- Modifying legitimate executables on removable media or hiding legitimate documents while placing a similarly named executable.

Defender-relevant characteristics:
- Propagation chains often include: removable drive mount → file write activity on the drive → subsequent process execution from the removable drive on another host.
- Removable-media propagation can bypass network controls and segmentation if users physically move media between systems.

## 3. Subtechnique Considerations
T1091 has **no subtechniques**.
- Coverage should include both endpoints that originate the infection (writing to USB) and endpoints that receive it (executing from USB).
- Environments with strong device control policies may still be exposed via exceptions (contractors, IT imaging workflows, kiosks, OT maintenance).

## 4. Procedure Examples
MITRE ATT&CK documents removable-media replication including:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]] infecting USB devices to transfer malware to air-gapped computers.
- [[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7]] mailing malicious USB drives to victims to deliver malware and enable follow-on activity.
- [[30_CIPHER/03_Threat_Actors/G0012 - Darkhotel|Darkhotel]] modifying executables stored on removable media to spread.
- [[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]] propagating via removable media (including Autorun and LNK exploitation paths, as documented by ATT&CK references).
- [[30_CIPHER/05_Malware/S1130 - Raspberry Robin|Raspberry Robin]] historically using infected USB media to spread.

## 5. Detection Guidance
Detection should emphasize **device mount + file write + execution correlation**, not isolated events.

High-value detection patterns:
- Removable drive mount followed by creation or modification of:
  - Executables, scripts, shortcuts, or suspicious autorun configuration files on the removable drive.
- Process execution originating from removable media shortly after mount, especially:
  - Unsigned or untrusted binaries
  - Suspicious parent processes (Explorer launching an unusual executable from removable media)
- Evidence of propagation:
  - Multiple hosts executing similarly named binaries from removable media within a time window
  - Same removable device identifier associated with execution events on multiple hosts

MITRE Detection Strategy (technique analytics):
- **DET0301 – Removable Media Execution Chain Detection via File and Process Activity** (execution of files from removable media after drive mount, correlated to file write activity, autorun usage, or staged tool spread).

### 5.1. Data Source Notes
Telemetry requirements for high-confidence detection:
- Removable device insertion/mount telemetry (device identifiers, drive letters/mount points, timestamps).
- File creation/modification telemetry on removable drives.
- Process creation telemetry that includes image path and originating drive.
- (Optional but valuable) code signing reputation and policy outcomes (application control, ASR decisions).

## 6. Response Guidance
- Contain: isolate impacted hosts; block execution from removable media where feasible; quarantine suspect removable devices.
- Scope: identify other hosts that mounted or executed from the same removable device identifier; hunt for the same file hashes and paths.
- Remediate: remove malicious files from endpoints and removable media; rotate credentials if post-compromise actions are suspected.
- Recover: validate no persistence was established beyond removable-media propagation and confirm clean reimaging criteria where required.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1091 - Replication Through Removable Media|T1091]]
- [[20_Entities/07_TTPs/TA0001 - Initial Access/T1091 - Replication Through Removable Media|T1091]]

## 8. SOC Relevance
High-signal triage pivots:
- Which process executed from removable media, and what was the parent process?
- What files were written to the removable media before execution (timestamps and hashes)?
- Did the same removable media identifier appear across multiple hosts?
- Are there signs of follow-on activity (new services/tasks, outbound connections, credential access)?

## 9. Threat Actor Usage
Documented examples include:
- [[30_CIPHER/03_Threat_Actors/G1007 - Aoqin Dragon|Aoqin Dragon]]
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]
- [[30_CIPHER/03_Threat_Actors/G0012 - Darkhotel|Darkhotel]]
- [[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7]]
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]
- [[30_CIPHER/03_Threat_Actors/G1014 - LuminousMoth|LuminousMoth]]
- [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]
- [[30_CIPHER/03_Threat_Actors/G0081 - Tropic Trooper|Tropic Trooper]]

## 10. Campaign Usage
- None explicitly captured in this note.

## 11. Malware Usage
Documented examples include:
- [[30_CIPHER/05_Malware/S0092 - Agent.btz|Agent.btz]]
- [[30_CIPHER/05_Malware/S1074 - ANDROMEDA|ANDROMEDA]]
- [[30_CIPHER/05_Malware/S0023 - CHOPSTICK|CHOPSTICK]]
- [[30_CIPHER/05_Malware/S0608 - Conficker|Conficker]]
- [[30_CIPHER/05_Malware/S0115 - Crimson|Crimson]]
- [[30_CIPHER/05_Malware/S0062 - DustySky|DustySky]]
- [[30_CIPHER/05_Malware/S0143 - Flame|Flame]]
- [[30_CIPHER/05_Malware/S0132 - H1N1|H1N1]]
- [[30_CIPHER/05_Malware/S1230 - HIUPAN|HIUPAN]]
- [[30_CIPHER/05_Malware/S0385 - njRAT|njRAT]]
- [[30_CIPHER/05_Malware/S0013 - PlugX|PlugX]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]
- [[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay]]
- [[30_CIPHER/05_Malware/S1130 - Raspberry Robin|Raspberry Robin]]
- [[30_CIPHER/05_Malware/S0028 - SHIPSHAPE|SHIPSHAPE]]
- [[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]]
- [[30_CIPHER/05_Malware/S0130 - Unknown Logger|Unknown Logger]]
- [[30_CIPHER/05_Malware/S0386 - Ursnif|Ursnif]]
- [[30_CIPHER/05_Malware/S0452 - USBferry|USBferry]]
- [[30_CIPHER/05_Malware/S0136 - USBStealer|USBStealer]]

## 12. Mitigations
ATT&CK-listed mitigations for T1091 include:
- **M1040 – Behavior Prevention on Endpoint**: enable controls that block suspicious execution patterns from removable drives (e.g., Attack Surface Reduction rules on Windows 10, as referenced by ATT&CK).
- **M1042 – Disable or Remove Feature or Program**: disable Autorun where unnecessary; restrict removable media at policy level if not required.
- **M1034 – Limit Hardware Installation**: limit the use of USB devices and removable media within the network.

## 13. Testing & Validation
- Validate drive insertion/mount telemetry collection across endpoints (including device IDs).
- Confirm file creation telemetry includes removable drive paths and timestamps.
- Test detections using controlled simulations that:
  - Write a benign test executable to a removable drive
  - Execute it after mount and ensure correlation logic triggers appropriately
- Verify application control/ASR policies prevent execution from removable media in targeted high-risk segments.

## 14. References
- MITRE. (n.d.). *Replication Through Removable Media (T1091)*. MITRE ATT&CK. https://attack.mitre.org/techniques/T1091/
- Microsoft. (n.d.). *Attack Surface Reduction rules reference*. https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference
- Microsoft Support. (n.d.). *How to disable Autorun/AutoPlay (Windows)*. https://support.microsoft.com/

## 15. Notes
- The most reliable detections are chain-based: mount → write → execute, plus removable device identifier reuse across hosts.
- High-risk environments (OT, air-gapped, classified enclaves) should treat removable media control as a primary security boundary.
