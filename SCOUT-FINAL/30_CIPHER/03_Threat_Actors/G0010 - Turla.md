---
entity_type: "threat_actor"
actor_name: "Turla"
common_name: "Turla"
actor_id: "G0010"
actor_type: "Nation-state / cyber espionage (attributed)"
aliases: ["Snake", "Uroburos", "Venomous Bear", "Waterbug", "Krypton", "WhiteBear", "Secret Blizzard", "IRON HUNTER", "Group 88", "BELUGASTURGEON"]
country_of_origin: "Russia (attributed)"
suspected_sponsors: ["Russia FSB (attributed)"]
attribution_confidence: "High"
first_seen: "2004-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Strategic intelligence collection (espionage)"]
objectives: ["Strategic intelligence collection", "Long-term access and persistence", "Credential access and lateral movement enablement", "Email and document collection", "Covert exfiltration"]
victimology_summary: "Turla is a long-running Russian intelligence-attributed cyber espionage actor linked to the FSB. Public reporting and government advisories describe global targeting since at least 2004, including government, embassies/diplomatic missions, military, education, and research organizations. Turla is known for spearphishing and watering hole activity, extensive use of bespoke malware ecosystems (notably Snake/Uroburos), and for leveraging compromised third-party infrastructure and web services for command-and-control and exfiltration."
target_sectors: ["Government", "Embassies/Diplomatic missions", "Military/Defense", "Education", "Research", "Pharmaceuticals", "International organizations", "NGOs/Think tanks"]
target_regions: ["Global"]
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Uroburos]]", "[[30_CIPHER/05_Malware/Carbon]]", "[[30_CIPHER/05_Malware/ComRAT]]", "[[30_CIPHER/05_Malware/Kazuar]]", "[[30_CIPHER/05_Malware/Crutch]]", "[[30_CIPHER/05_Malware/KOPILUWAK]]", "[[30_CIPHER/05_Malware/LightNeuron]]", "[[30_CIPHER/05_Malware/Mosquito]]", "[[30_CIPHER/05_Malware/Gazer]]", "[[30_CIPHER/05_Malware/TinyTurla]]", "[[30_CIPHER/05_Malware/ApolloShadow]]"]
tools: ["[[30_CIPHER/05_Malware/certutil]]", "[[30_CIPHER/05_Malware/Mimikatz]]", "[[30_CIPHER/05_Malware/PsExec]]", "[[30_CIPHER/05_Malware/Net]]", "[[30_CIPHER/05_Malware/Reg]]", "[[30_CIPHER/05_Malware/Tasklist]]", "[[30_CIPHER/05_Malware/Systeminfo]]", "[[30_CIPHER/05_Malware/netstat]]", "[[30_CIPHER/05_Malware/nbtstat]]", "[[30_CIPHER/05_Malware/Arp]]", "[[30_CIPHER/05_Malware/NBTscan]]"]
infrastructure: ["[[Watering Hole]]", "[[Spearphishing]]", "[[Compromised WordPress Sites]]", "[[Compromised Web Services]]", "[[Virtual Private Server]]", "[[Legitimate Web Services]]", "[[Pastebin]]", "[[Dropbox]]", "[[GitHub]]", "[[Internal Proxy]]", "[[Multi-hop Proxy]]", "[[Email-based C2]]", "[[Cloud Storage Exfiltration]]", "[[Iranian APT Infrastructure]]", "[[ISP-level Adversary-in-the-Middle]]", "[[Captive Portal]]"]
ttps: ["[[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]", "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]", "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]", "[[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]", "[[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]", "[[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]", "[[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]]", "[[20_Entities/07_TTPs/T1546.013 - Event Triggered Execution: PowerShell Profile]]", "[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]", "[[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]", "[[20_Entities/07_TTPs/T1584.003 - Compromise Infrastructure: Virtual Private Server]]", "[[20_Entities/07_TTPs/T1584.006 - Compromise Infrastructure: Web Services]]", "[[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]", "[[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]", "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]", "[[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]", "[[20_Entities/07_TTPs/T1555.004 - Credentials from Password Stores: Windows Credential Manager]]", "[[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]", "[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]", "[[20_Entities/07_TTPs/T1134.002 - Access Token Manipulation: Create Process with Token]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK (Group G0010): Turla (Last modified 2024-06-26)","CISA/FBI/NSA et al. (2023-05-09): AA23-129A Hunting Russian Intelligence 'Snake' Malware","NSA/NCSC (2019-10-21): Turla group exploits Iranian APT to expand coverage of victims (PDF)","Microsoft Threat Intelligence (2024-12-04): Frequent freeloader Part I (Secret Blizzard/Turla)","Microsoft Threat Intelligence (2025-07-31): Frozen in transit (Secret Blizzard/Turla AiTM campaign against diplomats)"]
tags: ["threat-actor", "apt", "russia", "fsb", "cyber-espionage", "turla", "snake", "uroburos", "secret-blizzard", "mitre-g0010"]
---

