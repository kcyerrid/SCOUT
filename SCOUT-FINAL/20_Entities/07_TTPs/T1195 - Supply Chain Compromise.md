---
entity_type: mitre_technique

technique_id: "T1195"
subtechnique_id: ""
technique_name: "Supply Chain Compromise"

tactic: ["Initial Access"]
platforms: ["windows", "linux", "macos", "cloud", "saas", "network"]
datasources: ["Application Logs", "Package Manager Logs", "Network Traffic", "Code Repository Logs", "CI/CD Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1195.001", "T1195.002", "T1195.003"]

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

# Supply Chain Compromise (T1195)

## 1. Summary
Supply Chain Compromise describes adversary tampering with hardware, software, or services at any point in the supply chain to gain initial access to downstream targets. This technique enables attackers to scale access, bypass perimeter defenses, and inherit trust relationships by compromising vendors, dependencies, or delivery mechanisms.

The operational impact is often severe, as a single compromise can affect thousands of organizations simultaneously.

---

## 2. Technical Overview
Adversaries compromise trusted suppliers, update mechanisms, or dependencies by:
- Injecting malicious code into legitimate software updates
- Compromising build systems, CI/CD pipelines, or code repositories
- Abusing package managers or software dependencies
- Manipulating hardware or firmware before delivery

Artifacts may include signed but malicious updates, anomalous build artifacts, unexpected outbound connections, and execution of trusted binaries with malicious behavior.

---

## 3. Subtechnique Considerations
T1195 includes several subtechniques based on the compromised component:
- Software supply chain
- Hardware supply chain
- Software dependencies and development tools

Each subtechnique presents different detection challenges depending on visibility into vendor environments and internal build processes.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Backdooring legitimate software updates
- Injecting malicious dependencies into open-source packages
- Compromising CI/CD pipelines to alter build outputs
- Abusing trusted update channels for payload delivery

Analysts may observe malicious behavior originating from trusted, signed software.

---

## 5. Detection Guidance
Detection should emphasize integrity and behavior monitoring:
- Unexpected behavior from trusted applications
- Changes in software hashes or signing metadata
- Anomalous outbound network connections from trusted processes
- CI/CD pipeline activity inconsistent with baseline workflows

Detection is challenging and often requires behavioral analysis rather than signature-based controls.

### Data Source Notes
- **Application Logs:** Useful for identifying abnormal behavior post-installation
- **Code Repository Logs:** Critical for detecting unauthorized commits or access
- **CI/CD Logs:** High value for identifying build pipeline tampering

---

## 6. Response Guidance
When a supply chain compromise is suspected:
- Isolate affected systems and halt deployments
- Identify the compromised component and scope of exposure
- Revoke trust in affected vendors or artifacts
- Coordinate with vendors and stakeholders for remediation

Preserve build artifacts, logs, and affected binaries for forensic analysis.

---

## 7. Related ATT&CK Content
- Subtechniques:  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1195.001 - Compromise Software Supply Chain|T1195.001]]  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1195.002 - Compromise Hardware Supply Chain|T1195.002]]  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1195.003 - Compromise Software Dependencies and Development Tools|T1195.003]]

- Often paired with persistence and execution techniques following initial access

---

## 8. SOC Relevance
Supply Chain Compromise represents a high-impact, low-frequency but catastrophic risk. Detection maturity is typically low due to limited visibility into third-party environments, making proactive monitoring and vendor risk management critical.

---

## 9. Threat Actor Usage
This technique has been used by:
- Advanced persistent threat groups conducting strategic espionage
- Nation-state actors targeting technology ecosystems
- Highly capable adversaries seeking large-scale access

Confidence in usage by advanced actors is high.

---

## 10. Campaign Usage
Supply chain compromise has appeared in:
- Large-scale espionage operations
- Strategic access campaigns targeting software providers
- Long-term, stealthy intrusions with broad downstream impact

---

## 11. Malware Usage
Malware delivered via supply chain compromise often appears as:
- Backdoored legitimate software
- Signed loaders embedded in updates
- Modified dependencies masquerading as benign libraries

Examples include tooling later used for command-and-control and lateral movement such as:
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]

---

## 12. Mitigations
Effective mitigations include:
- Vendor risk management and security assessments
- Code signing validation and integrity monitoring
- Dependency auditing and software composition analysis (SCA)
- Securing CI/CD pipelines and build environments
- Network monitoring for anomalous behavior from trusted applications

---

## 13. Testing & Validation
Validation approaches include:
- Red team simulations of compromised dependencies
- Integrity monitoring tests for build artifacts
- Purple team exercises targeting CI/CD security controls

Successful validation results in detection of anomalous trusted software behavior.

---

## 14. References
MITRE ATT&CK. (2024). *Supply Chain Compromise (T1195)*.  
https://attack.mitre.org/techniques/T1195/

CISA. (2023). *Securing the Software Supply Chain*.  
https://www.cisa.gov/software-supply-chain-security

NIST. (2022). *Secure Software Development Framework (SSDF)*.  
https://csrc.nist.gov/Projects/ssdf

---

## 15. Notes
- Detection often lags initial compromise by weeks or months
- Trust relationships amplify blast radius
- Continuous monitoring of “trusted” software is essential

