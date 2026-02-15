---
entity_type: campaign
campaign_name: ShadowRay
campaign_id: C0045
first_seen: 2023-09
last_seen: 2023-09
suspected_attribution: Unknown (opportunistic exploitation / financially motivated suspected)
associated_actors: []
associated_malware:
  - XMRig (cryptominer)
target_geography:
  - Global (internet-exposed Ray deployments)
target_sectors:
  - Any org exposing Ray (AI/ML + distributed compute) services
goals:
  - Compute hijacking (cryptomining); potential lateral discovery via exposed workloads
intel_sources:
  - https://attack.mitre.org/campaigns/C0045/
  - https://www.oligo.security/blog/shadowray-attack-ai-workloads-cve-2023-48022
  - https://nvd.nist.gov/vuln/detail/CVE-2023-48022
  - https://www.anyscale.com/blog/cve-2023-48022-remote-code-execution-in-ray
---

# ShadowRay (C0045)

## Executive synopsis
A short-lived (publicly reported) exploitation campaign targeting exposed Ray instances, leveraging CVE-2023-48022 to execute commands, dump credentials (e.g., `/etc/shadow`), and deploy cryptomining payloads (commonly XMRig). Public discussion includes dispute/clarification on exploitability conditions depending on deployment posture.

## Timeline (high level)
- 2023-09: First/last seen window in ATT&CK campaign entry (publicly reported)

## Initial access
- Exploit: CVE-2023-48022 in Ray (exposed service / insecure deployment conditions)
- Impact path: remote command execution leading to payload download + execution

## Tradecraft (ATT&CK highlights)
- Execution:
  - Python (base64-encoded payloads executed via interpreter)
  - Shell execution and pseudo-terminal allocation patterns
- Credential access:
  - Read of `/etc/shadow` for password hash capture
- Discovery / collection:
  - `uname`, host discovery, and environment enumeration patterns
- Ingress tool transfer:
  - Download of XMRig and other utilities
- Defense evasion:
  - Encoded/obfuscated payload delivery

## Tooling
- Cryptomining: XMRig (or equivalent)
- Canary interaction: use of external interaction services (e.g., Interactsh) reported in some analyses

## IOC / artifact summary (starter set)
- Network:
  - Unexpected outbound to mining pools; sustained high-bandwidth TCP to pool endpoints
  - Ray head/node traffic patterns from unusual source IPs
- Host:
  - New miner binaries, cron/systemd persistence attempts (environment-dependent)
  - Spikes in CPU/GPU utilization on AI worker nodes

## Detection & hunting (practical)
- Exposure controls (highest ROI):
  - Ensure Ray is not internet-exposed; restrict to private networks/VPN and strong auth
- Runtime monitoring:
  - Alert on creation/execution of known miner binaries; block pool domains/IPs at egress
- Credential theft:
  - Hunt for reads of `/etc/shadow` and unexpected archive/exfil staging in worker directories

## Risks & implications
- AI/ML workloads are attractive for compute theft; incidents can be noisy (resource spikes) but fast-moving.
- Even “single-purpose” crypto-mining intrusions can become staging points for broader cloud compromise depending on IAM and secrets exposure.

## Links (internal workspace)
- Campaign: [[30_CIPHER/03_Campaigns/C0045 - ShadowRay|ShadowRay (C0045)]]

## Recommended OSINT queries
- "C0045 ShadowRay CVE-2023-48022"
- "Oligo ShadowRay Ray AI workloads cryptomining"
- "CVE-2023-48022 Ray exploitation conditions"
- "Ray cluster exposed miner XMRig indicators"

## Confidence
Medium: strong technical reporting on exploit chain and cryptomining outcomes; lower confidence on actor identity and true prevalence due to limited public telemetry.

## Changelog
- 2026-01-03: Initial SCOUT-CAM note created.
