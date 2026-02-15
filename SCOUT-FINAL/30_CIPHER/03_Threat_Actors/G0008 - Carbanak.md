---
entity_type: "threat_actor"
actor_name: "Carbanak"
common_name: "Carbanak"
actor_id: "G0008"
actor_type: "Cybercriminal / financially motivated"
aliases: ["Anunak"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2013-01"
last_seen: ""
status: "Unknown"
motivations: ["Financial gain"]
objectives: ["Financial theft and fraud", "Long-term access and persistence in banking environments"]
victimology_summary: "MITRE ATT&CK describes Carbanak as a cybercriminal group that has used [[30_CIPHER/05_Malware/Carbanak]] to target financial institutions since at least 2013. Public reporting characterizes campaigns as intrusions into bank environments enabling fraudulent transactions and operational manipulation, with significant cumulative losses alleged across affected institutions."
target_sectors: ["Financial institutions", "Banking", "Payment processing"]
target_regions: ["Global"]
related_groups: ["Cobalt Group", "FIN7"]
malware: ["[[30_CIPHER/05_Malware/Carbanak]]"]
tools: ["[[30_CIPHER/05_Malware/Mimikatz]]", "[[30_CIPHER/05_Malware/PsExec]]", "[[30_CIPHER/05_Malware/netsh]]", "[[30_CIPHER/05_Malware/TeamViewer]]", "[[30_CIPHER/05_Malware/Ammyy Admin]]", "[[30_CIPHER/05_Malware/VNC]]"]
infrastructure: ["[[Google Apps Script]]", "[[Google Sheets]]", "[[Google Forms]]", "[[Web Service C2]]", "[[Remote Access Tools]]", "[[Windows Services]]"]
ttps: ["[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]", "[[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]", "[[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]", "[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]", "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]", "[[20_Entities/07_TTPs/T1219 - Remote Access Tools]]", "[[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]", "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]", "[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (G0008): Carbanak (Last modified 2025-04-25)","MITRE ATT&CK (S0030): Carbanak malware (Last modified 2025-04-16)","Kaspersky (2015-02): CARBANAK APT — The Great Bank Robbery (PDF)","Visa (2015): Carbanak (Anunak) Advanced Persistent Threat alert (PDF)","U.S. DOJ (2018-08-01): FIN7 members charged/arraigned; FIN7 also referred to as Carbanak Group","U.S. DOJ (2021-06-24): FIN7 member sentencing; FIN7 also referred to as Carbanak Group"]
tags: ["threat-actor", "cybercrime", "financial-crime", "banking", "carbanak", "anunak", "mitre-g0008"]
---

# Carbanak

## 1. BLUF / Executive Summary
Carbanak (MITRE ATT&CK **G0008**, also known as **Anunak**) is a financially motivated cybercriminal group associated with intrusions against financial institutions since at least 2013. MITRE and major industry reporting characterize Carbanak activity as “APT-like” in persistence and tradecraft, using [[30_CIPHER/05_Malware/Carbanak]] plus credential theft and remote administration tooling to maintain access and enable fraudulent outcomes in banking environments. MITRE notes Carbanak may be linked to groups tracked separately as Cobalt Group and FIN7, reflecting ecosystem overlap and shared malware usage.

## 2. Attribution Notes
- **Tracking scope:** “Carbanak” is both a group designation and a malware family name; analytic precision requires separating the **actor cluster** (G0008) from the **software** ([[30_CIPHER/05_Malware/Carbanak]] / MITRE S0030).
- **Ecosystem overlap:** MITRE states Carbanak **may be linked** to Cobalt Group and FIN7 due to shared malware usage; this should be treated as a cautious linkage, not a definitive equivalence.
- **Law-enforcement naming:** U.S. DOJ communications describing FIN7 refer to FIN7 as “also referred to as Carbanak Group” in some documents, underscoring naming overlap across investigations and vendor tracking.

## 3. Motivations & Objectives
- **Motivation:** Financial gain via cyber-enabled fraud.
- **Objectives:** Obtain and use privileged access inside banking environments to enable fraudulent transactions and other theft mechanisms while sustaining access to support repeat operations.

## 4. Targeting Profile
- **Primary targets:** Financial institutions and banking environments (including systems supporting transaction processing and operational workflows).
- **Geography:** Public reporting frames Carbanak activity as multinational/global in victim reach.

## 5. Tradecraft Overview
- **Persistence & privilege:** Use of [[Windows Services]] for persistence aligned with [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]].
- **Credential-centric operations:** Reliance on legitimate credentials aligned with [[20_Entities/07_TTPs/T1078 - Valid Accounts]], supported by use of tools such as [[30_CIPHER/05_Malware/Mimikatz]] (as documented in MITRE’s software associations for the group).
- **Remote operations:** Use of legitimate remote administration utilities and interactive access consistent with [[20_Entities/07_TTPs/T1219 - Remote Access Tools]] (MITRE cites AmmyyAdmin/TeamViewer-style tooling in group reporting).
- **Defense impairment and concealment:** Firewall modification patterns aligned with [[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]] and masquerading behaviors aligned with [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]] and [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]].
- **Web-service enabled C2:** MITRE documents use of Google Workspace services for command-and-control consistent with [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
- [[20_Entities/07_TTPs/T1562.004 - Impair Defenses: Disable or Modify System Firewall]]
- [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1219 - Remote Access Tools]]
- [[20_Entities/07_TTPs/T1218.011 - System Binary Proxy Execution: Rundll32]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]

