---
entity_type: ttp

ttp_id: "T1671"
ttp_name: "Cloud Application Integration"
tactic: "Persistence"
platforms:
  - "SaaS"
  - "Cloud"

description_short: "Adversaries leverage legitimate cloud application integrations to maintain persistent access by abusing OAuth consent, app provisioning, or API authorization workflows."

related_subtechniques: []

detection_difficulty: "Medium"
impact_severity: "High"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1671 – Cloud Application Integration

## 1. Technique Overview
**Cloud Application Integration (T1671)** is a technique in MITRE ATT&CK v18 where adversaries achieve **persistent access** by abusing **cloud application integration mechanisms**. These integrations often involve OAuth consent grants, service principal authorization, or API access arrangements that enable third-party applications to interact with enterprise cloud services. By tricking users or administrators into granting permissions to attacker-controlled apps, adversaries can maintain access and perform actions via trusted integrations even after credential resets. :contentReference[oaicite:0]{index=0}

This technique is particularly relevant in environments with SaaS platforms such as Office 365, Salesforce, Google Workspace, and other cloud ecosystems where integrations are common and user-approved app workflows exist. :contentReference[oaicite:1]{index=1}

## 2. Adversary Objectives
Adversaries use cloud application integration to:
- Maintain **long-term access** independent of compromised credentials
- Evade credential-based remediation
- Operate through **trusted application sessions**
- Enable unauthorized API calls and data access
- Support subsequent collection, exfiltration, or account manipulation

## 3. Common Abuse Patterns
- Trick users or administrators into granting OAuth consent to attacker-controlled applications
- Register malicious apps as authorized integrations in cloud identity and access systems
- Exploit overly broad OAuth scopes or weak policy controls
- Abuse service principals or delegated app permissions for automated access
- Use integration tokens for persistent API access

## 4. Detection Considerations
Detection relies on **cloud identity and application telemetry**:
- Monitoring for new or modified OAuth app registrations
- Alerting on application consent grants with high-privilege scopes
- Correlation of integration authorizations with anomalous API activity
- Reviewing cloud audit logs for unexpected app token issuance
- Baseline analysis of approved integrations vs recent changes

## 5. Defensive Mitigations
- Enforce least privilege for application permissions
- Harden OAuth consent policies (e.g., admin-only consent)
- Review and approve third-party app integrations centrally
- Use conditional access policies to restrict app access
- Regularly audit authorized integrations and token lifetimes

## 6. Operational Impact
If exploited, T1671 can:
- Provide persistent access even after credential revocation
- Enable attackers to act as trusted applications
- Bypass traditional identity protection controls
- Complicate incident response due to legitimate app context

## 7. Analyst Notes
Cloud application integration abuse is increasingly observed in modern attacks, particularly those targeting SaaS environments where user-approved apps are ubiquitous. This technique is distinct from traditional persistence because it leverages **legitimate integration frameworks** rather than installed malware or configured startup artifacts. :contentReference[oaicite:2]{index=2}

## 8. References
- MITRE ATT&CK. (n.d.). *Cloud Application Integration (T1671)*. https://attack.mitre.org/techniques/T1671/  
- MITRE ATT&CK Detection Strategy. (2025). *Cloud Application Integration*. https://attack.mitre.org/detectionstrategies/DET0539/  
- Community resource: Overview of cloud integration persistence mechanisms. https://attack.mitre.org/techniques/T1671/ :contentReference[oaicite:3]{index=3}
