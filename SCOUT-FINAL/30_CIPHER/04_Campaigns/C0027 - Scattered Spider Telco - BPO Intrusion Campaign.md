---
entity_type: campaign

campaign_name: "C0027 (Scattered Spider Telco/BPO Intrusion Campaign)"
campaign_id: "C0027"
aliases: []

description: "Financially motivated campaign targeting telecommunications and BPO companies, involving social engineering, SIM swapping, and attempts to leverage access into mobile carrier networks."

attribution:
  attributed:
    - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|G1015 - Scattered Spider]]"
  suspected: []
  attribution_confidence: "high"

first_observed: "2022-06"
last_observed: "2022-12"
campaign_status: "inactive"

primary_objectives:
  - "Financially motivated access"
  - "SIM swapping enablement"
secondary_objectives:
  - "Persistence in cloud and remote access"
  - "Credential harvesting and privilege escalation"

target_sectors:
  - "Telecommunications"
  - "Business Process Outsourcing (BPO)"
target_regions:
  - "Global"
target_technologies:
  - "Azure AD / Microsoft 365"
  - "Citrix / VPN"
  - "AWS (credential manipulation reported)"

initial_access_vectors:
  - "Social engineering (voice + SMS phishing)"
  - "Exploit of public-facing application (CVE-2021-35464 in ForgeRock OpenAM per reporting)"
  - "Credential harvesting"

key_ttp_themes:
  - "Impersonation and social engineering"
  - "Cloud identity discovery + persistence"
  - "Remote tooling and proxying"

associated_ttps:
  - "T1656 - Impersonation"
  - "T1566.004 - Spearphishing Voice"
  - "T1589.001 - Credentials"
  - "T1133 - External Remote Services"
  - "T1621 - Multi-Factor Authentication Request Generation"
  - "T1087.003 - Email Account"
  - "T1087.004 - Cloud Account"
  - "T1098.001 - Additional Cloud Credentials"
  - "T1090 - Proxy"
  - "T1003.006 - DCSync"
  - "T1190 - Exploit Public-Facing Application"
  - "T1105 - Ingress Tool Transfer"

malware_families: []
tools_used:
  - "[[30_CIPHER/05_Malware/S0357 - Impacket|Impacket (S0357)]]"

infrastructure_patterns:
  - "Credential-harvesting sites"
  - "Use of public web services for tool distribution"
  - "Reverse proxy / tunneling for persistence"

risk_level: "high"
impact_assessment: "High business impact driven by identity compromise, potential telecom carrier access, and downstream fraud (SIM swapping)."

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0027/"
  - "https://www.crowdstrike.com/en-us/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a"
  - "https://www.securityweek.com/scattered-spider-cybercrime-group-targets-mobile-carriers-telecom-bpo-firms/"
  - "https://www.darkreading.com/threat-intelligence/cybercriminals-target-telecom-provider-networks"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# C0027 (C0027)

## 1. Executive Summary
**C0027** is a financially motivated campaign attributed to **[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|G1015 - Scattered Spider]]**, targeting **telecommunications** and **BPO** organizations (June–December 2022). Tradecraft emphasizes **social engineering**, **SIM swapping**, and **cloud identity abuse**.

## 2. Attribution & Victimology
- **Attributed actor:** [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|G1015 - Scattered Spider]]
- **Victim profile:** Telco + BPO providers; objective includes access enabling SIM swaps and telecom network pivoting

## 3. Malware & Tooling (Atomic Links)
- [[30_CIPHER/05_Malware/S0357 - Impacket|Impacket (S0357)]]

## 4. Associated MITRE ATT&CK Techniques (Flat TTP Links)
- [[T1656 - Impersonation]]
- [[T1566.004 - Spearphishing Voice]]
- [[T1589.001 - Credentials]]
- [[T1133 - External Remote Services]]
- [[T1621 - Multi-Factor Authentication Request Generation]]
- [[T1087.003 - Email Account]]
- [[T1087.004 - Cloud Account]]
- [[T1098.001 - Additional Cloud Credentials]]
- [[T1090 - Proxy]]
- [[T1003.006 - DCSync]]
- [[T1190 - Exploit Public-Facing Application]]
- [[T1105 - Ingress Tool Transfer]]

## 5. Infrastructure & Access Patterns
- Voice/SMS phishing → credential harvesting
- RMM tooling and proxying/tunneling used for remote control and persistence
- Tool download via common web services (reported)

## 6. Timeline of Campaign Activity (Chronos + Markdown)
```chronos
- [2022-06] Earliest observed activity timeframe per ATT&CK campaign dating.
- [2022-12-02] CrowdStrike publishes detailed campaign analysis.
- [2022-12] Last observed activity timeframe per ATT&CK campaign dating.
```

| Date | Event |
|---|---|
| 2022-06 | Earliest observed activity timeframe per ATT&CK campaign dating. |
| 2022-12-02 | CrowdStrike publishes detailed campaign analysis. |
| 2022-12 | Last observed activity timeframe per ATT&CK campaign dating. |

## 7. Detection & Hunting Ideas
- Detect anomalous MFA push fatigue patterns and new device registrations.
- Alert on suspicious helpdesk interactions + password reset bursts + new VPN/Citrix sessions.
- Hunt for Impacket lateral movement artifacts and unusual WMI execution chains.

## 8. References (APA)
- Parisi, T. (2022, December 2). *Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies*. CrowdStrike. https://www.crowdstrike.com/en-us/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/
- CISA. (2023). *AA23-320A: Scattered Spider*. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- Arghire, I. (2022, December 6). *‘Scattered Spider’ Cybercrime Group Targets Mobile Carriers via Telecom, BPO Firms*. SecurityWeek. https://www.securityweek.com/scattered-spider-cybercrime-group-targets-mobile-carriers-telecom-bpo-firms/
- Dark Reading. (2023, January 19). *Cybercriminals Target Telecom Provider Networks*. https://www.darkreading.com/threat-intelligence/cybercriminals-target-telecom-provider-networks
- MITRE ATT&CK. (n.d.). *Campaign C0027: C0027*. https://attack.mitre.org/campaigns/C0027/
