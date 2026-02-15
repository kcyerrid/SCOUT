---
entity_type: "threat_actor"
actor_name: "Deep Panda"
common_name: "Deep Panda"
actor_id: "G0009"
actor_type: "Nation-state / cyber espionage (suspected)"
aliases: ["Shell Crew", "WebMasters", "KungFu Kittens", "PinkPanther", "Black Vine"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: ""
last_seen: ""
status: "Unknown"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Strategic intelligence collection", "Credential theft and access enablement", "Long-term access and persistence", "Data theft"]
victimology_summary: "MITRE ATT&CK describes Deep Panda as a suspected Chinese threat group targeting multiple industries including government, defense, financial, and telecommunications; public reporting also attributes the Anthem healthcare intrusion to Deep Panda. Some analysts track Deep Panda and APT19 as the same group, but MITRE notes it is unclear from open sources if they are the same."
target_sectors: ["Government", "Defense", "Financial", "Telecommunications", "Healthcare"]
target_regions: ["United States"]
related_groups: ["APT19 (disputed overlap)"]
malware: ["[[30_CIPHER/05_Malware/Derusbi]]", "[[30_CIPHER/05_Malware/Mivast]]", "[[30_CIPHER/05_Malware/Sakula]]", "[[30_CIPHER/05_Malware/StreamEx]]"]
tools: ["[[30_CIPHER/05_Malware/Net]]", "[[30_CIPHER/05_Malware/Ping]]", "[[30_CIPHER/05_Malware/Tasklist]]", "[[30_CIPHER/05_Malware/PowerShell]]", "[[30_CIPHER/05_Malware/regsvr32]]", "[[30_CIPHER/05_Malware/WMI]]"]
infrastructure: ["[[Web Shell]]", "[[Publicly Accessible Web Server]]", "[[SMB/Windows Admin Shares]]", "[[RDP]]", "[[Stolen Code Signing Certificates]]"]
ttps: ["[[20_Entities/07_TTPs/T1059.001 - PowerShell]]", "[[20_Entities/07_TTPs/T1546.008 - Accessibility Features]]", "[[20_Entities/07_TTPs/T1564.003 - Hidden Window]]", "[[20_Entities/07_TTPs/T1027.005 - Indicator Removal from Tools]]", "[[20_Entities/07_TTPs/T1057 - Process Discovery]]", "[[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares]]", "[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]", "[[20_Entities/07_TTPs/T1505.003 - Web Shell]]", "[[20_Entities/07_TTPs/T1218.010 - Regsvr32]]", "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0009): Deep Panda (Last modified 2025-04-16)","CrowdStrike (2014-11-24): DEEP PANDA uses Sakula malware to target multiple sectors","ThreatConnect (2015-02-27): The Anthem Hack: All Roads Lead to China","Reuters (2015-06-20): Hunt for Deep Panda intensifies amid US-China cyber tensions","RSA Incident Response (2014-01): Emerging Threat Profile: Shell Crew (referenced by MITRE)"]
tags: ["threat-actor", "apt", "china", "cyber-espionage", "deep-panda", "shell-crew", "black-vine", "mitre-g0009"]
---

# Deep Panda

## 1. BLUF / Executive Summary
Deep Panda (MITRE ATT&CK **G0009**) is a suspected China-nexus cyber espionage threat group associated in public reporting with targeting across government, defense, financial services, telecommunications, and healthcare. MITRE ATT&CK and vendor reporting link the group to intrusions involving web-access footholds (including [[Web Shell]] usage), credential-enabled lateral movement, and multiple malware families such as [[30_CIPHER/05_Malware/Sakula]] and [[30_CIPHER/05_Malware/Derusbi]]. The Anthem healthcare intrusion is publicly attributed to Deep Panda in widely cited reporting.

## 2. Attribution Notes
- MITRE ATT&CK classifies Deep Panda as **suspected Chinese** and notes it is also known as **Shell Crew**, **WebMasters**, **KungFu Kittens**, **PinkPanther**, and **Black Vine**.
- Public attribution is complicated by **cluster overlap**: MITRE notes some analysts track Deep Panda and **APT19** as the same group, but emphasizes that open sources are **unclear** on equivalence.
- Reporting that links Deep Panda to high-profile incidents (e.g., Anthem) should be treated as attribution within the limits of public evidence and naming conventions.

## 3. Motivations & Objectives
- **Motivation:** Strategic intelligence collection consistent with state-aligned espionage.
- **Objectives:** Establish and maintain durable access, collect sensitive data (including identity and organizational information), and enable continued collection through credential theft and remote movement.

## 4. Targeting Profile
- **Sectors (reported):** Government, defense, financial services, telecommunications, and healthcare.
- **Regions (reported/attributed):** Public reporting prominently references U.S.-based victim organizations; broader geographic scope is not consistently enumerated in the core authoritative sources cited here.

## 5. Tradecraft Overview
- **Execution & in-memory activity:** Use of PowerShell for in-memory download/execute behaviors consistent with [[20_Entities/07_TTPs/T1059.001 - PowerShell]] and concealment via hidden windows consistent with [[20_Entities/07_TTPs/T1564.003 - Hidden Window]].
- **Credential-enabled lateral movement:** Movement using compromised credentials over Windows shares consistent with [[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares]] and discovery of reachable systems consistent with [[20_Entities/07_TTPs/T1018 - Remote System Discovery]].
- **Web footholds:** Use of [[Web Shell]] on [[Publicly Accessible Web Server]] assets consistent with [[20_Entities/07_TTPs/T1505.003 - Web Shell]].
- **Living-off-the-land execution:** Use of regsvr32.exe for proxy execution consistent with [[20_Entities/07_TTPs/T1218.010 - Regsvr32]].
- **Operator tradecraft:** Use of basic discovery utilities (e.g., [[30_CIPHER/05_Malware/Tasklist]]) and WMI activity consistent with [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1059.001 - PowerShell]]
- [[20_Entities/07_TTPs/T1546.008 - Accessibility Features]]
- [[20_Entities/07_TTPs/T1564.003 - Hidden Window]]
- [[20_Entities/07_TTPs/T1027.005 - Indicator Removal from Tools]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1505.003 - Web Shell]]
- [[20_Entities/07_TTPs/T1218.010 - Regsvr32]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]

