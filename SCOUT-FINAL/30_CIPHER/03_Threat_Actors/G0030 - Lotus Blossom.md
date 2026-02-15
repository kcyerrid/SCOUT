---
entity_type: threat_actor
actor_name: "Lotus Blossom"
common_name: "Lotus Blossom"
actor_id: "G0030"
actor_type: "Espionage-focused intrusion set; likely state-sponsored per public reporting"
aliases: ["DRAGONFISH","Spring Dragon","RADIUM","Raspberry Typhoon","Bilbug","Thrip"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2009-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Obtain sensitive government/military and strategic sector information in Asia","Maintain long-term access using custom backdoors and persistence mechanisms","Collect and exfiltrate selected data, including via non-traditional C2 channels (reported)"]
victimology_summary: "Lotus Blossom (MITRE ATT&CK G0030) is a long-standing threat group largely targeting entities in Asia since at least 2009, including government-related targets and digital certificate issuers. Public reporting has described sustained espionage activity against government and military organizations in Southeast Asia using spearphishing and the custom backdoor [[30_CIPHER/05_Malware/Elise]]. More recent reporting links Lotus Blossom to multi-campaign activity across government and commercial sectors (e.g., manufacturing, telecommunications, media) leveraging [[30_CIPHER/05_Malware/Sagerunex]] variants and additional tooling; separate reporting under the \"Billbug\" label describes compromise of a digital certificate authority and use of [[30_CIPHER/05_Malware/Hannotog]] and [[30_CIPHER/05_Malware/Sagerunex]]."
target_sectors: ["Government","Military/Defense","Manufacturing (reported)","Telecommunications (reported)","Media (reported)","Digital certificate issuers / Certificate authorities (reported)"]
target_regions: ["Asia (primary)","Hong Kong (reported)","Taiwan (reported)","Vietnam (reported)","Philippines (reported)","Indonesia (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Elise]]","[[30_CIPHER/05_Malware/Emissary]]","[[30_CIPHER/05_Malware/Sagerunex]]","[[30_CIPHER/05_Malware/Hannotog]]"]
tools: ["[[30_CIPHER/05_Malware/AdFind]]","[[30_CIPHER/05_Malware/certutil]]","[[30_CIPHER/05_Malware/Impacket]]","[[30_CIPHER/05_Malware/NBTscan]]","[[30_CIPHER/05_Malware/Ping]]","[[30_CIPHER/05_Malware/WinRAR]]","[[30_CIPHER/05_Malware/HTran]]","[[30_CIPHER/05_Malware/Venom Proxy]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Decoy Documents]]","[[Registry-based installation]]","[[Windows Service persistence]]","[[Web Service C2]]","[[Proxy chaining]]","[[Non-standard port C2]]","[[Credential/Directory enumeration]]","[[Compromised certificate authority]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]","[[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]","[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]","[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]","[[20_Entities/07_TTPs/T1560.003 - Archive Collected Data: Archive via Custom Method]]","[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]","[[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]","[[20_Entities/07_TTPs/T1482 - Domain Trust Discovery]]","[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]","[[20_Entities/07_TTPs/T1112 - Modify Registry]]","[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]","[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]","[[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]","[[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]","[[20_Entities/07_TTPs/T1012 - Query Registry]]","[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]","[[20_Entities/07_TTPs/T1539 - Steal Web Session Cookie]]","[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]","[[20_Entities/07_TTPs/T1016.001 - System Network Configuration Discovery: Internet Connection Discovery]]","[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]","[[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]","[[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]","[[20_Entities/07_TTPs/T1571 - Non-Standard Port]]","[[20_Entities/07_TTPs/T1489 - Service Stop]]","[[20_Entities/07_TTPs/T1573.002 - Encrypted Channel: Asymmetric Cryptography]]","[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]","[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]","[[20_Entities/07_TTPs/T1480 - Execution Guardrails]]","[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1106 - Native API]]","[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]","[[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Lotus Blossom (G0030) (Last Modified 2025-04-23): https://attack.mitre.org/groups/G0030/","Palo Alto Networks Unit 42 — Operation Lotus Blossom: A New Nation-State Cyberthreat? (2015-06-16): https://unit42.paloaltonetworks.com/operation-lotus-blossom/","Cisco Talos — Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools (2025-02-27): https://blog.talosintelligence.com/lotus-blossom-espionage-group/","Broadcom/Symantec — Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries (2022-11-15): https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority","MITRE ATT&CK — Sagerunex (S1210) (Last Modified 2025-03-16): https://attack.mitre.org/software/S1210/"]
tags: ["threat-actor","lotus-blossom","g0030","espionage","asia","sagerunex","elise","hannotog","bilbug","thrip","spring-dragon"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Lotus Blossom

## 1. BLUF / Executive Summary
Lotus Blossom (MITRE ATT&CK **G0030**) is a long-running espionage-oriented intrusion set primarily reported targeting **entities across Asia** since at least **2009**, with sustained emphasis on **government/military** and other strategic targets (including **digital certificate issuers**). Reporting describes spearphishing-led operations featuring the custom backdoor [[30_CIPHER/05_Malware/Elise]] and later activity using [[30_CIPHER/05_Malware/Sagerunex]] variants, including use of **legitimate web services** as command-and-control channels and long-term persistence mechanisms. Public reporting continues into **2025**, indicating ongoing operational activity.

## 2. Attribution Notes
- MITRE ATT&CK tracks Lotus Blossom as **G0030** and lists associated names including **DRAGONFISH, Spring Dragon, RADIUM/Raspberry Typhoon, Bilbug,** and **Thrip**.
- Multiple public sources characterize the activity as **state-sponsored or likely state-sponsored**, but do not provide a universally accepted, high-confidence country attribution in the primary references used here.
- Vendor naming can differ (e.g., “Bilbug”/“Thrip” clustering); this note follows the MITRE grouping and uses conservative language where mappings are label-based.

## 3. Motivations & Objectives
- **Motivation:** Strategic intelligence collection (espionage).
- **Objectives (observed/reported):**
  - Compromise targeted organizations to obtain sensitive government, defense, and strategic-sector information.
  - Maintain access over time using custom backdoors (e.g., [[30_CIPHER/05_Malware/Elise]], [[30_CIPHER/05_Malware/Sagerunex]], [[30_CIPHER/05_Malware/Hannotog]]) and persistence mechanisms (registry/service-based).
  - Stage, compress, and exfiltrate collected data, including via non-traditional or proxy-enabled C2 routes.

## 4. Targeting Profile
- **Primary geography:** Asia-focused targeting (reported).
- **Notable reported locations/campaign coverage:** Hong Kong, Taiwan, Vietnam, the Philippines, Indonesia (reported in Operation Lotus Blossom).
- **Sectors (reported):** Government and military/defense; additional reporting includes manufacturing, telecommunications, media; and digital certificate issuers/certificate authorities.

## 5. Tradecraft Overview
- **Initial access:** Reported reliance on spearphishing attachments aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]], often paired with decoy content to reduce suspicion during execution (Operation Lotus Blossom reporting).
- **Custom backdoors and evolution:** Early reporting highlights [[30_CIPHER/05_Malware/Elise]] as a custom Trojan used to establish footholds; later reporting emphasizes [[30_CIPHER/05_Malware/Sagerunex]] variants used in multiple campaigns.
- **Persistence & execution patterns:** Public reporting and ATT&CK mappings include registry-based installation and Windows service persistence (e.g., [[20_Entities/07_TTPs/T1112 - Modify Registry]] and [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]).
- **Data handling:** Local staging and archiving using utilities and custom methods (e.g., [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]], [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]], [[20_Entities/07_TTPs/T1560.003 - Archive Collected Data: Archive via Custom Method]]).
- **C2 and routing:** Use of proxy tooling and, in later reporting, leveraging legitimate web services as C2 tunnels (aligned to [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]], [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]], and [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]] / [[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]).
- **Discovery:** Host and network discovery, directory enumeration, and environment validation behaviors are represented in ATT&CK mappings (e.g., [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]], [[20_Entities/07_TTPs/T1046 - Network Service Discovery]], [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]
- [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1560.003 - Archive Collected Data: Archive via Custom Method]]
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
- [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]
- [[20_Entities/07_TTPs/T1482 - Domain Trust Discovery]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1112 - Modify Registry]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]]
- [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]]
- [[20_Entities/07_TTPs/T1012 - Query Registry]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1539 - Steal Web Session Cookie]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1016.001 - System Network Configuration Discovery: Internet Connection Discovery]]
- [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
- [[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]
- [[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]
- [[20_Entities/07_TTPs/T1571 - Non-Standard Port]]
- [[20_Entities/07_TTPs/T1489 - Service Stop]]
- [[20_Entities/07_TTPs/T1573.002 - Encrypted Channel: Asymmetric Cryptography]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1480 - Execution Guardrails]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1106 - Native API]]
- [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]
- [[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]]

## 7. Malware & Tools Used
**Primary malware families / implants (per ATT&CK and vendor reporting)**
- [[30_CIPHER/05_Malware/Elise]] — custom Trojan/backdoor highlighted in early “Operation Lotus Blossom” reporting and tracked in ATT&CK software associations for the group.
- [[30_CIPHER/05_Malware/Emissary]] — associated Lotus Blossom malware family tracked by ATT&CK.
- [[30_CIPHER/05_Malware/Sagerunex]] — malware family described by ATT&CK as exclusively associated with Lotus Blossom operations; reporting highlights multiple variants and non-traditional C2 mechanisms.
- [[30_CIPHER/05_Malware/Hannotog]] — backdoor associated with Lotus Blossom operations in public reporting (notably under “Billbug” activity).

**Operational tooling (per ATT&CK group software listings and vendor reporting)**
- [[30_CIPHER/05_Malware/AdFind]] — used for Active Directory queries in victim environments (reported via ATT&CK sourcing).
- [[30_CIPHER/05_Malware/certutil]] — used during operations; ATT&CK associates it with multiple operational purposes for the group.
- [[30_CIPHER/05_Malware/Impacket]] — used during operations (reported via ATT&CK sourcing).
- [[30_CIPHER/05_Malware/NBTscan]] — used during operations (reported via ATT&CK sourcing).
- [[30_CIPHER/05_Malware/Ping]] — used to verify connectivity / identify remote systems (reported via ATT&CK sourcing).
- [[30_CIPHER/05_Malware/WinRAR]] — used for compressing data prior to staging/exfiltration (reported via ATT&CK sourcing).
- [[30_CIPHER/05_Malware/HTran]] — referenced as a publicly available proxy tool used for traffic proxying in victim environments (reported via ATT&CK sourcing).
- [[30_CIPHER/05_Malware/Venom Proxy]] — referenced as a publicly available proxy tool used for proxying traffic out of victim environments (reported via ATT&CK sourcing).

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] with [[Decoy Documents]] used to entice execution and mask malicious activity during initial compromise (reported).
- [[Registry-based installation]] and [[Windows Service persistence]] patterns to maintain footholds over time (reported/ATT&CK-mapped).
- [[Web Service C2]] leveraging legitimate third-party platforms for command and control (reported in 2025 research; ATT&CK-mapped via Sagerunex associations).
- [[Proxy chaining]] including internal and multi-hop proxy usage, consistent with reported use of publicly available proxy tooling.
- [[Non-standard port C2]] and defensive impairment behaviors (reported in Hannotog-related associations and ATT&CK mappings).
- [[Compromised certificate authority]] targeting, consistent with reporting describing intrusion into a digital certificate issuer environment.

