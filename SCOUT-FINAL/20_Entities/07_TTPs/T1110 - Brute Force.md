---
entity_type: mitre_technique

technique_id: "T1110"
subtechnique_id: ""
technique_name: "Brute Force"

tactic:
  - Credential Access
platforms:
  - Containers
  - ESXi
  - IaaS
  - Identity Provider
  - Linux
  - Network Devices
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
  - "[[30_CIPHER/03_Threat_Actors/G1030 - Agrius]]"
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0082 - APT38]]"
  - "[[30_CIPHER/03_Threat_Actors/G0087 - APT39]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41]]"
  - "[[30_CIPHER/03_Threat_Actors/G0105 - DarkVishnya]]"
  - "[[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly]]"
  - "[[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear]]"
  - "[[30_CIPHER/03_Threat_Actors/G0053 - FIN5]]"
  - "[[30_CIPHER/03_Threat_Actors/G0117 - Fox Kitten]]"
  - "[[30_CIPHER/03_Threat_Actors/G1001 - HEXANE]]"
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G1053 - Storm-0501]]"
  - "[[30_CIPHER/03_Threat_Actors/G0010 - Turla]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0572 - Caterpillar WebShell]]"
  - "[[30_CIPHER/05_Malware/S0220 - Chaos]]"
  - "[[30_CIPHER/05_Malware/S0488 - CrackMapExec]]"
  - "[[30_CIPHER/05_Malware/S0599 - Kinsing]]"
  - "[[30_CIPHER/05_Malware/S0378 - PoshC2]]"
  - "[[30_CIPHER/05_Malware/S0583 - Pysa]]"
  - "[[30_CIPHER/05_Malware/S0650 - QakBot]]"
associated_campaigns:
  - "C0025 - 2016 Ukraine Electric Power Attack"
  - "C0022 - Operation Dream Job"
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

# T1110 - Brute Force

## 1. Summary
Brute Force (T1110) covers attempts to gain access to accounts by iteratively trying credentials when passwords are unknown, or by leveraging obtained credential material (e.g., hashes) and attempting to recover usable passwords. In enterprise environments, brute force activity often manifests as abnormal authentication failure patterns and may be paired with external remote services, identity providers, and SaaS sign-in workflows.

## 2. Technical Overview
Adversaries perform brute force in two broad modes:
- **Online**: Repeated authentication attempts against a service (VPN, OWA, RDP gateways, IdP portals, SSH, network device management) until a valid combination is found or defenses trigger.
- **Offline** (often represented by subtechniques): Using stolen password hashes or dumps to recover plaintext passwords, then authenticating normally.

Common defensive friction points adversaries work around:
- Account lockouts and rate limits
- MFA and conditional access
- IP reputation controls, geo-velocity checks, “impossible travel”
- Detection thresholds based on Event IDs/log patterns

High-signal patterns include distributed attempts across many accounts, slow-and-low throttling, use of residential/proxy infrastructure, and alignment with target geography to bypass conditional access.

## 3. Subtechnique Considerations
T1110 is a parent for:
- **T1110.001 Password Guessing**: common-password/dictionary guessing without prior credential material.
- **T1110.002 Password Cracking**: recovering plaintext from obtained hashes.
- **T1110.003 Password Spraying**: one/few passwords across many accounts to avoid lockouts.
- **T1110.004 Credential Stuffing**: using breach-derived username/password pairs across services to exploit password reuse.

Operationally, distinguish subtechniques by **attempt distribution** (one account vs many), **credential source** (guessed vs leaked vs hashed), and **rate/shape** (bursty vs throttled).

## 4. Procedure Examples
Examples of usage captured in ATT&CK procedure examples include:
- Campaigns: **C0025 - 2016 Ukraine Electric Power Attack**, **C0022 - Operation Dream Job**
- Threat actors (sample): [[30_CIPHER/03_Threat_Actors/G0007 - APT28]], [[30_CIPHER/03_Threat_Actors/G1030 - Agrius]], [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]], [[30_CIPHER/03_Threat_Actors/G0010 - Turla]]
- Malware/tools (sample): [[30_CIPHER/05_Malware/S0488 - CrackMapExec]], [[30_CIPHER/05_Malware/S0650 - QakBot]], [[30_CIPHER/05_Malware/S0378 - PoshC2]]

## 5. Detection Guidance
Primary detection objective: **identify abnormal authentication failure patterns and correlate them with successful authentication, lateral movement, or privileged access**.

Detection engineering patterns:
- **Failure → success correlation**
  - Multiple failures followed by success for the same user, source, device, or session.
  - “New” success after prolonged failures from unfamiliar IP/ASN/country.
- **Horizontal patterns (many users)**
  - Many distinct usernames targeted from one IP / client fingerprint within a window.
  - One/few passwords used across many usernames (spray).
- **Distributed patterns**
  - Same username targeted from many IPs (botnet / proxy rotation) with similar UA/client hints.
  - Low-rate attempts over long dwell to evade thresholds.
- **Service-specific telemetry**
  - IdP/SaaS: conditional access outcomes, risk flags, device compliance results.
  - Windows: track 4625/4624 patterns (and equivalents), plus logon type changes.
  - Network devices: AAA/syslog authentication failures, management plane access attempts.

Triage-enrich signals:
- IP reputation, TOR/proxy markers, residential proxy providers
- Geo-velocity / impossible travel
- UA / OAuth client / legacy protocol usage (where applicable)
- Targeted account tiering (admins/service accounts vs standard users)

