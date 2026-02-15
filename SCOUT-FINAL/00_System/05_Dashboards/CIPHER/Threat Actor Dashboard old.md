```dataviewjs
const FOLDER = "30_CIPHER/03_Threat_Actors";

// --------------------
// Helpers
// --------------------
const norm = (v) => (v ?? "").toString().trim();
const lower = (v) => norm(v).toLowerCase();
const arr = (v) => Array.isArray(v) ? v : (v ? [v] : []);

const STATUS_ORDER = { "active": 1, "suspected": 2, "dormant": 3, "inactive": 4, "": 9 };
const CONF_ORDER   = { "high": 1, "medium": 2, "low": 3, "": 9 };

function buildHaystack(p) {
  const aliases = arr(p.aliases).map(norm);
  return [
    p.file?.name,
    p.common_name,
    p.actor_id,
    ...aliases
  ].filter(Boolean).join(" ").toLowerCase();
}

function makeTable(headers, rows) {
  const table = document.createElement("table");
  table.style.width = "100%";

  const thead = document.createElement("thead");
  const trh = document.createElement("tr");
  for (const h of headers) {
    const th = document.createElement("th");
    th.textContent = h;
    trh.appendChild(th);
  }
  thead.appendChild(trh);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  for (const row of rows) {
    const tr = document.createElement("tr");
    for (const cell of row) {
      const td = document.createElement("td");
      if (cell instanceof HTMLElement) td.appendChild(cell);
      else td.textContent = (cell ?? "").toString();
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  }
  table.appendChild(tbody);

  return table;
}

function makeLink(path, text) {
  // Use Obsidian's link format; clicking works normally in preview/reading view.
  const a = document.createElement("a");
  a.setAttribute("data-href", path);
  a.href = path;
  a.className = "internal-link";
  a.textContent = text;
  return a;
}

// --------------------
// UI
// --------------------
const root = dv.el("div", "");
const label = dv.el("div", "Search threat actors (name, actor_id, aliases):", {}, root);

const input = document.createElement("input");
input.type = "text";
input.placeholder = "e.g., APT28, G0007, Fancy Bear…";
input.style.width = "100%";
input.style.padding = "8px 10px";
input.style.border = "1px solid var(--background-modifier-border)";
input.style.borderRadius = "8px";
input.style.background = "var(--background-primary)";
input.style.color = "var(--text-normal)";
root.appendChild(input);

const resultsDiv = document.createElement("div");
resultsDiv.style.marginTop = "12px";
root.appendChild(resultsDiv);

// --------------------
// Load pages once
// --------------------
const pages = dv.pages(`"${FOLDER}"`)
  .where(p => lower(p.entity_type) === "threat_actor");

// --------------------
// Build rows + group
// --------------------
function getGrouped(filterText) {
  const q = lower(filterText);

  let rows = pages.map(p => {
    const displayName = norm(p.common_name) || p.file.name;

    return {
      path: p.file.path,
      name: displayName,
      country: norm(p.country_of_origin) || "Unknown",
      status: norm(p.status) || "Unknown",
      conf: norm(p.attribution_confidence) || "Unknown",
      statusKey: STATUS_ORDER[lower(p.status)] ?? 8,
      confKey: CONF_ORDER[lower(p.attribution_confidence)] ?? 8,
      hay: buildHaystack(p)
    };
  });

  if (q) rows = rows.filter(r => r.hay.includes(q));

  const byCountry = new Map();
  for (const r of rows) {
    if (!byCountry.has(r.country)) byCountry.set(r.country, []);
    byCountry.get(r.country).push(r);
  }

  const countries = Array.from(byCountry.keys()).sort((a,b) => a.localeCompare(b));

  for (const c of countries) {
    byCountry.get(c).sort((a,b) =>
      (a.statusKey - b.statusKey) ||
      (a.confKey - b.confKey) ||
      a.name.localeCompare(b.name)
    );
  }

  return { byCountry, countries, total: rows.length };
}

// --------------------
// Render
// --------------------
function render() {
  resultsDiv.innerHTML = "";

  const { byCountry, countries, total } = getGrouped(input.value);

  const meta = document.createElement("div");
  meta.textContent = `Results: ${total}`;
  meta.style.color = "var(--text-muted)";
  meta.style.margin = "6px 0 12px";
  resultsDiv.appendChild(meta);

  // Summary table
  const summaryRows = countries.map(c => {
    const group = byCountry.get(c);
    const active = group.filter(x => lower(x.status) === "active").length;
    const high = group.filter(x => lower(x.conf) === "high").length;
    return [c, group.length, active, high];
  });

  const h2a = document.createElement("h2");
  h2a.textContent = "Threat Actors by Country (Summary)";
  resultsDiv.appendChild(h2a);

  resultsDiv.appendChild(
    makeTable(["Country of Origin", "# Actors", "# Active", "# High Confidence"], summaryRows)
  );

  // Detail
  const h2b = document.createElement("h2");
  h2b.textContent = "Threat Actors by Country (Detail)";
  h2b.style.marginTop = "18px";
  resultsDiv.appendChild(h2b);

  for (const c of countries) {
    const group = byCountry.get(c);

    const h3 = document.createElement("h3");
    h3.textContent = `${c} (${group.length})`;
    resultsDiv.appendChild(h3);

    const detailRows = group.map(x => ([
      makeLink(x.path, x.name),
      x.status,
      x.conf
    ]));

    resultsDiv.appendChild(
      makeTable(["Threat Actor", "Status", "Confidence"], detailRows)
    );
  }
}

input.addEventListener("input", render);
render();

```