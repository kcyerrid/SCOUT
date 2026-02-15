---
entity_type: mitre_technique

technique_id: "T1113"
subtechnique_id: ""
technique_name: "Screen Capture"

tactic:
  - "TA0009 - Collection"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "Process Creation (DC0032)"
  - "Module Load (DC0016)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "G0007 - APT28"
  - "G0087 - APT39"
  - "G1044 - APT42"
associated_malware:
  - "S0331 - Agent Tesla"
  - "S0622 - AppleSeed"
  - "S1087 - AsyncRAT"
  - "S0154 - Cobalt Strike"
associated_campaigns: []
related_techniques:
  - "T1125"

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
  - screen-capture

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Adversaries may capture screenshots of the desktop to collect sensitive on-screen information (documents, credentials, chats, internal tools) during post-compromise operations. Screen capture can be performed via native utilities or programmatic API calls and is frequently built into RATs. (MITRE: T1113)  

## 2. Technical Overview
Common defender-relevant patterns include:
- **Native utilities / commands**: OS-provided screenshot tools invoked interactively or via automation (e.g., macOS `screencapture`, X11 capture tooling on Linux).  
- **API-driven capture**: Use of screen capture APIs to grab the framebuffer/window surfaces (e.g., .NET `Graphics.CopyFromScreen` on Windows).  
- **Artifact creation**: Image files written to disk (often `.png`, `.bmp`, `.jpg`) in **unusual paths** (temp, hidden directories, application data) or at **regular intervals**.  
- **RAT feature usage**: Remote operators initiating captures through existing access tooling; may correlate with remote session activity and follow-on **exfiltration**.

## 3. Subtechnique Considerations
No sub-techniques are defined for T1113.  
Operationally, distinguish **screen** capture (T1113) from **camera/webcam** capture (T1125), which tends to involve device access, camera frameworks, and different telemetry requirements.

## 4. Procedure Examples
ATT&CK documents broad usage across threat actors and malware. Examples include:
- Threat Actors:
  - [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]] — used tools to take screenshots from victims. (MITRE: T1113 Procedure Examples)
  - [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39 (G0087)]] — used a screen capture utility on compromised hosts. (MITRE: T1113 Procedure Examples)
  - [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42 (G1044)]] — used malware to take screenshots. (MITRE: T1113 Procedure Examples)
- Malware / Tooling:
  - [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]] — captures desktop screenshots. (MITRE: T1113 Procedure Examples)
  - [[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed (S0622)]] — takes screenshots via API calls. (MITRE: T1113 Procedure Examples)
  - [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]] — Beacon capability includes screenshot capture. (MITRE: T1113 Procedure Examples)

## 5. Detection Guidance
Primary detection opportunities are **process lineage**, **command/tooling usage**, and (where available) **API-level telemetry**.

High-signal analytics (MITRE detection strategy guidance):
1. **Unusual screen-capture API usage / tooling**  
   - Detect atypical processes invoking screen capture behavior (e.g., scripting hosts, office children, remote agents) and/or writing image artifacts. (MITRE: DET0346 / AN0980)
2. **macOS suspicious `screencapture` usage**  
   - Flag `screencapture` executions with suspicious parents, odd execution context, or silent/automated behavior patterns. (MITRE: DET0346 / AN0981)
3. **Linux X11 screenshot tooling**  
   - Alert on `xwd` / `import` invocation, especially when launched from non-interactive contexts or remote shells. (MITRE: DET0346 / AN0982)

Recommended correlation/enrichment:
- **Burst/interval behavior**: repeated screenshot creation at consistent intervals.
- **Suspicious parents**: `powershell`, `wscript/cscript`, remote management agents, unusual service parents.
- **Output path anomalies**: temp directories, hidden user profile locations, uncommon system paths.
- **Follow-on exfil**: network egress shortly after image creation (proxy logs/EDR net telemetry).

