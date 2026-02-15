---
entity_type: campaign

campaign_name: "Maroochy Water Breach"
campaign_id: "C0020"

associated_actors: []
suspected_actors: []

attribution_confidence: "2-medium"
confidence_notes: "Incident is well documented, but attribution is to an individual adversary rather than an established cyber threat group; confidence reflects strong incident documentation."

first_observed: "2000-02"
last_observed: "2000-04"
campaign_status: "concluded"

primary_objectives: ["disruption", "sabotage"]
secondary_objectives: ["impact"]

target_sectors: ["water", "wastewater", "critical_infrastructure"]
target_regions: ["Australia"]
target_technologies: ["ICS", "radio communications", "wastewater pumping stations"]

initial_access_vectors: ["stolen_equipment", "wireless_compromise", "external_remote_services"]
key_ttp_themes: ["wireless_ics_access", "alarm_suppression", "unauthorized_commands", "denial_of_view"]

malware_families: []
tools_used: []

infrastructure_patterns: ["radio_based_remote_access", "spoofed_addresses"]
notable_victims: ["Maroochy Shire wastewater control system"]
related_incidents: []

risk_level: "critical"
impact_assessment: "Physical-world impact: unauthorized control actions contributed to the release of ~800,000 liters of raw sewage, affecting the community and environment."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0020/"
  - "https://www.mitre.org/sites/default/files/publications/pr-18-1154-maroochy-water-services-case-study.pdf"
  - "https://www.controleng.com/articles/maroochy-water-services-breach-what-happened-and-what-to-do/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
The **Maroochy Water Breach (C0020)** was a 2000 incident in Australia where an adversary used stolen engineering equipment and unauthorized remote access to disrupt a wastewater control system, contributing to the release of approximately **800,000 liters of raw sewage** into the environment.

---

## Attribution Assessment
Attribution is to an adversary actor involved in the incident (not a named cyber threat group). Confidence is **medium** because the incident is strongly documented, though not always with full technical telemetry by modern standards.

---

## Objectives & Intent
- **Primary:** disruption/sabotage of wastewater operations
- **Secondary:** sustained operational impact via alarm and control interference

---

## Targeting Analysis
### Sectors Targeted
- Water / wastewater critical infrastructure

### Region
- Australia (Maroochy Shire area)

### Technologies / Platforms Targeted
- ICS environment controlling pumping stations
- Radio-based communications and remote access workflows
- Alarm/reporting mechanisms to central control

---

## Campaign Tradecraft
### High-Level Tradecraft Summary
The adversary leveraged unauthorized remote access over radio, altered control parameters, interfered with visibility, and manipulated alarm settings/reporting to reduce operator awareness and response effectiveness.

---

## MITRE ATT&CK Alignment (ICS)
### Techniques Observed
- [[T0878 - Alarm Suppression]]
- [[T0879 - Damage to Property]]
- [[T0813 - Denial of Control]]
- [[T0815 - Denial of View]]
- [[T0822 - External Remote Services]]
- [[T0838 - Modify Alarm Settings]]
- [[T0836 - Modify Parameter]]
- [[T0848 - Rogue Master]]
- [[T0856 - Spoof Reporting Message]]
- [[T0864 - Transient Cyber Asset]]
- [[T0855 - Unauthorized Command Message]]
- [[T0860 - Wireless Compromise]]

### Notable Tradecraft Characteristics
- Reliance on **wireless/radio** access paths
- Emphasis on **alarm suppression** and **spoofed reporting** to mask effects

---

## Infrastructure & Operational Patterns
- Dedicated analog two-way radio communications used to deliver unauthorized messages
- Spoofing network addresses / masquerading as legitimate controllers (“rogue master” behavior)

---

## Timeline of Campaign Activity (Chronos)
```chronos
- [2000-02]: Incident activity begins (first seen window in ATT&CK).
- [2000-04]: Incident activity ends (last seen window in ATT&CK).
- [2008-07-23]: Case study publication documenting the incident (later referenced by ATT&CK).
```

## Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2000-02 | Incident activity begins (first seen window) |
| 2000-04 | Incident activity ends (last seen window) |
| 2008-07-23 | Case study publication documenting the incident |

---

## Notable Victims & Impact
- Environmental and community impact from sewage release
- Demonstrates the real-world risk of unauthorized ICS command/control

---

## Defensive Considerations
- Inventory and protect engineering workstations/software; prevent theft and unauthorized use.
- Secure wireless/radio access paths; implement authentication and monitoring where possible.
- Monitor for abnormal alarm configuration changes and command message anomalies.

---

## References (APA)
- MITRE ATT&CK. (2025, April 16). *Maroochy Water Breach (C0020)*. Retrieved 2026-01-03 from https://attack.mitre.org/campaigns/C0020/
- Abrams, M. (2008, July 23). *Malicious Control System Cyber Security Attack Case Study: Maroochy Water Services, Australia* [Case study]. MITRE. Retrieved 2026-01-03 from https://www.mitre.org/sites/default/files/publications/pr-18-1154-maroochy-water-services-case-study.pdf
- Control Engineering. (2023, March 2). *Maroochy Water Services breach: What happened and what to do*. Retrieved 2026-01-03 from https://www.controleng.com/articles/maroochy-water-services-breach-what-happened-and-what-to-do/
