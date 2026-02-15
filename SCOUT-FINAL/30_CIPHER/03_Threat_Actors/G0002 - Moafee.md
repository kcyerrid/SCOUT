---
entity_type: threat_actor
actor_name: "Moafee"
common_name: "Moafee"
actor_id: "G0002"
actor_type: "Nation-state / cyber espionage (suspected)"
aliases: []
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2014-09-10"
last_seen: ""
status: "Unknown"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Strategic intelligence collection", "Defense-related intelligence collection"]
victimology_summary: "Public reporting characterizes Moafee as operating from China’s Guangdong Province and targeting military organizations and governments of countries with interests in the South China Sea, including entities within the U.S. defense industrial base. Reporting also describes a relationship (direct or indirect) with DragonOK based on overlapping TTPs and similar custom tools."
target_sectors: ["Government", "Military", "Defense Industrial Base"]
target_regions: ["South China Sea region", "United States"]
related_groups: ["DragonOK"]
malware: ["[[30_CIPHER/05_Malware/PoisonIvy]]", "[[30_CIPHER/05_Malware/CT]]", "[[30_CIPHER/05_Malware/NewCT]]", "[[30_CIPHER/05_Malware/NewCT2]]", "[[30_CIPHER/05_Malware/Mongall]]", "[[30_CIPHER/05_Malware/NFlog]]"]
tools: ["[[30_CIPHER/05_Malware/HTRAN]]"]
infrastructure: ["[[CHINANET]]", "[[Command and Control Server]]", "[[Proxy Infrastructure]]", "[[Password-Protected Documents]]", "[[Decoy Document]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment]]", "[[20_Entities/07_TTPs/T1090 - Proxy]]", "[[20_Entities/07_TTPs/T1497.001 - System Checks]]", "[[20_Entities/07_TTPs/T1027.001 - Binary Padding]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0002): Moafee (last modified 2025-04-25)","FireEye (archived) (2014-09-10): The Path to Mass-Producing Cyber Attacks","Council on Foreign Relations Cyber Operations Tracker: Moafee (report date Sep 2014)","SecurityWeek (2014-09-11): Chinese Attack Groups Operate in Parallel in Cyber Espionage Campaigns"]
tags: ["threat-actor", "apt", "china", "cyber-espionage", "moafee", "mitre-g0002"]
---

# Moafee

## 1. BLUF / Executive Summary
Moafee (MITRE ATT&CK **G0002**) is a suspected China-based cyber espionage threat group publicly reported as operating from Guangdong Province and targeting military organizations and governments associated with South China Sea interests, including elements of the U.S. defense industrial base. Reporting describes spearphishing-led intrusion activity and shared/overlapping tooling and tradecraft with [[DragonOK]], including use of [[30_CIPHER/05_Malware/HTRAN]] proxying and multiple RAT/backdoor families (e.g., [[30_CIPHER/05_Malware/PoisonIvy]], [[30_CIPHER/05_Malware/NFlog]], [[30_CIPHER/05_Malware/NewCT]]).

## 2. Attribution Notes
- Public attribution is **assessed/suspected** (not judicially proven in the core sources used here).
- MITRE ATT&CK notes Moafee “appears to operate” from Guangdong Province and is thought to have a **direct or indirect relationship** with [[DragonOK]] due to overlapping TTPs and similar custom tools.
- “Moafee” is reported to be named from observed command-and-control infrastructure; label stability should be treated cautiously when mapping historic reporting to current activity clusters.

## 3. Motivations & Objectives
- **Primary motivation:** Espionage aligned with strategic and defense-related intelligence requirements.
- **Operational objectives:** Collect sensitive information from government/military-related targets and defense-adjacent organizations tied to regional interests.

## 4. Targeting Profile
- **Target sets (reported):** Military organizations and governments connected to South China Sea interests; reporting explicitly notes targeting that includes the U.S. defense industrial base.
- **Regional focus (reported):** South China Sea-related geopolitical interest space; U.S.-based defense industry targets are specifically referenced in reporting.

## 5. Tradecraft Overview
- **Initial access (reported):** Spearphishing emails with attachments, including password-protected documents and embedded executables consistent with [[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment]].
- **Defense evasion (reported):** File-size inflation via padding (including null bytes) consistent with [[20_Entities/07_TTPs/T1027.001 - Binary Padding]]; environment checks such as CPU core count consistent with [[20_Entities/07_TTPs/T1497.001 - System Checks]].
- **C2 concealment (reported):** Use of proxy tooling (notably [[30_CIPHER/05_Malware/HTRAN]]) consistent with [[20_Entities/07_TTPs/T1090 - Proxy]], and operation of [[Command and Control Server]] infrastructure on [[CHINANET]] (as described in reporting).
- **Operator tradecraft (reported):** Use of [[Decoy Document]] content presented to victims while malware executes in the background.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1090 - Proxy]]
- [[20_Entities/07_TTPs/T1497.001 - System Checks]]
- [[20_Entities/07_TTPs/T1027.001 - Binary Padding]]