## 9. Campaign History
- **2009 (at least):** MITRE ATT&CK describes Lotus Blossom as active since at least 2009, primarily targeting entities across Asia.
- **2012–2015 (reported):** Unit 42 described “Operation Lotus Blossom,” linking dozens of attacks across Hong Kong, Taiwan, Vietnam, the Philippines, and Indonesia, primarily against government and military targets, using spearphishing and [[30_CIPHER/05_Malware/Elise]].
- **2016 (at least, reported):** ATT&CK and vendor reporting associate Lotus Blossom as the exclusive user of [[30_CIPHER/05_Malware/Sagerunex]] variants since at least 2016.
- **2022-11-15 (reported):** Reporting under the “Billbug” label described compromise of an Asian digital certificate authority and government/defense agencies, with use of [[30_CIPHER/05_Malware/Hannotog]] and [[30_CIPHER/05_Malware/Sagerunex]].
- **2025-02-27 (reported):** Cisco Talos reported ongoing multi-campaign activity across government and multiple industries, highlighting new and evolving [[30_CIPHER/05_Malware/Sagerunex]] variants and the use of legitimate web services as C2 tunnels.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Strengthen detection and user-resilience against targeted attachment-based phishing aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]], with emphasis on high-risk roles and regionally relevant lure themes.
- Monitor and constrain persistence patterns aligned to [[20_Entities/07_TTPs/T1112 - Modify Registry]] and [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]], especially when correlated with suspicious tool execution or new/unknown binaries.
- Improve visibility into discovery and lateral movement behaviors aligned to [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]], [[20_Entities/07_TTPs/T1046 - Network Service Discovery]], and [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]].
- Treat abnormal proxying and egress routing aligned to [[20_Entities/07_TTPs/T1090.001 - Proxy: Internal Proxy]] and [[20_Entities/07_TTPs/T1090.003 - Proxy: Multi-hop Proxy]] as higher-signal when paired with staging/archiving activity (e.g., [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]).
- Establish governance and monitoring for enterprise use of legitimate web services to reduce abuse opportunities aligned to [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]] and [[20_Entities/07_TTPs/T1102.003 - Web Service: One-Way Communication]].
- For organizations that issue or manage digital certificates, increase monitoring and access controls around certificate infrastructure given reporting of certificate authority targeting.

