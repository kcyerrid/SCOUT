---
entity_type: intel_ttp

technique_id: ""                    # e.g., T1059
subtechnique_id: ""                 # e.g., T1059.003 or empty string
technique_name: ""                  # MITRE technique name

actor_or_group: ""                  # primary threat actor OR campaign using this TTP
associated_actors: []               # additional actors known to use this procedure
associated_campaigns: []            # campaigns using this TTP

attribution_confidence:             # low | moderate | high
- 3-low
- 2-medium
- 1-high

first_observed: ""
last_observed: ""

operational_style: 
- stealthy
- noisy
- hands-on keyboard
- automated
- hybrid
sophistication_level: 
- 4-low
- 3-medium
- 2-high
- 1-very_high

procedure_variants: []              # variations of how actor uses this technique
tools_used: []                      # living-off-the-land, malware families, scripts
infrastructure_used: []             # C2, VPNs, domains (link to IOCs, not raw values)

lateral_movement_relevance: false
persistence_relevance: false
collection_relevance: false
impact_relevance: false

related_iocs: []                    # atomic IOC links
related_malware: []                 # malware entities used to implement this technique
related_tools: []                   # tool entities tied to this TTP
related_incidents: []               # internal incidents reflecting this actor technique

tactic: []                           # ATT&CK tactical category
mitre_version: ""
attack_source: Enterprise

detection_notes: ""                 # high-level detection considerations
response_notes: ""                  # high-level response considerations

intel_sources: []                   # vendor, government, internal research
tlp_classification: 
- TLP:RED 
- TLP:AMBER
- TLP:GREEN 
- TLP:CLEAR 

created: 
updated: 

tags:
  - intel_ttp
  - mitre
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# Intel TTP: {{technique_name}} ({{technique_id}}{{#if subtechnique_id}} / {{subtechnique_id}}{{/if}})

## 1. Summary
Briefly describe:
- How this specific threat actor or campaign uses the technique
- Why this variation matters
- Any unique characteristics compared to typical MITRE ATT&CK definitions

Emphasize “actor-specific flavor” of the procedure.

---

## 2. Background & Attribution
### 2.1 Actor or Campaign
Describe the threat actor(s) or campaign(s) that use this procedure:
- Primary actor or group
- Historical usage
- Operational motivations
- Attribution confidence and rationale

### 2.2 Intelligence Context
Explain:
- When this technique first appeared in the actor’s operations
- Whether its usage has evolved over time
- Whether other actors share similar procedure variants

---

## 3. Technical Procedure Overview
Explain how the actor **actually performs** the technique:
- Commands, scripts, or tooling patterns  
- Infrastructure specifics (C2 hosts, cloud services, domain themes)  
- Pre-conditions or required privileges  
- Step-by-step flow of execution (without sensitive payloads)  

Focus on the tradecraft sequence, not raw IOCs.

---

## 4. Procedure Variants (Actor-Specific)
List known variations:
- Variant A — description
- Variant B — description
- Variant C — OS-specific variation


Notes to include:
- Operating system differences  
- Cloud-specific variants (Azure, AWS, etc.)  
- SaaS / identity abuse variants  
- EDR evasion patterns  

---

## 5. Tactic & Technique Mapping
### 5.1 ATT&CK Tactics
List associated ATT&CK tactics (e.g., Privilege Escalation, Defense Evasion).

### 5.2 ATT&CK Techniques
Document the exact ATT&CK technique/subtechnique IDs used:
- TXXXX — Technique Name
- TYYYY — Technique Name

---

## 6. Tools, Scripts & Malware Used
### 6.1 Living-off-the-Land
Describe any LOLBins (PowerShell, WMI, CMD, bash, python).

### 6.2 Malware & Implants
List malware families enabling this TTP (linked to Malware entities).

### 6.3 Supporting Tools
List helper scripts, credential utilities, tunneling tools, etc.

---

## 7. Infrastructure & IOCs
Describe actor-specific infrastructure patterns:
- C2 providers  
- VPNs or proxy networks  
- Domain registration habits  
- Cloud service abuse  

Then link to atomic IOC entries:
- IOC:IP (link)
- IOC:Domain (link)
- IOC:Hash (link)


Do **not** embed raw IOCs directly here.

---

## 8. Detection Guidance (Actor-Specific)
Explain how to detect *this actor's version* of the technique:
- High-value telemetry  
- Detection logic characteristics  
- Behavior signatures  
- Timing or sequencing clues  
- Cloud/SaaS log indicators  
- Common false positives or tuning considerations  

Highlight differences from generic MITRE detections.

---

## 9. Response Guidance (Actor-Specific)
Provide IR guidance:
- Immediate triage steps  
- What evidence this actor typically modifies or deletes  
- Foreseeable lateral movement from this technique  
- Typical escalation patterns  
- Containment recommendations  

Actor-specific IR nuance is key.

---

## 10. Historical Usage Examples
Document notable appearances of this TTP:
- Internal incidents  
- Public breach reporting  
- Vendor intel reports  
- Industry-wide campaigns  

Provide a timeline or table if useful.

---

## 11. Impact & Risk Assessment
Describe risks associated with this actor’s implementation:
- Potential business impact  
- Likelihood of recurrence  
- Escalation potential  
- Geographic or sector-specific relevance  

---

## 12. Intelligence Gaps & Outstanding Questions
Record unknowns:
- Incomplete patterns  
- Unconfirmed hypotheses  
- Areas requiring further collection or monitoring  

---

## 13. References
List all supporting sources:
- Vendor writeups  
- Government advisories  
- AT&T, CISA, MSRC, Symantec, Mandiant, CrowdStrike, etc.  
- Threat research blogs  
- Internal intel reports  

