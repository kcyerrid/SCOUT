---
entity_type: threat_actor
actor_name: "Operation Wocao"
common_name: "Operation Wocao"
actor_id: "G0116"
actor_type: "Cyber espionage"
aliases: []
country_of_origin: "China"
suspected_sponsors: []
attribution_confidence: ""
first_seen: ""
last_seen: ""
status: "Deprecated"

motivations:
  - "Espionage"
objectives:
  - "Initial access via exploitation and stolen credentials"
  - "Credential access and privileged account discovery"
  - "Lateral movement across Windows environments"
  - "Collection, staging, and exfiltration of targeted data"
victimology_summary: "Deprecated ATT&CK group entry describing activity by a China-based cyber espionage adversary; targeted government organizations, managed service providers, and energy/health care/technology sectors across multiple countries. MITRE notes tooling/TTP overlap with APT20, suggesting possible overlap."
target_sectors:
  - "Government"
  - "Managed Service Providers (MSPs)"
  - "Energy"
  - "Health care"
  - "Technology"
target_regions:
  - "Brazil"
  - "China"
  - "France"
  - "Germany"
  - "Italy"
  - "Mexico"
  - "Portugal"
  - "Spain"
  - "United Kingdom"
  - "United States"
related_groups: []
malware: []
tools:
  - "[[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound]]"
  - "[[30_CIPHER/05_Malware/S0105 - dsquery|dsquery]]"
  - "[[30_CIPHER/05_Malware/S0357 - Impacket|Impacket]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0104 - netstat|netstat]]"
  - "[[30_CIPHER/05_Malware/S0194 - PowerSploit|PowerSploit]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]"
  - "[[30_CIPHER/05_Malware/S0183 - Tor|Tor]]"
  - "[[30_CIPHER/05_Malware/S0645 - Wevtutil|Wevtutil]]"
infrastructure:
  - "Purchased servers used during the campaign (Acquire Infrastructure: Server)"
  - "Registered email accounts for campaign operations"
  - "Proxy chaining / multi-hop proxying; Tor exit nodes observed"
