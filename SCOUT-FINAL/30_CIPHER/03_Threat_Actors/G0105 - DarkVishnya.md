---
entity_type: threat_actor
actor_name: "DarkVishnya"
common_name: "DarkVishnya"
actor_id: "G0105"
actor_type: "Cybercrime (financially motivated)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "High"
first_seen: "2017-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Financial Gain"]
objectives: ["Compromise financial institutions","Credential theft and internal movement for monetization"]
victimology_summary: "Financially motivated actor targeting financial institutions in Eastern Europe. Reported activity in 2017–2018 included attacks against at least 8 banks, including tradecraft involving physical network access, credential acquisition (including sniffing and brute force), and lateral movement via remote administration tooling."
target_sectors: ["Financial Services"]
target_regions: ["Eastern Europe"]
related_groups: []
malware: []
tools: ["PsExec","Winexe","Impacket","DameWare"]
infrastructure: ["Physical access implants/devices to join local networks","Non-standard ports used for listeners/C2 as reported"]
ttps:
  - "[[20_Entities/07_TTPs/T1200 - Hardware Additions]]"
  - "[[20_Entities/07_TTPs/T1110 - Brute Force]]"
  - "[[20_Entities/07_TTPs/T1040 - Network Sniffing]]"
  - "[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1135 - Network Share Discovery]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]"
  - "[[20_Entities/07_TTPs/T1571 - Non-Standard Port]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]"
  - "[[20_Entities/07_TTPs/T1219 - Remote Access Tools]]"
notable_claims: ["Used physical device additions (e.g., Bash Bunny/Raspberry Pi) to gain local network access (per ATT&CK-referenced reporting)."]
intel_sources:
  - "MITRE ATT&CK - G0105 DarkVishnya - https://attack.mitre.org/groups/G0105/"
  - "Kaspersky Securelist reporting referenced by ATT&CK - https://securelist.com/"
tags: ["scout","threat-actor","mitre-g0105","cybercrime","financial","eastern-europe"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
DarkVishnya (G0105) is a financially motivated threat actor targeting **financial institutions in Eastern Europe**, with documented activity during **2017–2018**. The actor’s reported tradecraft includes **physical network access**, credential capture via **sniffing** and **brute force**, and lateral movement using well-known remote administration tools.

## 2. Attribution & Profile
- **Type:** Cybercrime / financially motivated
- **Confidence:** High for victimology and tooling as ATT&CK cites primary reporting
- **Operational hallmark:** physical device introduction to internal networks (not typical for many purely remote campaigns)

## 3. Targeting & Victimology
- **Primary victims:** banks and financial institutions in Eastern Europe
- **Operational goals:** access acquisition and monetization enabled by credential capture and internal movement

## 4. Known Malware, Tools & Infrastructure
**Tools**
- PsExec, Winexe (explicitly listed on ATT&CK group page)
- Impacket and DameWare (noted in group technique narrative)

**Infrastructure**
- Physical access devices enabling internal network access aligned with [[20_Entities/07_TTPs/T1200 - Hardware Additions]]
- Listener/C2 usage on non-standard ports aligned with [[20_Entities/07_TTPs/T1571 - Non-Standard Port]]

## 5. Tradecraft Overview
- **Access enablement:** direct connection to local networks using hardware implants/devices
- **Credential acquisition:** brute force + sniffing to obtain login data ([[20_Entities/07_TTPs/T1110 - Brute Force]], [[20_Entities/07_TTPs/T1040 - Network Sniffing]])
- **Internal movement:** remote tooling and services to deploy loaders and execute payloads ([[20_Entities/07_TTPs/T1219 - Remote Access Tools]], [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]])

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1200 - Hardware Additions]]
- [[20_Entities/07_TTPs/T1110 - Brute Force]]
- [[20_Entities/07_TTPs/T1040 - Network Sniffing]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1135 - Network Share Discovery]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
- [[20_Entities/07_TTPs/T1571 - Non-Standard Port]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1219 - Remote Access Tools]]

## 7. Detection Opportunities
1. **Physical access indicators**
   - New/unknown devices on switches, unexpected DHCP leases, rogue Wi-Fi/ethernet adapters, or unusual USB network interfaces.
2. **Credential capture signals**
   - Unexplained packet capture activity, promiscuous-mode indicators where detectable, and abnormal auth failures (brute force).
3. **Lateral movement tooling**
   - PsExec/Winexe service creation and execution artifacts; remote service control operations; admin share use.
4. **Non-standard port listeners**
   - New listening services on uncommon ports; correlate to process ancestry and recent admin activity.

## 8. Response & Mitigation Guidance
- Tighten physical security and network access controls (NAC/802.1X where feasible).
- Enforce strong password policies, MFA where possible, and lockout thresholds to reduce brute-force success.
- Restrict and monitor remote admin tooling; block where not required; enforce privileged access workstations for admin actions.

## 9. Hunting Ideas
- Hunt for endpoints or network segments with unexpected new devices and short-lived connections.
- Identify PsExec-like execution patterns (service install + remote execution) around times of suspicious authentication activity.
- Review firewall logs for new inbound/outbound listeners on uncommon ports tied to internal endpoints.

## 10. Associated Malware
- None explicitly listed on the ATT&CK group page for G0105 (focus is on tradecraft and tooling).

## 11. Associated Tools
- PsExec
- Winexe
- Impacket
- DameWare

## 12. Analyst Notes
- **High-signal anchor:** physical device introduction to corporate networks + immediate discovery/scanning + credential acquisition.
- **Operational caution:** incident response should include physical inspection of affected areas, not only digital forensics.

## 13. Further Reading / External Resources
- MITRE Group: https://attack.mitre.org/groups/G0105/
- Kaspersky report referenced by ATT&CK: https://securelist.com/

## 14. References
- MITRE ATT&CK. (2025). *DarkVishnya (Group G0105).* https://attack.mitre.org/groups/G0105/
- Golovanov, S. (2018, December 6). *DarkVishnya: Banks attacked through direct connection to local network.* Kaspersky Securelist. https://securelist.com/
