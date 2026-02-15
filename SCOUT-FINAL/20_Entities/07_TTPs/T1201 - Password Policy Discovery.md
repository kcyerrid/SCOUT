---
entity_type: mitre_technique

technique_id: "T1201"
subtechnique_id: ""
technique_name: "Password Policy Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - IaaS
  - Identity Provider
  - Linux
  - Network Devices
  - Office Suite
  - SaaS
  - Windows
  - macOS
datasources:
  - "DC0032 - Process Creation"
  - "DC0064 - Command Execution"
  - "DC0071 - Active Directory Object Access"
  - "DC0013 - User Account Metadata"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]]"
  - "[[30_CIPHER/03_Threat_Actors/G0010 - Turla|Turla]]"
  - "[[30_CIPHER/03_Threat_Actors/G0114 - Chimera|Chimera]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec]]"
  - "[[30_CIPHER/05_Malware/S0378 - PoshC2|PoshC2]]"
associated_campaigns:
  - "C0012 - Operation CuckooBees"
related_techniques:
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]"
  - "[[20_Entities/07_TTPs/TA0007 - Discovery/T1069 - Permission Groups Discovery|T1069]]"

detection_priority:
  - Medium

detection_maturity: "Established"
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
Password Policy Discovery (T1201) captures adversary attempts to learn enterprise/cloud password policy constraints (length, complexity, lockout thresholds, history, expiration). This commonly enables more efficient password guessing, spraying, and account takeover attempts while avoiding lockouts.

## 2. Technical Overview
Adversaries may query password policy through:
- **Windows/AD**: domain policy queries and local policy exports; AD policy cmdlets (where available).
- **Linux**: reading PAM and password-quality configuration and user policy details.
- **macOS**: querying account policy configuration via native utilities and MDM/DirectoryServices.
- **Cloud/IaaS**: API calls that return account password policy settings (e.g., cloud IAM password policy endpoints).
- **Identity Provider / SaaS / Office Suite**: administrative API/cmdlet reads of tenant authentication/password policy configuration.
- **Network devices**: CLI commands that display AAA/password policy configuration.

Defender-relevant characteristics:
- Often occurs early in intrusion, clustered with other discovery and/or credential-access behaviors.
- Cloud/IdP policy reads can be low-noise in isolation—context and identity risk posture matter.

## 3. Subtechnique Considerations
No sub-techniques for T1201.

## 4. Procedure Examples
Examples from ATT&CK procedure references include:
- [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]] using domain password policy queries as part of scripted discovery.
- [[30_CIPHER/03_Threat_Actors/G0010 - Turla|Turla]] using password policy queries (local/domain) during operations.
- [[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec]] discovering password policies on a target.
- [[30_CIPHER/05_Malware/S0378 - PoshC2|PoshC2]] enumerating domain password policy via a dedicated module.
- **C0012 - Operation CuckooBees** using password policy discovery as part of advanced reconnaissance.

## 5. Detection Guidance
Core detection approach: **identify policy query actions** and correlate them with **adjacent risky behaviors** (credential probing, suspicious admin actions, privilege changes).

Recommended analytics (cross-platform):
1. **Windows/AD policy query sequences**
   - Process creation and command/script telemetry indicative of domain/local password policy queries.
   - Correlate with directory reads and follow-on auth failures, password spraying indicators, or privilege escalation attempts.
2. **Linux configuration reads**
   - Audit reads of PAM/password-quality configuration and policy-related files, paired with command execution indicative of enumeration.
3. **macOS policy reads**
   - Track execution of policy query tools and MDM/DirectoryService policy reads, correlated with subsequent credential activity.
4. **Cloud/IaaS and IdP/SaaS policy reads**
   - Cloud audit logs / IdP audit logs: policy read operations by a principal that is unusual by role, device, geo, or client app.
   - Correlate with subsequent risky admin actions: new users, credential rotation, role changes, app consent, mailbox/tenant changes.
5. **Network device password policy read**
   - CLI “show password/aaa policy” style reads followed by AAA/user DB modifications.

### 5.1 Data Source Notes
Prioritize:
- **DC0032 Process Creation**: policy query utilities and management shells.
- **DC0064 Command Execution**: PowerShell ScriptBlock/module logging; shell command telemetry; network device command accounting.
- **DC0071 Active Directory Object Access**: directory reads tied to policy retrieval (where available).
- **DC0013 User Account Metadata**: cloud/IdP/SaaS audit events for policy reads and adjacent identity admin operations.

## 6. Response Guidance
1. Identify the requesting principal and access path (interactive shell, remote admin, automation, cloud app).
2. Validate legitimacy:
   - Is this principal expected to read policies? From expected device/geo? At expected cadence?
3. Correlate with follow-on behaviors:
   - Password spraying, abnormal auth failures, new sessions, risky admin changes, or reconnaissance bursts.
4. Contain if suspicious:
   - Revoke sessions/tokens, enforce MFA, reset credentials, and restrict admin API access where appropriate.
5. Expand hunt:
   - Search for the same principal reading policy across multiple tenants/services or multiple environments.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1069 - Permission Groups Discovery|T1069]]

## 8. SOC Relevance
- Moderate-to-high utility as an early warning for **credential attacks**, especially when paired with:
  - authentication failure spikes,
  - brute force / password spray telemetry,
  - privilege changes or suspicious app consent,
  - anomalous admin API usage.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0049 - OilRig|OilRig]]: scripted enumeration of domain password policy.
- [[30_CIPHER/03_Threat_Actors/G0010 - Turla|Turla]]: repeated use of policy queries to guide credential operations.
- [[30_CIPHER/03_Threat_Actors/G0114 - Chimera|Chimera]]: referenced use of utilities related to account/password discovery.

## 10. Campaign Usage
- **C0012 - Operation CuckooBees**: referenced password policy discovery during reconnaissance.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0488 - CrackMapExec|CrackMapExec]]: can enumerate/derive password policy for a target environment.
- [[30_CIPHER/05_Malware/S0378 - PoshC2|PoshC2]]: includes a module for enumerating domain password policy.

## 12. Mitigations
- **M1027 Password Policies** (ATT&CK mitigation):
  - Ensure only valid password filters are registered (Windows filter DLL registration and associated registry configuration).
- Additional hardening (defender-focused):
  - Enforce MFA, conditional access, and rate-limiting/lockout monitoring to reduce downstream impact of policy discovery.

## 13. Testing & Validation
- Validate that you can detect:
  - Windows policy query process and script telemetry,
  - Linux policy file reads + command execution correlation,
  - macOS policy query execution and MDM/DirectoryService read indicators,
  - Cloud/IdP policy read audit events and correlation to risky admin actions.
- Recommended test content:
  - Atomic Red Team T1201 test cases (where available), mapped to your EDR/SIEM schemas.

## 14. References
- MITRE ATT&CK. (n.d.). *Password Policy Discovery (T1201)*. https://attack.mitre.org/techniques/T1201/
- MITRE ATT&CK. (n.d.). *Password Policy Discovery – cross-platform behavior-chain analytics (DET0161)*. https://attack.mitre.org/detectionstrategies/DET0161/
- Microsoft. (n.d.). *Installing and Registering a Password Filter DLL*. https://learn.microsoft.com/windows/win32/secmgmt/installing-and-registering-a-password-filter-dll
- Atomic Red Team. (n.d.). *Atomic tests for T1201*. https://atomicredteam.io/atomic-red-team/atomics/T1201/

## 15. Notes
- Treat policy reads from **non-admin** principals, unusual locations/devices, or via unfamiliar client apps as higher risk—especially when followed by auth failures or identity control-plane changes.
