---
entity_type: campaign

campaign_name: "Operation Ghost"
campaign_id: "C0023"
aliases: []

description: "Cyber-espionage campaign linked to APT29 (The Dukes) leveraging stealthy tradecraft (including steganography) and multiple custom malware families targeting diplomatic and government entities."

attribution:
  attributed:
    - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]"
  suspected: []
  attribution_confidence: "high"

first_observed: "2013"
last_observed: "2019-10"
campaign_status: "inactive"

primary_objectives:
  - "Cyber espionage"
  - "Credential and document collection"
secondary_objectives:
  - "Long-term persistence"
  - "Covert command-and-control"

target_sectors:
  - "Government"
  - "Diplomatic organizations"
target_regions:
  - "Global"
target_technologies:
  - "Windows"

initial_access_vectors:
  - "Spearphishing (suspected/observed in reporting)"
  - "Post-compromise tool deployment"

key_ttp_themes:
  - "Covert C2 and payload delivery"
  - "Living-off-the-land tooling for movement/execution"
  - "Stealthy persistence and staged deployment"

associated_ttps:
  - "T1059.001 - PowerShell"
  - "T1071.001 - Web Protocols"
  - "T1105 - Ingress Tool Transfer"
  - "T1036.004 - Masquerade Task or Service"

malware_families:
  - "[[30_CIPHER/05_Malware/S0511 - RegDuke|RegDuke (S0511)]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]"

infrastructure_patterns:
  - "Steganography-based payload staging"
  - "HTTP-based C2"

risk_level: "high"
impact_assessment: "Primarily espionage-focused; impact driven by exposure of sensitive diplomatic/government communications and long-dwell collection."

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0023/"
  - "https://www.welivesecurity.com/2019/10/17/operation-ghost-dukes-never-left/"
  - "https://web-assets.esetstatic.com/wls/2019/10/ESET_Operation_Ghost_Dukes.pdf"
  - "https://www.eset.com/in/about/newsroom/press-releases/research/operation-ghost-the-dnc-hacking-group-dukes-still-attacks-government-targets-eset-discovers/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Operation Ghost (C0023)

## 1. Executive Summary
**Operation Ghost** is a cyber-espionage campaign attributed to **[[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]** (aka “The Dukes”). Public reporting describes long-running activity with an emphasis on **stealth**, including **steganography-assisted staging** and multiple bespoke malware families.

## 2. Attribution & Victimology
- **Attributed actor:** [[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]
- **Likely victim profile:** Government and diplomatic targets
- **Likely motivation:** Intelligence collection

## 3. Malware & Tooling (Atomic Links)
- [[30_CIPHER/05_Malware/S0511 - RegDuke|RegDuke (S0511)]]
- [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]

## 4. Associated MITRE ATT&CK Techniques (Flat TTP Links)
- [[T1059.001 - PowerShell]]
- [[T1071.001 - Web Protocols]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1036.004 - Masquerade Task or Service]]

## 5. Infrastructure & Access Patterns
- Covert staging/delivery mechanisms (including steganography described in public reporting)
- Web-protocol based communications for C2

## 6. Timeline of Campaign Activity (Chronos + Markdown)
```chronos
- [2013] Public reporting indicates campaign activity dating back to at least this year.
- [2019-10-17] Public disclosure: ESET publishes Operation Ghost research describing new tooling and tradecraft.
```

| Date | Event |
|---|---|
| 2013 | Public reporting indicates campaign activity dating back to at least this year. |
| 2019-10-17 | Public disclosure: ESET publishes Operation Ghost research describing new tooling and tradecraft. |

## 7. Detection & Hunting Ideas
- Look for suspicious image/media files used as droppers or carriers in unusual directories.
- Monitor for anomalous PowerShell execution chains tied to browser/network activity.
- Baseline legitimate PsExec usage; alert on off-hours usage and unusual admin shares.

## 8. References (APA)
- ESET Research. (2019, October 17). *Operation Ghost: The Dukes aren’t back – they never left*. WeLiveSecurity. https://www.welivesecurity.com/2019/10/17/operation-ghost-dukes-never-left/
- Faou, M., & ESET Research. (2019). *Operation Ghost: The Dukes aren’t back – they never left* (PDF). ESET. https://web-assets.esetstatic.com/wls/2019/10/ESET_Operation_Ghost_Dukes.pdf
- ESET. (2019). *Operation Ghost: The DNC hacking group “Dukes” still attacks government targets – ESET discovers* (Press release). https://www.eset.com/in/about/newsroom/press-releases/research/operation-ghost-the-dnc-hacking-group-dukes-still-attacks-government-targets-eset-discovers/
- MITRE ATT&CK. (n.d.). *Campaign C0023: Operation Ghost*. https://attack.mitre.org/campaigns/C0023/
