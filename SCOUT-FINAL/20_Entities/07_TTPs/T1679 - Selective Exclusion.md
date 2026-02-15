---
entity_type: mitre_technique

technique_id: "T1679"
subtechnique_id: ""
technique_name: "Selective Exclusion"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Cloud

datasources:
  - Security Software Logs
  - Configuration Management Logs
  - File Monitoring
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
  - "T1562"
  - "T1027"
  - "T1055"

detection_priority:
  - High
  - Critical

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - defense-evasion
  - evasion
  - exclusions
  - security-controls
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Selective Exclusion (T1679)

## 1. Summary
Selective Exclusion describes adversaries **strategically configuring security tools, policies, or monitoring controls to ignore specific files, directories, processes, accounts, or behaviors**, while leaving the broader security solution operational. This allows attackers to evade detection without triggering alarms associated with disabling security controls outright.

Adversaries use this technique to:
- Hide specific malicious artifacts from detection
- Maintain stealth while security tools appear functional
- Reduce alerting noise tied to attacker activity
- Support long-term persistence and lateral movement

---

## 2. Technical Overview
Modern security platforms allow administrators to define exclusions for performance, compatibility, or operational reasons. Adversaries abuse these mechanisms by:
- Adding malware file paths or hashes to exclusion lists
- Excluding attacker-controlled processes from scanning
- Creating account- or directory-based monitoring exceptions
- Leveraging cloud or SaaS policy exclusions to suppress logging

Common targets include:
- Endpoint protection exclusions (AV/EDR)
- File integrity monitoring allowlists
- SIEM or logging pipeline filters
- Cloud security posture management exclusions

Indicators include:
- Newly added exclusions without change approval
- Exclusions targeting suspicious paths or binaries
- Security tools running but failing to alert on known malicious activity
- Configuration changes shortly before or after intrusion stages

---

## 3. Subtechnique Considerations
Key considerations for T1679:
- Often follows initial privilege escalation
- Subtler than outright defense disablement
- Highly environment-specific
- Can persist unnoticed for extended periods

Selective exclusion is a **precision evasion technique**, optimized to avoid detection while minimizing operational impact.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Adding malware directories to endpoint exclusion lists
- Excluding specific service accounts from monitoring
- Suppressing logging for attacker-used cloud resources
- Filtering known malicious command patterns from detection rules

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **configuration drift and context-aware review**:
- Monitor changes to security exclusion policies
- Alert on exclusions added outside approved workflows
- Detect exclusions referencing unusual or high-risk paths
- Correlate exclusion creation with attacker activity timelines

### Data Source Notes
- **Security software logs**: Track exclusion creation and modification
- **Configuration management logs**: Identify unauthorized changes
- **EDR telemetry**: Detect execution in excluded contexts

Common false positives:
- Legitimate performance tuning
- Approved application compatibility changes

Tuning guidance:
- Require justification and approval metadata for exclusions
- Alert when exclusions intersect with high-risk behaviors

---

## 6. Response Guidance
When suspected:
1. Inventory and review all active exclusions
2. Remove unauthorized or suspicious exclusions
3. Scan previously excluded assets thoroughly
4. Investigate how exclusion privileges were obtained
5. Hunt for additional evasion techniques in use

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1055 - Process Injection|T1055]]

---

## 8. SOC Relevance
T1679 is critical because:
- Security tooling may appear healthy while blind
- Detection gaps are selective and harder to spot
- Impact scales with attacker dwell time

SOC teams must continuously audit **what security tools are not watching**.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threat actors
- Ransomware operators post-compromise
- Intrusions prioritizing stealth over disruption

---

## 10. Campaign Usage
Observed in:
- Long-dwell enterprise intrusions
- Cloud abuse campaigns
- Ransomware staging operations

---

## 11. Malware Usage
Associated with:
- Stealth backdoors
- Long-lived loaders
- Persistence frameworks requiring reduced visibility

---

## 12. Mitigations
Recommended mitigations:
- Enforce approval workflows for exclusions
- Log and alert on all exclusion changes
- Periodically audit exclusion lists
- Apply least-privilege to security configuration roles

---

## 13. Testing & Validation
Validation approaches:
- Attempt to create unauthorized exclusions in lab
- Validate alerting on exclusion changes
- Simulate malware execution in excluded paths
- Test SOC playbooks for selective evasion scenarios

Include:
- Preconditions: security configuration logging enabled
- Required roles/tools: SOC, endpoint engineering, SIEM
- Expected outcomes: detection of exclusion abuse
- Success criteria: rapid identification and rollback

---

## 14. References
MITRE ATT&CK. (2025). *Selective Exclusion (T1679)*.  
https://attack.mitre.org/techniques/T1679/

Microsoft. (2024). *Managing antivirus exclusions securely*.  
https://learn.microsoft.com/security/

CrowdStrike. (2024). *Abuse of security exclusions in intrusions*.  
https://www.crowdstrike.com/resources/

---

## 15. Notes
- Exclusions define blind spots.
- Blind spots are attacker-controlled attack surface.
- Continuous auditing is non-negotiable.
