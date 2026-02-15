---
entity_type: campaign

campaign_name: "Operation Dream Job / Operation North Star / Operation Interception"
campaign_id: "C0022"

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|G0032 - Lazarus Group]]"
suspected_actors: []

attribution_confidence: "3-high"
confidence_notes: "MITRE ATT&CK explicitly associates the campaign cluster to Lazarus Group and references multiple vendor investigations describing social engineering, tooling, and malware families."

first_observed: "2019-09"
last_observed: "2020-08"
campaign_status: "concluded"

primary_objectives: ["espionage"]
secondary_objectives: ["initial_access", "credential_access", "data_theft"]

target_sectors: ["defense", "aerospace", "military", "technology"]
target_regions: ["Europe", "United States", "global"]
target_technologies: ["Windows", "LinkedIn", "email", "IIS", "code signing"]

initial_access_vectors: ["spearphishing_attachment", "spearphishing_link", "spearphishing_via_service", "social_engineering"]
key_ttp_themes: ["hr_impersonation", "job_lure_social_engineering", "staged_payloads", "code_signing_abuse", "cloud_exfiltration"]

malware_families:
  - "[[30_CIPHER/05_Malware/S0694 - DRATzarus|S0694 - DRATzarus]]"
  - "[[30_CIPHER/05_Malware/S0678 - Torisma|S0678 - Torisma]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0174 - Responder|S0174 - Responder]]"

infrastructure_patterns: ["compromised_servers_hosting_payloads", "linkedin_lure_accounts", "cloud_storage_exfiltration"]
notable_victims: ["defense/aerospace employees (multiple organizations)"]
related_incidents: []

risk_level: "high"
impact_assessment: "Sustained social-engineering operations against defense/aerospace with multi-stage malware delivery, credential access tooling, and exfiltration paths including cloud storage."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0022/"
  - "https://www.clearskysec.com/operation-dream-job/"
  - "https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-campaign/"
  - "https://www.welivesecurity.com/2020/06/17/operation-interception-targeted-attacks-european-aerospace-military-companies/"
  - "https://thehackernews.com/2022/08/north-korea-hackers-spotted.html"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
**C0022** is a cluster of related operations—**Operation Dream Job**, **Operation North Star**, and **Operation Interception**—associated with **[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|G0032 - Lazarus Group]]**. Activity spans roughly **Sep 2019 to Aug 2020**, leveraging **job-themed lures** and **HR impersonation** (notably via **LinkedIn**) to deliver malware and tools to targets in defense/aerospace and related sectors.

---

## Attribution Assessment
Attribution confidence is **high** based on MITRE ATT&CK association and multiple vendor investigations describing consistent Lazarus tradecraft, malware families, and operational patterns.

---

## Objectives & Intent
- **Primary:** espionage / intelligence collection
- **Secondary:** initial access enablement, credential access, and data exfiltration

---

## Targeting Analysis
### Sectors Targeted
- Defense, aerospace, military-adjacent organizations and personnel
- Technology organizations and individuals relevant to those sectors

### Regions Targeted
- Europe and the U.S. prominently in reporting, with global victim potential via social platforms

### Technologies / Platforms Targeted
- Social platforms (LinkedIn) and email delivery
- Windows endpoints; IIS servers in parts of the activity
- Code signing usage/abuse reported for some tooling

---

## Campaign Tradecraft
### High-Level Tradecraft Summary
The campaign uses **tailored job offers** and impersonation of recruiters/HR to induce targets to open malicious files or links. Multi-stage payloads are delivered, with subsequent tool download/staging, credential access tooling, and exfiltration—sometimes leveraging **cloud storage**.

---

## MITRE ATT&CK Alignment
### Techniques Observed (Selected)
- [[T1566.001 - Spearphishing Attachment]]
- [[T1566.002 - Spearphishing Link]]
- [[T1566.003 - Spearphishing via Service]]
- [[T1593.001 - Social Media]]
- [[T1656 - Impersonation]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1608.001 - Upload Malware]]
- [[T1608.002 - Upload Tool]]
- [[T1553.002 - Code Signing]]
- [[T1027.002 - Software Packing]]
- [[T1027.013 - Encrypted/Encoded File]]
- [[T1218.010 - Regsvr32]]
- [[T1218.011 - Rundll32]]
- [[T1053.005 - Scheduled Task]]
- [[T1047 - Windows Management Instrumentation]]
- [[T1220 - XSL Script Processing]]
- [[T1221 - Template Injection]]
- [[T1070.004 - File Deletion]]
- [[T1567.002 - Exfiltration to Cloud Storage]]
- [[T1534 - Internal Spearphishing]]
- [[T1505.004 - IIS Components]]

