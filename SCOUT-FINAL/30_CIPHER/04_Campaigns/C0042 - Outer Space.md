---
entity_type: campaign

campaign_name: "Outer Space"
campaign_id: "C0042"

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig (G0049)]]"
suspected_actors: []

attribution_confidence: "3-high"
confidence_notes: "ESET research and MITRE attribute Outer Space to OilRig with consistent tooling (SampleCheck5000, Solar) and targeting."

first_observed: "2021-01"
last_observed: "2021-12"
campaign_status: "concluded"

primary_objectives:
  - "espionage_like"
secondary_objectives:
  - "long_term_access"
  - "competitive_advantage"

target_sectors:
  - "unknown"
target_regions:
  - "Israel"
target_technologies:
  - "Microsoft 365 (reported account creation/C2 aspects in summaries)"
  - "Windows environments"

initial_access_vectors:
  - "unknown (campaign reporting emphasizes subsequent malware/tooling and infrastructure use)"
key_ttp_themes:
  - "downloader + backdoor staging"
  - "compromised server C2"
  - "cloud account use for operations"

associated_ttps:
  - "T1059.005 - Visual Basic"
  - "T1584.004 - Server"
  - "T1585.003 - Cloud Accounts"
  - "T1105 - Ingress Tool Transfer"
  - "T1071.001 - Web Protocols"

malware_families:
  - "[[30_CIPHER/05_Malware/S1168 - SampleCheck5000|SampleCheck5000 (S1168)]]"
  - "[[30_CIPHER/05_Malware/S1166 - Solar|Solar (S1166)]]"
tools_used: []

infrastructure_patterns:
  - "[[Compromised Web Server C2]]"
  - "[[Cloud Accounts for C2]]"
  - "[[Ephemeral Infrastructure]]"

notable_victims:
  - "Israeli organizations (not exhaustively enumerated publicly)"
related_incidents:
  - "[[Juicy Mix]]"

risk_level: "high"
impact_assessment: "Espionage-focused campaign leveraged staged downloaders/backdoors and compromised infrastructure to support sustained collection against Israeli targets."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0042/"
  - "https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/"
  - "https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/"
  - "https://attack.mitre.org/software/S1168/"
  - "https://attack.mitre.org/software/S1166/"
  - "https://attack.mitre.org/groups/G0049/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Outer Space (C0042)

## 1. Campaign Overview
Outer Space describes a 2021 OilRig campaign targeting Israeli organizations, using the SampleCheck5000 downloader to deliver additional payloads and the Solar backdoor to support follow-on access and collection. Public research (ESET) analyzes Outer Space alongside Juicy Mix, highlighting tooling evolution and operational patterns consistent with OilRig’s established espionage posture.

## 2. Attribution Assessment
- MITRE attributes Outer Space to [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig (G0049)]] and documents associated tooling (SampleCheck5000, Solar).
- ESET provides a detailed campaign analysis linking tradecraft, tooling, and target profile to OilRig.

**Attribution Confidence: 3-high**

## 3. Objectives & Intent
Primary intent assessed as espionage-like:
- Establish persistent footholds and stage collection/exfiltration tooling.
- Maintain long-term access to sensitive organizational information in targeted Israeli entities.

## 4. Targeting Analysis
- **Sectors Targeted:** Not consistently enumerated publicly; “Israeli organizations” as a broad descriptor.
- **Regions Targeted:** Israel.
- **Technologies / Platforms Targeted:** Windows endpoints; reported use of cloud accounts and compromised servers for C2 elements.

## 5. Campaign Tradecraft
Initial access (varies/undisclosed) → downloader (SampleCheck5000) stages payloads → Solar backdoor establishes operational capability → C2 via compromised servers and/or cloud-linked channels → collection/exfiltration (incident-specific).

## 6. MITRE ATT&CK Alignment
- **Techniques Observed**
  - [[T1059.005 - Visual Basic]] (VBS droppers reported in campaign summaries)
  - [[T1584.004 - Server]] (compromised server infrastructure)
  - [[T1585.003 - Cloud Accounts]] (reported creation/use)
  - [[T1105 - Ingress Tool Transfer]]
  - [[T1071.001 - Web Protocols]]
- **Notable Tradecraft Characteristics**
  - Modular staging (downloader → backdoor).
  - Compromised legitimate sites used as C2 nodes.
  - Cloud-account use to support operational resiliency (per MITRE summary).