## 7. Malware & Tools Used
- **Malware:**
  - [[30_CIPHER/05_Malware/Carbanak]]
- **Tools / utilities (documented in MITRE group/software context and widely cited reporting):**
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/PsExec]]
  - [[30_CIPHER/05_Malware/netsh]]
  - [[30_CIPHER/05_Malware/TeamViewer]]
  - [[30_CIPHER/05_Malware/Ammyy Admin]]
  - [[30_CIPHER/05_Malware/VNC]]

## 8. Infrastructure Patterns
- Use of [[Web Service C2]] via Google Workspace components (e.g., [[Google Apps Script]], [[Google Sheets]], [[Google Forms]]) as described in MITRE’s technique notes for the group.
- Reliance on [[Remote Access Tools]] for interactive control in victim environments (legitimate tooling repurposed for unauthorized access).
- Persistence via [[Windows Services]] and service-name masquerading consistent with the ATT&CK mapping above.

## 9. Campaign History
- **2013–2015 (public emergence):** Industry reporting frames Carbanak as a major bank-focused intrusion set active since at least 2013, with large-scale losses alleged across affected institutions.
- **2018 (law-enforcement actions in adjacent tracking):** U.S. DOJ actions against FIN7 describe the group as also referred to as “Carbanak Group,” illustrating how investigations and vendor tracking sometimes merge or overlap labels in financial cybercrime ecosystems.
- **Ongoing tracking:** MITRE continues to maintain Carbanak (G0008) as a distinct cluster, while noting possible linkages to other financially motivated groups that also used the Carbanak malware family.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Strengthen detection for unauthorized remote administration and interactive tooling consistent with [[20_Entities/07_TTPs/T1219 - Remote Access Tools]], especially when correlated with unusual authentication patterns.
- Prioritize monitoring for credential misuse consistent with [[20_Entities/07_TTPs/T1078 - Valid Accounts]] in banking environments where privileged access can enable high-impact fraud.
- Improve visibility for persistence and service tampering aligned with [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]] and masquerading patterns aligned with [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]].
- Treat unusual third-party web-service communications consistent with [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]] as higher-signal when combined with other corroborating behaviors in sensitive finance workflows.

## 12. Analyst Notes
- **Attribution confidence:** Medium (strong MITRE cluster definition and multiple reputable reports; however, naming overlap across financial cybercrime actors complicates strict boundary-setting).
- **Name collision risk:** “Carbanak” frequently appears in reporting as both an actor label and a malware label, and may be used interchangeably with FIN7 in some legal and vendor contexts; apply convergence analysis rather than label matching.
- **Scope discipline:** Carbanak is best treated as a bank-focused financially motivated cluster; broader retail-focused payment-card theft narratives are more commonly described under FIN7 in public law-enforcement reporting.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Carbanak (G0008)  
  https://attack.mitre.org/groups/G0008/
- MITRE ATT&CK — Carbanak malware (S0030)  
  https://attack.mitre.org/software/S0030/
- Kaspersky — CARBANAK APT: The Great Bank Robbery (PDF)  
  https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf
- Visa — Carbanak (Anunak) Advanced Persistent Threat (PDF)  
  https://usa.visa.com/dam/VCOM/download/merchants/Alert-CARBANAK.pdf
- U.S. DOJ — Three members of FIN7 in custody (FIN7 also referred to as Carbanak Group) (2018-08-01)  
  https://www.justice.gov/archives/opa/pr/three-members-notorious-international-cybercrime-group-fin7-custody-role-attacking-over-100
- U.S. DOJ — FIN7 sentencing (FIN7 also referred to as Carbanak Group) (2021-06-24)  
  https://www.justice.gov/archives/opa/pr/high-level-member-hacking-group-sentenced-prison-scheme-compromised-tens-millions-debit-and

## 14. References
- MITRE ATT&CK. “Carbanak (G0008).” (Last modified 2025-04-25)  
  https://attack.mitre.org/groups/G0008/
- MITRE ATT&CK. “Carbanak malware (S0030).” (Last modified 2025-04-16)  
  https://attack.mitre.org/software/S0030/
- Kaspersky Lab Global Research and Analysis Team. “CARBANAK APT: The Great Bank Robbery.” (2015-02) PDF  
  https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf
- Visa. “Carbanak (Anunak) Advanced Persistent Threat.” (PDF)  
  https://usa.visa.com/dam/VCOM/download/merchants/Alert-CARBANAK.pdf
- U.S. Department of Justice. “Three Members of Notorious International Cybercrime Group ‘Fin7’ In Custody for Role in Attacking Over 100 U.S. Companies.” (2018-08-01)  
  https://www.justice.gov/archives/opa/pr/three-members-notorious-international-cybercrime-group-fin7-custody-role-attacking-over-100
- U.S. Department of Justice. “High-Level Member of Hacking Group Sentenced to Prison for Scheme that Compromised Tens of Millions of Debit and Credit Cards.” (2021-06-24)  
  https://www.justice.gov/archives/opa/pr/high-level-member-hacking-group-sentenced-prison-scheme-compromised-tens-millions-debit-and
