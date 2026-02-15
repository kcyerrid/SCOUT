---
entity_type: mitre_technique

technique_id: "T1567"
subtechnique_id: ""
technique_name: "Exfiltration Over Web Service"

tactic: ["Exfiltration"]
platforms: ["windows", "linux", "macos", "cloud", "saas"]
datasources: ["Network Traffic", "Web Proxy Logs", "Cloud Service Logs", "DNS Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1041", "T1567.001", "T1567.002"]

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

# Exfiltration Over Web Service (T1567)

## 1. Summary
Exfiltration Over Web Service describes adversary exfiltration of data using legitimate web-based services such as cloud storage providers, code repositories, file-sharing platforms, or web APIs. By abusing trusted services and standard protocols (e.g., HTTPS), adversaries can blend malicious data transfer with normal outbound traffic, reducing the likelihood of detection.

This technique is commonly used during the final stages of an intrusion to steal sensitive data prior to monetization or disclosure.

---

## 2. Technical Overview
Adversaries leverage web services to upload or synchronize stolen data using standard web protocols.

Common mechanisms include:
- Uploading data to cloud storage services (e.g., file-sharing platforms)
- Pushing data to code repositories or paste services
- Using REST APIs to transmit data over HTTPS
- Encoding or compressing data prior to upload

Artifacts include outbound HTTPS connections, large or anomalous uploads, API calls, and authentication events to external services.

---

## 3. Subtechnique Considerations
T1567 includes multiple subtechniques that differentiate the specific web service abused, such as:
- Cloud storage services
- Code repositories
- Web-based file hosting platforms

Each subtechnique presents unique detection challenges depending on the service’s prevalence and logging capabilities.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Uploading stolen documents to attacker-controlled cloud storage accounts
- Using legitimate APIs to push data to external repositories
- Leveraging synchronization clients to exfiltrate data incrementally
- Compressing and encrypting data prior to upload

Analysts may observe sustained outbound data transfers to trusted services outside normal usage patterns.

---

## 5. Detection Guidance
Detection should focus on behavioral and contextual analysis:
- Large or unusual outbound uploads to web services
- Authentication to cloud services not previously used by the host or user
- Use of APIs or clients outside approved tooling
- Data transfer volumes inconsistent with user role or system purpose

Visibility into proxy, network, and cloud audit logs is essential.

### Data Source Notes
- **Web Proxy Logs:** High value for identifying anomalous uploads
- **Network Traffic:** Useful for detecting volume anomalies
- **Cloud Service Logs:** Critical for identifying unauthorized service usage

---

## 6. Response Guidance
When exfiltration over web services is suspected:
- Immediately restrict outbound access to abused services
- Identify scope and sensitivity of exfiltrated data
- Revoke credentials or API keys used for exfiltration
- Notify legal, compliance, and leadership teams as required

Preserve network and application logs for forensic analysis.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0010 - Exfiltration/T1041 - Exfiltration Over C2 Channel|T1041]]  
  [[20_Entities/07_TTPs/TA0010 - Exfiltration/T1567.001 - Exfiltration to Cloud Storage|T1567.001]]  
  [[20_Entities/07_TTPs/TA0010 - Exfiltration/T1567.002 - Exfiltration to Code Repository|T1567.002]]

---

## 8. SOC Relevance
Exfiltration over web services is difficult to detect due to its use of encrypted traffic and trusted destinations. SOCs must rely on behavioral baselining and contextual analysis rather than simple blocklists.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Ransomware operators prior to extortion
- Espionage-focused advanced persistent threat groups
- Insider threat actors abusing legitimate access

Confidence in widespread usage is high.

---

## 10. Campaign Usage
Exfiltration over web services appears in:
- Double-extortion ransomware campaigns
- Long-dwell espionage operations
- Insider data theft incidents

---

## 11. Malware Usage
Malware frequently associated with web-based exfiltration includes:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]

---

## 12. Mitigations
Effective mitigations include:
- Egress filtering and proxy enforcement
- Monitoring and limiting uploads to cloud services
- Data loss prevention (DLP) controls
- Restricting use of unauthorized web services
- Network anomaly detection

---

## 13. Testing & Validation
Validation approaches include:
- Simulated data exfiltration to test detection thresholds
- Purple team exercises focusing on cloud service abuse
- Review of proxy and DLP alerting effectiveness

Successful validation identifies anomalous data transfer activity.

---

## 14. References
MITRE ATT&CK. (2024). *Exfiltration Over Web Service (T1567)*.  
https://attack.mitre.org/techniques/T1567/

Mandiant. (2023). *Detecting data exfiltration over HTTPS*.  
https://www.mandiant.com/resources/blog/detecting-data-exfiltration-https

Microsoft. (2023). *Monitoring data exfiltration in cloud environments*.  
https://learn.microsoft.com/en-us/security/operations/data-exfiltration

---

## 15. Notes
- HTTPS encryption significantly complicates detection
- Cloud service abuse often appears legitimate
- Behavioral baselining is critical for effective detection

