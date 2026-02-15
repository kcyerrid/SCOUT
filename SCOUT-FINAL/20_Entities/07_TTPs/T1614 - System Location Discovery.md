---
entity_type: mitre_technique

technique_id: "T1614"
subtechnique_id: ""
technique_name: "System Location Discovery"

tactic:
  - TA0007 - Discovery
platforms:
  - IaaS
  - Linux
  - Windows
  - macOS
datasources: []

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G1008 - SideCopy|SideCopy]]"
  - "[[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S1025 - Amadey|Amadey]]"
  - "[[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]"
  - "[[30_CIPHER/05_Malware/S1138 - Gootloader|Gootloader]]"
  - "[[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]]"
associated_campaigns: []
related_techniques:
  - "T1614.001"

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

# T1614 - System Location Discovery

## 1. Summary
Adversaries infer a victim system’s **geographical location** to gate execution (e.g., avoid certain regions), tailor targeting, or enrich victim profiling. Location inference may rely on locale/timezone/language settings, IP-based geolocation, or cloud region/availability zone metadata.

## 2. Technical Overview
Common location inference methods:
- **Host configuration checks**:
  - locale, timezone, keyboard layout, language settings
  - OS APIs that return locale/timezone metadata
- **IP-based geolocation**:
  - external lookup services or locally embedded geolocation logic
- **Cloud context checks (IaaS)**:
  - querying instance metadata services to infer region/availability zone

Signals often occur early in execution as “environment gating,” and may be repeated before high-risk actions.

## 3. Subtechnique Considerations
- **T1614.001 (System Language Discovery)** is used when the activity specifically targets system language as the location signal.
- Parent **T1614** applies when the discovery includes broader signals (timezone, keyboard layout, IP geolocation, cloud AZ/region).

## 4. Procedure Examples
MITRE procedure examples include:
- Malware families using locale/geolocation to gate execution or tailor behavior, including [[30_CIPHER/05_Malware/S1025 - Amadey|Amadey]], [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]], [[30_CIPHER/05_Malware/S1138 - Gootloader|Gootloader]], and [[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]].
- Threat actors such as [[30_CIPHER/03_Threat_Actors/G1008 - SideCopy|SideCopy]] and [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]] performing location discovery behaviors (per the technique page).

## 5. Detection Guidance
This technique is less common in benign enterprise workflows; alert fidelity improves when you focus on **unusual process context**.

High-signal patterns:
- Unknown/rare binaries or scripts calling locale/timezone APIs shortly after execution.
- Command execution that reads locale/timezone configuration from unusual parent processes.
- Requests to **cloud instance metadata services** from workloads/principals that do not normally perform management discovery.

Analytics ideas:
- Detect locale/timezone query APIs or configuration reads by:
  - unsigned binaries
  - office/script-originated chains
  - newly created scheduled tasks/services
- Flag outbound requests consistent with IP geolocation enrichment when initiated by suspicious processes.
- Cloud: alert on IMDS/Azure metadata access patterns that appear atypical for the workload and are followed by additional discovery or C2.

### Data Source Notes
Useful telemetry:
- **Endpoint**: process creation, command line, parent/child lineage; API telemetry (EDR) for locale/timezone calls where available.
- **Linux/macOS**: shell history/process exec; reads of locale/timezone files/commands.
- **Cloud**: VPC/flow logs + workload telemetry for metadata service access; cloud audit logs for identity context and related API usage.

## 6. Response Guidance
1. **Triage process lineage**: confirm origin (download, email, script).
2. **Assess gating intent**: look for conditional branches in script/executable behavior (e.g., “do nothing” outcomes).
3. **Pivot to next actions**: if location checks succeed, watch for payload deployment, persistence, or data access.
4. **Contain**: isolate the host/workload if the check is linked to suspicious execution.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1614 - System Location Discovery|T1614]]
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1614.001 - System Location Discovery: System Language Discovery|T1614.001]]

## 8. SOC Relevance
- Useful for identifying malware “environment gating” and region-based targeting.
- Especially relevant for catching loader/infostealer families that avoid specific geographies.

## 9. Threat Actor Usage
Examples included on the technique page:
- [[30_CIPHER/03_Threat_Actors/G1008 - SideCopy|SideCopy]]
- [[30_CIPHER/03_Threat_Actors/G1017 - Volt Typhoon|Volt Typhoon]]

## 10. Campaign Usage
- Not pinned here; correlate to your incident timeline and malware family behaviors.

## 11. Malware Usage
Examples included on the technique page:
- [[30_CIPHER/05_Malware/S1025 - Amadey|Amadey]]
- [[30_CIPHER/05_Malware/S1111 - DarkGate|DarkGate]]
- [[30_CIPHER/05_Malware/S1138 - Gootloader|Gootloader]]
- [[30_CIPHER/05_Malware/S1240 - RedLine Stealer|RedLine Stealer]]

## 12. Mitigations
Preventive controls are limited; emphasize:
- Strong execution prevention (application control, macro/script restrictions)
- EDR visibility into process + API behavior
- Cloud workload hardening and monitoring for metadata service misuse

## 13. Testing & Validation
- Validate detections by simulating:
  - locale/timezone checks via benign scripts
  - metadata service access from a test workload that typically would not query IMDS
- Confirm tuning differentiates:
  - legitimate system configuration utilities vs suspicious binaries/scripts

## 14. References
- MITRE ATT&CK. (n.d.). *System Location Discovery (T1614).* https://attack.mitre.org/techniques/T1614/
- MITRE ATT&CK. (n.d.). *Detection Strategy for System Location Discovery (DET0043).* https://attack.mitre.org/detectionstrategies/DET0043/
- Amazon. (n.d.). *Instance identity documents (IMDS).* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html

## 15. Notes
- Location discovery is often a “quiet gate” step—combine weak single signals into a strong chain with execution origin and follow-on activity.
