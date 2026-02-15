---
entity_type: mitre_technique

technique_id: "T1526"
subtechnique_id: ""
technique_name: "Cloud Service Discovery"

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
  - "[[30_CIPHER/03_Threat_Actors/G1053 - Storm-0501]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0677 - AADInternals]]"
  - "[[30_CIPHER/05_Malware/S1091 - Pacu]]"
  - "[[30_CIPHER/05_Malware/S0684 - ROADTools]]"
associated_campaigns: []
related_techniques:
  - "T1580"

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
Cloud Service Discovery (T1526) is the enumeration of cloud services enabled or accessible in an environment after access is obtained. This can include IaaS/PaaS/SaaS services (e.g., logging, security services, identity integrations, CI/CD) and is often used to select follow-on targets and evade defenses.

## 2. Technical Overview
Discovery methods commonly include:
- Querying **cloud control-plane APIs** and management planes (e.g., ARM/Graph-style enumeration, “list providers/services,” project/service listings).
- Enumerating **identity and app integrations** (applications, service principals, OAuth apps) to map service access paths.
- Enumerating **security and logging services** to understand detection posture and potential evasion opportunities.

Defender-relevant intent signals:
- Broad enumeration of “what services exist here” followed by targeted access attempts (storage, mail, CI/CD, secrets).
- Enumeration of security controls (policies, locks, immutability) that precedes disablement attempts.

## 3. Subtechnique Considerations
This technique has no sub-techniques. ATT&CK distinguishes it from Cloud Infrastructure Discovery (T1580) by focusing on **services and capabilities** rather than **specific infrastructure components**.

## 4. Procedure Examples
Examples documented in ATT&CK include:
- Tooling that enumerates Office 365/SharePoint/OpenID configuration and other cloud services.
- Enumeration of AWS services such as logging/monitoring services.
- Enumeration of Azure AD applications and service principals.
- Actor discovery of protections such as policies, resource locks, and storage immutability settings.

## 5. Detection Guidance
Cloud service discovery is typically visible in audit logs; detection should emphasize **volume, novelty, and identity context**.

High-signal detection themes:
- **New principal performing admin-like enumeration** (especially service principals/apps that don’t usually do inventory).
- **High-volume service listings** across multiple product areas (identity + logging + compute + storage).
- **Discovery-to-action sequences**: enumeration quickly followed by role changes, disabling logs, or changing security configurations.

Practical analytics:
- Alert on bursts of “list services/providers/resources” operations by user/service principals, especially from new IP/device.
- Detect enumeration of identity integrations (applications/service principals) paired with token/credential changes (new secrets, new certs, consent grants).
- Correlate discovery with subsequent attempts to modify logging/security services.

### Data Source Notes
Recommended telemetry:
- Provider audit logs (control-plane reads and list operations).
- Identity audit logs (app/service principal enumeration, OAuth changes, sign-in context).
- Conditional access and risk signals (to prioritize suspicious enumeration).

## 6. Response Guidance
1. **Identify actor/session**: principal, app ID (if applicable), token creation time, source IP/device.
2. **Enumerate scope**: which services were listed and what categories were queried (identity, logging, security, storage, CI/CD).
3. **Assess intent**: look for follow-on activity targeting enumerated services (data access, privilege escalation, defense evasion).
4. **Contain**: revoke sessions/keys, disable suspicious apps/service principals, and restrict directory/service listing privileges.
5. **Hardening**: tighten least privilege for service discovery APIs and reduce standing permissions for inventory-like access.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1526 - Cloud Service Discovery|T1526]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1580 - Cloud Infrastructure Discovery|T1580]]

## 8. SOC Relevance
- High value early cloud recon signal; frequently precedes credential access, persistence, and large-scale data access.
- Especially important for detecting **compromised service principals** and **consented OAuth apps** performing tenant-wide enumeration.

## 9. Threat Actor Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1053 - Storm-0501]]

## 10. Campaign Usage
No campaign mappings explicitly captured in the referenced ATT&CK procedure examples for this technique note.

## 11. Malware Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S0677 - AADInternals]]
- [[30_CIPHER/05_Malware/S1091 - Pacu]]
- [[30_CIPHER/05_Malware/S0684 - ROADTools]]

## 12. Mitigations
- MITRE notes this behavior is difficult to prevent because it often leverages legitimate system/service features.
- Reduce impact by enforcing least privilege for service listing and identity enumeration operations; constrain service principals and app permissions.

## 13. Testing & Validation
- Validate logging for:
  - “list/describe services” calls
  - identity/app/service principal enumeration
  - sign-in context for actors performing discovery
- Purple-team scenario:
  - compromised identity enumerates enabled services, then pivots to a high-value service (storage/mail/CI/CD); confirm correlated alerting.

## 14. References
- MITRE ATT&CK. (n.d.). *Cloud Service Discovery (T1526)*. https://attack.mitre.org/techniques/T1526/
- MITRE ATT&CK. (n.d.). *Detection Strategy for Cloud Service Discovery (DET0402)*. https://attack.mitre.org/techniques/T1526/
- Dirk-jan Mollema. (n.d.). *ROADtools* (referenced by ATT&CK procedure examples). https://dirkjanm.io/roadtools/

## 15. Notes
- Treat tenant-wide enumeration by unfamiliar apps/service principals as a priority-one triage condition in cloud environments.
