---
entity_type: mitre_technique

technique_id: "T1056"
subtechnique_id: ""
technique_name: "Input Capture"

tactic:
  - Collection
  - Credential Access
platforms:
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
  - "[[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]"
  - "[[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]]"
  - "[[30_CIPHER/03_Threat_Actors/G1046 - Storm-1811|Storm-1811]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]]"
  - "[[30_CIPHER/05_Malware/S0381 - FlawedAmmyy|FlawedAmmyy]]"
  - "[[30_CIPHER/05_Malware/S1245 - InvisibleFerret|InvisibleFerret]]"
  - "[[30_CIPHER/05_Malware/S0641 - Kobalos|Kobalos]]"
  - "[[30_CIPHER/05_Malware/S1060 - Mafalda|Mafalda]]"
  - "[[30_CIPHER/05_Malware/S1059 - metaMain|metaMain]]"
  - "[[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]"
associated_campaigns:
  - "C0049 - Leviathan Australian Intrusions"
  - "C0039 - Versa Director Zero Day Exploitation"
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
Input Capture (T1056) involves adversaries collecting user input—such as keystrokes, mouse events, or other interaction artifacts—to gather credentials, MFA codes, or sensitive data. It is used for both **collection** and **credential access** objectives.

## 2. Technical Overview
Common implementation categories (high-level):
- **OS/API interception:** hooking or polling OS functions that expose input events.
- **Device-level capture:** reading from input device interfaces (platform-dependent).
- **Session interception:** capturing credentials/MFA artifacts during remote access or interactive workflows.
- **App-level capture:** capturing input within targeted applications (e.g., login prompts, SSH clients).

Defender-observable outcomes often include:
- Unusual processes interacting with input APIs/devices.
- Credential or MFA artifacts appearing in attacker-accessed locations shortly after capture activity.
- Abnormal access patterns to remote services following periods of suspected input capture.

## 3. Subtechnique Considerations
- Sub-techniques (not exhaustive) include specific approaches such as **Keylogging (T1056.001)** and other forms of GUI/API capture. If your detections are more specific, map to the relevant sub-technique for higher fidelity.

## 4. Procedure Examples
Representative MITRE-listed examples include:
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]] captured input as reported in associated activity.
- [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]] used input capture techniques in reported operations.
- [[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]] and [[30_CIPHER/05_Malware/S0381 - FlawedAmmyy|FlawedAmmyy]] have been reported capturing user input.
- [[30_CIPHER/05_Malware/S1245 - InvisibleFerret|InvisibleFerret]] collected mouse/keyboard events using a library referenced in reporting.
- [[30_CIPHER/05_Malware/S0641 - Kobalos|Kobalos]] captured connection details via a compromised SSH client.
- C0049 - Leviathan Australian Intrusions involved captured MFA codes and remote access artifacts.
- [[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]] captured input by redirecting Windows logon-related traffic (as described in reporting).
- [[30_CIPHER/03_Threat_Actors/G1046 - Storm-1811|Storm-1811]] used a script to capture credentials after prompting a user to authenticate.
- C0039 - Versa Director Zero Day Exploitation involved intercepted and harvested credentials from user logins to compromised devices.

## 5. Detection Guidance
MITRE detection guidance emphasizes **behavioral monitoring** across platforms, focusing on suspicious input API usage and device access.

**High-signal detection themes**
- **Windows**
  - Suspicious calls/usage patterns involving input-related APIs from non-UI or unexpected processes.
  - Unusual module loads or hooks in processes that do not typically handle user input.
- **Linux**
  - Non-privileged or unexpected processes opening or reading from input device interfaces (platform-specific) or using input event libraries.
- **macOS**
  - Unauthorized access patterns to input/event services (e.g., event taps) from unexpected executables; correlate with TCC/privacy prompts where applicable.
- **Network devices**
  - Indicators of tampering that enable capture of interactive console input or remote session keystrokes.

