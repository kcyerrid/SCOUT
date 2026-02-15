---
entity_type: incident
cssclass: incident-properties-collapsed
incident_id: ""
title: ""
incident_type: ""
incident_subtype: ""
severity:
priority:
status:
tlp_classification:
created_time: ""
created:
updated:
detected_time: ""
reported_time: ""
triage_start_time: ""
triage_end_time: ""
containment_time: ""
eradication_time: ""
recovery_time: ""
closed_time: ""
mttd: ""
mttr: ""
alert_sources: []
root_cause: ""
impact_summary: ""
primary_asset: ""
primary_user: ""
affected_assets: []
affected_users: []
related_iocs: []
related_ttp: []
related_detections: []
related_tools: []
related_malware: []
related_campaigns: []
related_actors: []
response_actions: []
observations: []
escalation_required: false
escalated_to: ""
regulatory_reporting_required: false
regulatory_deadline: ""
regulatory_status: ""
business_owner_notified: false
executive_notification_required: false
lessons_learned_status:
tags: []
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# Incident: {{title}}

## 1. Executive Summary
Provide a concise overview of:
- What happened
- What triggered detection
- What systems or identities were affected
- What actions were taken
- Current status
- Business impact

This summary is leadership-facing.

---

## 2. Incident Timeline Overview
Summarize key timestamps:
- Detection
- Reporting
- Triage
- Containment
- Eradication
- Recovery
- Closure

Highlight major delays or accelerations.

```chronos
{{incident_chronos_marker}}
```

---

## 3. Initial Detection & Triage
### 3.1 Detection Path
Explain:
- Where the detection came from (alert, observation, hunt, third-party report)
- Which tools or logs contributed to discovery

### 3.2 Initial Triage Summary
Include:
- Hypotheses formed during triage
- Indicators that elevated the event to an incident
- Key findings from early analysis

---

## 4. Technical Analysis
Describe what was actually happening under the hood.  
Organize by relevant ATT&CK TTPs, behaviors, or stages of the kill chain.

Include:
- Attack vector  
- Privilege usage  
- Lateral movement evidence  
- Persistence mechanisms  
- Data access or exfiltration  
- Misconfigurations exploited  
- Malware or tools involved  

This is the core analytical narrative.

---

## 5. Scope & Impact Assessment
Document:
- Assets affected  
- Users impacted  
- Systems or data at risk  
- Business function disruption  
- Estimated severity and potential consequences  

If impact is unknown, describe what is being done to determine it.

---

## 6. Containment, Eradication & Recovery
### 6.1 Containment Actions
Summarize steps, linked to Response Action pages.

### 6.2 Eradication
Document what was removed or corrected.

### 6.3 Recovery
Describe:
- What systems were restored
- Business steps taken
- Verification actions performed  
- Risk of recurrence

---

## 7. Linked Entities
### 7.1 Alerts
- link

### 7.2 Observations
- link

### 7.3 Response Actions
- link

### 7.4 Assets / Users
- link

### 7.5 IOCs
- link

### 7.6 MITRE TTPs
- link

### 7.7 Malware / Tools
- link

### 7.8 Threat Actors / Campaigns
- link

---

## 8. Root Cause Analysis
Explain:
- The primary cause of the incident  
- Contributing factors  
- Environmental weaknesses exploited  
- How similar incidents could be prevented

This should be actionable and precise.

---

## 9. Lessons Learned
Document:
- What went well  
- What needs improvement  
- Process gaps  
- Detection blind spots  
- Operational inefficiencies  
- Communication issues  

Assign owners for corrective actions if applicable.

---

## 10. Recommendations
Provide actionable recommendations for:
- Detection engineering  
- Infrastructure/security hardening  
- IAM improvements  
- Tooling or visibility gaps  
- Playbook or SOP updates  
- Training needed for analysts

Prioritize clearly.

---

## 11. Final Status & Closure
Summarize:
- Current state of systems
- Any residual risk
- Outstanding tasks
- Confirmation that the business is fully restored

**REMEMBER** 

Close Notes tell a story.  They are a mini retrospective, a get out of jail free card, and just solid business practices.  Take your time creating them and assume that your boss will be reading them.  

Mark the incident as closed when appropriate.


