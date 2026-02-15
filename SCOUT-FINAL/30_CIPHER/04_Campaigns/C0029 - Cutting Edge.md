---
entity_type: campaign

campaign_name: "Cutting Edge"
campaign_id: "C0029"
aliases: []
status: "inactive"
risk_level: "high"

first_seen: "2023-12"
last_seen: "2024-02"

attribution:
  associated_threat_actors: []
  suspected_threat_actors:
    - "UNC5221"
    - "UTA0178"
    - "UNC5325"
  attribution_confidence: "medium"
  attribution_notes: "MITRE describes suspected China-nexus espionage actors; public reporting tracks activity under the listed private-sector clusters."

targets:
  regions:
    - "Global"
    - "United States"
  sectors:
    - "Defense Industrial Base"
    - "Telecommunications"
    - "Financial"
    - "Aerospace"
    - "Technology"
  technologies:
    - "Ivanti Connect Secure (formerly Pulse Secure) VPN appliances"
    - "Windows environments (post-compromise lateral movement)"
    - "Samba/Linux hosts (enumeration and lateral movement)"

initial_access_vectors:
  - "Exploitation of public-facing application (Ivanti Connect Secure) via chained vulnerabilities"

key_ttp_themes:
  - "Edge-device exploitation and persistence"
  - "Web shell deployment on appliances"
  - "Defense evasion via log clearing, timestomping, and binary patching"
  - "Credential access and lateral movement into internal networks"

associated_malware:
  - "[[30_CIPHER/05_Malware/S1115 - WIREFIRE|WIREFIRE (S1115)]]"
  - "[[30_CIPHER/05_Malware/S1117 - GLASSTOKEN|GLASSTOKEN (S1117)]]"
  - "[[30_CIPHER/05_Malware/S1118 - BUSHWALK|BUSHWALK (S1118)]]"
  - "[[30_CIPHER/05_Malware/S1119 - LIGHTWIRE|LIGHTWIRE (S1119)]]"
  - "[[30_CIPHER/05_Malware/S1120 - FRAMESTING|FRAMESTING (S1120)]]"
  - "[[30_CIPHER/05_Malware/S1123 - PITSTOP|PITSTOP (S1123)]]"
  - "[[30_CIPHER/05_Malware/S1114 - ZIPLINE|ZIPLINE (S1114)]]"
  - "[[30_CIPHER/05_Malware/S1116 - WARPWIRE|WARPWIRE (S1116)]]"
  - "[[30_CIPHER/05_Malware/S1121 - LITTLELAMB.WOOLTEA|LITTLELAMB.WOOLTEA (S1121)]]"

tools_used:
  - "[[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec (S0488)]]"
  - "[[30_CIPHER/05_Malware/S0357 - Impacket|Impacket (S0357)]]"

associated_ttps:
  - "T1190 - Exploit Public-Facing Application"
  - "T1595.002 - Vulnerability Scanning"
  - "T1071.004 - DNS"
  - "T1560.001 - Archive via Utility"
  - "T1059 - Command and Scripting Interpreter"
  - "T1059.006 - Python"
  - "T1554 - Compromise Host Software Binary"
  - "T1584.008 - Network Devices"
  - "T1005 - Data from Local System"
  - "T1562.001 - Disable or Modify Tools"
  - "T1070 - Indicator Removal"
  - "T1070.004 - File Deletion"
  - "T1070.006 - Timestomp"
  - "T1105 - Ingress Tool Transfer"
  - "T1056.001 - Keylogging"
  - "T1056.003 - Web Portal Capture"
  - "T1095 - Non-Application Layer Protocol"
  - "T1027.013 - Encrypted/Encoded File"
  - "T1588.002 - Tool"
  - "T1003.001 - LSASS Memory"
  - "T1003.003 - NTDS"
  - "T1055 - Process Injection"
  - "T1572 - Protocol Tunneling"
  - "T1021.001 - Remote Desktop Protocol"
  - "T1021.002 - SMB/Windows Admin Shares"
  - "T1021.004 - SSH"
  - "T1594 - Search Victim-Owned Websites"
  - "T1505.003 - Web Shell"
  - "T1082 - System Information Discovery"
  - "T1205 - Traffic Signaling"
  - "T1078.002 - Domain Accounts"

notable_vulns:
  - "CVE-2023-46805 (Ivanti Connect Secure auth bypass)"
  - "CVE-2024-21887 (Ivanti Connect Secure command injection)"
  - "CVE-2024-21893 (SSRF used in chaining/bypass scenarios)"

infrastructure_patterns:
  - "Use of compromised/out-of-support VPN appliances for C2/proxying"
  - "DNS tunneling and protocol tunneling to blend traffic"

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0029/"
  - "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ivanti-zero-day-exploitation/"
  - "https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/"
  - "https://www.volexity.com/blog/2024/01/15/ivanti-connect-secure-vpn-exploitation-goes-global/"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Cutting Edge (C0029)

## 1. Executive Summary
**Cutting Edge (C0029)** is a suspected China-nexus espionage campaign focused on **exploiting Ivanti Connect Secure VPN appliances** to gain initial access, establish persistence via **web shells**, and pivot into victim internal networks. The campaign is characterized by **edge-device tradecraft**, **defense evasion** (log clearing/timestomping/binary patching), and **credential access + lateral movement** into Windows environments.

## 2. Campaign Overview
- **Timeframe:** 2023-12 to 2024-02  
- **Primary targets:** U.S. defense industrial base and multiple global sectors (telecom, finance, aerospace, technology).  
- **Access pattern:** Exploitation of Ivanti vulnerabilities → web shell/backdoor persistence on appliance → credential capture and pivoting inward.

