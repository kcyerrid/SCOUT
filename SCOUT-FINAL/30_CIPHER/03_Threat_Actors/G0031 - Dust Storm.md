---
entity_type: threat_actor
actor_name: "Dust Storm"
common_name: "Dust Storm"
actor_id: "G0031"
actor_type: "Espionage-focused intrusion set (attributed/suspected state-linked in public reporting)"
aliases: ["Operation Dust Storm", "Stone Panda (reported by some sources)"]
country_of_origin: "China (suspected)"
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2010-01-01"
last_seen: "2016-02-01"
status: "Inactive/Unknown (last publicly observed 2016-02 per MITRE campaign)"
motivations: ["Espionage", "Information theft"]
objectives: ["Long-term access to strategic targets across multiple industries", "Shift focus (by 2015) toward Japanese critical infrastructure-supporting organizations", "Expand collection to mobile (Android) victims by 2015 (reported)"]
victimology_summary: "Dust Storm (G0031) is linked in public reporting and MITRE’s campaign tracking to a long-running intrusion set/campaign (Operation Dust Storm) active from at least 2010 through early 2016. Reported targeting spans multiple industries across Japan, South Korea, the United States, Europe, and several Southeast Asian countries, with a reported shift by 2015 toward Japanese organizations supporting critical infrastructure (energy, oil & gas, finance, transportation, construction). Reporting also notes Android backdoor usage beginning by 2015 against victims in Japan or South Korea."
target_sectors: ["Government/Defense-related intelligence (reported early focus)", "Critical infrastructure (Japan) (reported)", "Electricity generation (reported)", "Oil and natural gas (reported)", "Finance (reported)", "Transportation (reported)", "Construction (reported)"]
target_regions: ["Japan", "South Korea", "United States (reported)", "Europe (reported)", "Southeast Asia (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/gh0st RAT]]", "[[30_CIPHER/05_Malware/PoisonIvy]]", "[[30_CIPHER/05_Malware/Misdat]]", "[[30_CIPHER/05_Malware/Mis-Type]]", "[[30_CIPHER/05_Malware/S-Type]]", "[[30_CIPHER/05_Malware/ZLib]]"]
tools: ["[[30_CIPHER/05_Malware/VBScript]]", "[[30_CIPHER/05_Malware/JavaScript]]", "[[30_CIPHER/05_Malware/mshta.exe]]", "[[30_CIPHER/05_Malware/UPX]]"]
infrastructure: ["[[Dynamic DNS]]", "[[Dynamic resolution]]", "[[Spearphishing]]", "[[Watering hole]]", "[[Domain registration]]", "[[Email accounts for infrastructure]]", "[[Android backdoors]]"]
ttps: ["[[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]", "[[20_Entities/07_TTPs/T1585.002 - Establish Accounts: Email Accounts]]", "[[20_Entities/07_TTPs/T1568 - Dynamic Resolution]]", "[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]", "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]", "[[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]", "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]", "[[20_Entities/07_TTPs/T1518 - Software Discovery]]", "[[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta]]", "[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]", "[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]", "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]", "[[20_Entities/07_TTPs/T1036 - Masquerading]]", "[[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]", "[[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]", "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]", "[[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]", "[[20_Entities/07_TTPs/T1533 - Data from Local System]]", "[[20_Entities/07_TTPs/T1646 - Exfiltration Over C2 Channel]]", "[[20_Entities/07_TTPs/T1420 - File and Directory Discovery]]", "[[20_Entities/07_TTPs/T1636.004 - Protected User Data: SMS Messages]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Dust Storm (G0031): https://attack.mitre.org/groups/G0031/","MITRE ATT&CK — Operation Dust Storm (C0016): https://attack.mitre.org/campaigns/C0016/","Cylance — Operation Dust Storm report PDF: https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf","MITRE ATT&CK — Misdat (S0083): https://attack.mitre.org/software/S0083/","MITRE ATT&CK — Mis-Type (S0084): https://attack.mitre.org/software/S0084/","MITRE ATT&CK — S-Type (S0085): https://attack.mitre.org/software/S0085/","MITRE ATT&CK — ZLib (S0086): https://attack.mitre.org/software/S0086/","MITRE ATT&CK — gh0st RAT (S0032): https://attack.mitre.org/software/S0032/","MITRE ATT&CK — PoisonIvy (S0012): https://attack.mitre.org/software/S0012/"]
tags: ["threat-actor","dust-storm","g0031","operation-dust-storm","espionage","watering-hole","spearphishing","dynamic-dns","japan"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Dust Storm

## 1. BLUF / Executive Summary
Dust Storm (MITRE ATT&CK **G0031**) is associated with **Operation Dust Storm** (MITRE Campaign **C0016**), a long-running cyber-espionage activity set tracked from **2010-01** through **2016-02**. Public reporting describes multi-region targeting (Japan, South Korea, the U.S., Europe, and parts of Southeast Asia) and a reported shift by **2015** toward **Japanese organizations supporting critical infrastructure** (electricity generation, oil & gas, finance, transportation, construction). Reporting also indicates the operators began using **Android backdoors** by **2015**, focusing on victims in Japan or South Korea.

## 2. Attribution Notes
- MITRE’s group entry for Dust Storm (G0031) currently displays a **deprecation warning**, so analysts should rely heavily on the **campaign record (C0016)** and primary reporting when referencing the cluster.
- Public reporting has described the activity as **likely state-linked** and **China-associated**, but these assessments are largely circumstantial in open sources; attribution is therefore treated here as **suspected** with **Low** confidence.
- Some sources refer to “Dust Storm” as “Stone Panda,” but “Stone Panda” is also used in other vendor ecosystems for different clusters; treat the alias as **reported naming**, not a confirmed equivalence.

## 3. Motivations & Objectives
- **Motivation:** Espionage / information theft.
- **Operational objectives (reported):**
  - Establish and maintain access across multiple industries and regions over multiple years.
  - By **2015**, prioritize Japanese entities supporting critical infrastructure.
  - Expand collection and reach to **mobile (Android)** victims by **2015**.

## 4. Targeting Profile
- **Regions (reported):** Japan, South Korea, United States, Europe, Southeast Asia.
- **Sectors (reported):**
  - Earlier targeting described as government/defense-related intelligence.
  - Later targeting (by 2015) emphasized organizations supporting Japanese critical infrastructure, including electricity generation, oil & natural gas, finance, transportation, and construction.

## 5. Tradecraft Overview
- **Initial access:** Combination of spearphishing (attachments and links) and watering-hole style drive-by compromise is reported for Operation Dust Storm.
- **Infrastructure:** Use of attacker-controlled domains (including dynamic DNS) and email accounts for registering/operating infrastructure.
- **Execution chain themes:** Scripted stages (Visual Basic / JavaScript), decoding/packing/encoding behaviors, and masquerading (e.g., disguising executables as images) are documented in the campaign’s ATT&CK mappings.
- **Tooling evolution:** The campaign’s publicly tracked software includes multiple Windows backdoors over time (Misdat → Mis-Type → S-Type → ZLib), plus the use of public RATs (e.g., gh0st RAT, PoisonIvy) as reported in the primary campaign write-up.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1583.001 - Acquire Infrastructure: Domains]]
- [[20_Entities/07_TTPs/T1585.002 - Establish Accounts: Email Accounts]]
- [[20_Entities/07_TTPs/T1568 - Dynamic Resolution]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]]
- [[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution]]
- [[20_Entities/07_TTPs/T1518 - Software Discovery]]
- [[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]
- [[20_Entities/07_TTPs/T1036 - Masquerading]]
- [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]
- [[20_Entities/07_TTPs/T1027.013 - Obfuscated Files or Information: Encrypted/Encoded File]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1204.002 - User Execution: Malicious File]]
- [[20_Entities/07_TTPs/T1533 - Data from Local System]]
- [[20_Entities/07_TTPs/T1646 - Exfiltration Over C2 Channel]]
- [[20_Entities/07_TTPs/T1420 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1636.004 - Protected User Data: SMS Messages]]

