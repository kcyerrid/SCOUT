---
cssclasses: dashboard
banner: 99_Attachments/gold texture 3.png
---
# Common Tasks
- Quick Tasks
	- `BUTTON[open_daily_note]`
	- `BUTTON[gen_incident]`
	- `BUTTON[gen_meeting]`
	- `BUTTON[gen_playbook]`
	- `BUTTON[gen_procedure]`
	- `BUTTON[gen_kcy]`
	- `BUTTON[gen_sla]`
	- `BUTTON[gen_faq]`
	- `BUTTON[gen_how-to]`
- Quick Add Entities
	- `BUTTON[qa_assets]`
	- `BUTTON[qa_users]`
	- `BUTTON[qa_telemetry]`
	- `BUTTON[qa_detections]`
	- `BUTTON[qa_vulnerabilities]`
	- `BUTTON[qa_ioc]`
	- `BUTTON[qa_ttp]`
	- `BUTTON[qa_tools]`
	- `BUTTON[qa_configuration]`

# Dashboards, Views, and Reports
- SCOUT 
	- Scout Dashboard
	- Mental Health Dashboard
- CIPHER
	- Threat Actor Dashboard
	- Campaign Dashboard
	- Malware Dashboard

# Artificial Intelligence Integration
- 🏡 Generate Content
	- Threat Actor Note
	- Malware Note
	- Campaign Note
	- MITRE ATT&CK TTP Note

# Vault Info
- 🗄️ Recent file updates
 `$=dv.list(dv.pages('').sort(f=>f.file.mtime.ts,"desc").limit(4).file.link)`
- 🔖 Tagged:  favorite 
 `$=dv.list(dv.pages('#favorite').sort(f=>f.file.name,"desc").limit(4).file.link)`
- 〽️ Stats
	-  File Count: `$=dv.pages().length`
	-  Personal recipes: `$=dv.pages('"Family/Recipes"').length`

```meta-bind-button
label: "Open Today's Journal Note"
icon: ""
hidden: true
class: ""
tooltip: ""
id: open_daily_note
style: primary
actions:
  - type: command
    command: daily-notes
    folderPath: 10_Operations/09_Journals/01_Daily
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Spawn an Incident Investigation"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_incident
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Attend a Meeting"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_meeting
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/01_Entities/Meeting Template.md
    folderPath: 10_Operations/10_Meetings
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Create a New Playbook"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_playbook
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Playbook Template.md
    folderPath: 10_Operations/07_Playbooks
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Create a New Procedure"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_procedure
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/SOP Template.md
    folderPath: 10_Operations/05_Procedures
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Create a New ITID"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_kcy
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/04_ITID/ITID Bootstrap.md
    folderPath: 40_ITIDs/01_Definitions
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Create a New Service Level Agreement (SLA)"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_sla
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Service Level Agreement Bootstrap Script.md
    folderPath: 10_Operations/11_Service_Level_Agreements
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Create a New FAQ"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_faq
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/06_Knowledge_Base/FAQ.md
    folderPath: 60_Knowledge/FAQs
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Create a New How-To"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_how-to
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/06_Knowledge_Base/KB_How-To.md
    folderPath: 60_Knowledge/How-Tos
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```


```meta-bind-button
label: "Generate Threat Actor"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_threat_actor
style: default
actions:
  - type: open
    link: "[[Threat Actor]]"
```

```meta-bind-button
label: "Generate Malware Profile"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_malware
style: default
actions:
  - type: open
    link: "[[Malware]]"
```

```meta-bind-button
label: "Generate MITRE ATT&CK TTP"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_ttp
style: default
actions:
  - type: open
    link: "[[MITRE TTP]]"
```

```meta-bind-button
label: "Auto-Generate Threat Actor Note"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_ai_threat_actor
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/03_Prompts/04_CIPHER/Master Prompt - TA.md
    folderPath: 30_CIPHER/03_Threat_Actors
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Auto-Generate Malware Note"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_ai_malware
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/03_Prompts/04_CIPHER/Master Prompt - TA.md
    folderPath: 30_CIPHER/03_Threat_Actors
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "Auto-Generate MITRE ATT&CK TTP Note"
icon: ""
hidden: true
class: ""
tooltip: ""
id: gen_ai_ttp
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/03_Prompts/04_CIPHER/Master Prompt - TA.md
    folderPath: 30_CIPHER/03_Threat_Actors
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Asset"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_assets
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New User"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_users
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Telemetry Source"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_telemetry
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Detection"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_detections
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Vulnerability"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_vulnerabilities
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Indicator of Compromise (IOC)"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_ioc
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Tactic, Technique, Procedure (TTP)"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_ttp
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Tool"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_tools
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```

```meta-bind-button
label: "New Configuration"
icon: ""
hidden: true
class: ""
tooltip: ""
id: qa_configuration
style: default
actions:
  - type: templaterCreateNote
    templateFile: 00_System/00_Templates/02_Operations/Incident Bootstrap.md
    folderPath: 10_Operations/04_Incidents
    fileName: ""
    openNote: true
    openIfAlreadyExists: false
```