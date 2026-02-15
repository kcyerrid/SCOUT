---
entity_type: campaign

campaign_name: "FrostyGoop Incident"
campaign_id: "C0041"

associated_actors: []
suspected_actors: []

attribution_confidence: "1-low"
confidence_notes: "Public reporting focuses on malware and incident mechanics; attribution to a specific actor varies or is not definitively stated across sources."

first_observed: "2024-01"
last_observed: "2024-01"
campaign_status: "concluded"

primary_objectives:
  - "disruption"
secondary_objectives:
  - "business_disruption"

target_sectors:
  - "critical_infrastructure"
  - "energy"
target_regions:
  - "Ukraine"
target_technologies:
  - "OT/ICS environments"
  - "Modbus TCP"
  - "ENCO controllers (per reporting)"
  - "external-facing routers (initial access enabler, per reporting)"

initial_access_vectors:
  - "likely exploitation of external-facing router/vulnerability (reporting varies)"
key_ttp_themes:
  - "OT manipulation via legitimate protocol commands"
  - "firmware downgrade to reduce visibility (reported)"
  - "web shell enablement and remote access (reported)"

associated_ttps:
  - "T1190 - Exploit Public-Facing Application"
  - "T1505.003 - Web Shell"
  - "T0826 - Loss of Availability"
  - "T0836 - Modify Parameter"
  - "T0857 - System Firmware"

malware_families:
  - "[[30_CIPHER/05_Malware/S1165 - FrostyGoop|FrostyGoop (S1165)]]"
tools_used: []

infrastructure_patterns:
  - "[[Internet-Exposed OT]]"
  - "[[Unauthenticated Modbus TCP]]"
  - "[[Remote Access Pivot]]"

notable_victims:
  - "Municipal district heating company in Ukraine (public sources do not consistently name the victim)"
related_incidents: []

risk_level: "critical"
impact_assessment: "Attack disrupted district heating operations by manipulating OT devices via Modbus TCP, demonstrating real-world service impact to civilians."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0041/"
  - "https://hub.dragos.com/report/frostygoop-ics-malware-impacting-operational-technology"
  - "https://www.nozominetworks.com/blog/protecting-against-frostygoop-bustleberm-malware"
  - "https://unit42.paloaltonetworks.com/frostygoop-malware-analysis/"
  - "https://www.wired.com/story/russia-ukraine-frostygoop-malware-heating-utility"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# FrostyGoop Incident (C0041)

## 1. Campaign Overview
FrostyGoop Incident describes a January 2024 operational technology (OT) disruptive event against a Ukrainian municipal district heating environment. Public reporting indicates the adversary used FrostyGoop (aka BUSTLEBERM) to interact with control systems over Modbus TCP, leveraging legitimate protocol commands to manipulate OT parameters and disrupt heat delivery.

## 2. Attribution Assessment
- Sources emphasize incident mechanics and the malware’s OT interaction capabilities.
- Attribution to a specific actor is not consistently or definitively stated across widely cited public sources.

**Attribution Confidence: 1-low**

## 3. Objectives & Intent
Primary intent appears disruptive:
- Impair heating services by modifying OT controller parameters and/or influencing control logic via Modbus interactions.

## 4. Targeting Analysis
- **Sectors Targeted:** Critical infrastructure / district heating operations.
- **Regions Targeted:** Ukraine.
- **Technologies / Platforms Targeted:** Modbus TCP environments, ENCO controllers (reported), and supporting IT/edge access paths.

## 5. Campaign Tradecraft
Likely initial access via external-facing router/vulnerability → establish remote foothold → access OT network segment → issue Modbus commands via FrostyGoop → modify parameters/measurements → cause loss of availability and service disruption.

## 6. MITRE ATT&CK Alignment
- **Techniques Observed**
  - [[T1190 - Exploit Public-Facing Application]] (reported as likely enabler; exact CVE may be uncertain)
  - [[T1505.003 - Web Shell]] (reported as part of access/persistence in some summaries)
  - [[T0826 - Loss of Availability]]
  - [[T0836 - Modify Parameter]]
  - [[T0857 - System Firmware]] (firmware downgrade reported in incident summaries)
- **Notable Tradecraft Characteristics**
  - OT manipulation via legitimate Modbus commands (not “noisy” packet floods).
  - Emphasis on operational impact (service outage) rather than pure data theft.

## 7. Malware & Tooling
- **Malware Families**
  - [[30_CIPHER/05_Malware/S1165 - FrostyGoop|FrostyGoop (S1165)]]
