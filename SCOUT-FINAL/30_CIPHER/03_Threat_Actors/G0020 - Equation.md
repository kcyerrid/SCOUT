---
entity_type: "threat_actor"
actor_name: "Equation"
common_name: "Equation"
actor_id: "G0020"
actor_type: "Nation-state / cyber espionage (attributed)"
aliases: ["Equation Group"]
country_of_origin: "United States (attributed)"
suspected_sponsors: ["NSA (attributed in public reporting)"]
attribution_confidence: "High"
first_seen: "2001-01"
last_seen: ""
status: "Active (reported; public visibility varies)"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Covert, long-term access to high-value networks", "Collection of strategic intelligence", "Advanced persistence and stealth operations", "Capability development and platform access in target environments"]
victimology_summary: "Equation Group (MITRE ATT&CK G0020) is widely assessed in public reporting as a highly capable nation-state cyber espionage actor, commonly linked to the United States and the NSA. Reporting describes operations since at least the early 2000s, targeting governments, telecoms, energy, and other strategic sectors globally. Public technical reporting attributes to Equation Group an extensive malware ecosystem (including firmware/boot-level persistence in some cases), modular toolchains, and long-term operational discipline. Later public disclosures and leaks (e.g., toolset revelations) contributed to broader awareness of associated capabilities and tradecraft."
target_sectors: ["Government", "Telecommunications", "Energy", "Defense", "Technology", "Research", "Finance (reported)", "Aerospace (reported)"]
target_regions: ["Global"]
related_groups: ["Lazarus Group (reported tooling overlap via shared exploits; debated)", "Stuxnet operators (reported overlap/debate)"]
malware: ["[[30_CIPHER/05_Malware/EquationDrug]]", "[[30_CIPHER/05_Malware/DoubleFantasy]]", "[[30_CIPHER/05_Malware/GrayFish]]", "[[30_CIPHER/05_Malware/Fanny]]", "[[30_CIPHER/05_Malware/TripleFantasy]]"]
tools: ["[[30_CIPHER/05_Malware/RC5/RC6-based encryption modules]]", "[[30_CIPHER/05_Malware/Custom kernel drivers]]"]
infrastructure: ["[[Air-Gapped Network Bridging]]", "[[Removable Media Propagation]]", "[[Firmware Persistence]]", "[[Bootkit]]", "[[Modular Malware Platform]]", "[[Covert C2]]", "[[Multi-stage Toolchains]]"]
ttps: ["[[20_Entities/07_TTPs/T1091 - Replication Through Removable Media]]", "[[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]]", "[[20_Entities/07_TTPs/T1542.001 - Pre-OS Boot: System Firmware]]", "[[20_Entities/07_TTPs/T1542.003 - Pre-OS Boot: Bootkit]]", "[[20_Entities/07_TTPs/T1574.002 - Hijack Execution Flow: DLL Side-Loading]]", "[[20_Entities/07_TTPs/T1055 - Process Injection]]", "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]", "[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]", "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK — Equation (G0020) (Last modified 2025-04-25)","Kaspersky (2015-02): Equation Group: The Crown Creator of Cyber-Espionage (report)","The Shadow Brokers leaks (2016) referenced in multiple analyses (context)","Wired (2015-02): Kaspersky reveals Equation Group findings (journalism)","The Intercept (2017): Reporting on NSA toolset exposure (context)"]
tags: ["threat-actor", "equation-group", "g0020", "nation-state", "espionage", "nsa-attributed", "firmware", "bootkit"]
created: "2025-12-24"
last_modified: "2025-12-24"
---

# Equation

## 1. BLUF / Executive Summary
Equation (MITRE ATT&CK **G0020**), often referred to as “Equation Group,” is widely assessed in public reporting as a top-tier nation-state cyber espionage actor commonly linked to the **United States/NSA**. Reporting describes a long operational history since at least the early 2000s, with a deep, modular malware ecosystem (e.g., [[30_CIPHER/05_Malware/EquationDrug]], [[30_CIPHER/05_Malware/GrayFish]]) and high-end stealth/persistence capabilities, including reported cases of [[Firmware Persistence]] and [[Bootkit]]-style tradecraft. Public visibility of the actor’s operations has varied over time, with notable bursts of attention following technical reporting and later toolset exposures.

## 2. Attribution Notes
- MITRE ATT&CK tracks the cluster as **Equation (G0020)** and frames it as a highly sophisticated cyber espionage actor.  
- Major public vendor reporting (notably 2015-era) strongly linked Equation Group activity to U.S. intelligence based on infrastructure/tooling and operational characteristics; this remains an attribution judgment in open sources rather than a judicial finding.
- Later public disclosures and leaks are frequently cited in analyses as contextual reinforcement for capability claims, but they do not independently establish attribution without corroboration.

## 3. Motivations & Objectives
- **Motivation:** Strategic intelligence collection.
- **Objectives:** Covert long-term access to high-value networks; stealthy collection and exfiltration; maintaining persistence at multiple layers; and deploying modular capabilities to adapt across diverse target environments.

## 4. Targeting Profile
- **Sectors:** Government, telecom, energy, defense, technology, and research are repeatedly cited in public reporting; some sources describe additional targeting across finance and aerospace.
- **Geography:** Global targeting, with emphasis on strategic and geopolitical priority regions (varies by reporting period and dataset).

