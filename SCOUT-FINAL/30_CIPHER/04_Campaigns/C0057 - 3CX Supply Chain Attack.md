---
entity_type: campaign

campaign_name: "3CX Supply Chain Attack"
campaign_id: "C0057"

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1049 - AppleJeus|AppleJeus (G1049)]]"
suspected_actors: []

attribution_confidence: "3-high"
confidence_notes: "MITRE ATT&CK maps this campaign to AppleJeus (G1049). Public reporting from multiple independent sources (including the victim’s incident updates and major threat research) assessed the intrusion as North Korea–linked (e.g., UNC4736/UNC4736-like clustering), consistent with AppleJeus-associated activity."

first_observed: "2022-11"
last_observed: "2023-03"
campaign_status: "concluded"

primary_objectives:
  - "crypto_theft"
  - "data_theft"
secondary_objectives:
  - "financial_gain"
  - "long_term_access"

target_sectors:
  - "Cryptocurrency / blockchain ecosystem"
  - "Technology / communications (supply-chain exposure)"
target_regions:
  - "Global"
target_technologies:
  - "3CX Desktop App (Windows/macOS)"
  - "Electron-based application components"
  - "Enterprise endpoints with auto-update enabled"
  - "Enterprise identity + remote access (VPN) contexts (victim-side)"

initial_access_vectors:
  - "Supply Chain Compromise (trojanized 3CX software update)"
  - "Valid Accounts (credential/VPN access in initial intrusion chain; source-dependent)"

key_ttp_themes:
  - "Chained supply-chain compromise (precursor compromise enabling downstream supply-chain event)"
  - "Signed software update delivery + malicious component loading"
  - "Payload staging/selection to reach a narrower set of high-value targets"
  - "Dead-drop style tasking via public web services"

associated_ttps:
  - "T1195.002 - Compromise Software Supply Chain"
  - "T1189 - Drive-by Compromise"
  - "T1203 - Exploitation for Client Execution"
  - "T1218.007 - Msiexec"
  - "T1218.015 - Electron Applications"
  - "T1574.001 - DLL"
  - "T1055 - Process Injection"
  - "T1055.002 - Portable Executable Injection"
  - "T1620 - Reflective Code Loading"
  - "T1027 - Obfuscated Files or Information"
  - "T1027.009 - Embedded Payloads"
  - "T1027.013 - Encrypted/Encoded File"
  - "T1553.002 - Code Signing"
  - "T1559 - Inter-Process Communication"
  - "T1071.001 - Web Protocols"
  - "T1102.001 - Dead Drop Resolver"
  - "T1217 - Browser Information Discovery"
  - "T1546.016 - Installer Packages"
  - "T1543.004 - Launch Daemon"
  - "T1678 - Delay Execution"
  - "T1573.001 - Symmetric Cryptography"
  - "T1078 - Valid Accounts"

malware_families:
  - "[[ICONICSTEALER]]"
  - "[[VEILEDSIGNAL]]"
  - "[[Gopuram]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]"
  - "[[DAVESHELL]]"
  - "[[SigFlip]]"

infrastructure_patterns:
  - "[[Supply Chain Compromise]]"
  - "[[Signed Update Abuse]]"
  - "[[Malicious DLL Side-Loading]]"
  - "[[Dead Drop Resolver]]"
  - "[[GitHub Abuse]]"

notable_victims: []
related_incidents: []

risk_level: "critical"
impact_assessment: "A trojanized 3CX software update enabled large-scale downstream exposure with selective follow-on targeting, creating enterprise-wide risk through trusted software distribution channels."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0057/"
  - "https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise"
  - "https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/"
  - "https://unit42.paloaltonetworks.com/3cxdesktopapp-supply-chain-attack/"
  - "https://www.3cx.com/blog/news/mandiant-security-update2/"
  - "https://www.cisa.gov/news-events/alerts/2023/03/30/supply-chain-attack-against-3cxdesktopapp"

tlp_classification: "TLP:CLEAR"

created: "2026-01-10"
updated: "2026-01-10"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# 3CX Supply Chain Attack (C0057)

## 1. Campaign Overview
The **3CX Supply Chain Attack (C0057)** describes a chained intrusion in which attackers gained access to the 3CX environment and then distributed **trojanized 3CX Desktop App installers/updates**, enabling downstream compromise of customer endpoints. Public reporting indicates the campaign used **malicious component loading and staged payload execution** to selectively pursue follow-on objectives, including activity assessed as aligned with **financially motivated (crypto-adjacent) targeting**.

