---
entity_type: mitre_technique
technique_id: T1221
subtechnique_id: ""
technique_name: Template Injection
tactic:
  - Defense Evasion
platforms:
  - Windows
datasources:
  - Process Creation
  - Network Connection Creation
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]"
  - "[[30_CIPHER/03_Threat_Actors/G0142 - Confucius|Confucius]]"
  - "[[G0079 - DarkHydrus|DarkHydrus]]"
  - "[[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly|Dragonfly]]"
  - "[[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G0100 - Inception|Inception]]"
  - "[[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]"
  - "[[30_CIPHER/03_Threat_Actors/G0081 - Tropic Trooper|Tropic Trooper]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]]"
  - "[[30_CIPHER/05_Malware/S0670 - WarzoneRAT|WarzoneRAT]]"
associated_campaigns:
  - C0001 - Frankenstein
  - C0022 - Operation Dream Job
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
Template Injection (T1221) is the abuse of document template references (e.g., Office Open XML template pointers or RTF template control words) to fetch remote content at document open-time. This can **bypass static document controls** (no embedded macro/script until after retrieval) and may also be used to **trigger forced authentication** via SMB/HTTP(S) template URLs.

## 2. Technical Overview
- **Core behavior:** A document contains (or is modified to contain) a template reference that causes the application (commonly Office) to retrieve a remote template/resource during rendering.
- **Why it works:** Template resolution is a legitimate feature; adversaries leverage it to:
  - Pull down a malicious template (e.g., DOTM/remote template) or secondary payload.
  - Coerce outbound authentication attempts to attacker-controlled resources.
- **Common touchpoints (defender view):**
  - Office/document viewer process makes **network connection(s)** shortly after a document open event.
  - Follow-on **child process creation** (e.g., scripting engine or LOLBin) may occur if the retrieved content executes or triggers secondary stages.

## 3. Subtechnique Considerations
- No sub-techniques defined for T1221.

## 4. Procedure Examples
Examples documented in ATT&CK include:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]] using weaponized Word documents abusing remote templates to retrieve malicious macro content.
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]] using DOCX/RTF template injection to download malicious payloads and inject remote templates/macros into documents already present on systems.
- [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]] (via campaign reporting) using DOCX to retrieve malicious document templates/DOTM.
- Malware examples include [[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]] and [[30_CIPHER/05_Malware/S0670 - WarzoneRAT|WarzoneRAT]] leveraging template-based delivery chains.

## 5. Detection Guidance
High-signal detection typically requires correlating **document open → outbound connection(s) → suspicious child process / content execution**.

**Behavioral detections (recommended):**
- **Office / document viewer outbound network**:
  - Parent process: `WINWORD.EXE`, `EXCEL.EXE`, `POWERPNT.EXE`, and other viewers.
  - Destination characteristics:
    - External domains/IPs not typical for the user/org.
    - Direct-to-IP, newly registered domains, unusual TLDs, or enterprise-unapproved file-sharing/CDN endpoints.
  - Timing: network connection within a short window after document open.
- **Document-spawned process tree anomalies**:
  - Office spawning `powershell.exe`, `cmd.exe`, `rundll32.exe`, `regsvr32.exe`, `mshta.exe`, `wscript.exe`, `cscript.exe`, `curl.exe`, `bitsadmin.exe`, `certutil.exe`.
  - Office spawning browser processes with suspicious command lines.
- **Forced authentication indicators**:
  - Office initiating outbound connections to UNC paths or SMB endpoints.
  - Repeated authentication attempts following document open.

**Tuning/allowlisting guidance:**
- Allowlist known corporate template servers and sanctioned O365/SharePoint patterns (careful: attackers can abuse compromised/similar infra).
- Baseline normal Office outbound patterns per business unit (templates, add-ins, collaboration tools).

### 5.1. Data Source Notes
- **Process Creation:** Needed to detect suspicious Office child processes and LOLBin execution chains.
- **Network Connection Creation:** Needed to observe Office/viewer outbound connections (including destination, port, and timing correlation).

## 6. Response Guidance
1. **Containment**
   - Quarantine the document and isolate affected endpoints (especially if child process execution observed).
   - Block identified IOCs (domains/IPs/URLs) at proxy/DNS/firewall.