- **Tools**
  - Not exhaustively listed here; refer to technical analyses for sample-specific tooling.

## 8. Infrastructure & Operational Patterns
- [[Internet-Exposed OT]] as a recurring risk factor in public reporting.
- [[Unauthenticated Modbus TCP]]: protocol exposure and weak authentication assumptions amplify risk.
- [[Remote Access Pivot]]: IT-to-OT bridging enables adversary reach into control networks.

## 9. Timeline of Campaign Activity (Table + Chronos)

**Timeline (Markdown)**

|Date|Event|
|---|---|
|**2024-01**|Incident timeframe (district heating disruption) documented in public reporting and MITRE campaign summary.|
|**2024-07-23**|Dragos publicly reports on FrostyGoop OT malware and incident impact (public disclosure wave).|
|**2024-07-24**|Nozomi Networks publishes OT defensive guidance for FrostyGoop/BUSTLEBERM.|
|**2024-11-19**|Unit 42 publishes deeper malware artifact/behavior analysis (contextual).|

**Timeline (Chronos)**

```chronos
- [2024-01]: FrostyGoop Incident in Ukraine district heating environment (MITRE campaign summary).
- [2024-07-23]: Dragos public disclosure on FrostyGoop and incident impact.
- [2024-07-24]: Nozomi Networks publishes defensive guidance for FrostyGoop/BUSTLEBERM.
- [2024-11-19]: Unit 42 publishes technical analysis and artifact review.
```

## 10. Notable Victims & Impact
- **Victim:** Municipal district heating operator in Ukraine (name inconsistently disclosed publicly).
- **Impact:** Loss of heating service to civilians for a limited period; demonstrates OT cyber operations translating into real-world service disruption.

## 11. Related Campaigns & Activity
- Relates to broader OT/ICS threat landscape where exposed OT protocols (Modbus) are leveraged for direct manipulation rather than conventional IT disruption.

## 12. Known Indicators (Contextual)
No IOCs included here. High-signal pivots:
- Unexpected Modbus write commands to holding registers.
- Remote access sessions into OT segments outside maintenance windows.
- Firmware downgrade events on edge/monitoring devices.

## 13. Defensive Considerations
- Remove OT devices from direct internet exposure; enforce strict segmentation and allow-listing.
- Monitor Modbus traffic for write operations and out-of-baseline command patterns.
- Ensure secure remote access with MFA, audited sessions, and jump-host controls.
- Validate firmware integrity and prevent downgrade paths (where possible).

## 14. Analyst Notes
- This note deliberately avoids naming a perpetrator absent definitive public attribution consensus.
- If building detections: prioritize network-based OT telemetry (Modbus command monitoring) over endpoint-only AV assumptions.

## 15. Further Reading / External Resources
- Dragos report landing page — https://hub.dragos.com/report/frostygoop-ics-malware-impacting-operational-technology
- Nozomi Networks guidance — https://www.nozominetworks.com/blog/protecting-against-frostygoop-bustleberm-malware
- Unit 42 analysis — https://unit42.paloaltonetworks.com/frostygoop-malware-analysis/
- MITRE ATT&CK Campaign (C0041) — https://attack.mitre.org/campaigns/C0041/
- Wired coverage — https://www.wired.com/story/russia-ukraine-frostygoop-malware-heating-utility

## 16. References (APA)
- Dragos. (2024, July). *Impact of FrostyGoop ICS Malware on Connected OT Systems.* Dragos. https://hub.dragos.com/report/frostygoop-ics-malware-impacting-operational-technology
- MITRE. (2024, November 20). *FrostyGoop Incident (C0041).* MITRE ATT&CK. https://attack.mitre.org/campaigns/C0041/
- Nozomi Networks Labs. (2024, July 24). *Cyberwarfare Targeting OT: Protecting Against FrostyGoop/BUSTLEBERM Malware.* Nozomi Networks. https://www.nozominetworks.com/blog/protecting-against-frostygoop-bustleberm-malware
- Palo Alto Networks Unit 42. (2024, November 19). *FrostyGoop’s Zoom-In: A Closer Look into the Malware Artifacts, Behaviors, and Network Communications.* Unit 42. https://unit42.paloaltonetworks.com/frostygoop-malware-analysis/
- Wired. (2024, July 23). *How Russia-Linked Malware Cut Heat to 600 Ukrainian Buildings in Deep Winter.* Wired. https://www.wired.com/story/russia-ukraine-frostygoop-malware-heating-utility
