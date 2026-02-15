---
entity_type: campaign
campaign_name: Operation MidnightEclipse
campaign_id: C0048
first_seen: 2024-03
last_seen: 2024-04
suspected_attribution: Unknown (publicly tracked as threat actor(s) exploiting CVE-2024-3400)
associated_actors: []
associated_malware:
  - "[[30_CIPHER/05_Malware/S1164 - UPSTYLE|UPSTYLE (S1164)]]"
target_geography:
  - Global (internet-exposed PAN-OS GlobalProtect)
target_sectors:
  - Organizations running affected PAN-OS GlobalProtect configurations
goals:
  - Initial access via edge RCE; credential theft; lateral movement; data staging/exfiltration
intel_sources:
  - https://attack.mitre.org/campaigns/C0048/
  - https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/
  - https://unit42.paloaltonetworks.com/cve-2024-3400/
  - https://security.paloaltonetworks.com/CVE-2024-3400
  - https://nvd.nist.gov/vuln/detail/cve-2024-3400
  - https://www.cisa.gov/news-events/alerts/2024/04/12/palo-alto-networks-releases-guidance-vulnerability-pan-os-cve-2024-3400
---

# Operation MidnightEclipse (C0048)

## Executive synopsis
A March–April 2024 campaign exploiting CVE-2024-3400 (PAN-OS GlobalProtect command injection) to gain unauthenticated RCE on perimeter devices, then pivoting through victim environments to steal credentials and stage/exfiltrate data. Reported tooling includes UPSTYLE and use of tunneling/proxy utilities (e.g., GOST) during post-exploitation.

## Timeline (high level)
- 2024-03: First observed exploitation window
- 2024-04: Last observed window in campaign entry

## Initial access
- Exploit: CVE-2024-3400 on affected PAN-OS GlobalProtect configurations
- Execution pattern: command injection used to fetch and run payloads (e.g., piping to bash)

## Tradecraft (ATT&CK highlights)
- Ingress:
  - Tool transfer via `wget`/HTTP
  - Unix shell execution (stdout-to-bash)
- Credential access & lateral movement:
  - Credential dumping (including NTDS.DIT in some victim contexts)
  - SMB and WinRM for internal movement
  - Use of valid (domain) accounts post-compromise
- Persistence / automation:
  - Cron jobs to retrieve payloads
- Staging/exfil:
  - Copying/staging within web app paths for later retrieval

## Malware / tooling
- UPSTYLE (S1164): attempted installs reported during the campaign
- Reverse proxy/tunneling:
  - GOST (Go Simple Tunnel) used as a reverse proxy/proxy component (per reporting)

## IOC / artifact summary (starter set)
- Perimeter device artifacts:
  - Unexpected file creation in web-accessible paths
  - Cron entries referencing external retrieval hosts
- Network:
  - Outbound from firewall management plane to suspicious VPS/AWS buckets
  - Lateral SMB/WinRM bursts after edge compromise
- Identity:
  - Sudden use of domain admin or newly compromised privileged accounts

## Detection & hunting (practical)
- Immediate exposure management:
  - Verify PAN-OS versions/configs against vendor guidance; apply fixes/hotfixes and mitigations
- Firewall telemetry:
  - Alert on unusual `wget`/bash execution traces and unexpected cron modifications
- Enterprise IR:
  - Assume credential exposure; rotate credentials and review AD for NTDS access indicators
  - Hunt for staging in web folders and unexpected egress to VPS/storage buckets

## Risks & implications
- Edge RCE collapses trust boundary; compromise can expand quickly into AD and enterprise assets.
- Post-exploitation indicates both credential-theft and operational “hands-on-keyboard” activity.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0048 - Operation MidnightEclipse|Operation MidnightEclipse (C0048)]]
- Malware: [[30_CIPHER/05_Malware/S1164 - UPSTYLE|UPSTYLE (S1164)]]

## Recommended OSINT queries
- "C0048 Operation MidnightEclipse CVE-2024-3400"
- "Volexity MidnightEclipse GOST UPSTYLE"
- "Unit42 CVE-2024-3400 post exploitation cron web folder staging"
- "PAN-OS CVE-2024-3400 detection artifacts"

## Confidence
High on exploit vector (CVE-2024-3400) and general post-exploitation behaviors (multi-source). Medium on actor attribution (public reporting does not conclusively map to a single named group in the campaign entry).

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
