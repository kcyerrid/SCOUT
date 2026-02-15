# Threat Actor Dashboard

```dataviewjs
const FOLDER = "30_CIPHER/03_Threat_Actors";
const norm = (v) => (v ?? "").toString().trim();
const lower = (v) => norm(v).toLowerCase();
const arr = (v) => Array.isArray(v) ? v : (v ? [v] : []);

const pages = dv.pages(`"${FOLDER}"`)
  .where(p => lower(p.entity_type) === "threat_actor");

const total = pages.length;
const active = pages.filter(p => lower(p.status) === "active").length;
const highConf = pages.filter(p => lower(p.attribution_confidence) === "high").length;
const missingActorId = pages.filter(p => !norm(p.actor_id) || !/^G\d{4}$/.test(norm(p.actor_id))).length;
const missingIntel = pages.filter(p => arr(p.intel_sources).length === 0).length;
const missingTtps = pages.filter(p => arr(p.ttps).length === 0).length;

dv.header(2, "Summary");
dv.table(
  ["Metric", "Count"],
  [
    ["Total threat actors", total],
    ["Active", active],
    ["High confidence", highConf],
    ["Missing actor_id", missingActorId],
    ["Missing intel_sources", missingIntel],
    ["Missing ttps", missingTtps],
  ]
);

const topTtps = pages
  .map(p => ({
    name: norm(p.common_name) || p.file.name,
    ttps: arr(p.ttps).length,
    path: p.file.path
  }))
  .sort((a, b) => b.ttps - a.ttps)
  .slice(0, 10);

const link = (path, text) => {
  const a = document.createElement("a");
  a.setAttribute("data-href", path);
  a.href = path;
  a.className = "internal-link";
  a.textContent = text;
  return a;
};

dv.header(2, "Coverage Highlights");
dv.table(
  ["Threat Actor", "TTP Count"],
  topTtps.map(r => [link(r.path, r.name), r.ttps])
);

const freq = (items) => {
  const map = new Map();
  for (const it of items) {
    const key = norm(it);
    if (!key) continue;
    map.set(key, (map.get(key) || 0) + 1);
  }
  return Array.from(map.entries()).sort((a, b) => b[1] - a[1]);
};

const allMalware = [];
const allTools = [];
for (const p of pages) {
  allMalware.push(...arr(p.malware));
  allTools.push(...arr(p.tools));
}

const topMalware = freq(allMalware).slice(0, 10);
const topTools = freq(allTools).slice(0, 10);

dv.table(["Top Malware", "Count"], topMalware);
dv.table(["Top Tools", "Count"], topTools);

const allSectors = [];
for (const p of pages) {
  allSectors.push(...arr(p.target_sectors));
}
const topSectors = freq(allSectors);

dv.header(2, "Threat Actors by Target Sector");
dv.table(["Target Sector", "Count"], topSectors);

const sectorLabels = topSectors.map(([label]) => label);
const sectorCounts = topSectors.map(([, count]) => count);
const sectorChartYaml =
  "type: bar\n" +
  "labels: [" + sectorLabels.map(l => '"' + l.replace(/"/g, '\\"') + '"').join(", ") + "]\n" +
  "series:\n" +
  "  - title: Actors\n" +
  "    data: [" + sectorCounts.join(", ") + "]\n" +
  "options:\n" +
  "  indexAxis: y\n";

dv.paragraph("```chart\n" + sectorChartYaml + "```");
```

## Recent Updates
```dataview
TABLE file.mtime AS "Modified", common_name, actor_id, status
FROM "30_CIPHER/03_Threat_Actors"
WHERE entity_type = "threat_actor"
SORT file.mtime DESC
LIMIT 20
```

## Active Actors
```dataview
TABLE common_name, actor_id, country_of_origin, attribution_confidence
FROM "30_CIPHER/03_Threat_Actors"
WHERE entity_type = "threat_actor" AND lower(status) = "active"
SORT common_name ASC
```

## Aliases Quick View
```dataview
TABLE common_name, actor_id, aliases
FROM "30_CIPHER/03_Threat_Actors"
WHERE entity_type = "threat_actor"
SORT common_name ASC
```

## Data Gaps
```dataview
TABLE common_name, actor_id, intel_sources, ttps, aliases
FROM "30_CIPHER/03_Threat_Actors"
WHERE entity_type = "threat_actor" AND (
  !actor_id OR actor_id = "" OR
  !intel_sources OR length(intel_sources) = 0 OR
  !ttps OR length(ttps) = 0 OR
  !aliases OR length(aliases) = 0
)
SORT common_name ASC
```
