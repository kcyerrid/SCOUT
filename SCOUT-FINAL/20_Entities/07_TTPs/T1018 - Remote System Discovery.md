---
entity_type: mitre_technique

technique_id: "T1018"
subtechnique_id: ""
technique_name: "Remote System Discovery"

tactic:
  - Discovery
platforms:
  - ESXi
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]"
  - "[[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]"
  - "[[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0552 - AdFind|AdFind]]"
  - "[[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound]]"
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]"
associated_campaigns: []
related_techniques:
  - "T1046"
  - "T1016"

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

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

# T1018 - Remote System Discovery

## 1. Summary
Adversaries enumerate other systems in the environment (hostnames, IPs, identifiers) to build a target list for lateral movement, identify critical infrastructure, and map reachable assets. This behavior is often a precursor to credentialed access expansion and remote execution.

## 2. Technical Overview
Remote system discovery is achieved via:
- **Active probing**: ICMP echo, name service queries, directory queries, and network scanning utilities.
- **Directory-based discovery**: querying directory services to identify computers and servers.
- **Passive collection**: parsing local host files or caches (e.g., hosts file equivalents, ARP cache) to infer nearby systems.
- **Network device CLI**: discovery via infrastructure device commands to view neighbors/ARP tables (platform-dependent).

## 3. Subtechnique Considerations
- No sub-techniques.
- The same technique appears across IT and OT contexts; on mixed networks, adversaries may pivot from IT visibility into OT assets where routing/segmentation permits.

## 4. Procedure Examples
MITRE procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]] performing remote discovery in Ukraine power grid-related intrusions (per MITRE procedure examples).
- Use of directory and enumeration tools such as [[30_CIPHER/05_Malware/S0552 - AdFind|AdFind]] and [[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound]] to identify computers/domain controllers and enumerate network-relevant objects.
- Multiple groups (e.g., [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]], [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]) using discovery utilities and custom tooling to map reachable hosts (per MITRE procedure examples).

## 5. Detection Guidance
Detections should focus on **abnormal enumeration behavior** and chaining.

High-signal patterns:
- Bursty discovery: many hosts probed/enumerated in a short timeframe.
- Discovery launched from newly compromised hosts, unusual user contexts, or from endpoints that do not typically perform network administration.
- Correlation between discovery and subsequent authentication attempts, remote service connections, or remote execution.

Practical analytics ideas:
- Correlate process creation for known discovery utilities/frameworks with:
  - spikes in outbound connections to many internal destinations
  - name resolution bursts (DNS/NBNS/LLMNR/mDNS depending on environment)
- Detect directory queries for computer objects from non-admin endpoints or unusual principals.
- Baseline “network management subnets” and alert when similar activity occurs elsewhere.

### Data Source Notes
- **Endpoint**: process creation + command line, parent/child lineage, script logging, network connection telemetry (EDR).
- **Network**: DNS logs, NetFlow/VPC flow logs, internal scanning heuristics, ICMP telemetry where collected.
- **Identity/Directory**: DC logs, directory query telemetry (where available), authentication telemetry for follow-on attempts.
- **Network devices**: CLI audit logs if discovery is performed from infrastructure devices.

## 6. Response Guidance
1. **Determine scope**: identify source host/account and enumerate targeted destinations.
2. **Assess intent**: check whether activity aligns with admin tools/change windows; if not, treat as lateral movement staging.
3. **Hunt follow-ons**: failed/successful logons across many hosts, remote service creation, RDP/SMB/WMI/WinRM usage.
4. **Contain**: isolate the source host; restrict east-west movement; rotate credentials if the activity indicates compromise.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1046 - Network Service Discovery|T1046]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1016 - System Network Configuration Discovery|T1016]]

## 8. SOC Relevance
- Strong precursor for lateral movement; often appears shortly before remote authentication spraying or exploitation.
- High-volume scanning is easy to catch; **low-and-slow** enumeration requires baselining and longer-window analytics.

## 9. Threat Actor Usage
Examples from MITRE procedure examples include:
- [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team|Sandworm Team]]
- [[30_CIPHER/03_Threat_Actors/G0050 - APT32|APT32]]
- [[30_CIPHER/03_Threat_Actors/G0096 - APT41|APT41]]

## 10. Campaign Usage
- Campaign references exist in MITRE procedure examples; tie to your environment’s observed intrusion narrative.

## 11. Malware Usage
Representative software/tooling includes:
- [[30_CIPHER/05_Malware/S0552 - AdFind|AdFind]]
- [[30_CIPHER/05_Malware/S0521 - BloodHound|BloodHound]]
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|Cobalt Strike]]

## 12. Mitigations
Remote discovery can be hard to prevent outright. Prioritize:
- Network segmentation and host-based firewalls to reduce discovery reachability
- Restrict/administer ICMP and legacy name resolution protocols where feasible
- Least privilege and tiered admin models to limit directory query and remote access capabilities
- Monitor and control installation/use of admin discovery tools on non-admin endpoints

## 13. Testing & Validation
- In a lab:
  - run controlled discovery from an admin workstation vs a standard user workstation
  - validate logging for endpoint/network/directory signals
- Validate detections:
  - burst scanning analytics
  - anomaly-based host enumeration
  - correlation to follow-on authentication/lateral movement behaviors

## 14. References
- MITRE ATT&CK. (n.d.). *Remote System Discovery (T1018).* https://attack.mitre.org/techniques/T1018/
- MITRE ATT&CK. (n.d.). *Sandworm Team (G0034).* https://attack.mitre.org/groups/G0034/
- CISA. (n.d.). *ICS Alert / critical infrastructure reporting (referenced by MITRE for discovery on network devices).* https://www.cisa.gov/

## 15. Notes
- For best results, build detections around “**who** is enumerating **what**, from **where**, and **what happens next**,” rather than single-event alerts.
