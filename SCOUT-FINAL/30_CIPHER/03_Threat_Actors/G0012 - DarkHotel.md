---
entity_type: threat_actor
actor_name: "DarkHotel"
common_name: "DarkHotel"
actor_id: "G0012"
actor_type: "Nation-state / cyber espionage (suspected)"
aliases: ["DUBNIUM", "Zigzag Hail", "SIG25", "APT-C-06", "Shadow Crane", "Fallout Team", "CTG-1948", "Tungsten Bridge", "Higaisa"]
country_of_origin: "South Korea (suspected)"
suspected_sponsors: ["South Korea (suspected)"]
attribution_confidence: "Medium"
first_seen: "2004-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage", "Information theft"]
objectives: ["Targeted intelligence collection against high-value individuals and organizations", "Credential theft and keylogging to enable access and collection", "Selective victim targeting and staged payload delivery", "Abuse of trusted network access points and signed software to increase success"]
victimology_summary: "DarkHotel (MITRE ATT&CK G0012) is a suspected South Korea-linked cyber espionage actor reported active since at least 2004, with operations historically associated with hotel and business-center internet networks used to target traveling executives. Public reporting also describes spearphishing activity and distribution via peer-to-peer/file-sharing channels, a focus on select victim categories, and use of signed/forged or stolen code-signing certificates and advanced delivery tradecraft to reduce suspicion and improve compromise rates."
target_sectors: ["Government", "Defense industrial base", "NGOs", "Technology", "Telecommunications", "Hospitality (as access vector)", "Business executives (high-value individuals)"]
target_regions: ["East Asia", "Global (travel-linked targeting)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Tapaoux]]", "[[30_CIPHER/05_Malware/Karba]]", "[[30_CIPHER/05_Malware/Nemim]]", "[[30_CIPHER/05_Malware/Pioneer]]"]
tools: []
infrastructure: ["[[Hotel Wi-Fi]]", "[[Hotel Login Portal]]", "[[Captive Portal]]", "[[Iframe Injection]]", "[[Strategic Web Compromise]]", "[[Watering Hole]]", "[[Spearphishing]]", "[[RAR Archive]]", "[[Windows Shortcut (LNK)]]", "[[Peer-to-Peer Distribution]]", "[[File Sharing Networks]]", "[[Dynamic DNS]]", "[[Stolen Code-Signing Certificates]]"]
ttps: ["[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]", "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]", "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]", "[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]", "[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]", "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]", "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]", "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]", "[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]", "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]", "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]", "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]", "[[20_Entities/07_TTPs/T1057 - Process Discovery]]", "[[20_Entities/07_TTPs/T1091 - Replication Through Removable Media]]", "[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]", "[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]", "[[20_Entities/07_TTPs/T1082 - System Information Discovery]]", "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]", "[[20_Entities/07_TTPs/T1124 - System Time Discovery]]", "[[20_Entities/07_TTPs/T1080 - Taint Shared Content]]", "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]", "[[20_Entities/07_TTPs/T1497 - Virtualization/Sandbox Evasion]]", "[[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks]]", "[[20_Entities/07_TTPs/T1497.002 - Virtualization/Sandbox Evasion: User Activity Based Checks]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0012): Darkhotel (Last modified 2024-01-08)","Kaspersky GReAT (2014-11): The Darkhotel APT — A Story of Unusual Hospitality (PDF)","Kaspersky Securelist (2015-08-10): Darkhotel’s attacks in 2015","Microsoft Security Blog (2016-06-09): Reverse-engineering DUBNIUM","Google Threat Analysis Group (2020-03-26): Identifying vulnerabilities and protecting you from phishing"]
tags: ["threat-actor", "apt", "cyber-espionage", "darkhotel", "dubnium", "zigzag-hail", "hotel-wifi", "mitre-g0012"]
---

# DarkHotel

