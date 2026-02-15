---
entity_type: mitre_technique

technique_id: "T1123"
subtechnique_id: ""
technique_name: "Audio Capture"

tactic:
  - "TA0009 - Collection"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "Process Access (DC0035)"
  - "File Creation (DC0039)"
  - "Process Creation (DC0032)"
  - "File Access (DC0055)"
  - "OS API Execution (DC0021)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0234 - Bandook|Bandook]]"
  - "[[30_CIPHER/05_Malware/S0334 - DarkComet|DarkComet]]"
  - "[[30_CIPHER/05_Malware/S0467 - TajMahal|TajMahal]]"
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
Adversaries may capture audio by accessing microphones or voice/video-call applications to listen to sensitive conversations. This often involves calling OS or application APIs, potentially writing audio files to disk for later exfiltration. Detection is primarily behavioral and dependent on strong endpoint telemetry and allowlisting of legitimate audio-capable applications.

## 2. Technical Overview
**What it is:** Unauthorized access to audio input devices (microphones) or audio streams through OS frameworks, device files, or application APIs.

**Typical observable behaviors:**
- Processes interacting with microphone/audio APIs or device interfaces.
- Creation of audio files (e.g., WAV/MP3/AIFF) in unusual paths (caches, temp directories).
- Use of system audio capture binaries or libraries (platform-dependent) by unexpected parent processes.
- Repeated/periodic audio capture activity aligned with user presence or scheduled tasks.

**Constraints/nuance:** Many legitimate apps access microphones (Teams/Zoom/browsers). The detection problem is distinguishing sanctioned access from suspicious access (rare process, rare parent, suspicious file outputs, odd timing, stealthy persistence).

## 3. Subtechnique Considerations
Audio Capture (T1123) has no subtechniques. When building coverage, segment by platform:
- Windows: API usage + process access behaviors + file writes
- Linux: device file access (e.g., `/dev/snd/*`) + known capture binaries
- macOS: TCC microphone access events + CoreAudio/AVFoundation activity + output file creation

## 4. Procedure Examples
ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]] using an audio capture utility (SOUNDWAVE) to capture microphone input.
- Multiple malware families with audio recording capability, including:
  - [[30_CIPHER/05_Malware/S0234 - Bandook|Bandook]]
  - [[30_CIPHER/05_Malware/S0334 - DarkComet|DarkComet]]
  - [[30_CIPHER/05_Malware/S0467 - TajMahal|TajMahal]]

## 5. Detection Guidance
**MITRE Detection Strategy (DET0221) highlights:**
- Detect **unusual or unauthorized** processes accessing microphone APIs followed by audio file writes.
- On Linux, detect processes accessing ALSA/PulseAudio device paths or executing capture binaries followed by file creation.
- On macOS, detect AVFoundation/CoreAudio activity, especially via TCC microphone access events, followed by audio file writes to suspicious directories.

**Practical detection approach:**
- Start with an allowlist of approved microphone-capable applications per environment.
- Alert on microphone access by rare/unsigned/low-prevalence processes or unusual parents.
- Correlate microphone access with file creation of audio formats in temp/cache directories.
- Add timing anomalies (microphone access outside business hours by non-collaboration apps).

### 5.1 Data Source Notes
Primary data components from DET0221:
- **Process Access (DC0035)**: Windows Sysmon Event 10 (process interactions consistent with microphone API usage as instrumented by EDR/Sysmon context)
- **Process Creation (DC0032)**: Windows 4688 / Linux Sysmon / macOS process exec telemetry
- **File Creation (DC0039)**: Audio file drops (WAV/MP3/AIFF) in suspicious directories
- **File Access (DC0055)**: Linux auditd open/write against audio device paths
- **OS API Execution (DC0021)**: macOS unified logs for audio API usage; **Apple TCC logs** for microphone access events (per DET0221)

## 6. Response Guidance
1. **Validate legitimacy:** Confirm whether the process is an approved audio application and whether the user initiated audio capture.
2. **Collect evidence:** Capture process details (hash, signer, command line), parent process, and microphone access events.
3. **Preserve outputs:** Locate and preserve created audio files (hash, timestamps, paths); follow privacy/HR/legal procedures as required.
4. **Scope the intrusion:** Check persistence, lateral movement, and other collection techniques; hunt for similar microphone access events on other endpoints.
5. **Contain:** Isolate host and remove malicious persistence; rotate credentials if broader compromise is suspected.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1123 - Audio Capture|T1123]]

## 8. SOC Relevance
**Highest-value detections:**
- Microphone access by non-standard processes (rare binary, unsigned, unexpected parent).
- Microphone access + audio file writes to cache/temp directories.
- Repeated microphone access patterns aligned with stealth (short captures, periodic execution, background services).

**Operational cautions:**
- This technique is privacy-sensitive; ensure response procedures align with policy and legal requirements.
- False positives are common without a well-maintained allowlist.

## 9. Threat Actor Usage
ATT&CK example:
- [[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]]

## 10. Campaign Usage
No specific campaigns are enumerated on the ATT&CK T1123 page.

## 11. Malware Usage
Selected ATT&CK examples include:
- [[30_CIPHER/05_Malware/S0234 - Bandook|Bandook]]
- [[30_CIPHER/05_Malware/S0334 - DarkComet|DarkComet]]
- [[30_CIPHER/05_Malware/S0467 - TajMahal|TajMahal]]

## 12. Mitigations
ATT&CK notes this technique is difficult to mitigate preventively because it abuses common system features. Emphasize:
- Application allowlisting / enterprise controls for microphone access (where available)
- Endpoint hardening and least privilege
- Strong endpoint telemetry and continuous monitoring

## 13. Testing & Validation
- Validate DET0221-style detections using controlled, authorized tests:
  - Confirm visibility into microphone access events (platform-specific)
  - Confirm correlation with audio file creation in suspicious paths
  - Validate allowlist-based suppression to manage noise
- Use Atomic Red Team coverage for T1123 to exercise detection and response workflows.

## 14. References
- MITRE ATT&CK. (2025, October 24). *Audio Capture (T1123).* https://attack.mitre.org/techniques/T1123/
- MITRE ATT&CK. (2025, October 21). *Behavioral Detection Strategy for T1123 Audio Capture Across Windows, Linux, macOS (DET0221).* https://attack.mitre.org/detectionstrategies/DET0221/
- Red Canary. (n.d.). *Atomic Red Team: T1123 – Audio Capture.* https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.md

## 15. Notes
- Prioritize detections that combine **microphone access + anomalous process context + suspicious file output**.
- If TCC (macOS) or equivalent permission telemetry is available, treat unexpected microphone grants/access as high-signal pivots.
