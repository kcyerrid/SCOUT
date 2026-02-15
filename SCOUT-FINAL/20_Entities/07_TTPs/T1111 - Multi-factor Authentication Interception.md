---
entity_type: mitre_technique

technique_id: "T1111"
subtechnique_id: ""
technique_name: "Multi-Factor Authentication Interception"

tactic:
  - "TA0006 - Credential Access"
platforms:
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
  - "[[30_CIPHER/03_Threat_Actors/G1044 - APT42]]"
  - "[[30_CIPHER/03_Threat_Actors/G0114 - Chimera]]"
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky]]"
  - "[[30_CIPHER/03_Threat_Actors/G1004 - LAPSUS$]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1104 - SLOWPULSE]]"
  - "[[30_CIPHER/05_Malware/S0018 - Sykipot]]"
associated_campaigns:
  - "C0049 - Leviathan Australian Intrusions"
  - "C0014 - Operation Wocao"
related_techniques: []

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

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
Multi-Factor Authentication Interception (T1111) describes adversary attempts to capture, redirect, or proxy MFA factors (e.g., smart card PIN entry, hardware token input, one-time codes delivered via SMS/email, or service-provider delivered MFA messages) so they can complete authentication and access protected resources.

## 2. Technical Overview
Common interception patterns include:
- **Input capture of MFA secrets**: Capturing PINs or one-time codes as the user enters them (e.g., smart card PINs, token codes).
- **Out-of-band factor theft/redirect**: Intercepting SMS/email OTPs by compromising the endpoint/service used to receive them, or by redirecting where codes are delivered (e.g., adding alternate phone numbers for SMS-based codes).
- **MFA proxying**: Using an infected host as a “proxy” while the legitimate MFA device/token is present (e.g., smart card inserted on a compromised workstation).
- **Service/provider compromise**: Targeting upstream messaging or identity services responsible for delivering second factors.

Defender-relevant telemetry often spans **IdP/MFA audit logs**, **endpoint input/API access telemetry**, and **identity changes** (MFA enrollment factors, recovery numbers, forwarding rules, etc.).

## 3. Subtechnique Considerations
- No subtechniques are defined for T1111.
- Operationally, interception can look very different depending on MFA type (smart cards vs. push vs. OTP over SMS/email). Detections should be segmented by factor type and control plane (endpoint vs. IdP vs. telecom/email).

## 4. Procedure Examples
- [[30_CIPHER/03_Threat_Actors/G1044 - APT42]]: intercepted SMS-based one-time passwords and captured MFA tokens via cloned/fake sites (per ATT&CK procedure examples).
- [[30_CIPHER/03_Threat_Actors/G0114 - Chimera]]: registered alternate phone numbers to intercept 2FA codes sent via SMS.
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky]]: used tooling to intercept one-time passwords required for two-factor authentication.
- [[30_CIPHER/03_Threat_Actors/G1004 - LAPSUS$]]: replayed stolen session tokens/passwords to trigger simple-approval MFA prompts.
- C0049 - Leviathan Australian Intrusions: interception/collection of MFA token values during the intrusion.
- C0014 - Operation Wocao: custom collection method to intercept two-factor soft tokens.
- [[30_CIPHER/05_Malware/S1104 - SLOWPULSE]]: logged credentials during a VPN 2FA authentication procedure.
- [[30_CIPHER/05_Malware/S0018 - Sykipot]]: included functionality targeting smart card tech to proxy authentication.

## 5. Detection Guidance
Prioritize detections that combine **identity-plane anomalies** with **endpoint evidence**.

High-signal detection ideas:
- **MFA factor enrollment/changes**
  - New/changed MFA methods (new phone number, TOTP seed resets, new device registrations), especially shortly after a new device login, helpdesk interaction, or password reset.
  - Sudden disabling of stronger factors (FIDO2/WebAuthn) in favor of weaker fallbacks.
- **OTP delivery channel anomalies**
  - Email/SMS OTP delivery to newly added destinations, suspicious forwarding rules, or mailbox access from unusual geos/ASNs immediately preceding successful MFA challenges.
  - Telecom-related alerts (SIM swap indicators) correlated with successful MFA validations.
