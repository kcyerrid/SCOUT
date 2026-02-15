---
entity_type: campaign

campaign_name: "2015 Ukraine Electric Power Attack"
campaign_id: "C0028"
aliases: []

description: "Sandworm Team campaign using BlackEnergy (BlackEnergy3) and KillDisk to disrupt Ukrainian power grid operations; widely recognized as the first major publicly known cyber-induced power outage."

attribution:
  attributed:
    - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|G0034 - Sandworm Team]]"
  suspected: []
  attribution_confidence: "high"

first_observed: "2015-12"
last_observed: "2016-01"
campaign_status: "inactive"

primary_objectives:
  - "Operational disruption (power outage)"
secondary_objectives:
  - "Credential theft and lateral movement"
  - "Destructive cleanup / recovery impediment"

target_sectors:
  - "Energy (electric utilities)"
target_regions:
  - "Ukraine"
target_technologies:
  - "ICS/SCADA"
  - "Windows"

initial_access_vectors:
  - "Spearphishing attachment with malicious macros (reported)"
  - "Credential theft and remote access pivoting (reported)"

key_ttp_themes:
  - "ICS manipulation and remote operations"
  - "Credential theft + lateral tool transfer"
  - "Defense impairment + destructive wiping"

associated_ttps:
  - "T1566.001 - Spearphishing Attachment"
  - "T1071.001 - Web Protocols"
  - "T1059.005 - Visual Basic"
  - "T1133 - External Remote Services"
  - "T1562.001 - Disable or Modify Tools"
  - "T1070.004 - File Deletion"
  - "T1056.001 - Keylogging"
  - "T1570 - Lateral Tool Transfer"
  - "T1055 - Process Injection"
  - "T1218.011 - Rundll32"
  - "T1204.002 - Malicious File"
  - "T0855 - Unauthorized Command Message"
  - "T0857 - System Firmware"
  - "T0886 - Remote Services"
  - "T0859 - Valid Accounts"

malware_families:
  - "[[30_CIPHER/05_Malware/S0089 - BlackEnergy|BlackEnergy (S0089)]]"
  - "[[30_CIPHER/05_Malware/S0607 - KillDisk|KillDisk (S0607)]]"

tools_used: []
infrastructure_patterns:
  - "Remote access into OT environment via stolen credentials"
  - "Manual/interactive control actions inside ICS environment (reported)"
  - "Destructive wiping to impede recovery"

risk_level: "critical"
impact_assessment: "Demonstrated real-world disruption of electric grid operations and destructive actions affecting operator workstations and recovery."

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0028/"
  - "https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf"
  - "https://www.wired.com/2016/01/everything-we-know-about-ukraines-power-plant-hack/"
  - "https://www.justice.gov/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware"
  - "https://nsarchive.gwu.edu/document/25046-analysis-cyber-attack-ukrainian-power"
  - "https://www.zdnet.com/article/how-hackers-attacked-ukraines-power-grid-implications-for-industrial-iot-security/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# 2015 Ukraine Electric Power Attack (C0028)

## 1. Executive Summary
The **2015 Ukraine Electric Power Attack** is attributed to **[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|G0034 - Sandworm Team]]** and involved **[[30_CIPHER/05_Malware/S0089 - BlackEnergy|BlackEnergy (S0089)]]** and **[[30_CIPHER/05_Malware/S0607 - KillDisk|KillDisk (S0607)]]**. It is widely cited as the first major public example of a cyber operation causing a power outage.

## 2. Attribution & Victimology
- **Attributed actor:** [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|G0034 - Sandworm Team]]
- **Victim profile:** Ukrainian electric distribution/transmission operators

## 3. Malware & Tooling (Atomic Links)
- [[30_CIPHER/05_Malware/S0089 - BlackEnergy|BlackEnergy (S0089)]]
- [[30_CIPHER/05_Malware/S0607 - KillDisk|KillDisk (S0607)]]

## 4. Associated MITRE ATT&CK Techniques (Flat TTP Links)
- [[T1566.001 - Spearphishing Attachment]]
- [[T1071.001 - Web Protocols]]
- [[T1059.005 - Visual Basic]]
- [[T1133 - External Remote Services]]
- [[T1562.001 - Disable or Modify Tools]]
- [[T1070.004 - File Deletion]]
- [[T1056.001 - Keylogging]]
- [[T1570 - Lateral Tool Transfer]]
- [[T1055 - Process Injection]]
- [[T1218.011 - Rundll32]]
- [[T1204.002 - Malicious File]]
- [[T0855 - Unauthorized Command Message]]
- [[T0857 - System Firmware]]
- [[T0886 - Remote Services]]
- [[T0859 - Valid Accounts]]

## 5. Infrastructure & Access Patterns
- Remote access to OT via compromised credentials and dual-homed pathways (reported)
- Destructive wiping and operational lockout actions to impede recovery (reported)

## 6. Timeline of Campaign Activity (Chronos + Markdown)
```chronos
- [2015-12] Attack timeframe begins (ATT&CK campaign dating).
- [2016-01] Last observed timeframe (ATT&CK campaign dating).
- [2016] Booz Allen publishes “When The Lights Went Out” (widely cited analysis).
```

| Date | Event |
|---|---|
| 2015-12 | Attack timeframe begins (ATT&CK campaign dating). |
| 2016-01 | Last observed timeframe (ATT&CK campaign dating). |
| 2016 | Booz Allen publishes “When The Lights Went Out” (widely cited analysis). |

## 7. Detection & Hunting Ideas
- Alert on macro-enabled Office documents and unusual VBA execution on user workstations.
- Monitor for OT-adjacent remote access sessions and anomalous operator workstation interactions.
- Hunt for KillDisk-like destructive behaviors and firmware modification workflows.

## 8. References (APA)
- Booz Allen Hamilton. (2016). *When The Lights Went Out* (PDF). https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf
- Greenberg, A. (2016, January). *Everything We Know About Ukraine's Power Plant Hack*. Wired. https://www.wired.com/2016/01/everything-we-know-about-ukraines-power-plant-hack/
- U.S. Department of Justice. (2020). *Six Russian GRU officers charged in connection with worldwide deployment of destructive malware and other disruptive actions*. https://www.justice.gov/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware
- Electricity ISAC & SANS ICS. (2016). *Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case*. National Security Archive. https://nsarchive.gwu.edu/document/25046-analysis-cyber-attack-ukrainian-power
- McLellan, C. (2016, March 4). *How hackers attacked Ukraine's power grid: Implications for Industrial IoT security*. ZDNet. https://www.zdnet.com/article/how-hackers-attacked-ukraines-power-grid-implications-for-industrial-iot-security/
- MITRE ATT&CK. (n.d.). *Campaign C0028: 2015 Ukraine Electric Power Attack*. https://attack.mitre.org/campaigns/C0028/
