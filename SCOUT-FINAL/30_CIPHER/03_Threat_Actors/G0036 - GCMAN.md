---
entity_type: threat_actor
actor_name: "GCMAN"
common_name: "GCMAN"
actor_id: "G0036"
actor_type: "Financially motivated cybercrime group targeting banks to fraudulently transfer funds to e-currency services"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2015-01-01"
last_seen: "2017-01-01"
status: "Inactive since 2017 (reported)"
motivations: ["Financial gain"]
objectives: ["Establish access in banking environments","Move laterally using legitimate tools","Automate and conceal fraudulent fund transfers to e-currency services"]
victimology_summary: "GCMAN (MITRE ATT&CK G0036) is a financially motivated threat group described as targeting banks to transfer money to e-currency services. Public reporting links the group’s activity to spearphishing with malicious archives and follow-on use of legitimate remote administration and penetration-testing tools for lateral movement, followed by scheduled execution of scripts to generate fraudulent transactions. Reporting also describes opportunistic initial access through SQL injection against public-facing services, with attackers maintaining access prior to cash-out attempts."
target_sectors: ["Financial services","Banks"]
target_regions: ["Russia (reported early activity)","Global (reported targeting footprint)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/GCMAN]]"]
tools: ["[[30_CIPHER/05_Malware/PuTTY]]","[[30_CIPHER/05_Malware/VNC]]","[[30_CIPHER/05_Malware/Meterpreter]]","[[30_CIPHER/05_Malware/Metasploit]]"]
infrastructure: ["[[Spearphishing Attachment]]","[[Malicious RAR archive]]","[[Exploit Public-Facing Application]]","[[SQL injection]]","[[Cron-based scheduled execution]]","[[TOR exit nodes]]","[[Compromised SOHO routers]]"]
ttps: ["[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]","[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]","[[20_Entities/07_TTPs/T1053.003 - Scheduled Task/Job: Cron]]","[[20_Entities/07_TTPs/T1021.004 - Remote Services: SSH]]","[[20_Entities/07_TTPs/T1021.005 - Remote Services: VNC]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — GCMAN (G0036) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0036/","Kaspersky Securelist — APT-style bank robberies increase with Metel, GCMAN and Carbanak 2.0 attacks (2016-02-08): https://securelist.com/apt-style-bank-robberies-increase-with-metel-gcman-and-carbanak-2-0-attacks/73638/","Kaspersky Resource Center — GCMAN threat definition: https://me-en.kaspersky.com/resource-center/threats/gcman","Kaspersky APT TI Portal — GCMAN malware logbook entry: https://apt.securelist.com/apt/gcman","SecurityWeek — Hackers Steal Money from Banks via APT-Style Attacks (2016-02-08): https://www.securityweek.com/hackers-steal-money-banks-apt-style-attacks/"]
tags: ["threat-actor","gcman","g0036","financial-crime","bank-fraud"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# GCMAN

## 1. BLUF / Executive Summary
GCMAN (MITRE ATT&CK **G0036**) is a financially motivated threat group associated with bank intrusions aimed at **fraudulent transfers to e-currency services**. Public reporting describes a pattern of **spearphishing with malicious archive attachments**, lateral movement using **legitimate remote and pentesting tools** (e.g., PuTTY, VNC, Meterpreter), and the use of **scheduled execution** (cron) to automate transaction generation. Reporting also notes **SQL injection** against public-facing services as a path to initial access in at least one investigated case.

## 2. Attribution Notes
- GCMAN is tracked in MITRE ATT&CK as **G0036**, with sourcing tied to public reporting by Kaspersky.
- Public sources do not provide a definitive sponsor or national attribution. Some reporting focuses on incidents handled in Russia, but that alone is insufficient to attribute origin or tasking.

## 3. Motivations & Objectives
- **Primary motivation:** direct financial gain via bank fraud.
- **Operational objectives:** obtain durable access, expand privileges and reach via lateral movement, and execute concealed, repeatable transfer workflows to move money to e-currency services.

## 4. Targeting Profile
- **Primary victims:** financial institutions/banks.
- **Geography:** reporting includes incidents investigated in Russia and describes a broader “worldwide” footprint in threat summaries.

## 5. Tradecraft Overview
- **Initial access:** spearphishing with malicious RAR archives that present as benign documents; separate reporting also describes exploitation of public web services via SQL injection preceding later cash-out attempts.
- **Lateral movement:** reliance on “living-off-the-land” or legitimate tooling (PuTTY/SSH, VNC, Meterpreter) rather than exclusively custom malware.
- **Automation of fraud:** planting and scheduling scripts (cron) to generate or post transactions at regular intervals, enabling sustained theft while attempting to remain under normal monitoring thresholds.
- **Operational security:** reporting notes use of anonymization/relay infrastructure (e.g., TOR) and compromised home routers as part of attack-source diversity in at least one described intrusion.

## 6. MITRE ATT&CK Mapping
- Initial Access
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
  - [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- Execution / Persistence
  - [[20_Entities/07_TTPs/T1053.003 - Scheduled Task/Job: Cron]]
- Lateral Movement
  - [[20_Entities/07_TTPs/T1021.004 - Remote Services: SSH]]
  - [[20_Entities/07_TTPs/T1021.005 - Remote Services: VNC]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/GCMAN]] — backdoor/malware described in banking intrusions; notable for GCC-compiled components in public reporting.
- [[30_CIPHER/05_Malware/PuTTY]] — used to facilitate SSH-based movement within victim environments.
- [[30_CIPHER/05_Malware/VNC]] — used for remote control and lateral movement.
- [[30_CIPHER/05_Malware/Meterpreter]] / [[30_CIPHER/05_Malware/Metasploit]] — legitimate pentesting framework component referenced in reporting as used operationally post-compromise.

## 8. Infrastructure Patterns
- [[Spearphishing Attachment]] delivery via [[Malicious RAR archive]] masquerading as documents.
- [[Exploit Public-Facing Application]] with [[SQL injection]] against exposed banking-adjacent services (reported in at least one intrusion narrative).
- [[Cron-based scheduled execution]] to automate periodic transaction generation/posting.
- Diverse “attack source” posture using [[TOR exit nodes]] and [[Compromised SOHO routers]] (reported), complicating simple source-based blocking.

## 9. Campaign History
- **2015 (reported first known samples):** public summaries place first observed GCMAN malware samples in 2015.
- **2016 (public disclosure):** Kaspersky reporting publicly describes GCMAN operations, including spearphishing delivery and use of legitimate tools for lateral movement, and scheduled scripts to generate transfers to e-currency services.
- **Inactive since 2017 (reported):** Kaspersky’s APT TI portal summary for GCMAN malware states inactivity since 2017; MITRE’s group entry remains primarily sourced to the 2016 public reporting.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize controls and monitoring for **phishing with archive attachments** in financial workflows, and treat unusual archive-to-executable execution patterns as high risk.
- Increase detection emphasis on **legitimate-tool abuse** (remote admin + pentest utilities) inside high-value banking segments, especially when paired with unusual authentication paths or remote service usage.
- In fraud-sensitive environments, correlate endpoint/server activity with **transaction system telemetry** to identify automation-like patterns and anomalous posting behavior.
- Ensure exposed banking-adjacent services receive rigorous security assurance to reduce likelihood of **public-facing exploitation** (including injection classes) becoming a long-dwell access vector.

## 12. Analyst Notes
- GCMAN is a relatively narrow-scope actor profile in public sources compared to larger banking intrusion ecosystems; avoid over-linking it to other “banking APT-style” clusters without explicit source support.
- Status reporting (“inactive since 2017”) is derived from a vendor portal summary and should be treated as **best-available open reporting**, not definitive proof of cessation.

## 13. Further Reading / External Resources
- MITRE ATT&CK — GCMAN (G0036): https://attack.mitre.org/groups/G0036/
- Kaspersky Securelist (primary narrative): https://securelist.com/apt-style-bank-robberies-increase-with-metel-gcman-and-carbanak-2-0-attacks/73638/
- Kaspersky Threat Definition: https://me-en.kaspersky.com/resource-center/threats/gcman
- Kaspersky APT TI Portal summary: https://apt.securelist.com/apt/gcman
- SecurityWeek (secondary coverage): https://www.securityweek.com/hackers-steal-money-banks-apt-style-attacks/

## 14. References
1. MITRE ATT&CK. “GCMAN (G0036).” (Last Modified 2025-04-25). https://attack.mitre.org/groups/G0036/
2. Kaspersky Securelist. “APT-style bank robberies increase with Metel, GCMAN and Carbanak 2.0 attacks.” (2016-02-08). https://securelist.com/apt-style-bank-robberies-increase-with-metel-gcman-and-carbanak-2-0-attacks/73638/
3. Kaspersky Resource Center. “GCMAN: how to steal $200 per minute (Threat Definition).” (Accessed 2025-12-25). https://me-en.kaspersky.com/resource-center/threats/gcman
4. Kaspersky APT Threat Intelligence Portal. “GCMAN malware infects financial institutions.” (Accessed 2025-12-25). https://apt.securelist.com/apt/gcman
5. SecurityWeek. “Hackers Steal Money from Banks via APT-Style Attacks.” (2016-02-08). https://www.securityweek.com/hackers-steal-money-banks-apt-style-attacks/
---