# Turla

## 1. BLUF / Executive Summary
Turla (MITRE ATT&CK **G0010**) is a Russia-attributed cyber espionage threat actor widely linked to the **FSB**, assessed active since at least **2004**. Public reporting and government advisories describe persistent, multi-year operations targeting high-value diplomatic and government environments globally, often using spearphishing and watering holes, layered persistence, and a deep in-house malware ecosystem (notably [[30_CIPHER/05_Malware/Uroburos]]/“Snake”). Recent public reporting continues to describe Turla (also tracked as **Secret Blizzard**) innovating in access and collection tradecraft.

## 2. Attribution Notes
- MITRE ATT&CK attributes Turla to **Russia’s Federal Security Service (FSB)** and tracks the cluster under **G0010**.
- U.S. and allied government advisories also attribute “Snake” to Russian intelligence-linked activity and describe it as a flagship espionage capability associated with Turla/FSB-aligned operations.
- Vendor/government naming varies (e.g., “Secret Blizzard,” “Venomous Bear,” “Waterbug”); analytic confidence should be anchored to converging evidence (TTPs + malware lineage + victimology + infrastructure patterns), not aliases alone.

## 3. Motivations & Objectives
- **Motivation:** Strategic intelligence collection aligned with state priorities.
- **Objectives:** Establish durable access; collect diplomatic, government, military, and research information; maintain stealthy exfiltration channels; and preserve re-entry options through resilient infrastructure and tooling.

## 4. Targeting Profile
- **Sectors (reported):** Government, embassies/diplomatic missions, military/defense, education, research, and pharmaceutical organizations; broader reporting includes international organizations and NGOs/think tanks.
- **Regions (reported):** Global targeting across many countries over long time horizons; recent reporting highlights diplomatic-focused targeting.

## 5. Tradecraft Overview
- **Initial access:** Use of [[Watering Hole]] activity consistent with [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]] and targeted phishing workflows consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]].
- **Command execution & scripting:** Broad use of Windows-native scripting and interpreters consistent with [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]], [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]], and [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]].
- **Persistence:** Multiple persistence mechanisms including registry-based startup persistence consistent with [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] and event-triggered persistence consistent with [[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]] and [[20_Entities/07_TTPs/T1546.013 - Event Triggered Execution: PowerShell Profile]].
- **Infrastructure strategy:** Heavy use of compromised infrastructure and third-party services—VPS and web services—consistent with [[20_Entities/07_TTPs/T1584.003 - Compromise Infrastructure: Virtual Private Server]] and [[20_Entities/07_TTPs/T1584.006 - Compromise Infrastructure: Web Services]]; documented patterns include [[Compromised WordPress Sites]] and [[Legitimate Web Services]] for C2.
- **C2 & exfiltration:** Use of web services for bidirectional communications consistent with [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]] and exfiltration to cloud services consistent with [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]].
- **Tradecraft adaptation:** Public government reporting describes Turla leveraging other actors’ infrastructure (e.g., Iranian APT infrastructure) to expand coverage, complicating attribution and detection based on infrastructure alone.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1059.001 - Command and Scripting Interpreter: PowerShell]]
- [[20_Entities/07_TTPs/T1059.005 - Command and Scripting Interpreter: Visual Basic]]
- [[20_Entities/07_TTPs/T1059.007 - Command and Scripting Interpreter: JavaScript]]
- [[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]]
- [[20_Entities/07_TTPs/T1546.013 - Event Triggered Execution: PowerShell Profile]]
- [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]
- [[20_Entities/07_TTPs/T1583.006 - Acquire Infrastructure: Web Services]]
- [[20_Entities/07_TTPs/T1584.003 - Compromise Infrastructure: Virtual Private Server]]
- [[20_Entities/07_TTPs/T1584.006 - Compromise Infrastructure: Web Services]]
- [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]]
- [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]
- [[20_Entities/07_TTPs/T1555.004 - Credentials from Password Stores: Windows Credential Manager]]
- [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]]
- [[20_Entities/07_TTPs/T1018 - Remote System Discovery]]
- [[20_Entities/07_TTPs/T1134.002 - Access Token Manipulation: Create Process with Token]]

