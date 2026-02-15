---
entity_type: campaign

campaign_name: "Suspected Iranian Intrusion Activity (UNC3890)"
campaign_id: "C0010"
aliases: ["UNC3890 campaign"]

associated_actors: []
suspected_actors: []
attribution_confidence: "2-medium"
confidence_notes: "Public reporting attributes the activity cluster to a suspected Iran-nexus intrusion set (UNC3890 in vendor reporting). MITRE documents this as Campaign C0010; a MITRE G#### mapping is not provided for UNC3890."

first_observed: "2020-12"
last_observed: "2022-08"
campaign_status: "unknown"

primary_objectives: ["espionage"]
secondary_objectives: ["initial_access_brokering", "credential_access"]

target_sectors: ["government", "healthcare", "energy", "shipping", "technology"]
target_regions: ["Middle East", "global"]
target_technologies: ["Windows", "web_infrastructure", "enterprise_networks"]

initial_access_vectors: ["spearphishing", "watering_hole", "web_delivery"]
key_ttp_themes: ["living_off_the_land", "custom_implants", "credential_targeting", "stealth_c2"]

malware_families:
  - "[[30_CIPHER/05_Malware/S1049 - SUGARUSH|SUGARUSH (S1049)]]"
  - "[[30_CIPHER/05_Malware/S1042 - SUGARDUMP|SUGARDUMP (S1042)]]"
tools_used: []
infrastructure_patterns: ["acquired_domains", "cert_abuse"]
notable_victims: []
related_incidents: []

associated_ttps:
  - "T1583.001 - Domains"
  - "T1587.003 - Digital Certificates"
  - "T1566.002 - Spearphishing Link"
  - "T1189 - Drive-by Compromise"
  - "T1105 - Ingress Tool Transfer"
  - "T1059.003 - Windows Command Shell"
  - "T1071.001 - Web Protocols"
  - "T1027 - Obfuscated Files or Information"

risk_level: "high"
impact_assessment: "Espionage-driven intrusion set targeting multiple sectors with custom implants; risk elevated due to stealthy persistence and potential credential theft."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0010/"
  - "https://attack.mitre.org/software/S1049/"
  - "https://attack.mitre.org/software/S1042/"
  - "https://www.mandiant.com/resources/blog"
  - "https://www.securityweek.com/"
  - "https://thehackernews.com/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
**C0010** describes intrusion activity publicly reported as **UNC3890**, assessed as Iran-nexus in vendor reporting. The campaign is characterized by targeted intrusion operations across multiple sectors and the use of custom implants including **SUGARUSH** and **SUGARDUMP**.

---

## Attribution Assessment
UNC-designation clusters do not always map cleanly to a MITRE **G####** group. Attribution confidence is **medium** based on vendor reporting and ATT&CK documentation.

---

## Objectives & Intent
- **Primary:** Espionage / strategic collection  
- **Secondary:** Credential access to enable lateral movement and sustained access

---

## MITRE ATT&CK Alignment (Selected)
- [[T1583.001 - Domains]]
- [[T1587.003 - Digital Certificates]]
- [[T1566.002 - Spearphishing Link]]
- [[T1189 - Drive-by Compromise]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1071.001 - Web Protocols]]
- [[T1059.003 - Windows Command Shell]]
- [[T1027 - Obfuscated Files or Information]]

---

## Malware & Tooling
### Malware Families
- [[30_CIPHER/05_Malware/S1049 - SUGARUSH|SUGARUSH (S1049)]]
- [[30_CIPHER/05_Malware/S1042 - SUGARDUMP|SUGARDUMP (S1042)]]

---

## Timeline of Campaign Activity

```chronos
- [2020-12]: Earliest activity window reported for C0010/UNC3890 (month-level).
- [2022-08]: Latest activity window reported for this campaign (month-level).
- [2022-08-17]: Public vendor reporting highlights targeting and malware families (report date varies by source).
```

| Date | Event |
|---|---|
| 2020-12 | Earliest reported activity window (month-level). |
| 2022-08 | Latest reported activity window (month-level). |
| 2022-08-17 | Public reporting highlighting the cluster and malware families (approx.). |

---

## Infrastructure & Operational Patterns
- Domain acquisition and possible certificate-related tradecraft supporting stealth and delivery.
- Emphasis on custom implants and web-based C2 patterns.

---

## Defensive Considerations
- Monitor for suspicious domain/certificate usage and anomalous web traffic to rare endpoints.
- Enforce MFA and conditional access for privileged users; alert on unusual authentication patterns.
- Threat hunt for implant families (SUGARUSH/SUGARDUMP) behaviors and persistence artifacts.

---

## Analyst Notes
UNC clusters may later merge/split with other tracked sets; keep attribution flexible and evidence-driven.

---

## References
- MITRE ATT&CK. (n.d.). *C0010*. https://attack.mitre.org/campaigns/C0010/  
- MITRE ATT&CK. (n.d.). *SUGARUSH (S1049)*. https://attack.mitre.org/software/S1049/  
- MITRE ATT&CK. (n.d.). *SUGARDUMP (S1042)*. https://attack.mitre.org/software/S1042/  
- Mandiant. (2022). *Reporting on suspected Iranian activity cluster UNC3890 and related tooling*. https://www.mandiant.com/resources/blog  
- SecurityWeek. (2022). *Coverage of suspected Iranian intrusion activity affecting multiple sectors*. https://www.securityweek.com/  
- The Hacker News. (2022). *News coverage summarizing campaign tradecraft and malware usage*. https://thehackernews.com/  
