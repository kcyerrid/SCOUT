---
entity_type: sla
sla_id: SLA-00002
sla_title: Test SLA 2
sla_version: ""
sla_status: Draft
sla_type: Internal
sla_owner_primary: YOUR NAME
sla_owner_secondary: ""
sla_owning_team: ""
sla_stakeholders: []
sla_provider_org: ""
sla_provider_contact: ""
sla_provider_email: ""
sla_customer_org: ""
sla_customer_contact: ""
sla_customer_email: ""
sla_third_parties: []
sla_service_name: ""
sla_service_category: security
sla_service_description: ""
sla_in_scope: []
sla_out_of_scope: []
sla_coverage_model: 24x7
sla_timezone: America/New_York
sla_business_hours: ""
sla_service_locations: []
sla_supported_platforms: []
sla_dependencies: []
sla_effective_date: 2026-02-15
sla_expiration_date: 2026-02-2027
sla_renewal_terms: ""
sla_review_cadence: quarterly
sla_termination_notice_days: 30
sla_data_classification: internal
sla_regulated_data: []
sla_security_requirements: []
sla_compliance_frameworks: []
sla_audit_rights: ""
sla_breach_notify_window_hours: ""
sla_breach_notify_method: ""
sla_access_controls: []
sla_logging_monitoring: []
sla_log_retention_days: ""
sla_ticket_retention_days: ""
sla_dpa_required: false
sla_dpa_location: ""
sla_availability_target_percent: ""
sla_availability_window: monthly
sla_availability_method: ""
sla_availability_exclusions: []
sla_perf_metrics: []
sla_perf_targets: []
sla_perf_windows: []
sla_perf_methods: []
sla_perf_exclusions: []
sla_support_channels: []
sla_ticketing_system: ""
sla_languages_supported: []
sla_rto: ""
sla_rpo: ""
sla_sev1_definition: ""
sla_sev2_definition: ""
sla_sev3_definition: ""
sla_sev4_definition: ""
sla_severity_reference_note: ""
sla_sev1_acknowledge: ""
sla_sev1_engage: ""
sla_sev1_restore: ""
sla_sev2_acknowledge: ""
sla_sev2_engage: ""
sla_sev2_restore: ""
sla_sev3_acknowledge: ""
sla_sev3_engage: ""
sla_sev3_restore: ""
sla_sev4_acknowledge: ""
sla_sev4_engage: ""
sla_sev4_restore: ""
sla_escalation_tiers: []
sla_escalation_contacts: []
sla_exec_notification_required: false
sla_exec_notification_criteria: ""
sla_status_update_cadence: ""
sla_pir_required: true
sla_pir_due_within_days: 5
sla_maintenance_windows: []
sla_change_notice_period_days: 7
sla_emergency_change_process: ""
sla_customer_approval_required: false
sla_reporting_cadence: monthly
sla_standard_reports: []
sla_dashboards: []
sla_kpis: []
sla_data_sources: []
sla_pricing_model: fixed_fee
sla_service_credits_eligible: false
sla_service_credits_terms: ""
sla_penalties: ""
sla_invoicing_terms: ""
sla_known_risks: []
sla_assumptions: []
sla_exceptions: []
sla_risk_acceptance_required: false
sla_risk_acceptance_authority: ""
sla_risk_acceptance_date: ""
sla_master_agreement_location: ""
sla_exhibits_appendices: []
sla_runbooks: []
sla_playbooks: []
sla_kb_links: []
related_vendors: []
related_services: []
related_itids: []
related_incidents: []
related_assets: []
related_controls: []
tags: ""
tlp_classification: TLP:CLEAR
created: 2026-02-15 14:59:32
updated: 2026-02-15 14:59:45
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

# Service Level Agreement (SLA): Test SLA 2

## Overview
- **SLA ID:** SLA-00002
- **Type / Status:** Internal / Draft
- **Version:** {{sla_version}}
- **Effective → Expiration:** {{sla_effective_date}} → {{sla_expiration_date}}
- **Owner / Team:** YOUR NAME / 

## Parties
- **Provider:** {{sla_provider_org}} (Contact: )
- **Customer:** {{sla_customer_org}} (Contact: )
- **Third Parties:** {{sla_third_parties}}

## Scope
### Service Description
{{sla_service_description}}

### In Scope
{{sla_in_scope}}

### Out of Scope
{{sla_out_of_scope}}

