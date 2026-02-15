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

This document defines the **authoritative naming standards** for all notes, entities, folders, and identifiers within SCOUT.

Consistent naming is essential to:

- Maintain navigability at scale
    
- Prevent ambiguity and duplication
    
- Support automation and templating
    
- Preserve institutional knowledge over time
    

Naming conventions in SCOUT are **governance rules**, not stylistic preferences.

---

## Scope

This reference applies to:

- Entity notes (ITIDs, Assets, Users, TTPs, Detections, etc.)
    
- Operational notes (Incidents, Investigations, Timelines, Response Actions)
    
- Governance and knowledge documents
    
- Folder structures
    
- Identifiers and codes embedded in filenames
    

It does **not** govern prose style inside note bodies.

---

## Core Naming Principles

All naming within SCOUT adheres to the following principles:

### 1. Predictability

Given a name, an analyst should be able to infer:

- What the note represents
    
- Where it belongs in the vault
    
- How it relates to other notes
    

Surprises are a failure mode.

---

### 2. Stability

Names must remain valid over time.

Avoid:

- Tool-specific references
    
- Temporary conditions
    
- Analyst-specific shorthand
    
- Incident-specific details in entity names
    

Names should survive tooling changes and staff turnover.

---

### 3. Human Readability First

Names are optimized for **human scanning**, not machine compression.

Abbreviations are acceptable only when:

- They are widely understood
    
- They are defined elsewhere
    
- They do not introduce ambiguity
    

---

### 4. One Concept per Name

Each name should represent **one thing only**.

Avoid compound or overloaded names that merge:

- Classification + severity
    
- Entity + outcome
    
- Tool + behavior
    

---

## File Naming Standards

### General Format

`<Identifier> - <Human Readable Name>.md`

Examples:

`ITID`-11100 - Password Spray.md INC-2025-0003.md TA-APT29 - Cozy Bear.md`

The delimiter `-` (space, dash, space) is mandatory.

---

### Identifier Rules

Identifiers must:

- Be unique
    
- Be stable
    
- Never be reused
    
- Never encode mutable attributes (severity, date, status)
    

Identifiers belong **at the beginning** of the filename.

---

## ITID Naming

### Format

`<ITID_ID> - <ITID_Name>.md`

Example:

`ITID-11300 - MFA Fatigue.md`

### Rules

- ITID names describe _what happened_, not _how it was detected_
    
- Avoid vendor or tool names
    
- Avoid actor attribution
    
- Avoid response terminology
    

Good:

- Password Spray
    
- Token Abuse
    
- Impossible Travel
    

Bad:

- Azure AD Password Spray
    
- MFA Fatigue – Blocked
    
- APT Password Spray
    

---

## Incident Naming

### Format

`INC-YYYY-NNNN.md`

Example:

`INC-2025-0007.md`

### Rules

- Incidents do not include descriptive names in filenames
    
- Context belongs in metadata and body content
    
- Stability and sortability are the priority
    

---

## Investigation, Timeline, and Response Artifacts

### Investigation

`INV-YYYY-NNNN.md`

### Timeline

`TL-YYYY-NNNN.md`

### Response Actions

`RA-<IncidentID>-<Short Descriptor>.md`

Example:

`RA-INC-2025-0007-Disable Account.md`

Descriptors should be short and action-oriented.

---

## Asset Naming

Assets should be named according to **organizationally meaningful identifiers**, not discovery artifacts.

Examples:

- Hostnames
    
- Application names
    
- Cloud resource identifiers
    

Avoid:

- IP-only names (unless unavoidable)
    
- Temporary discovery labels
    
- Tool-generated IDs without context
    

---

## Folder Naming

### Numeric Prefixing

Folders use **two-digit numeric prefixes** to enforce sort order:

`01_Entities 02_Operations 03_Detections`

Rules:

- Numbers indicate conceptual order, not importance
    
- Gaps are intentional and acceptable
    
- Renumbering is discouraged once in use
    

---

### Folder Name Format

`NN_Descriptive_Name`

Rules:

- Use underscores, not spaces
    
- Capitalize each word
    
- Avoid abbreviations unless universally understood
    

---

## Case, Spacing, and Characters

### Case

- Title Case for names
    
- Uppercase for identifiers
    
- Lowercase for YAML keys
    

### Spacing

- Use spaces in filenames
    
- Use underscores in folders and YAML keys
    

### Special Characters

Avoid:

- `/ \ : * ? " < > |`
    

These are invalid or problematic across platforms.

---

## Naming vs Metadata Responsibilities

Naming and metadata serve different roles:

- **Names** identify and orient humans
    
- **Metadata** drives classification, filtering, and automation
    

Do not attempt to encode:

- Severity
    
- Priority
    
- Status
    
- Attribution
    
- Outcome
    

Into names.

That information belongs in metadata.

---

## Renaming Rules

Renaming governed entities is **strongly discouraged**.

If renaming is required:

- Document the rationale
    
- Update all references
    
- Preserve historical context
    

Prefer creating a **new entity** over renaming an existing one.

---

## Common Anti-Patterns

The following are explicitly discouraged:

- Encoding dates in entity names
    
- Encoding severity or outcome in names
    
- Tool-specific prefixes
    
- Analyst initials
    
- “Final”, “New”, “v2” naming
    

These patterns degrade system integrity over time.

---

## Governance and Enforcement

Naming standards are governed by:

- Security Operations leadership
    
- Threat Intelligence leadership
    
- Platform owners
    

Analysts are expected to follow conventions.  
Templates exist to make compliance easy and deviation rare.

---

## Guiding Statement

Naming conventions exist to ensure that **clarity scales with complexity**.

A well-named system reduces friction, enables automation, and preserves meaning long after individual analysts or tools change.