## 7. Malware & Tools Used
- **Core malware ecosystem (MITRE ATT&CK software associated with Turla):**
  - [[30_CIPHER/05_Malware/Uroburos]]
  - [[30_CIPHER/05_Malware/Carbon]]
  - [[30_CIPHER/05_Malware/ComRAT]]
  - [[30_CIPHER/05_Malware/Kazuar]]
  - [[30_CIPHER/05_Malware/Crutch]]
  - [[30_CIPHER/05_Malware/KOPILUWAK]]
  - [[30_CIPHER/05_Malware/LightNeuron]]
  - [[30_CIPHER/05_Malware/Mosquito]]
  - [[30_CIPHER/05_Malware/Gazer]]
  - [[30_CIPHER/05_Malware/TinyTurla]]
- **Tooling & utilities (MITRE ATT&CK software associated with Turla tradecraft):**
  - [[30_CIPHER/05_Malware/certutil]]
  - [[30_CIPHER/05_Malware/Mimikatz]]
  - [[30_CIPHER/05_Malware/PsExec]]
  - [[30_CIPHER/05_Malware/Net]]
  - [[30_CIPHER/05_Malware/Reg]]
  - [[30_CIPHER/05_Malware/Tasklist]]
  - [[30_CIPHER/05_Malware/Systeminfo]]
  - [[30_CIPHER/05_Malware/netstat]]
  - [[30_CIPHER/05_Malware/nbtstat]]
  - [[30_CIPHER/05_Malware/Arp]]
  - [[30_CIPHER/05_Malware/NBTscan]]
- **Recently described (public reporting):**
  - [[30_CIPHER/05_Malware/ApolloShadow]]

## 8. Infrastructure Patterns
- Use of [[Compromised WordPress Sites]] and other [[Compromised Web Services]] as staging/C2 nodes, consistent with long-running infrastructure abuse patterns.
- Recurrent use of [[Legitimate Web Services]] (e.g., [[Pastebin]], [[Dropbox]], [[GitHub]]) for communications and/or data movement consistent with [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]].
- Leveraging [[Virtual Private Server]] infrastructure and, at times, third-party actor infrastructure (e.g., [[Iranian APT Infrastructure]]) to complicate infrastructure-based attribution and widen access opportunities.
- Proxying and relay behaviors consistent with [[Internal Proxy]] / [[Multi-hop Proxy]] patterns to conceal operator origin and segment operations.

## 9. Campaign History
- **2004–present (public tracking):** MITRE ATT&CK and multiple vendors describe continuous Turla operations across decades, with evolving toolchains and multi-stage implants.
- **2019 (government reporting):** Allied advisories describe Turla leveraging Iranian APT infrastructure to broaden victim coverage, highlighting operational pragmatism and deception.
- **2023-05 (government reporting):** Joint advisory (AA23-129A) details the “Snake” toolset and publicly describes coordinated disruption efforts targeting long-running Snake operations.
- **2024–2025 (vendor reporting):** Microsoft reporting on “Secret Blizzard” (Turla) describes sustained espionage operations including the use of other actors’ infrastructure and, separately, an AiTM-focused campaign targeting diplomats in Moscow.

