---
entity_type: campaign

campaign_name: "Transparent Tribe Education Sector Campaign"
campaign_id: "C0011"
aliases: ["Transparent Tribe campaign (education sector)"]

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0134 - Transparent Tribe|Transparent Tribe (G0134)]]"
suspected_actors: []
attribution_confidence: "2-medium"
confidence_notes: "MITRE documents the campaign as conducted by Transparent Tribe (G0134). Public reporting supports education-sector targeting with phishing-based delivery."

first_observed: "2021-12"
last_observed: "2022-07"
campaign_status: "unknown"

primary_objectives: ["espionage"]
secondary_objectives: ["credential_access"]

target_sectors: ["education"]
target_regions: ["South Asia", "global"]
target_technologies: ["Windows", "email", "web"]

initial_access_vectors: ["spearphishing_attachment", "spearphishing_link"]
key_ttp_themes: ["phishing", "user_execution", "payload_delivery"]

malware_families: []
tools_used: []
infrastructure_patterns: ["malware_upload", "domain_use"]
notable_victims: []
related_incidents: []

associated_ttps:
  - "T1583.001 - Domains"
  - "T1059.005 - Visual Basic"
  - "T1587.003 - Digital Certificates"
  - "T1566.001 - Spearphishing Attachment"
  - "T1566.002 - Spearphishing Link"
  - "T1608.001 - Upload Malware"
  - "T1204.001 - Malicious Link"
  - "T1204.002 - Malicious File"

risk_level: "medium"
impact_assessment: "Targeted education-sector intrusion activity with phishing delivery and user-execution dependence; risk moderated by common detection opportunities in email telemetry and endpoint controls."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0011/"
  - "https://attack.mitre.org/groups/G0134/"
  - "https://blog.talosintelligence.com/"
  - "https://www.proofpoint.com/us/threat-insight"
  - "https://www.recordedfuture.com/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
**C0011** documents a campaign attributed to **[[30_CIPHER/03_Threat_Actors/G0134 - Transparent Tribe|Transparent Tribe (G0134)]]** targeting the **education sector**, using phishing and user-execution paths.

---

## Attribution Assessment
Primary attribution: **[[30_CIPHER/03_Threat_Actors/G0134 - Transparent Tribe|Transparent Tribe (G0134)]]** (MITRE-documented). Confidence is **medium** based on public reporting and ATT&CK documentation.

---

## MITRE ATT&CK Alignment
- [[T1566.001 - Spearphishing Attachment]]
- [[T1566.002 - Spearphishing Link]]
- [[T1204.001 - Malicious Link]]
- [[T1204.002 - Malicious File]]
- [[T1059.005 - Visual Basic]]
- [[T1583.001 - Domains]]
- [[T1587.003 - Digital Certificates]]
- [[T1608.001 - Upload Malware]]

---

## Timeline of Campaign Activity

```chronos
- [2021-12]: Earliest reported activity window (month-level).
- [2022-07]: Latest reported activity window (month-level).
```

| Date | Event |
|---|---|
| 2021-12 | Earliest reported activity window (month-level). |
| 2022-07 | Latest reported activity window (month-level). |

---

## Infrastructure & Delivery
Delivery patterns center on spearphishing and user execution, supported by domains and payload staging/upload activity.

---

## Defensive Considerations
- Email security: attachment detonation, URL rewriting, and macro/script controls.
- Endpoint hardening: restrict script execution where possible and monitor VBScript engines.
- Threat hunting: investigate suspicious education-targeted lures and lookalike domains.

---

## Analyst Notes
If you provide the specific vendor writeups you care about (or your internal mail telemetry), we can enrich the timeline with exact lure themes, file hashes, and infrastructure pivots.

---

## References
- MITRE ATT&CK. (n.d.). *C0011*. https://attack.mitre.org/campaigns/C0011/  
- MITRE ATT&CK. (n.d.). *Transparent Tribe (G0134)*. https://attack.mitre.org/groups/G0134/  
- Cisco Talos. (n.d.). *Transparent Tribe / related reporting*. https://blog.talosintelligence.com/  
- Proofpoint. (n.d.). *Threat research and phishing telemetry insights*. https://www.proofpoint.com/us/threat-insight  
- Recorded Future. (n.d.). *Threat intelligence reporting on regional actor activity*. https://www.recordedfuture.com/  
