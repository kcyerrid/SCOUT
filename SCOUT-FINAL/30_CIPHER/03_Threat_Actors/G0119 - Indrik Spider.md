---
entity_type: threat_actor
actor_name: "Indrik Spider"
common_name: "Indrik Spider"
actor_id: "G0119"
actor_type: "Cybercrime (ransomware / financial)"
aliases:
  - "Evil Corp"
country_of_origin: "Russia"
suspected_sponsors: []
attribution_confidence: ""
first_seen: "2014-01-01"
last_seen: ""
status: ""

motivations:
  - "Financial gain"
objectives:
  - "Credential theft and access brokerage"
  - "Ransomware deployment and extortion"
  - "Data theft to enable double-extortion"
victimology_summary: "Russia-based cybercrime group active since at least 2014, associated with Dridex and ransomware operations (e.g., BitPaymer, WastedLocker, Hades); observed using a mix of phishing, exploitation of public-facing systems, lateral movement, and encryption-for-impact tradecraft."
target_sectors: []
target_regions: []

related_groups: []

malware:
  - "[[30_CIPHER/05_Malware/Dridex]]"
  - "[[30_CIPHER/05_Malware/BitPaymer]]"
  - "[[30_CIPHER/05_Malware/WastedLocker]]"
  - "[[30_CIPHER/05_Malware/Hades]]"
tools: []

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1583 - Acquire Infrastructure|T1583 - Acquire Infrastructure]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility|T1560.001 - Archive Collected Data: Archive via Utility]]"
  - "[[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control|T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]"
  - "[[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]"
  - "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information|T1140 - Deobfuscate/Decode Files or Information]]"
  - "[[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools|T1562.001 - Impair Defenses: Disable or Modify Tools]]"
  - "[[20_Entities/07_TTPs/T1189 - Drive-by Compromise|T1189 - Drive-by Compromise]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1133 - External Remote Services|T1133 - External Remote Services]]"
  - "[[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp|T1070.006 - Indicator Removal: Timestomp]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1621 - Multi-Factor Authentication Interception|T1621 - Multi-Factor Authentication Interception]]"
  - "[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]"
  - "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory|T1003.001 - OS Credential Dumping: LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1055 - Process Injection|T1055 - Process Injection]]"
  - "[[20_Entities/07_TTPs/T1219 - Remote Access Tools|T1219 - Remote Access Tools]]"
  - "[[20_Entities/07_TTPs/T1021 - Remote Services|T1021 - Remote Services]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol|T1021.001 - Remote Services: Remote Desktop Protocol]]"
  - "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task|T1053.005 - Scheduled Task/Job: Scheduled Task]]"
  - "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery|T1033 - System Owner/User Discovery]]"
  - "[[20_Entities/07_TTPs/T1102 - Web Service|T1102 - Web Service]]"
  - "[[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver|T1102.001 - Web Service: Dead Drop Resolver]]"
  - "[[20_Entities/07_TTPs/T1077 - Windows Admin Shares|T1077 - Windows Admin Shares]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell|T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0119/"
  - "https://www.mitre.org/"
  - "https://www.welivesecurity.com/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0119"
  - "ransomware"
  - "cybercrime"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Indrik Spider (G0119) is a **Russia-based cybercrime group** active since at least **2014**, associated with **Dridex** and multiple ransomware operations (including **BitPaymer**, **WastedLocker**, and **Hades**). Their intrusions commonly combine **phishing**, **public-facing exploitation**, **credential access**, **lateral movement**, and **encryption for impact**, with recurring use of **web-based C2/“dead drop” patterns** and **remote administration**.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0119
- **Alias:** Evil Corp (per ATT&CK associated name)
- **Country of origin:** Russia (explicitly described by ATT&CK)
- **Confidence:** Not specified by ATT&CK beyond “Russia-based” characterization.

## 3. Motivations & Objectives
- **Primary motivation:** Financial gain.
- **Operational objectives (as reflected in ATT&CK tradecraft):**
  - Obtain initial access (phishing, drive-by, public-facing exploitation, external remote services).
  - Establish remote control and staging (web protocols, web services).
  - Expand access and harvest credentials (LSASS dumping; discovery).
  - Deliver ransomware and execute encryption (Data Encrypted for Impact).