ttps:
  - "[[20_Entities/07_TTPs/T1087.002 - Domain Account|T1087.002 - Domain Account]]"
  - "[[20_Entities/07_TTPs/T1583.004 - Server|T1583.004 - Server]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001 - Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001 - Archive via Utility]]"
  - "[[20_Entities/07_TTPs/T1119 - Automated Collection|T1119 - Automated Collection]]"
  - "[[20_Entities/07_TTPs/T1115 - Clipboard Data|T1115 - Clipboard Data]]"
  - "[[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001 - PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003 - Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1059.005 - Visual Basic|T1059.005 - Visual Basic]]"
  - "[[20_Entities/07_TTPs/T1059.006 - Python|T1059.006 - Python]]"
  - "[[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]]"
  - "[[20_Entities/07_TTPs/T1005 - Data from Local System|T1005 - Data from Local System]]"
  - "[[20_Entities/07_TTPs/T1001 - Data Obfuscation|T1001 - Data Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1074.001 - Local Data Staging|T1074.001 - Local Data Staging]]"
  - "[[20_Entities/07_TTPs/T1587.001 - Malware|T1587.001 - Malware]]"
  - "[[20_Entities/07_TTPs/T1573.002 - Asymmetric Cryptography|T1573.002 - Asymmetric Cryptography]]"
  - "[[20_Entities/07_TTPs/T1585.002 - Email Accounts|T1585.002 - Email Accounts]]"
  - "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel|T1041 - Exfiltration Over C2 Channel]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1133 - External Remote Services|T1133 - External Remote Services]]"
  - "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]"
  - "[[20_Entities/07_TTPs/T1589 - Gather Victim Identity Information|T1589 - Gather Victim Identity Information]]"
  - "[[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]]"
  - "[[20_Entities/07_TTPs/T1070.001 - Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]]"
  - "[[20_Entities/07_TTPs/T1070.004 - File Deletion|T1070.004 - File Deletion]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1056.001 - Keylogging|T1056.001 - Keylogging]]"
  - "[[20_Entities/07_TTPs/T1570 - Lateral Tool Transfer|T1570 - Lateral Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1680 - Local Storage Discovery|T1680 - Local Storage Discovery]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1112 - Modify Registry|T1112 - Modify Registry]]"
  - "[[20_Entities/07_TTPs/T1111 - Multi-Factor Authentication Interception|T1111 - Multi-Factor Authentication Interception]]"
  - "[[20_Entities/07_TTPs/T1106 - Native API|T1106 - Native API]]"
  - "[[20_Entities/07_TTPs/T1046 - Network Service Discovery|T1046 - Network Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1135 - Network Share Discovery|T1135 - Network Share Discovery]]"
  - "[[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol|T1095 - Non-Application Layer Protocol]]"
  - "[[20_Entities/07_TTPs/T1571 - Non-Standard Port|T1571 - Non-Standard Port]]"
  - "[[20_Entities/07_TTPs/T1027.005 - Indicator Removal from Tools|T1027.005 - Indicator Removal from Tools]]"
  - "[[20_Entities/07_TTPs/T1027.010 - Command Obfuscation|T1027.010 - Command Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Tool|T1588.002 - Tool]]"
  - "[[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001 - LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1003.006 - DCSync|T1003.006 - DCSync]]"
  - "[[20_Entities/07_TTPs/T1120 - Peripheral Device Discovery|T1120 - Peripheral Device Discovery]]"
  - "[[20_Entities/07_TTPs/T1069.001 - Local Groups|T1069.001 - Local Groups]]"
  - "[[20_Entities/07_TTPs/T1057 - Process Discovery|T1057 - Process Discovery]]"
  - "[[20_Entities/07_TTPs/T1055 - Process Injection|T1055 - Process Injection]]"
  - "[[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]"
  - "[[20_Entities/07_TTPs/T1090.001 - Internal Proxy|T1090.001 - Internal Proxy]]"
  - "[[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]"
  - "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task|T1053.005 - Scheduled Task]]"
  - "[[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]]"
  - "[[20_Entities/07_TTPs/T1518 - Software Discovery|T1518 - Software Discovery]]"
  - "[[20_Entities/07_TTPs/T1518.001 - Security Software Discovery|T1518.001 - Security Software Discovery]]"
  - "[[20_Entities/07_TTPs/T1558.003 - Kerberoasting|T1558.003 - Kerberoasting]]"
  - "[[20_Entities/07_TTPs/T1082 - System Information Discovery|T1082 - System Information Discovery]]"
  - "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]"
  - "[[20_Entities/07_TTPs/T1016.001 - Internet Connection Discovery|T1016.001 - Internet Connection Discovery]]"
  - "[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery|T1049 - System Network Connections Discovery]]"
  - "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery|T1033 - System Owner/User Discovery]]"
  - "[[20_Entities/07_TTPs/T1007 - System Service Discovery|T1007 - System Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1569.002 - Service Execution|T1569.002 - Service Execution]]"
  - "[[20_Entities/07_TTPs/T1124 - System Time Discovery|T1124 - System Time Discovery]]"
  - "[[20_Entities/07_TTPs/T1552.004 - Private Keys|T1552.004 - Private Keys]]"
  - "[[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]]"
  - "[[20_Entities/07_TTPs/T1078.002 - Domain Accounts|T1078.002 - Domain Accounts]]"
  - "[[20_Entities/07_TTPs/T1078.003 - Local Accounts|T1078.003 - Local Accounts]]"
  - "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0116/"
  - "https://attack.mitre.org/campaigns/C0014/"
  - "https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "mitre-g0116"
  - "G0116"
  - "china"
  - "espionage"
created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Operation Wocao (G0116) is a **deprecated** ATT&CK group entry describing activity by a **China-based cyber espionage** adversary. MITRE reports targeting across government, MSPs, and multiple commercial sectors, with **tooling/TTP similarity to APT20** suggesting possible overlap. Primary public detail is preserved in the associated ATT&CK campaign record for **Operation Wocao (C0014)** and the Fox-IT reporting referenced by ATT&CK.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0116 (Deprecated).  
- **Geopolitical nexus (per MITRE):** China-based cyber espionage adversary.  
- **Overlap note (per MITRE):** Similar TTPs/tools to “APT20,” suggesting possible overlap.  
- **Confidence:** Not explicitly stated by ATT&CK for sponsorship; treat as **unconfirmed**.

## 3. Motivations & Objectives
- **Motivation:** Espionage (per ATT&CK characterization).  
- **Operational objectives (observed via C0014 behaviors):**
  - Gain and maintain access (public-facing exploitation and stolen VPN credentials).
  - Credential access (AD credential dumping, password manager access, private keys/certs).
  - Internal recon and lateral movement (SMB/WMI/service exec/scheduled tasks).
  - Data collection, staging, and exfiltration over C2 channels.

## 4. Targeting Profile
- **Sectors (MITRE group page):** Government, MSPs, energy, health care, technology.  
- **Geographies:** Campaign reporting includes organizations across **Brazil, China, France, Germany, Italy, Mexico, Portugal, Spain, the United Kingdom, and the United States** (campaign record), and the group deprecation note highlights multiple countries including **China, France, Germany, UK, US**.

