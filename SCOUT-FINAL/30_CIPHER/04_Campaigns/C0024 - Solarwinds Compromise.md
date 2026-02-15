---
entity_type: campaign

campaign_name: "SolarWinds Compromise"
campaign_id: "C0024"
aliases: []

description: "Supply-chain compromise of SolarWinds Orion leading to widespread downstream intrusion activity using SUNBURST and follow-on tooling; publicly attributed to Russia’s SVR (APT29/Cozy Bear)."

attribution:
  attributed:
    - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]"
  suspected: []
  attribution_confidence: "high"

first_observed: "2019-09"
last_observed: "2020-12"
campaign_status: "inactive"

primary_objectives:
  - "Strategic espionage"
  - "Access to government and enterprise environments"
secondary_objectives:
  - "Credential theft and cloud access expansion"
  - "Long-dwell persistence"

target_sectors:
  - "Government"
  - "Technology"
  - "Critical infrastructure (secondary exposure via downstream victims)"
target_regions:
  - "Global"
target_technologies:
  - "Windows"
  - "Microsoft 365 / Azure AD (post-compromise activity reported broadly)"
  - "SolarWinds Orion"

initial_access_vectors:
  - "Software supply-chain compromise"
  - "Trusted signed update delivery"

key_ttp_themes:
  - "Stealthy backdoor via trusted update channel"
  - "Follow-on payload staging and lateral movement"
  - "Credential access and token abuse (reported broadly in public advisories)"

associated_ttps:
  - "T1195.002 - Compromise Software Supply Chain"
  - "T1071.001 - Web Protocols"
  - "T1105 - Ingress Tool Transfer"
  - "T1059.001 - PowerShell"
  - "T1078 - Valid Accounts"
  - "T1003.001 - LSASS Memory"

malware_families:
  - "[[30_CIPHER/05_Malware/S0559 - SUNBURST|SUNBURST (S0559)]]"
  - "[[30_CIPHER/05_Malware/S0560 - TEARDROP|TEARDROP (S0560)]]"
  - "[[30_CIPHER/05_Malware/S0561 - Raindrop|Raindrop (S0561)]]"

infrastructure_patterns:
  - "C2 over web protocols"
  - "Staged deployment of follow-on payloads"

risk_level: "critical"
impact_assessment: "Large-scale strategic compromise via trusted vendor channel; high systemic risk due to downstream victim spread and stealthy long-dwell access."

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0024/"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a"
  - "https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html"
  - "https://www.microsoft.com/security/blog/2020/12/13/customers-protecting-against-solarwinds-supply-chain-attack/"
  - "https://www.ncsc.gov.uk/news/joint-statement-on-solarwinds"
  - "https://www.cisa.gov/sites/default/files/publications/CISA_Fact_Sheet_Russian_SVR_Activities_Related_to_SolarWinds_Compromise_508C.pdf"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# SolarWinds Compromise (C0024)

## 1. Executive Summary
The **SolarWinds Compromise** was a high-impact **software supply-chain intrusion** in which adversaries inserted malicious code into SolarWinds Orion builds and distributed trojanized updates. Public reporting and government advisories broadly attribute activity to **[[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]** (SVR).

## 2. Attribution & Victimology
- **Attributed actor:** [[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]
- **Victim profile:** Broad downstream victim set (government + enterprise), selected follow-on targeting

## 3. Malware & Tooling (Atomic Links)
- [[30_CIPHER/05_Malware/S0559 - SUNBURST|SUNBURST (S0559)]]
- [[30_CIPHER/05_Malware/S0560 - TEARDROP|TEARDROP (S0560)]]
- [[30_CIPHER/05_Malware/S0561 - Raindrop|Raindrop (S0561)]]

## 4. Associated MITRE ATT&CK Techniques (Flat TTP Links)
- [[T1195.002 - Compromise Software Supply Chain]]
- [[T1071.001 - Web Protocols]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1059.001 - PowerShell]]
- [[T1078 - Valid Accounts]]
- [[T1003.001 - LSASS Memory]]

## 5. Infrastructure & Access Patterns
- Trusted update channel used for initial foothold at scale
- Web-based C2 and staged follow-on deployment

## 6. Timeline of Campaign Activity (Chronos + Markdown)
```chronos
- [2019-09] Earliest observed timeframe referenced in public reporting/ATT&CK campaign dating.
- [2020-12] Public disclosure and broad incident response actions begin.
```

| Date | Event |
|---|---|
| 2019-09 | Earliest observed timeframe referenced in public reporting/ATT&CK campaign dating. |
| 2020-12 | Public disclosure and broad incident response actions begin. |

## 7. Detection & Hunting Ideas
- Audit SolarWinds Orion build/update integrity and historical telemetry.
- Hunt for unusual Orion process network beacons and child process spawning.
- Validate identity logs for anomalous authentication/token activity tied to privileged accounts.

## 8. References (APA)
- CISA. (2020). *Alert AA20-352A: Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure, and Private Sector Organizations*. https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a
- CISA. (2021). *Fact Sheet: Russian SVR Activities Related to the SolarWinds Compromise* (PDF). https://www.cisa.gov/sites/default/files/publications/CISA_Fact_Sheet_Russian_SVR_Activities_Related_to_SolarWinds_Compromise_508C.pdf
- FireEye. (2020, December). *Evasive attacker leverages SolarWinds supply chain compromises with SUNBURST backdoor*. https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html
- Microsoft. (2020, December 13). *Customers protecting against SolarWinds supply chain attack*. https://www.microsoft.com/security/blog/2020/12/13/customers-protecting-against-solarwinds-supply-chain-attack/
- NCSC. (2020). *Joint statement on SolarWinds*. https://www.ncsc.gov.uk/news/joint-statement-on-solarwinds
- MITRE ATT&CK. (n.d.). *Campaign C0024: SolarWinds Compromise*. https://attack.mitre.org/campaigns/C0024/
