---
entity_type: mitre_technique

technique_id: "T1205"
subtechnique_id: ""
technique_name: "Traffic Signaling"

tactic:
  - Defense Evasion
  - Persistence
  - Command and Control
platforms:
  - Linux
  - Network Devices
  - Windows
  - macOS
datasources:
  - Process Creation
  - Network Connection Creation
  - Network Traffic Flow
  - Network Traffic Content
  - Command Execution

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]"
  - "[[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]"
  - "[[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1118 - BUSHWALK|BUSHWALK]]"
  - "[[30_CIPHER/05_Malware/S0220 - Chaos|Chaos]]"
  - "[[30_CIPHER/05_Malware/S1203 - J-magic|J-magic]]"
  - "[[30_CIPHER/05_Malware/S0641 - Kobalos|Kobalos]]"
  - "[[30_CIPHER/05_Malware/S0664 - Pandora|Pandora]]"
  - "[[30_CIPHER/05_Malware/S0587 - Penquin|Penquin]]"
  - "[[30_CIPHER/05_Malware/S1228 - PUBLOAD|PUBLOAD]]"
  - "[[30_CIPHER/05_Malware/S1219 - REPTILE|REPTILE]]"
  - "[[30_CIPHER/05_Malware/S0446 - Ryuk|Ryuk]]"
  - "[[30_CIPHER/05_Malware/S0519 - SYNful Knock|SYNful Knock]]"
  - "[[30_CIPHER/05_Malware/S1239 - TONESHELL|TONESHELL]]"
  - "[[30_CIPHER/05_Malware/S1201 - TRANSLATEXT|TRANSLATEXT]]"
  - "[[30_CIPHER/05_Malware/S0221 - Umbreon|Umbreon]]"
  - "[[30_CIPHER/05_Malware/S0022 - Uroburos|Uroburos]]"
  - "[[30_CIPHER/05_Malware/S0430 - Winnti for Linux|Winnti for Linux]]"
  - "[[30_CIPHER/05_Malware/S1114 - ZIPLINE|ZIPLINE]]"
associated_campaigns:
  - "C0029 - Cutting Edge"
  - "C0056 - RedPenguin"
related_techniques:
  - "T1205.001 - Port Knocking"
  - "T1205.002 - Socket Filters"

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
Traffic Signaling (T1205) hides malicious functionality (persistence/C2 enablement) behind “magic” values or sequences sent over the network. The system behaves normally until it sees the correct trigger (e.g., a port-knock sequence, special flags/strings, or a crafted packet), then it opens a port, activates a backdoor feature, or performs a discrete action.

## 2. Technical Overview
- **Core pattern:** “trigger traffic” → “state change” → “follow-on access”
  - Trigger may be a sequence of failed connections to closed ports, unusual flags, a specific packet payload/token, or “magic bytes.”
  - Response may be:
    - Firewall rule change / ACL enablement
    - Daemon/service activation or new socket bind
    - Backdoor feature activation on an existing port
    - Wake-on-LAN powered-on host becomes reachable
- **Implementation modes (common):**
  - Passive sniffing via packet capture libraries (e.g., `libpcap`/WinPcap/Npcap) or raw sockets.
  - Embedded device/network device signaling to enable management services or backdoor behaviors.

## 3. Subtechnique Considerations
- **T1205.001 Port Knocking:** Sequence-based trigger; defender focus is on closed-port “touch” patterns followed by a new listener/firewall rule and first successful connection.
- **T1205.002 Socket Filters:** Filter/trigger on raw socket or capture stack; defender focus is on packet capture/driver/library usage plus low-volume trigger packet(s) preceding outbound beacon/reverse connection.
- Parent T1205 detections often benefit from **cross-layer correlation** (network telemetry + host changes).

## 4. Procedure Examples
ATT&CK documents traffic signaling usage across malware, campaigns, and groups, including:
- Malware listening for magic packets/strings to activate reverse shells or processing logic (e.g., [[30_CIPHER/05_Malware/S0220 - Chaos|Chaos]], [[30_CIPHER/05_Malware/S1203 - J-magic|J-magic]]).
- Group usage and tool behaviors such as [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]] and [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]] leveraging “magic packet”/tokenized signaling in C2-related behaviors.
- Campaign and incident contexts (e.g., C0029 - Cutting Edge; C0056 - RedPenguin) describing magic sequences enabling backdoor communications.

## 5. Detection Guidance
**Detection objective:** Identify the trigger → response transition that should be rare in legitimate operations.

**Network-centric detections:**
- **Closed-port sequence (“knock”) patterns:**
  - Same source IP touches multiple closed destination ports within a short time window.
  - Followed by a successful connection to a previously closed/newly opened port.
- **Trigger packet anomalies:**
  - Single or low-volume inbound packets with unusual characteristics (flags, payload token, ICMP patterns, or protocol oddities).
  - Trigger packet is quickly followed by:
    - New listener bind
    - Firewall/ACL modification
    - Outbound connection to the trigger origin (reverse connection)

**Host-centric detections (high-signal):**
- **Firewall/ACL changes** shortly after knock/trigger traffic:
  - Windows Firewall with Advanced Security events (rule add/modify/enable)
  - Linux `iptables`/`nftables` changes; macOS PF/socketfilterfw changes
- **New socket binds / listener activation** correlated to knock windows.
- **Packet capture / raw socket enablement**:
  - Loading capture libraries/drivers; starting capture services; processes invoking raw socket APIs.
- **LOLBins & command execution** used to implement response:
  - `netsh`, `powershell`, `iptables`, `nft`, `pfctl`, `systemctl` used shortly after trigger.

