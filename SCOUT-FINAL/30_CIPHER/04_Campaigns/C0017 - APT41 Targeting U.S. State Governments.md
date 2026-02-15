---
entity_type: campaign

campaign_name: "APT41 Targeting U.S. State Governments"
campaign_id: "C0017"

associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|G0096 - APT41]]"
suspected_actors: []

attribution_confidence: "3-high"
confidence_notes: "Attribution is strong: MITRE ATT&CK explicitly associates the campaign to APT41 and references detailed vendor reporting with observed exploitation, tooling, and infrastructure."

first_observed: "2021-05"
last_observed: "2022-02"
campaign_status: "concluded"

primary_objectives: ["espionage", "data_theft"]
secondary_objectives: ["credential_access"]

target_sectors: ["state_government"]
target_regions: ["United States"]
target_technologies: [".NET web applications", "Windows", "Internet-facing web apps", "Cloudflare services"]

initial_access_vectors: ["exploit_public_facing_application"]
key_ttp_themes: ["rapid_recompromise", "webshells", "credential_dumping", "dns_exfiltration", "cdn_proxying"]

malware_families:
  - "[[30_CIPHER/05_Malware/S1052 - DEADEYE|S1052 - DEADEYE]]"
  - "[[30_CIPHER/05_Malware/S1051 - KEYPLUG|S1051 - KEYPLUG]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|S0154 - Cobalt Strike]]"
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|S0002 - Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0105 - dsquery|S0105 - dsquery]]"
  - "[[30_CIPHER/05_Malware/S0097 - Ping|S0097 - Ping]]"

infrastructure_patterns: ["cloudflare_c2", "dead_drop_resolvers", "dns_exfiltration"]
notable_victims: ["U.S. state government networks (multiple)"]
related_incidents: []

risk_level: "high"
impact_assessment: "Successful compromise of multiple state government networks via exploitation of internet-facing applications; observed PII exfiltration and rapid re-compromise attempts increase operational risk."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0017/"
  - "https://www.mandiant.com/resources/blog/apt41-targeting-us-state-governments"
  - "https://www.bleepingcomputer.com/news/security/chinese-hackers-apt41-target-us-state-governments-via-0-day-exploits/"

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
**C0017** is an **APT41** campaign conducted between **May 2021** and **February 2022** that compromised at least six **U.S. state government** networks by exploiting **vulnerable public-facing web applications**. Reporting notes APT41’s ability to adapt quickly—leveraging both publicly disclosed vulnerabilities and **zero-days**—and in some cases **re-compromising** victims after remediation.

---

## Attribution Assessment
Attribution confidence is **high** because the campaign is explicitly linked to **[[30_CIPHER/03_Threat_Actors/G0096 - APT41|G0096 - APT41]]** in MITRE ATT&CK and grounded in detailed vendor reporting that includes exploitation, malware families, and infrastructure patterns.

---

## Objectives & Intent
- **Primary:** espionage and **PII data theft**
- **Secondary:** credential access enabling continued intrusion capability

---

## Targeting Analysis
### Sectors Targeted
- U.S. state government entities (multiple networks)

### Regions Targeted
- United States

### Technologies / Platforms Targeted
- Internet-facing web applications (including apps impacted by Log4j-era issues)
- Windows environments
- Cloudflare-proxied infrastructure for C2/exfil

---

## Campaign Tradecraft
### High-Level Tradecraft Summary
The campaign combined **public-facing application exploitation** with staged payload delivery, webshell deployment, credential dumping, and multiple exfiltration paths (including **DNS-based exfiltration** and web services). Notably, APT41 used **Cloudflare** both to proxy C2 traffic and to support exfiltration workflows.

---

