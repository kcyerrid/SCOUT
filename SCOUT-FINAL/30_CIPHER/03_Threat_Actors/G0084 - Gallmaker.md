---
entity_type: threat_actor
actor_name: "Gallmaker"
common_name: "Gallmaker"
actor_id: "G0084"
actor_type: "Cyberespionage"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2017-12-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Initial access via phishing","Living-off-the-land execution","Collection and exfiltration preparation"]
victimology_summary: "Cyberespionage group documented in ATT&CK as active since at least December 2017, targeting victims in the Middle East, mainly in defense, military, and government sectors; noted for living-off-the-land approaches."
target_sectors: ["Defense","Military","Government"]
target_regions: ["Middle East"]
related_groups: []
malware: []
tools: ["[[Microsoft Office]]","[[PowerShell]]","[[WinZip]]"]
infrastructure: ["[[Email lure delivery]]"]
ttps: ["[[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]","[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0084 Gallmaker - https://attack.mitre.org/groups/G0084/"]
tags: ["scout","threat-actor","mitre-g0084","gallmaker","middle-east","espionage","living-off-the-land"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
Gallmaker (G0084) is documented in ATT&CK as a Middle East–focused cyberespionage group active since at least December 2017, primarily targeting defense, military, and government sectors. ATT&CK emphasizes tradecraft that minimizes custom malware by leveraging built-in capabilities and document-driven execution, including DDE-based execution attempts and PowerShell-driven payload retrieval.

## 2. Attribution Notes
ATT&CK does not assign a sponsor or nation-state attribution. This note treats sponsorship as unknown and focuses on ATT&CK-described behaviors.

## 3. Motivations & Objectives
- Espionage targeting of sensitive defense/government information
- Initial access via phishing attachments and user-enabled document execution
- Collection preparation via archiving utilities before potential exfiltration

## 4. Targeting Profile
- **Region (ATT&CK):** Middle East
- **Sectors (ATT&CK):** Defense, Military, Government
- **Likely access points:** Email and Office document workflows

## 5. Tradecraft Overview
- **Initial access:** Spearphishing attachments with malicious Office documents.
- **Execution:** DDE-based execution attempts and user-driven enablement flows.
- **Living-off-the-land:** PowerShell used for execution and downloading additional payloads.
- **Preparation for exfiltration:** Archiving via utility (WinZip noted in ATT&CK narrative).
- **Evasion:** Obfuscation of shellcode used during execution.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1560.001 - Archive Collected Data: Archive via Utility]]
- [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]

## 7. Malware & Tools Used
- **Malware:** ATT&CK emphasizes LOTL behavior; no ATT&CK software entries are listed on the group page.
- **Tools / built-ins:**
  - [[PowerShell]] (execution and payload retrieval)
  - [[WinZip]] (archive prior to exfiltration)
  - [[Microsoft Office]] (document-driven lure/execution workflow)

## 8. Infrastructure Patterns
- Email-based lure delivery with Office attachments
- Payload retrieval over standard network channels as part of PowerShell download behavior (per ATT&CK narrative)

## 9. Campaign History
- **2017–present (reported):** Middle East cyberespionage operations described in ATT&CK reporting.

## 10. Known Indicators
No stable public indicators are included. Prefer detections based on Office process lineage, PowerShell download patterns, and DDE-related telemetry.

## 11. Defensive Recommendations
- Disable or restrict Office DDE features where feasible; monitor Office spawning child processes (PowerShell/cmd) and suspicious command-lines.
- Alert on PowerShell with network download behaviors, especially from Office parent processes or shortly after document open events.
- Monitor for utility-based archiving of sensitive directories followed by outbound connections or staging in unusual user-writable paths.

## 12. Analyst Notes
**Confidence:** High for ATT&CK-described techniques; limited breadth on tooling due to minimal ATT&CK software attribution on the group page.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0084/

## 14. References
- MITRE ATT&CK. (2025). *Gallmaker (G0084).* https://attack.mitre.org/groups/G0084/
