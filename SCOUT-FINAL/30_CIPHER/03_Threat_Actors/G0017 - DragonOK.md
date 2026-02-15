---
entity_type: threat_actor
actor_name: "DragonOK"
common_name: "DragonOK"
actor_id: "G0017"
actor_type: "Suspected state-linked cyber espionage"
aliases: ["BRONZE OVERBROOK","Shallow Taurus"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2014-09"
last_seen: ""
status: "Unknown"
motivations: ["Espionage","Information theft"]
objectives: ["Strategic and economic intelligence collection","Persistent access to targeted organizations via phishing-led intrusions"]
victimology_summary: "DragonOK (G0017) is a threat group reported for phishing-led intrusions primarily targeting organizations in Japan, with reporting also describing targeting of additional regions including Taiwan, Tibet, and Russia. Public sources link DragonOK activity to multiple RAT/backdoor families (notably Sysget/HelloBridge, PlugX, PoisonIvy, FormerFirstRat, NFlog, and NewCT) and note overlap in tooling and tradecraft with the group Moafee."
target_sectors: ["Manufacturing","High-tech","Technology","Semiconductor","Higher Education","Energy"]
target_regions: ["Japan","Taiwan","Russia","Tibet"]
related_groups: ["[[Moafee]]"]
malware: ["[[30_CIPHER/05_Malware/Sysget]]","[[30_CIPHER/05_Malware/HelloBridge]]","[[30_CIPHER/05_Malware/FormerFirstRat]]","[[30_CIPHER/05_Malware/NFlog]]","[[30_CIPHER/05_Malware/NewCT]]","[[30_CIPHER/05_Malware/PlugX]]","[[30_CIPHER/05_Malware/PoisonIvy]]","[[30_CIPHER/05_Malware/IsSpace]]","[[30_CIPHER/05_Malware/TidePool]]"]
tools: []
infrastructure: ["[[Phishing emails]]","[[Decoy documents]]","[[Malicious attachments]]","[[C2 over HTTP]]","[[C2 over DNS]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1113 - Screen Capture]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1564.001 - Hide Artifacts: Hidden Files and Directories]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — DragonOK (G0017) (Last Modified 2024-11-17)","Palo Alto Networks Unit 42 (2015-04-14) — New DragonOK backdoor malware deployed against Japanese targets","Palo Alto Networks Unit 42 (2017-01-05) — DragonOK updates toolset and targets multiple geographic regions","LAC (2018-01-23) — PlugX activity related to DragonOK (Japan-focused reporting)","Malpedia — DragonOK actor profile (summary and references)","ETDA Threat Group Cards — DragonOK (alias mapping)"]
tags: ["threat-actor","dragonok","g0017","china-suspected","espionage","japan","phishing","rat"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# DragonOK

## 1. BLUF / Executive Summary
DragonOK (MITRE Group **G0017**) is a threat group documented for **phishing-driven intrusions** with a strong emphasis on **Japanese organizations**, and reporting that includes additional targeting beyond Japan (e.g., Taiwan, Tibet, and Russia). Open sources associate DragonOK with multiple backdoor/RAT families—most notably [[30_CIPHER/05_Malware/Sysget]] / [[30_CIPHER/05_Malware/HelloBridge]], [[30_CIPHER/05_Malware/PlugX]], and [[30_CIPHER/05_Malware/PoisonIvy]]—and note tooling overlap suggesting a direct or indirect relationship with [[Moafee]].

## 2. Attribution Notes
- Public attribution commonly assesses DragonOK as **China-linked/suspected**, but open reporting generally frames this as an analytic assessment rather than a formal legal attribution.
- MITRE ATT&CK explicitly notes a likely relationship between DragonOK and [[Moafee]] based on overlapping TTPs and custom tooling.
- Confidence is set to **Medium** given multiple credible vendor/research sources, but limited public primary-source attribution detail.

## 3. Motivations & Objectives
- **Motivation:** Espionage and information theft aligned to strategic/economic interests.
- **Objectives:** Establish access through phishing and maintain persistence using backdoors/RATs to enable collection and exfiltration of sensitive organizational data.

## 4. Targeting Profile
- **Primary geography:** Japan (repeatedly emphasized across reporting).
- **Other reported geographies:** Taiwan, Tibet, Russia.
- **Reported sectors:** Manufacturing, high-tech/technology (including semiconductor), higher education, and energy.

## 5. Tradecraft Overview
- **Initial access:** Spearphishing with malicious attachments consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and execution via [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- **Exploit-assisted delivery (reported):** Use of weaponized document formats exploiting client-side vulnerabilities consistent with [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]].
- **C2 communications:** Reported use of web protocols (HTTP) and, per malware capability documentation, DNS-based communications consistent with [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] and [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]].
- **Persistence & execution:** Registry Run Keys/Startup mechanisms and additional execution methods consistent with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]].
- **Collection features (capability-level):** Backdoor functionality associated with keylogging and screen capture is consistent with [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1113 - Screen Capture]] (capability mapping based on documented malware functionality attributed to this cluster).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1113 - Screen Capture]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1564.001 - Hide Artifacts: Hidden Files and Directories]]

