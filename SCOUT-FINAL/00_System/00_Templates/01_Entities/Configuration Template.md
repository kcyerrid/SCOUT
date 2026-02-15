---
entity_type: configuration
config_id: ""                     # unique SCOUT ID, e.g. CFG-Sentinel-UF-001
config_name: ""                   # descriptive name

config_type:     
- edr_policy
- siem_rule
- iam_role
- firewall_rule
- mfa_policy
- casb_control
- email_filter
- network_acl
- cloud_config
- logging_policy
- other
environment:
- production
- staging
- development
- test
- other

platform: 
- sentinel
- crowdstrike
- microsoft_365
- azure
- aws
- gcp
- okta
- cisco
- palo_alto
- other
product_area:
- identity
- edr
- siem
- email
- network
- cloud
- endpoint
- monitoring
- access_control
- other

description: ""                   # what this configuration does

intended_purpose: 
- detection
- prevention
- hardening
- visibility
- restriction
- compliance
- other
security_objective: 
- confidentiality
- integrity
- availability
- least_privilege
- segmentation

status: 
- active
- disabled
- draft
- deprecated
change_control_status: 
- approved
- pending
- rejected
- emergency
- untracked
last_change_date: ""
last_change_by: ""
change_ticket_reference: ""       # link to internal change request or CAB entry
version: 1

# Configuration Details
parameters: []                    # key-value pairs of settings
default_values: []                # vendor defaults (optional)
current_values: []                # current active settings (optional)
config_snippets: ""               # YAML/JSON/policy snippet

# Impact Analysis
security_impact: 
- 3-low
- 2-medium
- 1-high
operational_risk: ""              # notes on risk, blast radius, dependency issues
coverage_provided: []             # TTPs or attack classes this config mitigates
coverage_gaps: []                 # known limitations

# Detection & Response Relationships
related_detections: []            # detection entities depending on this config
related_tactics: []               # ATT&CK tactics addressed
related_techniques: []            # ATT&CK techniques mitigated or detected
related_assets: []                # systems governed by this configuration
related_incidents: []             # incidents influenced by misconfiguration or fixes

# Validation & Review
validation_status: 
- untested
- tested
- validated
- recurring
testing_notes: ""                # results or considerations
review_frequency_days: 180
next_review_date: ""

# Ownership & Governance
service_owner: ""                # business/IT owner
technical_contact: ""            # SME / administrator
security_team_contact: ""        # SOC/CTI/IR point of contact
documentation_links: []          # internal wiki, vendor docs
compliance_relevance: []         # PCI | HIPAA | SOX | ISO | CIS

notes: ""
tags: []
created:
updated:
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
