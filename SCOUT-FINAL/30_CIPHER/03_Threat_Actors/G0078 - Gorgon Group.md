---
entity_type: threat_actor
actor_name: "Gorgon Group"
common_name: "Gorgon Group"
actor_id: "G0078"
actor_type: "Suspected state-linked (reported) / Mixed criminal-targeted"
aliases: []
country_of_origin: "Pakistan (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2017"
last_seen: ""
status: "Unknown"
motivations: ["Mixed (criminal and targeted)"]
objectives: ["Initial access via spearphishing attachments","RAT deployment and remote control","Credential theft and collection"]
victimology_summary: "Gorgon Group is described in ATT&CK as Pakistan-linked (suspected) and conducting a mix of criminal and targeted attacks, including campaigns against government organizations in the UK, Spain, Russia, and the US."
target_sectors: ["Government"]
target_regions: ["United Kingdom","Spain","Russia","United States"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/S0336 - NanoCore|NanoCore]]","[[30_CIPHER/05_Malware/S0385 - njRAT|njRAT]]","[[30_CIPHER/05_Malware/S0262 - QuasarRAT|QuasarRAT]]","[[30_CIPHER/05_Malware/S0332 - Remcos|Remcos]]"]
tools: []
infrastructure: ["[[Spearphishing Attachment]]","[[Commodity RAT C2]]","[[PowerShell Download Cradles]]"]
ttps: ["[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1547.009 - Boot or Logon Autostart Execution: Shortcut Modification]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]","[[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]","[[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1112 - Modify Registry]]","[[20_Entities/07_TTPs/T1106 - Native API]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1055.002 - Process Injection: Portable Executable Injection]]","[[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0078 Gorgon Group - https://attack.mitre.org/groups/G0078/","MITRE ATT&CK - S0336 NanoCore - https://attack.mitre.org/software/S0336/","MITRE ATT&CK - S0385 njRAT - https://attack.mitre.org/software/S0385/","MITRE ATT&CK - S0262 QuasarRAT - https://attack.mitre.org/software/S0262/","MITRE ATT&CK - S0332 Remcos - https://attack.mitre.org/software/S0332/","Unit 42 - The Gorgon Group: Slithering Between Nation State and Cybercrime - https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/"]
tags: ["scout","threat-actor","mitre-g0078","gorgon-group","pakistan","spearphishing","rat"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
Gorgon Group (G0078) is described in ATT&CK as a threat group with members **suspected to be Pakistan-based or connected to Pakistan**, conducting **a mix of criminal and targeted attacks**, including campaigns against **government organizations in the UK, Spain, Russia, and the US**. ATT&CK documents a spearphishing-centric access pattern and use of commodity remote access tooling (e.g., [[30_CIPHER/05_Malware/S0262 - QuasarRAT|QuasarRAT]], [[30_CIPHER/05_Malware/S0332 - Remcos|Remcos]]).

## 2. Attribution Notes
ATT&CK frames geographic attribution as **suspected**. Treat attribution as **medium confidence** and avoid extrapolation to sponsors or mission sets not explicitly supported.

## 3. Motivations & Objectives
- Mixed activity profile: opportunistic/commodity tradecraft blended with targeted government campaigns
- Establish access via spearphishing attachments and user execution
- Maintain remote control using commodity RAT families and common Windows tradecraft

## 4. Targeting Profile
- **Sectors:** Government organizations
- **Regions/Countries:** United Kingdom, Spain, Russia, United States (per ATT&CK summary)
- **Typical victim environment:** Windows endpoints and Office-based workflows

## 5. Tradecraft Overview
- Initial access via [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and user execution [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- Scripted execution and payload staging aligned to:
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- Defense evasion and concealment aligned to:
  - [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]
  - [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]
  - [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]] (decode/deobfuscation in malware workflows)
- Process injection behaviors aligned to [[20_Entities/07_TTPs/T1055.002 - Process Injection: Portable Executable Injection]] and [[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1112 - Modify Registry]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1547.009 - Boot or Logon Autostart Execution: Shortcut Modification]]
- [[20_Entities/07_TTPs/T1106 - Native API]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1564.003 - Hide Artifacts: Hidden Window]]
- [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1055.002 - Process Injection: Portable Executable Injection]]
- [[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]

## 7. Malware & Tools Used
- Malware (per ATT&CK software mapping):
  - [[30_CIPHER/05_Malware/S0336 - NanoCore|NanoCore]]
  - [[30_CIPHER/05_Malware/S0385 - njRAT|njRAT]]
  - [[30_CIPHER/05_Malware/S0262 - QuasarRAT|QuasarRAT]]
  - [[30_CIPHER/05_Malware/S0332 - Remcos|Remcos]]

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] delivery of malicious Office documents
- Commodity RAT command-and-control patterns (variable infra, common ports/protocols)
- Script-based download and staging patterns consistent with PowerShell/cmd payload delivery

## 9. Campaign History
- **2017–present (reported):** ATT&CK describes activity beginning no later than 2017, including multi-country government targeting.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Email and attachment hardening: block high-risk filetypes, enforce macro controls, detonate Office documents in sandbox.
- Telemetry-driven detections:
  - PowerShell/cmd process trees spawned from Office
  - Registry Run key / .lnk modification persistence attempts
  - Process injection telemetry (cross-process memory write + thread start, hollowing artifacts)
- Prioritize endpoint controls to prevent/alert on commodity RAT families and their common execution chains.

## 12. Analyst Notes
**Confidence:** Medium for geographic attribution (ATT&CK: suspected). High confidence for technique mapping where ATT&CK provides explicit technique narratives.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0078/
- https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/

## 14. References
- MITRE ATT&CK. (2025). *Gorgon Group (G0078)*. https://attack.mitre.org/groups/G0078/
- Falcone, R., Fuertes, D., Grunzweig, J., & Wilhoit, K. (2018, August 2). *The Gorgon Group: Slithering Between Nation State and Cybercrime*. Palo Alto Networks Unit 42. https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/
- MITRE ATT&CK. (2025). *NanoCore (S0336)*. https://attack.mitre.org/software/S0336/
- MITRE ATT&CK. (2025). *njRAT (S0385)*. https://attack.mitre.org/software/S0385/
- MITRE ATT&CK. (2025). *QuasarRAT (S0262)*. https://attack.mitre.org/software/S0262/
- MITRE ATT&CK. (2025). *Remcos (S0332)*. https://attack.mitre.org/software/S0332/
