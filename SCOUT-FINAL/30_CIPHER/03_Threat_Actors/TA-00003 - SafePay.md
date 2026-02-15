---
entity_type: threat_actor
actor_name: "SafePay"
common_name: "SafePay"
actor_id: ""
actor_type: "Ransomware threat actor associated with double-extortion operations (reported)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2024-09-01"
last_seen: ""
status: "Active (reported)"
motivations: ["Financial gain"]
objectives:
  - "Encrypt victim systems and disrupt operations to coerce payment (reported)"
  - "Steal data and threaten public release to increase extortion leverage (double extortion; reported)"
  - "Exploit weaknesses in externally exposed remote access and identity controls to gain entry (reported)"
victimology_summary: "SafePay is a ransomware threat actor first publicly observed/identified in late 2024 (often described as emerging around September–November 2024) and reported as highly active through 2025. Multiple sources describe SafePay as a double-extortion operator (data theft + encryption) with broad, cross-industry targeting globally. Public reporting highlights high-impact incidents affecting large service providers and supply-chain-adjacent organizations, and describes recurring initial-access themes involving external remote access/VPN exposure, weak credentials/misconfigurations, and high-pressure social-engineering tactics (e.g., email bombing and phone-based scams) in some cases."
target_sectors:
  - "Managed Service Providers (MSPs) (reported)"
  - "IT services / distribution / supply-chain-adjacent organizations (reported)"
  - "Manufacturing (reported)"
  - "Healthcare (reported)"
  - "Education (reported)"
  - "Government contractors / service providers (reported)"
target_regions:
  - "Global"
related_groups: []
malware:
  - "[[30_CIPHER/05_Malware/SafePay]]"
  - "[[30_CIPHER/05_Malware/LockBit]]"
tools: []
infrastructure:
  - "[[Double extortion leak site]]"
  - "[[Ransom note]]"
  - "[[External remote services]]"
  - "[[VPN access]]"
  - "[[Social engineering pressure tactics]]"
  - "[[Data staging]]"
ttps:
  - "[[20_Entities/07_TTPs/T1566 - Phishing]]"
  - "[[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Voice Phishing]]"
  - "[[20_Entities/07_TTPs/T1133 - External Remote Services]]"
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1078 - Valid Accounts]]"
  - "[[20_Entities/07_TTPs/T1110 - Brute Force]]"
  - "[[20_Entities/07_TTPs/T1560 - Archive Collected Data]]"
  - "[[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]"
  - "[[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]"
  - "[[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]"
notable_claims:
  - "Described by multiple sources as a fast-rising, high-tempo ransomware operator emerging in late 2024 and highly active through 2025 (reported)"
  - "Frequently characterized as a double-extortion actor (reported)"
  - "Some reporting assesses SafePay uses code derived from or modified from [[30_CIPHER/05_Malware/LockBit]] leaks/source (reported)"
  - "Some reporting highlights aggressive social-engineering pressure (email bombing and phone scams/vishing) as a differentiator (reported)"
intel_sources:
  - "Huntress — It's Not Safe to Pay SafePay (2024-11-14): https://www.huntress.com/blog/its-not-safe-to-pay-safepay"
  - "Check Point — SafePay Ransomware: An Emerging Threat in 2025: https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/safepay-ransomware/"
  - "Acronis TRU — SafePay ransomware: The fast-rising threat targeting MSPs (2025-07-08): https://www.acronis.com/en/tru/posts/safepay-ransomware-the-fast-rising-threat-targeting-msps/"
  - "Bitdefender Business Insights — SafePay ransomware attacks: TTPs (2025-09-04): https://www.bitdefender.com/en-us/blog/businessinsights/safepay-ransomware-attacks-ttps"
  - "Barracuda — SafePay: Email bombs, phone scams and really big ransoms (2025-07-25): https://blog.barracuda.com/2025/07/25/safepay--email-bombs--phone-scams--and-really-big-ransoms"
  - "NCC Group — Weak Passwords Led to (SafePay) Ransomware…Yet Again: https://www.nccgroup.com/research-blog/weak-passwords-led-to-safepay-ransomware-yet-again/"
  - "TechRadar — Ingram Micro incident coverage (2025-07): https://www.techradar.com/pro/security/ransomware-gang-sets-deadline-to-leak-huge-cache-of-stolen-ingram-micro-data"
