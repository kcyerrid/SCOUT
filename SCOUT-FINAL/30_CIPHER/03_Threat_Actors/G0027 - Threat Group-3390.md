---
entity_type: threat_actor
actor_name: "Threat Group-3390"
common_name: "Threat Group-3390"
actor_id: "G0027"
actor_type: "State-linked intrusion set (attributed); espionage with mixed-motive activity reported"
aliases: ["TG-3390","Emissary Panda","APT27","BRONZE UNION","LuckyMouse","Iron Tiger","Earth Smilodon","Linen Typhoon"]
country_of_origin: "China (attributed)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2010-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage","Financial gain (reported)"]
objectives: ["Collect political/industrial/defense intelligence via strategic web compromises and targeted intrusions","Establish durable footholds (notably through compromised email and collaboration servers)","Credential theft and lateral movement to reach high-value data stores","Exfiltrate selected confidential data; in some reporting, monetize access/data (mixed-motive)"]
victimology_summary: "Threat Group-3390 (MITRE ATT&CK G0027) is described as a China-attributed threat group active since at least 2010, known for extensive use of strategic web compromises (watering holes) to reach select victims and for intrusions affecting aerospace/defense, government, technology, energy, manufacturing, and gambling/betting sectors. Public reporting has highlighted operations that pivot quickly to compromise Microsoft Exchange and other enterprise servers, use web shells and credential logging, and employ malware families such as [[30_CIPHER/05_Malware/PlugX]] and [[30_CIPHER/05_Malware/HTTPBrowser]]. U.S. law-enforcement reporting in 2025 described activity historically labeled as “APT27/Threat Group 3390/Emissary Panda/Bronze Union/Lucky Mouse/Iron Tiger” as part of long-running hacking conspiracies with alleged ties to PRC government entities and profit-motivated outcomes."
target_sectors: ["Aerospace","Defense","Government","Technology","Energy","Manufacturing","Gambling/Betting","Education (reported)","Legal (reported)","International relations / NGOs (reported)"]
target_regions: ["United States (reported)","United Kingdom (reported)","France (reported)","Middle East (reported)","Global (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/HTTPBrowser]]","[[30_CIPHER/05_Malware/PlugX]]","[[30_CIPHER/05_Malware/China Chopper]]","[[30_CIPHER/05_Malware/ASPXSpy]]","[[30_CIPHER/05_Malware/Clambling]]","[[30_CIPHER/05_Malware/RCSession]]","[[30_CIPHER/05_Malware/SysUpdate]]","[[30_CIPHER/05_Malware/ZxShell]]","[[30_CIPHER/05_Malware/HyperBro]]"]
tools: ["[[30_CIPHER/05_Malware/certutil]]","[[30_CIPHER/05_Malware/Cobalt Strike]]","[[30_CIPHER/05_Malware/Mimikatz]]","[[30_CIPHER/05_Malware/NBTscan]]","[[30_CIPHER/05_Malware/Net]]","[[30_CIPHER/05_Malware/netstat]]","[[30_CIPHER/05_Malware/pwdump]]","[[30_CIPHER/05_Malware/Windows Credential Editor]]","[[30_CIPHER/05_Malware/Tasklist]]","[[30_CIPHER/05_Malware/Systeminfo]]","[[30_CIPHER/05_Malware/Impacket]]"]
infrastructure: ["[[Strategic Web Compromises]]","[[Watering hole delivery]]","[[IP whitelisting]]","[[Compromised Internet-facing servers]]","[[Web shells]]","[[Exchange server compromise]]","[[SharePoint exploitation]]","[[Dropbox staging/exfiltration]]","[[Domain registration for C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]","[[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]","[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]","[[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]","[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1053.002 - Scheduled Task/Job: At]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Threat Group-3390 (G0027) (Last Modified 2025-10-15): https://attack.mitre.org/groups/G0027/","Dell SecureWorks CTU — Threat Group-3390 Targets Organizations for Cyberespionage (2015-08-05): https://www.sophos.com/en-us/research/threat-group-3390-targets-organizations-for-cyberespionage","Palo Alto Networks Unit 42 — Emissary Panda Attacks Middle East Government SharePoint Servers (2019-05-28): https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/","Council on Foreign Relations — Cyber Operations Tracker: Emissary Panda (2015-08-05): https://www.cfr.org/cyber-operations/2015/08/05/emissary-panda/","U.S. Department of Justice (USADC) — Chinese Nationals with Ties to the PRC Government and “APT27” Charged… (2025-03-05): https://www.justice.gov/usao-dc/pr/chinese-nationals-ties-prc-government-and-apt27-charged-computer-hacking-campaign-profit"]
tags: ["threat-actor","threat-group-3390","tg-3390","g0027","apt27","emissary-panda","bronze-union","china","cyber-espionage","watering-hole","exchange","sharepoint"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Threat Group-3390

## 1. BLUF / Executive Summary
Threat Group-3390 (MITRE ATT&CK **G0027**) is a China-attributed intrusion set strongly associated with **strategic web compromises (watering holes)** and targeted enterprise intrusions affecting **aerospace/defense, government, technology, energy, manufacturing**, and related sectors. Public reporting highlights a pattern of **selective victim filtering**, rapid pivoting to **server-side footholds** (including Exchange and SharePoint compromises), **credential capture**, and **targeted data theft**. U.S. law-enforcement reporting in 2025 additionally describes long-running hacking conspiracies tied to labels that include “Threat Group 3390/APT27/Emissary Panda,” alleging PRC government ties alongside **profit-motivated outcomes**, suggesting a **mixed-motive** posture in at least some activity.

## 2. Attribution Notes
- MITRE ATT&CK identifies Threat Group-3390 as a **Chinese threat group** and lists multiple associated tracking names (e.g., Emissary Panda, APT27, BRONZE UNION, LuckyMouse, Iron Tiger).  
- Vendor reporting (notably SecureWorks) assessed with **moderate confidence** that the group is based in China, emphasizing circumstantial indicators and the possibility of false-flag considerations.  
- A 2025 U.S. DOJ press release states that activity historically labeled with “APT27/Threat Group 3390/Emissary Panda/Bronze Union/Lucky Mouse/Iron Tiger” relates to charged hacking conspiracies alleging ties to PRC government entities and monetization of stolen data/access.

## 3. Motivations & Objectives
- **Primary (widely reported):** Espionage—collection of defense technology/capability intelligence, industrial intelligence, and political intelligence through selective targeting and long-running access.  
- **Additional (reported in 2025 law enforcement):** Monetization—profit-oriented intrusions and brokering/sale of stolen data/access in parallel with alleged state ties (mixed-motive activity).

## 4. Targeting Profile
- **Sectors (MITRE + vendor reporting):** aerospace/defense, government, technology, energy, manufacturing, gambling/betting; additional reported verticals include legal, education, and organizations involved in international relations.  
- **Geography (reported):** U.S. and U.K. victimization is explicitly noted in open reporting; additional reporting includes activity impacting other regions (e.g., Middle East government organizations via SharePoint compromise).

## 5. Tradecraft Overview
- **Strategic web compromises / watering holes:** Compromise of legitimate websites likely to attract intended victims, with selective delivery mechanisms (e.g., filtering/whitelisting) to reduce exposure and increase targeting precision (aligns to [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]).  
- **Phishing complement:** Use of spearphishing attachments in addition to watering holes, enabling victim-specific initial access (aligns to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]).  
- **Server-side persistence focus:** Recurrent emphasis on compromising and maintaining access via enterprise servers (notably Exchange and SharePoint), often paired with web shells (aligns to [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]).  
- **Credential and access expansion:** Credential capture/logging and abuse of stolen credentials to deepen access (aligns to [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]]).  
- **Operational enablement and cleanup:** Tool transfer, execution via Windows shell/PowerShell, and log/trace reduction behaviors are documented in ATT&CK technique associations (e.g., [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]], [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]).  
- **Data theft and cloud staging:** Reported use of cloud services (e.g., Dropbox) for staging/exfiltration and hosting payloads aligns to [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]
- [[20_Entities/07_TTPs/T1210 - Exploitation of Remote Services]]
- [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- [[20_Entities/07_TTPs/T1053.002 - Scheduled Task/Job: At]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
- [[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]
- [[20_Entities/07_TTPs/T1608.002 - Stage Capabilities: Upload Tool]]
- [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]

## 7. Malware & Tools Used
**Malware / web-shell ecosystem (MITRE & vendor reporting)**
- [[30_CIPHER/05_Malware/HTTPBrowser]]
- [[30_CIPHER/05_Malware/PlugX]]
- [[30_CIPHER/05_Malware/China Chopper]]
- [[30_CIPHER/05_Malware/ASPXSpy]]
- [[30_CIPHER/05_Malware/Clambling]]
- [[30_CIPHER/05_Malware/RCSession]]
- [[30_CIPHER/05_Malware/SysUpdate]]
- [[30_CIPHER/05_Malware/ZxShell]]
- [[30_CIPHER/05_Malware/HyperBro]] (reported in Emissary Panda/TG-3390 SharePoint activity)

**Operator tooling frequently referenced in public reporting**
- [[30_CIPHER/05_Malware/certutil]]
- [[30_CIPHER/05_Malware/Cobalt Strike]]
- [[30_CIPHER/05_Malware/Mimikatz]]
- [[30_CIPHER/05_Malware/Windows Credential Editor]]
- [[30_CIPHER/05_Malware/pwdump]]
- [[30_CIPHER/05_Malware/NBTscan]]
- [[30_CIPHER/05_Malware/Net]]
- [[30_CIPHER/05_Malware/netstat]]
- [[30_CIPHER/05_Malware/Tasklist]]
- [[30_CIPHER/05_Malware/Systeminfo]]
- [[30_CIPHER/05_Malware/Impacket]]

## 8. Infrastructure Patterns
- [[Strategic Web Compromises]] / [[Watering hole delivery]] with selective targeting (e.g., filtering/whitelisting) to reduce broad exposure while reaching intended victim profiles.
- [[Compromised Internet-facing servers]] used as staging points for exfiltration and as intermediate infrastructure, including reuse of already-compromised servers for later operations.
- [[Web shells]] as a recurrent persistence and operator-access mechanism on enterprise servers.
- [[Dropbox staging/exfiltration]] reported for payload hosting and data movement aligned to cloud-service abuse.
- [[Domain registration for C2]] and ongoing infrastructure management described in ATT&CK technique associations.

## 9. Campaign History
- **At least 2010:** MITRE ATT&CK describes activity as active since at least this year.  
- **2015-08-05:** SecureWorks published analysis of TG-3390 emphasizing strategic web compromises, selective delivery, and Exchange-focused compromise patterns (U.S./U.K. victims explicitly noted).  
- **2019-04 to 2019-05 (reported):** Unit 42 described Emissary Panda/TG-3390 exploitation of SharePoint (CVE-2019-0604) against Middle East government organizations with follow-on tool deployment and web shells.  
- **2025-03-05:** U.S. DOJ announced unsealed indictments and seizures tied to activity historically labeled as “APT27/Threat Group 3390/Emissary Panda/Bronze Union/Lucky Mouse/Iron Tiger,” alleging PRC ties and profit-driven hacking conspiracies spanning 2011–present (as reported).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Emphasize detection and response focused on **watering-hole/strategic web compromise** exposure pathways (high-risk browsing cohorts, partner sites, sector-specific sites), mapped to [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]].
- Harden and monitor **public-facing enterprise servers** (especially collaboration/email stacks) and watch for behaviors aligned to [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]] and [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell]].
- Increase monitoring for **credential capture and reuse** patterns aligned to [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Treat abnormal cloud-service interactions for staging/exfiltration as high-signal when correlated with intrusion context, aligned to [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]].
- Strengthen telemetry and response for common operator enablement behaviors such as [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]] and cleanup aligned to [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]].

