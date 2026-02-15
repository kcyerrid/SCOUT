---
entity_type: campaign

campaign_name: "Salesforce Data Exfiltration"
campaign_id: "C0059"

associated_actors: []
suspected_actors: []

attribution_confidence: "3-high"
confidence_notes: "Attribution to the financially motivated clusters tracked publicly as UNC6040 (initial access + data theft) and UNC6240 (follow-on extortion claiming the “ShinyHunters” name) is supported by authoritative reporting (FBI IC3 CSA; Google Threat Intelligence Group) and reflected in MITRE’s campaign description. Links to the broader “The Com” ecosystem are assessed as plausible overlaps in infrastructure/TTPs rather than confirmed operational coordination."

first_observed: "2024-10"
last_observed: "2025-09"
campaign_status: "unknown"

primary_objectives:
  - "data_theft"
  - "extortion"
secondary_objectives:
  - "financial_gain"
  - "reputation_damage"
  - "business_disruption"

target_sectors: []
target_regions:
  - "Global"
target_technologies:
  - "Salesforce (CRM instances)"
  - "Salesforce Connected Apps / OAuth token authorization"
  - "Salesforce Data Loader (legitimate tool abused or imitated)"
  - "Okta (credential harvesting / follow-on access)"
  - "Microsoft 365 (follow-on access)"

initial_access_vectors:
  - "Spearphishing Voice (vishing) / phone-based social engineering"
  - "Cloud Application Integration abuse (malicious connected app authorization)"
  - "Valid Accounts (credential and MFA code capture; OAuth token issuance)"

key_ttp_themes:
  - "IT-support impersonation and call-center social engineering (vishing)"
  - "Malicious/modified 'connected app' authorization to obtain OAuth-based access"
  - "Bulk export via Salesforce APIs / Data Loader-like automation"
  - "Use of Tor and commercial VPN infrastructure to proxy interactions and collection"
  - "Delayed extortion following theft; extortion actor claiming “ShinyHunters” branding"

associated_ttps:
  - "T1598.004 - Spearphishing Voice"
  - "T1656 - Impersonation"
  - "T1036 - Masquerading"
  - "T1671 - Cloud Application Integration"
  - "T1585 - Establish Accounts"
  - "T1585.002 - Email Accounts"
  - "T1586.002 - Email Accounts"
  - "T1587.001 - Malware"
  - "T1588.002 - Tool"
  - "T1059.006 - Python"
  - "T1083 - File and Directory Discovery"
  - "T1213.004 - Customer Relationship Management Software"
  - "T1020 - Automated Exfiltration"
  - "T1567 - Exfiltration Over Web Service"
  - "T1090 - Proxy"
  - "T1090.003 - Multi-hop Proxy"
  - "T1608.005 - Link Target"
  - "T1078.002 - Domain Accounts"

malware_families: []
tools_used:
  - "[[Salesforce Data Loader]]"
  - "[[Mullvad VPN]]"
  - "[[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]"

infrastructure_patterns:
  - "[[Voice Phishing]]"
  - "[[Helpdesk / Call Center Impersonation]]"
  - "[[Connected App Abuse]]"
  - "[[OAuth Token Abuse]]"
  - "[[Phishing Panels]]"
  - "[[Tor Exit Nodes]]"
  - "[[Commercial VPN Abuse]]"
  - "[[Extortion Email]]"

notable_victims: []
related_incidents: []

risk_level: "high"
impact_assessment: "Financially motivated actors used vishing-driven social engineering and malicious connected-app authorization to gain OAuth-backed access to corporate Salesforce instances, enabling bulk API-based exports of CRM data followed by extortion pressure (sometimes delayed) leveraging stolen information."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0059/"
  - "https://www.ic3.gov/CSA/2025/250912.pdf"
  - "https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion"
  - "https://cyberscoop.com/google-unc6040-salesforce-attacks/"
  - "https://www.mitiga.io/blog/how-threat-actors-used-salesforce-data-loader-for-covert-api-exfiltration"

