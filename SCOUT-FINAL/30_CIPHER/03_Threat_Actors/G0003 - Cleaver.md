---
entity_type: "threat_actor"
actor_name: "Cleaver"
common_name: "Cleaver"
actor_id: "G0003"
actor_type: "Nation-state / cyber espionage (attributed)"
aliases: ["Threat Group 2889", "TG-2889"]
country_of_origin: "Iran (attributed)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2012-01"
last_seen: ""
status: "Unknown"
motivations: ["Strategic intelligence collection (espionage)", "Potential sabotage / disruption"]
objectives: ["Long-term access and persistence", "Data theft", "Strategic intelligence collection", "Preparation for disruptive impact (reported as potential)"]
victimology_summary: "Public reporting attributes Operation Cleaver activity to Iranian actors targeting government agencies and a wide range of critical infrastructure and industrial sectors globally. Reporting describes use of both publicly available and customized tooling, including credential theft and network-level manipulation, alongside social engineering via fake professional personas."
target_sectors: ["Government", "Military", "Oil and Gas", "Energy and Utilities", "Transportation", "Airlines", "Airports", "Hospitals", "Telecommunications", "Technology", "Education", "Aerospace", "Defense Industrial Base (DIB)", "Chemical"]
target_regions: ["Canada", "China", "England", "France", "Germany", "India", "Israel", "Kuwait", "Mexico", "Pakistan", "Qatar", "Saudi Arabia", "South Korea", "Turkey", "United Arab Emirates", "United States"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/TinyZBot]]", "[[30_CIPHER/05_Malware/Net Crawler]]"]
tools: ["[[30_CIPHER/05_Malware/Mimikatz]]", "[[30_CIPHER/05_Malware/PsExec]]", "[[30_CIPHER/05_Malware/Windows Credential Editor]]", "[[30_CIPHER/05_Malware/Shell Creator 2]]"]
infrastructure: ["[[Fake LinkedIn Profiles]]", "[[Social Engineering]]", "[[Custom Tooling]]", "[[ARP Poisoning]]", "[[ASP.NET Web Shell]]"]
ttps: ["[[20_Entities/07_TTPs/T1557.002 - Adversary-in-the-Middle: ARP Cache Poisoning]]", "[[20_Entities/07_TTPs/T1587.001 - Develop Capabilities: Malware]]", "[[20_Entities/07_TTPs/T1585.001 - Establish Accounts: Social Media Accounts]]", "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]", "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0003): Cleaver (last modified 2025-04-16)","Cylance (2014-12) Operation Cleaver report (hosted PDF via ACLU)","SecureWorks CTU (2015-10-07): Network of fake LinkedIn profiles tied to TG-2889"]
tags: ["threat-actor", "apt", "iran", "cyber-espionage", "operation-cleaver", "cleaver", "tg-2889", "mitre-g0003"]
---

# Cleaver

## 1. BLUF / Executive Summary
Cleaver (MITRE ATT&CK **G0003**, associated with **TG-2889 / Threat Group 2889**) is attributed in public reporting to Iranian actors and linked to activity tracked as **Operation Cleaver**. Reporting describes targeting of government agencies and a broad set of critical infrastructure and industrial sectors across multiple countries since at least 2012, with operations characterized by customized tooling (including network manipulation and credential theft) and social engineering via [[Fake LinkedIn Profiles]].

## 2. Attribution Notes
- MITRE ATT&CK attributes Cleaver to Iranian actors and links the cluster to activity tracked as **Operation Cleaver**, with circumstantial evidence suggesting linkage to **TG-2889**.
- Public reporting uses multiple labels (Cleaver vs. TG-2889). Treat these as analytic tracking designations; attribution should be based on converging evidence (TTPs, software, and infrastructure), not naming alone.

## 3. Motivations & Objectives
- **Espionage-focused objectives** are emphasized in reporting: intelligence collection, theft, and persistent access to high-value networks.
- Reporting also discusses **potential disruptive intent** (e.g., establishing footholds that could enable sabotage), but this should be treated as assessed potential rather than confirmed execution.

## 4. Targeting Profile
- **Sectors:** Reporting enumerates a wide range of targets including government, military, oil and gas, energy/utilities, transportation (including airlines/airports), hospitals, telecommunications, technology, education, aerospace, defense industrial base, and chemical companies.
- **Geography:** Reporting lists victims across North America, Europe, the Middle East, and Asia (see YAML `target_regions` for the specifically enumerated countries).

