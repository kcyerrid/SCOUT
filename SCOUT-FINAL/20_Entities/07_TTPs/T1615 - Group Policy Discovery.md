---
entity_type: mitre_technique
technique_id: "T1615"
subtechnique_id: ""
technique_name: "Group Policy Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "Windows"
datasources:
  - "DC0071 - Active Directory Object Access"
  - "DC0032 - Process Creation"
  - "DC0064 - Command Execution"
  - "DC0085 - Network Traffic Content"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0010 - Turla|Turla]]"
  - "[[30_CIPHER/03_Threat_Actors/G0030 - Lotus Blossom|Lotus Blossom]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]]"
  - "[[30_CIPHER/05_Malware/S0082 - Emissary|Emissary]]"
  - "[[30_CIPHER/05_Malware/S1141 - LunarWeb|LunarWeb]]"
associated_campaigns: []
related_techniques:
  - "T1087"
  - "T1018"
detection_priority:
  - "High"
detection_maturity: ""
threat_score: 4
created: 2026-01-06
updated: 2026-01-06
contributors: []
tags:
  - "mitre"
  - "technique"
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Group Policy Discovery is collection of Group Policy Objects (GPOs) and related settings in Active Directory to understand enforced security controls, identify privileged local group assignments, discover domain management patterns, and map attack paths.

## 2. Technical Overview
Common adversary approaches:
- Execute built-in Windows tooling to report applied policies (e.g., `gpresult`) and interpret results for privilege paths, security settings, and software deployment.
- Use PowerShell-based domain enumeration to list GPOs and local group policy effects (e.g., functions that enumerate GPOs and GPO local group assignments).
- Query AD via LDAP for Group Policy containers and associated attributes, often from a workstation foothold against a domain controller.

Defender-relevant behavioral signals:
- GPO discovery from non-admin users or unusual endpoints
- PowerShell script block activity tied to domain enumeration functions
- LDAP queries filtering for Group Policy container objects at abnormal rates or from abnormal hosts
- `gpresult` usage in suspicious process lineages (office app → shell → gpresult)

## 3. Subtechnique Considerations
None (no sub-techniques).

## 4. Procedure Examples
- [[30_CIPHER/05_Malware/S0082 - Emissary|Emissary]] executes `gpresult` to enumerate Group Policy information.
- [[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]] identifies Group Policy information in victim environments.
- [[30_CIPHER/05_Malware/S1141 - LunarWeb|LunarWeb]] captures information on group policy settings.
- [[30_CIPHER/03_Threat_Actors/G0010 - Turla|Turla]] uses `gpresult` during host survey to discover Group Policy details.

## 5. Detection Guidance
Core strategy: detect **command/script-based GPO enumeration** and **LDAP-based GPO container queries**, then add context.

Recommended detection logic:
- Alert on `gpresult` executions from:
  - non-interactive/service contexts that do not normally run it
  - unusual parents (e.g., browsers/office apps) or living-off-the-land wrappers
- PowerShell detections:
  - script block logging for GPO enumeration functions and AD enumeration modules
  - suspicious PowerShell lineage and constrained language mode bypass attempts (if observed)
- LDAP monitoring:
  - unusual clients querying groupPolicyContainer objects
  - high-volume or repetitive GPO-related queries outside known admin tooling

### Data Source Notes
- **DC0071 – Active Directory Object Access**: directory service object access events (e.g., object reads) to support “who queried what” auditing.
- **DC0032 – Process Creation**: `gpresult` and PowerShell process lineage (Sysmon/4688).
- **DC0064 – Command Execution**: PowerShell operational logs (4103–4106) and command auditing.
- **DC0085 – Network Traffic Content**: LDAP query visibility (NSM/EDR network telemetry) with filters indicating GPO container targeting.

## 6. Response Guidance
1. Identify the enumerating principal and endpoint; determine whether the user is a domain admin or expected admin operator.
2. Review command lines and PowerShell script blocks; pivot on the same user/host for broader AD enumeration.
3. If LDAP-based enumeration is detected, validate the domain controller(s) contacted and consider restricting session tokens.
4. Hunt for follow-on actions: credential access, policy modification attempts, new scheduled tasks, remote service execution.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1615 - Group Policy Discovery|T1615]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1018 - Remote System Discovery|T1018]]

## 8. SOC Relevance
- **High**: strong indicator of AD attack-path mapping and privilege escalation planning.
- Most valuable when correlated with: other AD discovery, credential access attempts, or access to SYSVOL/GPT.INI/GPO files.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0010 - Turla|Turla]]: host survey includes `gpresult` for Group Policy details.
- [[30_CIPHER/03_Threat_Actors/G0030 - Lotus Blossom|Lotus Blossom]]: via [[30_CIPHER/05_Malware/S0082 - Emissary|Emissary]] capabilities.
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]: via [[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]] capabilities.

## 10. Campaign Usage
None noted.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S1159 - DUSTTRAP|DUSTTRAP]]: GPO information discovery in victim environments.
- [[30_CIPHER/05_Malware/S0082 - Emissary|Emissary]]: `gpresult` execution.
- [[30_CIPHER/05_Malware/S1141 - LunarWeb|LunarWeb]]: collection of Group Policy settings.

## 12. Mitigations
This technique largely abuses normal features; emphasize:
- Reduce who can query sensitive AD objects where feasible (least privilege + auditing).
- Limit PowerShell exposure (Constrained Language Mode where appropriate, script signing, logging).
- Segment/admin-tier endpoints to reduce where domain discovery can occur.

## 13. Testing & Validation
- Controlled test:
  - Run `gpresult` under a standard user and an admin account; validate process creation + PowerShell logs.
  - Execute benign LDAP queries for groupPolicyContainer objects from a test workstation; validate NSM visibility and DC auditing.
- Validate tuning:
  - Allowlist known admin hosts/tools that perform routine GPO auditing.
  - Confirm alerts fire for unusual parent processes and for non-admin endpoints querying GPO containers.

## 14. References
- MITRE ATT&CK. (n.d.). *Group Policy Discovery (T1615).* https://attack.mitre.org/techniques/T1615/
- MITRE ATT&CK. (2025). *Detection strategy for Group Policy Discovery on Windows (DET0055).* https://attack.mitre.org/detectionstrategies/DET0055/
- MITRE ATT&CK. (n.d.). *Emissary (S0082).* https://attack.mitre.org/software/S0082/
- MITRE ATT&CK. (n.d.). *DUSTTRAP (S1159).* https://attack.mitre.org/software/S1159/
- MITRE ATT&CK. (n.d.). *LunarWeb (S1141).* https://attack.mitre.org/software/S1141/

## 15. Notes
- Practical win: monitor **non-admin workstations** that suddenly generate GPO-related LDAP activity or run `gpresult` during an intrusion window.
