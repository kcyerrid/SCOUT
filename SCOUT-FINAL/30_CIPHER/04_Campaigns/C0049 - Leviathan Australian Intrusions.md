---
entity_type: campaign
campaign_name: Leviathan Australian Intrusions
campaign_id: C0049
first_seen: 2022-04
last_seen: 2022-09
suspected_attribution: PRC MSS-aligned (APT40/Leviathan ecosystem per multi-agency advisory context)
associated_actors:
  - "[[30_CIPHER/02_Actors/G0065 - Leviathan|Leviathan (G0065)]]"
associated_malware: []
target_geography:
  - Australia
target_sectors:
  - Government / private sector (Australia; long-term intrusions)
goals:
  - Sensitive data theft; credential capture and reuse; lateral movement; sustained access
intel_sources:
  - https://attack.mitre.org/campaigns/C0049/
  - https://www.cyber.gov.au/sites/default/files/2024-07/apt40-advisory-prc-mss-tradecraft-in-action.pdf
  - https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3831226/joint-cybersecurity-advisory-releases-details-on-prc-state-sponsored-cy/
---

# Leviathan Australian Intrusions (C0049)

## Executive synopsis
At least two long-term intrusions against Australian victims attributed to Leviathan, characterized by exploitation of external services followed by extensive credential capture/reuse for privilege escalation and lateral movement, with a focus on exfiltrating sensitive data (including credentials).

## Timeline (high level)
- 2022-04: First seen (intrusion window)
- 2022-09: Last seen (intrusion window)

## Initial access
- Exploitation of public-facing web applications and appliances (initial foothold)
- Follow-on: web shell placement and credential access to expand control

## Tradecraft (ATT&CK highlights)
- Credential access:
  - Capture of credentials (including MFA-related artifacts in some cases)
  - Theft of application access tokens (e.g., JWTs) and reuse of valid accounts
- Discovery:
  - AD enumeration, domain trust discovery, remote system/share discovery
- Lateral movement:
  - SMB/Windows admin shares, SSH (including brute force noted in mapping)
- Persistence:
  - Extensive web shell reliance early post-compromise
- Defense evasion:
  - Firewall rule modifications (ports opened) reported in mapping
- Collection/exfil:
  - Data from repositories (SQL/BMS servers) and exfil over C2 channels

## IOC / artifact summary (starter set)
- Identity:
  - Repeated successful logons across systems using harvested credentials; anomalous MFA token handling
- Web layer:
  - Web shells on internet-facing servers; unusual web app resource enumeration
- Network:
  - Unexpected open ports (e.g., 9998/9999) and lateral SMB/SSH spread patterns

## Detection & hunting (practical)
- External attack surface:
  - Patch/mitigate internet-facing apps/appliances; monitor for exploit attempts and web shell drop indicators
- Identity & access:
  - Detect “credential replay” patterns and impossible-travel/admin-share movement bursts
  - Review token issuance and session creation anomalies (JWT / VDI session creation patterns)
- BMS/OT-adjacent IT:
  - Inventory and harden Building Management System servers; monitor credential storage and unusual database access

## Risks & implications
- Credential-centric intrusions can scale quickly and persist across segmented environments.
- BMS and other “non-core” systems can provide high-value footholds and stealthy data access.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0049 - Leviathan Australian Intrusions|Leviathan Australian Intrusions (C0049)]]
- Actor: [[30_CIPHER/02_Actors/G0065 - Leviathan|Leviathan (G0065)]]

## Recommended OSINT queries
- "C0049 Leviathan Australian Intrusions"
- "Leviathan G0065 APT40 tradecraft in action advisory"
- "APT40 Australia MSS credential theft web shells BMS"
- "PRC MSS tradecraft in action case studies Australia"

## Confidence
Medium-High on attribution (explicit mapping to Leviathan in ATT&CK campaign entry + aligned advisory context). Medium on exact exploited CVEs and victim enumeration due to limited publicly accessible primary advisory content from some hosts.

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