## 5. Tradecraft Overview
Telemetry-anchored behaviors reflected in ATT&CK campaign mapping (C0014):
- **Initial access:** Exploitation of **public-facing applications** and use of **stolen VPN credentials** ([[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]], [[20_Entities/07_TTPs/T1133 - External Remote Services|T1133 - External Remote Services]], [[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]]).
- **Command execution & automation:** PowerShell/cmd/VBScript/Python used for recon and ops ([[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001 - PowerShell]], [[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003 - Windows Command Shell]], [[20_Entities/07_TTPs/T1059.005 - Visual Basic|T1059.005 - Visual Basic]], [[20_Entities/07_TTPs/T1059.006 - Python|T1059.006 - Python]]).
- **Credential access:** LSASS access, DCSync, password manager credential access, private keys/certificates dumping ([[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001 - LSASS Memory]], [[20_Entities/07_TTPs/T1003.006 - DCSync|T1003.006 - DCSync]], [[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]], [[20_Entities/07_TTPs/T1552.004 - Private Keys|T1552.004 - Private Keys]]).
- **Discovery & lateral movement:** Network share/service discovery; SMB tool transfer; WMI and service execution; scheduled task execution; proxy chaining ([[20_Entities/07_TTPs/T1046 - Network Service Discovery|T1046 - Network Service Discovery]], [[20_Entities/07_TTPs/T1135 - Network Share Discovery|T1135 - Network Share Discovery]], [[20_Entities/07_TTPs/T1570 - Lateral Tool Transfer|T1570 - Lateral Tool Transfer]], [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation|T1047 - Windows Management Instrumentation]], [[20_Entities/07_TTPs/T1569.002 - Service Execution|T1569.002 - Service Execution]], [[20_Entities/07_TTPs/T1053.005 - Scheduled Task|T1053.005 - Scheduled Task]], [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]).
- **Defense evasion:** Firewall rule changes, event log clearing, file deletion/trace removal, masquerading tool names/paths ([[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]], [[20_Entities/07_TTPs/T1070.001 - Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]], [[20_Entities/07_TTPs/T1070.004 - File Deletion|T1070.004 - File Deletion]], [[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]).
- **Collection & exfiltration:** Automated collection, clipboard capture, staging, archiving, exfil over C2 channel ([[20_Entities/07_TTPs/T1119 - Automated Collection|T1119 - Automated Collection]], [[20_Entities/07_TTPs/T1115 - Clipboard Data|T1115 - Clipboard Data]], [[20_Entities/07_TTPs/T1074.001 - Local Data Staging|T1074.001 - Local Data Staging]], [[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001 - Archive via Utility]], [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel|T1041 - Exfiltration Over C2 Channel]]).

## 6. MITRE ATT&CK Mapping
High-signal / triage-priority TTPs from the ATT&CK campaign mapping:
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]] — initial access via vulnerable internet-facing apps (e.g., JBoss noted in ATT&CK examples for C0014).
- [[20_Entities/07_TTPs/T1133 - External Remote Services|T1133 - External Remote Services]] + [[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]] — use of stolen VPN credentials for entry and movement.
- [[20_Entities/07_TTPs/T1003.006 - DCSync|T1003.006 - DCSync]] and [[20_Entities/07_TTPs/T1558.003 - Kerberoasting|T1558.003 - Kerberoasting]] — domain credential theft paths that strongly indicate AD compromise.
- [[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]] — persistent access on servers; also enables staging and internal recon.
- [[20_Entities/07_TTPs/T1070.001 - Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]] + [[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]] — active defense impairment/covering tracks.

## 7. Malware & Tools Used
ATT&CK software mapped to Operation Wocao campaign activity (C0014):
- Tools:
  - [[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound]]
  - [[30_CIPHER/05_Malware/S0105 - dsquery|dsquery]]
  - [[30_CIPHER/05_Malware/S0357 - Impacket|Impacket]]
  - [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]
  - [[30_CIPHER/05_Malware/S0104 - netstat|netstat]]
  - [[30_CIPHER/05_Malware/S0194 - PowerSploit|PowerSploit]]
  - [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]
  - [[30_CIPHER/05_Malware/S0183 - Tor|Tor]]
  - [[30_CIPHER/05_Malware/S0645 - Wevtutil|Wevtutil]]
- Malware:
  - ATT&CK notes **custom web shells** developed/used in the campaign (T1587.001/T1505.003), but the group/campaign record does not provide a distinct MITRE S-ID for those web shells.

