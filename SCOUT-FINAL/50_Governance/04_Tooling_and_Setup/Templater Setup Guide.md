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

This document defines the **approved configuration, usage patterns, and safety rules** for using the Obsidian Templater plugin within SCOUT.

Its purpose is to ensure that:

- Templates execute predictably
- Canonical content is not corrupted
- Analysts can safely create entities and operational notes
- Automation supports analysts without introducing fragility

This guide is **normative**. Deviations should be intentional and documented.

---

## Scope

This guide applies to:

- All executable templates in `00_System/00_Templates`
- All Templater-based bootstrapping workflows (ITIDs, Incidents, Operations)
- All users authoring or modifying Templater scripts in SCOUT

It does **not** cover non-executable documentation or governance notes.

---

## Required Plugin Configuration

### Templater Plugin

The following configuration is required:

- **Plugin:** Templater (Obsidian community plugin)
- **Template folder location:**
    `00_System/00_Templates`
- **Trigger on new file creation:** Enabled
- **Timeout:** Default (do not reduce)
- **JavaScript enabled:** Required
    
Templates outside this folder are not considered executable.

---

## Template Types and Responsibilities

Templater usage in SCOUT is divided into two clear categories:

### 1. Bootstrap Templates

Bootstrap templates:

- Prompt the user for input
- Create new notes and folder structures
- Populate metadata programmatically
- Perform file system operations
    

Examples:

- ITID Bootstrap
- Incident Bootstrap

**Rules:**

- Bootstrap templates may contain `<%* ... %>` blocks
- Bootstrap templates may prompt the user
- Bootstrap templates may create or modify files
- Bootstrap templates must be treated as code

---

### 2. Canonical Entity Templates

Canonical templates:

- Define YAML frontmatter schemas
- Define body structure
- Derive values from filenames or metadata

Examples:

- ITID.md
- Incident.md
- Asset.md

**Rules:**

- Canonical templates **must not** contain `<%* ... %>` blocks
- Canonical templates must not prompt the user
- Canonical templates should be idempotent
- Inline `<% ... %>` expressions are allowed for derivation only

This separation is critical to system stability.

---

## Folder and File Safety Rules

### Templates Folder Safety

The following rules are absolute:

- No governance or reference documents belong in `00_System/00_Templates`
- Only executable templates should exist in this folder
- Template files must never be deleted or renamed by scripts
- Scripts must never operate on the templates folder itself

Violations of these rules risk system-wide breakage.

---

### Scratch Notes

When using **“Create new note from template”**, Obsidian creates a temporary “scratch” note (often named `Untitled.md`).

SCOUT bootstraps:

- May clean up scratch notes **only if explicitly intended**
- Must never assume the active file is safe to delete
- Must never delete notes in the templates folder

If cleanup is implemented, it must be:

- Deterministic
- Narrowly scoped
- Non-fatal on failure

---

## Naming and Path Assumptions

Templater scripts in SCOUT assume:

- Forward-slash (`/`) paths
- Vault-relative paths
- Stable folder names
- Predictable filename conventions

Hard-coded paths are acceptable **only** when governed and documented.

Dynamic path discovery is discouraged for critical workflows.

---

## Common Failure Modes (and How to Avoid Them)

### Recursive Template Execution

**Cause:**  
A bootstrap script creates a note using a template that itself executes prompts.

**Prevention:**

- Bootstrap templates prompt
- Canonical templates do not

Never mix responsibilities.

---

### Template Deletion or Corruption

**Cause:**  
Scripts operating on `activeFile` or `tp.file.path` without safety checks.

**Prevention:**

- Never delete files by “active” state alone
- Never modify or delete templates
- Always scope file operations explicitly

---

### Placeholder Not Replacing

**Cause:**  
Using non-Templater syntax (e.g., `{{field}}`) in templates.

**Prevention:**

- Use Templater expressions (`<% ... %>`)
- Derive from filename or frontmatter
- Avoid custom placeholder schemes

---

### ENOENT / File Not Found Errors

**Cause:**  
Operating on files that no longer exist or have moved.

**Prevention:**

- Re-resolve files by path before deletion
- Treat cleanup as best-effort
- Never let cleanup failures abort creation

---

## Recommended Development Practices

- Test templates in an isolated vault first
- Commit templates to version control
- Make one change at a time
- Avoid clever logic in favor of explicit logic
- Comment complex scripts

Templater scripts are **production code**, not macros.

---

## Change Management

Changes to executable templates should follow governance:

- Review by a designated owner
- Testing before deployment
- Documentation of behavioral changes
- Version control where possible

Unreviewed changes increase operational risk.

---

## Intended Audience

This guide is written for:

- Platform engineers
- Power users authoring templates
- SOC leads responsible for tooling reliability

Analysts should be able to use templates without understanding their internals.

---

## Guiding Statement

Templater exists to **reduce analyst effort**, not to introduce hidden complexity.

When in doubt:

- Prefer clarity over cleverness
- Prefer safety over convenience
- Prefer explicit structure over automation magic

A stable system is more valuable than a clever one.