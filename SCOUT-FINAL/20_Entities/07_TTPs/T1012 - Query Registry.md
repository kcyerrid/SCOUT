---
entity_type: mitre_technique

technique_id: "T1012"
subtechnique_id: ""
technique_name: "Query Registry"

tactic:
  - Discovery
platforms:
  - Windows
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]"
  - "[[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0414 - BabyShark|BabyShark]]"
  - "[[30_CIPHER/05_Malware/S0344 - Azorult|Azorult]]"
associated_campaigns: []
related_techniques: []

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 3

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

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

# T1012 - Query Registry

## 1. Summary
Adversaries query the Windows Registry to gather system, configuration, software, and security details. Registry reconnaissance supports decisions such as what payloads to run, which defenses are present, what network settings apply, and where to establish persistence.

## 2. Technical Overview
Common query targets:
- Installed software inventory, security tools, and system configuration
- Network/proxy settings and remote access configuration
- User environment and application configuration
- RDP/client history and connection artifacts (context-dependent)

Query methods:
- Built-in command-line utilities
- PowerShell and WMI-backed discovery
- Direct Registry API access by malware/tooling

## 3. Subtechnique Considerations
- No sub-techniques.
- Registry querying is pervasive in both benign and malicious tooling; detection should emphasize **context and intent**.

## 4. Procedure Examples
MITRE procedure examples include:
- Threat groups such as [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]], [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]], and [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]] querying registry values for host and configuration discovery.
- Malware families including [[30_CIPHER/05_Malware/S0414 - BabyShark|BabyShark]] and [[30_CIPHER/05_Malware/S0344 - Azorult|Azorult]] performing registry queries as part of their reconnaissance and execution logic.

## 5. Detection Guidance
Registry queries are common; focus on **rare processes**, **suspicious ancestry**, and **sensitive key patterns**.

High-signal patterns:
- Registry query activity from Office apps, browsers, script hosts, LOLBins, or newly dropped binaries.
- Enumeration of many keys/values in rapid succession (inventory sweep).
- Queries for security-relevant locations (security product keys, policy/hardening keys), followed by defense evasion or credential access.

Practical analytics ideas:
- Detect unusual `reg.exe` usage (or equivalent) with suspicious parent processes or from non-admin endpoints.
- PowerShell-based registry discovery from encoded/obfuscated scripts.
- Correlate registry query bursts with:
  - new persistence artifacts
  - suspicious network beacons
  - privilege escalation attempts

### Data Source Notes
- **Windows Security + EDR**: process creation + command line, script telemetry, parent/child lineage.
- **PowerShell logging**: Script Block + module logging (where enabled).
- **Registry monitoring** (EDR): key/value read telemetry if supported; otherwise infer from process + command line.

## 6. Response Guidance
1. **Identify the query origin**: process lineage, user context, signer reputation, and execution source.
2. **Determine target intent**: what keys were queried and whether they map to security posture, persistence, or credential artifacts.
3. **Pivot to follow-ons**: look for subsequent tampering, persistence creation, credential access, or lateral movement.
4. **Contain and collect**: if malicious, isolate host; collect triage artifacts and preserve relevant telemetry.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1012 - Query Registry|T1012]]

## 8. SOC Relevance
- Valuable for early-stage situational awareness in intrusions, but must be **tuned** to avoid high false positives.
- Strongest when combined with process ancestry and next-step correlation.

## 9. Threat Actor Usage
Examples from MITRE procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]

## 10. Campaign Usage
- Not pinned here; correlate registry-query bursts with your incident timeline.

## 11. Malware Usage
Representative examples include:
- [[30_CIPHER/05_Malware/S0414 - BabyShark|BabyShark]]
- [[30_CIPHER/05_Malware/S0344 - Azorult|Azorult]]

## 12. Mitigations
Registry querying itself is hard to prevent. Mitigate by:
- Principle of least privilege and application control for scripting/LOLBins
- Strong logging (process creation, PowerShell) and EDR coverage
- Reducing local admin footprint and enforcing secure baselines

## 13. Testing & Validation
- In a lab, generate benign registry queries from:
  - IT inventory tools
  - interactive admin troubleshooting
- Then test suspicious patterns (encoded PowerShell, unusual parents) and validate alerts:
  - correct lineage capture
  - key pattern detection
  - correlation to follow-on behaviors

## 14. References
- MITRE ATT&CK. (n.d.). *Query Registry (T1012).* https://attack.mitre.org/techniques/T1012/
- Palo Alto Networks Unit 42. (n.d.). *BabyShark analysis and related telemetry (referenced by MITRE procedure examples).* https://unit42.paloaltonetworks.com/
- Microsoft. (n.d.). *Reg command documentation.* https://learn.microsoft.com/windows-server/administration/windows-commands/reg

## 15. Notes
- Consider maintaining a curated list of “sensitive registry keys” tied to your org’s security controls and crown-jewel applications to improve detection precision.
