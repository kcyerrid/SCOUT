---
type: dashboard
system: CIPHER
title: CIPHER Campaign Dashboard
created: 2025-12-24
tags:
  - "#dashboard/cipher"
  - "#system/cipher"
campaigns_folder: 30_CIPHER/04_Campaigns
campaign_assets_folder:
campaign_notes_folder:
campaign_meetings_folder: 10_Operations/10_Meetings
daily_folder: 10_Operations/09_Journals/01_Daily
campaign_tag_prefix: "#cipher/campaign"
active_status_values:
  - active
  - in_progress
  - live
---

# CIPHER Campaign Dashboard

This dashboard is a single-pane view of **campaign status, activity, execution, and signal**.  
It assumes each campaign is tracked as an **atomic campaign note** with frontmatter (example schema below).

---
# Campaign Control Panel

## Campaign Overview Table (Core Index)
```dataview
TABLE
  campaign_id as "ID",
  campaign_status as "Status",
  risk_level as "Risk",
  first_observed as "First",
  last_observed as "Last",
  length(associated_actors) as "Actors",
  length(malware_families) as "Malware",
  length(associated_ttps) as "TTPs",
  updated as "Updated"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign"
SORT updated DESC

```

---

## Active / Paused / Concluded Counts (Quick Statistics)
```dataview
TABLE
  campaign_status as "Status",
  length(rows) as "Count"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign"
GROUP BY campaign_status
SORT length(rows) DESC

```

---

## Risk Distribution
```dataviewjs
const pages = dv.pages('"30_CIPHER/04_Campaigns"')
  .where(p => p.entity_type === "campaign");

const rank = (r) => {
  r = (r ?? "").toLowerCase();
  if (r === "critical") return 1;
  if (r === "high") return 2;
  if (r === "medium") return 3;
  if (r === "low") return 4;
  return 9; // unknown/missing/other
};

const counts = new Map();
for (const p of pages) {
  const r = (p.risk_level ?? "unknown").toLowerCase();
  counts.set(r, (counts.get(r) ?? 0) + 1);
}

const rows = [...counts.entries()]
  .map(([risk, count]) => [risk, count, rank(risk)])
  .sort((a, b) => a[2] - b[2]);

dv.table(["Risk Level", "Count"], rows.map(r => [r[0], r[1]]));

```

---

## Most Recently Updated Campaigns
```dataview
TABLE
  file.link as "Campaign",
  campaign_id as "ID",
  updated as "Updated",
  risk_level as "Risk",
  campaign_status as "Status"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type = "campaign" AND updated
SORT updated DESC
LIMIT 20

```

---

## Needs Enrichment Queue (Missing Key Fields)
```dataview
TABLE
  file.link as "Campaign",
  campaign_id as "ID",
  campaign_status as "Status",
  risk_level as "Risk",
  first_observed as "First",
  last_observed as "Last",
  choice(length(intel_sources)=0, "❗No sources", "OK") as "Sources",
  choice(length(associated_ttps)=0, "❗No TTPs", "OK") as "TTPs",
  choice(length(malware_families)=0 AND length(tools_used)=0, "❗No tooling", "OK") as "Tooling"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign"
AND (
  !first_observed OR
  !last_observed OR
  !risk_level OR
  length(intel_sources)=0 OR
  length(associated_ttps)=0
)
SORT updated DESC

```

---

## Campaigns By Primary Objective
```dataview
TABLE
  primary_objectives as "Objective",
  length(rows) as "Count"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign" AND primary_objectives
FLATTEN primary_objectives
GROUP BY primary_objectives
SORT length(rows) DESC

```

---

## Campaigns By Target Sector
```dataview
TABLE
  target_sectors as "Sector",
  length(rows) as "Count"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign" AND target_sectors
FLATTEN target_sectors
GROUP BY target_sectors
SORT length(rows) DESC

```

---

## Campaigns By Target Region
```dataview
TABLE
  target_regions as "Region",
  length(rows) as "Count"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign" AND target_regions
FLATTEN target_regions
GROUP BY target_regions
SORT length(rows) DESC

```

---

