---
entity_type: threat_actor
actor_name: "MONSOON"
common_name: "Patchwork"
actor_id: "G0040"
actor_type: "Cyber espionage threat group; MONSOON is a campaign/tracking name used by Forcepoint and other reporting for activity aligned to Patchwork"
aliases: ["Patchwork","Dropping Elephant","Hangover Group","Operation Hangover","Chinastrats"]
country_of_origin: "India (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2015-12-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Intelligence collection against diplomatic/government-adjacent targets","Initial access via spearphishing and web-based lure delivery","Exploit client-side vectors using weaponized documents","Maintain access and stage collection with lightweight tooling and modular malware","Use signed malware (including self-signed certificates) to increase trust and reduce detection (reported)"]
victimology_summary: "MONSOON is the name Forcepoint used for an espionage campaign it tracked from May 2016 and assessed to have started in December 2015. Forcepoint and subsequent reporting linked MONSOON to the actor widely tracked as Patchwork (MITRE ATT&CK G0040), also known as Dropping Elephant and Operation Hangover. Open reporting and MITRE describe a persistent espionage focus on government/diplomatic and strategic targets across South Asia, with later reporting also documenting spearphishing activity against U.S. think tanks (2018)."
target_sectors: ["Government","Diplomacy / foreign affairs","Think tanks","International affairs NGOs (reported)"]
target_regions: ["South Asia","United States (think tanks, reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/BADNEWS]]","[[30_CIPHER/05_Malware/BackConfig]]","[[30_CIPHER/05_Malware/AutoIt backdoor]]","[[30_CIPHER/05_Malware/NDiskMonitor]]"]
tools: ["[[30_CIPHER/05_Malware/PowerSploit]]","[[30_CIPHER/05_Malware/QuasarRAT]]","[[30_CIPHER/05_Malware/Meterpreter]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Spearphishing Link]]","[[Watering hole delivery]]","[[Exploit-laden Office documents]]","[[DDE-based execution]]","[[Dead drop resolver]]","[[BITS-based payload delivery]]","[[Self-signed code-signing]]","[[DLL side-loading]]","[[Tracking pixels / web bugs]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]","[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1197 - BITS Jobs]]","[[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]","[[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]","[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Patchwork (G0040): https://attack.mitre.org/groups/G0040/","Forcepoint Security Labs — MONSOON: Analysis of an APT Campaign (PDF) (2016-08-08): https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf","SecurityWeek — MONSOON campaign linked to Patchwork APT (2016-08-12): https://www.securityweek.com/monsoon-cyber-espionage-campaign-linked-patchwork-apt/","Palo Alto Networks Unit 42 — Patchwork (aka Dropping Elephant/Monsoon) BADNEWS delivery (2018-03-07): https://unit42.paloaltonetworks.com/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/","Volexity — Patchwork APT targets US think tanks (2018-06-07): https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/"]
tags: ["threat-actor","monsoon","patchwork","g0040","dropping-elephant","operation-hangover","cyber-espionage","south-asia"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# MONSOON

## 1. BLUF / Executive Summary
MONSOON is a campaign and tracking name introduced by Forcepoint for an espionage operation assessed to have begun in **2015-12** and still active as of **2016-07** in Forcepoint’s reporting. Multiple public sources (including Forcepoint-aligned follow-on coverage and MITRE ATT&CK) link MONSOON to the actor commonly tracked as **Patchwork (G0040)**, also known as **Dropping Elephant** and **Operation Hangover**. The cluster is associated with sustained espionage targeting of government, diplomatic, and strategic organizations, with recurring reliance on spearphishing, weaponized documents, and lightweight modular malware families such as [[30_CIPHER/05_Malware/BADNEWS]].

## 2. Attribution Notes
- **MONSOON** is best treated as a **campaign/tracking label**, not a distinct MITRE actor separate from Patchwork. MITRE tracks the underlying activity cluster as **Patchwork (G0040)**.
- Public reporting consistently frames MONSOON as overlapping with Patchwork/Dropping Elephant/Operation Hangover naming, but definitive sponsor attribution remains unproven; “India (suspected)” appears as an inference in multiple public analyses rather than a primary attribution statement.

## 3. Motivations & Objectives
- Primary objective: **espionage** and strategic intelligence collection.
- Operational objectives: gain initial access through social engineering and client-side vectors; establish persistence and staged collection; maintain low-to-moderate sophistication tradecraft that is repeatable across target sets.

## 4. Targeting Profile
- Frequently reported target types: **government**, **diplomatic/foreign affairs**, and strategic organizations in **South Asia**.
- Additional reporting documents time-bounded targeting of **U.S. think tanks** (2018).

## 5. Tradecraft Overview
- **Spearphishing-led access** using malicious attachments and links; engagement measurement via tracking elements is described in campaign reporting.
- **Weaponized documents** enabling client-side execution/exploitation patterns, with follow-on payload delivery and staging via background mechanisms.
- **C2 indirection** using web content as a dead-drop pointer (dead drop resolver pattern) is a recurrent theme in Patchwork/MONSOON reporting.
- **Trust subversion** via signed malware (including self-signed certificates) is described in campaign analyses to increase execution success and reduce user suspicion.
- A pragmatic blend of custom malware and repurposed/open-source tooling (as reflected in MITRE’s Patchwork entry).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1197 - BITS Jobs]]
- [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]]
- [[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/BADNEWS]] — backdoor family used in Patchwork/MONSOON-linked operations and discussed in multiple vendor reports; commonly associated with web-content-driven C2 patterns.
- [[30_CIPHER/05_Malware/BackConfig]] — Patchwork-attributed modular trojan described in public reporting and tracked by MITRE under the Patchwork actor cluster.
- [[30_CIPHER/05_Malware/AutoIt backdoor]] — reported in Forcepoint’s MONSOON campaign analysis as part of the malware/tooling ecosystem.
- [[30_CIPHER/05_Malware/NDiskMonitor]] — Patchwork-attributed .NET backdoor described in public reporting and tracked by MITRE.
- Supporting/obtained tooling referenced in Patchwork tradecraft narratives:
  - [[30_CIPHER/05_Malware/PowerSploit]]
  - [[30_CIPHER/05_Malware/QuasarRAT]]
  - [[30_CIPHER/05_Malware/Meterpreter]]

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] and [[Spearphishing Link]] delivery, sometimes paired with [[Tracking pixels / web bugs]] for engagement measurement.
- [[Watering hole delivery]] to reach targets via sites relevant to their interests or roles (reported).
- [[Dead drop resolver]] patterns using legitimate web content as indirect C2 pointers.
- [[BITS-based payload delivery]] for background retrieval of additional components.
- [[Self-signed code-signing]] and signed payloads to influence trust decisions.
- [[DLL side-loading]] and related execution-flow hijacking behaviors to run payloads under legitimate binaries.

