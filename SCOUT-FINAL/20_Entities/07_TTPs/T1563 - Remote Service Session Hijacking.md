---
entity_type: mitre_technique

technique_id: "T1563"
subtechnique_id: ""
technique_name: "Remote Service Session Hijacking"

tactic:
  - "TA0008 - Lateral Movement"
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

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "[[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563.001 - SSH Hijacking|T1563.001]]"
  - "[[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563.002 - RDP Hijacking|T1563.002]]"

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
Adversaries take control of **preexisting remote-service sessions** (e.g., SSH, RDP) to move laterally without establishing a new authenticated session. This differs from typical Remote Services use because the attacker **hijacks** an existing session rather than logging in with credentials. :contentReference[oaicite:56]{index=56}

## 2. Technical Overview
- **What it is:** Session takeover of an already-established remote access session.
- **Why it matters:** Can bypass common “new logon” detections—activity may appear under an existing session context.
- **Typical enabling conditions:**
  - Attacker has local access on a host where users maintain persistent sessions
  - Misconfigurations enabling session sharing/shadowing
  - Weak session isolation or credential/session token exposure

## 3. Subtechnique Considerations
This technique is best treated as an umbrella with distinct detection/telemetry requirements:
- **T1563.001 (SSH Hijacking):** focus on agent/socket access and unexpected lateral SSH actions without corresponding logins. :contentReference[oaicite:57]{index=57}  
- **T1563.002 (RDP Hijacking):** focus on session reassignment/`tscon.exe`-like behavior and RDS logs indicating shadowing/takeover. :contentReference[oaicite:58]{index=58}  

## 4. Procedure Examples
See sub-techniques:
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563.001 - SSH Hijacking|T1563.001]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563.002 - RDP Hijacking|T1563.002]]

## 5. Detection Guidance
**MITRE detection strategy themes**
- Detect anomalous remote-session activity where a session is hijacked rather than newly created:
  - mismatched credentials vs active session tokens
  - session takeovers without a corresponding successful logon event
  - RDP shadowing activity without consent :contentReference[oaicite:59]{index=59}
- Detect SSH/telnet session hijacking:
  - discrepancies between authentication logs and active session tables
  - commands issued without corresponding login events
  - abnormal network activity tied to dormant sessions :contentReference[oaicite:60]{index=60}

**Practical detection approaches**
- **RDP:** alert when session ID ownership changes or reconnection events occur without expected authentication chain; correlate with process starts in that session.
- **SSH:** correlate active session tables (`who`, `w`, `sshd` sessions) with auth logs; flag commands executed under sessions lacking recent authentication events.

### Data Source Notes
*(Leave YAML `datasources` empty unless you have a canonical local mapping. Below are practical telemetry requirements.)*
- **Windows RDS logs:** session connect/disconnect/reconnect, shadowing events; plus EDR process lineage in session context.
- **Linux/macOS SSH logs:** `sshd` auth logs, session open/close events, user/session tables, EDR/auditd for process execution tied to TTY/PTY.
- **EDR telemetry:** process executions within remote sessions, especially after “quiet” session transitions.

## 6. Response Guidance
1. **Preserve session evidence:** collect host logs and EDR timelines; identify which user sessions were active and when ownership changed.
2. **Invalidate access paths:** terminate active remote sessions, rotate credentials/keys, revoke tokens where applicable.
3. **Scope laterally:** determine whether hijacked sessions were used to pivot to additional hosts or access privileged consoles.
4. **Harden remote access:** enforce MFA where applicable, reduce persistent sessions, and apply least privilege to remote access groups.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563 - Remote Service Session Hijacking|T1563]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563.001 - SSH Hijacking|T1563.001]]
- [[20_Entities/07_TTPs/TA0008 - Lateral Movement/T1563.002 - RDP Hijacking|T1563.002]]

## 8. SOC Relevance
- **Priority:** High—can enable stealthy lateral movement under “legitimate” session context.
- **Alerting challenge:** many controls key off new logons; session hijacking requires **session-state** monitoring and endpoint correlation.

## 9. Threat Actor Usage
None explicitly captured at the parent technique level (see sub-techniques).

## 10. Campaign Usage
None explicitly captured in this note.

## 11. Malware Usage
None explicitly captured at the parent technique level (see sub-techniques).

## 12. Mitigations
- **Disable or Remove Feature or Program (M1042):** disable remote services (SSH/RDP/etc.) if unnecessary. :contentReference[oaicite:61]{index=61}  
- **Network Segmentation (M1030):** firewall rules to block unnecessary traffic between zones. :contentReference[oaicite:62]{index=62}  
- **Password Policies (M1027):** enforce secure password policies. :contentReference[oaicite:63]{index=63}  
- **Privileged Account Management (M1026):** avoid privileged accounts for routine remote access. :contentReference[oaicite:64]{index=64}  
- **User Account Management (M1018):** limit remote user permissions. :contentReference[oaicite:65]{index=65}  

## 13. Testing & Validation
- **RDP:** validate detections for session transitions (connect/disconnect/reconnect) without normal authentication chains.
- **SSH:** validate detections for commands under sessions lacking recent authentication events (use benign admin workflows).
- **EDR validation:** ensure session context (user, session ID/TTY) is captured and queryable.

## 14. References
- MITRE ATT&CK. (2025, October 24). *Remote Service Session Hijacking (T1563).* MITRE ATT&CK. https://attack.mitre.org/techniques/T1563/ :contentReference[oaicite:66]{index=66}  
- Hodgson, M. (2019, May 8). *Post-mortem and remediations for Apr 11 security incident.* Matrix.org. https://matrix.org/blog/2019/05/08/post-mortem-and-remediations-for-apr-11-security-incident/ :contentReference[oaicite:67]{index=67}  

## 15. Notes
- Consider separate detection content per remote-service type; signals differ substantially between SSH and RDP.
