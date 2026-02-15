---
entity_type: ttp

ttp_id: "T1556"
ttp_name: "Modify Authentication Process"
tactic: "Credential Access, Defense Evasion, Persistence"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Network"

description_short: "Adversaries modify authentication mechanisms to capture credentials, bypass authentication controls, or maintain persistent access."

related_subtechniques:
  - "T1556.001"
  - "T1556.002"
  - "T1556.003"
  - "T1556.004"
  - "T1556.005"
  - "T1556.006"
  - "T1556.007"
  - "T1556.008"

detection_difficulty: "High"
impact_severity: "High"

created: "2025-12-19"
updated: "2025-12-19"

tlp_classification: "TLP:CLEAR"
---

# T1556 – Modify Authentication Process

## 1. Technique Overview
**Modify Authentication Process (T1556)** is a technique in **MITRE ATT&CK v18** where adversaries alter legitimate authentication mechanisms to intercept credentials, bypass authentication safeguards, or establish durable persistence. Rather than stealing credentials directly, attackers compromise the components responsible for validating identity.

This technique represents a direct attack on **enterprise trust boundaries** and is typically associated with advanced, high-impact intrusions.

## 2. Adversary Objectives
Adversaries leverage authentication modification to:
- Capture credentials during legitimate authentication flows
- Bypass or weaken authentication enforcement (including MFA)
- Maintain access despite password resets or account changes
- Blend malicious logic into trusted identity infrastructure

## 3. Related Sub-Techniques
The following sub-techniques fall under **Modify Authentication Process (T1556)** and are stored under `20_Entities/07_TTPs`:

- [[20_Entities/07_TTPs/T1556.001 - Domain Controller Authentication|T1556.001]]
- [[20_Entities/07_TTPs/T1556.002 - Password Filter DLL|T1556.002]]
- [[20_Entities/07_TTPs/T1556.003 - Pluggable Authentication Modules|T1556.003]]
- [[20_Entities/07_TTPs/T1556.004 - Network Device Authentication|T1556.004]]
- [[20_Entities/07_TTPs/T1556.005 - Reversible Encryption|T1556.005]]
- [[20_Entities/07_TTPs/T1556.006 - Multi-Factor Authentication|T1556.006]]
- [[20_Entities/07_TTPs/T1556.007 - Hybrid Identity|T1556.007]]
- [[20_Entities/07_TTPs/T1556.008 - Network Provider DLL|T1556.008]]

## 4. Common Abuse Patterns
- Installing malicious authentication modules (DLLs, PAMs, providers)
- Modifying identity-related configuration files or registry keys
- Intercepting credentials during login, Kerberos, or MFA validation
- Persisting via authentication components that load on every logon
- Targeting domain controllers, identity servers, or network devices

## 5. Detection Considerations
Detection requires **identity-focused and integrity-based monitoring**, including:
- Monitoring changes to authentication binaries and modules
- Auditing installation of new authentication providers or filters
- Correlating authentication activity with unexpected credential exposure
- Inspecting domain controllers and identity systems for tampering
- Applying file and registry integrity monitoring to auth components

## 6. Defensive Mitigations
- Enforce strict change control on authentication infrastructure
- Require code signing for authentication modules and providers
- Monitor and alert on unauthorized auth configuration changes
- Limit administrative access to identity systems
- Regularly audit domain controllers, MFA systems, and network auth devices

## 7. Operational Impact
If successful, T1556 can:
- Enable long-term, covert credential harvesting
- Undermine enterprise-wide authentication trust
- Bypass MFA and password rotation defenses
- Force large-scale incident response and credential resets

## 8. Analyst Notes
Any modification to authentication mechanisms should be treated as **critical severity**. Unlike credential dumping, this technique often indicates an adversary intent on **persistent, strategic access**. Investigations should prioritize identity containment, credential hygiene, and validation of all authentication components.

## 9. References
- MITRE ATT&CK. (n.d.). *Modify Authentication Process (T1556).* https://attack.mitre.org/techniques/T1556/
- MITRE ATT&CK. (n.d.). *Credential Access Tactic (TA0006).* https://attack.mitre.org/tactics/TA0006/
- Microsoft. (n.d.). *Securing Authentication Infrastructure*. https://learn.microsoft.com/security/
- SANS Institute. (n.d.). *Credential Theft and Authentication Abuse*. https://www.sans.org/
