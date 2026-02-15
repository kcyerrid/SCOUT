---
entity_type: ttp

ttp_id: "T1197"
ttp_name: "BITS Jobs"
tactic: "Persistence, Defense Evasion"
platforms:
  - "Windows"

description_short: "Adversaries abuse Background Intelligent Transfer Service (BITS) jobs to download or execute malicious code and maintain persistence."

related_subtechniques: []

detection_difficulty: "Medium"
impact_severity: "Medium"

created: "2025-12-18"
updated: "2025-12-18"

tlp_classification: "TLP:CLEAR"
---

# T1197 – BITS Jobs

## 1. Technique Overview
**BITS Jobs (T1197)** is a MITRE ATT&CK technique in which adversaries abuse the **Background Intelligent Transfer Service (BITS)** on Windows systems to **download, upload, or execute malicious payloads**. BITS is a legitimate Windows service designed to transfer files asynchronously and resiliently, making it attractive for stealthy adversary activity.

Attackers may use BITS jobs for **persistence** by creating jobs that resume after reboot, or for **defense evasion** by leveraging a trusted system service to blend malicious activity into normal operating behavior.

## 2. Adversary Objectives
Adversaries leverage BITS jobs to:
- Download additional payloads with reduced visibility
- Maintain persistence across system reboots
- Execute code using a trusted Windows service
- Evade network and endpoint detection controls

## 3. Common Abuse Patterns
- Creating persistent BITS jobs that execute malicious binaries
- Downloading payloads from attacker-controlled servers using BITS
- Using `bitsadmin.exe` or PowerShell cmdlets to manage jobs
- Scheduling BITS jobs to resume periodically or at system startup
- Combining BITS with other living-off-the-land techniques

## 4. Detection Considerations
Detection relies on **process, service, and command-line telemetry**, including:
- Monitoring execution of `bitsadmin.exe` or BITS-related PowerShell cmdlets
- Detecting creation of new or persistent BITS jobs
- Identifying BITS jobs referencing suspicious URLs or file paths
- Correlating BITS activity with unusual parent processes
- Reviewing Windows event logs related to BITS service activity

## 5. Defensive Mitigations
- Monitor and restrict use of `bitsadmin.exe` where feasible
- Use application control to limit unauthorized scripting tools
- Inspect BITS job metadata for suspicious commands or destinations
- Correlate BITS activity with network monitoring data
- Remove unauthorized or suspicious BITS jobs during incident response

## 6. Operational Impact
If abused successfully, T1197 can:
- Enable stealthy payload delivery
- Provide persistence without traditional startup artifacts
- Allow adversaries to leverage trusted system services
- Complicate detection due to legitimate BITS usage

## 7. Analyst Notes
BITS abuse exemplifies how attackers repurpose benign Windows services for malicious ends. While BITS is commonly used by legitimate software (e.g., Windows Update), adversary-created jobs often stand out through **unexpected command execution, unusual URLs, or anomalous job lifetimes**. Effective detection depends on contextual analysis rather than binary presence alone.

## 8. References
- MITRE ATT&CK. (n.d.). *BITS Jobs (T1197)*. https://attack.mitre.org/techniques/T1197/
- Microsoft. (n.d.). *Background Intelligent Transfer Service*. https://learn.microsoft.com/windows/win32/bits/background-intelligent-transfer-service-portal
- SANS Institute. (n.d.). *Living-off-the-Land: BITS Abuse*. https://www.sans.org/