## 7. Malware & Tools Used
**Windows malware / RAT families (MITRE campaign/software tracking)**
- [[30_CIPHER/05_Malware/Misdat]] — backdoor used in Operation Dust Storm from 2010–2011 (MITRE).
- [[30_CIPHER/05_Malware/Mis-Type]] — backdoor hybrid used in Operation Dust Storm by 2012 (MITRE).
- [[30_CIPHER/05_Malware/S-Type]] — backdoor used in Operation Dust Storm since at least 2013 (MITRE).
- [[30_CIPHER/05_Malware/ZLib]] — second-stage backdoor used since at least 2014 (MITRE).
- [[30_CIPHER/05_Malware/gh0st RAT]] — public-source RAT associated with the campaign’s software set (MITRE).
- [[30_CIPHER/05_Malware/PoisonIvy]] — public-source RAT associated with the campaign’s software set (MITRE).

**Execution/utility tooling (campaign-mapped)**
- [[30_CIPHER/05_Malware/VBScript]]
- [[30_CIPHER/05_Malware/JavaScript]]
- [[30_CIPHER/05_Malware/mshta.exe]]
- [[30_CIPHER/05_Malware/UPX]]

## 8. Infrastructure Patterns
- [[Dynamic DNS]] / [[Dynamic resolution]] use across infrastructure, including free DDNS providers (reported in primary write-up).
- [[Domain registration]] supported by attacker-controlled [[Email accounts for infrastructure]].
- Mixed delivery via [[Spearphishing]] (attachment/link) and [[Watering hole]] drive-by compromise.
- Cross-platform expansion with [[Android backdoors]] reported by 2015 in the same campaign context.