**Correlation tips:**
- Build a correlation window (e.g., 60–300s): knock/trigger → firewall/listener change → first successful session.
- Maintain allowlists for:
  - Known management scanners
  - Patch/agent processes that legitimately alter firewall rules
  - Known Wake-on-LAN maintenance windows (if applicable)

### 5.1. Data Source Notes
- **Process Creation:** Identify firewall tools, capture tooling, and new listener processes.
- **Network Connection Creation / Network Traffic Flow:** Identify knock sequences, first successful connect, and follow-on sessions.
- **Network Traffic Content:** Useful when trigger packets are identifiable by payload token or unique byte patterns (where permitted).
- **Command Execution:** Spot scripted rule changes and service starts tied to the trigger window.

## 6. Response Guidance
1. **Containment**
   - Block the triggering source(s) and associated destinations temporarily.
   - Quarantine hosts showing correlated knock→state-change behaviors.
2. **Triage**
   - Determine what changed: firewall rules, services, sockets, drivers/modules.
   - Identify the responsible process tree and any persistence tied to it.
3. **Eradication**
   - Remove unauthorized listeners/backdoors and revert firewall/ACL changes.
   - Remove capture/raw-socket tooling installed outside policy.
4. **Recovery**
   - Re-enable legitimate services with verified configs; validate network device integrity if implicated.
5. **Hardening**
   - Restrict raw socket / packet capture capability to approved admins/tools.
   - Add egress controls for suspicious reverse connections after trigger traffic.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1205 - Traffic Signaling|T1205]]
- [[20_Entities/07_TTPs/TA0003 - Persistence/T1205 - Traffic Signaling|T1205]]
- [[20_Entities/07_TTPs/TA0011 - Command and Control/T1205 - Traffic Signaling|T1205]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1205.001 - Port Knocking|T1205.001]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1205.002 - Socket Filters|T1205.002]]

## 8. SOC Relevance
- **High signal** when network anomalies correlate with host configuration changes.
- Particularly relevant for:
  - Stealthy backdoors on Linux/network devices
  - Environments with limited EDR coverage on appliances
  - Remote access edge devices and management planes

## 9. Threat Actor Usage
ATT&CK documents usage by, at minimum:
- [[30_CIPHER/03_Threat_Actors/G0094 - Kimsuky|Kimsuky]]
- [[30_CIPHER/03_Threat_Actors/G0129 - Mustang Panda|Mustang Panda]]
- [[30_CIPHER/03_Threat_Actors/G1048 - UNC3886|UNC3886]]

## 10. Campaign Usage
- C0029 - Cutting Edge
- C0056 - RedPenguin

## 11. Malware Usage
Examples documented in ATT&CK include:
- [[30_CIPHER/05_Malware/S1118 - BUSHWALK|BUSHWALK]]
- [[30_CIPHER/05_Malware/S0220 - Chaos|Chaos]]
- [[30_CIPHER/05_Malware/S1203 - J-magic|J-magic]]
- [[30_CIPHER/05_Malware/S0641 - Kobalos|Kobalos]]
- [[30_CIPHER/05_Malware/S0664 - Pandora|Pandora]]
- [[30_CIPHER/05_Malware/S0587 - Penquin|Penquin]]
- [[30_CIPHER/05_Malware/S1228 - PUBLOAD|PUBLOAD]]
- [[30_CIPHER/05_Malware/S1219 - REPTILE|REPTILE]]
- [[30_CIPHER/05_Malware/S0446 - Ryuk|Ryuk]]
- [[30_CIPHER/05_Malware/S0519 - SYNful Knock|SYNful Knock]]
- [[30_CIPHER/05_Malware/S1239 - TONESHELL|TONESHELL]]
- [[30_CIPHER/05_Malware/S1201 - TRANSLATEXT|TRANSLATEXT]]
- [[30_CIPHER/05_Malware/S0221 - Umbreon|Umbreon]]
- [[30_CIPHER/05_Malware/S0022 - Uroburos|Uroburos]]
- [[30_CIPHER/05_Malware/S0430 - Winnti for Linux|Winnti for Linux]]
- [[30_CIPHER/05_Malware/S1114 - ZIPLINE|ZIPLINE]]

## 12. Mitigations
- **Disable or Remove Feature or Program:** Disable Wake-on-LAN where not required.
- **Filter Network Traffic:** Use stateful firewalling and segmentation to reduce viable signaling paths; restrict inbound management access.
- **Policy/Control (defender practice):** Limit packet capture/raw socket permissions; monitor for unauthorized drivers/modules.

## 13. Testing & Validation
- Validate detections with authorized lab scenarios:
  - Generate a benign “closed-port sequence” from a test host and verify network telemetry captures it.
  - Simulate a firewall rule change and verify correlation to prior network events.
  - On Linux/macOS testbeds, validate visibility into `socket/bind` and firewall command execution.
  - Confirm alerting differentiates common scanners from repeatable knock-like sequences.

## 14. References
1. MITRE ATT&CK. (2025). *Traffic Signaling (T1205).* Retrieved 2026-01-01, from https://attack.mitre.org/techniques/T1205/ :contentReference[oaicite:4]{index=4}  
2. MITRE ATT&CK. (2025). *Traffic Signaling (Port-knock / magic-packet → firewall or service activation) – T1205 (DET0524).* Retrieved 2026-01-01, from https://attack.mitre.org/detectionstrategies/DET0524/ :contentReference[oaicite:5]{index=5}  
3. Mandiant. (2024). *Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts.* https://www.mandiant.com/ :contentReference[oaicite:6]{index=6}  

## 15. Notes
- Treat “knock/trigger packet + immediate config change” as the primary analytic anchor.
- For appliances/network devices, prioritize centralized logs and passive network monitoring due to limited endpoint visibility.
