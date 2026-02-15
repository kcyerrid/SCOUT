---
entity_type: mitre_technique

technique_id: "T1570"
subtechnique_id: ""
technique_name: "Lateral Tool Transfer"

tactic:
  - "TA0008 - Lateral Movement"
platforms:
  - ESXi
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
  - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]"
  - "[[30_CIPHER/03_Threat_Actors/G0051 - FIN10|FIN10]]"
  - "[[30_CIPHER/03_Threat_Actors/G0093 - GALLIUM|GALLIUM]]"
associated_malware: []
associated_campaigns:
  - "C0028 - 2015 Ukraine Electric Power Attack"
  - "C0025 - 2016 Ukraine Electric Power Attack"
related_techniques: []

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 3

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
Adversaries copy tools or files between compromised systems to stage capability, enable follow-on execution, or prepare data for collection/exfiltration. Transfers commonly leverage built-in protocols (SMB/admin shares, RDP) and native utilities (scp/rsync/curl/sftp/ftp), and may also use synced cloud folders for intra-org spread. :contentReference[oaicite:38]{index=38}

## 2. Technical Overview
- **What it is:** Movement of binaries/scripts/configs between internal hosts after initial ingress.
- **Where it shows up:**  
  - SMB/Windows admin shares, authenticated RDP sessions, scp/rsync/sftp/ftp, internal web services, or cloud-sync folders. :contentReference[oaicite:39]{index=39}
- **Defender value:** Transfers produce observable **write events + network flows**, and often precede immediate execution (high-confidence correlation opportunities).

## 3. Subtechnique Considerations
N/A (no sub-techniques).

## 4. Procedure Examples
- **C0028 - 2015 Ukraine Electric Power Attack:** [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]] moved tools laterally within corporate and between ICS/corporate networks. :contentReference[oaicite:40]{index=40}  
- **C0025 - 2016 Ukraine Electric Power Attack:** [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]] used file moves to network shares. :contentReference[oaicite:41]{index=41}  
- [[30_CIPHER/03_Threat_Actors/G0051 - FIN10|FIN10]] deployed additional tooling after moving laterally. :contentReference[oaicite:42]{index=42}  
- [[30_CIPHER/03_Threat_Actors/G0093 - GALLIUM|GALLIUM]] used PsExec as part of lateral activity and staging. :contentReference[oaicite:43]{index=43}  

## 5. Detection Guidance
**MITRE detection strategy-aligned analytics**
- Correlate suspicious **SMB/Admin$ writes** with near-time **process creation/execution** on the target (especially from user-writable or temp locations). :contentReference[oaicite:44]{index=44}
- Monitor **scp/rsync/curl/sftp/ftp** initiating transfers to internal systems plus file creation in unusual directories, then immediate execution. :contentReference[oaicite:45]{index=45}
- For ESXi: detect datastore uploads or internal scp/ssh transfers that result in new scripts or config modifications, correlated to admin activity baselines. :contentReference[oaicite:46]{index=46}

**High-signal patterns**
- **Write→Execute burst:** file written over SMB/RDP drive mapping, executed within minutes.
- **Unusual tooling:** `ftp`, `scp`, `rsync`, `curl` used by users/hosts that rarely perform admin transfers.
- **Unusual destinations:** tool drops into `C:\Users\Public\`, `%TEMP%`, `ProgramData`, `/tmp`, `/var/tmp`, user home directories.
- **Cross-segment transfers:** workstation-to-server or workstation-to-workstation transfers outside approved admin paths.

### Data Source Notes
*(Leave YAML `datasources` empty unless you have a canonical local mapping. Below are practical telemetry requirements.)*
- **File creation telemetry:** endpoint EDR, Sysmon (file create), auditd/FIM.
- **Process telemetry:** process creation (especially following file writes).
- **Network telemetry:** SMB/RDP/SSH flows, firewall logs, proxy logs for internal downloads.
- **Authentication telemetry:** lateral auth events (SMB/RDP/SSH logons) to separate admin vs anomalous.

## 6. Response Guidance
1. **Identify “seed” host(s):** determine where the tool originated and the first internal destination.
2. **Hunt the artifact:** hash + filename + path variants; check for renames/packing/masquerading.
3. **Contain staging channels:** temporarily restrict SMB/admin shares and lateral protocols between segments where feasible.
4. **Eradicate and harden:** remove staged tooling, rotate credentials used for lateral access, and enforce least privilege.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1570 - Lateral Tool Transfer|T1570]]

## 8. SOC Relevance
- **Priority:** Medium (often high context-dependent). Elevate to **High/Critical** when paired with remote execution, credential access, or ransomware precursors.
- **Best detection ROI:** correlation rules that join **remote file write** with **subsequent execution**.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]] :contentReference[oaicite:47]{index=47}  
- [[30_CIPHER/03_Threat_Actors/G0051 - FIN10|FIN10]] :contentReference[oaicite:48]{index=48}  
- [[30_CIPHER/03_Threat_Actors/G0093 - GALLIUM|GALLIUM]] :contentReference[oaicite:49]{index=49}  

## 10. Campaign Usage
- C0028 - 2015 Ukraine Electric Power Attack :contentReference[oaicite:50]{index=50}  
- C0025 - 2016 Ukraine Electric Power Attack :contentReference[oaicite:51]{index=51}  

## 11. Malware Usage
None explicitly captured in this note.

## 12. Mitigations
- **Filter Network Traffic (M1037):** restrict file-sharing communications (e.g., SMB) using host firewalls. :contentReference[oaicite:52]{index=52}  
- **Network Intrusion Prevention (M1031):** detect unusual data transfer over tools/protocols like FTP using signatures/behavioral inspection. :contentReference[oaicite:53]{index=53}  

## 13. Testing & Validation
- **Detection unit tests:** simulate benign admin file copies vs. suspicious workstation-driven transfers; validate alert thresholds.
- **Write→Execute correlation drill:** generate file write events to common staging dirs, followed by benign execution (e.g., signed test binary) to ensure correlation rules fire.
- **Segment control test:** confirm east-west controls block or log SMB/Admin$ transfers between restricted zones.

## 14. References
- MITRE ATT&CK. (2025, October 24). *Lateral Tool Transfer (T1570).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1570/ :contentReference[oaicite:54]{index=54}  
- Cisco Talos. (n.d.). *Avos ransomware group expands with new attack arsenal.* Cisco Talos Intelligence Group. https://blog.talosintelligence.com/avoslocker-new-arsenal/ :contentReference[oaicite:55]{index=55}  

## 15. Notes
- Consider a dedicated “SMB write + remote exec” correlation pack, as this technique often precedes execution and persistence staging.
