---
entity_type: threat_actor
actor_name: "Scattered Spider"
common_name: "Scattered Spider"
actor_id: ""
actor_type: "Cybercrime / intrusion set (social-engineering-led)"
aliases: ["UNC3944", "Octo Tempest"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: ""
last_seen: ""
status: "Active (reported)"
motivations: ["Financial gain"]
objectives: ["Obtain initial access via social engineering and credential theft", "Abuse identity systems (SSO/MFA/helpdesk workflows) to expand access", "Steal sensitive data for extortion leverage", "Enable follow-on monetization via ransomware deployment (reported in some incidents)"]
victimology_summary: "Scattered Spider is commonly described in public reporting as a cybercriminal intrusion set notable for high-success social engineering (including helpdesk impersonation and identity-workflow abuse) to obtain and expand access, often prioritizing identity providers, privileged accounts, and remote access pathways. Reporting links the cluster to data theft and extortion operations, and in some incidents to ransomware deployment via partnerships/affiliations with ransomware operators. Target selection is frequently described as opportunistic but focused on organizations with high extortion leverage and complex identity environments."
target_sectors: ["Technology/IT services", "Telecommunications (reported)", "Hospitality & Gaming (reported)", "Retail (reported)", "Financial services (reported)"]
target_regions: ["United States (reported)", "United Kingdom (reported)", "Global"]
related_groups: ["ALPHV/BlackCat (reported collaboration/affiliate relationship in some incidents)"]
malware: ["[[30_CIPHER/05_Malware/ALPHV]]", "[[30_CIPHER/05_Malware/BlackCat]]"]
tools: ["[[30_CIPHER/05_Malware/AnyDesk]]", "[[30_CIPHER/05_Malware/TeamViewer]]", "[[30_CIPHER/05_Malware/ScreenConnect]]", "[[30_CIPHER/05_Malware/Splashtop]]", "[[30_CIPHER/05_Malware/Mimikatz]]"]
infrastructure: ["[[Vishing]]", "[[Helpdesk impersonation]]", "[[MFA fatigue]]", "[[SSO abuse]]", "[[SIM swapping]]", "[[Remote Monitoring and Management]]", "[[Living-off-the-land]]", "[[Data theft for extortion]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]", "[[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing via Service]]", "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]", "[[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]]", "[[20_Entities/07_TTPs/T1110 - Brute Force]]", "[[20_Entities/07_TTPs/T1621 - Multi-Factor Authentication Request Generation]]", "[[20_Entities/07_TTPs/T1098 - Account Manipulation]]", "[[20_Entities/07_TTPs/T1133 - External Remote Services]]", "[[20_Entities/07_TTPs/T1219 - Remote Access Tools]]", "[[20_Entities/07_TTPs/T1528 - Steal Application Access Token]]", "[[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]", "[[20_Entities/07_TTPs/T1087 - Account Discovery]]", "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]", "[[20_Entities/07_TTPs/T1567.002 - Exfiltration to Cloud Storage: Exfiltration to Cloud Storage]]", "[[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]"]
notable_claims: []
intel_sources: ["Mandiant — UNC3944 / Scattered Spider reporting (https://www.mandiant.com/resources/blog)","Microsoft Security — Octo Tempest reporting (https://www.microsoft.com/en-us/security/blog/)","CISA/USG advisories referencing Scattered Spider-style intrusions in critical sectors (https://www.cisa.gov/news-events/cybersecurity-advisories)","UK NCSC guidance and threat updates on social-engineering-enabled intrusions (https://www.ncsc.gov.uk/section/keep-up-to-date/all-blogs)","MITRE ATT&CK technique references (https://attack.mitre.org/)"]
tags: ["threat-actor", "scattered-spider", "unc3944", "octo-tempest", "cybercrime", "social-engineering", "identity-compromise", "extortion"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

# Scattered Spider

## 1. BLUF / Executive Summary
Scattered Spider is a cybercriminal intrusion set widely characterized by **social-engineering-led initial access** and **identity-system abuse** (helpdesk impersonation, SSO/MFA workflow manipulation, and privileged account takeover). Public reporting links the group to **data theft and extortion** and, in some incidents, to **ransomware deployment** through collaboration/affiliate relationships with ransomware operators. The most distinctive operational theme is prioritizing identity control planes and remote access pathways rather than exploiting complex malware-only intrusion chains.

## 2. Attribution Notes
- “Scattered Spider” is a **cross-vendor cluster label**; common tracking names include **UNC3944** (Mandiant) and **Octo Tempest** (Microsoft). Clustering boundaries can vary by vendor dataset and time period.
- Public attribution generally treats this actor as a **criminal** intrusion set, not a state-sponsored group, with tradecraft heavily centered on human-driven access operations.
- Some high-profile incidents are publicly discussed as Scattered Spider-linked, but incident-to-actor linkage can be uneven across sources; this note uses conservative phrasing where public reporting diverges.

## 3. Motivations & Objectives
- **Motivation:** Financial gain via extortion and follow-on monetization.
- **Objectives:** Gain initial access through identity compromise, expand privileges, steal high-value data, and create leverage for extortion; in some cases, enable ransomware deployment by a partner/affiliate ecosystem.

## 4. Targeting Profile
- **Victim profile:** Organizations with high extortion leverage, complex identity environments, and extensive remote access footprints.
- **Sectors (reported):** Technology/IT services, telecommunications, hospitality & gaming, retail, and other enterprises with high operational impact potential.
- **Regions (reported):** Strong presence in U.S./U.K. victim reporting, with broader global victimology described.

## 5. Tradecraft Overview
- **Initial access (identity-first):** Credential theft and identity-provider targeting using link-based phishing and service-based credential collection consistent with [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]] and [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing via Service]].
- **Human-driven escalation:** Helpdesk/social-engineering to reset credentials and enroll attacker-controlled authentication factors; behaviors frequently align with account takeover and workflow abuse rather than exploit-heavy entry.
- **MFA/SSO pressure tactics:** Reported MFA fatigue patterns consistent with [[20_Entities/07_TTPs/T1621 - Multi-Factor Authentication Request Generation]] and subsequent use of compromised cloud identities consistent with [[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]].
- **Remote access enablement:** Use of commercial remote access and RMM tools consistent with [[20_Entities/07_TTPs/T1219 - Remote Access Tools]] and [[20_Entities/07_TTPs/T1133 - External Remote Services]].
- **Credential and token leverage:** Credential dumping and token/session abuse consistent with [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]] and [[20_Entities/07_TTPs/T1528 - Steal Application Access Token]].
- **Extortion pipeline:** Data theft and exfiltration to cloud storage in support of leverage, consistent with [[20_Entities/07_TTPs/T1567.002 - Exfiltration to Cloud Storage: Exfiltration to Cloud Storage]]; ransomware impact is reported in some incidents consistent with [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Spearphishing via Service]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]]
- [[20_Entities/07_TTPs/T1110 - Brute Force]]
- [[20_Entities/07_TTPs/T1621 - Multi-Factor Authentication Request Generation]]
- [[20_Entities/07_TTPs/T1098 - Account Manipulation]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1219 - Remote Access Tools]]
- [[20_Entities/07_TTPs/T1528 - Steal Application Access Token]]
- [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]
- [[20_Entities/07_TTPs/T1087 - Account Discovery]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1567.002 - Exfiltration to Cloud Storage: Exfiltration to Cloud Storage]]
- [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]

