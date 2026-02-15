---
entity_type: campaign
campaign_name: Juicy Mix
campaign_id: C0044
first_seen: 2022-01
last_seen: 2022-12
suspected_attribution: Iran-aligned cyber-espionage
associated_actors:
  - "[[30_CIPHER/02_Actors/G0049 - OilRig|OilRig (G0049)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1169 - Mango|Mango (S1169)]]"
target_geography:
  - Israel
target_sectors:
  - Israeli organizations (including healthcare/government-adjacent per reporting context)
goals:
  - Espionage; credential theft; data collection and exfiltration
intel_sources:
  - https://attack.mitre.org/campaigns/C0044/
  - https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/
---

# Juicy Mix (C0044)

## Executive synopsis
A 2022 campaign attributed to OilRig targeting Israeli organizations, delivering the Mango backdoor via VBS droppers and leveraging a set of post-compromise stealers to harvest browser data and credentials.

## Timeline (high level)
- 2022-01: First observed activity
- 2022-12: Last observed activity

## Initial access & delivery
- Likely spearphishing-delivered droppers (VBS) used to install Mango.
- Use of compromised legitimate Israeli websites as C2 / staging infrastructure (reported).

## Tradecraft (ATT&CK highlights)
- Execution:
  - Visual Basic (VBS) droppers
  - PowerShell used for credential theft
- Persistence:
  - Scheduled tasks created by droppers
- Credential access & collection:
  - Browser data and credential dumpers (Chrome/Edge)
  - Windows Credential Manager theft
- C2 / infra:
  - HTTP POST registration beacons; base64-encoded host identifiers
  - Compromised site used as C2 server

## Malware / tooling
- Mango (S1169): C#/.NET backdoor with obfuscation, used as the campaign’s core implant.
- Post-compromise stealers:
  - Browser cookie/history/credential dumpers
  - Windows Credential Manager stealer

## IOC / artifact summary (starter set)
- Host artifacts:
  - %TEMP% staging: files named like Cupdate / Eupdate / IUpdate (reported pattern)
  - Scheduled task entries tied to VBS droppers
- Network:
  - HTTP POST “registration” traffic to a compromised legitimate domain
  - Suspicious base64 blobs carrying host identifiers

## Detection & hunting (practical)
- Email + endpoint:
  - Block/flag VBS attachments and abnormal WScript/CScript spawning
  - Correlate VBS → task creation → .NET execution chains
- Credential theft:
  - Monitor access to browser credential stores and Credential Manager APIs
- Web proxy:
  - Detect unusual POST beacons to legitimate-but-compromised Israeli portals; validate with web reputation + change history

## Risks & implications
- High credential risk due to broad browser and Credential Manager harvesting.
- Compromised legitimate infrastructure reduces efficacy of simplistic domain-blocking.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0044 - Juicy Mix|Juicy Mix (C0044)]]
- Actor: [[30_CIPHER/02_Actors/G0049 - OilRig|OilRig (G0049)]]
- Malware: [[30_CIPHER/05_Malware/S1169 - Mango|Mango (S1169)]]

## Recommended OSINT queries
- "C0044 Juicy Mix Mango S1169"
- "OilRig Juicy Mix 2022 Mango VBS dropper"
- "ESET Juicy Mix compromised Israeli job portal C2"
- "CDumper EDumper OilRig Juicy Mix"

## Confidence
High on attribution to OilRig and Mango usage (strong single-source technical writeup + ATT&CK mapping); Medium on victim scope beyond what’s publicly described.

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
