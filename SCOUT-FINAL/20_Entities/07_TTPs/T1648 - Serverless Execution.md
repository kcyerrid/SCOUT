---
entity_type: mitre_technique

technique_id: "T1648"
subtechnique_id: ""
technique_name: "Serverless Execution"

tactic: ["Execution"]
platforms: ["cloud"]
datasources: ["Cloud Audit Logs", "Function Execution Logs", "API Call Logs", "Authentication Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1059.009", "T1106", "T1526", "T1550"]

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

# Serverless Execution (T1648)

## 1. Summary
Serverless Execution describes adversaries executing malicious logic by abusing serverless compute services provided by cloud platforms. Rather than executing code on traditional virtual machines or endpoints, attackers leverage managed services such as AWS Lambda, Azure Functions, or Google Cloud Functions to run attacker-controlled code.

This technique enables highly stealthy execution that bypasses endpoint-based defenses and relies almost entirely on cloud control-plane visibility for detection.

---

## 2. Technical Overview
Cloud providers offer serverless services that automatically execute code in response to events such as API calls, object uploads, or scheduled triggers.

Adversaries abuse serverless execution by:
- Deploying malicious serverless functions using stolen credentials
- Modifying existing functions to include malicious logic
- Triggering execution via events (storage uploads, API requests, schedules)
- Using serverless functions as staging, persistence, or C2 infrastructure

Artifacts include function creation/modification logs, execution logs, API calls, and identity activity associated with serverless services.

---

## 3. Subtechnique Considerations
T1648 does not define subtechniques. Variations are driven by:
- Cloud provider (AWS, Azure, GCP)
- Trigger mechanisms (event-driven, scheduled, API-invoked)
- Execution role permissions
- Integration with other managed services

Detection strategies must be cloud-provider–specific and account for normal automation usage.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Creating malicious Lambda or Azure Functions for payload staging
- Injecting malicious logic into legitimate serverless workflows
- Using serverless execution to exfiltrate data from cloud storage
- Leveraging scheduled triggers for delayed or recurring execution

Analysts may observe serverless execution outside expected deployment pipelines or operational workflows.

---

## 5. Detection Guidance
Detection should focus on:
- Creation or modification of serverless functions outside CI/CD pipelines
- Execution of functions with anomalous triggers or permissions
- Serverless functions accessing unexpected resources or networks
- API calls originating from unusual locations or identities

Behavioral baselining of serverless activity is critical for effective detection.

### Data Source Notes
- **Cloud Audit Logs:** Primary source for detection
- **Function Execution Logs:** High-value for runtime behavior
- **API Call Logs:** Useful for tracing execution initiation

---

## 6. Response Guidance
When malicious serverless execution is suspected:
- Disable or quarantine affected serverless functions
- Revoke and rotate associated credentials or roles
- Review function code and deployment history
- Assess downstream impact to data and services

Preserve audit logs, execution logs, and function code for investigation.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059.009 - Cloud API|T1059.009]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1106 - Native API|T1106]]  
  [[20_Entities/07_TTPs/TA0003 - Persistence/T1526 - Cloud Service Discovery|T1526]]  
  [[20_Entities/07_TTPs/TA0006 - Credential Access/T1550 - Use Alternate Authentication Material|T1550]]

---

## 8. SOC Relevance
Serverless execution represents a growing blind spot for many SOC teams due to limited control-plane monitoring maturity. As organizations increase serverless adoption, this technique becomes increasingly relevant for both stealthy execution and persistence.

---

## 9. Threat Actor Usage
This technique is used by:
- Cloud-focused threat actors
- Ransomware operators targeting cloud-native environments
- Advanced persistent threat groups
- Insider threat scenarios

Confidence in increasing real-world usage is high.

---

## 10. Campaign Usage
Serverless execution has appeared in:
- Cloud resource hijacking campaigns
- Data exfiltration operations
- Long-dwell cloud persistence intrusions

---

## 11. Malware Usage
Malware and tooling leveraging serverless execution include:
- [[30_CIPHER/05_Malware/S0552 - CloudSploit|CloudSploit]]
- [[30_CIPHER/05_Malware/S1048 - TeamTNT Tooling|TeamTNT Tooling]]
- [[30_CIPHER/05_Malware/S1096 - Serverless Backdoor Tooling|Serverless Backdoor Tooling]]

---

## 12. Mitigations
Effective mitigations include:
- Enforcing least-privilege IAM roles for serverless functions
- Monitoring and alerting on serverless creation/modification events
- Restricting function deployment to approved pipelines
- Applying CSPM controls for serverless services
- Regular audits of serverless code and triggers

---

## 13. Testing & Validation
Validation approaches include:
- Purple team simulations of malicious serverless deployment
- Testing detection of unauthorized function creation
- Review of alerts tied to anomalous serverless execution

Successful validation results in detection of unauthorized serverless code execution.

---

## 14. References
MITRE ATT&CK. (2024). *Serverless Execution (T1648)*.  
https://attack.mitre.org/techniques/T1648/

AWS. (2023). *Security best practices for AWS Lambda*.  
https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html

Microsoft. (2023). *Azure Functions security overview*.  
https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts

---

## 15. Notes
- Serverless execution is identity- and API-driven
- Endpoint-based controls provide no visibility
- Logging maturity determines detection effectiveness
