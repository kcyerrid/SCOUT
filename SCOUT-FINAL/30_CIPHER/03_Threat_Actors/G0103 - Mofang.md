---
entity_type: threat_actor
actor_name: "Mofang"
common_name: "Mofang"
actor_id: "G0103"
actor_type: "Cyber espionage (likely China-based)"
aliases: []
country_of_origin: "China (likely)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2012-05-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Information theft from government and critical infrastructure","Strategic collection against military and related industries"]
victimology_summary: "Likely China-based cyber espionage group observed since at least May 2012. Conducts focused attacks against government and critical infrastructure in Myanmar and other countries/sectors. Noted for frequent imitation of victim infrastructure and use of spearphishing with malicious attachments/links."
target_sectors: ["Government","Critical Infrastructure","Military","Automotive","Weapons/Defense-related industries"]
target_regions: ["Myanmar","Multiple (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/ShimRat]]","[[30_CIPHER/05_Malware/ShimRatReporter]]"]
tools: []
infrastructure: ["Spearphishing attachments and links","Compromised websites for click-through delivery","Victim infrastructure imitation / lookalike services"]
ttps:
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]"
  - "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]"
  - "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"
  - "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]"
  - "[[20_Entities/07_TTPs/T1027.015 - Obfuscated Files or Information: Compression]]"
notable_claims: ["Group name derived from frequent imitation of victim infrastructure (per ATT&CK summary)."]
intel_sources:
  - "MITRE ATT&CK - G0103 Mofang - https://attack.mitre.org/groups/G0103/"
  - "Primary reporting referenced by ATT&CK (Fox-IT) - https://attack.mitre.org/groups/G0103/"
tags: ["scout","threat-actor","mitre-g0103","china-likely","espionage","spearphishing"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Mofang (G0103) is a **likely China-based** cyber espionage actor active since at least **2012-05**, conducting targeted operations against **government and critical infrastructure** (notably including Myanmar), plus military and industry targets. ATT&CK highlights Mofang’s tendency to **imitate victim infrastructure**, combined with spearphishing and staged payload delivery.

## 2. Attribution & Profile
- **Type:** Cyber espionage (likely China-based)
- **Confidence:** Medium (as stated in ATT&CK summary language “likely”)
- **Notable trait:** infrastructure imitation to increase lure credibility and blend with expected services

## 3. Targeting & Victimology
- **Primary victims:** government and critical infrastructure entities
- **Additional sectors:** military, automotive, weapons/defense-adjacent industries
- **Geography:** Myanmar and multiple other reported countries/sectors

## 4. Known Malware, Tools & Infrastructure
**Malware**
- [[30_CIPHER/05_Malware/ShimRat]]
- [[30_CIPHER/05_Malware/ShimRatReporter]]

**Delivery / Infrastructure**
- Spearphishing attachments/links aligned with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- Click-through to compromised web resources aligned with [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- Obfuscation via encryption/compression aligned with [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]] and [[20_Entities/07_TTPs/T1027.015 - Obfuscated Files or Information: Compression]]

## 5. Tradecraft Overview
- **Lure-driven execution:** relies on user interaction (open file/click link)
- **Payload protection:** encrypted and compressed payload handling to defeat content inspection and simple detonation
- **Operational masking:** imitation of victim infrastructure to reduce suspicion and increase success rates

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1027.015 - Obfuscated Files or Information: Compression]]

## 7. Detection Opportunities
1. **Spearphishing telemetry**
   - Attachment detonation chains, suspicious external links, and unusual document types in targeted orgs.
2. **Obfuscated payload staging**
   - Endpoints writing encrypted/compressed executables into user-writable paths; anomalous archive extraction or decompression routines.
3. **Infrastructure imitation**
   - Lookalike domains/services resembling internal apps; TLS cert mismatches; unexpected hosting geos/ASNs for “internal-like” endpoints.

## 8. Response & Mitigation Guidance
- Tighten attachment and URL detonation controls; block known lookalike services; apply user-risk reduction for targeted departments.
- Enforce DMARC/SPF/DKIM and phishing-resistant authentication where feasible.
- Rapidly triage any incident where “internal-looking” infrastructure is actually external.

## 9. Hunting Ideas
- Hunt for first-seen external domains that visually/semantically resemble internal services.
- Search proxy/DNS for users accessing newly observed domains shortly after receiving phishing emails.
- Identify endpoints repeatedly handling compressed/encrypted payload blobs followed by new process creation.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/ShimRat]]
- [[30_CIPHER/05_Malware/ShimRatReporter]]

## 11. Associated Tools
- None explicitly listed on the ATT&CK group page beyond malware families.

## 12. Analyst Notes
- **High-signal detection anchors:** targeted spearphishing + lookalike infrastructure + encrypted/compressed payload handling.
- **Operational note:** infrastructure imitation is a strong pivot for enterprise blocking and user education.

## 13. Further Reading / External Resources
- MITRE Group: https://attack.mitre.org/groups/G0103/
- MITRE Software (ShimRat / ShimRatReporter): https://attack.mitre.org/software/

## 14. References
- MITRE ATT&CK. (2024). *Mofang (Group G0103).* https://attack.mitre.org/groups/G0103/
- MITRE ATT&CK. (n.d.). *ShimRat (Software S0444).* https://attack.mitre.org/software/S0444/
- MITRE ATT&CK. (n.d.). *ShimRatReporter (Software S0445).* https://attack.mitre.org/software/S0445/
