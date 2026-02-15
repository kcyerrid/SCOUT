---
entity_type: mitre_technique

technique_id: "T1204"
subtechnique_id: ""
technique_name: "User Execution"

tactic: ["Execution"]
platforms: ["windows", "linux", "macos"]
datasources: ["Process Execution", "Command-Line Parameters", "File Creation", "Authentication Logs", "Application Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059", "T1106", "T1203", "T1566"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-17"
updated: "2025-12-17"

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

# User Execution (T1204)

## 1. Summary
User Execution describes adversaries relying on a user to execute malicious code. This may occur through opening a file, clicking a link, enabling macros, or otherwise interacting with attacker-supplied content. The technique exploits trust, curiosity, or deception rather than a technical vulnerability.

User Execution is a foundational execution mechanism and commonly overlaps with social engineering and phishing-based initial access.

---

## 2. Technical Overview
This technique does not mandate a specific execution mechanism; instead, it leverages legitimate user actions to initiate malicious code paths.

Common execution vectors include:
- Opening malicious attachments (documents, installers, scripts)
- Clicking links that trigger downloads or execution
- Enabling macros or active content
- Running trojanized applications or updates

Artifacts typically include process execution events tied to user actions, file creation in user directories, and application logs indicating document or installer execution.

---

## 3. Subtechnique Considerations
T1204 includes multiple subtechniques (e.g., malicious file, malicious link), but at the parent level focuses on the requirement for user interaction.

Key considerations include:
- Heavy reliance on social engineering
- High variability in execution artifacts
- Strong dependency on delivery technique and content type

Detection must correlate execution with user context and delivery vector.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Convincing users to open weaponized documents
- Disguising malware as software updates or invoices
- Prompting users to bypass security warnings
- Delivering installers that execute malicious payloads

Analysts may observe execution shortly after email or browser activity.

---

## 5. Detection Guidance
Detection should focus on:
- Execution of newly downloaded or email-delivered files
- User-launched processes from temporary or download directories
- Execution following user interaction events (email open, browser download)
- Command-line arguments indicating installer or script execution

Behavioral correlation across email, endpoint, and browser telemetry is critical.

### Data Source Notes
- **Process Execution:** Core signal for execution tracking
- **File Creation:** Useful for identifying newly introduced payloads
- **Application Logs:** Provide context around user actions

---

## 6. Response Guidance
When User Execution is suspected:
- Identify the delivery vector (email, web, removable media)
- Isolate the affected endpoint if execution is confirmed
- Capture the executed file and associated artifacts
- Assess for follow-on persistence or lateral movement

Preserve email headers, downloaded files, and endpoint telemetry for investigation.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1203 - Exploitation for Client Execution|T1203]]  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1566 - Phishing|T1566]]

---

## 8. SOC Relevance
User Execution remains one of the most common execution paths in real-world intrusions. SOC teams must integrate endpoint, email, and web telemetry to identify suspicious user-initiated execution events at scale.

---

## 9. Threat Actor Usage
This technique is used by:
- Commodity malware operators
- Ransomware affiliates
- Initial access brokers
- Advanced persistent threat groups

Confidence in ubiquitous usage is extremely high.

---

## 10. Campaign Usage
User Execution appears in:
- Phishing-based malware delivery campaigns
- Ransomware initial access operations
- Social engineering-driven intrusions

---

## 11. Malware Usage
Malware and tooling commonly relying on User Execution include:
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]

---

## 12. Mitigations
Effective mitigations include:
- User security awareness training
- Blocking execution from user-writable directories
- Enforcing macro and script restrictions
- Email and web gateway filtering
- Application control and allowlisting

---

## 13. Testing & Validation
Validation approaches include:
- Phishing simulation and user execution testing
- Purple team exercises correlating delivery to execution
- Review of alerts for user-initiated malicious execution

Successful validation results in detection of unauthorized user-driven execution.

---

## 14. References
MITRE ATT&CK. (2024). *User Execution (T1204)*.  
https://attack.mitre.org/techniques/T1204/

CISA. (2023). *Social engineering and user-driven attacks*.  
https://www.cisa.gov/social-engineering

Proofpoint. (2023). *User execution trends in phishing campaigns*.  
https://www.proofpoint.com/us/blog/threat-insight/user-execution-phishing

---

## 15. Notes
- User context is essential for accurate detection
- Execution often appears benign without delivery correlation
- This technique frequently precedes persistence and lateral movement