## 12. Analyst Notes
- Lotus Blossom is a multi-alias cluster with overlapping vendor naming (e.g., Bilbug/Thrip). This note follows MITRE ATT&CK’s consolidation (G0030) and keeps attribution conservative where country sponsorship is not directly asserted by primary references.
- The group’s tooling and tradecraft appear to have evolved from earlier Elise-centric operations to modern Sagerunex variants and broader post-compromise tooling, while retaining consistent themes: persistence, staging/archiving, and stealthy C2.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Lotus Blossom (G0030): https://attack.mitre.org/groups/G0030/
- MITRE ATT&CK — Sagerunex (S1210): https://attack.mitre.org/software/S1210/
- Palo Alto Networks Unit 42 — Operation Lotus Blossom: https://unit42.paloaltonetworks.com/operation-lotus-blossom/
- Cisco Talos — Lotus Blossom espionage group targets multiple industries… (2025-02-27): https://blog.talosintelligence.com/lotus-blossom-espionage-group/
- Broadcom/Symantec — Billbug targets cert authority and government agencies (2022-11-15): https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority

## 14. References
1. MITRE ATT&CK. “Lotus Blossom (G0030).” (Last Modified 2025-04-23). https://attack.mitre.org/groups/G0030/
2. Palo Alto Networks Unit 42. “Operation Lotus Blossom: A New Nation-State Cyberthreat?” (2015-06-16). https://unit42.paloaltonetworks.com/operation-lotus-blossom/
3. Cisco Talos. “Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools.” (2025-02-27). https://blog.talosintelligence.com/lotus-blossom-espionage-group/
4. Broadcom/Symantec Threat Hunter Team. “Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries.” (2022-11-15). https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority
5. MITRE ATT&CK. “Sagerunex (S1210).” (Last Modified 2025-03-16). https://attack.mitre.org/software/S1210/
---
