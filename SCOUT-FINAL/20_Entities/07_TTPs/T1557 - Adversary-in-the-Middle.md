---
entity_type: mitre_technique

technique_id: "T1557"
subtechnique_id: ""
technique_name: "Adversary-in-the-Middle"

tactic:
  - Credential Access
  - Collection
platforms:
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
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]"
  - "[[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]"
  - "[[30_CIPHER/03_Threat_Actors/G1041 - Sea Turtle|Sea Turtle]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0281 - Dok|Dok]]"
  - "[[30_CIPHER/05_Malware/S1188 - Line Runner|Line Runner]]"
  - "[[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]"
associated_campaigns:
  - "C0046 - ArcaneDoor"
related_techniques: []

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

created: 2026-01-06
updated: 2026-01-06

contributors:
  - "Daniil Yugoslavskiy (@yugoslavskiy), Atomic Threat Coverage project"
  - "Mayuresh Dani, Qualys"
  - "NEC"
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
Adversary-in-the-Middle (AiTM) describes attempts to position an adversary-controlled system or component between two or more communicating parties in order to intercept, observe, modify, or redirect traffic. AiTM commonly enables credential interception, session hijacking, and downstream payload delivery through redirection.

## 2. Technical Overview
AiTM can be established by abusing network or identity trust boundaries:
- **Traffic interception/relaying:** The adversary coerces endpoints into routing traffic through an attacker-controlled hop (e.g., rogue gateway/DNS, ARP poisoning, rogue DHCP, rogue Wi-Fi AP).
- **Credential/session interception:** Once in-path, the adversary may capture credentials, tokens, or cookies and/or replay them against legitimate services.
- **Manipulation/redirection:** DNS/gateway changes, captive portal hijacking, or TLS downgrade patterns can redirect users to controlled infrastructure, deliver payloads, or degrade encryption.

MITRE detection guidance highlights correlation of **network/configuration anomalies** with **subsequent unusual network flows or authentication events**, as well as host configuration changes (Windows registry/network settings, Linux/macOS resolver/hosts files) and device configuration integrity issues.

## 3. Subtechnique Considerations
T1557 is a parent technique with distinct subtechniques that produce different telemetry:
- **T1557.001 (LLMNR/NBT-NS Poisoning and SMB Relay):** Name-resolution poisoning and NTLM relay patterns on Windows networks.
- **T1557.002 (ARP Cache Poisoning):** ARP cache changes, gratuitous ARP floods, multiple IPs resolving to one MAC, endpoint ARP table churn.
- **T1557.003 (DHCP Spoofing):** Rogue DHCP OFFER/ACK, unexpected DNS/gateway assignments, DHCP exhaustion warnings, competing DHCP servers.
- **T1557.004 (Evil Twin):** Rogue Wi-Fi APs (same SSID, different BSSID/MAC), captive portal redirection, anomalous wireless authentication behavior.

Design detections per subtechnique, then roll up to T1557 coverage as a correlation layer.

## 4. Procedure Examples
Documented examples of T1557 usage include:
- **C0046 ArcaneDoor:** Intercepted HTTP traffic to identify/parse C2-related information.
- **S0281 Dok:** Proxied HTTP(S) traffic to monitor/alter victim web traffic.
- **[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]:** Used modified proxy tooling to examine victim web traffic.
- **[[30_CIPHER/05_Malware/S1188 - Line Runner|Line Runner]]:** Intercepted HTTP requests on Cisco ASA and conditionally executed payload logic.
- **[[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]:** Leveraged captive portal hijack to redirect victims to a download prompt.
- **[[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]:** Established an alternative RPC channel to intercept credential material during logon flows.
- **[[30_CIPHER/03_Threat_Actors/G1041 - Sea Turtle|Sea Turtle]]:** Modified DNS records to redirect victim traffic for credential capture.

## 5. Detection Guidance
Prioritize detections that combine **network-plane anomalies** with **host/network configuration changes**:
- **DNS anomalies:** Unauthorized resolver changes (DHCP-assigned DNS changes, local resolver configuration edits), suspicious DNS record changes at providers, sudden shift to uncommon resolvers.
- **ARP anomalies:** Repeated unsolicited ARP replies, IP↔MAC inconsistencies, multiple IPs mapping to one MAC, rapid ARP table churn on endpoints.
- **TLS downgrade indicators:** Unexpected protocol/cipher downgrades, inconsistent certificate chains, certificate trust store changes preceding interception-like flows.
- **Endpoint configuration tampering:**  
  - Linux: unauthorized edits to `/etc/hosts`, `/etc/resolv.conf` with subsequent unexpected sessions.  
  - Windows: registry/network configuration changes correlated with abnormal network flows/auth events.  
  - macOS: unexpected configuration profile or certificate trust changes paired with ARP/DNS anomalies.
- **Network device integrity:** Routing/DNS/SSL settings changes on network devices; configuration integrity failures preceding traffic redirection.

### Data Source Notes
Use the technique’s detection strategies as a guide for telemetry requirements:
- **Network telemetry:** DNS/ARP/DHCP traffic, TLS handshake metadata, proxy/captive portal redirects.
- **Endpoint telemetry:** file modification auditing for resolver/hosts files, registry/network setting auditing, certificate store changes, process/service creation that follows interception setup.
- **Network device telemetry:** configuration change logs, routing table changes, DHCP snooping/DAI events, WIPS alerts (wireless).

## 6. Response Guidance
1. **Scope the interception surface:** Identify impacted VLANs/SSIDs/subnets, gateway/DNS/DHCP servers in use, and any recent changes.
2. **Contain the path:**  
   - Quarantine suspected rogue devices (APs, DHCP servers, poisoning sources).  
   - Enforce known-good DNS/gateway/DHCP infrastructure; rotate credentials/tokens if interception suspected.
3. **Validate trust anchors:** Check certificate stores/trust settings and VPN/proxy configurations; remediate unauthorized profiles and certs.
4. **Hunt for follow-on:** Look for credential replay, lateral movement, new persistence, and payload delivery originating from redirected sessions.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1557 - Adversary-in-the-Middle|T1557]]
- [[20_Entities/07_TTPs/TA0009 - Collection/T1557 - Adversary-in-the-Middle|T1557]]

