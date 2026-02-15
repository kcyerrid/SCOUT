---
entity_type: tool
tool_id: ""                      # Unique SCOUT ID (e.g., TOOL-SENTINEL, TOOL-FALCON)
tool_name: ""                    # Human-readable name (Microsoft Sentinel) 
tool_type:                     
- siem
- edr
- ndr
- cloud
- identity
- saas
- network
- email_security
- forensics
- utility
- other

vendor: ""                       # Microsoft, CrowdStrike, AWS, Okta, etc.
product_version: ""              # optional version/build
deployment_model:                # cloud | on-prem | hybrid | agent | agentless
- cloud
- on-prem
- hybrid
- agent
- agentless

description: ""                  # high-level tool overview
primary_functions: []            # logging, detection, response, EDR, identity, etc.
use_cases: []                    # top capabilities SOC relies on

environment_coverage:            # production | staging | dev | test
- production
- staging
- dev
- test
- other

asset_coverage:                
- windows
- linux
- macos
- iot
- cloud
- saas
- network
- mobile
- other

visibility_scope_endpoint:
- none
- partial
- good
- strong

visibility_scope_network:
- none
- partial
- good
- strong

visibility_scope_identity:
- none
- partial
- good
- strong

visibility_scope_cloud:
- none
- partial
- good
- strong

visibility_scope_email:
- none
- partial
- good
- strong

visibility_scope_saas:
- none
- partial
- good
- strong

integrations: []                 # integrations supported (SIEM, SOAR, EDR, CASB, email security)
data_sources_provided: []        # Telemetry sources this tool generates (link to Telemetry Source entities)
supported_techniques: []         # ATT&CK techniques the tool is capable of detecting or mitigating

authentication_method: 
- sso
- api key
- token
- username/password
- Azure AD
- Okta
- other
api_availability:                # yes | no | partial
- yes
- no
- partial
api_docs: ""                     # URL or internal doc

playbooks_available: []          # Playbooks referencing this tool
procedures_referenced: []        # SOPs that rely on this tool

known_limitations: []            # visibility gaps, blind spots, coverage issues
performance_notes: ""            # latency, ingestion delay, overhead, resource usage
operational_risks:             
- single point of failure
- licensing limits
- agent stability
- other

licensing_license_type:                  # per-user, per-endpoint, per-gb, etc.
- per-user
- per-endpoint
- per-gb
- other
renewal_date: ""
seats_used: ""
seats_total: ""

ownership_service_owner: ""              # who owns the tool internally
ownership_technical_contact: ""          # engineering SME
ownership_escalation_contact: ""
change_process: ""               # link to change mgmt document

training_resources: []           # internal training links or external courses
documentation_links: []          # vendor docs, internal guides

related_incidents: []            # incidents where this tool was pivotal
related_detections: []           # detections leveraging this tool
related_ttp_coverage: []         # ATT&CK IDs that the tool contributes coverage for

tags: []
created:
updated:
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---