## 1. BLUF / Executive Summary
DarkHotel (MITRE ATT&CK **G0012**) is a suspected South Korea-linked cyber espionage actor reported active since at least **2004**, historically known for compromising **hotel/business-center internet networks** to selectively target **traveling executives**. Public reporting also describes **spearphishing** and **peer-to-peer/file-sharing** distribution, the use of **code-signing certificate abuse**, and staged payload delivery that supports credential theft and long-term intelligence collection.

## 2. Attribution Notes
- **MITRE ATT&CK** describes DarkHotel as a *suspected South Korean* threat group and lists **DUBNIUM** and **Zigzag Hail** as associated group designations used by other trackers.
- Public reporting on attribution is **not uniform**; the most defensible posture is “suspected South Korea-linked” with **medium** confidence, anchored to convergent reporting rather than any single naming scheme.

## 3. Motivations & Objectives
- **Motivations:** Espionage and information theft.
- **Objectives:** Selective victim targeting (often travel-linked), credential/keylogging-based collection, and sustained access via staged implants and trusted-delivery abuse (e.g., signed/forged certificate use).

## 4. Targeting Profile
- **Primary victim profile (reported):** High-value individuals (e.g., executives) and organizations with strategic value.
- **Sectors (reported):** Government, defense industrial base, NGOs, tech/telecom; hospitality is prominently used as an **access vector** rather than a primary end-target.
- **Geography (reported):** Primarily East Asia with global reach driven by travel-linked targeting.

## 5. Tradecraft Overview
- **Hotel-network compromise & selective delivery:** Abuse of [[Hotel Login Portal]] / [[Captive Portal]] style infrastructure with [[Iframe Injection]] consistent with targeted [[Strategic Web Compromise]] / [[Watering Hole]] behavior.
- **Spearphishing workflows:** Use of attachment-based lures consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and user execution patterns consistent with [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]].
- **Credential & input capture:** Keylogging consistent with [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] to support intelligence collection.
- **Evasion & trust subversion:** Obfuscation/decryption behavior consistent with [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]] and [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]; certificate abuse consistent with [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]].
- **Discovery & staging:** Host/network discovery consistent with [[20_Entities/07_TTPs/T1082 - System Information Discovery]] and [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]], plus staged component delivery consistent with [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].
- **Anti-analysis:** Behaviors consistent with [[20_Entities/07_TTPs/T1497 - Virtualization/Sandbox Evasion]] (including [[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks]] and [[20_Entities/07_TTPs/T1497.002 - Virtualization/Sandbox Evasion: User Activity Based Checks]]).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1124 - System Time Discovery]]
- [[20_Entities/07_TTPs/T1497 - Virtualization/Sandbox Evasion]]
- [[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks]]
- [[20_Entities/07_TTPs/T1497.002 - Virtualization/Sandbox Evasion: User Activity Based Checks]]
- [[20_Entities/07_TTPs/T1091 - Replication Through Removable Media]]
- [[20_Entities/07_TTPs/T1080 - Taint Shared Content]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]

## 7. Malware & Tools Used
- **Reported malware families / detections:**
  - [[30_CIPHER/05_Malware/Tapaoux]]
  - [[30_CIPHER/05_Malware/Karba]]
  - [[30_CIPHER/05_Malware/Nemim]]
  - [[30_CIPHER/05_Malware/Pioneer]]
- **Tools:** No specific operator tooling is listed here beyond what is defensibly described in the cited public sources.

## 8. Infrastructure Patterns
- Compromise of hospitality network touchpoints (e.g., [[Hotel Login Portal]] / [[Captive Portal]]) with [[Iframe Injection]] to drive selective delivery.
- Recurrent use of travel-linked “strategic web compromise” behavior consistent with [[Strategic Web Compromise]] / [[Watering Hole]] patterns.
- Use of [[RAR Archive]] / [[Windows Shortcut (LNK)]] style artifacts in delivery chains described in public reporting (high-level).
- Reliance on flexible infrastructure such as [[Dynamic DNS]] and web-server based staging, as described in public reporting.
- Abuse of trust mechanisms through [[Stolen Code-Signing Certificates]] to increase user execution success and reduce suspicion.

