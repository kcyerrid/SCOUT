---
entity_type: threat_actor
actor_name: "Silent Librarian"
common_name: "Silent Librarian"
actor_id: "G0122"
actor_type: ""
aliases:
  - "TA407"
  - "COBALT DICKENS"
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: ""
first_seen: ""
last_seen: ""
status: ""

motivations: []
objectives:
  - "Credential harvesting against webmail/SSO"
  - "Mailbox access and bulk email theft"
  - "Account takeover and persistence via forwarding rules"
victimology_summary: "Threat group tracked as Silent Librarian (a.k.a. TA407 / COBALT DICKENS) that conducts credential harvesting and account compromise, including password spraying, establishing email accounts for forwarding, and exfiltrating full mailboxes from compromised victims."
target_sectors: []
target_regions: []

related_groups: []

malware: []
tools: []

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains|T1583.001 - Acquire Infrastructure: Domains]]"
  - "[[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying|T1110.003 - Brute Force: Password Spraying]]"
  - "[[20_Entities/07_TTPs/T1114 - Email Collection|T1114 - Email Collection]]"
  - "[[20_Entities/07_TTPs/T1114.003 - Email Collection: Email Forwarding Rule|T1114.003 - Email Collection: Email Forwarding Rule]]"
  - "[[20_Entities/07_TTPs/T1585.002 - Establish Accounts: Email Accounts|T1585.002 - Establish Accounts: Email Accounts]]"
  - "[[20_Entities/07_TTPs/T1589.002 - Gather Victim Identity Information: Email Addresses|T1589.002 - Gather Victim Identity Information: Email Addresses]]"
  - "[[20_Entities/07_TTPs/T1589.003 - Gather Victim Identity Information: Employee Names|T1589.003 - Gather Victim Identity Information: Employee Names]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool|T1588.002 - Obtain Capabilities: Tool]]"
  - "[[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link|T1598.003 - Phishing for Information: Spearphishing Link]]"
  - "[[20_Entities/07_TTPs/T1594 - Search Victim-Owned Websites|T1594 - Search Victim-Owned Websites]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0122/"
  - "https://www.justice.gov/"
  - "https://www.proofpoint.com/"
  - "https://www.secureworks.com/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0122"
  - "credential_harvesting"
  - "email_compromise"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Silent Librarian (G0122) is tracked for **credential-harvesting and email-account compromise** operations, including **domain acquisition for spoofed login pages**, **password spraying**, **mailbox exfiltration**, and **persistence via forwarding rules**. Their activity is highly relevant to SOC teams due to strong detection surface in **identity and mail telemetry** rather than malware-heavy endpoint artifacts.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0122
- **Aliases (ATT&CK):** TA407, COBALT DICKENS
- **Country/sponsor:** Not explicitly stated on the ATT&CK Group page.

## 3. Motivations & Objectives
- Motivations not explicitly stated by ATT&CK.
- Operational objectives (as evidenced by ATT&CK techniques): credential capture, account takeover, and sustained mailbox access.

## 4. Targeting Profile
- ATT&CK examples indicate targeted organizations are selected and researched, including collection of employee names/emails and reconnaissance of victim-owned web properties.

## 5. Tradecraft Overview
- **Prep & recon:** harvest employee identities and email formats; search victim-owned websites for context and entry points.
- **Infrastructure:** acquire spoofed domains for credential harvesting pages.
- **Access:** password spraying against private-sector targets; phishing-for-information via links to fake login pages.
- **Persistence & collection:** establish email accounts to receive forwarded mail; exfiltrate full mailboxes.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains|T1583.001 - Acquire Infrastructure: Domains]]
- [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing Link|T1598.003 - Phishing for Information: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying|T1110.003 - Brute Force: Password Spraying]]
- [[20_Entities/07_TTPs/T1114 - Email Collection|T1114 - Email Collection]]
- [[20_Entities/07_TTPs/T1114.003 - Email Collection: Email Forwarding Rule|T1114.003 - Email Collection: Email Forwarding Rule]]
- [[20_Entities/07_TTPs/T1585.002 - Establish Accounts: Email Accounts|T1585.002 - Establish Accounts: Email Accounts]]
- [[20_Entities/07_TTPs/T1589.002 - Gather Victim Identity Information: Email Addresses|T1589.002 - Gather Victim Identity Information: Email Addresses]]
- [[20_Entities/07_TTPs/T1589.003 - Gather Victim Identity Information: Employee Names|T1589.003 - Gather Victim Identity Information: Employee Names]]
- [[20_Entities/07_TTPs/T1594 - Search Victim-Owned Websites|T1594 - Search Victim-Owned Websites]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool|T1588.002 - Obtain Capabilities: Tool]]

## 7. Malware & Tools Used
- Silent Librarian operations are commonly identity/mail-centric; specific malware/software mappings (S####) were not captured in the extracted material for this note.

## 8. Infrastructure Patterns
- **Lookalike domain acquisition** for credential harvesting.
- **Web-based phishing funnels** that mimic enterprise SSO and email login pages.

## 9. Campaign History
- ATT&CK documents multiple activity examples tied to password spraying, mailbox exfiltration, and forwarding-rule persistence.

## 10. Known Indicators
- **Identity & email telemetry anchors:**
  - Password spray bursts (low-and-slow across many accounts) with consistent IP ranges / user agents.
  - New or unusual email forwarding rules, especially to external domains.
  - Unusual mailbox export / IMAP/Graph/API access at scale.
  - Newly registered lookalike domains resembling org branding and login flows.

## 11. Defensive Recommendations
- **Identity:** enforce MFA (phishing-resistant where possible); rate-limit and block password spraying; implement smart lockouts and conditional access.
- **Mail security:** disable auto-forwarding to external domains where feasible; alert on new forwarding rules; monitor mailbox export operations.
- **Brand protection:** track lookalike domains; takedown credential harvesting sites rapidly.
- **User defense:** continuous phishing awareness focused on SSO lookalikes.

## 12. Analyst Notes
- Silent Librarian detection is strongest in **IdP + email platform** logs, not endpoint EDR alone. Correlate with domain-registration monitoring.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0122/
- DOJ (public reporting portal): https://www.justice.gov/
- Proofpoint research portal: https://www.proofpoint.com/
- Secureworks research portal: https://www.secureworks.com/

## 14. References
- MITRE ATT&CK. (n.d.). *Silent Librarian (G0122).* https://attack.mitre.org/groups/G0122/
- U.S. Department of Justice. (n.d.). *Justice.gov (public portal).* https://www.justice.gov/
- Proofpoint. (n.d.). *Proofpoint (research portal).* https://www.proofpoint.com/
- Secureworks. (n.d.). *Secureworks (research portal).* https://www.secureworks.com/

## 15. Notes
- Build detections around **forwarding-rule creation**, **spray heuristics**, and **impossible travel / risky sign-in** signals.
