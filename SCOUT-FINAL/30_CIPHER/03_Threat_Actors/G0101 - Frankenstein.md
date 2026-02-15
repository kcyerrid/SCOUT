---
entity_type: threat_actor
actor_name: "Frankenstein"
common_name: "Frankenstein"
actor_id: "G0101"
actor_type: "Unattributed (Deprecated ATT&CK Group; replaced by Campaign C0001)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2019-01-01"
last_seen: "2019-04-01"
status: "Deprecated (Converted to Campaign)"
motivations: []
objectives: []
victimology_summary: "ATT&CK previously tracked 'Frankenstein' as a Group (G0101) but later converted it into the Campaign object C0001. The campaign was described as a highly targeted operation in early 2019, relying heavily on open-source tooling (notably Empire) and common tradecraft such as spearphishing attachments, client-side exploitation, command obfuscation, and scheduled task persistence."
target_sectors: []
target_regions: []
related_groups: []
malware: []
tools: ["[[30_CIPHER/05_Malware/Empire]]"]
infrastructure: ["HTTP(S) C2 over web protocols","Encrypted C2 (RC4/AES-CBC as reported)","Scheduled task persistence (WinUpdate)","Remote template retrieval via trojanized documents"]
ttps:
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"
  - "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]"
  - "[[20_Entities/07_TTPs/T1221 - Template Injection]]"
  - "[[20_Entities/07_TTPs/T1127.001 - Trusted Developer Utilities Proxy Execution: MSBuild]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]"
  - "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]"
  - "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]"
  - "[[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]"
  - "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1119 - Automated Collection]]"
  - "[[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]"
  - "[[20_Entities/07_TTPs/T1005 - Data from Local System]]"
  - "[[20_Entities/07_TTPs/T1057 - Process Discovery]]"
  - "[[20_Entities/07_TTPs/T1518.001 - Software Discovery: Security Software Discovery]]"
  - "[[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks]]"
  - "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"
  - "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery]]"
  - "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]"
notable_claims: ["ATT&CK Group G0101 was deprecated and replaced by Campaign C0001."]
intel_sources:
  - "MITRE ATT&CK (Update Note) - October 2022: https://attack.mitre.org/resources/updates/updates-october-2022/"
  - "MITRE ATT&CK (Campaign) - C0001 Frankenstein: https://attack.mitre.org/campaigns/C0001/"
  - "Cisco Talos (Primary reporting referenced by ATT&CK): https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html"
tags: ["scout","threat-actor","mitre-g0101","deprecated","campaign-conversion"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Frankenstein (G0101) is a **deprecated** ATT&CK Group entry that was **converted into Campaign C0001**. The underlying activity describes a highly targeted operation observed in **2019-01 through 2019-04**, emphasizing **open-source tooling (Empire)**, phishing-driven initial access, client-side exploitation, and defense-aware execution gating.

## 2. Attribution & Profile
- **ATT&CK status:** Deprecated Group → replaced by **Campaign C0001**
- **Attribution:** Unattributed; described as moderately sophisticated and highly resourceful actors
- **Confidence:** Low for actor identity; High for campaign tradecraft as documented in sources

## 3. Targeting & Victimology
- **Targeting:** Not consistently attributed to a single sector/region in ATT&CK campaign summary
- **Victimology pattern:** Highly targeted delivery (phishing attachments, trojanized docs with remote templates)

## 4. Known Malware, Tools & Infrastructure
**Tools**
- [[30_CIPHER/05_Malware/Empire]] (open-source post-exploitation framework; referenced by ATT&CK campaign page)

**Infrastructure / C2**
- HTTP GET-based communications aligned with [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- Encrypted C2 streams aligned with [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]

## 5. Tradecraft Overview
- **Initial access:** spearphishing attachments and user execution ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]], [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]])
- **Client-side execution:** exploitation (reported CVE-2017-11882) aligned with [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- **Execution:** PowerShell + cmd with encoded payload staging ([[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]], [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]])
- **Persistence:** scheduled task “WinUpdate” with masquerading ([[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]], [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]])
- **Evasion:** sandbox/VM checks ([[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks]]), command obfuscation ([[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]])

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1221 - Template Injection]]
- [[20_Entities/07_TTPs/T1127.001 - Trusted Developer Utilities Proxy Execution: MSBuild]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1027.010 - Obfuscated Files or Information: Command Obfuscation]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1573.001 - Encrypted Channel: Symmetric Cryptography]]
- [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1119 - Automated Collection]]
- [[20_Entities/07_TTPs/T1020 - Automated Exfiltration]]

## 7. Detection Opportunities
1. **Office exploit + follow-on script staging**
   - Watch for Office spawning `cmd.exe`, `powershell.exe`, or WMI usage shortly after document open.
2. **Encoded/obfuscated PowerShell**
   - Script block logging & AMSI coverage for Base64 decode chains, suspicious stagers, and empire-like tasking patterns.
3. **Suspicious scheduled task creation**
   - Creation of tasks with names resembling Windows update processes (e.g., “WinUpdate”) and odd triggers/paths.
4. **Remote template retrieval**
   - Office template fetches to non-corporate domains or newly registered infrastructure (proxy for [[20_Entities/07_TTPs/T1221 - Template Injection]]).

## 8. Response & Mitigation Guidance
- Contain endpoints showing **Office→script interpreter** chains and scheduled task persistence.
- Re-image or surgically remove persistence (task + dropped stagers), rotate credentials if post-exploitation frameworks suspected.
- Block/alert on outbound C2 patterns (HTTP GET beacons) and investigate encryption-wrapped traffic baselines.

## 9. Hunting Ideas
- Hunt for scheduled task creation events + command lines containing `/Create` and suspicious `/TN` values.
- Hunt for WMI queries in proximity to document execution (possible security tool checks).
- Identify anomalous external template loads from Office processes.

## 10. Associated Malware
- None explicitly listed for this deprecated Group entry (campaign references focus on tooling).

## 11. Associated Tools
- [[30_CIPHER/05_Malware/Empire]]

## 12. Analyst Notes
- **Key SOC signal:** Office-driven initial execution + obfuscated script staging + scheduled task persistence.
- **Deprecation handling:** Treat G0101 as historical; prefer Campaign C0001 for up-to-date ATT&CK object references.

## 13. Further Reading / External Resources
- MITRE Campaign C0001: https://attack.mitre.org/campaigns/C0001/
- MITRE Updates (Oct 2022): https://attack.mitre.org/resources/updates/updates-october-2022/
- Cisco Talos report: https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html

## 14. References
- MITRE ATT&CK. (2025). *Frankenstein (Campaign C0001).* https://attack.mitre.org/campaigns/C0001/
- MITRE ATT&CK. (2022). *Updates – October 2022 (Campaigns replacing Groups, incl. G0101).* https://attack.mitre.org/resources/updates/updates-october-2022/
- Adamitis, D., et al. (2019, June 4). *It’s alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign.* Cisco Talos. https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html
