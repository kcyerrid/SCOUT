<%*
/*
 Service Level Agreement Bootstrap Script
 - Prompts for SLA ID and SLA Title
 - Creates SLA note at the folder level (no per-SLA subfolder)
 - Uses Canonical SLA Template
*/

// Prompt user for identifiers
const slaIdInput = await tp.system.prompt("Enter SLA ID (e.g., SLA-00012)");
const slaTitleInput = await tp.system.prompt("Enter SLA Title");

// Defensive defaults
const slaId = slaIdInput?.trim() || "SLA-UNASSIGNED";
const slaTitle = slaTitleInput?.trim() || "Unnamed SLA";

// Build safe filename
let filename = `${slaId} - ${slaTitle}`;
filename = filename.replace(/[\\/:*?"<>|]/g, "-");

// Target folder ONLY (not a per-SLA directory)
const targetFolder = "10_Operations/11_Service_Level_Agreements";

// Create SLA note from Canonical SLA Template
await tp.file.create_new(
  tp.file.find_tfile(
    "00_System/00_Templates/02_Operations/Service Level Agreement Template.md"
  ),
  filename,
  false,
  targetFolder
);

// Open the newly created SLA note
await tp.file.open(`${targetFolder}/${filename}`);

// Prevent bootstrap script content from rendering
tR = "";
%>
