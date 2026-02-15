---
entity_type: threat_actor
actor_name: "menuPass"
common_name: "menuPass"
actor_id: "G0045"
actor_type: "China-nexus cyber espionage threat group associated with large-scale MSP-enabled intrusions (e.g., Operation Cloud Hopper)"
aliases: ["APT10","Stone Panda","Red Apollo","Cicada","POTASSIUM","CVNX","HOGFISH","BRONZE RIVERSIDE"]
country_of_origin: "China"
suspected_sponsors: ["Ministry of State Security (MSS)","Tianjin State Security Bureau (TSSB)"]
attribution_confidence: "High"
first_seen: "2006-01-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Intelligence collection from global public and private sector targets","Leverage Managed Service Providers (MSPs) and other trusted relationships to pivot into downstream networks","Credential access and lateral movement to reach high-value systems and data repositories","Data staging, archiving, and exfiltration at scale (reported in Cloud Hopper-era activity)"]
victimology_summary: "menuPass (MITRE ATT&CK G0045), also tracked as APT10/Stone Panda/Red Apollo, is assessed to have been active since at least 2006. MITRE reports that individual members acted in association with the Chinese Ministry of State Security’s Tianjin State Security Bureau, and U.S./U.K. government communications describe the actor as conducting long-running global intrusion activity. Reported targeting spans healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors worldwide, with emphasis on Japanese organizations. A widely reported operational pattern (2016–2017) involved compromising Managed Service Providers to access multiple client environments (often referred to as Operation Cloud Hopper)."
target_sectors: ["Government","Defense","Aerospace","Healthcare","Biotechnology","Energy","Finance","Maritime","Technology / MSPs (managed services)","Manufacturing","Mining","Higher education"]
target_regions: ["Global","Japan (emphasis, reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/RedLeaves]]","[[30_CIPHER/05_Malware/PlugX]]","[[30_CIPHER/05_Malware/UPPERCUT]]","[[30_CIPHER/05_Malware/ChChes]]","[[30_CIPHER/05_Malware/EvilGrab]]"]
tools: ["[[30_CIPHER/05_Malware/Mimikatz]]","[[30_CIPHER/05_Malware/Impacket]]","[[30_CIPHER/05_Malware/PowerSploit]]","[[30_CIPHER/05_Malware/Cobalt Strike]]","[[30_CIPHER/05_Malware/AdFind]]","[[30_CIPHER/05_Malware/certutil]]"]
infrastructure: ["[[Managed Service Provider compromise]]","[[Trusted relationship abuse]]","[[Malicious domain registration]]","[[Dynamic DNS / Fast Flux]]","[[External proxy infrastructure]]","[[Signed/modified binaries]]"]
ttps: ["[[20_Entities/07_TTPs/T1199 - Trusted Relationship]]","[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]","[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]","[[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]","[[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]","[[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]","[[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]","[[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]","[[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1560 - Archive Collected Data]]","[[20_Entities/07_TTPs/T1119 - Automated Collection]]","[[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]","[[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]","[[20_Entities/07_TTPs/T1090.002 - Proxy: External Proxy]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — menuPass (G0045) (Last Modified 2024-11-17): https://attack.mitre.org/groups/G0045/","U.S. DOJ — Two Chinese Hackers Associated With the Ministry of State Security Charged in Global Computer Intrusion Campaign (2018-12-20): https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion","UK NCSC — APT10 continuing to target UK organisations (2018-12-20): https://www.ncsc.gov.uk/news/apt10-continuing-target-uk-organisations","UK NCSC — APT10 advisory v2 (PDF) (2018-12-20): https://www.ncsc.gov.uk/files/APT10%20advisory%20v2.pdf","CISA/DHS — Chinese Cyber Activity Targeting Managed Service Providers (PDF): https://www.cisa.gov/sites/default/files/c3vp/Chinese-Cyber-Activity-Targeting-Managed-Service-Providers.pdf","PwC UK & BAE Systems — Operation Cloud Hopper report (PDF) (2017-04): https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-report-april-2017.pdf","Reuters Investigates — Inside the West’s failed fight against China’s ‘Cloud Hopper’ hackers (2019-06-26): https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/","ACSC — Compromise of an Australian Company via their Managed Service Provider (Investigation Report PDF): https://www.cyber.gov.au/sites/default/files/2023-03/msp_investigation_report.pdf"]
tags: ["threat-actor","menupass","apt10","g0045","stone-panda","red-apollo","cloud-hopper","china-nexus","cyber-espionage","msp"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# menuPass

## 1. BLUF / Executive Summary
menuPass (**G0045**) is a China-nexus cyber espionage threat actor widely associated with **MSP-enabled intrusions** and global strategic collection activity. Public government statements and MITRE reporting tie elements of the activity to China’s **Ministry of State Security (MSS)** (including the **Tianjin State Security Bureau**), and reporting highlights multi-industry targeting with an emphasis on **Japanese organizations**. A defining operational pattern (2016–2017) described in multiple public sources is the abuse of **trusted relationships with Managed Service Providers** to pivot into downstream customer environments.

## 2. Attribution Notes
- MITRE states menuPass members are known to have acted in association with the Chinese MSS’s **Tianjin State Security Bureau** (TSSB).
- The U.S. Department of Justice unsealed charges in 2018 describing APT10-linked individuals acting in association with the TSSB and conducting a long-running global intrusion campaign.
- UK NCSC public communications describe **APT10** (also known as Stone Panda/menuPass/Red Apollo) as acting on behalf of the **Chinese MSS**.

## 3. Motivations & Objectives
- **Primary motivation:** strategic **espionage** and sensitive information theft.
- **Operational objectives:** access acquisition via third parties (MSPs/IT service providers), credential capture and reuse, and sustained collection from high-value systems and shared repositories.

## 4. Targeting Profile
- **Sectors (reported/MITRE):** healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government; additionally MSPs and other service providers as access brokers to clients.
- **Geographic emphasis:** global operations with repeated emphasis on **Japan** in MITRE’s summary.

## 5. Tradecraft Overview
- **Trusted relationship abuse:** leveraging MSP access and shared credentials to move between provider and client environments ([[20_Entities/07_TTPs/T1199 - Trusted Relationship]]; [[20_Entities/07_TTPs/T1078 - Valid Accounts]]).
- **Phishing-led access:** spearphishing attachments and lure files reported across multiple campaigns ([[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]; [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]).
- **Credential theft and lateral movement:** use of credential dumping and remote administration patterns (e.g., RDP/WMI) to expand access ([[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]; [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]; [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]).
- **Malware ecosystem:** multiple implants/backdoors linked to the group in public reporting, including [[30_CIPHER/05_Malware/RedLeaves]] and [[30_CIPHER/05_Malware/PlugX]].
- **Operational resilience:** use of registered malicious domains and dynamic resolution behaviors (including fast-flux patterns reported in ATT&CK technique mapping) ([[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]; [[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]).
- **Data handling:** staged collection and archiving prior to exfiltration are described in ATT&CK technique mapping and Cloud Hopper-era reporting ([[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]; [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]).

## 6. MITRE ATT&CK Mapping
- Initial Access / Execution
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
  - [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- Persistence / Privilege / Defense Evasion (representative)
  - [[20_Entities/07_TTPs/T1053.005 - Scheduled Task/Job: Scheduled Task]]
  - [[20_Entities/07_TTPs/T1574.001 - Hijack Execution Flow: DLL]]
  - [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
  - [[20_Entities/07_TTPs/T1055.012 - Process Injection: Process Hollowing]]
- Credential Access / Lateral Movement
  - [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]
  - [[20_Entities/07_TTPs/T1003.003 - OS Credential Dumping: NTDS]]
  - [[20_Entities/07_TTPs/T1003.004 - OS Credential Dumping: LSA Secrets]]
  - [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]]
  - [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]]
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
  - [[20_Entities/07_TTPs/T1199 - Trusted Relationship]]
- Collection / Exfiltration Support
  - [[20_Entities/07_TTPs/T1119 - Automated Collection]]
  - [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]
  - [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]
  - [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
  - [[20_Entities/07_TTPs/T1090.002 - Proxy: External Proxy]]
- Infrastructure
  - [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
  - [[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/RedLeaves]] — malware family used by menuPass per MITRE ATT&CK (S0153).
- [[30_CIPHER/05_Malware/PlugX]] — widely used modular RAT associated with the group’s activity in MITRE mapping.
- [[30_CIPHER/05_Malware/UPPERCUT]] — malware used by menuPass per MITRE ATT&CK (S0275).
- [[30_CIPHER/05_Malware/ChChes]] — malware/tooling referenced in MITRE’s software list for the group (S0144).
- [[30_CIPHER/05_Malware/EvilGrab]] — malware referenced in MITRE’s software list for the group (S0152).
- Commonly referenced post-compromise tooling in MITRE mapping and Cloud Hopper-era reporting:
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/Impacket]]
  - [[30_CIPHER/05_Malware/PowerSploit]]
  - [[30_CIPHER/05_Malware/Cobalt Strike]]
  - [[30_CIPHER/05_Malware/AdFind]]
  - [[30_CIPHER/05_Malware/certutil]]

## 8. Infrastructure Patterns
- [[Managed Service Provider compromise]] to reach many downstream organizations through a single upstream intrusion path (Cloud Hopper-era reporting).
- [[Trusted relationship abuse]] where shared/admin access between MSPs and clients becomes the pivot mechanism.
- [[Malicious domain registration]] for phishing/C2 and campaign infrastructure.
- [[Dynamic DNS / Fast Flux]]-aligned domain resolution patterns described in ATT&CK technique mapping.
- [[External proxy infrastructure]] (including proxying through third-party IP space) described in ATT&CK technique mapping.
- [[Signed/modified binaries]] and related trust subversion behaviors described in ATT&CK technique mapping.

## 9. Campaign History
- **2006+ (MITRE):** menuPass assessed active since at least 2006.
- **2016–2017 (reported):** activity described as targeting **MSPs** and leveraging their access into client environments; commonly discussed under the label **Operation Cloud Hopper**.
- **2017-04 (public reporting):** Operation Cloud Hopper report published (PwC UK / BAE Systems), describing MSP-focused global espionage activity attributed to APT10.
- **2018-12-20 (government statements):** UK NCSC issues updated advisory and public statement on APT10; U.S. DOJ announces charges against individuals associated with APT10 and the Tianjin MSS bureau.
- **2019-06-26 (investigative reporting):** Reuters Investigates publishes an in-depth account of Cloud Hopper-era MSP compromises and downstream impact.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Reduce MSP blast radius by segmenting and constraining third-party administrative paths; treat MSP access as a high-risk trust boundary aligned to [[20_Entities/07_TTPs/T1199 - Trusted Relationship]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Improve detections for credential theft and abnormal administrative tooling consistent with [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]] and remote admin patterns like [[20_Entities/07_TTPs/T1047 - Windows Management Instrumentation]] / [[20_Entities/07_TTPs/T1021.001 - Remote Services: Remote Desktop Protocol]].
- Prioritize controls against targeted phishing and malicious attachments aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]].
- Track suspicious domain acquisition and dynamic resolution behaviors aligned to [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]] and [[20_Entities/07_TTPs/T1568.001 - Dynamic Resolution: Fast Flux DNS]].
- Treat signed-but-unexpected binaries and anomalous signing behavior as high-signal events aligned to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]].

## 12. Analyst Notes
- menuPass is one of several China-nexus clusters with overlapping naming across vendors (APT10/Stone Panda/Red Apollo). This note anchors identity to **MITRE G0045** to reduce naming drift.
- “Cloud Hopper” is best treated as an operation/campaign label used in public reporting for MSP-enabled activity attributed to the group; not all menuPass activity is necessarily Cloud Hopper-specific.

## 13. Further Reading / External Resources
- MITRE ATT&CK — menuPass (G0045): https://attack.mitre.org/groups/G0045/
- U.S. DOJ — APT10-linked charging announcement (2018-12-20): https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion
- UK NCSC — APT10 public statement: https://www.ncsc.gov.uk/news/apt10-continuing-target-uk-organisations
- UK NCSC — APT10 advisory v2 (PDF): https://www.ncsc.gov.uk/files/APT10%20advisory%20v2.pdf
- CISA/DHS — Chinese cyber activity targeting MSPs (PDF): https://www.cisa.gov/sites/default/files/c3vp/Chinese-Cyber-Activity-Targeting-Managed-Service-Providers.pdf
- PwC UK / BAE — Operation Cloud Hopper report (PDF): https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-report-april-2017.pdf
- Reuters Investigates — Cloud Hopper special report: https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/
- ACSC — MSP investigation report (PDF): https://www.cyber.gov.au/sites/default/files/2023-03/msp_investigation_report.pdf

## 14. References
1. MITRE ATT&CK. “menuPass (G0045).” (Last Modified 2024-11-17). https://attack.mitre.org/groups/G0045/
2. U.S. Department of Justice. “Two Chinese Hackers Associated With the Ministry of State Security Charged in Global Computer Intrusion Campaign.” (2018-12-20). https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion
3. UK National Cyber Security Centre (NCSC). “APT10 continuing to target UK organisations.” (2018-12-20). https://www.ncsc.gov.uk/news/apt10-continuing-target-uk-organisations
4. UK National Cyber Security Centre (NCSC). “APT10 advisory v2.” (2018-12-20) (PDF). https://www.ncsc.gov.uk/files/APT10%20advisory%20v2.pdf
5. Cybersecurity and Infrastructure Security Agency (CISA) / DHS. “Chinese Cyber Activity Targeting Managed Service Providers.” (PDF). https://www.cisa.gov/sites/default/files/c3vp/Chinese-Cyber-Activity-Targeting-Managed-Service-Providers.pdf
6. PwC UK & BAE Systems. “Operation Cloud Hopper.” (2017-04) (PDF). https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-report-april-2017.pdf
7. Reuters Investigates. “Inside the West’s failed fight against China’s ‘Cloud Hopper’ hackers.” (2019-06-26). https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/
8. Australian Cyber Security Centre (ACSC). “Compromise of an Australian Company via their Managed Service Provider.” (Investigation Report) (PDF). https://www.cyber.gov.au/sites/default/files/2023-03/msp_investigation_report.pdf
---
