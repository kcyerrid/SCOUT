---
entity_type: threat_actor
actor_name: ""
aliases: []
actor_id: ""
nation_state: ""
sponsor_type: []
motivation: []
attribution_confidence:
first_identified: ""
active_period: ""
target_sectors: []
target_regions: []
target_technologies: []
ttp_profile: []
malware_used: []
tools_used: []
infrastructure_profile: []
associated_campaigns: []
related_incidents: []
risk_level: ""
threat_score: 1
intel_sources: []
tlp_classification: ""
created:
updated:
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
<%*
/*
  Threat Actor Master Template — SCOUT / CIPHER
  YAML is the single source of truth.
  File is auto-renamed using actor_id (preferred) and actor_name.
  Body renders RIA-compliant backlinks to related entities.
*/

// ---------- Core identifiers ----------
const actor_name = tp.frontmatter.actor_name ?? "";
const actor_id   = tp.frontmatter.actor_id ?? "";

// ---------- Auto-rename logic (actor_id preferred) ----------
if (actor_name && actor_name.trim().length > 0) {
  let baseName = actor_name
    .replace(/[\\/:*?"<>|]/g, "-")
    .replace(/\s+/g, " ")
    .trim();

  let finalName = (actor_id && actor_id.trim().length > 0)
    ? `${actor_id} - ${baseName}`
    : baseName;

  await tp.file.rename(finalName);
}

// ---------- Frontmatter constants ----------
const aliases                = tp.frontmatter.aliases ?? [];
const nation_state           = tp.frontmatter.nation_state ?? "";
const sponsor_type           = tp.frontmatter.sponsor_type ?? [];
const motivation             = tp.frontmatter.motivation ?? [];
const attribution_confidence = tp.frontmatter.attribution_confidence ?? [];
const first_identified       = tp.frontmatter.first_identified ?? "";
const active_period          = tp.frontmatter.active_period ?? "";
const target_sectors         = tp.frontmatter.target_sectors ?? [];
const target_regions         = tp.frontmatter.target_regions ?? [];
const target_technologies    = tp.frontmatter.target_technologies ?? [];
const ttp_profile            = tp.frontmatter.ttp_profile ?? [];
const malware_used           = tp.frontmatter.malware_used ?? [];
const tools_used             = tp.frontmatter.tools_used ?? [];
const infrastructure_profile = tp.frontmatter.infrastructure_profile ?? [];
const associated_campaigns   = tp.frontmatter.associated_campaigns ?? [];
const related_incidents      = tp.frontmatter.related_incidents ?? [];
const risk_level             = tp.frontmatter.risk_level ?? "";
const threat_score           = tp.frontmatter.threat_score ?? 1;
const intel_sources          = tp.frontmatter.intel_sources ?? [];
const tlp_classification     = tp.frontmatter.tlp_classification ?? "";

// ---------- Helper renderers ----------
const asBullets = (arr) => (Array.isArray(arr) && arr.length)
  ? arr.map(v => `- ${v}`).join("\n")
  : "- (none recorded)";

const asInline = (arr) => (Array.isArray(arr) && arr.length)
  ? arr.join(", ")
  : "(none recorded)";

const asValue = (v) => (v && String(v).trim().length)
  ? v
  : "(not specified)";

const confidenceValue = (arr) => {
  if (!Array.isArray(arr) || arr.length === 0) return "(not specified)";
  return arr[0];
};

// ---------- RIA backlink renderers ----------
const asBacklinks = (arr) => (Array.isArray(arr) && arr.length)
  ? arr.map(v => `- [[${v}]]`).join("\n")
  : "- (none recorded)";

const asInlineBacklinks = (arr) => (Array.isArray(arr) && arr.length)
  ? arr.map(v => `[[${v}]]`).join(", ")
  : "(none recorded)";
%>

# <%= actor_name || "Threat Actor" %>

## 1. Executive Summary
Provide a concise, evidence-based overview of <%= actor_name || "this threat actor" %>. Emphasize durable characteristics (motivation, tradecraft, targeting) and clearly distinguish confirmed reporting from analytic assessment.

## 2. Attribution Notes
**Attribution Confidence:** `<%= confidenceValue(attribution_confidence) %>`

**Nation-State Association:** <%= asValue(nation_state) %>  
**Sponsor Type:** <%= asInline(sponsor_type) %>  
**Aliases:** <%= asInline(aliases) %>  
**Actor ID:** <%= asValue(actor_id) %>

Justify the attribution confidence using reputable sources. Explicitly note uncertainties, competing hypotheses, and limitations in available reporting.

## 3. Motivations & Objectives
**Assessed Motivation(s):** <%= asInline(motivation) %>

Describe objectives in a way that supports long-term reuse (e.g., credential access enabling cloud control-plane abuse, data theft for extortion). Avoid incident-specific language unless required to establish a durable pattern.

## 4. Targeting Profile
**First Identified:** <%= asValue(first_identified) %>  
**Active Period:** <%= asValue(active_period) %>

### Sectors
<%= asBullets(target_sectors) %>

### Regions
<%= asBullets(target_regions) %>

### Technologies / Platforms
<%= asBullets(target_technologies) %>

## 5. Tradecraft Overview
Summarize stable operational behaviors likely to persist over time. Focus on how access is obtained, expanded, and abused rather than step-by-step intrusion narratives.

### High-Level TTP Profile
<%= asBullets(ttp_profile) %>

## 6. MITRE ATT&CK Mapping
Only include validated ATT&CK techniques supported by cited sources.

### 6.1 Techniques Used
- **TXXXX – Technique Name** → [[TXXXX]]
- (Add additional techniques as appropriate)

### 6.2 Notable Procedure Variations
Document procedure-level variations that materially affect detection or attribution (e.g., dependence on help desk verification practices, cloud-first post-access behavior).

## 7. Malware & Tools Used

### 7.1 Malware
<%= asBacklinks(malware_used) %>

### 7.2 Tools (Living-off-the-Land or COTS)
<%= asBacklinks(tools_used) %>

## 8. Infrastructure Patterns
Summarize durable infrastructure characteristics. Use backlinks only if infrastructure is tracked as first-class entities.

<%= asBullets(infrastructure_profile) %>

## 9. Campaign History

### Associated Campaigns
<%= asBacklinks(associated_campaigns) %>

### Related Incidents
<%= asBacklinks(related_incidents) %>

## 10. Known Indicators
Summarize indicator *patterns* rather than raw IOCs. Link to atomic IOC entities where appropriate.

- Identity abuse patterns → [[IOC-Identity-Abuse]]
- MFA manipulation patterns → [[IOC-MFA-Fatigue]]
- Help desk impersonation indicators → [[IOC-HelpDesk-Impersonation]]

## 11. Defensive Recommendations
Focus on detection opportunities and common blind spots rather than prescriptive response playbooks.

- **Identity plane:** account recovery, MFA changes, anomalous sign-in sequences, privileged role grants.
- **SaaS / cloud plane:** admin actions, OAuth/app consent, repository access patterns.
- **Visibility gaps:** logging and retention limitations across IdP, SaaS, and administrative systems.

## 12. Analyst Notes
**Risk Level:** <%= asValue(risk_level) %>  
**Threat Score:** <%= threat_score %>

Capture caveats, open intelligence gaps, and guidance on safe operationalization (e.g., prefer sequence-based detections over static IOC matching).

## 13. References
<%= asBullets(intel_sources) %>

**TLP Classification:** <%= asValue(tlp_classification) %>
