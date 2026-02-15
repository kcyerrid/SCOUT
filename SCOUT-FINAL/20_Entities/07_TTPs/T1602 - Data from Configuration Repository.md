---
entity_type: mitre_technique

technique_id: "T1602"
subtechnique_id: ""
technique_name: "Data from Configuration Repository"

tactic:
  - "TA0009 - Collection"
platforms:
  - Network Devices
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: []

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

created: 2026-01-06
updated: 2026-01-06

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

## 1. Summary
**Data from Configuration Repository** targets configuration repositories used to manage devices (especially network devices). Adversaries collect sensitive administrative/configuration data at scale via protocols and management interfaces, often aligning with discovery goals and enabling follow-on access, credential harvesting, and lateral movement.

## 2. Technical Overview
Key concepts:
- Configuration repositories store/serve device configuration and management state.
- Exposure occurs via management protocols and APIs (protocol examples referenced in ATT&CK detection narrative include SNMP and network configuration interfaces).
- Adversaries may:
  - enumerate managed devices,
  - request/dump configuration data,
  - extract credentials, routing/topology, ACLs, VPN settings, or admin contacts.

## 3. Subtechnique Considerations
This technique has two sub-techniques:
- [[20_Entities/07_TTPs/TA0009 - Collection/T1602.001 - SNMP (MIB Dump)|T1602.001]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1602.002 - Network Device Configuration Dump|T1602.002]]

## 4. Procedure Examples
Review the technique and sub-technique pages for ATT&CK procedure examples and mappings relevant to your device ecosystem (SNMP, NETCONF/RESTCONF-like management access patterns are referenced in detection guidance on the technique page).

## 5. Detection Guidance
ATT&CK detection strategy (DET0592 / AN1630) emphasizes monitoring for anomalous configuration extraction attempts, including:
- Repeated management queries from **untrusted sources** (unexpected IPs/segments).
- Abnormal query types requesting **sensitive configuration data**.
- Access outside **normal administrative windows**.
- Unusual sequences: enumeration → bulk repository access → sustained pulls.

Recommended detections:
- Rate-based alerts for SNMP/config queries exceeding baseline.
- Source-based alerts: management traffic from non-management subnets.
- Temporal alerts: management pulls during off-hours paired with other intrusion indicators.
- Context correlation: config pulls followed by changes, new accounts, ACL modifications, or lateral movement attempts.

### 5.1 Data Source Notes
- Collect and retain:
  - network telemetry for management protocols (flow + deep logs where available)
  - device logs (AAA, auth failures, config access operations)
  - IDS/IPS signatures for unauthorized management traffic
- Ensure management-plane segmentation is observable (separate mgmt VLAN/VRF, jump hosts).

## 6. Response Guidance
1. **Contain management access**: block offending sources; restrict management protocols to jump hosts.
2. **Credential actions**: rotate SNMP communities/credentials; enforce SNMPv3 authPriv where applicable.
3. **Scope**: determine which devices were queried and what data was accessed/dumped.
4. **Hunt**: look for follow-on behaviors leveraging harvested config data (new routes, ACL changes, VPN access, credential reuse).
5. **Hardening**: implement allowlists for MIB objects/views, least privilege, and management-plane monitoring.

## 7. Related ATT&CK Content
- Primary:
  - [[20_Entities/07_TTPs/TA0009 - Collection/T1602 - Data from Configuration Repository|T1602]]

## 8. SOC Relevance
High SOC value because:
- Configuration data is “high leverage” (credentials, topology, access rules).
- Unauthorized management-plane access is typically rare and highly detectable with segmentation and baseline monitoring.
- Enables rapid scoping and containment by focusing on the management plane.

## 9. Threat Actor Usage
ATT&CK enumerates adversary usage on technique/sub-technique pages where available.

## 10. Campaign Usage
ATT&CK lists campaign usage on the technique page where applicable.

## 11. Malware Usage
ATT&CK lists software usage on the technique page where applicable.

## 12. Mitigations
ATT&CK-listed mitigations include:
- **Encrypt Sensitive Information (M1041)**: configure SNMPv3 with highest security (authPriv).
- **Filter Network Traffic (M1037)**: apply extended ACLs to block unauthorized protocols outside trusted networks.
- **Network Intrusion Prevention (M1031)**: detect unauthorized SNMP queries/commands.
- **Network Segmentation (M1030)**: separate management traffic on dedicated networks.
- **Software Configuration (M1054)**: allowlist MIB objects and implement SNMP views.
- **Update Software (M1051)**: keep device images/software updated; migrate to SNMPv3.

## 13. Testing & Validation
- In a lab:
  - generate benign SNMP queries from approved mgmt hosts vs. unapproved hosts; confirm detections and blocking
  - test rate-based thresholds for config queries to avoid false positives during maintenance windows
- Validate controls:
  - SNMPv3 authPriv enforcement
  - ACL effectiveness for management-plane restrictions

## 14. References
- MITRE ATT&CK. (2025, October 24). *Data from Configuration Repository (T1602)*. https://attack.mitre.org/techniques/T1602/
- US-CERT. (n.d.). *Alert and guidance referenced on the ATT&CK technique page for configuration repository exposure.* https://www.us-cert.gov/
- Cisco. (n.d.). *SNMP configuration and security guidance (as referenced on ATT&CK mitigation list).* https://www.cisco.com/

## 15. Notes
- Prioritize management-plane visibility and segmentation; it dramatically increases detection confidence and reduces response time.
- Consider device-specific nuances (vendor logging, management protocols enabled, and AAA integrations).
