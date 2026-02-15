---
entity_type: ttp

ttp_id: "T1574"
ttp_name: "Hijack Execution Flow"
tactic: "Persistence, Privilege Escalation"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"

description_short: "Adversaries hijack execution flow by manipulating how programs load or execute code, causing malicious code to run instead of or in addition to legitimate code."

related_subtechniques:
  - "T1574.001"
  - "T1574.002"
  - "T1574.003"
  - "T1574.004"
  - "T1574.005"
  - "T1574.006"
  - "T1574.007"
  - "T1574.008"
  - "T1574.009"
  - "T1574.010"
  - "T1574.011"
  - "T1574.012"
  - "T1574.013"

detection_difficulty: "High"
impact_severity: "High"

created: "2025-12-19"
updated: "2025-12-19"

tlp_classification: "TLP:CLEAR"
---

# T1574 – Hijack Execution Flow

## 1. Technique Overview
**Hijack Execution Flow (T1574)** is a technique in **MITRE ATT&CK v18** in which adversaries manipulate how legitimate software loads code or executes dependencies so that **attacker-controlled code is executed**. This can occur through DLL search order manipulation, library path abuse, environment variable modification, or other mechanisms that influence program execution behavior.

Because these behaviors exploit normal OS and application functionality, they are difficult to detect and commonly used for persistence and privilege escalation.

## 2. Adversary Objectives
Adversaries use execution flow hijacking to:
- Achieve stealthy execution within trusted processes
- Maintain persistence without obvious autorun artifacts
- Escalate privileges by abusing high-privilege binaries
- Evade detection by blending into legitimate execution paths

## 3. Sub-Technique Summary
- **T1574.001 – DLL Search Order Hijacking**
- **T1574.002 – DLL Side-Loading**
- **T1574.003 – Dynamic Linker Hijacking**
- **T1574.004 – Dylib Hijacking**
- **T1574.005 – Executable Installer File Permissions Weakness**
- **T1574.006 – Path Interception by PATH Environment Variable**
- **T1574.007 – Path Interception by Search Order Hijacking**
- **T1574.008 – Path Interception by Unquoted Path**
- **T1574.009 – Path Interception by PATH Environment Variable (Linux/macOS)**
- **T1574.010 – Services File Permissions Weakness**
- **T1574.011 – Services Registry Permissions Weakness**
- **T1574.012 – COR_PROFILER**
- **T1574.013 – LD_PRELOAD**

## 4. Common Abuse Patterns
- Placing malicious libraries in directories searched before legitimate paths
- Exploiting unquoted service paths or writable directories
- Modifying environment variables to redirect execution
- Leveraging installer or service permission weaknesses
- Hijacking runtime loaders to inject malicious code

## 5. Detection Considerations
Detection requires **deep visibility into process creation and library loading**, including:
- Monitoring library load paths and order
- Detecting execution of binaries from writable directories
- Alerting on environment variable manipulation affecting execution
- Auditing service and installer permissions
- Correlating execution flow anomalies with privilege escalation

## 6. Defensive Mitigations
- Enforce least-privilege file and directory permissions
- Use application allowlisting and code signing
- Monitor DLL and library loading behavior
- Quote service paths and restrict writable directories
- Audit environment variable usage and execution contexts

## 7. Operational Impact
If successful, T1574 can:
- Provide stealthy persistence without explicit startup artifacts
- Enable execution within trusted or elevated processes
- Evade traditional detection mechanisms
- Complicate incident response due to indirect execution paths

## 8. Analyst Notes
Hijack Execution Flow is a **foundational persistence and escalation technique family**. Analysts should prioritize investigating **why a program resolved a dependency from an unexpected location**, as this is often the only visible indicator of compromise.

## 9. References
- MITRE ATT&CK. (n.d.). *Hijack Execution Flow (T1574).* https://attack.mitre.org/techniques/T1574/
- Microsoft. (n.d.). *Dynamic-Link Library Security*. https://learn.microsoft.com/windows/win32/dlls/dynamic-link-library-security
- Elastic Security. (n.d.). *DLL and Execution Flow Hijacking Detection*. https://www.elastic.co/security
- SANS Institute. (n.d.). *Execution Flow Hijacking Techniques*. https://www.sans.org/
