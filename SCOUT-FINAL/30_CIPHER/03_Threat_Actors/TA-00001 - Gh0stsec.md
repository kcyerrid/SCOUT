---
actor_name: "Gh0stsec"
common_name: "GhostSec"
actor_id: ""
actor_type: "Hacktivist / Hybrid (ransomware-adjacent)"
aliases: ["Ghost Security", "GhostSecMafia", "GSM"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2015-01"
last_seen: "2025-05-21"
status: "Active (brand/use varies; reported shifts in activity)"
motivations: ["Ideological (hacktivism)", "Financial (extortion / RaaS)"]
objectives: ["Disruption", "Data theft", "Extortion", "Public messaging / influence"]
victimology_summary: "Public reporting describes activity spanning hacktivist disruption (e.g., DDoS/defacement/leaks) and ransomware-linked extortion activity (including RaaS marketing). Target lists and impacts are often derived from actor-claimed disclosures and may be incomplete or exaggerated."
target_sectors: ["Government", "Critical infrastructure", "Technology", "Telecommunications", "Surveillance/IoT"]
target_regions: ["Middle East", "Africa", "Europe", "Asia", "Americas"]
related_groups: ["Stormous", "ThreatSec", "Blackforums", "SiegedSec"]
malware: ["[[30_CIPHER/05_Malware/GhostLocker]]", "[[30_CIPHER/05_Malware/GhostLocker 2.0]]", "[[30_CIPHER/05_Malware/StormousX]]"]
tools: ["[[30_CIPHER/05_Malware/GhostPresser]]", "[[30_CIPHER/05_Malware/GhostSec Deep Scan Tool]]"]
infrastructure: ["[[Telegram Channels]]", "[[Ransomware Data Leak Site]]", "[[TOR Hidden Service]]", "[[RaaS Affiliate Program]]"]
ttps: ["[[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]", "[[20_Entities/07_TTPs/T1498 - Network Denial of Service]]", "[[20_Entities/07_TTPs/T1491 - Defacement]]", "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]", "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]", "[[20_Entities/07_TTPs/T1489 - Service Stop]]", "[[20_Entities/07_TTPs/T1071.001 - Web Protocols]]"]
notable_claims: ["Publicly framed some monetized activity as funding hacktivism; public reporting also references claimed sector exclusions (not independently verified)."]
intel_sources: ["Cisco Talos (2024-03-05): GhostSec joint ransomware ops & GhostLocker 2.0", "Rapid7 (2023-11-08; upd. 2024-09-03): GhostLocker RaaS analysis", "Outpost24 (last updated 2025-05-21): Threat Actor Profile – GhostSec", "Recorded Future News / The Record (2024-06-19): GhostSec interview on shift toward ransomware and claimed return", "Palo Alto Networks Unit 42 (2024-08-09): Ransomware review noting GhostSec claimed exit/hand-off"]
tags: ["threat-actor", "hacktivism", "ransomware", "double-extortion", "raas", "ghostsec", "gh0stsec"]
---

# GhostSec (Gh0stsec)

## 1. BLUF / Executive Summary
GhostSec (often stylized “Gh0stsec”) is most consistently described as an Anonymous-adjacent hacktivist collective that gained visibility during anti-ISIS operations circa 2015. Multiple public intelligence sources later describe a shift (or splintering) into financially motivated activity, including ransomware-linked extortion and RaaS marketing (notably [[30_CIPHER/05_Malware/GhostLocker]] / [[30_CIPHER/05_Malware/GhostLocker 2.0]]) and collaboration with [[Stormous]]. Attribution is complicated by repeated brand reuse and confusion with “Ghost Security Group,” making name-only claims unreliable without corroborating tradecraft.

## 2. Attribution Notes
- **Brand ambiguity:** “GhostSec/Gh0stsec” is reused and sometimes conflated with “Ghost Security Group.” Public reporting describes name confusion and potential impersonation/brand-jacking, increasing misattribution risk.
- **Activity cohesion:** Reporting supports ransomware-adjacent activity under the GhostSec name, including joint operations and ecosystem overlap with [[Stormous]], but it is not always clear whether this reflects a single stable organization or a shifting coalition.
- **MITRE ID:** No authoritative public mapping to a MITRE ATT&CK Group ID was identified at the time of writing; therefore `actor_id` remains blank.

## 3. Motivations & Objectives
- **Ideological / hacktivist:** Publicly framed operations around counter-terrorism and broader Anonymous-aligned themes.
- **Financial / extortion:** Public reporting describes monetization via leak promotion, “premium” channels, and ransomware/RaaS-linked extortion behavior.
- **Hybrid influence:** Public messaging has at times blended ideological narratives with financially motivated activity; these narratives should be treated as self-reported and not inherently trustworthy.

## 4. Targeting Profile
- **Reported sectors:** Government, technology, telecommunications, surveillance/IoT, and entities adjacent to critical infrastructure.
- **Reported regions:** Multi-region targeting; reporting frequently references activity claims spanning multiple countries.
- **Caveat:** Much victimology is derived from actor-claimed disclosures (leak posts / Telegram statements) and may not reflect complete or independently verified targeting.

## 5. Tradecraft Overview
- **Visibility/disruption:** Use of [[DDoS Attacks]], [[Website Defacement]], and public leak-and-shame messaging amplified through [[Telegram Channels]].
- **Extortion model:** Reporting describes [[Double Extortion]] patterns aligned with ransomware ecosystems and [[RaaS Affiliate Program]] structures.
- **Web compromise emphasis:** Public reporting associates the GhostSec brand with tooling and activity consistent with scanning and compromising public-facing web assets (including CMS-focused activity in some reporting).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1489 - Service Stop]]
- [[20_Entities/07_TTPs/T1071.001 - Web Protocols]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1491 - Defacement]]
- [[20_Entities/07_TTPs/T1498 - Network Denial of Service]]

