---
entity_type: mitre_technique

technique_id: "T1553"
subtechnique_id: ""
technique_name: "Subvert Trust Controls"

tactic:
  - Defense Evasion

platforms:
  - Windows
  - Linux
  - macOS

datasources:
  - Windows Registry Key Modification
  - File Creation
  - File Modification
  - Process Creation
  - Command-Line Parameters
  - Certificate Authentication
  - Application Log
  - macOS Unified Logs
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
  - "T1140"
  - "T1036"
  - "T1562"
  - "T1552"

detection_priority:
  - High
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - technique
  - defense-evasion
  - trust-controls
  - code-signing
  - certificates
  - motw
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Subvert Trust Controls (T1553)

## 1. Summary
Subvert Trust Controls describes adversaries **undermining mechanisms that warn users about untrusted activity or prevent execution of untrusted programs**. Trust controls may include code signing validation, quarantine or “downloaded from the Internet” markings, and root certificate trust stores. By subverting these controls, adversaries can make malicious content appear legitimate, reduce user prompts, and bypass application control policies. (MITRE ATT&CK, 2025). https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:0]{index=0}

---

## 2. Technical Overview
Operating systems and security products use trust signals to determine whether to allow execution or display warnings. Adversaries may subvert these controls by:
- Abusing or forging **code signing** trust (valid signatures, stolen certificates)
- Tampering with **trust providers** (e.g., Windows SIP/WinVerifyTrust plumbing)
- Installing **root certificates** to expand what the system trusts
- Bypassing **Mark-of-the-Web (MOTW)** and other provenance markers
- Modifying **code signing policies** (e.g., enforcement settings) (MITRE ATT&CK, 2025). https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:1]{index=1}

Typical artifacts include:
- Changes to trust stores / certificate inventories
- Registry modifications impacting signature validation or trust providers
- File extended attribute changes (e.g., removing quarantine/MOTW metadata)
- Policy changes affecting application control enforcement

---

## 3. Subtechnique Considerations
T1553 includes the following subtechniques (MITRE ATT&CK, 2025). https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:2]{index=2}
- **T1553.001** — Gatekeeper Bypass
- **T1553.002** — Code Signing
- **T1553.003** — SIP and Trust Provider Hijacking
- **T1553.004** — Install Root Certificate
- **T1553.005** — Mark-of-the-Web Bypass
- **T1553.006** — Code Signing Policy Modification

Operationally:
- macOS-focused activity often clusters around **Gatekeeper**, notarization/quarantine, and signing controls. :contentReference[oaicite:3]{index=3}  
- Windows-focused activity commonly clusters around **Authenticode**, SIP/trust provider plumbing, root store manipulation, and policy enforcement. :contentReference[oaicite:4]{index=4}

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Using valid or stolen code-signing materials to make malware appear trustworthy
- Manipulating trust provider components so signature checks classify malicious code as trusted
- Installing new root certificates to expand trusted signing chains
- Removing or bypassing download provenance markers so files execute without warnings (MITRE ATT&CK, 2025). https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:5]{index=5}

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **trust-store changes, provenance-marker tampering, and signature-validation anomalies**:
- Alert on **new/modified root or code-signing certificates** outside approved workflows
- Detect **registry/config changes** associated with trust providers or validation behavior
- Monitor for **extended attribute** or MOTW changes on newly downloaded executables/scripts
- Correlate “should have warned/blocked” events with observed execution

### Data Source Notes
MITRE’s detection strategy for T1553 emphasizes correlating certificate, registry, and attribute manipulation with suspicious execution patterns (MITRE ATT&CK, 2025). https://attack.mitre.org/detectionstrategies/DET0452/ :contentReference[oaicite:6]{index=6}

Common false positives:
- Legitimate certificate deployment (enterprise PKI, proxy inspection certs)
- Approved application control or signing policy changes
- Software installers that legitimately adjust trust settings

Tuning guidance:
- Require change-control correlation for trust-store changes
- Raise severity when trust changes closely precede suspicious execution chains

---

## 6. Response Guidance
When suspected:
1. Identify the trust mechanism targeted (certificate store, MOTW/quarantine, trust providers, policy)
2. Capture the changed artifacts (certificates, registry keys, policy objects, extended attributes)
3. Roll back unauthorized changes using known-good baselines
4. Re-scan and hunt for payloads that may have relied on the subverted trust path
5. Rotate credentials and re-issue certificates if signing material compromise is suspected

