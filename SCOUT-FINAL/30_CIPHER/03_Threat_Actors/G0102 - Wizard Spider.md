---
entity_type: threat_actor
actor_name: "Wizard Spider"
common_name: "Wizard Spider"
actor_id: "G0102"
actor_type: "Cybercrime (financially motivated)"
aliases: ["UNC1878","TEMP.MixMaster","Grim Spider","FIN12","GOLD BLACKBURN","ITG23","Periwinkle Tempest","DEV-0193"]
country_of_origin: "Russia (reported)"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2016-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Financial Gain"]
objectives: ["Credential theft and access brokerage","Ransomware deployment and extortion operations"]
victimology_summary: "Russia-based financially motivated threat group known for creation/deployment of TrickBot and broader ransomware operations. The group maintains a diverse toolset and has targeted a wide range of organizations (including healthcare)."
target_sectors: ["Multiple (varied)","Healthcare"]
target_regions: ["Global"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/TrickBot]]","[[30_CIPHER/05_Malware/Bazar]]","[[30_CIPHER/05_Malware/Anchor]]","[[30_CIPHER/05_Malware/Emotet]]"]
tools: ["AdFind","BloodHound","Cobalt Strike","BITSAdmin","PsExec"]
infrastructure: ["HTTP-based C2","Name service poisoning / relay opportunities (LLMNR/NBT-NS)","SMB/Windows Admin Shares for lateral movement"]
ttps:
  - "[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]"
  - "[[20_Entities/07_TTPs/T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]"
  - "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"
  - "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]"
  - "[[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]"
  - "[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]"
  - "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"
  - "[[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]"
  - "[[20_Entities/07_TTPs/T1552.006 - Unsecured Credentials: Group Policy Preferences]]"
  - "[[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]"
notable_claims: []
intel_sources:
  - "MITRE ATT&CK - G0102 Wizard Spider - https://attack.mitre.org/groups/G0102/"
  - "CrowdStrike reporting referenced by ATT&CK - https://www.crowdstrike.com/"
  - "CISA advisory referenced by ATT&CK - https://us-cert.cisa.gov/"
tags: ["scout","threat-actor","mitre-g0102","cybercrime","ransomware","trickbot"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Wizard Spider (G0102) is a **Russia-based**, financially motivated threat group best known for **TrickBot** and related ecosystem activity, including **ransomware campaigns** and hands-on-keyboard intrusions. The group’s tradecraft frequently blends commodity infection vectors with enterprise-focused post-exploitation (credential theft, AD discovery, lateral movement, and remote execution).

## 2. Attribution & Profile
- **Type:** Cybercrime / financially motivated
- **Core ecosystem:** [[30_CIPHER/05_Malware/TrickBot]], [[30_CIPHER/05_Malware/Bazar]], [[30_CIPHER/05_Malware/Anchor]]
- **Operational pattern:** Initial foothold → credential access & discovery → lateral movement → impact (often encryption/extortion)

## 3. Targeting & Victimology
- **Victim profile:** Broad, including high-pressure environments such as healthcare (per ATT&CK summary)
- **Geography:** Global/varied
- **Common access paths:** phishing-driven delivery, staged loader frameworks, and subsequent enterprise tooling

## 4. Known Malware, Tools & Infrastructure
**Malware**
- [[30_CIPHER/05_Malware/TrickBot]]
- [[30_CIPHER/05_Malware/Bazar]]
- [[30_CIPHER/05_Malware/Anchor]]
- [[30_CIPHER/05_Malware/Emotet]] (noted as a possible delivered payload in reported intrusion chains)

**Tools (commonly observed in ATT&CK mapping)**
- AdFind, BloodHound, Cobalt Strike, BITSAdmin, PsExec

**Infrastructure / C2**
- HTTP-based communications aligned with [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- Network poisoning/relay opportunities aligned with [[20_Entities/07_TTPs/T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay]]

## 5. Tradecraft Overview
- **Discovery in AD-heavy environments:** domain account/group discovery patterns (e.g., enumerating “Domain Admins”)
- **Credential access + replay:** memory credential theft + pass-the-hash patterns (high signal for post-compromise progression)
- **Remote execution at scale:** service execution + SMB admin shares + WMI for lateral spread
- **Ransomware staging/impact:** tool transfer + lateral execution + encryption

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]
- [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
- [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]
- [[20_Entities/07_TTPs/T1552.006 - Unsecured Credentials: Group Policy Preferences]]
- [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]

## 7. Detection Opportunities
1. **Name service poisoning / relay activity (High Signal)**
   - Monitor LLMNR/NBT-NS queries/responses, SMB relay attempts, and anomalous authentication patterns.
2. **Credential dumping & replay**
   - LSASS access telemetry, suspicious handle requests, and downstream NTLM hash usage anomalies.
3. **AD discovery toolmarks**
   - `AdFind`-like LDAP query patterns, BloodHound collection bursts, `net group` enumeration of privileged groups.
4. **Remote execution waves**
   - Service creation + remote SCM usage, PsExec-like lateral patterns, WMI remote process creation.
5. **Pre-impact staging**
   - Bulk tool transfer, scripted remote execution, disabling defenses, and concurrent encryption activity signals.

## 8. Response & Mitigation Guidance
- Contain affected hosts and isolate lateral movement pathways (SMB/WMI/service control).
- Reset/rotate credentials and invalidate hashes where feasible; prioritize domain admin and service accounts.
- Enforce hardened name-resolution settings (disable LLMNR/NBT-NS where possible) and require SMB signing to reduce relay viability.
- Improve detection for AD discovery bursts and post-exploitation tooling.

## 9. Hunting Ideas
- Hunt for LLMNR/NBT-NS traffic in segments that should not use it; correlate with NTLM auth spikes.
- Identify uncommon binaries executing remote service creation or launching `services.exe`-mediated execution.
- Look for patterns of rapid enumeration + credential access preceding ransomware-impact timelines.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/TrickBot]]
- [[30_CIPHER/05_Malware/Bazar]]
- [[30_CIPHER/05_Malware/Anchor]]
- [[30_CIPHER/05_Malware/Emotet]]

## 11. Associated Tools
- AdFind
- BloodHound
- Cobalt Strike
- BITSAdmin
- PsExec

## 12. Analyst Notes
- **High-signal anchors:** name-service poisoning/relay, credential dumping + replay, AD discovery surges, remote service execution bursts.
- **Operational caution:** the ecosystem evolves; validate malware family names and affiliate relationships per incident.

## 13. Further Reading / External Resources
- MITRE Group: https://attack.mitre.org/groups/G0102/
- ATT&CK Software (examples referenced from the group page): https://attack.mitre.org/software/
- Public reporting portals referenced by ATT&CK: CrowdStrike, CISA, Mandiant, Microsoft

## 14. References
- MITRE ATT&CK. (2025). *Wizard Spider (Group G0102).* https://attack.mitre.org/groups/G0102/
- MITRE ATT&CK. (n.d.). *Anchor (Software S0504).* https://attack.mitre.org/software/S0504/
- MITRE ATT&CK. (n.d.). *Bazar (Software S0534).* https://attack.mitre.org/software/S0534/
- MITRE ATT&CK. (n.d.). *TrickBot (Software).* https://attack.mitre.org/software/
