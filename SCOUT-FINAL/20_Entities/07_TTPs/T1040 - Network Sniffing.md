---
entity_type: mitre_technique

technique_id: "T1040"
subtechnique_id: ""
technique_name: "Network Sniffing"

tactic:
  - "TA0006 - Credential Access"
  - "TA0007 - Discovery"
platforms:
  - IaaS
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
  - "[[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team]]"
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0064 - APT33]]"
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0089 - BlackEnergy]]"
  - "[[30_CIPHER/05_Malware/S0367 - Emotet]]"
  - "[[30_CIPHER/05_Malware/S0357 - Impacket]]"
  - "[[30_CIPHER/05_Malware/S0174 - Responder]]"
associated_campaigns:
  - "C0028 - 2015 Ukraine Electric Power Attack"
related_techniques: []

detection_priority:
  - Medium

detection_maturity: ""
threat_score: 3

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
Network Sniffing (T1040) is passive capture/monitoring of network traffic to collect information about an environment, including credentials transmitted over the network, service configuration details, and network characteristics useful for follow-on intrusion activity.

## 2. Technical Overview
Common adversary approaches:
- **Host-based sniffing**: enabling promiscuous mode and capturing packets using packet capture utilities or custom libpcap-based tooling.
- **Cloud traffic mirroring abuse**: creating/modifying mirroring sessions (e.g., virtual taps / packet mirroring) to redirect traffic to attacker-controlled collectors.
- **Network device packet capture**: using built-in capture/monitor CLI capabilities on routers/switches/firewalls.
- **Credential-focused capture**: harvesting cleartext credentials (legacy protocols) or capturing challenge/response material usable for relay/abuse.

Why it matters to defenders:
- Captured traffic can expose **credentials**, **service endpoints**, **hostnames**, **VLAN/topology**, and other details enabling lateral movement and defense evasion.

## 3. Subtechnique Considerations
- No subtechniques are defined for T1040.
- Detections should be split by collection plane:
  - **Endpoints**
  - **Cloud control plane**
  - **Network device plane**

## 4. Procedure Examples
- C0028 - 2015 Ukraine Electric Power Attack: [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team]] used [[30_CIPHER/05_Malware/S0089 - BlackEnergy]]’s sniffer module to discover credentials in transit.
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28]]: used credential capture tooling associated with name-service poisoning/relay activity and Wi-Fi interception (per ATT&CK procedure examples).
- [[30_CIPHER/03_Threat_Actors/G0064 - APT33]]: used SniffPass to collect credentials by sniffing traffic.
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky]]: used SniffPass to obtain passwords sent over non-secure protocols.
- [[30_CIPHER/05_Malware/S0367 - Emotet]]: observed hooking network APIs to monitor traffic.
- [[30_CIPHER/05_Malware/S0357 - Impacket]]: can be used to sniff traffic via an interface or raw socket.
- [[30_CIPHER/05_Malware/S0174 - Responder]]: captures hashes/credentials after name service poisoning (credential capture via redirected traffic).

## 5. Detection Guidance
High-signal detection areas:
- **Promiscuous mode / capture enablement**
  - Interface mode changes to promiscuous.
  - Packet capture driver loads or privileged operations enabling capture.
- **Suspicious packet capture execution**
  - Unexpected packet capture utilities on servers/workstations (especially non-admin user contexts).
  - Unsanctioned use on sensitive segments (DCs, IdP connectors, jump hosts).
- **Cloud control plane monitoring**
  - Creation/modification of traffic mirroring resources, especially redirecting from critical instances to new/unknown collectors.
  - IAM actions granting permissions to create/modify mirroring sessions.
- **Network device capture**
  - Capture/monitor commands executed via CLI on infrastructure devices; correlate with unusual admin access.

Correlation recommendations:
- Tie capture activity to **subsequent exfiltration**, **credential use**, or **lateral movement** to reduce false positives.
- Monitor for **capture file creation** (pcap artifacts) and rapid access to those artifacts by unusual processes/users.

### Data Source Notes
Map to available telemetry:
- **Endpoint EDR**: process start, privilege context, module loads, network interface configuration changes, file creation for pcap outputs.
- **OS logs**: interface configuration changes, driver/service installation, auditing of privileged commands.
- **Cloud audit logs**: API calls for traffic mirroring/vTAP/packet mirroring, IAM policy changes, new collectors/targets.
- **Network device logs**: AAA/auth logs, config changes, packet capture/monitor command history.

## 6. Response Guidance
- **Containment**: stop/disable packet capture sessions, remove unauthorized mirroring, isolate suspected collectors.
- **Credential protection**: rotate credentials that may have traversed the sniffed path; invalidate sessions/tokens.
- **Scope**: identify which interfaces/segments were captured and for how long; enumerate affected protocols/apps.
- **Hardening**: restrict who can enable mirroring/capture (cloud IAM + network device RBAC), enforce least privilege.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1040 - Network Sniffing|T1040]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1040 - Network Sniffing|T1040]]

## 8. SOC Relevance
- Often a **precursor** to credential theft and internal discovery.
- Useful pivots:
  - “Who enabled capture?” (user/service principal)
  - “Where was traffic redirected?” (collector host/account)
  - “What happened next?” (new authentications, exfil, lateral movement)

## 9. Threat Actor Usage
- Widely observed across APT and cybercrime when attackers can access network vantage points (endpoints, devices, or cloud mirroring).
- Notable: [[30_CIPHER/03_Threat_Actors/G0034 - Sandworm Team]], [[30_CIPHER/03_Threat_Actors/G0007 - APT28]], [[30_CIPHER/03_Threat_Actors/G0064 - APT33]].

## 10. Campaign Usage
- C0028 - 2015 Ukraine Electric Power Attack: included sniffing to obtain credentials and environment details.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0089 - BlackEnergy]]: included a sniffer module used for credential discovery.
- [[30_CIPHER/05_Malware/S0367 - Emotet]]: network API hooking for traffic monitoring has been reported.
- [[30_CIPHER/05_Malware/S0174 - Responder]]: used for credential capture after redirected name-service traffic.

## 12. Mitigations
- **M1041 - Encrypt Sensitive Information**: enforce TLS/secure protocols; avoid cleartext credential transit.
- **M1032 - Multi-factor Authentication**: reduce value of captured passwords.
- **M1030 - Network Segmentation**: limit broadcast/multicast exposure and constrain sniffing impact.
- **M1018 - User Account Management**: restrict cloud permissions to create/modify mirroring sessions.

## 13. Testing & Validation
- Validate detection in a lab:
  - Endpoint: run sanctioned packet capture tooling on a test host and confirm alerts on capture start + pcap creation + privilege use.
  - Cloud: create a test traffic mirroring session and confirm audit-driven alerting on create/modify actions.
  - Network devices: simulate a packet capture command execution in a lab device and validate command logging/alerting.

## 14. References
- MITRE ATT&CK. (n.d.). *Network Sniffing (T1040).* https://attack.mitre.org/techniques/T1040/
- Amazon Web Services. (n.d.). *How Traffic Mirroring works.* https://docs.aws.amazon.com/
- US-CERT. (2018, April 20). *Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices.* https://www.us-cert.gov/

## 15. Notes
- Treat unauthorized cloud traffic mirroring as a high-impact control-plane event; it often provides broad visibility into sensitive traffic with minimal endpoint artifacts.
