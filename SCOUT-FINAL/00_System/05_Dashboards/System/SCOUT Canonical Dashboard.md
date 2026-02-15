## 📈 Current Signal (last 14 days)
```dataviewjs
// ===== Configuration =====
const DAYS = 14;

const thresholds = {
  energy: { green: 7, yellow: 4 },
  cynicism: { green: 3, yellow: 6 },   // inverted
  productivity: { green: 7, yellow: 4 }
};

function flag(value, metric) {
  if (value == null) return "⚪";
  if (metric === "cynicism") {
    if (value <= thresholds.cynicism.green) return "🟢";
    if (value <= thresholds.cynicism.yellow) return "🟡";
    return "🔴";
  } else {
    if (value >= thresholds[metric].green) return "🟢";
    if (value >= thresholds[metric].yellow) return "🟡";
    return "🔴";
  }
}

// ===== Data =====
const pages = dv.pages('"10_Operations/09_Journals/01_Daily"')
  .where(p => p.file.day && p.file.day >= dv.date("today").minus({ days: DAYS }))
  .sort(p => p.file.day, "desc");

dv.table(
  ["Date", "Energy", "Cynicism", "Productivity"],
  pages.map(p => [
    p.file.day,
    flag(p.energy_rating, "energy") + " " + p.energy_rating,
    flag(p.cynicism_rating, "cynicism") + " " + p.cynicism_rating,
    flag(p.productivity_rating, "productivity") + " " + p.productivity_rating
  ])
);
```

```dataviewjs
const FOLDER = '"10_Operations/09_Journals/01_Daily"';
const DAYS = 14;

// Collect last 14 days
const start = dv.date("today").minus({ days: DAYS - 1 });

const pages = dv.pages(FOLDER)
  .where(p => p.file.day && p.file.day >= start && p.energy_rating != null)
  .sort(p => p.file.day, "asc");

const labels = pages.map(p => p.file.day.toFormat("MM-dd"));
const values = pages.map(p => Number(p.energy_rating));

// Build Charts plugin YAML (no markdown fences needed)
const chartYaml =
  "type: line\n" +
  "labels: [" + labels.map(l => '"' + l + '"').join(", ") + "]\n" +
  "series:\n" +
  "  - title: Energy\n" +
  "    data: [" + values.join(", ") + "]\n" +
  "options:\n" +
  "  scales:\n" +
  "    y:\n" +
  "      min: 0\n" +
  "      max: 10\n";

const code =
  "```chart\n" +
  chartYaml +
  "```";

// Emit the chart block
dv.paragraph(code);
```

```dataviewjs
const FOLDER = '"10_Operations/09_Journals/01_Daily"';
const DAYS = 14;

// Collect last 14 days
const start = dv.date("today").minus({ days: DAYS - 1 });

const pages = dv.pages(FOLDER)
  .where(p => p.file.day && p.file.day >= start && p.cyncism_rating != null)
  .sort(p => p.file.day, "asc");

const labels = pages.map(p => p.file.day.toFormat("MM-dd"));
const values = pages.map(p => Number(p.cynicism_rating));

// Build Charts plugin YAML (no markdown fences needed)
const chartYaml =
  "type: line\n" +
  "labels: [" + labels.map(l => '"' + l + '"').join(", ") + "]\n" +
  "series:\n" +
  "  - title: Cynicism\n" +
  "    data: [" + values.join(", ") + "]\n" +
  "options:\n" +
  "  scales:\n" +
  "    y:\n" +
  "      min: 0\n" +
  "      max: 10\n";

const code =
  "```chart\n" +
  chartYaml +
  "```";

// Emit the chart block
dv.paragraph(code);
```

```dataviewjs
const FOLDER = '"10_Operations/09_Journals/01_Daily"';
const DAYS = 14;

// Collect last 14 days
const start = dv.date("today").minus({ days: DAYS - 1 });

const pages = dv.pages(FOLDER)
  .where(p => p.file.day && p.file.day >= start && p.productivity_rating != null)
  .sort(p => p.file.day, "asc");

const labels = pages.map(p => p.file.day.toFormat("MM-dd"));
const values = pages.map(p => Number(p.productivity_rating));

// Build Charts plugin YAML (no markdown fences needed)
const chartYaml =
  "type: line\n" +
  "labels: [" + labels.map(l => '"' + l + '"').join(", ") + "]\n" +
  "series:\n" +
  "  - title: Productivity\n" +
  "    data: [" + values.join(", ") + "]\n" +
  "options:\n" +
  "  scales:\n" +
  "    y:\n" +
  "      min: 0\n" +
  "      max: 10\n";

const code =
  "```chart\n" +
  chartYaml +
  "```";

// Emit the chart block
dv.paragraph(code);
```


## 🗓️ This Week: What Changed (Sunday - Saturday)
```dataviewjs
const folder = "10_Operations/10_Meetings";
const today = dv.date("today");
const daysSinceSunday = today.weekday % 7;
const weekStart = today.minus({ days: daysSinceSunday }).startOf("day");
const weekEnd = weekStart.plus({ days: 7 });

const pages = dv.pages(`"${folder}"`)
  .where(p => p.type === "meeting" && p.date && p.date >= weekStart && p.date < weekEnd)
  .sort(p => p.date, "asc");

dv.table(
  ["Date", "Meeting", "Projects", "Attendees"],
  pages.map(p => [p.date, p.file.link, p.projects ?? [], p.attendees ?? []])
);
```

## 📝Daily Reviews Logged This Week
```dataview
TASK
FROM "10_Operations/09_Journals/01_Daily"
WHERE icontains(text, "#log/day_review")
AND file.day >= date(today) - dur(7 days)
SORT file.day ASC
```

## ✅ Open Action Items
```dataview
TASK
FROM "10_Operations/10_Meetings"
WHERE !completed
SORT file.ctime DESC
```

## ⏳ Aging Tasks (30+ days)
```dataview
TASK
WHERE !completed
AND created <= date(today) - dur(30 days)
SORT created ASC
```