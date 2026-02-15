---
entity_type: threat_actor
actor_name: "Fox Kitten"
common_name: "Fox Kitten"
actor_id: "G0117"
actor_type: "State-linked (cyber espionage)"
aliases:
  - "UNC757"
  - "Parisite"
  - "Pioneer Kitten"
  - "RUBIDIUM"
  - "Lemon Sandstorm"
country_of_origin: "Iran"
suspected_sponsors:
  - "Iran"
attribution_confidence: "Medium"
first_seen: "2017-01-01"
last_seen: ""
status: "Active"

motivations:
  - "Espionage"
  - "Financial gain"
objectives:
  - "Initial access to target environments (notably remote access/VPN and public-facing services)"
  - "Credential access and account manipulation to maintain access"
  - "Establish persistent remote control via web shells and remote services"
  - "Data theft and, in some activity, ransomware deployment (Pay2Key)"
victimology_summary: "Iran-linked threat actor active since at least 2017 with suspected nexus to the Iranian government; targets organizations across the Middle East, North Africa, Europe, Australia, and North America. Targeted verticals include oil & gas, technology, government, defense, healthcare, manufacturing, and engineering; has also been associated with Pay2Key ransomware activity against Israeli companies."
target_sectors:
  - "Oil and gas"
  - "Technology"
  - "Government"
  - "Defense"
  - "Healthcare"
  - "Manufacturing"
  - "Engineering"
target_regions:
  - "Middle East"
  - "North Africa"
  - "Europe"
  - "Australia"
  - "North America"
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/S0020 - China Chopper|China Chopper]]"
  - "[[30_CIPHER/05_Malware/S0556 - Pay2Key|Pay2Key]]"
tools:
  - "[[30_CIPHER/05_Malware/S0508 - ngrok|ngrok]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]]"
infrastructure:
  - "Cloud-hosted C2 (AWS referenced in ATT&CK examples)"
  - "Reverse proxy tooling to bridge C2 to internal/local services"
  - "Web shells on compromised servers"
ttps:
  - "[[20_Entities/07_TTPs/T1087.001 - Local Account|T1087.001 - Local Account]]"
  - "[[20_Entities/07_TTPs/T1087.002 - Domain Account|T1087.002 - Domain Account]]"
  - "[[20_Entities/07_TTPs/T1560.001 - Archive via Utility|T1560.001 - Archive via Utility]]"
  - "[[20_Entities/07_TTPs/T1217 - Browser Information Discovery|T1217 - Browser Information Discovery]]"
  - "[[20_Entities/07_TTPs/T1110 - Brute Force|T1110 - Brute Force]]"
  - "[[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter|T1059 - Command and Scripting Interpreter]]"
  - "[[20_Entities/07_TTPs/T1059.001 - PowerShell|T1059.001 - PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Windows Command Shell|T1059.003 - Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1136.001 - Local Account|T1136.001 - Local Account]]"
  - "[[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]]"
  - "[[20_Entities/07_TTPs/T1530 - Data from Cloud Storage|T1530 - Data from Cloud Storage]]"
  - "[[20_Entities/07_TTPs/T1213.005 - Messaging Applications|T1213.005 - Messaging Applications]]"
  - "[[20_Entities/07_TTPs/T1005 - Data from Local System|T1005 - Data from Local System]]"
  - "[[20_Entities/07_TTPs/T1039 - Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]"
  - "[[20_Entities/07_TTPs/T1585 - Establish Accounts|T1585 - Establish Accounts]]"
  - "[[20_Entities/07_TTPs/T1585.001 - Social Media Accounts|T1585.001 - Social Media Accounts]]"
  - "[[20_Entities/07_TTPs/T1546.008 - Accessibility Features|T1546.008 - Accessibility Features]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1210 - Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]"
  - "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1036.004 - Masquerade Task or Service|T1036.004 - Masquerade Task or Service]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1046 - Network Service Discovery|T1046 - Network Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1027.010 - Command Obfuscation|T1027.010 - Command Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1027.013 - Encrypted/Encoded File|T1027.013 - Encrypted/Encoded File]]"
  - "[[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001 - LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1003.003 - NTDS|T1003.003 - NTDS]]"
  - "[[20_Entities/07_TTPs/T1572 - Protocol Tunneling|T1572 - Protocol Tunneling]]"
  - "[[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]"
  - "[[20_Entities/07_TTPs/T1012 - Query Registry|T1012 - Query Registry]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]"
  - "[[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]"
  - "[[20_Entities/07_TTPs/T1021.004 - SSH|T1021.004 - SSH]]"
  - "[[20_Entities/07_TTPs/T1021.005 - VNC|T1021.005 - VNC]]"
  - "[[20_Entities/07_TTPs/T1018 - Remote System Discovery|T1018 - Remote System Discovery]]"
  - "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task|T1053.005 - Scheduled Task]]"
  - "[[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]]"
  - "[[20_Entities/07_TTPs/T1552.001 - Credentials In Files|T1552.001 - Credentials In Files]]"
  - "[[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]]"
  - "[[20_Entities/07_TTPs/T1102 - Web Service|T1102 - Web Service]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0117/"
  - "https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-Kitten-Campaign.pdf"
  - "https://www.crowdstrike.com/en-us/blog/who-is-pioneer-kitten/"
  - "https://attack.mitre.org/software/S0556/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "mitre-g0117"
  - "G0117"
  - "iran"
  - "espionage"
  - "ransomware"
