---
entity_type: campaign

campaign_name: "Pikabot Distribution February 2024"
campaign_id: "C0036"

associated_actors: []
suspected_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1037 - TA577|TA577 (G1037)]]"

attribution_confidence: "1-low"
confidence_notes: "MITRE documents the campaign but does not publicly attribute it to a specific actor. TA577 is listed by MITRE as an IAB that has distributed Pikabot; inclusion here is a low-confidence hypothesis, not a confirmed attribution."

first_observed: "2024-02"
last_observed: "2024-02"
campaign_status: "unknown"

primary_objectives:
  - "access_brokering"
  - "data_theft"
secondary_objectives:
  - "financial_gain"
  - "long_term_access"

target_sectors:
  - "unknown"
target_regions:
  - "unknown"
target_technologies:
  - "Windows endpoints"
  - "Email clients / email infrastructure"

initial_access_vectors:
  - "phishing link to ZIP payload"
key_ttp_themes:
  - "email-based initial access"
  - "loader/backdoor staging for follow-on payloads"

associated_ttps:
  - "T1566.002 - Spearphishing Link"
  - "T1204.001 - Malicious Link"
  - "T1105 - Ingress Tool Transfer"
  - "T1059.007 - JavaScript"
  - "T1027.009 - Embedded Payloads"

malware_families:
  - "[[30_CIPHER/05_Malware/S1145 - Pikabot|Pikabot (S1145)]]"
tools_used: []

infrastructure_patterns:
  - "[[Ephemeral Infrastructure]]"
  - "[[Phishing Infrastructure]]"

notable_victims: []
related_incidents: []

risk_level: "high"
impact_assessment: "Email-delivered Pikabot variants can establish initial access and enable rapid follow-on tooling (e.g., remote tooling, credential theft, ransomware precursors) depending on operator objectives."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0036/"
  - "https://www.elastic.co/security-labs/pikabot-i-choose-you"
  - "https://www.esentire.com/blog/the-rising-threat-of-pikabot"
  - "https://www.mcafee.com/blogs/other-blogs/mcafee-labs/distinctive-campaign-evolution-of-pikabot-malware/"
  - "https://attack.mitre.org/groups/G1037/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Pikabot Distribution February 2024 (C0036)

## 1. Campaign Overview
Pikabot Distribution February 2024 describes an email-driven initial access cluster where recipients were lured into interacting with embedded links that led to ZIP archives and script-based infection chains, resulting in the delivery of Pikabot. MITRE notes the February 2024 activity featured notable changes compared to prior 2023 variants.  

Public reporting on early 2024 Pikabot activity highlights rapid evolution of packing/unpacking and obfuscation approaches, consistent with an active loader ecosystem used to stage follow-on payloads.

## 2. Attribution Assessment
- MITRE documents the campaign timeline and high-level infection chain but does not provide a definitive public actor attribution.  
- TA577 is documented by MITRE as an initial access broker that has distributed Pikabot; however, no public source in the above set conclusively ties TA577 to C0036 specifically.  

**Attribution Confidence: 1-low**

## 3. Objectives & Intent
The most consistent intent pattern for Pikabot ecosystems is establishing a foothold (initial access) that enables follow-on delivery (credential theft tooling, remote tooling, ransomware precursors). Where direct evidence is unavailable for C0036, intent is assessed based on known loader usage patterns and reported Pikabot operational use in 2024.

## 4. Targeting Analysis
- **Sectors Targeted:** Unknown (public reporting emphasizes delivery mechanics over sector scope).  
- **Regions Targeted:** Unknown.  
- **Technologies / Platforms Targeted:** Windows endpoints; email delivery channels.

## 5. Campaign Tradecraft
Phishing email → hyperlink to download ZIP → user interaction/execution of script-based chain → Pikabot installation → operator-controlled follow-on actions (varies by affiliate/operator).

## 6. MITRE ATT&CK Alignment
- **Techniques Observed** (source-supported at high level):
  - [[T1566.002 - Spearphishing Link]]
  - [[T1204.001 - Malicious Link]]
  - [[T1059.007 - JavaScript]]
  - [[T1105 - Ingress Tool Transfer]]
  - [[T1027.009 - Embedded Payloads]]
- **Notable Tradecraft Characteristics**
  - Email hyperlinks leading to ZIP/script chains used for initial access (campaign + multiple vendor reporting).
  - Rapid variant changes observed in early 2024 campaigns (vendor reporting).

