---
entity_type: threat_actor
actor_name: "PROMETHIUM"
common_name: "PROMETHIUM"
actor_id: "G0056"
actor_type: "Espionage-focused activity group (Microsoft taxonomy) associated with StrongPity operations (reported)"
aliases: ["StrongPity"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "High"
first_seen: "2012-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Targeted surveillance and information theft from individuals (reported)","Initial access via trojanized legitimate software installers and watering-hole delivery (reported)","Use of malicious documents/links leveraging client-side exploitation to launch first-stage malware (reported)","Collection and exfiltration of user files and metadata (reported)","Mobile data collection (e.g., notifications, call logs, contacts, SMS) in Android campaigns attributed to StrongPity/PROMETHIUM (reported)"]
victimology_summary: "PROMETHIUM (MITRE ATT&CK G0056) is an espionage-focused activity group reported active since at least 2012. Public reporting describes global operations with a heavy emphasis on Turkish targets, and notes overlap/similarity with NEODYMIUM based on victim and campaign characteristics. PROMETHIUM is closely associated with the StrongPity malware/toolset, including campaigns leveraging trojanized installers, watering-hole delivery, and (in at least one documented 2016 window) use of an Adobe Flash zero-day (CVE-2016-4117) to launch the first-stage malware Truvasys."
target_sectors: ["Individuals","Encryption software users (reported)","Mobile users (targeted; reported)"]
target_regions: ["Turkey","Europe","Global"]
related_groups: ["NEODYMIUM"]
malware: ["[[30_CIPHER/05_Malware/StrongPity]]","[[30_CIPHER/05_Malware/Truvasys]]"]
tools: []
infrastructure: ["[[Watering hole]]","[[Trojanized installers]]","[[Self-signed certificates]]","[[HTTPS C2]]","[[Port knocking]]","[[Instant messenger lure links]]","[[In-path interception]]","[[Spoofed download sites]]"]
ttps: ["[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]","[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]","[[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]","[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1205.001 - Traffic Signaling: Port Knocking]]","[[20_Entities/07_TTPs/T1078.003 - Valid Accounts: Local Accounts]]","[[20_Entities/07_TTPs/T1587.002 - Develop Capabilities: Code Signing Certificates]]","[[20_Entities/07_TTPs/T1587.003 - Develop Capabilities: Digital Certificates]]","[[20_Entities/07_TTPs/T1517 - Access Notifications]]","[[20_Entities/07_TTPs/T1437.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1521.001 - Encrypted Channel: Symmetric Cryptography]]","[[20_Entities/07_TTPs/T1624.001 - Event Triggered Execution: Broadcast Receivers]]","[[20_Entities/07_TTPs/T1646 - Exfiltration Over C2 Channel]]","[[20_Entities/07_TTPs/T1430 - Location Tracking]]","[[20_Entities/07_TTPs/T1636.002 - Protected User Data: Call Log]]","[[20_Entities/07_TTPs/T1636.003 - Protected User Data: Contact List]]","[[20_Entities/07_TTPs/T1636.004 - Protected User Data: SMS Messages]]"]
notable_claims: ["Microsoft reported PROMETHIUM and NEODYMIUM ran similarly timed campaigns in early May 2016 using the same Adobe Flash zero-day (CVE-2016-4117), but with different delivery tradecraft (reported)","PROMETHIUM/StrongPity campaigns have repeatedly used trojanized legitimate installers and watering-hole style delivery to reach targets (reported)","MITRE tracks an Android-focused PROMETHIUM campaign (C0033) with activity spanning May 2016 through January 2023 (reported)"]
intel_sources: ["MITRE ATT&CK — PROMETHIUM (G0056) (Last Modified 2024-04-19): https://attack.mitre.org/groups/G0056/","MITRE ATT&CK — StrongPity (S0491): https://attack.mitre.org/software/S0491/","MITRE ATT&CK — Truvasys (S0178): https://attack.mitre.org/software/S0178/","MITRE ATT&CK — Campaign C0033 (PROMETHIUM mobile campaign): https://attack.mitre.org/campaigns/C0033/","Microsoft Security Blog — Twin zero-day attacks: PROMETHIUM and NEODYMIUM target individuals in Europe (2016-12-14): https://www.microsoft.com/en-us/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/","Microsoft — Security Intelligence Report Volume 21 (PDF) (2016-12-14): https://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_Parallel_Zero-day_Attacks_English.pdf","Cisco Talos — PROMETHIUM extends global reach with StrongPity3 APT (2020-06-29): https://blog.talosintelligence.com/promethium-extends-with-strongpity3/","Bitdefender — StrongPity APT whitepaper (PDF) (2020-06): https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf","Kaspersky Securelist — StrongPity waterhole attacks targeting Italian and Belgian encryption users (2016-10-03): https://securelist.com/on-the-strongpity-waterhole-attacks-targeting-italian-and-belgian-encryption-users/76147/","Trend Micro — StrongPity APT Group Deploys Android Malware for the First Time (2021-07-21): https://www.trendmicro.com/en_gb/research/21/g/strongpity-apt-group-deploys-android-malware-for-the-first-time.html","ESET — StrongPity espionage campaign targeting Android users (2023-01-10): https://www.welivesecurity.com/2023/01/10/strongpity-espionage-campaign-targeting-android-users/"]
tags: ["threat-actor","promethium","g0056","strongpity","espionage","watering-hole","trojanized-installers","turkey-targeting"]
created: "2025-12-28"
last_modified: "2025-12-28"
---