tags:
  - "threat-actor"
  - "ransomware"
  - "double-extortion"
  - "safepay"
created: "2025-12-29"
last_modified: "2025-12-29"
---

# SafePay

## 1. BLUF / Executive Summary
SafePay is a ransomware threat actor reported to have **emerged in late 2024** and become **highly active through 2025**. Public reporting consistently describes **double extortion** (data theft plus encryption) and broad, cross-industry victimization. Several sources highlight recurring entry conditions involving **external remote access/VPN exposure**, **weak credentials and misconfigurations**, and (in some cases) aggressive social-engineering pressure such as **email bombing and phone-based scams** to accelerate victim response.

## 2. Attribution Notes
- “SafePay” is tracked as a ransomware *brand/operation* in public reporting; operator identity, sponsor, and geography are **not publicly confirmed** in the cited sources.
- Some reporting infers possible regional ties from operational choices (e.g., language/environment checks), but this is not treated as definitive attribution.
- Some vendors assess SafePay’s encryptor may be derived from or influenced by leaked [[30_CIPHER/05_Malware/LockBit]] materials; this is included as an **assessment**, not a proven lineage.

## 3. Motivations & Objectives
- **Primary motivation:** financial gain via extortion.
- **Objectives (reported):**
  - Encrypt systems to disrupt operations and increase urgency ([[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]).
  - Steal and stage data to enable leak-site pressure ([[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]).
  - Leverage externally exposed access paths and credential weaknesses to gain entry ([[20_Entities/07_TTPs/T1133 - External Remote Services]], [[20_Entities/07_TTPs/T1078 - Valid Accounts]]).

## 4. Targeting Profile
- **Geography:** global, with notable large-organization impacts reported in 2024–2025.
- **Sectors (representative, reported):** MSPs, IT distribution/supply-chain-adjacent organizations, manufacturing, healthcare, education, and large service providers/government contractors.
- **Targeting style:** opportunistic-at-scale within high-impact enterprise environments, including organizations whose disruption can cascade to downstream customers.

## 5. Tradecraft Overview
- **Initial access themes (reported):**
  - Exploitation or abuse of weaknesses in internet-facing systems and remote access paths ([[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]], [[20_Entities/07_TTPs/T1133 - External Remote Services]]).
  - Credential-driven access, including valid credential use and weak-password exposure ([[20_Entities/07_TTPs/T1078 - Valid Accounts]], [[20_Entities/07_TTPs/T1110 - Brute Force]]).
  - Social-engineering pressure and interaction, including voice phishing/vishing reported in some cases ([[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Voice Phishing]]).
- **Extortion model:** data theft + encryption with leak-site pressure ([[Double extortion leak site]]).
- **Operational tempo:** described by multiple sources as fast-moving, with compressed timelines from intrusion to encryption in some incidents.

## 6. MITRE ATT&CK Mapping
- Access / Social Engineering
  - [[20_Entities/07_TTPs/T1566 - Phishing]]
  - [[20_Entities/07_TTPs/T1598.003 - Phishing for Information: Voice Phishing]]
  - [[20_Entities/07_TTPs/T1133 - External Remote Services]]
  - [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
  - [[20_Entities/07_TTPs/T1078 - Valid Accounts]]
  - [[20_Entities/07_TTPs/T1110 - Brute Force]]
- Collection / Staging / Exfiltration (high-level, reported)
  - [[20_Entities/07_TTPs/T1560 - Archive Collected Data]]
  - [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]]
  - [[20_Entities/07_TTPs/T1041 - Exfiltration Over C2 Channel]]
- Impact
  - [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]

## 7. Malware & Tools Used
- [[30_CIPHER/05_Malware/SafePay]] — ransomware family/operator label described in multiple incident and threat intel write-ups.
- [[30_CIPHER/05_Malware/LockBit]] — cited by some sources as a potential code lineage influence (assessment; not universally stated).
- Public sources frequently focus more on **entry conditions and extortion mechanics** than on a stable, uniquely named toolchain; therefore, tools are left **blank** unless consistently corroborated.

## 8. Infrastructure Patterns
- [[Double extortion leak site]] used to pressure victims with publication threats (reported).
- [[External remote services]] and [[VPN access]] as recurring entry/abuse themes (reported).
- [[Social engineering pressure tactics]] including email bombing and phone-based scams reported in some cases (reported).
- [[Data staging]] and archival behavior preceding exfiltration (reported).
- [[Ransom note]] conventions exist in incident reporting, but details are not enumerated here to avoid operational specificity.

## 9. Campaign History
- **2024-09 to 2024-11 (reported):** multiple sources describe SafePay emerging/being identified in this period; early incident observations were published in late 2024.
- **2025 (reported):** multiple vendor reports describe rapid growth in claimed victims and notable high-impact incidents affecting large organizations and MSP-adjacent environments.
- **2025-07 (reported):** public incident coverage highlights a disruptive ransomware event affecting a major IT distribution organization, framed as a SafePay-attributed operation in reporting.
- **2025-07 to 2025-09 (reported):** vendor write-ups describe SafePay’s sustained high activity levels and evolving operational patterns.

## 10. Known Indicators
[]

## 11. Defensive Recommendations
- Reduce exposure of remote entry paths aligned to [[20_Entities/07_TTPs/T1133 - External Remote Services]] and [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]] through rigorous patching, configuration management, and continuous monitoring of externally accessible services.
- Treat identity hardening as critical against [[20_Entities/07_TTPs/T1078 - Valid Accounts]] and [[20_Entities/07_TTPs/T1110 - Brute Force]]: prioritize strong authentication controls, credential hygiene, and anomaly detection around remote access.
- Build detections for pre-encryption staging aligned to [[20_Entities/07_TTPs/T1074.001 - Data Staged: Local Data Staging]] and [[20_Entities/07_TTPs/T1560 - Archive Collected Data]] (unusual bulk access, anomalous compression/staging patterns, and atypical outbound transfers).
- Plan for extortion response aligned to [[20_Entities/07_TTPs/T1486 - Data Encrypted for Impact]]: ensure resilient backups, tested recovery, and clear decision workflows for legal, communications, and containment.

## 12. Analyst Notes
- SafePay reporting evolves quickly; treat victim counts, rankings, and claimed incidents as **volatile** unless corroborated by multiple independent sources.
- “Brand vs. actor” ambiguity is common in ransomware tracking; use conservative phrasing when mapping SafePay to specific incidents unless a source provides strong linkage.

## 13. Further Reading / External Resources
- Huntress (2024): https://www.huntress.com/blog/its-not-safe-to-pay-safepay
- Check Point (2025): https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/safepay-ransomware/
- Acronis TRU (2025): https://www.acronis.com/en/tru/posts/safepay-ransomware-the-fast-rising-threat-targeting-msps/
- Bitdefender (2025): https://www.bitdefender.com/en-us/blog/businessinsights/safepay-ransomware-attacks-ttps
- Barracuda (2025): https://blog.barracuda.com/2025/07/25/safepay--email-bombs--phone-scams--and-really-big-ransoms
- NCC Group (case study lens): https://www.nccgroup.com/research-blog/weak-passwords-led-to-safepay-ransomware-yet-again/

## 14. References
1. Huntress. “It’s Not Safe to Pay SafePay.” 2024-11-14. https://www.huntress.com/blog/its-not-safe-to-pay-safepay
2. Check Point. “SafePay Ransomware: An Emerging Threat in 2025.” (Accessed 2025). https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/safepay-ransomware/
3. Acronis Threat Research Unit. “SafePay ransomware: The fast-rising threat targeting MSPs.” 2025-07-08. https://www.acronis.com/en/tru/posts/safepay-ransomware-the-fast-rising-threat-targeting-msps/
4. Bitdefender Business Insights. “SafePay Ransomware Attacks: TTPs.” 2025-09-04. https://www.bitdefender.com/en-us/blog/businessinsights/safepay-ransomware-attacks-ttps
5. Barracuda. “SafePay: Email bombs, phone scams and really big ransoms.” 2025-07-25. https://blog.barracuda.com/2025/07/25/safepay--email-bombs--phone-scams--and-really-big-ransoms
6. NCC Group. “Weak Passwords Led to (SafePay) Ransomware…Yet Again.” (Accessed 2025). https://www.nccgroup.com/research-blog/weak-passwords-led-to-safepay-ransomware-yet-again/
7. TechRadar. “Ransomware gang sets deadline to leak huge cache of stolen Ingram Micro data.” 2025-07 (published date varies by update). https://www.techradar.com/pro/security/ransomware-gang-sets-deadline-to-leak-huge-cache-of-stolen-ingram-micro-data