created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Fox Kitten (G0117) is a threat actor with a **suspected nexus to the Iranian government**, active since at least **2017**, targeting organizations across **MENA, Europe, Australia, and North America** and spanning multiple industrial verticals (oil & gas, technology, government, defense, healthcare, manufacturing, engineering). ATT&CK documents a tradecraft mix of **exploitation and remote access abuse**, persistent **web shell** footholds, **proxy/tunneling** to bridge access, and credential-focused operations. ATT&CK also associates Fox Kitten with **Pay2Key (S0556)** ransomware used since at least **July 2020**, including campaigns against **Israeli companies**.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0117
- **Attribution framing (ATT&CK):** “suspected nexus to the Iranian government” (treat as **suspected/likely**, not confirmed).
- **Aliases / associated clusters (ATT&CK):** UNC757, Parisite, Pioneer Kitten, RUBIDIUM, Lemon Sandstorm.
- **Confidence:** Medium (ATT&CK uses “suspected nexus,” and vendor reporting clusters the activity).

## 3. Motivations & Objectives
- **Motivations (source-grounded):**
  - Espionage (primary framing in vendor/ATT&CK descriptions).
  - Financial gain (supported by ATT&CK’s linkage to Pay2Key ransomware activity).
- **Objectives (as reflected by mapped behaviors):**
  - Compromise exposed services and maintain durable access ([[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]], [[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]]).
  - Obtain and use credentials to expand control ([[20_Entities/07_TTPs/T1552.001 - Credentials In Files|T1552.001 - Credentials In Files]], [[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]], [[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]]).
  - Establish proxy/tunnel paths for resilient operator access ([[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]], [[20_Entities/07_TTPs/T1572 - Protocol Tunneling|T1572 - Protocol Tunneling]]).
  - In some operations, deploy ransomware for impact/monetization (Pay2Key).

## 4. Targeting Profile
- **Regions (ATT&CK):** Middle East, North Africa, Europe, Australia, North America.
- **Sectors (ATT&CK):** oil & gas, technology, government, defense, healthcare, manufacturing, engineering.
- **Operational implication:** prioritize monitoring where external remote access and legacy perimeter appliances are common (VPN/RDP/public-facing apps), especially in industrial and government-adjacent environments.

## 5. Tradecraft Overview
Common behaviors in ATT&CK technique examples:
- **Initial access & expansion:** exploitation of public-facing applications and remote service exploitation ([[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]], [[20_Entities/07_TTPs/T1210 - Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]).
- **Persistence:** web shells and scheduled tasks (including loading/executing reverse proxy binaries) ([[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]], [[20_Entities/07_TTPs/T1053.005 - Scheduled Task|T1053.005 - Scheduled Task]]).
- **Credential-driven operations:** brute force against RDP; password manager access; credentials pulled from files ([[20_Entities/07_TTPs/T1110 - Brute Force|T1110 - Brute Force]], [[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]], [[20_Entities/07_TTPs/T1552.001 - Credentials In Files|T1552.001 - Credentials In Files]]).
- **Operator access bridging:** proxying and tunneling, including commercial/commodity tooling (e.g., ngrok in ATT&CK software mapping) ([[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]], [[20_Entities/07_TTPs/T1572 - Protocol Tunneling|T1572 - Protocol Tunneling]]).
- **Remote services for lateral movement:** RDP/SMB/SSH/VNC usage ([[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]], [[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]], [[20_Entities/07_TTPs/T1021.004 - SSH|T1021.004 - SSH]], [[20_Entities/07_TTPs/T1021.005 - VNC|T1021.005 - VNC]]).
- **Cloud/service abuse:** hosting C2 in AWS and using web services ([[20_Entities/07_TTPs/T1102 - Web Service|T1102 - Web Service]]).

## 6. MITRE ATT&CK Mapping
Key TTPs (triage + detection engineering anchors):
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]] — external exploitation to gain foothold.
- [[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]] — server persistence; often correlates with follow-on internal recon and staging.
- [[20_Entities/07_TTPs/T1110 - Brute Force|T1110 - Brute Force]] + [[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]] — credential guessing against remote access paths.
- [[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]] and [[20_Entities/07_TTPs/T1572 - Protocol Tunneling|T1572 - Protocol Tunneling]] — “bridge” infrastructure to maintain resilient operator connectivity.
- [[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]] and [[20_Entities/07_TTPs/T1552.001 - Credentials In Files|T1552.001 - Credentials In Files]] — practical credential theft pivots.

## 7. Malware & Tools Used
ATT&CK software mappings for Fox Kitten:
- Malware:
  - [[30_CIPHER/05_Malware/S0020 - China Chopper|China Chopper]] (web shell)
  - [[30_CIPHER/05_Malware/S0556 - Pay2Key|Pay2Key]] (ransomware)