## 7. Malware & Tools Used
**Ransomware ecosystem (reported in some incidents)**
- [[30_CIPHER/05_Malware/ALPHV]]
- [[30_CIPHER/05_Malware/BlackCat]]

**Remote access / operator tooling (commonly reported across identity-led intrusions)**
- [[30_CIPHER/05_Malware/AnyDesk]]
- [[30_CIPHER/05_Malware/TeamViewer]]
- [[30_CIPHER/05_Malware/ScreenConnect]]
- [[30_CIPHER/05_Malware/Splashtop]]

**Credential tooling (reported in some cases)**
- [[30_CIPHER/05_Malware/Mimikatz]]

## 8. Infrastructure Patterns
- [[Vishing]] and [[Helpdesk impersonation]] as a primary enablement layer for credential resets and authentication-factor manipulation.
- [[SIM swapping]] (reported) as a facilitator for intercepting authentication channels in some victim narratives.
- Heavy reliance on enterprise identity infrastructure and third-party services ([[SSO abuse]], [[Remote Monitoring and Management]]) to minimize custom malware dependency.
- [[Data theft for extortion]] patterns including use of common cloud storage for staging/exfiltration.

## 9. Campaign History
- **2022 (reported):** Multiple sources describe a wave of identity-provider–centric intrusions and large-scale credential-harvesting campaigns; some reporting links this activity to the broader Scattered Spider/UNC3944 cluster, though naming and clustering may vary by source.
- **2023 (reported):** Public reporting widely discusses major U.S. hospitality & gaming incidents in which social engineering and identity compromise were highlighted; some reporting links these to Scattered Spider/UNC3944 with follow-on extortion and ransomware outcomes.
- **2024 (reported):** Vendor reporting emphasizes ongoing evolution in identity compromise tradecraft (cloud accounts, token abuse, remote access tool usage), continuing the “identity-first” operational profile.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize identity-centric controls and monitoring aligned to [[20_Entities/07_TTPs/T1078 - Valid Accounts]] and [[20_Entities/07_TTPs/T1078.004 - Valid Accounts: Cloud Accounts]], especially for helpdesk password resets, MFA enrollment events, and privileged account changes.
- Treat unusual MFA prompt patterns consistent with [[20_Entities/07_TTPs/T1621 - Multi-Factor Authentication Request Generation]] as high-signal when correlated with new device registrations, password resets, or anomalous sign-ins.
- Increase governance and detection around remote access tooling consistent with [[20_Entities/07_TTPs/T1219 - Remote Access Tools]] and [[20_Entities/07_TTPs/T1133 - External Remote Services]] (focus on unexpected installs, first-time usage, and abnormal session contexts).
- Expand detection for token/session misuse aligned to [[20_Entities/07_TTPs/T1528 - Steal Application Access Token]] and for suspicious exfiltration aligned to [[20_Entities/07_TTPs/T1567.002 - Exfiltration to Cloud Storage: Exfiltration to Cloud Storage]].
- Maintain preparedness for extortion/ransomware outcomes where relevant to your risk model, aligned to [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]].

