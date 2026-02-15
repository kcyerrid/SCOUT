---
entity_type: mitre_technique

technique_id: "T1003"
subtechnique_id: ""
technique_name: "OS Credential Dumping"

tactic:
  - "TA0006 - Credential Access"
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
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0050 - APT32]]"
  - "[[30_CIPHER/03_Threat_Actors/G0087 - APT39]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0002 - Mimikatz]]"
  - "[[30_CIPHER/05_Malware/S0030 - Carbanak]]"
  - "[[30_CIPHER/05_Malware/S0232 - HOMEFRY]]"
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
OS Credential Dumping (T1003) covers adversary attempts to extract credential material from operating systems (hashes, plaintext passwords, cached credentials, secrets) by accessing memory, credential stores, registry hives, or OS structures. Retrieved credentials are typically used for lateral movement and privilege escalation.

## 2. Technical Overview
Credential dumping targets differ by OS and authentication stack:
- **Windows**: LSASS process memory, SAM/SECURITY hives, NTDS on domain controllers, LSA secrets, cached domain credentials, and related APIs/structures.
- **Linux**: memory scraping of credential-bearing processes and OS-specific sources (varies by subtechnique/implementation).
- **macOS**: credential material may be targeted via memory access or system credential stores (often coupled with elevated privileges).

Common characteristics relevant to detection:
- Requires **high privileges** (admin/SYSTEM/root) in many cases.
- Involves suspicious access to **sensitive processes**, **credential store files**, **registry keys**, or **memory**.
- Often chained with discovery, privilege escalation, persistence, and lateral movement.

## 3. Subtechnique Considerations
T1003 has multiple subtechniques; detections and response should be specific to the target:
- Process-memory focused (e.g., LSASS memory)
- Registry/hive focused (e.g., SAM/LSA Secrets)
- Directory replication focused (e.g., DCSync)
- OS file focused (e.g., `/etc/passwd` and `/etc/shadow`)

When possible, implement **subtechnique-specific** detection content rather than a single generic rule.

## 4. Procedure Examples
ATT&CK procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28]]: used publicly available and custom password retrieval tooling.
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32]]: used credential dumping tooling to harvest credentials.
- [[30_CIPHER/03_Threat_Actors/G0087 - APT39]]: used variants of credential dumping tools.
- [[30_CIPHER/05_Malware/S0002 - Mimikatz]]: commonly associated with Windows credential dumping.
- [[30_CIPHER/05_Malware/S0030 - Carbanak]] and [[30_CIPHER/05_Malware/S0232 - HOMEFRY]]: included credential dumping capability (per ATT&CK procedure examples/software entries).

## 5. Detection Guidance
Build layered detections across **process access**, **artifact creation**, and **follow-on behavior**.

Core analytics (high signal):
- **Sensitive process access**
  - Untrusted processes opening handles to credential-bearing processes (e.g., LSASS on Windows) with high-access rights.
  - Non-security tools attempting to read process memory or invoke dump-related APIs.
- **Credential store access**
  - Access to registry hives/keys associated with credentials (Windows) outside of normal management/security tooling.
  - Access to domain controller databases/backups where applicable (DC-specific controls).
- **Dump artifact creation**
  - Creation of dump files or credential output files in unusual directories; rapid access/exfil of those artifacts.
- **Tooling behaviors**
  - Known credential dumping tools are common, but **behavioral detections** (handle access + dump + file write) are more durable than pure signatures.
- **Correlation**
  - Credential dumping followed by new authentications to additional hosts/services within a short window.
  - Pair with privilege escalation indicators (token changes, service creation, scheduled tasks).

### Data Source Notes
Map to your sensors:
- **EDR**: process start + ancestry, process access events, memory read/dump behaviors, DLL/module loads, suspicious command-line patterns (avoid over-reliance), file creation for dumps.
- **Windows security telemetry**: object access auditing for sensitive keys/hives, protected process/LSASS protections status.
- **Linux audit**: access to `/proc` memory maps, debug tooling usage in privileged contexts.
- **Identity and network auth logs**: post-dump lateral movement and “new host” authentications.

## 6. Response Guidance
- **Immediate containment**: isolate affected hosts; block suspicious tooling; terminate malicious sessions where safe.
- **Credential actions**: reset impacted credentials; rotate privileged credentials; invalidate Kerberos tickets/session tokens as appropriate.
- **Scope**: identify which credential sources were accessed (memory vs. registry vs. directory replication); enumerate accounts potentially exposed.
- **Eradication**: remove persistence and initial access vectors; harden privileged access paths to reduce re-compromise.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1003 - OS Credential Dumping|T1003]]

## 8. SOC Relevance
- **One of the highest-impact** credential access techniques; frequently precedes ransomware deployment or large-scale lateral movement.
- **Escalation criteria**: any confirmed access to credential-bearing processes/hives by an unapproved process should be treated as urgent.

## 9. Threat Actor Usage
- Widely used across threat ecosystems; many groups use both commodity and custom tooling.
- Notable examples in ATT&CK procedure examples include [[30_CIPHER/03_Threat_Actors/G0007 - APT28]] and [[30_CIPHER/03_Threat_Actors/G0050 - APT32]].

## 10. Campaign Usage
- Not enumerated here; see MITRE technique page “Procedure Examples” for additional campaign mappings.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0002 - Mimikatz]]: widely used credential dumping tool.
- Other malware/tools may implement dumping modules or leverage built-in OS facilities.

## 12. Mitigations
(From ATT&CK mitigation guidance for T1003)
- **M1043 - Credential Access Protection**: enable OS protections (e.g., Windows Credential Guard where applicable).
- **M1040 - Behavior Prevention on Endpoint**: enable endpoint hardening rules that specifically protect credential-bearing processes.
- **M1015 - Active Directory Configuration**: restrict directory replication privileges and secure DC backups.
- **M1025 - Privileged Process Integrity**: protect sensitive OS processes (e.g., Protected Process Light for LSA where supported).
- **M1017 - User Training**: reduce credential reuse and overlap across systems.

## 13. Testing & Validation
- In a controlled lab, use approved internal security tooling to simulate:
  - Access to a credential-bearing process + dump artifact creation
  - Registry hive access patterns consistent with credential dumping
- Validate alerts based on behavior chains (process access → dump → file write → lateral auth) rather than static signatures.

## 14. References
- MITRE ATT&CK. (n.d.). *OS Credential Dumping (T1003).* https://attack.mitre.org/techniques/T1003/
- MITRE ATT&CK. (n.d.). *Mimikatz (S0002).* https://attack.mitre.org/software/S0002/
- Microsoft. (n.d.). *Attack Surface Reduction rules (LSASS protections and related guidance).* https://learn.microsoft.com/

## 15. Notes
- Treat “credential dumping confirmed” as an indicator that broader identity compromise may already be in progress; prioritize identity containment and lateral movement review.
