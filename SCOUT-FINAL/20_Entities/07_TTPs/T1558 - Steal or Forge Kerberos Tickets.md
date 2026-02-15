---
entity_type: mitre_technique

technique_id: "T1558"
subtechnique_id: ""
technique_name: "Steal or Forge Kerberos Tickets"

tactic:
  - Credential Access
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
  - "[[30_CIPHER/03_Threat_Actors/G1024 - Akira]]"
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1003 - OS Credential Dumping"
  - "T1550 - Use Alternate Authentication Material"
  - "T1528 - Steal Application Access Token"
  - "T1649 - Steal or Forge Authentication Certificates"

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
**Steal or Forge Kerberos Tickets (T1558)** describes adversary theft or forgery of Kerberos authentication tickets to enable unauthorized access (commonly “Pass the Ticket”). It is a high-impact technique in Kerberos realms (especially Windows domains) because it can enable stealthy lateral movement and persistence without repeatedly presenting passwords.

## 2. Technical Overview
Key defender-relevant behaviors:
- **Ticket theft**: extracting cached tickets from hosts where users/services have authenticated.
- **Ticket forgery**: creating tickets that appear valid to services/KDCs based on compromised key material or misconfigurations.
- **Abuse of ticket-granting workflow**: unusual sequences of TGT/TGS activity, ticket lifetimes, or encryption types can indicate theft/forgery.

Sub-techniques under T1558 (for awareness and scoping):
- T1558.001 Golden Ticket
- T1558.002 Silver Ticket
- T1558.003 Kerberoasting
- T1558.004 AS-REP Roasting
- T1558.005 Ccache Files

## 3. Subtechnique Considerations
- Because T1558 is a parent technique, detection engineering is often best implemented via:
  - Ticket anomalies (KDC/service logs)
  - Host-based evidence of ticket access (LSASS/access on Windows; ccache/key material access on Linux/macOS)
  - Identity behavior anomalies following suspected theft/forgery
- Consider environment specifics:
  - Modern domains should minimize weak/legacy encryption and enforce strong Kerberos policies.
  - Linux/macOS Kerberos usage (ccache files, key material) is often under-monitored—high opportunity for detections.

## 4. Procedure Examples
MITRE ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1024 - Akira]] using scripts to dump Kerberos authentication credentials.

## 5. Detection Guidance
Design detections around **authentication telemetry + host artifacts**.

High-signal analytics (Windows domains):
- **Anomalous Kerberos log patterns**
  - Ticket requests inconsistent with normal user/service behavior (volume, targets, time)
  - TGS requests without expected preceding activity, or patterns that indicate replay
  - Unexpected encryption types (e.g., RC4 usage in environments expected to be AES-only)
- **Abnormal ticket characteristics**
  - Unusually long lifetimes, malformed fields, or privilege-bearing tickets inconsistent with baseline
- **Host-level corroboration**
  - Evidence of credential/ticket access tooling behavior (process access to authentication subsystems) preceding Kerberos anomalies

Linux/macOS:
- **Key material / cache access**
  - Suspicious access to Kerberos credential cache files or secrets databases paired with unusual Kerberos authentication patterns

### Data Source Notes
Recommended telemetry:
- Domain controller security logs and Kerberos-related audit events (KDC/service)
- Endpoint process and memory-access telemetry on Windows
- Linux/macOS file access telemetry for Kerberos cache/key material
- Identity analytics for lateral movement patterns immediately after suspected ticket theft/forgery

## 6. Response Guidance
- **Contain**
  - Isolate suspected operator endpoints; stop active credential/ticket harvesting
- **Identity actions**
  - Rotate impacted service account secrets where relevant; evaluate domain-wide impact if high-privilege ticket forgery is suspected
- **Scope**
  - Identify target services accessed using suspicious tickets; enumerate impacted hosts and accounts
- **Hardening**
  - Reduce privileged account exposure, enforce tiered admin models, and tighten Kerberos policy/encryption baselines

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1558 - Steal or Forge Kerberos Tickets|T1558]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1558.001 - Golden Ticket|T1558.001]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1558.003 - Kerberoasting|T1558.003]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1003 - OS Credential Dumping|T1003]]

## 8. SOC Relevance
- One of the most important SOC techniques for Active Directory security.
- Best pivots:
  - Kerberos anomalies → identify originating host(s) and initiating account(s)
  - Ticket anomalies → map to service access and lateral movement timelines
  - Correlate with credential dumping or certificate abuse to determine root cause

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1024 - Akira]]

## 10. Campaign Usage
- No specific ATT&CK “Campaigns” procedure examples are listed for this technique on the MITRE page (last modified 2025-10-24).

## 11. Malware Usage
- No specific ATT&CK “Software” procedure examples are listed for this parent technique on the MITRE page (software examples are often documented on subtechnique pages).

## 12. Mitigations
- **M1015 - Active Directory Configuration**: implement Kerberos hardening and recovery practices (including KRBTGT rotation procedures when applicable).
- **M1047 - Audit**: audit permissions, insecure configurations, and authentication baselines; ensure Kerberos logging is centralized.
- **M1043 - Credential Access Protection**: protect key material and sensitive authentication resources (including OS-level protections and access controls).
- **M1026 - Privileged Account Management**: restrict domain admin use; separate duties; minimize service account privileges.

## 13. Testing & Validation
- Validate detections for:
  - Anomalous Kerberos ticket lifetimes and encryption types
  - Surges in TGS requests or unusual target service patterns
  - Host-level signals of ticket/key access correlated with authentication anomalies
- Exercise incident playbooks for Kerberos compromise scenarios (containment, identity recovery, and hardening).

## 14. References
- MITRE ATT&CK. (n.d.). *Steal or Forge Kerberos Tickets (T1558).* https://attack.mitre.org/techniques/T1558/
- MITRE ATT&CK. (2025). *Detect Kerberos Ticket Theft or Forgery (T1558) (DET0522).* https://attack.mitre.org/detectionstrategies/DET0522/
- Microsoft. (n.d.). *klist command.* https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/klist

## 15. Notes
- Treat Kerberos ticket theft/forgery as an identity incident: successful investigations typically require correlating DC/KDC logs with endpoint telemetry and lateral movement evidence.
