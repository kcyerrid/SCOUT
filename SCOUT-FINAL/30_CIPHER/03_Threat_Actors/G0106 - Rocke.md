---
entity_type: threat_actor
actor_name: "Rocke"
common_name: "Rocke"
actor_id: "G0106"
actor_type: "Cybercrime (cryptojacking / financially motivated)"
aliases: []
country_of_origin: ""
suspected_sponsors: []
attribution_confidence: "Medium"
first_seen: "2018-08-30"
last_seen: ""
status: "Unknown"
motivations: ["Financial Gain"]
objectives:
  - "Cryptojacking / unauthorized cryptocurrency mining (Monero)"
  - "Opportunistic exploitation of public-facing applications"
  - "Worm-like spreading within reachable environments (via SSH noted in reporting)"
victimology_summary: "Financially motivated cryptojacking threat actor (reported as Chinese-speaking) whose operations center on compromising internet-exposed systems to deploy Monero miners. Tradecraft includes exploitation of public-facing apps (e.g., Apache Struts, Oracle WebLogic CVE-2017-10271, Adobe ColdFusion CVE-2017-3066), use of web services for C2/update delivery (Pastebin, Git services), persistence via cron/systemd/init scripts, defense evasion via uninstalling security tools and hiding processes using /etc/ld.so.preload-based techniques."
target_sectors:
  - "Cloud / Hosting"
  - "Technology (internet-exposed infrastructure)"
target_regions: ["Global"]
related_groups:
  - "Iron Cybercrime Group (reported overlap; unconfirmed)"
malware:
  - "Cryptomining payloads (e.g., XMRig / XMR-stak usage noted in reporting)"
  - "Pro-Ocean (Rocke-linked cryptojacking malware family described by Unit 42)"
tools:
  - "wget / curl (download + execution)"
  - "UPX (packing / header manipulation)"
  - "libprocesshider (LD_PRELOAD process hiding technique referenced in reporting)"
infrastructure:
  - "Web services used for C2/update distribution (Pastebin; also Gitee/GitLab mentioned in ATT&CK mapping)"
  - "C2 over non-standard ports (e.g., port 51640 noted in ATT&CK technique use)"
  - "Mining pool connectivity (MinerGate pool usage described in early reporting)"
ttps:
  - "[[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[20_Entities/07_TTPs/T1102 - Web Service]]"
  - "[[20_Entities/07_TTPs/T1102.001 - Dead Drop Resolver]]"
  - "[[20_Entities/07_TTPs/T1071 - Application Layer Protocol]]"
  - "[[20_Entities/07_TTPs/T1071.001 - Web Protocols]]"
  - "[[20_Entities/07_TTPs/T1105 - Ingress Tool Transfer]]"
  - "[[20_Entities/07_TTPs/T1053.003 - Cron]]"
  - "[[20_Entities/07_TTPs/T1543.002 - Systemd Service]]"
  - "[[20_Entities/07_TTPs/T1037 - Boot or Logon Initialization Scripts]]"
  - "[[20_Entities/07_TTPs/T1547.001 - Registry Run Keys / Startup Folder]]"
  - "[[20_Entities/07_TTPs/T1562.001 - Disable or Modify Tools]]"
  - "[[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall]]"
  - "[[20_Entities/07_TTPs/T1564.001 - Hidden Files and Directories]]"
  - "[[20_Entities/07_TTPs/T1574.006 - Dynamic Linker Hijacking]]"
  - "[[20_Entities/07_TTPs/T1014 - Rootkit]]"
  - "[[20_Entities/07_TTPs/T1552.004 - Private Keys]]"
  - "[[20_Entities/07_TTPs/T1021.004 - SSH]]"
  - "[[20_Entities/07_TTPs/T1018 - Remote System Discovery]]"
  - "[[20_Entities/07_TTPs/T1046 - Network Service Discovery]]"
  - "[[20_Entities/07_TTPs/T1496.001 - Compute Hijacking]]"
  - "[[20_Entities/07_TTPs/T1027 - Obfuscated Files or Information]]"
  - "[[20_Entities/07_TTPs/T1027.002 - Software Packing]]"
  - "[[20_Entities/07_TTPs/T1027.004 - Compile After Delivery]]"
  - "[[20_Entities/07_TTPs/T1070.002 - Clear Linux or Mac System Logs]]"
  - "[[20_Entities/07_TTPs/T1070.004 - File Deletion]]"
  - "[[20_Entities/07_TTPs/T1070.006 - Timestomp]]"
  - "[[20_Entities/07_TTPs/T1082 - System Information Discovery]]"
  - "[[20_Entities/07_TTPs/T1518.001 - Security Software Discovery]]"
  - "[[20_Entities/07_TTPs/T1055.002 - Portable Executable Injection]]"
  - "[[20_Entities/07_TTPs/T1140 - Deobfuscate/Decode Files or Information]]"
  - "[[20_Entities/07_TTPs/T1036.005 - Match Legitimate Resource Name or Location]]"
  - "[[20_Entities/07_TTPs/T1571 - Non-Standard Port]]"
