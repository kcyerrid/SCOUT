---
entity_type: mitre_technique

technique_id: "T1539"
subtechnique_id: ""
technique_name: "Steal Web Session Cookie"

tactic:
  - "TA0006 - Credential Access"
platforms:
  - Linux
  - Office Suite
  - SaaS
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]]"
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]]"
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]"
  - "[[30_CIPHER/03_Threat_Actors/G0030 - Lotus Blossom|Lotus Blossom]]"
  - "[[30_CIPHER/03_Threat_Actors/G1014 - LuminousMoth|LuminousMoth]]"
  - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]"
  - "[[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]"
  - "[[30_CIPHER/03_Threat_Actors/G1033 - Star Blizzard|Star Blizzard]]"
  - "[[30_CIPHER/03_Threat_Actors/G0120 - Evilnum|Evilnum]]"

associated_malware:
  - "[[30_CIPHER/05_Malware/S0657 - BLUELIGHT|BLUELIGHT]]"
  - "[[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]]"
  - "[[30_CIPHER/05_Malware/S0492 - CookieMiner|CookieMiner]]"
  - "[[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]"
  - "[[30_CIPHER/05_Malware/S0568 - EVILNUM|EVILNUM]]"
  - "[[30_CIPHER/05_Malware/S0531 - Grandoreiro|Grandoreiro]]"
  - "[[30_CIPHER/05_Malware/S1213 - Lumma Stealer|Lumma Stealer]]"
  - "[[30_CIPHER/05_Malware/S1146 - MgBot|MgBot]]"
  - "[[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]"
  - "[[30_CIPHER/05_Malware/S1148 - Raccoon Stealer|Raccoon Stealer]]"
  - "[[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]]"
  - "[[30_CIPHER/05_Malware/S1140 - Spica|Spica]]"
  - "[[30_CIPHER/05_Malware/S0467 - TajMahal|TajMahal]]"
  - "[[30_CIPHER/05_Malware/S1201 - TRANSLATEXT|TRANSLATEXT]]"
  - "[[30_CIPHER/05_Malware/S0658 - XCSSET|XCSSET]]"
  - "[[30_CIPHER/05_Malware/S1207 - XLoader|XLoader]]"

associated_campaigns:
  - "C0024 - SolarWinds Compromise"

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
Adversaries may steal browser or application session cookies (session tokens) and reuse (“replay”) them to access web applications and Internet services as an authenticated user—often bypassing password prompts and sometimes bypassing MFA enforcement tied to the interactive login.

## 2. Technical Overview
Session cookies are typically stored:
- **On disk** (e.g., browser profile databases/files)
- **In process memory** (browser/app process token/cookie stores)
- **In transit** (captured within network traffic if controls are weak or via on-path techniques)

Common defender-relevant collection patterns:
- Reading browser cookie stores (SQLite DBs, profile directories) from unusual processes or contexts
- Memory access against browser processes (dumping, handle access, read-process-memory patterns)
- Proxy/phishing frameworks that intercept tokens/cookies during authentication flows
- Subsequent **token replay** from new devices, unusual IPs, new user agents, or impossible travel

## 3. Subtechnique Considerations
N/A (no sub-techniques).

## 4. Procedure Examples
MITRE documents this technique in use by multiple actors and malware families, including:
- Threat actors: [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]], [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]], [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]], [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]
- Malware/Tools: [[30_CIPHER/05_Malware/S1148 - Raccoon Stealer|Raccoon Stealer]], [[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]], [[30_CIPHER/05_Malware/S0492 - CookieMiner|CookieMiner]], [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]

## 5. Detection Guidance
High-signal detection focuses on **(1) cookie access/collection** and **(2) cookie replay/abuse**.

Key analytic approaches:
- **Endpoint file access**: non-browser processes reading browser profile/cookie DB paths, especially shortly after initial access or user interaction.
- **Endpoint process/memory**: unusual handle access to browser processes, memory dump utilities, or suspicious parent-child chains interacting with browser processes.
- **Network/auth**: token reuse from unfamiliar device fingerprints, atypical geo/IP, impossible travel, or new user-agent strings without a corresponding interactive login.

Practical detection pivots:
- Access to Chrome/Edge/Firefox/Safari cookie stores by processes outside expected browser ecosystem
- Sudden new sessions without prior successful interactive authentication
- Correlate cookie-store reads → outbound connections to web apps / IdPs → privileged activity

