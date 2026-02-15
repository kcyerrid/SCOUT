---
entity_type: mitre_technique

technique_id: "T1199"
subtechnique_id: ""
technique_name: "Trusted Relationship"

tactic: ["Initial Access"]
platforms: ["windows", "linux", "macos", "cloud", "saas", "network"]
datasources: ["Authentication Logs", "Network Traffic", "Federation Logs", "Application Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1078", "T1195", "T1133"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-16"
updated: "2025-12-16"

contributors: []
tags: ["mitre", "technique"]

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Trusted Relationship (T1199)

## 1. Summary
Trusted Relationship describes adversary abuse of existing trust relationships between organizations, systems, services, or networks to gain initial access. Rather than directly compromising the target environment, attackers exploit implicit trust in partners, vendors, managed service providers (MSPs), or federated identity relationships.

This technique enables stealthy access while bypassing many perimeter-based defenses.

---

## 2. Technical Overview
Adversaries compromise or impersonate a trusted entity and then leverage established connectivity or authentication pathways.

Common abuse patterns include:
- Compromising managed service providers or IT vendors
- Abusing federated identity or single sign-on (SSO) trust
- Leveraging VPN or network peering relationships
- Exploiting trusted application-to-application connections

Artifacts include legitimate authentication events, cross-tenant access, and network traffic from expected partner infrastructure.

---

## 3. Subtechnique Considerations
T1199 does not currently define subtechniques. Variations are driven by:
- Nature of the trust (identity, network, application)
- Scope and privilege of the trusted relationship
- Monitoring and logging maturity for third-party access

Risk increases significantly when trust is broad or poorly scoped.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Using compromised MSP credentials to access customer environments
- Abusing SAML or OAuth trust to access cloud tenants
- Leveraging VPN trust relationships for lateral access

Analysts may observe legitimate-looking access originating from partner networks.

---

## 5. Detection Guidance
Detection should focus on contextual and behavioral anomalies:
- Access from trusted partners outside normal patterns
- Privileged actions performed by third-party accounts
- Changes to trust configurations or federation settings
- Authentication events spanning multiple tenants or environments

Detection efficacy depends heavily on partner visibility and baselining.

### Data Source Notes
- **Authentication Logs:** Critical for identifying anomalous partner access
- **Federation Logs:** High value for detecting trust abuse
- **Network Traffic:** Useful for identifying unusual partner-originated activity

---

## 6. Response Guidance
When Trusted Relationship abuse is suspected:
- Immediately restrict or suspend the affected trust relationship
- Validate partner compromise and coordinate response
- Review scope of access and impacted assets
- Rotate credentials and review federation configurations

Preserve authentication, federation, and network logs for investigation.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1078 - Valid Accounts|T1078]]  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1195 - Supply Chain Compromise|T1195]]  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1133 - External Remote Services|T1133]]

---

## 8. SOC Relevance
Trusted Relationship abuse is increasingly common in large-scale intrusions, particularly those involving MSPs and cloud service providers. Detection maturity is often low due to limited visibility into partner environments.

---

## 9. Threat Actor Usage
This technique is frequently used by:
- Advanced persistent threat groups
- Ransomware operators targeting MSPs
- Nation-state actors seeking indirect access

Confidence in continued usage is high.

---

## 10. Campaign Usage
Trusted Relationship abuse appears in:
- MSP-targeted ransomware campaigns
- Cloud tenant compromise operations
- Strategic access campaigns leveraging partner ecosystems

---

## 11. Malware Usage
Malware is often secondary in trusted relationship abuse, but post-access tooling may include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]

---

## 12. Mitigations
Effective mitigations include:
- Minimizing scope of trusted relationships
- Continuous monitoring of third-party access
- Enforcing MFA for all partner access
- Regular trust relationship reviews and audits
- Segmentation of partner-accessible systems

---

## 13. Testing & Validation
Validation approaches include:
- Simulated compromise of partner accounts
- Purple team exercises involving federated identity abuse
- Review of trust relationship baselines

Successful validation identifies anomalous partner access promptly.

---

## 14. References
MITRE ATT&CK. (2024). *Trusted Relationship (T1199)*.  
https://attack.mitre.org/techniques/T1199/

CISA. (2023). *Securing trusted access relationships*.  
https://www.cisa.gov/resources-tools/resources/securing-trusted-access

Microsoft. (2023). *Managing and securing partner access*.  
https://learn.microsoft.com/en-us/security/zero-trust/partner-access

---

## 15. Notes
- Overly broad trust relationships significantly increase risk
- Partner security posture directly impacts organizational security
- Continuous trust review should be a governance priority

