---
entity_type: threat_actor
actor_name: "DarkHydrus"
common_name: "DarkHydrus"
actor_id: "G0079"
actor_type: "Targeted intrusion set (reported)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2016"
last_seen: ""
status: "Unknown"
motivations: []
objectives: ["Credential harvesting via Office template injection","Targeted access to government and education","Tooling acquisition and staged payload execution"]
victimology_summary: "DarkHydrus is described in ATT&CK as targeting government agencies and educational institutions in the Middle East since at least 2016, leveraging open-source tools and custom payloads."
target_sectors: ["Government","Education"]
target_regions: ["Middle East"]
related_groups: []
malware: []
tools: ["[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]","[[30_CIPHER/05_Malware/S0363 - Empire|Empire]]","[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]"]
infrastructure: ["[[Spearphishing]]","[[Office Template Injection]]","[[RAR-delivered payload staging]]","[[HTTP/S C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1187 - Forced Authentication]]","[[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1221 - Template Injection]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0079 DarkHydrus - https://attack.mitre.org/groups/G0079/","MITRE ATT&CK - S0154 Cobalt Strike - https://attack.mitre.org/software/S0154/","MITRE ATT&CK - S0363 Empire - https://attack.mitre.org/software/S0363/","MITRE ATT&CK - S0002 Mimikatz - https://attack.mitre.org/software/S0002/","Unit 42 - New Threat Actor Group DarkHydrus Targets Middle East Government - https://unit42.paloaltonetworks.com/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/","Unit 42 - DarkHydrus Uses Phishery to Harvest Credentials in the Middle East - https://unit42.paloaltonetworks.com/unit42-darkhydrus-uses-phishery-harvest-credentials-middle-east/"]
tags: ["scout","threat-actor","mitre-g0079","darkhydrus","middle-east","template-injection"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
DarkHydrus (G0079) is described in ATT&CK as a threat group targeting **government agencies and educational institutions in the Middle East** since at least **2016**, leveraging **open-source tools and custom payloads**. ATT&CK highlights credential theft and access patterns aligned to **Office template injection** ([[20_Entities/07_TTPs/T1221 - Template Injection]]) and **forced authentication** ([[20_Entities/07_TTPs/T1187 - Forced Authentication]]), with tooling acquisition aligned to [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]].

## 2. Attribution Notes
ATT&CK does not assert a clear sponsor/country attribution for DarkHydrus in the group summary. This note treats attribution as **low confidence/unknown** absent explicit sourcing.

## 3. Motivations & Objectives
- Targeted access against government and education institutions
- Credential collection via authentication prompts induced by Office tradecraft
- Tool-assisted post-compromise operations using publicly available frameworks and utilities

## 4. Targeting Profile
- **Regions:** Middle East
- **Sectors:** Government; education
- **Delivery themes:** spearphishing attachments and Office document-based workflows

## 5. Tradecraft Overview
- Spearphishing attachments aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and user execution [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- Credential harvesting patterns aligned to:
  - [[20_Entities/07_TTPs/T1221 - Template Injection]] (remote template loads in Office workflows)
  - [[20_Entities/07_TTPs/T1187 - Forced Authentication]] (credential prompts / forced auth)
- Use of PowerShell aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- Concealment aligned to [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]
- Tool acquisition aligned to [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1221 - Template Injection]]
- [[20_Entities/07_TTPs/T1187 - Forced Authentication]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]

## 7. Malware & Tools Used
- Tools (documented/commonly associated in ATT&CK context and public reporting referenced by ATT&CK):
  - [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
  - [[30_CIPHER/05_Malware/S0363 - Empire|Empire]]
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]

## 8. Infrastructure Patterns
- [[Spearphishing]] delivering password-protected archives and Office documents (per referenced reporting)
- [[Office Template Injection]] leading to authentication prompts (credential harvesting workflow)
- [[HTTP/S C2]] patterns consistent with post-exploitation frameworks

## 9. Campaign History
- **2016–present (reported):** ATT&CK describes operations since at least early 2016, with public reporting in 2018 detailing the group’s playbook.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Block/monitor Office remote template retrieval and enforce policy controls for external templates where feasible.
- Alert on authentication prompts or outbound connections consistent with forced auth/credential harvesting originating from Office.
- Monitor suspicious PowerShell process trees launched from Office and associated network beacons.
- Validate that endpoint controls can detect common post-exploitation toolmarks (e.g., [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]] artifacts, suspicious reflective loading patterns, abnormal named pipes).

## 12. Analyst Notes
**Confidence:** High for victimology (per ATT&CK summary) and technique mapping. Low for attribution/sponsorship.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0079/
- https://unit42.paloaltonetworks.com/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/
- https://unit42.paloaltonetworks.com/unit42-darkhydrus-uses-phishery-harvest-credentials-middle-east/

## 14. References
- MITRE ATT&CK. (2025). *DarkHydrus (G0079)*. https://attack.mitre.org/groups/G0079/
- Palo Alto Networks Unit 42. (2018, July 27). *New Threat Actor Group DarkHydrus Targets Middle East Government*. https://unit42.paloaltonetworks.com/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/
- Palo Alto Networks Unit 42. (2018, August 7). *DarkHydrus Uses Phishery to Harvest Credentials in the Middle East*. https://unit42.paloaltonetworks.com/unit42-darkhydrus-uses-phishery-harvest-credentials-middle-east/
- MITRE ATT&CK. (2025). *Cobalt Strike (S0154)*. https://attack.mitre.org/software/S0154/
- MITRE ATT&CK. (2025). *Empire (S0363)*. https://attack.mitre.org/software/S0363/
- MITRE ATT&CK. (2025). *Mimikatz (S0002)*. https://attack.mitre.org/software/S0002/
