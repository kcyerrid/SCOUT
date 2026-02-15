---
entity_type: mitre_technique

technique_id: "T1134"
subtechnique_id: ""
technique_name: "Access Token Manipulation"

tactic:
  - Privilege Escalation
  - Defense Evasion

platforms:
  - Windows

datasources:
  - Process Creation
  - OS API Execution
  - Authentication Logs
  - Security Event Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1055"
  - "T1078"
  - "T1548"

detection_priority:
  - Medium
  - High
  - Critical

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - privilege-escalation
  - defense-evasion
  - windows
  - token
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Access Token Manipulation (T1134)

## 1. Summary
Access Token Manipulation describes adversary techniques that **modify, duplicate, impersonate, or replace Windows access tokens** to escalate privileges or evade security controls. Windows access tokens define the security context of processes and threads; by abusing token handling APIs, adversaries can assume the identity and privileges of other users without authenticating.

T1134 is commonly used to:
- Escalate from user to administrator or SYSTEM
- Impersonate other users or services
- Bypass access controls
- Enable stealthy lateral movement and persistence

---

## 2. Technical Overview
Windows uses access tokens to represent the identity and privileges of a process or thread. Adversaries abuse this model by:
- Duplicating tokens from privileged processes
- Impersonating tokens at the thread level
- Replacing primary process tokens
- Leveraging stolen tokens to spawn new processes

Common APIs involved include:
- `DuplicateTokenEx`
- `ImpersonateLoggedOnUser`
- `SetThreadToken`
- `CreateProcessAsUser`

Artifacts often include:
- Privileged child processes with anomalous parentage
- Token privilege changes without corresponding logon events
- SYSTEM-level execution initiated by non-SYSTEM parents

---

## 3. Subtechnique Considerations
T1134 includes multiple subtechniques (e.g., Token Impersonation/Theft, Token Duplication, Make and Impersonate Token). Considerations include:
- Requires sufficient access to manipulate tokens
- Often paired with process injection or handle theft
- Detection difficulty varies by subtechnique and telemetry quality

Token abuse is highly effective once attackers achieve local execution.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Stealing tokens from SYSTEM services to spawn elevated shells
- Impersonating service accounts to access protected resources
- Using token manipulation to bypass UAC and ACLs
- Combining token theft with process injection for stealth

These actions typically follow initial access or local privilege escalation.

---

## 5. Detection Guidance
Detection strategies should focus on:
- Monitoring token privilege changes and impersonation events
- Detecting process creation with mismatched user contexts
- Correlating token use with authentication logs
- Alerting on SYSTEM processes spawned by unexpected parents

### Data Source Notes
- **Security Event Logs**: Useful for tracking logon and privilege use
- **Process telemetry**: Critical for identifying anomalous execution chains
- **API monitoring**: Enables detection of token manipulation calls

---

## 6. Response Guidance
When suspected:
1. Identify affected processes and token contexts
2. Terminate malicious processes using stolen tokens
3. Investigate the source of token access
4. Review for lateral movement or persistence
5. Reset credentials associated with abused tokens

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1055 - Process Injection|T1055]]
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1078 - Valid Accounts|T1078]]
  - [[20_Entities/07_TTPs/TA0004 - Privilege Escalation/T1548 - Abuse Elevation Control Mechanism|T1548]]

---

## 8. SOC Relevance
T1134 is highly relevant in:
- Windows enterprise environments
- Post-exploitation and hands-on-keyboard attacks
- Ransomware and APT intrusions

Token abuse enables powerful escalation with limited forensic noise.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Ransomware operators
- Advanced persistent threats
- Post-exploitation frameworks (e.g., credential theft toolchains)

Usage reflects its reliability and stealth.

---

## 10. Campaign Usage
Observed in:
- Domain compromise campaigns
- Lateral movement operations
- Privilege escalation chains following phishing or exploit access

---

## 11. Malware Usage
Malware leveraging access token manipulation includes:
- Post-exploitation frameworks
- Credential dumping tools
- Custom implants targeting Windows services

---

## 12. Mitigations
Recommended mitigations:
- Enforce least privilege on services and users
- Monitor and restrict token manipulation APIs
- Use credential isolation features (e.g., LSASS protection)
- Apply OS and security patches
- Implement EDR with token-level visibility

---

## 13. Testing & Validation
Validation approaches:
- Simulate token theft in controlled environments
- Use Atomic Red Team tests for T1134
- Conduct red team exercises focused on Windows privilege escalation
- Validate SOC alerting on token anomalies

---

## 14. References
MITRE ATT&CK. (2024). *Access Token Manipulation (T1134)*.  
https://attack.mitre.org/techniques/T1134/

Microsoft. (2023). *Access tokens and security context*.  
https://learn.microsoft.com/windows/win32/secauthz/access-tokens

Red Canary. (2022). *Detecting token theft and impersonation*.  
https://redcanary.com/blog/access-token-theft/

---

## 15. Notes
- Token abuse often leaves minimal authentication artifacts
- Parent-child process analysis is critical for detection
- High-fidelity telemetry significantly improves visibility
