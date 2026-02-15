---
entity_type: threat_actor
actor_name: "Honeybee"
common_name: "Honeybee"
actor_id: "G0072"
actor_type: ""
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Unknown"
first_seen: ""
last_seen: ""
status: "Deprecated"
motivations: ["Espionage"]
objectives: ["Targeted access to government/defense-affiliated entities","Collection and staging of sensitive data","Maintain access through credential theft and persistence tradecraft documented in Operation Honeybee"]
victimology_summary: "Honeybee (G0072) is marked as **deprecated** in ATT&CK and is replaced by the campaign [[30_CIPHER/04_Campaigns/C0006 - Operation Honeybee|Operation Honeybee]]. Use campaign-level mappings for tradecraft and detection engineering until/unless ATT&CK restores a current group entity for this activity cluster."
target_sectors: ["Government","Defense"]
target_regions: ["Central Asia"]
related_groups: []
malware: []
tools: []
infrastructure: ["[[Phishing]]","[[Web-based C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]]","[[20_Entities/07_TTPs/T1114.003 - Email Collection: Email Forwarding Rule]]","[[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]","[[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]","[[20_Entities/07_TTPs/T1560 - Archive Collected Data]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1113 - Screen Capture]]"]
notable_claims: ["ATT&CK marks G0072 Honeybee as deprecated and replaced by campaign C0006."]
intel_sources: ["MITRE ATT&CK - G0072 Honeybee (Deprecated) - https://attack.mitre.org/groups/G0072","MITRE ATT&CK - C0006 Operation Honeybee - https://attack.mitre.org/campaigns/C0006/"]
tags: ["scout","threat-actor","mitre-g0072","deprecated","espionage","central-asia"]
created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Honeybee (G0072) is **deprecated** in ATT&CK and replaced by the campaign entity [[30_CIPHER/04_Campaigns/C0006 - Operation Honeybee|Operation Honeybee]]. For operational use, treat the campaign as the authoritative container for TTPs, targeting, and detections.

## 2. Attribution Notes
ATT&CK does not present an active, current group record for G0072. Avoid extending attribution beyond what is captured in the replacing campaign record.

## 3. Motivations & Objectives
- Espionage-driven collection against government/defense-adjacent targets
- Credential theft and access maintenance to enable email and document collection

## 4. Targeting Profile
- **Victim themes:** government and defense-affiliated entities (per Operation Honeybee)
- **Region:** Central Asia (per Operation Honeybee)

## 5. Tradecraft Overview
*(Derived from ATT&CK’s Operation Honeybee campaign mapping; use this as the practical substitute for the deprecated group record.)*
- Initial access via [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]].
- Credential collection aligned to [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]].
- Email collection aligned to [[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]] and [[20_Entities/07_TTPs/T1114.003 - Email Collection: Email Forwarding Rule]].
- Discovery aligned to [[20_Entities/07_TTPs/T1082 - System Information Discovery]], [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]], and [[20_Entities/07_TTPs/T1217 - Browser Information Discovery]].
- Staging/packaging aligned to [[20_Entities/07_TTPs/T1560 - Archive Collected Data]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1555.003 - Credentials from Password Stores: Credentials from Web Browsers]]
- [[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]]
- [[20_Entities/07_TTPs/T1114.003 - Email Collection: Email Forwarding Rule]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]
- [[20_Entities/07_TTPs/T1113 - Screen Capture]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]

## 7. Malware & Tools Used
ATT&CK’s deprecated group record does not provide a stable, current software mapping here; follow [[30_CIPHER/04_Campaigns/C0006 - Operation Honeybee|Operation Honeybee]] for software references.

## 8. Infrastructure Patterns
- [[Phishing]] delivery with attachment-based execution chains
- [[Web-based C2]] patterns (proxy, DNS, and endpoint network telemetry)

## 9. Campaign History
- [[30_CIPHER/04_Campaigns/C0006 - Operation Honeybee|Operation Honeybee]] is the replacing ATT&CK entity for this activity.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Emphasize attachment detonation controls, macro/script policy controls, and robust email telemetry.
- Monitor mailbox rules/forwarding changes and unusual local email access paths.
- Detect browser credential store access patterns and follow-on staging (archiving) activity.

## 12. Analyst Notes
**Handling guidance:** Treat G0072 as a legacy label only; anchor workflows, detections, and reporting to the campaign entity unless ATT&CK reintroduces an updated group record.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0072
- https://attack.mitre.org/campaigns/C0006/

## 14. References
- MITRE ATT&CK. (n.d.). *Honeybee (G0072) [Deprecated].* https://attack.mitre.org/groups/G0072
- MITRE ATT&CK. (n.d.). *Operation Honeybee (C0006).* https://attack.mitre.org/campaigns/C0006/
