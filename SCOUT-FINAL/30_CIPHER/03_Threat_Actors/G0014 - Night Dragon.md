---
entity_type: threat_actor
actor_name: "Night Dragon"
common_name: "Night Dragon"
actor_id: "G0014"
actor_type: "Cyber espionage campaign (unidentified actors; suspected China-based)"
aliases: ["Night Dragon Operation"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2009-11"
last_seen: "2011-02"
status: "Unknown"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Competitive and strategic intelligence collection in the energy sector", "Collection of operational and financial data", "Access to industrial/SCADA-adjacent information (reported)"]
victimology_summary: "Night Dragon is documented as a cyber espionage campaign targeting oil, energy, and petrochemical companies, along with executives/individuals in Kazakhstan, Taiwan, Greece, and the United States. Reporting describes collection focused on oil and gas field production systems, financials, and data related to SCADA environments. The actors were not publicly identified; researchers assessed, based on observed techniques and infrastructure, that the activity likely involved a China-based threat group."
target_sectors: ["Oil & Gas", "Energy", "Petrochemical", "Industrial (ICS/SCADA-adjacent; reported)"]
target_regions: ["Kazakhstan", "Taiwan", "Greece", "United States"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/ASPXSpy]]", "[[30_CIPHER/05_Malware/zwShell]]"]
tools: ["[[30_CIPHER/05_Malware/gsecdump]]", "[[30_CIPHER/05_Malware/PsExec]]", "[[30_CIPHER/05_Malware/at]]", "[[30_CIPHER/05_Malware/Cain & Abel]]"]
infrastructure: ["[[Dynamic DNS]]", "[[Purchased Hosted Servers]]", "[[Compromised Web Servers]]", "[[Company Extranet Servers]]", "[[Web Shell]]", "[[External Remote Services]]", "[[VPN Accounts]]", "[[SQL Injection]]"]
ttps: ["[[20_Entities/07_TTPs/T1583.004 - Acquire Infrastructure: Server]]", "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]", "[[20_Entities/07_TTPs/T1110.002 - Brute Force: Password Cracking]]", "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]", "[[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]]", "[[20_Entities/07_TTPs/T1005 - Data from Local System]]", "[[20_Entities/07_TTPs/T1074.002 - Data Staged: Remote Data Staging]]", "[[20_Entities/07_TTPs/T1568 - Dynamic Resolution]]", "[[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]]", "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]", "[[20_Entities/07_TTPs/T1133 - External Remote Services]]", "[[20_Entities/07_TTPs/T1008 - Fallback Channels]]", "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]", "[[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]", "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]", "[[20_Entities/07_TTPs/T1112 - Modify Registry]]", "[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]", "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]", "[[20_Entities/07_TTPs/T1588.001 - Obtain Capabilities: Malware]]", "[[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]", "[[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]", "[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]", "[[20_Entities/07_TTPs/T1219 - Remote Access Tools]]", "[[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]", "[[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]", "[[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]", "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]", "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]", "[[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Campaign C0002): Night Dragon (Last modified 2024-04-11)","McAfee Foundstone & McAfee Labs (2011-02-10): Global Energy Cyberattacks: Night Dragon (PDF)","CISA ICS Advisory (ICSA-11-041-01A, 2018-09-06): McAfee Night Dragon Report (Update A)"]
tags: ["threat-actor", "campaign", "cyber-espionage", "energy-sector", "oil-and-gas", "night-dragon"]
---

# Night Dragon

## 1. BLUF / Executive Summary
Night Dragon is a documented cyber espionage campaign (first publicly described in early 2011) that targeted oil, energy, and petrochemical organizations, as well as selected executives/individuals in Kazakhstan, Taiwan, Greece, and the United States. The operators were not publicly identified, but researchers assessed—based on observed tactics, infrastructure, and activity patterns—that the campaign likely involved a China-based threat group. Reported collection priorities included oil and gas production-related information, financial data, and SCADA-adjacent data sources.

## 2. Attribution Notes
- Public reporting consistently treats Night Dragon as a **campaign name** rather than a uniquely identified, long-lived intrusion set with a stable public identity.
- MITRE ATT&CK documents the actors as **unidentified** and characterizes the “China-based” assessment as an analyst judgment derived from observed operational signals rather than a public attribution to a named government organization.
- Attribution confidence is **low** due to limited public, primary-source attribution evidence and the age of foundational reporting.

## 3. Motivations & Objectives
- **Motivation:** Strategic and competitive intelligence collection within the energy sector.
- **Objectives:** Obtain sensitive business and operational data (including project-financing and production-related information) and access internal systems enabling sustained collection, including data sources adjacent to industrial/SCADA environments (as reported).

## 4. Targeting Profile
- **Primary sectors:** Oil & gas, energy, petrochemical.
- **Victim profile:** Both organizations and select high-value individuals/executives.
- **Regions reported:** Kazakhstan, Taiwan, Greece, and the United States.

