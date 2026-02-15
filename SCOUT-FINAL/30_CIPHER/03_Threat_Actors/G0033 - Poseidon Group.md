---
entity_type: threat_actor
actor_name: "Poseidon Group"
common_name: "Poseidon Group"
actor_id: "G0033"
actor_type: "Commercial espionage/extortion-oriented intrusion set (Portuguese-speaking)"
aliases: []
country_of_origin: "Brazil (suspected)"
suspected_sponsors: []
attribution_confidence: "Low"
first_seen: "2005-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Commercial espionage","Extortion / coercion","Information theft"]
objectives: ["Exfiltrate sensitive corporate information for leverage","Coerce victims into contracting a front security firm using stolen data as pressure","Prioritize access to high-value systems (e.g., Domain Controllers) for deeper collection","Harvest credentials (especially domain/database) to expand access and sustain collection"]
victimology_summary: "Poseidon Group (MITRE ATT&CK G0033) is a Portuguese-speaking threat group reported active since at least 2005. Public reporting describes a business-model component in which exfiltrated information is used to blackmail victims into contracting the group as a security firm. Reporting highlights targeting across energy/utilities, telecommunications, public relations/media, financial institutions, government institutions, and manufacturing, with a victim geography skewed toward Brazil, the United States, France, Kazakhstan, the United Arab Emirates, India, and Russia."
target_sectors: ["Energy","Utilities","Telecommunications","Public relations","Media","Financial services","Government","Manufacturing","General services (reported)"]
target_regions: ["Brazil","United States","France","Kazakhstan","United Arab Emirates","India","Russia"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Nhopro]]"]
tools: ["[[30_CIPHER/05_Malware/IGT]]","[[30_CIPHER/05_Malware/PowerShell]]"]
infrastructure: ["[[Commercial front company]]","[[Extortion-based coercion]]","[[Short-lived C2 infrastructure]]","[[Redundant C2]]","[[Digitally signed malware]]","[[Abuse of code signing certificates]]","[[Satellite uplink abuse]]","[[Domain Controller targeting]]","[[Masqueraded process names]]"]
ttps: ["[[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]","[[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]","[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]","[[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]","[[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]","[[20_Entities/07_TTPs/T1057 - Process Discovery]]","[[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]","[[20_Entities/07_TTPs/T1007 - System Service Discovery]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Poseidon Group (G0033) (Last Modified 2025-04-25): https://attack.mitre.org/groups/G0033/","Kaspersky Securelist — Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage (2016-02-09): https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/","Kaspersky Blog — A Touch of Artistry: Poseidon’s APT Boutique (2016-02-09): https://www.kaspersky.com/blog/poseidon-apt/5165/","Kaspersky Resource Center — Poseidon Group: a Commercial Malware Boutique Specializing in Global Cyberespionage: https://usa.kaspersky.com/resource-center/threats/poseidon"]
tags: ["threat-actor","poseidon-group","g0033","commercial-espionage","extortion","portuguese-speaking","brazil-suspected"]
created: "2025-12-25"
last_modified: "2025-12-25"
---

# Poseidon Group

## 1. BLUF / Executive Summary
Poseidon Group (MITRE ATT&CK **G0033**) is a Portuguese-speaking intrusion set reported active since at least **2005**, notable for combining targeted intrusion activity with an **extortion/coercion business model**: stolen corporate data is reportedly used to pressure victims into contracting a **front security firm** associated with the operators. Public reporting emphasizes Windows-centric operations, credential theft aimed at domain/database access, and post-compromise collection focused on high-value enterprise systems.

## 2. Attribution Notes
- MITRE characterizes Poseidon Group primarily by language and business-model characteristics (Portuguese-speaking; blackmail-to-contract pattern), rather than by a confirmed state sponsor.
- Kaspersky reporting indicates Portuguese from Brazil appears in code/command language and that the toolset is designed to function on English and Portuguese systems; this supports a **Brazil-suspected** origin assessment but is not definitive.
- Overall attribution should be treated as **low confidence** beyond the group’s reported language/campaign traits.

## 3. Motivations & Objectives
- **Primary motivation:** Commercial espionage and information theft to generate leverage and revenue.
- **Operational objectives:** Establish access, expand via credential harvesting (with emphasis on domain/database credentials), reach high-value systems (notably Domain Controllers), and exfiltrate sensitive data suitable for coercion or competitive advantage narratives.

## 4. Targeting Profile
- **Sectors (reported):** energy/utilities, telecommunications, PR/media, financial institutions, government institutions, manufacturing, and services.
- **Regions (reported):** victim set is reported as skewed toward Brazil, United States, France, Kazakhstan, UAE, India, and Russia; reporting also notes many victims have partner/joint-venture operations in Brazil.

