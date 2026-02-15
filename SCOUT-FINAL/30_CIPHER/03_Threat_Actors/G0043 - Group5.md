---
entity_type: threat_actor
actor_name: "Group5"
common_name: "Group5"
actor_id: "G0043"
actor_type: "Suspected Iranian-nexus cyber espionage activity cluster targeting Syrian opposition figures"
aliases: []
country_of_origin: "Iran (suspected)"
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2015-10-03"
last_seen: ""
status: "Unknown (limited public reporting beyond 2016)"
motivations: ["Espionage","Surveillance"]
objectives: ["Compromise Syrian opposition-associated individuals","Collect sensitive information from Windows systems and Android devices","Monitor victim activity using commodity RAT capabilities"]
victimology_summary: "Group5 is tracked as a suspected Iran-linked threat group targeting individuals connected to the Syrian opposition using spearphishing and watering-hole style delivery with Syrian/Iranian-themed lures. Public reporting ties the activity to commodity Windows RATs (NanoCore and njRAT) and an Android RAT (DroidJack)."
target_sectors: ["Civil society / political opposition","Activism","Political organizations"]
target_regions: ["Syria","Syrian diaspora (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/NanoCore]]","[[30_CIPHER/05_Malware/njRAT]]","[[30_CIPHER/05_Malware/DroidJack]]"]
tools: []
infrastructure: ["[[Spearphishing Attachment]]","[[Watering hole]]","[[Theme-based lures]]","[[Iran-hosted infrastructure]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]","[[20_Entities/07_TTPs/T1113 - Screen Capture]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]","[[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]","[[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Group5 (G0043): https://attack.mitre.org/groups/G0043/","Citizen Lab — Group5: Syria and the Iranian Connection (2016-08-02): https://citizenlab.ca/2016/08/group5-syria/","SecurityWeek — Iranian Actor 'Group5' Targeting Syrian Opposition (2016-08-04): https://www.securityweek.com/iranian-actor-group5-targeting-syrian-opposition/","MITRE ATT&CK — NanoCore (S0336): https://attack.mitre.org/software/S0336/","MITRE ATT&CK — njRAT (S0385): https://attack.mitre.org/software/S0385/","MITRE ATT&CK — DroidJack (S0320): https://attack.mitre.org/software/S0320/"]
tags: ["threat-actor","group5","g0043","iran-nexus-suspected","syria","cyber-espionage","spearphishing","watering-hole"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Group5

## 1. BLUF / Executive Summary
Group5 (MITRE ATT&CK **G0043**) is a suspected Iran-linked cyber espionage activity cluster best known from public reporting describing targeted operations against individuals connected to the **Syrian opposition**. The activity leveraged **spearphishing attachments** and **watering-hole style delivery**, and relied heavily on **commodity RATs** on Windows (notably [[30_CIPHER/05_Malware/NanoCore]] and [[30_CIPHER/05_Malware/njRAT]]) plus an Android RAT ([[30_CIPHER/05_Malware/DroidJack]]). Attribution to an Iranian nexus is **circumstantial** and described as not definitive in authoritative public sources.

## 2. Attribution Notes
- MITRE ATT&CK characterizes Group5 as having a **suspected Iranian nexus**, explicitly noting attribution is **not definite**.
- The primary public technical narrative originates from investigative research describing Iran-linked operational artifacts (e.g., hosting and language cues) while also highlighting uncertainty and the potential for competing hypotheses.

## 3. Motivations & Objectives
- **Primary motivation:** intelligence collection / surveillance aligned to the operational environment of the Syrian conflict.
- **Operational objectives:** obtain access to target endpoints (Windows and Android), maintain control via RAT functionality, and collect data of interest (e.g., user activity and sensitive files) consistent with spyware-style tradecraft.

## 4. Targeting Profile
- **Who:** individuals and networks connected to the **Syrian opposition**, including well-connected political figures and related circles (reported).
- **Where:** Syria-focused targeting with diaspora exposure reported in the primary investigative write-up.
- **Themes:** lure content and staging described as using **Syrian and Iranian themes** to improve social-engineering success.

## 5. Tradecraft Overview
- **Initial access:** [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] (malicious document delivery) and [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]-aligned watering-hole behavior (reported).
- **Tooling philosophy:** reliance on widely available RAT families rather than bespoke malware, paired with tailored lures and staging.
- **Collection behaviors (reported/ATT&CK-tracked):** capability for [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1113 - Screen Capture]], as well as defense-evasion/cleanup behaviors such as [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]] and obfuscation consistent with [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]].

