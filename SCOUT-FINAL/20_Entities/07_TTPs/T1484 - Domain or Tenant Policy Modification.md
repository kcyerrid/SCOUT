---
entity_type: mitre_technique

technique_id: "T1484"
subtechnique_id: ""
technique_name: "Domain Policy Modification"

tactic:
  - Defense Evasion
  - Privilege Escalation

platforms:
  - Windows

datasources:
  - Active Directory Logs
  - Group Policy Objects
  - Authentication Logs
  - Security Event Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1098"
  - "T1489"
  - "T1562"

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
  - privilege-escalation
  - active-directory
  - gpo
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Domain Policy Modification (T1484)

## 1. Summary
Domain Policy Modification describes adversaries **altering Active Directory domain-level policies** to weaken security controls, escalate privileges, or maintain persistence. By modifying Group Policy Objects (GPOs), attackers can affect **all systems or users** within the domain, making this technique highly impactful.

T1484 is commonly used to:
- Disable or weaken security controls
- Grant elevated privileges broadly
- Facilitate lateral movement and persistence
- Prepare the environment for ransomware deployment

---

## 2. Technical Overview
Active Directory enforces domain-wide behavior through Group Policy Objects stored in:
- SYSVOL
- Active Directory configuration containers

Adversaries abuse this mechanism by:
- Modifying existing GPOs
- Creating malicious GPOs and linking them to OUs
- Changing policies related to security settings, scripts, or software deployment
- Leveraging compromised domain admin credentials

Artifacts often include:
- Unexpected GPO changes
- SYSVOL file modifications
- Policy changes applied across multiple hosts
- Security settings reverting after remediation

---

## 3. Subtechnique Considerations
T1484 has subtechniques (e.g., **T1484.001 – Group Policy Modification**). Considerations include:
- Requires domain-level privileges
- High blast radius and rapid impact
- Difficult to detect without GPO auditing
- Often paired with defense evasion techniques

This technique is typically used late in attack chains.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Disabling endpoint security via GPO
- Deploying malicious startup scripts
- Weakening password or lockout policies
- Enabling insecure protocols across the domain

These actions often precede ransomware or destructive activity.

---

## 5. Detection Guidance
Detection strategies should focus on:
- Monitoring GPO creation and modification events
- Auditing changes to SYSVOL contents
- Detecting policy changes outside maintenance windows
- Correlating GPO changes with widespread host behavior changes

### Data Source Notes
- **AD logs**: Essential for tracking who modified policies
- **SYSVOL monitoring**: Critical for detecting file-level changes
- **Endpoint telemetry**: Useful for identifying policy effects

---

## 6. Response Guidance
When detected:
1. Identify the modified GPOs and scope of impact
2. Revert unauthorized policy changes immediately
3. Audit domain admin activity
4. Isolate affected systems if malicious scripts were deployed
5. Review AD security posture and privileged access

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1098 - Account Manipulation|T1098]]
  - [[20_Entities/07_TTPs/TA0040 - Impact/T1489 - Service Stop|T1489]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]

---

## 8. SOC Relevance
T1484 is especially relevant in:
- Enterprise Active Directory environments
- Ransomware-prone networks
- Organizations with limited GPO monitoring

Domain policy abuse can neutralize security controls at scale.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Ransomware operators
- Advanced persistent threats
- Intrusions focused on rapid enterprise-wide impact

Usage reflects high attacker maturity and intent.

---

## 10. Campaign Usage
Observed in:
- Ransomware domain takeover campaigns
- Post-exploitation enterprise intrusions
- Destructive or coercive operations

---

## 11. Malware Usage
Malware leveraging domain policy modification includes:
- Ransomware deployment frameworks
- Domain-wide loaders
- Post-exploitation toolkits

---

## 12. Mitigations
Recommended mitigations:
- Restrict and monitor domain admin privileges
- Enable detailed GPO auditing
- Monitor SYSVOL for unauthorized changes
- Use tiered administrative models
- Regularly review and baseline domain policies

---

## 13. Testing & Validation
Validation approaches:
- Simulate unauthorized GPO changes in lab domains
- Validate SOC alerts for policy modification
- Conduct red team exercises focused on domain takeover
- Review backup and restoration procedures for GPOs

---

## 14. References
MITRE ATT&CK. (2024). *Domain Policy Modification (T1484)*.  
https://attack.mitre.org/techniques/T1484/

Microsoft. (2023). *Group Policy security and auditing*.  
https://learn.microsoft.com/windows/security/threat-protection/security-policy-settings

SpecterOps. (2022). *Abusing Group Policy for lateral movement and persistence*.  
https://posts.specterops.io

---

## 15. Notes
- GPO abuse often precedes ransomware execution
- SYSVOL integrity monitoring is frequently overlooked
- Domain policy changes should be treated as high-severity events