## 12. Analyst Notes
- “Threat Group-3390” is a long-lived, multi-alias cluster. Vendor boundaries can differ; this note follows MITRE’s consolidation (G0027) and uses conservative language when bridging to other labels.  
- The 2025 DOJ description suggests **mixed-motive** outcomes (espionage-aligned targeting plus profit), but public reporting can vary by time window and subcluster; avoid assuming all historic activity shares the same motive mix.  
- Where public sources emphasize Exchange/SharePoint compromise and web-shell usage, interpret this as a prominent observed pattern rather than an exclusive capability set.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Threat Group-3390 (G0027): https://attack.mitre.org/groups/G0027/
- SecureWorks CTU (via Sophos) — Threat Group-3390 Targets Organizations for Cyberespionage (2015-08-05): https://www.sophos.com/en-us/research/threat-group-3390-targets-organizations-for-cyberespionage
- Unit 42 — Emissary Panda Attacks Middle East Government SharePoint Servers (2019-05-28): https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/
- CFR Cyber Operations Tracker — Emissary Panda (2015-08-05): https://www.cfr.org/cyber-operations/2015/08/05/emissary-panda/
- U.S. DOJ (USADC) — “APT27” charged; activity historically referred to as Threat Group 3390 (2025-03-05): https://www.justice.gov/usao-dc/pr/chinese-nationals-ties-prc-government-and-apt27-charged-computer-hacking-campaign-profit

## 14. References
1. MITRE ATT&CK. “Threat Group-3390 (G0027).” (Last Modified 2025-10-15). https://attack.mitre.org/groups/G0027/
2. Dell SecureWorks Counter Threat Unit. “Threat Group-3390 Targets Organizations for Cyberespionage.” (2015-08-05). https://www.sophos.com/en-us/research/threat-group-3390-targets-organizations-for-cyberespionage
3. Palo Alto Networks Unit 42. “Emissary Panda Attacks Middle East Government SharePoint Servers.” (2019-05-28). https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/
4. Council on Foreign Relations. “Cyber Operations Tracker: Emissary Panda.” (2015-08-05). https://www.cfr.org/cyber-operations/2015/08/05/emissary-panda/
5. U.S. Department of Justice, U.S. Attorney’s Office (District of Columbia). “Chinese Nationals with Ties to the PRC Government and ‘APT27’ Charged…” (2025-03-05). https://www.justice.gov/usao-dc/pr/chinese-nationals-ties-prc-government-and-apt27-charged-computer-hacking-campaign-profit
