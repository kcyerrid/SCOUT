---
entity_type: mitre_technique

technique_id: "T1555"
subtechnique_id: ""
technique_name: "Credentials from Password Stores"

tactic:
  - TA0006 - Credential Access
platforms:
  - IaaS
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
  - "[[30_CIPHER/03_Threat_Actors/G0064 - APT33|APT33]]"
  - "[[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
  - "[[30_CIPHER/03_Threat_Actors/G0120 - Evilnum|Evilnum]]"
  - "[[30_CIPHER/03_Threat_Actors/G0037 - FIN6|FIN6]]"
  - "[[30_CIPHER/03_Threat_Actors/G0069 - MuddyWater|MuddyWater]]"
  - "[[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]]"
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]]"
  - "[[30_CIPHER/03_Threat_Actors/G0038 - Stealth Falcon|Stealth Falcon]]"
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0349 - LaZagne|LaZagne]]"
  - "[[30_CIPHER/05_Malware/S0378 - PoshC2|PoshC2]]"
  - "[[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]]"
  - "[[30_CIPHER/05_Malware/S1207 - XLoader|XLoader]]"
associated_campaigns:
  - "C0024 - SolarWinds Compromise"
related_techniques: []

detection_priority:
  - High

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
Adversaries may search for and extract credentials from common password storage locations on endpoints and cloud environments, including OS credential stores, application vaults, browser credential databases, and cloud secrets managers. Stolen credentials can accelerate lateral movement, privilege escalation, and long-term persistence.

## 2. Technical Overview
Credentials may be stored by operating systems, browsers, developer tooling, remote access utilities, email clients, password managers, and cloud secret vaults. Common adversary approaches include:
- **File-based harvesting:** Reading local databases or configuration files that store secrets (often encrypted).
- **API-assisted decryption:** Using OS-provided cryptographic APIs (e.g., DPAPI on Windows) via the victim context to decrypt stored secrets.
- **Process/memory access:** Pulling secrets from memory of credential-related processes or unlocked vault sessions.
- **Native tooling abuse:** Using legitimate binaries/utilities to enumerate or export stored secrets (high-signal, especially in non-admin user contexts).

## 3. Subtechnique Considerations
Use subtechniques to align detections and response playbooks to platform-specific storage mechanisms:
- macOS Keychain access patterns differ from Windows Credential Manager enumeration.
- Browser credential databases have distinct file paths and access behaviors per browser/OS.
- Cloud secrets stores pivot from endpoint telemetry to **cloud audit logs** and API monitoring.

## 4. Procedure Examples
Representative real-world patterns include:
- Execution of credential-stealing tooling to enumerate credentials from multiple applications and OS stores.
- Enumeration of stored credentials using native utilities (e.g., Windows vault/credential enumeration).
- Use of stolen credentials during campaigns (e.g., attempts to access additional secrets after compromise).

## 5. Detection Guidance
Prioritize detections that tie **unusual process execution** to **access of known password store artifacts** and/or **credential enumeration APIs**.

High-signal analytics patterns:
- Non-browser processes reading browser credential databases (e.g., Chrome/Edge/Firefox login stores).
- Unusual invocation of credential-store utilities (e.g., `vaultcmd.exe`, `rundll32.exe keymgr.dll ...`) outside of IT workflows.
- Access to password-store files shortly after initial compromise, privilege escalation, or new tool transfer.
- Suspicious process-to-process access and memory reads targeting security/credential services.

Suggested correlation:
- Process creation → file access to credential store paths → outbound network connection or archive creation.
- Parent/child lineage anomalies (Office → script host → credential access; browser → unknown binary reading login DB).

### Data Source Notes
Populate based on environment coverage (examples):
- Endpoint: process creation, command-line logging, file access telemetry, registry events, module loads, API telemetry (where available).
- Identity: authentication logs for subsequent suspicious logons.
- Cloud: secrets manager audit logs and unusual bulk secret retrieval.

## 6. Response Guidance
1. **Containment:** Isolate impacted host(s) if active credential theft is suspected; block known tooling hashes and suspicious binaries.
2. **Credential hygiene:** Reset potentially exposed credentials; prioritize privileged accounts and any credentials stored on affected endpoints.
3. **Scope:** Hunt across fleet for the same process lineage, file access indicators, and credential utility usage.
4. **Follow-on activity:** Look for lateral movement attempts, new service creation, remote execution, and abnormal sign-ins after credential access time window.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1555 - Credentials from Password Stores|T1555]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1555.001 - Keychain|T1555.001]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1555.002 - Securityd Memory|T1555.002]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1555.003 - Credentials from Web Browsers|T1555.003]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1555.004 - Windows Credential Manager|T1555.004]]

## 8. SOC Relevance
- **Severity:** High (credential exposure is often a direct precursor to domain/tenant compromise).
- **Triage focus:** Identify the store targeted, whether decryption occurred, and whether credentials were subsequently used.
- **Common false positives:** Enterprise password managers, sanctioned IT automation, browser enterprise sync tooling—mitigate with allowlists and admin device scoping.

## 9. Threat Actor Usage
Frequently observed among diverse actors due to high ROI:
- [[30_CIPHER/03_Threat_Actors/G0064 - APT33|APT33]]
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39|APT39]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]
- [[30_CIPHER/03_Threat_Actors/G0016 - APT29|APT29]]
- [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]]

## 10. Campaign Usage
- C0024 - SolarWinds Compromise (credential use and follow-on access attempts after compromise).

## 11. Malware Usage
Common tooling and malware families associated with password store access:
- [[30_CIPHER/05_Malware/S0002 - Mimikatz|Mimikatz]]
- [[30_CIPHER/05_Malware/S0349 - LaZagne|LaZagne]]
- [[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]]

## 12. Mitigations
- **Password Policies (M1027):** Enforce strong, unique passwords; reduce credential reuse impact.
- **Privileged Account Management (M1026):** Minimize accounts that can query/access stores; restrict access to only required secrets.
- **Update Software (M1051):** Reduce exploitation paths that enable credential store access.
- **Reduce credential storage where feasible:** Policy and user training to avoid storing high-value credentials in browsers or unmanaged stores (balanced against usability).

## 13. Testing & Validation
- Validate alerting for:
  - Unapproved processes reading known credential store locations.
  - Native credential enumeration utility usage outside normal IT baselines.
  - Correlated credential access followed by suspicious authentication attempts.
- Use controlled lab endpoints and sanctioned test accounts; ensure test artifacts are removed after validation.

## 14. References
- MITRE ATT&CK. (2025, October 24). *Credentials from Password Stores (T1555)*. https://attack.mitre.org/techniques/T1555/
- MITRE ATT&CK. (2025, October 21). *Detect Credentials Access from Password Stores (DET0430)*. https://attack.mitre.org/techniques/T1555/
- F-Secure Labs. (2015, September 17). *The Dukes: 7 years of Russian cyberespionage*. https://www.f-secure.com/
- Microsoft. (n.d.). *Data Protection API (CryptUnprotectData)*. https://learn.microsoft.com/

## 15. Notes
- Treat any confirmed access to password stores as **potential credential compromise** until proven otherwise.
- Align detection engineering to the specific subtechnique for best signal-to-noise.
