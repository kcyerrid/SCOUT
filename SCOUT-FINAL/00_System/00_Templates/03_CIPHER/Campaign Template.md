---
entity_type: campaign

campaign_name: ""
campaign_id: ""                     # internal SCOUT ID: CMP-YYYY-###
aliases: []                         # alternative or vendor campaign names

attribution: []                     # suspected threat actors (links to Threat Actor entities)
attribution_confidence: ""             # low | moderate | high

tlp_classification: ""                # TLP:RED | TLP:AMBER | TLP:GREEN | TLP:CLEAR

admiralty_source_reliability: ""    # A–F

admiralty_information_credibility: ""   # 1–6

first_seen: ""
last_seen: ""
activity_peak: ""                   # e.g., Q3 2023

target_sectors: []
target_regions: []
target_technologies: []             # technologies, systems, or applications targeted

tactics: []                         # ATT&CK tactics
techniques: []                      # ATT&CK technique IDs
procedures: []                      # freeform behaviors or steps observed

malware_used: []                    # primary malware families
tools_used: []                      # COTS or LOLBins

iocs: []                            # link to atomic IOC notes
infrastructure: []                  # IPs, domains, cloud assets, VPNs, hosting patterns

related_incidents: []               # internal SCOUT incidents tied to this campaign
related_cases_external: []          # public cases or reports

campaign_summary: ""                # short executive summary (1–3 sentences)

created: 
updated: 

contributors: []
tags: []
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# {{campaign_name}}

## 1. Executive Summary
Provide a short (1–3 paragraph) summary describing:
- What the campaign attempted to accomplish
- Who it targeted and why
- Why it matters to your organization or sector
- The suspected threat actor(s) behind it

Keep this high-level and readable by executives.

---

## 2. Attribution Notes
Discuss attribution and confidence:

### 2.1 Suspected Threat Actors
List threat actors with links to their profiles:
- Threat Actor Name (link)
- Threat Actor Name (link)


### 2.2 Confidence Assessment
Explain why attribution is:
- **High:** strong infrastructure overlap, unique malware, consistent TTPs  
- **Moderate:** partial overlap, ambiguous IOCs  
- **Low:** speculative, conflicting vendor reports  

---

## 3. Campaign Timeline
Describe the evolution of the campaign:

- **Initial Observations** – when it first appeared  
- **Escalation / Peak Activity** – months or quarters  
- **Recent Behavior** – whether it is ongoing, dormant, or resurfacing  

Add a Chronos Timeline if desired:

```chronos
- [2020] Event 1

- [2020-01-04~2020-01-14] Event 2

- [2020-01-10] Event 3

@ [2020-01-06~2020-01-10] Period 1
```

---

## 4. Targeting Profile
Describe who the campaign focused on:

### 4.1 Industries / Sectors
- Financial Services  
- Technology  
- Government  
- Healthcare  

### 4.2 Geographic Regions
- North America  
- EMEA  
- APAC  

### 4.3 Technologies & Platforms Targeted
- Email (phishing)  
- VPN gateways  
- Azure AD  
- SaaS suite  
- On-prem infrastructure  

Explain any targeting rationale.

---

## 5. Tactics, Techniques & Procedures (TTPs)
### 5.1 MITRE ATT&CK Techniques
Document all relevant ATT&CK mappings:
- TXXXX – Technique Name
- TYYYY – Technique Name


### 5.2 Procedures (Step-by-Step Behaviors)
Describe observed procedures:
- Initial access patterns  
- Privilege escalation techniques  
- Persistence mechanisms  
- Lateral movement methods  
- Defense evasion  
- Exfiltration flows  

Add details about unique tradecraft.

---

## 6. Malware & Tools Used
### 6.1 Malware
Identify malware families:
- MalwareFamily1 – role, capabilities
- MalwareFamily2 – role, capabilities


### 6.2 Tools
Include COTS tools, LOLBins, or cloud-tooling reused:
- ToolName – purpose in this campaign
- ToolName – how it is executed or abused


---

## 7. Infrastructure Profile
Document adversary infrastructure:
- C2 servers  
- Proxy networks  
- VPNs  
- Cloud services  
- Domain registration patterns  
- Hosting providers  
- SSL certificate anomalies  

List specific IOCs (linked atomically).

---

## 8. IOCs (Indicators of Compromise)
Reference atomic IOC notes:
- IOC:IP: 192.x.x.x (link)
- IOC:Domain: malicious-domain[.]com (link)
- IOC:URL: https://malicious[.]example (link)
- IOC:Hash: SHA256-xxxx (link)


Do **not** overload the campaign profile with raw IOC lists.  
Keep it link-only.

---

## 9. Defensive Recommendations
Provide actionable advice:
- Detection engineering priorities  
- High-value telemetry requirements  
- Hunting hypotheses  
- Suggested improvements to SOC processes  
- Visibility enhancements  
- Recommended response guidance  

Highlight the TTPs that pose the highest risk to your environment.

---

## 10. Historical Incidents
Link internal incidents and external reporting:

### 10.1 Internal Incidents
- INC-YYYYMMDD-### (link)
- INC-YYYYMMDD-### (link)


### 10.2 External Cases
Vendor reports or advisories explaining real-world impacts.

---

## 11. Analyst Notes
Internal analyst commentary:
- Open intelligence questions  
- Disputed assessments  
- Emerging patterns  
- Forward-looking hypotheses  

---

## 12. References
List all relevant citations:
- Vendor reports  
- ISAC/ISAO bulletins  
- Blog posts  
- MITRE ATT&CK  
- Research papers  

