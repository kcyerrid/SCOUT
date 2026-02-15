---
entity_type: mitre_technique

technique_id: "T1115"
subtechnique_id: ""
technique_name: "Clipboard Data"

tactic:
  - "TA0009 - Collection"
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
  - "[[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0455 - Metamorfo|Metamorfo]]"
  - "[[30_CIPHER/05_Malware/S0283 - jRAT|jRAT]]"
  - "[[30_CIPHER/05_Malware/S0250 - Koadic|Koadic]]"
  - "[[30_CIPHER/05_Malware/S0148 - RTM|RTM]]"
associated_campaigns: []
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
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
**Clipboard Data** collects information stored in the OS clipboard (text, images, copied secrets). Adversaries may also monitor and replace clipboard contents (e.g., swapping cryptocurrency wallet addresses) to enable fraud or credential theft.

## 2. Technical Overview
Typical mechanisms:
- **Direct clipboard reads** using OS utilities/APIs (e.g., Windows clipboard tooling; macOS/Linux commands noted on the ATT&CK page).
- **Clipboard monitoring** via event listeners or periodic polling to capture newly copied content.
- **Clipboard manipulation** to replace content after copy events (common in financial malware).

Clipboard access is often paired with:
- staging/aggregation,
- credential theft workflows,
- exfiltration, or transaction redirection.

## 3. Subtechnique Considerations
- **No sub-techniques** (Enterprise).

## 4. Procedure Examples
Representative ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S0455 - Metamorfo|Metamorfo]] hijacks clipboard data by monitoring clipboard contents and replacing cryptocurrency wallet values.
- [[30_CIPHER/05_Malware/S0283 - jRAT|jRAT]] captures clipboard data.
- [[30_CIPHER/05_Malware/S0250 - Koadic|Koadic]] retrieves current clipboard contents.
- [[30_CIPHER/05_Malware/S0148 - RTM|RTM]] collects clipboard data.
- [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]] is listed using infostealer tooling to copy clipboard data.
(ATT&CK includes many additional software examples.)

## 5. Detection Guidance
ATT&CK emphasizes detecting clipboard access with anomalous context:
- Clipboard access via OS utilities/APIs executed by **non-interactive** processes, unusual parents, or automation chains.
- Clipboard reads immediately followed by **staging/exfil commands** (archive/encode + network transfer).
- Abnormal clipboard polling frequency or access outside typical user session activity.

ATT&CK detection strategy highlights:
- DET0341 / AN0965–AN0967: anomalous clipboard access via platform-specific utilities and contexts.

### 5.1 Data Source Notes
- Ensure visibility into:
  - Process creation + command line (clipboard utilities and scripting)
  - Parent/child process relationships (e.g., service → clipboard read)
  - User session/interactive context (terminal session, GUI session)
  - Optional: API telemetry for clipboard read calls (EDR-dependent)

## 6. Response Guidance
1. **Confirm process context**: identify the binary/script reading clipboard and whether it ran interactively.
2. **Check for manipulation**: look for wallet/address substitution indicators and follow-on transaction artifacts.
3. **Contain**: isolate host; remove persistence; block IOCs for known stealers.
4. **User notification**: if clipboard manipulation is suspected, advise users to verify pasted sensitive values and rotate impacted secrets.

## 7. Related ATT&CK Content
- Primary:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1115 - Clipboard Data|T1115]]

## 8. SOC Relevance
High SOC relevance because:
- Frequently used by stealers and commodity malware.
- Detectable with strong signal when clipboard utilities appear in non-user contexts.
- Useful correlation pivot for financial fraud cases (clipboard replace → outbound C2 → transaction activity).

## 9. Threat Actor Usage
ATT&CK-listed examples include:
- [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]].

## 10. Campaign Usage
ATT&CK lists campaign usage on the technique page where applicable.

## 11. Malware Usage
ATT&CK-listed examples include:
- [[30_CIPHER/05_Malware/S0455 - Metamorfo|Metamorfo]], [[30_CIPHER/05_Malware/S0283 - jRAT|jRAT]], [[30_CIPHER/05_Malware/S0250 - Koadic|Koadic]], [[30_CIPHER/05_Malware/S0148 - RTM|RTM]].

## 12. Mitigations
ATT&CK notes this technique is **not easily mitigated** with preventive controls because it abuses system features. Focus on:
- Hardening execution paths (limit scripting/LOLBIN abuse where feasible)
- Monitoring and rapid response to anomalous clipboard access
- User protection against clipboard manipulation in high-risk workflows

## 13. Testing & Validation
- Controlled tests:
  - Execute benign clipboard reads from interactive shells vs. service contexts; verify alerts differentiate context.
  - Simulate clipboard polling at high frequency; confirm detection thresholds without excessive false positives.
- Validate correlations:
  - clipboard read → archive/encode → outbound connection within a time window.

## 14. References
- MITRE ATT&CK. (2025, October 24). *Clipboard Data (T1115)*. https://attack.mitre.org/techniques/T1115/
- Microsoft. (n.d.). *About the Clipboard.* https://msdn.microsoft.com/en-us/library/windows/desktop/ms649012(v=vs.85).aspx
- CISA. (2021, August 20). *Alert (AA21-200B) Chinese State-Sponsored Cyber Operations: Observed TTPs.* https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-200b

## 15. Notes
- Use session context (interactive vs. non-interactive) as a primary reducer of false positives.
- Clipboard replacement detections are especially valuable for fraud-centric intrusions.