## 7. Malware & Tools Used
- **Malware (MITRE ATT&CK software associated with Deep Panda):**
  - [[30_CIPHER/05_Malware/Derusbi]]
  - [[30_CIPHER/05_Malware/Mivast]]
  - [[30_CIPHER/05_Malware/Sakula]]
  - [[30_CIPHER/05_Malware/StreamEx]]
- **Tools / utilities (MITRE ATT&CK software and technique-context utilities associated with Deep Panda reporting):**
  - [[30_CIPHER/05_Malware/Net]]
  - [[30_CIPHER/05_Malware/Ping]]
  - [[30_CIPHER/05_Malware/Tasklist]]
  - [[30_CIPHER/05_Malware/PowerShell]]
  - [[30_CIPHER/05_Malware/regsvr32]]
  - [[30_CIPHER/05_Malware/WMI]]

## 8. Infrastructure Patterns
- Web footholds via [[Web Shell]] on [[Publicly Accessible Web Server]] assets to enable access and pivoting.
- Lateral movement facilitated by [[SMB/Windows Admin Shares]] and Windows-native remote administration mechanisms.
- Reporting describes malware (notably [[30_CIPHER/05_Malware/Sakula]]) observed signed with [[Stolen Code Signing Certificates]] in some campaigns.

## 9. Campaign History
- **2014 (reporting):** Public reporting describes Deep Panda activity against U.S. national security organizations and multi-sector targeting tied to malware delivery and post-compromise operations.
- **2015 (reporting):** The Anthem intrusion is publicly attributed to Deep Panda in widely cited industry reporting; contemporaneous journalism also frames Deep Panda as a leading suspect in major U.S. government-related breaches, reflecting heightened attention to the cluster and its aliases.
- **Ongoing tracking:** MITRE ATT&CK continues to maintain Deep Panda (G0009) as a distinct group entry, while noting ambiguity in open sources regarding overlap with APT19.

