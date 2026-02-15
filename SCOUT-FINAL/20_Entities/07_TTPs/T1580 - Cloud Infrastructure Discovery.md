---
entity_type: mitre_technique

technique_id: "T1580"
subtechnique_id: ""
technique_name: "Cloud Infrastructure Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - IaaS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]"
  - "[[30_CIPHER/03_Threat_Actors/G1053 - Storm-0501]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1091 - Pacu]]"
associated_campaigns: []
related_techniques:
  - "T1526"

detection_priority:
  - Critical

detection_maturity: ""
threat_score: 5

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
Cloud Infrastructure Discovery (T1580) is the enumeration of infrastructure resources within an IaaS environment (e.g., instances/VMs, snapshots, volumes, buckets, databases). The goal is to map accessible assets, identify high-value data stores, and plan persistence, lateral movement, or impact operations in cloud.

## 2. Technical Overview
Adversaries commonly discover cloud infrastructure via:
- **Cloud APIs** (e.g., “describe/list” operations for compute, storage, database resources)
- **CLI tooling** (AWS CLI, Azure CLI, gcloud)
- **Open-source cloud recon/exploitation frameworks** (where permissions allow)
- **Permission probing** (attempting read-only calls to infer accessible resources)

Defender-relevant intent signals:
- Rapid, multi-service discovery sequences across compute + storage + IAM-adjacent inventory.
- Discovery activity by newly compromised identities (fresh tokens, unusual device/IP).
- Enumeration that precedes snapshot creation, bucket access policy changes, or instance/role modifications.

## 3. Subtechnique Considerations
This technique has no sub-techniques. ATT&CK distinguishes it from Cloud Service Discovery (T1526) by focusing on **components/resources** (instances, buckets, snapshots) rather than **enabled services** at large.

## 4. Procedure Examples
Examples documented in ATT&CK include:
- Use of cloud exploitation frameworks to enumerate infrastructure (e.g., EC2 instances).
- Threat actors enumerating S3 buckets and other resources to identify management infrastructure, databases, and storage.

## 5. Detection Guidance
Cloud discovery is often highly detectable in provider audit logs; prioritize **behavioral baselining** and **identity context**.

High-signal detection themes:
- **Burst enumeration**: unusually high volume of list/describe calls over short windows.
- **Rare identity/app context**: discovery by principals that don’t typically perform infrastructure inventory (users, service principals, newly consented apps).
- **Unusual source**: new geolocation, new device fingerprint, suspicious ASN, or atypical user agent.
- **Chaining**: discovery followed by:
  - snapshot operations
  - access policy changes
  - instance profile/role changes
  - storage object listing and download

Practical analytics:
- Threshold alerts on repeated list/describe calls (compute/storage/db) per principal per time bucket.
- Sequence-based alerts: “enumerate → enumerate another service → enumerate IAM-adjacent inventory” within minutes.
- Correlate discovery with subsequent configuration changes or data-plane access.

### Data Source Notes
Recommended telemetry:
- Cloud provider audit logs (CloudTrail / Azure Activity Logs / GCP Audit Logs) for read-only discovery calls.
- Identity logs for sign-in context (device, IP, conditional access signals).
- Inventory metadata (resource owner, tags, account/project) to enrich triage and prioritize critical assets.

## 6. Response Guidance
1. **Identify the actor**: principal (user/role/service principal), session/token provenance, source IP/device.
2. **Quantify scope**: which services were queried, how many resources enumerated, and time window.
3. **Assess permissions**: whether the actor’s permissions are expected for their role; identify privilege escalation paths.
4. **Hunt follow-on**: snapshots, policy changes, new keys/credentials, storage access, instance modifications.
5. **Contain**: revoke tokens/keys, disable suspicious principals, and apply break-glass containment for highly privileged roles.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1580 - Cloud Infrastructure Discovery|T1580]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1526 - Cloud Service Discovery|T1526]]

## 8. SOC Relevance
- Critical in cloud IR: infrastructure discovery is a strong precursor to data access and impact.
- Enables prioritization: identify which enumerated assets are crown jewels (databases, backups, CI/CD, key vaults).

## 9. Threat Actor Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]
- [[30_CIPHER/03_Threat_Actors/G1053 - Storm-0501]]

## 10. Campaign Usage
No campaign mappings explicitly captured in the referenced ATT&CK procedure examples for this technique note.

## 11. Malware Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S1091 - Pacu]]

## 12. Mitigations
- **M1018 – User Account Management**: enforce least privilege by limiting who can discover and enumerate infrastructure; reduce permanent privileged assignments and perform entitlement reviews.

## 13. Testing & Validation
- Ensure audit logs capture read-only discovery calls across compute/storage/database services.
- Validate alerts for:
  - high-rate list/describe activity
  - discovery from new geolocations/devices
  - discovery chained with snapshot creation or policy modification
- Tabletop: simulate compromised API keys performing multi-service enumeration and verify end-to-end alerting.

## 14. References
- MITRE ATT&CK. (n.d.). *Cloud Infrastructure Discovery (T1580)*. https://attack.mitre.org/techniques/T1580/
- MITRE ATT&CK. (n.d.). *Detection Strategy for Cloud Infrastructure Discovery (DET0169)*. https://attack.mitre.org/detectionstrategies/DET0169/
- Amazon Web Services. (n.d.). *Amazon EC2 API Reference: DescribeInstances*. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html

## 15. Notes
- Treat “discovery at attacker speed” (rapid, broad enumeration) as higher risk than slow, role-consistent inventory operations.
