---
entity_type: threat_actor
actor_name: "Windshift"
common_name: "Windshift"
actor_id: "G0112"
actor_type: "Cyber espionage / surveillance-focused (reported)"
aliases: ["Bahamut"]
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "2-medium"
first_seen: "2017-01-01"
last_seen: ""
status: "Unknown"
motivations: ["Espionage"]
objectives: ["Targeted surveillance and credential collection against selected victims"]
victimology_summary: "Windshift (also reported as Bahamut) is an espionage-oriented cluster described in public reporting as conducting targeted operations, including phishing and credential collection, and mobile-focused surveillance tradecraft."
target_sectors: []
target_regions: ["Middle East (reported)","Global (selective targeting reported)"]
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/S0466 - WindTail|WindTail (S0466)]]"
tools: []
infrastructure: ["[[Phishing]]","[[Credential Harvesting]]","[[Mobile Surveillance]]"]
ttps:
  - "[[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]"
  - "[[20_Entities/07_TTPs/T1098.001 - Account Manipulation: Additional Cloud Credentials]]"
  - "[[20_Entities/07_TTPs/T1136.001 - Create Account: Local Account]]"
  - "[[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]"
  - "[[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]"
  - "[[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]"
  - "[[20_Entities/07_TTPs/T1647 - Virtualization/Sandbox Evasion]]"
  - "[[20_Entities/07_TTPs/T1648.001 - Serverless Execution: WebAssembly]]"
  - "[[20_Entities/07_TTPs/T1656 - Impersonation]]"
notable_claims:
  - "Public reporting commonly references the 'Bahamut' naming; operational details vary by source."
intel_sources:
  - "https://attack.mitre.org/groups/G0112/"
  - "https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf"
tags: ["scout","threat-actor","mitre-g0112","espionage","bahamut","mobile"]
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Windshift (G0112), also commonly reported as **Bahamut**, is an espionage-oriented cluster associated with **targeted phishing**, **credential collection**, and **surveillance tradecraft**, including techniques that appear in **mobile-focused** reporting.

## 2. Attribution & Profile
- **Type:** Espionage / surveillance
- **Aliases:** Bahamut
- **Attribution Confidence:** 2-medium (consistent reporting of tradecraft; operator identity remains assessed)

## 3. Targeting & Victimology
- Targeting is described as selective (individuals/orgs of interest), with reporting frequently focusing on **Middle East-related** victim sets.
- Track exact victimology in-case (avoid assuming sectors/regions beyond sourced cases).

## 4. Known Malware, Tools & Infrastructure
**Malware**
- [[30_CIPHER/05_Malware/S0466 - WindTail|WindTail (S0466)]]

**Infrastructure themes**
- Spearphishing delivery + credential harvesting
- Web-protocol C2 patterns in enterprise reporting
- Mobile surveillance / impersonation themes in related reporting

## 5. Tradecraft Overview
- **Delivery:** spearphishing attachments and malicious links
- **Collection:** keylogging / credential capture
- **Evasion:** sandbox/virtualization evasion and (reported) modern web execution patterns

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1071.001 - Application Layer Protocol: Web Protocols]]
- [[20_Entities/07_TTPs/T1059.003 - Command and Scripting Interpreter: Windows Command Shell]]
- [[20_Entities/07_TTPs/T1098.001 - Account Manipulation: Additional Cloud Credentials]]
- [[20_Entities/07_TTPs/T1136.001 - Create Account: Local Account]]
- [[20_Entities/07_TTPs/T1566.001 - Phishing: Spearphishing Attachment]]
- [[20_Entities/07_TTPs/T1056.001 - Input Capture: Keylogging]]
- [[20_Entities/07_TTPs/T1204.001 - User Execution: Malicious Link]]
- [[20_Entities/07_TTPs/T1647 - Virtualization/Sandbox Evasion]]
- [[20_Entities/07_TTPs/T1648.001 - Serverless Execution: WebAssembly]]
- [[20_Entities/07_TTPs/T1656 - Impersonation]]

## 7. Detection Opportunities
1. **Spearphishing + link execution**
   - Email gateway + endpoint telemetry around link-click → download → execution chains.
2. **Keylogging / input capture**
   - Monitor suspicious keyboard hooks, unexpected input-capture libraries, and abnormal accessibility API use.
3. **Impersonation**
   - Look for lookalike sender domains, credential-harvesting pages, and brand impersonation kits.

## 8. Response & Mitigation Guidance
- Harden identity (MFA, phishing-resistant factors for high-risk users, conditional access).
- Restrict macro/script execution; monitor command shell usage on endpoints with link-click provenance.
- Mobile controls: MDM baselines, app allowlisting for high-risk populations, and mobile threat defense where feasible.

## 9. Hunting Ideas
- Find clusters of spearphishing recipients who later show unusual account changes (new credentials, local accounts).
- Identify endpoints with suspicious command shell executions shortly after email/web activity.

## 10. Associated Malware
- [[30_CIPHER/05_Malware/S0466 - WindTail|WindTail (S0466)]]

## 11. Associated Tools
None beyond publicly summarized reporting.

## 12. Analyst Notes
- Victimology varies significantly by dataset; avoid hardcoding sectors unless your cases provide evidence.
- Completeness: **Medium** (ATT&CK provides limited narrative depth for some behaviors referenced by vendors).

## 13. Further Reading / External Resources
- MITRE ATT&CK Group G0112: https://attack.mitre.org/groups/G0112/
- BlackBerry report (Bahamut): https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf

## 14. References (APA)
- MITRE ATT&CK. (n.d.). *Windshift (G0112).* https://attack.mitre.org/groups/G0112/
- BlackBerry. (n.d.). *SPARK: Bahamut (report).* https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf
