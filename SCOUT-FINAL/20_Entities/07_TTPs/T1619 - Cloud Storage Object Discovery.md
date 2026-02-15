---
entity_type: mitre_technique
technique_id: "T1619"
subtechnique_id: ""
technique_name: "Cloud Storage Object Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "IaaS"
datasources:
  - "Cloud Storage Enumeration (DC0017)"
  - "Cloud Storage Access (DC0025)"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors: []
associated_malware:
  - "[[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]]"
  - "[[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]]"
associated_campaigns: []
related_techniques: []
detection_priority:
  - High
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
Adversaries enumerate objects (files/blobs) within cloud storage services to understand what data exists and to plan follow-on actions such as targeted retrieval, bulk collection, or staging.

## 2. Technical Overview
Cloud providers expose APIs to list objects within buckets/containers (e.g., AWS S3 listing operations, Azure Blob listing operations). Attackers with valid credentials (or temporary access tokens) can enumerate object keys, prefixes, sizes, timestamps, and metadata. This discovery is often a precursor to:
- Targeted data access (sensitive prefixes, backups, logs)
- Large-scale collection and exfiltration planning
- Identifying application artifacts (configs, keys, database dumps) stored in object storage

Common signals include repeated listing calls across many prefixes, buckets, or storage accounts, and enumeration from atypical identities, regions, or user agents.

## 3. Subtechnique Considerations
No sub-techniques.

## 4. Procedure Examples
Observed in ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]] enumerates AWS storage services such as S3 buckets and EBS volumes.
- [[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]] can list AWS S3 buckets.

## 5. Detection Guidance
Detection focus: identify anomalous *enumeration* patterns rather than one-off administrative listings.
- Baseline normal listing behaviors by role (CI/CD, backup jobs, data pipelines) and expected regions/IP ranges.
- Alert on bursts of enumeration (many List operations in a short time), especially when followed by object retrieval (Get/Copy/Download).
- Correlate enumeration with identity context (new access keys, newly assumed roles, unusual device posture, impossible travel, or new user agent).
- Prioritize high-value buckets/containers (backups, audit logs, customer PII, secrets/config artifacts).

Heuristic ideas (implementation depends on your telemetry):
- Enumeration volume anomaly: identity performs object listings > baseline (per bucket + per time window).
- Breadth anomaly: identity enumerates many distinct buckets/containers or prefixes in a short window.
- Sequence anomaly: List → rapid, repeated GetObject/Download for newly discovered keys.
- Geo/network anomaly: listing from new region, ASN, or “break-glass” network not associated with that role.

### Data Source Notes
Required/strongly recommended telemetry:
- **Cloud Storage Enumeration (DC0017)**: provider audit logs capturing list operations (e.g., AWS CloudTrail ListObjectsV2).
- **Cloud Storage Access (DC0025)**: provider audit logs capturing object retrieval/copy operations (e.g., AWS CloudTrail GetObject/CopyObject).

Operational notes:
- Ensure storage data events are enabled where applicable (some platforms require explicit enablement for object-level events).
- Preserve request parameters where available (bucket/container, prefix, pagination markers, caller identity, user agent, source IP, region).

## 6. Response Guidance
1. **Triage identity and scope**: confirm the principal (user/role/service account), source IP/region, user agent, and time window.
2. **Enumerated targets**: list buckets/containers/prefixes enumerated; identify whether they contain sensitive data.
3. **Follow-on access**: check for subsequent object reads/copies/downloads, cross-account access attempts, or abnormal egress.
4. **Containment**: revoke/rotate keys, disable sessions/tokens, restrict bucket policies temporarily, and enforce least privilege.
5. **Eradication and hardening**: tighten IAM permissions for list operations; add conditional access (IP allowlists, device posture, MFA where possible).
6. **Evidence preservation**: export audit logs and object access logs; snapshot relevant IAM and bucket policy state for incident record.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1619 - Cloud Storage Object Discovery|T1619]]

## 8. SOC Relevance
High SOC value because storage enumeration often precedes impactful outcomes (data theft, extortion). It also produces durable audit trails in most cloud environments when logging is correctly enabled.

## 9. Threat Actor Usage
No ATT&CK procedure examples list a specific threat group for this technique.

## 10. Campaign Usage
No ATT&CK procedure examples list a specific campaign for this technique.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]]
- [[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]]

## 12. Mitigations
- **User Account Management (M1018)**: restrict object listing permissions to necessary accounts; separate duties for admins vs. workload identities; prefer narrowly scoped roles.

## 13. Testing & Validation
Safe validation ideas (in a lab/non-production account):
- Generate a small burst of object listing calls using a test role against a test bucket; verify audit log capture for enumeration.
- Simulate “breadth” enumeration across multiple test buckets/prefixes; confirm detections on volume/breadth anomalies.
- Validate correlation rules by generating a sequence: List → Get for several objects; confirm alerts include both enumeration and follow-on access.

## 14. References
- MITRE ATT&CK. (n.d.). *Cloud Storage Object Discovery (T1619)*. https://attack.mitre.org/techniques/T1619/
- Amazon Web Services. (n.d.). *Amazon S3 API: ListObjectsV2*. https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html
- Microsoft. (n.d.). *List Blobs (Azure Storage)*. https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs
- Rhino Security Labs. (2019, August 22). *Pacu*. https://github.com/RhinoSecurityLabs/pacu

## 15. Notes
- Ensure object-level audit coverage is enabled for high-value buckets; many “mystery” gaps in investigations trace back to incomplete data-event logging.