---

## 7. Related ATT&CK Content
- Technique:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553 - Subvert Trust Controls|T1553]]

- Subtechniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553.001 - Gatekeeper Bypass|T1553.001]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553.002 - Code Signing|T1553.002]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553.003 - SIP and Trust Provider Hijacking|T1553.003]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553.004 - Install Root Certificate|T1553.004]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553.005 - Mark-of-the-Web Bypass|T1553.005]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553.006 - Code Signing Policy Modification|T1553.006]]

- Related techniques (common pairings):
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1140 - Deobfuscate/Decode Files or Information|T1140]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1036 - Masquerading|T1036]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1552 - Unsecured Credentials|T1552]]

---

## 8. SOC Relevance
T1553 matters because it can:
- Turn user prompts and application control into “allow by default”
- Reduce visibility by ensuring payloads execute without expected warnings
- Enable follow-on execution chains that appear legitimate (signed, trusted, or unmarked)

Organizations relying on application control, certificate hygiene, and download provenance should prioritize **continuous auditing of trust settings**. :contentReference[oaicite:7]{index=7}

---

## 9. Threat Actor Usage
Known actor usage exists in public reporting and is enumerated on MITRE’s technique page under procedure examples (MITRE ATT&CK, 2025). https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:8]{index=8}

---

## 10. Campaign Usage
Commonly appears in campaigns where adversaries need to:
- Deliver payloads through user-exposed channels (email/web)
- Bypass application control or reputation systems
- Maintain execution reliability in hardened environments

---

## 11. Malware Usage
Commonly associated with:
- Loaders and droppers seeking “trusted” execution paths
- Signed malware variants or trojanized signed binaries
- Tooling that removes quarantine/MOTW or alters trust stores

---

## 12. Mitigations
Mitigations vary by trust mechanism targeted and include:
- Enforcing application control / execution prevention policies
- Restricting who can install certificates and modify trust settings
- Hardening registry and policy permissions related to trust provider components
- Monitoring certificate store modifications and provenance-marker changes (MITRE ATT&CK, 2025). https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:9]{index=9}

---

## 13. Testing & Validation
Validation approaches:
- Confirm you can detect certificate store changes (system and user stores)
- Validate alerting on trust provider/policy changes (registry/GPO/MDM where applicable)
- Validate that files retain MOTW/quarantine metadata through your common ingress paths
- Confirm detections on “signed-but-suspicious” execution events in high-risk contexts

Include:
- Preconditions: baseline trust settings captured; change auditing enabled
- Required roles/tools: endpoint engineering, PKI/admin, SOC, EDR/SIEM
- Expected outcomes: alerts on unauthorized trust changes and correlated suspicious execution
- Success criteria: reliable detection and rapid rollback capability

---

## 14. References
MITRE ATT&CK. (2025). *Subvert Trust Controls (T1553).* https://attack.mitre.org/techniques/T1553/ :contentReference[oaicite:10]{index=10}

MITRE ATT&CK. (2025). *Detect Subversion of Trust Controls via Certificate, Registry, and Attribute Manipulation (DET0452).* https://attack.mitre.org/detectionstrategies/DET0452/ :contentReference[oaicite:11]{index=11}

MITRE ATT&CK. (2025). *Subvert Trust Controls: Code Signing (T1553.002).* https://attack.mitre.org/techniques/T1553/002/ :contentReference[oaicite:12]{index=12}

MITRE ATT&CK. (2025). *Subvert Trust Controls: Gatekeeper Bypass (T1553.001).* https://attack.mitre.org/techniques/T1553/001/ :contentReference[oaicite:13]{index=13}

MITRE ATT&CK. (2025). *Subvert Trust Controls: SIP and Trust Provider Hijacking (T1553.003).* https://attack.mitre.org/techniques/T1553/003/ :contentReference[oaicite:14]{index=14}

MITRE ATT&CK. (2025). *Subvert Trust Controls: Code Signing Policy Modification (T1553.006).* https://attack.mitre.org/techniques/T1553/006/ :contentReference[oaicite:15]{index=15}

---

## 15. Notes
- Treat trust controls as critical security infrastructure, not “configuration.”
- Baselines + change control are the fastest path to detecting selective trust subversion.
- Pair trust-control detections with high-fidelity execution telemetry for best results.
