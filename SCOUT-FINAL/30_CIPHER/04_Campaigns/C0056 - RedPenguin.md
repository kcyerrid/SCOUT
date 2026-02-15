---
scoutcam_id: C0056
entity_type: campaign
campaign_id: C0056
campaign_name: "RedPenguin"
aliases:
  - "RedPenguin"
first_observed: 2024-07
last_observed: 2025-03
campaign_status: unknown
risk_level: high
confidence: high
primary_objectives:
  - espionage_like
  - network_device_persistence
target_sectors: []
target_regions: []
associated_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886 (G1048)]]"
suspected_actors: []
associated_malware:
  - "[[30_CIPHER/05_Malware/S1220 - MEDUSA|MEDUSA (S1220)]]"
  - "[[30_CIPHER/05_Malware/S1219 - REPTILE|REPTILE (S1219)]]"
associated_tools: []
associated_ttps:
  - "[[20_Entities/07_TTPs/T1059.004 - Unix Shell|T1059.004 - Unix Shell]]"
  - "[[20_Entities/07_TTPs/T1059.008 - Network Device CLI|T1059.008 - Network Device CLI]]"
  - "[[20_Entities/07_TTPs/T1554 - Compromise Host Software Binary|T1554 - Compromise Host Software Binary]]"
  - "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information|T1140 - Deobfuscate/Decode Files or Information]]"
  - "[[20_Entities/07_TTPs/T1587.001 - Malware|T1587.001 - Malware]]"
  - "[[20_Entities/07_TTPs/T1573.001 - Symmetric Cryptography|T1573.001 - Symmetric Cryptography]]"
  - "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel|T1041 - Exfiltration Over C2 Channel]]"
  - "[[20_Entities/07_TTPs/T1203 - Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]"
  - "[[20_Entities/07_TTPs/T1562.003 - Impair Command History Logging|T1562.003 - Impair Command History Logging]]"
  - "[[20_Entities/07_TTPs/T1070.004 - File Deletion|T1070.004 - File Deletion]]"
  - "[[20_Entities/07_TTPs/T1070.007 - Clear Network Connection History and Configurations|T1070.007 - Clear Network Connection History and Configurations]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location|T1036.005 - Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1104 - Multi-Stage Channels|T1104 - Multi-Stage Channels]]"
  - "[[20_Entities/07_TTPs/T1040 - Network Sniffing|T1040 - Network Sniffing]]"
  - "[[20_Entities/07_TTPs/T1095 - Non-Application Layer Protocol|T1095 - Non-Application Layer Protocol]]"
  - "[[20_Entities/07_TTPs/T1571 - Non-Standard Port|T1571 - Non-Standard Port]]"
  - "[[20_Entities/07_TTPs/T1027.013 - Encrypted/Encoded File|T1027.013 - Encrypted/Encoded File]]"
  - "[[20_Entities/07_TTPs/T1057 - Process Discovery|T1057 - Process Discovery]]"
  - "[[20_Entities/07_TTPs/T1055 - Process Injection|T1055 - Process Injection]]"
  - "[[20_Entities/07_TTPs/T1090 - Proxy|T1090 - Proxy]]"
  - "[[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]"
  - "[[20_Entities/07_TTPs/T1014 - Rootkit|T1014 - Rootkit]]"
  - "[[20_Entities/07_TTPs/T1016 - System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]"
  - "[[20_Entities/07_TTPs/T1205 - Traffic Signaling|T1205 - Traffic Signaling]]"
  - "[[20_Entities/07_TTPs/T1078 - Valid Accounts|T1078 - Valid Accounts]]"
intel_sources:
  - https://attack.mitre.org/campaigns/C0056/
created: 2026-01-03
last_updated: 2026-01-03
tlp: CLEAR
tags:
  - scout-cam
  - mitre-campaign
  - juniper
  - routers
  - unc3886
---

## Overview
RedPenguin (C0056) is a Juniper-led investigation initiative tied to malware infections affecting Juniper MX Series routers and activity attributed to [[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886 (G1048)]]. ATT&CK associates the campaign with deployment of multiple custom TINYSHELL-based backdoors and includes rootkit usage such as [[30_CIPHER/05_Malware/S1219 - REPTILE|REPTILE (S1219)]] and [[30_CIPHER/05_Malware/S1220 - MEDUSA|MEDUSA (S1220)]].

## Linked Associations
### Threat Actors
- [[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886 (G1048)]]

### Malware
- [[30_CIPHER/05_Malware/S1219 - REPTILE|REPTILE (S1219)]]
- [[30_CIPHER/05_Malware/S1220 - MEDUSA|MEDUSA (S1220)]]

### TTPs (ATT&CK)
- [[20_Entities/07_TTPs/T1014 - Rootkit|T1014 - Rootkit]]
- [[20_Entities/07_TTPs/T1554 - Compromise Host Software Binary|T1554 - Compromise Host Software Binary]]
- [[20_Entities/07_TTPs/T1055 - Process Injection|T1055 - Process Injection]]
- [[20_Entities/07_TTPs/T1059.008 - Network Device CLI|T1059.008 - Network Device CLI]]
- [[20_Entities/07_TTPs/T1040 - Network Sniffing|T1040 - Network Sniffing]]
- [[20_Entities/07_TTPs/T1205 - Traffic Signaling|T1205 - Traffic Signaling]]
- [[20_Entities/07_TTPs/T1562.003 - Impair Command History Logging|T1562.003 - Impair Command History Logging]]
- [[20_Entities/07_TTPs/T1070.007 - Clear Network Connection History and Configurations|T1070.007 - Clear Network Connection History and Configurations]]
- [[20_Entities/07_TTPs/T1571 - Non-Standard Port|T1571 - Non-Standard Port]]
- [[20_Entities/07_TTPs/T1090.003 - Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]

## Detection Opportunities
- Integrity monitoring on Junos OS daemons/binaries for tampering aligned to [[20_Entities/07_TTPs/T1554 - Compromise Host Software Binary|T1554 - Compromise Host Software Binary]].
- Watch for anomalous packet “magic string” triggers aligned to [[20_Entities/07_TTPs/T1205 - Traffic Signaling|T1205 - Traffic Signaling]] and unexpected passive sniffing aligned to [[20_Entities/07_TTPs/T1040 - Network Sniffing|T1040 - Network Sniffing]].
- Non-standard listener ports aligned to [[20_Entities/07_TTPs/T1571 - Non-Standard Port|T1571 - Non-Standard Port]] plus evidence removal aligned to [[20_Entities/07_TTPs/T1070.004 - File Deletion|T1070.004 - File Deletion]] / [[20_Entities/07_TTPs/T1070.007 - Clear Network Connection History and Configurations|T1070.007 - Clear Network Connection History and Configurations]].

## Notes
- Canonical vault links for Threat Actor / Malware / TTPs have been restored to match the master prompt path + filename conventions.
