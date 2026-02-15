---
scoutcam_id: C0052
entity_type: campaign
campaign_id: C0052
campaign_name: "SPACEHOP Activity"
aliases:
  - "SPACEHOP Activity"
first_observed: 2019-01
last_observed: 2024-05
campaign_status: unknown
risk_level: high
confidence: medium
primary_objectives:
  - espionage_like
  - infrastructure_obfuscation
target_sectors: []
target_regions:
  - North America
  - Europe
  - Middle East
associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1023 - APT5|APT5 (G1023)]]"
  - "[[30_CIPHER/03_Threat_Actors/G0004 - Ke3chang|Ke3chang (G0004)]]"
suspected_actors: []
associated_malware: []
associated_tools: []
associated_ttps:
  - "[[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Tool|T1588.002 - Tool]]"
  - "[[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0052/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - orb
  - proxy-infrastructure
---

## Overview
SPACEHOP Activity (C0052) describes provisioned Operational Relay Box (ORB) infrastructure composed of commercially leased VPS, used to enable scanning and exploitation workflows and to proxy downstream operations. ATT&CK links this activity to use by [[30_CIPHER/03_Threat_Actors/G1023 - APT5|APT5 (G1023)]] and [[30_CIPHER/03_Threat_Actors/G0004 - Ke3chang|Ke3chang (G0004)]].

## Linked Associations
### Threat Actors
- [[30_CIPHER/03_Threat_Actors/G1023 - APT5|APT5 (G1023)]]
- [[30_CIPHER/03_Threat_Actors/G0004 - Ke3chang|Ke3chang (G0004)]]

### TTPs (ATT&CK)
- [[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1588.002 - Tool|T1588.002 - Tool]]
- [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]

## Detection Opportunities
- Identify VPS relay patterns consistent with [[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]] (especially chained proxy paths matching [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]).
- Exploitation telemetry on edge services consistent with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]].

## Notes
- This record normalizes the Actor/TTP link targets; SPACEHOP is best treated as enabling infrastructure rather than a single-actor intrusion set.
