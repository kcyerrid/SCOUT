---
entity_type: mitre_technique

technique_id: "T1014"
subtechnique_id: ""
technique_name: "Rootkit"

tactic:
  - Defense Evasion
  - Persistence
  - Privilege Escalation

platforms:
  - Windows
  - Linux
  - macOS

datasources:
  - Kernel Drivers
  - API Monitoring
  - Memory Analysis
  - Process Monitoring
  - EDR Telemetry

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1055"
  - "T1620"
  - "T1542"
  - "T1562"

detection_priority:
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - defense-evasion
  - persistence
  - privilege-escalation
  - rootkit
  - kernel
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Rootkit (T1014)

## 1. Summary
Rootkit describes adversaries **hiding malicious code and activity by modifying operating system components**, often at the kernel or low-level system layer. Rootkits are designed to evade detection by security tools, conceal attacker presence, and provide long-term privileged access.

Adversaries use rootkits to:
- Conceal files, processes, registry keys, or network connections
- Maintain persistent and privileged access
- Bypass security monitoring and forensics
- Support stealthy long-term intrusions

---

## 2. Technical Overview
Rootkits operate by altering or intercepting core system functionality. Common implementation methods include:
- Kernel-mode drivers that hook system calls
- User-mode rootkits that modify APIs or libraries
- Bootkits and firmware-level rootkits
- Memory-resident rootkits that avoid disk artifacts

Common techniques used by rootkits:
- API hooking and inline patching
- Direct Kernel Object Manipulation (DKOM)
- Driver replacement or malicious driver loading
- Manipulation of system structures to hide artifacts

Indicators include:
- Inconsistencies between user-mode and kernel-mode views
- Hidden processes or files
- Unexpected kernel drivers or modules
- Disabled or impaired security tooling

---

## 3. Subtechnique Considerations
Key considerations for T1014:
- Often paired with **Process Injection (T1055)** and **Reflective Code Loading (T1620)**
- Kernel-level rootkits are harder to detect and remediate
- Bootkits and firmware rootkits provide deeper persistence
- Detection often requires memory and kernel telemetry

Rootkits represent **stealth-focused persistence and evasion**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Loading a malicious kernel driver to hide processes
- Hooking system APIs to filter out attacker artifacts
- Modifying kernel structures to conceal network connections
- Installing rootkits to protect other malware components

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **integrity, memory, and behavioral analysis**:
- Monitor kernel driver loading and modifications
- Detect discrepancies between API outputs and raw system data
- Analyze memory for hidden modules or hooks
- Identify security tool impairment

### Data Source Notes
- **Kernel telemetry**: Detect unauthorized drivers and hooks
- **Memory analysis**: Identify hidden code and altered structures
- **EDR telemetry**: Observe abnormal low-level behaviors

Common false positives:
- Legitimate security software using kernel drivers
- Virtualization or monitoring tools

Tuning guidance:
- Baseline known-good drivers and kernel modules
- Correlate rootkit indicators with other malicious activity

---

## 6. Response Guidance
When suspected:
1. Isolate the affected system immediately
2. Capture memory images for forensic analysis
3. Identify and remove malicious drivers or hooks
4. Rebuild the system from trusted media if necessary
5. Hunt for rootkit artifacts across the environment

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1055 - Process Injection|T1055]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1620 - Reflective Code Loading|T1620]]
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1542 - Pre-OS Boot|T1542]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]

---

## 8. SOC Relevance
T1014 is critical because:
- Rootkits undermine trust in system telemetry
- Detection often requires advanced tools and expertise
- Remediation may require full system rebuilds

SOC teams must treat **rootkit detection as a high-severity incident**.

---

## 9. Threat Actor Usage
Commonly used by:
- Nation-state threat actors
- Advanced persistent threats
- Long-dwell intrusion operators

---

## 10. Campaign Usage
Observed in:
- Espionage-focused campaigns
- Stealth persistence operations
- Long-term covert access intrusions

---

## 11. Malware Usage
Associated with:
- Kernel-mode rootkits
- Bootkits and firmware rootkits
- Stealth backdoors

---

## 12. Mitigations
Recommended mitigations:
- Enforce driver signing and Secure Boot
- Restrict kernel driver installation
- Use EDR with kernel visibility
- Monitor system integrity continuously

---

## 13. Testing & Validation
Validation approaches:
- Test detection of unauthorized driver loading
- Validate memory analysis workflows
- Conduct tabletop exercises for rootkit response
- Ensure rebuild procedures are documented and practiced

Include:
- Preconditions: kernel telemetry enabled
- Required roles/tools: SOC, DFIR, EDR platform
- Expected outcomes: detection of rootkit behavior
- Success criteria: confirmed removal and restored trust

---

## 14. References
MITRE ATT&CK. (2025). *Rootkit (T1014)*.  
https://attack.mitre.org/techniques/T1014/

Microsoft. (2024). *Kernel-mode rootkit detection*.  
https://learn.microsoft.com/security/

ESET Research. (2024). *Modern rootkits and stealth malware*.  
https://www.welivesecurity.com/

---

## 15. Notes
- Rootkits compromise system trust at its core.
- Memory and kernel visibility are mandatory.
- Reimaging may be required to restore confidence.
