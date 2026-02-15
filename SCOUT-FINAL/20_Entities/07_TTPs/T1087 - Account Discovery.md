---
entity_type: mitre_technique

technique_id: "T1087"
subtechnique_id: ""
technique_name: "Account Discovery"

tactic:
  - "TA0007 - Discovery"
platforms:
  - ESXi
  - IaaS
  - Identity Provider
  - Linux
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
  - "[[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda]]"
  - "[[30_CIPHER/03_Threat_Actors/G1016 - FIN13]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1229 - Havoc]]"
associated_campaigns: []
related_techniques:
  - "T1078"

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
Account Discovery (T1087) describes attempts to enumerate valid usernames, accounts, or email addresses across hosts, directories, and cloud/SaaS identity systems. This commonly precedes credential access, lateral movement, persistence, and social engineering by identifying high-value or privileged principals.

## 2. Technical Overview
Adversaries enumerate accounts using:
- **Host-level enumeration**: built-in OS utilities, shell commands, directory/service lookups, or parsing local account databases.
- **Directory enumeration**: AD/LDAP queries, domain utilities, or PowerShell directory cmdlets.
- **Cloud/SaaS enumeration**: identity provider and cloud APIs/CLIs to list users/roles/groups, or tenant directory endpoints.
- **File-based harvesting**: extracting usernames/emails from local application data, mail clients, or configuration files.

Sought-after artifacts typically include usernames, email addresses, group/role membership, and privilege indicators (e.g., domain admins, tenant global admins, service accounts).

## 3. Subtechnique Considerations
Use the subtechniques when the target scope is explicit:
- **Local accounts**: [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.001 - Local Account|T1087.001]]
- **Domain accounts**: [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.002 - Domain Account|T1087.002]]
- **Email accounts / address lists**: [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.003 - Email Account|T1087.003]]
- **Cloud accounts**: [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.004 - Cloud Account|T1087.004]]

Detection requirements and telemetry differ substantially between endpoint, directory, and cloud identity surfaces—treat these as separate pipelines.

## 4. Procedure Examples
Representative observed behaviors include:
- Enumerating recently active users on Linux hosts (e.g., querying login history).
- Enumerating enterprise users and associated roles in business applications.
- Identifying privileged local users on endpoints.

## 5. Detection Guidance
Prioritize detection around **identity enumeration at scale**, **non-admin enumeration**, and **cross-host repetition**.

High-signal detection themes:
- **Burst enumeration**: repeated listing of users/groups/roles within short windows.
- **Unusual principal/device context**: enumeration from endpoints that do not typically administer identity.
- **Abnormal tools**: recon utilities or scripts not standard in the environment.
- **Privilege targeting**: explicit checks for admin/global admin roles, domain admin groups, or privileged group membership.

Suggested analytics (implementation-agnostic):
- Alert on endpoints executing account enumeration utilities with suspicious command-lines or parent processes (e.g., Office/PDF readers spawning shells).
- Correlate account discovery with follow-on authentication events (failed logons, new sessions, token theft signals) and lateral movement attempts.
- For cloud, alert on repeated directory list/read operations across users/groups/roles, especially by atypical apps, service principals, or newly-consented OAuth apps.

### Data Source Notes
Minimum telemetry to support reliable detections:
- **Endpoint**: process creation + full command line, PowerShell script block logging (where applicable), shell history telemetry (where available), security audit logs for local account queries.
- **Directory services**: AD/LDAP query telemetry, DC security logs, and directory service auditing where feasible.
- **Cloud/IdP**: identity audit logs (user/group enumeration), admin activity logs, API call logs, and sign-in logs with device/app context.

## 6. Response Guidance
1. **Scope the enumeration**: identify principal, source host/app, and enumeration volume (users/groups/roles queried).
2. **Determine legitimacy**: confirm if the actor is an admin tool, IT process, or approved script.
3. **Hunt follow-on activity**: look for credential access attempts, privilege escalation, new tokens/sessions, mailbox access, and lateral movement from the same principal/host.
4. **Contain if suspicious**: isolate host, revoke sessions/tokens, rotate credentials, and disable/limit the querying identity where appropriate.
5. **Hardening actions**: enforce least privilege for directory read/list permissions; tighten consent and app permissions for cloud directory access.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087 - Account Discovery|T1087]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.001 - Local Account|T1087.001]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.002 - Domain Account|T1087.002]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.003 - Email Account|T1087.003]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1087.004 - Cloud Account|T1087.004]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1078 - Valid Accounts|T1078]]

## 8. SOC Relevance
- **Stage**: Often early-to-mid intrusion (post-initial access) and during internal recon.
- **Value**: Strong precursor to credential attacks and privilege targeting.
- **Triage shortcut**: If enumeration occurs from a non-admin workstation or via unusual tooling, treat as suspicious by default.

## 9. Threat Actor Usage
Examples observed in ATT&CK procedure examples:
- [[30_CIPHER/03_Threat_Actors/G0143 - Aquatic Panda]] (Linux user identification activity)
- [[30_CIPHER/03_Threat_Actors/G1016 - FIN13]] (enumeration of users/roles in a treasury system)

## 10. Campaign Usage
No campaign mappings explicitly captured in the referenced ATT&CK procedure examples for this technique note.

## 11. Malware Usage
Examples observed in ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S1229 - Havoc]] (identification of privileged accounts)

## 12. Mitigations
- Emphasize **least privilege** over directory/account listing, especially for cloud roles and service principals.
- Restrict administrative tooling to hardened admin workstations; segment identity administration networks.
- Monitor and govern OAuth/app permissions that enable directory read/list access in cloud tenants.

## 13. Testing & Validation
- Validate endpoint analytics with benign administrative workflows (IT scripts, inventory tools) to set allowlists.
- Simulate enumeration from:
  - Non-admin workstation contexts
  - Unapproved binaries/scripts
  - Unusual parent-child process chains
- Ensure detections trigger on **volume**, **context**, and **tooling** rather than single command execution.

## 14. References
- MITRE ATT&CK. (n.d.). *Account Discovery (T1087)*. https://attack.mitre.org/techniques/T1087/
- Microsoft. (n.d.). *Azure CLI command group: az ad user*. https://learn.microsoft.com/en-us/cli/azure/ad/user
- Amazon Web Services. (n.d.). *IAM API Reference: ListUsers*. https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html

## 15. Notes
- Treat account enumeration from endpoints not used for identity administration as high-signal.
- Where possible, baseline legitimate enumeration (inventory/IT operations) to reduce false positives.
