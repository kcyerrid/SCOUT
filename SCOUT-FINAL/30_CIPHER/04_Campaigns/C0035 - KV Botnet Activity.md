---
entity_type: campaign

campaign_name: "KV Botnet Activity"
campaign_id: "C0035"
aliases:
  - "KV-Botnet"
status: "disrupted"
risk_level: "high"

first_seen: "2022-10"
last_seen: "2024-01"

attribution:
  associated_threat_actors:
    - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon (G1017)]]"
  suspected_threat_actors: []
  attribution_confidence: "high"
  attribution_notes: "MITRE associates KV Botnet Activity with Volt Typhoon; public reporting notes disruption by U.S. law enforcement in early 2024."

targets:
  regions:
    - "United States"
    - "Guam"
  sectors:
    - "Critical Infrastructure (multiple)"
    - "Energy"
    - "Telecommunications"
  technologies:
    - "SOHO routers / edge devices (Cisco, NETGEAR, DrayTek; end-of-life emphasized)"
    - "Linux-based embedded devices"
    - "Botnet C2 infrastructure (VPS control nodes)"

initial_access_vectors:
  - "Exploitation/compromise of end-of-life SOHO network devices"

key_ttp_themes:
  - "Botnet construction on compromised network devices"
  - "Obfuscation of operator-to-victim connectivity (relay chain)"
  - "Defense evasion via artifact hiding and security tool removal"
  - "In-memory operation and file deletion"

associated_malware: []
malware_notes: "KV Botnet is referenced as malware in reporting; MITRE campaign entry does not enumerate a separate ATT&CK software ID for KV Botnet on the campaign page."

associated_ttps:
  - "T1583.003 - Virtual Private Server"
  - "T1059.004 - Unix Shell"
  - "T1584.008 - Network Devices"
  - "T1573 - Encrypted Channel"
  - "T1546 - Event Triggered Execution"
  - "T1083 - File and Directory Discovery"
  - "T1222.002 - Linux and Mac File and Directory Permissions Modification"
  - "T1564.013 - Bind Mounts"
  - "T1562.001 - Disable or Modify Tools"
  - "T1070.004 - File Deletion"
  - "T1105 - Ingress Tool Transfer"
  - "T1036 - Masquerading"
  - "T1036.004 - Masquerade Task or Service"
  - "T1095 - Non-Application Layer Protocol"
  - "T1571 - Non-Standard Port"
  - "T1057 - Process Discovery"
  - "T1055.009 - Proc Memory"
  - "T1518.001 - Security Software Discovery"
  - "T1082 - System Information Discovery"
  - "T1016 - System Network Configuration Discovery"

infrastructure_patterns:
  - "Use of VPS control systems for botnet management"
  - "Use of compromised SOHO devices as intermediaries/relays"
  - "Overlap with 'JDY cluster' botnet activity per reporting"

tlp_classification: "TLP:CLEAR"
intel_sources:
  - "https://attack.mitre.org/campaigns/C0035/"
  - "https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/"
  - "https://www.justice.gov/archives/opa/pr/us-government-disrupts-botnet-peoples-republic-china-used-conceal-hacking-critical"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a"
  - "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060b"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# KV Botnet Activity (C0035)

## 1. Executive Summary
**KV Botnet Activity (C0035)** describes the compromise of primarily **end-of-life SOHO network devices** to build a botnet used by **[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon (G1017)]]** as an **operational relay layer** to obfuscate connectivity to victims, including critical infrastructure entities and organizations connected to **Guam**. Public reporting indicates the botnet was **disrupted in early 2024** by U.S. law enforcement.

## 2. Campaign Overview
- **Timeframe:** 2022-10 to 2024-01  
- **Primary purpose:** relay/obfuscation infrastructure supporting downstream operations.  
- **Key behaviors:** scripts for installation, in-memory execution, bind mounts, security tool disabling, and artifact deletion.

## 3. Linked Entities
### Threat Actor
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon (G1017)]]

### Malware / Software
- KV Botnet (no dedicated ATT&CK software ID enumerated on the campaign page)

## 4. Timeline of Campaign Activity (Chronos)
```chronos
- [2022-10] First observed activity timeframe (per MITRE entry).
- [2023-12-13] Public technical investigation published describing KV-Botnet and overlap with JDY cluster (reporting date).
- [2024-01-31] U.S. government announces disruption of KV botnet used to conceal critical infrastructure hacking (reporting date).
- [2024-02-07] Government advisory describes PRC state-sponsored actors using KV Botnet on SOHO devices (reporting date).
- [2024-01] Last observed timeframe (per MITRE entry).
```

## 5. Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2022-10 | First observed activity timeframe (per MITRE entry) |
| 2023-12-13 | Technical investigation published on KV-Botnet and JDY overlap |
| 2024-01-31 | U.S. government announces disruption of KV botnet |
| 2024-02-07 | Government advisory on KV Botnet use in PRC operations |
| 2024-01 | Last observed timeframe (per MITRE entry) |

## 6. MITRE ATT&CK Alignment (Observed TTPs)
- [[T1584.008 - Network Devices]]
- [[T1059.004 - Unix Shell]]
- [[T1564.013 - Bind Mounts]]
- [[T1070.004 - File Deletion]]
- [[T1562.001 - Disable or Modify Tools]]
- [[T1055.009 - Proc Memory]]
- [[T1036 - Masquerading]]
- [[T1036.004 - Masquerade Task or Service]]

## 7. Defensive Considerations
1. **SOHO/edge device lifecycle:** remove/replace end-of-life routers; enforce patch SLAs and managed configurations.
2. **Network device monitoring:** detect unexpected outbound connections, random high-port listeners, and suspicious process names.
3. **Ingress tool transfer patterns:** watch for scripted downloads (wget/curl/tftp) and unusual toolchains on embedded Linux.
4. **Botnet disruption alignment:** incorporate CISA/LE guidance; hunt for known infrastructure patterns and IoT indicators.

## 8. References (APA)
- Black Lotus Labs. (2023, December 13). *Routers Roasting On An Open Firewall: The KV-Botnet Investigation.* Lumen. https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/  
- CISA. (2024, February 7). *PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure.* https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a  
- U.S. Department of Justice. (2024, January 31). *U.S. Government Disrupts Botnet People’s Republic of China Used to Conceal Hacking of Critical Infrastructure.* https://www.justice.gov/archives/opa/pr/us-government-disrupts-botnet-peoples-republic-china-used-conceal-hacking-critical  
- MITRE ATT&CK. (n.d.). *KV Botnet Activity (C0035).* https://attack.mitre.org/campaigns/C0035/
