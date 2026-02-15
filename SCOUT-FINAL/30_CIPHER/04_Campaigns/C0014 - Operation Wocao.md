---
entity_type: campaign

campaign_name: "Operation Wocao"
campaign_id: "C0014"
aliases: ["Wocao"]

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0116 - APT20|APT20 (G0116)]]"
suspected_actors: []
attribution_confidence: "2-medium"
confidence_notes: "ATT&CK documents Operation Wocao and notes tool/technique overlap with APT20 in industry reporting. Public reporting includes a detailed incident-response report that maps TTPs and tooling."

first_observed: "2017-12"
last_observed: "2019-12"
campaign_status: "concluded"

primary_objectives: ["espionage"]
secondary_objectives: ["credential_access", "collection", "exfiltration"]

target_sectors: ["government", "managed_service_providers", "aviation", "construction", "energy", "finance", "healthcare", "insurance", "software_development", "transportation"]
target_regions: ["Brazil", "China", "France", "Germany", "Italy", "Mexico", "Portugal", "Spain", "United Kingdom", "United States"]
target_technologies: ["Windows", "VPN", "public_facing_apps", "Active_Directory"]

initial_access_vectors: ["exploit_public_facing_app", "valid_accounts", "webshell"]
key_ttp_themes: ["vpn_persistence", "credential_dumping", "log_clearing", "webshells", "proxy_hops", "rar_staging"]

malware_families:
  - "[[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound (S0521)]]"
  - "[[30_CIPHER/05_Malware/S0105 - dsquery|dsquery (S0105)]]"
  - "[[30_CIPHER/05_Malware/S0357 - Impacket|Impacket (S0357)]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]"
  - "[[30_CIPHER/05_Malware/S0104 - netstat|netstat (S0104)]]"
  - "[[30_CIPHER/05_Malware/S0194 - PowerSploit|PowerSploit (S0194)]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]"
  - "[[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]"
  - "[[30_CIPHER/05_Malware/S0645 - Wevtutil|Wevtutil (S0645)]]"

tools_used: []
infrastructure_patterns: ["tor_exit_usage", "bitcoin_purchased_servers", "multi_hop_proxy"]
notable_victims: []
related_incidents: []

associated_ttps:
  - "T1190 - Exploit Public-Facing Application"
  - "T1133 - External Remote Services"
  - "T1078 - Valid Accounts"
  - "T1078.002 - Domain Accounts"
  - "T1059.001 - PowerShell"
  - "T1059.003 - Windows Command Shell"
  - "T1059.005 - Visual Basic"
  - "T1059.006 - Python"
  - "T1505.003 - Web Shell"
  - "T1003.001 - LSASS Memory"
  - "T1003.006 - DCSync"
  - "T1070.001 - Clear Windows Event Logs"
  - "T1070.004 - File Deletion"
  - "T1041 - Exfiltration Over C2 Channel"
  - "T1560.001 - Archive via Utility"
  - "T1012 - Query Registry"
  - "T1021.002 - SMB/Windows Admin Shares"
  - "T1090.003 - Multi-hop Proxy"

risk_level: "high"
impact_assessment: "Global espionage campaign with credential theft, VPN persistence, webshell use, log clearing, and data exfiltration; high operational impact potential especially in MSP environments."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0014/"
  - "https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf"
  - "https://attack.mitre.org/software/S0002/"
  - "https://attack.mitre.org/software/S0357/"
  - "https://attack.mitre.org/software/S0521/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
**Operation Wocao (C0014)** is a cyber espionage campaign documented in ATT&CK and detailed extensively in public incident-response reporting. Reporting highlights compromise of government entities and managed service providers (MSPs), credential theft, VPN-based persistence, webshell usage, and systematic trace removal.

---

## Attribution Assessment
Industry reporting cites overlap with **APT20**, reflected here as:
- [[30_CIPHER/03_Threat_Actors/G0116 - APT20|APT20 (G0116)]]

---

## Malware & Tooling (ATT&CK Software)
- [[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound (S0521)]]
- [[30_CIPHER/05_Malware/S0357 - Impacket|Impacket (S0357)]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]
- [[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]
- [[30_CIPHER/05_Malware/S0645 - Wevtutil|Wevtutil (S0645)]]
- [[30_CIPHER/05_Malware/S0194 - PowerSploit|PowerSploit (S0194)]]
- [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]
- [[30_CIPHER/05_Malware/S0105 - dsquery|dsquery (S0105)]]
- [[30_CIPHER/05_Malware/S0104 - netstat|netstat (S0104)]]

---

## MITRE ATT&CK Alignment (Selected)
- [[T1190 - Exploit Public-Facing Application]]
- [[T1133 - External Remote Services]]
- [[T1078 - Valid Accounts]]
- [[T1059.001 - PowerShell]]
- [[T1505.003 - Web Shell]]
- [[T1003.001 - LSASS Memory]]
- [[T1003.006 - DCSync]]
- [[T1070.001 - Clear Windows Event Logs]]
- [[T1560.001 - Archive via Utility]]
- [[T1041 - Exfiltration Over C2 Channel]]

---

## Timeline of Campaign Activity

```chronos
- [2017-12]: Earliest reported activity window (month-level).
- [2019-12]: Latest reported activity window (month-level).
- [2019-12-19]: Detailed public report on Operation Wocao published (Fox-IT).
```

| Date | Event |
|---|---|
| 2017-12 | Earliest reported activity window (month-level). |
| 2019-12 | Latest reported activity window (month-level). |
| 2019-12-19 | Detailed public report published describing tooling and TTPs. |

---

## Defensive Considerations
- Prioritize MSP hardening, VPN telemetry monitoring, and privileged access governance.
- Hunt for log clearing patterns (wevtutil), suspicious scheduled tasks, and credential dump artifacts.
- Monitor PowerShell + Impacket lateral movement patterns and abnormal SMB admin share usage.
- Enforce segmentation and protect password manager stores and AD infrastructure.

---

## Analyst Notes
This campaign has unusually rich public documentation. If desired, we can mirror **all** ATT&CK techniques from the MITRE campaign page into `associated_ttps` (expanded “T####(.###) - Name” format) for complete fidelity.

---

## References
- MITRE ATT&CK. (n.d.). *Operation Wocao (C0014)*. https://attack.mitre.org/campaigns/C0014/  
- Dantzig, M. v., & Schamper, E. (2019, December 19). *Operation Wocao: Shining a light on one of China’s hidden hacking groups*. https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf  
- MITRE ATT&CK. (n.d.). *Mimikatz (S0002)*. https://attack.mitre.org/software/S0002/  
- MITRE ATT&CK. (n.d.). *Impacket (S0357)*. https://attack.mitre.org/software/S0357/  
- MITRE ATT&CK. (n.d.). *BloodHound (S0521)*. https://attack.mitre.org/software/S0521/  