### Data Source Notes
This technique page does not present an explicit ATT&CK “Data Sources” list in the technique header; prioritize **authentication and identity telemetry** from:
- IdP sign-in logs (success/failure, risk, conditional access outcomes)
- OS authentication logs (Windows, Linux auth, macOS unified logs)
- Remote access and edge logs (VPN, reverse proxies, WAF/SSO front doors)
- Network device AAA/syslog logs

## 6. Response Guidance
Immediate actions (containment-first):
- Block/limit offending IPs/ASNs where safe; consider dynamic block lists and geo-fencing.
- Force password resets for impacted users; invalidate sessions/tokens where supported.
- Enforce/step-up MFA and conditional access (device compliance, location, risk-based policies).
- Review lockout policy tuning to balance prevention vs DoS risk; enable smart lockout where available.
- Hunt for post-authentication activity: privilege escalation, mailbox access, new OAuth grants, suspicious remote sessions.

Recovery / hardening:
- Implement password reuse controls and breach-password checks.
- Remove or restrict legacy protocols and weak auth paths.
- Add adaptive rate limiting and bot mitigation for public auth endpoints.

## 7. Related ATT&CK Content
[[20_Entities/07_TTPs/TA0006 - Credential Access/T1110 - Brute Force|T1110]]
[[20_Entities/07_TTPs/TA0006 - Credential Access/T1110.001 - Password Guessing|T1110.001]]
[[20_Entities/07_TTPs/TA0006 - Credential Access/T1110.002 - Password Cracking|T1110.002]]
[[20_Entities/07_TTPs/TA0006 - Credential Access/T1110.003 - Password Spraying|T1110.003]]
[[20_Entities/07_TTPs/TA0006 - Credential Access/T1110.004 - Credential Stuffing|T1110.004]]

## 8. SOC Relevance
High SOC relevance due to:
- Frequent real-world use for initial access and credential access
- Strong reliance on log/telemetry correlation rather than single-event alerts
- Clear opportunities for automation: risk scoring, block actions, password resets, token revocation

Recommended SOC automations:
- Correlate failures→success across IdP + endpoint + edge logs
- “Spray detector” and “credential stuffing detector” pipelines by service
- Enrichment (ASN, geo, proxy) and case clustering by source + target set

## 9. Threat Actor Usage
Seen in procedure examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G1030 - Agrius]]
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28]]
- [[30_CIPHER/03_Threat_Actors/G0082 - APT38]]
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41]]
- [[30_CIPHER/03_Threat_Actors/G0105 - DarkVishnya]]
- [[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly]]
- [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear]]
- [[30_CIPHER/03_Threat_Actors/G0053 - FIN5]]
- [[30_CIPHER/03_Threat_Actors/G0117 - Fox Kitten]]
- [[30_CIPHER/03_Threat_Actors/G1001 - HEXANE]]
- [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]]
- [[30_CIPHER/03_Threat_Actors/G1053 - Storm-0501]]
- [[30_CIPHER/03_Threat_Actors/G0010 - Turla]]

## 10. Campaign Usage
- C0025 - 2016 Ukraine Electric Power Attack
- C0022 - Operation Dream Job

## 11. Malware Usage
Seen in procedure examples (non-exhaustive):
- [[30_CIPHER/05_Malware/S0572 - Caterpillar WebShell]]
- [[30_CIPHER/05_Malware/S0220 - Chaos]]
- [[30_CIPHER/05_Malware/S0488 - CrackMapExec]]
- [[30_CIPHER/05_Malware/S0599 - Kinsing]]
- [[30_CIPHER/05_Malware/S0378 - PoshC2]]
- [[30_CIPHER/05_Malware/S0583 - Pysa]]
- [[30_CIPHER/05_Malware/S0650 - QakBot]]

## 12. Mitigations
ATT&CK-listed mitigations for this technique include:
- **M1036 - Account Use Policies**: lockout policies, conditional access constraints, proxy/anonymizer restrictions where possible.
- **M1032 - Multi-factor Authentication**: require MFA on externally facing services and high-risk auth paths.
- **M1027 - Password Policies**: align password policy with modern guidance and prevent weak/default passwords.
- **M1018 - User Account Management**: proactively reset/disable known-compromised accounts; monitor for breached credential exposure.

## 13. Testing & Validation
Validation goals:
- Confirm telemetry coverage for authentication failures/success across IdP, OS, edge, and key apps.
- Verify correlation rules (failures→success, spray shape, distributed attempts) trigger with benign lab simulations.
- Measure false positives: shared NATs, jump boxes, automated health checks, misconfigured clients.
- Ensure response playbooks function: block, reset, token/session revocation, MFA enforcement.

## 14. References
- MITRE. (n.d.). *Brute Force (T1110).* MITRE ATT&CK®. https://attack.mitre.org/techniques/T1110/
- NIST. (n.d.). *Digital Identity Guidelines: Authentication and Lifecycle Management (SP 800-63B).* https://pages.nist.gov/800-63-3/sp800-63b.html
- CISA. (n.d.). *Alert TA18-068A: Brute Force Attacks Conducted by Cyber Actors.* https://www.cisa.gov/news-events/alerts/ta18-068a

## 15. Notes
- Prioritize correlation and clustering: brute force rarely provides a single definitive event.
- Treat successful authentications following abnormal failure patterns as high-risk pivots for rapid containment.
