---
entity_type: "sla"

# Identity
sla_id: "SLA-00001"
sla_title: "Test SLA"
sla_version: ""                        # e.g., 1.0
sla_status: "Draft"
sla_type: "Internal"

# Ownership & Stakeholders
sla_owner_primary: "YOUR NAME"
sla_owner_secondary: ""
sla_owning_team: ""
sla_stakeholders: []                   # e.g., ["IT Ops","GRC","Vendor Mgmt"]

# Parties
sla_provider_org: ""
sla_provider_contact: ""
sla_provider_email: ""
sla_customer_org: ""
sla_customer_contact: ""
sla_customer_email: ""
sla_third_parties: []                  # e.g., ["MSSP Subcontractor Y"]

# Scope
sla_service_name: ""                   # e.g., "Managed Detection and Response"
sla_service_category: "security"       # security | it_operations | identity | network | cloud | application | business_services | other
sla_service_description: ""            # 1-paragraph description

sla_in_scope: []                       # strings
sla_out_of_scope: []                   # strings

sla_coverage_model: "24x7"             # 24x7 | business_hours | follow_the_sun | on_call | other
sla_timezone: "America/New_York"
sla_business_hours: ""                 # if applicable, e.g., "Mon–Fri 08:00–18:00"
sla_service_locations: []              # e.g., ["NA","EMEA"]
sla_supported_platforms: []            # e.g., ["Windows","M365","AWS","Okta"]
sla_dependencies: []                   # e.g., ["SIEM","EDR","Ticketing"]

# Term & Governance
sla_effective_date: ""                 # YYYY-MM-DD
sla_expiration_date: ""                # YYYY-MM-DD
sla_renewal_terms: ""                  # e.g., "Auto-renews annually..."
sla_review_cadence: "quarterly"        # quarterly | semi_annual | annual | ad_hoc
sla_termination_notice_days: 30

# Security & Compliance
sla_data_classification: "internal"    # public | internal | confidential | restricted
sla_regulated_data: []                 # e.g., ["PCI","PHI","PII"]
sla_security_requirements: []          # e.g., ["MFA required","Encryption at rest"]
sla_compliance_frameworks: []          # e.g., ["SOC 2","ISO 27001","NIST 800-53"]
sla_audit_rights: ""                   # summary text
sla_breach_notify_window_hours: ""     # e.g., "24"
sla_breach_notify_method: ""           # e.g., "Email + phone escalation"
sla_access_controls: []                # e.g., ["Least privilege","JIT access","PAM enforced"]
sla_logging_monitoring: []             # e.g., ["SIEM ingest","EDR telemetry retention 180 days"]
sla_log_retention_days: ""             # string to allow "180" or "180 days"
sla_ticket_retention_days: ""
sla_dpa_required: false
sla_dpa_location: ""                   # link/path to DPA note/file

# SLOs / Service Levels
sla_availability_target_percent: ""    # e.g., "99.9"
sla_availability_window: "monthly"     # monthly | quarterly | annual
sla_availability_method: ""            # how uptime is measured
sla_availability_exclusions: []        # planned maintenance, force majeure, etc.

# Performance (flat, but extensible via parallel arrays)
sla_perf_metrics: []                   # e.g., ["Alert ingestion latency","Report delivery time"]
sla_perf_targets: []                   # e.g., ["P95 < 60s","<= 5 business days"]
sla_perf_windows: []                   # e.g., ["monthly","monthly"]
sla_perf_methods: []                   # e.g., ["SIEM timestamp delta","Delivery timestamp"]
sla_perf_exclusions: []                # e.g., ["Customer-side outage","Customer approval delay"]

# Support Model
sla_support_channels: []               # e.g., ["Email","Portal","Phone","Slack"]
sla_ticketing_system: ""               # e.g., "ServiceNow"
sla_languages_supported: []            # optional

# Resilience
sla_rto: ""                            # e.g., "4h"
sla_rpo: ""                            # e.g., "15m"

