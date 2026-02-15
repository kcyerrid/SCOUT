---
entity_type: response_action

response_action_id: ""             # e.g., RA-2025-0012
title: ""                          # short actionable description

action_type: 
- containment
- remediation
- eradication
- investigation
- recovery
- communication
- validation
- other
action_status: 
- planned
- in_progress
- completed
- cancelled
- failed
action_priority: 
- 4-low
- 3-medium
- 2-high
- 1-critical
initiated_by: ""                   # analyst or team who initiated action
executed_by: ""                    # who actually performed the action
approved_by: ""                    # if required (manager, lead, etc.)

start_time: ""
end_time: ""
duration: ""

related_alert: ""
related_incident: ""
related_investigation: ""
related_observation: ""

target_asset: ""                   # link to Asset
target_user: ""                    # link to User
related_assets: []
related_users: []

related_iocs: []
related_ttp: []                    # MITRE ATT&CK techniques involved
related_detections: []
related_tools: []                  # tools/platforms used to perform the action

justification: ""                  # why this action was necessary
expected_outcome: ""
actual_outcome: ""
verification_steps: ""             # how success/failure was validated

risk_of_action: 
- 3-low
- 2-medium
- 1-high
operational_impact: 
- 3-low
- 2-medium
- 1-high
- 0-none

notes: []
tags: []

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
created: "{{date}}"
updated: "{{date}}"
---
# Response Action: {{title}}

## 1. Summary
Describe the action taken, including:
- What the action was
- Why it was initiated
- Context within an incident, alert, or investigation

Keep this short and operational.

---

## 2. Action Details
Document:
- The exact steps performed  
- Tools/systems used  
- Commands or workflows executed  
- Timestamp alignment if multiple steps were required  

Avoid sensitive data; describe behaviorally.

---

## 3. Justification & Risk
Explain:
- Why the action was necessary  
- What risk it was mitigating  
- Potential side effects or operational impact  

Examples:
- “Account disabled to prevent further malicious authentication attempts"  
- “Host isolated to stop data exfiltration”  

---

## 4. Expected vs. Actual Outcome
### 4.1 Expected Outcome
What you believed the action would accomplish.

### 4.2 Actual Outcome
What actually happened, including:
- Success/failure  
- Partial success  
- Unexpected behavior  
- Errors encountered  

---

## 5. Verification
Document how the success of the action was validated:
- Logs checked  
- Asset telemetry status  
- Identity or network verification  
- Third-party tool confirmation  

Example:
- “Verified host isolation via CrowdStrike: status=isolated”  

---

## 6. Linked Entities
Cross-link to all relevant items:

### Alerts
- link

### Incidents
- link

### Assets
- link

### Users
- link

### IOCs
- link

### Detections
- link

---

## 7. Analyst Notes
A space for:
- Additional details  
- Caveats  
- Follow-up tasks  
- Audit considerations  


