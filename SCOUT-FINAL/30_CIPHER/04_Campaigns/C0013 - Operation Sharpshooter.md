---
entity_type: campaign

campaign_name: "Operation Sharpshooter"
campaign_id: "C0013"
aliases: ["Sharpshooter"]

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group (G0032)]]"
suspected_actors: []
attribution_confidence: "2-medium"
confidence_notes: "Public reporting and ATT&CK documentation connect Operation Sharpshooter to Lazarus-nexus activity. Some reporting focuses on malware/tooling overlaps rather than direct attribution proof, so confidence remains medium."

first_observed: "2017-09"
last_observed: "2019-03"
campaign_status: "concluded"

primary_objectives: ["espionage"]
secondary_objectives: ["credential_access", "collection"]

target_sectors: ["government", "defense", "energy", "telecommunications", "research"]
target_regions: ["global"]
target_technologies: ["Windows", "email", "enterprise_networks"]

initial_access_vectors: ["spearphishing", "watering_hole"]
key_ttp_themes: ["phishing_delivery", "stealthy_collection", "multi-stage_implants"]

malware_families: []
tools_used: []
infrastructure_patterns: ["phishing_infrastructure", "web_delivery"]
notable_victims: []
related_incidents: []

associated_ttps:
  - "T1566.001 - Spearphishing Attachment"
  - "T1566.002 - Spearphishing Link"
  - "T1204.002 - Malicious File"
  - "T1059.003 - Windows Command Shell"
  - "T1071.001 - Web Protocols"
  - "T1105 - Ingress Tool Transfer"
  - "T1005 - Data from Local System"
  - "T1027 - Obfuscated Files or Information"

risk_level: "high"
impact_assessment: "Multi-year espionage campaign with broad sector targeting and multi-stage intrusion patterns; elevated risk due to persistence and data collection objectives."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0013/"
  - "https://attack.mitre.org/groups/G0032/"
  - "https://www.mcafee.com/blogs/"
  - "https://securelist.com/"
  - "https://www.bleepingcomputer.com/"

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
**Operation Sharpshooter (C0013)** is an espionage campaign widely reported in public sources and documented in ATT&CK, commonly associated with **[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group (G0032)]]**. Public narratives emphasize phishing and multi-stage tooling supporting long-term collection.

---

## Attribution Assessment
- Primary: [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group (G0032)]]
- Confidence: **medium** (public reporting + ATT&CK documentation)

---

## MITRE ATT&CK Alignment (Selected)
- [[T1566.001 - Spearphishing Attachment]]
- [[T1566.002 - Spearphishing Link]]
- [[T1204.002 - Malicious File]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1071.001 - Web Protocols]]
- [[T1059.003 - Windows Command Shell]]
- [[T1005 - Data from Local System]]
- [[T1027 - Obfuscated Files or Information]]

---

## Timeline of Campaign Activity

```chronos
- [2017-09]: Earliest reported activity window (month-level).
- [2019-03]: Latest reported activity window (month-level).
- [2018-12-xx]: Public disclosures describing Operation Sharpshooter published (varies by outlet).
```

| Date | Event |
|---|---|
| 2017-09 | Earliest reported activity window (month-level). |
| 2019-03 | Latest reported activity window (month-level). |
| 2018-12 | Public disclosures describing the campaign published (varies by outlet). |

---

## Infrastructure & Delivery
- Spearphishing and web-delivery patterns frequently cited in public reporting.
- Collection objective implies staged tooling and outbound communications to attacker infrastructure.

---

## Defensive Considerations
- Strengthen email controls and user-execution mitigations.
- Detect suspicious ingress tool transfer and outbound web-protocol beaconing to rare hosts.
- Apply least privilege and segment high-value networks.

---

## Analyst Notes
If you want this note to include the full MITRE technique list expanded into YAML, provide your preferred completeness level (e.g., “mirror all techniques from MITRE into YAML”).

---

## References
- MITRE ATT&CK. (n.d.). *Operation Sharpshooter (C0013)*. https://attack.mitre.org/campaigns/C0013/  
- MITRE ATT&CK. (n.d.). *Lazarus Group (G0032)*. https://attack.mitre.org/groups/G0032/  
- McAfee. (2018). *Operation Sharpshooter public reporting and analysis*. https://www.mcafee.com/blogs/  
- Kaspersky Securelist. (2018–2019). *Coverage of Lazarus-linked activity clusters*. https://securelist.com/  
- BleepingComputer. (2018–2019). *News summaries referencing Operation Sharpshooter reporting*. https://www.bleepingcomputer.com/  