## 5. Tradecraft Overview
- **Windows enterprise focus:** Public reporting describes tailoring infection methods for different Windows versions and prioritizing server systems that provide control and visibility over enterprise environments.
- **Two-stage collection theme:** Reporting describes an “initial phase” implant footprint followed by deeper collection once high-value systems (e.g., Domain Controllers) are reached, enabled by an internal toolkit described as an information-gathering “supertool.”
- **Credential access emphasis:** MITRE documents credential dumping with a stated focus on domain and database server credentials (aligns to [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]).
- **Discovery and enumeration:** MITRE documents account discovery, process discovery, service discovery, and network connection discovery as part of standard post-compromise profiling (aligns to [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]], [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]], [[20_Entities/07_TTPs/T1057 - Process Discovery]], [[20_Entities/07_TTPs/T1007 - System Service Discovery]], [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]).
- **Defense evasion via masquerading:** MITRE describes spoofing of anti-virus process names/locations as a self-defense measure (aligns to [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]).
- **Operational security themes (reported):** Kaspersky describes redundancy and rapid discarding of C2 infrastructure, along with reported use of digitally signed malware and (in at least one campaign) abuse of maritime satellite communications downlinks.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]]
- [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]]
- [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]]
- [[20_Entities/07_TTPs/T1057 - Process Discovery]]
- [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]]
- [[20_Entities/07_TTPs/T1007 - System Service Discovery]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/Nhopro]] — malware family name reflected in Kaspersky detections referenced in the primary Poseidon reporting.
- [[30_CIPHER/05_Malware/IGT]] — “Information Gathering Tool” toolkit described as the principal collection component once high-value enterprise systems are reached.
- [[30_CIPHER/05_Malware/PowerShell]] — MITRE notes the IGT includes PowerShell components (mapped as [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]).

## 8. Infrastructure Patterns
- [[Commercial front company]] used to legitimize “security contractor” positioning while retaining or re-establishing access (reported).
- [[Short-lived C2 infrastructure]] with [[Redundant C2]] and rapid discard practices (reported).
- [[Digitally signed malware]] / [[Abuse of code signing certificates]] involving certificates issued to rogue or legitimate company names (reported).
- [[Satellite uplink abuse]] reported in at least one campaign involving maritime satellite communications infrastructure.

## 9. Campaign History
- **Early 2000s (reported):** Kaspersky states early samples were detected in the early 2000s, with broader correlation to a single actor established by mid-2015.
- **2005 (reported):** Both MITRE and Kaspersky reporting describe activity since at least 2005 (with possible earlier outliers/prototypes referenced by Kaspersky).
- **2016-02-09:** Kaspersky publishes consolidated public reporting describing the group’s commercial espionage and coercion model.
- **2017-05-31:** MITRE ATT&CK created the Poseidon Group entry.
- **2025-04-25:** MITRE ATT&CK last modified the Poseidon Group entry (per page metadata).

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Prioritize monitoring for credential access activity aligned to [[20_Entities/07_TTPs/T1003 - OS Credential Dumping]], especially when associated with Domain Controller or database-adjacent systems.
- Treat bursts of discovery activity aligned to [[20_Entities/07_TTPs/T1087.001 - Account Discovery: Local Account]], [[20_Entities/07_TTPs/T1087.002 - Account Discovery: Domain Account]], [[20_Entities/07_TTPs/T1057 - Process Discovery]], [[20_Entities/07_TTPs/T1007 - System Service Discovery]], and [[20_Entities/07_TTPs/T1049 - System Network Connections Discovery]] as higher-signal when correlated with unusual authentication or privilege changes.
- Increase scrutiny of suspicious PowerShell use aligned to [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]] in environments where PowerShell is not routinely used for administrative automation.
- Hunt for masquerading behaviors aligned to [[20_Entities/07_TTPs/T1036.005 - Masquerading: Match Legitimate Resource Name or Location]], especially processes or binaries imitating security tooling names/paths.
- Strengthen governance and monitoring around code-signing trust chains and execution policy controls, given reported use of signed malware and execution-policy awareness.

## 12. Analyst Notes
- Poseidon Group’s distinguishing characteristic in public reporting is the **coercion-to-contract** model; defenders should treat this as a risk factor for secondary impacts (legal, reputational, competitive) beyond standard data theft.
- The public record provides limited standardized malware family naming beyond reporting-specific labels and vendor detections; this note stays conservative and avoids overstating specific tool inventories.
- Current operational status is unclear in open reporting beyond historical activity and MITRE’s maintained record.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Poseidon Group (G0033): https://attack.mitre.org/groups/G0033/
- Kaspersky Securelist — Poseidon Group: a Targeted Attack Boutique…: https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/
- Kaspersky Blog — Poseidon’s APT Boutique: https://www.kaspersky.com/blog/poseidon-apt/5165/
- Kaspersky Resource Center — Poseidon Group overview: https://usa.kaspersky.com/resource-center/threats/poseidon

## 14. References
1. MITRE ATT&CK. “Poseidon Group (G0033).” (Last Modified 2025-04-25). https://attack.mitre.org/groups/G0033/
2. Kaspersky (Securelist). “Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage.” (2016-02-09). https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/
3. Kaspersky Blog. “A Touch of Artistry: Poseidon’s APT Boutique.” (2016-02-09). https://www.kaspersky.com/blog/poseidon-apt/5165/
4. Kaspersky Resource Center. “Poseidon Group: a Commercial Malware Boutique Specializing in Global Cyberespionage.” https://usa.kaspersky.com/resource-center/threats/poseidon
---
