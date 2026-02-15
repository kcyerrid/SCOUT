---
entity_type: campaign

campaign_name: "Oldsmar Treatment Plant Intrusion"
campaign_id: "C0009"

associated_actors: []
suspected_actors: []

attribution_confidence: "1-low"
confidence_notes: "Public reporting did not conclusively attribute the incident to a known threat actor; details vary across sources and the ATT&CK entry is deprecated."

first_observed: "2021-02-05"
last_observed: "2021-02-05"
campaign_status: "concluded"

primary_objectives:
  - "disruption"
secondary_objectives:
  - "unknown"

target_sectors:
  - "Water / Utilities"
target_regions:
  - "United States"
target_technologies:
  - "Operational Technology (OT)"
  - "Remote access tooling"
  - "HMI/Operator workstation (reported)"

initial_access_vectors:
  - "External Remote Services (reported)"
key_ttp_themes:
  - "Interactive remote session to operator environment (reported)"
  - "Attempted process manipulation via legitimate interfaces (reported)"

associated_ttps:
  - "T1133 - External Remote Services"
  - "T1219 - Remote Access Tools"

malware_families: []
tools_used: []

infrastructure_patterns:
  - "[[Remote Access Exposure]]"
  - "[[Weak Authentication / Shared Accounts]]"

notable_victims:
  - "City of Oldsmar (Florida)"
related_incidents: []

risk_level: "medium"
impact_assessment: "Public reporting describes an unauthorized remote access event with an attempted parameter change in a municipal water treatment environment; attribution and technical specifics remain inconsistent across sources."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0009/"
  - "https://www.nozominetworks.com/blog/florida-water-treatment-plant-hack-what-you-need-to-know"
  - "https://www.armis.com/blog/oldsmar-florida-water-plant-hack"
  - "https://cybersecurityclinics.org/oldsmar-water-treatment-plant-incident/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Oldsmar Treatment Plant Intrusion (C0009)

## 1. Campaign Overview
Oldsmar Treatment Plant Intrusion refers to a publicly reported incident involving unauthorized remote access to a municipal water treatment facility in Oldsmar, Florida. Reporting indicates an attacker attempted to modify treatment process parameters via interactive access. The ATT&CK campaign entry is marked **deprecated**, and open-source narratives vary on root cause and technical detail.

## 2. Attribution Assessment
No definitive actor attribution is established in the cited open sources. Treat this note as **case tracking** rather than attribution-ready intelligence.

**Attribution Confidence: 1-low**

## 3. Objectives & Intent
- Primary objective (reported): disruption/sabotage attempt via process parameter manipulation.
- Secondary: unknown.

## 4. Targeting Analysis
### Sectors Targeted
- Water / Utilities
### Regions Targeted
- United States
### Technologies / Platforms Targeted
- OT environment with remote access exposure (reported), HMI/operator workstation.

## 5. Campaign Tradecraft
Interactive remote access to an operator environment (reported), followed by attempted parameter change through legitimate interfaces.

## 6. MITRE ATT&CK Alignment
### Techniques Observed
- [[T1133 - External Remote Services]]
- [[T1219 - Remote Access Tools]]

## 7. Malware & Tooling
No custom malware is confirmed in the cited public reporting; commonly described as use of remote access tooling.

## 8. Infrastructure & Operational Patterns
- [[Remote Access Exposure]]
- [[Weak Authentication / Shared Accounts]]

## 9. Timeline of Campaign Activity

### Timeline (Markdown)
| Date | Event |
|---|---|
| **2021-02-05** | Unauthorized remote access observed; attempted parameter change reported. |
| **2021-02-10** | Technical analysis published (Nozomi Networks). |
| **2021-02-11** | Vendor analysis published (Armis). |
| **2023-03-13** | Retrospective case study published (Cybersecurity Clinics). |

### Timeline (Chronos)
```chronos
- [2021-02-05]: Unauthorized remote access observed; attempted parameter change reported.
- [2021-02-10]: Technical analysis published (Nozomi Networks).
- [2021-02-11]: Vendor analysis published (Armis).
- [2023-03-13]: Retrospective case study published (Cybersecurity Clinics).
```

## 10. Notable Victims & Impact
### Victim Profile
- City of Oldsmar (Florida)
### Operational Impact
Impact varies by reporting; incident is widely cited as a warning case for remote access controls in OT.

## 11. Related Campaigns & Activity
None confirmed.

## 12. Known Indicators (Contextual)
- After-hours interactive remote sessions to OT operator endpoints.
- Remote access from unusual source IPs/geos/devices.

## 13. Defensive Considerations
- Enforce MFA and eliminate shared accounts for remote access.
- Restrict remote access by allowlist + VPN + conditional access.
- Centralize remote session logging and alert on anomalous interactive access.

## 14. Analyst Notes
Because the ATT&CK entry is deprecated and public reporting differs, keep confidence conservative and prioritize hardening/monitoring of remote access pathways.

## 15. Further Reading / External Resources
- Nozomi Networks analysis
- Armis analysis
- Cybersecurity Clinics retrospective

## 16. References (APA)
- Armis. (2021, February 11). *The Oldsmar, Florida water treatment plant hack: what you need to know*. https://www.armis.com/blog/oldsmar-florida-water-plant-hack
- Cybersecurity Clinics. (2023, March 13). *Oldsmar water treatment plant incident*. https://cybersecurityclinics.org/oldsmar-water-treatment-plant-incident/
- MITRE ATT&CK. (n.d.). *Oldsmar Treatment Plant Intrusion (C0009)*. https://attack.mitre.org/campaigns/C0009/
- Nozomi Networks. (2021, February 10). *Florida water treatment plant hack: what you need to know*. https://www.nozominetworks.com/blog/florida-water-treatment-plant-hack-what-you-need-to-know
