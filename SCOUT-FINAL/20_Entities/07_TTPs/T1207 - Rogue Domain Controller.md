---
entity_type: mitre_technique

technique_id: "T1207"
subtechnique_id: ""
technique_name: "Rogue Domain Controller"

tactic:
  - Persistence
  - Privilege Escalation
  - Defense Evasion

platforms:
  - Windows

datasources:
  - Active Directory Logs
  - Authentication Logs
  - Network Traffic
  - Windows Event Logs
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
  - "T1098"
  - "T1556"
  - "T1558"
  - "T1484"

detection_priority:
  - Critical

detection_maturity: ""
threat_score: 5

created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

contributors: []
tags:
  - mitre
  - persistence
  - privilege-escalation
  - defense-evasion
  - active-directory
  - domain-controller
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Rogue Domain Controller (T1207)

## 1. Summary
Rogue Domain Controller describes adversaries **introducing or simulating a malicious Active Directory Domain Controller (DC)** within a Windows domain environment. By doing so, attackers can intercept authentication traffic, replicate directory data, manipulate trust relationships, and establish highly privileged persistence.

Adversaries use this technique to:
- Steal credentials via authentication interception
- Replicate sensitive Active Directory data
- Manipulate domain trust and replication
- Maintain persistent, domain-wide access

---

## 2. Technical Overview
Active Directory allows domain controllers to replicate directory data using well-defined protocols (e.g., DRSUAPI). Adversaries abuse this by:
- Promoting a compromised system to a domain controller
- Registering a rogue DC in Active Directory
- Exploiting replication protocols to pull directory data
- Masquerading as a legitimate DC to intercept credentials

Key technical elements include:
- Directory replication services
- Kerberos authentication
- NTLM authentication fallback
- DNS and service records associated with DCs

Indicators include:
- Unexpected domain controller objects
- Unauthorized replication requests
- Authentication traffic to unknown DCs
- Changes to AD Sites and Services

---

## 3. Subtechnique Considerations
Key considerations for T1207:
- Requires high privileges (often Domain Admin)
- Impact is domain-wide and severe
- Detection depends on AD-specific monitoring
- Often paired with credential access techniques

A rogue DC fundamentally undermines **Active Directory trust boundaries**.

---

## 4. Procedure Examples
Representative adversary behaviors include:
- Promoting a compromised host to a domain controller
- Using replication protocols to extract NTDS data
- Intercepting authentication traffic via rogue DC placement
- Persisting rogue DC objects within AD configuration

*(Examples are representative and intentionally non-operational.)*

---

## 5. Detection Guidance
Detection should emphasize **directory integrity and replication monitoring**:
- Monitor creation of new domain controller objects
- Alert on unauthorized DRS replication requests
- Detect authentication traffic to non-approved DCs
- Review changes in AD Sites and Services

### Data Source Notes
- **Active Directory logs**: Identify replication and role changes
- **Authentication logs**: Detect unusual DC authentication paths
- **Network traffic**: Observe replication and Kerberos anomalies

Common false positives:
- Legitimate domain controller provisioning
- Authorized disaster recovery testing

Tuning guidance:
- Require change control correlation for DC creation
- Maintain authoritative inventories of DCs

---

## 6. Response Guidance
When suspected:
1. Identify and isolate the rogue domain controller
2. Block replication traffic from unauthorized systems
3. Validate integrity of all domain controllers
4. Rotate domain credentials and KRBTGT accounts
5. Perform full Active Directory compromise assessment

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0003 - Persistence/T1098 - Account Manipulation|T1098]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1556 - Modify Authentication Process|T1556]]
  - [[20_Entities/07_TTPs/TA0006 - Credential Access/T1558 - Steal or Forge Kerberos Tickets|T1558]]
  - [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1484 - Domain Policy Modification|T1484]]

---

## 8. SOC Relevance
T1207 is critical because:
- It enables total domain compromise
- Detection windows may be short
- Recovery is complex and disruptive

SOC teams must treat **rogue DC activity as an emergency**.

---

## 9. Threat Actor Usage
Commonly used by:
- Advanced persistent threat actors
- Ransomware operators post-compromise
- Intrusions targeting full domain takeover

---

## 10. Campaign Usage
Observed in:
- Domain-wide compromise campaigns
- Espionage and ransomware intrusions
- Long-dwell Active Directory abuse

---

## 11. Malware Usage
Associated with:
- Credential harvesting frameworks
- AD exploitation toolkits
- Replication abuse tooling

---

## 12. Mitigations
Recommended mitigations:
- Restrict domain controller promotion privileges
- Monitor and alert on DC creation and replication
- Enforce tiered administrative models
- Harden Active Directory replication security

---

## 13. Testing & Validation
Validation approaches:
- Simulate unauthorized DC promotion in lab
- Validate alerts on replication abuse
- Test SOC response to rogue DC scenarios
- Ensure KRBTGT rotation procedures are practiced

Include:
- Preconditions: AD monitoring enabled
- Required roles/tools: AD admins, SOC, DFIR
- Expected outcomes: detection of rogue DC activity
- Success criteria: containment and domain integrity restoration

---

## 14. References
MITRE ATT&CK. (2025). *Rogue Domain Controller (T1207)*.  
https://attack.mitre.org/techniques/T1207/

Microsoft. (2024). *Detecting rogue domain controllers*.  
https://learn.microsoft.com/security/

SpecterOps. (2024). *Active Directory attack paths*.  
https://specterops.io/resources/

---

## 15. Notes
- Rogue DCs represent total trust failure.
- Recovery often requires domain-wide remediation.
- Continuous AD monitoring is essential.
