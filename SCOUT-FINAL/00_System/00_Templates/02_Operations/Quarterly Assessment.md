---
entity_type: quarterly_journal
journal_date: 
spiritual: 8
career: 6
relationships: 2
health: 5
growth: 7
recreation: 2
social: 8
finance: 8
quarter_start: <% tp.date.now("YYYY-MM-DD").startOf("quarter").format("YYYY-MM-DD") %>
quarter_end: <% tp.date.now("YYYY-MM-DD").endOf("quarter").format("YYYY-MM-DD") %>
created: 
updated: 
journal: Journal Quarterly
---


```dataviewjs
const DIMENSIONS = [
  { key: "spiritual", label: "Spiritual" },
  { key: "career", label: "Career" },
  { key: "relationships", label: "Relationships" },
  { key: "health", label: "Health" },
  { key: "growth", label: "Personal Growth" },
  { key: "recreation", label: "Fun" },
  { key: "social", label: "Social" },
  { key: "finance", label: "Finances" },
];

const COLORS = {
  background: [
    "rgba(103, 58, 183, 0.4)",
    "rgba(3, 169, 244, 0.4)",
    "rgba(233, 30, 99, 0.4)",
    "rgba(0, 150, 136, 0.4)",
    "rgba(255, 87, 34, 0.4)",
    "rgba(255, 193, 7, 0.4)",
    "rgba(156, 39, 176, 0.4)",
    "rgba(76, 175, 80, 0.4)",
  ],
  border: [
    "rgba(103, 58, 183, 0.9)",
    "rgba(3, 169, 244, 0.9)",
    "rgba(233, 30, 99, 0.9)",
    "rgba(0, 150, 136, 0.9)",
    "rgba(255, 87, 34, 0.9)",
    "rgba(255, 193, 7, 0.9)",
    "rgba(156, 39, 176, 0.9)",
    "rgba(76, 175, 80, 0.9)",
  ],
};

const clamp = (value) => Math.max(0, Math.min(10, Number(value) || 0));
const values = {};
for (const dim of DIMENSIONS) {
  values[dim.key] = clamp(dv.current()[dim.key]);
}

const buildChartData = () => ({
  type: "polarArea",
  data: {
    labels: DIMENSIONS.map((d) => d.label),
    datasets: [
      {
        data: DIMENSIONS.map((d) => values[d.key]),
        backgroundColor: COLORS.background,
        borderColor: COLORS.border,
        borderWidth: 2,
      },
    ],
  },
  options: {
    plugins: {
      legend: { position: "bottom" },
    },
    scales: {
      r: {
        angleLines: {
          display: true,
          color: "rgba(200,200,200,0.5)",
        },
        grid: {
          color: "rgba(150,150,150,0.3)",
          lineWidth: 1,
        },
        ticks: {
          display: true,
          stepSize: 1,
          color: "black",
          font: { size: 12, family: "'Inter', sans-serif" },
          backdropColor: "transparent",
        },
        min: 1,
        max: 10,
      },
    },
  },
});

const container = this.container;
container.style.padding = "20px";
container.style.overflow = "hidden";

const chartContainer = container.createDiv({ cls: "wheel-of-life-chart" });
chartContainer.style.height = "520px";
chartContainer.style.marginBottom = "24px";

const form = container.createDiv({ cls: "wheel-of-life-form" });
form.style.display = "grid";
form.style.gridTemplateColumns = "1fr";
form.style.rowGap = "12px";
form.style.marginTop = "150px";

const controls = {};
for (const dim of DIMENSIONS) {
  const row = form.createDiv({ cls: "wheel-of-life-row" });
  row.style.display = "grid";
  row.style.gridTemplateColumns = "140px 1fr 32px";
  row.style.alignItems = "center";
  row.style.columnGap = "12px";

  row.createSpan({ text: dim.label });

  const slider = row.createEl("input", {
    type: "range",
    attr: { min: "0", max: "10", step: "1" },
  });
  slider.value = String(values[dim.key]);

  const valueLabel = row.createSpan({ text: String(values[dim.key]) });
  valueLabel.style.textAlign = "right";

  slider.addEventListener("input", () => {
    values[dim.key] = clamp(slider.value);
    valueLabel.textContent = String(values[dim.key]);
    window.renderChart(buildChartData(), chartContainer);
  });

  controls[dim.key] = { slider, valueLabel };
}

const actions = container.createDiv({ cls: "wheel-of-life-actions" });
actions.style.marginTop = "16px";
actions.style.display = "flex";
actions.style.gap = "12px";
actions.style.alignItems = "center";

const saveButton = actions.createEl("button", { text: "Save scores" });
const status = actions.createSpan({ text: "" });

saveButton.addEventListener("click", async () => {
  const file = app.vault.getAbstractFileByPath(dv.current().file.path);
  if (!file) {
    status.textContent = "Could not locate the current note.";
    return;
  }

  saveButton.disabled = true;
  status.textContent = "Saving...";

  try {
    await app.fileManager.processFrontMatter(file, (fm) => {
      for (const dim of DIMENSIONS) {
        fm[dim.key] = values[dim.key];
      }
    });
    status.textContent = "Saved.";
  } catch (err) {
    status.textContent = "Save failed.";
  } finally {
    saveButton.disabled = false;
  }
});

window.renderChart(buildChartData(), chartContainer);
```