# PROMETHIUM

## 1. BLUF / Executive Summary
PROMETHIUM (**G0056**) is an espionage-focused activity group reported active since at least **2012**, with operations described as global but with a **heavy emphasis on Turkish targets**. The cluster is closely associated with the StrongPity toolset (tracked in ATT&CK as [[30_CIPHER/05_Malware/StrongPity]]) and is publicly described in connection with trojanized installers, watering-hole delivery, and targeted surveillance of individuals. PROMETHIUM is also reported to show similarity to NEODYMIUM based on overlapping campaign characteristics.

## 2. Attribution Notes
- **Primary anchor:** MITRE ATT&CK tracks PROMETHIUM as **G0056** and lists **StrongPity** as an associated group name and software family.
- **Taxonomy note:** “PROMETHIUM” is a Microsoft activity-group label; “StrongPity” has been used in public reporting to describe both the actor and its malware/tooling lineage.
- **Sponsor attribution:** Public sources cited here do **not** provide a defensible, definitive state sponsor; this note leaves sponsor fields empty.

## 3. Motivations & Objectives
- **Motivation:** intelligence collection / surveillance (espionage).
- **Operational objectives (reported):**
  - Compromise targeted individuals and maintain access long enough to collect files and communications metadata.
  - Blend into normal user behavior by masquerading as legitimate utilities and software installers.
  - Use encrypted web communications and trust-abuse patterns (certificates/signing) to reduce visibility and increase victim trust.

## 4. Targeting Profile
- **Regions:** Turkey (prominent in reporting), Europe, and broader global victimology in later reporting.
- **Victim types:** individuals (including users seeking privacy/encryption tools in documented waterhole cases), and mobile users in Android-focused StrongPity campaigns.

## 5. Tradecraft Overview
- **Watering-hole and trojanized installer delivery:** PROMETHIUM/StrongPity reporting repeatedly emphasizes compromised download paths and trojanized installers (often bundling legitimate software with malware).
- **Masquerading:** malware and persistence artifacts are designed to look like legitimate tasks/services and legitimate software locations/names.
- **Persistence patterns (Windows):** registry run key usage and Windows service creation/modification appear repeatedly in public reporting.
- **Trust subversion:** use of self-signed certificates for both code-signing and HTTPS C2 has been documented in public sources.
- **Signaling/OPSEC:** port-knocking style signaling is documented in public reporting to gate C2 acceptance in some scenarios.
- **Mobile expansion:** MITRE tracks a PROMETHIUM mobile campaign (C0033) and multiple vendors describe Android StrongPity activity with modular data collection and exfiltration over HTTPS.