- **Endpoint indicators of factor capture**
  - Unusual access to OS input APIs / device interfaces (e.g., `/dev/input` on Linux), accessibility privileges or HID polling (macOS), keylogging-like API usage and driver loads (Windows), especially by non-UI apps.
- **Authentication proxy signals**
  - Successful MFA from a device/session that does not match the user’s typical device posture, coupled with suspicious remote access tooling, browser session anomalies, or impossible travel patterns.

### Data Source Notes
Because ATT&CK “Data Sources” may vary by environment, map detections to your telemetry stack:
- **Identity Provider / MFA logs**: challenge initiated/approved/denied, factor type, device identifiers, push/SMS/email delivery events, risk signals, conditional access outcomes.
- **Directory / IAM audit logs**: MFA enrollment/registration, phone number changes, recovery method edits, policy changes.
- **Endpoint security telemetry**: process ancestry, API calls related to input capture, driver/module loads, suspicious access to secure input subsystems.
- **Email/SaaS audit logs** (if OTP via email): mailbox logins, rule creation, forwarding changes, message access events.
- **Network/VPN logs**: new device posture, token-based auth patterns, abrupt session token re-use.

## 6. Response Guidance
- **Contain identity abuse**: revoke sessions/tokens, force re-authentication, reset compromised credentials, and re-enroll MFA using a verified channel.
- **Harden factor lifecycle**: require phishing-resistant factors (FIDO2/WebAuthn) for high-risk apps; restrict/monitor factor enrollment; enforce step-up verification for MFA setting changes.
- **Investigate delivery channels**: validate recent SIM swap events; review mailbox access and forwarding rules; confirm helpdesk tickets tied to identity changes.
- **Endpoint triage** (if capture suspected): isolate impacted endpoints, collect EDR triage, check for keylogging/accessibility abuse, and hunt for persistence.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1111 - Multi-Factor Authentication Interception|T1111]]

## 8. SOC Relevance
- **Best first pivot**: the user’s authentication timeline (failed logins → MFA prompts → approvals → new session/device → MFA setting changes).
- **Triage key question**: did the user *initiate* the MFA flow, and is the approving device known/managed?
- **Escalate quickly** when MFA method enrollment changes or OTP delivery destinations change in proximity to suspicious logins.

## 9. Threat Actor Usage
- Commonly associated with targeted intrusion operators and financially motivated groups when MFA is a barrier.
- Notable: [[30_CIPHER/03_Threat_Actors/G1044 - APT42]], [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky]], [[30_CIPHER/03_Threat_Actors/G1004 - LAPSUS$]].

## 10. Campaign Usage
- C0049 - Leviathan Australian Intrusions: included MFA token interception/collection.
- C0014 - Operation Wocao: used custom methods to intercept soft tokens.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1104 - SLOWPULSE]]: credential logging during VPN 2FA flows.
- [[30_CIPHER/05_Malware/S0018 - Sykipot]]: smart card proxying functionality.

## 12. Mitigations
- **M1017 - User Training**: reinforce user behavior for smart cards/OTP handling and reporting suspicious prompts; remove smart cards when not in use (per ATT&CK mitigation notes).
- Additional hardening (policy-level) typically includes restricting MFA enrollment changes, requiring phishing-resistant MFA for privileged access, and enforcing conditional access.

## 13. Testing & Validation
- **Identity-only tests (recommended)**: In a test tenant, simulate OTP destination change and verify alerting on enrollment changes + subsequent successful auth.
- **Endpoint tests (controlled lab)**: validate detections for unusual access to input capture APIs/devices using approved internal tooling and test hosts.
- Confirm correlation rules: “MFA enrollment change” + “new device/session” within a short time window.

## 14. References
- MITRE ATT&CK. (n.d.). *Multi-Factor Authentication Interception (T1111).* https://attack.mitre.org/techniques/T1111/
- Okta. (2022, August 25). *Detecting Scatter Swine: Insights into a Relentless Phishing Campaign.* https://sec.okta.com/
- Microsoft. (2022, March 24). *DEV-0537 criminal actor targeting organizations for data exfiltration and destruction.* https://www.microsoft.com/

## 15. Notes
- Consider separate analytic packs for (1) enrollment/setting changes, (2) OTP delivery anomalies, and (3) endpoint input-capture signals to reduce noise and speed triage.