- Tools:
  - [[30_CIPHER/05_Malware/S0508 - ngrok|ngrok]] (tunneling/proxying)
  - [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec]] (remote execution / lateral movement)

## 8. Infrastructure Patterns
Observed/derived from ATT&CK examples:
- **Cloud-hosted C2:** AWS referenced as hosting C2 ([[20_Entities/07_TTPs/T1102 - Web Service|T1102 - Web Service]]).
- **Reverse proxy/tunnel chains:** use of proxy and tunneling patterns (and ngrok as a mapped tool) to bridge C2 to internal services.
- **Server-side persistence:** web shell placement/usage on compromised hosts.

## 9. Campaign History
ATT&CK does not define a dedicated campaign ID for G0117 on the group page, but does document notable activity via references:
- **Fox Kitten campaign reporting (ClearSky):** exploitation-led access and sustained operations (2020).
- **Pay2Key activity:** ATT&CK states Pay2Key has been used by Fox Kitten since at least **July 2020**, including campaigns against **Israeli companies** (see Pay2Key software record).

## 10. Known Indicators
ATT&CK provides behaviors and software mapping rather than durable IOCs. Prioritize behavioral hunting:
- **Web shell telemetry:** anomalous server-side script creation/modification; unusual child processes from web server workers ([[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]]).
- **Tunneling/proxying:** outbound connections consistent with tunneling (ngrok-like patterns), unexpected long-lived connections, and reverse proxy artifacts ([[20_Entities/07_TTPs/T1572 - Protocol Tunneling|T1572 - Protocol Tunneling]], [[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]).
- **Remote access misuse:** RDP brute force signals and subsequent successful logons; lateral SMB admin share access ([[20_Entities/07_TTPs/T1110 - Brute Force|T1110 - Brute Force]], [[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]).
- **Credential store access:** KeePass database access patterns and scripts touching credential material ([[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]]).

## 11. Defensive Recommendations
- **External perimeter hardening (priority 1):**
  - Aggressively patch/mitigate public-facing apps and remote services; enforce MFA and conditional access for remote entry points ([[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]], [[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]).
  - Rate-limit and alert on RDP brute force and password spraying patterns ([[20_Entities/07_TTPs/T1110 - Brute Force|T1110 - Brute Force]]).
- **Server and identity detections (priority 1–2):**
  - Web server integrity monitoring + EDR detections for web shell behaviors; correlate with new scheduled tasks and remote tooling execution ([[20_Entities/07_TTPs/T1505.003 - Web Shell|T1505.003 - Web Shell]], [[20_Entities/07_TTPs/T1053.005 - Scheduled Task|T1053.005 - Scheduled Task]]).
  - Alert on administrative share access from non-admin workstations; constrain lateral SMB where possible ([[20_Entities/07_TTPs/T1021.002 - SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]).
- **Egress + tunneling controls (priority 2):**
  - Detect/deny unauthorized tunneling and reverse proxy tooling; monitor for unusual long-lived outbound sessions and “relay” hosts ([[20_Entities/07_TTPs/T1572 - Protocol Tunneling|T1572 - Protocol Tunneling]], [[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]).
- **Credential hygiene (priority 2):**
  - Audit password manager access and file-based credential storage; enforce strong secret management and rotation ([[20_Entities/07_TTPs/T1555.005 - Password Managers|T1555.005 - Password Managers]], [[20_Entities/07_TTPs/T1552.001 - Credentials In Files|T1552.001 - Credentials In Files]]).

## 12. Analyst Notes
- Fox Kitten clustering includes multiple names; keep a **crosswalk** between aliases and your internal case labeling.
- Incident scoping pivots: **external access logs → web shell discovery → proxy/tunnel artifacts → credential theft → lateral remote services**.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0117/
- ClearSky report (PDF): https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-Kitten-Campaign.pdf
- CrowdStrike: https://www.crowdstrike.com/en-us/blog/who-is-pioneer-kitten/
- MITRE Pay2Key (S0556): https://attack.mitre.org/software/S0556/

## 14. References
- MITRE ATT&CK. (n.d.). *Fox Kitten (G0117).* https://attack.mitre.org/groups/G0117/
- ClearSky. (2020, February 16). *Fox Kitten – Widespread Iranian Espionage-Offensive Campaign.* https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-Kitten-Campaign.pdf
- CrowdStrike. (2020, August 31). *Who Is PIONEER KITTEN?* https://www.crowdstrike.com/en-us/blog/who-is-pioneer-kitten/
- MITRE ATT&CK. (n.d.). *Pay2Key (S0556).* https://attack.mitre.org/software/S0556/

## 15. Notes
- Populate the **Known Indicators** section with validated, time-scoped IOCs when available (domains, IPs, hashes, web shell paths).
- Consider adding internal detection links (Sigma/KQL/Splunk) aligned to: web shell execution chains, scheduled task creation, tunneling signals, and remote admin share activity.