## RSS Watchlist Keyword Frequency (Quarter)
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

const startRaw = dv.current().quarter_start;
const endRaw = dv.current().quarter_end;
const start = startRaw ? dv.date(startRaw) : dv.date("today").startOf("quarter");
const end = endRaw ? dv.date(endRaw) : dv.date("today").endOf("quarter");

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
const top = rows.slice(0, 25);
const bottom = rows.slice(-25).reverse();

dv.table(["Top Keywords", "Count"], top);
dv.table(["Bottom Keywords", "Count"], bottom);
```

```dataviewjs
const DAILY_FOLDER = "10_Operations/09_Journals/01_Daily";
const currentDate = dv.current().file?.day ?? dv.date("today");
const overrideStart = dv.current().quarter_start ? dv.date(dv.current().quarter_start) : null;
const overrideEnd = dv.current().quarter_end ? dv.date(dv.current().quarter_end) : null;
const start = overrideStart ?? currentDate.startOf("quarter");
const end = overrideEnd ?? currentDate.endOf("quarter");

if (!start || !end) {
  dv.paragraph("Unable to determine quarter range for energy trends.");
} else {
  const rows = dv.pages(`"${DAILY_FOLDER}"`)
    .where((p) => p.file?.day && p.file.day >= start && p.file.day <= end)
    .map((p) => ({
      date: p.file.day,
      energy: Number(p.energy_rating),
    }))
    .where((p) => !Number.isNaN(p.energy))
    .array()
    .sort((a, b) => a.date - b.date);

  if (rows.length === 0) {
    dv.paragraph("No daily notes with energy_rating in the selected quarter.");
  } else {
    const total = rows.reduce((sum, row) => sum + row.energy, 0);
    const average = total / rows.length;

    dv.header(2, "Energy Rating (Quarter)");
    dv.paragraph(`Average energy_rating: ${average.toFixed(2)} (${rows.length} days)`);

    const labels = rows.map((row) => row.date.toFormat("yyyy-LL-dd"));
    const values = rows.map((row) => row.energy);

    const n = rows.length;
    const xs = rows.map((_, i) => i);
    const sumX = xs.reduce((s, x) => s + x, 0);
    const sumY = values.reduce((s, y) => s + y, 0);
    const sumXY = xs.reduce((s, x, i) => s + x * values[i], 0);
    const sumX2 = xs.reduce((s, x) => s + x * x, 0);
    const denom = n * sumX2 - sumX * sumX;
    const slope = denom === 0 ? 0 : (n * sumXY - sumX * sumY) / denom;
    const intercept = n === 0 ? 0 : (sumY - slope * sumX) / n;
    const trend = xs.map((x) => slope * x + intercept);

    const chartData = {
      type: "line",
      data: {
        labels,
        datasets: [
          {
            label: "Energy rating",
            data: values,
            fill: true,
            backgroundColor: "rgba(3, 169, 244, 0.25)",
            borderColor: "rgba(3, 169, 244, 0.9)",
            tension: 0.3,
            pointRadius: 2,
          },
          {
            label: "Trend",
            data: trend,
            fill: false,
            borderColor: "rgba(255, 255, 255, 0.7)",
            borderDash: [6, 4],
            pointRadius: 0,
          },
        ],
      },
      options: {
        plugins: {
          legend: { position: "bottom" },
        },
        scales: {
          y: {
            min: 0,
            max: 10,
            ticks: { stepSize: 1, color: "white" },
            grid: { color: "rgba(150,150,150,0.3)" },
          },
          x: {
            type: "category",
            title: { display: true, text: "Date", color: "white" },
            ticks: { color: "white", maxTicksLimit: 10 },
            grid: { color: "rgba(150,150,150,0.1)" },
          },
        },
      },
    };

    const chartContainer = this.container.createDiv({
      cls: "energy-rating-chart",
    });
    chartContainer.style.height = "360px";
    chartContainer.style.marginTop = "12px";

    window.renderChart(chartData, chartContainer);

    const cynicismRows = dv.pages(`"${DAILY_FOLDER}"`)
      .where((p) => p.file?.day && p.file.day >= start && p.file.day <= end)
      .map((p) => ({
        date: p.file.day,
        cynicism: Number(p.cynicism_rating),
      }))
      .where((p) => !Number.isNaN(p.cynicism))
      .array()
      .sort((a, b) => a.date - b.date);

    if (cynicismRows.length === 0) {
      dv.paragraph("No daily notes with cynicism_rating in the selected quarter.");
    } else {
      const totalCynicism = cynicismRows.reduce((sum, row) => sum + row.cynicism, 0);
      const avgCynicism = totalCynicism / cynicismRows.length;

      dv.header(2, "Cynicism Rating (Quarter)");
      dv.paragraph(`Average cynicism_rating: ${avgCynicism.toFixed(2)} (${cynicismRows.length} days)`);

      const cynicismLabels = cynicismRows.map((row) => row.date.toFormat("yyyy-LL-dd"));
      const cynicismValues = cynicismRows.map((row) => row.cynicism);

      const n2 = cynicismRows.length;
      const xs2 = cynicismRows.map((_, i) => i);
      const sumX2 = xs2.reduce((s, x) => s + x, 0);
      const sumY2 = cynicismValues.reduce((s, y) => s + y, 0);
      const sumXY2 = xs2.reduce((s, x, i) => s + x * cynicismValues[i], 0);
      const sumX22 = xs2.reduce((s, x) => s + x * x, 0);
      const denom2 = n2 * sumX22 - sumX2 * sumX2;
      const slope2 = denom2 === 0 ? 0 : (n2 * sumXY2 - sumX2 * sumY2) / denom2;
      const intercept2 = n2 === 0 ? 0 : (sumY2 - slope2 * sumX2) / n2;
      const trend2 = xs2.map((x) => slope2 * x + intercept2);

      const cynicismChartData = {
        type: "line",
        data: {
          labels: cynicismLabels,
          datasets: [
            {
              label: "Cynicism rating",
              data: cynicismValues,
              fill: true,
              backgroundColor: "rgba(233, 30, 99, 0.25)",
              borderColor: "rgba(233, 30, 99, 0.9)",
              tension: 0.3,
              pointRadius: 2,
            },
            {
              label: "Trend",
              data: trend2,
              fill: false,
              borderColor: "rgba(255, 255, 255, 0.7)",
              borderDash: [6, 4],
              pointRadius: 0,
            },
          ],
        },
        options: {
          plugins: {
            legend: { position: "bottom" },
          },
          scales: {
            y: {
              min: 0,
              max: 10,
              ticks: { stepSize: 1, color: "white" },
              grid: { color: "rgba(150,150,150,0.3)" },
            },
            x: {
              type: "category",
              title: { display: true, text: "Date", color: "white" },
              ticks: { color: "white", maxTicksLimit: 10 },
              grid: { color: "rgba(150,150,150,0.1)" },
            },
          },
        },
      };

      const cynicismChartContainer = this.container.createDiv({
        cls: "cynicism-rating-chart",
      });
      cynicismChartContainer.style.height = "360px";
      cynicismChartContainer.style.marginTop = "12px";

      window.renderChart(cynicismChartData, cynicismChartContainer);
    }

    const productivityRows = dv.pages(`"${DAILY_FOLDER}"`)
      .where((p) => p.file?.day && p.file.day >= start && p.file.day <= end)
      .map((p) => ({
        date: p.file.day,
        productivity: Number(p.productivity_rating),
      }))
      .where((p) => !Number.isNaN(p.productivity))
      .array()
      .sort((a, b) => a.date - b.date);

    if (productivityRows.length === 0) {
      dv.paragraph("No daily notes with productivity_rating in the selected quarter.");
    } else {
      const totalProductivity = productivityRows.reduce(
        (sum, row) => sum + row.productivity,
        0
      );
      const avgProductivity = totalProductivity / productivityRows.length;

      dv.header(2, "Productivity Rating (Quarter)");
      dv.paragraph(
        `Average productivity_rating: ${avgProductivity.toFixed(2)} (${productivityRows.length} days)`
      );

      const productivityLabels = productivityRows.map((row) =>
        row.date.toFormat("yyyy-LL-dd")
      );
      const productivityValues = productivityRows.map((row) => row.productivity);

      const n3 = productivityRows.length;
      const xs3 = productivityRows.map((_, i) => i);
      const sumX3 = xs3.reduce((s, x) => s + x, 0);
      const sumY3 = productivityValues.reduce((s, y) => s + y, 0);
      const sumXY3 = xs3.reduce((s, x, i) => s + x * productivityValues[i], 0);
      const sumX23 = xs3.reduce((s, x) => s + x * x, 0);
      const denom3 = n3 * sumX23 - sumX3 * sumX3;
      const slope3 = denom3 === 0 ? 0 : (n3 * sumXY3 - sumX3 * sumY3) / denom3;
      const intercept3 = n3 === 0 ? 0 : (sumY3 - slope3 * sumX3) / n3;
      const trend3 = xs3.map((x) => slope3 * x + intercept3);

      const productivityChartData = {
        type: "line",
        data: {
          labels: productivityLabels,
          datasets: [
            {
              label: "Productivity rating",
              data: productivityValues,
              fill: true,
              backgroundColor: "rgba(76, 175, 80, 0.25)",
              borderColor: "rgba(76, 175, 80, 0.9)",
              tension: 0.3,
              pointRadius: 2,
            },
            {
              label: "Trend",
              data: trend3,
              fill: false,
              borderColor: "rgba(255, 255, 255, 0.7)",
              borderDash: [6, 4],
              pointRadius: 0,
            },
          ],
        },
        options: {
          plugins: {
            legend: { position: "bottom" },
          },
          scales: {
            y: {
              min: 0,
              max: 10,
              ticks: { stepSize: 1, color: "white" },
              grid: { color: "rgba(150,150,150,0.3)" },
            },
            x: {
              type: "category",
              title: { display: true, text: "Date", color: "white" },
              ticks: { color: "white", maxTicksLimit: 10 },
              grid: { color: "rgba(150,150,150,0.1)" },
            },
          },
        },
      };

      const productivityChartContainer = this.container.createDiv({
        cls: "productivity-rating-chart",
      });
      productivityChartContainer.style.height = "360px";
      productivityChartContainer.style.marginTop = "12px";

      window.renderChart(productivityChartData, productivityChartContainer);
    }

    const quarterDays = Math.floor(end.diff(start, "days").days) + 1;
    const asOf = currentDate > end ? end : currentDate;
    const elapsedDays = Math.max(0, Math.floor(asOf.diff(start, "days").days) + 1);

    dv.header(2, "Journal Coverage (Quarter)");
    const coverageDays = Math.max(1, elapsedDays);
    const coveragePct = Math.min(100, (rows.length / coverageDays) * 100);
    dv.paragraph(
      `Daily notes recorded: ${rows.length} / ${coverageDays} days (elapsed)`
    );
    dv.paragraph(`Coverage rate: ${coveragePct.toFixed(1)}%`);
    dv.paragraph(
      `Days elapsed in quarter as of ${asOf.toFormat("yyyy-LL-dd")}: ${elapsedDays} / ${quarterDays}`
    );
  }
}
```