## 5. Tradecraft Overview
- **Initial access paths (reported):** Exploitation of public-facing applications (including SQL injection against extranet-facing servers) consistent with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]], and spearphishing that lured users to click links leading to malware download consistent with [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]] and [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]].
- **Credential-centric operations:** Password cracking and reuse plus pass-the-hash behavior consistent with [[20_Entities/07_TTPs/T1110.002 - Brute Force: Password Cracking]] and [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]], including credential dumping from the SAM consistent with [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]].
- **Remote access enablement:** Use of remote administration and external remote services (including compromised VPN accounts) consistent with [[20_Entities/07_TTPs/T1219 - Remote Access Tools]] and [[20_Entities/07_TTPs/T1133 - External Remote Services]].
- **Collection and staging:** File and email collection from compromised systems consistent with [[20_Entities/07_TTPs/T1005 - Data from Local System]] and [[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]], with remote staging on company web servers consistent with [[20_Entities/07_TTPs/T1074.002 - Data Staged: Remote Data Staging]].
- **Operational concealment:** Disabling security tooling and enabling direct internet comms (reported) consistent with [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]], plus packing/encoding for some components consistent with [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]] and [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583.004 - Acquire Infrastructure: Server]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1110.002 - Brute Force: Password Cracking]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1074.002 - Data Staged: Remote Data Staging]]
- [[20_Entities/07_TTPs/T1568 - Dynamic Resolution]]
- [[20_Entities/07_TTPs/T1114.001 - Email Collection: Local Email Collection]]
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1133 - External Remote Services]]
- [[20_Entities/07_TTPs/T1008 - Fallback Channels]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1112 - Modify Registry]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1588.001 - Obtain Capabilities: Malware]]
- [[20_Entities/07_TTPs/T1588.002 - Obtain Capabilities: Tool]]
- [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1219 - Remote Access Tools]]
- [[20_Entities/07_TTPs/T1608.001 - Stage Capabilities: Upload Malware]]
- [[20_Entities/07_TTPs/T1033 - System Owner/User Discovery]]
- [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1078.002 - Valid Accounts: Domain Accounts]]

## 7. Malware & Tools Used
- **Malware / implants (reported):**
  - [[30_CIPHER/05_Malware/zwShell]]
  - [[30_CIPHER/05_Malware/ASPXSpy]]
- **Tools / utilities (reported):**
  - [[30_CIPHER/05_Malware/gsecdump]]
  - [[30_CIPHER/05_Malware/PsExec]]
  - [[30_CIPHER/05_Malware/at]]
  - [[30_CIPHER/05_Malware/Cain & Abel]]

## 8. Infrastructure Patterns
- Use of [[Purchased Hosted Servers]] and [[Compromised Web Servers]] for command-and-control, aligning with [[20_Entities/07_TTPs/T1583.004 - Acquire Infrastructure: Server]] and [[20_Entities/07_TTPs/T1584.004 - Compromise Infrastructure: Server]].
- Use of [[Dynamic DNS]] for C2 resolution consistent with [[20_Entities/07_TTPs/T1568 - Dynamic Resolution]].
- Use of [[Company Extranet Servers]] as secondary channels consistent with [[20_Entities/07_TTPs/T1008 - Fallback Channels]].
- Deployment of [[Web Shell]] capabilities on compromised servers (e.g., [[30_CIPHER/05_Malware/ASPXSpy]]) to support access and operations.

## 9. Campaign History
- **2009-11 (first seen):** Campaign activity is documented as beginning in November 2009.
- **2011-02 (last seen):** Campaign activity is documented through February 2011 in core reporting and ATT&CK campaign records.
- **2011 (public disclosure):** Major public reporting described the campaign’s focus on global energy firms and highlighted combined use of phishing, public-facing exploitation, credential attacks, and RAT/web-shell tooling.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Reduce exposure of internet-facing applications and monitor for exploitation attempts consistent with [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]].
- Strengthen controls and monitoring around remote access/VPN usage consistent with [[20_Entities/07_TTPs/T1133 - External Remote Services]] and credential abuse consistent with [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Improve detection for credential dumping and replay behaviors consistent with [[20_Entities/07_TTPs/T1003.002 - OS Credential Dumping: Security Account Manager]] and [[20_Entities/07_TTPs/T1550.002 - Use Alternate Authentication Material: Pass the Hash]].
- Monitor for suspicious web-service C2 and staging behaviors consistent with [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] and [[20_Entities/07_TTPs/T1074.002 - Data Staged: Remote Data Staging]], especially in environments holding sensitive energy operations or strategic project data.
- Prioritize visibility into security-control tampering consistent with [[20_Entities/07_TTPs/T1562.001 - Impair Defenses: Disable or Modify Tools]].

## 12. Analyst Notes
- This note models “Night Dragon” as a threat-actor entity for tracking convenience, but the most authoritative framing is a **campaign** with **unidentified operators**.
- Given the age of the reporting baseline (2009–2011), infrastructure and tooling details should be treated as historically informative rather than predictive without corroborating modern sightings.
- Where your environment requires an actor ID, consider tracking the MITRE Campaign ID (**C0002**) in a separate field in your local schema; per SCOUT constraints, `actor_id` remains blank.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Night Dragon (Campaign C0002)  
  https://attack.mitre.org/campaigns/C0002/
- McAfee Foundstone & McAfee Labs — Global Energy Cyberattacks: “Night Dragon” (2011-02-10, PDF)  
  https://www.mcafee.com/blogs/wp-content/uploads/2011/02/McAfee_NightDragon_wp_draft_to_customersv1-1.pdf
- CISA ICS Advisory — McAfee Night Dragon Report (Update A) (ICSA-11-041-01A, 2018-09-06)  
  https://www.cisa.gov/news-events/ics-advisories/icsa-11-041-01a

## 14. References
- MITRE ATT&CK. “Night Dragon (Campaign C0002).” (Last modified 2024-04-11)  
  https://attack.mitre.org/campaigns/C0002/
- McAfee Foundstone Professional Services and McAfee Labs. “Global Energy Cyberattacks: ‘Night Dragon’.” (2011-02-10) PDF  
  https://www.mcafee.com/blogs/wp-content/uploads/2011/02/McAfee_NightDragon_wp_draft_to_customersv1-1.pdf
- CISA. “McAfee Night Dragon Report (Update A).” (ICSA-11-041-01A, 2018-09-06)  
  https://www.cisa.gov/news-events/ics-advisories/icsa-11-041-01a