## 6. MITRE ATT&CK Mapping
**Initial Access / Execution**
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]

**Persistence**
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]

**Defense Evasion / Masquerading**
- [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]

**Credential / Access Enablement**
- [[20_Entities/07_TTPs/T1078.003 - Valid Accounts: Local Accounts]]

**Trust / Certificates**
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- [[20_Entities/07_TTPs/T1587.002 - Develop Capabilities: Code Signing Certificates]]
- [[20_Entities/07_TTPs/T1587.003 - Develop Capabilities: Digital Certificates]]

**Network / Signaling**
- [[20_Entities/07_TTPs/T1205.001 - Traffic Signaling: Port Knocking]]

**Mobile (C0033 / StrongPity Android activity)**
- [[20_Entities/07_TTPs/T1437.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1521.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1624.001 - Event Triggered Execution: Broadcast Receivers]]
- [[20_Entities/07_TTPs/T1646 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1517 - Access Notifications]]
- [[20_Entities/07_TTPs/T1636.002 - Protected User Data: Call Log]]
- [[20_Entities/07_TTPs/T1636.003 - Protected User Data: Contact List]]
- [[20_Entities/07_TTPs/T1636.004 - Protected User Data: SMS Messages]]
- [[20_Entities/07_TTPs/T1430 - Location Tracking]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/StrongPity]] — primary malware/toolset associated with PROMETHIUM in multiple public reports and MITRE ATT&CK.
- [[30_CIPHER/05_Malware/Truvasys]] — first-stage malware described by Microsoft as used by PROMETHIUM and masquerading as common utilities.

## 8. Infrastructure Patterns
- [[Watering hole]] delivery and compromised download paths, including cases tied to encryption/utility software users.
- [[Trojanized installers]] that install legitimate software alongside malicious components to reduce suspicion.
- [[Self-signed certificates]] used to support both signing and encrypted communications; commonly paired with [[HTTPS C2]].
- [[Port knocking]] or similar gating/signal patterns to restrict inbound C2 acceptance.
- [[Instant messenger lure links]] reported as part of PROMETHIUM delivery workflows in 2016 reporting.
- [[In-path interception]] and/or redirected download traffic is discussed as a plausible mechanism in some reporting on later StrongPity waves.

## 9. Campaign History
- **2012-01-01 (at least):** PROMETHIUM reported active since at least 2012.
- **2016-05 (reported):** Microsoft describes PROMETHIUM and NEODYMIUM using the Adobe Flash zero-day **CVE-2016-4117** in similarly timed campaigns in Europe/Turkey; PROMETHIUM’s chain is described as link-delivered malicious documents that launch [[30_CIPHER/05_Malware/Truvasys]].
- **2016-10-03:** Kaspersky documents StrongPity waterhole activity targeting Italian and Belgian encryption users (StrongPity is tracked by MITRE as associated with PROMETHIUM).
- **2020-06-29:** Cisco Talos reports StrongPity3 and expanding victimology with continued emphasis on trojanized legitimate installers and self-signed certificate usage.
- **2021-07-21 to 2023-01-10 (reported):** Trend Micro and ESET publish research on Android StrongPity activity; MITRE tracks a PROMETHIUM mobile campaign (C0033) with activity spanning **May 2016** to **January 2023**.

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Emphasize controls that reduce watering-hole exposure aligned to [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] (web integrity monitoring for owned domains; browser isolation/hardening posture for high-risk users).
- Treat unsigned/unexpected installer execution and unusual “installer + legit app” bundling as high-signal aligned to [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]] and masquerading techniques.
- Strengthen detection for persistence patterns aligned to [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]].
- Monitor for anomalous certificate/signing behavior aligned to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]] and suspicious use of self-signed certificates.
- For mobile fleets, prioritize visibility for HTTPS-based exfiltration and protected-user-data access aligned to [[20_Entities/07_TTPs/T1646 - Exfiltration Over C2 Channel]] and [[20_Entities/07_TTPs/T1636.004 - Protected User Data: SMS Messages]] (plus related protected-data techniques listed above).