## 7. Malware & Tools Used
- **Ransomware / extortion tooling (reported):**
  - [[30_CIPHER/05_Malware/GhostLocker]]
  - [[30_CIPHER/05_Malware/GhostLocker 2.0]]
  - [[30_CIPHER/05_Malware/StormousX]] (reported in joint-activity context with [[Stormous]])
- **Website compromise/scanning tooling (reported):**
  - [[30_CIPHER/05_Malware/GhostSec Deep Scan Tool]]
  - [[30_CIPHER/05_Malware/GhostPresser]]

## 8. Infrastructure Patterns
- [[Telegram Channels]] used for publicity, recruitment signaling, and victim “disclosure” messaging.
- [[Ransomware Data Leak Site]] behavior consistent with extortion ecosystems (publication of victim names/data claims).
- [[TOR Hidden Service]] references appear in public reporting for leak/affiliate presence.
- [[RaaS Affiliate Program]] framing, including partnership branding and cross-promotion with other groups (notably [[Stormous]]).

## 9. Campaign History
- **2015 (approx.):** Publicly associated with anti-ISIS / counter-terror hacktivist operations and Anonymous-adjacent messaging.
- **2022-07 (reported):** Public reporting describes visible monetization narratives and subscription-style promotion in some channels.
- **2023-07 (reported):** Public reporting ties GhostSec branding to joint activity with [[Stormous]] and high-profile targeting claims.
- **2023-10 to 2023-11 (reported):** Public reporting notes marketing of [[30_CIPHER/05_Malware/GhostLocker]] and subsequent evolution to [[30_CIPHER/05_Malware/GhostLocker 2.0]] branding.
- **2024-02 to 2024-03 (reported):** Public reporting describes joint RaaS/extortion activity with [[Stormous]] and tooling evolution.
- **2024-05 to 2024-06 (reported):** Public reporting documents GhostSec statements about ending ransomware operations and “returning to hacktivism,” including claims of handing off ransomware operations to [[Stormous]].
- **2025-05-21 (profile update):** Vendor profile updates continue to describe GhostSec as an organized actor with hacktivist roots and ransomware-adjacent activity.

## 10. Known Indicators
No high-confidence, stable public indicators are included in this note due to the risk of stale/repurposed infrastructure, brand mimicry, and uneven public reporting. Use telemetry-driven validation and reputable vendor reporting for incident-specific IOCs.

## 11. Defensive Recommendations
- Strengthen organizational resilience against ransomware-style impact and extortion scenarios (recovery readiness, identity protection, and governance around data exposure).
- Reduce exposure and improve assurance for public-facing web assets and CMS ecosystems (risk management, testing discipline, and rapid response capability for defacement/disruption).
- Treat actor-claimed leaks and victim lists as leads rather than ground truth; prioritize independent validation before attribution or comms actions.

## 12. Analyst Notes
- **Attribution risk remains elevated** due to brand reuse and public-facing “ops” theater; require convergence of [[TTPs]], timing, and infrastructure before assigning activity.
- **Self-reported “rules” or sector exclusions** (e.g., claims about avoiding certain sectors) should be treated as non-authoritative unless corroborated by independent victim reporting or enforcement actions.
- **Confidence (overall): Medium** — broad narrative is supported by multiple reputable sources, but precise incident attribution requires case-specific corroboration.

## 13. Further Reading / External Resources
- Cisco Talos — GhostSec’s joint ransomware operation and evolution of their arsenal (2024-03-05)  
  https://blog.talosintelligence.com/ghostsec-ghostlocker2-ransomware/
- Rapid7 — GhostLocker: A “Work In Progress” RaaS (2023-11-08; updated 2024-09-03)  
  https://www.rapid7.com/blog/post/2023/11/08/ghostlocker-a-work-in-progress-raas/
- Outpost24 — Threat Actor Profile: GhostSec (last updated 2025-05-21)  
  https://outpost24.com/blog/threat-actor-profile-ghostsec/
- Recorded Future News / The Record — “Road to redemption: GhostSec’s hacktivists went to the dark side…” (2024-06-19)  
  https://therecord.media/ghostsec-hacktivism-cybercrime-interview-click-here-podcast
- Palo Alto Networks Unit 42 — Ransomware Review: First Half of 2024 (2024-08-09)  
  https://unit42.paloaltonetworks.com/unit-42-ransomware-leak-site-data-analysis/

## 14. References
- Cisco Talos Intelligence Blog (2024-03-05) — “GhostSec’s joint ransomware operation and evolution of their arsenal”  
  https://blog.talosintelligence.com/ghostsec-ghostlocker2-ransomware/
- Rapid7 Blog (2023-11-08; updated 2024-09-03) — “GhostLocker - A ‘Work In Progress’ RaaS”  
  https://www.rapid7.com/blog/post/2023/11/08/ghostlocker-a-work-in-progress-raas/
- Outpost24 (last updated 2025-05-21) — “Threat Actor Profile – GhostSec”  
  https://outpost24.com/blog/threat-actor-profile-ghostsec/
- Recorded Future News / The Record (2024-06-19) — “Road to redemption: GhostSec's hacktivists went to the dark side…”  
  https://therecord.media/ghostsec-hacktivism-cybercrime-interview-click-here-podcast
- Palo Alto Networks Unit 42 (2024-08-09) — “Ransomware Review: First Half of 2024”  
  https://unit42.paloaltonetworks.com/unit-42-ransomware-leak-site-data-analysis/
