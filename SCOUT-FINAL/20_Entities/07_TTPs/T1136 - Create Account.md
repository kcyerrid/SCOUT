---
entity_type: ttp

ttp_id: "T1136"
ttp_name: "Create Account"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Cloud"
  - "Active Directory"

description_short: "Adversaries create new local, domain, or cloud accounts to establish persistent access or escalate privileges."

related_subtechniques:
  - "T1136.001"
  - "T1136.002"
  - "T1136.003"

detection_difficulty: "Medium"
impact_severity: "High"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1136 – Create Account

## 1. Technique Overview
**Create Account (T1136)** is a MITRE ATT&CK v18 technique in which adversaries **create new user, service, or cloud accounts** to gain or maintain persistent access. By introducing accounts that appear legitimate, attackers can evade remediation steps focused solely on credential resets or token revocation.

This technique applies across **on-premises systems, Active Directory, and cloud identity platforms**, and may support both persistence and privilege escalation depending on assigned roles and permissions.

## 2. Adversary Objectives
Adversaries create accounts to:
- Establish long-term persistence independent of stolen credentials
- Bypass account lockouts or password resets
- Blend malicious access into normal administrative activity
- Enable lateral movement and privilege escalation

## 3. Sub-Technique Summary
- **T1136.001 – Local Account**  
- **T1136.002 – Domain Account**  
- **T1136.003 – Cloud Account**

## 4. Common Abuse Patterns
- Creating local administrator accounts on endpoints or servers
- Adding newly created accounts to privileged groups
- Creating service accounts for scheduled tasks or services
- Registering cloud identities with elevated roles
- Using benign naming conventions to avoid suspicion

## 5. Detection Considerations
Detection relies on **identity, directory, and audit logging**, including:
- Monitoring account creation events across platforms
- Alerting on new accounts added to privileged groups
- Correlating account creation with anomalous authentication activity
- Reviewing cloud audit logs for new user or service principal creation
- Detecting accounts created outside approved provisioning workflows

## 6. Defensive Mitigations
- Enforce least privilege and approval workflows for account creation
- Enable comprehensive auditing for identity changes
- Monitor and alert on privileged account creation
- Regularly review and reconcile account inventories
- Disable or remove unauthorized accounts promptly

## 7. Operational Impact
If successful, T1136 can:
- Provide durable persistence resistant to credential remediation
- Enable stealthy administrative access
- Facilitate lateral movement and follow-on attacks
- Undermine trust in identity governance controls

## 8. Analyst Notes
Account creation is a deceptively simple but highly effective persistence technique. During incident response, analysts must enumerate **all recently created accounts**, including service and cloud identities, and verify their legitimacy. Failing to remove attacker-created accounts often results in rapid re-compromise.

## 9. References
- MITRE ATT&CK. (n.d.). *Create Account (T1136)*. https://attack.mitre.org/techniques/T1136/
- Microsoft. (n.d.). *Audit Account Management*. https://learn.microsoft.com/windows/security/threat-protection/auditing/audit-account-management
- MITRE ATT&CK. (n.d.). *Create Account Sub-techniques*. https://attack.mitre.org/techniques/T1136/
