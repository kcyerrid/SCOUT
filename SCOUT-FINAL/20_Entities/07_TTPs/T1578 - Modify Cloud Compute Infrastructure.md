---
entity_type: mitre_technique

technique_id: "T1578"
subtechnique_id: ""
technique_name: "Modify Cloud Compute Infrastructure"

tactic:
  - Defense Evasion
  - Persistence

platforms:
  - Cloud
  - SaaS

datasources:
  - Cloud Audit Logs
  - IAM Logs
  - Resource Configuration Logs
  - Network Traffic
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
  - "T1098"
  - "T1078"
  - "T1556"
  - "T1577"

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
  - cloud
  - defense-evasion
  - persistence
  - infrastructure
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Modify Cloud Compute Infrastructure (T1578)

## 1. Summary
Modify Cloud Compute Infrastructure describes adversaries **changing the configuration or behavior of cloud-based compute resources** to evade detection, maintain persistence, or enable further malicious activity. This includes modifying virtual machines, instances, containers, or serverless configurations.

Attackers use this technique to:
- Establish durable persistence in cloud environments
- Evade monitoring and security controls
- Enable lateral movement or data exfiltration
- Maintain access without deploying traditional malware

---

## 2. Technical Overview
Cloud environments rely on declarative configuration and control-plane APIs. Adversaries abuse these mechanisms by:

- Modifying instance metadata or startup scripts
- Changing network security groups or firewall rules
- Altering instance roles, permissions, or service accounts
- Enabling remote access mechanisms (e.g., SSH keys, RDP)
- Modifying autoscaling, snapshots, or images to propagate access

Common targets include:
- Virtual machines and compute instances
- Container workloads and orchestration settings
- Serverless functions and triggers
- Cloud-native management agents

Indicators include:
- Unexpected configuration changes outside change windows
- Compute resources modified shortly after suspicious authentication
- Startup scripts or metadata containing unauthorized logic
- Persistence mechanisms embedded in images or templates

---

## 3. Subtechnique Considerations
T1578 includes cloud-provider–specific subtechniques (e.g., instance settings, metadata, or images). Considerations include:
- Provider differences (AWS, Azure, GCP)
- Whether changes affect a single instance or propagate broadly
- Persistence via templates, images, or autoscaling groups

This technique often complements **account abuse** rather than endpoint exploitation.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Adding malicious startup scripts to instances
- Modifying instance metadata to inject SSH keys
- Altering firewall rules to allow covert access
- Updating images or templates to persist across redeployments

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **control-plane visibility and change management**:
- Monitor cloud audit logs for configuration changes
- Alert on compute modifications by non-administrative identities
- Correlate changes with authentication anomalies
- Detect persistence mechanisms embedded in metadata or templates

### Data Source Notes
- **Cloud audit logs**: Primary source for detection
- **IAM logs**: Attribute changes to identities
- **Configuration logs**: Detect drift and unauthorized changes
- **Network telemetry**: Identify newly exposed services

Common false positives:
- Legitimate infrastructure automation
- Scheduled maintenance or scaling operations

Tuning guidance:
- Baseline expected automation identities
- Enforce approval workflows for compute changes
- Increase severity for changes following suspicious login events

---

## 6. Response Guidance
When suspected:
1. Identify modified resources and scope of changes
2. Roll back unauthorized configurations
3. Rotate affected credentials and keys
4. Review audit logs for lateral movement or persistence
5. Implement stricter change controls and monitoring

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1098 - Account Manipulation|T1098]]
  - [[20_Entities/07_TTPs/TA0001 - Initial Access/T1078 - Valid Accounts|T1078]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1556 - Modify Authentication Process|T1556]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1577 - Cloud Infrastructure Discovery|T1577]]

---

## 8. SOC Relevance
T1578 is critical in cloud-centric environments because:
- Persistence can exist entirely in configuration
- Malware may never touch disk
- Traditional endpoint detections may fail

SOC teams must treat **cloud configuration as an attack surface**.

---

## 9. Threat Actor Usage
Commonly used by:
- Cloud-focused intrusion groups
- Actors targeting SaaS and IaaS platforms
- Adversaries abusing stolen cloud credentials

---

## 10. Campaign Usage
Observed in:
- Cloud account takeover campaigns
- Long-term cloud persistence operations
- Supply-chain–adjacent cloud intrusions

---

## 11. Malware Usage
Associated with:
- Minimal or no malware usage
- Scripts embedded in startup metadata
- Cloud-native persistence mechanisms

---

## 12. Mitigations
Recommended mitigations:
- Enforce least-privilege IAM roles
- Monitor and alert on infrastructure changes
- Require approvals for compute modifications
- Use infrastructure-as-code with drift detection

---

## 13. Testing & Validation
Validation approaches:
- Simulate benign compute configuration changes
- Validate alerts on unauthorized modifications
- Test SOC workflows for cloud persistence scenarios
- Ensure rollback and recovery procedures are effective

---

## 14. References
MITRE ATT&CK. (2025). *Modify Cloud Compute Infrastructure (T1578)*.  
https://attack.mitre.org/techniques/T1578/

AWS. (2024). *Detecting unauthorized EC2 changes*.  
https://docs.aws.amazon.com/

Microsoft. (2024). *Azure resource change monitoring*.  
https://learn.microsoft.com/azure/

Google Cloud. (2024). *Cloud audit logging best practices*.  
https://cloud.google.com/logging/

---

## 15. Notes
- Cloud persistence often lives in configuration, not binaries.
- Audit logs are the primary forensic record.
- Drift detection is a key defensive capability.
