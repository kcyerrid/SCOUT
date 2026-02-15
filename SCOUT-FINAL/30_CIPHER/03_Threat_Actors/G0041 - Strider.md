---
entity_type: threat_actor
actor_name: "Strider"
common_name: "Strider"
actor_id: "G0041"
actor_type: "Highly targeted cyber espionage group associated with the ProjectSauron platform and the Remsec modular backdoor"
aliases: ["ProjectSauron"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2011-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Covert collection and exfiltration of sensitive information from high-value targets","Operate with extreme stealth and long dwell time via modular tooling and per-victim customization (reported)","Enable data movement from segmented or air-gapped environments using removable media modules (reported)"]
victimology_summary: "Strider (MITRE ATT&CK G0041), also referred to as ProjectSauron, is a highly targeted espionage group publicly disclosed in 2016 and assessed active since at least 2011. MITRE reporting notes victims across Russia, China, Sweden, Belgium, Iran, and Rwanda. The group is associated with the ProjectSauron/Remsec modular malware platform (MITRE S0125), described as an espionage-focused backdoor with Lua-based modules and multiple communication/exfiltration options. Documented tradecraft includes a hidden file system for concealment, credential interception via a password-filter DLL on domain controllers, and the use of internal proxy nodes to enable exfiltration from non-Internet-connected network segments."
target_sectors: ["Government","Diplomatic / foreign affairs (reported)","State-linked organizations (reported)"]
target_regions: ["Russia","China","Sweden","Belgium","Iran","Rwanda"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Remsec]]","[[30_CIPHER/05_Malware/ProjectSauron]]"]
tools: []
infrastructure: ["[[Per-victim tooling customization]]","[[Hidden file system on disk]]","[[Internal proxy nodes]]","[[Multi-protocol C2]]","[[Air-gapped data transfer via USB]]","[[Domain controller credential interception]]"]
ttps: ["[[20_Entities/07_TTPs/T1564.005 - Hide Artifacts: Hidden File System]]","[[20_Entities/07_TTPs/T1556.002 - Modify Authentication Process: Password Filter DLL]]","[[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]","[[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]","[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]","[[20_Entities/07_TTPs/T1059.011 - Command and Scripting Interpreter: Lua]]","[[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]]","[[20_Entities/07_TTPs/T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol]]","[[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]","[[20_Entities/07_TTPs/T1055.001 - Process Injection: Dynamic-link Library Injection]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]","[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]","[[20_Entities/07_TTPs/T1082 - System Information Discovery]]","[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]","[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]","[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Strider (G0041) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0041/","MITRE ATT&CK — Remsec (S0125) (Last Modified 2025-06-06): https://attack.mitre.org/software/S0125/","Kaspersky Securelist — FAQ: The ProjectSauron APT (2016-08-08): https://securelist.com/faq-the-projectsauron-apt/75533/","Kaspersky Securelist — The ProjectSauron APT (PDF Technical Analysis, 2016-08): https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf","Broadcom Community (Symantec Security Response) — Strider: Cyberespionage group turns eye of Sauron on targets (2016-08-08): https://community.broadcom.com/viewdocument/strider-cyberespionage-group-turns?CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments","SecurityWeek — “Strider” Espionage Group Targets China, Russia, Europe (2016-08-08): https://www.securityweek.com/strider-espionage-group-targets-china-russia-europe/"]
tags: ["threat-actor","strider","projectsauron","g0041","remsec","espionage","modular-malware"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Strider

## 1. BLUF / Executive Summary
Strider (MITRE ATT&CK **G0041**), also referred to as **ProjectSauron**, is a highly targeted espionage actor publicly disclosed in 2016 and assessed active since at least **2011**. MITRE lists victims across **Russia, China, Sweden, Belgium, Iran, and Rwanda**. Strider is associated with the **ProjectSauron/Remsec** modular platform (MITRE **S0125**), designed for stealthy, long-term collection and featuring modular capabilities (many written in Lua) and multiple communication/exfiltration options, including mechanisms suitable for segmented or air-gapped environments.

## 2. Attribution Notes
- Public sources do not provide a definitive sponsor or country attribution for Strider/ProjectSauron; reporting generally characterizes the operation as nation-state–grade based on sophistication and targeting scope.
- Alias discipline: “ProjectSauron” is used in public reporting as both the campaign/platform name and an associated group label; this note anchors the actor identity to **MITRE G0041**.

## 3. Motivations & Objectives
- **Primary motivation:** strategic intelligence collection.
- **Operational objectives:** stealthy persistence, credential access at privileged choke points (e.g., domain controllers), and exfiltration of sensitive data—including from networks with limited or no direct Internet connectivity (reported).

## 4. Targeting Profile
- **Victim countries (MITRE):** Russia, China, Sweden, Belgium, Iran, Rwanda.
- **Target types (reported):** high-value government/state-linked entities and organizations handling sensitive communications, with campaigns described as low-volume and bespoke.

## 5. Tradecraft Overview
- **Stealth and anti-forensics:** use of a **hidden file system** stored as a file on disk to conceal artifacts ([[20_Entities/07_TTPs/T1564.005 - Hide Artifacts: Hidden File System]]).
- **Credential interception at identity infrastructure:** registration of a **password filter DLL** on domain controllers to capture credentials during logon/password changes ([[20_Entities/07_TTPs/T1556.002 - Modify Authentication Process: Password Filter DLL]]).
- **Segmentation-aware exfiltration:** use of **internal proxy nodes** (systems with both internal and Internet access) to route data out from network segments without direct egress ([[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]).
- **Modular malware design:** Remsec/ProjectSauron described as modular (Lua modules) with multiple C2 and exfiltration pathways (web, mail, DNS, non-app-layer protocols; removable media modules), with strong emphasis on encryption/encoding of stored or transferred data (MITRE S0125).

## 6. MITRE ATT&CK Mapping
- Core group-level behaviors (MITRE G0041)
  - [[20_Entities/07_TTPs/T1564.005 - Hide Artifacts: Hidden File System]]
  - [[20_Entities/07_TTPs/T1556.002 - Modify Authentication Process: Password Filter DLL]]
  - [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]
- Remsec/ProjectSauron platform capabilities associated with Strider (MITRE S0125)
  - [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
  - [[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]
  - [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
  - [[20_Entities/07_TTPs/T1059.011 - Command and Scripting Interpreter: Lua]]
  - [[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]]
  - [[20_Entities/07_TTPs/T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol]]
  - [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]
  - [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
  - [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
  - [[20_Entities/07_TTPs/T1055.001 - Process Injection: Dynamic-link Library Injection]]
  - [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
  - [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
  - [[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]
  - [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
  - [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
  - [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
  - [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
  - [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
  - [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]
  - [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Remsec]] — modular backdoor used by Strider; described as espionage-focused with many Lua-based modules and multiple C2/exfiltration options (MITRE S0125).
- [[30_CIPHER/05_Malware/ProjectSauron]] — reporting name used for the overall platform/campaign; often used interchangeably with Remsec in public references (MITRE and vendor reporting).

## 8. Infrastructure Patterns
- [[Per-victim tooling customization]] to reduce reusable indicators and hinder pattern-based detection (reported).
- [[Hidden file system on disk]] to conceal payloads and operational data.
- [[Internal proxy nodes]] to bridge segmented networks and support exfiltration without direct Internet access from collection points.
- [[Multi-protocol C2]] (web/mail/DNS and other protocols) to provide resiliency and flexibility across constrained environments.
- [[Air-gapped data transfer via USB]] modules to move data from isolated networks to Internet-connected hosts (reported).
- [[Domain controller credential interception]] as a privileged credential access strategy.

## 9. Campaign History
- **2011+ (MITRE):** activity assessed active since at least 2011.
- **2016-08 (public disclosure):** Symantec and Kaspersky publish analyses describing Strider/ProjectSauron operations, the Remsec platform, and small-number, high-value targeting across multiple countries.
- **Post-2016:** public reporting is comparatively limited versus the initial disclosure; MITRE continues to maintain the group/software entries and associated techniques.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Protect identity infrastructure: harden and monitor domain controllers for unusual authentication component changes aligned to [[20_Entities/07_TTPs/T1556.002 - Modify Authentication Process: Password Filter DLL]].
- Prioritize detections for stealth storage and unusual filesystem artifacts aligned to [[20_Entities/07_TTPs/T1564.005 - Hide Artifacts: Hidden File System]].
- Monitor segmentation “bridge” hosts and internal egress chokepoints for proxying behavior aligned to [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]].
- Strengthen controls around removable media in sensitive environments, and monitor for patterns consistent with [[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]].
- Ensure broad protocol-aware monitoring (web/mail/DNS and non-app-layer) and anomaly detection where constrained networks may force unconventional C2.

## 12. Analyst Notes
- Strider/ProjectSauron is characterized in open reporting as exceptionally selective and bespoke; absence of widespread public indicators is consistent with the described operating model rather than evidence of non-activity.
- Technique lists include both group-level behaviors (MITRE G0041) and capabilities associated with the Remsec platform (MITRE S0125). Not all Remsec capabilities may appear in every intrusion.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Strider (G0041): https://attack.mitre.org/groups/G0041/
- MITRE ATT&CK — Remsec (S0125): https://attack.mitre.org/software/S0125/
- Kaspersky Securelist — FAQ: The ProjectSauron APT: https://securelist.com/faq-the-projectsauron-apt/75533/
- Kaspersky Securelist — The ProjectSauron APT (PDF): https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf
- Broadcom Community (Symantec) — Strider overview: https://community.broadcom.com/viewdocument/strider-cyberespionage-group-turns?CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments

## 14. References
1. MITRE ATT&CK. “Strider (G0041).” (Last Modified 2025-04-25). https://attack.mitre.org/groups/G0041/
2. MITRE ATT&CK. “Remsec (S0125).” (Last Modified 2025-06-06). https://attack.mitre.org/software/S0125/
3. Kaspersky Securelist. “FAQ: The ProjectSauron APT.” (2016-08-08). https://securelist.com/faq-the-projectsauron-apt/75533/
4. Kaspersky Securelist (GReAT). “The ProjectSauron APT” (PDF Technical Analysis). (2016-08). https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf
5. Broadcom Community (Symantec Security Response). “Strider: Cyberespionage group turns eye of Sauron on targets.” (2016-08-08). https://community.broadcom.com/viewdocument/strider-cyberespionage-group-turns?CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments
6. SecurityWeek. “'Strider' Espionage Group Targets China, Russia, Europe.” (2016-08-08). https://www.securityweek.com/strider-espionage-group-targets-china-russia-europe/
---
