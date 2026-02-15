---
entity_type: mitre_technique

technique_id: "T1649"
subtechnique_id: ""
technique_name: "Steal or Forge Authentication Certificates"

tactic:
  - Credential Access
platforms:
  - Identity Provider
  - Linux
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0677 - AADInternals]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz]]"
associated_campaigns: []
related_techniques:
  - "T1558 - Steal or Forge Kerberos Tickets"
  - "T1552 - Unsecured Credentials"
  - "T1553.004 - Install Root Certificate"
  - "T1484.001 - Domain Policy Modification"

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
**Steal or Forge Authentication Certificates (T1649)** covers adversary theft or creation of certificates used as authentication material (e.g., AD CS certificates, device certificates in identity providers). Abuse can enable persistent, passwordless authentication and is frequently associated with **enterprise PKI/AD CS misconfiguration** and identity compromise.

## 2. Technical Overview
Primary attack surfaces:
- **AD CS certificate theft/abuse (Windows domains)**
  - Theft of certificate private keys from storage (registry/files) or export from certificate stores
  - Abuse of misconfigured/enrollable certificate templates to request certificates for privileged identities
  - CA compromise enabling broader forging of authentication certificates
- **Identity-provider device certificates**
  - Stealing device identity material used for authentication in modern identity platforms
- **Cross-platform certificate/key stores**
  - Windows cert stores / DPAPI-protected key material
  - macOS Keychain certificate/private key access
  - Linux key material and PKCS#12/OpenSSL export paths

High-impact outcome:
- “Certificate becomes a credential”—enabling access that may outlast password resets and can undermine some MFA/conditional access controls depending on configuration.

## 3. Subtechnique Considerations
- No subtechniques.
- Treat certificate-based auth abuse as a **Tier 0 identity security** event when it touches:
  - Enterprise CA/AD CS
  - Highly privileged user certificates
  - Token-signing or authentication infrastructure certificates

## 4. Procedure Examples
MITRE ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S0677 - AADInternals]] creating/exporting authentication certificates (including identity-provider device certificates).
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29]] abusing misconfigured AD CS certificate templates to impersonate admin users and create authentication certificates.
- [[30_CIPHER/05_Malware/S0002 - Mimikatz]] using certificate-related functionality to create/export authentication certificates.

## 5. Detection Guidance
Focus on **enrollment/issuance + export/access + anomalous authentication**.

High-signal analytics (Windows/AD CS):
- **Certificate enrollment anomalies**
  - Unusual certificate requests (template, requester, target identity) outside baseline
  - Requests for templates capable of client authentication from non-standard users/hosts
  - Sudden spikes in enrollment volume or failed enrollment attempts indicating probing
- **CA / template configuration drift**
  - Changes to certificate template permissions, EKUs, subject/SAN settings, manager approval settings
  - Changes to CA configuration, publication of new permissive templates
- **Private key export/access**
  - Processes accessing certificate private keys or exporting to PFX/PKCS#12 formats
  - Unusual use of certificate utilities and crypto APIs outside admin workflows

Cross-platform:
- **Linux/macOS key store access**
  - Unusual OpenSSL/PKCS#12 tooling usage aligned with key export/import behavior
  - Keychain access anomalies on macOS (unexpected processes interacting with key material)

Identity provider:
- **Device identity and certificate usage anomalies**
  - New/rare device certificate usage for high-privilege access
  - Unexpected certificate-based logons tied to new IPs, geos, or clients

### Data Source Notes
Recommended telemetry:
- AD CS logs (CA operational logs), Windows security logs, and directory service change auditing
- Certificate template and CA configuration monitoring (baseline + change detection)
- Endpoint telemetry for certificate store/private key access and export artifacts (PFX/PKCS#12 creation)
- Identity provider sign-in logs for certificate/device-based auth anomalies

## 6. Response Guidance
- **Contain**
  - Disable/revoke suspicious certificates; block impacted certificate templates; restrict enrollment
  - Isolate and treat CA servers and PKI management endpoints as Tier 0
- **Remediate root cause**
  - Audit and fix template misconfigurations (enrollment permissions, subject/SAN controls, EKUs)
  - Rotate/replace compromised CA/private keys as required; re-issue affected certificates
- **Scope**
  - Identify all certificates issued/used by the adversary and all accounts they map to
  - Hunt for subsequent access using certificate-based authentication
- **Recover**
  - Treat as identity compromise; validate conditional access and device trust controls

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1649 - Steal or Forge Authentication Certificates|T1649]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1528 - Steal Application Access Token|T1528]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1558 - Steal or Forge Kerberos Tickets|T1558]]

## 8. SOC Relevance
- High SOC urgency because certificate abuse can provide **durable, stealthy access**.
- Best pivots:
  - Enrollment events (who/what template/what subject) → certificate usage in sign-in logs
  - CA/template changes → new issuance patterns
  - Endpoint evidence of private key export → immediate sign-in anomalies

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29]]

## 10. Campaign Usage
- No specific ATT&CK “Campaigns” procedure examples are listed for this technique on the MITRE page (last modified 2025-04-15).

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0677 - AADInternals]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz]]

## 12. Mitigations
- **M1015 - Active Directory Configuration**: secure AD CS/CA servers as Tier 0; harden abusable CA settings and template attributes (including strict identity mapping controls).
- **M1047 - Audit**: continuously review and remediate certificate enrollment permissions and overly permissive templates; baseline and alert on CA/template drift.
- **M1042 - Disable or Remove Feature or Program**: disable unnecessary or risky certificate services/roles and legacy auth protocols where feasible.
- **M1041 - Encrypt Sensitive Information**: protect private keys and sensitive certificate material at rest; restrict exportability.

## 13. Testing & Validation
- Validate detection coverage for:
  - New template publication or permission changes
  - Enrollment spikes and anomalous template usage
  - Private key export artifacts (PFX/PKCS#12) and unusual crypto API callers
  - Certificate-based sign-ins from new devices/locations
- Conduct periodic PKI security assessments focusing on template abuse scenarios.

## 14. References
- MITRE ATT&CK. (n.d.). *Steal or Forge Authentication Certificates (T1649).* https://attack.mitre.org/techniques/T1649/
- MITRE ATT&CK. (n.d.). *Detection Strategy for Steal or Forge Authentication Certificates (DET0240).* https://attack.mitre.org/detectionstrategies/DET0240/
- NCC Group. (n.d.). *Defending your directory: fortifying Active Directory Certificate Services (AD CS) against exploitation.* https://www.nccgroup.com/research-blog/defending-your-directory-an-expert-guide-to-fortifying-active-directory-certificate-services-adcs-against-exploitation/

## 15. Notes
- If you confirm unauthorized certificate enrollment or private key export, prioritize identity containment and PKI remediation—password resets alone may be insufficient.
