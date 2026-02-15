---
entity_type: mitre_technique

technique_id: "T1606"
subtechnique_id: ""
technique_name: "Forge Web Credentials"

tactic:
  - Credential Access
platforms:
  - IaaS
  - Identity Provider
  - Linux
  - Office Suite
  - SaaS
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]]"
associated_malware: []
associated_campaigns:
  - "C0024 - SolarWinds Compromise"
related_techniques:
  - "T1539 - Steal Web Session Cookie"
  - "T1528 - Steal Application Access Token"
  - "T1550 - Use Alternate Authentication Material"
  - "T1552.004 - Unsecured Credentials: Private Keys"

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
Forge Web Credentials (T1606) covers adversary creation of *new* web authentication materials (e.g., cookies, SAML tokens) that can be used to access SaaS/IaaS/IdP-backed applications and services—often bypassing MFA when token/cookie trust is intact. This differs from stealing existing sessions/tokens; the artifact is minted/forged by the adversary.

## 2. Technical Overview
Adversaries forge credential materials by abusing signing keys, shared secrets, federation trust, or cloud/IdP features that legitimately mint temporary credentials. Common patterns include:
- **Forged cookies** generated from a stolen/derived secret (e.g., AD FS/OWA-related secrets) and injected into a session store or request headers.
- **Forged federation assertions** (e.g., SAML “Golden SAML”) created using a compromised token-signing certificate or by establishing/abusing federation trust to sign attacker-controlled assertions.
- **Cloud/API abuse** where token minting occurs via legitimate APIs (e.g., unusual AssumeRole/GetFederationToken-style minting behavior) combined with abnormal session usage.

## 3. Subtechnique Considerations
- **T1606.001 (Web Cookies):** High-signal on endpoints (browser cookie stores) and web app session telemetry; correlation to MFA-bypass patterns is key.
- **T1606.002 (SAML Tokens):** High-signal in IdP/AD FS/Entra ID sign-in telemetry; strongest detections rely on event correlation gaps (valid assertions without expected prerequisite auth events) and issuer/claims anomalies.

## 4. Procedure Examples
- **SolarWinds Compromise (C0024):** Reporting indicates cookie/token forgery used to bypass MFA for cloud/web access. See sub-techniques for specifics.  
  - Web Cookies: [[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]] generated a cookie value from a previously stolen secret key to bypass MFA on OWA.  
  - SAML Tokens: [[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]] created tokens using compromised SAML signing certificates.

## 5. Detection Guidance
Prioritize correlation-driven detections that answer: **“How did this session/token become valid?”**

**High-signal detection themes**
- **IdP / Federation anomalies**
  - SAML/OIDC tokens accepted with **no corresponding interactive auth / Kerberos prerequisites** for the same principal/time window.
  - Token lifetimes, issuers, audiences, or claims **outside baseline** (e.g., new/rare issuers; privilege claims not typical for user).
  - **Token signing certificate usage** anomalies (unexpected thumbprints, sudden signing key change, signing outside maintenance windows).
- **Cloud control plane anomalies**
  - Unusual token minting activity (e.g., security token service calls by unusual principals, regions, source IPs), followed by privileged access.
- **Endpoint/browser artifacts**
  - Non-browser processes accessing or writing cookie stores/session databases, followed by web logons without normal interactive prompts.

### Data Source Notes
Minimum telemetry to support robust detections:
- **IdP/SSO logs:** AD FS/Azure AD (Entra ID) sign-in logs, federation logs, token issuance logs, certificate/key management/audit logs.
- **Cloud audit logs:** cloud control-plane logs for token/service credential creation and role assumption; identity audit trails.
- **Web app access logs:** session creation/validation, MFA state, geolocation/IP/device fingerprinting, user-agent patterns.
- **Endpoint telemetry:** process/file access for browser session stores; keychain/credential store access; EDR event correlation.

