---
entity_type: mitre_technique

technique_id: "T1220"
subtechnique_id: ""
technique_name: "XSL Script Processing"

tactic:
  - "Defense Evasion"
platforms:
  - "Windows"
  - "Network Devices"
datasources:
  - "Process"
  - "Module"

mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false

associated_threat_actors:
  - "Cobalt Group"
  - "Higaisa"
  - "Lazarus Group"
associated_malware:
  - "Astaroth"
associated_campaigns:
  - "Operation Dream Job"
related_techniques: []

detection_priority:
  - High

detection_maturity: ""
threat_score: 4

created: 2026-01-06
updated: 2026-01-06

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

## Summary
**XSL Script Processing (T1220)** is a defense-evasion technique where adversaries abuse XSLT/XSL execution pathways to run logic (including embedded script in some implementations) while blending into legitimate XML/XSL processing activity and trusted utilities. 

## Technical Overview
XSLT is commonly used to transform XML into other formats. On Windows and some ecosystems, XSL processing can be invoked by legitimate components/utilities, and certain XSL engines support script blocks (or equivalent extension functions), allowing code execution during transformation. This makes XSL artifacts useful for:
- **Masquerading execution** as “data processing” (XML/XSL transforms).
- **Living-off-the-land** via trusted binaries/libraries that parse XML and apply stylesheets.
- **Policy/allowlist bypass pressure** when the executing host process is trusted and the payload is “just XML”.

Defender-relevant artifacts often include:
- A **host process** performing XSL transforms (sometimes a trusted/legacy utility).
- **XSL files** on disk or staged transiently (temp/user profile shares).
- **Child process creation** or suspicious module loads tied to transformation-time execution.

## Subtechnique Considerations
No subtechniques are defined for T1220 in Enterprise ATT&CK. 

## Procedure Examples
MITRE-curated examples indicate multiple adversary sets have leveraged XSL script processing, including **Cobalt Group**, **Higaisa**, and **Lazarus Group**, with associated software and campaigns documented by ATT&CK (e.g., **Astaroth**, **Operation Dream Job**). 

Operationally, defenders should think in terms of:
- “**XSL used as a stageable execution container**” (XML wrapper + transform runtime).
- “**Trusted binary/library doing the execution**” (difficult to block without collateral).

## Detection Guidance
Prioritize detection where XSL processing is **rare** in your environment or occurs in **unexpected contexts** (user-writable paths, email/client processes, Office lineage, browser lineage, remote admin tooling lineage).

High-signal detection angles:
1. **Process ancestry & rarity**
   - Uncommon XSL-processing parent processes (or unusual parent-child relationships).
   - XSL transformations initiated by user-facing apps (mail client, browser, office suite) without a clear business reason.
2. **Command-line & file provenance**
   - References to `.xsl`/`.xslt` and XML inputs from temp/user download directories, shares, or recently created files.
3. **Behavioral join**
   - XSL transformation activity **followed quickly by process creation** (especially interpreters, LOLBins, or tooling not aligned to the host).
4. **Module/library load**
   - XML/XSL-related library loads in processes that don’t normally do transforms; correlate with subsequent suspicious execution.

### Data Source Notes
Relevant telemetry categories include ATT&CK data sources such as **Process** and **Module**.   
Minimum telemetry expectations:
- **Process creation** with full command line, parent/child, integrity level, signer, and user.
- **Module loads** (where available) for XML/XSL libraries and scripting runtimes.
- **File events** (recommended) for creation/modification of `.xsl/.xslt/.xml` in user-writable locations.

## Response Guidance
Triage workflow:
1. **Confirm execution context**
   - Identify the transforming process, parent lineage, user session, and host role.
2. **Collect artifacts**
   - Acquire the `.xsl/.xslt` and associated XML inputs (preserve originals; hash).
   - Capture process tree and command lines; collect module load evidence if available.
3. **Scope**
   - Search for the same stylesheet hash/path across endpoints and shares.
   - Look for follow-on behaviors: persistence attempts, credential access, lateral movement.
4. **Contain**
   - If confirmed malicious: isolate host, block known hashes/paths, and consider restricting execution of legacy utilities used for transforms where feasible.

## Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0005 - Defense Evasion/T1220 - XSL Script Processing|T1220]]

## SOC Relevance
**Why SOC should care:** XSL processing is frequently “allowed by default” and can appear as benign data manipulation. When abused, it becomes a **high-leverage evasive execution path**—especially in environments with weak application control around legacy/trusted tooling.

**Best placements:** EDR process telemetry, allowlisting/audit logs, and file monitoring for stylesheet staging.

## Threat Actor Usage
Documented usage exists in ATT&CK CTI for:
- Cobalt Group
- Higaisa
- Lazarus Group 

## Campaign Usage
- Operation Dream Job 

## Malware Usage
- Astaroth 

## Mitigations
MITRE lists mitigation concepts for this technique including:
- **Execution Prevention (M1038)**
- **Behavior Prevention on Endpoint (M1040)** 

Additional defender guidance (environment-dependent):
- Reduce/monitor legacy XML/XSL tooling usage; enforce signer and path rules where possible.
- Harden script execution controls and constrain user-writable execution paths.
- Apply strong email/web ingress controls to reduce delivery of staged `.xsl/.xml` artifacts.

## Testing & Validation
Validation ideas (safe, defender-focused):
- Create a **benign** XSL transform workload and confirm your telemetry captures:
  - process creation with `.xsl/.xslt` references,
  - file creation of stylesheets in user-writable paths,
  - any correlated child process behavior (if your environment generates it).
- Build a detection test that alerts on:
  - rare transform executables,
  - `.xsl/.xslt` in temp/download locations,
  - suspicious parent processes initiating transforms.

## References
MITRE ATT&CK. (n.d.). *XSL Script Processing (T1220).* https://attack.mitre.org/techniques/T1220/   
MITRE ATT&CK. (n.d.). *Data Sources.* https://attack.mitre.org/datasources/   
Microsoft. (2025, September 9). *Script Blocks Using msxsl:script.* https://learn.microsoft.com/en-us/dotnet/standard/data/xml/script-blocks-using-msxsl-script   
Microsoft. (2025, June 2). *wmic.* https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wmic 

## Notes
- Track local “known-good” XSL usage (apps, paths, service accounts) to reduce false positives.
- Consider adding a stylesheet-hash allowlist for sanctioned transform workflows (ETL/reporting stacks).
