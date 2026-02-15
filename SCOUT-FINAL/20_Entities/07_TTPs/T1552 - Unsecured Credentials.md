---
entity_type: mitre_technique

technique_id: "T1552"
subtechnique_id: ""
technique_name: "Unsecured Credentials"

tactic:
  - "TA0006 - Credential Access"
platforms:
  - Containers
  - IaaS
  - Identity Provider
  - Linux
  - Network Devices
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
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]"

associated_malware:
  - "[[30_CIPHER/05_Malware/S0373 - Astaroth|Astaroth]]"
  - "[[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]"
  - "[[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]"
  - "[[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]]"

associated_campaigns:
  - "C0049 - Leviathan Australian Intrusions"

related_techniques:
  - "T1552.001"
  - "T1552.002"
  - "T1552.003"
  - "T1552.004"
  - "T1552.005"
  - "T1552.006"
  - "T1552.007"
  - "T1552.008"

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
Adversaries may search compromised environments for credentials that are **stored insecurely** (e.g., plaintext configuration files, registry keys, shell history, hard-coded secrets, cloud metadata endpoints, container APIs). These artifacts can provide immediate access to systems, services, and cloud/SaaS resources.

## 2. Technical Overview
Unsecured credential exposure commonly occurs due to:
- Convenience storage (scripts, config, documentation, “temporary” notes)
- Legacy platform behaviors (auto-logon values, embedded service creds)
- Over-privileged secrets distribution (shared keys reused across hosts)
- Cloud/containers where credentials are written to local files, environment variables, or metadata surfaces

Defender-relevant behaviors:
- Broad **search/discovery activity** (enumerating files, registry, known secret locations)
- Reads of **high-risk artifacts** (credential stores, private key paths, cloud credential files)
- Rapid follow-on **authentication** or **privilege escalation** after discovery

## 3. Subtechnique Considerations
This technique includes multiple sub-techniques. Detection engineering is strongest when you:
- Maintain a **catalog of secret locations** used in your environment (apps, agents, admins).
- Implement targeted monitoring for each sub-technique’s high-signal artifacts.
- Correlate secret access events with **subsequent credential use** (new logons, token issuance, service access).

## 4. Procedure Examples
MITRE documents usage across software and groups, including:
- [[30_CIPHER/05_Malware/S0373 - Astaroth|Astaroth]] (credential recovery tooling)
- [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]] (credential theft using third-party utilities)
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]] (cloud-focused collection of sensitive data/credentials)
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]] (obtaining insecurely stored credentials on network appliances)
- Campaign reference: C0049 - Leviathan Australian Intrusions

## 5. Detection Guidance
Primary detection objective: **identify discovery/access of sensitive credential artifacts** and **confirm misuse**.

Core analytics:
- **Artifact access**: reads of known credential file paths, registry locations, key material, deployment secrets, or metadata endpoints.
- **Suspicious discovery tooling**: unusual process trees performing bulk search (grep/find/ripgrep/powershell search), registry enumeration, or config parsing.
- **Credential use correlation**: artifact access followed by authentication, session issuance, privilege changes, remote access, or cloud API calls.

### Data Source Notes
Telemetry to prioritize (vendor-neutral):
- EDR file access & process telemetry (file read/open, process ancestry, command line)
- Windows security auditing (object access where feasible), registry auditing
- Linux/macOS audit/file access telemetry (auditd/ESF/EDR equivalents)
- Cloud control plane logs (STS/role assumption, API calls, secret reads)
- Identity provider sign-in logs (new sessions, new devices, token issuance)
- Container runtime and orchestration logs (secrets mounts, API access)

## 6. Response Guidance
1. **Containment**
   - Disable/revoke affected credentials (passwords, keys, tokens); invalidate sessions.
2. **Eradication**
   - Remove plaintext secrets from endpoints/repos; rotate at source of truth.
   - Fix application/service configuration to use managed secret stores.
3. **Hunt & Scope**
   - Search for similar artifacts across fleet (secret scanning + endpoint hunts).
   - Identify downstream access using those secrets (cloud API, VPN, service logons).
4. **Hardening**
   - Implement secret governance: least privilege, rotation policy, vaulting, scanning in CI/CD.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552 - Unsecured Credentials|T1552]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.001 - Credentials In Files|T1552.001]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.002 - Credentials in Registry|T1552.002]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.003 - Shell History|T1552.003]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.004 - Private Keys|T1552.004]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.005 - Cloud Instance Metadata API|T1552.005]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.006 - Group Policy Preferences|T1552.006]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.007 - Container API|T1552.007]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552.008 - Chat Messages|T1552.008]]

## 8. SOC Relevance
High impact because it enables:
- Rapid account takeover and lateral movement
- Cloud tenancy compromise via leaked keys/tokens
- Persistence via reused service credentials

SOC triage quick wins:
- Alert on reads of high-risk secret paths + unusual process context
- Correlate with anomalous authentications shortly after discovery
- Prioritize incidents involving “shared” or “long-lived” secrets

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]

## 10. Campaign Usage
- C0049 - Leviathan Australian Intrusions

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0373 - Astaroth|Astaroth]]
- [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]
- [[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]
- [[30_CIPHER/05_Malware/S1091 - Pacu|Pacu]]

## 12. Mitigations
- **M1015 - Active Directory Configuration**: Remove vulnerable GPP/legacy secret exposures where applicable.
- **M1047 - Audit**: Proactively search for and remediate exposed credentials.
- **M1041 - Encrypt Sensitive Information**: Use hardware-backed storage or encrypted secret stores.
- **M1037 - Filter Network Traffic**: Limit metadata endpoints and sensitive services exposure.
- **M1035 - Limit Access to Resource Over Network**: Restrict network paths to secret surfaces/APIs.
- **M1028 - Operating System Configuration**: Reduce persistence of shell history where appropriate; harden logging.
- **M1027 - Password Policies**: Prohibit secret storage in files/registry; enforce strong passphrases for keys.
- **M1026 - Privileged Account Management**: Reduce privileges for accounts whose creds may be exposed.
- **M1022 - Restrict File and Directory Permissions**: Apply least privilege to shares/config directories.
- **M1051 - Update Software**: Patch known secret exposure vectors and legacy behaviors.
- **M1017 - User Training**: Train dev/admin teams on secure secret management.

## 13. Testing & Validation
- Perform controlled secret discovery simulations in a lab and verify:
  - File/registry access telemetry fidelity
  - Alerting on “high-risk artifact read” with nonstandard process lineage
  - Correlation to subsequent authentication activity
- Atomic Red Team technique page: https://www.atomicredteam.io/atomic-red-team/atomics/T1552

## 14. References
MITRE ATT&CK. (n.d.). *Unsecured Credentials (T1552).* MITRE. https://attack.mitre.org/techniques/T1552/

Wadhwa-Brown, T. (2018, December 6). *Where 2 worlds collide: Bringing Mimikatz et al to UNIX.* Portcullis Labs. https://labs.portcullis.co.uk/presentations/where-2-worlds-collide-bringing-mimikatz-et-al-to-unix/

CISA. (2024, February 7). *PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure.* https://www.cisa.gov/

Atomic Red Team. (n.d.). *T1552 - Unsecured Credentials.* https://www.atomicredteam.io/atomic-red-team/atomics/T1552

## 15. Notes
- Maintain a living “secret locations inventory” for your environment and bind detections to it.
- Track credential rotations as a response KPI (time-to-rotate after discovery).
