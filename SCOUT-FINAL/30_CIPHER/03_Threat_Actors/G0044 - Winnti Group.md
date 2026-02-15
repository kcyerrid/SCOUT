---
entity_type: threat_actor
actor_name: "Winnti Group"
common_name: "Winnti Group"
actor_id: "G0044"
actor_type: "China-nexus cyber espionage and intrusion group historically linked to gaming-sector intrusions and broader supply-chain-enabled operations"
aliases: ["Blackfly","Winnti Umbrella (umbrella label used in public reporting)"]
country_of_origin: "China"
suspected_sponsors: []
attribution_confidence: "High"
first_seen: "2010-01-01"
last_seen: ""
status: "Active (reported; exact current status unclear)"
motivations: ["Espionage","Financial gain (possible/secondary in some activity)"]
objectives: ["Initial access via supply-chain and targeted intrusion paths","Theft and abuse of code-signing certificates to increase trust and persistence","Long-term access and intelligence collection across targeted organizations","Operational expansion beyond gaming into additional sectors over time"]
victimology_summary: "Winnti Group (MITRE ATT&CK G0044) is assessed to have Chinese origins and to be active since at least 2010. Reporting initially emphasized heavy targeting of the video game industry, including compromises linked to update mechanisms and use of signed components, with later reporting describing expanded targeting and multiple major supply-chain incidents associated to Winnti Group tradecraft. MITRE notes reporting that other China-nexus groups (e.g., Axiom, APT17, Ke3chang) are closely linked to Winnti Group. Separate reporting discusses partial overlap between Winnti-related reporting and the actor tracked as APT41 (G0096), but the clusters are not universally treated as identical."
target_sectors: ["Video game industry","Software/IT suppliers (supply chain)","Manufacturing / industrial (reported)","Pharmaceuticals (reported)","Higher education (reported)"]
target_regions: ["East Asia","Europe (reported)","Global (via supply-chain distribution, reported)"]
related_groups: ["Axiom","APT17","Ke3chang","APT41 (partial overlap discussed in public reporting)"]
malware: ["[[30_CIPHER/05_Malware/Winnti for Windows]]","[[30_CIPHER/05_Malware/Winnti for Linux]]","[[30_CIPHER/05_Malware/PlugX]]","[[30_CIPHER/05_Malware/PipeMon]]","[[30_CIPHER/05_Malware/ShadowPad]]","[[30_CIPHER/05_Malware/PortReuse]]","[[30_CIPHER/05_Malware/skip-2.0]]"]
tools: ["[[30_CIPHER/05_Malware/Azazel]]"]
infrastructure: ["[[Supply-chain compromise]]","[[Compromised update/distribution mechanism]]","[[Target-mimicking domains]]","[[Stolen code-signing certificates]]","[[Signed malware]]","[[Rootkit-enabled stealth]]","[[Web-based command and control]]"]
ttps: ["[[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1057 - Process Discovery]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1014 - Rootkit]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Winnti Group (G0044): https://attack.mitre.org/groups/G0044/","MITRE ATT&CK — Winnti for Windows (S0141): https://attack.mitre.org/software/S0141/","MITRE ATT&CK — Winnti for Linux (S0430): https://attack.mitre.org/software/S0430/","MITRE ATT&CK — PlugX (S0013): https://attack.mitre.org/software/S0013/","MITRE ATT&CK — PipeMon (S0501): https://attack.mitre.org/software/S0501/","Kaspersky — Winnti: More than just a game (2013-04-11): https://securelist.com/winnti-more-than-just-a-game/37029/","Kaspersky — “Winnti” | More than just a game (PDF): https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20134508/winnti-more-than-just-a-game-130410.pdf","Kaspersky — Games are over: Winnti is now targeting pharmaceutical companies (2015-06-22): https://securelist.com/games-are-over/70991/","ESET — Connecting the dots: Exposing the arsenal and methods of the Winnti Group (2019-10-14): https://www.welivesecurity.com/2019/10/14/connecting-dots-exposing-arsenal-methods-winnti/","ESET — Connecting the dots (PDF): https://web-assets.esetstatic.com/wls/2019/10/ESET_Winnti.pdf","ESET — No “Game over” for the Winnti Group (PipeMon) (2020-05-21): https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/","Google Cloud / Mandiant — APT41: A Dual Espionage and Cyber Crime Operation (2019-08-07): https://cloud.google.com/blog/topics/threat-intelligence/apt41-dual-espionage-and-cyber-crime-operation","BR/NDR (investigative reporting) — Winnti: Attacking the Heart of the German Industry (2019-07-24): https://web.br.de/interaktiv/winnti/english/","401TRG — Burning Umbrella: Winnti Umbrella report (PDF): https://cyber-peace.org/wp-content/uploads/2018/07/20180503_Burning_Umbrella.pdf","Cybereason — Operation CuckooBees: A Winnti Malware Arsenal Deep Dive (2022-05-02): https://www.cybereason.com/blog/operation-cuckoobees-a-winnti-malware-arsenal-deep-dive"]
tags: ["threat-actor","winnti","g0044","china-nexus","supply-chain","code-signing","gaming-industry","blackfly"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Winnti Group

## 1. BLUF / Executive Summary
Winnti Group (MITRE ATT&CK **G0044**) is a China-origin intrusion and espionage cluster active since at least **2010**, historically prominent for targeting the **gaming industry** and for operations leveraging **supply-chain compromise** and **abuse of code-signing certificates**. Public reporting also describes expanded targeting beyond gaming over time, including high-profile supply-chain activity and intrusions in additional sectors. Naming and clustering are contested in open reporting; some sources discuss a broader “Winnti umbrella” and partial overlaps with other China-nexus clusters (notably APT41), so analytic confidence is highest for **tradecraft themes** (supply chain + code signing + modular backdoors) and more conservative for strict actor boundary claims.

## 2. Attribution Notes
- MITRE assesses Winnti Group as having **Chinese origins** and active since at least **2010**, with a historic emphasis on the gaming industry and later expanded scope.
- “Winnti” is used in public reporting as both a **malware family label** and an **actor label**, and some research frames multiple subclusters under a “Winnti umbrella,” increasing the risk of over-broad attribution.
- Mandiant’s APT41 reporting notes partial coincidence/overlap with “Winnti” reporting, but this does not establish that all “Winnti” activity is synonymous with APT41.

## 3. Motivations & Objectives
- **Primary:** espionage-enabled access and intelligence collection (consistent with long-term intrusion posture and target selection described in multiple reports).
- **Secondary/possible:** financial gain or opportunistic monetization in some subsets of activity (raised as plausible in some vendor narratives discussing downstream actions).

## 4. Targeting Profile
- **Core historical focus:** video game companies and related ecosystem (publishers, developers, distribution/update infrastructure).
- **Expanded scope:** additional industries and regions described over time in reporting, including pharmaceuticals, industrial targets, and universities.
- **Geography:** activity reported across East Asia and Europe, with global downstream exposure when supply-chain distribution is involved.

## 5. Tradecraft Overview
- **Supply-chain enablement:** compromise of upstream software/dev environments or update/distribution channels to push malicious code to downstream victims (central theme in ESET’s linking of multiple supply-chain incidents).
- **Trust abuse via code signing:** theft and use of legitimate certificates (or signed components) to increase execution success and reduce suspicion, aligned with long-running “Winnti” reporting and MITRE’s group technique mapping.
- **Modular backdoor ecosystem:** multiple families and loaders observed over time (e.g., [[30_CIPHER/05_Malware/Winnti for Windows]], [[30_CIPHER/05_Malware/PlugX]], [[30_CIPHER/05_Malware/ShadowPad]], [[30_CIPHER/05_Malware/PipeMon]], [[30_CIPHER/05_Malware/PortReuse]]).
- **Stealth/persistence patterns:** rootkit-enabled stealth is described in Winnti-related reporting, and MITRE maps [[20_Entities/07_TTPs/T1014 - Rootkit]] to Winnti Group activity.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]
- [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1014 - Rootkit]]
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Winnti for Windows]] — modular Windows RAT historically associated with Winnti-related intrusions; tracked by MITRE as used by Winnti Group and also noted as used by multiple groups.
- [[30_CIPHER/05_Malware/Winnti for Linux]] — Linux-targeting trojan in the Winnti malware family; MITRE notes shared use across multiple actors and documents rootkit-related stealth via a modified [[30_CIPHER/05_Malware/Azazel]] userland rootkit.
- [[30_CIPHER/05_Malware/PlugX]] — widely used modular RAT; tracked by MITRE and repeatedly present in Winnti-related reporting.
- [[30_CIPHER/05_Malware/ShadowPad]] — modular backdoor family discussed in Winnti Group supply-chain narratives (ESET’s linking of incidents highlights ShadowPad as part of the ecosystem).
- [[30_CIPHER/05_Malware/PortReuse]] — backdoor described in ESET’s Winnti Group supply-chain analysis as part of tooling used across incidents.
- [[30_CIPHER/05_Malware/PipeMon]] — modular backdoor identified by ESET in 2020 targeting gaming companies; tracked as S0501 in MITRE.
- [[30_CIPHER/05_Malware/skip-2.0]] — MSSQL-focused backdoor publicly reported by ESET as part of Winnti Group tracking (included here as a malware/tool name used in reporting).