## 12. Analyst Notes
- PROMETHIUM vs. StrongPity naming varies by vendor; using **G0056** as the stable identifier helps normalize reporting.
- The actor’s tradecraft blends social/behavioral targeting (trojanized installers, masquerading) with selective technical mechanisms (certificates, signaling), which can yield false positives if analysts focus on any single artifact in isolation.
- Similarity claims with NEODYMIUM should be treated as “overlap in campaign characteristics,” not a confirmed alias, consistent with ATT&CK language.

## 13. Further Reading / External Resources
- MITRE ATT&CK — PROMETHIUM (G0056): https://attack.mitre.org/groups/G0056/
- Microsoft — Twin zero-day attacks: PROMETHIUM and NEODYMIUM (2016-12-14): https://www.microsoft.com/en-us/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/
- Cisco Talos — PROMETHIUM extends global reach with StrongPity3 (2020-06-29): https://blog.talosintelligence.com/promethium-extends-with-strongpity3/
- Kaspersky — StrongPity waterhole targeting encryption users (2016-10-03): https://securelist.com/on-the-strongpity-waterhole-attacks-targeting-italian-and-belgian-encryption-users/76147/
- ESET — StrongPity espionage campaign targeting Android users (2023-01-10): https://www.welivesecurity.com/2023/01/10/strongpity-espionage-campaign-targeting-android-users/

## 14. References
1. MITRE ATT&CK. “PROMETHIUM (G0056).” Last Modified 2024-04-19. https://attack.mitre.org/groups/G0056/
2. MITRE ATT&CK. “StrongPity (S0491).” https://attack.mitre.org/software/S0491/
3. MITRE ATT&CK. “Truvasys (S0178).” https://attack.mitre.org/software/S0178/
4. MITRE ATT&CK. “Campaign C0033.” https://attack.mitre.org/campaigns/C0033/
5. Microsoft Defender Security Research Team. “Twin zero-day attacks: PROMETHIUM and NEODYMIUM target individuals in Europe.” 2016-12-14. https://www.microsoft.com/en-us/security/blog/2016/12/14/twin-zero-day-attacks-promethium-and-neodymium-target-individuals-in-europe/
6. Microsoft. “Microsoft Security Intelligence Report Volume 21: Parallel Zero-day Attacks (PDF).” 2016-12-14. https://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_Parallel_Zero-day_Attacks_English.pdf
7. Cisco Talos. “PROMETHIUM extends global reach with StrongPity3 APT.” 2020-06-29. https://blog.talosintelligence.com/promethium-extends-with-strongpity3/
8. Bitdefender. “StrongPity APT whitepaper (PDF).” 2020-06. https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf
9. Kaspersky Securelist. “On the StrongPity Waterhole Attacks Targeting Italian and Belgian Encryption Users.” 2016-10-03. https://securelist.com/on-the-strongpity-waterhole-attacks-targeting-italian-and-belgian-encryption-users/76147/
10. Trend Micro. “StrongPity APT Group Deploys Android Malware for the First Time.” 2021-07-21. https://www.trendmicro.com/en_gb/research/21/g/strongpity-apt-group-deploys-android-malware-for-the-first-time.html
11. ESET. “StrongPity espionage campaign targeting Android users.” 2023-01-10. https://www.welivesecurity.com/2023/01/10/strongpity-espionage-campaign-targeting-android-users/
