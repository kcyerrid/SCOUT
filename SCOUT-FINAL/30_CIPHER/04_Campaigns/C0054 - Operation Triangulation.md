---
scoutcam_id: C0054
entity_type: campaign
campaign_id: C0054
campaign_name: "Operation Triangulation"
aliases:
  - "Operation Triangulation"
first_observed: 2019-01
last_observed: 2023-06
campaign_status: concluded
risk_level: critical
confidence: high
primary_objectives:
  - espionage_like
  - mobile_surveillance
target_sectors: []
target_regions: []
associated_actors: []
suspected_actors: []
associated_malware:
  - "[[30_CIPHER/05_Malware/S1216 - TriangleDB|TriangleDB (S1216)]]"
associated_tools:
  - "[[30_CIPHER/05_Malware/S1215 - Binary Validator|Binary Validator (S1215)]]"
associated_ttps:
  - "[[20_Entities/07_TTPs/T1658 - Exploitation for Client Execution|T1658 - Exploitation for Client Execution]]"
  - "[[20_Entities/07_TTPs/T1404 - Exploitation for Privilege Escalation|T1404 - Exploitation for Privilege Escalation]]"
  - "[[20_Entities/07_TTPs/T1437 - Application Layer Protocol|T1437 - Application Layer Protocol]]"
  - "[[20_Entities/07_TTPs/T1544 - Ingress Tool Transfer|T1544 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1634.001 - Keychain|T1634.001 - Keychain]]"
  - "[[20_Entities/07_TTPs/T1521.001 - Symmetric Cryptography|T1521.001 - Symmetric Cryptography]]"
  - "[[20_Entities/07_TTPs/T1521.002 - Asymmetric Cryptography|T1521.002 - Asymmetric Cryptography]]"
  - "[[20_Entities/07_TTPs/T1630 - Indicator Removal on Host|T1630 - Indicator Removal on Host]]"
  - "[[20_Entities/07_TTPs/T1630.002 - File Deletion|T1630.002 - File Deletion]]"
  - "[[20_Entities/07_TTPs/T1430 - Location Tracking|T1430 - Location Tracking]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0054/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - mobile
  - ios
  - zero-click
---

## Overview
Operation Triangulation (C0054) is a mobile campaign targeting iOS devices and deploying [[30_CIPHER/05_Malware/S1216 - TriangleDB|TriangleDB (S1216)]], with an execution chain that includes validators such as [[30_CIPHER/05_Malware/S1215 - Binary Validator|Binary Validator (S1215)]]. The campaign is characterized by zero-click exploitation for initial access via iMessage attachments, followed by privilege escalation and extensive data collection/exfiltration behaviors.

## Linked Associations
### Malware / Tools
- [[30_CIPHER/05_Malware/S1216 - TriangleDB|TriangleDB (S1216)]]
- [[30_CIPHER/05_Malware/S1215 - Binary Validator|Binary Validator (S1215)]]

### TTPs (ATT&CK Mobile)
- [[20_Entities/07_TTPs/T1658 - Exploitation for Client Execution|T1658 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1404 - Exploitation for Privilege Escalation|T1404 - Exploitation for Privilege Escalation]]
- [[20_Entities/07_TTPs/T1437 - Application Layer Protocol|T1437 - Application Layer Protocol]]
- [[20_Entities/07_TTPs/T1544 - Ingress Tool Transfer|T1544 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1634.001 - Keychain|T1634.001 - Keychain]]
- [[20_Entities/07_TTPs/T1521.001 - Symmetric Cryptography|T1521.001 - Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1521.002 - Asymmetric Cryptography|T1521.002 - Asymmetric Cryptography]]
- [[20_Entities/07_TTPs/T1630 - Indicator Removal on Host|T1630 - Indicator Removal on Host]]
- [[20_Entities/07_TTPs/T1630.002 - File Deletion|T1630.002 - File Deletion]]
- [[20_Entities/07_TTPs/T1430 - Location Tracking|T1430 - Location Tracking]]

## Detection Opportunities
- Indicators of iMessage zero-click exploitation are often sparse; prioritize endpoint integrity telemetry, anomalous process behavior, and unexpected network egress over HTTPS consistent with [[20_Entities/07_TTPs/T1437 - Application Layer Protocol|T1437 - Application Layer Protocol]].
- Watch for deletion of initial exploitation artifacts consistent with [[20_Entities/07_TTPs/T1630.002 - File Deletion|T1630.002 - File Deletion]].

## Notes
- Canonical vault links for Tools/Malware/TTPs have been restored to the master prompt format.
