---
entity_type: threat_actor
actor_name: "Sharpshooter"
common_name: "Sharpshooter"
actor_id: "G0104"
actor_type: "Cyber espionage (Deprecated ATT&CK Group; replaced by Campaign C0013 Operation Sharpshooter)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2017-09-01"
last_seen: "2019-03-01"
status: "Deprecated (Converted to Campaign)"
motivations: ["Espionage"]
objectives: ["Collection against nuclear, defense, government, energy, and financial sectors (campaign-targeted)"]
victimology_summary: "ATT&CK previously tracked 'Sharpshooter' as a Group (G0104) but later converted it into the Campaign object C0013 (Operation Sharpshooter). The campaign targeted nuclear, defense, government, energy, and financial companies globally, with many victims in Germany, Turkey, the UK, and the US. Reporting noted similarities to Lazarus Group operations (e.g., recruitment-themed lures and shared code), but ATT&CK describes it as a campaign."
target_sectors: ["Nuclear","Defense","Government","Energy","Financial Services"]
target_regions: ["Germany","Turkey","United Kingdom","United States","Global (reported)"]
related_groups: ["[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]]"]
malware: ["[[30_CIPHER/05_Malware/Rising Sun]]"]
tools: []
infrastructure: ["Dropbox/web services for hosting lures and stage payloads","Startup-folder persistence + masquerading","Proxy/VPN use reported (ExpressVPN)"]
ttps:
  - "[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]"
  - "[[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]"
  - "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"
  - "[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]"
  - "[[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]"
  - "[[20_Entities/07_TTPs/T1055 - Process Injection]]"
  - "[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1587.001 - Develop Capabilities: Malware]]"
  - "[[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]]"
  - "[[20_Entities/07_TTPs/T1090 - Proxy]]"
  - "[[20_Entities/07_TTPs/T1106 - Native API]]"
notable_claims: ["ATT&CK Group G0104 was deprecated and replaced by Campaign C0013."]
intel_sources:
  - "MITRE ATT&CK (Update Note) - October 2022: https://attack.mitre.org/resources/updates/updates-october-2022/"
  - "MITRE ATT&CK (Campaign) - C0013 Operation Sharpshooter: https://attack.mitre.org/campaigns/C0013/"
tags: ["scout","threat-actor","mitre-g0104","deprecated","espionage","campaign-conversion"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Sharpshooter (G0104) is a **deprecated** ATT&CK Group entry converted into **Campaign C0013 (Operation Sharpshooter)**. The campaign represents a global espionage operation targeting **nuclear, defense, government, energy, and financial** sectors, leveraging staged lure delivery (including web services), VBA-enabled documents, and the **Rising Sun** modular backdoor.

## 2. Attribution & Profile
- **ATT&CK status:** Deprecated Group → replaced by Campaign C0013
- **Attribution:** Unattributed campaign; reporting noted similarities to [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]] operations (not definitive attribution)
- **Confidence:** Low for actor identity; Medium for campaign behavior per documented reporting

## 3. Targeting & Victimology
- **Sectors:** nuclear, defense, government, energy, financial
- **Regions:** many victims reported in Germany, Turkey, the UK, and the US (plus broader global reach)
- **Lure theme:** recruitment/job-related lures (per reporting cited by ATT&CK)

## 4. Known Malware, Tools & Infrastructure
**Malware**
- [[30_CIPHER/05_Malware/Rising Sun]]

**Infrastructure**
- Dropbox/web services hosting aligned with [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]] and [[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]
- Startup-folder persistence + masquerade aligned with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- Proxy/VPN usage aligned with [[20_Entities/07_TTPs/T1090 - Proxy]]

## 5. Tradecraft Overview
- **Delivery:** malicious Word/PDF files requiring user execution ([[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]])
- **Macro-based execution:** VBA download/install chain ([[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]])
- **OLE/DDE abuse surface:** malicious OLE documents and DDE usage ([[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]])
- **Injection:** shellcode-based injection into Word noted in reporting ([[20_Entities/07_TTPs/T1055 - Process Injection]])

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]
- [[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1559.002 - Inter-Process Communication: Dynamic Data Exchange]]
- [[20_Entities/07_TTPs/T1055 - Process Injection]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1587.001 - Develop Capabilities: Malware]]
- [[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]]
- [[20_Entities/07_TTPs/T1090 - Proxy]]
- [[20_Entities/07_TTPs/T1106 - Native API]]

## 7. Detection Opportunities
1. **Office execution + macro downloader chains**
   - Monitor Office spawning script engines and creating/launching binaries from user-writable or Startup paths.
2. **DDE/OLE anomalies**
   - Alert on unusual DDE invocation flows, embedded object activation patterns, and document-driven command execution.
3. **Process injection from document context**
   - Word with suspicious memory allocation + write + execution patterns; injection into Office process space.
4. **Web-service hosted lures**
   - Egress to Dropbox or similar services for payload staging when inconsistent with baseline usage.

## 8. Response & Mitigation Guidance
- Block or heavily restrict macro execution from the internet; enforce Mark-of-the-Web protections.
- Enhance email gateway and sandboxing for Office documents; validate DDE/OLE handling policies.
- Rapidly isolate endpoints exhibiting Office-driven staging or injection indicators; perform credential hygiene and persistence removal.

## 9. Hunting Ideas
- Hunt for `mssync.exe`-like artifacts in Startup locations paired with suspicious creation times and unknown signatures.
- Identify Office processes making outbound connections to file-sharing/web-service hosts atypical for the org.
- Triage any proxy/VPN artifacts on endpoints tied to staged delivery.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/Rising Sun]]

## 11. Associated Tools
- None explicitly listed on the ATT&CK campaign page beyond malware.

## 12. Analyst Notes
- **High-signal anchors:** Office-driven downloaders, DDE/OLE exploitation surface, injection into Office, and Startup-folder persistence.
- **Deprecation handling:** Use Campaign C0013 for ATT&CK-aligned tracking; G0104 should be treated as historical.

## 13. Further Reading / External Resources
- MITRE Campaign C0013: https://attack.mitre.org/campaigns/C0013/
- MITRE Updates (Oct 2022): https://attack.mitre.org/resources/updates/updates-october-2022/

## 14. References
- MITRE ATT&CK. (2025). *Operation Sharpshooter (Campaign C0013).* https://attack.mitre.org/campaigns/C0013/
- MITRE ATT&CK. (2022). *Updates – October 2022 (Campaigns replacing Groups, incl. G0104).* https://attack.mitre.org/resources/updates/updates-october-2022/
- Sherstobitoff, R., Malhotra, A., et al. (2018, December 18). *Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure.* McAfee. https://www.mcafee.com/
