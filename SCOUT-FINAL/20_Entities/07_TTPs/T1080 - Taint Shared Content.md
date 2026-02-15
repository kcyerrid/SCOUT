---
entity_type: mitre_technique

technique_id: "T1080"
subtechnique_id: ""
technique_name: "Taint Shared Content"

tactic:
  - "TA0008 - Lateral Movement"
platforms:
  - Linux
  - Office Suite
  - SaaS
  - Windows
  - macOS
datasources:
  - "File Creation (DC0039)"
  - "File Modification (DC0061)"
  - "Network Share Access (DC0102)"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER]]"
  - "[[30_CIPHER/03_Threat_Actors/G1021 - Cinnamon Tempest|Cinnamon Tempest]]"
  - "[[30_CIPHER/03_Threat_Actors/G0012 - Darkhotel|Darkhotel]]"
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G1039 - RedCurl|RedCurl]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0575 - Conti|Conti]]"
  - "[[30_CIPHER/05_Malware/S0132 - H1N1|H1N1]]"
  - "[[30_CIPHER/05_Malware/S0260 - InvisiMole|InvisiMole]]"
  - "[[30_CIPHER/05_Malware/S0133 - Miner-C|Miner-C]]"
  - "[[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay]]"
  - "[[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]]"
  - "[[30_CIPHER/05_Malware/S0386 - Ursnif|Ursnif]]"
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
banner-height: 100
content-start: 101
---

# T1080 - Taint Shared Content

## 1. Summary
Adversaries may achieve lateral movement by **modifying content in shared locations** (e.g., SMB/NFS shares, shared folders, or cloud collaboration repositories) so that users or automated processes execute malicious content when they open or run otherwise “trusted” files. This frequently manifests as **trojanized binaries**, **malicious shortcuts**, or **document/script tampering** placed where users routinely browse.

## 2. Technical Overview
Taint Shared Content involves adversaries writing or altering files in shared storage so execution occurs on other systems via normal user or workflow behavior. Common patterns:
- **File share drop + user execution**: attacker places LNK/EXE/script in a shared folder; user executes it.
- **Directory share pivots**: attacker replaces/creates directory-like shortcuts that execute hidden payloads then open the legitimate directory.
- **Binary infection/trojanization**: attacker modifies legitimate executables stored on a share; remote systems run infected binary.
- **Office/collab repo abuse**: attacker injects macros/scripts or manipulates shared documents and templates in shared repositories.

Defender-relevant signals:
- **Write access abuse** to widely used shares (finance/HR/software distribution) followed by new executable content
- **Masquerading** (double extensions, lookalike names, hidden payloads) in shared folders
- File changes on shares from accounts that don’t typically modify executables or scripts
- Subsequent execution of binaries/scripts **directly from UNC paths**, mounted shares, or synced cloud folders

## 3. Subtechnique Considerations
This technique has **no sub-techniques**. Differentiate by:
- **Storage type**: SMB/NFS vs. cloud share vs. internal code repo
- **Payload form**: LNK/script/doc macro vs. trojanized binary
- **Trigger**: user-driven open/execute vs. automated job (login scripts, build pipelines, updater tasks)

## 4. Procedure Examples
Observed usage examples (non-exhaustive):
- [[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER]] placed malware on file shares and used legitimate-looking filenames.
- [[30_CIPHER/03_Threat_Actors/G1021 - Cinnamon Tempest|Cinnamon Tempest]] deployed ransomware from a batch file staged on a network share.
- [[30_CIPHER/03_Threat_Actors/G0012 - Darkhotel|Darkhotel]] propagated by infecting executables stored on shared drives.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]] injected malicious macros into Office documents on mapped network drives.
- [[30_CIPHER/03_Threat_Actors/G1039 - RedCurl|RedCurl]] placed modified LNK files on network drives for lateral movement.
- Malware families observed propagating via shared locations include: [[30_CIPHER/05_Malware/S0575 - Conti|Conti]], [[30_CIPHER/05_Malware/S0133 - Miner-C|Miner-C]], [[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]], and others listed below.

## 5. Detection Guidance
Core detection objective: identify **suspicious file writes/modifications to shared storage** that are plausibly intended for downstream execution, then correlate with **execution from those shared paths**.

High-value detection themes:
- **Executable content in shared paths**: new/modified `.lnk`, `.exe`, `.dll`, `.vbs`, `.bat`, `.scr`, `.ps1`, `.js`, `.hta` or platform-specific bundles (e.g., `.app`) in shared directories.
- **File deception**: double extensions (e.g., `report.docx.exe`, `docx.app`), hidden extensions, or directory-like naming.
- **Abnormal writers**: accounts/hosts writing to shares they don’t normally touch; workstation writing executables into departmental shares.
- **Share + execute chain**: file creation/modification on share followed shortly by process execution from UNC/mounted paths or cloud-synced folders on one or more endpoints.
- **Burst propagation**: same file hash/name appearing across many shares or many endpoints accessing the same new file.

