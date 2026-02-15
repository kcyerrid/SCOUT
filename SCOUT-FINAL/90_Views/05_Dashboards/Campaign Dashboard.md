# Campaign Dashboard

```dataviewjs
const FOLDER = "30_CIPHER/04_Campaigns";
const norm = (v) => (v ?? "").toString().trim();
const lower = (v) => norm(v).toLowerCase();
const arr = (v) => Array.isArray(v) ? v : (v ? [v] : []);
const first = (...vals) => {
  for (const v of vals) {
    const n = norm(v);
    if (n) return n;
  }
  return "";
};

const pages = dv.pages(`"${FOLDER}"`)
  .where(p => lower(p.entity_type) === "campaign");

const total = pages.length;
const active = pages.filter(p => {
  const status = lower(first(p.campaign_status, p.status));
  return status === "active" || status === "ongoing" || status === "current";
}).length;
const concluded = pages.filter(p => {
  const status = lower(first(p.campaign_status, p.status));
  return status === "concluded" || status === "closed" || status === "inactive";
}).length;
const highRisk = pages.filter(p => {
  const risk = lower(first(p.risk_level));
  return risk === "high" || risk === "critical";
}).length;

const withActors = pages.filter(p => (
  arr(p.associated_actors).length > 0 ||
  arr(p.suspected_actors).length > 0 ||
  arr(p.attribution).length > 0
)).length;
const withMalware = pages.filter(p => (
  arr(p.malware_used).length > 0 ||
  arr(p.malware_families).length > 0
)).length;
const withTtps = pages.filter(p => (
  arr(p.associated_ttps).length > 0 ||
  arr(p.techniques).length > 0
)).length;
const withSources = pages.filter(p => arr(p.intel_sources).length > 0).length;

const missingId = pages.filter(p => !norm(first(p.campaign_id))).length;
const missingName = pages.filter(p => !norm(first(p.campaign_name, p.file?.name))).length;
const missingTlp = pages.filter(p => !norm(first(p.tlp_classification))).length;
const missingDate = pages.filter(p => !norm(first(p.first_seen, p.first_observed))).length;

dv.header(2, "Summary");
dv.table(
  ["Metric", "Count"],
  [
    ["Total campaigns", total],
    ["Active / ongoing", active],
    ["Concluded / inactive", concluded],
    ["High or critical risk", highRisk],
    ["With actor links", withActors],
    ["With malware links", withMalware],
    ["With ATT&CK mapping", withTtps],
    ["With intel sources", withSources],
    ["Missing campaign_id", missingId],
    ["Missing campaign_name", missingName],
    ["Missing TLP", missingTlp],
    ["Missing first seen", missingDate],
  ]
);

const toKey = (v) => {
  if (v === null || v === undefined) return "";
  if (typeof v === "string" || typeof v === "number" || typeof v === "boolean") {
    return String(v);
  }
  if (v.path) return String(v.path);
  if (v.file && v.file.path) return String(v.file.path);
  if (Array.isArray(v)) return v.map(toKey).filter(Boolean).join(", ");
  try {
    return JSON.stringify(v);
  } catch (err) {
    return String(v);
  }
};

const freq = (items) => {
  const map = new Map();
  for (const it of items) {
    const key = norm(toKey(it));
    if (!key) continue;
    map.set(key, (map.get(key) || 0) + 1);
  }
  return Array.from(map.entries()).sort((a, b) => b[1] - a[1]);
};

const allActors = [];
const allMalware = [];
const allTools = [];
const allTtps = [];
const allRegions = [];
const allSectors = [];
for (const p of pages) {
  allActors.push(...arr(p.associated_actors), ...arr(p.suspected_actors), ...arr(p.attribution));
  allMalware.push(...arr(p.malware_used), ...arr(p.malware_families));
  allTools.push(...arr(p.tools_used));
  allTtps.push(...arr(p.associated_ttps), ...arr(p.techniques));
  allRegions.push(...arr(p.target_regions));
  allSectors.push(...arr(p.target_sectors));
}

dv.header(2, "Coverage Highlights");
dv.table(["Top Threat Actors", "Count"], freq(allActors).slice(0, 10));
dv.table(["Top Malware Families", "Count"], freq(allMalware).slice(0, 10));
dv.table(["Top Tools", "Count"], freq(allTools).slice(0, 10));
dv.table(["Top ATT&CK Techniques", "Count"], freq(allTtps).slice(0, 10));
dv.table(["Top Target Regions", "Count"], freq(allRegions).slice(0, 10));
dv.table(["Top Target Sectors", "Count"], freq(allSectors).slice(0, 10));
```

## Recent Updates
```dataview
TABLE file.mtime AS "Modified", campaign_name, campaign_id, campaign_status, risk_level
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign"
SORT file.mtime DESC
LIMIT 20
```

## Active / Ongoing Campaigns
```dataview
TABLE campaign_name, campaign_id, campaign_status, first_observed, last_observed, risk_level
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign" AND (
  lower(campaign_status) = "active" OR
  lower(campaign_status) = "ongoing" OR
  lower(campaign_status) = "current"
)
SORT first_observed DESC
```

## ATT&CK Coverage
```dataview
TABLE campaign_name, campaign_id, associated_ttps, techniques
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign" AND (
  length(associated_ttps) > 0 OR length(techniques) > 0
)
SORT campaign_name ASC
```

## Malware & Tooling Links
```dataview
TABLE campaign_name, campaign_id, malware_families, malware_used, tools_used
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign" AND (
  length(malware_families) > 0 OR length(malware_used) > 0 OR length(tools_used) > 0
)
SORT campaign_name ASC
```

## Data Gaps
```dataview
TABLE campaign_name, campaign_id, first_observed, last_observed, campaign_status, attribution_confidence, tlp_classification, intel_sources
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign" AND (
  !campaign_id OR campaign_id = "" OR
  !campaign_name OR campaign_name = "" OR
  !tlp_classification OR tlp_classification = "" OR
  !intel_sources OR length(intel_sources) = 0 OR
  !associated_ttps OR length(associated_ttps) = 0
)
SORT campaign_name ASC
```