2. **Triage & Scope**
   - Identify recipients (email logs, collaboration shares) and determine who opened the file.
   - Hunt for similar documents (same hash, filename, or structural markers) across mailboxes and shares.
3. **Eradication**
   - Remove persistence or secondary payloads if present (endpoint remediation).
   - Reset credentials if forced-authentication evidence exists (focus on accounts that attempted outbound auth).
4. **Recovery**
   - Reinstate clean templates and validate Office policy baselines.
5. **Post-incident hardening**
   - Strengthen egress controls for Office processes; implement risk-based blocks for SMB egress.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1221 - Template Injection|T1221]]

## 8. SOC Relevance
- **Alert candidates:** Office → external network + suspicious child process; Office → SMB/UNC egress; anomalous template fetches.
- **Why SOCs care:** This is a frequent “macro-less” delivery pattern that can defeat naive attachment scanning and increases credential exposure risk.

## 9. Threat Actor Usage
ATT&CK reports usage by, at minimum:
- [[30_CIPHER/03_Threat_Actors/G0007 - APT28|APT28]]
- [[30_CIPHER/03_Threat_Actors/G0142 - Confucius|Confucius]]
- [[G0079 - DarkHydrus|DarkHydrus]]
- [[30_CIPHER/03_Threat_Actors/G0035 - Dragonfly|Dragonfly]]
- [[30_CIPHER/03_Threat_Actors/G0047 - Gamaredon Group|Gamaredon Group]]
- [[30_CIPHER/03_Threat_Actors/G0100 - Inception|Inception]]
- [[30_CIPHER/03_Threat_Actors/G0032 - Lazarus Group|Lazarus Group]]
- [[30_CIPHER/03_Threat_Actors/G0081 - Tropic Trooper|Tropic Trooper]]

## 10. Campaign Usage
- C0001 - Frankenstein
- C0022 - Operation Dream Job

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0631 - Chaes|Chaes]]
- [[30_CIPHER/05_Malware/S0670 - WarzoneRAT|WarzoneRAT]]

## 12. Mitigations
- **Antivirus/Antimalware:** Use detonation/sandboxing and layered scanning to observe runtime template fetch behavior.
- **Network Intrusion Prevention:** Detect/block suspicious template retrieval patterns and known-bad destinations.
- **Disable or Remove Feature or Program:** Harden Office macro/active content settings where appropriate (note: may not address forced-authentication use cases).
- **User Training:** Reduce likelihood of opening malicious documents; emphasize “unexpected document asks to enable content” patterns and suspicious senders.

## 13. Testing & Validation
- Build a benign test plan that verifies:
  - Office outbound template fetches are logged and correlated to document open events.
  - Alerts trigger when Office spawns high-risk children or performs SMB egress.
- Validate detections against:
  - Simulated Office process opening a document followed by controlled outbound HTTP(s) connection (to an internal test server).
  - Controlled generation of process-tree anomalies (Office → PowerShell) in a lab with proper authorization.

## 14. References
1. MITRE ATT&CK. (2025). *Template Injection (T1221).* Retrieved 2026-01-01, from https://attack.mitre.org/techniques/T1221/ :contentReference[oaicite:0]{index=0}  
2. MITRE ATT&CK. (2025). *Template Injection Detection - Windows (DET0566).* Retrieved 2026-01-01, from https://attack.mitre.org/detectionstrategies/DET0566/ :contentReference[oaicite:1]{index=1}  
3. Raggi, M. (2021, December 1). *Injection is the New Black: Novel RTF Template Inject Technique Poised for Widespread Adoption Beyond APT Actors.* Proofpoint. https://www.proofpoint.com/ :contentReference[oaicite:2]{index=2}  
4. Microsoft. (2014, July 9). *Introducing the Office (2007) Open XML File Formats.* https://docs.microsoft.com/ :contentReference[oaicite:3]{index=3}  

## 15. Notes
- Prioritize **egress control + process-tree correlation**; template injection is often only visible at runtime.
- Treat Office-originated SMB egress as high-risk, especially when tied to document open events.
