---
doc_type: governance
governance_domain: ""
governance_scope: ""
status: authoritative
audience:
  - analysts
  - engineers
  - leadership
last_reviewed: ""
next_review: ""
owner: ""
related_programs:
  - SCOUT
tags:
  - governance
  - reference
exclude_from_graph: true
exclude_from_reporting: true
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
---
## Purpose

The ITID (Incident Type Identification Digit) system exists to provide a **consistent, durable, and analyst-friendly method of classifying security incidents** across Security Cyber Operations.

The ITID Master Template defines the **authoritative structure, required metadata, and governance rules** for all ITID notes in SCOUT. Its purpose is to ensure that incident classification is:

- Consistent across analysts and time
- Precise at the operational level
- Stable at the reporting level
- Decoupled from tools, vendors, and transient alert names

---

## What an ITID Is

An ITID is a **canonical classification entity** that represents _what happened_, independent of:

- Detection source
- Tooling
- Incident volume
- Threat actor attribution
- Response outcome

An ITID answers the question:

> “What type of security event is this, in a way that remains meaningful over time?”

Each ITID is a **first-class entity** within SCOUT and must be treated as a stable reference point.

---

## What an ITID Is Not

An ITID is **not**:

- A detection or alert name
- A case or incident record
- A threat actor label
- A malware family
- A playbook or response procedure
- A reporting category alone

ITIDs intentionally avoid coupling classification to tooling or intelligence conclusions.

---

## Canonical Structure

Each ITID must be represented by **a single note** created from the ITID template.  
That note is the **sole source of truth** for that ITID.

ITID notes contain:

- Definition and scope
- Inclusion and exclusion criteria
- Classification guidance
- Reporting rollups
- Framework mappings
- Governance metadata

Duplicated or “shadow” ITID definitions are not permitted.

---

## Required vs Optional Fields

### Required Fields

Every ITID must define, at minimum:

- `itid_id` – Stable identifier
- `itid_name` – Human-readable classification name
- `itid_category` – Logical grouping
- `definition` – Plain-English description
- `scope_includes` / `scope_excludes` – Boundary clarity
- `reporting_rollup` – Executive aggregation mapping
- `status` – Lifecycle state

An ITID without these elements is incomplete and should not be used.

---

### Optional (But Strongly Encouraged) Fields

Optional fields enhance consistency and analytical value:

- MITRE ATT&CK mappings
- Detection coverage references
- Typical indicators or signals
- Common false positives
- Severity guidance
- Related ITIDs (parent/child relationships)

Optional does not mean unimportant; it means **not required for initial creation**.

---

## Filename as Authority

ITIDs follow a strict filename convention:

`<ITID_ID> - <ITID_Name>.md`

Example:

`LD-11100 - Password Spray.md`

The filename is the **authoritative source** for:

- `itid_id`
- `itid_name`
    

Templates derive these values from the filename to prevent drift.

---

## Parent and Child ITIDs

ITIDs may be hierarchical:

- Parent ITIDs represent broad categories
- Child ITIDs represent specific manifestations

Example:

- `LD-11000` — Credential Abuse
    - `LD-11100` — Password Spray
    - `LD-11200` — Credential Stuffing
    - `LD-11300` — MFA Fatigue

Parent ITIDs are used for **conceptual grouping**, not incident classification unless explicitly intended.

---

## Reporting Rollup

The `reporting_rollup` field exists to **decouple operational precision from executive reporting**.

Analysts classify incidents using the most specific ITID possible.  
Leadership reporting aggregates incidents using `reporting_rollup`.

This allows:

- ITID taxonomy evolution without reworking dashboards
- Stable reporting language over time
- Multiple ITIDs to map to a single reporting category

`reporting_rollup` is defined **once**, on the ITID, and inherited by all incidents that reference it.

---

## Relationship to Incidents

Incidents reference ITIDs; ITIDs do **not** reference incidents by default.

This ensures that:

- ITIDs remain stable
- Incident volume does not pollute classification entities
- Historical incidents automatically benefit from ITID updates

When examples are useful, they may be listed in the ITID body as **non-exhaustive illustrations**, not as authoritative records.

---

## Change Management

ITIDs are governed entities and must evolve carefully.

### Allowed Changes

- Clarifying definitions
- Refining scope language
- Updating mappings
- Adjusting reporting rollups

### Restricted Changes

- Renaming ITIDs
- Reusing ITID IDs
- Deleting ITIDs with historical usage

Breaking changes should result in **new ITIDs**, not retroactive modification.

---

## Lifecycle States

Each ITID must declare a lifecycle status:

- `active` – Approved and in use
- `deprecated` – No longer recommended, retained for history
- `draft` – Under development, not for production use

Deprecated ITIDs must include guidance on replacement ITIDs.

---

## Governance Responsibilities

ITID governance is the responsibility of:

- Security Operations leadership
- Threat Intelligence leadership (where applicable)
- Designated taxonomy owners

Analysts may propose new ITIDs, but creation and modification must follow governance review.

---

## Common Pitfalls

The following are explicitly discouraged:

- Creating ITIDs for one-off incidents
- Encoding tooling names in ITIDs
- Using severity as a classifier
- Mixing “what happened” with “who did it”
- Overloading ITIDs with response logic

ITIDs classify **events**, not conclusions.

---

## Guiding Statement

The ITID system exists to ensure that **incident classification is precise for analysts, stable for leadership, and durable over time**.

A well-governed ITID taxonomy enables learning, reporting, and strategic decision-making without sacrificing operational clarity.