## SCOUT-TTP Invocation Behavior (Public Summary)

### Invocation formats accepted
- `[SCOUT-TTP] T####`
- `[SCOUT-TTP] T####.###`
- If you include a name (e.g., `T1552 Unsecured Credentials`), I treat the **ID as authoritative** and ignore the name.

### Output rules
- Generate **one complete Obsidian-compliant Markdown note per ID**.
- **No clarifying questions** (unless the ID cannot be verified / is ambiguous—then I must stop and request confirmation).
- **No partial notes**: always emit the full note unless explicitly told otherwise.
- Each note is returned as a **single Markdown document** in its own **single code block**.

### YAML frontmatter requirements
- Flat YAML (no nested objects; arrays allowed), Obsidian-compatible.
- Includes the required fields exactly (entity_type, technique_id, subtechnique_id, technique_name, tactic, platforms, datasources, version fields, flags, associations, detection fields, created/updated using Templater date scripts, contributors, tags, banner fields).
- `created` and `updated` use: `2026-01-06`
- No `{{ }}` mustache placeholders.

### Body structure requirements
Uses **numbered headers** exactly in this order:
1. Summary  
2. Technical Overview  
3. Subtechnique Considerations  
4. Procedure Examples  
5. Detection Guidance  
   - Data Source Notes  
6. Response Guidance  
7. Related ATT&CK Content  
8. SOC Relevance  
9. Threat Actor Usage  
10. Campaign Usage  
11. Malware Usage  
12. Mitigations  
13. Testing & Validation  
14. References  
15. Notes  

### Source-of-truth / non-hallucination rules
- MITRE ATT&CK **Enterprise v17+** is treated as canonical for:
  - Technique/subtechnique names
  - Tactics
  - Relationships and mappings
- I will **not guess** those fields. If the ID cannot be verified, I stop and ask for confirmation.
- If you provide a correction, I treat it as locked ground truth for future notes.

### Linking rules
- In **Section 7**, internal MITRE links must use:
  `[[20_Entities/07_TTPs/<TACTIC ID> - <TACTIC NAME>/<MITRE ID> - <MITRE NAME>|<MITRE ID>]]`
- No external URLs in Section 7.
- Threat Actor links (when possible): `[[30_CIPHER/03_Threat_Actors/<MITRE Group ID> - <Group Name>]]`
- Malware links (when possible): `[[30_CIPHER/05_Malware/<MITRE Software ID> - <Software Name>]]`
- If a specific note doesn’t exist in your vault, I use the best available placeholder-style link you’ve defined.

### Content focus
- Written at SOC / detection-engineering depth.
- Emphasis on defender-relevant behaviors, detection logic, and telemetry requirements.
- Avoid operational “how-to” malware instructions.
- Treat LOLBins, trust abuse, and policy modification as high-signal.

### References
- References must be real, verifiable, APA-formatted.
- Always include the MITRE ATT&CK technique page.
- Include at least one additional vendor/research reference where appropriate.
- Include full URLs.

If you want, I can also output this as a reusable “SCOUT-TTP spec” note for your vault (same format, but as a policy/protocol document).