## 9. Campaign History
- **2010-01 (First seen):** MITRE campaign tracking places Operation Dust Storm first seen in January 2010.
- **2010–2014 (reported):** Campaign tooling progression includes Misdat (2010–2011), Mis-Type (by 2012), S-Type (since at least 2013), and ZLib (since at least 2014) per MITRE software entries tied to C0016.
- **2015 (reported):** Shift in targeting toward Japanese companies supporting critical infrastructure; Android backdoor usage begins by 2015 with victims in Japan or South Korea (MITRE campaign description).
- **2016-02 (Last seen):** MITRE campaign tracking places last seen in February 2016.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize defense-in-depth for phishing and web compromise exposure aligned to [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]], [[20_Entities/07_TTPs/T1566.002 - Phishing: Spearphishing Link]], and [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]].
- Increase visibility for script-based execution chains aligned to [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]] and [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]], especially when coupled with decoding/packing behaviors (e.g., [[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]], [[20_Entities/07_TTPs/T1027.002 - Obfuscated Files or Information: Software Packing]]).
- Monitor for suspicious use of signed system binaries aligned to [[20_Entities/07_TTPs/T1218.005 - System Binary Proxy Execution: Mshta]] in correlation with user execution events.
- For environments with mobile exposure, include mobile telemetry and data-protection considerations aligned to [[20_Entities/07_TTPs/T1533 - Data from Local System]] and [[20_Entities/07_TTPs/T1636.004 - Protected User Data: SMS Messages]] in threat modeling.

## 12. Analyst Notes
- MITRE’s Dust Storm (G0031) entry shows a deprecation warning; treat “Dust Storm” as a **label** and anchor analysis to **Operation Dust Storm (C0016)** and primary reporting for defensible claims.
- The most stable analytical throughline is the campaign’s **multi-year duration**, **Japan/South Korea focus**, **delivery diversity (phishing + watering hole)**, and **tooling evolution** across multiple backdoors.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Dust Storm (G0031): https://attack.mitre.org/groups/G0031/
- MITRE ATT&CK — Operation Dust Storm (C0016): https://attack.mitre.org/campaigns/C0016/
- Cylance — Operation Dust Storm report (PDF): https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf
- MITRE ATT&CK — ZLib (S0086): https://attack.mitre.org/software/S0086/
- MITRE ATT&CK — Misdat (S0083): https://attack.mitre.org/software/S0083/

## 14. References
1. MITRE ATT&CK. “Dust Storm (G0031).” https://attack.mitre.org/groups/G0031/
2. MITRE ATT&CK. “Operation Dust Storm (C0016).” https://attack.mitre.org/campaigns/C0016/
3. Gross, J. “Operation Dust Storm.” (Primary reporting hosted as PDF). https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf
4. MITRE ATT&CK. “Misdat (S0083).” https://attack.mitre.org/software/S0083/
5. MITRE ATT&CK. “Mis-Type (S0084).” https://attack.mitre.org/software/S0084/
6. MITRE ATT&CK. “S-Type (S0085).” https://attack.mitre.org/software/S0085/
7. MITRE ATT&CK. “ZLib (S0086).” https://attack.mitre.org/software/S0086/
8. MITRE ATT&CK. “gh0st RAT (S0032).” https://attack.mitre.org/software/S0032/
9. MITRE ATT&CK. “PoisonIvy (S0012).” https://attack.mitre.org/software/S0012/
---