## 8. Infrastructure Patterns
- [[Compromised update/distribution mechanism]] and broader [[Supply-chain compromise]] enabling downstream victim reach.
- [[Stolen code-signing certificates]] supporting [[Signed malware]] and trust subversion during execution and persistence.
- [[Target-mimicking domains]] and related domain registration patterns consistent with [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]].
- Use of [[Web-based command and control]] patterns in multiple toolchains described across Winnti-related reporting.
- [[Rootkit-enabled stealth]] observed in Winnti-related tooling and technique mapping.

## 9. Campaign History
- **2010 (at least):** MITRE assesses Winnti Group active since at least this year.
- **2013-04:** Kaspersky publishes early detailed reporting on “Winnti” intrusions tied to the gaming sector, including signed components and update-server compromise themes.
- **2015-06:** Kaspersky reports Winnti-related activity expanding beyond games to targets including pharmaceutical companies.
- **2018-05:** “Winnti umbrella” reporting argues for linkages among multiple China-nexus operations under a broader umbrella construct (useful for hypothesis generation; treat boundaries cautiously).
- **2019-10:** ESET publishes analysis linking multiple major supply-chain incidents via shared tooling/techniques and details Winnti Group methods and arsenal (including [[30_CIPHER/05_Malware/PortReuse]] and [[30_CIPHER/05_Malware/ShadowPad]] narratives).
- **2020-05:** ESET reports discovery of [[30_CIPHER/05_Malware/PipeMon]] used against gaming companies (South Korea and Taiwan), reinforcing continued activity against the gaming sector.

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Treat software supply-chain integrity as a primary risk surface in Winnti-relevant threat models (vendor access, build pipelines, update channels, and distribution trust).
- Increase scrutiny of **code-signing trust events**, especially anomalous or unexpected signing chains and signed modules appearing in unusual contexts, aligned to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]].
- Maintain detections for rootkit-like stealth behaviors and low-level tampering patterns consistent with [[20_Entities/07_TTPs/T1014 - Rootkit]].
- Prioritize behavioral detection and incident triage around modular backdoor ecosystems associated with this cluster (notably [[30_CIPHER/05_Malware/Winnti for Windows]], [[30_CIPHER/05_Malware/PlugX]], [[30_CIPHER/05_Malware/ShadowPad]], [[30_CIPHER/05_Malware/PipeMon]]), focusing on intrusion lifecycle signals rather than brittle indicators.