notable_claims:
  - "The name 'Rocke' comes from the MinerGate login email 'rocke@live.cn' used for mining proceeds."
  - "ATT&CK notes unconfirmed overlap with Iron Cybercrime Group."
  - "Uses web services (Pastebin, plus Git services) for C2/update distribution; includes dead-drop style redirection."
  - "Linux hiding via /etc/ld.so.preload-based hooking and libprocesshider (LD_PRELOAD)."
  - "Non-standard port usage for miner↔C2 noted (port 51640)."
intel_sources:
  - "MITRE ATT&CK - G0106 Rocke - https://attack.mitre.org/groups/G0106/"
  - "Cisco Talos - Rocke: The Champion of Monero Miners - https://blog.talosintelligence.com/rocke-champion-of-monero-miners/"
  - "Palo Alto Networks Unit 42 - Malware Used by Rocke Group Evolves to Evade Detection by Cloud Security Products - https://unit42.paloaltonetworks.com/malware-used-by-rocke-group-evolves-to-evade-detection-by-cloud-security-products/"
  - "Palo Alto Networks Unit 42 - Pro-Ocean: Rocke Group’s New Cryptojacking Malware - https://unit42.paloaltonetworks.com/pro-ocean-rocke-groups-new-cryptojacking-malware/"
  - "Anomali Labs - Rocke Evolves Its Arsenal With a New Malware Family Written in Golang - https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang"
tags:
  - "scout"
  - "threat-actor"
  - "mitre-g0106"
  - "cybercrime"
  - "cryptojacking"
  - "monero"
  - "pastebin"
created: 2026-01-06
last_modified: 2026-01-06
---

## 1. Summary
Rocke (G0106) is a **financially motivated cryptojacking** threat actor (reported as Chinese-speaking) focused on compromising systems to mine cryptocurrency (notably Monero). The “Rocke” name is derived from the MinerGate login email **rocke@live.cn** used in mining operations. :contentReference[oaicite:1]{index=1}

## 2. Attribution & Profile
- **Type:** Cybercrime / financially motivated cryptomining :contentReference[oaicite:2]{index=2}  
- **Confidence:** Medium (clear tradecraft + monetization objective; “Chinese-speaking” and overlap claims are reported but not definitive) :contentReference[oaicite:3]{index=3}  
- **Overlap note:** Researchers reported overlap with “Iron Cybercrime Group,” but ATT&CK flags it as **unconfirmed**. :contentReference[oaicite:4]{index=4}

## 3. Targeting & Victimology
- **Victim profile:** internet-exposed servers and cloud workloads susceptible to application exploitation and weak admin controls. :contentReference[oaicite:5]{index=5}  
- **Operational goal:** hijack compute to mine Monero (resource hijacking). :contentReference[oaicite:6]{index=6}  
- **Geography:** reported operations are best treated as **global/opportunistic** (targets defined by exposure rather than region). :contentReference[oaicite:7]{index=7}  

## 4. Known Malware, Tools & Infrastructure
**Malware / Payloads (reported)**
- Monero mining payload usage including **XMRig / XMR-stak** configurations in early reporting. :contentReference[oaicite:8]{index=8}  
- **Pro-Ocean**: Rocke-linked cryptojacking malware family with improved hiding and worming capabilities (Unit 42). :contentReference[oaicite:9]{index=9}  

