---
entity_type: threat_actor
actor_name: "Whitefly"
common_name: "Whitefly"
actor_id: "G0107"
actor_type: "Cyber espionage (suspected Singaporean)"
aliases: []
country_of_origin: "Singapore (suspected)"
suspected_sponsors: []
attribution_confidence: "2-medium"
first_seen: "2017-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Long-term access for collection against organizations in Singapore and Southeast Asia"]
victimology_summary: "Whitefly is a suspected Singapore-linked espionage cluster that has targeted organizations primarily in Singapore, with reported activity against organizations in other Southeast Asian countries as well."
target_sectors: []
target_regions: ["Singapore","Cambodia","Indonesia","Philippines","Thailand","Vietnam","Southeast Asia (reported)"]
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]"
tools: []
infrastructure: ["[[Ingress Tool Transfer]]","[[Masquerading]]","[[DLL Search Order Hijacking]]"]
ttps:
  - "[[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]]"
  - "[[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]"
  - "[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]"
  - "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]"
notable_claims:
  - "Reporting attributed the cluster to a suspected Singapore-linked espionage effort; attribution remains assessed rather than confirmed."
intel_sources:
  - "https://attack.mitre.org/groups/G0107/"
  - "https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore"
tags: ["scout","threat-actor","mitre-g0107","espionage","southeast-asia"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Whitefly (G0107) is a suspected Singapore-linked espionage cluster associated with intrusions against organizations primarily in **Singapore**, with additional reporting of activity across **Southeast Asia**.

## 2. Attribution & Profile
- **Type:** Espionage
- **Attribution:** Assessed (suspected Singapore linkage); not definitively confirmed in public reporting
- **Attribution Confidence:** 2-medium

## 3. Targeting & Victimology
- **Regions:** Singapore; reported spillover into Cambodia, Indonesia, Philippines, Thailand, Vietnam
- **Sectors:** Not consistently specified in ATT&CK summaries (track as unknown unless local cases add sector detail)

## 4. Known Malware, Tools & Infrastructure
**Malware / Tooling**
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]

**Operational patterns**
- DLL search-order hijacking for execution flow hijack
- Encoded/encrypted payloads and masquerading for stealth
- Credential access via LSASS dumping

## 5. Tradecraft Overview
- **Initial execution:** user execution of malicious files
- **Post-compromise:** tool transfer, privilege escalation, credential dumping
- **Stealth:** masquerading + encoded artifacts; DLL search order hijacking

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter]]
- [[20_Entities/07_TTPs/T1068 - Exploitation for Privilege Escalation]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]

## 7. Detection Opportunities
1. **DLL search-order hijacking**
   - Alert on unsigned DLL loads from user-writable dirs; anomalous DLL load paths for signed binaries.
2. **LSASS access + dumping**
   - Monitor suspicious LSASS handle access, dump artifacts, and known dumping utilities.
3. **Ingress tool transfer**
   - EDR detections for file transfers to unusual directories + immediate execution.

## 8. Response & Mitigation Guidance
- Harden DLL loading (SafeDllSearchMode, application whitelisting, signed DLL enforcement where feasible).
- Enable credential dumping protections (LSA protection, EDR LSASS rules).
- Contain compromised hosts; rotate credentials where LSASS access is suspected.

## 9. Hunting Ideas
- Hunt for new services/tasks around the time of suspicious DLL loads.
- Identify processes launching from unusual directories after file transfers.
- Correlate endpoint events with encoded payload blobs staged to disk.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]

## 11. Associated Tools
- None beyond ATT&CK-referenced software in public summaries.

## 12. Analyst Notes
- Sector targeting is underspecified in ATT&CK summaries; enrich with local case telemetry.
- Completeness: **Medium** (ATT&CK provides limited victimology detail beyond geography).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group G0107: https://attack.mitre.org/groups/G0107/
- Symantec reporting: https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore

## 14. References (APA)
- MITRE ATT&CK. (n.d.). *Whitefly (G0107).* https://attack.mitre.org/groups/G0107/
- Symantec Threat Intelligence. (2019). *Whitefly: Espionage group has Singapore in its sights.* https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore
