---
entity_type: threat_actor
actor_name: "Thrip"
common_name: "Thrip"
actor_id: "G0076"
actor_type: ""
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Unknown"
first_seen: ""
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Target satellite communications, telecoms, and defense contractors","Use a blend of custom malware and living-off-the-land tooling","Exfiltrate data over alternative protocols and maintain remote access tooling"]
victimology_summary: "Thrip (G0076) is documented in ATT&CK as an espionage group targeting satellite communications, telecoms, and defense contractor companies in the U.S. and Southeast Asia. ATT&CK maps Thrip to custom malware [[30_CIPHER/05_Malware/S0261 - Catchamas|Catchamas]] and notes use of common tools (e.g., Mimikatz, PsExec) as well as data exfiltration over FTP via WinSCP and cloud-based remote access software."
target_sectors: ["Satellite communications","Telecommunications","Defense contractors"]
target_regions: ["United States","Southeast Asia"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/S0261 - Catchamas|Catchamas]]"]
tools: ["Mimikatz","PsExec","WinSCP","LogMeIn"]
infrastructure: ["[[FTP exfiltration]]","[[Remote desktop software]]"]
ttps: ["[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1219.002 - Remote Access Tools: Remote Desktop Software]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0076 Thrip - https://attack.mitre.org/groups/G0076/","MITRE ATT&CK - S0261 Catchamas - https://attack.mitre.org/software/S0261/","MITRE ATT&CK - S0002 Mimikatz - https://attack.mitre.org/software/S0002/"]
tags: ["scout","threat-actor","mitre-g0076","espionage","telecom","defense"]
created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Thrip (G0076) is an espionage-focused actor documented by ATT&CK targeting satellite communications, telecoms, and defense contractors. Mapped behaviors include **PowerShell-driven operations**, **exfiltration over non-C2 protocols (e.g., FTP)**, and **remote access tooling**, alongside custom malware [[30_CIPHER/05_Malware/S0261 - Catchamas|Catchamas]]. This combination makes Thrip relevant for defenders prioritizing endpoint script telemetry, data movement monitoring, and remote access software governance.

## 2. Attribution Notes
ATT&CK describes targeting and mapped behaviors but does not, in the material captured here, provide sponsor attribution fields suitable for locking into YAML.

## 3. Motivations & Objectives
- Espionage-driven collection within high-value communications and defense supply chains
- Maintain access using both custom malware and widely available tools
- Exfiltrate data using alternative protocols outside primary C2 channels

## 4. Targeting Profile
- **Sectors:** satellite communications, telecommunications, defense contractors
- **Regions:** U.S. and Southeast Asia (ATT&CK summary)

## 5. Tradecraft Overview
- **Command execution & operator activity:** PowerShell aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]].
- **Exfiltration:** FTP-based exfiltration behavior aligned to [[20_Entities/07_TTPs/T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol]].
- **Tooling acquisition:** obtain/operate common tools aligned to [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]].
- **Remote access:** cloud/remote desktop software aligned to [[20_Entities/07_TTPs/T1219.002 - Remote Access Tools: Remote Desktop Software]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1219.002 - Remote Access Tools: Remote Desktop Software]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0261 - Catchamas|Catchamas]]
- Tools (as described in ATT&CK narrative):
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]] *(software entity; adjust path if you store tools separately)*
  - PsExec
  - WinSCP
  - LogMeIn

## 8. Infrastructure Patterns
- [[FTP exfiltration]] and related data-movement paths (proxy/firewall + endpoint network telemetry)
- [[Remote desktop software]] governance gaps (approved tool baselines, unusual installs/usage)

## 9. Campaign History
ATT&CK maintains technique/software mappings for Thrip; campaign delineation is not captured in this note.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Enable and operationalize PowerShell logging (script block, module, transcription where appropriate) and correlate with download/exec patterns.
- Monitor for non-standard data egress (FTP) from sensitive networks; correlate with staging indicators and unusual credential access.
- Govern remote access software with allowlists, deployment controls, and alerting on unauthorized installs or anomalous sessions.

## 12. Analyst Notes
**Confidence:** Medium for ATT&CK mappings. Confirm tooling specifics and exfiltration paths in each case, as commodity tools and protocols can vary widely across intrusions.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0076/
- https://attack.mitre.org/software/S0261/
- https://attack.mitre.org/software/S0002/

## 14. References
- MITRE ATT&CK. (n.d.). *Thrip (G0076).* https://attack.mitre.org/groups/G0076/
- MITRE ATT&CK. (n.d.). *Catchamas (S0261).* https://attack.mitre.org/software/S0261/
- MITRE ATT&CK. (n.d.). *Mimikatz (S0002).* https://attack.mitre.org/software/S0002/