### Notable Tradecraft Characteristics
- Recruiter/HR **impersonation** with interactive grooming (interviews, job descriptions)
- Staged payload hosting on compromised infrastructure
- Exfiltration via cloud tooling (e.g., Dropbox CLI variants reported)

---

## Malware & Tooling
### Malware Families
- [[30_CIPHER/05_Malware/S0694 - DRATzarus|S0694 - DRATzarus]]
- [[30_CIPHER/05_Malware/S0678 - Torisma|S0678 - Torisma]]

### Tools
- [[30_CIPHER/05_Malware/S0174 - Responder|S0174 - Responder]]

---

## Infrastructure & Operational Patterns
- LinkedIn lure accounts and recruiter personas
- Compromised servers hosting staged malware and tools
- Use of cloud storage for exfiltration in some reporting

---

## Timeline of Campaign Activity (Chronos)
```chronos
- [2019-09]: Earliest observed activity window begins (MITRE first seen).
- [2020-06-17]: Vendor report published on Operation Interception targeting European aerospace/military.
- [2020-07-29]: Vendor report published on Operation North Star campaign activity.
- [2020-08]: Last observed activity window ends (MITRE last seen).
- [2020-08-13]: Vendor report published on Operation Dream Job activity and tradecraft.
- [2020-11-05]: Additional vendor reporting expands details on Operation North Star.
- [2022-08-17]: Public reporting highlights continued job-lure operations including macOS targeting.
```

## Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2019-09 | Earliest observed activity window begins |
| 2020-06-17 | Report published on Operation Interception targeting aerospace/military |
| 2020-07-29 | Report published on Operation North Star campaign |
| 2020-08 | Last observed activity window ends |
| 2020-08-13 | Report published on Operation Dream Job activity |
| 2020-11-05 | Follow-on reporting expands Operation North Star details |
| 2022-08-17 | Public reporting highlights job-lure operations including macOS |

---

## Defensive Considerations
- Implement LinkedIn/HR impersonation awareness and strict out-of-band verification for recruiting outreach.
- Harden email and web isolation for document-based lures; restrict Office template retrieval paths.
- Monitor for `regsvr32`, `rundll32`, and WMI/XSL execution chains tied to remote payload fetch.
- Track newly created scheduled tasks and suspicious deletion of staging artifacts post-execution.

---

## Analyst Notes
C0022 emphasizes that high-success intrusions can be driven by **human-layer compromise** (recruiting workflows) combined with staged technical payloads. Defenses require both security controls and process validation.

---

## References (APA)
- MITRE ATT&CK. (2025, April 16). *Operation Dream Job / Operation North Star / Operation Interception (C0022)*. Retrieved 2026-01-03 from https://attack.mitre.org/campaigns/C0022/
- ClearSky Research Team. (2020, August 13). *Operation “Dream Job” Widespread North Korean Espionage Campaign*. Retrieved 2026-01-03 from https://www.clearskysec.com/operation-dream-job/
- Cashman, M. (2020, July 29). *Operation North Star Campaign*. McAfee. Retrieved 2026-01-03 from https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-campaign/
- Breitenbacher, D., & Osis, K. (2020, June 17). *OPERATION IN(TER)CEPTION: Targeted Attacks Against European Aerospace and Military Companies*. ESET WeLiveSecurity. Retrieved 2026-01-03 from https://www.welivesecurity.com/2020/06/17/operation-interception-targeted-attacks-european-aerospace-military-companies/
- Beek, C. (2020, November 5). *Operation North Star: Behind The Scenes*. McAfee. Retrieved 2026-01-03 from https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/
- Lakshmanan, R. (2022, August 17). *North Korea hackers spotted targeting job seekers with macOS malware*. The Hacker News. Retrieved 2026-01-03 from https://thehackernews.com/2022/08/north-korea-hackers-spotted.html
