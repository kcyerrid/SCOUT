---
entity_type: mitre_technique

technique_id: "T1036"
subtechnique_id: ""
technique_name: "Masquerading"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS
  - Cloud
  - Containers

datasources:
  - File System Monitoring
  - Process Creation
  - Command-Line Parameters
  - Image Load
  - EDR Telemetry

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1564"
  - "T1027"
  - "T1070"
  - "T1218"

detection_priority:
  - Medium
  - High

detection_maturity: ""
threat_score: 4

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - defense-evasion
  - masquerading
  - evasion
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Masquerading (T1036)

## 1. Summary
Masquerading describes adversaries **disguising malicious files, processes, or services as legitimate system or application components** to evade detection. This can involve renaming binaries, altering metadata, mimicking directory structures, or abusing trusted naming conventions.

Attackers use masquerading to:
- Blend malicious artifacts into normal system activity
- Evade signature- and name-based detections
- Trick users and analysts during triage
- Increase dwell time by reducing suspicion

---

## 2. Technical Overview
Masquerading can occur at multiple layers of the operating system and application stack. Adversaries commonly:

- Rename malware to resemble legitimate binaries
- Place malicious files in trusted directories
- Use filenames similar to system processes (e.g., typosquatting)
- Modify metadata (company name, description, icons)
- Masquerade services, scheduled tasks, or registry entries

Key characteristics:
- Malicious content with benign-looking names or paths
- Execution from directories typically associated with trusted software
- Metadata inconsistencies when inspected closely

Indicators include:
- Executables in system directories that do not match known baselines
- Processes with suspicious parent–child relationships despite benign names
- Files with mismatched metadata and behavior

---

## 3. Subtechnique Considerations
T1036 has several subtechniques that address specific masquerading methods (e.g., file name, path, extension). Even without subtechniques, analysts should consider:

- Whether the artifact’s **name, path, and behavior align**
- Whether metadata matches vendor expectations
- Whether execution context is consistent with the purported application

Masquerading is often paired with **Hide Artifacts (T1564)** and **Obfuscation (T1027)**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Renaming malware to resemble common system utilities
- Placing malicious files in application or system folders
- Creating services with names similar to legitimate services
- Using misleading file extensions or icons

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **behavior over naming**:
- Alert on execution of binaries from trusted paths that deviate from baselines
- Detect processes with benign names performing suspicious actions
- Monitor for metadata mismatches (e.g., unsigned binaries in system directories)
- Correlate execution with file origin and creation context

### Data Source Notes
- **File system monitoring**: Detect unexpected file placement
- **Process telemetry**: Identify suspicious behavior regardless of name
- **Image load events**: Identify unsigned or unusual libraries
- **EDR telemetry**: Provide lineage and behavioral context

Common false positives:
- Legitimate third-party software with generic names
- Custom enterprise tooling
- Portable applications

Tuning guidance:
- Maintain allowlists of known-good binaries and paths
- Increase severity when masquerading coincides with other intrusion indicators

---

## 6. Response Guidance
When suspected:
1. Verify file hashes and signatures against known-good sources
2. Inspect metadata and file origin
3. Analyze behavior and process lineage
4. Isolate affected systems if malicious activity is confirmed
5. Expand hunt for similarly named artifacts across the environment

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1564 - Hide Artifacts|T1564]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1027 - Obfuscated Files or Information|T1027]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1070 - Indicator Removal on Host|T1070]]
  - [[20_Entities/07_TTPs/TA0002 - Execution/T1218 - Signed Binary Proxy Execution|T1218]]

---

## 8. SOC Relevance
Masquerading is highly relevant because:
- It undermines name- and path-based detections
- It exploits analyst assumptions during triage
- It is commonly used alongside other evasion techniques

SOC teams should prioritize **behavioral analysis** over artifact naming.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threats
- Ransomware operators
- Commodity malware families seeking longevity

---

## 10. Campaign Usage
Observed in:
- Stealth-focused espionage campaigns
- Ransomware staging and persistence phases
- Intrusions targeting environments with weak application controls

---

## 11. Malware Usage
Associated with:
- Loaders and droppers
- Backdoors and implants
- Post-exploitation frameworks
- LOLBin-abusing malware

---

## 12. Mitigations
Recommended mitigations:
- Enforce application allowlisting
- Validate digital signatures on executables
- Restrict execution from user-writable directories
- Monitor trusted paths for unauthorized file creation

---

## 13. Testing & Validation
Validation approaches:
- Rename benign binaries to mimic system files in lab environments
- Validate alerts on suspicious execution despite benign naming
- Test SOC workflows for masquerading scenarios
- Ensure detections do not rely solely on filenames

---

## 14. References
MITRE ATT&CK. (2025). *Masquerading (T1036)*.  
https://attack.mitre.org/techniques/T1036/

Microsoft. (2024). *Windows Defender Application Control*.  
https://learn.microsoft.com/windows/security/

Elastic Security Labs. (2023). *Detecting masquerading techniques*.  
https://www.elastic.co/security-labs

---

## 15. Notes
- Names and paths lie; behavior tells the truth.
- Masquerading is most effective against static detections.
- Pair behavioral analytics with strong baselining.