# Incident Management (Severity Model)
sla_sev1_definition: ""
sla_sev2_definition: ""
sla_sev3_definition: ""
sla_sev4_definition: ""
sla_severity_reference_note: ""        # link/path to ITID severity model, if applicable

# Response Targets
sla_sev1_acknowledge: ""               # e.g., "15m"
sla_sev1_engage: ""                    # e.g., "30m"
sla_sev1_restore: ""                   # e.g., "4h"
sla_sev2_acknowledge: ""
sla_sev2_engage: ""
sla_sev2_restore: ""
sla_sev3_acknowledge: ""
sla_sev3_engage: ""
sla_sev3_restore: ""
sla_sev4_acknowledge: ""
sla_sev4_engage: ""
sla_sev4_restore: ""

# Escalation & Communications
sla_escalation_tiers: []               # e.g., ["L1","L2","L3","On-call"]
sla_escalation_contacts: []            # strings, or keep as "Name (Role) - Method"
sla_exec_notification_required: false
sla_exec_notification_criteria: ""     # e.g., "Data exfil suspected; Sev1 > 2h"
sla_status_update_cadence: ""          # e.g., "Every 30 minutes for Sev1"
sla_pir_required: true
sla_pir_due_within_days: 5

# Change Management
sla_maintenance_windows: []            # e.g., ["Sat 01:00–03:00 ET"]
sla_change_notice_period_days: 7
sla_emergency_change_process: ""
sla_customer_approval_required: false

# Metrics & Reporting
sla_reporting_cadence: "monthly"       # weekly | monthly | quarterly | on_demand
sla_standard_reports: []               # e.g., ["Availability","MTTA/MTTR","Case volume by severity"]
sla_dashboards: []                     # links/paths
sla_kpis: []                           # e.g., ["MTTA","MTTR","False positive rate","Backlog"]
sla_data_sources: []                   # e.g., ["SIEM","Ticketing","Uptime monitor"]

# Financials
sla_pricing_model: "fixed_fee"         # fixed_fee | usage_based | per_user | per_device | other
sla_service_credits_eligible: false
sla_service_credits_terms: ""
sla_penalties: ""
sla_invoicing_terms: ""                # e.g., "Net 30"

# Risk & Exceptions
sla_known_risks: []
sla_assumptions: []
sla_exceptions: []
sla_risk_acceptance_required: false
sla_risk_acceptance_authority: ""
sla_risk_acceptance_date: ""           # YYYY-MM-DD

# Documentation
sla_master_agreement_location: ""      # link/path to contract or MSA
sla_exhibits_appendices: []            # links/paths
sla_runbooks: []                       # links/paths
sla_playbooks: []                      # links/paths
sla_kb_links: []                       # links/paths

# Relationships (SCOUT linking)
related_vendors: []
related_services: []
related_itids: []
related_incidents: []
related_assets: []
related_controls: []

# Admin
tags: ""
tlp_classification: "TLP:CLEAR"
created: "2026-02-15 14:54:21"
updated: "2026-02-15 14:55:17"
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Service Level Agreement (SLA): {{title}}

## Overview
- **SLA ID:** <% tp.frontmatter.sla_id %>
- **Type / Status:** <% tp.frontmatter.sla_type %> / <% tp.frontmatter.sla_status %>
- **Version:** <% tp.frontmatter.sla_version %>
- **Effective → Expiration:** <% tp.frontmatter.sla_effective_date %> → <% tp.frontmatter.sla_expiration_date %>
- **Owner / Team:** <% tp.frontmatter.sla_owner_primary %> / <% tp.frontmatter.sla_owning_team %>

## Parties
- **Provider:** <% tp.frontmatter.sla_provider_org %> (Contact: <% tp.frontmatter.sla_provider_contact %>)
- **Customer:** <% tp.frontmatter.sla_customer_org %> (Contact: <% tp.frontmatter.sla_customer_contact %>)
- **Third Parties:** <% tp.frontmatter.sla_third_parties %>