## 7. Malware & Tooling
- **Malware Families**
  - [[30_CIPHER/05_Malware/S1168 - SampleCheck5000|SampleCheck5000 (S1168)]]
  - [[30_CIPHER/05_Malware/S1166 - Solar|Solar (S1166)]]
- **Tools**
  - Not exhaustively enumerated here; see ESET analysis for campaign tooling detail.

## 8. Infrastructure & Operational Patterns
- [[Compromised Web Server C2]]: use of compromised servers/sites to blend traffic and reduce bespoke infra.
- [[Cloud Accounts for C2]]: operational accounts created to support C2 or staging.
- [[Ephemeral Infrastructure]]: staging and redirect components may rotate across campaign phases.

## 9. Timeline of Campaign Activity (Table + Chronos)

**Timeline (Markdown)**

|Date|Event|
|---|---|
|**2021-01**|Campaign begins (first-seen window).|
|**2021-12**|Campaign last observed window.|
|**2023-09-21**|ESET publishes analysis covering Outer Space (2021) and Juicy Mix (2022) (contextual retrospective).|
|**2024-11-21**|MITRE campaign entry created/updated timeframe for C0042 (contextual publication metadata).|

**Timeline (Chronos)**

```chronos
- [2021-01]: MITRE first-seen window for Outer Space (C0042).
- [2021-12]: MITRE last-seen window for Outer Space (C0042).
- [2023-09-21]: ESET publishes “OilRig’s Outer Space and Juicy Mix” analysis (contextual).
- [2024-11-21]: MITRE creates campaign entry for C0042 (publication metadata).
```

## 10. Notable Victims & Impact
- **Notable Victims:** Israeli organizations (specific victims not exhaustively enumerated publicly).
- **Impact:** Sustained espionage risk—credential/data access, internal discovery, and potential long-term persistence.

## 11. Related Campaigns & Activity
- [[Juicy Mix]] (ESET analyzes alongside Outer Space as related OilRig operations with tooling evolution).
- Related: OilRig’s broader use of cloud service-powered downloaders (see ESET 2023 research).

## 12. Known Indicators (Contextual)
No IOCs included here. Pivots:
- Presence of SampleCheck5000 and Solar artifacts (hashes/domains are volatile; use threat intel feeds).
- Evidence of compromised legitimate servers used for C2.
- Creation/use of suspicious cloud email accounts for operational purposes.

## 13. Defensive Considerations
- Detect staged downloader behavior (initial lightweight implant retrieving second-stage payloads).
- Monitor outbound HTTP/S to unusual endpoints from user workstations/servers.
- Protect cloud identities and monitor for suspicious account creations and mailbox rules where applicable.
- Treat OilRig activity as persistent espionage—emphasize long-term hunting and retroactive log review.

## 14. Analyst Notes
- Outer Space overlaps conceptually with multiple OilRig campaigns; avoid over-associating incidents without tooling/infrastructure corroboration.
- Consider building atomic notes for related OilRig tooling and techniques as you enrich.

## 15. Further Reading / External Resources
- ESET: Outer Space & Juicy Mix — https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/
- MITRE ATT&CK Campaign (C0042) — https://attack.mitre.org/campaigns/C0042/
- MITRE Software: SampleCheck5000 (S1168) — https://attack.mitre.org/software/S1168/
- MITRE Software: Solar (S1166) — https://attack.mitre.org/software/S1166/
- MITRE Group: OilRig (G0049) — https://attack.mitre.org/groups/G0049/

## 16. References (APA)
- ESET Research. (2023, September 21). *OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes.* WeLiveSecurity. https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/
- ESET Research. (2023, December 14). *OilRig’s persistent attacks using cloud service-powered downloaders.* WeLiveSecurity. https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/
- MITRE. (2024, November 25). *Outer Space (C0042).* MITRE ATT&CK. https://attack.mitre.org/campaigns/C0042/
- MITRE. (2024, November 25). *SampleCheck5000 (S1168).* MITRE ATT&CK. https://attack.mitre.org/software/S1168/
- MITRE. (2024, November 21). *Solar (S1166).* MITRE ATT&CK. https://attack.mitre.org/software/S1166/
- MITRE. (2017). *OilRig (G0049).* MITRE ATT&CK. https://attack.mitre.org/groups/G0049/

## 17. SCOUT-CAM Prompt Reference
:contentReference[oaicite:0]{index=0}