## MITRE ATT&CK Alignment
### Techniques Observed
- [[T1134 - Access Token Manipulation]]
- [[T1071.001 - Web Protocols]]
- [[T1560.003 - Archive via Custom Method]]
- [[T1059.003 - Windows Command Shell]]
- [[T1059.007 - JavaScript]]
- [[T1005 - Data from Local System]]
- [[T1001.003 - Protocol or Service Impersonation]]
- [[T1074.001 - Local Data Staging]]
- [[T1140 - Deobfuscate/Decode Files or Information]]
- [[T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1041 - Exfiltration Over C2 Channel]]
- [[T1567 - Exfiltration Over Web Service]]
- [[T1190 - Exploit Public-Facing Application]]
- [[T1574 - Hijack Execution Flow]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1680 - Local Storage Discovery]]
- [[T1036.004 - Masquerade Task or Service]]
- [[T1036.005 - Match Legitimate Resource Name or Location]]
- [[T1027 - Obfuscated Files or Information]]
- [[T1027.002 - Software Packing]]
- [[T1588.002 - Tool]]
- [[T1003.002 - Security Account Manager]]
- [[T1090 - Proxy]]
- [[T1053.005 - Scheduled Task]]
- [[T1505.003 - Web Shell]]
- [[T1016 - System Network Configuration Discovery]]
- [[T1033 - System Owner/User Discovery]]
- [[T1102 - Web Service]]
- [[T1102.001 - Dead Drop Resolver]]

### Notable Tradecraft Characteristics
- **Rapid adaptation** to vulnerability disclosures and post-remediation re-entry attempts
- **Cloudflare** used for proxying and operational concealment
- **DNS lookups** used as an exfiltration mechanism

---

## Malware & Tooling
### Malware Families / Backdoors
- [[30_CIPHER/05_Malware/S1052 - DEADEYE|S1052 - DEADEYE]]
- [[30_CIPHER/05_Malware/S1051 - KEYPLUG|S1051 - KEYPLUG]]

### Tools (COTS / LOLBins)
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|S0154 - Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|S0002 - Mimikatz]]
- [[30_CIPHER/05_Malware/S0105 - dsquery|S0105 - dsquery]]
- [[30_CIPHER/05_Malware/S0097 - Ping|S0097 - Ping]]

---

## Infrastructure & Operational Patterns
- Cloudflare-backed C2 and exfiltration workflows
- Dead drop resolver usage hosted on community forums (resolver rotation observed)
- DNS-based exfiltration via encoded subdomain lookups

---

## Timeline of Campaign Activity (Chronos)
```chronos
- [2021-05]: First observed compromise activity (campaign start window).
- [2021-12]: Exploitation of Log4j-era vulnerabilities reported within victim environments.
- [2022-02]: Last observed activity in the campaign window.
- [2022-03-08]: Vendor report published summarizing APT41 targeting U.S. state governments.
```

## Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2021-05 | First observed compromise activity (campaign start window) |
| 2021-12 | Log4j-era exploitation reported in victim environments |
| 2022-02 | Last observed activity |
| 2022-03-08 | Vendor reporting published summarizing campaign |

---

## Notable Victims & Impact
- At least **six** U.S. state government networks reported compromised.
- Observed **PII exfiltration** elevates privacy/regulatory and national-level risk.

---

## Defensive Considerations
- Prioritize patching and monitoring of **public-facing applications**; validate remediation effectiveness.
- Detect **webshells** and suspicious JScript/.NET ViewState patterns where relevant.
- Monitor for scheduled task tampering and IAT/library hijack indicators in Microsoft binaries.
- Baseline and alert on anomalous DNS query patterns consistent with data encoding.

---

## Analyst Notes
This campaign is a strong example of “**edge-to-core**” intrusion behavior: exploit perimeter apps → drop payloads → stage/obfuscate data → exfiltrate via multiple channels, with resilience through re-compromise.

---

## References (APA)
- MITRE ATT&CK. (2025, April 16). *C0017 (Campaign)*. Retrieved 2026-01-03 from https://attack.mitre.org/campaigns/C0017/
- Brown, R., Ta, V., Bienstock, D., Ackerman, G., & Wolfram, J. (2022, March 8). *Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments*. Mandiant. Retrieved 2026-01-03 from https://www.mandiant.com/resources/blog/apt41-targeting-us-state-governments
- Cimpanu, C. (2022, March 9). *Chinese hackers APT41 target US state governments via 0-day exploits*. BleepingComputer. Retrieved 2026-01-03 from https://www.bleepingcomputer.com/news/security/chinese-hackers-apt41-target-us-state-governments-via-0-day-exploits/
