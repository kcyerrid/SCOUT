---
entity_type: ttp

ttp_id: "T1547"
ttp_name: "Boot or Logon Autostart Execution"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"

description_short: "Adversaries configure system mechanisms to automatically execute malicious code during boot or user logon."

related_subtechniques:
  - "T1547.001"
  - "T1547.002"
  - "T1547.003"
  - "T1547.004"
  - "T1547.005"
  - "T1547.006"
  - "T1547.007"
  - "T1547.008"
  - "T1547.009"
  - "T1547.010"
  - "T1547.012"
  - "T1547.013"
  - "T1547.014"

detection_difficulty: "Medium"
impact_severity: "High"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1547 – Boot or Logon Autostart Execution

## 1. Technique Overview
**Boot or Logon Autostart Execution (T1547)** is a core MITRE ATT&CK persistence technique in which adversaries configure operating system features to **automatically execute code** when a system boots or a user logs on. These mechanisms are commonly used by legitimate software, allowing malicious use to blend into normal system behavior.

Depending on configuration, this technique may also support **privilege escalation** if the autostart mechanism executes with elevated permissions.

## 2. Adversary Objectives
Adversaries use autostart execution to:
- Maintain persistence across reboots and logons
- Regain access after remediation attempts
- Execute payloads early in the system lifecycle
- Leverage trusted startup mechanisms to evade detection

## 3. Sub-Technique Summary (Linked)

- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.001 - Registry Run Keys or Startup Folder|T1547.001]] – Registry Run Keys / Startup Folder
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.002 - Authentication Package|T1547.002]] – Authentication Package
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.003 - Time Providers|T1547.003]] – Time Providers
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.004 - Winlogon Helper DLL|T1547.004]] – Winlogon Helper DLL
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.005 - Security Support Provider|T1547.005]] – Security Support Provider
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.006 - Kernel Modules and Extensions|T1547.006]] – Kernel Modules and Extensions
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.007 - Re-opened Applications|T1547.007]] – Re-opened Applications
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.008 - LSASS Driver|T1547.008]] – LSASS Driver
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.009 - Shortcut Modification|T1547.009]] – Shortcut Modification
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.010 - Port Monitors|T1547.010]] – Port Monitors
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.012 - Print Processors|T1547.012]] – Print Processors
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.013 - XDG Autostart Entries|T1547.013]] – XDG Autostart Entries
    
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1547.014 - Active Setup|T1547.014]] – Active Setup

## 4. Common Abuse Patterns
- Adding executables to startup folders or registry run keys
- Modifying authentication or security providers to load malicious DLLs
- Installing kernel modules or drivers to execute at boot
- Altering shortcuts or application settings to trigger execution
- Registering malicious components in print or logon subsystems

## 5. Detection Considerations
Detection typically requires **startup and configuration monitoring**, including:
- Changes to registry keys or startup directories
- Installation of new drivers, kernel modules, or extensions
- Modifications to authentication or logon-related components
- Creation or alteration of autostart configuration files
- Correlation of startup changes with suspicious process execution

## 6. Defensive Mitigations
- Monitor and alert on changes to autostart locations
- Restrict administrative privileges required to modify startup mechanisms
- Enforce application allowlisting and driver signing
- Audit startup configurations regularly
- Use endpoint detection tools that track persistence artifacts

## 7. Operational Impact
Successful abuse of T1547 can:
- Provide reliable, long-term persistence
- Enable repeated execution of malware
- Facilitate privilege escalation
- Complicate incident response and cleanup efforts

## 8. Analyst Notes
T1547 is one of the most widely abused persistence techniques due to the sheer number of legitimate autostart mechanisms across platforms. Effective defense depends on understanding **which startup entries are expected** in a given environment and detecting deviations rather than attempting to block all autostart behavior.

## 9. References
- MITRE ATT&CK. (n.d.). *Boot or Logon Autostart Execution (T1547)*. https://attack.mitre.org/techniques/T1547/
- Microsoft. (n.d.). *Windows Autostart Extensibility Points*. https://learn.microsoft.com/windows/win32/setupapi/autostart-extensibility-points
- Red Hat. (n.d.). *Linux Boot and Autostart Mechanisms*. https://access.redhat.com/
