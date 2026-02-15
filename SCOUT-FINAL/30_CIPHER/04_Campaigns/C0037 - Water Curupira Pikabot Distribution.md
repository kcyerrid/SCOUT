---
entity_type: campaign

campaign_name: "Water Curupira Pikabot Distribution"
campaign_id: "C0037"

associated_actors: []
suspected_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1046 - Storm-1811|Storm-1811 (G1046)]]"

attribution_confidence: "1-low"
confidence_notes: "MITRE describes the activity as linked to Black Basta deployment but does not provide a direct public mapping to a specific ATT&CK group ID for 'Water Curupira'. Storm-1811 is documented by MITRE as linked to Black Basta ransomware deployment; inclusion here is a low-confidence hypothesis, not a confirmed equivalence."

first_observed: "2023"
last_observed: "2023"
campaign_status: "unknown"

primary_objectives:
  - "access_brokering"
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
  - "phishing attachments / PDFs containing malicious links"
  - "spam-based malware distribution"
key_ttp_themes:
  - "post-QakBot loader replacement behaviors"
  - "email-based delivery for initial access"

associated_ttps:
  - "T1566.001 - Spearphishing Attachment"
  - "T1566.002 - Spearphishing Link"
  - "T1204.001 - Malicious Link"
  - "T1105 - Ingress Tool Transfer"

malware_families:
  - "[[30_CIPHER/05_Malware/S1145 - Pikabot|Pikabot (S1145)]]"
tools_used: []

infrastructure_patterns:
  - "[[Phishing Infrastructure]]"
  - "[[Ephemeral Infrastructure]]"

notable_victims: []
related_incidents: []

risk_level: "high"
impact_assessment: "Pikabot distribution linked to ransomware-adjacent ecosystems increases likelihood of rapid escalation from initial access to hands-on intrusion and extortion/ransomware outcomes."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0037/"
  - "https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html"
  - "https://www.elastic.co/security-labs/pikabot-i-choose-you"
  - "https://attack.mitre.org/groups/G1046/"
  - "https://attack.mitre.org/software/S1145/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Water Curupira Pikabot Distribution (C0037)

## 1. Campaign Overview
Water Curupira Pikabot Distribution describes a 2023 Pikabot distribution cluster associated with spam/phishing delivery, including documents (e.g., PDFs) containing malicious links that lead to Pikabot installers. MITRE characterizes the activity as linked to Black Basta ransomware deployment ecosystems and notes overlaps/similarities with QakBot-era distribution tradecraft following QakBot disruption.

## 2. Attribution Assessment
- MITRE: activity “linked to Black Basta ransomware deployment” but does not publicly map “Water Curupira” to a definitive ATT&CK group ID.  
- Trend Micro tracks “Water Curupira” as an intrusion set operating Pikabot spam waves.  
- Storm-1811 is documented by MITRE as linked to Black Basta ransomware deployment; however, public sources do not conclusively equate Storm-1811 with Trend Micro’s “Water Curupira.”

**Attribution Confidence: 1-low**

## 3. Objectives & Intent
Assessed objective is initial access/foothold creation via Pikabot delivery with plausible downstream monetization (ransomware/extortion) when affiliates transition from loader staging to hands-on intrusion.

## 4. Targeting Analysis
- **Sectors Targeted:** Unknown (public reporting emphasizes distribution mechanics).  
- **Regions Targeted:** Unknown.  
- **Technologies / Platforms Targeted:** Windows endpoints; email-based delivery.

## 5. Campaign Tradecraft
Spam/phishing → attachment or PDF lure → user clicks embedded link → payload retrieval/install → Pikabot foothold → potential handoff to follow-on tooling and ransomware operators (only when evidenced in incident-specific reporting).

## 6. MITRE ATT&CK Alignment
- **Techniques Observed**
  - [[T1566.001 - Spearphishing Attachment]]
  - [[T1566.002 - Spearphishing Link]]
  - [[T1204.001 - Malicious Link]]
  - [[T1105 - Ingress Tool Transfer]]