## 12. Analyst Notes
- **Confidence:** High on China-origin attribution at the level stated by MITRE; Medium on specific campaign linkages when sourced primarily to “umbrella” frameworks; Medium on strict boundaries vs. adjacent clusters (e.g., APT41) due to explicit overlap/partial-coincidence language in public reporting.
- The name “Winnti” is overloaded (malware family vs. actor vs. umbrella). Maintain careful scoping in analytic products to avoid conflating unrelated activity that shares tooling or certificate-theft tradecraft.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Winnti Group (G0044): https://attack.mitre.org/groups/G0044/
- Kaspersky — Winnti: More than just a game (2013): https://securelist.com/winnti-more-than-just-a-game/37029/
- Kaspersky — Games are over: Winnti targeting pharma (2015): https://securelist.com/games-are-over/70991/
- ESET — Connecting the dots (2019): https://www.welivesecurity.com/2019/10/14/connecting-dots-exposing-arsenal-methods-winnti/
- ESET — No “Game over” (PipeMon) (2020): https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/
- BR/NDR — Winnti: Attacking the Heart of the German Industry (2019): https://web.br.de/interaktiv/winnti/english/
- Cybereason — Operation CuckooBees (2022): https://www.cybereason.com/blog/operation-cuckoobees-a-winnti-malware-arsenal-deep-dive