## Scope
### Service Description
<% tp.frontmatter.sla_service_description %>

### In Scope
<%*
const inScope = tp.frontmatter.sla_in_scope || [];
tR += inScope.length ? inScope.map(x => `- ${x}`).join("\n") : "- (not specified)";
%>

### Out of Scope
<%*
const outScope = tp.frontmatter.sla_out_of_scope || [];
tR += outScope.length ? outScope.map(x => `- ${x}`).join("\n") : "- (not specified)";
%>

### Coverage
- **Coverage Model:** <% tp.frontmatter.sla_coverage_model %>
- **Timezone:** <% tp.frontmatter.sla_timezone %>
- **Business Hours:** <% tp.frontmatter.sla_business_hours %>

### Dependencies
<%*
const deps = tp.frontmatter.sla_dependencies || [];
tR += deps.length ? deps.map(x => `- ${x}`).join("\n") : "- (not specified)";
%>

## Service Level Objectives (SLOs)
### Availability
- **Target:** <% tp.frontmatter.sla_availability_target_percent %>%
- **Window:** <% tp.frontmatter.sla_availability_window %>
- **Method:** <% tp.frontmatter.sla_availability_method %>

**Exclusions**
<%*
const ex = tp.frontmatter.sla_availability_exclusions || [];
tR += ex.length ? ex.map(x => `- ${x}`).join("\n") : "- (not specified)";
%>

### Performance
> This template models performance SLOs using aligned arrays:
> `sla_perf_metrics[n]` maps to `sla_perf_targets[n]`, `sla_perf_windows[n]`, etc.

<%*
const m = tp.frontmatter.sla_perf_metrics || [];
const t = tp.frontmatter.sla_perf_targets || [];
const w = tp.frontmatter.sla_perf_windows || [];
const md = tp.frontmatter.sla_perf_methods || [];
const ex2 = tp.frontmatter.sla_perf_exclusions || [];

if (!m.length) {
  tR += "- (not specified)\n";
} else {
  for (let i = 0; i < m.length; i++) {
    tR += `- **${m[i]}**\n`;
    tR += `  - Target: ${t[i] || ""}\n`;
    tR += `  - Window: ${w[i] || ""}\n`;
    tR += `  - Method: ${md[i] || ""}\n`;
    if (ex2[i]) tR += `  - Exclusions: ${ex2[i]}\n`;
  }
}
%>

### Support Model
- **Channels:** <% tp.frontmatter.sla_support_channels %>
- **Ticketing:** <% tp.frontmatter.sla_ticketing_system %>

### RTO / RPO
- **RTO:** <% tp.frontmatter.sla_rto %>
- **RPO:** <% tp.frontmatter.sla_rpo %>

## Incident Management
### Severity Definitions
- **Sev1:** <% tp.frontmatter.sla_sev1_definition %>
- **Sev2:** <% tp.frontmatter.sla_sev2_definition %>
- **Sev3:** <% tp.frontmatter.sla_sev3_definition %>
- **Sev4:** <% tp.frontmatter.sla_sev4_definition %>
- **Reference:** <% tp.frontmatter.sla_severity_reference_note %>

### Response Targets
| Severity | Acknowledge | Engage | Restore/Resolve |
|---|---:|---:|---:|
| Sev1 | <% tp.frontmatter.sla_sev1_acknowledge %> | <% tp.frontmatter.sla_sev1_engage %> | <% tp.frontmatter.sla_sev1_restore %> |
| Sev2 | <% tp.frontmatter.sla_sev2_acknowledge %> | <% tp.frontmatter.sla_sev2_engage %> | <% tp.frontmatter.sla_sev2_restore %> |
| Sev3 | <% tp.frontmatter.sla_sev3_acknowledge %> | <% tp.frontmatter.sla_sev3_engage %> | <% tp.frontmatter.sla_sev3_restore %> |
| Sev4 | <% tp.frontmatter.sla_sev4_acknowledge %> | <% tp.frontmatter.sla_sev4_engage %> | <% tp.frontmatter.sla_sev4_restore %> |

