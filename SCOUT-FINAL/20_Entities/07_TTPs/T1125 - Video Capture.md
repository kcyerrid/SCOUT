---
entity_type: mitre_technique

technique_id: "T1125"
subtechnique_id: ""
technique_name: "Video Capture"

tactic:
  - "TA0009 - Collection"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "Process Creation (DC0032)"
  - "Network Connection Creation (DC0082)"
  - "Module Load (DC0016)"
  - "File Creation (DC0039)"
  - "OS API Execution (DC0021)"
  - "Process Metadata (DC0034)"
  - "File Access (DC0055)"
  - "Command Execution (DC0064)"
  - "Network Traffic Content (DC0085)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "G0046 - FIN7"
  - "G1003 - Ember Bear"
  - "G0091 - Silence"
associated_malware:
  - "S0331 - Agent Tesla"
  - "S0363 - Empire"
  - "S0234 - Bandook"
  - "S0334 - DarkComet"
  - "S0591 - ConnectWise"
associated_campaigns: []
related_techniques:
  - "T1113"

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
  - collection
  - video-capture

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Adversaries may capture video (or periodic still images) from webcams, integrated cameras, IP cameras, or video-capable applications to collect intelligence. This differs from screen capture (T1113) by focusing on **camera/device** capture rather than framebuffer capture. (MITRE: T1125)

## 2. Technical Overview
Defender-relevant behaviors commonly fall into three buckets:
- **Windows camera stack access**: unexpected processes interacting with camera frameworks/devices and loading capture-related libraries, then writing video/image artifacts and potentially exfiltrating them. (MITRE: DET0197 / AN0568)
- **Linux V4L2 device access**: processes opening/reading `/dev/video*`, performing capture IOCTL/read loops, and writing sizable video artifacts (or streaming off-host). (MITRE: DET0197 / AN0569)
- **macOS privacy + AVFoundation access**: non-whitelisted binaries receiving/using camera permissions (TCC), opening camera handles/frameworks, and writing `.mov/.mp4` artifacts to unusual locations. (MITRE: DET0197 / AN0570)

Artifacts/telemetry to expect:
- Video/image file creation (extensions such as `.mp4`, `.avi`, `.mov`, raw formats), often in **temp/hidden** directories.
- Library/module loads associated with capture workflows (Windows).
- Device node access (`/dev/video*`) (Linux) or camera permission events (macOS).
- **Optional** correlation with outbound transfer shortly after capture starts. (MITRE: DET0197)

## 3. Subtechnique Considerations
No sub-techniques are defined for T1125.  
Key modeling boundary: T1125 targets **camera/peripheral capture**; for screenshot capture of the display, use [[20_Entities/07_TTPs/TA0009 - Collection/T1113 - Screen Capture|T1113]].

## 4. Procedure Examples
ATT&CK documents broad real-world usage. Examples include:
- Threat Actors:
  - [[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7 (G0046)]] — created custom video recording capability to monitor victim operations. (MITRE: T1125 Procedure Examples)
  - [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear (G1003)]] — exfiltrated images from compromised IP cameras. (MITRE: T1125 Procedure Examples)
  - [[30_CIPHER/03_Threat_Actors/G0091 - Silence|Silence (G0091)]] — observed making videos of victims to monitor bank employees. (MITRE: T1125 Procedure Examples)
- Malware / Tooling:
  - [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]] — accesses webcam/records video. (MITRE: T1125 Procedure Examples)
  - [[30_CIPHER/05_Malware/S0363 - Empire|Empire (S0363)]] — captures webcam data on Windows/macOS. (MITRE: T1125 Procedure Examples)
  - [[30_CIPHER/05_Malware/S0234 - Bandook|Bandook (S0234)]] — modules capable of webcam video capture. (MITRE: T1125 Procedure Examples)

## 5. Detection Guidance
Prioritize detections that combine **unexpected camera access** with **artifact creation** and (optionally) **egress correlation**.

MITRE detection strategy analytics (recommended starting points):
1. **Windows: suspicious camera library loads + artifact creation**  
   - Non-standard process loads camera/video capture libraries, opens camera device pipeline, writes video/image artifacts to unusual locations, and may initiate outbound transfer shortly after. (MITRE: DET0197 / AN0568)
2. **Linux: `/dev/video*` access with continuous capture patterns**  
   - Process opens/reads `/dev/video*` (V4L2), performs repeated IOCTL/read loops, writes large/continuous video artifacts, and/or quickly establishes outbound connections. (MITRE: DET0197 / AN0569)
3. **macOS: TCC camera entitlement + suspicious writers**  
   - Non-whitelisted process triggers/receives camera permission decisions (kTCCServiceCamera), opens camera handles/frameworks, writes `.mov/.mp4` artifacts to unusual locations, and/or beacons soon after. (MITRE: DET0197 / AN0570)

Tuning and false-positive reduction:
- Maintain an allowlist of legitimate camera consumers (conferencing apps, browser processes, recording tools) as suggested by MITRE’s mutable elements (e.g., “AllowedProcesses” / allowlists). (MITRE: DET0197)
- Threshold on **file size** / **continuous access counts** to avoid alerting on thumbnails/snapshots. (MITRE: DET0197)
- Alert more aggressively when capture is initiated by **script hosts**, **office children**, **unsigned binaries**, or from **service contexts**.