**Tools / Utilities (reported)**
- `wget` / `curl` for download-and-execute chains. :contentReference[oaicite:10]{index=10}  
- UPX packing and anti-unpacking behavior (header manipulation). :contentReference[oaicite:11]{index=11}  
- **libprocesshider** and **LD_PRELOAD** (/etc/ld.so.preload) for process hiding. :contentReference[oaicite:12]{index=12}  

**Infrastructure**
- Use of **Pastebin** (and other web services including Git platforms) for C2/update distribution; includes **dead-drop resolver** patterns. :contentReference[oaicite:13]{index=13}  
- Non-standard ports observed for miner/C2 connectivity (ATT&CK notes **51640**). :contentReference[oaicite:14]{index=14}  

## 5. Tradecraft Overview
- **Initial access:** exploitation of public-facing apps, including Apache Struts, Oracle WebLogic (CVE-2017-10271), and Adobe ColdFusion (CVE-2017-3066). :contentReference[oaicite:15]{index=15}  
- **Persistence:** cron jobs, init scripts, and systemd services on Linux; Windows persistence via startup folder / run-key style behavior observed in miner packaging. :contentReference[oaicite:16]{index=16}  
- **Defense evasion:** removal/disablement of security tooling and firewall manipulation; process hiding via /etc/ld.so.preload + libprocesshider. :contentReference[oaicite:17]{index=17}  
- **Propagation:** SSH spreading using discovered private keys and known_hosts-derived targets. :contentReference[oaicite:18]{index=18}  
- **Impact:** compute hijacking for mining. :contentReference[oaicite:19]{index=19}  

## 6. MITRE ATT&CK Mapping
- [[20_Entities/07_TTPs/T1190 - Exploit Public-Facing Application]]
- [[20_Entities/07_TTPs/T1102 - Web Service]]
- [[20_Entities/07_TTPs/T1102.001 - Dead Drop Resolver]]
- [[20_Entities/07_TTPs/T1071 - Application Layer Protocol]]
- [[20_Entities/07_TTPs/T1071.001 - Web Protocols]]
- [[20_Entities/07_TTPs/T1053.003 - Cron]]
- [[20_Entities/07_TTPs/T1543.002 - Systemd Service]]
- [[20_Entities/07_TTPs/T1037 - Boot or Logon Initialization Scripts]]
- [[20_Entities/07_TTPs/T1562.001 - Disable or Modify Tools]]
- [[20_Entities/07_TTPs/T1562.004 - Disable or Modify System Firewall]]
- [[20_Entities/07_TTPs/T1574.006 - Dynamic Linker Hijacking]]
- [[20_Entities/07_TTPs/T1552.004 - Private Keys]]
- [[20_Entities/07_TTPs/T1021.004 - SSH]]
- [[20_Entities/07_TTPs/T1496.001 - Compute Hijacking]]
- [[20_Entities/07_TTPs/T1571 - Non-Standard Port]]
(Full technique list is reflected in the YAML frontmatter.) :contentReference[oaicite:20]{index=20}

## 7. Detection Opportunities
1. **Exploit → downloader → persistence chain**
   - Web exploit telemetry followed by `wget/curl` retrieval and rapid creation of cron/systemd persistence. :contentReference[oaicite:21]{index=21}  
2. **Dead-drop style web-service C2**
   - Regular outbound HTTPS to Pastebin “raw” endpoints (and redirects to updated payload locations). :contentReference[oaicite:22]{index=22}  
3. **Process hiding & /etc/ld.so.preload changes**
   - Unexpected modifications to `/etc/ld.so.preload`, presence of libprocesshider artifacts, and inconsistencies between process telemetry sources. :contentReference[oaicite:23]{index=23}  
4. **Firewall manipulation to suppress competitors**
   - iptables changes and killing competing miners; look for sudden rule additions and repeated process kills. :contentReference[oaicite:24]{index=24}  
5. **SSH fan-out behavior**
   - Automated SSH attempts across internal ranges using harvested keys/known_hosts. :contentReference[oaicite:25]{index=25}  

