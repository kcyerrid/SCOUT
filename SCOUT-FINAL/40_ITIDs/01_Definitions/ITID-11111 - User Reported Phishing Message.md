---
entity_type: itid
itid_id: ITID-11111
itid_name: User Reported Phishing Message
itid_category:
  - human
  - company_brand
  - device
  - infrastructure
  - company
  - supply_chain
  - testing
  - other
itid_parent: ITID-11110
itid_children: []
definition: ITID-11111 is designed to capture all instances of a human actor reporting a phishing message to security.  Unlike machine-based detections, a user-reported phish has a higher probability of being a false positive (spam, junk, etc.).
scope_includes:
  - User Reported Phishing Messages to the security team.
scope_excludes:
  - Machine detected phishing messages to the security team.
severity_guidance:
  - 4-low
priority_guidance:
  - 4-low
escalation_guidance: Escalate to management if the Service Level Agreement is at risk of being exceeded or if there is a campaign of over 50 recipients.
typical_indicators:
  - Email to the phishing mailbox
common_attack_vectors:
  - Email  
common_root_causes:
  - User Awareness
  - Public Information
mapped_mitre_tactics:
  - TA0001 - Initial Access
mapped_mitre_techniques:
  - T1566
  - T1566.001
  - T1566.002
  - T1566.003 
mapped_controls:
  - Email Filtering
related_playbooks:
  - ITID-11112
related_sops: []
related_detections: []
reporting_rollup: Identity Threats
metrics_tracked:
  - "Volume of Inbound Phishing Messages over time"
  - "% of False Positive Phishing Messages Reported By Human Actors"
  - "% of True Positive Phishing Messages Containing Malicious Attachments"
status: active
review_cycle: annual
last_reviewed: 2025-12-22
owner: K.C. Yerrid
tags:
  - "#phishing"
  - "#spearphishing"
created: 2025-12-28
updated:
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# ITID-11111 — User Reported Phishing Message



## 1. Purpose

ITIDs in the ITID-11110 family are categorized as mass phishing attacks against the human, using various social engineering techniques.  [[ITID-11111 - User Reported Phishing Message | ITID-11111]] represents the most common incident type in most environments:  the user-reported phishing message.  Whether the phishing message was detected by a machine is irrelevant; the trigger for activating this ITID is that it must be **reported** by a human actor.  The channel does not matter either.  

[[ITID-11111 - User Reported Phishing Message|ITID-11111]] is distinct from other ITIDs in this family based on the manner by which it was reported into the security team.  For example, [[ITID-11112 - Machine Detected Phishing Message|ITID-11112]] is designed exclusively for flagged phishing messages that are reported by a machine or application control.  The difference and split in ITIDs allows security operations teams to get very granular on the effectiveness of their controls.  

Leaders and security operations personnel should focus on the macro view of this ITID's candidate metrics, and avoid wearing "blinders" and looking too closely at individual incidents.  


---

## 2. Definition
This ITID shall be recorded in the SIEM whenever one or more of the following conditions are present and true:
- A customer sends an email, either directly or through a self-reporting mechanism like a Report Phish button to the security team and reports the message as suspicious.
- A customer contacts a member of the Security Operations team and reports a message as suspicious through any channel other than email.

---

## 3. Scope

### 3.1 Included
To be included in the scope of this ITID, the following conditions must be met:

- A human actor must be the entity that reports the suspicious message.

### 3.2 Excluded
All other actors, including computer infrastructure, applications, automated controls, and any other actors that are non-Human.  

---

## 4. Severity & Escalation Guidance

Phishing messages have become commoditized and compensating controls have improved over time.  In addition, the convenience of a programs like KnowBe4's Report Phish button make it easier than ever to empower the end users to avoid phish messages. As such, we de-emphasize the severity and priority of user reported phishing messages.  

By default, a user reported phish is a **low severity**, low priority incident type.  Security analysts are empowered to raise or lower the severity of an incident to any severity other than critical, which requires management approval.   The following are guidelines on when it is appropriate to escalate a phishing message to management:

- When the target distribution contains more than 50 company employees (Mass Phishing Campaign, see [[RB-0001 - Mass Phishing Campaign Runbook]].
- When the target distribution contains either the CEO, or any of the CEO's directs or other priority targets (Spearphishing / Whaling).
- When the end user shows evidence that he/she interacted with the phishing landing infrastructure, such as providing credentials or sensitive information.
- When a privacy event is suspected.
- When the phishing message contains a malware payload.
- When the [[SLA-0002 - SecOps SLA with Company Employees on Phishing Response]] Service Level Agreement expiration is approaching.

Escalating any phishing-related report is encouraged when unsure of the origin or payload of the suspected phishing message.


---

## 5. Indicators & Patterns

While user reported phishing messages are among the most common incident types in the ITID taxonomy, they also remain among the highest in false positive investigations.  As such, typical indicators of a phishing message include the following:

- Spoofed sender and server information.
- Messages that fail integrity and security checks.
- Messages that attempt to produce a feeling of anxiousness, either due to needing something immediately, or with scenarios that attempt to frighten the recipient into becoming a victim. 

---

## 6. Attack Vectors & Root Causes
### 6.1 Common Attack Vectors

[[ITID-11111 - User Reported Phishing Message|ITID-11111]] is squarely an email-borne ITID.  The attack is 100% delivered over email.  While other message types are similar, such as Vishing messages in the #ITID-11200 family, and Smishing messages in the #ITID-11300 family, they are typically delivered over different channels and are tracked differently, while still allowing for the metrics to roll up to a general category.

### 6.2 Common Root Causes

Most organizations have email filtering in their organization, whose sole job is to evaluate messages for malicious behavior.  While the efficacy of these solutions appear to be improving rapidly, thanks to advancements in artificial intelligence (AI).  

---

## 7. MITRE ATT&CK Mapping

- [[T1566 - Phishing]]
- [[T1566.001 - Spearphishing Attachment]]
- [[T1566.002 - Spearphishing Link]]
- [[T1566.003 - Spearphishing via Service]]

---

## 8. Detection & Response Alignment
### 8.1 Detection Coverage

This ITID can be detected either by a human or a machine.

Human detection requires logic and awareness to the true intentions of an email.

Machine detection requires logic of the technical techniques and behaviors of an email message.  

### 8.2 Response Expectations

Typical response is for a single analyst to conduct the investigation throughly, inaccordance with standard operating procedures.  See section 10 for a listing of relevant administrative documentation to guide and assist.  

---

## 9. Reporting & Metrics

Incidents in this ITID are tracked weekly, monthly, quarterly, and yearly and rolled up under 'Identity Threats' for executive reporting.  The purpose is not to flinch at spikes and valleys in the individual data points, but to look at the trendlines and forecast spikes due to seasonal holidays, current events, etc.  

---

## 10. Related Content

### ITIDs
- [[ITID-11112 - Machine Detected Phishing Message]]

### Playbooks
- 

### Standard Operating Procedures
- SOP-XXXX — Name

### Detections
- [[DET-00001 - EDR Phishing Message Detection]]

### Runbooks
-  [[RB-0001 - Mass Phishing Campaign Runbook]]

### Service Level Agreements
- [[SLA-0002 - SecOps SLA with Company Employees on Phishing Response]]

---

## 11. Notes & Review History


