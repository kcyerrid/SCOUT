---
entity_type: threat_actor
actor_name: "Taidoor"
actor_id: "G0015"
aliases:
  - "Earth Aughisky"
  - "Budminer"
suspected_country_of_origin: "China"
attribution: "PRC-linked (open-source reporting)"
first_seen: "2009-03-04"
last_seen: ""
active: ""
motivations:
  - "Espionage"
objectives:
  - "Information theft"
primary_targets_countries:
  - "Taiwan"
  - "Japan"
primary_targets_sectors:
  - "Government"
  - "Telecommunications"
  - "Manufacturing"
  - "Technology"
  - "Transportation"
  - "Heavy industry"
  - "Healthcare"
targeting_profile_notes: "Heavily Taiwan-focused victimology in multiple reports; later reporting notes expansion to Japan from late 2017/2018."
associated_malware:
  - "[[30_CIPHER/05_Malware/Taidoor]]"
  - "[[30_CIPHER/05_Malware/Roudan]]"
  - "[[30_CIPHER/05_Malware/Kuangdao]]"
  - "[[30_CIPHER/05_Malware/Taleret]]"
  - "[[30_CIPHER/05_Malware/Serkdes]]"
  - "[[30_CIPHER/05_Malware/DropNetClient]]"
  - "[[30_CIPHER/05_Malware/Buxzop]]"
  - "[[30_CIPHER/05_Malware/SiyBot]]"
  - "[[30_CIPHER/05_Malware/TWTRAT]]"
  - "[[30_CIPHER/05_Malware/GOORAT]]"
associated_tools:
  - "[[30_CIPHER/05_Malware/MemoryLoad]]"
infrastructure_patterns:
  - "[[Spoofed government email lures]]"
  - "[[Taiwan-themed decoy documents]]"
  - "[[Taiwan-based C2 nodes]]"
  - "[[C2 over HTTP]]"
  - "[[Registry Run Key persistence]]"
mitre_attack_techniques:
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]]"
  - "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]"
confidence: "Medium"
created: "2025-12-25"
last_modified: "2025-12-25"
intel_sources:
  - "MITRE ATT&CK (Software S0011): Taidoor"
  - "CISA AR20-216A: Chinese Remote Access Trojan (TAIDOOR)"
  - "Trend Micro (2022): The Rise of Earth Aughisky (aka Taidoor)"
  - "Reuters (2020-08-19): Taiwan says China behind cyberattacks (mentions Taidoor)"
  - "Malpedia: Taidoor (actor) summary and references"
tags:
  - "apt"
  - "china"
  - "espionage"
  - "taiwan"
  - "rat"
---

## 1. BLUF / Executive Summary
Taidoor (MITRE Group ID **G0015**) is an espionage-oriented threat actor cluster strongly associated with long-running targeting of **Taiwan**, with credible reporting also indicating **expansion into Japan** from late 2017/2018. Open reporting consistently links Taidoor operations to **spearphishing-driven intrusions**, followed by deployment of multiple backdoor families (including malware often labeled [[30_CIPHER/05_Malware/Taidoor]] / [[30_CIPHER/05_Malware/Roudan]]) to maintain access and support collection/exfiltration objectives.

## 2. Attribution Notes
- Multiple open sources describe Taidoor/Earth Aughisky as **PRC-linked** and aligned with intelligence collection goals rather than financial extortion. :contentReference[oaicite:0]{index=0}  
- Public, government-facing reporting in 2020 connected “TAIDOOR” malware activity to **Chinese government cyber actors** (malware-centric attribution, not necessarily a full organizational mapping). :contentReference[oaicite:1]{index=1}  
- Taiwan publicly attributed certain 2020 intrusions to groups including Taidoor (political attribution; treat as one input among several). :contentReference[oaicite:2]{index=2}  

## 3. Motivations & Objectives
- Primary motivation assessed as **espionage / information theft**. :contentReference[oaicite:3]{index=3}  
- Objectives commonly align with **persistent access** to enable long-term intelligence collection against government and critical sectors. :contentReference[oaicite:4]{index=4}  

