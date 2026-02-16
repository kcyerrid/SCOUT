---
entity_type: "procedure"
procedure_id: "0002"
title: "Test Procedure"
procedure_type: []
sop_version: "1.0"
status: "draft"
owner: "YOUR NAME"
review_cycle: Annual
last_reviewed: ""
applicable_roles: []
required_permissions: []
prerequisites: []
dependencies: []
related_detections: []
related_ttp: []
related_tools: []
related_incidents: []
risk_level: "low"
compliance_relevance: []
tags: ""
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
created: "2026-02-15 10:13:33"
updated: "2026-02-15 10:13:33"
related_itids: []
related_playbooks: []
tlp_classification: "TLP:GREEN"
---
# Procedure: Test Procedure

## 1. Purpose
Describe the purpose of the procedure in 2–3 sentences:
- Why this SOP exists  
- What operational need it satisfies  
- The risks it addresses  

Example:
> “This procedure defines how to isolate an endpoint using the EDR platform to prevent lateral movement during suspected compromise.”

---

## 2. Scope
Define what this SOP *does* and *does not* cover:
- Environments included/excluded  
- Tools or platforms applicable  
- Constraints or limitations  
- Situations where this SOP should NOT be used  

---

## 3. Prerequisites & Preconditions
List everything required before starting:
- Required roles or permissions  
- Required approvals  
- Data required (ticket, device ID, logs, etc.)  
- Environmental checks (e.g., confirm active incident, verify identity of user)  

This prevents misuse and reduces errors.

---

## 4. Step-by-Step Procedure
This is the core operational content.

Use numbered steps:
1. Step one — describe clearly.
2. Step two — include UI navigation or command examples if needed.
3. Step three — include validation steps.
4. Step four — include fallback paths or “if/then” logic.


Guidelines:
- Write steps so a new analyst could follow them safely.  
- Use optional callouts for UI paths, commands, or screenshots.  
- Never include sensitive values (passwords, tokens, IPs).

---

## 5. Validation & Verification
Describe how to confirm the procedure succeeded:
- Commands to run  
- Logs to check  
- UI indicators  
- Expected system or user state  

Example:
> “Verify EDR isolation status = ‘Isolated’ within 2 minutes.”

---

## 6. Rollback / Undo Steps
If applicable, describe how to reverse the procedure safely:
- When rollback is appropriate  
- Risks associated with rollback  
- Approvals needed  

Not every SOP has rollback steps, but many should.

---

## 7. Troubleshooting
Document common issues:
- Authentication failures  
- Timeouts  
- UI inconsistencies  
- System state mismatches  

And provide recommended corrective actions.

---

## 8. Risks & Considerations
Highlight operational risk:
- Potential service disruptions  
- Impact to user workflows  
- Forensic impact (e.g., reboot clears memory artifacts)  
- Regulatory implications  

This ensures analysts think before executing.

---

## 9. Compliance & Audit Notes
Document any compliance relevance:
- PCI DSS  
- HIPAA  
- SOX  
- GDPR  

If applicable, describe:
- Required logging  
- Required approvals  
- Required notifications  

---

## 10. Related SOPs, Playbooks & Tools
List links to:
- Other procedures this one depends on  
- Playbooks using this SOP  
- Tools involved  
- Detection logic or alerting mechanisms associated  

This turns SCOUT into a *modular operational system*.

---

## 11. Revision History
Track changes to ensure accountability:

| Version | Date | Author | Description |
|--------|------|--------|-------------|
| 1.0    | {{date}} | your_name | Initial release |