Subtechniques:
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay|T1557.001]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1557.002 - Adversary-in-the-Middle: ARP Cache Poisoning|T1557.002]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1557.003 - Adversary-in-the-Middle: DHCP Spoofing|T1557.003]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1557.004 - Adversary-in-the-Middle: Evil Twin|T1557.004]]

## 8. SOC Relevance
**High signal** when paired indicators occur:
- Resolver/gateway changes + new suspicious outbound sessions
- ARP/DHCP anomalies + authentication spikes or new SMB/LDAP activity
- Certificate errors + new proxy/captive portal redirects
- Network device config changes + route/DNS manipulation

Recommended operationalization:
- Baseline known-good DNS/DHCP/gateway and certificate trust, alert on drift.
- Build correlation rules that tie config drift → unusual auth or traffic destinations.

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]: proxy-based interception of web traffic.
- [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]: captive portal hijack leading to malicious download prompt.
- [[30_CIPHER/03_Threat_Actors/G1041 - Sea Turtle|Sea Turtle]]: DNS record manipulation at providers to redirect traffic.

## 10. Campaign Usage
- C0046 - ArcaneDoor: traffic interception to parse victim device C2-related information.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0281 - Dok|Dok]]: proxies web traffic for monitoring/alteration.
- [[30_CIPHER/05_Malware/S1188 - Line Runner|Line Runner]]: intercepts HTTP requests and conditionally executes payload logic.
- [[30_CIPHER/05_Malware/S1131 - NPPSPY|NPPSPY]]: intercepts/redirects logon information via alternate RPC channel.

## 12. Mitigations
- **M1042 Disable or Remove Feature or Program:** Disable legacy protocols that facilitate interception where feasible.
- **M1041 Encrypt Sensitive Information:** Enforce strong encryption and modern authentication (e.g., TLS best practices, Kerberos).
- **M1037 Filter Network Traffic:** Block unnecessary legacy protocols and limit exposure of interception-enabling traffic.
- **M1035 Limit Access to Resource Over Network:** Restrict access to network infrastructure/resources that can reshape traffic.
- **M1031 Network Intrusion Prevention:** Deploy NIDS/NIPS to detect AiTM patterns at the network level.
- **M1030 Network Segmentation:** Segment networks to limit AiTM blast radius.
- **M1017 User Training:** Train users to recognize certificate errors and suspicious Wi-Fi/captive portal behavior.

## 13. Testing & Validation
- Validate detection strategies with controlled lab simulations (authorized only):
  - DNS/ARP/DHCP anomaly generation and correlation with host config-change alerts.
  - TLS downgrade/cert-trust change detection using test certificates and proxy scenarios.
- Use defensive emulation frameworks (e.g., Atomic testing concepts) to verify:
  - Alert fidelity (low false positives on benign DHCP renewals/ARP changes)
  - Correlation quality (config drift → suspicious auth/network behavior)
  - Coverage across OS platforms and network devices.

## 14. References
- MITRE ATT&CK. (n.d.). *Adversary-in-the-Middle (T1557).* https://attack.mitre.org/techniques/T1557/
- Rapid7. (n.d.). *Man-in-the-Middle (MITM) Attacks.* https://www.rapid7.com/fundamentals/man-in-the-middle-attacks/
- Microsoft Incident Response. (2022, November 16). *Token tactics: How to prevent, detect, and respond to cloud token theft.* https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/
- Volexity Threat Research. (2022, June 15). *DriftingCloud: Zero-Day Sophos Firewall Exploitation and an Insidious Breach.* https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/
- Cisco Talos. (2024). *ArcaneDoor blog coverage (traffic interception / Line Runner).* https://blog.talosintelligence.com/

## 15. Notes
- 
