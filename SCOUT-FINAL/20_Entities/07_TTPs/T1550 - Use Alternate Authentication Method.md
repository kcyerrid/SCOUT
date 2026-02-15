---
entity_type: mitre_technique

technique_id: "T1550"
subtechnique_id: ""
technique_name: "Use Alternate Authentication Material"

tactic:
  - Defense Evasion
  - Lateral Movement
platforms:
  - Containers
  - IaaS
  - Identity Provider
  - Linux
  - Office Suite
  - SaaS
  - Windows
datasources:
  - Logon Session Creation (DC0067)
  - Process Creation (DC0032)
  - User Account Authentication (DC0002)
  - Web Credential Usage (DC0007)

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - APT29
associated_malware:
  - FoggyWeb
associated_campaigns:
  - SolarWinds Compromise
related_techniques:
  - T1550.001
  - T1550.002
  - T1550.003
  - T1550.004

detection_priority:
  - High

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
Use Alternate Authentication Material (T1550) captures adversary use of non-password authentication artifacts (e.g., tokens, tickets, hashes) to authenticate and operate without interactive credential entry—often bypassing MFA and normal access controls, and enabling lateral movement.

## 2. Technical Overview
- **Core behavior:** Authenticate using *derived or cached* authentication material rather than plaintext secrets.
- **Common artifacts (covered by sub-techniques):**
  - **Application access tokens** (OAuth/SAML/JWT, cloud federation, service principals)
  - **Password hashes** (NTLM hashes used for network logons)
  - **Kerberos tickets** (TGT/TGS injection/replay)
  - **Web session cookies** (already-authenticated browser/service sessions)
- **Why SOCs care:** These are high-signal events because they often present as “valid logons” but with anomalies in context, issuance chain, device binding, or prerequisite events.

## 3. Subtechnique Considerations
- **T1550.001 Application Access Token:** Cloud/API authentication without interactive logon, often with suspicious scopes, app IDs, issuance context, or geographic/device mismatch.
- **T1550.002 Pass the Hash:** Windows NTLM authentication using a stolen hash; often correlates with remote service usage and non-interactive logon types.
- **T1550.003 Pass the Ticket:** Kerberos ticket injection/reuse; look for abnormal TGT/TGS chains and ticket use without expected logons.
- **T1550.004 Web Session Cookie:** Session hijacking; look for session reuse from new device fingerprints, IPs, or without prior MFA/login.

## 4. Procedure Examples
- **FoggyWeb:** Abuse of a compromised AD FS server’s SAML token for impersonation.
- **SolarWinds Compromise:** Forged SAML tokens used to impersonate users and bypass MFA for cloud access. :contentReference[oaicite:0]{index=0}

## 5. Detection Guidance
Prioritize **behavior chains** that prove “authentication material was used” without the expected upstream events (interactive login, MFA, token issuance, Kerberos chain, etc.).

**High-signal detection themes**
- **Missing prerequisite events**
  - Token/session use without preceding MFA/login.
  - Kerberos TGS activity without corresponding TGT/logon chain.
  - NTLM network logons inconsistent with domain logon/session creation patterns.
- **Context mismatches**
  - New geo/ASN/device fingerprint for same session/token.
  - Access token used from non-baseline client/app ID or scope.
  - Remote access/service start shortly after suspicious authentication on a different host.
- **Telemetry correlations**
  - Tie authentication events to process creation, network connections, and privilege/role changes.

### Data Source Notes
Leverage MITRE detection strategy log sources as a baseline:
- **Logon Session Creation (DC0067):** Windows Security 4624/4648; session anomalies; correlation anchor. :contentReference[oaicite:1]{index=1}
- **Process Creation (DC0032):** Sysmon 1; suspicious spawning around authentication events. :contentReference[oaicite:2]{index=2}
- **User Account Authentication (DC0002):** auditd/SSHD accepted auth, IdP auth logs, SaaS sign-ins. :contentReference[oaicite:3]{index=3}
- **Web Credential Usage (DC0007):** Cloud/IdP token issuance/usage, CloudTrail/SignIn logs, API access via tokens. :contentReference[oaicite:4]{index=4}

## 6. Response Guidance
1. **Contain**
   - Isolate affected endpoints and suspend suspicious sessions (IdP, SaaS, cloud consoles).
   - Revoke/rotate tokens, sessions, federation trust artifacts (as applicable).