## 8. Infrastructure Patterns
Patterns grounded in ATT&CK campaign notes:
- **Infrastructure acquisition:** purchased servers (including via cryptocurrency) ([[20_Entities/07_TTPs/T1583.004 - Server|T1583.004 - Server]]).
- **Account infrastructure:** registered campaign email accounts ([[20_Entities/07_TTPs/T1585.002 - Email Accounts|T1585.002 - Email Accounts]]).
- **C2 and proxying:** HTTP/HTTPS plus custom protocols; proxy chaining/multi-hop; Tor exit nodes observed ([[20_Entities/07_TTPs/T1071.001 - Web Protocols|T1071.001 - Web Protocols]], [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]], [[30_CIPHER/05_Malware/S0183 - Tor|Tor]]).

## 9. Campaign History
- **ATT&CK Campaign:** Operation Wocao (**C0014**) — canonical ATT&CK campaign record with technique/software mapping and examples.  
  - Campaign URL: https://attack.mitre.org/campaigns/C0014/
- **Primary public reporting referenced by ATT&CK:** Fox-IT report (2019-12-19).  
  - Report PDF: https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf

## 10. Known Indicators
ATT&CK does not publish a stable, campaign-wide IOC set for G0116; treat IOCs as **time-bound** and **victim-specific**. Prioritize behavior-based pivots:
- **Event log clearing:** `wevtutil cl system` / `wevtutil cl security` execution traces ([[30_CIPHER/05_Malware/S0645 - Wevtutil|Wevtutil]], [[20_Entities/07_TTPs/T1070.001 - Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]]).
- **AD credential theft:** DCSync patterns (Directory Replication permissions usage) ([[20_Entities/07_TTPs/T1003.006 - DCSync|T1003.006 - DCSync]]).
- **Kerberoasting:** spikes in service ticket requests followed by offline cracking activity ([[20_Entities/07_TTPs/T1558.003 - Kerberoasting|T1558.003 - Kerberoasting]]).
- **Remote execution:** WMI/service creation/PsExec usage in non-admin workflows ([[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation|T1047 - Windows Management Instrumentation]], [[20_Entities/07_TTPs/T1569.002 - Service Execution|T1569.002 - Service Execution]], [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]).

## 11. Defensive Recommendations
Detection engineering and hardening aligned to mapped TTPs:
- **External attack surface (highest ROI):**
  - Patch/mitigate internet-facing app stacks (e.g., JBoss class exposures) and enforce WAF/virtual patching for known exploit chains ([[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]).
  - Tighten VPN access: MFA, device posture, geo/ASN anomaly detection, impossible travel, conditional access ([[20_Entities/07_TTPs/T1133 - External Remote Services|T1133 - External Remote Services]], [[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]]).
- **Windows/AD controls:**
  - Enable and centralize PowerShell logging (Module/Script Block), process creation, and WMI/service creation telemetry ([[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001 - PowerShell]], [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation|T1047 - Windows Management Instrumentation]], [[20_Entities/07_TTPs/T1569.002 - Service Execution|T1569.002 - Service Execution]]).
  - Alert on DCSync indicators (replication API calls by non-DC principals) and on suspicious Kerberos service ticket harvesting ([[20_Entities/07_TTPs/T1003.006 - DCSync|T1003.006 - DCSync]], [[20_Entities/07_TTPs/T1558.003 - Kerberoasting|T1558.003 - Kerberoasting]]).
- **Defense evasion monitoring:**
  - High-priority alerts for event log clearing and firewall rule modifications from interactive shells or remote execution contexts ([[20_Entities/07_TTPs/T1070.001 - Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]], [[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall|T1562.004 - Disable or Modify System Firewall]]).
- **Web shell posture:**
  - File integrity monitoring and EDR detections for suspicious server-side script drops/edits; correlate with unusual outbound C2 and internal scanning ([[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]]).

## 12. Analyst Notes
- Treat **G0116 as a deprecated label**; operationally, scope incidents using the **C0014 behavior set** and your internal clustering (infrastructure, tooling, victimology).
- Highest-confidence pivots for response: **external access logs (VPN/app)** → **web shell presence** → **AD credential theft (DCSync/Kerberoast)** → **service/WMI remote exec** → **log tampering**.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group (Deprecated): https://attack.mitre.org/groups/G0116/
- MITRE ATT&CK Campaign (C0014): https://attack.mitre.org/campaigns/C0014/
- Fox-IT report (PDF): https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf

## 14. References
- MITRE ATT&CK. (n.d.). *Operation Wocao (G0116).* https://attack.mitre.org/groups/G0116/
- MITRE ATT&CK. (n.d.). *Operation Wocao (C0014).* https://attack.mitre.org/campaigns/C0014/
- Fox-IT. (2019, December 19). *Operation Wocao: Shining a light on one of China’s hidden hacking groups.* https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf

## 15. Notes
- Populate **Known Indicators** with case-specific IOCs only (hashes/domains/URLs) once verified and time-scoped.
- If your vault adds a Campaign folder convention, consider creating a campaign note for C0014 and linking it from Section 9.
