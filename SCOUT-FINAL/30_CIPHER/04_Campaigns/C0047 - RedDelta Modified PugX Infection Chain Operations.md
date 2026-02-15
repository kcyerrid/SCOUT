---
entity_type: campaign
campaign_name: RedDelta Modified PlugX Infection Chain Operations
campaign_id: C0047
first_seen: 2023-07
last_seen: 2024-12
suspected_attribution: PRC-aligned
associated_actors:
  - "[[30_CIPHER/02_Actors/G0129 - Mustang Panda|Mustang Panda (G0129)]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0013 - PlugX|PlugX (S0013)]]"
  - "[[30_CIPHER/05_Malware/S0596 - ShadowPad|ShadowPad (S0596)]]"
target_geography:
  - East Asia
  - Southeast Asia
target_sectors:
  - Government / diplomatic / regional entities (as described in reporting)
goals:
  - Espionage; persistent footholds via PlugX variants; selective payload delivery control
intel_sources:
  - https://attack.mitre.org/campaigns/C0047/
  - https://go.recordedfuture.com/hubfs/reports/cta-2025-0109.pdf
---

# RedDelta Modified PlugX Infection Chain Operations (C0047)

## Executive synopsis
A mid-2023 through end-2024 campaign linked to Mustang Panda, using phishing to drive follow-on downloads that establish persistent PlugX, with selective delivery controls (guardrails) and use of CDN/proxy infrastructure.

## Timeline (high level)
- 2023-07: First seen
- 2024-12: Last seen

## Initial access & delivery chain
- Spearphishing attachments and links
- User-execution of LNK/HTML leading to MSI installer chain
- MMC/MSC execution via mmc.exe used to run follow-on PowerShell in some variants (per mapping)

## Tradecraft (ATT&CK highlights)
- Resource development:
  - Re-registration of expired domains
  - Acquisition/use of TLS certificates (including Cloudflare Origin CA)
- Execution & persistence:
  - PowerShell execution via LNK
  - Run keys / startup persistence
  - DLL search-order hijacking with signed binaries for sideloading
- Guardrails / operational security:
  - Geofencing controls via CDN mechanisms to limit who gets payloads
  - Proxying via CDN
- C2:
  - HTTP POST-based C2
  - Additional TCP channelization (reported port usage)

## Malware / tooling
- PlugX (S0013): primary implant focus
- ShadowPad (S0596): observed in similar installation patterns (DLL sideloading)

## IOC / artifact summary (starter set)
- Email + execution:
  - LNK or MSC files leading to PowerShell → MSI download
- Registry:
  - Run key names masquerading as legitimate updaters (e.g., OneNote-like strings reported)
- Network:
  - CDN/proxy traffic patterns masking true origin; look for suspicious domain age + re-registered domains

## Detection & hunting (practical)
- Attachment and LOLBin controls:
  - Block/contain LNK and MSC from email; constrain mmc.exe spawning PowerShell
- DLL sideloading:
  - Alert on signed executables loading DLLs from user-writable directories
- CDN abuse:
  - Enrich domains (creation/ownership changes); hunt for Cloudflare-fronted C2 with anomalous endpoints

## Risks & implications
- Delivery guardrails reduce incidental detection and increase targeted success.
- Re-registered domains can bypass naive allowlists tied to historical reputations.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0047 - RedDelta Modified PlugX Infection Chain Operations|RedDelta Modified PlugX Infection Chain Operations (C0047)]]
- Actor: [[30_CIPHER/02_Actors/G0129 - Mustang Panda|Mustang Panda (G0129)]]
- Malware: [[30_CIPHER/05_Malware/S0013 - PlugX|PlugX (S0013)]], [[30_CIPHER/05_Malware/S0596 - ShadowPad|ShadowPad (S0596)]]

## Recommended OSINT queries
- "C0047 RedDelta Modified PlugX infection chain"
- "Mustang Panda G0129 MSC MMC msiexec PlugX"
- "Recorded Future January 2025 RedDelta PlugX ShadowPad"
- "Cloudflare geofencing Mustang Panda"

## Confidence
High on actor linkage and major TTPs (explicit mapping to Mustang Panda + detailed chain). Medium on full victim list due to limited public enumeration.

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