tlp_classification: "TLP:CLEAR"

created: "2026-01-10"
updated: "2026-01-10"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Salesforce Data Exfiltration (C0059)

## 1. Campaign Overview
Salesforce Data Exfiltration is a cybercrime campaign in which financially motivated actors used **voice phishing (vishing)** and **IT-support impersonation** to trick employees (often in support/call-center contexts) into actions that granted access to **corporate Salesforce CRM instances**. Rather than exploiting a Salesforce platform vulnerability, reporting describes a workflow centered on **malicious connected-app authorization** and the abuse (or imitation) of **Salesforce Data Loader**-like tooling to perform **bulk exports via Salesforce APIs**.

Following theft, some victims received **extortion demands** attributed to a separate actor cluster that claimed the “**ShinyHunters**” name. Reporting also notes plausible overlap in infrastructure/TTPs with actors associated with the broader **“The Com”** ecosystem, while cautioning that overlap does not necessarily imply direct operational coordination.

## 2. Attribution Assessment
This campaign is attributed in authoritative reporting to **tracked criminal clusters** rather than a single MITRE Enterprise Group ID:
- **UNC6040**: initial access via vishing/social engineering; connected-app authorization; bulk data theft.
- **UNC6240** (as described in MITRE’s campaign narrative): follow-on extortion actor claiming “ShinyHunters” branding.

Overlap with the broader **“The Com”** ecosystem is discussed as plausible based on infrastructure/TTP similarities, but sources treat this as **assessment** rather than a confirmed direct relationship.

**Attribution Confidence: 3-high**

## 3. Objectives & Intent
Primary intent aligns with **data theft → extortion leverage**:
- Rapid acquisition of CRM data (customer and business records) through bulk export.
- Monetization via direct extortion demands, including threats of public release.

Secondary effects include **reputational damage** and **business disruption** driven by public exposure threats and incident response burden.

## 4. Targeting Analysis

### Sectors Targeted
Public reporting describes targeting across multiple organizations (often multinational), but does not consistently enumerate sectors in the core sources listed here.

### Regions Targeted
- Global (campaign described as affecting multinational organizations; English-speaking branches were highlighted in reporting).

### Technologies / Platforms Targeted
- Salesforce CRM instances and data repositories
- Salesforce Connected Apps / OAuth-based integrations (authorization abuse)
- Salesforce Data Loader (legitimate tool abused or imitated via custom apps)
- Follow-on access targets described in reporting: Okta and Microsoft 365

## 5. Campaign Tradecraft
A commonly described workflow:
1) **Vishing**: operator calls victim support/helpdesk posing as IT support addressing “connectivity issues” or ticket workflows.
2) **Credential or action capture**: victim is socially engineered into disclosing credentials/MFA codes and/or approving a **malicious connected app**.
3) **OAuth-backed access**: connected-app authorization issues tokens that can bypass some traditional controls (e.g., password resets/MFA changes may not invalidate existing OAuth authorizations without specific remediation steps).
4) **Bulk export**: actor uses Data Loader or Data Loader-like automation to query and export large volumes of Salesforce data via APIs.
5) **Operational security**: proxying/collection via **Mullvad VPN** and **Tor** is reported.
6) **Extortion**: separate actor cluster may issue demands days to months later, claiming “ShinyHunters” branding.

## 6. MITRE ATT&CK Alignment

### Techniques Observed
- [[T1598.004 - Spearphishing Voice]]
- [[T1656 - Impersonation]]
- [[T1036 - Masquerading]]
- [[T1671 - Cloud Application Integration]]
- [[T1585 - Establish Accounts]]
- [[T1585.002 - Email Accounts]]
- [[T1586.002 - Email Accounts]]
- [[T1587.001 - Malware]]
- [[T1588.002 - Tool]]
- [[T1059.006 - Python]]
- [[T1083 - File and Directory Discovery]]
- [[T1213.004 - Customer Relationship Management Software]]
- [[T1020 - Automated Exfiltration]]
- [[T1567 - Exfiltration Over Web Service]]
- [[T1090 - Proxy]]
- [[T1090.003 - Multi-hop Proxy]]
- [[T1608.005 - Link Target]]
- [[T1078.002 - Domain Accounts]]

