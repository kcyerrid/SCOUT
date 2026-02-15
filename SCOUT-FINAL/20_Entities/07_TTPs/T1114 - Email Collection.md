---
entity_type: mitre_technique

technique_id: "T1114"
subtechnique_id: ""
technique_name: "Email Collection"

tactic:
  - TA0009 - Collection
platforms:
  - Linux
  - Office Suite
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear]]"
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]"
  - "[[30_CIPHER/03_Threat_Actors/G0122 - Silent Librarian|Silent Librarian]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]"
  - "[[30_CIPHER/05_Malware/S1201 - TRANSLATEXT|TRANSLATEXT]]"
associated_campaigns: []
related_techniques:
  - "T1114.001 - Local Email Collection"
  - "T1114.002 - Remote Email Collection"
  - "T1114.003 - Email Forwarding Rule"

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
Adversaries target user or organizational email to collect sensitive information (business data, credentials, communications, incident response details). Collection can occur locally on endpoints, remotely from email services, or via forwarding rules that silently copy mail to adversary-controlled destinations.

## 2. Technical Overview
Common collection avenues:
- **Local client artifacts**: email stores and databases (e.g., PST/OST, mbox/maildir, Mail.app databases), client caches, and attachments.
- **Remote service access**: mailboxes accessed via webmail, Exchange/Graph/EWS-like APIs, or administrative export features.
- **Forwarding/redirect rules**: inbox rules, transport rules, or client-side rules that automatically forward messages.

Behavioral anchors for defenders:
- Unexpected **mailbox-wide access** or **export actions**
- Creation/modification of **mail forwarding** rules
- Unusual **mail client access** patterns (new device/IP, atypical geolocation, anomalous user agent)
- Correlation between email activity and **process/file access** on endpoints (for local harvesting)

## 3. Subtechnique Considerations
- **T1114.001 (Local Email Collection)**: endpoint-focused; relies heavily on EDR file/process telemetry.
- **T1114.002 (Remote Email Collection)**: identity + SaaS audit logs are primary; watch for mailbox export/search, API access, and administrative cmdlets.
- **T1114.003 (Email Forwarding Rule)**: strongest signal when you can detect rule creation/changes and auto-forward headers or transport-rule actions.

## 4. Procedure Examples
Examples observed in ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]] searching Exchange for intrusion/IR-related emails.
- [[30_CIPHER/03_Threat_Actors/G0122 - Silent Librarian|Silent Librarian]] exfiltrating entire mailboxes.
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]] scraping email addresses from Outlook.
- [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear]] attempting to collect mail from accessed systems/servers.

## 5. Detection Guidance
Core strategy: detect **(a) email access/exfil behaviors** and **(b) rule-based persistence**, then correlate to identity and endpoint anomalies.

High-signal detections
- **Forwarding rule creation** or modification (user or admin), especially forwarding to external addresses.
- Presence of auto-forward indicators (e.g., headers associated with auto-forwarding in certain environments) correlated with suspicious sign-ins.
- **Mailbox export/search** activities performed by unusual accounts or from unusual IPs/devices.
- **Local harvesting indicators**: processes reading large volumes of email store files + network egress to external destinations.

Recommended correlations
- Identity: suspicious sign-in → mailbox operations → rule changes
- Endpoint: file access of email stores → compression/staging → outbound transfer
- Admin events: use of administrative cmdlets or delegated permissions shortly before mailbox access

### Data Source Notes
- Ensure coverage for:
  - SaaS/email audit logs (admin actions, mailbox access, rule changes)
  - Identity logs (MFA, risky sign-ins, device/geo changes)
  - Endpoint telemetry (file access to email stores, process lineage)

## 6. Response Guidance
1) **Contain**
- Disable suspicious forwarding and transport rules; block external forwarding where possible.
- Reset credentials, revoke sessions/tokens, enforce MFA for affected identities.

2) **Scope**
- Determine which mailboxes were accessed/exported, what searches/exports occurred, and whether additional mail routing was configured.
- Identify lateral access: delegated permissions, app consent, or admin role misuse.

3) **Remediate**
- Remove unauthorized mailbox delegates/app permissions.
- Enforce conditional access and restrict legacy authentication if present.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0009 - Collection/T1114.001 - Email Collection: Local Email Collection|T1114.001]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1114.002 - Email Collection: Remote Email Collection|T1114.002]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1114.003 - Email Collection: Email Forwarding Rule|T1114.003]]

## 8. SOC Relevance
- **High**: Email is a rich source of sensitive data and often contains IR/defense communications.
- This technique commonly overlaps with account takeover, OAuth abuse, and BEC tradecraft—treat rule creation and mailbox export as high-priority alerts.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1003 - Ember Bear|Ember Bear]]
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]
- [[30_CIPHER/03_Threat_Actors/G0122 - Silent Librarian|Silent Librarian]]

## 10. Campaign Usage
- None listed.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]
- [[30_CIPHER/05_Malware/S1201 - TRANSLATEXT|TRANSLATEXT]]

## 12. Mitigations
- **M1047 Audit**: Regularly audit forwarding/inbox/transport rules and mailbox access patterns.
- **M1041 Encrypt Sensitive Information**: Use encryption for sensitive email content where feasible.
- **M1032 Multi-factor Authentication**: Enforce MFA for webmail/admin access and reduce credential-only compromise.
- **M1060 Out-of-Band Communications Channel**: Use secure OOB verification for sensitive actions (password resets, financial changes) to reduce impact of email compromise.

## 13. Testing & Validation
- Validate alerting for:
  - rule creation/modification (user + admin),
  - mailbox export/search actions,
  - anomalous sign-ins followed by mailbox operations.
- Run table-top simulations:
  - “Compromised user creates forward-to-external rule”
  - “Admin role used to export mailbox data”
- Confirm detections include full context: mailbox, actor, IP/device, rule details, and affected messages.

## 14. References
- MITRE ATT&CK. (2025). *Email Collection (T1114)*. Retrieved 2026-01-01, from https://attack.mitre.org/techniques/T1114/
- Microsoft. (2015-06-08). *Exchange and Office 365: Mail Forwarding*. Retrieved 2026-01-01, from https://learn.microsoft.com/en-us/archive/blogs/timmcmic/exchange-and-office-365-mail-forwarding-2

## 15. Notes
- Treat newly-created forwarding rules to external domains as high severity unless explicitly approved by policy.
- Consider separate detections for “stealth forwarding” (hidden rules) versus standard rule creation.
