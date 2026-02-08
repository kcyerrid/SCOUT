# SCOUT Regression Suite (High-Risk Paths)

## RSS
- Multi-select report generation in New/Flagged/Reported views.
- Report queue creation, stale cleanup, and report write.
- Weekly rollup creation for last 7 days.
- Watchlist keyword parsing and auto-flagging.

## Templates and frontmatter
- Template merge preserves required keys and YAML format.
- Frontmatter updates with missing YAML create a valid header.
- ID normalization (incident, threat actor).

## Paths and config
- Token expansion resolves `{APP_DIR}`, `{VAULT_ROOT}`, and other tokens.
- Invalid paths are surfaced with clear errors and no crash.

## Intake windows
- Draft save/load/clear across Incident, Meeting, Project, Playbook, Procedure, ITID, SLA.
- Required field validation blocks submit and shows message.

## Reports and exports
- IOC enrichment report creation and file naming.
- Project Status Rollup report generation.
- PPTX export for a known note; slides render with correct titles.

## State persistence
- RSS flags, notes/tags, and recents persist after restart.
