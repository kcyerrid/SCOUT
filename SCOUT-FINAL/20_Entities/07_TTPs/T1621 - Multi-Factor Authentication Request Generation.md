---
entity_type: mitre_technique

technique_id: "T1621"
subtechnique_id: ""
technique_name: "Multi-Factor Authentication Request Generation"

tactic:
  - "TA0006 - Credential Access"
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
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29]]"
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]"
  - "[[30_CIPHER/03_Threat_Actors/G1004 - LAPSUS$]]"
associated_malware: []
associated_campaigns:
  - "C0027"
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
Multi-Factor Authentication Request Generation (T1621) covers adversary behavior that attempts to bypass MFA by repeatedly generating MFA prompts (push/SMS/call/OTP challenges) to coerce the user into approving a request (often referred to as “MFA fatigue”) or to exploit self-service password reset flows that trigger MFA.

## 2. Technical Overview
Typical flow:
- Adversary obtains credentials (or can trigger SSPR prompts) but cannot complete MFA.
- They repeatedly initiate authentication attempts, causing:
  - **Push notification floods** (Duo/Okta/Microsoft Authenticator-like prompts)
  - **SMS/call/OTP prompt floods**
- Victim eventually approves a prompt, enabling account access.

Key telemetry is concentrated in the **identity plane**:
- Repeated login attempts + repeated MFA challenges
- Many denied/ignored prompts followed by a single approval
- Source IP/ASN/geolocation anomalies
- New device/browser fingerprints or impossible travel around the approval event

## 3. Subtechnique Considerations
- No subtechniques are defined for T1621.
- Separate detections by **factor type** (push vs. SMS vs. call vs. OTP) and by **authentication surface** (SSO portal vs. VPN vs. privileged apps).

## 4. Procedure Examples
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29]]: used repeated MFA requests to gain access to victim accounts (per ATT&CK procedure examples).
- C0027: campaign linked to [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]; generated repeated MFA messages until the victim accepted.
- [[30_CIPHER/03_Threat_Actors/G1004 - LAPSUS$]]: spammed targets with MFA prompts hoping users would approve.
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]: used MFA fatigue via repeated authentication requests.

## 5. Detection Guidance
High-signal analytics:
- **Bursting MFA challenges**
  - Threshold-based: high volume of MFA challenges per user per time window.
  - Baseline-based: deviation from user’s historical MFA volume.
- **Sequence-based correlation**
  - `N` failed logins → `N` MFA challenges → eventual approval from same source OR new source.
  - MFA challenge approvals following unusual login attempts (new geo/ASN/device).
- **Cross-user spray indicators**
  - Same IP/device triggering MFA challenges across multiple users (esp. admin/helpdesk accounts).
- **SSPR abuse visibility**
  - Password reset flow initiation events correlated with MFA challenge generation.

Detection tuning notes:
- Account for legitimate spikes (mobile device reconfiguration, travel, outages).
- Use “deny/timeout rate” and “approval after many denials” as stronger signals than raw counts.

### Data Source Notes
Map to your environment:
- **IdP / SSO logs**: auth attempts, MFA challenge events, challenge outcome, factor type, device ID, session ID, conditional access policy results.
- **MFA provider logs**: push request counts, delivery failures, user responses, device registration.
- **VPN / remote access logs**: MFA triggers tied to VPN logins, device posture/context.
- **SOAR enrichment**: geo/ASN reputation, impossible travel, “new device” risk signals.

## 6. Response Guidance
- **Immediate account protection**: block source IPs where appropriate, require password reset, revoke tokens/sessions, enforce step-up auth.
- **Reduce fatigue viability**: rate-limit MFA prompts; configure “number matching” / code entry rather than one-tap approvals; require phishing-resistant MFA for privileged accounts.
- **User contact & verification**: confirm whether the user initiated the authentication attempts; collect timestamps/screenshots of prompts where possible.
- **Hunt adjacent access**: review for successful logins immediately after approval; check for rapid privilege escalation, mailbox access, MFA method changes.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1621 - Multi-Factor Authentication Request Generation|T1621]]

## 8. SOC Relevance
- **High value for SOC** because it often precedes full account compromise.
- **Fast triage**: identify the first anomalous auth attempt and the first MFA push; validate whether approvals correlate with user activity.
- **Containment trigger**: “approval after many prompts” + “new device/geo” should be treated as urgent.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]] and [[30_CIPHER/03_Threat_Actors/G1004 - LAPSUS$]] have been publicly associated with MFA fatigue-style access attempts.
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29]] has used repeated MFA requests to gain account access (per ATT&CK procedure examples).

## 10. Campaign Usage
- C0027: financially motivated campaign linked to [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]] that included MFA push challenge flooding.

## 11. Malware Usage
- Not a malware-driven technique by default; it is primarily **identity workflow abuse**. Malware may appear only as a precursor to credential theft or session hijacking.

## 12. Mitigations
- **M1036 - Account Use Policies**: conditional access/location/device policies to restrict when MFA prompts can be initiated from suspicious contexts.
- **M1032 - Multi-factor Authentication**: implement stronger MFA UX (number matching/code entry) and enforce prompt rate limits.
- **M1017 - User Training**: train users to deny and report unsolicited prompts.

## 13. Testing & Validation
- In a test IdP tenant, generate controlled repeated login attempts to trigger MFA challenges and validate:
  - Alert thresholds (per-user, per-IP, per-app)
  - Correlation logic (denies/timeouts → eventual approval)
  - Analyst workflow (auto-enrichment + auto-containment options)
- Validate “benign burst” exceptions (new phone setup, travel) to tune false positives.

## 14. References
- MITRE ATT&CK. (n.d.). *Multi-Factor Authentication Request Generation (T1621).* https://attack.mitre.org/techniques/T1621/
- Parisi, T. (2022, December 2). *Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies.* CrowdStrike. https://www.crowdstrike.com/
- Microsoft. (2022, March 24). *DEV-0537 criminal actor targeting organizations for data exfiltration and destruction.* https://www.microsoft.com/

## 15. Notes
- Treat “prompt spam + new device/geo” as a compound detection; it materially reduces noise compared to volume-only alerting.
