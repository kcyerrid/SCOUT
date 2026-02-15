---
entity_type: campaign

campaign_name: "Suspected APT29 Spearphishing Campaign (Nov 2018)"
campaign_id: "C0021"

associated_actors: []
suspected_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]]"

attribution_confidence: "2-medium"
confidence_notes: "MITRE ATT&CK notes overlap with prior suspected APT29 activity; attribution is based on artifact/TTP overlap and vendor reporting rather than definitive public confirmation."

first_observed: "2018-11"
last_observed: "2018-11"
campaign_status: "concluded"

primary_objectives: ["espionage"]
secondary_objectives: ["initial_access"]

target_sectors: ["public_sector", "ngo", "education", "oil_and_gas", "chemical", "hospitality"]
target_regions: ["United States", "Europe", "Hong Kong", "India", "Canada"]
target_technologies: ["Windows", "email", "PowerShell", "Cobalt Strike"]

initial_access_vectors: ["spearphishing_link", "user_execution"]
key_ttp_themes: ["domain_infrastructure", "lnk_payloads", "powershell_obfuscation", "c2_over_https"]

malware_families: []
tools_used:
  - "[[30_CIPHER/05_Malware/S0154 - Cobalt Strike|S0154 - Cobalt Strike]]"

infrastructure_patterns: ["registered_domains", "compromised_domains"]
notable_victims: ["public sector and NGO targets (multiple)"]
related_incidents: []

risk_level: "medium"
impact_assessment: "Spearphishing campaign with broad public/private targeting and infrastructure acquisition; impact likely centered on espionage-driven access and follow-on exploitation."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0021/"
  - "https://www.microsoft.com/en-us/security/blog/2018/12/03/analysis-of-cyberattack-on-u-s-think-tanks-non-profits-public-sector-by-unidentified-attackers/"
  - "https://www.mandiant.com/resources/blog/not-so-cozy-suspected-apt29-phishing-campaign"

tlp_classification: "TLP:CLEAR"

created: "2026-01-03"
updated: "2026-01-03"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## Campaign Overview
**C0021** was a **November 2018** spearphishing campaign targeting public sector institutions, NGOs, education, and private-sector organizations (notably oil & gas, chemical, and hospitality). Reporting indicates substantial overlap with prior **suspected** [[30_CIPHER/03_Threat_Actors/G0016 - APT29|G0016 - APT29]] activity.

---

## Attribution Assessment
Attribution confidence is **medium**: sources cite TTP and artifact overlap with suspected APT29 operations, but public reporting does not always provide definitive victim-side confirmation.

---

## Objectives & Intent
- **Primary:** espionage-oriented access (collection potential)
- **Secondary:** foothold establishment via phishing and staged payload delivery

---

## Targeting Analysis
### Sectors Targeted
- Public sector, NGOs, education
- Oil & gas, chemical, hospitality

### Regions Targeted
- Primarily U.S. (Washington, D.C. area noted), plus Europe, Hong Kong, India, Canada

### Technologies / Platforms Targeted
- Email-based delivery → ZIP → LNK payload chain
- PowerShell for decoding/execution
- C2 over HTTP/HTTPS

---

## Campaign Tradecraft
### High-Level Tradecraft Summary
Actors registered and/or used compromised domains, delivered malicious links leading to LNK-based payloads, and used obfuscated/encoded PowerShell to extract and decode embedded payloads. C2 leveraged HTTPS on port 443 in parts of the chain.

---

## MITRE ATT&CK Alignment
### Techniques Observed
- [[T1583.001 - Domains]]
- [[T1071.001 - Web Protocols]]
- [[T1059.001 - PowerShell]]
- [[T1584.001 - Domains]]
- [[T1140 - Deobfuscate/Decode Files or Information]]
- [[T1573.002 - Asymmetric Cryptography]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1095 - Non-Application Layer Protocol]]
- [[T1027.009 - Embedded Payloads]]
- [[T1027.010 - Command Obfuscation]]
- [[T1588.002 - Tool]]
- [[T1566.002 - Spearphishing Link]]
- [[T1608.001 - Upload Malware]]
- [[T1218.011 - Rundll32]]
- [[T1204.001 - Malicious Link]]

### Notable Tradecraft Characteristics
- LNK-based embedded payload + PowerShell deobfuscation chain
- Mix of **registered** and **compromised** domains for hosting and C2

---

## Malware & Tooling
### Tools
- [[30_CIPHER/05_Malware/S0154 - Cobalt Strike|S0154 - Cobalt Strike]] (Beacon loader execution via rundll32 reported)

---

## Infrastructure & Operational Patterns
- Domain acquisition and domain compromise for hosting/c2
- SSL/TLS on TCP/443 for C2 segments

---

## Timeline of Campaign Activity (Chronos)
```chronos
- [2018-11]: Spearphishing campaign activity observed across multiple sectors and regions.
- [2018-11-19]: Vendor report published analyzing suspected APT29 phishing campaign tradecraft.
- [2018-12-03]: Microsoft analysis published on attacks against U.S. think tanks, non-profits, and public sector targets.
```

## Timeline of Campaign Activity (Markdown)
| Date | Activity |
|---|---|
| 2018-11 | Campaign activity observed |
| 2018-11-19 | Vendor report published analyzing campaign tradecraft |
| 2018-12-03 | Microsoft analysis published describing related activity |

---

## Defensive Considerations
- Block/inspect suspicious LNK delivery via archives; harden email gateway rules.
- Detect encoded/obfuscated PowerShell and unusual base64 decode routines.
- Monitor for `rundll32.exe` executing from atypical paths and unsigned DLL loaders.
- Track newly registered or suspicious lookalike domains used in lures.

---

## Analyst Notes
C0021 demonstrates high-leverage phishing tradecraft that blends infrastructure acquisition with Windows-native execution paths; detections benefit from correlating email telemetry, script logging, and egress domain reputation/age.

---

## References (APA)
- MITRE ATT&CK. (2025, April 16). *C0021 (Campaign)*. Retrieved 2026-01-03 from https://attack.mitre.org/campaigns/C0021/
- Microsoft Defender Research Team. (2018, December 3). *Analysis of cyberattack on U.S. think tanks, non-profits, public sector by unidentified attackers*. Microsoft Security Blog. Retrieved 2026-01-03 from https://www.microsoft.com/en-us/security/blog/2018/12/03/analysis-of-cyberattack-on-u-s-think-tanks-non-profits-public-sector-by-unidentified-attackers/
- Dunwoody, M., et al. (2018, November 19). *Not So Cozy: An Uncomfortable Examination of a Suspected APT29 Phishing Campaign*. FireEye / Mandiant. Retrieved 2026-01-03 from https://www.mandiant.com/resources/blog/not-so-cozy-suspected-apt29-phishing-campaign