## 5. Tradecraft Overview
- **Custom capability development:** Public reporting describes customized tools and payloads for functions including encryption, credential dumping, web backdoors (including [[ASP.NET Web Shell]]), system and process enumeration, and network/interface sniffing.
- **Network-level manipulation:** MITRE documents use of ARP cache poisoning supported by custom tooling (see [[20_Entities/07_TTPs/T1557.002 - Adversary-in-the-Middle: ARP Cache Poisoning]]).
- **Credential access:** Use of credential dumping tooling is described, including commodity tools such as [[30_CIPHER/05_Malware/Mimikatz]] and [[30_CIPHER/05_Malware/Windows Credential Editor]].
- **Social engineering enablement:** TG-2889-linked reporting describes creation of convincing fake professional personas via [[Fake LinkedIn Profiles]] to support [[Social Engineering]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1557.002 - Adversary-in-the-Middle: ARP Cache Poisoning]]
- [[20_Entities/07_TTPs/T1587.001 - Develop Capabilities: Malware]]
- [[20_Entities/07_TTPs/T1585.001 - Establish Accounts: Social Media Accounts]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]

## 7. Malware & Tools Used
- **Malware (reported / tracked):**
  - [[30_CIPHER/05_Malware/TinyZBot]]
  - [[30_CIPHER/05_Malware/Net Crawler]]
- **Tools (reported / tracked):**
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/Windows Credential Editor]]
  - [[30_CIPHER/05_Malware/PsExec]]
  - [[30_CIPHER/05_Malware/Shell Creator 2]]

## 8. Infrastructure Patterns
- Use of [[Fake LinkedIn Profiles]] forming interconnected persona networks to facilitate [[Social Engineering]] and target development.
- Use of [[Custom Tooling]] aligned with both offensive network manipulation (e.g., [[ARP Poisoning]]) and web backdoors (including [[ASP.NET Web Shell]]) as described in public reporting.
- Reliance on commodity post-compromise tooling (e.g., credential access utilities) consistent with [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]].

## 9. Campaign History
- **2012 (reported):** Operation Cleaver reporting describes activity dating back to at least 2012, including persistence and extraction of sensitive materials from government agencies and critical infrastructure organizations.
- **2014-12 (reporting):** A major public report (Operation Cleaver) details multi-sector global targeting and describes the use of customized and publicly available tools.
- **2015-10 (reporting):** TG-2889 reporting describes a network of fake LinkedIn personas assessed to support targeting via social engineering.

## 10. Known Indicators
No stable public indicators are included in this note due to the age of the most detailed reporting, expected infrastructure churn, and the risk of stale/reused artifacts. Use incident-specific, validated telemetry for any IOC handling.

## 11. Defensive Recommendations
- Prioritize detection of credential theft and post-compromise credential access behaviors consistent with [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]].
- Increase visibility for anomalous network behaviors that could indicate [[20_Entities/07_TTPs/T1557.002 - Adversary-in-the-Middle: ARP Cache Poisoning]] in environments where such manipulation would be plausible.
- Treat professional-network persona outreach and unexpected recruiting/connection activity as potential precursors to [[Social Engineering]], particularly where it aligns with sector-specific targeting narratives in public reporting.
- Maintain awareness that operations may blend customized components with commodity utilities (as reflected by [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]), complicating attribution by tooling alone.

## 12. Analyst Notes
- **Attribution confidence:** Medium (strong public attribution and MITRE tracking, but limited recent public reporting that cleanly extends the cluster beyond historical Operation Cleaver characterization).
- **Analytic caution:** “Cleaver” and “TG-2889” overlap in public reporting; use a bounded definition anchored to corroborated TTPs, software, and infrastructure patterns.
- **Operational implication:** The mix of customized capability development and commodity utilities increases the risk of false positives if assessments rely on generic tools without context.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Cleaver (G0003)  
  https://attack.mitre.org/groups/G0003/
- Cylance — Operation Cleaver (PDF hosted via ACLU)  
  https://www.aclu.org/sites/default/files/field_document/Cylance-Operation-Cleaver-Report-1748-1833.pdf
- SecureWorks CTU — Hacker Group Creates Network of Fake LinkedIn Profiles (2015-10-07)  
  https://www.sophos.com/en-us/research/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles

## 14. References
- MITRE ATT&CK. “Cleaver (G0003).” (Last modified 2025-04-16)  
  https://attack.mitre.org/groups/G0003/
- Cylance. “Operation Cleaver.” (2014-12) PDF hosted via ACLU  
  https://www.aclu.org/sites/default/files/field_document/Cylance-Operation-Cleaver-Report-1748-1833.pdf
- SecureWorks CTU (now Sophos). “Hacker Group Creates Network of Fake LinkedIn Profiles.” (2015-10-07)  
  https://www.sophos.com/en-us/research/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles
