---
entity_type: ttp

ttp_id: "T1137"
ttp_name: "Office Application Startup"
tactic: "Persistence"
platforms:
  - "Windows"
  - "macOS"

description_short: "Adversaries establish persistence by configuring Microsoft Office applications to automatically load malicious components when the application starts."

related_subtechniques:
  - "T1137.001"
  - "T1137.002"
  - "T1137.003"
  - "T1137.004"
  - "T1137.005"
  - "T1137.006"

detection_difficulty: "Medium"
impact_severity: "Medium"

created: "2025-12-19"
updated: "2025-12-19"

tlp_classification: "TLP:CLEAR"
---

# T1137 – Office Application Startup

## 1. Technique Overview
**Office Application Startup (T1137)** is a **Persistence** technique in **MITRE ATT&CK v18** where adversaries abuse **Microsoft Office startup behaviors** to automatically load malicious templates, add-ins, or components when an Office application (e.g., Word, Excel) launches. This enables execution without requiring explicit user interaction beyond opening the application.

Office startup mechanisms are frequently trusted and commonly enabled in enterprise environments, making them attractive for stealthy persistence.

## 2. Adversary Objectives
Adversaries leverage Office startup persistence to:
- Achieve reliable execution when users open Office applications
- Maintain persistence without traditional autorun locations
- Blend malicious execution into routine user workflows
- Evade detection by leveraging trusted Office extensibility features

## 3. Related Sub-Techniques
The following sub-techniques fall under **Office Application Startup (T1137)** and are stored under `20_Entities/07_TTPs`:

- [[20_Entities/07_TTPs/T1137.001 - Office Template Macros|T1137.001]]
- [[20_Entities/07_TTPs/T1137.002 - Office Add-ins|T1137.002]]
- [[20_Entities/07_TTPs/T1137.003 - Outlook Forms|T1137.003]]
- [[20_Entities/07_TTPs/T1137.004 - Outlook Home Page|T1137.004]]
- [[20_Entities/07_TTPs/T1137.005 - Outlook Rules|T1137.005]]
- [[20_Entities/07_TTPs/T1137.006 - Add-ins|T1137.006]]

## 4. Common Abuse Patterns
- Placing malicious templates in Office startup directories
- Registering malicious COM or VSTO add-ins
- Abusing Outlook forms, rules, or homepage features
- Using macros that execute automatically on application startup
- Combining with social engineering to ensure frequent application launch

## 5. Detection Considerations
Detection relies on **Office configuration and behavior monitoring**, including:
- Auditing Office startup folders and template locations
- Monitoring installation or registration of Office add-ins
- Inspecting Outlook rules, forms, and homepage settings
- Correlating Office startup with unexpected script or process execution
- Baseline comparison of known-good Office configurations

## 6. Defensive Mitigations
- Restrict write access to Office startup and template directories
- Disable or limit macro execution where possible
- Monitor and control Office add-in installation
- Apply application allowlisting for Office-related components
- Educate users and administrators on Office persistence risks

## 7. Operational Impact
If successful, T1137 can:
- Provide reliable user-context persistence
- Enable execution without explicit user enablement of macros
- Blend malicious activity into normal business workflows
- Complicate detection due to trusted application context

## 8. Analyst Notes
Office Application Startup persistence often overlaps with **user-focused initial access and execution techniques**. Analysts should examine Office configuration changes alongside document delivery vectors, as persistence may be established immediately following initial compromise.

## 9. References
- MITRE ATT&CK. (n.d.). *Office Application Startup (T1137).* https://attack.mitre.org/techniques/T1137/
- Microsoft. (n.d.). *Security considerations for Office add-ins and templates*. https://learn.microsoft.com/office/
- SANS Institute. (n.d.). *Detecting Malicious Microsoft Offi*