## 9. Campaign History
- **2015-12 (reported):** Forcepoint assesses MONSOON began in December 2015.
- **2016-05 to 2016-07 (reported):** Forcepoint tracks and analyzes the campaign during this period; publication in 2016 describes ongoing activity.
- **2016-08 (public linkage):** follow-on coverage summarizes Forcepoint’s linkage of MONSOON to Patchwork/Dropping Elephant/Operation Hangover naming.
- **2018-03 (reported):** Unit 42 reports Patchwork (aka Dropping Elephant/Monsoon) delivering updated [[30_CIPHER/05_Malware/BADNEWS]] payloads in the Indian subcontinent.
- **2018-06 (reported):** Volexity reports Patchwork-attributed spearphishing targeting U.S. think tanks.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize protection against **targeted phishing** and **document-driven intrusion chains** in high-risk teams (policy, foreign affairs, research, executive support).
- Maintain visibility for **signed-but-untrusted** or anomalously signed binaries aligned to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]].
- Improve monitoring for **background transfer and staged delivery** behaviors aligned to [[20_Entities/07_TTPs/T1197 - BITS Jobs]] and [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- Watch for **dead-drop-style web indirection** aligned to [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver]] in environments where users routinely access policy/research content.

## 12. Analyst Notes
- This note treats **MONSOON** as a **Patchwork (G0040)**-aligned label to prevent duplicate actor entities that fragment tradecraft and sourcing.
- Public attribution remains circumstantial; avoid overconfidence in sponsor/origin without primary statements.
- Patchwork/MONSOON tooling shows repeated reuse and repurposing; correlation should rely on multi-factor evidence (victimology + infrastructure patterns + malware lineage), not single artifacts.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Patchwork (G0040): https://attack.mitre.org/groups/G0040/
- Forcepoint Security Labs — MONSOON report (PDF): https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf
- Unit 42 — Patchwork (aka Monsoon) BADNEWS delivery: https://unit42.paloaltonetworks.com/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/
- Volexity — Patchwork targets US think tanks: https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/

## 14. References
1. MITRE ATT&CK. “Patchwork (G0040).” https://attack.mitre.org/groups/G0040/
2. Forcepoint Security Labs. “MONSOON – Analysis of an APT Campaign.” (2016-08-08) (PDF). https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf
3. SecurityWeek. “MONSOON Cyber-Espionage Campaign Linked to Patchwork APT.” (2016-08-12). https://www.securityweek.com/monsoon-cyber-espionage-campaign-linked-patchwork-apt/
4. Palo Alto Networks Unit 42. “Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent.” (2018-03-07). https://unit42.paloaltonetworks.com/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/
5. Volexity. “Patchwork APT Group Targets US Think Tanks.” (2018-06-07). https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/
---