## 10. Known Indicators
No stable public indicators are included in this note. Deep Panda is assessed as a long-running espionage actor with expected infrastructure and tooling churn; IOC handling should rely on incident-specific validation and current authoritative reporting.

## 11. Defensive Recommendations
- Prioritize detection of script-driven execution and concealment patterns consistent with [[20_Entities/07_TTPs/T1059.001 - PowerShell]] and [[20_Entities/07_TTPs/T1564.003 - Hidden Window]] when correlated with suspicious network retrieval or execution chains.
- Emphasize monitoring for credential-enabled movement via file shares consistent with [[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares]] and host reachability discovery consistent with [[20_Entities/07_TTPs/T1018 - Remote System Discovery]].
- Maintain strong visibility and hardening for public-facing web infrastructure to reduce risk of [[20_Entities/07_TTPs/T1505.003 - Web Shell]] footholds.
- Treat regsvr32-based proxy execution consistent with [[20_Entities/07_TTPs/T1218.010 - Regsvr32]] as higher-signal when combined with corroborating Deep Panda victimology and associated malware detections.

## 12. Analyst Notes
- **Attribution confidence:** Medium (strong MITRE cluster definition and multiple reputable sources, but ambiguity remains regarding overlap with APT19 and alias reuse).
- **Name/alias risk:** Deep Panda is frequently discussed alongside multiple alias sets (Shell Crew, Black Vine, etc.); analysts should prefer evidence-driven clustering (software + TTPs + victimology) over label matching.
- **Technique scope:** The ATT&CK technique list reflects behaviors documented across sources; it should not be interpreted as universal across all intrusions attributed to Deep Panda.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Deep Panda (G0009)  
  https://attack.mitre.org/groups/G0009/
- CrowdStrike — “I am Ironman: DEEP PANDA Uses Sakula Malware to Target Organizations in Multiple Sectors” (2014-11-24)  
  https://www.crowdstrike.com/en-us/blog/ironman-deep-panda-uses-sakula-malware-target-organizations-multiple-sectors/
- ThreatConnect — “The Anthem Hack: All Roads Lead to China” (2015-02-27)  
  https://www.threatconnect.com/blog/anthem-hack-all-roads-lead-china/
- Reuters — “Hunt for Deep Panda intensifies in trenches of U.S.-China cyberwar” (2015-06-20)  
  https://www.reuters.com/article/technology/hunt-for-deep-panda-intensifies-in-trenches-of-us-china-cyberwar-idUSKBN0P1023/

## 14. References
- MITRE ATT&CK. “Deep Panda (G0009).” (Last modified 2025-04-16)  
  https://attack.mitre.org/groups/G0009/
- CrowdStrike. “I am Ironman: DEEP PANDA Uses Sakula Malware to Target Organizations in Multiple Sectors.” (2014-11-24)  
  https://www.crowdstrike.com/en-us/blog/ironman-deep-panda-uses-sakula-malware-target-organizations-multiple-sectors/
- ThreatConnect. “The Anthem Hack: All Roads Lead to China.” (2015-02-27)  
  https://www.threatconnect.com/blog/anthem-hack-all-roads-lead-china/
- Reuters. “Hunt for Deep Panda intensifies in trenches of U.S.-China cyberwar.” (2015-06-20)  
  https://www.reuters.com/article/technology/hunt-for-deep-panda-intensifies-in-trenches-of-us-china-cyberwar-idUSKBN0P1023/
