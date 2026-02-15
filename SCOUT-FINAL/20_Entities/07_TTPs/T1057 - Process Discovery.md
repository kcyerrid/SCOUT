---
entity_type: mitre_technique

technique_id: "T1057"
subtechnique_id: ""
technique_name: "Process Discovery"

tactic:
  - Discovery
platforms:
  - ESXi
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]]"
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]]"
  - "[[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]]"
  - "[[30_CIPHER/03_Threat_Actors/G0138 - Andariel|Andariel]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]"
  - "[[30_CIPHER/05_Malware/S0687 - Cyclops Blink|Cyclops Blink]]"
  - "[[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]"
associated_campaigns: []
related_techniques: []

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 3

created: 2026-01-06
updated: 2026-01-06

contributors: []
tags:
  - mitre
  - technique

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# T1057 - Process Discovery

## 1. Summary
Adversaries enumerate running processes to understand host activity, identify security tooling, locate target applications (e.g., databases, browsers), and decide follow-on actions such as credential theft, defense evasion, or lateral movement.

## 2. Technical Overview
Process discovery can be performed via:
- **Windows**: built-in utilities and scripting (e.g., Tasklist, PowerShell), or native API calls that enumerate processes.
- **Linux/macOS/ESXi**: `ps` and `/proc` inspection; ESXi supports process listing via platform tooling.
- **Network devices**: device CLI commands (e.g., “show processes”) depending on platform.

Adversaries may:
- Look for **security products** (EDR/AV process names)
- Identify **high-value apps** (database services, backup agents)
- Validate execution of their own tooling (beacon process presence)

## 3. Subtechnique Considerations
- No sub-techniques. Expect broad variability across OS and tooling.
- Process discovery is frequently used as part of **automated discovery playbooks**, sometimes repeatedly or at fixed intervals.

## 4. Procedure Examples
MITRE procedure examples include:
- Threat groups such as [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]], [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]], [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]], [[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]], and [[30_CIPHER/03_Threat_Actors/G0138 - Andariel|Andariel]] enumerating processes to shape follow-on behaviors.
- Multiple software families and frameworks performing process checks, including [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]] and others (per MITRE procedure examples).

## 5. Detection Guidance
Process discovery is common for administrators and IT tooling; detections should prioritize **context** and **sequence**.

High-signal patterns:
- Process discovery from **unusual parent processes** (Office apps, browsers, script hosts, unsigned binaries).
- Discovery shortly after suspicious ingress signals (macro execution, LOLBin abuse, new remote service, suspicious scheduled task).
- Enumeration coupled with immediate follow-on actions: credential access, security tool tampering, lateral movement.

Practical analytics ideas:
- Alert on process-listing utilities/scripting invoked by non-interactive accounts or rare binaries.
- Detect PowerShell process enumeration from encoded/obfuscated scripts, or from uncommon hosts.
- On Linux/macOS, flag suspicious access to `/proc` patterns (high-frequency reads) from newly dropped binaries.

### Data Source Notes
- **Endpoint telemetry**: process creation + command line + parent/child lineage, script logging (PowerShell, shell telemetry).
- **EDR**: module loads, API call telemetry where available, process access patterns.
- **Network device logs**: CLI command auditing for “show processes” and equivalent.

## 6. Response Guidance
1. **Validate legitimacy**: confirm whether the initiating process/user/host is consistent with admin tooling.
2. **Review lineage**: inspect parent process and preceding events to determine if this is part of an intrusion chain.
3. **Hunt follow-ons**: look for security tool discovery, tampering attempts, credential access, and remote execution.
4. **Contain if chained**: isolate host and collect triage artifacts if the behavior is part of a broader compromise.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1057 - Process Discovery|T1057]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1010 - Application Window Discovery|T1010]]

## 8. SOC Relevance
- Low standalone confidence; **high confidence when sequenced** with other intrusion behaviors.
- Useful for **early compromise** tracking and **defense evasion** hypotheses (security tool checks).

## 9. Threat Actor Usage
Examples from MITRE procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0006 - APT1|APT1]]
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]
- [[30_CIPHER/03_Threat_Actors/G0022 - APT3|APT3]]
- [[30_CIPHER/03_Threat_Actors/G0067 - APT37|APT37]]
- [[30_CIPHER/03_Threat_Actors/G0138 - Andariel|Andariel]]

## 10. Campaign Usage
- Not pinned here; correlate to your incident’s campaign timeline and intrusion chain.

## 11. Malware Usage
Representative examples include:
- [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]
- [[30_CIPHER/05_Malware/S0687 - Cyclops Blink|Cyclops Blink]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]

## 12. Mitigations
Limited direct prevention since process listing is a legitimate OS feature. Emphasize:
- Application control and least privilege
- Strong scripting controls and logging (PowerShell, shell auditing)
- Restrict/monitor admin tooling on non-admin endpoints
- Baseline normal admin behavior and alert on deviations

## 13. Testing & Validation
- Use a lab host to generate benign process listing from:
  - interactive admin session
  - non-admin user session
  - scripted automation
- Validate detection tuning by comparing:
  - parent process, user context, time-of-day, host role
  - adjacency to simulated suspicious events

## 14. References
- MITRE ATT&CK. (n.d.). *Process Discovery (T1057).* https://attack.mitre.org/techniques/T1057/
- Sygnia. (n.d.). *ESXi incident response and threat activity reporting (referenced by MITRE).* https://www.sygnia.co/
- Cisco. (n.d.). *IOS / network device operational commands and auditing guidance.* https://www.cisco.com/

## 15. Notes
- Treat repeated or bursty process discovery as higher risk, especially when paired with suspicious process ancestry or identity anomalies.