This campaign matters because it demonstrates the defensive challenge of **trusted software distribution**: a legitimate vendor update channel can become a high-leverage initial access vector, and only a subset of victims may receive late-stage payloads—requiring defenders to combine **software inventory**, **endpoint telemetry**, and **network behavior** to scope impact.

## 2. Attribution Assessment
MITRE ATT&CK associates this campaign with **[[30_CIPHER/03_Threat_Actors/G1049 - AppleJeus|AppleJeus (G1049)]]**. Multiple independent investigations (including the vendor’s incident updates and major threat research) assessed the activity as consistent with **North Korea–linked tradecraft/clustering** (often referenced publicly as UNC4736 or related).  

**Attribution Confidence: 3-high**

## 3. Objectives & Intent
The publicly documented activity supports **financially motivated targeting** with emphasis on:
- **Selective follow-on access** (post-update staging and second-stage delivery)
- **Data access/collection** and environment discovery to identify high-value assets
- Targeting patterns frequently discussed in the context of **cryptocurrency ecosystem** interests (where explicitly stated by sources)

## 4. Targeting Analysis

### Sectors Targeted
- Cryptocurrency / blockchain ecosystem (selective follow-on targeting reported by major research)
- Broad cross-sector exposure via supply chain distribution (initial reach)

### Regions Targeted
- Global (3CX software distribution footprint; targeted follow-on varies by victim)

### Technologies / Platforms Targeted
- 3CX Desktop App endpoints (Windows/macOS)
- Electron application component loading chains
- Customer enterprise environments where the app was installed and updated

## 5. Campaign Tradecraft
High-level flow (source-supported, generalized):
1) Upstream compromise enables **trojanized 3CX software distribution**
2) Victim endpoints install/execute signed/trusted software containing **malicious components**
3) **Execution + injection/loading** behaviors activate staged functionality
4) **Network callbacks / dead-drop style tasking** used to gate follow-on payload delivery
5) **Selective secondary payload deployment** for narrowed targeting objectives

## 6. MITRE ATT&CK Alignment

### Techniques Observed
- [[T1195.002 - Compromise Software Supply Chain]]
- [[T1189 - Drive-by Compromise]]
- [[T1203 - Exploitation for Client Execution]]
- [[T1218.007 - Msiexec]]
- [[T1218.015 - Electron Applications]]
- [[T1574.001 - DLL]]
- [[T1055 - Process Injection]]
- [[T1055.002 - Portable Executable Injection]]
- [[T1620 - Reflective Code Loading]]
- [[T1027 - Obfuscated Files or Information]]
- [[T1027.009 - Embedded Payloads]]
- [[T1027.013 - Encrypted/Encoded File]]
- [[T1553.002 - Code Signing]]
- [[T1559 - Inter-Process Communication]]
- [[T1071.001 - Web Protocols]]
- [[T1102.001 - Dead Drop Resolver]]
- [[T1217 - Browser Information Discovery]]
- [[T1546.016 - Installer Packages]]
- [[T1543.004 - Launch Daemon]]
- [[T1678 - Delay Execution]]
- [[T1573.001 - Symmetric Cryptography]]
- [[T1078 - Valid Accounts]]

### Notable Tradecraft Characteristics
- **Trusted update channel abuse** (supply chain) to gain endpoint execution at scale
- **Staged/conditional payloading** (broad distribution, narrow follow-on targeting)
- **DLL/component loading chains** consistent with sideloading-style execution paths
- Use of **public web services for dead-drop/tasking** patterns (where observed)

## 7. Malware & Tooling

### Malware Families
- [[ICONICSTEALER]]
- [[VEILEDSIGNAL]]
- [[Gopuram]]

### Tools
- [[30_CIPHER/05_Malware/S1144 - FRP|FRP (S1144)]]
- [[DAVESHELL]]
- [[SigFlip]]

## 8. Infrastructure & Operational Patterns
- [[Signed Update Abuse]] to blend distribution with legitimate software trust
- [[Dead Drop Resolver]] behaviors to gate tasking/payload retrieval
- [[GitHub Abuse]] / public-service usage in support of operational staging (where reported)
- [[Malicious DLL Side-Loading]] patterns for execution inside trusted application context

## 9. Timeline of Campaign Activity (Table + Chronos)

### Timeline (Markdown)
|Date|Event|
|---|---|
|**2022-11**|First observed window begins (per MITRE campaign record).|
|**2023-03**|Last observed window (per MITRE campaign record).|
|**2023-03-30**|Major public reporting/analysis on 3CX supply-chain compromise (multiple research + public alerting).|
|**2023-04-20**|Follow-on public reporting emphasizing chained supply-chain aspects and attribution assessments.|