## 7. Malware & Tools Used
- **Malware / backdoors / RATs (reported):**
  - [[30_CIPHER/05_Malware/PoisonIvy]]
  - [[30_CIPHER/05_Malware/CT]]
  - [[30_CIPHER/05_Malware/NewCT]]
  - [[30_CIPHER/05_Malware/NewCT2]]
  - [[30_CIPHER/05_Malware/Mongall]]
  - [[30_CIPHER/05_Malware/NFlog]]
- **Tools (reported):**
  - [[30_CIPHER/05_Malware/HTRAN]] (proxy/relay utility referenced in reporting and ATT&CK context)

## 8. Infrastructure Patterns
- Reported operation of multiple [[Command and Control Server]] nodes on [[CHINANET]] (infrastructure locality characteristics referenced in public reporting).
- [[Proxy Infrastructure]] via [[30_CIPHER/05_Malware/HTRAN]] to obscure origin and complicate attribution.
- Delivery tradecraft involving [[Password-Protected Documents]] and large padded payloads to reduce scanning efficacy and evade some controls.
- Use of [[Decoy Document]] lures aligned to targeted spearphishing operations.

## 9. Campaign History
- **2014-09:** Public reporting describes Moafee as one of two China-based espionage groups operating “in parallel,” highlighting distinct regional operations (Guangdong for Moafee) and overlapping toolchains with [[DragonOK]]. The same reporting connects Moafee’s targeting to South China Sea-related interests and U.S. defense industrial base targets.
- **Ongoing characterization:** MITRE ATT&CK maintains a Moafee group entry and links the group to overlapping tradecraft with [[DragonOK]]; publicly available reporting in core sources does not provide a reliable “end date” for activity.

## 10. Known Indicators
No high-confidence, stable public indicators are included in this note. Moafee reporting is largely tradecraft- and tooling-centric, and historic infrastructure can be repurposed or no longer relevant.

## 11. Defensive Recommendations
- Strengthen resilience against targeted email-borne intrusion activity consistent with [[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment]] (focus on reducing successful attachment execution and improving detection of suspicious attachment-driven process chains).
- Improve visibility for proxy-mediated command-and-control patterns consistent with [[20_Entities/07_TTPs/T1090 - Proxy]] and environments where relay utilities such as [[30_CIPHER/05_Malware/HTRAN]] may be present.
- Treat unusually large binaries and padding anomalies as potential weak signals for [[20_Entities/07_TTPs/T1027.001 - Binary Padding]], especially when correlated with targeted-phishing context.
- Incorporate sandbox/analysis-evasion awareness into triage and enrichment workflows for suspected targeted intrusions (e.g., behaviors consistent with [[20_Entities/07_TTPs/T1497.001 - System Checks]]).

## 12. Analyst Notes
- **Attribution confidence:** Medium (multiple reputable sources and MITRE tracking; however, the foundational reporting is older and attribution remains “appears/suspected”).
- **Cluster relationships:** Public reporting emphasizes overlaps with [[DragonOK]] (shared TTPs/tools). Treat “Moafee” as a bounded analytic label tied to convergent evidence rather than a guaranteed continuous organization.
- **Time horizon caution:** Most detailed reporting is dated (Sep 2014). Use current telemetry and up-to-date vendor/government reporting to confirm relevance during incident response.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Moafee (G0002)  
  https://attack.mitre.org/groups/G0002/
- FireEye (archived) — The Path to Mass-Producing Cyber Attacks (2014-09-10)  
  https://web.archive.org/web/20140914215115/http://www.fireeye.com:80/blog/technical/targeted-attack/2014/09/the-path-to-mass-producing-cyber-attacks.html
- Council on Foreign Relations — Cyber Operations Tracker: Moafee  
  https://www.cfr.org/cyber-operations/moafee
- SecurityWeek — Chinese Attack Groups Operate in Parallel in Cyber Espionage Campaigns: FireEye (2014-09-11)  
  https://www.securityweek.com/chinese-attack-groups-operate-parallel-cyber-espionage-campaigns-fireeye/

## 14. References
- MITRE ATT&CK. “Moafee (G0002).” (Last modified 2025-04-25)  
  https://attack.mitre.org/groups/G0002/
- FireEye (archived via Internet Archive). “The Path to Mass-Producing Cyber Attacks.” (2014-09-10)  
  https://web.archive.org/web/20140914215115/http://www.fireeye.com:80/blog/technical/targeted-attack/2014/09/the-path-to-mass-producing-cyber-attacks.html
- Council on Foreign Relations. “Cyber Operations Tracker: Moafee.” (Report date Sep 2014)  
  https://www.cfr.org/cyber-operations/moafee
- SecurityWeek. “Chinese Attack Groups Operate in Parallel in Cyber Espionage Campaigns: FireEye.” (2014-09-11)  
  https://www.securityweek.com/chinese-attack-groups-operate-parallel-cyber-espionage-campaigns-fireeye/
