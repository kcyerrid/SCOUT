---
entity_type: mitre_technique

technique_id: "T1647"
subtechnique_id: ""
technique_name: "Plist Modification"

tactic:
  - Persistence
  - Privilege Escalation

platforms:
  - macOS

datasources:
  - File Monitoring
  - Process Creation
  - System Configuration Changes
  - EDR Telemetry
  - macOS Unified Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1547"
  - "T1059"
  - "T1106"

detection_priority:
  - High
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - persistence
  - privilege-escalation
  - macos
  - plist
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Plist Modification (T1647)

## 1. Summary
Plist Modification describes adversaries **modifying macOS property list (`.plist`) files to achieve persistence or elevate privileges**. Plist files are widely used by macOS to store configuration data for applications, services, and system components, making them a valuable target for stealthy manipulation.

Adversaries use this technique to:
- Establish persistence across reboots
- Execute malicious code automatically
- Modify application or system behavior
- Blend malicious changes into legitimate configuration files

---

## 2. Technical Overview
Property list files are structured configuration files used by macOS and applications. Adversaries abuse plist modification by:
- Adding or altering keys that specify executable paths
- Registering malicious binaries as launch agents or daemons
- Modifying login item configurations
- Altering application settings to enable execution

Common target locations include:
- `~/Library/LaunchAgents`
- `/Library/LaunchAgents`
- `/Library/LaunchDaemons`
- Application-specific plist files

Indicators include:
- Unexpected plist file modifications
- New or altered execution paths in plist keys
- Plist changes followed by execution at login or startup
- Plist edits performed by non-administrative processes

---

## 3. Subtechnique Considerations
Key considerations for T1647:
- macOS-specific technique
- Often paired with **Launch Agent or Daemon abuse**
- Changes may persist silently across reboots
- Legitimate software frequently modifies plist files

Plist modification blends **malicious persistence into normal system configuration activity**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Adding malicious programs to launch agent plists
- Modifying application plists to load malicious libraries
- Altering login item configurations via plist edits
- Replacing legitimate plist entries with attacker-controlled values

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **unexpected configuration changes and execution context**:
- Monitor plist file modifications in sensitive directories
- Detect new or altered execution entries in plist keys
- Correlate plist edits with process execution
- Track processes writing to plist locations

### Data Source Notes
- **File monitoring**: Detect plist creation and modification
- **EDR telemetry**: Observe execution triggered by plist entries
- **Unified logs**: Provide context for configuration changes

Common false positives:
- Legitimate software updates
- Application configuration changes

Tuning guidance:
- Baseline expected plist modifications
- Alert on new execution entries or unusual writers

---

## 6. Response Guidance
When suspected:
1. Identify modified plist files and keys
2. Compare against known-good baselines
3. Remove malicious entries and binaries
4. Review startup and login behaviors
5. Hunt for similar plist modifications across endpoints

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1547 - Boot or Logon Autostart Execution|T1547]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]

---

## 8. SOC Relevance
T1647 is critical because:
- Persistence is achieved through trusted configuration files
- Changes may survive reboots and updates
- Detection requires macOS-specific telemetry

SOC teams must maintain **visibility into macOS configuration changes**.

---

## 9. Threat Actor Usage
Commonly used by:
- macOS-focused threat actors
- Advanced persistent threats
- Stealth-oriented malware operators

---

## 10. Campaign Usage
Observed in:
- macOS persistence campaigns
- Long-dwell macOS intrusions
- Supply-chain or trojanized software attacks

---

## 11. Malware Usage
Associated with:
- macOS backdoors
- Persistent launch agent malware
- Privilege escalation toolkits

---

## 12. Mitigations
Recommended mitigations:
- Restrict write access to plist directories
- Monitor and audit plist modifications
- Use EDR with macOS configuration visibility
- Validate startup and login items regularly

---

## 13. Testing & Validation
Validation approaches:
- Modify benign plist files in lab environments
- Validate alerts on unauthorized plist edits
- Test SOC playbooks for macOS persistence
- Ensure tooling captures plist modification events

---

## 14. References
MITRE ATT&CK. (2025). *Plist Modification (T1647)*.  
https://attack.mitre.org/techniques/T1647/

Apple. (2024). *Launch agents and daemons documentation*.  
https://developer.apple.com/library/

Elastic Security Labs. (2024). *Detecting macOS persistence mechanisms*.  
https://www.elastic.co/security-labs

---

## 15. Notes
- Plists are trusted configuration artifacts.
- Persistence often hides in plain sight.
- Baselines are essential for detection.
