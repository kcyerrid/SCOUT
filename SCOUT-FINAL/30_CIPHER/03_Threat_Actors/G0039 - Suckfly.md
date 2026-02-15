---
entity_type: threat_actor
actor_name: "Suckfly"
common_name: "Suckfly"
actor_id: "G0039"
actor_type: "China-based cyber espionage threat group associated with theft and abuse of code-signing certificates and a custom backdoor (Nidiran)"
aliases: []
country_of_origin: "China"
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2014-04-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Espionage"]
objectives: ["Compromise government and commercial organizations for intelligence collection","Steal and abuse legitimate code-signing certificates to sign malware and tools","Obtain credentials and use valid accounts for internal access and movement"]
victimology_summary: "Suckfly (MITRE ATT&CK G0039) is described as a China-based threat group active since at least April 2014. Public reporting ties the actor to the theft of code-signing certificates (including from South Korean companies) used to sign malware and hacking tools, improving stealth and trust bypass. MITRE attributes Suckfly’s custom backdoor [[30_CIPHER/05_Malware/Nidiran]] (aka [[30_CIPHER/05_Malware/Backdoor.Nidiran]]) to the group and documents activity including command-line tooling, network service discovery, credential dumping, and the use of valid accounts."
target_sectors: ["Government","Technology","E-commerce","Financial services","Shipping & logistics","Healthcare"]
target_regions: ["India","Saudi Arabia","South Korea","Multiple countries (reported)"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Nidiran]]","[[30_CIPHER/05_Malware/Backdoor.Nidiran]]"]
tools: ["[[30_CIPHER/05_Malware/Windows Command Shell]]"]
infrastructure: ["[[Stolen code-signing certificates]]","[[Signed malware]]","[[Signed hacking tools]]","[[Strategic web compromise delivery]]","[[Internal network service discovery]]","[[Credential dumping tooling]]","[[Valid account abuse]]"]
ttps: ["[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]","[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]","[[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]","[[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]","[[20_Entities/07_TTPs/T1078 - Valid Accounts]]","[[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]","[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]","[[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Suckfly (G0039) (Last Modified 2025-04-16): https://attack.mitre.org/groups/G0039/","MITRE ATT&CK — Nidiran (S0118) (Last Modified 2025-04-16): https://attack.mitre.org/software/S0118/","SecurityWeek — Suckfly Hackers Target Organizations in India (2016-05-19): https://www.securityweek.com/suckfly-hackers-target-organizations-india/","SC Media — ‘Suckfly’ in the ointment: Chinese APT group steals code-signing certificates (2016-03-16): https://www.scworld.com/brief/suckfly-in-the-ointment-chinese-apt-group-steals-code-signing-certificates","HHS HC3 — China-Based Threat Actors (TLP:CLEAR) (2023-08-16) (naming-collision context for “Suckfly” as an alias elsewhere): https://www.hhs.gov/sites/default/files/china-based-threat-actor-profiles-tlpclear.pdf"]
tags: ["threat-actor","suckfly","g0039","china","cyber-espionage","code-signing","nidiran"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Suckfly

## 1. BLUF / Executive Summary
Suckfly (MITRE ATT&CK **G0039**) is a China-based cyber espionage threat group active since at least **April 2014**. Open reporting emphasizes the actor’s repeated theft and operational abuse of **legitimate code-signing certificates**, which were used to sign both malware and hacking tools to reduce suspicion and evade controls. The group is associated with a custom Windows backdoor, [[30_CIPHER/05_Malware/Nidiran]] (aka [[30_CIPHER/05_Malware/Backdoor.Nidiran]]), and documented behaviors including command-line driven operations, network service discovery, credential dumping, and movement using valid accounts.

## 2. Attribution Notes
- MITRE describes Suckfly as **China-based** and tracks the group as **G0039**.
- Public reporting (2016) connects Suckfly to infrastructure and activity assessed as originating from China and to certificate theft from organizations in South Korea, used to sign malicious tooling.
- **Naming collision risk:** at least one government-sector summary uses “Suckfly” as an alias within a different China-linked actor taxonomy; this should be treated as nomenclature overlap rather than proof of equivalence. Use **G0039** as the anchor identifier for this note.

## 3. Motivations & Objectives
- **Espionage-oriented collection:** compromise politically and economically significant organizations to obtain sensitive information.
- **Trust subversion as an enabler:** maintain operational stealth by abusing **stolen code-signing certificates** to sign implants and tools.
- **Credential-centric access:** acquire credentials for internal access and persistence via legitimate accounts.

## 4. Targeting Profile
- **Primary targeting (reported):** government organizations and government-adjacent IT service providers.
- **Commercial targeting (reported):** technology, e-commerce, finance, logistics/shipping, and healthcare-related business units.
- **Geographic emphasis (reported):** India features prominently in public reporting; additional activity includes attacks involving government entities in other countries (e.g., Saudi Arabia) and certificate theft from organizations in South Korea.

## 5. Tradecraft Overview
- **Signed tooling and implants:** repeated theft and use of code-signing certificates to sign malware and hack tools (aligns to [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]).
- **Command-line driven operations:** multiple components and operator tooling described as command-line driven (aligns to [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]).
- **Internal discovery and access expansion:** documented scanning/discovery of internal services (aligns to [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]).
- **Credential acquisition and reuse:** credential dumping paired with subsequent movement using valid accounts (aligns to [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]]).
- **Backdoor-enabled persistence and staging:** the Suckfly-associated backdoor [[30_CIPHER/05_Malware/Nidiran]] includes behaviors consistent with service-based persistence and downloading additional files (aligns to [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]] and [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]) and task/service masquerading (aligns to [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1553.002 - Subvert Trust Controls: Code Signing]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1046 - Network Service Discovery]]
- [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]
- [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
- [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]
- [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Nidiran]] / [[30_CIPHER/05_Malware/Backdoor.Nidiran]] — custom Windows backdoor attributed to Suckfly in MITRE; described as delivered via [[Strategic web compromise delivery]] and supporting service-based persistence, file download/execution, and masquerading behaviors.
- [[30_CIPHER/05_Malware/Windows Command Shell]] — operator activity described as relying on command-line driven tooling in reporting.
- Public reporting also references Suckfly’s broader toolkit categories (e.g., keylogging, credential dumping, port scanning) but does not consistently provide stable public family names beyond Nidiran in the sources used here.

