---
entity_type: ttp

ttp_id: "T1546"
ttp_name: "Event Triggered Execution"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"

description_short: "Adversaries establish persistence or escalate privileges by configuring execution to occur in response to specific system or application events."

related_subtechniques:
  - "T1546.001"
  - "T1546.002"
  - "T1546.003"
  - "T1546.004"
  - "T1546.005"
  - "T1546.006"
  - "T1546.007"
  - "T1546.008"
  - "T1546.009"
  - "T1546.010"
  - "T1546.011"
  - "T1546.012"
  - "T1546.013"
  - "T1546.014"
  - "T1546.015"
  - "T1546.016"
  - "T1546.017"
  - "T1546.018"

detection_difficulty: "High"
impact_severity: "High"

created: "2025-12-19"
updated: "2025-12-19"

tlp_classification: "TLP:CLEAR"
---

# T1546 – Event Triggered Execution

## 1. Technique Overview
**Event Triggered Execution (T1546)** is a technique in **MITRE ATT&CK v18** where adversaries configure malicious code to execute **automatically in response to specific system, application, or runtime events**. Rather than relying on traditional autorun locations, attackers abuse legitimate event-handling mechanisms embedded within operating systems and runtimes.

This technique is widely used for stealthy persistence and privilege escalation because execution occurs only when predefined conditions are met.

## 2. Adversary Objectives
Adversaries use event-triggered execution to:
- Establish persistence without obvious startup artifacts
- Execute payloads conditionally to reduce noise
- Escalate privileges by abusing privileged event handlers
- Blend malicious execution into legitimate system behavior

## 3. Related Sub-Techniques
The following sub-techniques are associated with **Event Triggered Execution (T1546)** and are stored under `20_Entities/07_TTPs`:

- [[20_Entities/07_TTPs/T1546.001 - Change Default File Association|T1546.001]]
- [[20_Entities/07_TTPs/T1546.002 - Screensaver|T1546.002]]
- [[20_Entities/07_TTPs/T1546.003 - Windows Management Instrumentation Event Subscription|T1546.003]]
- [[20_Entities/07_TTPs/T1546.004 - Unix Shell Configuration Modification|T1546.004]]
- [[20_Entities/07_TTPs/T1546.005 - Trap|T1546.005]]
- [[20_Entities/07_TTPs/T1546.006 - LC_LOAD_DYLIB Addition|T1546.006]]
- [[20_Entities/07_TTPs/T1546.007 - Netsh Helper DLL|T1546.007]]
- [[20_Entities/07_TTPs/T1546.008 - Accessibility Features|T1546.008]]
- [[20_Entities/07_TTPs/T1546.009 - AppCert DLLs|T1546.009]]
- [[20_Entities/07_TTPs/T1546.010 - AppInit DLLs|T1546.010]]
- [[20_Entities/07_TTPs/T1546.011 - Application Shimming|T1546.011]]
- [[20_Entities/07_TTPs/T1546.012 - Image File Execution Options Injection|T1546.012]]
- [[20_Entities/07_TTPs/T1546.013 - PowerShell Profile|T1546.013]]
- [[20_Entities/07_TTPs/T1546.014 - Emond|T1546.014]]
- [[20_Entities/07_TTPs/T1546.015 - Component Object Model Hijacking|T1546.015]]
- [[20_Entities/07_TTPs/T1546.016 - Installer Packages|T1546.016]]
- [[20_Entities/07_TTPs/T1546.017 - Udev Rules|T1546.017]]
- [[20_Entities/07_TTPs/T1546.018 - Python Startup Hooks|T1546.018]]

## 4. Common Abuse Patterns
- Registering malicious components to execute on system or application events
- Leveraging scripting runtimes and configuration files for conditional execution
- Abusing legacy or obscure event handlers to evade detection
- Targeting high-privilege event triggers for escalation
- Combining multiple triggers for redundancy

## 5. Detection Considerations
Detection requires **behavioral and configuration-focused monitoring**, including:
- Auditing event-triggered execution mechanisms across platforms
- Monitoring changes to configuration files and registries tied to event handlers
- Correlating execution with triggering events (logon, file access, runtime start)
- Baseline comparison of known-good event subscriptions and handlers
- Leveraging EDR telemetry for low-frequency but high-impact execution

## 6. Defensive Mitigations
- Restrict permissions to configure event-driven execution mechanisms
- Monitor and alert on creation or modification of event handlers
- Remove or disable unused legacy execution features
- Apply least-privilege principles to event-handling components
- Include event-trigger review in persistence-hunting workflows

## 7. Operational Impact
If successful, T1546 can:
- Provide stealthy, condition-based persistence
- Enable execution without traditional autorun artifacts
- Evade detection by limiting execution frequency
- Complicate forensic timelines due to delayed triggers

## 8. Analyst Notes
Event Triggered Execution represents a **broad and flexible persistence class**. Analysts should prioritize understanding **what event caused execution**, as identifying the trigger often leads directly to the persistence mechanism itself.

## 9. References
- MITRE ATT&CK. (n.d.). *Event Triggered Execution (T1546).* https://attack.mitre.org/techniques/T1546/
- MITRE ATT&CK. (n.d.). *Persistence Tactic (TA0003).* https://attack.mitre.org/tactics/TA0003/
- SANS Institute. (n.d.). *Advanced Persistence Mechanisms*. https://www.sans.org/
