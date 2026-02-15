---
entity_type: campaign

campaign_name: "Night Dragon"
campaign_id: "C0002"

associated_actors: []
suspected_actors: []

attribution_confidence: "2-medium"
confidence_notes: "Multiple public sources assessed the activity as consistent with China-based operators, but there is no definitive, widely accepted linkage to a specific named threat actor group in the core public reporting cited here."

first_observed: "2009-11"
last_observed: "2011-02"
campaign_status: "concluded"

primary_objectives:
  - "data_theft"
  - "espionage_like"
secondary_objectives:
  - "competitive_advantage"
  - "long_term_access"

target_sectors:
  - "Oil & Gas"
  - "Energy"
  - "Petrochemical"
target_regions:
  - "Kazakhstan"
  - "Taiwan"
  - "Greece"
  - "United States"
target_technologies:
  - "Windows endpoints and servers"
  - "Public-facing web applications/servers (extranet portals)"
  - "VPN / external remote access services"
  - "Active Directory environments"
  - "SCADA-adjacent repositories (project/operations data)"

initial_access_vectors:
  - "Exploit Public-Facing Application"
  - "Spearphishing Link"
  - "Valid Accounts"

key_ttp_themes:
  - "Extranet/web server exploitation for entry and staging"
  - "Credential access via dumping + cracking"
  - "Commodity RATs and admin utilities (remote control + lateral movement)"
  - "Dynamic DNS / hosted or compromised servers for C2"
  - "Data staging on compromised infrastructure prior to exfiltration"

associated_ttps:
  - "T1190 - Exploit Public-Facing Application"
  - "T1566.002 - Spearphishing Link"
  - "T1204.001 - Malicious Link"
  - "T1133 - External Remote Services"
  - "T1078 - Valid Accounts"
  - "T1078.002 - Domain Accounts"
  - "T1003.002 - Security Account Manager"
  - "T1110.002 - Password Cracking"
  - "T1550.002 - Pass the Hash"
  - "T1059.003 - Windows Command Shell"
  - "T1083 - File and Directory Discovery"
  - "T1033 - System Owner/User Discovery"
  - "T1005 - Data from Local System"
  - "T1114.001 - Local Email Collection"
  - "T1074.002 - Remote Data Staging"
  - "T1071.001 - Web Protocols"
  - "T1568 - Dynamic Resolution"
  - "T1008 - Fallback Channels"
  - "T1219 - Remote Access Tools"
  - "T1105 - Ingress Tool Transfer"
  - "T1608.001 - Upload Malware"
  - "T1112 - Modify Registry"
  - "T1562.001 - Disable or Modify Tools"
  - "T1027.002 - Software Packing"
  - "T1027.013 - Encrypted/Encoded File"
  - "T1583.004 - Virtual Private Server"
  - "T1584.004 - Virtual Private Server"
  - "T1588.001 - Malware"
  - "T1588.002 - Tool"

malware_families:
  - "[[30_CIPHER/05_Malware/S0073 - ASPXSpy|ASPXSpy (S0073)]]"
  - "[[30_CIPHER/05_Malware/S0350 - zwShell|zwShell (S0350)]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0110 - at|at (S0110)]]"
  - "[[30_CIPHER/05_Malware/S0008 - gsecdump|gsecdump (S0008)]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]"

infrastructure_patterns:
  - "[[Compromised Web Server C2]]"
  - "[[Hosted C2 Infrastructure]]"
  - "[[Dynamic DNS]]"
  - "[[Extranet Portal Exploitation]]"
  - "[[Staging on DMZ Systems]]"

notable_victims: []
related_incidents: []