## 8. Infrastructure Patterns
- [[Stolen code-signing certificates]] enabling [[Signed malware]] and [[Signed hacking tools]] for trust and reputation abuse.
- [[Strategic web compromise delivery]] for initial malware delivery (documented for Nidiran in MITRE).
- [[Internal network service discovery]] followed by [[Credential dumping tooling]] and [[Valid account abuse]] to expand access while blending with legitimate activity.

## 9. Campaign History
- **2014-04 onward (reported):** sustained targeting of government and commercial organizations; India is highlighted in 2015–2016 reporting as a major focus area.
- **2015 (reported):** public reporting notes discovery of signed malicious tooling and the broader code-signing abuse pattern.
- **2016 (public reporting):** multiple outlets summarize vendor findings describing Suckfly’s India-focused targeting and certificate theft used to sign malware and tools; MITRE later formalizes group/software entries (G0039 / S0118).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Treat certificate trust as a monitored control surface: build detection/response around **unexpected code-signing usage** in the enterprise and improve governance of certificate issuance, storage, and anomaly review.
- Strengthen visibility for **credential access** and **valid-account** abuse behaviors, prioritizing detection on endpoints and identity telemetry aligned to [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]] and [[20_Entities/07_TTPs/T1078 - Valid Accounts]].
- Increase monitoring for **service creation/modification** and suspicious service masquerading patterns aligned to [[20_Entities/07_TTPs/T1543.003 - Create or Modify System Process: Windows Service]] and [[20_Entities/07_TTPs/T1036.004 - Masquerading: Masquerade Task or Service]].
- Maintain robust detection for **internal discovery** and reconnaissance activity aligned to [[20_Entities/07_TTPs/T1046 - Network Service Discovery]] in sensitive network segments.

## 12. Analyst Notes
- Open reporting on Suckfly is concentrated around 2016-era disclosures; later public material is comparatively sparse in widely cited sources. Anchor tradecraft claims to MITRE’s G0039/S0118 entries to remain conservative.
- Alias overlap in some sources (e.g., broader China actor taxonomies) can cause conflation. Maintain strict ID discipline (G0039) and avoid cross-walking without explicit evidence.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Suckfly (G0039): https://attack.mitre.org/groups/G0039/
- MITRE ATT&CK — Nidiran (S0118): https://attack.mitre.org/software/S0118/
- SecurityWeek — India-focused targeting summary (2016): https://www.securityweek.com/suckfly-hackers-target-organizations-india/
- SC Media — certificate theft overview (2016): https://www.scworld.com/brief/suckfly-in-the-ointment-chinese-apt-group-steals-code-signing-certificates

## 14. References
1. MITRE ATT&CK. “Suckfly (G0039).” (Last Modified 2025-04-16). https://attack.mitre.org/groups/G0039/
2. MITRE ATT&CK. “Nidiran (S0118).” (Last Modified 2025-04-16). https://attack.mitre.org/software/S0118/
3. SecurityWeek. “Suckfly Hackers Target Organizations in India.” (2016-05-19). https://www.securityweek.com/suckfly-hackers-target-organizations-india/
4. SC Media. “‘Suckfly’ in the ointment: Chinese APT group steals code-signing certificates.” (2016-03-16). https://www.scworld.com/brief/suckfly-in-the-ointment-chinese-apt-group-steals-code-signing-certificates
5. U.S. HHS HC3. “China-Based Threat Actors” (TLP:CLEAR). (2023-08-16). https://www.hhs.gov/sites/default/files/china-based-threat-actor-profiles-tlpclear.pdf
---
