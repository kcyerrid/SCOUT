---
entity_type: threat_actor
actor_name: "Blue Mockingbird"
common_name: "Blue Mockingbird"
actor_id: "G0108"
actor_type: "Cybercrime (cryptomining / financially motivated)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "2-medium"
first_seen: "2019-12-01"
last_seen: ""
status: "Unknown"
motivations: ["Financial Gain"]
objectives: ["Deploy cryptominers and maintain access to compromised Windows servers"]
victimology_summary: "Blue Mockingbird is a financially motivated cluster associated with exploitation of public-facing applications and post-exploitation tradecraft (credential access, lateral movement) to deploy cryptomining payloads."
target_sectors: []
target_regions: []
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]"
  - "[[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]"
tools:
  - "[[XMRig]]"
infrastructure: ["[[Proxy]]","[[Remote Services]]","[[Windows Service Persistence]]"]
ttps:
  - "[[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]"
  - "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]"
  - "[[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1574.012 - Hijack Execution Flow: COR_PROFILER]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1112 - Modify Registry]]"
  - "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]"
  - "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]"
  - "[[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]"
  - "[[20_Entities/07_TTPs/T1090 - Proxy]]"
  - "[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]"
  - "[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]"
  - "[[20_Entities/07_TTPs/T1496.001 - Resource Hijacking: Compute Hijacking]]"
  - "[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]"
  - "[[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32]]"
  - "[[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]"
  - "[[20_Entities/07_TTPs/T1082 - System Information Discovery]]"
  - "[[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]"
  - "[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]"
notable_claims:
  - "Observed using COR_PROFILER execution-flow hijack to load a cryptomining DLL in-process."
intel_sources:
  - "https://attack.mitre.org/groups/G0108/"
  - "https://redcanary.com/blog/blue-mockingbird-cryptominer/"
tags: ["scout","threat-actor","mitre-g0108","cybercrime","cryptomining"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Blue Mockingbird (G0108) is a financially motivated intrusion cluster linked to **server-side exploitation** and **cryptomining** deployment, with tradecraft that includes persistence, credential access, and lateral movement.

## 2. Attribution & Profile
- **Type:** Cybercrime / financially motivated
- **Attribution Confidence:** 2-medium (cluster behavior is well described; operator identity remains unknown)

## 3. Targeting & Victimology
- **Primary victimology:** broadly internet-facing Windows server environments (public reporting varies by dataset)
- **Goal:** compute hijacking for cryptomining

## 4. Known Malware, Tools & Infrastructure
**Software (ATT&CK)**
- [[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]

**Other tooling**
- [[XMRig]] (commonly referenced cryptominer; no S#### confirmed)

## 5. Tradecraft Overview
- **Initial access:** [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- **Execution-flow hijack:** [[20_Entities/07_TTPs/T1574.012 - Hijack Execution Flow: COR_PROFILER]]
- **Persistence:** services, scheduled tasks, WMI event subscriptions
- **Objective:** [[20_Entities/07_TTPs/T1496.001 - Resource Hijacking: Compute Hijacking]]

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1134 - Access Token Manipulation]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
- [[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1574.012 - Hijack Execution Flow: COR_PROFILER]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1112 - Modify Registry]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1003.001 - OS Credential Dumping: LSASS Memory]]
- [[20_Entities/07_TTPs/T1090 - Proxy]]
- [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1496.001 - Resource Hijacking: Compute Hijacking]]
- [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
- [[20_Entities/07_TTPs/T1218.010 - System Binary Proxy Execution: Regsvr32]]
- [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]
- [[20_Entities/07_TTPs/T1082 - System Information Discovery]]
- [[20_Entities/07_TTPs/T1569.002 - System Services: Service Execution]]
- [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]

## 7. Detection Opportunities
1. **COR_PROFILER abuse**
   - Alert on registry/environment-variable changes enabling COR_PROFILER on server workloads.
2. **Compute hijacking signals**
   - Sustained high CPU on server processes + unexpected outbound pools/stratum-like traffic.
3. **WMI persistence**
   - Monitor WMI event subscription creation/modification, especially tied to suspicious binaries.
4. **Credential dumping**
   - LSASS access alerts + post-compromise admin tool activity (PsExec-like lateral movement patterns).

## 8. Response & Mitigation Guidance
- Patch/mitigate public-facing services; reduce attack surface on internet-exposed servers.
- Restrict administrative shares, enforce MFA for remote access, and segment servers from workstations.
- Remove persistence (services/tasks/WMI subscriptions) and rotate credentials after containment.

## 9. Hunting Ideas
- Hunt for COR_PROFILER keys/vars on servers that should not run managed profilers.
- Search for FRP binaries/configs and anomalous reverse proxy connections.
- Identify base64-encoded PowerShell usage on server fleets.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz (S0002)]]

## 11. Associated Tools
- [[XMRig]] (no S#### confirmed)

## 12. Analyst Notes
- XMRig is referenced in public reporting, but no ATT&CK S#### mapping is confirmed here—track as plain wikilink.
- Completeness: **High for TTPs** (ATT&CK technique list is extensive); **Medium for victimology** (often underspecified).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group G0108: https://attack.mitre.org/groups/G0108/
- Red Canary reporting: https://redcanary.com/blog/blue-mockingbird-cryptominer/

## 14. References (APA)
- MITRE ATT&CK. (n.d.). *Blue Mockingbird (G0108).* https://attack.mitre.org/groups/G0108/
- Red Canary. (n.d.). *Blue Mockingbird: a financially motivated cryptomining threat.* https://redcanary.com/blog/blue-mockingbird-cryptominer/