Correlation ideas:
- `Network Share Access` (writes) **→** `File Creation/File Modification` **→** `Process Creation` from shared path (endpoint)
- Identify “patient zero” writer (the first host/account to drop the malicious file) and pivot across all subsequent access events.

### 5.1. Data Source Notes
Minimum telemetry for useful coverage:
- **File Creation (DC0039)**  
  - Endpoint file creation telemetry (e.g., Sysmon Event 11 where available) and/or platform-native file event streams (macOS file events, cloud drive audit logs)
- **File Modification (DC0061)**  
  - Audit logs for write/modify operations on shared content; Office/collaboration telemetry for document changes
- **Network Share Access (DC0102)**  
  - Windows Security 5145 (detailed share access), SMB/NFS server logs, and cloud share audit logs (uploads/downloads/access)

## 6. Response Guidance
1. **Quarantine the tainted content**: remove/disable access to the suspicious file(s) on shares (preserve originals for forensics).
2. **Identify the initial writer**: determine the first account/device that created or modified the tainted content; isolate if necessary.
3. **Hunt downstream execution**: find endpoints that accessed/executed the content; prioritize privileged users and high-value systems.
4. **Credential hygiene**: if share write privileges were abused, reset credentials/tokens for implicated accounts and review group memberships/ACLs.
5. **Hardening**: tighten share permissions (least privilege, separate write zones), enforce allowlisting/application control, and review DLP/Office macro policies.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1080 - Taint Shared Content|T1080]]

## 8. SOC Relevance
- **High signal when combined**: share write events plus subsequent execution is a strong detection chain.
- **Common in ransomware and worm-like propagation**: shared locations provide low-friction spread in flat networks.
- **Requires good governance**: SOC outcomes improve dramatically when shares are classified, owners are known, and write access is limited and auditable.

## 9. Threat Actor Usage
Known to be used by (examples from ATT&CK procedure observations):
- [[30_CIPHER/03_Threat_Actors/G0060 - BRONZE BUTLER|BRONZE BUTLER]]
- [[30_CIPHER/03_Threat_Actors/G1021 - Cinnamon Tempest|Cinnamon Tempest]]
- [[30_CIPHER/03_Threat_Actors/G0012 - Darkhotel|Darkhotel]]
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]
- [[30_CIPHER/03_Threat_Actors/G1039 - RedCurl|RedCurl]]

## 10. Campaign Usage
None explicitly listed in ATT&CK procedure examples for this technique.

## 11. Malware Usage
Observed in ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S0575 - Conti|Conti]]
- [[30_CIPHER/05_Malware/S0132 - H1N1|H1N1]]
- [[30_CIPHER/05_Malware/S0260 - InvisiMole|InvisiMole]]
- [[30_CIPHER/05_Malware/S0133 - Miner-C|Miner-C]]
- [[30_CIPHER/05_Malware/S0458 - Ramsay|Ramsay]]
- [[30_CIPHER/05_Malware/S0603 - Stuxnet|Stuxnet]]
- [[30_CIPHER/05_Malware/S0386 - Ursnif|Ursnif]]

## 12. Mitigations
- **M1049 – Antivirus/Antimalware**: detect/quarantine suspicious files written to shared locations.
- **M1038 – Execution Prevention**: apply application control/allowlisting to block unknown or untrusted binaries/scripts executed from shared paths.
- **M1050 – Exploit Protection**: reduce exploitation paths that may be paired with tainted content delivery.
- **M1022 – Restrict File and Directory Permissions**: minimize write access to shared folders; separate write-enabled staging areas from read-only distribution shares.

## 13. Testing & Validation
- Validate detections by emulating benign “share write + access” workflows in a lab:
  - Create non-malicious test files matching risky extensions and confirm alerts on unexpected write sources or write-to-sensitive-share events.
  - Confirm correlation between share write telemetry and subsequent endpoint access/execution (where permitted).
  - Validate cloud share audit coverage for uploads, modifications, and downstream downloads.

## 14. References
- MITRE. (n.d.). *Taint Shared Content (T1080).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1080/
- MITRE. (2025, October 21). *Detection of Tainted Content Written to Shared Storage (DET0471).* MITRE ATT&CK. https://attack.mitre.org/detectionstrategies/DET0471/
- Secureworks Counter Threat Unit Research Team. (2017, October 12). *BRONZE BUTLER Targets Japanese Enterprises.* Secureworks. https://www.sophos.com/en-us/research/bronze-butler-targets-japanese-businesses
- Boutin, J.-I. (2020, June 11). *Gamaredon group grows its game.* WeLiveSecurity (ESET). https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/

## 15. Notes
- Treat executable/script writes to business shares as “policy-grade” events; shared storage should rarely be a distribution point for ad-hoc executables.
- Consider dedicated “software distribution” shares with strong change control, signing requirements, and immutable logging.
