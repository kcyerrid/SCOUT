---
entity_type: mitre_technique

technique_id: "T1010"
subtechnique_id: ""
technique_name: "Application Window Discovery"

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
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G1001 - HEXANE]]"
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0094 - Trojan.Karagany]]"
  - "[[30_CIPHER/05_Malware/S0265 - Kazuar]]"
  - "[[30_CIPHER/05_Malware/S1044 - FunnyDream]]"
  - "[[30_CIPHER/05_Malware/S1111 - DarkGate]]"
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

## 1. Summary
Application Window Discovery (T1010) is the enumeration of open/active application windows to understand user activity, identify security tooling, and pinpoint targets for collection (e.g., specific apps, titles, or workflows). It is frequently paired with keylogging, screen capture, and collection staging decisions.

## 2. Technical Overview
Common implementation patterns include:
- **Windows**: querying window titles/handles via Win32 APIs (e.g., enumerating windows, foreground window title), often from native code or script-wrapped API calls.
- **Linux/X11**: enumerating active windows/desktops using window manager tooling or X11 query utilities.
- **macOS**: querying running apps/windows via AppleScript or native APIs that expose window/application metadata.

Defender-relevant intent signals:
- Discovery of **security tool UIs** (EDR consoles, password managers, VPN clients).
- Discovery of **target applications** (browsers, finance apps, RDP clients, admin consoles).
- Using window titles as context for **keylogging** or **screen capture** decisions.

## 3. Subtechnique Considerations
This technique has no sub-techniques.

## 4. Procedure Examples
Examples documented in ATT&CK include:
- Tooling that enumerates window titles to provide **context for keylogging** or to select targets for **screen capture**.
- Malware and actor tradecraft that collects window title information for operational awareness and targeting.

## 5. Detection Guidance
Because T1010 can be implemented via legitimate OS features, high-fidelity detection depends on **context + correlation**.

High-signal detection themes:
- **Unusual process context**: window enumeration originating from non-UI automation tools, document readers, browsers, or newly dropped binaries.
- **Suspicious API usage** (where EDR exposes telemetry): repeated enumeration calls in tight loops, especially paired with keylogging/screenshot modules.
- **Cross-telemetry correlation**:
  - window enumeration → keystroke capture indicators
  - window enumeration → screenshot events
  - window enumeration → rapid discovery + collection sequence

Practical analytics (platform-agnostic):
- Alert when a process performs window enumeration shortly after executing from user-writable locations or after suspicious persistence/initial access signals.
- Alert on window enumeration by unsigned/low-prevalence binaries, especially when combined with clipboard/keylogger/screenshot telemetry.
- On endpoints with API telemetry, detect patterns consistent with enumeration loops rather than a single query.

### Data Source Notes
Recommended telemetry to support strong detections:
- Endpoint process creation (full command line, parent chain, signer/reputation).
- EDR telemetry for UI/window enumeration APIs (if available) and associated modules (keylogging/screen capture).
- Host artifacts indicating screen capture and input capture behaviors for correlation.

## 6. Response Guidance
1. **Scope**: identify the initiating binary, parent chain, user session, and frequency of enumeration.
2. **Enrich**: determine whether the process also exhibits collection behavior (screenshots, keylogging, clipboard, browser data access).
3. **Hunt**: look for follow-on discovery/collection and credential access within the same time window.
4. **Contain**: isolate the endpoint if the process is unapproved or low-trust; revoke sessions/rotate credentials if paired with keylogging.
5. **Eradicate**: remove persistence and block the binary/hash; validate no secondary tooling remains.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1010 - Application Window Discovery|T1010]]

## 8. SOC Relevance
- Typically **medium-to-high** value as a behavioral precursor: often not the final objective, but strongly predictive when correlated with collection or credential access signals.
- Especially relevant for detections involving **keyloggers**, **infostealers**, and **operator-in-the-loop** activity.

## 9. Threat Actor Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon]]
- [[30_CIPHER/03_Threat_Actors/G1001 - HEXANE]]
- [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group]]

## 10. Campaign Usage
No campaign mappings explicitly captured in the referenced ATT&CK procedure examples for this technique note.

## 11. Malware Usage
Examples referenced in ATT&CK procedure examples include:
- [[30_CIPHER/05_Malware/S1111 - DarkGate]]
- [[30_CIPHER/05_Malware/S1044 - FunnyDream]]
- [[30_CIPHER/05_Malware/S0265 - Kazuar]]
- [[30_CIPHER/05_Malware/S0094 - Trojan.Karagany]]

## 12. Mitigations
- MITRE notes this behavior is difficult to prevent because it commonly abuses legitimate OS features.
- Focus on **execution prevention and control** (application allowlisting, signed code enforcement where feasible) and **rapid detection/containment** when paired with collection.

## 13. Testing & Validation
- Validate that your EDR captures:
  - process lineage + signer
  - (if supported) window enumeration API telemetry
  - correlated keylogging/screen capture signals
- Purple-team scenarios:
  - benign admin tooling baseline (to reduce false positives)
  - unknown binary performs repeated window enumeration + follow-on screenshot collection

## 14. References
- MITRE ATT&CK. (n.d.). *Application Window Discovery (T1010)*. https://attack.mitre.org/techniques/T1010/
- MITRE ATT&CK. (n.d.). *Detection of Application Window Enumeration via API or Scripting (DET0097)*. https://attack.mitre.org/detectionstrategies/DET0097/
- Cybersecurity and Infrastructure Security Agency. (n.d.). *Volt Typhoon* (referenced by ATT&CK for T1010 procedure examples). https://attack.mitre.org/techniques/T1010/

## 15. Notes
- Treat window enumeration as higher-risk when the same process also accesses browsers, credential stores, clipboard, or performs screen capture.