### Timeline (Chronos)
```chronos
- [2022-11]: First observed window begins (per MITRE campaign record).
- [2023-03]: Last observed window (per MITRE campaign record).
- [2023-03-30]: Major public reporting/analysis on 3CX supply-chain compromise (multiple research + public alerting).
- [2023-04-20]: Follow-on public reporting emphasizing chained supply-chain aspects and attribution assessments.
```

## 10. Notable Victims & Impact
### Victim Profile
Public reporting generally treats the initial exposure as supply-chain wide (customers running affected versions), with **selective follow-on targeting**. Many impacted organizations are not publicly enumerated.

### Operational Impact
- Risk of **endpoint compromise via trusted app install/update**
- Potential for **credential/session/material collection** and follow-on access depending on second-stage delivery
- Disproportionate risk to high-value targets (including crypto-adjacent organizations) when follow-on payloading occurs

## 11. Related Campaigns & Activity
No specific related campaign is asserted here beyond what’s explicitly linked in the cited public sources.  
**Pivot idea:** compare chained supply-chain mechanics and staged follow-on payloading patterns with other “broad first stage → selective second stage” operations.

## 12. Known Indicators (Contextual)
*(Pattern-based pivots only; do not treat as durable IOCs.)*
- New/unsigned or anomalous DLL loads in the 3CX Desktop App process tree
- Process injection/reflective loading telemetry from otherwise benign 3CX components
- Network callbacks from 3CX-related processes to unusual external endpoints; dead-drop style retrieval patterns
- Artifact review of installed 3CX versions vs. known affected build windows; unexpected post-update file additions

## 13. Defensive Considerations
- **Supply-chain blast-radius controls**
  - Maintain accurate **software inventory** and rapid **emergency update/rollback** capability for widely deployed apps
  - Segment high-risk endpoints and restrict egress where feasible for desktop apps that do not require broad outbound access

- **Endpoint detections**
  - Alert on **DLL sideloading indicators** (unexpected module paths, user-writable directories, non-standard load order)
  - Correlate **process injection + reflective loading** with signed vendor processes that typically do not exhibit these behaviors

- **Network detections**
  - Baseline normal 3CX Desktop App outbound behavior; alert on deviations and **dead-drop style** patterns
  - Monitor access to public services for tasking-like fetches from enterprise endpoints when not expected

- **Incident response scoping**
  - Identify affected versions, isolate systems, and assess for second-stage payload evidence (not all exposed hosts are equally targeted)

## 14. Analyst Notes
- This campaign is an archetype of **high-scale initial access** with **low-volume targeted follow-on**, so scoping must distinguish:
  1) exposed endpoints vs.
  2) endpoints that actually received/ran later-stage payloads.
- Completeness limits: public reporting emphasizes key phases, but full victim enumeration and complete second-stage targeting logic are not always public.
- Confidence recap:
  - Attribution: **high** (MITRE mapping + broad public assessments)
  - Tradecraft completeness: **medium**
  - Victim enumeration/impact specificity: **low–medium**

## 15. Further Reading / External Resources
- Google Threat Intelligence Group (Apr 2023) — chained supply-chain narrative and targeting context
- Volexity (Mar 2023) — technical incident chain and payload observations
- Unit 42 (Mar 2023) — execution chain and staged payload analysis
- CISA Alert (Mar 2023) — defensive framing and public-sector guidance
- 3CX/Mandiant incident updates (Apr 2023) — victim-side disclosure and investigation notes

## 16. References (APA)
- Cybersecurity and Infrastructure Security Agency. (2023, March 30). *Supply Chain Attack Against 3CXDesktopApp*. https://www.cisa.gov/news-events/alerts/2023/03/30/supply-chain-attack-against-3cxdesktopapp
- Google Threat Intelligence Group. (2023, April 20). *3CX Software Supply Chain Compromise*. https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise
- MITRE ATT&CK. (2025, October 23). *3CX Supply Chain Attack (C0057).* https://attack.mitre.org/campaigns/C0057/
- Palo Alto Networks Unit 42. (2023, March 30). *Threat Brief: 3CXDesktopApp Supply Chain Attack (Updated).* https://unit42.paloaltonetworks.com/3cxdesktopapp-supply-chain-attack/
- 3CX. (2023, April 20). *Mandiant Security Update – Initial Intrusion Vector*. https://www.3cx.com/blog/news/mandiant-security-update2/
- Volexity. (2023, March 30). *3CX Supply Chain Compromise Leads to ICONIC Incident*. https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/
