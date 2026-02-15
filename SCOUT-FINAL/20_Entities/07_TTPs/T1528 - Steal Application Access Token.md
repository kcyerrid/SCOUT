---
entity_type: mitre_technique

technique_id: "T1528"
subtechnique_id: ""
technique_name: "Steal Application Access Token"

tactic:
  - Credential Access
platforms:
  - Containers
  - IaaS
  - Identity Provider
  - Office Suite
  - SaaS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0677 - AADInternals]]"
  - "[[30_CIPHER/05_Malware/S0683 - Peirates]]"
associated_campaigns:
  - "C0049 - Leviathan Australian Intrusions"
related_techniques:
  - "T1550 - Use Alternate Authentication Material"
  - "T1556 - Modify Authentication Process"
  - "T1539 - Steal Web Session Cookie"
  - "T1566.002 - Spearphishing Link"

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
**Steal Application Access Token (T1528)** is the theft of application/API access tokens (e.g., OAuth tokens, JWTs, cloud instance tokens, Kubernetes service account tokens) to access remote services as a user or service—often bypassing passwords and some MFA controls. Because tokens frequently represent delegated authorization, token theft can rapidly translate into **data access and privilege escalation** in cloud/SaaS/container environments.

## 2. Technical Overview
Common patterns:
- **OAuth token theft**: tokens granted to malicious or compromised applications; tokens obtained via phishing or consent-grant abuse.
- **Workload token theft**: service account tokens from containers (e.g., Kubernetes) or CI/CD pipeline tokens used for automation.
- **Cloud instance metadata token theft**: short-lived tokens retrieved from instance metadata services (IMDS) on compromised compute.
- **Refresh token abuse**: theft of refresh tokens to continuously mint new access tokens, extending adversary access.

Token value drivers:
- Token scope (roles/permissions)
- Lifetime/refreshability
- Ability to use tokens from unusual IPs/clients without additional step-up auth

## 3. Subtechnique Considerations
- No subtechniques.
- Treat this technique as an **identity + application security** problem, not only endpoint security:
  - App registrations, consent grants, and service principals
  - Token issuance, audience/scope, conditional access, and token replay protections

## 4. Procedure Examples
MITRE ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S0677 - AADInternals]] stealing user access tokens (including via phishing links).
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28]] using malicious applications to steal OAuth access tokens (masquerading as legitimate apps).
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29]] using stolen tokens to access victim accounts without needing a password.
- **C0049 - Leviathan Australian Intrusions**: collection of JWTs used to create virtual desktop sessions.
- [[30_CIPHER/05_Malware/S0683 - Peirates]] gathering Kubernetes service account tokens.

## 5. Detection Guidance
Focus on **token acquisition + token replay**.

High-signal analytics:
- **Container token access + API activity**
  - Reads of Kubernetes service account token material (e.g., under `/var/run/secrets/kubernetes.io/serviceaccount/`) followed by unusual Kubernetes API calls.
- **IMDS token retrieval**
  - Access to cloud instance metadata endpoints followed by API calls from non-standard processes/agents.
- **OAuth consent/app registration anomalies**
  - New OAuth app registrations, unusual consent grants, or high-privilege scopes granted unexpectedly
  - Apps requesting mail, file, directory, or admin-level scopes outside baseline
- **Token replay anomalies**
  - Token usage from new geographies/ASNs, unusual clients, abnormal user agents, or impossible-travel patterns
  - Sudden access to high-value resources immediately after token issuance/consent
- **Correlation**
  - Phishing event → consent grant → token usage surge
  - Endpoint compromise → token file read → cloud control-plane activity

### Data Source Notes
Recommended telemetry:
- Identity provider audit logs (app registration, consent grants, service principal changes)
- Token usage logs (resource access, sign-in logs, conditional access decisions)
- Cloud control-plane audit logs (Kubernetes audit logs, cloud API logs)
- Endpoint/container file access and process telemetry for token file reads

## 6. Response Guidance
- **Revoke/contain**
  - Revoke refresh tokens/sessions for impacted accounts and service principals
  - Disable or remove suspicious OAuth apps and rotate application secrets/certs where relevant
- **Reduce blast radius**
  - Tighten scopes/roles for apps and service accounts; remove unused permissions
  - Rotate compromised workload identities and redeploy affected workloads
- **Scope**
  - Enumerate which resources were accessed using the token (mailboxes, drives, repos, cloud resources)
  - Identify secondary tokens minted via refresh tokens or delegated app access
- **Hardening**
  - Enforce admin consent workflows, restrict end-user consent, require conditional access, and implement strong monitoring for new app grants

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1528 - Steal Application Access Token|T1528]]

## 8. SOC Relevance
- Critical for cloud/SaaS detection engineering because token theft often bypasses traditional credential controls.
- Best pivots:
  - “Token issued/consent granted” → “token used” → “resource accessed”
  - Link identity events to workload/endpoint token acquisition signals

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28]]
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29]]

## 10. Campaign Usage
- C0049 - Leviathan Australian Intrusions

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0677 - AADInternals]]
- [[30_CIPHER/05_Malware/S0683 - Peirates]]

## 12. Mitigations
- **M1047 - Audit**: continuously audit cloud/container accounts, OAuth applications, and granted permissions; baseline and alert on drift.
- **M1021 - Restrict Web-Based Content**: restrict end-user OAuth consent; enforce admin consent; block risky third-party apps via CASB/app governance controls.
- Enforce conditional access and token protection controls (device compliance, step-up auth, token lifetime policies).
- Apply least privilege to workload identities (Kubernetes RBAC, cloud IAM) and rotate credentials routinely.

## 13. Testing & Validation
- Purple-team validations:
  - Validate detections for token file access in containers plus Kubernetes API anomalies
  - Validate alerting on new OAuth apps/consents with high-privilege scopes
  - Validate token replay detection (new geo, new client, impossible travel) with safe test accounts
- Ensure investigation playbooks include rapid token/session revocation actions.

## 14. References
- MITRE ATT&CK. (n.d.). *Steal Application Access Token (T1528).* https://attack.mitre.org/techniques/T1528/
- MITRE ATT&CK. (2025). *Detection Strategy for T1528 - Steal Application Access Token (DET0515).* https://attack.mitre.org/detectionstrategies/DET0515/
- Kubernetes. (n.d.). *Service Accounts.* https://kubernetes.io/docs/concepts/security/service-accounts/

## 15. Notes
- Treat token theft as a “credential theft” equivalent with **faster impact**. Successful investigations typically require joining identity logs, cloud audit logs, and endpoint/container telemetry.
