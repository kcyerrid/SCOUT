---
scoutcam_id: C0050
entity_type: campaign
campaign_id: C0050
campaign_name: "J-magic Campaign"
aliases:
  - "J-magic Campaign"
first_observed: 2023-06
last_observed: 2024-06
campaign_status: concluded
risk_level: high
confidence: medium
primary_objectives:
  - espionage_like
  - network_device_access
target_sectors:
  - semiconductor
  - energy
  - manufacturing
  - IT
target_regions: []
associated_actors: []
suspected_actors: []
associated_malware:
  - "[[30_CIPHER/05_Malware/S1203 - J-magic|J-magic (S1203)]]"
associated_tools: []
associated_ttps:
  - "[[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]"
  - "[[20_Entities/07_TTPs/T1587.003 - Digital Certificates|T1587.003 - Digital Certificates]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1588.001 - Malware|T1588.001 - Malware]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0050/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - network-devices
  - juniper
---

## Overview
J-magic Campaign (C0050) targeted Junos OS routers used as VPN gateways and leveraged a custom cd00r-variant backdoor identified as [[30_CIPHER/05_Malware/S1203 - J-magic|J-magic (S1203)]]. Activity is described as spanning June 2023 through at least June 2024, with targeting concentrated in semiconductor, energy, manufacturing, and IT sectors.

## Linked Associations
### Threat Actors
- (No ATT&CK Group explicitly linked to C0050)

### Malware / Tools
- [[30_CIPHER/05_Malware/S1203 - J-magic|J-magic (S1203)]]

### TTPs (ATT&CK)
- [[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]
- [[20_Entities/07_TTPs/T1587.003 - Digital Certificates|T1587.003 - Digital Certificates]]
- [[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1588.001 - Malware|T1588.001 - Malware]]

## Detection Opportunities
- Monitor Junos OS devices for unexpected services/process names mimicking legitimate Junos components (e.g., masquerade patterns consistent with [[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]).
- Inspect management-plane telemetry and outbound connections from VPN gateways to VPS infrastructure (pivot on [[20_Entities/07_TTPs/T1583.003 - Virtual Private Server|T1583.003 - Virtual Private Server]]).

## Notes
- This note focuses on restoring canonical vault links for TTPs / Malware / Actors. For deeper infra/IOC pivots, use the campaign source in `intel_sources`.