risk_level: "high"
impact_assessment: "Night Dragon targeted energy-sector organizations to obtain sensitive operational, financial, and project data (including SCADA-adjacent artifacts) using a blend of web-server compromise, credential theft, and commodity remote administration tooling."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0002/"
  - "https://www.mcafee.com/blogs/wp-content/uploads/2011/02/McAfee_NightDragon_wp_draft_to_customersv1-1.pdf"
  - "https://www.cisa.gov/news-events/ics-advisories/icsa-11-041-01a"
  - "https://www.reuters.com/article/technology/chinese-hackers-infiltrated-five-energy-firms-mcafee-idUSTRE7190XP/"
  - "https://news.sophos.com/en-us/2011/02/10/night-dragon-hackers-target-energy-and-oil-industry/"
  - "https://www.eweek.com/security/mcafee-night-dragon-cyber-attack-unsophisticated-but-effective/"
  - "https://www.darkreading.com/cyberattacks-data-breaches/-night-dragon-attacks-threaten-major-energy-firms"
  - "https://www.darkreading.com/cyberattacks-data-breaches/schwartz-on-security-unraveling-night-dragon-attacks"
  - "https://www.forbes.com/sites/williampentland/2011/02/19/night-dragon-attacks-target-technology-in-energy-industry/"

tlp_classification: "TLP:CLEAR"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Night Dragon (C0002)

## 1. Campaign Overview
Night Dragon is a cyber intrusion campaign targeting **oil, energy, and petrochemical** organizations, described publicly as focused on theft of sensitive corporate and operational information. Reporting characterizes the activity as effective and persistent, using a blend of **public-facing system compromise**, **credential theft**, and **commodity remote access tooling** to access internal resources and **stage data** for exfiltration.

The campaign is frequently referenced in the context of energy-sector threat activity because it highlights how compromises of corporate IT environments can expose **SCADA-adjacent documentation and project artifacts** (even where operational systems are segmented).

## 2. Attribution Assessment
Public reporting commonly assessed Night Dragon as consistent with **China-based operators**, but the most cited open sources do not provide a definitive mapping to a specific named threat actor group. This note therefore treats attribution as **assessed** rather than **confirmed**.

**Attribution Confidence: 2-medium**

## 3. Objectives & Intent
Primary intent appears to be **data theft** aligned with **espionage-like** outcomes:
- Theft of operational and project documentation (including SCADA-adjacent artifacts accessible from corporate IT)
- Collection of internal files and email
- Credential capture enabling broader access and long-term presence

Secondary intent likely included **competitive advantage** and **long-term access** through continued credential use and remote tooling.

## 4. Targeting Analysis

### Sectors Targeted
- Oil & Gas
- Energy
- Petrochemical

### Regions Targeted
- Kazakhstan
- Taiwan
- Greece
- United States

### Technologies / Platforms Targeted
- Windows endpoints and servers
- Public-facing extranet portals / web applications
- VPN and external remote access pathways
- AD environments and file repositories
- SCADA-adjacent project/document repositories accessible via IT networks

## 5. Campaign Tradecraft

### High-Level Tradecraft Summary
A commonly described workflow is:
1) Initial access via **public-facing application compromise** (frequently summarized as extranet/web server exploitation) and/or **spearphishing links**, plus **compromised VPN credentials**  
2) Follow-on **credential access** (including hash acquisition and cracking)  
3) Remote control and lateral movement using commodity tooling  
4) **Discovery + collection**, with **remote staging** on compromised systems (including DMZ/web servers)  
5) Exfiltration and C2 over web protocols, supported by resilient infrastructure patterns (e.g., dynamic DNS, hosted servers)

## 6. MITRE ATT&CK Alignment

### Techniques Observed
- [[T1190 - Exploit Public-Facing Application]]
- [[T1566.002 - Spearphishing Link]]
- [[T1204.001 - Malicious Link]]
- [[T1133 - External Remote Services]]
- [[T1078 - Valid Accounts]]
- [[T1078.002 - Domain Accounts]]
- [[T1003.002 - Security Account Manager]]
- [[T1110.002 - Password Cracking]]
- [[T1550.002 - Pass the Hash]]
- [[T1059.003 - Windows Command Shell]]
- [[T1083 - File and Directory Discovery]]
- [[T1033 - System Owner/User Discovery]]
- [[T1005 - Data from Local System]]
- [[T1114.001 - Local Email Collection]]
- [[T1074.002 - Remote Data Staging]]
- [[T1071.001 - Web Protocols]]
- [[T1568 - Dynamic Resolution]]
- [[T1008 - Fallback Channels]]
- [[T1219 - Remote Access Tools]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1608.001 - Upload Malware]]
- [[T1112 - Modify Registry]]
- [[T1562.001 - Disable or Modify Tools]]
- [[T1027.002 - Software Packing]]
- [[T1027.013 - Encrypted/Encoded File]]
- [[T1583.004 - Virtual Private Server]]
- [[T1584.004 - Virtual Private Server]]
- [[T1588.001 - Malware]]
- [[T1588.002 - Tool]]

