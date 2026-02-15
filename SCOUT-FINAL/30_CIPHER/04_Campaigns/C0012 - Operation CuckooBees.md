---
entity_type: campaign

campaign_name: "Operation CuckooBees"
campaign_id: "C0012"
aliases: ["CuckooBees"]

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0044 - Winnti Group|Winnti Group (G0044)]]"
suspected_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]"
attribution_confidence: "2-medium"
confidence_notes: "Public reporting and ATT&CK documentation associate the campaign with Winnti-nexus activity; overlap with APT41 is frequently discussed in industry reporting. Confidence remains medium due to public-source constraints and varying vendor nomenclature."

first_observed: "2019-12"
last_observed: "2022-05"
campaign_status: "unknown"

primary_objectives: ["espionage", "intellectual_property_theft"]
secondary_objectives: ["credential_access", "lateral_movement"]

target_sectors: ["technology", "manufacturing", "pharmaceuticals", "research"]
target_regions: ["East Asia", "global"]
target_technologies: ["Windows", "enterprise_networks"]

initial_access_vectors: ["unknown", "webshell", "credential_abuse"]
key_ttp_themes: ["stealthy_collection", "persistence", "credential_theft", "archiving_and_exfiltration"]

malware_families: []
tools_used: []
infrastructure_patterns: ["web_protocol_c2", "staged_archives"]
notable_victims: []
related_incidents: []

associated_ttps:
  - "T1087.001 - Local Account"
  - "T1087.002 - Domain Account"
  - "T1071.001 - Web Protocols"
  - "T1560.001 - Archive via Utility"
  - "T1547.006 - Kernel Modules and Extensions"
  - "T1059.003 - Windows Command Shell"
  - "T1059.005 - Visual Basic"
  - "T1543.003 - Windows Service"
  - "T1005 - Data from Local System"
  - "T1119 - Automated Collection"
  - "T1105 - Ingress Tool Transfer"
  - "T1036.005 - Match Legitimate Resource Name or Location"

risk_level: "high"
impact_assessment: "Multi-year IP theft/espionage campaign with broad enterprise targeting; elevated risk due to persistence, credential focus, and staged collection/exfiltration workflows."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0012/"
  - "https://attack.mitre.org/groups/G0044/"
  - "https://attack.mitre.org/groups/G0096/"
  - "https://www.cybereason.com/blog"
  - "https://therecord.media/"
  - "https://www.theregister.com/"

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
**Operation CuckooBees (C0012)** is a long-running espionage and IP theft campaign widely reported as Winnti-nexus activity, with frequent discussion of overlap with **APT41** in industry reporting. The campaign’s public characterization emphasizes stealthy collection, persistence, and large-scale targeting of organizations holding valuable intellectual property.

---

## Attribution Assessment
- Primary: [[30_CIPHER/03_Threat_Actors/G0044 - Winnti Group|Winnti Group (G0044)]]
- Suspected overlap: [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41 (G0096)]]

---

## MITRE ATT&CK Alignment (Selected)
- [[T1087.001 - Local Account]]
- [[T1087.002 - Domain Account]]
- [[T1071.001 - Web Protocols]]
- [[T1560.001 - Archive via Utility]]
- [[T1543.003 - Windows Service]]
- [[T1547.006 - Kernel Modules and Extensions]]
- [[T1059.003 - Windows Command Shell]]
- [[T1059.005 - Visual Basic]]
- [[T1005 - Data from Local System]]
- [[T1119 - Automated Collection]]

---

## Timeline of Campaign Activity

```chronos
- [2019-12]: Earliest reported activity window (month-level).
- [2022-05]: Latest reported activity window (month-level).
- [2022-05-xx]: Major public report(s) describing Operation CuckooBees published (date varies by outlet).
```

| Date | Event |
|---|---|
| 2019-12 | Earliest reported activity window (month-level). |
| 2022-05 | Latest reported activity window (month-level). |
| 2022-05 | Public reporting describing Operation CuckooBees published (varies by source). |

---

## Infrastructure & Operational Patterns
- Web-protocol C2 and tooling behavior consistent with stealthy exfil patterns.
- Archiving/staging prior to exfiltration aligns with IP theft objectives.

---

## Defensive Considerations
- Focus hunts on credential abuse + persistence + archive staging in sensitive R&D networks.
- Detect unusual archive creation in admin-like locations (Temp/ProgramData) and outbound web traffic anomalies.
- Harden service creation paths and monitor for suspicious service installs tied to unusual parent processes.

---

## Analyst Notes
The technique list above is a defensible **selected** subset. The MITRE campaign page includes additional techniques; expand `associated_ttps` further if you want a fully exhaustive mapping mirrored into Obsidian.

---

## References
- MITRE ATT&CK. (n.d.). *Operation CuckooBees (C0012)*. https://attack.mitre.org/campaigns/C0012/  
- MITRE ATT&CK. (n.d.). *Winnti Group (G0044)*. https://attack.mitre.org/groups/G0044/  
- MITRE ATT&CK. (n.d.). *APT41 (G0096)*. https://attack.mitre.org/groups/G0096/  
- Cybereason. (2022). *Operation CuckooBees: Large-scale IP theft/espionage reporting*. https://www.cybereason.com/blog  
- The Record. (2022). *News coverage summarizing Operation CuckooBees and suspected attribution*. https://therecord.media/  
- The Register. (2022). *Reporting on Winnti-linked IP theft campaign disclosures*. https://www.theregister.com/  
