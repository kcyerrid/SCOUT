---
entity_type: mitre_technique

technique_id: "T1222"
subtechnique_id: ""
technique_name: "File and Directory Permissions Modification"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - ESXi

datasources:
  - File Metadata
  - Process Creation
  - Command Execution
  - OS API Execution
  - Audit Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1222.001"
  - "T1222.002"
  - "T1546.008"
  - "T1037"
  - "T1574"

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - defense-evasion
  - permissions
  - acl
  - dacl
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# File and Directory Permissions Modification (T1222)

## 1. Summary
File and Directory Permissions Modification describes adversaries **changing file or directory permissions/attributes to evade access controls** and enable actions such as reading protected data, modifying system files, replacing binaries, or preventing other users and processes from accessing resources. This is frequently a **supporting step** that enables persistence, privilege escalation, or defense evasion.

---

## 2. Technical Overview
Adversaries may modify permissions using platform-specific mechanisms, including:
- **Windows**: Discretionary Access Control Lists (DACLs), ownership changes, inheritance modifications
- **Linux/macOS**: `chmod`, `chown`, `setfacl` (ACL), extended attributes and flags
- **ESXi**: permission and ownership changes on datastore or configuration files (often via SSH access)

Common objectives:
- Grant attacker-controlled principals access to sensitive objects
- Take ownership to enable future changes
- Remove/deny access to defenders or legitimate services
- Enable tampering with startup, authentication, or security tooling files

Typical artifacts:
- ACL/DACL changes on sensitive files/directories
- Ownership changes on system or application files
- New or unusual permission values (e.g., world-writable, permissive ACLs)
- Follow-on file modifications shortly after permission changes

---

## 3. Subtechnique Considerations
T1222 has two canonical subtechniques:
- **T1222.001 – Windows File and Directory Permissions Modification**
- **T1222.002 – Linux and Mac File and Directory Permissions Modification**

Analyst focus should typically differentiate by:
- The permission model (DACL vs POSIX permissions vs ACL extensions)
- Which sensitive objects are targeted (system binaries, config, scripts, auth material)
- Whether permission changes are paired with ownership changes (a common escalation step)

---

## 4. Procedure Examples
Observed patterns include:
- Modifying permissions to enable replacement of binaries or scripts used in trusted execution paths
- Changing ownership of protected files/directories to support tampering
- Adjusting permissions on symbolic links to redirect access paths (common in some ransomware tradecraft)
- Making targeted directories writable to stage payloads or tooling

*(Examples should remain representative and avoid providing actionable malicious commands.)*

---

## 5. Detection Guidance
Detection should emphasize **behavioral sequences**, not just single events:
- Permission/ownership change event → followed by file write/replace → followed by execution or service start
- Permission changes on high-value paths (system dirs, service configs, auth stores, application binaries)
- Permission changes performed by unusual principals, at unusual times, or from unusual parent processes

### Data Source Notes
- **File metadata/audit events**: Needed for ACL/owner change visibility (Windows 4670/4663; Linux auditd; macOS unified logs where available)
- **Process creation + command-line**: Identify permission-modifying utilities or libraries (e.g., `icacls`, `takeown`, `chmod`, `chown`, `setfacl`)
- **EDR telemetry**: Correlate follow-on writes and executions

Common false positives:
- Legitimate admin activity (patching, deployment, configuration management)
- Backup/restore tools that adjust permissions
- Software installers/updaters

Tuning guidance:
- Baseline known-good admin tools/users and maintenance windows
- Alert on sensitive-path permission changes outside expected workflows
- Require correlation with follow-on execution or modification for high-confidence alerts

---

## 6. Response Guidance
Recommended SOC actions:
1. Identify the actor (user/service account) and originating host/process
2. Determine which objects were modified and whether ownership changed
3. Check for follow-on modifications (file writes, binary replacement, config changes)
4. Assess persistence implications (startup scripts, service configs, login hooks)
5. If confirmed malicious, revert permissions/ownership using known-good baselines and validate integrity of affected files

---

## 7. Related ATT&CK Content
- Subtechniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1222.001 - Windows File and Directory Permissions Modification|T1222.001]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1222.002 - Linux and Mac File and Directory Permissions Modification|T1222.002]]

- Related enabling techniques (common follow-on or dependency relationships):
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1546.008 - Accessibility Features|T1546.008]]
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1037 - Boot or Logon Initialization Scripts|T1037]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1574 - Hijack Execution Flow|T1574]]

---

## 8. SOC Relevance
T1222 is high-signal when it targets:
- System directories, auth material, service configs, security tooling paths
- Enterprise application binaries/configs (e.g., web servers, database services)
- Cluster/virtualization infrastructure (e.g., ESXi datastore/config paths)

It is particularly important because it often precedes:
- binary tampering, persistence installation, or defensive impairment.

---

## 9. Threat Actor Usage
Commonly observed among:
- Ransomware operators (to enable file access or tamper with links/paths)
- Post-exploitation frameworks used by advanced intrusion sets
- Attackers attempting to persist by modifying startup-related resources

Confidence should be tied to corroborating telemetry (who changed what, and what happened next).

---

## 10. Campaign Usage
Appears frequently in:
- Ransomware intrusion chains (prep steps before encryption or lateral movement)
- Persistence establishment phases
- Tool deployment phases where payload staging requires writable paths

---

## 11. Malware Usage
Associated with:
- Loaders and implants that need to replace or modify files in protected paths
- Ransomware families that adjust permissions to maximize file access
- Tooling that disables defenses by modifying permissions on security binaries/configs

---

## 12. Mitigations
Effective mitigations include:
- Enforce least privilege and restrict local admin rights
- Harden permissions on critical system files and application directories
- Monitor and restrict permission/ownership change utilities via application control
- Use file integrity monitoring for sensitive paths
- Prevent/limit SSH access to ESXi and enforce strong access control

---

## 13. Testing & Validation
Validation approaches:
- Confirm telemetry exists for ACL/ownership change events on key systems
- Run controlled administrative permission changes and ensure alerts/tickets generate appropriately
- Validate correlations (permission change → write → execute) are detectable in SIEM/EDR
- Use adversary emulation plans (e.g., Atomic testing where available) to test detection logic safely

---

## 14. References
MITRE ATT&CK. (2024). *File and Directory Permissions Modification (T1222)*.  
https://attack.mitre.org/techniques/T1222/ :contentReference[oaicite:0]{index=0}

MITRE ATT&CK. (2024). *Windows File and Directory Permissions Modification (T1222.001)*.  
https://attack.mitre.org/techniques/T1222/001/ :contentReference[oaicite:1]{index=1}

MITRE ATT&CK. (2024). *Linux and Mac File and Directory Permissions Modification (T1222.002)*.  
https://attack.mitre.org/techniques/T1222/002/ :contentReference[oaicite:2]{index=2}

MITRE D3FEND. (n.d.). *File and Directory Permissions Modification (ATT&CK T1222)*.  
https://d3fend.mitre.org/offensive-technique/attack/T1222/ :contentReference[oaicite:3]{index=3}

---

## 15. Notes
- Treat permission changes on sensitive objects as high-risk, especially when followed by file writes or execution.
- Ensure coverage across Linux/macOS/Windows, as permission models and logging differ materially.
- Consider baselining expected permission changes from patching and configuration management to reduce false positives.
