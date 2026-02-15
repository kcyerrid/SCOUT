---
entity_type: mitre_technique

technique_id: "T1185"
subtechnique_id: ""
technique_name: "Browser Session Hijacking"

tactic:
  - "TA0009 - Collection"
platforms:
  - Windows
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]]"
  - "[[30_CIPHER/05_Malware/S0522 - Cobalt Strike|Cobalt Strike]]"
  - "[[30_CIPHER/05_Malware/S0384 - Dridex|Dridex]]"
  - "[[30_CIPHER/05_Malware/S0660 - QakBot|QakBot]]"
  - "[[30_CIPHER/05_Malware/S0700 - TrickBot|TrickBot]]"
associated_campaigns: []
related_techniques: []

detection_priority:
  - Critical

detection_maturity: ""
threat_score: 5

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
**Browser Session Hijacking** abuses browser functionality and/or vulnerabilities to intercept or manipulate active authenticated sessions (cookies, HTTP sessions, client SSL certs) and user behavior. This can enable pivots into intranet resources and theft of sensitive web session data.

## 2. Technical Overview
Common patterns:
- **Web injects / form grabbing**: intercept credentials and form submissions inside the browser session.
- **Session token theft/reuse**: capture cookies/session artifacts to impersonate a user.
- **Browser pivoting/injection**: modify a running browser process to inherit its authenticated context; may require elevated rights and access to browser process memory/handles.
- **Malicious extensions/modules**: hook browser APIs to monitor content and credentials.

## 3. Subtechnique Considerations
- **No sub-techniques** (Enterprise).

## 4. Procedure Examples
Representative ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]] used form-grabbing to extract data from web forms.
- [[30_CIPHER/05_Malware/S0522 - Cobalt Strike|Cobalt Strike]] can inject into a user’s browser to inherit cookies, authenticated sessions, and client SSL certificates (browser pivoting).
- [[30_CIPHER/05_Malware/S0384 - Dridex|Dridex]] performs browser attacks via web injects to steal credentials/cookies/certificates.
- [[30_CIPHER/05_Malware/S0660 - QakBot|QakBot]] uses advanced web injects to steal banking credentials.
- [[30_CIPHER/05_Malware/S0700 - TrickBot|TrickBot]] uses web injects/browser redirection to trick users into providing credentials.
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]] is listed using form-grabbing for credential collection.

## 5. Detection Guidance
High-signal detection focuses on **privileged interaction with browser processes** and **injection-like behavior**:
- Browser process accessed with suspicious rights (write/inject) from non-browser processes.
- Remote thread creation / module loads / suspicious handle opens targeting common browsers.
- Privilege enablement patterns preceding injection (e.g., special privileges used to access other processes).
- Evidence of web inject frameworks: browser hooks, anomalous DLLs loaded into browser processes, abnormal browser child processes.
- Telemetry indicating “pivoting”: a controller process driving browser connections to internal resources atypical for that user.

ATT&CK detection strategy highlights: detect session hijacking via **privilege + handle access + remote thread into browsers** (DET0507 / AN1398 on the technique page).  

### 5.1 Data Source Notes
- Ensure visibility into:
  - Process injection telemetry (remote thread, module load, memory write)
  - Process handle access (target = browser, access masks)
  - Privilege use/enabled privileges
  - Browser extension inventory and extension install events (where available)
  - Network flows from browser processes to atypical internal targets

## 6. Response Guidance
1. **Isolate affected endpoint** and capture volatile evidence (browser process modules, suspicious injected artifacts).
2. **Invalidate sessions**: force sign-out, revoke tokens, rotate credentials for impacted applications.
3. **Eradicate injection vector**: remove malicious extensions, injected modules, or malware loaders; remediate persistence.
4. **Hunt laterally**: look for reuse of captured session artifacts from new IPs/devices and internal pivots.
5. **Strengthen controls**: enforce MFA, token binding/conditional access where possible, and browser hardening.

## 7. Related ATT&CK Content
- Primary:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1185 - Browser Session Hijacking|T1185]]

## 8. SOC Relevance
Critical SOC relevance because:
- Direct path to account takeover and internal pivots without immediate password theft.
- Detectable via EDR telemetry (injection + handle access) and identity telemetry (token reuse anomalies).
- High value for correlation: injection event → suspicious browser auth activity → internal access.

## 9. Threat Actor Usage
ATT&CK-listed examples include:
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]].

## 10. Campaign Usage
ATT&CK lists campaign usage on the technique page where applicable.

## 11. Malware Usage
ATT&CK-listed examples include:
- [[30_CIPHER/05_Malware/S0331 - Agent Tesla|Agent Tesla]], [[30_CIPHER/05_Malware/S0522 - Cobalt Strike|Cobalt Strike]], [[30_CIPHER/05_Malware/S0384 - Dridex|Dridex]], [[30_CIPHER/05_Malware/S0660 - QakBot|QakBot]], [[30_CIPHER/05_Malware/S0700 - TrickBot|TrickBot]].

## 12. Mitigations
ATT&CK lists mitigations including:
- **User Account Management (M1018)**: reduce high-integrity execution paths and privilege escalation/UAC bypass exposure required for some pivoting.
- **User Training (M1017)**: encourage closing sessions and reducing persistent authenticated browsing contexts.

## 13. Testing & Validation
- Validate EDR detections by controlled testing of:
  - suspicious handle access to browser processes
  - benign module loads vs. anomalous unsigned/unexpected modules into browser
- Validate identity controls by testing:
  - forced token revocation and session invalidation workflows
  - conditional access response to unusual device/IP for browser sessions

## 14. References
- MITRE ATT&CK. (2025, October 24). *Browser Session Hijacking (T1185)*. https://attack.mitre.org/techniques/T1185/
- Mudge, R. (n.d.). *Browser Pivoting.* https://www.cobaltstrike.com/help-browser-pivoting
- De Tore, M., & Warner, J. (2018, January 15). *Malicious Chrome Extensions…* https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses/

## 15. Notes
- Treat **browser process injection** and **privilege-enabled handle access** as top-tier signals.
- Prioritize correlations between endpoint injection and downstream identity/session anomalies.