## 3. Attribution & Confidence
- **Suspected:** China-nexus espionage (public reporting clusters: UNC5221 / UTA0178 / UNC5325)
- **Confidence:** Medium (consistent multi-source reporting; actor naming differs by vendor)

## 4. Linked Entities

### Threat Actors (Associated / Suspected)
- Suspected clusters (no ATT&CK G-ID asserted on the MITRE campaign entry): **UNC5221**, **UTA0178**, **UNC5325**

### Malware / Software (Obsidian Atomic Notes)
- [[30_CIPHER/05_Malware/S1115 - WIREFIRE|WIREFIRE (S1115)]]
- [[30_CIPHER/05_Malware/S1117 - GLASSTOKEN|GLASSTOKEN (S1117)]]
- [[30_CIPHER/05_Malware/S1118 - BUSHWALK|BUSHWALK (S1118)]]
- [[30_CIPHER/05_Malware/S1119 - LIGHTWIRE|LIGHTWIRE (S1119)]]
- [[30_CIPHER/05_Malware/S1120 - FRAMESTING|FRAMESTING (S1120)]]
- [[30_CIPHER/05_Malware/S1123 - PITSTOP|PITSTOP (S1123)]]
- [[30_CIPHER/05_Malware/S1114 - ZIPLINE|ZIPLINE (S1114)]]
- [[30_CIPHER/05_Malware/S1116 - WARPWIRE|WARPWIRE (S1116)]]
- [[30_CIPHER/05_Malware/S1121 - LITTLELAMB.WOOLTEA|LITTLELAMB.WOOLTEA (S1121)]]
- [[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec (S0488)]]
- [[30_CIPHER/05_Malware/S0357 - Impacket|Impacket (S0357)]]

## 5. Timeline of Campaign Activity (Chronos)
```chronos
- [2023-12] Initial exploitation observed in the wild targeting Ivanti Connect Secure VPNs.
- [2024-01-10] Public reporting on active exploitation of Ivanti Connect Secure zero-days (vendor reporting).
- [2024-01-12] Additional campaign reporting describing tactics, malware, and victimology.
- [2024-01-31] Follow-on reporting expands technical findings and persistence patterns.
- [2024-02-27] Additional reporting on exploitation + persistence attempts (campaign “last seen” window).
```

## 6. Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2023-12 | Initial exploitation observed targeting Ivanti Connect Secure VPNs |
| 2024-01-10 | Public reporting on active exploitation of Ivanti zero-days |
| 2024-01-12 | Follow-on technical reporting (malware + victimology) |
| 2024-01-31 | Additional technical findings and persistence patterns |
| 2024-02-27 | Further reporting on exploitation and persistence attempts |

## 7. MITRE ATT&CK Alignment (Observed TTPs)
- [[T1190 - Exploit Public-Facing Application]]
- [[T1595.002 - Vulnerability Scanning]]
- [[T1071.004 - DNS]]
- [[T1560.001 - Archive via Utility]]
- [[T1059 - Command and Scripting Interpreter]]
- [[T1059.006 - Python]]
- [[T1554 - Compromise Host Software Binary]]
- [[T1584.008 - Network Devices]]
- [[T1505.003 - Web Shell]]
- [[T1070 - Indicator Removal]]
- [[T1070.004 - File Deletion]]
- [[T1070.006 - Timestomp]]
- [[T1003.001 - LSASS Memory]]
- [[T1003.003 - NTDS]]
- [[T1021.001 - Remote Desktop Protocol]]
- [[T1021.002 - SMB/Windows Admin Shares]]
- [[T1021.004 - SSH]]

## 8. Defensive Considerations
1. **Edge-device hardening:** inventory/patch VPN appliances; remove EoL devices; enforce config baselines.
2. **Appliance integrity monitoring:** detect unexpected binaries, modified CGI components, and new web content.
3. **Credential protection:** monitor for credential capture on VPN portals; enforce MFA resistant to token replay where possible.
4. **Network telemetry:** look for DNS tunneling, unusual outbound from VPN appliances, and lateral movement using VPN accounts.

## 9. Analyst Notes
This campaign highlights the persistent risk of **edge-device compromise** where post-exploitation may be difficult to detect if appliances lack robust EDR/telemetry. Treat VPN appliances as high-risk assets and consider **out-of-band logging** and **integrity checks** as mandatory.

## 10. References (APA)
- Lin, M., et al. (2024, February 27). *Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts.* Mandiant. https://www.mandiant.com/resources/blog/cutting-edge-part-3-ivanti-connect-secure  
- Lin, M., et al. (2024, January 31). *Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation.* Mandiant. https://cloud.google.com/blog/topics/threat-intelligence/investigating-ivanti-zero-day-exploitation/  
- McLellan, T., et al. (2024, January 12). *Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation.* Mandiant. https://www.mandiant.com/resources/blog/cutting-edge-ivanti-0day  
- Meltzer, M., et al. (2024, January 10). *Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN.* Volexity. https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/  
- Gurkok, C., et al. (2024, January 15). *Ivanti Connect Secure VPN Exploitation Goes Global.* Volexity. https://www.volexity.com/blog/2024/01/15/ivanti-connect-secure-vpn-exploitation-goes-global/  
- MITRE ATT&CK. (n.d.). *Cutting Edge (C0029).* https://attack.mitre.org/campaigns/C0029/