### Notable Tradecraft Characteristics
- Use of **extranet/web server compromise** as both entry point and operational staging surface
- Heavy reliance on **commodity tooling** rather than purely bespoke malware
- Credential workflow combining **hash acquisition + cracking** and alternate authentication
- Use of **dynamic DNS** and resilient infrastructure patterns for continuity

## 7. Malware & Tooling

### Malware Families
- [[30_CIPHER/05_Malware/S0073 - ASPXSpy|ASPXSpy (S0073)]]
- [[30_CIPHER/05_Malware/S0350 - zwShell|zwShell (S0350)]]

### Tools (LOLBins / COTS / Frameworks)
- [[30_CIPHER/05_Malware/S0110 - at|at (S0110)]]
- [[30_CIPHER/05_Malware/S0008 - gsecdump|gsecdump (S0008)]]
- [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]

## 8. Infrastructure & Operational Patterns
- **Compromised web servers** used for footholds and data staging
- **Hosted servers/VPS** used for C2 and operational infrastructure
- **Dynamic DNS** for flexible resolution
- **Fallback/alternate channels** to sustain access even if primary infrastructure is disrupted

## 9. Timeline of Campaign Activity

### Timeline (Markdown)
| Date | Event |
|---|---|
| **2009-11** | First observed activity window begins (campaign observation period). |
| **2011-02** | Last observed activity window (campaign observation period). |
| **2011-02-10** | McAfee publishes the “Night Dragon” report describing targeting and tradecraft. |
| **2011-02-10** | Reuters publishes coverage based on McAfee findings. |
| **2011-02-10** | Sophos publishes coverage summarizing targeting of energy/oil industry. |
| **2011-02-11** | Dark Reading publishes coverage framing campaign risk to energy firms. |
| **2011-02-16** | Dark Reading follow-up (“Schwartz on Security”) expands narrative and context. |
| **2011-02-19** | Forbes publishes additional coverage framing impact to energy industry. |
| **2018-09-06** | CISA updates ICS advisory referencing the Night Dragon report for ICS stakeholders. |

### Timeline (Chronos)
```chronos
- [2009-11]: First observed activity window begins (campaign observation period).
- [2011-02]: Last observed activity window (campaign observation period).
- [2011-02-10]: McAfee publishes the “Night Dragon” report describing targeting and tradecraft.
- [2011-02-10]: Reuters publishes coverage based on McAfee findings.
- [2011-02-10]: Sophos publishes coverage summarizing targeting of energy/oil industry.
- [2011-02-11]: Dark Reading publishes coverage framing campaign risk to energy firms.
- [2011-02-16]: Dark Reading follow-up (“Schwartz on Security”) expands narrative and context.
- [2011-02-19]: Forbes publishes additional coverage framing impact to energy industry.
- [2018-09-06]: CISA updates ICS advisory referencing the Night Dragon report for ICS stakeholders.
```

## 10. Notable Victims & Impact

### Victim Profile
Public reporting describes victims as energy-sector organizations (oil, gas, petrochemical) and related individuals/executives. Many sources do not comprehensively enumerate victims publicly.

### Operational Impact
Likely impacts (as described broadly in reporting) include theft of:
- Proprietary operational and production-related documentation
- Financial and project-financing materials
- Internal files and email archives
- SCADA-adjacent project files accessible from corporate IT networks

## 11. Related Campaigns & Activity
No definitive related-campaign linkage is asserted in the cited sources.  
**Pivot idea:** compare the combination of *extranet compromise → credential theft → staging on DMZ/web servers → commodity RAT/admin tooling* with other energy-sector intrusions in adjacent timeframes.