## 12. Analyst Notes
- This actor’s defining characteristic in public reporting is **human-driven access operations** rather than unique malware; many “tools” are legitimate remote access utilities, which complicates indicator-based detections.
- Alias boundaries (UNC3944 vs. Octo Tempest vs. related clusters) may differ across vendors; retain ambiguity where sources do not explicitly equate labels.
- Ransomware linkage is best represented as “reported collaboration/affiliate relationship in some incidents” rather than an always-on intrinsic capability.

## 13. Further Reading / External Resources
- Microsoft Security Blog (Octo Tempest): https://www.microsoft.com/en-us/security/blog/
- Mandiant blog resources (UNC3944 / Scattered Spider): https://www.mandiant.com/resources/blog
- CISA Cybersecurity Advisories: https://www.cisa.gov/news-events/cybersecurity-advisories
- UK NCSC blogs and updates: https://www.ncsc.gov.uk/section/keep-up-to-date/all-blogs
- MITRE ATT&CK (techniques): https://attack.mitre.org/

## 14. References
- Microsoft Security Blog — Octo Tempest reporting hub: https://www.microsoft.com/en-us/security/blog/
- Mandiant — Resources and reporting hub (UNC3944/Scattered Spider references appear in relevant posts): https://www.mandiant.com/resources/blog
- CISA — Cybersecurity Advisories (Scattered Spider-style identity compromise guidance appears across relevant advisories): https://www.cisa.gov/news-events/cybersecurity-advisories
- UK NCSC — Keep up to date (identity and social-engineering intrusion guidance): https://www.ncsc.gov.uk/section/keep-up-to-date/all-blogs
- MITRE ATT&CK — Technique reference library: https://attack.mitre.org/
