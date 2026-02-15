---
entity_type: mitre_technique

technique_id: "T1601"
subtechnique_id: ""
technique_name: "Modify System Image"

tactic:
  - Defense Evasion
  - Persistence

platforms:
  - Windows
  - Linux
  - macOS
  - Network
  - Cloud

datasources:
  - Image Creation Logs
  - Boot Integrity Monitoring
  - Firmware Logs
  - OS Installation Logs
  - File Integrity Monitoring

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1542"
  - "T1553"
  - "T1070"
  - "T1562"

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
  - defense-evasion
  - persistence
  - image
  - boot
  - integrity
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Modify System Image (T1601)

## 1. Summary
Modify System Image describes adversaries **altering system images used to deploy or boot operating systems**, enabling stealthy persistence, defense evasion, or pre-compromise of future systems. Modified images can distribute malicious artifacts at scale and survive reinstallation or recovery actions.

Attackers use this technique to:
- Establish long-lived, stealthy persistence
- Pre-compromise systems before deployment
- Bypass endpoint security controls
- Undermine trust in system recovery mechanisms

---

## 2. Technical Overview
System images include OS installation media, virtual machine templates, golden images, firmware-backed images, and container base images. Adversaries abuse these by:

- Injecting malicious binaries, scripts, or services
- Modifying startup configurations or scheduled tasks
- Disabling security tooling within the image
- Altering integrity or signature validation mechanisms

Common targets:
- Virtual machine templates and images
- OS installation ISOs or PXE images
- Container base images
- Network appliance firmware images

Indicators include:
- Hash changes to trusted images
- Unexpected services or binaries in deployed systems
- Security tools disabled across newly provisioned hosts
- Consistent compromise across multiple deployments

---

## 3. Subtechnique Considerations
T1601 includes the following subtechniques:
- **T1601.001 – Patch System Image**
- **T1601.002 – Downgrade System Image**

Key considerations:
- Impact scales with image reuse
- Detection is difficult post-deployment
- Compromise may predate system ownership
- Often combined with boot or firmware persistence

This technique undermines **trust in infrastructure provisioning**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Modifying golden VM images to include backdoors
- Injecting malicious startup scripts into base images
- Downgrading images to vulnerable versions
- Altering container base images in registries

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should focus on **image integrity and provenance**:
- Monitor image creation and modification events
- Validate cryptographic hashes and signatures
- Detect drift between deployed systems and known-good images
- Alert on unauthorized access to image repositories

### Data Source Notes
- **Image creation logs**: Track modifications
- **Integrity monitoring**: Detect tampering
- **Boot logs**: Identify compromised startup paths

Common false positives:
- Legitimate image updates
- Approved patching or maintenance

Tuning guidance:
- Enforce change control for image updates
- Maintain immutable, signed image repositories
- Increase severity for unsigned or unexpected image changes

---

## 6. Response Guidance
When suspected:
1. Identify affected images and deployments
2. Quarantine compromised images
3. Redeploy systems from trusted images
4. Rotate credentials and secrets embedded in images
5. Audit image repositories and access controls

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1542 - Pre-OS Boot|T1542]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1553 - Subvert Trust Controls|T1553]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1562 - Impair Defenses|T1562]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1070 - Indicator Removal on Host|T1070]]

---

## 8. SOC Relevance
T1601 is critical because:
- Compromise propagates at deployment scale
- Traditional endpoint detections may miss root cause
- Recovery actions may reintroduce malware

SOC teams must treat **image pipelines as security-critical assets**.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threats
- Supply chain–focused adversaries
- Actors targeting infrastructure providers

---

## 10. Campaign Usage
Observed in:
- Supply chain compromise campaigns
- Long-term infrastructure intrusions
- Prepositioning operations

---

## 11. Malware Usage
Associated with:
- Backdoors embedded in images
- Supply-chain–delivered malware
- Preinstalled persistence mechanisms

---

## 12. Mitigations
Recommended mitigations:
- Use signed and verified system images
- Restrict access to image repositories
- Implement reproducible builds
- Monitor for image drift and unauthorized changes

---

## 13. Testing & Validation
Validation approaches:
- Compare deployed systems to golden images
- Validate hash and signature enforcement
- Test SOC workflows for image compromise
- Simulate image tampering in controlled environments

---

## 14. References
MITRE ATT&CK. (2025). *Modify System Image (T1601)*.  
https://attack.mitre.org/techniques/T1601/

NIST. (2024). *Secure system and image integrity*.  
https://csrc.nist.gov/

Microsoft. (2024). *Securing OS deployment images*.  
https://learn.microsoft.com/security/

---

## 15. Notes
- Image trust equals system trust.
- Compromise can predate deployment.
- Image pipelines require continuous security oversight.