- **Notable Tradecraft Characteristics**
  - PDF attachments containing malicious links to installers (campaign reporting).
  - Post-QakBot ecosystem overlap discussion (campaign reporting).

## 7. Malware & Tooling
- **Malware Families**
  - [[30_CIPHER/05_Malware/S1145 - Pikabot|Pikabot (S1145)]]
- **Tools**
  - Not consistently disclosed for this campaign ID.

## 8. Infrastructure & Operational Patterns
- [[Phishing Infrastructure]] used to distribute lures and host staged payloads.
- [[Ephemeral Infrastructure]] consistent with short-lived redirect/staging infrastructure used by spam waves.

## 9. Timeline of Campaign Activity (Table + Chronos)

**Timeline (Markdown)**

|Date|Event|
|---|---|
|**2023**|Water Curupira-associated Pikabot distribution activity window (C0037).|
|**2024-01-09**|Trend Micro publishes analysis linking “Water Curupira” to Pikabot spam wave activity (contextual, retrospective on 2023 activity).|
|**2024-10-28**|MITRE publishes/updates campaign entry describing C0037.|

**Timeline (Chronos)**

```chronos
- [2023]: MITRE documents Water Curupira Pikabot Distribution (C0037) activity window.
- [2024-01-09]: Trend Micro publishes analysis of Water Curupira Pikabot spam wave (contextual).
- [2024-10-28]: MITRE updates campaign entry for C0037.
```

## 10. Notable Victims & Impact
- **Notable Victims:** Not publicly enumerated for C0037.
- **Impact:** Elevated ransomware/extortion risk where initial access transitions to interactive intrusion.

## 11. Related Campaigns & Activity
- Related (by malware): C0036 (Pikabot Distribution February 2024).
- Related (by ecosystem): QakBot-era spam/distribution tradecraft (contextual; do not assume direct operator continuity without evidence).

## 12. Known Indicators (Contextual)
No stable IOCs included. High-signal pivots:
- PDF attachments with embedded external links leading to installers.
- Script/installer execution shortly after user click events.
- Rapidly changing staging domains and download paths.

## 13. Defensive Considerations
- Harden email ingress: block/inspect PDFs with embedded external links; URL rewriting and detonation for linked downloads.
- Endpoint: restrict script interpreters where possible; monitor chain “PDF viewer/browser → download → script/installer → network beacon.”
- Incident response: treat Pikabot detections as potential precursor to ransomware—scope quickly for lateral movement staging.

## 14. Analyst Notes
- “Water Curupira” is a vendor tracking label; keep actor mapping cautious unless direct crosswalks are sourced.
- If your environment observed similar spam waves, preserve: full email headers, URL click telemetry, and endpoint process trees.

## 15. Further Reading / External Resources
- MITRE ATT&CK Campaign: Water Curupira Pikabot Distribution (C0037) — https://attack.mitre.org/campaigns/C0037/
- Trend Micro: A look into Pikabot spam wave campaign (Water Curupira) — https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html
- Elastic: PIKABOT, I choose you! — https://www.elastic.co/security-labs/pikabot-i-choose-you
- MITRE ATT&CK Group: Storm-1811 (G1046) — https://attack.mitre.org/groups/G1046/

## 16. References (APA)
- MITRE. (2024, October 28). *Water Curupira Pikabot Distribution (C0037).* MITRE ATT&CK. https://attack.mitre.org/campaigns/C0037/
- Trend Micro Research. (2024, January 9). *A look into Pikabot spam wave campaign.* Trend Micro. https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html
- Elastic Security Labs. (2024, February 23). *PIKABOT, I choose you!* Elastic. https://www.elastic.co/security-labs/pikabot-i-choose-you
- MITRE. (2025, March 14). *Storm-1811 (G1046).* MITRE ATT&CK. https://attack.mitre.org/groups/G1046/
- MITRE. (2024, October 28). *Pikabot (S1145).* MITRE ATT&CK. https://attack.mitre.org/software/S1145/
