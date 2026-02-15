---
entity_type: campaign

campaign_name: "HomeLand Justice"
campaign_id: "C0038"

associated_actors: []
suspected_actors: []

attribution_confidence: "2-medium"
confidence_notes: "Multiple authoritative sources describe Iranian state cyber actors operating under the 'HomeLand Justice' persona targeting Albania; however, public reporting does not consistently map this activity to a single, stable ATT&CK group ID."

first_observed: "2021-05"
last_observed: "2022-09"
campaign_status: "concluded"

primary_objectives:
  - "disruption"
  - "data_theft"
secondary_objectives:
  - "reputation_damage"
  - "business_disruption"

target_sectors:
  - "government"
target_regions:
  - "Albania"
target_technologies:
  - "government enterprise networks"
  - "identity and email systems (contextual)"

initial_access_vectors:
  - "unknown (public summaries indicate early access established prior to disruptive phase)"
key_ttp_themes:
  - "long-dwell prepositioning"
  - "data exfiltration and public leaking"
  - "destructive impact operations"

associated_ttps: []

malware_families: []
tools_used: []

infrastructure_patterns:
  - "[[Ephemeral Infrastructure]]"

notable_victims:
  - "Government of Albania"
related_incidents: []

risk_level: "critical"
impact_assessment: "Campaign involved disruptive/destructive actions against Albanian government networks, including data theft/leaks and operational disruption impacts."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0038/"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a"
  - "https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/"
  - "https://cyberlaw.ccdcoe.org/wiki/Homeland_Justice_operations_against_Albania_%282022%29"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# HomeLand Justice (C0038)

## 1. Campaign Overview
HomeLand Justice describes a disruptive campaign targeting Albanian government networks, with reporting indicating initial access as early as May 2021 and culminating in disruptive/destructive actions and data leaks in 2022. U.S. government and vendor reporting describe Iranian state cyber actors using the “HomeLand Justice” persona in connection with the operation.

## 2. Attribution Assessment
- U.S. CISA advisory attributes the Albania operation to Iranian state cyber actors identifying as “HomeLand Justice.”
- Microsoft analysis discusses Iranian-linked attacks against the Albanian government and the “Homeland Justice” persona used to amplify messaging and leaks.
- Independent analytical summaries also generally attribute the activity to Iran, but do not always provide a single stable group mapping.

**Attribution Confidence: 2-medium**

## 3. Objectives & Intent
Observed intent combines:
- **Disruption/Destruction:** operational disruption against government networks.
- **Data Theft + Leverage:** theft and public leaking of data to amplify political messaging and reputational harm.

## 4. Targeting Analysis
- **Sectors Targeted:** Government.
- **Regions Targeted:** Albania.
- **Technologies / Platforms Targeted:** Government enterprise networks (specific stack varies by victim and disclosure).

## 5. Campaign Tradecraft
Assessed high-level flow (public summaries):
Initial access (pre-2022) → lateral movement/persistence over extended dwell → data collection/exfiltration → disruptive/destructive actions + leak operations.

## 6. MITRE ATT&CK Alignment
- **Techniques Observed:** Not enumerated here to avoid over-claiming; refer to the CISA advisory and MITRE campaign entry for sourced technique-level details.
- **Notable Tradecraft Characteristics**
  - Long dwell (multi-month) prior to disruptive phase.
  - Blended data leak + disruption operations.

## 7. Malware & Tooling
Public reporting references multiple tools and behaviors; campaign-specific tooling varies across reports. This note does not list specific malware families absent consistent, campaign-scoped sourcing.

## 8. Infrastructure & Operational Patterns
- [[Ephemeral Infrastructure]] may be used for leak hosting, staging, or transient C2; validate with incident-specific telemetry.

## 9. Timeline of Campaign Activity (Table + Chronos)

**Timeline (Markdown)**

|Date|Event|
|---|---|
|**2021-05**|Reported initial access period begins for HomeLand Justice activity (per MITRE campaign summary).|
|**2022-07**|Destructive/disruptive activity against Albanian government networks publicly reported; CISA issues advisory.|
|**2022-09**|Additional disruptive activity and leak-related developments reported (per MITRE campaign summary).|

**Timeline (Chronos)**

```chronos
- [2021-05]: Initial access established (per MITRE campaign summary).
- [2022-07]: Destructive/disruptive operation publicly reported; CISA publishes advisory AA22-264A.
- [2022-09]: Additional disruptive activity phase reported (per MITRE campaign summary).
```

## 10. Notable Victims & Impact
- **Notable Victims:** Government of Albania.
- **Impact:** Disruption of government services and reputational harm through data leak operations (details vary by disclosure).

## 11. Related Campaigns & Activity
- This activity is frequently discussed in the context of Iranian state cyber operations and influence messaging; treat “HomeLand Justice” as a persona/label that may not map 1:1 to a single enduring actor set.

## 12. Known Indicators (Contextual)
No IOCs included here. Suggested pivots:
- Leak-site infrastructure used for disclosure.
- Messaging artifacts and personas used to amplify claims (high volatility; may be spoofed).

## 13. Defensive Considerations
- Government networks: prioritize identity hardening, privileged access governance, and lateral movement detection.
- Prepare for destructive operations: offline backups, immutable backups, IR exercises, crisis comms and continuity planning.
- Monitor for data theft signals (mass archiving, unusual cloud sync/exfil patterns).

## 14. Analyst Notes
- Mapping to a single ATT&CK group ID is not stable in public sources; keep attribution at “Iranian state cyber actors” unless a reliable crosswalk is sourced.
- If investigating: preserve evidence early (email, endpoint, VPN/router logs) and track dwell indicators.

## 15. Further Reading / External Resources
- CISA AA22-264A — https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a
- Microsoft analysis — https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/
- MITRE ATT&CK Campaign: HomeLand Justice (C0038) — https://attack.mitre.org/campaigns/C0038/
- CCDCOE Cyber Law wiki summary — https://cyberlaw.ccdcoe.org/wiki/Homeland_Justice_operations_against_Albania_%282022%29

## 16. References (APA)
- CISA. (2022, September 23). *Iranian State Actors Conduct Cyber Operations Against the Government of Albania.* Cybersecurity Advisory AA22-264A. https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a
- Microsoft. (2022, September 8). *Microsoft investigates Iranian attacks against the Albanian government.* Microsoft Security Blog. https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/
- MITRE. (2024, October 31). *HomeLand Justice (C0038).* MITRE ATT&CK. https://attack.mitre.org/campaigns/C0038/
- CCDCOE. (2024, March 1). *Homeland Justice operations against Albania (2022).* CCDCOE Cyber Law wiki. https://cyberlaw.ccdcoe.org/wiki/Homeland_Justice_operations_against_Albania_%282022%29
