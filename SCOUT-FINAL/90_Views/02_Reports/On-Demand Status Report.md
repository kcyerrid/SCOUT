---
entity_type: report
report_type: status_on_demand
report_date:
report_period_start: 2026-01-18
report_period_end: 2026-01-25
report_status: draft
tags:
  - audience/analyst
report_sections:
  - name: Accomplishments
    tags:
      - "#action/highlight"
  - name: Incidents
    entity_type: incident
    tags: []
  - name: Impact
    tags:
      - "#milestone/impact"
  - name: Weekly Report Other
    tags:
      - "#report/weekly"
created:
updated:
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
# On-Demand Status Report

## Report Period
- Start: `INPUT[date:report_period_start]`
- End: `INPUT[date:report_period_end]`

## Section Tag Mapping
Edit `report_sections` in frontmatter to control tags or entity_type per section.

---
```dataviewjs
const startRaw = dv.current().report_period_start;
const endRaw = dv.current().report_period_end;
if (!startRaw || !endRaw) {
  dv.paragraph("Set the report period start/end dates to generate results.");
  return;
}

const start = dv.date(startRaw);
const end = dv.date(endRaw);
const dailyPath = "10_Operations/09_Journals/01_Daily";
const sections = dv.current().report_sections ?? [];
const tagRegex = /(#[A-Za-z0-9/_-]+)/g;

const pages = dv
  .pages(`"${dailyPath}"`)
  .where((p) => p.file?.day >= start && p.file?.day <= end)
  .sort((p) => p.file.day, "asc");

const pageContents = [];
for (const page of pages) {
  const content = await dv.io.load(page.file.path);
  pageContents.push({ page, lines: content.split("\n") });
}

const extractTags = (line) => (line.match(tagRegex) ?? []);
const getCreatedDate = (page) => {
  const created = page.created ?? page.file?.ctime;
  return created ? dv.date(created) : null;
};

for (const section of sections) {
  const sectionName = section?.name ?? "Section";
  const sectionTags = (section?.tags ?? []).map(String);
  const tagSet = new Set(sectionTags);
  const sectionEntity = section?.entity_type;

  dv.header(2, sectionName);

  if (sectionEntity) {
    const entityPages = dv
      .pages()
      .where((p) => p.entity_type === sectionEntity)
      .where((p) => {
        const created = getCreatedDate(p);
        return created && created >= start && created <= end;
      })
      .sort((p) => getCreatedDate(p), "asc");

    if (entityPages.length === 0) {
      dv.paragraph("No matching entity notes found for this section.");
    } else {
      dv.table(
        ["Note", "Created", "Status", "Severity"],
        entityPages.map((p) => [
          p.file.link,
          p.created ?? p.file?.ctime ?? "",
          p.status ?? "",
          p.severity ?? ""
        ])
      );
    }
    continue;
  }

  if (sectionTags.length === 0) {
    dv.paragraph("No tags configured for this section.");
    continue;
  }

  const rows = [];
  for (const { page, lines } of pageContents) {
    for (const rawLine of lines) {
      const line = rawLine.trim();
      if (!line.includes("#")) continue;
      const matchedTags = extractTags(line).filter((tag) => tagSet.has(tag));
      if (matchedTags.length === 0) continue;
      rows.push([page.file.link, line, matchedTags.join(", ")]);
    }
  }

  if (rows.length === 0) {
    dv.paragraph("No tagged entries found for this section.");
  } else {
    dv.table(["Daily Note", "Entry", "Tags"], rows);
  }
}
```
