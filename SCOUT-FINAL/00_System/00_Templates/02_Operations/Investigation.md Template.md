---
entity_type: investigation

investigation_id: ""               # e.g., INV-2025-0012
title: ""                          # short descriptive name

status: 
- open
- in_progress
- on_hold
- escalated
- closed
priority: 
- 4-low
- 3-medium
- 2-high
- 1-critical

investigation_type: 
- alert_triage
- anomaly_analysis
- hunt
- identity_investigation
- asset_investigation
- vulnerability_exploitation
- suspicious_behavior
- unknown
initiated_time: ""
completed_time: ""

initiated_by: ""                   # analyst who started investigation
assigned_to: []                    # primary analyst(s)
escalated_to: ""                   # if investigation requires IR escalation

trigger_source: 
- alert
- observation
- hunt
- ticket
- external
- other
trigger_reference: ""              # link to the triggering entity

related_alerts: []
related_incidents: []
related_observations: []
related_response_actions: []

related_assets: []
related_users: []
related_iocs: []
related_ttp: []                    # MITRE techniques
related_malware: []
related_tools: []
related_campaigns: []
related_actors: []

hypotheses: []                     # optional list of hypotheses stated at start or added later
key_findings: []                   # summarized findings

escalation_recommended: false
escalation_reason: ""

root_cause_suspected: ""
impact_suspected: ""
confidence_level: 
- 3-low
- 2-moderate
- 1-high
tags: []
created: 
updated: 
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# Investigation: {{title}}

## 1. Summary
Brief overview of:
- What triggered the investigation  
- What is being examined  
- Initial suspicion or anomaly  
- Current status and priority  

This summary should make sense on its own even months later.

---

## 2. Trigger Details
Describe the exact condition that caused the investigation:
- Alert details  
- Observation reference  
- Hunt signal  
- External report  
- System anomaly  

Include only the necessary context—link out to atomic entities instead of duplicating content.

---

## 3. Initial Hypotheses
State the working hypotheses at the beginning of the investigation:

Examples:
- “This may be credential misuse.”  
- “Possible malware execution following phishing.”  
- “Unusual authentication behavior; may be travel-related.”

Hypotheses can evolve over time.

---

## 4. Investigation Log (Iterative Analysis)
Use a structured, chronological log of reasoning, pivots, and discoveries.

### Format:

### Step N — Time: HH:MM

Action:  
Reasoning:  
Evidence:  
Pivot or Next Step:

Record:
- Queries performed  
- Evidence reviewed  
- Correlation pivots  
- Logs analyzed  
- Tools used  
- Eliminated hypotheses  
- New hypotheses formed  

This becomes the **forensic journal** of the investigation.

---

## 5. Evidence & Findings
Document the validated insights:
- Confirmed suspicious or malicious behavior  
- Benign explanations  
- Inconsistencies  
- Data gaps  
- Environmental misconfigurations  
- Unexpected side effects or deviations from baselines  

Use bullets for clarity.

---

## 6. Scope Analysis
Describe the breadth of what was uncovered:
- Number of users affected  
- Number of assets touched  
- Data access patterns  
- Lateral movement indicators  
- External communication patterns  
- Identity risks  
- Alignment with known actor tradecraft  

If multiple entities are involved, list and link them.

---

## 7. TTP Mapping (MITRE)
Map observed behaviors to ATT&CK techniques:
- TXXXX — Technique Name
- TYYYY — Technique Name


This supports hunting, detection engineering, and threat intel enrichment.

---

## 8. Risk & Impact Assessment
Describe:
- Potential business impact  
- Data access or exposure likelihood  
- Regulatory implications  
- Systems at risk  
- Identity or lateral movement risk  

This is the analytical assessment, not the final RCA.

---

## 9. Escalation Recommendation
If escalation to an Incident is warranted:

### 9.1 Recommendation
Explain why:
- Behavior meets incident criteria  
- Clear malicious activity  
- Material risk  
- Containment required  
- Positive IOC correlation  
- Threat actor alignment  

### 9.2 Escalation Destination
Specify:
- SOC IR lead  
- Incident commander  
- MSSP  
- Executive notification if needed  

---

## 10. Final Findings & Summary
Summarize the conclusion:
- Confirmed benign / malicious / inconclusive  
- Remaining open questions  
- Observations that need follow-up  
- Whether the investigation supports improvements in detection or response  

---

## 11. Follow-Up Actions
Document required next steps:
- Response actions  
- Detection tuning  
- Additional logging  
- Recommendations for asset or identity teams  
- Threat hunting expansions  
- Playbook updates  

Assign owners if applicable.

---

## 12. Linked Entities
List all entity links grouped by category:
- Alerts  
- Observations  
- Assets  
- Users  
- IOCs  
- TTPs  
- Malware  
- Tools  
- Actors  
- Campaigns  

This section makes the investigation graph-aware.

---

## 13. Analyst Notes
Freeform space for:
- Thoughts  
- Confidence statements  
- Caveats  
- Future considerations  
- Documentation that aids handoff or review  