## 8. Response & Mitigation Guidance
- **Patch & reduce exposure:** prioritize hardening/patching public-facing apps and appliances; remove unnecessary internet exposure. :contentReference[oaicite:26]{index=26}  
- **Lock down cloud workloads:** monitor for security agent tampering/uninstalls and enforce workload integrity controls. :contentReference[oaicite:27]{index=27}  
- **Egress + anomaly detection:** alert on mining pool traffic, unusual outbound to Pastebin/Git services from servers, and long-lived non-standard port sessions. :contentReference[oaicite:28]{index=28}  
- **SSH hygiene:** rotate keys, restrict where private keys exist, and enforce least-privilege + MFA where applicable. :contentReference[oaicite:29]{index=29}  

## 9. Hunting Ideas
- Retrospective query: inbound exploit attempts → `wget/curl` execution → cron/systemd creation within minutes/hours.
- Identify endpoints with `/etc/ld.so.preload` modifications during suspicious windows.
- Search auth logs for SSH propagation patterns: repeated auth attempts + key usage + scanning. :contentReference[oaicite:30]{index=30}  

## 10. Associated Malware
- Cryptomining payloads (XMRig / XMR-stak usage described in reporting). :contentReference[oaicite:31]{index=31}  
- Pro-Ocean (Rocke-linked cryptojacking malware described by Unit 42). :contentReference[oaicite:32]{index=32}  

## 11. Associated Tools
- wget / curl :contentReference[oaicite:33]{index=33}  
- UPX packing/anti-unpacking behavior :contentReference[oaicite:34]{index=34}  
- libprocesshider + LD_PRELOAD (/etc/ld.so.preload) :contentReference[oaicite:35]{index=35}  

## 12. Analyst Notes
- **High-signal anchor:** web-app exploitation leading to rapid miner deployment + persistence (cron/systemd) and explicit competitor-suppression (kill/firewall rules). :contentReference[oaicite:36]{index=36}  
- **Operational insight:** use of web services as update/control plane reduces the value of static IP blocks; prioritize behavior over IOC-only defenses. :contentReference[oaicite:37]{index=37}  

## 13. Further Reading / External Resources
- MITRE Group: https://attack.mitre.org/groups/G0106/ :contentReference[oaicite:38]{index=38}  
- Cisco Talos: https://blog.talosintelligence.com/rocke-champion-of-monero-miners/ :contentReference[oaicite:39]{index=39}  
- Unit 42 (2019): https://unit42.paloaltonetworks.com/malware-used-by-rocke-group-evolves-to-evade-detection-by-cloud-security-products/ :contentReference[oaicite:40]{index=40}  
- Unit 42 (2021): https://unit42.paloaltonetworks.com/pro-ocean-rocke-groups-new-cryptojacking-malware/ :contentReference[oaicite:41]{index=41}  
- Anomali: https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang :contentReference[oaicite:42]{index=42}  

## 14. References
- MITRE ATT&CK. (2025-04-25). *Rocke (Group G0106).* https://attack.mitre.org/groups/G0106/ :contentReference[oaicite:43]{index=43}  
- Liebenberg, D. (2018-08-30). *Rocke: The Champion of Monero Miners.* https://blog.talosintelligence.com/rocke-champion-of-monero-miners/ :contentReference[oaicite:44]{index=44}  
- Unit 42. (2019-01-17). *Malware Used by Rocke Group Evolves to Evade Detection by Cloud Security Products.* https://unit42.paloaltonetworks.com/malware-used-by-rocke-group-evolves-to-evade-detection-by-cloud-security-products/ :contentReference[oaicite:45]{index=45}  
- Unit 42. (2021-01-28). *Pro-Ocean: Rocke Group’s New Cryptojacking Malware.* https://unit42.paloaltonetworks.com/pro-ocean-rocke-groups-new-cryptojacking-malware/ :contentReference[oaicite:46]{index=46}  
- Anomali. (2019-03-15). *Rocke Evolves Its Arsenal With a New Malware Family Written in Golang.* https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang :contentReference[oaicite:47]{index=47}  
