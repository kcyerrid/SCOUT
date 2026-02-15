---
tags: [dashboard, scout, threat-actors]
# Optional: set a focus actor for the “Focus Panel” section (paste a wiki-link to a TA note)
# focus_actor: "[[30_CIPHER/03_Threat_Actors/G0106 - Rocke|Rocke (G0106)]]"
---

# Threat Actor Dashboard

> **Scope:** Threat actors (SCOUT-TA)  
> **Data source:** notes where `entity_type = threat_actor` OR tagged `scout-ta` OR in folder `30_CIPHER/03_Threat_Actors`

---

## KPI Overview

```dataviewjs
// ---- CONFIG ----
const FOLDER_HINT = "30_CIPHER/03_Threat_Actors";
const TAG_HINT = "scout-ta";

// ---- LOAD PAGES ----
const pages = dv.pages()
  .where(p =>
    p?.entity_type === "threat_actor" ||
    (Array.isArray(p?.tags) && p.tags.includes(TAG_HINT)) ||
    (p?.file?.path && p.file.path.includes(FOLDER_HINT))
  );

// ---- HELPERS ----
const norm = (v, fallback="Unknown") => (v === null || v === undefined || v === "" ? fallback : v);
const asArray = (v) => Array.isArray(v) ? v : (v ? [v] : []);
const daysBetween = (d1, d2) => Math.floor((d1 - d2) / (1000*60*60*24));

const now = new Date();
const total = pages.length;

const byStatus = {};
const byType = {};
const byAttrib = {};
const byMotivation = {};
const byRegion = {};
const missing = { actor_id: 0, actor_type: 0, ttps: 0, malware: 0 };

let modified7d = 0;
let created30d = 0;

for (const p of pages) {
  const status = norm(p.status);
  const type = norm(p.actor_type);
  const attrib = norm(p.attribution_confidence);

  byStatus[status] = (byStatus[status] || 0) + 1;
  byType[type] = (byType[type] || 0) + 1;
  byAttrib[attrib] = (byAttrib[attrib] || 0) + 1;

  for (const m of asArray(p.motivations)) {
    const mm = norm(m);
    byMotivation[mm] = (byMotivation[mm] || 0) + 1;
  }
  for (const r of asArray(p.target_regions)) {
    const rr = norm(r);
    byRegion[rr] = (byRegion[rr] || 0) + 1;
  }

  if (!p.actor_id) missing.actor_id++;
  if (!p.actor_type) missing.actor_type++;
  if (!p.ttps || asArray(p.ttps).length === 0) missing.ttps++;
  if (!p.malware || asArray(p.malware).length === 0) missing.malware++;

  if (daysBetween(now, p.file.mtime) <= 7) modified7d++;
  if (daysBetween(now, p.file.ctime) <= 30) created30d++;
}

function topN(obj, n=5) {
  return Object.entries(obj).sort((a,b) => b[1]-a[1]).slice(0,n);
}

function kpiCard(title, value, subtitle="") {
  const card = dv.el("div", "", { cls: "scout-kpi-card" });
  dv.el("div", title, { parent: card, cls: "scout-kpi-title" });
  dv.el("div", String(value), { parent: card, cls: "scout-kpi-value" });
  if (subtitle) dv.el("div", subtitle, { parent: card, cls: "scout-kpi-sub" });
  return card;
}

const wrap = dv.el("div", "", { cls: "scout-kpi-wrap" });
wrap.appendChild(kpiCard("Total Threat Actors", total, "entity_type=threat_actor / scout-ta / folder match"));
wrap.appendChild(kpiCard("Modified (last 7d)", modified7d));
wrap.appendChild(kpiCard("Created (last 30d)", created30d));
wrap.appendChild(kpiCard("Missing actor_id", missing.actor_id));
wrap.appendChild(kpiCard("Missing actor_type", missing.actor_type));
wrap.appendChild(kpiCard("No TTPs", missing.ttps));
wrap.appendChild(kpiCard("No Malware", missing.malware));

dv.el("hr");

dv.el("h3", "Top Distributions");
dv.el("div", "Status (top 5): " + topN(byStatus).map(([k,v]) => `${k}: ${v}`).join(" • "));
dv.el("div", "Type (top 5): " + topN(byType).map(([k,v]) => `${k}: ${v}`).join(" • "));
dv.el("div", "Attribution Confidence (top 5): " + topN(byAttrib).map(([k,v]) => `${k}: ${v}`).join(" • "));
dv.el("div", "Motivations (top 5): " + topN(byMotivation).map(([k,v]) => `${k}: ${v}`).join(" • "));
dv.el("div", "Target Regions (top 5): " + topN(byRegion).map(([k,v]) => `${k}: ${v}`).join(" • "));
```

---

## Threat Actor Registry (Master Table)
```dataview
TABLE
  actor_id as "ID",
  link(file.link, default(actor_name, file.name)) as "Actor",
  actor_type as "Type",
  attribution_confidence as "Attrib",
  status as "Status",
  join(motivations, ", ") as "Motivations",
  join(target_regions, ", ") as "Regions",
  length(ttps) as "TTPs",
  length(malware) as "Malware",
  file.mtime as "Modified"
FROM ""
WHERE
  entity_type = "threat_actor"
  OR contains(file.path, "30_CIPHER/03_Threat_Actors")
  OR contains(tags, "scout-ta")
SORT file.mtime DESC

```