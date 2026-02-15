---
entity_type: threat_actor
actor_name: "Bouncing Golf"
common_name: "Bouncing Golf"
actor_id: "G0097"
actor_type: "Cyberespionage campaign (mobile)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2019-01-01"
last_seen: ""
status: "Unknown"
motivations:
  - "Espionage"
objectives:
  - "Mobile device surveillance"
  - "Collection of communications and location data"
victimology_summary: "Cyberespionage campaign targeting Middle Eastern countries, distributing repackaged legitimate mobile applications containing malicious code."
target_sectors: []
target_regions:
  - "Middle East"
related_groups: []
ttps:
  - "[[20_Entities/07_TTPs/T1655.001 - Masquerading: Match Legitimate Name or Location|T1655.001]]"
malware:
  - "[[30_CIPHER/05_Malware/GolfSpy]]"
tools: []
infrastructure:
  - "Repackaged legitimate mobile applications embedding malicious code (notably within a specific package namespace)"
references:
  - "https://attack.mitre.org/groups/G0097/"
  - "https://www.trendmicro.com/en_us/research/19/f/mobile-cyberespionage-campaign-bouncing-golf-affects-middle-east.html"
mitre_version: "18.0"
attack_spec_version: "3.2"
created: 2026-01-06
last_modified: 2026-01-06
tags:
  - scout
  - threat-actor
  - mitre
  - group
  - G0097
  - mobile
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. BLUF / Executive Summary
Bouncing Golf is a mobile-focused cyberespionage campaign targeting Middle Eastern countries. It relies on **masquerading** by distributing **repackaged legitimate apps** that embed the GolfSpy malware.

## 2. Attribution Notes
- Public reporting frames Bouncing Golf as a campaign targeting the Middle East; sponsor and operator attribution remain unclear in ATT&CK.

## 3. Motivations & Objectives
- Primary motivation: **espionage** via mobile surveillance.
- Objectives include collecting sensitive user data (communications, contacts, call logs) and device context (location).

## 4. Targeting Profile
- **Region:** Middle East
- **Primary asset type:** mobile endpoints

## 5. Tradecraft Overview
- Delivery via trojanized/repackaged apps masquerading as legitimate software.
- Malware components embedded within app package structure; emphasizes stealth via legitimate-looking artifacts.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1655.001 - Masquerading: Match Legitimate Name or Location|T1655.001]] — repackaged legitimate applications to blend in.

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/GolfSpy]] — mobile spyware capabilities consistent with broad data collection and device surveillance.

## 8. Infrastructure Patterns
- Distribution ecosystem for trojanized apps (third-party stores, direct links, or side-loading pathways depending on victim workflows).
- C2 endpoints and hosting typically vary; treat as campaign-specific and time-bound.

## 9. Campaign History
- Documented publicly as a Middle East-targeting mobile cyberespionage effort (2019 reporting).

## 10. Known Indicators
- Maintain per-case app hashes, signing cert metadata, package names, and C2 endpoints; tie to acquisition source (store/site) and collection timestamp.

## 11. Defensive Recommendations
1. **Mobile app integrity:** enforce managed app catalogs; restrict side-loading; require verified signing.
2. **Package/name heuristics:** detections for mismatched app identity signals (developer vs package namespace, unexpected embedded packages).
3. **Network controls:** block known-bad mobile C2, and monitor unusual outbound traffic for managed devices.
4. **User awareness (mobile):** “legit app from non-official source” patterns are high-risk; prioritize policy controls over training.

## 12. Analyst Notes
- For mobile campaigns, retaining **original APK/IPA**, signing info, and distribution context is often more valuable than late-stage IOCs.

## 13. Further Reading / External Resources
- Trend Micro. (2019). *Mobile Campaign ‘Bouncing Golf’ Affects Middle East.* https://www.trendmicro.com/en_us/research/19/f/mobile-cyberespionage-campaign-bouncing-golf-affects-middle-east.html

## 14. References
- MITRE ATT&CK. (n.d.). *Bouncing Golf (G0097).* Retrieved 2026-01-06, from https://attack.mitre.org/groups/G0097/
- Xu, E., & Guo, G. (2019, June 28). *Mobile Cyberespionage Campaign ‘Bouncing Golf’ Affects Middle East.* Trend Micro. https://www.trendmicro.com/en_us/research/19/f/mobile-cyberespionage-campaign-bouncing-golf-affects-middle-east.html
