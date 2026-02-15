---
entity_type: mitre_technique

technique_id: ""              # e.g., T1059
subtechnique_id: ""           # e.g., T1059.001 (optional or empty string)
technique_name: ""            # official MITRE ATT&CK technique name

tactic: []                    # e.g., ["Execution", "Persistence"]
platforms: []                 # windows | linux | macos | saas | cloud | network | containers
datasources: []               # per MITRE: e.g., "Process Execution", "Network Traffic: Network Connection Creation"

mitre_version: ""             # e.g., 17.0
attack_spec_version: ""       # schema version
attack_source: Enterprise      # Enterprise, Mobile, ICS
deprecated: false
revoked: false

associated_threat_actors: []   # actor entities referencing this technique
associated_malware: []         # malware using this technique
associated_campaigns: []       # campaigns leveraging this technique
related_techniques: []         # parent, child, or “related” MITRE techniques

detection_priority:
  - Low
  - Medium
  - High
  - Critical

detection_maturity: ""         # None | Minimal | Moderate | Strong
threat_score: 1                # numeric scoring for triage, enrichment, or ranking

created:  
updated:  

contributors: []
tags:
  - mitre
  - technique
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# {{technique_name}} ({{technique_id}}{{#if subtechnique_id}} / {{subtechnique_id}}{{/if}})

## 1. Summary
Provide a concise description of the technique:
- What the technique achieves for the adversary.
- Why adversaries commonly use it.
- High-level operational impact.
- Relation to typical intrusion workflows.

## 2. Technical Overview
Explain how the technique works from a technical perspective:
- APIs, processes, commands, protocols used
- Prerequisites or required access level
- Common environments where technique is most effective (Windows, Linux, SaaS, cloud, containers)
- Typical artifacts generated

## 3. Subtechnique Considerations
Describe:
- How subtechniques differ from the parent technique
- Which subtechniques are most relevant to your environment
- Known variations (e.g., OS-specific, SaaS-specific, cloud-provider-specific)

## 4. Procedure Examples
Document real-world examples of how adversaries use the technique:
- Commands, scripts, and tooling used
- Infrastructure patterns
- Sequence of events during execution
- Behavioral indicators analysts can observe  
*(Avoid actual malicious content; use redacted/representative examples.)*

## 5. Detection Guidance
Describe how this technique should be detected:
- Required telemetry sources (SIEM, EDR, NDR, cloud logs, SaaS logs)
- Key fields and signals to monitor
- Behavioral patterns associated with this technique
- Common detection logic elements (KQL, SPL, EQL, Sigma pseudocode)
- Known false positives and tuning approaches

### Data Source Notes
Add details per data source:
- Coverage quality  
- Gaps or blind spots  
- Required configuration changes  

## 6. Response Guidance
Outline recommended SOC analyst actions when activity involving this TTP is observed:
- Immediate triage steps
- Validation instructions
- Escalation criteria
- Associated response actions (link to Response Action entities)
- Forensics considerations

## 7. Related ATT&CK Content
Cross-reference:
- Parent/child techniques
- Shared technique clusters
- Related ATT&CK mitigations
- Related ATT&CK data sources

## 8. SOC Relevance
Explain why this technique matters to your organization:
- Frequency of occurrence
- Historical incidents involving this technique
- Maturity of detection coverage
- Environmental exposure (cloud, SaaS, endpoints)

## 9. Threat Actor Usage
List known adversaries using the technique:
- Actor name (link to Threat Actor entities)
- How they prefer to use the technique
- Distinct TTP fingerprints or patterns
- Confidence levels for attribution

## 10. Campaign Usage
Document campaigns where this technique has appeared:
- Campaign name (link to Campaign entities)
- Stage(s) where technique is used
- Infrastructure or tooling patterns

## 11. Malware Usage
Identify malware families/variants connected to this technique:
- Malware family name (link to Malware entities)
- Payload behaviors associated with this technique
- Command-line or API usage details

## 12. Mitigations
List effective mitigations:
- Preventative controls
- Configuration hardening
- Access restrictions
- Network segmentation
- Endpoint protection policies
- Cloud configuration controls
- Vendor-specific best practices

## 13. Testing & Validation
Describe how to validate detection coverage for this technique:
- Atomic Red Team guidance
- Caldera or adversary simulation
- Manual test procedures
- Red team collaboration notes

Include:
- Preconditions
- Required roles/tools
- Expected outcomes
- Validation success criteria

## 14. References
Provide sources for deeper research:
- MITRE ATT&CK technique page
- Vendor analysis
- Threat intel reports
- Conference presentations
- Detection engineering resources
- Academic or community research

## 15. Notes
General notes, open questions, or future improvements:
- Known gaps in organizational detection coverage
- Ideas for upcoming tuning or playbook updates
- Pending test cases