## 5. Tradecraft Overview
- **Modular platforms:** Multi-component toolchains described as modular malware platforms (e.g., [[30_CIPHER/05_Malware/EquationDrug]], [[30_CIPHER/05_Malware/GrayFish]]) enabling flexible functionality and staged deployment ([[Multi-stage Toolchains]]).
- **High-end persistence:** Public reporting describes persistence below the OS (e.g., [[Firmware Persistence]] and [[Bootkit]] concepts) consistent with [[20_Entities/07_TTPs/T1542.001 - Pre-OS Boot: System Firmware]] and [[20_Entities/07_TTPs/T1542.003 - Pre-OS Boot: Bootkit]].
- **Air-gap bridging:** Reporting describes removable-media propagation and collection workflows consistent with [[Air-Gapped Network Bridging]], [[Removable Media Propagation]], [[20_Entities/07_TTPs/T1091 - Replication Through Removable Media]], and [[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]].
- **Stealth and evasion:** Use of obfuscation and covert comms patterns consistent with [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]] and [[Covert C2]].
- **Execution & injection:** Public reporting describes advanced in-memory behaviors and injection consistent with [[20_Entities/07_TTPs/T1055 - Process Injection]] and staged delivery consistent with [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]].

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1091 - Replication Through Removable Media]]
- [[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]]
- [[20_Entities/07_TTPs/T1542.001 - Pre-OS Boot: System Firmware]]
- [[20_Entities/07_TTPs/T1542.003 - Pre-OS Boot: Bootkit]]
- [[20_Entities/07_TTPs/T1574.002 - Hijack Execution Flow: DLL Side-Loading]]
- [[20_Entities/07_TTPs/T1055 - Process Injection]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]

## 7. Malware & Tools Used
**Malware (widely cited in public reporting and MITRE software associations)**
- [[30_CIPHER/05_Malware/EquationDrug]]
- [[30_CIPHER/05_Malware/DoubleFantasy]]
- [[30_CIPHER/05_Malware/GrayFish]]
- [[30_CIPHER/05_Malware/Fanny]]
- [[30_CIPHER/05_Malware/TripleFantasy]]

**Tools / components (high-level categories referenced in public reporting)**
- [[30_CIPHER/05_Malware/Custom kernel drivers]]
- [[30_CIPHER/05_Malware/RC5/RC6-based encryption modules]]

## 8. Infrastructure Patterns
- Use of [[Multi-stage Toolchains]] with compartmented staging and selective capability deployment.
- Reported reliance on [[Covert C2]] and operational relay patterns to minimize direct attribution and resist takedown.
- Air-gap compatible workflows using [[Removable Media Propagation]] and [[Air-Gapped Network Bridging]].

## 9. Campaign History
- **2001–2015 (reported):** Public reporting describes long-running operations with multiple platform generations and a large malware catalog, with victimology spanning strategic sectors globally.
- **2015-02 (major public disclosure):** A major vendor report publicly detailed the Equation Group ecosystem and characterized it as a “crown creator” of cyber espionage tooling.
- **2016–2017 (public context):** Leaked offensive tooling and subsequent reporting increased public discussion around state cyber capabilities and potential linkages to previously described toolchains; these events are often discussed as context rather than as primary attribution.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Strengthen controls and monitoring for removable-media workflows and data movement aligned to [[20_Entities/07_TTPs/T1091 - Replication Through Removable Media]] and [[20_Entities/07_TTPs/T1052.001 - Exfiltration Over Physical Medium: Exfiltration over USB]] in environments where air-gapped bridging is a realistic risk.
- Expand detection depth below the OS where feasible (firmware integrity checks, secure boot baselines) to reduce exposure to persistence consistent with [[20_Entities/07_TTPs/T1542.001 - Pre-OS Boot: System Firmware]] and [[20_Entities/07_TTPs/T1542.003 - Pre-OS Boot: Bootkit]].
- Use behavioral detection for staged payload delivery and covert comms consistent with [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]] and [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]], emphasizing correlation over single-signal alerts.
- Prioritize hardening around high-value admin and developer workstations, and ensure incident response plans account for deep persistence scenarios (firmware/boot-level) when appropriate to threat model.

## 12. Analyst Notes
- Many public claims about Equation Group are rooted in a small number of foundational technical reports; treat high-impact assertions (e.g., firmware persistence prevalence) as “reported” and validate against your own telemetry when possible.
- Related-group discussions (e.g., overlap with other major operations) can be politically sensitive and analytically ambiguous; maintain conservative linkage language unless your dataset provides strong corroboration.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Equation (G0020): https://attack.mitre.org/groups/G0020/
- Kaspersky (2015) — Equation Group report landing context: https://securelist.com/equation-the-crown-creator-of-cyber-espionage/68750/
- Wired (2015) coverage of Equation Group reporting: https://www.wired.com/2015/02/kaspersky-equation-group/
- The Intercept (2017) reporting on NSA toolset exposure (context): https://theintercept.com/2017/02/14/the-nsa-hacking-tools-leaked-by-the-shadow-brokers-are-a-goldmine/
- ATT&CK software entries (examples): https://attack.mitre.org/software/ (search for specific families listed above)

## 14. References
- MITRE ATT&CK. “Equation (G0020).” (Last modified 2025-04-25). https://attack.mitre.org/groups/G0020/
- Kaspersky. “Equation: The Crown Creator of Cyber-Espionage.” (2015-02). https://securelist.com/equation-the-crown-creator-of-cyber-espionage/68750/
- Wired. “Kaspersky Finds One of the Most Sophisticated Hacking Groups Ever.” (2015-02). https://www.wired.com/2015/02/kaspersky-equation-group/
- The Intercept. “The NSA Hacking Tools Leaked By The Shadow Brokers Are A Goldmine.” (2017-02-14). https://theintercept.com/2017/02/14/the-nsa-hacking-tools-leaked-by-the-shadow-brokers-are-a-goldmine/
---
