---
entity_type: ttp

ttp_id: "T1098"
ttp_name: "Account Manipulation"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Cloud"
  - "Network"

description_short: "Adversaries modify accounts to maintain persistence or escalate privileges."

related_subtechniques:
  - "T1098.001"
  - "T1098.002"
  - "T1098.003"
  - "T1098.004"

detection_difficulty: "Medium"
impact_severity: "High"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1098 – Account Manipulation

## 1. Technique Overview
**Account Manipulation (T1098)** is a MITRE ATT&CK technique used by adversaries to **maintain persistence, escalate privileges, or enable long-term access** by modifying existing accounts or their attributes. Rather than creating new accounts, attackers alter trusted identities to blend into normal administrative activity.

This technique is commonly observed after initial compromise and credential access.

## 2. Adversary Objectives
Adversaries use account manipulation to:
- Maintain **stealthy persistence**
- Escalate or retain **privileged access**
- Bypass security controls tied to identity
- Enable **lateral movement** and long-term operations

## 3. Sub-Techniques
- **T1098.001 – Additional Cloud Credentials**  
  Adding access keys, tokens, or API credentials to cloud identities.

- **T1098.002 – Account Privileges**  
  Modifying group memberships or role assignments to elevate permissions.

- **T1098.003 – Additional Cloud Roles**  
  Assigning new IAM roles to existing cloud accounts.

- **T1098.004 – SSH Authorized Keys**  
  Adding attacker-controlled SSH keys to existing user accounts.

## 4. Common Abuse Patterns
- Adding users to **Domain Admins** or equivalent privileged groups
- Modifying IAM roles in AWS, Azure, or GCP
- Injecting SSH keys into `authorized_keys`
- Changing account attributes to disable security controls
- Granting persistent API access in cloud environments

## 5. Detection Considerations
Detection typically relies on **identity and configuration monitoring**, including:
- Unexpected changes to group memberships
- New SSH keys added to existing accounts
- IAM role or permission changes outside approved workflows
- Account modifications occurring outside business hours
- Cloud audit logs showing credential or role changes

## 6. Defensive Mitigations
- Enforce **least privilege** and role-based access control
- Require **multi-factor authentication** for privileged accounts
- Monitor and alert on account and permission changes
- Implement **just-in-time (JIT)** access models
- Regularly audit local, domain, and cloud account configurations

## 7. Operational Impact
Successful account manipulation can:
- Provide **long-term, low-noise persistence**
- Undermine trust in identity-based security
- Enable follow-on attacks such as ransomware or espionage
- Complicate incident response and remediation

## 8. Analyst Notes
T1098 is particularly dangerous because it abuses **legitimate administrative mechanisms** rather than malware. Organizations with weak identity governance may never detect this technique, even during post-incident forensics. Cloud environments are especially susceptible without strong IAM visibility.

## 9. References
- MITRE ATT&CK. (n.d.). *Account Manipulation (T1098)*. https://attack.mitre.org/techniques/T1098/
- Microsoft. (2022). *Detecting identity-based persistence*. https://www.microsoft.com/security/blog/
- SANS Institute. (n.d.). *Identity abuse and persistence techniques*. https://www.sans.org/
