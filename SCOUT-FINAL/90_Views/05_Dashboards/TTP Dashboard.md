# TTP Dashboard

```dataviewjs
const FOLDER = "20_Entities/07_TTPs";
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
  .where(p => lower(p.entity_type) === "mitre_technique");

const total = pages.length;
const deprecated = pages.filter(p => Boolean(p.deprecated)).length;
const revoked = pages.filter(p => Boolean(p.revoked)).length;
const highThreat = pages.filter(p => Number(p.threat_score) >= 4).length;
const withActors = pages.filter(p => arr(p.associated_threat_actors).length > 0).length;
const withMalware = pages.filter(p => arr(p.associated_malware).length > 0).length;
const withCampaigns = pages.filter(p => arr(p.associated_campaigns).length > 0).length;
const withDatasources = pages.filter(p => arr(p.datasources).length > 0).length;

const missingId = pages.filter(p => !norm(p.technique_id)).length;
const missingName = pages.filter(p => !norm(p.technique_name)).length;
const missingTactic = pages.filter(p => arr(p.tactic).length === 0).length;
const missingPlatforms = pages.filter(p => arr(p.platforms).length === 0).length;
const missingMaturity = pages.filter(p => !norm(p.detection_maturity)).length;

dv.header(2, "Summary");
dv.table(
  ["Metric", "Count"],
  [
    ["Total techniques", total],
    ["High threat (score >= 4)", highThreat],
    ["Deprecated", deprecated],
    ["Revoked", revoked],
    ["With threat actor links", withActors],
    ["With malware links", withMalware],
    ["With campaign links", withCampaigns],
    ["With datasources", withDatasources],
    ["Missing technique_id", missingId],
    ["Missing technique_name", missingName],
    ["Missing tactics", missingTactic],
    ["Missing platforms", missingPlatforms],
    ["Missing detection_maturity", missingMaturity],
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

const allTactics = [];
const allPlatforms = [];
const allDatasources = [];
const allActors = [];
const allMalware = [];
const allCampaigns = [];
for (const p of pages) {
  allTactics.push(...arr(p.tactic));
  allPlatforms.push(...arr(p.platforms));
  allDatasources.push(...arr(p.datasources));
  allActors.push(...arr(p.associated_threat_actors));
  allMalware.push(...arr(p.associated_malware));
  allCampaigns.push(...arr(p.associated_campaigns));
}

dv.header(2, "Coverage Highlights");
dv.table(["Top Tactics", "Count"], freq(allTactics).slice(0, 10));
dv.table(["Top Platforms", "Count"], freq(allPlatforms).slice(0, 10));
dv.table(["Top Datasources", "Count"], freq(allDatasources).slice(0, 10));
dv.table(["Top Threat Actors", "Count"], freq(allActors).slice(0, 10));
dv.table(["Top Malware", "Count"], freq(allMalware).slice(0, 10));
dv.table(["Top Campaigns", "Count"], freq(allCampaigns).slice(0, 10));
```

## Recent Updates
```dataview
TABLE file.mtime AS "Modified", technique_id, subtechnique_id, technique_name, threat_score
FROM "20_Entities/07_TTPs"
WHERE entity_type = "mitre_technique"
SORT file.mtime DESC
LIMIT 20
```

## High Threat Score
```dataview
TABLE technique_id, subtechnique_id, technique_name, threat_score, detection_maturity
FROM "20_Entities/07_TTPs"
WHERE entity_type = "mitre_technique" AND threat_score >= 4
SORT threat_score DESC, technique_id ASC
```

## Datasource Coverage
```dataview
TABLE technique_id, subtechnique_id, technique_name, datasources
FROM "20_Entities/07_TTPs"
WHERE entity_type = "mitre_technique" AND length(datasources) > 0
SORT technique_id ASC
```

## Linked Actors / Malware / Campaigns
```dataview
TABLE technique_id, subtechnique_id, technique_name, associated_threat_actors, associated_malware, associated_campaigns
FROM "20_Entities/07_TTPs"
WHERE entity_type = "mitre_technique" AND (
  length(associated_threat_actors) > 0 OR
  length(associated_malware) > 0 OR
  length(associated_campaigns) > 0
)
SORT technique_id ASC
```

## Data Gaps
```dataview
TABLE technique_id, subtechnique_id, technique_name, tactic, platforms, detection_maturity, threat_score, datasources
FROM "20_Entities/07_TTPs"
WHERE entity_type = "mitre_technique" AND (
  !technique_id OR technique_id = "" OR
  !technique_name OR technique_name = "" OR
  !tactic OR length(tactic) = 0 OR
  !platforms OR length(platforms) = 0 OR
  !detection_maturity OR detection_maturity = "" OR
  !datasources OR length(datasources) = 0
)
SORT technique_id ASC
```
