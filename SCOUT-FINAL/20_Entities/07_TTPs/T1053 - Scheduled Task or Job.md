---
entity_type: mitre_technique

technique_id: "T1053"
subtechnique_id: ""
technique_name: "Scheduled Task/Job"

tactic: ["Execution", "Persistence", "Privilege Escalation"]
platforms: ["windows", "linux", "macos"]
datasources: ["Process Execution", "Task Scheduler Logs", "Cron Logs", "Authentication Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1053.005", "T1053.006", "T1547", "T1106"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-16"
updated: "2025-12-16"

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

# Scheduled Task/Job (T1053)

## 1. Summary
Scheduled Task/Job describes adversary abuse of operating system scheduling mechanisms to execute code at a specified time or on a recurring basis. This technique is commonly used to automate malicious execution, maintain persistence, or trigger payloads with elevated privileges.

Because task scheduling is a legitimate administrative function, malicious use can be difficult to distinguish from benign activity without proper baselining.

---

## 2. Technical Overview
Modern operating systems provide native scheduling frameworks:
- **Windows:** Task Scheduler
- **Linux/macOS:** `cron`, `at`, `launchd`

Adversaries create or modify scheduled jobs to execute scripts, binaries, or system commands. Tasks may run under specific user contexts or elevated privileges and may trigger on time-based or event-based conditions.

Artifacts include task definitions, scheduler logs, process execution records, and configuration file changes.

---

## 3. Subtechnique Considerations
T1053 includes several subtechniques that reflect OS-specific implementations:
- Windows Scheduled Task
- Cron jobs
- Platform-specific schedulers

Detection approaches must account for differences in storage location, logging, and execution behavior across platforms.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Creating hidden or obscurely named scheduled tasks
- Configuring tasks to run at system startup or user logon
- Using encoded or obfuscated command execution
- Modifying existing legitimate tasks to execute malicious payloads

Analysts may observe recurring execution patterns tied to scheduler activity.

---

## 5. Detection Guidance
Detection should focus on:
- Creation or modification of scheduled tasks outside approved workflows
- Tasks executing from unusual directories or user contexts
- Encoded or obfuscated command lines within task definitions
- Scheduled execution shortly after initial compromise

Correlation between task creation events and process execution improves fidelity.

### Data Source Notes
- **Task Scheduler Logs:** High value on Windows
- **Cron Logs:** Useful but often limited by default configuration
- **Process Execution:** Required to confirm payload execution

---

## 6. Response Guidance
When malicious scheduled tasks are identified:
- Disable and remove the task immediately
- Identify associated payloads and persistence mechanisms
- Review execution history for impact assessment
- Rotate credentials used to create or run the task

Preserve task definitions and scheduler logs for investigation.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1053.005 - Scheduled Task|T1053.005]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1053.006 - Cron|T1053.006]]  
  [[20_Entities/07_TTPs/TA0003 - Persistence/T1547 - Boot or Logon Autostart Execution|T1547]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]

---

## 8. SOC Relevance
Scheduled tasks are a high-signal persistence and execution mechanism frequently abused by ransomware operators and advanced threat actors. Detection maturity varies significantly depending on scheduler logging and baseline visibility.

---

## 9. Threat Actor Usage
This technique is used by:
- Ransomware groups establishing persistence
- Advanced persistent threat groups
- Initial access brokers maintaining footholds

Confidence in widespread usage is high.

---

## 10. Campaign Usage
Scheduled Task/Job abuse has appeared in:
- Ransomware intrusion chains
- Long-dwell enterprise compromises
- Automated lateral movement operations

---

## 11. Malware Usage
Malware and tooling leveraging scheduled tasks include:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]

---

## 12. Mitigations
Effective mitigations include:
- Restricting task creation privileges
- Monitoring and alerting on new or modified tasks
- Enforcing least-privilege execution contexts
- Reviewing scheduled tasks during incident response
- Hardening scheduler configurations

---

## 13. Testing & Validation
Validation approaches include:
- Atomic Red Team tests for scheduled task creation
- Purple team exercises simulating persistence via scheduler
- Review of alerting on task creation and execution

Successful validation results in detection of unauthorized scheduling activity.

---

## 14. References
MITRE ATT&CK. (2024). *Scheduled Task/Job (T1053)*.  
https://attack.mitre.org/techniques/T1053/

Microsoft. (2023). *Task Scheduler security considerations*.  
https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-security

Red Canary. (2023). *Detecting malicious scheduled tasks*.  
https://redcanary.com/blog/detecting-malicious-scheduled-tasks/

---

## 15. Notes
- Task names are often designed to appear legitimate
- Event-based triggers are increasingly abused
- Scheduler abuse often overlaps with persistence techniques
