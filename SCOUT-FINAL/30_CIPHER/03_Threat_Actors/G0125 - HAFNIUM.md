---
entity_type: threat_actor
actor_name: "HAFNIUM"
common_name: "HAFNIUM"
actor_id: "G0125"
actor_type: ""
aliases:
  - "Operation Exchange Marauder"
  - "Silk Typhoon"
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: ""
first_seen: ""
last_seen: ""
status: ""

motivations: []
objectives:
  - "Compromise Exchange and edge-facing services"
  - "Credential theft and lateral movement"
  - "Email and file exfiltration via web services/cloud storage"
victimology_summary: "Threat group tracked as HAFNIUM (also referenced as Operation Exchange Marauder / Silk Typhoon) observed exploiting on-premises Microsoft Exchange Server and using web shells, PowerShell/cmd execution, password spraying, credential dumping, and exfiltration to web services/cloud storage."
target_sectors: []
target_regions: []

related_groups: []

malware: []
tools:
  - "[[30_CIPHER/05_Malware/Covenant]]"
  - "[[30_CIPHER/05_Malware/Nishang]]"
  - "[[30_CIPHER/05_Malware/PowerCat]]"
  - "[[30_CIPHER/05_Malware/7-Zip]]"
  - "[[30_CIPHER/05_Malware/WinRAR]]"

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1098 - Account Manipulation|T1098 - Account Manipulation]]"
  - "[[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server|T1583.003 - Acquire Infrastructure: Virtual Private Server]]"
  - "[[20_Entities/07_TTPs/T1583.005 - Acquire Infrastructure: Botnet|T1583.005 - Acquire Infrastructure: Botnet]]"
  - "[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services|T1583.006 - Acquire Infrastructure: Web Services]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility|T1560.001 - Archive Collected Data: Archive via Utility]]"
  - "[[20_Entities/07_TTPs/T1119 - Automated Collection|T1119 - Automated Collection]]"
  - "[[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying|T1110.003 - Brute Force: Password Spraying]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell|T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell|T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1584.005 - Compromise Infrastructure: Botnet|T1584.005 - Compromise Infrastructure: Botnet]]"
  - "[[20_Entities/07_TTPs/T1136.002 - Create Account: Domain Account|T1136.002 - Create Account: Domain Account]]"
  - "[[20_Entities/07_TTPs/T1555.006 - Credentials from Password Stores: Cloud Secrets Management Stores|T1555.006 - Credentials from Password Stores: Cloud Secrets Management Stores]]"
  - "[[20_Entities/07_TTPs/T1132.001 - Data Encoding: Standard Encoding|T1132.001 - Data Encoding: Standard Encoding]]"
  - "[[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection|T1114.002 - Email Collection: Remote Email Collection]]"
  - "[[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage|T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]"
  - "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]"
  - "[[20_Entities/07_TTPs/T1592.004 - Gather Victim Host Information: Client Configurations|T1592.004 - Gather Victim Host Information: Client Configurations]]"
  - "[[20_Entities/07_TTPs/T1592.005 - Gather Victim Host Information: IP Addresses|T1592.005 - Gather Victim Host Information: IP Addresses]]"
  - "[[20_Entities/07_TTPs/T1564.001 - Hide Artifacts: Hidden Files and Directories|T1564.001 - Hide Artifacts: Hidden Files and Directories]]"
  - "[[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs|T1070.001 - Indicator Removal: Clear Windows Event Logs]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol|T1095 - Non-Application Layer Protocol]]"
  - "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory|T1003.001 - OS Credential Dumping: LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS|T1003.003 - OS Credential Dumping: NTDS]]"
  - "[[20_Entities/07_TTPs/T1057 - Process Discovery|T1057 - Process Discovery]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0125/"
  - "https://www.microsoft.com/"
  - "https://www.volexity.com/"
  - "https://www.rapid7.com/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0125"
  - "exchange"
  - "webshell"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
HAFNIUM (G0125) is tracked by ATT&CK for intrusions involving **exploitation of public-facing Microsoft Exchange Server**, followed by **web shell-enabled access**, **PowerShell/cmd execution**, **password spraying**, **credential dumping (LSASS/NTDS)**, and **exfiltration to cloud storage/web services**. ATT&CK examples also include **infrastructure acquisition/obfuscation** via VPS/botnets and **log clearing**.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0125
- **Aliases (ATT&CK):** Operation Exchange Marauder, Silk Typhoon
- **Sponsor/country:** Not explicitly stated on the ATT&CK Group page in the extracted material.

## 3. Motivations & Objectives
- Not explicitly stated by ATT&CK; operational objectives evidenced by technique set:
  - Gain access to edge systems (Exchange) and expand control.
  - Extract mailbox data and files; exfiltrate to cloud/web services.
  - Maintain operational security via obfuscation and log clearing.

## 4. Targeting Profile
- **Common victim profile:** organizations running on-prem Exchange and exposed edge services (ATT&CK examples).
- Sector/region specificity is not constrained by the extracted ATT&CK material for this note.