### Data Source Notes
Telemetry to prioritize (vendor-neutral):
- EDR file access telemetry (open/read of browser cookie DB/profile directories)
- Process creation + command line + parent process lineage
- OS audit logs for sensitive file access (Linux/macOS file open; Windows file access auditing where feasible)
- Browser security logs (enterprise browser management / extension install events)
- Identity provider sign-in logs (device, IP, UA, risk signals, session issuance)
- Cloud/SaaS audit logs (new session creation, token refresh patterns, admin actions)

## 6. Response Guidance
1. **Containment**
   - Invalidate sessions/tokens for the impacted user(s) (global sign-out).
   - Revoke refresh tokens where applicable; rotate API tokens tied to the session context.
2. **Credential & Session Hygiene**
   - Force re-authentication; require step-up MFA and device compliance.
   - Rotate passwords if compromise path suggests broader credential exposure.
3. **Host Remediation**
   - Triage endpoint for info-stealer indicators and unauthorized browser access.
   - Remove malicious extensions and reset browser profiles if needed.
4. **Hunt & Scope**
   - Search for cookie-store reads across the fleet.
   - Identify other accounts with suspicious new sessions from the same IP/device.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1539 - Steal Web Session Cookie|T1539]]

## 8. SOC Relevance
Why SOC should care:
- Session cookie theft can **bypass MFA** and reduce reliance on password compromise indicators.
- Often paired with **info-stealers** and **browser data theft**, producing rapid account takeover.

Triage checklist:
- Was there a prior interactive login? If not, treat as high risk.
- New device / new IP / anomalous UA?
- Evidence of browser profile access or stealer activity on endpoint?

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1044 - APT42|APT42]]
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]]
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]
- [[30_CIPHER/03_Threat_Actors/G0030 - Lotus Blossom|Lotus Blossom]]
- [[30_CIPHER/03_Threat_Actors/G1014 - LuminousMoth|LuminousMoth]]
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]
- [[30_CIPHER/03_Threat_Actors/G1015 - Scattered Spider|Scattered Spider]]
- [[30_CIPHER/03_Threat_Actors/G1033 - Star Blizzard|Star Blizzard]]
- [[30_CIPHER/03_Threat_Actors/G0120 - Evilnum|Evilnum]]

## 10. Campaign Usage
- C0024 - SolarWinds Compromise

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0492 - CookieMiner|CookieMiner]]
- [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]
- [[30_CIPHER/05_Malware/S1148 - Raccoon Stealer|Raccoon Stealer]]
- [[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]
- [[30_CIPHER/05_Malware/S1213 - Lumma Stealer|Lumma Stealer]]

## 12. Mitigations
- **M1047 - Audit**: Improve auditing of auth/session events; detect anomalous session usage.
- **M1032 - Multi-factor Authentication**: Prefer phishing-resistant MFA (FIDO2/WebAuthn) and bind tokens to device/context when possible.
- **M1021 - Restrict Web-Based Content**: Reduce risky browser behaviors/extensions; restrict untrusted scripts.
- **M1054 - Software Configuration**: Shorten cookie lifetime; reduce persistence; enforce secure cookie attributes where applicable.
- **M1051 - Update Software**: Patch browsers and related software to reduce exploit and token theft vectors.
- **M1017 - User Training**: Target token theft and adversary-in-the-middle phishing education.

## 13. Testing & Validation
- Validate **file access** detections by monitoring controlled reads of cookie stores in a lab and confirming EDR visibility.
- Validate **IdP/SaaS** detections using test accounts to simulate “new device/new IP” session establishment and confirm alerting on anomalous sign-ins.
- Atomic tests (where applicable):
  - Atomic Red Team technique page: https://www.atomicredteam.io/atomic-red-team/atomics/T1539
  - GitHub reference: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.md

## 14. References
MITRE ATT&CK. (n.d.). *Steal Web Session Cookie (T1539).* MITRE. https://attack.mitre.org/techniques/T1539/

Rehberger, J. (2018, December 16). *Pass the Cookie and Pivot to the Clouds.* Embrace The Red. https://embracethered.com/blog/posts/passthecookie/

Chen, Y., Hu, W., Xu, Z., et al. (2019, January 31). *Mac Malware Steals Cryptocurrency Exchanges' Cookies.* Palo Alto Networks Unit 42. https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/

OWASP Foundation. (n.d.). *Session Management Cheat Sheet.* OWASP Cheat Sheet Series. https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

## 15. Notes
- Add environment-specific “known-good” browser cookie store access patterns (backup agents, EDR components, enterprise browser tools) to reduce false positives.
- Record your organization’s session invalidation and forced sign-out procedures per IdP/SaaS.
