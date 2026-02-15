---
scoutcam_id: C0055
entity_type: campaign
campaign_id: C0055
campaign_name: "Quad7 Activity"
aliases:
  - "Quad7 Activity"
  - "CovertNetwork-1658"
  - "7777 Botnet"
first_observed: 2023-08
last_observed: 2025-08
campaign_status: active
risk_level: high
confidence: medium
primary_objectives:
  - access_brokering
  - credential_access
target_sectors:
  - government
  - NGOs
  - think-tanks
  - law
  - energy
  - IT
  - defense
target_regions:
  - North America
  - Europe
associated_actors: []
suspected_actors:
  - "[[Storm-0940]]"
associated_malware: []
associated_tools:
  - "[[30_CIPHER/05_Malware/S0095 - ftp|ftp (S0095)]]"
associated_ttps:
  - "[[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001 - Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1071.002 - File Transfer Protocols|T1071.002 - File Transfer Protocols]]"
  - "[[20_Entities/07_TTPs/T1110.003 - Password Spraying|T1110.003 - Password Spraying]]"
  - "[[20_Entities/07_TTPs/T1059.004 - Unix Shell|T1059.004 - Unix Shell]]"
  - "[[20_Entities/07_TTPs/T1584.005 - Botnet|T1584.005 - Botnet]]"
  - "[[20_Entities/07_TTPs/T1584.008 - Network Devices|T1584.008 - Network Devices]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1589.002 - Email Addresses|T1589.002 - Email Addresses]]"
  - "[[20_Entities/07_TTPs/T1665 - Hide Infrastructure|T1665 - Hide Infrastructure]]"
  - "[[20_Entities/07_TTPs/T1562.001 - Disable or Modify Tools|T1562.001 - Disable or Modify Tools]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1571 - Non-Standard Port|T1571 - Non-Standard Port]]"
  - "[[20_Entities/07_TTPs/T1027.011 - Fileless Storage|T1027.011 - Fileless Storage]]"
  - "[[20_Entities/07_TTPs/T1090.002 - External Proxy|T1090.002 - External Proxy]]"
  - "[[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0055/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - botnet
  - soho-routers
  - password-spraying
---

## Overview
Quad7 Activity (C0055) describes a SOHO router botnet used as rotating egress infrastructure for password-spraying and brute-force operations. ATT&CK notes downstream use of this infrastructure to obtain credentials later leveraged against organizations in North America and Europe.

## Linked Associations
### Threat Actors (Non-ATT&CK ID / Reported)
- [[Storm-0940]]

### Tools
- [[30_CIPHER/05_Malware/S0095 - ftp|ftp (S0095)]]

### TTPs (ATT&CK)
- [[20_Entities/07_TTPs/T1110.003 - Password Spraying|T1110.003 - Password Spraying]]
- [[20_Entities/07_TTPs/T1584.005 - Botnet|T1584.005 - Botnet]]
- [[20_Entities/07_TTPs/T1584.008 - Network Devices|T1584.008 - Network Devices]]
- [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]
- [[20_Entities/07_TTPs/T1665 - Hide Infrastructure|T1665 - Hide Infrastructure]]
- [[20_Entities/07_TTPs/T1571 - Non-Standard Port|T1571 - Non-Standard Port]]
- [[20_Entities/07_TTPs/T1027.011 - Fileless Storage|T1027.011 - Fileless Storage]]

## Detection Opportunities
- Look for throttled spray behavior aligned to [[20_Entities/07_TTPs/T1110.003 - Password Spraying|T1110.003 - Password Spraying]] (low-and-slow patterns, sparse attempts per account).
- Network device compromise signals consistent with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]] plus volatile artifact placement aligned to [[20_Entities/07_TTPs/T1027.011 - Fileless Storage|T1027.011 - Fileless Storage]].
- Egress anomalies: unusual SOCKS proxy creation consistent with [[20_Entities/07_TTPs/T1090.002 - External Proxy|T1090.002 - External Proxy]] and chained routing consistent with [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]].

## Notes
- Actor linking is provided as a generic vault link for Storm-0940 because it is not a canonical ATT&CK G#### entity.
