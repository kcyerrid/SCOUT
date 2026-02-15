---
entity_type: threat_actor
actor_name: "Elderwood"
common_name: "Elderwood"
actor_id: "G0066"
actor_type: "Suspected state-sponsored (espionage)"
aliases: ["Elderwood Gang","Beijing Group","Sneaky Panda"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2009-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage","Information theft"]
objectives: ["Strategic intelligence collection","Initial access via drive-by compromise and phishing","Delivery of exploit chains and backdoors"]
victimology_summary: "Suspected Chinese cyber espionage activity associated with the 2009 Operation Aurora intrusion set; reported targeting includes defense organizations, supply chain manufacturers, human rights/NGOs, and IT service providers."
target_sectors: ["Defense","Manufacturing / Supply Chain","Civil society / NGOs","IT services"]
target_regions: []
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Briba]]","[[30_CIPHER/05_Malware/Hydraq]]","[[30_CIPHER/05_Malware/Vasport]]"]
tools: []
infrastructure: ["[[Watering Hole]]","[[Drive-by Compromise]]","[[Spearphishing]]","[[Exploit Delivery]]"]
ttps: ["[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]","[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0066 Elderwood - https://attack.mitre.org/groups/G0066/","MITRE ATT&CK - S0204 Briba - https://attack.mitre.org/software/S0204/","MITRE ATT&CK - S0203 Hydraq - https://attack.mitre.org/software/S0203/","MITRE ATT&CK - S0207 Vasport - https://attack.mitre.org/software/S0207/"]
tags: ["scout","threat-actor","mitre-g0066","espionage"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

## 1. BLUF / Executive Summary
Elderwood (G0066) is a suspected China-linked cyber espionage activity cluster publicly associated with the 2009 Operation Aurora intrusion set. Reporting summarized in ATT&CK describes a blend of watering-hole/drive-by compromise and targeted phishing to deliver exploit chains and backdoor malware.

## 2. Attribution Notes
ATT&CK characterizes Elderwood as a “suspected Chinese cyber espionage group.” The actor is also referenced under multiple community aliases (Elderwood Gang, Beijing Group, Sneaky Panda), reflecting tracking-name variance rather than confirmed separate entities.

## 3. Motivations & Objectives
- Espionage and long-term intelligence collection
- Initial access through [[Drive-by Compromise]] and targeted [[Spearphishing]]
- Delivery of exploit chains and backdoors to enable follow-on collection

## 4. Targeting Profile
- **Sectors (reported):** defense, supply chain/manufacturing, human rights & NGOs, IT service providers
- **Geography:** not consistently bounded in ATT&CK’s summary; targeting is framed by sector and victim type

## 5. Tradecraft Overview
- [[Watering Hole]] and sector-specific web page compromise consistent with [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]].
- Use of [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]] (including zero-day/endpoint software exploitation) to gain execution.
- Staged delivery and retrieval of additional payloads aligned to [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- Obfuscation/packing and encryption patterns aligned to [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]] and [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/Briba]]
  - [[30_CIPHER/05_Malware/Hydraq]]
  - [[30_CIPHER/05_Malware/Vasport]]

## 8. Infrastructure Patterns
- [[Watering Hole]] delivery via compromised, sector-relevant web pages
- [[Exploit Delivery]] embedded in web content and malicious attachments/links
- [[Staged Payloading]] with remote retrieval consistent with loader-to-backdoor workflows

## 9. Campaign History
- **2009 (reported):** Activity associated with Operation Aurora is cited in ATT&CK’s Elderwood summary as a notable reference point.
- **Post-2009 (reported):** Ongoing sector-focused targeting patterns are described across defense, supply chain, NGOs, and IT services.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Reduce exposure to [[Drive-by Compromise]] through browser/plugin hardening and timely patching for client-side applications.
- Strengthen phishing resilience for high-risk roles; increase scrutiny for uncommon-hosted links and attachment execution paths.
- Improve detection for staged download behavior and suspicious post-exploitation tooling transfer.

## 12. Analyst Notes
**Confidence:** Medium. ATT&CK supports the high-level characterization and technique set, but incident-level clustering under “Elderwood” vs. adjacent China-nexus activity can vary by vendor taxonomy.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0066/

## 14. References
- https://attack.mitre.org/groups/G0066/
- https://attack.mitre.org/software/S0204/
- https://attack.mitre.org/software/S0203/
- https://attack.mitre.org/software/S0207/
