---
entity_type: ttp

ttp_id: "T1543"
ttp_name: "Create or Modify System Process"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"

description_short: "Adversaries create or modify system services, daemons, or agents to execute malicious code with elevated privileges."

related_subtechniques:
  - "T1543.001"
  - "T1543.002"
  - "T1543.003"
  - "T1543.004"

detection_difficulty: "Medium"
impact_severity: "High"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1543 – Create or Modify System Process

## 1. Technique Overview
**Create or Modify System Process (T1543)** is a MITRE ATT&CK v18 technique where adversaries establish persistence or escalate privileges by **creating new or modifying existing system-managed processes** such as services, daemons, or agents. These processes typically start automatically at boot and often run with elevated privileges, making them attractive for durable and stealthy persistence.

This technique spans multiple operating systems and leverages native service management frameworks.

## 2. Adversary Objectives
Adversaries use this technique to:
- Maintain long-term persistence across system reboots
- Execute malicious code with elevated privileges
- Blend malicious processes into legitimate system services
- Regain execution after partial remediation

## 3. Sub-Technique Summary
- **T1543.001 – Windows Service**
- **T1543.002 – Systemd Service**
- **T1543.003 – Launch Agent**
- **T1543.004 – Launch Daemon**

## 4. Common Abuse Patterns
- Creating new services or daemons that execute attacker-controlled binaries
- Modifying existing service configurations to point to malicious payloads
- Masquerading malicious services with legitimate-sounding names
- Configuring services to restart automatically on failure
- Leveraging elevated execution contexts provided by system process managers

## 5. Detection Considerations
Detection relies on **service and configuration monitoring**, including:
- Monitoring creation or modification of system services or daemons
- Alerting on changes to service executable paths or arguments
- Detecting unsigned or unexpected binaries referenced by services
- Correlating service changes with suspicious process execution
- Auditing startup-enabled system processes

## 6. Defensive Mitigations
- Restrict permissions required to create or modify system services
- Monitor and alert on service and daemon configuration changes
- Enforce code signing and application allowlisting
- Regularly audit system-managed processes
- Investigate unexpected or newly created services promptly

## 7. Operational Impact
If successful, T1543 can:
- Provide durable, high-privilege persistence
- Enable repeated execution without user interaction
- Undermine trust in system service infrastructure
- Complicate incident response due to automatic restarts

## 8. Analyst Notes
System process abuse is one of the most common and reliable persistence techniques across platforms. During incident response, analysts must enumerate **all startup-enabled services and daemons**, not just newly created ones, as attackers may modify existing services to reduce visibility.

## 9. References
- MITRE ATT&CK. (n.d.). *Create or Modify System Process (T1543)*. https://attack.mitre.org/techniques/T1543/
- Microsoft. (n.d.). *Windows Services*. https://learn.microsoft.com/windows/win32/services/services
- Red Hat. (n.d.). *systemd Service Management*. https://access.redhat.com/documentation/
- Apple. (n.d.). *Launch Agents and Daemons*. https://developer.apple.com/documentation/
