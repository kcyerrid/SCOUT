---
entity_type: mitre_technique

technique_id: "T1200"
subtechnique_id: ""
technique_name: "Hardware Additions"

tactic: ["Initial Access"]
platforms: ["windows", "linux", "macos", "network"]
datasources: ["USB Device Logs", "Endpoint Detection Logs", "System Configuration", "Physical Access Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1195", "T1059", "T1091"]

detection_priority: "Medium"
detection_maturity: ""
threat_score: 3

created: "2025-12-16"
updated: "2025-12-16"

contributors: []
tags: ["mitre", "technique"]

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Hardware Additions (T1200)

## 1. Summary
Hardware Additions describes adversary introduction of unauthorized hardware into a target environment to facilitate initial access. This includes devices such as malicious USB drives, rogue peripherals, network implants, or hardware keyloggers that enable code execution, credential capture, or covert access.

This technique typically requires physical access or insider assistance and is often associated with targeted or espionage-focused operations.

---

## 2. Technical Overview
Adversaries leverage hardware additions by:
- Inserting malicious USB devices that emulate keyboards or network adapters
- Deploying rogue peripherals that execute commands or drop payloads
- Introducing covert network devices to establish out-of-band access
- Using hardware to bypass endpoint security controls

Artifacts may include new device enumeration events, driver installations, unexpected network interfaces, or unexplained process execution following device insertion.

---

## 3. Subtechnique Considerations
T1200 does not currently define subtechniques. Variations depend on:
- Type of hardware introduced (USB, network, peripheral)
- Operating system device handling behavior
- Endpoint security posture and device control policies

Effectiveness is heavily influenced by physical security controls and device management enforcement.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Dropping malicious USB devices in public or office spaces
- Connecting rogue network devices to internal infrastructure
- Using HID-emulating devices to execute scripted commands
- Installing hardware keyloggers on target systems

Analysts may observe immediate command execution or network activity following device insertion.

---

## 5. Detection Guidance
Detection should focus on device and endpoint telemetry:
- New USB or peripheral device enumeration events
- Driver installation outside normal baselines
- Unexpected network interfaces or MAC addresses
- Endpoint behavior immediately following hardware insertion

Device control solutions significantly improve detection and prevention.

### Data Source Notes
- **USB Device Logs:** High value for identifying unauthorized device usage
- **Endpoint Logs:** Useful for correlating device insertion with execution
- **Physical Access Logs:** Important for attribution and investigation

---

## 6. Response Guidance
When Hardware Additions are suspected:
- Physically secure and remove unauthorized devices
- Isolate affected systems for analysis
- Review recent device connection history
- Assess for secondary payloads or persistence mechanisms

Preserve hardware and endpoint artifacts for forensic examination.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1195 - Supply Chain Compromise|T1195]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1091 - Replication Through Removable Media|T1091]]

---

## 8. SOC Relevance
Hardware-based initial access is less common than remote techniques but carries high impact and detection difficulty. SOC visibility is often limited without strong endpoint device controls and physical security integration.

---

## 9. Threat Actor Usage
This technique is primarily associated with:
- Nation-state espionage actors
- Insider threat scenarios
- Highly targeted intrusion campaigns

Confidence in usage is moderate due to required access constraints.

---

## 10. Campaign Usage
Hardware Additions have appeared in:
- Targeted espionage operations
- Insider-assisted intrusion campaigns
- Pre-positioning operations against high-value environments

---

## 11. Malware Usage
Malware delivered via hardware additions may include:
- Loaders dropped by malicious USB devices
- Scripts executed by HID-emulating peripherals
- Post-access frameworks such as:
  - [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]

---

## 12. Mitigations
Effective mitigations include:
- Enforcing USB and peripheral control policies
- Disabling autorun and HID emulation where possible
- Strong physical security and access controls
- Endpoint monitoring for device insertion events
- User awareness training regarding unknown devices

---

## 13. Testing & Validation
Validation approaches include:
- Controlled testing with authorized USB devices
- Purple team exercises simulating rogue peripheral insertion
- Review of device control alerting and response workflows

Successful validation results in rapid detection or prevention of unauthorized hardware usage.

---

## 14. References
MITRE ATT&CK. (2024). *Hardware Additions (T1200)*.  
https://attack.mitre.org/techniques/T1200/

CISA. (2022). *Securing USB and removable media*.  
https://www.cisa.gov/resources-tools/resources/securing-removable-media

Hak5. (2023). *Risks of malicious USB devices*.  
https://www.hak5.org/blogs/news/risks-of-malicious-usb-devices

---

## 15. Notes
- Physical security gaps often enable this technique
- Device control tooling dramatically reduces risk
- Insider threat considerations should be included in response planning

