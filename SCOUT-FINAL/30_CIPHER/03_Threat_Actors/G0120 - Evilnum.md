---
entity_type: threat_actor
actor_name: "Evilnum"
common_name: "Evilnum"
actor_id: "G0120"
actor_type: "Cybercrime"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: ""
first_seen: ""
last_seen: ""
status: ""

motivations:
  - "Financial gain"
objectives:
  - "Initial access via phishing and user execution"
  - "Credential theft and session theft"
  - "Remote access and follow-on tooling deployment"
victimology_summary: "Cybercriminal group observed using JavaScript-based infection chains and credential theft, deploying the EVILNUM malware family and related tooling to maintain access and steal credentials/session data."
target_sectors: []
target_regions: []

related_groups: []

malware:
  - "[[30_CIPHER/05_Malware/S0568 - EVILNUM|EVILNUM]]"
tools:
  - "[[30_CIPHER/05_Malware/S0349 - LaZagne|LaZagne]]"

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control|T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]"
  - "[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript|T1059.007 - Command and Scripting Interpreter: JavaScript]]"
  - "[[20_Entities/07_TTPs/T1555 - Credentials from Password Stores|T1555 - Credentials from Password Stores]]"
  - "[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001 - Hijack Execution Flow: DLL]]"
  - "[[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion|T1070.004 - Indicator Removal: File Deletion]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link|T1566.002 - Phishing: Spearphishing Link]]"
  - "[[20_Entities/07_TTPs/T1219.002 - Remote Access Tools: Remote Desktop Software|T1219.002 - Remote Access Tools: Remote Desktop Software]]"
  - "[[20_Entities/07_TTPs/T1539 - Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]"
  - "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link|T1204.001 - User Execution: Malicious Link]]"
  - "[[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks|T1497.001 - Virtualization/Sandbox Evasion: System Checks]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0120/"
  - "https://www.welivesecurity.com/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0120"
  - "cybercrime"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Evilnum (G0120) is a cybercriminal group tracked by ATT&CK for phishing-led intrusions leveraging **JavaScript-based artifacts**, **credential theft**, and **remote access** workflows. ATT&CK associates the group with the **EVILNUM** malware (S0568) and the credential recovery tool **LaZagne** (S0349), alongside common behaviors such as **UAC bypass**, **DLL hijacking**, **file deletion**, and **sandbox checks**.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0120
- **Aliases:** Not listed on the ATT&CK Group page beyond “Evilnum”.
- **Attribution (sponsor/country):** Not explicitly stated on the ATT&CK Group page.

## 3. Motivations & Objectives
- **Motivation:** Financial gain.
- **Objectives:** Gain access via phishing/user execution, steal credentials/session artifacts, and deploy additional components as needed.

## 4. Targeting Profile
- ATT&CK reporting indicates victim selection is campaign-dependent; validate targeting from incident telemetry and email lure themes.

## 5. Tradecraft Overview
- **Initial access:** Spearphishing links leading to hosted archives and user-triggered execution.
- **Execution:** JavaScript artifacts on host; malicious shortcuts/links driving staged download.
- **Credential access:** Credential extraction from password stores and session cookie theft.
- **Persistence/stealth:** Utility-based cleanup (file deletion) and evasion via system checks; DLL hijacking in legitimate app directories.
- **Remote access:** Legitimate remote desktop software to control compromised hosts.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link|T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link|T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript|T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control|T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control]]
- [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL|T1574.001 - Hijack Execution Flow: DLL]]
- [[20_Entities/07_TTPs/T1555 - Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[20_Entities/07_TTPs/T1539 - Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1070.004 - Indicator Removal: File Deletion|T1070.004 - Indicator Removal: File Deletion]]
- [[20_Entities/07_TTPs/T1497.001 - Virtualization/Sandbox Evasion: System Checks|T1497.001 - Virtualization/Sandbox Evasion: System Checks]]
- [[20_Entities/07_TTPs/T1219.002 - Remote Access Tools: Remote Desktop Software|T1219.002 - Remote Access Tools: Remote Desktop Software]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0568 - EVILNUM|EVILNUM]]
- Tools:
  - [[30_CIPHER/05_Malware/S0349 - LaZagne|LaZagne]]
  - (Campaign-dependent) legitimate remote desktop software referenced by ATT&CK.

## 8. Infrastructure Patterns
- **Phishing-hosted archives** (e.g., cloud file hosting) and staged download behavior.
- **Follow-on component delivery** via [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]].

## 9. Campaign History
- ATT&CK technique examples cite campaigns involving JavaScript-based infection components and TeamViewer-directory DLL hijacking patterns.

## 10. Known Indicators
- Prefer behavior-driven pivots:
  - Suspicious `.js` execution chains (user context) and LNK-driven download flows.
  - Evidence of DLL hijacking in legitimate app directories.
  - Browser credential store access and cookie theft indicators.
  - Remote desktop tool usage from unusual parent processes/users.

## 11. Defensive Recommendations
- **Email/web:** Harden link handling (detonation, safe browsing); block suspicious archive delivery routes; monitor cloud-hosted file downloads from email clients.
- **Endpoint:** Alert on script execution from user-writable paths; detect DLL search-order hijacking signals; enable PowerShell and script block logging.
- **Browser:** Restrict credential storage; monitor access to browser credential stores and cookie databases.
- **Remote tools:** Tighten allowlists for remote desktop software; alert on first-seen binaries and suspicious session origins.

## 12. Analyst Notes
- Highest-signal: spearphishing link → user execution → script chain → credential/session theft → remote tool usage.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0120/
- ESET research portal: https://www.welivesecurity.com/

## 14. References
- MITRE ATT&CK. (n.d.). *Evilnum (G0120).* https://attack.mitre.org/groups/G0120/
- ESET. (n.d.). *WeLiveSecurity (research portal).* https://www.welivesecurity.com/

## 15. Notes
- Validate remote desktop tooling and staging infrastructure per incident; Evilnum tradecraft is modular and campaign-specific.
