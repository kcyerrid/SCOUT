---
entity_type: mitre_technique

technique_id: "T1562"
subtechnique_id: ""
technique_name: "Impair Defenses"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Cloud
  - Containers

datasources:
  - Security Software Logs
  - Process Creation
  - Service Configuration Logs
  - Registry Monitoring
  - Cloud Audit Logs
  - EDR Telemetry

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1564"
  - "T1070"
  - "T1027"
  - "T1055"

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
  - defense-evasion
  - security-controls
  - evasion
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Impair Defenses (T1562)

## 1. Summary
Impair Defenses describes adversaries **disabling, modifying, bypassing, or degrading security controls** to evade detection and response. This technique is foundational to successful intrusions, as it reduces the effectiveness of endpoint, network, identity, and cloud security mechanisms.

Attackers use this technique to:
- Disable antivirus, EDR, or logging
- Bypass security enforcement
- Reduce telemetry visibility
- Increase dwell time and operational freedom

T1562 is often observed early in post-compromise activity and persists throughout an intrusion lifecycle.

---

## 2. Technical Overview
Defensive controls exist across multiple layers, including endpoint protection, logging infrastructure, identity controls, and cloud security services. Adversaries impair defenses by:

- Disabling or uninstalling security software
- Modifying configuration settings
- Stopping or altering security services
- Tampering with logging or alerting pipelines
- Leveraging exclusions or trusted paths

Common environments impacted:
- Endpoints (AV/EDR tampering)
- Servers (logging suppression)
- Cloud platforms (audit log disablement)
- Containers (runtime security bypass)

Indicators include:
- Sudden loss of telemetry
- Security services stopping unexpectedly
- Configuration changes outside approved workflows
- Malware executing without alerts

---

## 3. Subtechnique Considerations
T1562 is a **parent technique** with multiple subtechniques covering:
- Disabling security tools
- Modifying configuration
- Impairing logging
- Bypassing protections

Subtechniques should be evaluated individually for detection and response maturity, as impact varies significantly by environment.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Stopping endpoint protection services
- Adding exclusions to security tools
- Disabling audit logging
- Tampering with update mechanisms
- Removing or bypassing security agents

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection requires **defense-aware monitoring**:
- Alert on security service state changes
- Monitor configuration modifications
- Detect telemetry gaps or sudden silence
- Correlate impairment actions with suspicious execution

### Data Source Notes
- **Security tool logs**: Primary detection source
- **EDR telemetry**: Identify tampering attempts
- **Audit logs**: Track configuration changes
- **Cloud logs**: Detect logging disablement

Common false positives:
- Legitimate administrative maintenance
- Security software updates
- Performance tuning activities

Tuning guidance:
- Require change justification for security modifications
- Baseline expected security service behavior

---

## 6. Response Guidance
When suspected:
1. Verify security tool health and configuration
2. Restore disabled services or controls
3. Identify how impairment occurred
4. Investigate preceding and subsequent attacker actions
5. Rotate credentials and re-establish trust

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1564 - Hide Artifacts|T1564]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1070 - Indicator Removal on Host|T1070]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1055 - Process Injection|T1055]]

---

## 8. SOC Relevance
T1562 is one of the **highest-priority techniques** for SOC monitoring. Successful defense impairment dramatically increases attacker success across all subsequent tactics.

Loss of telemetry should always be treated as a **potential incident**, not merely a tooling issue.

---

## 9. Threat Actor Usage
This technique is universally used by:
- Advanced persistent threats
- Ransomware operators
- Financially motivated crimeware groups

Its presence is a strong indicator of **intentional intrusion** rather than opportunistic malware.

---

## 10. Campaign Usage
Observed in:
- Ransomware deployment phases
- Espionage campaigns
- Cloud account takeover incidents
- Long-dwell intrusions

---

## 11. Malware Usage
Associated with:
- Ransomware families
- Loaders and droppers
- Post-exploitation frameworks
- Custom implants

---

## 12. Mitigations
Recommended mitigations:
- Enable tamper protection for security tools
- Restrict administrative access
- Monitor security configuration changes
- Enforce least privilege
- Use defense-in-depth across endpoint, network, and cloud

---

## 13. Testing & Validation
Validation approaches:
- Simulate benign security control disablement in labs
- Validate alerting on telemetry loss
- Test SOC workflows for impaired defenses
- Ensure incident response playbooks address control restoration

---

## 14. References
MITRE ATT&CK. (2025). *Impair Defenses (T1562)*.  
https://attack.mitre.org/techniques/T1562/

Microsoft. (2024). *Tamper protection for endpoint security*.  
https://learn.microsoft.com/microsoft-365/security/defender-endpoint/tamper-protection

Elastic Security Labs. (2023). *Detecting defense evasion techniques*.  
https://www.elastic.co/security-labs

---

## 15. Notes
- Defense impairment is often a precursor to major impact.
- Telemetry loss should always trigger investigation.
- Treat control degradation as a security incident, not a tooling issue.