## 4. Targeting Profile
- **Targeting:** Broad enterprise victimology consistent with financially motivated ransomware operations (ATT&CK does not constrain to specific sectors/regions on the Group page; treat as variable).
- **Telemetry implication:** Prepare for opportunistic and/or access-broker driven entry (external remote services + phishing + exploitation).

## 5. Tradecraft Overview
Common behaviors reflected in ATT&CK technique examples:
- **Initial access:** Spearphishing attachments; drive-by compromise; exploit public-facing applications; leverage external remote services.
- **Command & control:** Web protocols and web services (including **dead drop resolver** patterns).
- **Credential access & privilege enablement:** LSASS memory dumping; UAC bypass; defense impairment (disable/modify tools).
- **Execution & lateral movement:** Windows command shell, WMI, Windows admin shares, Remote Desktop; scheduled tasks.
- **Impact:** Ransomware encryption; file obfuscation/packing and decoding during execution.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583 - Acquire Infrastructure|T1583 - Acquire Infrastructure]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility|T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control|T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]
- [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information|T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools|T1562.001 - Impair Defenses: Disable or Modify Tools]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services|T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp|T1070.006 - Indicator Removal: Timestomp]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1621 - Multi-Factor Authentication Interception|T1621 - Multi-Factor Authentication Interception]]
- [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory|T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment|T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1055 - Process Injection|T1055 - Process Injection]]
- [[20_Entities/07_TTPs/T1219 - Remote Access Tools|T1219 - Remote Access Tools]]
- [[20_Entities/07_TTPs/T1021 - Remote Services|T1021 - Remote Services]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol|T1021.001 - Remote Services: Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task|T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery|T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1102 - Web Service|T1102 - Web Service]]
- [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver|T1102.001 - Web Service: Dead Drop Resolver]]
- [[20_Entities/07_TTPs/T1077 - Windows Admin Shares|T1077 - Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell|T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## 7. Malware & Tools Used
- Malware (named on ATT&CK Group page):
  - [[30_CIPHER/05_Malware/Dridex]]
  - [[30_CIPHER/05_Malware/BitPaymer]]
  - [[30_CIPHER/05_Malware/WastedLocker]]
  - [[30_CIPHER/05_Malware/Hades]]
- Tools:
  - Not enumerated with MITRE Software IDs in the extracted material; treat tooling as campaign-dependent and validate per incident.

## 8. Infrastructure Patterns
- **Leased/acquired infrastructure** to support operations (see [[20_Entities/07_TTPs/T1583 - Acquire Infrastructure|T1583 - Acquire Infrastructure]]).
- **Web-based C2** and **dead-drop style tasking** (see [[20_Entities/07_TTPs/T1102.001 - Web Service: Dead Drop Resolver|T1102.001 - Web Service: Dead Drop Resolver]]).

## 9. Campaign History
- ATT&CK links Indrik Spider to multiple financially motivated intrusions and ransomware events; campaign boundaries vary by affiliate access and toolset.

## 10. Known Indicators
- Treat IOCs as **campaign-specific**. Focus on behavior:
  - External remote access anomalies + RDP/SMB admin share activity.
  - Scheduled task creation spikes and WMI remote execution patterns.
  - LSASS access/dumps and follow-on credential replay.
  - Rapid file encryption patterns and pre-encryption staging/archiving.

## 11. Defensive Recommendations
- **Identity:** Enforce phishing-resistant MFA; monitor MFA interception attempts; block legacy auth where possible.
- **Endpoint:** Enable PowerShell + command-line logging; detect LSASS access/dumps; alert on timestomp; watch for process injection signals.
- **Network:** Restrict/monitor inbound remote services; segment SMB admin shares; monitor suspicious web-service “dead drop” traffic.
- **Exposure management:** Patch internet-facing systems; monitor exploit attempts; harden externally exposed RDP/VPN/SSO.

## 12. Analyst Notes
- Highest-signal hunt pivots: **T1053.005**, **T1047**, **T1077**, **T1003.001**, followed by **T1486** impact chain.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0119/
- Public research portals (general): https://www.welivesecurity.com/

## 14. References
- MITRE ATT&CK. (n.d.). *Indrik Spider (G0119).* https://attack.mitre.org/groups/G0119/
- ESET. (n.d.). *WeLiveSecurity (research portal).* https://www.welivesecurity.com/

## 15. Notes
- Populate MITRE Software (S####) links after correlating the specific intrusion set/campaign in your environment.
