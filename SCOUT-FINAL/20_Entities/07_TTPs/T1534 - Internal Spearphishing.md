---
entity_type: mitre_technique

technique_id: "T1534"
subtechnique_id: ""
technique_name: "Internal Spearphishing"

tactic:
  - "TA0008 - Lateral Movement"
platforms:
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
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G1001 - HEXANE|HEXANE]]"
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]"
  - "[[30_CIPHER/03_Threat_Actors/G0065 - Leviathan|Leviathan]]"
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]"
associated_malware: []
associated_campaigns:
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

## 1. Summary
After gaining an initial foothold (compromised account or device), adversaries use trusted internal identities and channels (email, chat, collaboration tools) to phish additional users inside the same organization, increasing success rates through internal trust. :contentReference[oaicite:18]{index=18}

## 2. Technical Overview
- **What it is:** A lateral movement technique where an attacker leverages **already-compromised internal accounts** to distribute malicious links/attachments or to solicit sensitive data from coworkers.
- **Common internal channels:** corporate email, shared mailboxes, Microsoft Teams/Slack-like chat, collaboration platforms, and internal HR/IT workflows.
- **Typical objectives:** expand access, collect credentials, deliver payloads, or harvest sensitive information (e.g., finance/HR data). :contentReference[oaicite:19]{index=19}

## 3. Subtechnique Considerations
N/A (no sub-techniques).

## 4. Procedure Examples
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]] used an Outlook VBA module to send internal phishing emails with malicious attachments. :contentReference[oaicite:20]{index=20}  
- [[30_CIPHER/03_Threat_Actors/G1001 - HEXANE|HEXANE]] conducted internal spearphishing against executives/HR/IT. :contentReference[oaicite:21]{index=21}  
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]] used internal spearphishing for lateral movement after stealing victim information. :contentReference[oaicite:22]{index=22}  
- [[30_CIPHER/03_Threat_Actors/G0065 - Leviathan|Leviathan]] conducted internal spearphishing within victim environments. :contentReference[oaicite:23]{index=23}  
- **C0022 - Operation Dream Job:** [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]] conducted internal spearphishing from within a compromised organization. :contentReference[oaicite:24]{index=24}  

## 5. Detection Guidance
**Core idea:** Identify **abuse of trusted identity + internal delivery + follow-on interaction**.

**MITRE detection strategy-aligned chains**
- Internal message/email from a user with **recently abnormal account/device activity**, containing an attachment or URL, followed by:
  - click/download events
  - execution on endpoint
  - credential prompts/harvest behavior :contentReference[oaicite:25]{index=25}

**High-signal detection opportunities**
- **Account compromise precursor:** unusual login geography/device, impossible travel, OAuth consent anomalies, new mail rules.
- **Internal delivery anomalies:** sudden spike in internal recipients, uncommon attachment types, high-entropy filenames, macro-enabled docs sent internally.
- **User interaction correlation:** internal message → link click → browser to new domain → credential prompt → new sign-in.
- **Collaboration platform abuse (e.g., Teams):** message from internal user to unusual recipients/tenants with external link or file; prompt for credentials. :contentReference[oaicite:26]{index=26}

### Data Source Notes
*(Leave YAML `datasources` empty unless you have a canonical local mapping. Below are practical telemetry requirements.)*
- **Email security logs:** message trace, attachment metadata, URL rewriting/click logs, mail rule changes.
- **Identity logs:** IdP sign-ins, conditional access events, OAuth app grants, risky sign-ins.
- **Endpoint telemetry:** process creation from Office apps (macro spawns), browser downloads, execution from temp/email cache locations.
- **Collaboration audit logs:** Teams/Slack message/file events, sharing links, external tenant interactions. :contentReference[oaicite:27]{index=27}

## 6. Response Guidance
1. **Contain the identity:** reset credentials, revoke tokens/sessions, remove malicious OAuth grants, block suspicious client devices.
2. **Pull message traces:** isolate all internally delivered phishing artifacts (hashes, URLs, recipients) and mass-quarantine.
3. **Hunt for follow-on:** endpoint executions tied to recipients; new credential use; additional internal propagation.
4. **Strengthen controls:** enforce MFA/CA policies, disable legacy auth, tighten macro controls, increase scrutiny on internal-to-internal phishing.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1534 - Internal Spearphishing|T1534]]

## 8. SOC Relevance
- **Priority:** High—often converts a single compromised user into broader org compromise.
- **SOC focus:** identity security + email/collaboration telemetry correlation.
- **Key KPI:** time-to-quarantine internal phish messages and time-to-revoke compromised sessions.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]] :contentReference[oaicite:28]{index=28}  
- [[30_CIPHER/03_Threat_Actors/G1001 - HEXANE|HEXANE]] :contentReference[oaicite:29]{index=29}  
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]] :contentReference[oaicite:30]{index=30}  
- [[30_CIPHER/03_Threat_Actors/G0065 - Leviathan|Leviathan]] :contentReference[oaicite:31]{index=31}  
- [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]] :contentReference[oaicite:32]{index=32}  

## 10. Campaign Usage
- C0022 - Operation Dream Job :contentReference[oaicite:33]{index=33}  

## 11. Malware Usage
None explicitly captured in this note.

## 12. Mitigations
MITRE notes this technique is not easily mitigated purely with preventive controls because it abuses legitimate features and trusted relationships. :contentReference[oaicite:34]{index=34}  
Practical risk reduction measures:
- MFA + conditional access + device trust
- email/collaboration phishing protections (safe links/attachments)
- macro hardening and attachment sandboxing
- user reporting workflows + automated quarantine

## 13. Testing & Validation
- **Tabletop test:** simulate “internal sender compromised” workflow; validate mass-quarantine and token revocation.
- **Detection test:** generate benign internal messages vs. internal messages with macro-enabled attachments in a lab; verify chain detection (sender anomaly → delivery → click/execution).
- **Purple-team drill:** collaboration platform link delivery + click tracking + follow-on sign-in anomalies (no payload execution required).

## 14. References
- MITRE ATT&CK. (2025, October 24). *Internal Spearphishing (T1534).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1534/ :contentReference[oaicite:35]{index=35}  
- Boutin, J. (2020, June 11). *Gamaredon group grows its game.* WeLiveSecurity (ESET). https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/ :contentReference[oaicite:36]{index=36}  
- Microsoft Threat Intelligence. (2023, August 2). *Midnight Blizzard conducts targeted social engineering over Microsoft Teams.* Microsoft. https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/ :contentReference[oaicite:37]{index=37}  

## 15. Notes
- Treat internal-to-internal phishing as a first-class detection problem; internal trust is the adversary’s advantage.