## 12. Known Indicators (Contextual)
*(Pattern-based pivots only; do not treat as durable IOCs.)*
- SQLi/injection patterns and anomalous writes on internet-facing extranet portals
- Unusual VPN logons (new geos/devices/times) for privileged or service accounts
- Hash dumping + cracking workflow artifacts and execution telemetry
- Remote execution and lateral tooling patterns (e.g., PsExec service creation)
- Outbound web-protocol C2 from atypical processes paired with dynamic DNS resolution
- Large or unusual data staging activity on web/DMZ systems

## 13. Defensive Considerations
- Public-facing application security:
  - WAF coverage and injection-class detection
  - Hardening and monitoring of DMZ/web servers for anomalous file writes and privilege changes
- External remote access controls:
  - MFA + conditional access + anomaly detection for VPN
  - Rapid credential rotation and session invalidation on suspicious access
- Credential access detection:
  - Monitor for SAM/credential dumping behaviors and offline cracking prep
  - Alert on tools and artifacts consistent with hash dumping and pass-the-hash
- Lateral movement and staging controls:
  - Detect PsExec-like remote execution patterns
  - Monitor for abnormal staging to DMZ systems and subsequent outbound transfers

## 14. Analyst Notes
- Attribution is **assessed** and not confirmed; do not map to a named group without additional sourced evidence.
- Several public narratives emphasize effectiveness through basic tradecraft; prioritize visibility and hygiene (patching, web app telemetry, identity security, and staging detection).
- Recommended pivots:
  1) Web server/app logs for injection patterns + anomalous file writes
  2) VPN identity telemetry (impossible travel, new devices, admin logons)
  3) Process creation for credential dumping tooling and remote execution utilities
  4) Data staging detection on DMZ systems (size/volume anomalies + outbound connections)
- Confidence recap:
  - Attribution: **medium**
  - Tradecraft completeness: **medium**
  - Victim enumeration/impact specificity: **low**

## 15. Further Reading / External Resources
- McAfee Night Dragon whitepaper (core technical narrative)
- MITRE ATT&CK campaign entry (structured technique/software mapping)
- Reuters (contemporaneous coverage)
- Sophos + Dark Reading coverage (accessible summaries and context)
- CISA ICS advisory update (ICS stakeholder framing)

## 16. References (APA)
- Cybersecurity and Infrastructure Security Agency. (2018, September 6). *ICSA-11-041-01A: McAfee Night Dragon Report (Update A)*. https://www.cisa.gov/news-events/ics-advisories/icsa-11-041-01a
- Dark Reading. (2011, February 11). *‘Night Dragon’ attacks threaten major energy firms*. https://www.darkreading.com/cyberattacks-data-breaches/-night-dragon-attacks-threaten-major-energy-firms
- McAfee Foundstone Professional Services & McAfee Labs. (2011, February 10). *Global Energy Cyberattacks: “Night Dragon”*. https://www.mcafee.com/blogs/wp-content/uploads/2011/02/McAfee_NightDragon_wp_draft_to_customersv1-1.pdf
- MITRE ATT&CK. (n.d.). *Night Dragon (C0002)*. https://attack.mitre.org/campaigns/C0002/
- Pentland, W. (2011, February 19). *Night Dragon attacks target technology in energy industry*. *Forbes*. https://www.forbes.com/sites/williampentland/2011/02/19/night-dragon-attacks-target-technology-in-energy-industry/
- Reuters. (2011, February 10). *Chinese hackers infiltrated five energy firms: McAfee*. https://www.reuters.com/article/technology/chinese-hackers-infiltrated-five-energy-firms-mcafee-idUSTRE7190XP/
- Schwartz, M. J. (2011, February 16). *Schwartz on Security: Unraveling Night Dragon attacks*. *Dark Reading*. https://www.darkreading.com/cyberattacks-data-breaches/schwartz-on-security-unraveling-night-dragon-attacks
- Sophos. (2011, February 10). *Night Dragon hackers target energy and oil industry*. https://news.sophos.com/en-us/2011/02/10/night-dragon-hackers-target-energy-and-oil-industry/
- eWEEK. (2011, February 10). *McAfee: Night Dragon cyber-attack unsophisticated but effective*. https://www.eweek.com/security/mcafee-night-dragon-cyber-attack-unsophisticated-but-effective/
