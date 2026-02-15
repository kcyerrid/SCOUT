---
date: <% moment(tp.file.title, "YYYY-MM").startOf("month").format("YYYY-MM-DD") %>
tags:
  - "#type/monthly_rollup"
---

---
```calendar-nav

```
---

## Month
<%*
var start_of_month = moment(tp.file.title, "YYYY-MM").startOf("month");
var days_in_month = start_of_month.daysInMonth();
var monthStart = start_of_month.format("YYYY-MM-DD");
var monthEnd = moment(tp.file.title, "YYYY-MM").endOf("month").format("YYYY-MM-DD");

// Admonition header
tR += "> [!picture]- Pictures\n";

// Regex to match image embeds like: ![[...]]
var imageRegex = /!\[\[(.+?)\]\]/g;

for (var i = 0; i < days_in_month; i++) {
  var current = moment(start_of_month).add(i, "days");
  var d = current.format("YYYY-MM-DD");

  // Find the daily note by title (e.g., "2025-01-06")
  var tfile = tp.file.find_tfile(d);
  if (!tfile) {
    continue;
  }

  // Read the daily note contents
  var content = await tp.app.vault.read(tfile);
  var match;

  // Start a line for this day
  var line = "> " + d + ": ";
  var hasImage = false;

  // Extract images and resize as thumbnails
  while ((match = imageRegex.exec(content)) !== null) {
    var target = match[1];
    // Append "|150" to force thumbnail width
    line += "![[" + target + "|150]] ";
    hasImage = true;
  }

  if (hasImage) {
    tR += line + "\n";
  }
}
%>

---
## RSS Watchlist Keyword Frequency (Month)
```dataviewjs
const NEWS_FOLDERS = [
  "20_Intelligence/21_News",
  "00_System/99_Inbox/_staging/21_News"
];
const WATCHLIST_FOLDERS = [
  "10_Operations/13_Watchlists",
  "30_CIPHER/05_Watchlists"
];

const norm = (v) => (v ?? "").toString().trim().toLowerCase();
const arr = (v) => Array.isArray(v) ? v : (v ? [v] : []);

const start = dv.date("<% monthStart %>");
const end = dv.date("<% monthEnd %>");

const watchPages = [];
for (const f of WATCHLIST_FOLDERS) {
  watchPages.push(...dv.pages(`"${f}"`).array());
}

const terms = new Set();
for (const p of watchPages) {
  for (const entry of arr(p.keywords)) {
    if (typeof entry === "string") {
      const t = norm(entry);
      if (t) terms.add(t);
    } else if (entry && typeof entry === "object") {
      const t = norm(entry.term ?? entry.keyword ?? entry.value);
      if (t) terms.add(t);
    }
  }
}

if (terms.size === 0) {
  dv.paragraph("No watchlist keywords found.");
  return;
}

const newsPages = [];
for (const f of NEWS_FOLDERS) {
  newsPages.push(...dv.pages(`"${f}"`).array());
}

const filtered = newsPages.filter((p) => {
  const d = dv.date(p.published ?? p.file?.day ?? p.file?.ctime);
  return d && d >= start && d <= end;
});

if (filtered.length === 0) {
  dv.paragraph("No RSS items in the selected date range.");
  return;
}

const counts = new Map();
for (const t of terms) counts.set(t, 0);

for (const p of filtered) {
  const content = await dv.io.load(p.file.path);
  const blob = norm(`${p.title ?? p.file.name}\n${content}`);
  for (const t of terms) {
    if (blob.includes(t)) {
      counts.set(t, (counts.get(t) || 0) + 1);
    }
  }
}

const rows = Array.from(counts.entries()).sort((a, b) => b[1] - a[1]);
const top = rows.slice(0, 20);
const bottom = rows.slice(-20).reverse();

dv.table(["Top Keywords", "Count"], top);
dv.table(["Bottom Keywords", "Count"], bottom);
```



> [!highlight]- Stand-Out Days
> ```dataview
TABLE aliases
WHERE aliases != null
AND length(aliases) >= 1
AND date >= date(this.file.name + "-01")
AND date <  date(this.file.name + "-01") + dur(1 month)


