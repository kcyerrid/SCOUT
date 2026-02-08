# SCOUT Comprehensive Test Plan

## Scope and environment
- Scope: full app sweep across Launcher, intake flows, RSS, reports, PPTX, setup/config, and state persistence.
- Environment: production-like vault and data; use read-only paths where applicable.

## Flow-to-code coverage map
## Launcher and routing
- Launcher cards, sections, dispatch: `SCOUT_Launcher.py` (`LauncherApp`, `_dispatch`, card builder)
- Command palette/search: `SCOUT_Launcher.py` (search handlers, recent tracking)
- State persistence: `SCOUT_Launcher.py` (`load_state`, `save_state`)

## Intake workflows
- Incident intake: `SCOUT_Launcher.py` (`IncidentIntakeWindow`, `_collect`, `_save_draft`)
- Meeting intake: `SCOUT_Launcher.py` (`MeetingIntakeWindow`)
- Playbook intake: `SCOUT_Launcher.py` (`PlaybookIntakeWindow`)
- Procedure intake: `SCOUT_Launcher.py` (`ProcedureIntakeWindow`)
- ITID intake: `SCOUT_Launcher.py` (`ITIDIntakeWindow`)
- SLA intake: `SCOUT_Launcher.py` (`SLAIntakeWindow`)
- FAQ intake: `SCOUT_Launcher.py` (`FAQIntakeWindow`)
- How-To intake: `SCOUT_Launcher.py` (`HowToIntakeWindow`)
- Template merge/frontmatter: `SCOUT_Launcher.py` (template merge helpers)

## RSS pipeline
- Collect/ingest: `scout_rss.py` (`collect`, DB helpers)
- Review/triage UI: `SCOUT_Launcher.py` (`_open_rss_review`, `_rss_apply_filters`)
- Flag/read/report queue: `SCOUT_Launcher.py` (`_rss_toggle_flag_selected`, `_rss_report_selected`, `_rss_generate_report`)
- Report/weekly rollup outputs: `SCOUT_Launcher.py` (`_rss_write_report_note`, `_rss_write_weekly_rollup_note`)
- Keywords/watchlists: `SCOUT_Launcher.py` (`_build_rss_keywords_tab`, watchlist parsing)

## Reports and PPTX
- Reports catalog: `SCOUT_Launcher.py` (`_open_reports_catalog`)
- IOC enrichment report: `SCOUT_Launcher.py` (`_open_ioc_enrich`, `_write_ioc_enrichment_report`)
- PPTX export: `SCOUT_Launcher.py` (`_pptx_*` helpers)

## Setup/config
- Setup wizard: `SCOUT_SetupWizard.py`
- Config validation and defaults: `config.json`, `SCOUT_Launcher.py` config utilities
- Path token resolution: `SCOUT_Launcher.py` (`resolve_path`, token expansion helpers)

## State/drafts
- Draft storage: `Code/*_draft.json`, `SCOUT_Launcher.py` draft load/save helpers
- RSS state persistence: `SCOUT_Launcher.py` (`rss_article_state`, `rss_report_queue`)

---

## Detailed test cases
### 1) Launcher and navigation
- Launch app and verify cards render for all sections.
- Validate each card dispatch opens the expected window.
- Use command palette search; verify results and recent items.
- Close and relaunch; verify recents persist.

Expected: No exceptions; cards open correctly; recents and badges persist after restart.

### 2) Intake workflows
For each intake window (Incident, Meeting, Playbook, Procedure, ITID, SLA, FAQ, How-To):
- Open intake window and verify default values.
- Save draft, close window, reopen; draft values persist.
- Clear draft; verify fields reset.
- Submit with required fields populated; verify note creation path and content.
- Validate frontmatter fields, timestamps, tags, and template sections.

Expected: Draft persistence works; notes created in expected folders with correct frontmatter and body.

### 3) RSS pipeline
- Run RSS collection; verify count increments and last-run status.
- Review tab: filter by New/Flagged/Reported and search.
- Flag and mark read; verify status tags update.
- Multi-select in each view (New/Flagged/Reported) and generate report.
- Generate weekly rollup and verify date range.

Expected: Filters and status tags work; reports include all selected items; rollup contains last 7 days.

### 4) Reports and Perspectives
- Open Reports Catalog and run each report action.
- Verify output path, filename, and required sections.
- IOC enrichment report: test with valid IOCs and with empty input.

Expected: Report files created; errors surfaced clearly when invalid inputs provided.

### 5) PPTX export
- Export from a known Obsidian note.
- Validate slide count, titles, and key fields.
- Confirm template selection and image embedding (if any).

Expected: PPTX file generated without errors; slide content matches source note.

### 6) Setup/config validation
- Run setup wizard; verify required paths and token resolution.
- Check config defaults for missing values.
- Validate malformed paths are caught with clear errors.

Expected: Wizard prevents invalid config; tokens resolve to actual paths.

### 7) State persistence
- Change state (RSS flags, notes, tags, recents).
- Restart app and verify persistence.

Expected: State is retained across restarts.

---

## Bug triage + repair checklist
1. Capture reproduction steps with view mode, selection count, status flags, and any popups.
2. Identify affected area (Launcher/RSS/Setup/PPTX/Intake).
3. Locate relevant function(s) and state dependencies.
4. Apply minimal fix; add guard rails for empty inputs or missing paths.
5. Retest the exact scenario plus adjacent cases (multi-select, different filters).

---

## Optional automation targets
- RSS scoring, watchlist parsing, and report generation helpers.
- Template merge/frontmatter utilities.
- Path resolution/token expansion helpers.
- ID normalization functions (incident, threat actor).
