---
entity_type: campaign

campaign_name: "Unitronics Defacement Campaign"
campaign_id: "C0031"
aliases: []
status: "inactive"
risk_level: "high"

first_seen: "2023-11"
last_seen: "2023-11"

attribution:
  associated_threat_actors:
    - "[[30_CIPHER/03_Threat_Actors/G1027 - CyberAv3ngers|CyberAv3ngers (G1027)]]"
  suspected_threat_actors: []
  attribution_confidence: "high"
  attribution_notes: "MITRE attributes the campaign to CyberAv3ngers."

targets:
  regions:
    - "Global"
    - "United States"
  sectors:
    - "Water and Wastewater"
    - "Energy"
    - "Food and Beverage Manufacturing"
    - "Healthcare"
  technologies:
    - "Unitronics Vision Series PLCs"
    - "HMI interfaces in OT environments"
    - "Internet-exposed OT devices and cellular modems"

initial_access_vectors:
  - "Internet-exposed OT device access"
  - "Default credentials on PLC/HMI systems"

key_ttp_themes:
  - "Opportunistic scanning and access of exposed OT devices"
  - "Defacement of HMI to disrupt operations"
  - "Use of default passwords"

associated_malware: []

associated_ttps:
  - "T0812 - Default Credentials"
  - "T0814 - Denial of Service"
  - "T0883 - Internet Accessible Device"
  - "T0826 - Loss of Availability"
  - "T0828 - Loss of Productivity and Revenue"
  - "T0829 - Loss of View"

impact_assessment:
  - "HMI defacement and operational disruption in OT contexts"
  - "Potential safety and availability impacts in critical services"

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0031/"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a"
  - "https://www.cisa.gov/news-events/alerts/2023/11/28/exploitation-unitronics-plcs-used-water-and-wastewater-systems"
  - "https://apnews.com/"
  - "https://www.bloomberg.com/"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Unitronics Defacement Campaign (C0031)

## 1. Executive Summary
**Unitronics Defacement Campaign (C0031)** is an OT-focused intrusion set attributed to **[[30_CIPHER/03_Threat_Actors/G1027 - CyberAv3ngers|CyberAv3ngers (G1027)]]** involving **global opportunistic targeting and defacement** of **Unitronics Vision Series PLCs with HMIs**. The campaign leveraged **internet exposure + default credentials** to access devices and disrupt operations via HMI defacement.

## 2. Campaign Overview
- **Timeframe:** 2023-11 (first and last seen in November 2023)  
- **Primary technique:** exploitation of default credentials (commonly reported default password “1111”).  
- **Operational outcome:** defacement leading to loss of view/availability and operational interruption.

## 3. Linked Entities
### Threat Actor
- [[30_CIPHER/03_Threat_Actors/G1027 - CyberAv3ngers|CyberAv3ngers (G1027)]]

### Malware / Software
- None explicitly enumerated on the MITRE campaign entry (activity centers on device access/defacement).

## 4. Timeline of Campaign Activity (Chronos)
```chronos
- [2023-11-27] Public reporting on investigation of a municipal water authority OT cyber incident (reporting date).
- [2023-11-28] Government alert on exploitation of Unitronics PLCs in WWS environments (reporting date).
- [2023-12-01] Government advisory on IRGC-affiliated actors exploiting PLCs across sectors (reporting date).
- [2023-12-02] Media coverage describing multi-state impacts and agency warnings (reporting date).
- [2023-12-22] Additional reporting highlighting systemic OT exposure and safeguards gaps (reporting date).
```

## 5. Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2023-11-27 | Public reporting on investigation of municipal water authority incident |
| 2023-11-28 | Government alert on exploitation of Unitronics PLCs |
| 2023-12-01 | Government advisory on IRGC-affiliated actors exploiting PLCs |
| 2023-12-02 | Media coverage of breaches and agency warnings |
| 2023-12-22 | Reporting on OT exposure and safeguard gaps |

## 6. MITRE ATT&CK Alignment (Observed TTPs)
- [[T0812 - Default Credentials]]
- [[T0883 - Internet Accessible Device]]
- [[T0814 - Denial of Service]]
- [[T0826 - Loss of Availability]]
- [[T0828 - Loss of Productivity and Revenue]]
- [[T0829 - Loss of View]]

## 7. Defensive Considerations
1. **Eliminate default credentials** on OT devices; enforce unique strong credentials and MFA where possible.
2. **Reduce internet exposure**: remove direct exposure of PLC/HMI; require VPN + strong auth; segment OT networks.
3. **OT monitoring**: alert on remote logins, configuration changes, and HMI graphic/logic changes.
4. **Asset inventory**: locate all Unitronics/OT devices, including cellular modems and unmanaged gateways.

## 8. Analyst Notes
This campaign is a strong example of how **basic hygiene failures** (internet exposure + default passwords) can enable disruptive outcomes without sophisticated malware.

## 9. References (APA)
- Bajak, F., & Levy, M. (2023, December 2). *Breaches by Iran-affiliated hackers spanned multiple U.S. states, federal agencies say.* AP News. https://apnews.com/  
- DHS/CISA. (2023, November 28). *Exploitation of Unitronics PLCs used in Water and Wastewater Systems.* CISA. https://www.cisa.gov/news-events/alerts/2023/11/28/exploitation-unitronics-plcs-used-water-and-wastewater-systems  
- DHS/CISA. (2023, December 1). *IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including U.S. Water and Wastewater Systems Facilities.* CISA. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a  
- Tarabay, J., & Manson, K. (2023, December 22). *Iranian-Linked Hacks Expose Failure to Safeguard US Water System.* Bloomberg. https://www.bloomberg.com/  
- MITRE ATT&CK. (n.d.). *Unitronics Defacement Campaign (C0031).* https://attack.mitre.org/campaigns/C0031/