### Notable Tradecraft Characteristics
- Vishing-based **IT support impersonation** to induce high-impact administrative actions.
- **Connected app / OAuth authorization** as the durable access primitive for Salesforce data theft.
- **API-driven bulk export** to rapidly harvest CRM repositories at scale.
- Use of **Tor and commercial VPNs** to proxy calls and/or collection workflows.
- Potential separation of duties: initial access/data theft actor vs. extortion actor claiming “ShinyHunters.”

## 7. Malware & Tooling

### Malware Families
None publicly and consistently identified as a distinct malware family in the core sources for this campaign; the reported approach centers on **authorization abuse** and **Data Loader-like automation** rather than traditional endpoint malware deployment.

### Tools (LOLBins / COTS / Frameworks)
- [[Salesforce Data Loader]] (legitimate tool abused or imitated)
- [[Mullvad VPN]] (proxying in reported workflows)
- [[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]

## 8. Infrastructure & Operational Patterns
- **Phishing panels** used during calls to harvest credentials and/or guide victims through authorization steps.
- **Connected app registration** via trial accounts and/or compromised email accounts to make app origins harder to trace.
- **Extortion communications** leveraging newly created email accounts and “ShinyHunters” branding (as described in reporting).
- **Proxy infrastructure** via commercial VPN IPs and Tor to reduce attribution confidence and complicate blocking.

## 9. Timeline of Campaign Activity (Table + Chronos)

### Timeline (Markdown)
|Date|Event|
|---|---|
|**2024-10**|Campaign activity begins / first observed (vishing-driven Salesforce compromises).|
|**2025-06-04**|GTIG publishes analysis of UNC6040 vishing to Salesforce Data Loader / connected-app abuse and extortion patterns.|
|**2025-09**|Last observed window reported in MITRE campaign record (aligned to FBI reporting period).|
|**2025-09-12**|FBI/IC3 publishes CSA describing UNC6040 targeting Salesforce for data theft and extortion and connected-app authorization abuse.|
|**2025-10-22**|MITRE creates campaign entry for C0059.|
|**2025-10-24**|MITRE updates/last modifies C0059 campaign entry.|

### Timeline (Chronos)
```chronos
- [2024-10]: Campaign activity begins / first observed (vishing-driven Salesforce compromises).
- [2025-06-04]: GTIG publishes analysis of UNC6040 vishing to Salesforce Data Loader / connected-app abuse and extortion patterns.
- [2025-09]: Last observed window reported in MITRE campaign record (aligned to FBI reporting period).
- [2025-09-12]: FBI/IC3 publishes CSA describing UNC6040 targeting Salesforce for data theft and extortion and connected-app authorization abuse.
- [2025-10-22]: MITRE creates campaign entry for C0059.
- [2025-10-24]: MITRE updates/last modifies C0059 campaign entry.
```

## 10. Notable Victims & Impact

### Victim Profile
Public reporting includes multiple impacted organizations, including multinational contexts; comprehensive victim enumeration is not consistently present in the core sources listed here.

### Operational Impact
- Exposure of sensitive CRM datasets (customer, contact, account, and related business records).
- Extortion pressure with potential public disclosure risk and downstream fraud/phishing risk based on stolen customer data.
- Follow-on access risk if exported data contains credentials/secrets or enables credential reset/social engineering against other platforms.

## 11. Related Campaigns & Activity
No definitive linkage to a single named MITRE Group is asserted in the core sources.  
**Pivot idea:** compare patterns of **helpdesk vishing**, **OAuth/connected-app abuse**, and **extortion branding reuse** across other cloud platform intrusions to assess ecosystem overlap without over-attribution.

## 12. Known Indicators (Contextual)
*(Pattern-based pivots only; do not treat as durable IOCs.)*
- Sudden creation/authorization of **new connected apps** in Salesforce, especially those resembling Data Loader naming/branding but not expected in your environment.
- Anomalous OAuth token usage from unusual IP space or new geo patterns (noting that Tor/VPN use can blur this).
- Bulk export/API job spikes (high-volume queries/exports) from newly authorized apps or uncommon client identifiers.
- Helpdesk/call-center tickets + call logs correlating with administrative actions (connected app approvals, API permission changes).
- Evidence of credential-harvesting panels used during calls (URLs/domains shown to users during support interactions).

## 13. Defensive Considerations
- **Harden connected-app authorization**
  - Restrict who can **authorize/manage connected apps**; require admin-only workflows with change control.
  - Implement allowlisting/approval for known-good connected apps; continuously audit app authorizations and OAuth grants.

- **Control bulk export capability**
  - Minimize assignment of high-risk permissions (e.g., API-enabled/export capabilities) to only essential roles.
  - Alert on abnormal bulk export volumes, new export jobs, and suspicious sequences (new app authorization → immediate mass export).

- **Identity + support process defenses**
  - Establish out-of-band verification for IT-support requests involving authentication changes or app authorization.
  - Train and instrument call centers/helpdesks to detect and escalate impersonation attempts (scripted verification, call-back policies).

- **Token response readiness**
  - Prepare playbooks to revoke OAuth tokens/connected app access rapidly (token revocation, app deauthorization, session invalidation).
  - Validate whether “password reset/MFA reset” alone is insufficient when a connected app remains authorized; include app/token remediation in IR steps.

## 14. Analyst Notes
- **Data quality note:** MITRE’s campaign page displays “First Seen: October 2004,” which conflicts with the narrative and authoritative FBI/GTIG reporting indicating **October 2024**; this note uses 2024-10 as first observed based on corroborated sources.
- Attribution is strong to **UNC6040/UNC6240 tracked clusters**, but those clusters do not map to a MITRE Enterprise Group ID in the cited materials; therefore `associated_actors` remains empty.
- Confidence recap:
  - Attribution (to UNC clusters): **high**
  - Tradecraft completeness: **high**
  - Victim enumeration/impact specificity: **low–medium**

## 15. Further Reading / External Resources
- MITRE campaign entry: https://attack.mitre.org/campaigns/C0059/
- FBI/IC3 CSA (authoritative operational summary): https://www.ic3.gov/CSA/2025/250912.pdf
- GTIG deep-dive (tradecraft + mitigations): https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion
- Cyberscoop coverage (contextual summary): https://cyberscoop.com/google-unc6040-salesforce-attacks/
- Mitiga analysis (Data Loader/API exfil lens): https://www.mitiga.io/blog/how-threat-actors-used-salesforce-data-loader-for-covert-api-exfiltration

## 16. References (APA)
- FBI Cyber Division. (2025, September 12). *Cyber Criminal Groups UNC6040 and UNC6395 Compromising Salesforce Instances for Data Theft and Extortion*. IC3. https://www.ic3.gov/CSA/2025/250912.pdf
- Google Threat Intelligence Group. (2025, June 4). *The Cost of a Call: From Voice Phishing to Data Extortion*. Google Cloud Blog. https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion
- Kapko, M. (2025, June 4). *Salesforce customers duped by series of social-engineering attacks*. CyberScoop. https://cyberscoop.com/google-unc6040-salesforce-attacks/
- MITRE ATT&CK. (n.d.). *Salesforce Data Exfiltration (C0059).* https://attack.mitre.org/campaigns/C0059/
- Mitiga. (2025, December 3). *How Threat Actors Used Salesforce Data Loader for Covert API Exfiltration*. https://www.mitiga.io/blog/how-threat-actors-used-salesforce-data-loader-for-covert-api-exfiltration
