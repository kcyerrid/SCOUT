---
entity_type: mitre_technique

technique_id: "T1535"
subtechnique_id: ""
technique_name: "Unused/Unsupported Cloud Regions"

tactic:
  - Defense Evasion
platforms:
  - IaaS
datasources:
  - Instance Start
  - Cloud Storage Creation
  - User Account Metadata
  - Network Connection Creation

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - T1496

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 3

created: 2026-01-06
updated: 2026-01-06

contributors: []
tags:
  - mitre
  - technique

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Adversaries may provision cloud resources in geographic regions your organization does not normally use (or that lack parity in detection services) to reduce visibility and delay response. This is especially relevant after cloud account compromise and is commonly paired with resource abuse such as cryptomining.

## 2. Technical Overview
**Core idea:** operate “out of sight” by moving activity to regions that are not part of normal operational monitoring.

Common patterns:
- **New resource provisioning** (instances, storage, services) in **historically unused** regions.
- **Detection-control gaps**: regions where security services (or log forwarding) are not enabled or have reduced coverage.
- **Follow-on activity** from the new region: outbound traffic, bulk data movement, or compute-heavy workloads (e.g., mining).

Defender-relevant behaviors:
- Sudden **region drift**: administrative actions from one region followed by resource creation in another.
- **First-time region usage** for a tenant/account/project that previously showed no activity.
- **Security service mismatch** across regions (logging, alerts, GuardDuty/Defender equivalents, SIEM exports).

## 3. Subtechnique Considerations
No sub-techniques.

## 4. Procedure Examples
MITRE ATT&CK does not enumerate specific CTI procedure examples on the technique page for this technique.

## 5. Detection Guidance
Detection should be built around **baseline + anomaly**:

- **Region allowlist / baseline**
  - Maintain an allowlist of expected regions by account/subscription/project.
  - Alert on *any* resource creation outside the allowlist (higher severity if the region is explicitly disabled/unused).

- **Correlate with identity and initial access signals**
  - Tie region anomalies to: suspicious login, new device, impossible travel, new API key usage, MFA changes, or elevated role assignment.

- **Service enablement parity checks**
  - Alert on region provisioning where baseline security services are not enabled (or log exports are not configured).

- **Egress and cost signals**
  - Flag unusual outbound traffic volume or destinations from newly created resources in an unused region.
  - Pair with budget/cost anomalies for rapid triage.

### Data Source Notes
**MITRE Detection Strategy (DET0247 / AN0690) log sources:**
- Instance Start — AWS CloudTrail `RunInstances`
- Cloud Storage Creation — AWS CloudTrail `CreateBucket`
- User Account Metadata — Cloud identity/API identity lookups (e.g., `GetCallerIdentity`)
- Network Connection Creation — VPC Flow Logs (notable outbound volume from new-region resources)

## 6. Response Guidance
1. **Containment (fastest wins)**
   - Disable/limit unused regions at the cloud provider level where possible.
   - Quarantine or stop newly created compute resources in the anomalous region.
   - Revoke/rotate access keys and sessions for implicated identities.

2. **Eradication**
   - Remove attacker-created resources (instances, storage, IAM roles/policies).
   - Audit region-by-region for persistence mechanisms (new IAM roles, trust policies, federated identities, scheduled functions).

3. **Recovery**
   - Enforce region guardrails (SCPs/Policies), centralized logging, and security service parity.
   - Update detection baselines and playbooks to include multi-region drift scenarios.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1496 - Resource Hijacking|T1496]]

## 8. SOC Relevance
High relevance for cloud SOCs because:
- Often indicates post-compromise activity aiming to evade centralized detections.
- Creates measurable operational impact (cost spikes, egress anomalies).
- Can be reliably detected with governance controls + CloudTrail/Activity Logs.

## 9. Threat Actor Usage
No specific threat actor mappings are listed on the technique page.

## 10. Campaign Usage
No specific campaign mappings are listed on the technique page.

## 11. Malware Usage
No specific malware/software mappings are listed on the technique page.

## 12. Mitigations
- **Software Configuration (M1054)**: Disable or restrict unused regions where supported; enforce logging and security service enablement consistently across all enabled regions.

## 13. Testing & Validation
Safe validation ideas (defender-controlled):
- Attempt to provision a minimal, legitimate instance in a “blocked/unused” region and confirm:
  - Policy prevents creation, or
  - Alerts fire for region drift and new-region provisioning.
- Verify CloudTrail/Activity Logs and SIEM pipelines ingest events from all enabled regions.
- Simulate a “logging gap” by disabling a security service in a test region and confirm detection for mismatched security posture.

## 14. References
- MITRE. (2025, October 24). *Unused/Unsupported Cloud Regions (T1535).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1535/
- MITRE. (2025, October 21). *Detection of Adversary Use of Unused or Unsupported Cloud Regions (IaaS) (DET0247).* MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0247/
- CloudSploit. (2019, June 8). *The Danger of Unused AWS Regions.* Medium. https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc

## 15. Notes
- Ensure “unused region” definitions are maintained per tenant/project and reviewed quarterly.
- Consider explicit severity upgrades when detection services (or log forwarding) are not enabled in the region where activity occurs.
