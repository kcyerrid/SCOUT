---
entity_type: mitre_technique

technique_id: "T1566"
subtechnique_id: ""
technique_name: "Phishing"

tactic: ["Initial Access"]
platforms: ["windows", "linux", "macos", "cloud", "saas"]
datasources: ["Email Gateway Logs", "Authentication Logs", "Web Proxy Logs", "Endpoint Detection Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1189", "T1204", "T1059"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-16"
updated: "2025-12-16"

contributors: []
tags: ["mitre", "technique"]

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Phishing (T1566)

## 1. Summary
Phishing describes adversary use of deceptive communications to trick users into revealing credentials, executing malicious content, or visiting attacker-controlled resources. This technique remains one of the most prevalent initial access vectors due to its low cost, scalability, and effectiveness against human targets.

Phishing enables follow-on techniques such as credential abuse, malware delivery, and account takeover, often bypassing technical controls through social engineering.

---

## 2. Technical Overview
Adversaries conduct phishing by delivering malicious or deceptive messages through email, messaging platforms, collaboration tools, or social media.

Common technical elements include:
- Spoofed sender domains or display names
- Embedded malicious links or attachments
- Credential harvesting via lookalike login pages
- HTML smuggling or archive-based payload delivery

Artifacts include email metadata, user click events, credential submissions, and subsequent authentication or endpoint activity.

---

## 3. Subtechnique Considerations
T1566 includes multiple subtechniques that differ by delivery method:
- Spearphishing Attachment
- Spearphishing Link
- Spearphishing via Service

Each subtechnique presents unique detection challenges and telemetry dependencies.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Sending invoices or delivery notifications with malicious attachments
- Impersonating trusted services to harvest credentials
- Delivering payloads via links to cloud-hosted content
- Leveraging compromised email accounts for internal phishing

Analysts may observe user interaction preceding credential use or malware execution.

---

## 5. Detection Guidance
Detection should focus on user interaction and message analysis:
- Suspicious sender domains or authentication failures (SPF/DKIM/DMARC)
- Malicious or newly registered URLs
- Attachments with unusual file types or behaviors
- Post-click authentication or endpoint activity

Correlation between email, identity, and endpoint telemetry is critical.

### Data Source Notes
- **Email Gateway Logs:** Primary source for detection and prevention
- **Authentication Logs:** Identify credential misuse following phishing
- **Endpoint Logs:** Confirm payload execution

---

## 6. Response Guidance
When phishing activity is suspected:
- Remove malicious messages from mailboxes
- Reset affected credentials and revoke sessions
- Isolate affected endpoints if payloads executed
- Conduct targeted user awareness and follow-up

Preserve email artifacts and user interaction logs for investigation.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1189 - Drive-by Compromise|T1189]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1204 - User Execution|T1204]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]

---

## 8. SOC Relevance
Phishing remains the most common entry point for enterprise compromise and ransomware campaigns. SOCs must balance detection sensitivity with alert fatigue, prioritizing high-confidence user interaction signals.

---

## 9. Threat Actor Usage
This technique is used by:
- Cybercriminal groups conducting credential theft
- Ransomware operators and affiliates
- Advanced persistent threat groups targeting specific users

Confidence in widespread usage is extremely high.

---

## 10. Campaign Usage
Phishing appears in:
- Mass credential harvesting campaigns
- Targeted spearphishing operations
- Initial access broker activity

---

## 11. Malware Usage
Malware commonly delivered via phishing includes:
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]

---

## 12. Mitigations
Effective mitigations include:
- Email filtering and sandboxing
- Enforcing MFA to reduce credential theft impact
- User awareness and phishing training
- Blocking newly registered or low-reputation domains
- Attachment type restrictions

---

## 13. Testing & Validation
Validation approaches include:
- Phishing simulations and user testing
- Purple team exercises measuring detection and response
- Review of post-click detection logic

Successful validation results in rapid identification and containment.

---

## 14. References
MITRE ATT&CK. (2024). *Phishing (T1566)*.  
https://attack.mitre.org/techniques/T1566/

Proofpoint. (2023). *State of the Phish*.  
https://www.proofpoint.com/us/resources/threat-reports/state-of-the-phish

Microsoft. (2023). *Protecting against phishing attacks*.  
https://learn.microsoft.com/en-us/security/operations/phishing

---

## 15. Notes
- Human factors remain the primary risk driver
- MFA significantly reduces impact but not prevalence
- Continuous tuning of email detections is required
