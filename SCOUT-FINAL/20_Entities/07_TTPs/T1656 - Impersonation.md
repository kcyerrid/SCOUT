---
entity_type: mitre_technique

technique_id: "T1656"
subtechnique_id: ""
technique_name: "Impersonation"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Cloud
  - SaaS

datasources:
  - Authentication Logs
  - Identity Provider Logs
  - OS API Execution
  - Process Creation
  - Cloud Audit Logs
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
  - "T1134"
  - "T1078"
  - "T1098"
  - "T1550"

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
  - impersonation
  - identity
  - authentication
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Impersonation (T1656)

## 1. Summary
Impersonation describes adversaries **assuming the identity of another user, service, or account** in order to perform actions that bypass access controls and security monitoring. Rather than stealing credentials outright, attackers leverage impersonation mechanisms to act *as* a legitimate identity.

This technique allows attackers to:
- Bypass authorization checks
- Evade identity-based detections
- Access restricted resources
- Blend malicious activity with legitimate user behavior

---

## 2. Technical Overview
Impersonation occurs when an attacker leverages operating system, application, or cloud identity features that allow one identity to act on behalf of another.

Common mechanisms include:
- OS-level impersonation tokens
- Delegation and service account impersonation
- Cloud IAM role assumption
- API-based impersonation features
- Application-level identity delegation

Indicators include:
- Actions performed by unexpected identities
- Identity usage outside normal context
- Privileged operations without corresponding authentication events
- Identity changes without credential usage

---

## 3. Subtechnique Considerations
T1656 is a **standalone technique** that overlaps with, but is distinct from:
- Credential theft
- Account manipulation
- Token abuse

Impersonation often relies on **existing trust relationships** rather than stolen secrets.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Using OS impersonation APIs to execute actions as another user
- Leveraging cloud IAM impersonation or role assumption
- Abusing service account delegation
- Acting on behalf of privileged identities without direct login

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **identity context and behavior**:
- Monitor identity usage anomalies
- Detect privilege use without corresponding authentication
- Alert on role assumption or delegation events
- Correlate impersonation events with suspicious process activity

### Data Source Notes
- **Authentication logs**: Identify missing or unexpected logins
- **Identity provider logs**: Track impersonation and delegation
- **Cloud audit logs**: Detect role assumption and API impersonation
- **EDR telemetry**: Correlate identity changes with execution

Common false positives:
- Legitimate service-to-service impersonation
- Approved administrative delegation
- Automated workflows

Tuning guidance:
- Baseline normal impersonation patterns
- Require justification for cross-identity actions

---

## 6. Response Guidance
When suspected:
1. Identify the impersonated and impersonating identities
2. Review authorization paths and delegation settings
3. Revoke or restrict impersonation permissions
4. Investigate actions performed under the impersonated identity
5. Rotate credentials and review trust relationships

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1134 - Access Token Manipulation|T1134]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1078 - Valid Accounts|T1078]]
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1098 - Account Manipulation|T1098]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1550 - Use Alternate Authentication Material|T1550]]

---

## 8. SOC Relevance
T1656 is especially relevant in:
- Cloud and SaaS environments
- Identity-centric attack chains
- Incidents with minimal malware footprint

Impersonation often explains **how attackers act without stolen credentials**.

---

## 9. Threat Actor Usage
This technique is commonly used by:
- Cloud-focused APT groups
- Financially motivated attackers
- Advanced intrusion sets leveraging identity abuse

Its presence often indicates **deep understanding of identity systems**.

---

## 10. Campaign Usage
Observed in:
- Cloud account takeover campaigns
- SaaS data access operations
- Stealthy lateral movement activity

---

## 11. Malware Usage
Associated with:
- Post-exploitation frameworks
- Cloud automation tooling
- Custom implants abusing identity APIs

---

## 12. Mitigations
Recommended mitigations:
- Enforce least privilege for impersonation rights
- Monitor and audit delegation configurations
- Require MFA for sensitive role assumptions
- Restrict service account impersonation
- Implement identity behavior analytics

---

## 13. Testing & Validation
Validation approaches:
- Test impersonation detection in lab environments
- Validate alerts on role assumption events
- Review SOC workflows for identity misuse
- Ensure identity telemetry is retained and searchable

---

## 14. References
MITRE ATT&CK. (2025). *Impersonation (T1656)*.  
https://attack.mitre.org/techniques/T1656/

Microsoft. (2024). *Impersonation and delegation in Windows security*.  
https://learn.microsoft.com/windows/win32/secauthz/impersonation-levels

Google Cloud. (2024). *Service account impersonation*.  
https://cloud.google.com/iam/docs/impersonating-service-accounts

AWS. (2024). *IAM role assumption and delegation*.  
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html

---

## 15. Notes
- Impersonation enables powerful stealth without credential theft.
- Identity telemetry is critical for detection.
- Treat unexpected impersonation as high-confidence malicious behavior.
