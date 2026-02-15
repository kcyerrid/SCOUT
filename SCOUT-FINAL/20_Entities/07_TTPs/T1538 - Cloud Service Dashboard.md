---
entity_type: mitre_technique

technique_id: "T1538"
subtechnique_id: ""
technique_name: "Cloud Service Dashboard"

tactic:
  - "TA0007 - Discovery"
platforms:
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
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]"
associated_malware: []
associated_campaigns: []
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
Cloud Service Dashboard (T1538) is the use of cloud provider/SaaS dashboards (web GUIs) with stolen credentials to enumerate services, resources, and security posture—often without making explicit API calls. This can reduce visibility if defenders focus only on API/CLI telemetry.

## 2. Technical Overview
Typical characteristics:
- Access occurs via **browser-based sessions** (or mobile clients), often using valid credentials and MFA-bypassed sessions.
- The dashboard can expose:
  - asset inventories
  - findings/security posture summaries
  - configuration visibility (depending on RBAC)
  - resource relationships and navigation paths

Defender-relevant intent signals:
- Dashboard navigation to sensitive pages (IAM, app integrations, security findings, export/reporting).
- Read-heavy exploration shortly after suspicious sign-in events.
- GUI usage by identities that typically use API/CLI automation.

## 3. Subtechnique Considerations
This technique has no sub-techniques.

## 4. Procedure Examples
Examples documented in ATT&CK include:
- Threat actor abuse of inventory/console features to identify targets prior to lateral movement.

## 5. Detection Guidance
High-fidelity detection requires **web/GUI telemetry** and correlation with identity context.

High-signal detection themes:
- **SaaS/IaaS console login** followed by immediate navigation to sensitive dashboards or reports.
- **Atypical access context**: new device, new geolocation, impossible travel, high-risk ASN, unusual user agent.
- **GUI vs API mismatch**: an identity normally associated with API automation suddenly uses GUI sessions extensively.
- **Session anomalies**: token replay signals, device binding failures, suspicious conditional access outcomes.

Practical analytics:
- Alert on GUI logins from unfamiliar device/IP followed by high-volume dashboard page views or metadata retrieval actions.
- Correlate dashboard access with:
  - subsequent role changes, app consent, credential additions
  - downloads/exports of reports or inventories (where logged)
- Enrich alerts with “what pages were accessed” and “what account role level” to prioritize investigations.

### Data Source Notes
Recommended telemetry:
- Cloud/SaaS audit logs for console sign-ins and GUI activity (where available).
- Identity provider sign-in logs (device/user agent, CA policy outcomes, risk signals).
- Web proxy logs (admin portal hostnames/paths) if first-party GUI telemetry is limited.

## 6. Response Guidance
1. **Validate legitimacy**: confirm whether the access aligns with the user’s job function and known devices.
2. **Scope the session**: pages visited, resources viewed, exports/downloads, and admin actions.
3. **Hunt follow-on**: role changes, new app consents, mailbox/storage access, key vault access, and policy modifications.
4. **Contain**: force sign-out, revoke sessions, rotate credentials, and review conditional access requirements for dashboards.
5. **Hardening**: restrict dashboard visibility via least privilege and require stronger authentication for admin portals.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1538 - Cloud Service Dashboard|T1538]]

## 8. SOC Relevance
- High relevance in cloud-first environments because GUI usage can be an early indicator of interactive intrusion.
- Particularly important when adversaries avoid noisy API calls and rely on what the console reveals.

## 9. Threat Actor Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider]]

## 10. Campaign Usage
No campaign mappings explicitly captured in the referenced ATT&CK procedure examples for this technique note.

## 11. Malware Usage
No malware mappings explicitly captured in the referenced ATT&CK procedure examples for this technique note.

## 12. Mitigations
- **M1018 – User Account Management**: enforce least privilege to limit what dashboards reveal; restrict high-risk pages to admin roles and privileged access workflows.

## 13. Testing & Validation
- Validate you can detect:
  - console login from unknown device/IP
  - rapid navigation to IAM/security posture/configuration pages
- Purple-team scenario:
  - compromised user session accesses admin dashboards in GUI, then queries inventory pages; confirm correlation and alerting.

## 14. References
- MITRE ATT&CK. (n.d.). *Cloud Service Dashboard (T1538)*. https://attack.mitre.org/techniques/T1538/
- MITRE ATT&CK. (n.d.). *Detection of Cloud Service Dashboard Usage via GUI-Based Cloud Access (DET0291)*. https://attack.mitre.org/techniques/T1538/
- Cybersecurity and Infrastructure Security Agency. (2023, November 16). *Cybersecurity Advisory: Scattered Spider (AA23-320A)*. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a

## 15. Notes
- If your logging is API-centric, explicitly add coverage for GUI-based admin activity and page-level audit trails where supported.
