---
entity_type: watchlist
watchlist_id: WL-0001
watchlist_name: "Company / Brand Watchlist"
purpose: "To track all vendors and companies that we do business with"
scope: ""                    # RSS | Threat Intel | Brand Monitoring | All
status: active               # active | paused | retired
owner: ""
maintainer: ""
review_cycle: quarterly
last_reviewed: ""

keywords:
  - term: "microsoft"
    weight: 1
  - term: "palo alto"
    weight: 1
  - term: "crowdstrike"
    weight: 1
  - term: "atlassian"
    weight: 1
  - term: "wiz"
    weight: 1
  - term: "google"
    weight: 1
  - term: "openai"
    weight: 1
  - term: "loanDepot"
    categories: ["Company"]
    weight: 2
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
  - example keyword