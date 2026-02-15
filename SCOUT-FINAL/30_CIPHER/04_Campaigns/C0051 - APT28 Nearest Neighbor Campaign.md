---
scoutcam_id: C0051
entity_type: campaign
campaign_id: C0051
campaign_name: "APT28 Nearest Neighbor Campaign"
aliases:
  - "APT28 Nearest Neighbor Campaign"
first_observed: 2022-02
last_observed: 2024-11
campaign_status: unknown
risk_level: high
confidence: high
primary_objectives:
  - espionage_like
  - long_term_access
target_sectors: []
target_regions: []
associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]"
suspected_actors: []
associated_malware: []
associated_tools:
  - "[[30_CIPHER/05_Malware/S1205 - cipher.exe|cipher.exe (S1205)]]"
  - "[[30_CIPHER/05_Malware/S0108 - netsh|netsh (S0108)]]"
associated_ttps:
  - "[[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001 - Archive via Utility]]"
  - "[[20_Entities/07_TTPs/T1110.003 - Password Spraying|T1110.003 - Password Spraying]]"
  - "[[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001 - PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003 - Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1584 - Compromise Infrastructure|T1584 - Compromise Infrastructure]]"
  - "[[20_Entities/07_TTPs/T1074.001 - Local Data Staging|T1074.001 - Local Data Staging]]"
  - "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information|T1140 - Deobfuscate/Decode Files or Information]]"
  - "[[20_Entities/07_TTPs/T1006 - Direct Volume Access|T1006 - Direct Volume Access]]"
  - "[[20_Entities/07_TTPs/T1561.001 - Disk Content Wipe|T1561.001 - Disk Content Wipe]]"
  - "[[20_Entities/07_TTPs/T1567 - Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]"
  - "[[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]]"
  - "[[20_Entities/07_TTPs/T1003.002 - Security Account Manager|T1003.002 - Security Account Manager]]"
  - "[[20_Entities/07_TTPs/T1003.003 - NTDS|T1003.003 - NTDS]]"
  - "[[20_Entities/07_TTPs/T1090.001 - Internal Proxy|T1090.001 - Internal Proxy]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]"
  - "[[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]"
  - "[[20_Entities/07_TTPs/T1016.002 - Wi-Fi Discovery|T1016.002 - Wi-Fi Discovery]]"
  - "[[20_Entities/07_TTPs/T1669 - Wi-Fi Networks|T1669 - Wi-Fi Networks]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0051/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - apt28
  - wifi
  - nearest-neighbor
---

## Overview
APT28 Nearest Neighbor Campaign (C0051) is attributed to [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]] and describes an intrusion pattern that leverages Wi-Fi networks in close physical proximity to the intended target, combined with credential acquisition and living-off-the-land activity.

## Linked Associations
### Threat Actors
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28 (G0007)]]

### Malware / Tools
- [[30_CIPHER/05_Malware/S1205 - cipher.exe|cipher.exe (S1205)]]
- [[30_CIPHER/05_Malware/S0108 - netsh|netsh (S0108)]]

### TTPs (ATT&CK)
- [[20_Entities/07_TTPs/T1110.003 - Password Spraying|T1110.003 - Password Spraying]]
- [[20_Entities/07_TTPs/T1016.002 - Wi-Fi Discovery|T1016.002 - Wi-Fi Discovery]]
- [[20_Entities/07_TTPs/T1669 - Wi-Fi Networks|T1669 - Wi-Fi Networks]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1003.002 - Security Account Manager|T1003.002 - Security Account Manager]]
- [[20_Entities/07_TTPs/T1003.003 - NTDS|T1003.003 - NTDS]]
- [[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001 - Archive via Utility]]
- [[20_Entities/07_TTPs/T1567 - Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]
- [[20_Entities/07_TTPs/T1561.001 - Disk Content Wipe|T1561.001 - Disk Content Wipe]]
- [[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]]
- [[20_Entities/07_TTPs/T1090.001 - Internal Proxy|T1090.001 - Internal Proxy]]

## Detection Opportunities
- Password-spray telemetry aligned to [[20_Entities/07_TTPs/T1110.003 - Password Spraying|T1110.003 - Password Spraying]] with subsequent Wi-Fi auth events.
- RDP lateral movement + registry hive access and staging consistent with [[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]] and [[20_Entities/07_TTPs/T1074.001 - Local Data Staging|T1074.001 - Local Data Staging]].
- Anti-forensics signals involving [[30_CIPHER/05_Malware/S1205 - cipher.exe|cipher.exe (S1205)]] and firewall modification consistent with [[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]].

## Notes
- Canonical vault links for Actor / Tools / TTPs have been normalized to the master prompt format.
