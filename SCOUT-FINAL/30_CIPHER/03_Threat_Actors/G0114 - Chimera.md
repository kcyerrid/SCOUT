---
entity_type: threat_actor
actor_name: "Chimera"
common_name: "Chimera"
actor_id: "G0114"
actor_type: "Cyber espionage (suspected China-based)"
aliases: []
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "2-medium"
first_seen: "2018-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Collection against strategic targets (e.g., technology/manufacturing, aviation data)"]
victimology_summary: "Chimera is a suspected China-linked espionage cluster reported in public sources to have targeted strategic victims, including technology-related entities, using common enterprise post-exploitation tradecraft."
target_sectors: ["Technology (reported)","Manufacturing (reported)","Aviation (reported)"]
target_regions: ["Taiwan (reported)","Asia (reported)","Global (selective targeting reported)"]
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]"
tools:
  - "[[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound (S0521)]]"
  - "[[30_CIPHER/05_Malware/S0404 - esentutl|esentutl (S0404)]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]"
  - "[[30_CIPHER/05_Malware/S0039 - Net|Net (S0039)]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]"
infrastructure: ["[[Remote Services]]","[[Living off the Land]]","[[Internal Reconnaissance]]"]
ttps:
  - "[[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]"
  - "[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]"
  - "[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]"
  - "[[20_Entities/07_TTPs/T1119 - Automated Collection]]"
  - "[[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]"
  - "[[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying]]"
  - "[[20_Entities/07_TTPs/T1110.004 - Brute Force: Credential Stuffing]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1213.002 - Data from Information Repositories: Sharepoint]]"
  - "[[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive]]"
  - "[[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]"
  - "[[20_Entities/07_TTPs/T1074.002 - Data Staged: Remote Data Staging]]"
  - "[[20_Entities/07_TTPs/T1482 - Domain Trust Discovery]]"
  - "[[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]]"
  - "[[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]"
  - "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]"
  - "[[20_Entities/07_TTPs/T1567.002 - Exfiltration to Cloud Storage]]"
  - "[[20_Entities/07_TTPs/T1133 - External Remote Services]]"
  - "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]"
  - "[[20_Entities/07_TTPs/T1589.001 - Gather Victim Identity Information: Credentials]]"
  - "[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]"
  - "[[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]"
  - "[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]"
  - "[[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1570 - Lateral Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1680 - Machine Identity Discovery]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1556.001 - Modify Authentication Process: Domain Controller Authentication]]"
  - "[[20_Entities/07_TTPs/T1111 - Multi-Factor Authentication Interception]]"
  - "[[20_Entities/07_TTPs/T1106 - Native API]]"
  - "[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1135 - Network Share Discovery]]"
  - "[[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]"
  - "[[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]"
  - "[[20_Entities/07_TTPs/T1201 - Password Policy Discovery]]"
  - "[[20_Entities/07_TTPs/T1069.001 - Permission Groups Discovery: Local Groups]]"
  - "[[20_Entities/07_TTPs/T1057 - Process Discovery]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]"
  - "[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]"
  - "[[20_Entities/07_TTPs/T1021.006 - Remote Services: Windows Remote Management]]"
  - "[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]"
  - "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]"
  - "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]"
  - "[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]"
  - "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]"
  - "[[20_Entities/07_TTPs/T1007 - System Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]"
  - "[[20_Entities/07_TTPs/T1124 - System Time Discovery]]"
  - "[[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]"
  - "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]"
  - "[[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]"
  - "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"
notable_claims:
  - "Public sources and ATT&CK summaries describe a suspected China-linked cluster; attribution remains assessed."
intel_sources:
  - "https://attack.mitre.org/groups/G0114/"
  - "https://www.darkreading.com/threat-intelligence/hackers-abuse-microsoft-azure-for-c2-data-exfiltration"
