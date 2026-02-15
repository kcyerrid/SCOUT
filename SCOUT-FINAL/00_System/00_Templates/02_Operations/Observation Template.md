---
entity_type: observation

observation_id: ""                   # e.g., OBS-2025-0012
title: ""                            # Short descriptive name

observation_time: ""                 # When the observation was made
source_context: 
- alert
- investigation
- hunt
- tuning
- research
- unknown
relevance: 
- 4-low
- 3-medium
- 2-high
- 1-critical

related_alert: ""                    # optional link
related_incident: ""                 # optional link
related_investigation: ""            # optional link
related_hunt: ""                     # hunt or hypothesis session
related_project: ""                  # long-running tuning or analysis work

related_assets: []
related_users: []
related_iocs: []
related_ttp: []                      # MITRE techniques
related_detections: []

hypothesis: ""                       # optional: what this observation may indicate
evidence: ""                         # supporting facts, logs, analysis

tags: []
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101

created: "{{date}}"
updated: "{{date}}"
---
# Observation: {{title}}

## 1. Summary
Describe the observation in 1–3 sentences:
- What was seen  
- Why it is interesting  
- What triggered the analyst to log it  

Keep it succinct and actionable.

---

## 2. Context & Background
Document where this came from:
- Alert triage  
- Ongoing investigation  
- Threat hunting  
- Pattern noticed across multiple logs  
- Correlation or enrichment insight  
- A hypothesis from a prior pivot  

Explain the conditions and environment in which the observation was made.

---

## 3. Details & Evidence
Describe what exactly was observed:
- Logs  
- Timestamps  
- Processes  
- Commands  
- Destinations  
- Correlated events  
- Frequency anomalies  
- Identity patterns  

Use bullet formatting for clarity.  
Do not dump raw logs; summarize them.  
Link to artifacts if needed.

---

## 4. Hypothesis (Optional)
If applicable, describe:
- What this might signify  
- Potential threats or misconfigurations  
- Possible attack stages implied  
- Whether this aligns with known actor behaviors  
- Whether this conflicts with expected baselines  

Example:  
> “This may represent early reconnaissance consistent with T1595.”

---

## 5. Pivot Opportunities
Describe what the analyst *could do next*:
- Query further logs  
- Expand timeframe  
- Check identity footprints  
- Investigate endpoint telemetry  
- Validate against detections  
- Review asset behavior  
- Compare to threat intel  

This is critical for building repeatability into your analysis.

---

## 6. Linked Entities
Document links to atomic notes:

### 6.1 Assets
- link to assets

### 6.2 Users
- link to assets

### 6.3 IOCs
- link to IP, domain, hash, etc.

### 6.4 TTPs
- MITRE technique entries

### 6.5 Detections
- Reference detection notes that may apply

---

## 7. Analyst Assessment
Provide a final assessment, including:
- Is this significant?  
- Should this be escalated?  
- Does this merit an incident?  
- Is this something that needs to be operationalized?  

Mark your confidence level.

---

## 8. Notes & Follow-Up
Anything else worth logging:
- Tasks to complete  
- Open questions  
- Signals needing monitoring  
- Recommendations for tuning  
- Ideas for future hunts  

