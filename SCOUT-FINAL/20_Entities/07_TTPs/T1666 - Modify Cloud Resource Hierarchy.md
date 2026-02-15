---
entity_type: mitre_technique

technique_id: "T1666"
subtechnique_id: ""
technique_name: "Modify Cloud Resource Hierarchy"

tactic:
  - Defense Evasion
  - Persistence

platforms:
  - Cloud
  - SaaS

datasources:
  - Cloud Audit Logs
  - IAM Logs
  - Resource Management Logs
  - Policy and Organization Logs

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
  - "T1078"
  - "T1578"
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
  - cloud
  - persistence
  - defense-evasion
  - governance
  - iam
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Modify Cloud Resource Hierarchy (T1666)

## 1. Summary
Modify Cloud Resource Hierarchy describes adversaries **altering the organizational structure of cloud environments**—such as projects, subscriptions, accounts, folders, or organizational units—to gain persistence, evade monitoring, or expand control over resources.

Attackers use this technique to:
- Inherit broader permissions through hierarchy changes
- Evade security monitoring scoped to specific projects or accounts
- Establish long-term persistence at the governance layer
- Enable follow-on abuse of cloud resources

This technique targets **cloud governance and trust boundaries**, not individual workloads.

---

## 2. Technical Overview
Cloud providers organize resources hierarchically to manage permissions, billing, and policy enforcement. Adversaries abuse this by:

- Moving projects, subscriptions, or accounts into different parents
- Creating new folders or organizational units under attacker control
- Reassigning resources to inherit weaker policies
- Modifying organization-level policies or constraints
- Exploiting inherited IAM permissions at higher levels

Examples of hierarchical elements:
- AWS Organizations (accounts, OUs)
- Azure Management Groups and Subscriptions
- Google Cloud Organizations, Folders, and Projects

Indicators include:
- Resources moved between organizational containers
- Unexpected inheritance of elevated permissions
- Policy scope changes without approval
- Governance changes outside maintenance windows

---

## 3. Subtechnique Considerations
Key considerations for T1666:
- Often paired with **Account Manipulation (T1098)** and **Valid Accounts (T1078)**
- Enables stealthy, durable persistence
- May invalidate assumptions about access boundaries
- Can silently affect large numbers of resources

This technique operates **above the workload layer**, making it difficult to detect with endpoint tooling.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Moving a compromised project into an attacker-controlled folder
- Reorganizing subscriptions to inherit permissive policies
- Creating new organizational units for malicious resources
- Adjusting hierarchy to bypass security controls

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **governance and control-plane monitoring**:
- Monitor audit logs for hierarchy modification events
- Alert on resource moves between organizational units
- Detect changes to inheritance paths and policy scopes
- Correlate hierarchy changes with suspicious authentication

### Data Source Notes
- **Cloud audit logs**: Primary detection source
- **IAM logs**: Attribute changes to identities
- **Organization logs**: Detect hierarchy and policy modifications

Common false positives:
- Legitimate organizational restructuring
- Approved onboarding or offboarding activity

Tuning guidance:
- Require approvals for hierarchy changes
- Baseline normal organizational operations
- Increase severity when changes follow suspicious login events

---

## 6. Response Guidance
When suspected:
1. Identify all hierarchy changes and affected resources
2. Revert unauthorized organizational modifications
3. Review inherited permissions and policy impacts
4. Rotate credentials associated with the changes
5. Audit for follow-on activity enabled by hierarchy abuse

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1098 - Account Manipulation|T1098]]
  - [[20_Entities/07_TTPs/TA0001 - Initial Access/T1078 - Valid Accounts|T1078]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1578 - Modify Cloud Compute Infrastructure|T1578]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]

---

## 8. SOC Relevance
T1666 is highly relevant because:
- Governance-layer changes can affect entire environments
- Impact may be invisible to workload-focused monitoring
- Persistence can survive credential rotation and remediation

SOC teams must monitor **cloud hierarchy as a first-class security surface**.

---

## 9. Threat Actor Usage
Commonly used by:
- Cloud-focused intrusion groups
- Advanced persistent threats
- Adversaries abusing stolen cloud administrator credentials

---

## 10. Campaign Usage
Observed in:
- Cloud account takeover campaigns
- Long-dwell cloud intrusions
- Multi-project or multi-account compromises

---

## 11. Malware Usage
Associated with:
- Minimal or no malware
- Scripted control-plane abuse
- Legitimate cloud management tooling misuse

---

## 12. Mitigations
Recommended mitigations:
- Enforce least-privilege access at organization level
- Require multi-party approval for hierarchy changes
- Monitor and alert on organizational modifications
- Apply strong governance and policy controls

---

## 13. Testing & Validation
Validation approaches:
- Simulate benign hierarchy changes in test environments
- Validate alerts on resource movement and policy inheritance
- Test SOC workflows for governance-layer abuse
- Ensure rollback procedures for organizational changes

---

## 14. References
MITRE ATT&CK. (2025). *Modify Cloud Resource Hierarchy (T1666)*.  
https://attack.mitre.org/techniques/T1666/

AWS. (2024). *AWS Organizations security best practices*.  
https://docs.aws.amazon.com/organizations/

Microsoft. (2024). *Azure management group governance*.  
https://learn.microsoft.com/azure/

Google Cloud. (2024). *Organization and folder security*.  
https://cloud.google.com/resource-manager/

---

## 15. Notes
- Cloud hierarchy equals implicit trust.
- Governance abuse scales impact rapidly.
- Monitoring must extend beyond workloads.
