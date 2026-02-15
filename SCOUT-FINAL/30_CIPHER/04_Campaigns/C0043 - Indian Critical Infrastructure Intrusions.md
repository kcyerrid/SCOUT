---
entity_type: campaign
campaign_name: Indian Critical Infrastructure Intrusions
campaign_id: C0043
first_seen: 2021-01
last_seen: 2022-04
suspected_attribution: PRC (state-sponsored)
associated_actors:
  - "[[30_CIPHER/02_Actors/G1042 - RedEcho|RedEcho (G1042)]]"
suspected_actors:
  - TAG38 (industry tracking; not mapped to a MITRE Group ID on this campaign page)
associated_malware:
  - "[[30_CIPHER/05_Malware/S0596 - ShadowPad|ShadowPad (S0596)]]"
  - "[[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]"
target_geography:
  - India
target_sectors:
  - Electric utilities (IT networks)
  - Logistics
  - Potentially MSPs (India)
goals:
  - Strategic espionage / network mapping (IT-side), credential and infrastructure reconnaissance
intel_sources:
  - https://attack.mitre.org/campaigns/C0043/
  - https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf
  - https://go.recordedfuture.com/hubfs/reports/cta-2022-0406.pdf
  - https://hub.dragos.com/2021-ics-cybersecurity-year-in-review
---

# Indian Critical Infrastructure Intrusions (C0043)

## Executive synopsis
A 2021–early 2022 intrusion sequence linked to PRC-aligned operators (notably RedEcho) targeting Indian electric utility entities and related organizations. Reporting indicates activity focused on IT-network compromise and information gathering; no confirmed progression into OT environments.

## Timeline (high level)
- 2021-01: Activity first observed (per public reporting)
- 2022-04: Activity last reported/linked to this intrusion sequence

## Targeting & victimology
- Primary: Indian power sector (IT assets), with spillover toward logistics and potential MSP dependencies.
- Notable infra note: use of compromised “edge/IoT” devices (e.g., DVR/IP cameras) as C2 or staging nodes.

## Access & tradecraft (ATT&CK highlights)
- Resource development & infra:
  - Acquire Infrastructure: Domains (spoofing/impersonation)
  - Dynamic DNS usage
  - Compromise Infrastructure (edge devices) for C2
- C2:
  - Web protocols, SSL/TLS, non-standard ports (e.g., TCP/8080)
- Remote access / boundary bridging:
  - FRP for NAT traversal / network boundary bridging
  - VPN tunneling via third-party/MSP exposure (reported)

## Malware / tooling
- ShadowPad (S0596): modular backdoor ecosystem frequently used in PRC-aligned operations
- FRP (S1144): reverse proxy/tunneling for remote reachability and segmentation bypass

## IOC / artifact summary (starter set)
- Network:
  - Unusual outbound SSL + HTTP to non-standard ports from utility IT zones
  - FRP-like proxy patterns / sustained tunnels to external nodes
- Endpoint:
  - ShadowPad-like persistence and modular plugin deployment indicators
- Infra:
  - Recently registered spoof domains resembling Indian critical infra entities
  - Dynamic DNS hostnames associated with suspicious endpoints

## Detection & hunting (practical)
- Network hunts:
  - Alert on outbound HTTP(S) on non-standard ports from admin/OT-adjacent IT subnets
  - Detect long-lived reverse tunnels; baseline egress and flag anomalous persistence
- Endpoint hunts:
  - ShadowPad family YARA/behavioral detections; look for signed-binary spoofing and plugin staging
- Exposure review:
  - Audit MSP/VPN trust paths; verify segmentation between IT and OT management planes

## Risks & implications
- Elevated prepositioning risk: even absent confirmed OT access, utility IT compromise can enable future pivoting.
- Managed service dependencies can act as force multipliers for access and persistence.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0043 - Indian Critical Infrastructure Intrusions|Indian Critical Infrastructure Intrusions (C0043)]]
- Actor: [[30_CIPHER/02_Actors/G1042 - RedEcho|RedEcho (G1042)]]
- Malware: [[30_CIPHER/05_Malware/S0596 - ShadowPad|ShadowPad (S0596)]], [[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]

## Recommended OSINT queries
- "C0043 Indian Critical Infrastructure Intrusions ShadowPad FRP"
- "RedEcho G1042 India power sector ShadowPad"
- "TAG38 India power grid Recorded Future April 2022"
- "ShadowPad DVR IP camera compromised infrastructure C2"

## Confidence
Medium-High on PRC alignment and toolchain (ShadowPad/FRP) due to consistent multi-source reporting; Medium on precise victim lists and access paths due to partial public detail.

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