## 6. Response Guidance
1. **Contain access**
   - Revoke active sessions where supported; force re-authentication; invalidate refresh tokens where applicable.
2. **Rotate trust material**
   - Rotate federation/token signing certs and relevant secrets/keys; validate certificate pinning/trust chains.
3. **Hunt and scope**
   - Identify accounts/resources accessed with forged artifacts; enumerate session IDs/assertion IDs; expand by issuer/claim anomalies.
4. **Hardening**
   - Reduce exposure of IdP/AD FS; enforce conditional access/device compliance; restrict token issuance to expected networks/devices.

## 7. Related ATT&CK Content
- Technique placement:
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1606 - Forge Web Credentials|T1606]]
- Sub-techniques:
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1606.001 - Web Cookies|T1606.001]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1606.002 - SAML Tokens|T1606.002]]
- Related techniques (commonly adjacent in investigations):
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1539 - Steal Web Session Cookie|T1539]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1528 - Steal Application Access Token|T1528]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1550 - Use Alternate Authentication Material|T1550]]
  - [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1550 - Use Alternate Authentication Material|T1550]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.004 - Private Keys|T1552.004]]

## 8. SOC Relevance
- **Why it matters:** Often indicates **identity perimeter compromise** and can enable rapid privilege escalation in cloud/SaaS.
- **Best alerts:** Token/session acceptance **without expected auth precursor events**; “impossible travel” sessions with valid tokens; signing key/cert anomalies.
- **Common pitfalls:** Looking only for “failed logins” or MFA prompts—successful forged tokens can be “clean” in superficial sign-in logs.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]] (documented in SolarWinds-era operations via cookie/token forgery).

## 10. Campaign Usage
- C0024 - SolarWinds Compromise

## 11. Malware Usage
- None explicitly enumerated at the parent-technique level; see sub-techniques for software references (e.g., token/cookie tooling).

## 12. Mitigations
- **M1047 – Audit:** Audit access lists/permissions for web apps and federation services; baseline and periodically re-audit.
- **M1026 – Privileged Account Management:** Restrict and harden privileged access to IdP/AD FS infrastructure and cloud identity administration.
- **M1054 – Software Configuration:** Configure clients to regularly delete/rotate persistent web credential artifacts where appropriate.
- **M1018 – User Account Management:** Reduce highly privileged role memberships; enforce strong auth and least privilege; restrict sensitive token minting APIs to approved principals.

## 13. Testing & Validation
- Validate detections in a **controlled lab** using benign identity-event simulations:
  - Confirm you can detect **token issuance without expected auth prerequisites** (gap-based correlation).
  - Confirm detection of **abnormal token lifetime/issuer/claims** relative to baseline.
- If using Atomic Red Team or similar frameworks, prefer **log-generation and correlation validation** over executing real credential-forgery procedures in production.

## 14. References
- MITRE ATT&CK. (n.d.). *Forge Web Credentials (T1606).* https://attack.mitre.org/techniques/T1606/
- MITRE ATT&CK. (n.d.). *Forge Web Credentials: Web Cookies (T1606.001).* https://attack.mitre.org/techniques/T1606/001/
- MITRE ATT&CK. (n.d.). *Forge Web Credentials: SAML Tokens (T1606.002).* https://attack.mitre.org/techniques/T1606/002/
- Bierstock, D., & Baker, A. (2019, March 21). *I am AD FS and So Can You.* https://www.troopers.de/troopers19/talks/9cpdld/
- MSRC. (2020, December 13). *Customer Guidance on Recent Nation-State Cyber Attacks.* https://msrc-blog.microsoft.com/2020/12/13/customerguidance/

## 15. Notes
- Detection Strategy (MITRE): **DET0260 – Detection Strategy for Forged Web Credentials** (analytics AN0717–AN0723).
- Treat any confirmed forging as a **trust-anchor incident**: keys/certs/secrets and federation trust should be assumed compromised until proven otherwise.