## 14. References
1. MITRE ATT&CK. “Winnti Group (G0044).” https://attack.mitre.org/groups/G0044/
2. MITRE ATT&CK. “Winnti for Windows (S0141).” https://attack.mitre.org/software/S0141/
3. MITRE ATT&CK. “Winnti for Linux (S0430).” https://attack.mitre.org/software/S0430/
4. MITRE ATT&CK. “PlugX (S0013).” https://attack.mitre.org/software/S0013/
5. MITRE ATT&CK. “PipeMon (S0501).” https://attack.mitre.org/software/S0501/
6. Kaspersky. “Winnti: More than just a game.” (2013-04-11). https://securelist.com/winnti-more-than-just-a-game/37029/
7. Kaspersky. “Winnti: More than just a game” (PDF). https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20134508/winnti-more-than-just-a-game-130410.pdf
8. Kaspersky. “Games are over: Winnti is now targeting pharmaceutical companies.” (2015-06-22). https://securelist.com/games-are-over/70991/
9. ESET Research. “Connecting the dots: Exposing the arsenal and methods of the Winnti Group.” (2019-10-14). https://www.welivesecurity.com/2019/10/14/connecting-dots-exposing-arsenal-methods-winnti/
10. ESET Research. “ESET_Winnti.pdf” (Connecting the dots — full report PDF). (2019). https://web-assets.esetstatic.com/wls/2019/10/ESET_Winnti.pdf
11. ESET Research. “No ‘Game over’ for the Winnti Group.” (2020-05-21). https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/
12. Google Cloud / Mandiant. “APT41: A Dual Espionage and Cyber Crime Operation.” (2019-08-07). https://cloud.google.com/blog/topics/threat-intelligence/apt41-dual-espionage-and-cyber-crime-operation
13. BR/NDR. “Winnti: Attacking the Heart of the German Industry.” (2019-07-24). https://web.br.de/interaktiv/winnti/english/
14. 401TRG. “Burning Umbrella” (PDF mirror). (2018-05-03). https://cyber-peace.org/wp-content/uploads/2018/07/20180503_Burning_Umbrella.pdf
15. Cybereason. “Operation CuckooBees: A Winnti Malware Arsenal Deep Dive.” (2022-05-02). https://www.cybereason.com/blog/operation-cuckoobees-a-winnti-malware-arsenal-deep-dive
---