## 7. Malware & Tooling
- **Malware Families**
  - [[30_CIPHER/05_Malware/S1145 - Pikabot|Pikabot (S1145)]]
- **Tools**
  - Unknown / not consistently disclosed for this specific campaign.

## 8. Infrastructure & Operational Patterns
- [[Phishing Infrastructure]] to deliver lure content and stage archives.
- [[Ephemeral Infrastructure]] is commonly used for short-lived staging and redirect chains in loader distribution.

## 9. Timeline of Campaign Activity (Table + Chronos)

**Timeline (Markdown)**

|Date|Event|
|---|---|
|**2024-02**|Campaign activity window documented for Pikabot distribution cluster (C0036).|
|**2024-02-08**|Public reporting observed renewed Pikabot campaigns and updated variants (contextual reporting; may overlap with C0036 activity).|
|**2024-02-23**|Additional public reporting on Pikabot campaign activity and variant evolution (contextual).|

**Timeline (Chronos)**

```chronos
- [2024-02]: MITRE documents Pikabot Distribution February 2024 (C0036) activity window.
- [2024-02-08]: Elastic reports observing new Pikabot campaigns and an updated variant (contextual).
- [2024-02-23]: Elastic publishes detailed write-up on Pikabot evolution and campaigns (contextual).
```

## 10. Notable Victims & Impact
- **Notable Victims:** Not publicly enumerated for this campaign ID.
- **Impact:** Initial access via Pikabot can enable follow-on payload delivery and materially increase ransomware/extortion risk depending on operator.

## 11. Related Campaigns & Activity
- [[Pikabot]] ecosystems have been linked to multiple distribution waves and affiliate-led intrusion chains in 2023–2024 (see sources).
- Related (by malware): C0037 (Pikabot distribution linked to “Water Curupira” per MITRE).

## 12. Known Indicators (Contextual)
No stable IOCs are included here. High-signal pivots:
- Email lures containing hyperlinks to ZIP archives.
- Script-based installers in archives (often JS-based) followed by network retrieval of secondary payloads.
- Short-lived staging domains and redirect chains (high volatility).

## 13. Defensive Considerations
- Email security: detonate/analyze linked archives; block suspicious archive downloads and script execution where feasible.
- Endpoint controls: restrict Windows Script Host where operationally possible; enforce ASR rules; monitor LOLBIN/script execution.
- Network: detect outbound beacons and unusual HTTPS patterns post user-click; isolate newly infected endpoints quickly.
- Preparedness: treat Pikabot detections as “initial access in progress” and perform rapid scoping for lateral movement.

## 14. Analyst Notes
- Public attribution is not definitive for C0036; keep actor fields empty unless new sourcing emerges.
- Consider enriching with telemetry: mail gateway logs (URL click events), EDR process tree (script → payload), and DNS/HTTP artifacts for pivoting.

## 15. Further Reading / External Resources
- MITRE ATT&CK Campaign: Pikabot Distribution February 2024 (C0036) — https://attack.mitre.org/campaigns/C0036/
- Elastic Security Labs: PIKABOT, I choose you! — https://www.elastic.co/security-labs/pikabot-i-choose-you
- eSentire: The Rising Threat of Pikabot — https://www.esentire.com/blog/the-rising-threat-of-pikabot
- McAfee Labs: Distinctive Campaign Evolution of Pikabot — https://www.mcafee.com/blogs/other-blogs/mcafee-labs/distinctive-campaign-evolution-of-pikabot-malware/

## 16. References (APA)
- Elastic Security Labs. (2024, February 23). *PIKABOT, I choose you!* Elastic. https://www.elastic.co/security-labs/pikabot-i-choose-you
- eSentire. (2024, January 10). *The Rising Threat of Pikabot.* eSentire. https://www.esentire.com/blog/the-rising-threat-of-pikabot
- McAfee Labs. (2024, April 2). *Distinctive Campaign Evolution of Pikabot Malware.* McAfee. https://www.mcafee.com/blogs/other-blogs/mcafee-labs/distinctive-campaign-evolution-of-pikabot-malware/
- MITRE. (2024, October 28). *Pikabot Distribution February 2024 (C0036).* MITRE ATT&CK. https://attack.mitre.org/campaigns/C0036/
- MITRE. (2024, September 17). *TA577 (G1037).* MITRE ATT&CK. https://attack.mitre.org/groups/G1037/