## 6. MITRE ATT&CK Mapping
- Access & Delivery
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- Collection & Monitoring
  - [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
  - [[20_Entities/07_TTPs/T1113 - Screen Capture]]
- Defense Evasion / OPSEC
  - [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
  - [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- Common RAT-Enabled Behaviors (ATT&CK software mapping for RATs associated to Group5)
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
  - [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
  - [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
  - [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
  - [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]
  - [[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/NanoCore]] — modular .NET RAT used by Group5 per MITRE ATT&CK tracking; supports a broad set of surveillance and post-compromise functions.
- [[30_CIPHER/05_Malware/njRAT]] — widely used commodity RAT observed across the Middle East; cited by MITRE as used by Group5.
- [[30_CIPHER/05_Malware/DroidJack]] — Android RAT cited by MITRE as used by Group5 in the Syria-opposition targeting context.

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] delivery to seed initial compromise, using context-relevant bait (reported).
- [[Watering hole]] staging to distribute malicious content via Syria-themed sites/content (reported).
- [[Iran-hosted infrastructure]] and operational artifacts referenced in public analysis as part of the circumstantial Iran-nexus case.

## 9. Campaign History
- **2015-10-03 (reported):** initial discovery path described via a suspicious email with a PowerPoint slideshow attachment sent to a Syrian opposition figure.
- **2016-08-02:** primary public investigative report published, naming the actor “Group5” and outlining circumstantial evidence for an Iranian nexus.
- **2016-08-04:** mainstream coverage summarizes the findings and highlights Windows + Android targeting.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Increase resilience against targeted phishing by prioritizing controls and awareness for high-risk roles (civil society leaders, political staff, advocacy networks).
- Treat **commodity RAT detections** (especially variants of [[30_CIPHER/05_Malware/NanoCore]] and [[30_CIPHER/05_Malware/njRAT]]) as potentially high-impact in Syria-related environments given documented targeting.
- Emphasize visibility for behaviors aligned to [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1113 - Screen Capture]] in endpoints handling sensitive communications.
- For mobile risk, focus on preventing installation of untrusted Android packages and monitoring for RAT-like telemetry consistent with known Android remote-access tooling such as [[30_CIPHER/05_Malware/DroidJack]].

## 12. Analyst Notes
- Confidence is constrained by the age and concentration of public reporting (primarily 2015–2016). Absent newer high-quality reporting, avoid extending claims about current activity level or evolution.
- “Iran (suspected)” should be treated as an **analytic assessment** grounded in circumstantial indicators and explicitly described as non-definitive in authoritative sources.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Group5 (G0043): https://attack.mitre.org/groups/G0043/
- Citizen Lab — Group5: Syria and the Iranian Connection (2016-08-02): https://citizenlab.ca/2016/08/group5-syria/
- SecurityWeek — Iranian Actor “Group5” Targeting Syrian Opposition (2016-08-04): https://www.securityweek.com/iranian-actor-group5-targeting-syrian-opposition/
- MITRE ATT&CK — NanoCore (S0336): https://attack.mitre.org/software/S0336/
- MITRE ATT&CK — njRAT (S0385): https://attack.mitre.org/software/S0385/
- MITRE ATT&CK — DroidJack (S0320): https://attack.mitre.org/software/S0320/

## 14. References
1. MITRE ATT&CK. “Group5 (G0043).” https://attack.mitre.org/groups/G0043/
2. Citizen Lab. “Group5: Syria and the Iranian Connection.” (2016-08-02). https://citizenlab.ca/2016/08/group5-syria/
3. SecurityWeek. “Iranian Actor ‘Group5’ Targeting Syrian Opposition.” (2016-08-04). https://www.securityweek.com/iranian-actor-group5-targeting-syrian-opposition/
4. MITRE ATT&CK. “NanoCore (S0336).” https://attack.mitre.org/software/S0336/
5. MITRE ATT&CK. “njRAT (S0385).” https://attack.mitre.org/software/S0385/
6. MITRE ATT&CK. “DroidJack (S0320).” https://attack.mitre.org/software/S0320/
---
