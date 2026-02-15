---
entity_type: threat_actor
actor_name: "GOLD SOUTHFIELD"
common_name: "GOLD SOUTHFIELD"
actor_id: "G0115"
actor_type: "Cybercrime (ransomware operator / affiliate ecosystem)"
aliases: ["Pinchy Spider"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "3-high"
first_seen: "2019-04-01"
last_seen: ""
status: "Unknown"
motivations: ["Financial Gain"]
objectives: ["Ransomware deployment and extortion using REvil/Sodinokibi operations and access enablement via RDP/RMM/supply chain compromise"]
victimology_summary: "GOLD SOUTHFIELD (also tracked as Pinchy Spider) is associated with REvil/Sodinokibi ransomware operations and related access methods including exploitation of public-facing applications, abuse of external remote services, and use of remote monitoring and management tooling for deployment."
target_sectors: []
target_regions: ["Global (reported)"]
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/S0496 - REvil|REvil (S0496)]]"
tools:
  - "[[30_CIPHER/05_Malware/S0591 - ConnectWise|ConnectWise (S0591)]]"
infrastructure: ["[[RMM Abuse]]","[[External Remote Services]]","[[Supply Chain Compromise]]"]
ttps:
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1133 - External Remote Services]]"
  - "[[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1566 - Phishing]]"
  - "[[20_Entities/07_TTPs/T1219 - Remote Access Tools]]"
  - "[[20_Entities/07_TTPs/T1113 - Screen Capture]]"
  - "[[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]"
  - "[[20_Entities/07_TTPs/T1199 - Trusted Relationship]]"
notable_claims:
  - "Public reporting connects this cluster to REvil/Sodinokibi operations and evolving ransomware ecosystem behavior."
intel_sources:
  - "https://attack.mitre.org/groups/G0115/"
  - "https://www.sophos.com/en-us/research/revil-sodinokibi-ransomware"
  - "https://www.secureworks.com/blog/revil-the-gandcrab-connection"
  - "https://www.crowdstrike.com/blog/the-evolution-of-revil-ransomware-and-pinchy-spider/"
tags: ["scout","threat-actor","mitre-g0115","cybercrime","ransomware","revil","pinchy-spider"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
GOLD SOUTHFIELD (G0115), also tracked as **Pinchy Spider**, is a cybercrime cluster associated with **REvil/Sodinokibi** ransomware operations and access enablement through a mix of **public-facing exploitation**, **RDP/RMM abuse**, **phishing**, and **trusted relationship / supply chain compromise** patterns.

## 2. Attribution & Profile
- **Type:** Cybercrime / ransomware ecosystem
- **Aliases:** Pinchy Spider
- **Attribution Confidence:** 3-high (strong multi-source alignment on ransomware association)

## 3. Targeting & Victimology
- Victimology is broadly described as opportunistic/high-value targets in public reporting; track exact sectors/regions per case.

## 4. Known Malware, Tools & Infrastructure
**Malware**
- [[30_CIPHER/05_Malware/S0496 - REvil|REvil (S0496)]]

**Tools**
- [[30_CIPHER/05_Malware/S0591 - ConnectWise|ConnectWise (S0591)]]

**Operational patterns**
- [[RMM Abuse]] for deployment and remote control
- Abuse of [[External Remote Services]] (including RDP exposure)
- [[Supply Chain Compromise]] and [[Trusted Relationship]] intrusion paths (MSP/customer propagation models)

## 5. Tradecraft Overview
- **Initial access:** exploit public-facing apps, phishing, external remote services, trusted relationship compromise
- **Execution:** PowerShell + command obfuscation
- **Deployment:** RMM tooling to stage and execute ransomware
- **Impact:** encryption/extortion via REvil operations

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]
- [[20_Entities/07_TTPs/T1566 - Phishing]]
- [[20_Entities/07_TTPs/T1219 - Remote Access Tools]]
- [[20_Entities/07_TTPs/T1113 - Screen Capture]]
- [[20_Entities/07_TTPs/T1195.002 - Supply Chain Compromise: Compromise Software Supply Chain]]
- [[20_Entities/07_TTPs/T1199 - Trusted Relationship]]

## 7. Detection Opportunities
1. **RMM abuse (ConnectWise)**
   - Detect new/rare RMM installs; anomalous ConnectWise usage on servers/endpoints without baseline.
2. **PowerShell + obfuscation**
   - Base64/encoded command lines and suspicious parent processes launching PowerShell.
3. **External remote services exposure**
   - Internet-facing RDP/RMM telemetry, unusual logons, and rapid post-logon tooling.

## 8. Response & Mitigation Guidance
- Reduce exposure of RDP and remote admin services; enforce MFA and conditional access.
- Lock down RMM deployment: allowlist, signed installers only, and administrative approvals.
- Ransomware readiness: immutable backups, restore testing, segmentation, and rapid containment playbooks.

## 9. Hunting Ideas
- Hunt for ConnectWise sessions that perform screen capture or push executables across multiple hosts.
- Identify spikes in PowerShell usage across server fleet, especially with encoded commands.
- Look for supply-chain indicators: unexpected software installer tampering signals and unusual update channels.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/S0496 - REvil|REvil (S0496)]]

## 11. Associated Tools
- [[30_CIPHER/05_Malware/S0591 - ConnectWise|ConnectWise (S0591)]]

## 12. Analyst Notes
- REvil has a wide technique surface beyond the group’s core access patterns; keep group-level TTPs scoped to sourced behaviors.
- Completeness: **High** (ATT&CK provides clear technique + software mapping; multiple high-quality sources corroborate).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group G0115: https://attack.mitre.org/groups/G0115/
- Sophos (Secureworks CTU) REvil overview: https://www.sophos.com/en-us/research/revil-sodinokibi-ransomware
- Secureworks/Sophos blog: https://www.secureworks.com/blog/revil-the-gandcrab-connection
- CrowdStrike evolution of Pinchy Spider/REvil: https://www.crowdstrike.com/blog/the-evolution-of-revil-ransomware-and-pinchy-spider/

## 14. References (APA)
- MITRE ATT&CK. (n.d.). *GOLD SOUTHFIELD (G0115).* https://attack.mitre.org/groups/G0115/
- Counter Threat Unit Research Team. (2025, November 27). *REvil/Sodinokibi Ransomware.* Sophos. https://www.sophos.com/en-us/research/revil-sodinokibi-ransomware
- Secureworks. (n.d.). *REvil: The GandCrab Connection.* https://www.secureworks.com/blog/revil-the-gandcrab-connection
- CrowdStrike. (2021, July 6). *The Evolution of PINCHY SPIDER from GandCrab to REvil.* https://www.crowdstrike.com/blog/the-evolution-of-revil-ransomware-and-pinchy-spider/
