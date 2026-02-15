---
entity_type: campaign

campaign_name: "Midnight Blizzard RDP Configuration File Spearphishing (2024)"
campaign_id: "MSFT-2024-MIDNIGHTBLIZZARD-RDP"

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29 (G0016)]]"
suspected_actors: []

attribution_confidence: "3-high"
confidence_notes: "Microsoft attributes this activity to Midnight Blizzard; Midnight Blizzard is listed as an associated name for APT29 (G0016) in MITRE ATT&CK."

first_observed: "2024-10"
last_observed: ""
campaign_status: "active"

primary_objectives:
  - "espionage_like"
secondary_objectives:
  - "long_term_access"

target_sectors:
  - "Government"
  - "Defense"
  - "Think tanks / policy"
target_regions:
  - "Europe"
  - "North America"
target_technologies:
  - "Email clients and mail gateways"
  - "Remote Desktop Protocol (RDP)"
  - "Windows endpoints"

initial_access_vectors:
  - "Spearphishing Attachment"
key_ttp_themes:
  - "RDP configuration files as lure/attachment"
  - "Remote access enablement via RDP workflows"

associated_ttps:
  - "T1566.001 - Phishing: Spearphishing Attachment"
  - "T1021.001 - Remote Services: Remote Desktop Protocol"

malware_families: []
tools_used: []

infrastructure_patterns:
  - "[[Spearphishing Operations]]"
  - "[[Remote Access Enablement]]"

notable_victims: []
related_incidents: []

risk_level: "high"
impact_assessment: "Midnight Blizzard used spearphishing emails with RDP configuration file attachments to facilitate remote access workflows and increase the likelihood of successful operator access to targeted environments."

intel_sources:
  - "https://www.microsoft.com/en-us/security/blog/2024/10/22/midnight-blizzard-conducting-spear-phishing-campaign-using-rdp-files/"
  - "https://attack.mitre.org/groups/G0016/"
  - "https://attack.mitre.org/techniques/T1566/001/"
  - "https://attack.mitre.org/techniques/T1021/001/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-10"
updated: "2026-01-10"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Midnight Blizzard RDP Configuration File Spearphishing (2024) (MSFT-2024-MIDNIGHTBLIZZARD-RDP)

## 1. Campaign Overview
Microsoft reported that **Midnight Blizzard** conducted a spearphishing campaign using **RDP configuration files** as attachments. The operational purpose appears aligned with enabling or accelerating remote access into targeted environments by leveraging user interaction with RDP workflows.

This campaign is a reminder that “low-malware” intrusion paths can still be operationally effective when paired with identity and remote access tradecraft.

## 2. Attribution Assessment
- Microsoft attributes the campaign to **Midnight Blizzard** and provides detection/defense guidance.
- MITRE lists **Midnight Blizzard** as an associated name for **APT29 (G0016)**.

**Attribution Confidence: 3-high**

## 3. Objectives & Intent
- Establish or enable **remote access** pathways using RDP workflows
- Support espionage-like operations through durable interactive access (where successful)

## 4. Targeting Analysis

### Sectors Targeted
- Government, defense, policy-oriented organizations (as described in public reporting themes)

### Regions Targeted
- Europe
- North America

### Technologies / Platforms Targeted
- Email delivery pipelines (for lure delivery)
- Windows endpoints initiating RDP sessions

## 5. Campaign Tradecraft
High-level flow:
1) Deliver spearphishing email with **RDP file attachment**
2) User opens/uses attachment; remote access workflow is initiated
3) Operator leverages resulting access/telemetry to progress operations

## 6. MITRE ATT&CK Alignment

### Techniques Observed
- [[T1566.001 - Phishing: Spearphishing Attachment]]
- [[T1021.001 - Remote Services: Remote Desktop Protocol]]

### Notable Tradecraft Characteristics
- Use of “benign-seeming” **configuration artifacts** as lures
- Reliance on user interaction and remote access conventions rather than overt malware delivery
- Defensive value of correlating **email telemetry → RDP connection attempts** in close time proximity

## 7. Malware & Tooling
No specific malware families are required for the primary lure mechanism; focus is on email + RDP workflow.

## 8. Infrastructure & Operational Patterns
- [[Spearphishing Operations]] for delivery
- [[Remote Access Enablement]] via RDP-centric workflows

## 9. Timeline of Campaign Activity (Table + Chronos)

### Timeline (Markdown)
|Date|Event|
|---|---|
|**2024-10-22**|Microsoft publishes research describing the spearphishing campaign using RDP files.|
|**2024-10**|Observed campaign window (public reporting timebox).|

### Timeline (Chronos)
```chronos
- [2024-10-22]: Microsoft publishes research describing the spearphishing campaign using RDP files.
- [2024-10]: Observed campaign window (public reporting timebox).
```

## 10. Notable Victims & Impact
Victim specifics are not comprehensively disclosed. Likely impacts include:
- Successful remote access sessions enabling additional discovery and collection
- Increased risk to organizations where RDP is accessible or where users frequently initiate RDP sessions

## 11. Related Campaigns & Activity
- Related to broader Midnight Blizzard operations where identity access and social engineering are used to enable espionage outcomes; direct linkages should be based on environment-specific evidence.

## 12. Known Indicators (Contextual)
*(Pattern-based pivots only; do not treat as durable IOCs.)*
- Email attachments containing .rdp files delivered to targeted recipients
- RDP session initiation shortly after email receipt/open events
- RDP connections to new/unusual external destinations or jump hosts

## 13. Defensive Considerations
- Email controls:
  - Restrict or quarantine high-risk attachment types (including .rdp where feasible)
  - Improve phishing detection for attachment-based lures
- RDP governance:
  - Limit outbound RDP where not required; enforce jump-box usage
  - Monitor unusual RDP destinations and session patterns
- Correlation detections:
  - Alert on email with RDP attachment followed by RDP session initiation from same endpoint/user

## 14. Analyst Notes
- This note keeps technique mapping tight to source-supported behaviors.
- Highest-value pivot is correlation across **EmailEvents + DeviceNetworkEvents + RDP session artifacts**.
- Confidence recap:
  - Attribution: high
  - Tradecraft completeness: medium (public narrative is clear; operational details vary)

## 15. Further Reading / External Resources
- Microsoft research post (2024-10-22)
- MITRE APT29 (G0016) page
- ATT&CK technique references for spearphishing attachment and RDP remote services

## 16. References (APA)
- MITRE ATT&CK. (n.d.). *APT29 (G0016).* https://attack.mitre.org/groups/G0016/
- MITRE ATT&CK. (n.d.). *Phishing: Spearphishing Attachment (T1566.001).* https://attack.mitre.org/techniques/T1566/001/
- MITRE ATT&CK. (n.d.). *Remote Services: Remote Desktop Protocol (T1021.001).* https://attack.mitre.org/techniques/T1021/001/
- Microsoft. (2024, October 22). *Midnight Blizzard conducting spear phishing campaign using RDP files.* Microsoft Security Blog. https://www.microsoft.com/en-us/security/blog/2024/10/22/midnight-blizzard-conducting-spear-phishing-campaign-using-rdp-files/