## 10. Known Indicators
- []

## 11. Defensive Recommendations
- Strengthen defenses against targeted phishing and drive-by exposure consistent with [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] and [[20_Entities/07_TTPs/T1189 - Drive-by Compromise]], especially for diplomatic/government user populations.
- Prioritize detection for event-triggered persistence mechanisms consistent with [[20_Entities/07_TTPs/T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription]] and profile-based persistence consistent with [[20_Entities/07_TTPs/T1546.013 - Event Triggered Execution: PowerShell Profile]].
- Treat suspicious use of third-party web services for comms/exfiltration consistent with [[20_Entities/07_TTPs/T1102.002 - Web Service: Bidirectional Communication]] and [[20_Entities/07_TTPs/T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage]] as higher-signal when correlated with Turla victimology and Turla-associated malware families.
- Maintain visibility into lateral movement patterns consistent with [[20_Entities/07_TTPs/T1021.002 - Remote Services: SMB/Windows Admin Shares]] and credential access from OS stores consistent with [[20_Entities/07_TTPs/T1555.004 - Credentials from Password Stores: Windows Credential Manager]].

## 12. Analyst Notes
- **Attribution confidence:** High (MITRE ATT&CK attribution + multiple government and major vendor reports).
- **Naming overlap:** “Turla,” “Snake,” and “Secret Blizzard” are often used interchangeably across reporting; ensure consistent cluster definitions within your environment to avoid duplicate entity management.
- **Infrastructure ambiguity:** Turla’s history of using compromised third-party infrastructure (including other actors’ assets) reduces the reliability of IOC-only or infra-only assessments without behavioral/software corroboration.

## 13. Further Reading / External Resources
- MITRE ATT&CK — Turla (G0010)  
  https://attack.mitre.org/groups/G0010/
- CISA — AA23-129A: Hunting Russian Intelligence “Snake” Malware (2023-05-09)  
  https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a
- NSA/NCSC — Turla group exploits Iranian APT to expand coverage of victims (2019-10-21)  
  https://media.defense.gov/2019/Oct/18/2002197242/-1/-1/0/NSA_CSA_TURLA_20191021%20VER%203%20-%20COPY.PDF
- Microsoft Threat Intelligence — Frequent freeloader Part I (2024-12-04)  
  https://www.microsoft.com/en-us/security/blog/2024/12/04/frequent-freeloader-part-i-secret-blizzard-compromising-storm-0156-infrastructure-for-espionage/
- Microsoft Threat Intelligence — Frozen in transit (2025-07-31)  
  https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/

## 14. References
- MITRE ATT&CK. “Turla (G0010).” (Last modified 2024-06-26)  
  https://attack.mitre.org/groups/G0010/
- CISA/FBI/NSA et al. “AA23-129A: Hunting Russian Intelligence ‘Snake’ Malware.” (2023-05-09)  
  https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a
- NSA/NCSC. “Cybersecurity Advisory: Turla Group Exploits Iranian APT To Expand Coverage Of Victims.” (2019-10-21)  
  https://media.defense.gov/2019/Oct/18/2002197242/-1/-1/0/NSA_CSA_TURLA_20191021%20VER%203%20-%20COPY.PDF
- Microsoft Threat Intelligence. “Frequent freeloader part I: Secret Blizzard compromising Storm-0156 infrastructure for espionage.” (2024-12-04)  
  https://www.microsoft.com/en-us/security/blog/2024/12/04/frequent-freeloader-part-i-secret-blizzard-compromising-storm-0156-infrastructure-for-espionage/
- Microsoft Threat Intelligence. “Frozen in transit: Secret Blizzard’s AiTM campaign against diplomats.” (2025-07-31)  
  https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/
