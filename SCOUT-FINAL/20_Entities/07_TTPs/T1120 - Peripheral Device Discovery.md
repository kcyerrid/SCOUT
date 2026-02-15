---
entity_type: mitre_technique

technique_id: "T1120"
subtechnique_id: ""
technique_name: "Peripheral Device Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - Linux
  - Windows
  - macOS
datasources:
  - "DC0032 - Process Creation"
  - "DC0035 - Process Access"
  - "DC0055 - File Access"
  - "DC0054 - Drive Access"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1149 - CHIMNEYSWEEP|CHIMNEYSWEEP]]"
  - "[[30_CIPHER/05_Malware/S0149 - MoonWind|MoonWind]]"
associated_campaigns:
  - "C0012 - Operation CuckooBees"
  - "C0014 - Operation Wocao"
related_techniques:
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1083 - File and Directory Discovery|T1083]]"

detection_priority:
  - Medium

detection_maturity: "Developing"
threat_score: 2

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
Peripheral Device Discovery (T1120) covers adversary attempts to enumerate attached peripherals (USB storage, smart card readers, printers, cameras, Bluetooth devices, etc.). This discovery can support collection, exfiltration staging, evasion/anti-analysis checks, or ransomware targeting of external drives.

## 2. Technical Overview
Typical enumeration methods:
- **Windows**: WMI, PowerShell, and Windows APIs to list Plug and Play devices, USB controllers, removable media, printers, and smart card readers.
- **Linux**: command utilities and direct reads from `/sys`/`/proc` and udev interfaces to enumerate USB and hardware, sometimes paired with mount or file access behavior.
- **macOS**: utilities (e.g., hardware profiling and I/O registry queries) to enumerate USB devices and hardware components.

Defender-relevant observations:
- Enumeration often occurs **near other behaviors**: removable drive access, mounting, file collection, or environment checks.
- Can be used as an **anti-sandbox / anti-VM** signal (e.g., checking for mouse/camera/smartcard presence), so context matters.

## 3. Subtechnique Considerations
No sub-techniques for T1120.

## 4. Procedure Examples
Examples from ATT&CK procedure references include:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]] monitoring/receiving notifications when USB mass storage devices are inserted.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]] tooling checking USB flash drive characteristics and scanning for removable drives.
- [[30_CIPHER/05_Malware/S1149 - CHIMNEYSWEEP|CHIMNEYSWEEP]] monitoring for removable drives.
- **C0012 - Operation CuckooBees** using system utilities to list drives as part of reconnaissance.
- **C0014 - Operation Wocao** discovering removable disks attached to a system.

## 5. Detection Guidance
Primary detection strategy: identify **device enumeration tooling** and correlate with **device access/mount events** and suspicious follow-on activity.

Recommended analytics:
1. **Windows device enumeration**
   - Process creation for enumeration utilities/scripting hosts (PowerShell/WMI tooling) associated with peripheral discovery.
   - Correlate with device change events, removable media access, and post-enumeration file operations.
2. **Linux enumeration + /sys reads**
   - Audit process execution of common enumeration binaries and correlate with reads of `/sys`, `/proc`, or udev interfaces.
   - Look for tight temporal coupling with mounting, drive access, or file collection.
3. **macOS hardware profiling**
   - Process execution for hardware profiling/ioreg-style enumeration.
   - Correlate with subsequent clipboard/file/network actions when unusual for the initiating user/host.

Noise-reduction guidance:
- Baseline legitimate IT/asset inventory tools and allowlist known management hosts.
- Treat enumeration from **user workstations** followed quickly by drive access or staging behaviors as higher risk.

### 5.1 Data Source Notes
Prioritize:
- **DC0032 Process Creation**: enumeration utilities, shells, and scripts that query devices.
- **DC0035 Process Access**: lower-level API usage patterns (where captured) that indicate device interrogation.
- **DC0055 File Access**: reads of `/sys`/`/proc`/device metadata paths on Linux.
- **DC0054 Drive Access**: removable media access, mounting, and device interaction telemetry.

## 6. Response Guidance
1. Identify the initiator (user/process lineage) and confirm whether the behavior aligns with IT inventory or endpoint management.
2. Determine device interaction:
   - Was removable media inserted? Was it mounted? Were files accessed or copied?
3. Hunt for follow-on behaviors:
   - collection from removable drives, staging, suspicious compression, or external transfer.
4. Containment:
   - If suspicious, isolate the endpoint and preserve removable media-related logs/artifacts.
5. Scope:
   - Search for concurrent device enumeration across multiple endpoints or by the same account.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1083 - File and Directory Discovery|T1083]]

## 8. SOC Relevance
- Medium relevance alone; becomes high relevance when correlated with:
  - device insert/mount events,
  - large file reads from removable media,
  - encryption behavior or staging/exfil signals,
  - anti-analysis/environment-check patterns on initial execution.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]: USB-related peripheral discovery and monitoring.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]: USB/peripheral discovery to guide subsequent actions.

## 10. Campaign Usage
- **C0012 - Operation CuckooBees**: referenced drive discovery during advanced reconnaissance.
- **C0014 - Operation Wocao**: referenced discovery of removable disks attached to systems.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1149 - CHIMNEYSWEEP|CHIMNEYSWEEP]]: monitoring for removable drive insertion.
- [[30_CIPHER/05_Malware/S0149 - MoonWind|MoonWind]]: gathering removable drive information (as referenced in ATT&CK procedure examples).

## 12. Mitigations
This technique is generally **not easily mitigated** preventively because it can rely on legitimate system features.
Defender-focused controls:
- Restrict removable media usage where feasible; apply device control policies for USB storage.
- Monitor and alert on unusual device enumeration paired with suspicious file operations.

## 13. Testing & Validation
- Validate end-to-end visibility for:
  - enumeration process creation,
  - Linux file reads against `/sys`/`/proc`,
  - removable media insert/mount and drive access telemetry.
- Recommended test content:
  - Atomic Red Team T1120 test cases (where available) plus benign device inventory activities from IT tooling to tune allowlists.

## 14. References
- MITRE ATT&CK. (n.d.). *Peripheral Device Discovery (T1120)*. https://attack.mitre.org/techniques/T1120/
- MITRE ATT&CK. (n.d.). *Peripheral Device Enumeration via System Utilities and API Calls (DET0491)*. https://attack.mitre.org/detectionstrategies/DET0491/
- Atomic Red Team. (n.d.). *Atomic tests for T1120*. https://atomicredteam.io/atomic-red-team/atomics/T1120/
- Microsoft. (n.d.). *Windows event logging and auditing guidance*. https://learn.microsoft.com/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection

## 15. Notes
- Consider classifying “device discovery → device access → file staging” as a higher-confidence behavioral chain than device discovery alone.
