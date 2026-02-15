---
entity_type: threat_actor
actor_name: "Leviathan"
common_name: "Leviathan"
actor_id: "G0065"
actor_type: "State-sponsored (espionage)"
aliases: ["MUDCARP","Kryptonite Panda","Gadolinium","BRONZE MOHAWK","TEMP.Jumper","APT40","TEMP.Periscope","Gingham Typhoon"]
country_of_origin: "China"
suspected_sponsors: ["Ministry of State Security (MSS) - Hainan State Security Department (attributed)"]
attribution_confidence: "High"
first_seen: "2009-01-01"
last_seen: ""
status: "Active"
motivations: ["Espionage","Strategic intelligence collection"]
objectives: ["Initial access via exploitation and phishing","Credential theft and reuse","Data theft and long-term access to targeted networks"]
victimology_summary: "A China state-sponsored espionage group attributed to the MSS Hainan State Security Department in public reporting; targets span academia, aviation/aerospace, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, transportation, and others across multiple regions."
target_sectors: ["Academia","Aerospace / Aviation","Biomedical","Defense Industrial Base","Government","Healthcare","Manufacturing","Maritime","Transportation"]
target_regions: ["United States","Canada","Australia","Europe","Middle East","Southeast Asia"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/BADFLICK]]","[[30_CIPHER/05_Malware/BLACKCOFFEE]]"]
tools: ["[[30_CIPHER/05_Malware/BITSAdmin]]","[[30_CIPHER/05_Malware/at]]"]
infrastructure: ["[[Lookalike Domains]]","[[Vulnerability Scanning]]","[[Web Shells]]","[[Web Services for C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]","[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]","[[20_Entities/07_TTPs/T1212 - Exploitation for Credential Access]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1547.009 - Boot or Logon Autostart Execution: Shortcut Modification]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]","[[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]","[[20_Entities/07_TTPs/T1560 - Archive Collected Data]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0065 Leviathan - https://attack.mitre.org/groups/G0065/","MITRE ATT&CK Campaign - C0049 Leviathan Australian Intrusions - https://attack.mitre.org/campaigns/C0049/","MITRE ATT&CK - S0642 BADFLICK - https://attack.mitre.org/software/S0642/","MITRE ATT&CK - S0069 BLACKCOFFEE - https://attack.mitre.org/software/S0069/","MITRE ATT&CK - S0190 BITSAdmin - https://attack.mitre.org/software/S0190/","MITRE ATT&CK - S0110 at - https://attack.mitre.org/software/S0110/"]
tags: ["scout","threat-actor","mitre-g0065","china","mss","espionage"]
created: "2026-01-01"
last_modified: "2026-01-01"
---

## 1. BLUF / Executive Summary
Leviathan (G0065) is a China state-sponsored espionage actor attributed in public reporting to the MSS Hainan State Security Department. ATT&CK-tracked activity highlights a mature intrusion lifecycle that includes domain acquisition and targeting infrastructure, scanning and exploitation of public-facing systems, extensive credential capture and reuse, and web shell–enabled persistence in victim environments.

## 2. Attribution Notes
MITRE ATT&CK describes attribution to the MSS Hainan State Security Department and notes multiple widely used tracking aliases (including APT40 and others). Public reporting and tracking names can overlap; this note uses ATT&CK’s conservative alignment and explicitly retains multiple aliases without asserting perfect equivalence beyond what ATT&CK states.

## 3. Motivations & Objectives
- Strategic intelligence collection across broad sector targets
- Rapid initial access through exploitation of exposed services and targeted phishing
- Credential theft and reuse to expand access and sustain operations
- Exfiltration of sensitive data, including credentials and operationally useful datasets

## 4. Targeting Profile
- **Sectors (reported):** academia, aerospace/aviation, biomedical, defense, government, healthcare, manufacturing, maritime, transportation
- **Regions (reported):** global, including US/Canada/Australia/Europe/Middle East/Southeast Asia

## 5. Tradecraft Overview
- **Acquire/impersonate infrastructure** (domains) to support targeting and delivery.
- **Reconnaissance and vulnerability scanning** followed by **public-facing exploitation** for initial access.
- **Web shell–centric post-exploitation** for persistence and command execution in compromised environments.
- **Credential capture and reuse** as a core enabling capability for lateral movement and privilege escalation.
- Use of both malware families (e.g., **[[30_CIPHER/05_Malware/BADFLICK]]**, **[[30_CIPHER/05_Malware/BLACKCOFFEE]]**) and common Windows utilities (e.g., **[[30_CIPHER/05_Malware/BITSAdmin]]**, **[[30_CIPHER/05_Malware/at]]**) as reflected in ATT&CK.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
- [[20_Entities/07_TTPs/T1595.002 - Active Scanning: Vulnerability Scanning]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1212 - Exploitation for Credential Access]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]
- [[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1547.009 - Boot or Logon Autostart Execution: Shortcut Modification]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
- [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/BADFLICK]]
  - [[30_CIPHER/05_Malware/BLACKCOFFEE]]
- Tools / dual-use:
  - [[30_CIPHER/05_Malware/BITSAdmin]]
  - [[30_CIPHER/05_Malware/at]]

## 8. Infrastructure Patterns
- [[Lookalike Domains]] used to impersonate legitimate entities (reported)
- [[Vulnerability Scanning]] to identify exploitable and end-of-life systems (reported)
- [[Web Shells]] used extensively after initial access in some campaigns (reported)
- [[Web Services for C2]] including one-way instruction retrieval from profiles on legitimate sites (reported)

## 9. Campaign History
- **2009–present (reported):** Long-running espionage activity across diverse sectors and regions.
- **2022-04 to 2022-09 (reported):** “Leviathan Australian Intrusions” campaign (ATT&CK C0049) describes long-term intrusions leveraging external service exploitation and extensive credential capture/reuse.

## 10. Known Indicators
No public, stable indicators are included in this note.

## 11. Defensive Recommendations
- Reduce exposure of internet-facing services; prioritize rapid patching and asset lifecycle management for end-of-life devices.
- Monitor for web shell–related behaviors and abnormal web server child-process patterns.
- Strengthen credential hygiene and monitoring (MFA where possible, privileged access controls, alerts for credential reuse and anomalous access).
- Expand detections for lateral movement patterns and use of dual-use admin utilities in suspicious contexts.

## 12. Analyst Notes
**Confidence:** High for broad attribution and tradecraft themes due to ATT&CK’s grounding in government and major vendor reporting. Note that individual “alias” mappings across vendors can be imperfect; preserve incident-level context when correlating.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0065/
- https://attack.mitre.org/campaigns/C0049/

## 14. References
- https://attack.mitre.org/groups/G0065/
- https://attack.mitre.org/campaigns/C0049/
- https://attack.mitre.org/software/S0642/
- https://attack.mitre.org/software/S0069/
- https://attack.mitre.org/software/S0190/
- https://attack.mitre.org/software/S0110/
