---
entity_type: threat_actor
actor_name: "Threat Group-1314"
common_name: "Threat Group-1314"
actor_id: "G0028"
actor_type: "Unattributed intrusion set"
aliases: ["TG-1314"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2015-05-28"
last_seen: ""
status: "Unknown"
motivations: ["Unknown"]
objectives: ["Leverage compromised credentials to access remote access infrastructure", "Move laterally using built-in/admin tooling and victim management platforms (reported)"]
victimology_summary: "Threat Group-1314 (MITRE ATT&CK G0028) is an unattributed threat group described as using compromised credentials to access a victim’s remote access infrastructure. Public reporting highlights a ‘living off the land’ approach, including use of legitimate remote access (e.g., Citrix/VPN), lateral movement leveraging an endpoint management platform (Altiris), and remote execution/lateral movement activity associated with tools such as PsExec and Windows networking utilities (net use)."
target_sectors: []
target_regions: []
related_groups: []
malware: []
tools: ["[[30_CIPHER/05_Malware/Net]]","[[30_CIPHER/05_Malware/PsExec]]"]
infrastructure: ["[[Remote access infrastructure]]","[[Internet-facing Citrix]]","[[VPN access]]","[[Altiris endpoint management]]","[[Living-off-the-land]]"]
ttps: ["[[20_Entities/07_TTPs/T1133 - External Remote Services]]","[[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]","[[20_Entities/07_TTPs/T1072 - Software Deployment Tools]]","[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Threat Group-1314 (G0028) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0028/","SecureWorks (archived via Sophos) — Living off the Land / TG-1314 incident response write-up (2015-05-28): https://www.secureworks.com/blog/living-off-the-land","MITRE ATT&CK — PsExec (S0029): https://attack.mitre.org/software/S0029/","MITRE ATT&CK — Net (S0039): https://attack.mitre.org/software/S0039/"]
tags: ["threat-actor","g0028","threat-group-1314","tg-1314","unattributed","living-off-the-land","remote-access","altiris"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Threat Group-1314

## 1. BLUF / Executive Summary
Threat Group-1314 (MITRE ATT&CK **G0028**) is an **unattributed** intrusion set best characterized in public reporting by **credential-based access** to a victim’s **remote access infrastructure** and a **living-off-the-land** posture. Reporting describes the use of legitimate remote access (including an Internet-facing Citrix entry point) and lateral movement enabled by the victim’s endpoint management platform (Altiris), with activity associated to common administrative tooling such as [[30_CIPHER/05_Malware/PsExec]] and Windows networking utilities (e.g., [[30_CIPHER/05_Malware/Net]] via “net use”).

## 2. Attribution Notes
- MITRE ATT&CK tracks this intrusion set as **Threat Group-1314 (G0028)** and describes it as **unattributed**.
- The “TG-1314” label originates from vendor tracking in incident response reporting; no public, high-confidence national attribution is established in the cited sources.

## 3. Motivations & Objectives
- **Motivation:** Not established in the referenced public sources.
- **Operational objective (observed):** Use compromised credentials to gain foothold through [[20_Entities/07_TTPs/T1133 - External Remote Services]], then leverage existing enterprise tooling for execution and lateral movement.

## 4. Targeting Profile
- **Sectors/regions:** Not specified in the primary public references used for this profile.
- **Victim environment characteristics (reported):** Presence of externally exposed remote access services and centralized endpoint management tooling (e.g., Altiris).

## 5. Tradecraft Overview
- **Initial access via remote access services:** Public incident reporting describes entry using compromised credentials through an Internet-facing Citrix server, aligning conceptually with [[20_Entities/07_TTPs/T1133 - External Remote Services]] and credential abuse patterns.
- **Credential-based movement:** Use of compromised domain credentials in support of internal platform access aligns with [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]].
- **Abuse of endpoint management for lateral movement:** Use of Altiris as a mechanism for broad execution/lateral reach aligns with [[20_Entities/07_TTPs/T1072 - Software Deployment Tools]].
- **SMB/admin share activity for lateral movement:** Mapping of network drives using “net use” aligns with [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]].
- **Command execution via Windows shell:** Spawned command shells on remote systems align with [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]
- [[20_Entities/07_TTPs/T1072 - Software Deployment Tools]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/PsExec]] — MITRE-associated tool for remote execution; reported in TG-1314 incident response context.
- [[30_CIPHER/05_Malware/Net]] — Windows networking utility; “net use” behavior is explicitly associated with TG-1314 on MITRE ATT&CK.

## 8. Infrastructure Patterns
- [[Remote access infrastructure]] as an entry and persistence surface (reported).
- [[Internet-facing Citrix]] gateway use with compromised credentials (reported).
- [[VPN access]] or comparable remote access solutions as part of the environment and access pattern (reported in the broader “living off the land” context).
- [[Altiris endpoint management]] leveraged to extend reach and move laterally (reported).
- [[Living-off-the-land]] emphasis: prioritizing legitimate tooling and built-in utilities over bespoke malware (reported).

## 9. Campaign History
- **2015-05-28:** Public incident response reporting describes a TG-1314 intrusion leveraging compromised credentials, an Internet-facing Citrix server, and Altiris for lateral movement (SecureWorks write-up).
- **2017-05-31:** MITRE ATT&CK created the group entry for Threat Group-1314 (G0028).
- **2025-04-25:** MITRE ATT&CK last modified the group entry (per MITRE page metadata).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize monitoring and control of remote access pathways aligned to [[20_Entities/07_TTPs/T1133 - External Remote Services]] (remote gateways and authentication workflows), especially for anomalous logins and credential reuse patterns.
- Strengthen identity controls and visibility aligned to [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]], focusing on privileged accounts used for management platforms and remote access.
- Harden and tightly govern endpoint management/administration platforms aligned to [[20_Entities/07_TTPs/T1072 - Software Deployment Tools]] (restrict admin roles, audit administrative actions, and enforce strong authentication).
- Increase detection fidelity for lateral movement patterns aligned to [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]] and remote execution patterns associated with [[30_CIPHER/05_Malware/PsExec]].
- Treat unexpected interactive shell activity aligned to [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]] as higher signal when correlated with remote access events and management platform actions.

## 12. Analyst Notes
- Public detail on TG-1314 is comparatively narrow and incident-driven; avoid overgeneralizing beyond the behaviors explicitly described by MITRE and vendor incident response reporting.
- This cluster is a useful “pattern exemplar” for credential-led intrusions that abuse legitimate tooling and management planes, but the actor’s broader scope and objectives remain unclear in the referenced sources.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Threat Group-1314 (G0028): https://attack.mitre.org/groups/G0028/
- SecureWorks — Living off the Land (TG-1314 incident response write-up): https://www.secureworks.com/blog/living-off-the-land
- MITRE ATT&CK — PsExec (S0029): https://attack.mitre.org/software/S0029/
- MITRE ATT&CK — Net (S0039): https://attack.mitre.org/software/S0039/

## 14. References
1. MITRE ATT&CK. “Threat Group-1314 (G0028).” (Last Modified 2025-04-25). https://attack.mitre.org/groups/G0028/
2. Dell SecureWorks Counter Threat Unit. “Living off the Land.” (2015-05-28). https://www.secureworks.com/blog/living-off-the-land
3. MITRE ATT&CK. “PsExec (S0029).” (Last Modified 2024-09-25). https://attack.mitre.org/software/S0029/
4. MITRE ATT&CK. “Net (S0039).” (Last Modified 2024-11-27). https://attack.mitre.org/software/S0039/
