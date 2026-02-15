---
entity_type: context_pack
context_type: threat_actor
actor_name: ""
context_pack_id: ""
tlp_classification:
  - TLP:AMBER
created: ""
updated: ""
maintainer: ""
source_scope: "public"
confidence_gate: "speculative"   # established | probable | plausible | speculative
notes:
  - "Authoritative evidence pack for canonical Threat Actor generation."
  - "MITRE ATT&CK is treated as a high-confidence source for actor identifiers and naming."
  - "Confidence ratings favor operationally serviceable intelligence over absolute certainty."
---

# Context Pack — Threat Actor — <actor_name>

## 1. Confidence Framework

### Confidence Levels

| Level | Definition |
|------|------------|
| **Established** | Strongly corroborated by multiple reliable sources; unlikely to materially change |
| **Probable** | Supported by credible sources with minor gaps or indirect corroboration |
| **Plausible** | Reasonable analytic judgment based on limited, emerging, or indirect evidence |
| **Speculative** | Hypothesis or early signal; included for tracking, not decision-making |

### Operational Rules

- **Confidence Gate ≥ Probable**
  - Generator may populate **full Threat Actor YAML** using supported facts.
- **Confidence Gate = Plausible**
  - Generator may populate YAML **selectively**, with explicit caveats in Analyst Notes.
- **Confidence Gate = Speculative**
  - Generator may populate **full Threat Actor YAML** using supported facts.
- **MITRE ATT&CK Rule**
  - MITRE ATT&CK Threat Actor IDs are **Established confidence** by default and MUST be used for `actor_id` when present.

---

## 2. Canonical YAML Candidate  
*(Populate only fields supported by Established, Probable, or Plausible facts)*

```yaml
entity_type: threat_actor

actor_name: ""
aliases: []
actor_id: ""        # REQUIRED: Use MITRE ATT&CK Threat Actor ID if available

nation_state: "unknown"
sponsor_type:
- unknown
motivation:
- other

attribution_confidence:
- 3-low
first_identified: "unknown"
active_period: "unknown"

target_sectors: []
target_regions: []
target_technologies: []

ttp_profile: []
malware_used: []
tools_used: []
infrastructure_profile: []

associated_campaigns: []
related_incidents: []

risk_level: "unknown"
threat_score: 1

intel_sources: []
tlp_classification: "unknown"
```

## 3. Confirmed Facts (5–10)

Each fact MUST include:

- A confidence rating (**Established / Probable / Plausible / Speculative**)
- At least one citation
- Clear, testable language
- **Fact 1:**  
    [Established] [Source: MITRE ATT&CK]
- **Fact 2:**  
    [Probable] [Source: ]
- **Fact 3:**  
    [Probable] [Source: ]
- **Fact 4:**  
    [Plausible] [Source: ]
- **Fact 5:**  
    [Plausible] [Source: ]
- **Fact 6 (optional):**  
    [Speculative] [Source: ]
- **Fact 7 (optional):**  
    [Established / Probable / Plausible / Speculative] [Source: ]

---

## 4. Analytic Assessments

Assessments synthesize facts into judgments. Each assessment MUST include:

- Confidence rating
- Supporting sources
- What evidence would raise confidence
- **Assessment 1:**  
    [Probable] [Source: MITRE ATT&CK; ]  
    _Rationale:_  
    _Confidence Drivers:_  
    _What would raise confidence:_
    
- **Assessment 2:**  
    [Plausible] [Source: ]  
    _Rationale:_  
    _Confidence Drivers:_  
    _What would raise confidence:_
    
- **Assessment 3 (optional):**  
    [Speculative] [Source: ]  
    _Rationale:_  
    _Confidence Drivers:_  
    _What would raise confidence:_
    

---

## 5. References

### 5.1 Full Citations (APA Preferred)

- MITRE ATT&CK. (Year). _Threat Actor: <Name>_. MITRE. [https://attack.mitre.org/](https://attack.mitre.org/)
- Author/Org. (Year, Month Day). _Title_. Publisher/Site. URL

### 5.2 Vendor / Advisory URLs

- Vendor/Org — Title — URL
- Vendor/Org — Title — URL

---

## 6. Change Log

- **YYYY-MM-DD:** Initial context pack created.
- **YYYY-MM-DD:** Replaced Low/Moderate/High with Established/Probable/Plausible/Speculative.
- **YYYY-MM-DD:** Updated operational confidence gating rules.