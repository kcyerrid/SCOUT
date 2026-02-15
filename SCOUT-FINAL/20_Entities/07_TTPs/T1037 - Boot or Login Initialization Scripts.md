---
entity_type: ttp

ttp_id: "T1037"
ttp_name: "Boot or Logon Initialization Scripts"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"

description_short: "Adversaries use initialization scripts that run at system boot or user logon to establish persistence or execute malicious code."

related_subtechniques:
  - "T1037.001"
  - "T1037.002"
  - "T1037.003"
  - "T1037.004"

detection_difficulty: "Medium"
impact_severity: "High"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1037 – Boot or Logon Initialization Scripts

## 1. Technique Overview
**Boot or Logon Initialization Scripts (T1037)** is a MITRE ATT&CK v18 technique in which adversaries abuse **scripts that automatically execute during system startup or user logon**. These scripts are commonly used by operating systems and enterprise environments for configuration and management, making them attractive for persistence and potential privilege escalation.

Depending on context, these scripts may execute with elevated privileges or within trusted administrative workflows.

## 2. Adversary Objectives
Adversaries use initialization scripts to:
- Maintain persistence across reboots and logons
- Execute malicious payloads automatically
- Blend malicious logic into legitimate administrative scripts
- Regain execution after partial remediation

## 3. Sub-Technique Summary
- **T1037.001 – Logon Script (Windows)**  
- **T1037.002 – Login Hook (macOS)**  
- **T1037.003 – Network Logon Script**  
- **T1037.004 – RC Scripts (Linux / Unix)**  

## 4. Common Abuse Patterns
- Modifying Group Policy–managed logon scripts
- Adding malicious commands to shell initialization files
- Abusing enterprise login hooks or profile scripts
- Injecting malicious logic into system startup scripts
- Leveraging scripts executed with elevated or inherited privileges

## 5. Detection Considerations
Detection relies on **script integrity and execution monitoring**, including:
- Monitoring changes to logon and startup script files
- Alerting on unexpected script modifications
- Correlating logon events with script execution
- Detecting execution of suspicious commands within trusted scripts
- Reviewing Group Policy or directory-based script assignments

## 6. Defensive Mitigations
- Restrict write access to initialization script locations
- Monitor integrity of startup and logon scripts
- Audit Group Policy and directory-managed scripts regularly
- Use application control to limit script execution
- Review script content during incident response

## 7. Operational Impact
If successful, T1037 can:
- Provide reliable persistence
- Enable repeated execution of malicious code
- Facilitate privilege escalation depending on execution context
- Undermine trust in administrative automation

## 8. Analyst Notes
Initialization script abuse is especially dangerous in enterprise environments where scripts are centrally managed and implicitly trusted. During investigations, analysts should review **both system-level and user-level initialization scripts**, as attackers often target the least monitored layer.

## 9. References
- MITRE ATT&CK. (n.d.). *Boot or Logon Initialization Scripts (T1037)*. https://attack.mitre.org/techniques/T1037/
- Microsoft. (n.d.). *Logon Scripts via Group Policy*. https://learn.microsoft.com/windows-server/identity/ad-ds/manage/understand-logon-scripts
- Apple. (n.d.). *Login Hooks and Startup Items*. https://developer.apple.com/
- Red Hat. (n.d.). *System Startup Scripts (rc.local)*. https://access.redhat.com/