## 9. Campaign History
- **2007–2014 (reported):** Public reporting describes DarkHotel-associated samples circulating as early as 2007 and long-running activity tied to hotel/business-center networks, with selective targeting of high-value guests.
- **2014-11 (reported):** Kaspersky publicly disclosed “DarkHotel” as an APT characterized by hotel network compromise, selective delivery, keylogging/stealing components, and certificate abuse.
- **2015-08 (reported):** Kaspersky reported continued activity including spearphishing and multi-stage delivery chains, with evolution in delivery and infrastructure management.
- **2016 (reported):** Microsoft published technical analysis under the tracker name “DUBNIUM,” describing exploitation and staged payload behaviors aligned with DarkHotel tradecraft.
- **2019–2020 (reported):** Google TAG described targeted exploitation of multiple zero-days in 2019; public reporting noted Kaspersky’s linkage of that activity to DarkHotel (actor identity not confirmed by Google).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize hardening and monitoring for travel-linked exposure pathways (guest Wi-Fi, captive portals, and hotel-business-center network usage) where feasible, especially for executives and diplomats.
- Treat unexpected “software update” prompts delivered via untrusted networks as high-risk and ensure strong controls around software installation trust and code-signing validation.
- Increase detection coverage for certificate abuse patterns consistent with [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]] and for keylogging/credential theft behaviors consistent with [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]].
- Use behavior-based detection and threat hunting for multi-stage download/execution sequences consistent with [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]] combined with discovery activity (e.g., [[20_Entities/07_TTPs/T1082 - System Information Discovery]], [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]).
- Incorporate anti-analysis behaviors into analytic logic where appropriate (e.g., sandbox-evasion patterns consistent with [[20_Entities/07_TTPs/T1497 - Virtualization/Sandbox Evasion]]), recognizing these are common but can add weight when correlated with victimology.

## 12. Analyst Notes
- **Naming risk:** DarkHotel is commonly cross-mapped to **DUBNIUM** and other vendor trackers; do not assume full equivalence across all alias sets without overlap validation (malware lineage + victimology + tradecraft).
- **Attribution posture:** “Suspected South Korea-linked” is the most defensible public posture; treat stronger claims as hypotheses unless corroborated by primary-source reporting.
- **Indicator discipline:** Infrastructure and file hashes in older reporting are frequently stale; analytic emphasis should remain on behavioral patterns and software lineages rather than IOC-only matching.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Darkhotel (G0012)  
  https://attack.mitre.org/groups/G0012/
- Kaspersky (PDF) — The Darkhotel APT: A Story of Unusual Hospitality (2014-11)  
  https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf
- Kaspersky Securelist — Darkhotel’s attacks in 2015 (2015-08-10)  
  https://securelist.com/darkhotels-attacks-in-2015/71713/
- Microsoft Security Blog — Reverse-engineering DUBNIUM (2016-06-09)  
  https://www.microsoft.com/security/blog/2016/06/09/reverse-engineering-dubnium-2/
- Google Threat Analysis Group — Identifying vulnerabilities and protecting you from phishing (2020-03-26)  
  https://blog.google/threat-analysis-group/identifying-vulnerabilities-and-protecting-you-phishing/

## 14. References
- MITRE ATT&CK. “Darkhotel (G0012).” (Last modified 2024-01-08)  
  https://attack.mitre.org/groups/G0012/
- Kaspersky GReAT. “The Darkhotel APT: A Story of Unusual Hospitality.” (2014-11)  
  https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf
- Kaspersky Securelist. “Darkhotel’s attacks in 2015.” (2015-08-10)  
  https://securelist.com/darkhotels-attacks-in-2015/71713/
- Microsoft Security Blog. “Reverse-engineering DUBNIUM.” (2016-06-09)  
  https://www.microsoft.com/security/blog/2016/06/09/reverse-engineering-dubnium-2/
- Google Threat Analysis Group. “Identifying vulnerabilities and protecting you from phishing.” (2020-03-26)  
  https://blog.google/threat-analysis-group/identifying-vulnerabilities-and-protecting-you-phishing/
