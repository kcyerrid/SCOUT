---
scoutcam_id: C0053
entity_type: campaign
campaign_id: C0053
campaign_name: "FLORAHOX Activity"
aliases:
  - "FLORAHOX Activity"
first_observed: 2019-01
last_observed: 2024-05
campaign_status: unknown
risk_level: high
confidence: medium
primary_objectives:
  - espionage_like
  - infrastructure_obfuscation
target_sectors: []
target_regions: []
associated_actors: []
suspected_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0128 - ZIRCONIUM|ZIRCONIUM (G0128)]]"
associated_malware: []
associated_tools:
  - "[[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]"
associated_ttps:
  - "[[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]"
  - "[[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter|T1059 - Command and Scripting Interpreter]]"
  - "[[20_Entities/07_TTPs/T1059.004 - Unix Shell|T1059.004 - Unix Shell]]"
  - "[[20_Entities/07_TTPs/T1584.008 - Network Devices|T1584.008 - Network Devices]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0053/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - orb
  - tor
  - proxy-infrastructure
---

## Overview
FLORAHOX Activity (C0053) describes a hybrid ORB network that blends compromised end-of-life routers/IoT with leased VPS infrastructure to proxy malicious traffic. ATT&CK notes the infrastructure has been leveraged by multiple actors, including [[30_CIPHER/03_Threat_Actors/G0128 - ZIRCONIUM|ZIRCONIUM (G0128)]], and highlights use of customized [[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]] routing layers.

## Linked Associations
### Threat Actors (Suspected / Leveraging)
- [[30_CIPHER/03_Threat_Actors/G0128 - ZIRCONIUM|ZIRCONIUM (G0128)]]

### Tools
- [[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]

### TTPs (ATT&CK)
- [[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]
- [[20_Entities/07_TTPs/T1584.008 - Network Devices|T1584.008 - Network Devices]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]
- [[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter|T1059 - Command and Scripting Interpreter]]
- [[20_Entities/07_TTPs/T1059.004 - Unix Shell|T1059.004 - Unix Shell]]

## Detection Opportunities
- Router/IoT recruitment patterns and exploitation traces aligned to [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]].
- Multi-hop proxy routing and Tor usage consistent with [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]] and [[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]].

## Notes
- Actor linkage is modeled as “leveraging/suspected” because FLORAHOX is described as shared ORB infrastructure used by multiple actors.