tags: ["scout","threat-actor","mitre-g0114","espionage","china-suspected"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Chimera (G0114) is a suspected China-linked espionage cluster associated with strategic targeting and a broad set of enterprise post-exploitation behaviors: credential access, discovery, lateral movement via remote services, and cloud-assisted exfiltration patterns.

## 2. Attribution & Profile
- **Type:** Espionage
- **Attribution:** Assessed; suspected China-based
- **Attribution Confidence:** 2-medium

## 3. Targeting & Victimology
- Reported targeting includes strategic/technology-relevant victim sets (track specific victims only when disclosed in primary reporting).
- Regions reported include Taiwan and broader Asia; treat as selective/global unless case data narrows it.

## 4. Known Malware, Tools & Infrastructure
**Software (ATT&CK)**
- [[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound (S0521)]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]
- [[30_CIPHER/05_Malware/S0404 - esentutl|esentutl (S0404)]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]
- [[30_CIPHER/05_Malware/S0039 - Net|Net (S0039)]]
- [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]

## 5. Tradecraft Overview
- **Access:** external remote services + valid account abuse (where achieved)
- **Discovery:** broad domain/network discovery including trust relationships and password policies
- **Credential access:** NTDS/credential dumping + pass-the-hash
- **Movement:** RDP/SMB/WinRM + lateral tool transfer
- **Exfiltration:** cloud storage and/or C2 channel

## 6. MITRE ATT&CK Mapping
(See YAML `ttps` for the complete observed technique list; included here verbatim.)
- [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1071.004 - Application Layer Protocol: DNS]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1119 - Automated Collection]]
- [[20_Entities/07_TTPs/T1217 - Browser Information Discovery]]
- [[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying]]
- [[20_Entities/07_TTPs/T1110.004 - Brute Force: Credential Stuffing]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1213.002 - Data from Information Repositories: Sharepoint]]
- [[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive]]
- [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]
- [[20_Entities/07_TTPs/T1074.002 - Data Staged: Remote Data Staging]]
- [[20_Entities/07_TTPs/T1482 - Domain Trust Discovery]]
- [[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]]
- [[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1567.002 - Exfiltration to Cloud Storage]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1589.001 - Gather Victim Identity Information: Credentials]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]
- [[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion]]
- [[20_Entities/07_TTPs/T1070.006 - Indicator Removal: Timestomp]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1570 - Lateral Tool Transfer]]
- [[20_Entities/07_TTPs/T1680 - Machine Identity Discovery]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1556.001 - Modify Authentication Process: Domain Controller Authentication]]
- [[20_Entities/07_TTPs/T1111 - Multi-Factor Authentication Interception]]
- [[20_Entities/07_TTPs/T1106 - Native API]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1135 - Network Share Discovery]]
- [[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]
- [[20_Entities/07_TTPs/T1201 - Password Policy Discovery]]
- [[20_Entities/07_TTPs/T1069.001 - Permission Groups Discovery: Local Groups]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1021.006 - Remote Services: Windows Remote Management]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]
- [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1007 - System Service Discovery]]
- [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]
- [[20_Entities/07_TTPs/T1124 - System Time Discovery]]
- [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]

## 7. Detection Opportunities
1. **Credential access + DC targeting**
   - Alert on NTDS access patterns, DCSync/NTDS dump workflows, and unusual replication/backup tooling.
2. **Remote services lateral movement**
   - Correlate RDP/SMB/WinRM spikes with new binaries transferred laterally.
3. **Cloud exfil signals**
   - Detect unusual cloud storage use from servers/DC-adjacent systems; watch for new OAuth/app creds.

## 8. Response & Mitigation Guidance
- Tiering for AD, restrict admin logons, enforce LAPS/strong password policy, and harden RDP/WinRM.
- Egress controls for cloud storage; baseline and alert on anomalous SharePoint access patterns.
- Contain + credential reset if NTDS/LSA compromise is suspected.

## 9. Hunting Ideas
- Hunt for BloodHound collection artifacts + SharpHound-like collection paths.
- Look for timestomp + log-clear sequences around intrusion windows.
- Identify encoded PowerShell + service execution chains.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike (S0154)]]

## 11. Associated Tools
- [[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound (S0521)]]
- [[30_CIPHER/05_Malware/S0404 - esentutl|esentutl (S0404)]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]
- [[30_CIPHER/05_Malware/S0039 - Net|Net (S0039)]]
- [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]

## 12. Analyst Notes
- Chimera’s technique surface is broad; prioritize based on environment exposure (AD/remote services/cloud storage).
- Completeness: **High for ATT&CK technique coverage**; **Medium for victimology specificity** (avoid overcommitting beyond sourced victims).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group G0114: https://attack.mitre.org/groups/G0114/
- Dark Reading (Azure abuse coverage): https://www.darkreading.com/threat-intelligence/hackers-abuse-microsoft-azure-for-c2-data-exfiltration

## 14. References (APA)
- MITRE ATT&CK. (n.d.). *Chimera (G0114).* https://attack.mitre.org/groups/G0114/
- Dark Reading. (n.d.). *Hackers abuse Microsoft Azure for C2, data exfiltration.* https://www.darkreading.com/threat-intelligence/hackers-abuse-microsoft-azure-for-c2-data-exfiltration
