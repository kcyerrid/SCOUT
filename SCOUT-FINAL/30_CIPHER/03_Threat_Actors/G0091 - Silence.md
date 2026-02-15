---
entity_type: threat_actor
actor_name: "Silence"
common_name: "Silence"
actor_id: "G0091"
actor_type: "Cybercrime (financially motivated)"
aliases:
  - "Whisper Spider"
country_of_origin: "Unknown"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2016-06-01"
last_seen: ""
status: "Active"

motivations:
  - "Financial gain"
objectives:
  - "Compromise banking infrastructure (banking systems, ATMs, card processing)"
victimology_summary: "Financially motivated threat actor targeting financial institutions; primary targets reported across Russia, Ukraine, Belarus, Azerbaijan, Poland, and Kazakhstan."
target_sectors:
  - "Financial Services"
target_regions:
  - "Russia"
  - "Ukraine"
  - "Belarus"
  - "Azerbaijan"
  - "Poland"
  - "Kazakhstan"

related_groups: []

malware: []
tools:
  - "[[30_CIPHER/05_Malware/S0363 - Empire|Empire]]"
  - "[[30_CIPHER/05_Malware/S0195 - SDelete|SDelete]]"
  - "[[30_CIPHER/05_Malware/S0191 - Winexe|Winexe]]"

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment|T1566.001]]"
  - "[[20_Entities/07_TTPs/T1218.001 - Compiled HTML File|T1218.001]]"
  - "[[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001]]"
  - "[[20_Entities/07_TTPs/T1072 - Software Deployment Tools|T1072]]"
  - "[[20_Entities/07_TTPs/T1113 - Screen Capture|T1113]]"
  - "[[20_Entities/07_TTPs/T1055 - Process Injection|T1055]]"
  - "[[20_Entities/07_TTPs/T1547.001 - Registry Run Keys - Startup Folder|T1547.001]]"

notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0091/"
  - "https://securelist.com/the-silence/83009/"
tags:
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0091"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Silence (G0091) is a financially motivated intrusion set focused on **financial institutions** and downstream banking infrastructure (banking systems, ATMs, card processing), with activity observed since at least **2016-06** and targeting reported across Eastern Europe and Central Asia.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0091
- **Associated name/cluster:** Whisper Spider
- **Confidence:** Medium (public reporting and ATT&CK mapping are strong; sponsorship/origin not asserted in ATT&CK summary).

## 3. Motivations & Objectives
- **Motivation:** Financial gain.
- **Objectives:** Compromise banking environments and enable fraud via access to banking systems and operational technology around ATMs/card processing.

## 4. Targeting Profile
- **Primary sectors:** Financial services (banks, payment processing).
- **Primary regions reported:** Russia, Ukraine, Belarus, Azerbaijan, Poland, Kazakhstan.
- **Operational focus:** Enterprise endpoints and operator workstations used by financial staff (including remote administration to ATMs).

## 5. Tradecraft Overview
Commonly reported behaviors include:
- **Initial access** via spearphishing attachments (DOCX/CHM/LNK/ZIP).
- **Execution** via scripting and LOLBAS-adjacent paths (PowerShell, cmd).
- **Persistence** via Run keys/Startup folder.
- **Credential access** targeting LSASS memory (often via Mimikatz-derived tooling).
- **Lateral movement** via RDP and remote service tooling.
- **Collection/monitoring** via screen and video capture to observe employee workflows.
- **Defense evasion** via artifact deletion and naming masquerade (e.g., naming a backdoor “WINWORD.exe” reported in ATT&CK technique examples).

## 6. MITRE ATT&CK Mapping (Key TTPs)
- [[20_Entities/07_TTPs/T1566.001 - Spearphishing Attachment|T1566.001]] — Malicious attachments used to entice execution.
- [[20_Entities/07_TTPs/T1218.001 - Compiled HTML File|T1218.001]] — Weaponized CHM delivery path.
- [[20_Entities/07_TTPs/T1547.001 - Registry Run Keys - Startup Folder|T1547.001]] — Persistence via Run keys/Startup folder.
- [[20_Entities/07_TTPs/T1003.001 - LSASS Memory|T1003.001]] — Credential dumping from LSASS.
- [[20_Entities/07_TTPs/T1021.001 - Remote Desktop Protocol|T1021.001]] — Lateral movement via RDP.
- [[20_Entities/07_TTPs/T1072 - Software Deployment Tools|T1072]] — Use of admin/remote control tooling (e.g., RAdmin) for control and movement.
- [[20_Entities/07_TTPs/T1113 - Screen Capture|T1113]] — Interactive monitoring.
- [[20_Entities/07_TTPs/T1055 - Process Injection|T1055]] — Injection for stealth/execution.

## 7. Malware & Tools Used
- Tools (ATT&CK Software mappings):
  - [[30_CIPHER/05_Malware/S0363 - Empire|Empire]]
  - [[30_CIPHER/05_Malware/S0195 - SDelete|SDelete]]
  - [[30_CIPHER/05_Malware/S0191 - Winexe|Winexe]]
- Note: ATT&CK technique examples also reference modified public tools (e.g., PsExec) and Mimikatz-derived credential dumping utilities.

## 8. Infrastructure Patterns
- Common patterns aligned to cybercrime operations:
  - Staging infrastructure for payload download (HTTP-based delivery observed in ATT&CK examples).
  - Use of non-standard ports for client-server communications (per ATT&CK technique examples).

## 9. Campaign History
- ATT&CK notes activity first seen **2016-06** with continued reporting in subsequent years focused on financial institutions.

## 10. Known Indicators
- Maintain case-specific IOCs separately. Prioritize:
  - CHM/LNK attachment artifacts and spawning chains (e.g., Office/Explorer → scripting host/PowerShell).
  - Persistence artifacts: Run keys/Startup folder additions.
  - RDP lateral movement with anomalous source hosts and timing.

## 11. Defensive Recommendations
- Email security: harden against attachment-based initial access; block/contain CHM and risky container formats.
- Endpoint telemetry: enable detailed PowerShell logging; monitor cmd/PowerShell from Office/Explorer attachment opens.
- Credential protection: LSASS protection (e.g., PPL where feasible), limit credential exposure, detect dumping tools.
- Remote admin controls: restrict RDP, require MFA, monitor RDP tooling and RAdmin usage, segment ATM management networks.
- Behavioral detections: detect screen/video capture tooling where possible and anomalous API usage.

## 12. Analyst Notes
- Silence is highly defender-relevant due to **direct monetization** and **high-signal behaviors** (CHM weaponization, credential dumping, remote admin to ATM environments).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0091/
- Kaspersky Securelist (Silence overview): https://securelist.com/the-silence/83009/

## 14. References
- MITRE ATT&CK. (n.d.). *Silence (G0091).* https://attack.mitre.org/groups/G0091/
- GReAT. (2017, November 1). *Silence – a new Trojan attacking financial organizations.* Kaspersky Securelist. https://securelist.com/the-silence/83009/
