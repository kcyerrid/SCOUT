---
entity_type: watchlist
watchlist_id: WL-0001
watchlist_name: ""
purpose: ""
scope: ""                    # RSS | Threat Intel | Brand Monitoring | All
status: active               # active | paused | retired
owner: ""
maintainer: ""
review_cycle: quarterly
last_reviewed: ""
watchlist_categories: []     # default categories for keywords
watchlist_weight: 1          # default weight for keywords (used in RSS ranking)

keywords:
  - term: ""
    categories: []
    weight: 1

tags:
  - "#type/watchlist"

created: ""
updated: ""
---

# 🔎 {{watchlist_name}}

## Purpose
Why this watchlist exists and what it is intended to catch.

---

## Scope & Usage
Describe where this watchlist is applied:
- RSS monitoring
- Incident correlation
- Threat actor tracking
- Executive reporting

---

## Keywords
The following keywords are automatically used by SCOUT to flag content.

> Guidelines:
> - Use **lowercase**
> - Prefer **substring-safe terms** (`cve-2025-`, not full CVE only)
> - Avoid overly generic words unless scoped

```yaml
keywords:
  - term: "microsoft"
    categories: ["vendor", "brand"]
    weight: 5
  - term: "ransomware"
    categories: ["threat"]
    weight: 10
