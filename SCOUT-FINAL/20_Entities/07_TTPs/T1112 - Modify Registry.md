---
entity_type: ttp

ttp_id: "T1112"
ttp_name: "Modify Registry"
tactic: "Defense Evasion"
platforms:
  - "Windows"

description_short: "Adversaries modify the Windows Registry to hide configuration information, evade detection, or alter system behavior."

related_subtechniques: []

detection_difficulty: "Medium"
impact_severity: "Medium"

created: "2025-12-19"
updated: "2025-12-19"

tlp_classification: "TLP:CLEAR"
---

# T1112 – Modify Registry

## 1. Technique Overview
**Modify Registry (T1112)** is a **Defense Evasion** technique in **MITRE ATT&CK v18** where adversaries change **Windows Registry keys and values** to conceal malicious activity, disable security controls, or influence system and application behavior. Unlike registry-based persistence techniques, this technique focuses on **evasion and operational concealment**, though it is frequently used in support of persistence, privilege escalation, or credential access.

Registry modification is common across all stages of intrusion due to the registry’s central role in Windows configuration.

## 2. Adversary Objectives
Adversaries modify the registry to:
- Disable or weaken security controls and logging
- Hide artifacts, tools, or execution traces
- Alter system or application behavior to support operations
- Support other techniques such as persistence or execution flow hijacking

## 3. Common Abuse Patterns
- Disabling or modifying security product settings
- Altering logging or audit-related registry keys
- Modifying system policies to reduce visibility or enforcement
- Hiding malware configuration data in obscure registry locations
- Supporting follow-on techniques such as [[20_Entities/07_TTPs/T1547 - Boot or Logon Autostart Execution|T1547]] or [[20_Entities/07_TTPs/T1546 - Event Triggered Execution|T1546]]

## 4. Detection Considerations
Detection relies on **registry integrity and behavior monitoring**, including:
- Monitoring changes to security-sensitive registry keys
- Detecting registry modifications made by non-administrative or unexpected processes
- Correlating registry changes with suspicious process execution
- Baseline comparison of known-good registry configurations
- Alerting on registry changes associated with defensive control tampering

## 5. Defensive Mitigations
- Apply least-privilege access to registry modification rights
- Monitor and alert on changes to high-risk registry locations
- Use endpoint protection tools that track registry write activity
- Regularly audit registry settings related to security and logging
- Restore registry configurations as part of remediation efforts

## 6. Operational Impact
If successful, T1112 can:
- Reduce defender visibility into adversary activity
- Enable other techniques by disabling safeguards
- Prolong attacker dwell time through stealth
- Complicate forensic reconstruction of events

## 7. Analyst Notes
Registry modification is often a **supporting technique**, not the primary objective. Analysts should examine **why** a registry key was modified and **what behavior it enables or suppresses**, rather than treating registry writes as isolated events. Context and sequencing with other techniques is critical.

## 8. References
- MITRE ATT&CK. (n.d.). *Modify Registry (T1112).* https://attack.mitre.org/techniques/T1112/
- Microsoft. (n.d.). *Windows Registry Security*. https://learn.microsoft.com/windows/security/
- MITRE ATT&CK. (n.d.). *Defense Evasion Tactic (TA0005).* https://attack.mitre.org/tactics/TA0005/
- SANS Institute. (n.d.). *Windows Registry Forensics*. https://www.sans.org/
