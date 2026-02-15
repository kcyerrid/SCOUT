---
entity_type: threat_actor
actor_name: "Dark Caracal"
common_name: "Dark Caracal"
actor_id: "G0070"
actor_type: "State-sponsored (surveillance / espionage)"
aliases: []
country_of_origin: "Lebanon (attributed)"
suspected_sponsors: ["Lebanese General Directorate of General Security (GDGS) (attributed)"]
attribution_confidence: "High"
first_seen: "2012-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage","Surveillance"]
objectives: ["Targeted compromise of individuals","Collection of local data and screenshots","Device monitoring via desktop and mobile implants"]
victimology_summary: "Threat group attributed in ATT&CK to Lebanon's General Directorate of General Security (GDGS), operating since at least 2012. ATT&CK describes spearphishing via services and watering-hole activity, and documents both Windows and Android surveillanceware associated with the actor."
target_sectors: ["Individuals of interest","Government-adjacent targets","Media / Journalism","Civil society / NGOs"]
target_regions: []
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Bandook]]","[[30_CIPHER/05_Malware/Pallas]]"]
tools: []
infrastructure: ["[[Spearphishing via Service]]","[[Watering Hole]]","[[HTTP C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1005 - Data from Local System]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]","[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]","[[20_Entities/07_TTPs/T1566.003 - Phishing: Spearphishing via Service]]","[[20_Entities/07_TTPs/T1113 - Screen Capture]]","[[20_Entities/07_TTPs/T1218.001 - System Binary Proxy Execution: Compiled HTML File]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0070 Dark Caracal - https://attack.mitre.org/groups/G0070/","MITRE ATT&CK - S0234 Bandook - https://attack.mitre.org/software/S0234/","MITRE ATT&CK - S0399 Pallas - https://attack.mitre.org/software/S0399/"]
tags: ["scout","threat-actor","mitre-g0070","surveillance","lebanon"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

## 1. BLUF / Executive Summary
Dark Caracal (G0070) is a surveillance-oriented threat group attributed in ATT&CK to Lebanon’s General Directorate of General Security (GDGS), operating since at least 2012. ATT&CK documents both desktop and mobile tooling—most notably [[30_CIPHER/05_Malware/Bandook]] and Android surveillanceware [[30_CIPHER/05_Malware/Pallas]]—and tradecraft including spearphishing via services and watering-hole/drive-by compromise.

## 2. Attribution Notes
ATT&CK attributes Dark Caracal to the Lebanese GDGS based on publicly reported research. This note treats attribution as high confidence in line with ATT&CK’s explicit framing, while avoiding extrapolation beyond documented reporting.

## 3. Motivations & Objectives
- Targeted surveillance and intelligence collection
- Collection of local files and user data, including screenshots (as documented in ATT&CK technique narratives)
- Persistence and long-lived access via commodity and custom implants

## 4. Targeting Profile
- **Victim themes:** individuals of interest and targeted populations aligned with surveillance objectives (ATT&CK summary and cited reporting)
- **Sectors:** mixed; often individual-centric rather than purely organizational targeting

## 5. Tradecraft Overview
- Spearphishing via services aligned to [[20_Entities/07_TTPs/T1566.003 - Phishing: Spearphishing via Service]].
- Watering-hole activity aligned to [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]].
- Persistence via autoruns aligned to [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]].
- Collection behaviors aligned to [[20_Entities/07_TTPs/T1005 - Data from Local System]] and [[20_Entities/07_TTPs/T1113 - Screen Capture]].
- Evasion/obfuscation aligned to [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]] and [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]].
- Use of built-in/proxy execution patterns aligned to [[20_Entities/07_TTPs/T1218.001 - System Binary Proxy Execution: Compiled HTML File]] as described in ATT&CK’s technique notes.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.003 - Phishing: Spearphishing via Service]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1113 - Screen Capture]]
- [[20_Entities/07_TTPs/T1218.001 - System Binary Proxy Execution: Compiled HTML File]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/Bandook]]
  - [[30_CIPHER/05_Malware/Pallas]]

## 8. Infrastructure Patterns
- [[Spearphishing via Service]] using common communication platforms to reach targets (as described in ATT&CK’s technique narratives)
- [[Watering Hole]] sites delivering malicious code
- [[HTTP C2]] patterns supporting implant communications

## 9. Campaign History
- **2012–present (reported):** ATT&CK describes operations beginning no later than 2012 with ongoing public reporting that documents both Windows and Android surveillance tooling.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Prioritize protections for high-risk individuals and communications workflows; emphasize phishing-resistant authentication and endpoint hardening.
- Improve detection for suspicious autorun persistence, abnormal web-protocol beaconing, and screenshot/data collection behaviors.
- Increase user-risk reduction measures for service-based phishing and deceptive file masquerading.

## 12. Analyst Notes
**Confidence:** High for attribution framing and key tools per ATT&CK; operational details should be validated per-incident because infrastructure and lures can shift rapidly.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0070/
- https://attack.mitre.org/software/S0399/

## 14. References
- https://attack.mitre.org/groups/G0070/
- https://attack.mitre.org/software/S0234/
- https://attack.mitre.org/software/S0399/