## 4. Targeting Profile
- **Geography:** Predominantly **Taiwan**; later reporting notes operations extending to **Japan** starting late 2017/2018. :contentReference[oaicite:5]{index=5}  
- **Sectors (commonly reported):** Government, telecommunications, and multiple critical industries (manufacturing, transportation, technology, etc.). :contentReference[oaicite:6]{index=6}  

## 5. Tradecraft Overview
- **Initial access:** Reported reliance on **spearphishing** as a common entry vector, including decoy documents/lures. :contentReference[oaicite:7]{index=7}  
- **Persistence & long dwell:** Use of backdoors across multiple “families” over time; reporting emphasizes iterative updates and routine changes to remain effective. :contentReference[oaicite:8]{index=8}  
- **Operational security & evasion:** Reporting notes efforts such as **abusing legitimate accounts** and adapting tooling to reduce detection. :contentReference[oaicite:9]{index=9}  
- **C2 & comms:** Malware publicly labeled Taidoor is documented using **web protocols (HTTP)** for command-and-control. :contentReference[oaicite:10]{index=10}  

## 6. MITRE ATT&CK Mapping
- Initial Access
  - [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]] :contentReference[oaicite:11]{index=11}
- Command and Control
  - [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]] :contentReference[oaicite:12]{index=12}
- Persistence
  - [[20_Entities/07_TTPs/T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder]] :contentReference[oaicite:13]{index=13}
- Defense Evasion / Persistence / Initial Access (Observed behavior class)
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]] :contentReference[oaicite:14]{index=14}

## 7. Malware & Tools Used
> Note: Names below reflect public reporting; overlaps and renames are common across vendors.

**Core / historically linked backdoors**
- [[30_CIPHER/05_Malware/Taidoor]] (RAT label used broadly in reporting) :contentReference[oaicite:15]{index=15}  
- [[30_CIPHER/05_Malware/Roudan]] (reported as “also known as Taidoor” in some reporting) :contentReference[oaicite:16]{index=16}  

**Additional malware families reported in the same actor ecosystem**
- [[30_CIPHER/05_Malware/Taleret]] (also referenced as “Dalgan” in some reporting) :contentReference[oaicite:17]{index=17}  
- [[30_CIPHER/05_Malware/Serkdes]] (also referenced as “Yalink” in some reporting) :contentReference[oaicite:18]{index=18}  
- [[30_CIPHER/05_Malware/DropNetClient]] / [[30_CIPHER/05_Malware/Buxzop]] (reported use of cloud API–mediated C2 concepts) :contentReference[oaicite:19]{index=19}  
- [[30_CIPHER/05_Malware/Kuangdao]] (reported as disclosed in 2020 under the “Taidoor” label by some reporting) :contentReference[oaicite:20]{index=20}  
- [[30_CIPHER/05_Malware/SiyBot]], [[30_CIPHER/05_Malware/TWTRAT]], [[30_CIPHER/05_Malware/GOORAT]] :contentReference[oaicite:21]{index=21}  

**Tools / loaders**
- [[30_CIPHER/05_Malware/MemoryLoad]] (reported as a custom loader associated with some deployments) :contentReference[oaicite:22]{index=22}  

## 8. Infrastructure Patterns
- [[Spoofed government email lures]] and [[Taiwan-themed decoy documents]] described as recurring social-engineering tradecraft. :contentReference[oaicite:23]{index=23}  
- [[Taiwan-based C2 nodes]] reported as common in campaign infrastructure (with exceptions). :contentReference[oaicite:24]{index=24}  
- [[C2 over HTTP]] consistent with documented Taidoor malware communications. :contentReference[oaicite:25]{index=25}  
- [[Registry Run Key persistence]] observed for Taidoor malware persistence in public reporting. :contentReference[oaicite:26]{index=26}  

## 9. Campaign History
- **2009-03-04:** Open reporting places Taidoor activity at least as early as this date, associated with targeted operations and Taiwan-focused victimology. :contentReference[oaicite:27]{index=27}  
- **2010s:** Persistent Taiwan-centric operations with long-term evolution of malware families and routines reported over the decade. :contentReference[oaicite:28]{index=28}  
- **Late 2017–2018:** Reporting describes expansion of targeting/activity into **Japan**. :contentReference[oaicite:29]{index=29}  
- **2020:** U.S. government reporting highlighted “TAIDOOR” as a Chinese-government-associated RAT variant. :contentReference[oaicite:30]{index=30}  

