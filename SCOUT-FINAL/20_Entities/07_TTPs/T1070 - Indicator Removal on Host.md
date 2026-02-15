---
entity_type: mitre_technique

technique_id: "T1070"
subtechnique_id: ""
technique_name: "Indicator Removal on Host"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Cloud
  - Containers

datasources:
  - File System Monitoring
  - Windows Event Logs
  - Audit Logs
  - Process Creation
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
  - "T1562"
  - "T1564"
  - "T1027"
  - "T1074"

detection_priority:
  - High
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - defense-evasion
  - artifact-removal
  - anti-forensics
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Indicator Removal on Host (T1070)

## 1. Summary
Indicator Removal on Host describes adversaries **deleting, modifying, or otherwise removing forensic artifacts** on a compromised system to evade detection and hinder incident response. This technique directly targets evidence such as logs, files, and configuration data that could reveal attacker activity.

Attackers use this technique to:
- Obscure their presence and actions
- Prolong dwell time
- Complicate forensic reconstruction
- Reduce likelihood of detection and attribution

---

## 2. Technical Overview
Operating systems and applications generate numerous artifacts during normal operation. Adversaries remove or alter these artifacts by:

- Deleting or truncating log files
- Clearing Windows Event Logs
- Removing malware binaries or tools
- Deleting command history and temporary files
- Modifying timestamps or metadata

Typical indicators include:
- Missing or cleared logs
- File deletions following suspicious execution
- Gaps in audit trails
- Timestamp inconsistencies

---

## 3. Subtechnique Considerations
T1070 has multiple subtechniques that focus on specific artifact types (e.g., logs, files, command history). Analysts should evaluate subtechniques individually to understand detection and response nuances.

Indicator removal often follows **Impair Defenses (T1562)** and **Hide Artifacts (T1564)**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Clearing system and security logs
- Deleting malicious tools after execution
- Removing temporary files used during exploitation
- Truncating or overwriting log files

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **artifact integrity and continuity**:
- Alert on log clearing or truncation events
- Detect unexpected file deletions
- Monitor for gaps in telemetry
- Correlate artifact removal with suspicious activity

### Data Source Notes
- **File system monitoring**: Detect deletions and modifications
- **Event logs**: Identify clearing events
- **EDR telemetry**: Observe anti-forensic behavior

Common false positives:
- Legitimate log rotation
- System maintenance or cleanup tasks

Tuning guidance:
- Baseline normal artifact retention behavior
- Require change approval for cleanup activities

---

## 6. Response Guidance
When suspected:
1. Preserve remaining artifacts immediately
2. Identify scope and timing of artifact removal
3. Correlate with execution and network telemetry
4. Investigate for additional defense evasion techniques
5. Treat evidence destruction as a security incident

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1564 - Hide Artifacts|T1564]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1074 - Data Staged|T1074]]

---

## 8. SOC Relevance
T1070 is a **high-severity defense evasion technique** because it directly undermines detection and investigation. Evidence removal should always be treated as suspicious and escalated.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Ransomware operators
- Advanced persistent threats
- Financially motivated intruders

Its use often indicates **intentional, hands-on intrusion activity**.

---

## 10. Campaign Usage
Observed in:
- Ransomware deployment phases
- Espionage campaigns
- Long-dwell intrusions

---

## 11. Malware Usage
Associated with:
- Ransomware families
- Post-exploitation frameworks
- Custom implants designed to evade forensics

---

## 12. Mitigations
Recommended mitigations:
- Centralize and protect logs
- Enforce immutable log storage
- Monitor and alert on artifact deletion
- Restrict administrative privileges
- Implement robust backup and retention policies

---

## 13. Testing & Validation
Validation approaches:
- Simulate benign log clearing in lab environments
- Validate alerts on file deletion and log truncation
- Test SOC workflows for evidence loss scenarios
- Ensure telemetry gaps trigger investigation

---

## 14. References
MITRE ATT&CK. (2025). *Indicator Removal on Host (T1070)*.  
https://attack.mitre.org/techniques/T1070/

Microsoft. (2024). *Windows event log clearing and auditing*.  
https://learn.microsoft.com/windows/security/threat-protection/auditing/

Elastic Security Labs. (2023). *Detecting anti-forensic techniques*.  
https://www.elastic.co/security-labs

---

## 15. Notes
- Evidence destruction is a strong indicator of malicious intent.
- Treat telemetry gaps as potential compromise indicators.
- Defense-in-depth logging is critical to resilience.