### Coverage
- **Coverage Model:** {{sla_coverage_model}}
- **Timezone:** {{sla_timezone}}
- **Business Hours:** {{sla_business_hours}}

### Dependencies
{{sla_dependencies}}

## Service Level Objectives (SLOs)
### Availability
- **Target:** {{sla_availability_target_percent}}%
- **Window:** {{sla_availability_window}}
- **Method:** {{sla_availability_method}}

**Exclusions**
{{sla_availability_exclusions}}

### Performance
> This template models performance SLOs using aligned arrays:
> `sla_perf_metrics[n]` maps to `sla_perf_targets[n]`, `sla_perf_windows[n]`, etc.

{{sla_perf_metrics}}
{{sla_perf_targets}}
{{sla_perf_windows}}
{{sla_perf_methods}}
{{sla_perf_exclusions}}

### Support Model
- **Channels:** {{sla_support_channels}}
- **Ticketing:** {{sla_ticketing_system}}

### RTO / RPO
- **RTO:** {{sla_rto}}
- **RPO:** {{sla_rpo}}

## Incident Management
### Severity Definitions
- **Sev1:** {{sla_sev1_definition}}
- **Sev2:** {{sla_sev2_definition}}
- **Sev3:** {{sla_sev3_definition}}
- **Sev4:** {{sla_sev4_definition}}
- **Reference:** {{sla_severity_reference_note}}

### Response Targets
| Severity | Acknowledge | Engage | Restore/Resolve |
|---|---:|---:|---:|
| Sev1 | {{sla_sev1_acknowledge}} | {{sla_sev1_engage}} | {{sla_sev1_restore}} |
| Sev2 | {{sla_sev2_acknowledge}} | {{sla_sev2_engage}} | {{sla_sev2_restore}} |
| Sev3 | {{sla_sev3_acknowledge}} | {{sla_sev3_engage}} | {{sla_sev3_restore}} |
| Sev4 | {{sla_sev4_acknowledge}} | {{sla_sev4_engage}} | {{sla_sev4_restore}} |

### Escalation & Communications
- **Escalation Tiers:** {{sla_escalation_tiers}}
- **Escalation Contacts:** {{sla_escalation_contacts}}
- **Executive Notification:** {{sla_exec_notification_required}}
- **Executive Criteria:** {{sla_exec_notification_criteria}}
- **Status Update Cadence:** {{sla_status_update_cadence}}
- **PIR Required / Due:** {{sla_pir_required}} / {{sla_pir_due_within_days}} days

## Change Management
- **Maintenance Windows:** {{sla_maintenance_windows}}
- **Notice Period:** {{sla_change_notice_period_days}} days
- **Emergency Process:** {{sla_emergency_change_process}}
- **Customer Approval Required:** {{sla_customer_approval_required}}

## Metrics & Reporting
- **Cadence:** {{sla_reporting_cadence}}
- **Standard Reports:** {{sla_standard_reports}}
- **KPIs:** {{sla_kpis}}
- **Dashboards:** {{sla_dashboards}}

## Security & Compliance
- **Classification:** {{sla_data_classification}}
- **Regulated Data:** {{sla_regulated_data}}
- **Frameworks:** {{sla_compliance_frameworks}}
- **Breach Notification (hrs):** {{sla_breach_notify_window_hours}}

## Financials
- **Pricing Model:** {{sla_pricing_model}}
- **Service Credits Eligible:** {{sla_service_credits_eligible}}
- **Service Credits Terms:** {{sla_service_credits_terms}}

## Risks, Assumptions, Exceptions
### Known Risks
{{sla_known_risks}}

### Assumptions
{{sla_assumptions}}

### Exceptions
{{sla_exceptions}}

## Documentation & References
- **Master Agreement / MSA:** {{sla_master_agreement_location}}
- **Exhibits / Appendices:** {{sla_exhibits_appendices}}
- **Runbooks:** {{sla_runbooks}}
- **Playbooks:** {{sla_playbooks}}
- **Knowledge Base:** {{sla_kb_links}}

## Relationships
- **Related Vendors:** {{related_vendors}}
- **Related Services:** {{related_services}}
- **Related ITIDs:** {{related_itids}}
- **Related Incidents:** {{related_incidents}}
- **Related Assets:** {{related_assets}}
- **Related Controls:** {{related_controls}}

---
## Activity Log
- **Created:** 2026-02-15 14:59:32
- **Updated:** 2026-02-15 14:59:45

## Notes
-
