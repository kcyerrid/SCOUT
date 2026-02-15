---
entity_type: mitre_technique

technique_id: "T1542"
subtechnique_id: ""
technique_name: "Pre-OS Boot"

tactic:
  - Persistence
  - Privilege Escalation
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Network

datasources:
  - Firmware Integrity Monitoring
  - Boot Logs
  - Disk Forensics
  - EDR Telemetry
  - Hardware Security Telemetry

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1542.001"
  - "T1542.003"
  - "T1068"
  - "T1556"

detection_priority:
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - persistence
  - privilege-escalation
  - defense-evasion
  - firmware
  - bootkit
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Pre-OS Boot (T1542)

## 1. Summary
Pre-OS Boot describes adversaries **modifying firmware, bootloaders, or other components that execute before the operating system loads**. By compromising this phase, attackers gain highly persistent and stealthy control that survives OS reinstallation and evades many endpoint security controls.

Adversaries use this technique to:
- Establish stealthy, long-term persistence
- Execute malicious code before OS defenses initialize
- Bypass disk-based and OS-level security controls
- Maintain privileged access across system rebuilds

---

## 2. Technical Overview
Pre-OS boot components include:
- BIOS / UEFI firmware
- Bootloaders (e.g., GRUB, Windows Boot Manager)
- Option ROMs and device firmware
- Secure Boot configuration data

Adversaries may:
- Implant bootkits or firmware rootkits
- Modify bootloader code or configuration
- Disable or bypass Secure Boot
- Abuse firmware update mechanisms

Indicators include:
- Unexpected firmware changes
- Altered bootloader binaries or configurations
- Boot-time anomalies or integrity failures
- Persistence that survives OS reinstallation

---

## 3. Subtechnique Considerations
Key considerations for T1542:
- Extremely high-impact but technically complex
- Often requires elevated privileges or physical access
- Detection and remediation are challenging
- Compromise may remain hidden for extended periods

Pre-OS persistence operates **outside traditional OS trust boundaries**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Installing a malicious UEFI driver
- Modifying bootloader configuration to load malicious code
- Replacing firmware modules with trojanized versions
- Disabling Secure Boot to allow unsigned components

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **integrity and hardware-level monitoring**:
- Verify firmware and bootloader integrity
- Monitor Secure Boot state changes
- Detect boot-time anomalies
- Correlate persistence despite OS rebuilds

### Data Source Notes
- **Firmware monitoring**: Identify unauthorized modifications
- **Boot logs**: Detect abnormal execution paths
- **Disk forensics**: Reveal altered boot sectors or loaders

Common false positives:
- Legitimate firmware updates
- Hardware replacements or repairs

Tuning guidance:
- Baseline firmware versions and hashes
- Alert on unauthorized or unexpected changes

---

## 6. Response Guidance
When suspected:
1. Isolate affected system immediately
2. Perform firmware integrity verification
3. Reflash firmware using trusted images
4. Reinstall OS after firmware remediation
5. Assess supply-chain or physical access risks

---

## 7. Related ATT&CK Content
- Subtechniques:
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1542.001 - System Firmware|T1542.001]]
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1542.003 - Bootkit|T1542.003]]

- Related techniques:
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1068 - Exploitation for Privilege Escalation|T1068]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1556 - Modify Authentication Process|T1556]]

---

## 8. SOC Relevance
T1542 is critical because:
- Persistence occurs below OS visibility
- Standard endpoint tools may be blind
- Remediation is costly and disruptive

SOC teams must treat **pre-OS compromise as a high-severity incident**.

---

## 9. Threat Actor Usage
Commonly used by:
- Nation-state threat actors
- Highly advanced intrusion groups
- Supply-chain compromise operators

---

## 10. Campaign Usage
Observed in:
- Espionage-focused campaigns
- Long-term stealth intrusions
- Hardware and firmware targeting operations

---

## 11. Malware Usage
Associated with:
- Bootkits
- Firmware rootkits
- Advanced persistent implants

---

## 12. Mitigations
Recommended mitigations:
- Enable and enforce Secure Boot
- Restrict firmware update permissions
- Monitor firmware integrity
- Use hardware-backed security (TPM)

---

## 13. Testing & Validation
Validation approaches:
- Verify Secure Boot enforcement
- Test firmware integrity monitoring
- Conduct boot-time forensics exercises
- Validate response procedures for firmware incidents

---

## 14. References
MITRE ATT&CK. (2025). *Pre-OS Boot (T1542)*.  
https://attack.mitre.org/techniques/T1542/

ESET Research. (2024). *UEFI rootkits and bootkits*.  
https://www.welivesecurity.com/

Microsoft. (2024). *Securing the boot process*.  
https://learn.microsoft.com/security/

---

## 15. Notes
- Pre-OS compromise is rare but devastating.
- Firmware trust is foundational.
- Recovery requires hardware-level action.