2. **Eradicate**
   - Identify and remove token/cookie theft tooling, credential dumping artifacts, and persistence mechanisms.
3. **Recover**
   - Force re-authentication and enforce MFA re-prompt; rotate secrets tied to token minting (client secrets, signing certs, KRBTGT if needed).
4. **Hunt**
   - Pivot from impacted principal → enumerate all sessions, issued tokens, Kerberos tickets, and lateral authentications in the time window.
5. **Hardening**
   - Token binding/DPoP where supported, conditional access, device compliance, session lifetime reduction, admin separation, and least privilege.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1550 - Use Alternate Authentication Material|T1550]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1550 - Use Alternate Authentication Material|T1550]]
- Sub-techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1550.001 - Application Access Token|T1550.001]]
  - [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1550.001 - Application Access Token|T1550.001]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1550.002 - Pass the Hash|T1550.002]]
  - [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1550.002 - Pass the Hash|T1550.002]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1550.003 - Pass the Ticket|T1550.003]]
  - [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1550.003 - Pass the Ticket|T1550.003]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1550.004 - Web Session Cookie|T1550.004]]
  - [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1550.004 - Web Session Cookie|T1550.004]]

## 8. SOC Relevance
- **Alerting:** Treat token/ticket/hash/cookie reuse anomalies as priority signals (often precede privilege escalation and lateral movement).
- **Visibility gaps to close:** Centralized IdP/SaaS logs, Windows event forwarding, Sysmon, cloud audit trails, and consistent identity telemetry enrichment (device, geo, app ID, auth method).
- **Best SOC outcome:** Catch and revoke sessions/tokens before adversary pivots to widespread lateral movement.

## 9. Threat Actor Usage
- **APT29** is documented using forged tokens (e.g., SAML) for cloud impersonation in SolarWinds-related activity. :contentReference[oaicite:5]{index=5}

## 10. Campaign Usage
- **SolarWinds Compromise (C0024)** includes token/cookie-related access patterns used to access cloud resources and bypass MFA. :contentReference[oaicite:6]{index=6}

## 11. Malware Usage
- **FoggyWeb** associated with AD FS token abuse. :contentReference[oaicite:7]{index=7}

## 12. Mitigations
- **Account Use Policies:** Restrict where/when authentication material can be used; enforce conditional access. :contentReference[oaicite:8]{index=8}
- **Active Directory Configuration:** Reduce Kerberos/AD abuse paths; apply filtering and hardened configs. :contentReference[oaicite:9]{index=9}
- **Application Developer Guidance:** Token binding / proof-of-possession controls where supported. :contentReference[oaicite:10]{index=10}
- **Audit:** Continuous review of permissions, insecure configs, token issuance capabilities. :contentReference[oaicite:11]{index=11}
- **Password Policies / Privileged Account Management / User Account Management:** Reduce credential overlap and admin sprawl. :contentReference[oaicite:12]{index=12}

## 13. Testing & Validation
- **Purple-team mapping:** Validate each sub-technique’s detection chain (prerequisite → issuance/creation → use).
- **Control tests (safe)**
  - Session/token anomaly simulations in test tenants (short-lived tokens, geo variance, client fingerprint variance).
  - Windows lab: validate correlation rules around 4624/4648 + Sysmon 1/3 + Kerberos events where applicable.
- **Open tooling (defender-oriented)**
  - MITRE Caldera: https://github.com/mitre/caldera
  - Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
  - Sigma rules: https://github.com/SigmaHQ/sigma

## 14. References
- MITRE ATT&CK. (n.d.). *Use Alternate Authentication Material (T1550).* https://attack.mitre.org/techniques/T1550/ :contentReference[oaicite:13]{index=13}
- MITRE ATT&CK. (2025-10-21). *Behavioral Detection Strategy for Use Alternate Authentication Material (T1550) (DET0338).* https://attack.mitre.org/detectionstrategies/DET0338/ :contentReference[oaicite:14]{index=14}
- Microsoft. (n.d.). *FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor.* https://www.microsoft.com/ (Referenced from MITRE technique page) :contentReference[oaicite:15]{index=15}

## 15. Notes
- Consider adding environment-specific “expected contexts” (approved geos, devices, IdP app IDs, token lifetimes) to reduce false positives while maintaining high sensitivity to abuse.
