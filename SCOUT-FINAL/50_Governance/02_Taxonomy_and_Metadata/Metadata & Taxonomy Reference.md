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

This document defines the **authoritative meaning, usage rules, and constraints** for metadata fields and taxonomic constructs used throughout SCOUT.

Its purpose is to ensure that:

- Metadata is applied consistently
- Taxonomy remains stable and understandable
- Fields mean the same thing across entities and time
- Automation, reporting, and analysis operate on reliable semantics

This document is a **reference**, not a tutorial.

---

## Scope

This reference applies to:

- All **entity templates** (ITIDs, Assets, Users, TTPs, Detections, etc.)
- All **operational templates** (Incidents, Investigations, Response Actions)
- Governance and knowledge documents (where applicable)

It does **not** define workflow steps or analyst procedures.

---

## Core Metadata Principles

All metadata in SCOUT adheres to the following principles:

### 1. Explicit Meaning

Every field must have:

- A single, clear definition
- One primary purpose
- Predictable usage

Fields must not rely on implicit or contextual interpretation.

---

### 2. Stability Over Time

Metadata definitions should change **rarely**.

If a field’s meaning must change significantly:

- Introduce a new field
- Deprecate the old field
- Document the change

Do not silently repurpose fields.

---

### 3. Separation of Concerns

Fields describe **one thing only**.

For example:

- Classification ≠ severity
- Attribution ≠ evidence
- Reporting ≠ analysis

Combining concerns in a single field is explicitly discouraged.

---

## Common Field Categories

### Identity Fields

Fields that uniquely identify an entity.

Examples:

- `itid_id`
- `incident_id`
- `campaign_id`
- `asset_id`

**Rules:**

- Must be stable
- Must not be reused
- Must not encode mutable information

---

### Classification Fields

Fields that describe _what something is_.

Examples:

- `itid_category`
- `entity_type`
- `asset_type`

**Rules:**

- Drawn from controlled vocabularies
- Independent of tooling
- Stable across incidents

---

### Relationship Fields

Fields that define explicit links between entities.

Examples:

- `related_itids`
- `associated_ttp`
- `related_assets`
- `related_incidents`

**Rules:**

- Prefer references over duplication
- Relationships should be meaningful, not exhaustive
- Directionality should be intentional

---

### Temporal Fields

Fields that capture time-related information.

Examples:

- `created`
- `updated`
- `first_seen`
- `last_seen`
- `detected_time`
- `closed_time`

**Rules:**

- Use ISO 8601 format where possible
- Clearly distinguish _event time_ from _documentation time_
- Avoid overloading time fields with interpretation

---

### Status & Lifecycle Fields

Fields that describe an entity’s lifecycle state.

Examples:

- `status`
- `lifecycle_state`
- `deprecated`

**Rules:**

- Status must reflect governance reality, not analyst opinion
- Deprecated entities remain valid for historical reference
- Status transitions should be deliberate and documented

---

### Reporting & Aggregation Fields

Fields designed for summarization and reporting.

Examples:

- `reporting_rollup`
- `severity_guidance`
- `priority_band`

**Rules:**

- These fields exist to support aggregation
- They must not be used for operational decision-making
- They should be defined once and reused consistently

---

## Controlled Vocabularies

Certain fields require controlled values to prevent drift.

Examples include:

- `status` (active, draft, deprecated)
- `confidence` (low, moderate, high)
- `severity_guidance` (informational, low, medium, high, critical)

Controlled vocabularies must be:

- Explicitly documented
- Reviewed periodically
- Updated through governance, not ad hoc usage

---

## Taxonomy Structure

Taxonomy in SCOUT is **intentional and hierarchical**, but not rigid.

### ITID Taxonomy

- Numeric ranges indicate conceptual groupings
- Parent ITIDs define categories
- Child ITIDs define specific manifestations

Hierarchy is used for **understanding and reporting**, not enforcement.

---

### Entity Taxonomy

Entities are grouped by **what they represent**, not how they are used.

Examples:

- Assets vs Users vs Detections
- Threat Actors vs Campaigns vs Malware

Do not create hybrid entities that blur these distinctions.

---

## Naming vs Metadata

Naming conventions and metadata serve different purposes:

- **Names** optimize for human readability
- **Metadata** optimizes for machine processing and consistency

Do not attempt to encode metadata semantics into filenames beyond identity.

---

## Deprecated Fields

Fields may be deprecated when they:

- Duplicate other fields
- Encode multiple concerns
- Are no longer required for analysis or reporting

Deprecated fields:

- Must remain readable
- Must not be reused
- Must be documented as deprecated

---

## Extensibility Rules

SCOUT is designed to evolve, but extensions must follow rules:

Before adding a new field:

1. Confirm no existing field serves the purpose
2. Define the field’s meaning precisely
3. Decide whether it requires a controlled vocabulary
4. Document it in this reference

Ad hoc field creation is discouraged.

---

## Governance and Ownership

Metadata and taxonomy governance is owned by:

- Security Operations leadership
- Threat Intelligence leadership (for CTI-related fields)
- Platform or Knowledge Architecture owners

Analysts may propose changes, but implementation requires governance approval.

---

## Guiding Statement

Metadata and taxonomy exist to ensure that **knowledge remains interpretable, automatable, and trustworthy over time**.

When in doubt:

- Favor clarity over cleverness
- Favor consistency over customization
- Favor durability over convenience