## 7. Malware & Tools Used
- **Malware / Backdoors (reported):**
  - [[30_CIPHER/05_Malware/Sysget]] (aka [[30_CIPHER/05_Malware/HelloBridge]])
  - [[30_CIPHER/05_Malware/FormerFirstRat]]
  - [[30_CIPHER/05_Malware/NFlog]]
  - [[30_CIPHER/05_Malware/NewCT]]
  - [[30_CIPHER/05_Malware/PlugX]]
  - [[30_CIPHER/05_Malware/PoisonIvy]]
  - [[30_CIPHER/05_Malware/IsSpace]] (reported in related delivery activity)
  - [[30_CIPHER/05_Malware/TidePool]] (reported in related delivery activity)

## 8. Infrastructure Patterns
- Recurrent [[Phishing emails]] with [[Malicious attachments]] and [[Decoy documents]] aligned to Japanese-language contexts and lures.
- Centralized [[C2 over HTTP]] described in campaign reporting for Sysget/HelloBridge variants.
- Capability-level support for [[C2 over DNS]] documented in malware references associated with this cluster.
- Execution patterns consistent with [[DLL side-loading]] concepts (captured here as [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]) in some reporting.

## 9. Campaign History
- **2014-09:** Public reporting referenced in ATT&CK documents overlapping tooling and tradecraft between DragonOK and [[Moafee]].
- **2015-01 to 2015-03:** Vendor reporting describes multiple phishing attacks against Japanese organizations, including delivery of Sysget/HelloBridge variants and additional backdoors.
- **2016–2017:** Reporting describes evolved delivery methods (including exploit-assisted document delivery) and expanded target geography beyond Japan while maintaining Japan as a primary focus.
- **2017-10 onward (reported in Japanese reporting):** Additional Japan-focused activity observations linking PlugX-related tooling to DragonOK tradecraft.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Strengthen resilience against **spearphishing attachments** and **malicious file execution** (policy, filtering, and user protections aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]).
- Maintain robust patching and risk reduction for **client application exploitation** pathways consistent with [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]].
- Improve monitoring for anomalous outbound **HTTP/DNS beaconing** patterns consistent with [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] and [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]].
- Increase visibility into persistence signals associated with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and suspicious task scheduling consistent with [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]].
- Ensure endpoint telemetry and detection coverage for behaviors consistent with backdoor capabilities (e.g., [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1113 - Screen Capture]]) where applicable to your environment.

## 12. Analyst Notes
- DragonOK is often treated as a cluster defined by shared tooling and repeated Japan-focused targeting; vendor naming and clustering boundaries may differ.
- Several techniques in this note are **capability-based mappings** (derived from documented malware functionality used by DragonOK-attributed campaigns) rather than direct observations in every single incident.
- Relationship with [[Moafee]] should be tracked as “potentially linked” rather than as a confirmed organizational unity.

## 13. Further Reading / External Resources
- MITRE ATT&CK — DragonOK (G0017): https://attack.mitre.org/groups/G0017/
- Palo Alto Networks Unit 42 (2015-04-14) — New DragonOK backdoor malware deployed against Japanese targets: https://unit42.paloaltonetworks.com/unit-42-identifies-new-dragonok-backdoor-malware-deployed-against-japanese-targets/
- Palo Alto Networks Unit 42 (2017-01-05) — DragonOK updates toolset and targets multiple geographic regions: https://unit42.paloaltonetworks.com/unit42-dragonok-updates-toolset-targets-multiple-geographic-regions/
- LAC (2018-01-23) — PlugX activity linked to DragonOK (Japan-focused): https://www.lac.co.jp/english/report/2018/01/23_alert_01.html
- Malpedia — DragonOK actor page (summary & references): https://malpedia.caad.fkie.fraunhofer.de/actor/dragonok
- ETDA Threat Group Cards — DragonOK (alias mapping): https://apt.etda.or.th/cgi-bin/showcard.cgi?g=DragonOK

## 14. References
- MITRE ATT&CK. “DragonOK (G0017).” (Last Modified 2024-11-17). https://attack.mitre.org/groups/G0017/
- Palo Alto Networks Unit 42. “Unit 42 Identifies New DragonOK Backdoor Malware Deployed Against Japanese Targets.” (2015-04-14). https://unit42.paloaltonetworks.com/unit-42-identifies-new-dragonok-backdoor-malware-deployed-against-japanese-targets/
- Palo Alto Networks Unit 42. “DragonOK Updates Toolset and Targets Multiple Geographic Regions.” (2017-01-05). https://unit42.paloaltonetworks.com/unit42-dragonok-updates-toolset-targets-multiple-geographic-regions/
- LAC Co., Ltd. “How PlugX is related to the APT attack group ‘DragonOK’.” (2018-01-23). https://www.lac.co.jp/english/report/2018/01/23_alert_01.html
- Malpedia. “DragonOK (Threat Actor).” https://malpedia.caad.fkie.fraunhofer.de/actor/dragonok
- ETDA. “DragonOK — Threat Group Cards.” https://apt.etda.or.th/cgi-bin/showcard.cgi?g=DragonOK