### Data Source Notes
Minimum telemetry to support DET0197-style detections:
- **Windows**
  - Process Creation (Sysmon EID 1), Network Connection Creation (Sysmon EID 3/22), Module Load (Sysmon EID 7), File Creation (Sysmon EID 11) (MITRE: DET0197 / AN0568)
  - Camera Frame Server operational logs (process session start/stop events for camera pipeline) as Process Metadata (DC0034) (MITRE: DET0197 / AN0568)
  - Object access auditing for relevant handles/paths where feasible (OS API Execution, DC0021) (MITRE: DET0197 / AN0568)
- **Linux**
  - auditd syscall telemetry for `openat/read/ioctl` targeting `/dev/video*` (OS API Execution, DC0021; File Access, DC0055) (MITRE: DET0197 / AN0569)
  - Optional: osquery process metadata; syslog/sudo command execution for tools used to drive capture (MITRE: DET0197 / AN0569)
- **macOS**
  - Unified log visibility into TCC camera access decisions (OS API Execution, DC0021) and file writes (File Creation, DC0039) (MITRE: DET0197 / AN0570)
  - Endpoint Security framework telemetry (exec/open events) where available (MITRE: DET0197 / AN0570)

## 6. Response Guidance
Triage steps:
1. **Confirm legitimacy**: is the process a known camera consumer? validate signing, install source, user context, and parent process.  
2. **Timeline capture**: correlate first device access → file writes → outbound connections within a tuned window. (MITRE: DET0197)
3. **Evidence collection**: process tree, hashes, loaded modules (Windows), device access audit records (Linux), TCC decision logs (macOS), and created media artifacts.
4. **Assess exposure**: determine if capture targeted webcam vs IP camera vs application; identify likely subjects (meeting apps, office areas, sensitive spaces).
5. **Contain and eradicate**: isolate endpoint, remove tooling/persistence, rotate credentials if concurrent credential access is suspected.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1125 - Video Capture|T1125]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1113 - Screen Capture|T1113]]

## 8. SOC Relevance
- **Why it matters**: high-impact privacy and intelligence loss; can reveal physical environments, whiteboards, meetings, and operational procedures.  
- **Alert quality**: high when a **non-whitelisted** process accesses camera devices and writes sizable media artifacts or exfiltrates shortly after.  
- **Common false positives**: conferencing clients, browsers with camera permissions, device drivers/helpers, legitimate recording software—baseline these explicitly.

## 9. Threat Actor Usage
ATT&CK-documented examples:
- [[30_CIPHER/03_Threat_Actors/G0046 - FIN7|FIN7 (G0046)]]
- [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear (G1003)]]
- [[30_CIPHER/03_Threat_Actors/G0091 - Silence|Silence (G0091)]]

## 10. Campaign Usage
ATT&CK does not enumerate campaigns directly on the T1125 technique page as of its last modification date (2025-10-24). (MITRE: T1125)

## 11. Malware Usage
ATT&CK-documented examples:
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]
- [[30_CIPHER/05_Malware/S0363 - Empire|Empire (S0363)]]
- [[30_CIPHER/05_Malware/S0234 - Bandook|Bandook (S0234)]]
- [[30_CIPHER/05_Malware/S0334 - DarkComet|DarkComet (S0334)]]
- [[30_CIPHER/05_Malware/S0591 - ConnectWise|ConnectWise (S0591)]]

## 12. Mitigations
ATT&CK notes this behavior is difficult to prevent with purely preventive controls because it abuses legitimate system features. (MITRE: T1125)
Compensating controls:
- **Permission hygiene**: reduce camera access entitlements to only approved apps; regularly audit camera permissions (especially on macOS via TCC).  
- **Application allowlisting**: block/alert on unapproved camera consumers and recording tools.  
- **Device access monitoring**: enable and retain camera stack/device access logs; enforce EDR policies for unusual device use.  
- **Network controls**: monitor/limit large outbound transfers from endpoints that don’t typically produce media artifacts.

## 13. Testing & Validation
Validation goals aligned to DET0197:
- Confirm you can observe (and alert on) the chain: **process start → device access → media file creation → outbound transfer**. (MITRE: DET0197)
- Platform-specific checks:
  - Windows: ensure Sysmon coverage for process/module/file/network events; validate visibility into Camera Frame Server operational events. (MITRE: DET0197 / AN0568)
  - Linux: ensure audit rules for `/dev/video*` and baseline legitimate callers. (MITRE: DET0197 / AN0569)
  - macOS: ensure TCC decision logging and ES telemetry where available. (MITRE: DET0197 / AN0570)
- Community test definitions (authorization required; lab only):
  - Atomic Red Team (T1125) technique test definitions: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1125/T1125.md

## 14. References
- MITRE ATT&CK. (n.d.). *Video Capture (T1125)*. https://attack.mitre.org/techniques/T1125/
- MITRE ATT&CK. (n.d.). *Behavior-chain, platform-aware detection strategy for T1125 Video Capture (DET0197)*. https://attack.mitre.org/detectionstrategies/DET0197/
- Wardle, P. (n.d.). *Objective-See (referenced by MITRE for macOS webcam-recording malware context)*. https://objective-see.com/
- Red Canary. (n.d.). *Atomic Red Team – T1125 Video Capture*. https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1125/T1125.md

## 15. Notes
- Treat unknown camera consumers as potentially high severity, especially on endpoints that do not normally use webcams.
- Keep an explicit allowlist for conferencing/recording apps to reduce noise, and alert on all other camera pipeline access.
