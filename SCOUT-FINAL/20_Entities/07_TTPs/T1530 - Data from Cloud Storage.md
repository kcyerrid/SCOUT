---
entity_type: mitre_technique

technique_id: "T1530"
subtechnique_id: ""
technique_name: "Data from Cloud Storage"

tactic:
  - "TA0009 - Collection"
platforms:
  - IaaS
  - Office Suite
  - SaaS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]"
  - "[[30_CIPHER/03_Threat_Actors/G0125 - HAFNIUM|HAFNIUM]]"
  - "[[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]]"
  - "[[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]]"
associated_campaigns:
  - "C0027"
related_techniques: []

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
**Data from Cloud Storage** captures adversary access to data stored in cloud object storage and cloud-hosted document repositories (IaaS object stores and SaaS/Office Suite drives). This is a common precursor to exfiltration and extortion, and can occur via stolen credentials, OAuth abuse, misconfiguration, or compromised administrative roles.

## 2. Technical Overview
Access paths:
- **Direct object access via APIs** (read/list/download operations on buckets/containers/objects).
- **Drive/document download** via SaaS platforms (e.g., enterprise drives and collaboration platforms).
- **Abuse of OAuth grants**: external apps granted access, then used to pull large volumes.
- **Shared-link exploitation**: public/over-permissive links enabling broad access.
- **Account/role misuse**: compromised IAM users/roles performing high-volume reads.

## 3. Subtechnique Considerations
- **No sub-techniques** (Enterprise).

## 4. Procedure Examples
Representative ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]] accessed victim OneDrive to search for sensitive onboarding/helpdesk/VPN/MFA-related documentation (C0027 context on ATT&CK).
- [[30_CIPHER/03_Threat_Actors/G0125 - HAFNIUM|HAFNIUM]] exfiltrated data from OneDrive.
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]] enumerates and downloads files from AWS storage services (e.g., S3).
- [[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]] can dump AWS S3 bucket contents and retrieve tokens from cloud buckets.

## 5. Detection Guidance
ATT&CK detection strategy highlights multi-platform behavior chains (DET0484 / AN1328–AN1330):
- **Spike in object access** from a new IAM user/role followed by outbound transfer.
- **OAuth token granted** to an external app followed by high-volume downloads from drive services.
- **Shared link access** outside the organization followed by mass download.

High-signal detection patterns:
- First-seen principal or new geographic/IP accessing many objects quickly.
- Unusual user agent (script/CLI) performing bulk downloads.
- Large deviations from baseline: list/read operations per minute, bytes downloaded, number of unique objects.
- Access to “high value” directories (finance, HR, identity/MFA runbooks) during intrusion windows.

### 5.1 Data Source Notes
- Ensure cloud audit telemetry is enabled and retained:
  - API call logs (who, what, where, how—principal, IP, user agent, operation, object)
  - OAuth consent/app grants and token usage
  - Storage access logs and anomaly detection features (provider-native)
- Correlate with identity logs: suspicious sign-ins, token refresh patterns, MFA prompts, and conditional access outcomes.

## 6. Response Guidance
1. **Contain identity**: disable compromised users/roles, revoke sessions, rotate keys, invalidate tokens.
2. **Contain OAuth**: revoke malicious app grants; remove app registrations/service principals if abused.
3. **Scope access**: enumerate accessed objects, shared links created/used, and download volumes.
4. **Lock down storage**: review bucket/container permissions, shared links, and cross-tenant sharing settings.
5. **Eradicate & harden**: enforce least privilege, short-lived tokens, conditional access, and IP allowlists where feasible.

## 7. Related ATT&CK Content
- Primary:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1530 - Data from Cloud Storage|T1530]]

## 8. SOC Relevance
Critical SOC relevance because cloud storage access is:
- High-impact (bulk data exposure) and common in extortion and espionage.
- Often detectable with strong baselines and identity correlation.
- A key pivot for incident scoping and legal/regulatory response.

## 9. Threat Actor Usage
ATT&CK-listed examples include:
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]], [[30_CIPHER/03_Threat_Actors/G0125 - HAFNIUM|HAFNIUM]], [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]].

## 10. Campaign Usage
ATT&CK-listed example:
- C0027 (as referenced on the ATT&CK technique page).

## 11. Malware Usage
ATT&CK-listed examples include:
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]], [[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]].

## 12. Mitigations
ATT&CK-listed mitigations include:
- **Audit (M1047)**: continuously review storage permissions and access patterns.
- **Encrypt Sensitive Information (M1041)**: encrypt at rest; plan for key rotation during incidents.
- **Filter Network Traffic (M1037)**: IP allowlisting/expected ranges for admin/API access.
- **Multi-factor Authentication (M1032)**: require MFA for access to cloud resources/APIs.
- **Restrict File and Directory Permissions (M1022)**: enforce ACLs on objects/shares.
- **User Account Management (M1018)**: least-privilege IAM roles; prefer temporary tokens.

## 13. Testing & Validation
- In a test tenant, perform controlled:
  - high-volume downloads via normal UI vs. CLI/user agents
  - OAuth consent to an app and subsequent drive reads
- Validate detections:
  - alerts for new principal + access spike
  - alerts for external OAuth app + bulk download
  - alerts for shared-link access + mass download

## 14. References
- MITRE ATT&CK. (2025, October 24). *Data from Cloud Storage (T1530)*. https://attack.mitre.org/techniques/T1530/
- Amazon. (2019, May 17). *How can I secure the files in my Amazon S3 bucket?* https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/
- Amlekar, M., Brooks, C., Claman, L., et al. (2019, March 20). *Azure Storage security guide.* https://learn.microsoft.com/en-us/azure/storage/common/storage-security-guide

## 15. Notes
- “New principal + bulk read + unusual user agent” is a high-confidence triad for detection engineering.
- Treat OAuth grants and cross-tenant sharing as first-class incident scope artifacts.
