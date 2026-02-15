---
entity_type: threat_actor
actor_name: "Windigo"
common_name: "Windigo"
actor_id: "G0124"
actor_type: ""
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: ""
first_seen: "2011-01-01"
last_seen: "2019-01-01"
status: ""

motivations: []
objectives:
  - "Compromise Linux/Unix servers at scale"
  - "Maintain SSH-based persistence and monetize via spam infrastructure"
victimology_summary: "Group operating since at least 2011 that compromised thousands of Linux/Unix servers using the Ebury SSH backdoor to create a spam botnet; despite law enforcement action against creators, operators continued updating Ebury through 2019."
target_sectors: []
target_regions: []

related_groups: []

malware:
  - "[[30_CIPHER/05_Malware/Ebury]]"
tools: []

infrastructure: []
ttps:
  - "[[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter|T1059 - Command and Scripting Interpreter]]"
  - "[[20_Entities/07_TTPs/T1005 - Data from Local System|T1005 - Data from Local System]]"
  - "[[20_Entities/07_TTPs/T1189 - Drive-by Compromise|T1189 - Drive-by Compromise]]"
  - "[[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]"
  - "[[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]"
notable_claims: []
intel_sources:
  - "https://attack.mitre.org/groups/G0124/"
  - "https://www.welivesecurity.com/"
tags:
  - "scout"
  - "mitre"
  - "threat_actor"
  - "group"
  - "G0124"
  - "linux"
  - "botnet"

created: "<% tp.date.now(\"YYYY-MM-DD\") %>"
last_modified: "<% tp.date.now(\"YYYY-MM-DD\") %>"
---

## 1. BLUF / Executive Summary
Windigo (G0124) is tracked for large-scale compromise of Linux/Unix servers using the **Ebury** SSH backdoor to enable a **spam botnet** ecosystem. ATT&CK notes operations since at least **2011** and continued Ebury updates through **2019**, with tradecraft including scripting for recon, local credential collection, drive-by delivery of Windows malware (in related activity), and proxying/traffic relays.

## 2. Attribution Notes
- **MITRE ATT&CK ID:** G0124
- **Sponsor/country:** Not explicitly stated on the ATT&CK Group page.

## 3. Motivations & Objectives
- Motivations not explicitly stated by ATT&CK; activity indicates monetization via botnet/spam infrastructure and sustained access to server fleets.

## 4. Targeting Profile
- **Targets:** Linux/Unix servers at scale (ATT&CK), consistent with infrastructure compromise for relays, spam, and credential harvesting.

## 5. Tradecraft Overview
- **Access & persistence:** SSH backdoor ecosystem (Ebury) enabling credential theft and continued access.
- **Collection:** scripts used for credential harvesting from local system and file discovery checks.
- **Infrastructure role:** servers used as proxies/relays (ATT&CK Proxy technique).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1059 - Command and Scripting Interpreter|T1059 - Command and Scripting Interpreter]]
- [[20_Entities/07_TTPs/T1005 - Data from Local System|T1005 - Data from Local System]]
- [[20_Entities/07_TTPs/T1083 - File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]
- [[20_Entities/07_TTPs/T1189 - Drive-by Compromise|T1189 - Drive-by Compromise]]

## 7. Malware & Tools Used
- Malware:
  - [[30_CIPHER/05_Malware/Ebury]] (SSH backdoor referenced on ATT&CK Group page)

## 8. Infrastructure Patterns
- Compromised Linux/Unix servers repurposed as:
  - SSH credential theft nodes
  - outbound proxy/relay infrastructure
  - spam botnet components

## 9. Campaign History
- Long-running operation spanning 2011–2019 per ATT&CK description, including continued tooling updates after law enforcement intervention.

## 10. Known Indicators
- Server-side anchors:
  - Unauthorized SSH daemon/library modifications; anomalous SSH auth flows.
  - Unexpected outbound SMTP traffic or mail transfer spikes from servers.
  - Proxy/relay behavior: unusual egress to many destinations, TOR-like relay patterns, or sudden increases in connection fan-out.

## 11. Defensive Recommendations
- **Linux hardening:** protect SSH keys; enforce MFA for privileged SSH; restrict password auth; monitor SSH binary integrity.
- **Network:** egress filtering for SMTP from non-mail hosts; monitor proxy behaviors and unusual fan-out.
- **IR playbook:** treat as fleet compromise—scope laterally by shared SSH keys, config management artifacts, and common admin accounts.

## 12. Analyst Notes
- Detection is strongest via **SSH telemetry + integrity monitoring** and **network egress** (SMTP/proxy signals).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group: https://attack.mitre.org/groups/G0124/
- ESET research portal: https://www.welivesecurity.com/

## 14. References
- MITRE ATT&CK. (n.d.). *Windigo (G0124).* https://attack.mitre.org/groups/G0124/
- ESET. (n.d.). *WeLiveSecurity (research portal).* https://www.welivesecurity.com/

## 15. Notes
- Add environment-specific detection logic for SSH anomalies (new shared objects, PAM tampering, unauthorized rootkit-like changes).
