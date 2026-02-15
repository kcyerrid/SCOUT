---
entity_type: report_index
tags: [report_index]
created:
updated:
---
# Reports Catalog

## Report Types
- rss
- rss_weekly
- executive_brief
- ioc_summary
- cti_campaign
- ir_postmortem
- risk_snapshot
- status_on_demand

## Audience Tags
- audience/analyst
- audience/leadership

---
## All Reports
```dataview
TABLE report_type, report_date, report_status, tags
FROM "90_Views/02_Reports"
WHERE entity_type = "report"
SORT report_date DESC
```

---
## Analyst Reports
```dataview
TABLE report_type, report_date, report_status, tags
FROM "90_Views/02_Reports"
WHERE entity_type = "report" AND contains(tags, "audience/analyst")
SORT report_date DESC
```

---
## Leadership Reports
```dataview
TABLE report_type, report_date, report_status, tags
FROM "90_Views/02_Reports"
WHERE entity_type = "report" AND contains(tags, "audience/leadership")
SORT report_date DESC
```
