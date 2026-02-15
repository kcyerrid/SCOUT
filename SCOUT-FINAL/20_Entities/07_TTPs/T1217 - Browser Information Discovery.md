---
entity_type: mitre_technique

technique_id: "T1217"
subtechnique_id: ""
technique_name: "Browser Information Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - Linux
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0082 - APT38]]"
  - "[[30_CIPHER/03_Threat_Actors/G0117 - Fox Kitten]]"
  - "[[30_CIPHER/03_Threat_Actors/G0049 - OilRig]]"
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1246 - BeaverTail]]"
  - "[[30_CIPHER/05_Malware/S0363 - Empire]]"
  - "[[30_CIPHER/05_Malware/S1042 - SUGARDUMP]]"
  - "[[30_CIPHER/05_Malware/S1240 - RedLine Stealer]]"
associated_campaigns:
  - "C0057"
  - "C0044"
  - "C0042"
related_techniques: []

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

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

## 1. Summary
Browser Information Discovery (T1217) is the enumeration of locally stored browser artifacts—such as bookmarks, history, cookies, saved form data, and installed extensions—to understand the victim environment, identify internal resources, and find additional targets or access opportunities.

## 2. Technical Overview
Browsers store high-value reconnaissance data:
- **Bookmarks / favorites** can reveal internal dashboards, admin portals, VPN endpoints, and SaaS resources.
- **History** can reveal operational workflows and frequently used internal applications.
- **Cookies / session artifacts** can indicate logged-in services and may enable session-based abuse if combined with other actions.
- **Extensions** can reveal password managers, MFA tools, crypto wallets, and enterprise tooling.

Common access patterns:
- Reading browser profile directories and database files (e.g., Chromium SQLite stores).
- Enumerating installed extensions and related metadata.
- Collecting artifacts across multiple browsers to maximize coverage.

## 3. Subtechnique Considerations
This technique has no sub-techniques.

## 4. Procedure Examples
Examples documented in ATT&CK include:
- Campaigns and malware that steal **browser history/bookmarks/cookies** for reconnaissance and follow-on targeting.
- Threat actors using bookmarks to identify **internal resources and assets**.

## 5. Detection Guidance
High-fidelity detection usually hinges on **file access telemetry** + **process context**.

High-signal detection themes:
- **Non-browser processes** accessing browser data stores (especially scripting engines, LOLBins, or unknown binaries).
- **Bulk reads** of browser profile directories shortly after suspicious execution/persistence.
- **Cross-browser harvesting** (Chrome + Edge + Firefox in short time window).
- Access to browser extension directories associated with authentication/crypto tooling.

Practical analytics:
- Alert when PowerShell/cmd/wscript/mshta/unknown binaries access known browser artifact paths and read SQLite/JSON stores at volume.
- Correlate browser artifact access with:
  - infostealer indicators (credential store access, network beacons, archive creation)
  - suspicious outbound connections soon after collection
- Baseline enterprise tools that legitimately access browser data (EDR, IT inventory, DLP) and suppress those with tight allowlists.

### Data Source Notes
Recommended telemetry:
- Endpoint file access telemetry for browser profile directories and key artifact files (history/bookmarks/cookies/extension manifests).
- Process creation lineage (parent chain, signer, user context, reputation).
- Network telemetry for post-collection exfiltration patterns (new domains, unusual user agents, short-burst uploads).

## 6. Response Guidance
1. **Identify scope**: which browsers and which artifact types were accessed (history, bookmarks, cookies, extensions).
2. **Attribute process**: determine whether access was by a known browser, an approved enterprise tool, or an unknown binary/script.
3. **Hunt follow-on**: look for archive creation, staging directories, outbound uploads, and credential access behaviors.
4. **Contain**: isolate host and reset relevant sessions if suspicious (invalidate tokens, force sign-out where possible).
5. **Recover**: review access to internal portals referenced by bookmarks/history; assess whether the attacker pivoted to those resources.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1217 - Browser Information Discovery|T1217]]

## 8. SOC Relevance
- High value for detecting **infostealers**, **post-compromise recon**, and **operator targeting** of internal resources.
- Often appears near credential access and collection/exfiltration stages; treat as an escalation trigger when paired with suspicious network activity.

## 9. Threat Actor Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0082 - APT38]]
- [[30_CIPHER/03_Threat_Actors/G0117 - Fox Kitten]]
- [[30_CIPHER/03_Threat_Actors/G0049 - OilRig]]
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon]]

## 10. Campaign Usage
Examples referenced in ATT&CK procedure examples include:
- C0057 (3CX Supply Chain Attack)
- C0044 (Juicy Mix)
- C0042 (Outer Space)

## 11. Malware Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S1246 - BeaverTail]]
- [[30_CIPHER/05_Malware/S0363 - Empire]]
- [[30_CIPHER/05_Malware/S1042 - SUGARDUMP]]
- [[30_CIPHER/05_Malware/S1240 - RedLine Stealer]]

## 12. Mitigations
- MITRE notes this behavior can be difficult to prevent because it abuses normal local data storage.
- Reduce impact by:
  - limiting local storage of sensitive browser data where feasible
  - enforcing strong session controls (shorter session lifetimes, conditional access)
  - hardening endpoints to prevent unauthorized code execution

## 13. Testing & Validation
- Verify coverage for browser artifact paths across:
  - Chrome/Chromium, Edge, Firefox, Safari (where applicable)
- Purple-team scenarios:
  - non-browser process reads browser SQLite stores
  - scripted enumeration of extension directories
  - correlate reads → archive → outbound upload

## 14. References
- MITRE ATT&CK. (n.d.). *Browser Information Discovery (T1217)*. https://attack.mitre.org/techniques/T1217/
- MITRE ATT&CK. (n.d.). *Detection of Local Browser Artifact Access for Reconnaissance (DET0013)*. https://attack.mitre.org/detectionstrategies/DET0013/
- Volexity. (2023, March). *3CX Supply Chain Attack* (referenced by ATT&CK for T1217 procedure examples). https://attack.mitre.org/techniques/T1217/

## 15. Notes
- Prioritize response when browser artifact access is performed by unusual processes and followed by outbound connections or staging activity.