### Data Source Notes
Minimum telemetry to support robust detections (per MITRE DET0346 log sources):
- **Process Creation (DC0032)**  
  - Windows: Sysmon Event ID 1  
  - macOS: unified log / exec events  
  - Linux: auditd `execve` (MITRE: DET0346)
- **Module Load (DC0016)** (Windows)  
  - Sysmon Event ID 7 to catch suspicious modules associated with capture workflows in unusual processes. (MITRE: DET0346)

## 6. Response Guidance
Triage and containment steps (defender-focused):
1. **Scope the capture**: identify process responsible, parents/children, user context, session type (interactive vs service/remote).  
2. **Collect key evidence**: command line, hashes, loaded modules, persistence checks, and any created image artifacts (paths, timestamps, frequency).  
3. **Assess exposure**: determine what applications/windows were likely visible; check for simultaneous credential prompts, admin consoles, or sensitive documents.  
4. **Hunt follow-on**: correlate screenshot creation timestamps with outbound connections, archive/staging activity, or known exfil channels.  
5. **Contain**: isolate host if active operator-driven capture is suspected; revoke tokens/rotate creds if sensitive material likely exposed.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1113 - Screen Capture|T1113]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1125 - Video Capture|T1125]]

## 8. SOC Relevance
- **Why it matters**: direct path to capturing privileged workflows, MFA prompts, internal dashboards, and sensitive documents without needing file access.  
- **Alert quality**: moderate-to-high when tied to suspicious parents, unusual paths, or periodic capture; lower when attributable to user-driven screenshot tools.  
- **Common false positives**: helpdesk tools, QA/testing, accessibility tools, screen sharing/collaboration features—baseline allowlists carefully.

## 9. Threat Actor Usage
ATT&CK-documented examples:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39 (G0087)]]
- [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42 (G1044)]]

## 10. Campaign Usage
ATT&CK does not enumerate campaigns directly on the T1113 technique page as of its last modification date (2025-10-24). (MITRE: T1113)

## 11. Malware Usage
ATT&CK-documented examples:
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla (S0331)]]
- [[30_CIPHER/05_Malware/S0622 - AppleSeed|AppleSeed (S0622)]]
- [[30_CIPHER/05_Malware/S1087 - AsyncRAT|AsyncRAT (S1087)]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]

## 12. Mitigations
ATT&CK notes this behavior is difficult to prevent with purely preventive controls because it abuses legitimate system features. (MITRE: T1113)
Compensating controls and hardening ideas:
- **Reduce post-compromise access**: limit remote admin tooling exposure; enforce least privilege and session isolation.
- **Application control**: restrict unapproved screenshot utilities and scripting hosts where feasible.
- **EDR/MDM policy**: alert on automated/hidden screenshot collection patterns; enforce tightened controls on remote management agents.
- **Data protection**: prefer passwordless/MFA flows that reduce on-screen secrets; use privileged access workstations for sensitive operations.

## 13. Testing & Validation
Purple-team validation suggestions:
- Execute controlled screen-capture simulations and confirm:
  - Process creation telemetry captures the expected parent/child lineage.
  - Any API/tool execution is observable in EDR.
  - Image artifact writes (name/path/interval) can be detected and correlated.
- Use community technique test definitions where appropriate (ensure authorization and safe lab execution):
  - Atomic Red Team (T1113) technique test definitions: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.md

## 14. References
- MITRE ATT&CK. (n.d.). *Screen Capture (T1113)*. https://attack.mitre.org/techniques/T1113/
- MITRE ATT&CK. (n.d.). *Detect Screen Capture via Commands and API Calls (DET0346)*. https://attack.mitre.org/detectionstrategies/DET0346/
- Microsoft. (n.d.). *Graphics.CopyFromScreen Method*. https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen
- Red Canary. (n.d.). *Atomic Red Team – T1113 Screen Capture*. https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.md

## 15. Notes
- Consider maintaining environment-specific allowlists for legitimate capture tools (support, conferencing, QA) and alert on **non-whitelisted** callers.
- For high-value endpoints, treat periodic screenshot capture from non-user contexts as a **priority hunt**.
