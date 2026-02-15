---
entity_type: mitre_technique

technique_id: "T1672"
subtechnique_id: ""
technique_name: "Email Spoofing"

tactic:
  - Initial Access
  - Social Engineering

platforms:
  - Email
  - SaaS
  - Cloud

datasources:
  - Email Gateway Logs
  - Email Header Metadata
  - DNS Logs
  - Authentication Logs

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques:
  - "T1566"
  - "T1566.002"
  - "T1071.003"

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
  - initial-access
  - social-engineering
  - email
  - spoofing
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Email Spoofing (T1672)

## 1. Summary
Email Spoofing describes adversaries **forging email sender information to impersonate trusted individuals, organizations, or domains**. This technique is frequently used to facilitate phishing, credential harvesting, malware delivery, and business email compromise (BEC).

T1672 is commonly used to:
- Bypass user trust controls
- Increase phishing success rates
- Masquerade as legitimate senders
- Enable downstream social engineering attacks

---

## 2. Technical Overview
Email spoofing exploits weaknesses or misconfigurations in email authentication mechanisms. Adversaries achieve this by:
- Forging the `From`, `Reply-To`, or `Return-Path` headers
- Abusing open or misconfigured SMTP relays
- Exploiting weak or missing SPF, DKIM, or DMARC policies
- Registering lookalike or typo-squatted domains

Technical elements involved include:
- SMTP protocol manipulation
- DNS-based email authentication records
- Email header obfuscation
- Cloud email infrastructure abuse

Artifacts often include:
- Header mismatches between display name and envelope sender
- Failed or soft-fail SPF/DKIM checks
- Emails originating from unexpected IP ranges
- User reports of impersonation attempts

---

## 3. Subtechnique Considerations
Key considerations for T1672:
- Can be highly effective even without malware
- Often used in BEC and credential theft campaigns
- Detection depends on robust email authentication enforcement
- Social context plays a significant role in success

Spoofing may occur even when authentication partially passes.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Impersonating executives to request urgent actions
- Spoofing vendors to redirect payments
- Forging internal IT communications
- Combining spoofing with credential-harvesting links

These activities typically precede credential compromise or financial loss.

---

## 5. Detection Guidance
Detection strategies should focus on:
- Monitoring SPF, DKIM, and DMARC failures
- Detecting header inconsistencies
- Alerting on display-name impersonation
- Identifying anomalous sender infrastructure

### Data Source Notes
- **Email gateway logs**: Primary detection surface
- **DNS telemetry**: Required for authentication analysis
- **User reports**: High-value signal for spoofing detection

---

## 6. Response Guidance
When detected:
1. Quarantine or block spoofed messages
2. Notify impacted users and stakeholders
3. Investigate sender domains and infrastructure
4. Harden email authentication policies
5. Review for follow-on phishing or compromise

---

## 7. Related ATT&CK Content
- Related techniques:
  - [[20_Entities/07_TTPs/TA0001 - Initial Access/T1566 - Phishing|T1566]]
  - [[20_Entities/07_TTPs/TA0001 - Initial Access/T1566.002 - Spearphishing Link|T1566.002]]
  - [[20_Entities/07_TTPs/TA0011 - Command and Control/T1071.003 - Mail Protocols|T1071.003]]

---

## 8. SOC Relevance
T1672 is highly relevant in:
- Enterprise email environments
- SaaS-based collaboration platforms
- Financially motivated intrusion campaigns

Email spoofing often represents the first observable step in an attack chain.

---

## 9. Threat Actor Usage
This technique is widely used by:
- Financially motivated cybercriminals
- Business email compromise groups
- Advanced persistent threats conducting social engineering

Usage reflects low technical cost with high operational payoff.

---

## 10. Campaign Usage
Observed in:
- Business email compromise campaigns
- Credential harvesting operations
- Malware delivery via phishing

---

## 11. Malware Usage
While email spoofing itself is malware-agnostic, it is commonly used to deliver:
- Loaders and droppers
- Credential-harvesting frameworks
- Remote access trojans

---

## 12. Mitigations
Recommended mitigations:
- Enforce strict DMARC policies (`p=reject`)
- Implement SPF and DKIM correctly
- Deploy email gateway impersonation detection
- Conduct regular user awareness training
- Monitor and takedown lookalike domains

---

## 13. Testing & Validation
Validation approaches:
- Simulate spoofed email delivery in test environments
- Validate gateway enforcement of DMARC policies
- Conduct phishing resilience exercises
- Review SOC response playbooks

---

## 14. References
MITRE ATT&CK. (2024). *Email-based initial access techniques*.  
https://attack.mitre.org/

RFC 7208. (2014). *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email*.  
https://datatracker.ietf.org/doc/html/rfc7208

RFC 6376. (2011). *DomainKeys Identified Mail (DKIM) Signatures*.  
https://datatracker.ietf.org/doc/html/rfc6376

Google. (2023). *Preventing email spoofing with DMARC*.  
https://support.google.com/a/answer/2466580

---

## 15. Notes
- Email spoofing remains effective despite mature defenses
- Human trust is the primary attack surface
- Continuous tuning of email defenses is required
