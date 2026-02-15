---
entity_type: alert

alert_id: ""                      # auto or manual ID (e.g., ALRT-SENT-2025-0012)
alert_name: ""                    # human-readable name
generated_by: ""                  # tool/source (Sentinel, Falcon, Defender, Email Gateway)

alert_time: ""                    # timestamp the alert was generated
received_time: ""                 # timestamp SOC received/triaged alert
severity: ""
category: ""
correlation_id: ""                # if part of a related alert cluster or incident
detection_id: ""                  # link to detection entity (23_Detections)
tactics: []                       # ATT&CK tactics involved (high-level)
techniques: []                    # ATT&CK technique IDs

primary_asset: ""                 # link to Asset entity
primary_user: ""                  # link to User entity
related_assets: []
related_users: []
related_iocs: []
related_ttp: []                   # operational TTPs (26_TTPs)

initial_disposition: ""
final_disposition: ""
disposition_reason: ""
triage_analyst: ""
escalation_required: false
escalated_to: ""

related_incidents: []
triage_notes: ""

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
created: 
updated:
---
# Alert: {{alert_name}}

## 1. Summary
Brief overview of the alert:
- What triggered it
- Why it matters
- Initial context (system, user, activity)

---

## 2. Alert Details
Describe:
- How the alert was generated (analytic, signature, anomaly, threat intel)  
- Relevant metadata from the tool  
- Any notable fields or values that stand out  
- Whether the alert appears reliable or noisy  

---

## 3. Triage Steps
Document what the analyst has already done:

- Checked related logs  
- Verified identity activity  
- Looked up reputation of IOC(s)  
- Examined device telemetry  
- Performed enrichment steps (VirusTotal, WHOIS, UA parsing, geo lookup)  
- Queried SIEM or EDR  

Include reference queries where applicable.

---

## 4. Findings
Summarize what was discovered:
- Suspicious behavior confirmed?  
- Benign explanation found?  
- Additional context linking this alert to other events?  

---

## 5. Next Actions & Recommendations
Specify required steps:
- Escalate to incident?  
- Request more logs?  
- Notify stakeholder?  
- Perform containment or other response actions?  

---

## 6. Linked Entities
List:
- Assets  
- Users  
- IOCs  
- TTPs  
- Detections  
- Incidents  

Cross-link to atomic notes.

---

## 7. Final Disposition
State and justify:
- false_positive  
- benign_positive  
- true_positive  
- unknown → requires additional review  

Provide succinct reasoning.

---

## 8. Analyst Notes
Freeform notes on:
- Ambiguities  
- Unusual patterns  
- Items requiring follow-up  