### Data Source Notes
- **EDR/process telemetry:** API-call telemetry (when available), module load events, injection/hook indicators, process ancestry.
- **OS auditing:** platform-native security logs (Windows Event Logs; Linux audit frameworks; macOS unified logs where applicable).
- **Remote access telemetry:** SSH/RDP/VPN logs; session metadata for timing correlation with suspicious input capture.
- **Network/security telemetry:** outbound connections to C2 immediately following likely capture windows.

## 6. Response Guidance
1. **Contain**
   - Isolate affected endpoints; restrict remote sessions; rotate exposed credentials/MFA factors as indicated.
2. **Eradicate**
   - Remove offending binaries/extensions; identify persistence; verify integrity of auth-related components.
3. **Credential hygiene**
   - Assume credential compromise; force resets; revoke sessions/tokens; review privileged accounts first.
4. **Hunt**
   - Pivot on input-capture indicators (hooking, device access, unusual module loads) across fleet.

## 7. Related ATT&CK Content
- Technique placement:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1056 - Input Capture|T1056]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1056 - Input Capture|T1056]]
- High-relevance sub-technique:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1056.001 - Keylogging|T1056.001]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1056.001 - Keylogging|T1056.001]]

## 8. SOC Relevance
- **Alerting value:** Often high when based on endpoint behavioral telemetry; noisy if relying on generic “keylogger” keywords.
- **Best correlation:** suspicious input API/device access → authentication events → lateral movement/exfiltration.
- **Common blind spots:** lack of API-call telemetry; limited logging on endpoints; missing baselines for UI vs non-UI process behavior.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]
- [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]]
- [[30_CIPHER/03_Threat_Actors/G1046 - Storm-1811|Storm-1811]]

## 10. Campaign Usage
- C0049 - Leviathan Australian Intrusions
- C0039 - Versa Director Zero Day Exploitation

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]]
- [[30_CIPHER/05_Malware/S0381 - FlawedAmmyy|FlawedAmmyy]]
- [[30_CIPHER/05_Malware/S1245 - InvisibleFerret|InvisibleFerret]]
- [[30_CIPHER/05_Malware/S0641 - Kobalos|Kobalos]]
- [[30_CIPHER/05_Malware/S1060 - Mafalda|Mafalda]]
- [[30_CIPHER/05_Malware/S1059 - metaMain|metaMain]]
- [[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]

## 12. Mitigations
- MITRE notes this technique is difficult to prevent with purely preventive controls because it can rely on legitimate system features.
- Compensating controls (defender best practice):
  - Reduce local admin exposure; enforce application control; monitor and restrict accessibility permissions (macOS) and kernel driver installation (Windows).
  - Harden remote access workflows; enforce phishing-resistant MFA where possible.

## 13. Testing & Validation
- Validate telemetry and detections in a lab by confirming:
  - You can detect suspicious input API usage/device access by non-UI processes.
  - Your EDR captures module loads/hooking indicators relevant to input capture behaviors.
- Prefer benign validation (log replay + known-good instrumentation) over deploying real keylogger tooling on production systems.

## 14. References
- MITRE ATT&CK. (n.d.). *Input Capture (T1056).* https://attack.mitre.org/techniques/T1056/
- Wazuh. (2023, December 28). *Detecting keyloggers (T1056.001) on Linux endpoints.* https://wazuh.com/blog/detecting-keyloggers-on-linux-endpoints/
- CISA, et al. (2024, July 8). *PRC MSS APT40 Tradecraft in Action.* https://www.cisa.gov/resources-tools/resources/peoples-republic-china-prc-ministry-state-security-apt40-tradecraft-action

## 15. Notes
- Detection Strategy (MITRE): **DET0102 – Behavioral Detection of Input Capture Across Platforms** (analytics AN0282–AN0285).
- Consider splitting detections by platform (Windows/Linux/macOS/Network Devices) to reduce false positives and improve triage speed.