## 5. Tradecraft Overview
- **Initial access:** [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]] plus password spraying.
- **Execution:** Exchange PowerShell module usage; cmd execution.
- **Credential access:** procdump/LSASS dumping; NTDS acquisition; cloud secret store theft (Azure Key Vault).
- **Collection & exfil:** automated collection; remote email collection; exfiltration to cloud storage/file sharing.
- **Operational security:** hidden files/dirs; clearing Windows event logs; use of botnet/VPS/web services for obfuscation.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1110.003 - Brute Force: Password Spraying|T1110.003 - Brute Force: Password Spraying]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell|T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell|T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1114.002 - Email Collection: Remote Email Collection|T1114.002 - Email Collection: Remote Email Collection]]
- [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage|T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory|T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS|T1003.003 - OS Credential Dumping: NTDS]]
- [[20_Entities/07_TTPs/T1555.006 - Credentials from Password Stores: Cloud Secrets Management Stores|T1555.006 - Credentials from Password Stores: Cloud Secrets Management Stores]]
- [[20_Entities/07_TTPs/T1070.001 - Indicator Removal: Clear Windows Event Logs|T1070.001 - Indicator Removal: Clear Windows Event Logs]]
- [[20_Entities/07_TTPs/T1564.001 - Hide Artifacts: Hidden Files and Directories|T1564.001 - Hide Artifacts: Hidden Files and Directories]]
- [[20_Entities/07_TTPs/T1583.003 - Acquire Infrastructure: Virtual Private Server|T1583.003 - Acquire Infrastructure: Virtual Private Server]]
- [[20_Entities/07_TTPs/T1583.005 - Acquire Infrastructure: Botnet|T1583.005 - Acquire Infrastructure: Botnet]]
- [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services|T1583.006 - Acquire Infrastructure: Web Services]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols|T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol|T1095 - Non-Application Layer Protocol]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery|T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility|T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1132.001 - Data Encoding: Standard Encoding|T1132.001 - Data Encoding: Standard Encoding]]
- [[20_Entities/07_TTPs/T1098 - Account Manipulation|T1098 - Account Manipulation]]
- [[20_Entities/07_TTPs/T1136.002 - Create Account: Domain Account|T1136.002 - Create Account: Domain Account]]
- [[20_Entities/07_TTPs/T1584.005 - Compromise Infrastructure: Botnet|T1584.005 - Compromise Infrastructure: Botnet]]
- [[20_Entities/07_TTPs/T1592.004 - Gather Victim Host Information: Client Configurations|T1592.004 - Gather Victim Host Information: Client Configurations]]
- [[20_Entities/07_TTPs/T1592.005 - Gather Victim Host Information: IP Addresses|T1592.005 - Gather Victim Host Information: IP Addresses]]
- [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## 7. Malware & Tools Used
- ATT&CK examples reference:
  - Covenant (open-source C2 framework) [[30_CIPHER/05_Malware/Covenant]]
  - Nishang and PowerCat (downloaded to compromised hosts) [[30_CIPHER/05_Malware/Nishang]]; [[30_CIPHER/05_Malware/PowerCat]]
  - Utility tooling for archiving (7-Zip, WinRAR) [[30_CIPHER/05_Malware/7-Zip]]; [[30_CIPHER/05_Malware/WinRAR]]
- Web shells are referenced in technique narratives; enumerate specific web shell families per incident.

## 8. Infrastructure Patterns
- Use of leased VPS and botnet infrastructure to obfuscate communications.
- Use of acquired web services for C2 and exfiltration.
- Exfiltration to file-sharing/cloud storage services.

## 9. Campaign History
- ATT&CK documents Exchange-focused intrusions and follow-on credential theft/exfiltration workflows via technique examples.

## 10. Known Indicators
- **Exchange & identity anchors:**
  - Exploit telemetry against Exchange endpoints and unusual OAB export activity.
  - Password spray patterns and anomalous sign-ins.
- **Endpoint anchors:**
  - procdump-like LSASS access; NTDS access patterns.
  - Hidden directories and unexpected file drops.
  - Event log clearing (especially security/system) following interactive activity.
- **Network anchors:**
  - Unusual outbound uploads to cloud storage/file-sharing; web protocol traffic from server processes.

## 11. Defensive Recommendations
- **Patch & harden:** rapid patching of Exchange/edge devices; restrict admin interfaces and management endpoints.
- **Identity:** rate-limit spraying; conditional access; monitor anomalous mailbox export activity; protect Azure Key Vault and secret stores.
- **Endpoint:** EDR rules for LSASS dumping, NTDS access; alert on event log clearing; detect web shell behaviors via IIS logs.
- **Network:** monitor exfil to cloud storage; restrict outbound from Exchange servers to only required destinations.

## 12. Analyst Notes
- Prioritize scoping around: exploited Exchange server(s) → web shell presence → mailbox export/exfil → credential dumping → lateral movement expansion.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0125/
- Microsoft security portal: https://www.microsoft.com/
- Volexity: https://www.volexity.com/
- Rapid7: https://www.rapid7.com/

## 14. References
- MITRE ATT&CK. (n.d.). *HAFNIUM (G0125).* https://attack.mitre.org/groups/G0125/
- Microsoft. (n.d.). *Microsoft (security content portal).* https://www.microsoft.com/
- Volexity. (n.d.). *Volexity (research portal).* https://www.volexity.com/
- Rapid7. (n.d.). *Rapid7 (research portal).* https://www.rapid7.com/

## 15. Notes
- Add incident-specific MITRE Software (S####) mappings after validating the exact web shells/tooling observed in your environment.
