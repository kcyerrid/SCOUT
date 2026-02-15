---
entity_type: mitre_technique

technique_id: "T1564"
subtechnique_id: ""
technique_name: "Hide Artifacts"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Cloud
  - Containers
  - SaaS

datasources:
  - File Metadata
  - Process Creation
  - Command Execution
  - OS API Execution
  - Application Logs
  - Cloud Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1564.001"
  - "T1564.002"
  - "T1564.003"
  - "T1480"
  - "T1497"

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
  - hide-artifacts
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Hide Artifacts (T1564)

## 1. Summary
Hide Artifacts describes adversaries **concealing malicious artifacts or activity to evade user discovery and defensive controls**. This can include hiding files/directories, user accounts, windows/UI elements, and other evidence of execution or persistence. The technique spans multiple operating systems and operational contexts (endpoint, cloud, SaaS). :contentReference[oaicite:0]{index=0}

---

## 2. Technical Overview
Adversaries may hide artifacts by abusing legitimate OS and application features intended to reduce clutter or prevent accidental modification. Common approaches include:
- Marking files/directories as hidden or system-protected
- Creating hidden or non-enumerable user accounts
- Running processes or scripts with hidden windows/UI
- Placing artifacts in locations typically excluded from casual inspection
- Using isolated compute contexts (virtual instances/containers) to avoid standard instrumentation

Typical artifacts and signals:
- Discrepancies between “expected” and “actual” inventory (files, users, tasks)
- Processes that execute without visible UI despite interactive context
- Hidden/obfuscated filesystem objects and unexpected metadata flags
- Administration tooling used in atypical contexts (e.g., by non-admin services)

---

## 3. Subtechnique Considerations
T1564 includes multiple subtechniques. Commonly leveraged examples include: :contentReference[oaicite:1]{index=1}
- **T1564.001 – Hidden Files and Directories**
- **T1564.002 – Hidden Users**
- **T1564.003 – Hidden Window**
- Additional subtechniques cover filesystem attributes, exclusions, and other concealment mechanics.

Analyst note: “Hide Artifacts” is often an **enabler**—it may not be the primary objective but supports stealth for execution, persistence, credential access, or lateral movement.

---

## 4. Procedure Examples
Representative patterns include:
- Creating hidden directories to stage tooling and payloads
- Marking payloads as hidden/system to reduce discovery
- Running scripts with hidden windows (e.g., hidden PowerShell) to avoid user suspicion :contentReference[oaicite:2]{index=2}
- Creating or modifying user accounts that do not appear in standard user interfaces :contentReference[oaicite:3]{index=3}

*(Examples are intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **cross-source reconciliation** and **sequence-based hunting**:
- Inventory mismatches (filesystem/user inventory vs UI-reported lists)
- Hidden file attribute/flag changes followed by writes/execution
- Unusual use of scripting engines with hidden window flags or off-screen window positioning :contentReference[oaicite:4]{index=4}
- Creation of user accounts that do not appear in normal login/UI views :contentReference[oaicite:5]{index=5}

### Data Source Notes
- **File metadata telemetry**: Required to capture hidden/system flags and attribute changes :contentReference[oaicite:6]{index=6}
- **Process creation + command line**: Detect hidden-window execution flags and suspicious parent/child chains :contentReference[oaicite:7]{index=7}
- **Identity/user management logs**: Detect creation/modification of accounts and attributes that suppress UI listing :contentReference[oaicite:8]{index=8}
- **Cloud/SaaS logs**: Identify hidden rules/config or stealthy resource creation (where applicable)

Common false positives:
- Legit administrative hardening and housekeeping
- Enterprise management tooling that sets attributes/flags
- UI suppression for legitimate service accounts (org dependent)

---

## 6. Response Guidance
When suspected:
1. Identify what is being hidden (files/users/windows/rules) and where
2. Capture endpoint telemetry and obtain forensic artifacts (file metadata, user records, process ancestry)
3. Hunt for follow-on behaviors (execution from hidden locations, persistence, credential access)
4. Restore visibility (remove hidden attributes, re-enable UI listing) where operationally safe
5. Contain and remediate based on confirmed malicious scope

---

## 7. Related ATT&CK Content
- Subtechniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1564.001 - Hidden Files and Directories|T1564.001]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1564.002 - Hidden Users|T1564.002]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1564.003 - Hidden Window|T1564.003]]

- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1480 - Execution Guardrails|T1480]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1497 - Virtualization/Sandbox Evasion|T1497]]

---

## 8. SOC Relevance
T1564 is high value for SOC operations because it often explains:
- “Missing” artifacts during triage (files/users not visible through normal views)
- User reports of suspicious outcomes with no visible UI
- Gaps in conventional hunting that relies on GUI-visible inventory

It is especially relevant in incidents requiring **stealthy dwell time** or **low user disruption**.

---

## 9. Threat Actor Usage
Hide Artifacts is broadly used by:
- Advanced intrusion sets for stealth and long dwell time
- Ransomware affiliates staging tools and disabling user awareness
- Commodity malware attempting to avoid user discovery

Confidence should be driven by corroborating telemetry (what was hidden, how, and what happened next).

---

## 10. Campaign Usage
Commonly appears in:
- Post-exploitation staging and tool deployment
- Persistence establishment phases
- Credential theft operations where artifacts are concealed between actions

---

## 11. Malware Usage
Frequently associated with:
- Loaders and droppers that hide payloads and supporting files
- Backdoors that conceal configuration files, logs, and tasking
- Scripts that run with hidden windows to reduce user observation :contentReference[oaicite:9]{index=9}

---

## 12. Mitigations
Recommended mitigations include:
- Baseline file/user inventories and detect drift from expected state
- Enforce and monitor OS audit policy for file attribute and user changes
- Use EDR capabilities that enumerate hidden artifacts outside standard UI tooling
- Harden administrative controls and constrain scripting execution options used for hidden windows :contentReference[oaicite:10]{index=10}

---

## 13. Testing & Validation
Validation approaches:
- Verify telemetry coverage for hidden attributes/flags, user creation/modification, and hidden-window execution
- Perform controlled “visibility toggles” in a lab environment and ensure detections fire appropriately
- Create correlation rules that tie concealment actions to follow-on execution or persistence

---

## 14. References
MITRE ATT&CK. (2025). *Hide Artifacts (T1564)*. https://attack.mitre.org/techniques/T1564/ :contentReference[oaicite:11]{index=11}  
MITRE ATT&CK. (2025). *Hidden Files and Directories (T1564.001)*. https://attack.mitre.org/techniques/T1564/001/ :contentReference[oaicite:12]{index=12}  
MITRE ATT&CK. (2025). *Hidden Users (T1564.002)*. https://attack.mitre.org/techniques/T1564/002/ :contentReference[oaicite:13]{index=13}  
MITRE ATT&CK. (2025). *Hidden Window (T1564.003)*. https://attack.mitre.org/techniques/T1564/003/ :contentReference[oaicite:14]{index=14}  
MITRE D3FEND. (n.d.). *Hide Artifacts (T1564)*. https://d3fend.mitre.org/offensive-technique/attack/T1564/ :contentReference[oaicite:15]{index=15}  

---

## 15. Notes
- Prioritize detection content that reconciles UI-visible inventory with authoritative telemetry sources.
- Treat concealment actions as suspicious when paired with follow-on execution or persistence.
- Consider building SOC playbooks that explicitly address “artifact visibility restoration” as part of containment.