### Escalation & Communications
- **Escalation Tiers:** <% tp.frontmatter.sla_escalation_tiers %>
- **Escalation Contacts:** <% tp.frontmatter.sla_escalation_contacts %>
- **Executive Notification:** <% tp.frontmatter.sla_exec_notification_required %>
- **Executive Criteria:** <% tp.frontmatter.sla_exec_notification_criteria %>
- **Status Update Cadence:** <% tp.frontmatter.sla_status_update_cadence %>
- **PIR Required / Due:** <% tp.frontmatter.sla_pir_required %> / <% tp.frontmatter.sla_pir_due_within_days %> days

## Change Management
- **Maintenance Windows:** <% tp.frontmatter.sla_maintenance_windows %>
- **Notice Period:** <% tp.frontmatter.sla_change_notice_period_days %> days
- **Emergency Process:** <% tp.frontmatter.sla_emergency_change_process %>
- **Customer Approval Required:** <% tp.frontmatter.sla_customer_approval_required %>

## Metrics & Reporting
- **Cadence:** <% tp.frontmatter.sla_reporting_cadence %>
- **Standard Reports:** <% tp.frontmatter.sla_standard_reports %>
- **KPIs:** <% tp.frontmatter.sla_kpis %>
- **Dashboards:** <% tp.frontmatter.sla_dashboards %>

## Security & Compliance
- **Classification:** <% tp.frontmatter.sla_data_classification %>
- **Regulated Data:** <% tp.frontmatter.sla_regulated_data %>
- **Frameworks:** <% tp.frontmatter.sla_compliance_frameworks %>
- **Breach Notification (hrs):** <% tp.frontmatter.sla_breach_notify_window_hours %>

## Financials
- **Pricing Model:** <% tp.frontmatter.sla_pricing_model %>
- **Service Credits Eligible:** <% tp.frontmatter.sla_service_credits_eligible %>
- **Service Credits Terms:** <% tp.frontmatter.sla_service_credits_terms %>

## Risks, Assumptions, Exceptions
### Known Risks
<%*
const risks = tp.frontmatter.sla_known_risks || [];
tR += risks.length ? risks.map(x => `- ${x}`).join("\n") : "- (not specified)";
%>

### Assumptions
<%*
const asm = tp.frontmatter.sla_assumptions || [];
tR += asm.length ? asm.map(x => `- ${x}`).join("\n") : "- (not specified)";
%>

### Exceptions
<%*
const exc = tp.frontmatter.sla_exceptions || [];
tR += exc.length ? exc.map(x => `- ${x}`).join("\n") : "- (none)";
%>

## Documentation & References
- **Master Agreement / MSA:** <% tp.frontmatter.sla_master_agreement_location %>
- **Exhibits / Appendices:** <% tp.frontmatter.sla_exhibits_appendices %>
- **Runbooks:** <% tp.frontmatter.sla_runbooks %>
- **Playbooks:** <% tp.frontmatter.sla_playbooks %>
- **Knowledge Base:** <% tp.frontmatter.sla_kb_links %>

## Relationships
- **Related Vendors:** <% tp.frontmatter.related_vendors %>
- **Related Services:** <% tp.frontmatter.related_services %>
- **Related ITIDs:** <% tp.frontmatter.related_itids %>
- **Related Incidents:** <% tp.frontmatter.related_incidents %>
- **Related Assets:** <% tp.frontmatter.related_assets %>
- **Related Controls:** <% tp.frontmatter.related_controls %>

---
## Activity Log
- **Created:** <% tp.frontmatter.created %>
- **Updated:** <% tp.frontmatter.updated %>

## Notes
-
