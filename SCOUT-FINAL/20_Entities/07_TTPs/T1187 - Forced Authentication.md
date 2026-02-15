---
entity_type: mitre_technique
technique_id: T1187
subtechnique_id: ""
technique_name: Forced Authentication
tactic:
  - Credential Access
platforms:
  - Windows
datasources: []
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[G0079 - DarkHydrus|G0079]]"
  - "[[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly|G0035]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0634 - EnvyScout|S0634]]"
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
  - credential-access
  - ntlm
  - smb
  - webdav
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Forced Authentication (T1187) describes adversaries coercing a Windows host/user into automatically attempting authentication (commonly over SMB/WebDAV), allowing the adversary to capture credential material such as NTLM challenge-response hashes for offline cracking or relay attacks.

## 2. Technical Overview
Common coercion vectors include:
- **Lure files** that reference attacker-controlled remote resources (e.g., shortcut/icon resources, shell navigation artifacts, or document templates) that trigger Windows to attempt SMB/WebDAV authentication when rendered/opened.
- **Protocol/feature abuse** that forces a host to authenticate to a remote system (e.g., coercion paths leveraging EFSRPC interfaces).

Defender-relevant signals:
- Outbound connections to untrusted destinations on **SMB ports (445/139)** or WebDAV over **80/443** initiated by user workstations.
- Authentication attempts to **rare external hosts** shortly after a user interacts with a file (open/render/browse).
- Repeated authentication attempts across multiple hosts/users to the same destination (campaign-like harvesting).

## 3. Subtechnique Considerations
No sub-techniques are defined for this technique.

## 4. Procedure Examples
Observed usage examples include:
- [[G0079 - DarkHydrus|G0079]] using Template Injection to launch credential prompts and capture credentials.
- [[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly|G0035]] gathering hashed credentials over SMB using spearphishing attachments with external resource links and modifying LNK icon resources.
- [[30_CIPHER/05_Malware/S0634 - EnvyScout|S0634]] using protocol handlers to coerce systems into sending NTLMv2 responses to attacker infrastructure.

## 5. Detection Guidance
Effective detection is correlation-driven: **lure → access/render → outbound auth**.

1. **Outbound NTLM/SMB/WebDAV to untrusted destinations**
   - Alert on egress SMB (445/139) from endpoints to the internet or non-corporate networks.
   - Alert on WebDAV patterns to rare destinations following document interaction.
2. **Lure artifact identification**
   - Detect creation/modification of LNK/SCF-like artifacts (and similar shell-visible items) referencing remote UNC paths or external resources.
   - Detect Office/document viewer processes initiating network connections to remote template/resources that then lead to authentication attempts.
3. **Repetition & targeting patterns**
   - Same destination contacted by many hosts (hash harvesting server).
   - Privileged workstations or specific user groups targeted disproportionately.
4. **Follow-on indicators**
   - Subsequent internal authentication anomalies consistent with relay activity, lateral movement, or abnormal access using newly cracked/relayed credentials.

### 5.1. Data Source Notes
Telemetry that improves confidence:
- **Network controls**: firewall/proxy logs for outbound SMB/WebDAV; DNS resolution for attacker hosts.
- **Windows event logs**: authentication events (NTLM), network connection logs if available, file creation logs for lure artifacts (where enabled).
- **EDR**: file creation/modification visibility (LNK/SCF/doc templates), process-to-network telemetry (winword.exe/explorer.exe → outbound), and script/tool execution related to lure staging.

## 6. Response Guidance
1. **Containment**
   - Block outbound SMB (445/139) and tightly control WebDAV egress; isolate affected hosts.
   - Identify and remove lure artifacts from user-accessible locations and shared drives.
2. **Credential actions**
   - Assume credential exposure for affected users; reset passwords and evaluate MFA coverage.
   - If NTLM relay is suspected, prioritize disabling/restricting NTLM where feasible and enforce signing/channel binding controls per environment guidance.
3. **Threat hunting**
   - Hunt for additional lure artifacts and outbound authentication attempts across the fleet.
   - Check for evidence of relay/follow-on access from compromised credentials.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1187 - Forced Authentication|T1187]]
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1221 - Template Injection|T1221]]
- [[20_Entities/07_TTPs/TA0006 - Credential Access/T1110 - Brute Force|T1110]]

## 8. SOC Relevance
- Strong “tripwire” potential: outbound SMB/WebDAV auth attempts are often rare and high-signal.
- Supports rapid containment via network control changes.
- Frequently precedes downstream compromise via cracked hashes or relay-based lateral movement.

## 9. Threat Actor Usage
- [[G0079 - DarkHydrus|G0079]]: leveraged template injection–style lures to capture credentials.
- [[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly|G0035]]: harvested hashes over SMB using external resource links and icon-resource manipulation.

## 10. Campaign Usage
- No campaign entries were listed in the canonical procedure examples for this technique at time of writing.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0634 - EnvyScout|S0634]]: coerced NTLMv2 authentication responses to attacker infrastructure.

## 12. Mitigations
- **M1037 - Filter Network Traffic**: block/egress-filter SMB and tightly restrict WebDAV to approved destinations only.
- **M1027 - Password Policies**: strong passwords reduce the feasibility of cracking obtained hashes (does not address relay).

## 13. Testing & Validation
- Validate detections safely:
  - Confirm your environment generates alerts for outbound SMB/WebDAV authentication attempts to non-approved destinations.
  - Validate that lure artifact creation in user-writable locations is logged and searchable.
- Reference frameworks:
  - Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
  - Sigma rules: https://github.com/SigmaHQ/sigma

## 14. References
- MITRE ATT&CK. (n.d.). *Forced Authentication (T1187)*. MITRE ATT&CK. https://attack.mitre.org/techniques/T1187/
- Condon, C. (2022, April 24). *PetitPotam: Novel Attack Chain Can Fully Compromise Windows Domains*. Rapid7. https://www.rapid7.com/blog/post/2022/04/24/petitpotam-novel-attack-chain-can-fully-compromise-windows-domains/
- US-CERT. (2017, October 20). *Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors*. https://www.cisa.gov/news-events/alerts/ta17-293a
- US-CERT. (2018, March 16). *Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors*. https://www.cisa.gov/news-events/alerts/ta18-074a
- Microsoft Threat Intelligence. (2021, May 28). *Breaking down NOBELIUM’s latest early-stage toolset*. Microsoft. https://www.microsoft.com/en-us/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/
- Stevens, D. (2017, November 13). *WebDAV Traffic To Malicious Sites*. Didier Stevens. https://blog.didierstevens.com/2017/11/13/webdav-traffic-to-malicious-sites/

## 15. Notes
- Treat any **outbound SMB authentication attempt** from user endpoints as an escalation-worthy event unless explicitly allowlisted.
- Correlate **file render events** (Explorer/Office) with **network auth attempts** to reduce false positives and improve triage speed.
