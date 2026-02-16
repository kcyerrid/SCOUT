---
entity_type: "itid"
itid_id: "ITID-12345"
itid_name: "Test ITID Title"
itid_category: ""
itid_parent: ""
itid_children: []
definition: "Test defintion"
scope_includes: []
scope_excludes: []
severity_guidance: "Low"
priority_guidance: ""
escalation_guidance: ""
typical_indicators: []
common_attack_vectors: []
common_root_causes: []
mapped_mitre_tactics: []
mapped_mitre_techniques: []
mapped_controls: []
related_playbooks: []
related_sops: []
related_detections: []
reporting_rollup: ""
metrics_tracked: []
status: active
review_cycle: annual
last_reviewed: ""
owner: "YOUR NAME"
tags: ""
created: "2026-02-15 14:42:08"
updated: "2026-02-15 14:43:56"
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# ITID-12345: Test ITID Title



## 1. Purpose
Describe why this ITID exists:
- What category of incidents it represents
- Why it is distinct from sibling ITIDs
- How leadership and the SOC should think about it

This should be written in clear, non-technical language.

---

## 2. Definition
Provide a precise definition of the incident type.
This definition should:
- Be stable over time
- Avoid referencing tools
- Avoid procedural language
- Be understandable by non-SOC stakeholders

---

## 3. Scope

### 3.1 Included
List scenarios or behaviors that qualify as this ITID:
- Examples of qualifying activity
- Conditions that must be met

### 3.2 Excluded
List scenarios that might appear similar but are *not* this ITID:
- Related ITIDs
- Benign behavior
- Operational issues

This prevents misclassification.

---

## 4. Severity & Escalation Guidance
Document typical expectations:
- Expected severity range
- Business impact considerations
- When escalation is required
- Regulatory or legal sensitivity

This guides analysts without hard-coding rules.

---

## 5. Indicators & Patterns
Describe **high-level signals**, not raw IOCs:
- Behavioral indicators
- Temporal patterns
- Identity or asset risk indicators
- Environmental context

This section feeds analyst intuition.

---

## 6. Attack Vectors & Root Causes
### 6.1 Common Attack Vectors
How attackers or failures typically manifest this ITID:
- Social engineering
- Misconfiguration
- Exploitation
- Abuse of legitimate functionality

### 6.2 Common Root Causes
Why this happens internally:
- Control gaps
- Visibility gaps
- Process failures
- Human factors

This feeds remediation strategy.

---

## 7. MITRE ATT&CK Mapping
List applicable tactics and techniques:
- TA0001 — Initial Access
- T1078 — Valid Accounts
- T1110 — Brute Force


This provides behavioral alignment without overfitting.

---

## 8. Detection & Response Alignment
### 8.1 Detection Coverage
Describe:
- Types of detections expected
- Visibility dependencies
- Common blind spots

### 8.2 Response Expectations
At a high level:
- Typical response actions
- Expected containment posture
- Coordination needs

Do **not** include playbook steps here.

---

## 9. Reporting & Metrics
Describe how this ITID is used in reporting:
- Executive rollups
- Trend analysis
- Risk reporting
- SOC performance metrics

Example:
> “Incidents in this ITID are tracked monthly and rolled up under ‘Identity Threats’ for executive reporting.”

---

## 10. Related Content
### Playbooks
- PB-XXXX — Name

### Standard Operating Procedures
- SOP-XXXX — Name

### Detections
- DET-XXXX — Name


---

## 11. Notes & Review History
Document:
- Known ambiguities
- Edge cases
- Changes to scope
- Lessons learned from misclassification

This section supports long-term maturity.

