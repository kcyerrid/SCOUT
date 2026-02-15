---
entity_type: campaign

campaign_name: "CostaRicto"
campaign_id: "C0004"
aliases: []
tlp_classification: "TLP:CLEAR"

associated_threat_actors: []
suspected_threat_actors: []
attribution_confidence: "1-low"
confidence_notes: "Reporting characterizes activity as potentially 'hackers-for-hire'/mercenary-style operations; attribution remains unclear."

first_observed: "2019-10"
last_observed: "2020-09"
campaign_status: "historic"

primary_objectives:
  - "Espionage"
  - "Credential Access"
  - "Collection"
secondary_objectives:
  - "Lateral Movement"
  - "Command and Control"
  - "Persistence"

target_sectors:
  - "Multiple (disparate global victims)"
target_regions:
  - "Global"
target_technologies:
  - "Windows"
  - "Remote access services"
  - "VPN/Proxy infrastructure"

initial_access_vectors:
  - "External Remote Services"
  - "Tool Transfer / Post-compromise staging"

associated_ttps:
  - "T1583.001 - Domains"
  - "T1005 - Data from Local System"
  - "T1587.001 - Malware"
  - "T1133 - External Remote Services"
  - "T1105 - Ingress Tool Transfer"
  - "T1046 - Network Service Discovery"
  - "T1588.002 - Tool"
  - "T1572 - Protocol Tunneling"
  - "T1090.003 - Multi-hop Proxy"
  - "T1053.005 - Scheduled Task"

malware_families:
  - "[[30_CIPHER/05_Malware/S0614 - CostaBricks|CostaBricks (S0614)]]"
  - "[[30_CIPHER/05_Malware/S0613 - PS1|PS1 (S0613)]]"
  - "[[30_CIPHER/05_Malware/S0615 - SombRAT|SombRAT (S0615)]]"
tools_used:
  - "[[30_CIPHER/05_Malware/S0194 - PowerSploit|PowerSploit (S0194)]]"
  - "[[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]"
  - "[[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]"

infrastructure_patterns:
  - "Layered VPN/Proxy chains"
  - "SSH tunneling / protocol tunneling"
  - "Multi-hop proxying"

notable_victims: []
related_incidents: []

risk_level: "Medium"
impact_assessment: "Espionage-oriented activity with complex infrastructure suggests capability for prolonged access and covert data movement."

intel_sources:
  - "https://attack.mitre.org/campaigns/C0004/"
  - "https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced"
  - "https://www.darkreading.com/cyberattacks-data-breaches/new-costaricto-hack-for-hire-group-targets-global-businesses"
  - "https://cyberscoop.com/hackers-for-hire-mercenary-south-asia-blackberry/"

created: "2026-01-02"
updated: "2026-01-02"

banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# CostaRicto (C0004)

## 1. Executive Summary
**CostaRicto** is an espionage campaign described in open reporting as potentially “outsourced” or mercenary-style, leveraging bespoke malware and **complex proxy/VPN/SSH tunneling** to operate covertly.

## 2. Technical Overview
Key characteristics reported across sources:
- Custom malware families (**CostaBricks**, **PS1**, **SombRAT**) with supporting tooling.
- Heavy use of **tunneling and proxy chaining** (including **Tor**) to obscure operator origin and route traffic.
- Post-compromise discovery and staging behaviors consistent with long-term espionage.

## 3. Associated MITRE ATT&CK Techniques
- [[T1583.001 - Domains]]
- [[T1005 - Data from Local System]]
- [[T1587.001 - Malware]]
- [[T1133 - External Remote Services]]
- [[T1105 - Ingress Tool Transfer]]
- [[T1046 - Network Service Discovery]]
- [[T1588.002 - Tool]]
- [[T1572 - Protocol Tunneling]]
- [[T1090.003 - Multi-hop Proxy]]
- [[T1053.005 - Scheduled Task]]

## 4. Malware & Tooling (Atomic Links)
**Malware Families**
- [[30_CIPHER/05_Malware/S0614 - CostaBricks|CostaBricks (S0614)]]
- [[30_CIPHER/05_Malware/S0613 - PS1|PS1 (S0613)]]
- [[30_CIPHER/05_Malware/S0615 - SombRAT|SombRAT (S0615)]]

**Tools Used**
- [[30_CIPHER/05_Malware/S0194 - PowerSploit|PowerSploit (S0194)]]
- [[30_CIPHER/05_Malware/S0029 - PsExec|PsExec (S0029)]]
- [[30_CIPHER/05_Malware/S0183 - Tor|Tor (S0183)]]

## 5. Timeline (Chronos)
```chronos
- [2019-10] First observed timeframe begins (MITRE reporting window)
- [2020-09] Last observed timeframe ends (MITRE reporting window)
- [2020-11-12] BlackBerry publishes primary “CostaRicto” campaign report
- [2020-11-12] Dark Reading coverage of CostaRicto report
- [2020-11-12] CyberScoop coverage of “hacker-for-hire” framing
```

## 6. Timeline of Campaign Activity (Markdown)
| Date | Event |
|---|---|
| 2019-10 | First observed timeframe begins (MITRE reporting window) |
| 2020-09 | Last observed timeframe ends (MITRE reporting window) |
| 2020-11-12 | BlackBerry publishes primary “CostaRicto” campaign report |
| 2020-11-12 | Dark Reading coverage of CostaRicto report |
| 2020-11-12 | CyberScoop coverage of “hacker-for-hire” framing |

## 7. Defensive Recommendations
- Monitor for **tunneling** and abnormal **proxy chaining** (SSH tunnels, unusual VPN/proxy patterns).
- Hunt for **scheduled task** persistence and remote service access anomalies (RDP/VPN gateways).
- Review endpoints for **PowerSploit**-like behaviors and **PsExec** lateral movement patterns.

## 8. References (APA)
- BlackBerry. (2020, November 12). *The CostaRicto campaign: Cyber-espionage outsourced*. https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced
- MITRE ATT&CK. (n.d.). *CostaRicto (Campaign C0004)*. Retrieved 2026-01-02, from https://attack.mitre.org/campaigns/C0004/
- Sheridan, K. (2020, November 12). *New 'CostaRicto' hack-for-hire group targets global businesses*. *Dark Reading*. https://www.darkreading.com/cyberattacks-data-breaches/new-costaricto-hack-for-hire-group-targets-global-businesses
- Vavra, S. (2020, November 12). *Hacker-for-hire group targeting South Asian organizations, research says*. *CyberScoop*. https://cyberscoop.com/hackers-for-hire-mercenary-south-asia-blackberry/
