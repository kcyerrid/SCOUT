---
entity_type: campaign

campaign_name: "C0015 Ransomware Intrusion (Bazar → Cobalt Strike → Conti)"
campaign_id: "C0015"
aliases: ["BazarCall to Conti intrusion", "CONTInuing the Bazar Ransomware Story case"]

associated_actors: []
suspected_actors: []
attribution_confidence: "2-medium"
confidence_notes: "ATT&CK documents the intrusion as conducted by unidentified actors. Public reporting assesses the operators followed a commonly circulated Conti playbook."

first_observed: "2021-08"
last_observed: "2021-08"
campaign_status: "concluded"

primary_objectives: ["extortion", "impact"]
secondary_objectives: ["data_theft", "lateral_movement"]

target_sectors: ["private_sector"]
target_regions: ["unknown"]
target_technologies: ["Windows", "Active_Directory", "SMB_shares"]

initial_access_vectors: ["spearphishing_attachment"]
key_ttp_themes: ["rapid_escalation", "tool_transfer", "cloud_exfiltration", "domain_encryption"]

malware_families:
  - "[[30_CIPHER/05_Malware/S0534 - Bazar|Bazar (S0534)]]"
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]"
  - "[[30_CIPHER/05_Malware/S0575 - Conti|Conti (S0575)]]"
  - "[[30_CIPHER/05_Malware/S1040 - Rclone|Rclone (S1040)]]"
  - "[[30_CIPHER/05_Malware/S0552 - AdFind|AdFind (S0552)]]"

tools_used: []
infrastructure_patterns: ["mega_cloud_storage", "remote_admin_tools"]
notable_victims: []
related_incidents: []

associated_ttps:
  - "T1566.001 - Spearphishing Attachment"
  - "T1204.002 - Malicious File"
  - "T1059.003 - Windows Command Shell"
  - "T1059.005 - Visual Basic"
  - "T1059.007 - JavaScript"
  - "T1218.005 - Mshta"
  - "T1218.011 - Rundll32"
  - "T1218.010 - Regsvr32"
  - "T1486 - Data Encrypted for Impact"
  - "T1039 - Data from Network Shared Drive"
  - "T1074.001 - Local Data Staging"
  - "T1567.002 - Exfiltration to Cloud Storage"
  - "T1030 - Data Transfer Size Limits"
  - "T1105 - Ingress Tool Transfer"
  - "T1047 - Windows Management Instrumentation"
  - "T1021.001 - Remote Desktop Protocol"
  - "T1018 - Remote System Discovery"

risk_level: "critical"
impact_assessment: "Ransomware intrusion with staged collection/exfiltration and domain-wide encryption; critical business impact potential including operational disruption and extortion pressure."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0015/"
  - "https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/"
  - "https://www.cisa.gov/news-events/alerts/2021/09/22/conti-ransomware"
  - "https://attack.mitre.org/software/S0534/"
  - "https://attack.mitre.org/software/S0154/"
  - "https://attack.mitre.org/software/S0575/"
  - "https://attack.mitre.org/software/S1040/"
  - "https://attack.mitre.org/software/S0552/"

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
**C0015** describes a ransomware intrusion during which unidentified attackers used **Bazar**, **Cobalt Strike**, and **Conti** over a short operational window. Public DFIR reporting highlights a rapid progression from initial access through discovery, lateral movement, data staging/exfiltration, and domain-wide encryption.

---

## Malware & Tooling
- [[30_CIPHER/05_Malware/S0534 - Bazar|Bazar (S0534)]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]
- [[30_CIPHER/05_Malware/S0575 - Conti|Conti (S0575)]]
- [[30_CIPHER/05_Malware/S1040 - Rclone|Rclone (S1040)]]
- [[30_CIPHER/05_Malware/S0552 - AdFind|AdFind (S0552)]]

---

## MITRE ATT&CK Alignment
- [[T1566.001 - Spearphishing Attachment]]
- [[T1218.005 - Mshta]]
- [[T1218.010 - Regsvr32]]
- [[T1218.011 - Rundll32]]
- [[T1047 - Windows Management Instrumentation]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1567.002 - Exfiltration to Cloud Storage]]
- [[T1486 - Data Encrypted for Impact]]

---

## Timeline of Campaign Activity

```chronos
- [2021-08]: Intrusion activity window reported (month-level).
- [2021-08-01]: Public DFIR case publication date for a closely associated intrusion narrative (report date).
- [2021-09-22]: Government advisory coverage on Conti ransomware (contextual defensive guidance).
```

| Date | Event |
|---|---|
| 2021-08 | Intrusion activity window reported (month-level). |
| 2021-11-29 | DFIR Report publication describing observed intrusion tradecraft. |
| 2021-09-22 | Government advisory coverage on Conti ransomware (defensive guidance). |

---

## Defensive Considerations
- Hunt for early-stage phishing → mshta/regsvr32/rundll32 execution chains.
- Alert on Rclone usage and anomalous cloud storage authentication / large transfers.
- Monitor for AdFind and domain discovery commands; constrain lateral movement via segmentation.
- Enforce MFA and tiered admin model; protect DCs and disable unnecessary remote services.

---

## Analyst Notes
This note is structured to support Dataview dashboards: `risk_level`, `campaign_status`, `first_observed`, `last_observed` are explicitly present for reliable grouping and filtering.

---

## References
- MITRE ATT&CK. (n.d.). *C0015*. https://attack.mitre.org/campaigns/C0015/  
- DFIR Report. (2021, November 29). *CONTInuing the Bazar Ransomware Story*. https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/  
- Cybersecurity and Infrastructure Security Agency. (2021, September 22). *Conti Ransomware*. https://www.cisa.gov/news-events/alerts/2021/09/22/conti-ransomware  
- MITRE ATT&CK. (n.d.). *Bazar (S0534)*. https://attack.mitre.org/software/S0534/  
- MITRE ATT&CK. (n.d.). *Cobalt Strike (S0154)*. https://attack.mitre.org/software/S0154/  
- MITRE ATT&CK. (n.d.). *Conti (S0575)*. https://attack.mitre.org/software/S0575/  
- MITRE ATT&CK. (n.d.). *Rclone (S1040)*. https://attack.mitre.org/software/S1040/  
- MITRE ATT&CK. (n.d.). *AdFind (S0552)*. https://attack.mitre.org/software/S0552/  
