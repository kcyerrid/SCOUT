---
entity_type: timeline

timeline_id: ""                      # e.g., TL-2025-0012
title: ""                             # descriptive name for the timeline

related_incident: ""                  # primary incident (if applicable)
related_investigation: ""             # optional; if timeline is part of analysis
related_alerts: []
related_observations: []
related_response_actions: []

scope_start_time: ""                  # earliest time of interest
scope_end_time: ""                    # latest time of interest
timezone: UTC                          # e.g., UTC, PST, CST

assets_involved: []
users_involved: []
iocs_involved: []
ttp_involved: []                      # MITRE techniques
malware_involved: []
tools_involved: []

timeline_status: 
- draft
- in_progress
- validated
- finalied

visibility_level: 
- internal
- leadership
- audit
- external

tags: []
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
created: "{{date}}"
updated: "{{date}}"
---
# Timeline: {{title}}

## 1. Overview
Describe:
- The purpose of this timeline  
- The scope of the events  
- What entities (users, assets, IOCs, tools) it covers  
- Whether the timeline is complete or ongoing  

Example:
> “This timeline reconstructs events surrounding suspicious authentication behavior on Host123 from 2025-01-10 to 2025-01-11.”

---

## 2. Summary of Key Events
Provide a high-level bulleted summary:
- The first event of interest  
- The most significant escalation point  
- When containment occurred  
- Any anomalies  
- Any unexplained gaps  

This section is designed for leadership/executive consumption.

```chronos
- [2020] Event 1

- [2020-01-04~2020-01-14] Event 2

- [2020-01-10] Event 3

@ [2020-01-06~2020-01-10] Period 1
```

---

## 3. Detailed Event Log (Chronological)
This is the core of the timeline — a structured chronological list of all relevant events.

### Format for each entry:
### YYYY-MM-DD HH:MM:SS (Timezone)

Event Type: alert | observation | system event | authentication | network communication | response action | other  
Source: SIEM | EDR | Identity Provider | Email Gateway | Firewall | Cloud Logs | Analyst Note | Other  
Entities: [assets, users, IOCs linked]

Description:

- What happened
- How it was detected or logged
- Why it matters

Linked Items:

- [Observation link]
- [Alert link]
- [Response Action link]
- [IOC link]


Repeat this format for each event.

---

## 4. Event Correlation Notes
Document how events relate to each other:
- Cause-effect relationships  
- Branching behavior  
- Dependencies or preconditions  
- Time proximity and statistical relationships  
- TTP alignment  

Example:

> “Failed logins at 01:12 preceded successful authentication at 01:15 from the same IP, indicating possible credential compromise.”

---

## 5. Gaps & Uncertainties
Identify missing information:
- Missing telemetry  
- Log retention issues  
- Blind spots in EDR  
- Identity logs not recorded  
- Devices offline  
- Timezones misaligned  

Document these so investigations and IR teams can plan compensating actions.

---

## 6. TTP & MITRE Analysis
For all events that map to MITRE TTPs:
- T1110 — Brute Force
- T1078 — Valid Accounts
- T1556 — Modify Authentication Process


Describe:
- Whether the behavior is consistent with known actor tradecraft  
- Whether this TTP sequence matches known actor patterns  

---

## 7. Impact Notes
Document:
- What systems were accessed  
- Whether privilege escalation occurred  
- Whether lateral movement happened  
- Whether data was accessed or exfiltrated  

This can be refined over time.

---

## 8. Response Actions Performed
List Response Action links chronologically:
- Isolated endpoint Host123
- Disabled user account jdoe
- Forced password reset


This gives a clear view of containment and remediation progression.

---

## 9. Final Assessment
Summarize:
- Whether the timeline is complete  
- Whether additional data collection is needed  
- Key conclusions  
- Residual uncertainties  
- Analyst confidence level  

This is the authoritative summary of the timeline.

---

## 10. Follow-Up Items
Document required follow-up tasks:
- Additional analysis  
- Hunt expansions  
- Recommendations for impacted teams  
- Gaps to address in detection engineering  
- Logging improvements  

Assign owners if applicable.