## 10. Known Indicators
- Public indicators (IPs/domains/hashes) are **intentionally omitted** from this note per operational constraints.
- See linked public reports in **Further Reading** for original-source indicator context.

## 11. Defensive Recommendations
- Prioritize controls for **phishing resistance** and attachment handling (user awareness, filtering, detonation workflows), aligned to the actor’s reported entry path. :contentReference[oaicite:31]{index=31}  
- Strengthen **credential hygiene** and monitoring to reduce/spot abuse of legitimate accounts (MFA coverage, privileged account reviews, anomalous login detection). :contentReference[oaicite:32]{index=32}  
- Monitor for **web-protocol C2 patterns** consistent with commodity HTTP-based beaconing; tune detections to your environment’s normal baselines. :contentReference[oaicite:33]{index=33}  
- Hunt for persistence aligned to **Run Key / Startup Folder** behaviors where relevant to Windows endpoints. :contentReference[oaicite:34]{index=34}  

## 12. Analyst Notes
- Naming collisions are common: “Taidoor” is used as both an **actor label** (G0015) and a **malware label** (S0011). Maintain separate entities in your graph and link via “uses/associated-with.” :contentReference[oaicite:35]{index=35}  
- Source-weighting: treat state statements and media reporting as supportive context; anchor technical behaviors to government advisories and vendor reverse-engineering where available. :contentReference[oaicite:36]{index=36}  

## 13. Further Reading / External Resources
- MITRE ATT&CK (Software): Taidoor (S0011) — https://attack.mitre.org/software/S0011/ :contentReference[oaicite:37]{index=37}  
- CISA AR20-216A: Chinese Remote Access Trojan (TAIDOOR) — https://www.cisa.gov/news-events/analysis-reports/ar20-216a :contentReference[oaicite:38]{index=38}  
- Trend Micro (white paper): The Rise of Earth Aughisky: Tracking the Campaigns Taidoor Started — https://documents.trendmicro.com/assets/white_papers/wp-the-rise-of-earth-aughisky.pdf :contentReference[oaicite:39]{index=39}  
- Malpedia (actor overview): Taidoor — https://malpedia.caad.fkie.fraunhofer.de/actor/taidoor :contentReference[oaicite:40]{index=40}  
- Reuters (context reporting; 2020-08-19): Taiwan says China behind cyberattacks (mentions Taidoor) — https://www.reuters.com/article/world/taiwan-says-china-behind-cyberattacks-on-government-agencies-emails-idUSKCN25F0NY/ :contentReference[oaicite:41]{index=41}  

## 14. References
- MITRE ATT&CK — Taidoor (Software S0011): https://attack.mitre.org/software/S0011/ :contentReference[oaicite:42]{index=42}  
- CISA — AR20-216A “Chinese Remote Access Trojan” (TAIDOOR): https://www.cisa.gov/news-events/analysis-reports/ar20-216a :contentReference[oaicite:43]{index=43}  
- Trend Micro — “The Rise of Earth Aughisky: Tracking the Campaigns Taidoor Started” (PDF): https://documents.trendmicro.com/assets/white_papers/wp-the-rise-of-earth-aughisky.pdf :contentReference[oaicite:44]{index=44}  
- Malpedia — Taidoor (Threat Actor): https://malpedia.caad.fkie.fraunhofer.de/actor/taidoor :contentReference[oaicite:45]{index=45}  
- Reuters — “Taiwan says China behind cyberattacks on government agencies, emails” (2020-08-19): https://www.reuters.com/article/world/taiwan-says-china-behind-cyberattacks-on-government-agencies-emails-idUSKCN25F0NY/ :contentReference[oaicite:46]{index=46}  
- ETDA Threat Group Cards — Taidoor (alias summary incl. Budminer / Earth Aughisky): https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Taidoor&n=1 :contentReference[oaicite:47]{index=47}