## Actor --> Campaign Pivot (Who Is Linked to What)
```dataview
TABLE
  associated_actors as "Actor",
  length(rows) as "Campaigns"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign" AND length(associated_actors) > 0
FLATTEN associated_actors
GROUP BY associated_actors
SORT length(rows) DESC

```

---

## Malware --> Campaign Pivot (Atomic Malware Notes)
```dataview
TABLE
  malware_families as "Malware",
  length(rows) as "Campaigns"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign" AND length(malware_families) > 0
FLATTEN malware_families
GROUP BY malware_families
SORT length(rows) DESC

```

---

## Technique Heatlist (Top TTPs Across Campaigns)
```dataview
TABLE
  associated_ttps as "TTP",
  length(rows) as "Campaigns"
FROM "30_CIPHER/04_Campaigns"
WHERE entity_type="campaign" AND length(associated_ttps) > 0
FLATTEN associated_ttps
GROUP BY associated_ttps
SORT length(rows) DESC
LIMIT 30

```

---

## Campaign Scoreboard (Sortable, Weighted)
```dataviewjs
const pages = dv.pages()
  .where(p => p.entity_type === "campaign");

function riskScore(r) {
  const v = (r || "").toLowerCase();
  if (v === "critical") return 5;
  if (v === "high") return 4;
  if (v === "medium") return 3;
  if (v === "low") return 2;
  return 1;
}

const rows = pages.map(p => {
  const ttpCount = (p.associated_ttps ?? []).length;
  const srcCount = (p.intel_sources ?? []).length;
  const actorCount = (p.associated_actors ?? []).length;
  const score = (riskScore(p.risk_level) * 10) + Math.min(ttpCount, 20) + Math.min(srcCount, 10) + Math.min(actorCount, 5);
  return {
    link: p.file.link,
    id: p.campaign_id ?? "",
    status: p.campaign_status ?? "",
    risk: p.risk_level ?? "unknown",
    first: p.first_observed ?? "",
    last: p.last_observed ?? "",
    ttps: ttpCount,
    sources: srcCount,
    score
  };
}).array();

rows.sort((a,b) => b.score - a.score);

dv.table(
  ["Campaign", "ID", "Status", "Risk", "First", "Last", "TTPs", "Sources", "Score"],
  rows.map(r => [r.link, r.id, r.status, r.risk, r.first, r.last, r.ttps, r.sources, r.score])
);

```

---

## Stale Notes (Not Updated in 1 Year)
```dataviewjs
const N_DAYS = 365;
const cutoff = dv.date("today").minus({ days: N_DAYS });

const pages = dv.pages()
  .where(p => p.entity_type === "campaign")
  .where(p => p.updated)
  .where(p => dv.date(p.updated) < cutoff)
  .sort(p => dv.date(p.updated), "asc");

dv.table(
  ["Campaign", "ID", "Risk", "Status", "Updated", "Days Stale"],
  pages.map(p => {
    const upd = dv.date(p.updated);
    const days = Math.floor(dv.date("today").diff(upd, "days").days);
    return [p.file.link, p.campaign_id ?? "", p.risk_level ?? "", p.campaign_status ?? "", p.updated, days];
  })
);

```

---

## Evidence Coverage (Source Count & Gaps)
Highlights campaigns with thin sourcing (e.g. fewer than 3 sources).
```dataviewjs
const MIN_SOURCES = 3;

const pages = dv.pages()
  .where(p => p.entity_type === "campaign")
  .map(p => {
    const srcCount = (p.intel_sources ?? []).length;
    return {
      link: p.file.link,
      id: p.campaign_id ?? "",
      risk: p.risk_level ?? "unknown",
      status: p.campaign_status ?? "unknown",
      sources: srcCount,
      ok: srcCount >= MIN_SOURCES
    };
  }).array();

pages.sort((a,b) => a.sources - b.sources);

dv.table(
  ["Campaign", "ID", "Risk", "Status", "Sources", "Coverage"],
  pages.map(p => [p.link, p.id, p.risk, p.status, p.sources, p.ok ? "OK" : "Needs Sources"])
);

```


