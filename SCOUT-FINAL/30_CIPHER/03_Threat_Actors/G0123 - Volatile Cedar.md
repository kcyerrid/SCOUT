---
entity_type: threat_actor
actor_name: "Volatile Cedar"
common_name: "Volatile Cedar"
actor_id: "G0123"
actor_type: ""
aliases:
  - "Lebanese Cedar"
country_of_origin: "Lebanon"
suspected_sponsors: []
attribution_confidence: ""
first_seen: "2012-01-01"
last_seen: ""
status: ""

motivations:
  - "Political and ideological"
objectives:
  - "Unauthorized access to public-facing servers"
  - "Persistent access via web shells and custom tooling"
victimology_summary: "Lebanese threat group operating since at least 2012, motivated by political and ideological interests, targeting individuals, companies, and institutions worldwide; observed compromising public-facing web servers, deploying web shells, and using the Explosive malware family."
target_sectors: []
target_regions: []

related_groups: []

malware:
  - "[[30_CIPHER/05_Malware/S0569 - Explosive|Explosive]]"
tools: []

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell|T1505.003 - Server Software Component: Web Shell]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0123/"
  - "https://www.clearskysec.com/"
  - "https://www.kaspersky.com/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0123"
  - "webshell"
  - "intrusion"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Volatile Cedar (G0123) is a **Lebanese** threat group operating since at least **2012**, motivated by **political and ideological interests**, and targeting entities worldwide. ATT&CK documents tradecraft focused on **public-facing web server compromise**, **web shell deployment**, and **follow-on tool transfer**, including the **Explosive** malware family (S0569).

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0123
- **Alias:** Lebanese Cedar (ATT&CK associated name)
- **Country of origin:** Lebanon (explicitly described by ATT&CK)
- **Sponsor:** Not specified by ATT&CK.

## 3. Motivations & Objectives
- **Motivation:** Political and ideological (ATT&CK).
- **Objectives:** compromise internet-facing applications, maintain persistence on servers, deploy tooling for collection and control.

## 4. Targeting Profile
- **Victimology:** individuals, companies, and institutions worldwide (ATT&CK). Specific sectors/regions are campaign-dependent.

## 5. Tradecraft Overview
- **Initial access:** exploit public-facing applications (manual + automated discovery and exploitation referenced in ATT&CK).
- **Persistence/control:** deploy web shells and server-side components.
- **Post-compromise:** transfer additional tooling as needed.

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1505.003 - Server Software Component: Web Shell|T1505.003 - Server Software Component: Web Shell]]
- [[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/S0569 - Explosive|Explosive]]

## 8. Infrastructure Patterns
- Compromise of public web servers and deployment of web shells; infrastructure pivots often begin with vulnerable internet-facing services.

## 9. Campaign History
- ATT&CK documents Volatile Cedar activity and its evolution since 2012; campaign naming varies by reporting source.

## 10. Known Indicators
- Focus on server telemetry:
  - New/unexpected web-accessible scripts and anomalous POST traffic to atypical endpoints.
  - Suspicious child processes spawned by web server workers.
  - New admin accounts/SSH keys (where applicable) following exploitation.

## 11. Defensive Recommendations
- **Exposure management:** continuous patching and vulnerability scanning of public-facing apps.
- **Web server hardening:** WAF tuned to exploit attempts; file integrity monitoring of web roots; least privilege for web workers.
- **Detection engineering:** alerts on web server process spawning, suspicious command execution, and web shell-like HTTP patterns.

## 12. Analyst Notes
- Highest-signal in many intrusions: exploit attempt telemetry → web shell placement → tool transfer and interactive control.

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0123/
- ClearSky research portal: https://www.clearskysec.com/
- Kaspersky (portal): https://www.kaspersky.com/

## 14. References
- MITRE ATT&CK. (n.d.). *Volatile Cedar (G0123).* https://attack.mitre.org/groups/G0123/
- ClearSky Cyber Security. (n.d.). *ClearSky (research portal).* https://www.clearskysec.com/
- Kaspersky. (n.d.). *Kaspersky (portal).* https://www.kaspersky.com/

## 15. Notes
- Enrich with organization-specific web logs (IIS/Apache/Nginx) and EDR on server endpoints to scope post-exploit activity.
