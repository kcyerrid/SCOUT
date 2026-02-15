---
entity_type: mitre_technique

technique_id: "T1189"
subtechnique_id: ""
technique_name: "Drive-by Compromise"

tactic: ["Initial Access"]
platforms: ["windows", "macos", "linux"]
datasources: ["Network Traffic", "Web Proxy Logs", "DNS Logs", "Endpoint Detection Logs"]

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: "Enterprise"
deprecated: false
revoked: false

associated_threat_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: ["T1566", "T1204", "T1059"]

detection_priority: "High"
detection_maturity: ""
threat_score: 4

created: "2025-12-16"
updated: "2025-12-16"

contributors: []
tags: ["mitre", "technique"]

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Drive-by Compromise (T1189)

## 1. Summary
Drive-by Compromise describes adversary delivery of malicious content to a victim system simply by causing the user to visit a compromised or adversary-controlled website. Unlike phishing, user interaction beyond browsing is often minimal or nonexistent, relying instead on browser vulnerabilities, malicious scripts, or exploit frameworks.

This technique is commonly used for initial access and is effective at scale when paired with traffic redirection, SEO poisoning, or malvertising.

---

## 2. Technical Overview
Adversaries compromise legitimate websites or stand up malicious infrastructure that serves exploit code, malicious scripts, or payload delivery mechanisms.

Common technical mechanisms include:
- Exploit kits targeting browser or plugin vulnerabilities
- Malicious JavaScript injected into legitimate sites
- Traffic redirection via malvertising or compromised ad networks
- Payload delivery through HTML, JavaScript, or file downloads

Artifacts include HTTP requests to malicious domains, script execution in browsers, and subsequent endpoint process creation.

---

## 3. Subtechnique Considerations
T1189 does not currently define subtechniques. Variations typically depend on:
- Browser type and version
- Operating system
- Exploit delivery mechanism (exploit kits vs. script-based delivery)

Effectiveness is heavily influenced by patch level and browser hardening.

---

## 4. Procedure Examples
Observed adversary procedures include:
- Redirecting users from compromised sites to exploit landing pages
- Serving browser exploits that drop loaders or backdoors
- Triggering silent downloads following script execution

Analysts may observe short-lived web sessions followed by endpoint activity.

---

## 5. Detection Guidance
Detection should focus on web and endpoint telemetry:
- Unexpected redirects to newly registered or low-reputation domains
- Browser process spawning child processes
- Script execution followed by file writes or downloads
- Correlation between web traffic and endpoint alerts

Network and endpoint correlation is critical for reliable detection.

### Data Source Notes
- **Web Proxy Logs:** High value for identifying malicious redirects
- **DNS Logs:** Useful for detecting newly registered domains
- **Endpoint Logs:** Required to confirm successful compromise

---

## 6. Response Guidance
When Drive-by Compromise is suspected:
- Isolate affected endpoints
- Identify and block malicious domains and URLs
- Patch vulnerable browsers and plugins
- Assess for secondary payloads or persistence mechanisms

Preserve browser, network, and endpoint artifacts for analysis.

---

## 7. Related ATT&CK Content
- Related techniques:  
  [[20_Entities/07_TTPs/TA0001 - Initial Access/T1566 - Phishing|T1566]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1204 - User Execution|T1204]]  
  [[20_Entities/07_TTPs/TA0002 - Execution/T1059 - Command and Scripting Interpreter|T1059]]

---

## 8. SOC Relevance
Drive-by Compromise remains a viable initial access vector, particularly against unpatched systems and unmanaged endpoints. Organizations with limited web visibility or endpoint protection face elevated risk.

---

## 9. Threat Actor Usage
This technique is used by:
- Opportunistic cybercriminal groups
- Ransomware operators leveraging loaders
- Advanced actors targeting specific browser vulnerabilities

Confidence in continued usage is high.

---

## 10. Campaign Usage
Drive-by Compromise appears in:
- Malvertising campaigns
- Exploit kit distribution waves
- Targeted watering hole attacks

---

## 11. Malware Usage
Malware families frequently delivered via drive-by compromise include:
- [[30_CIPHER/05_Malware/S0367 - Emotet|Emotet]]
- [[30_CIPHER/05_Malware/S0650 - QakBot|QakBot]]
- [[30_CIPHER/05_Malware/S0089 - ZeuS|ZeuS]]

---

## 12. Mitigations
Effective mitigations include:
- Regular patching of browsers and plugins
- Web filtering and DNS security controls
- Script execution restrictions
- Endpoint exploit protection and EDR

---

## 13. Testing & Validation
Validation approaches include:
- Simulated drive-by payload delivery in test environments
- Purple team exercises focusing on browser exploit detection
- Review of web-to-endpoint alert correlation

Successful validation results in timely alerts with minimal false positives.

---

## 14. References
MITRE ATT&CK. (2024). *Drive-by Compromise (T1189)*.  
https://attack.mitre.org/techniques/T1189/

Cisco Talos. (2022). *Exploit kits and drive-by compromises*.  
https://blog.talosintelligence.com/exploit-kits/

Google. (2023). *Protecting users from drive-by downloads*.  
https://security.googleblog.com/2023/02/protecting-users-from-drive-by-downloads.html

---

## 15. Notes
- Browser patching cadence directly impacts risk
- Web telemetry gaps significantly reduce detection fidelity
- Exploit kits continue to evolve with new evasion techniques

