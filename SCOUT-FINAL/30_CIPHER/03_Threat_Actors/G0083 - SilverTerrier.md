---
entity_type: threat_actor
actor_name: "SilverTerrier"
common_name: "SilverTerrier"
actor_id: "G0083"
actor_type: "Cybercriminal (BEC-focused)"
aliases: []
country_of_origin: "Nigeria"
suspected_sponsors: []
attribution_confidence: "High"
first_seen: "2014-01-01"
last_seen: ""
status: "Active"
motivations: ["Financial gain"]
objectives: ["Business Email Compromise (BEC)","Credential theft and email abuse","Financial theft"]
victimology_summary: "Nigerian threat group documented in ATT&CK as active since 2014, mainly targeting high technology, higher education, and manufacturing; associated with BEC campaigns and financial theft."
target_sectors: ["High Technology","Higher Education","Manufacturing"]
target_regions: []
related_groups: []
malware: ["[[30_CIPHER/05_Malware/Agent Tesla]]"]
tools: []
infrastructure: ["[[HTTP C2]]","[[FTP C2]]","[[SMTP C2]]"]
ttps: ["[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]","[[20_Entities/07_TTPs/T1071.002 - Application Layer Protocol: File Transfer Protocols]]","[[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]","[[20_Entities/07_TTPs/T1657 - Financial Theft]]"]
notable_claims: []
intel_sources: ["MITRE ATT&CK - G0083 SilverTerrier - https://attack.mitre.org/groups/G0083/","MITRE ATT&CK - S0331 Agent Tesla - https://attack.mitre.org/software/S0331/"]
tags: ["scout","threat-actor","mitre-g0083","silverterrier","bec","nigeria"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. BLUF / Executive Summary
SilverTerrier (G0083) is documented in ATT&CK as a Nigerian threat group active since at least 2014, primarily linked to business email compromise (BEC) activity and financial theft targeting high technology, higher education, and manufacturing. ATT&CK highlights command-and-control via common application-layer protocols and associates the group with [[30_CIPHER/05_Malware/Agent Tesla]].

## 2. Attribution Notes
ATT&CK characterizes SilverTerrier as a Nigerian threat group; this note treats the geographic attribution as high confidence as stated by ATT&CK, without extending beyond documented claims.

## 3. Motivations & Objectives
- Monetization via BEC workflows
- Email abuse and credential-driven account access
- Exfiltration/coordination via common web, FTP, and mail protocols

## 4. Targeting Profile
- **Sectors (ATT&CK):** High Technology, Higher Education, Manufacturing
- **Primary objective:** Financial theft (BEC)
- **Likely victim assets:** Mailboxes, identity systems, and finance/approval workflows

## 5. Tradecraft Overview
- Reliance on standard application-layer protocols for control and data movement (HTTP/FTP/SMTP per ATT&CK).
- Commodity infostealer/RAT tooling alignment (Agent Tesla in ATT&CK software table).

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1657 - Financial Theft]]
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1071.002 - Application Layer Protocol: File Transfer Protocols]]
- [[20_Entities/07_TTPs/T1071.003 - Application Layer Protocol: Mail Protocols]]

## 7. Malware & Tools Used
- **Malware (ATT&CK software):**
  - [[30_CIPHER/05_Malware/Agent Tesla]]

## 8. Infrastructure Patterns
- HTTP-based C2 and delivery coordination
- FTP for file movement in some reported cases
- SMTP as an operational channel aligned to email-centric fraud workflows

## 9. Campaign History
- **2014–present (reported):** Continued BEC-oriented activity across targeted sectors per ATT&CK summary and cited reporting.

## 10. Known Indicators
No stable IOCs are provided in this note; prioritize tenant/mail telemetry and endpoint EDR artifacts per incident.

## 11. Defensive Recommendations
- Prioritize detections for anomalous outbound SMTP from endpoints, unusual FTP clients/processes, and suspicious HTTP beacons from user workstations.
- Harden finance approvals: out-of-band verification, MFA enforcement, and strict inbox rule auditing for finance/accounting users.
- Monitor for common commodity-stealer behaviors (credential store access, browser credential reads, keystroke capture) in endpoints tied to finance workflows.

## 12. Analyst Notes
**Confidence:** High for ATT&CK-stated scope and the listed software association; BEC campaigns are highly variable, so validate per tenant and per case.

## 13. Further Reading / External Resources
- https://attack.mitre.org/groups/G0083/
- https://attack.mitre.org/software/S0331/

## 14. References
- MITRE ATT&CK. (2023). *SilverTerrier (G0083).* https://attack.mitre.org/groups/G0083/
- MITRE ATT&CK. (2023). *Agent Tesla (S0331).* https://attack.mitre.org/software/S0331/
