---
entity_type: mitre_technique

technique_id: "T1078"
subtechnique_id: ""
technique_name: "Valid Accounts"

tactic: ["Initial Access", "Persistence", "Privilege Escalation", "Defense Evasion"]
platforms: ["windows", "linux", "macos", "cloud", "saas"]
datasources: ["Authentication Logs", "User Account Metadata", "Cloud Service Logs", "Network Traffic"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1078.001", "T1078.002", "T1078.003", "T1078.004"]

detection_priority: "Critical"
detection_maturity: ""
threat_score: 5

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

# Valid Accounts (T1078)

## 1. Summary
Valid Accounts describes the use of legitimate, stolen, or otherwise compromised credentials to gain or maintain access to systems, services, or cloud environments. This technique is highly effective because it leverages trusted authentication mechanisms, often bypassing traditional security controls.

Adversaries favor this technique because it blends malicious activity with legitimate user behavior, enabling persistence, lateral movement, and privilege escalation with minimal noise.

---

## 2. Technical Overview
Adversaries obtain valid credentials through phishing, credential dumping, malware, data breaches, or purchasing access from initial access brokers. These credentials are then used to authenticate via standard mechanisms such as local login, domain authentication, VPNs, SaaS portals, or cloud APIs.

Prerequisites include possession of valid credentials and network or service reachability. Artifacts include authentication events, session creation logs, and cloud identity activity.

---

## 3. Subtechnique Considerations
T1078 includes multiple subtechniques scoped by account type:
- Default Accounts
- Domain Accounts
- Local Accounts
- Cloud Accounts

Each subtechnique introduces different detection challenges depending on identity provider, logging quality, and baseline behavior.

---

## 4. Procedure Examples
Common adversary procedures include:
- Logging in via VPN using compromised credentials
- Authenticating to cloud portals with stolen API keys
- Reusing local administrator credentials across hosts
- Leveraging default credentials on exposed services

Analysts may observe successful logins from unusual geographies, devices, or times.

---

## 5. Detection Guidance
Detection should prioritize identity-centric analytics:
- Successful authentications following phishing or malware activity
- Anomalous login locations, devices, or user agents
- Use of privileged accounts outside normal patterns
- Cloud API usage inconsistent with baseline behavior

Behavioral baselining and MFA enforcement significantly improve detection efficacy.

### Data Source Notes
- **Authentication Logs:** Primary detection source; ensure MFA context is logged
- **Cloud Logs:** High signal when enriched with identity metadata
- **Network Traffic:** Useful for correlating access paths (VPN, remote services)

---

## 6. Response Guidance
When Valid Account usage is suspected:
- Immediately validate account ownership and intent
- Reset credentials and revoke active sessions
- Review access scope and privilege assignments
- Investigate for follow-on activity (lateral movement, persistence)

Preserve identity and access logs for forensic analysis.

---

## 7. Related ATT&CK Content
- Subtechniques: `=this.related_techniques`
- Frequently paired with Phishing, Credential Dumping, and Remote Services

---

## 8. SOC Relevance
Valid Accounts is one of the most prevalent and dangerous ATT&CK techniques across ransomware, espionage, and fraud campaigns. Detection maturity varies widely, particularly in cloud and SaaS environments, making this a critical focus area for SOC investment.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Ransomware operators and affiliates
- Advanced persistent threat actors
- Initial access brokers monetizing stolen credentials

Confidence in widespread use is extremely high.

---

## 10. Campaign Usage
Valid Accounts appear in:
- Enterprise ransomware intrusions
- Cloud account takeovers
- Long-dwell espionage campaigns

---

## 11. Malware Usage
Malware families frequently associated with credential theft and subsequent Valid Account abuse include:
- [[30_CIPHER/05_Malware/S0266 - TrickBot|TrickBot]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]

---

## 12. Mitigations
Effective mitigations include:
- Enforcing multi-factor authentication everywhere possible
- Implementing conditional access and risk-based authentication
- Monitoring for anomalous login behavior
- Regular credential rotation and hygiene
- Disabling unused and default accounts

---

## 13. Testing & Validation
Validation approaches include:
- Atomic Red Team tests for T1078 subtechniques
- Purple team simulations of credential compromise scenarios
- Controlled testing of anomalous login detections

Successful validation produces timely alerts with low false positives.

---

## 14. References
MITRE ATT&CK. (2024). *Valid Accounts (T1078)*.  
https://attack.mitre.org/techniques/T1078/

Microsoft. (2023). *Protecting against credential-based attacks*.  
https://www.microsoft.com/en-us/security/blog/2023/01/18/protecting-against-credential-based-attacks/

CISA. (2022). *Securing credentials and access*.  
https://www.cisa.gov/resources-tools/resources/securing-credentials-and-access

---

## 15. Notes
- Identity compromise remains the primary initial access vector
- Cloud and SaaS visibility gaps increase risk
- Continuous improvement of identity telemetry is critical

