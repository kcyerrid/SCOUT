<%*
const TARGET_FOLDER = "30_CIPHER/03_Threat_Actors";
const SENTINEL = "SENTINEL: CIPHER_THREAT_ACTOR_V1";

// ---------- Utilities ----------
function sanitizeFileName(name) {
  return name.replace(/[\\\/:*?"<>|]/g, "-").replace(/\s+/g, " ").trim();
}

async function ensureFolderRecursive(path) {
  const parts = path.split("/").filter(Boolean);
  let current = "";
  for (const part of parts) {
    current = current ? `${current}/${part}` : part;
    if (!app.vault.getAbstractFileByPath(current)) await app.vault.createFolder(current);
  }
}

async function callAi(promptText) {
  if (tp.ai && typeof tp.ai.openai === "function") return await tp.ai.openai(promptText);
  if (tp.ai && typeof tp.ai.chat === "function") return await tp.ai.chat(promptText);
  if (tp.ai && typeof tp.ai.complete === "function") return await tp.ai.complete(promptText);
  if (tp.ai && typeof tp.ai.generate === "function") return await tp.ai.generate(promptText);
  throw new Error("No tp.ai.* function found. Check AI for Templater configuration.");
}

function normalizeText(text) {
  if (!text || typeof text !== "string") return "";
  let s = text.replace(/^\uFEFF/, "").trimStart();

  if (s.startsWith("```")) {
    s = s.replace(/^```[a-zA-Z]*\s*/, "");
    s = s.replace(/\s*```$/, "");
    s = s.trimStart();
  }

  const idx = s.indexOf("---");
  if (idx > 0) s = s.slice(idx);

  return s.trimStart();
}

async function callAiWithRetry(promptText, parseFn, label) {
  const first = normalizeText(await callAi(promptText));
  try {
    return parseFn(first);
  } catch (e1) {
    const retryPrompt =
      `RETRY: STRICT FORMAT REQUIRED for ${label}.
The FIRST LINE of your response MUST be exactly: ---
Return ONLY the required output format. No prose. No code fences. No blank lines before ---.

` + promptText;

    const second = normalizeText(await callAi(retryPrompt));
    return parseFn(second);
  }
}

// ---------- Parsing ----------
function parseAsk1Yaml(yamlText) {
  const s = (yamlText || "").trimStart();

  const start = s.indexOf("---");
  if (start === -1) throw new Error("Ask1: missing YAML start");

  const s2 = s.slice(start);
  const end = s2.indexOf("\n---", 3);
  if (end === -1) throw new Error("Ask1: missing YAML end");

  const body = s2.slice(3, end).trim();

  function getScalar(key) {
    const re = new RegExp(`^${key}:\\s*(.*)$`, "m");
    const m = body.match(re);
    if (!m) return "";
    return (m[1] || "").trim().replace(/^"(.*)"$/, "$1").replace(/^'(.*)'$/, "$1");
  }

  function getList(key) {
    const re = new RegExp(`^${key}:\\s*$([\\s\\S]*?)(^\\w[\\w_-]*:\\s|$)`, "m");
    const m = body.match(re);
    if (!m) return [];
    const block = m[1] || "";
    const items = [];
    for (const line of block.split("\n")) {
      const mm = line.match(/^\s*-\s*(.*)\s*$/);
      if (mm) {
        const v = (mm[1] || "").trim().replace(/^"(.*)"$/, "$1").replace(/^'(.*)'$/, "$1");
        if (v) items.push(v);
      }
    }
    return items;
  }

  const canonical_name = getScalar("canonical_name");
  const aliases = getList("aliases");
  const confidence = (getScalar("confidence") || "low").toLowerCase();
  const common_confusions = getList("common_confusions");
  const notes = getScalar("notes");

  if (!canonical_name) throw new Error("Ask1: canonical_name empty");
  return { canonical_name, aliases, confidence, common_confusions, notes };
}

function parseJsonStrict(jsonText) {
  const s = (jsonText || "").trim();
  if (!s.startsWith("{")) throw new Error("JSON: missing {");
  return JSON.parse(s);
}

// ---------- Small helpers ----------
function mapConfidenceToAttribution(conf) {
  const c = (conf || "").toLowerCase();
  if (c === "high") return "1-high";
  if (c === "medium") return "2-medium";
  return "3-low";
}

function listBullets(arr) {
  const items = (arr || []).filter(Boolean);
  if (!items.length) return "- (None noted in this bootstrap profile.)";
  return items.map(x => `- ${x}`).join("\n");
}

// ---------- Prompts ----------
function promptAsk1(inputName) {
  return `You are a CTI analyst. Normalize the identity for the threat actor name below.

INPUT_ACTOR_NAME: "${inputName}"

REQUIREMENTS
- Do not browse the web.
- Do not cite sources.
- Do not invent internal IDs.
- If you are uncertain, say so explicitly.
- Prefer widely used public names and widely known aliases.
- Avoid “Spider” alias proliferation unless you are confident it is actually used.

OUTPUT FORMAT (return ONLY this YAML block; no markdown, no prose)
---
canonical_name: ""
aliases:
  - ""
  - ""
confidence: "high|medium|low"
common_confusions:
  - ""
  - ""
notes: ""
---`;
}

function promptAsk2(canonicalName, aliases) {
  return `You are a CTI analyst producing a first-brief “foothold” characterization for a threat actor.
This is an orientation product, not a final intelligence report.

ACTOR_CANONICAL_NAME: "${canonicalName}"
ACTOR_ALIASES (if any): ${JSON.stringify(aliases || [])}

REQUIREMENTS
- Do not browse the web.
- Do not cite sources.
- Do not fabricate nation-state attribution as fact.
- Be decisive but honest: include uncertainty as constraints, not as filler.
- Keep language practical, defender-oriented.
- Avoid generic “APT-style” filler.

OUTPUT FORMAT (return ONLY valid JSON)
{
  "executive_summary": "2-5 sentences.",
  "attribution_notes": [
    "3-6 bullets; include uncertainty where appropriate."
  ],
  "motivations_objectives": [
    "3-6 bullets."
  ],
  "targeting_profile": [
    "3-6 bullets (sectors/regions/org-types) expressed at a practical level."
  ],
  "risk_level_suggestion": "Low|Medium|High|Critical",
  "confidence": "high|medium|low",
  "analyst_caveats": [
    "2-5 bullets describing what is most likely to be wrong or disputed."
  ]
}`;
}

// ---------- Assemble final note (minimal: Ask1 + Ask2 only) ----------
function buildFinalNote(actorName, aliases, attributionConfidence, riskLevel, a2) {
  const now = tp.date.now("YYYY-MM-DD");

  return [
`---`,
`entity_type: threat_actor`,
``,
`actor_name: "${actorName}"`,
`aliases: ${JSON.stringify(aliases || [])}`,
`actor_id: ""`,
``,
`nation_state: ""`,
`sponsor_type: []`,
`motivation: []`,
`attribution_confidence:`,
`  - ${attributionConfidence}`,
`first_identified: ""`,
`active_period: ""`,
``,
`target_sectors: []`,
`target_regions: []`,
`target_technologies: []`,
``,
`ttp_profile: []`,
`malware_used: []`,
`tools_used: []`,
`infrastructure_profile: []`,
``,
`associated_campaigns: []`,
`related_incidents: []`,
``,
`risk_level: "${riskLevel || ""}"`,
`threat_score: 1`,
``,
`intel_sources: []`,
`tlp_classification: ""`,
``,
`created: ${now}`,
`updated: ${now}`,
`banner: 99_Attachments/SCOUT_Obsidian_Banner.png`,
`banner-display: contain`,
`banner-repeat: false`,
`banner-height: 100`,
`content-start: 101`,
`---`,
``,
SENTINEL,
``,
`# ${actorName}`,
``,
`## 1. Executive Summary`,
`${a2.executive_summary || ""}`,
``,
`## 2. Attribution Notes`,
`${listBullets(a2.attribution_notes)}`,
``,
`## 3. Motivations & Objectives`,
`${listBullets(a2.motivations_objectives)}`,
``,
`## 4. Targeting Profile`,
`${listBullets(a2.targeting_profile)}`,
``,
`## 5. Tradecraft Overview`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 6. MITRE ATT&CK Mapping`,
``,
`### 6.1 Techniques Used`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`### 6.2 Notable Procedure Variations`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 7. Malware & Tools Used`,
``,
`### 7.1 Malware`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`### 7.2 Tools (Living-off-the-Land or COTS)`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 8. Infrastructure Patterns`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 9. Campaign History`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 10. Known Indicators`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 11. Defensive Recommendations`,
`- (Not generated in this minimal multi-ask smoke test.)`,
``,
`## 12. Analyst Notes`,
`${listBullets(a2.analyst_caveats)}`,
``,
`## 13. References`,
`- (Optional) Add authoritative sources as you validate and refine this bootstrap profile.`
].join("\n");
}

// ---------- Main ----------
const input = await tp.system.prompt("Threat actor name");
if (!input || !input.trim()) throw new Error("Threat actor name is required.");
const INPUT_NAME = input.trim();

// Resolve current note
const currentPath = tp.file.path(true);
const currentFile = tp.file.find_tfile(currentPath);
if (!currentFile) throw new Error("Could not resolve current note file: " + currentPath);

// Run Ask1 + Ask2 (minimal smoke test)
const a1 = await callAiWithRetry(promptAsk1(INPUT_NAME), parseAsk1Yaml, "Ask 1 (Normalization)");
const CANON = a1.canonical_name;
const ALIASES = a1.aliases || [];

const a2 = await callAiWithRetry(promptAsk2(CANON, ALIASES), parseJsonStrict, "Ask 2 (Characterization)");

const attributionConfidence = mapConfidenceToAttribution(a2.confidence || a1.confidence);
const riskLevel = a2.risk_level_suggestion || "";

// Write + move
await ensureFolderRecursive(TARGET_FOLDER);

const SAFE_NAME = sanitizeFileName(CANON);
const FINAL_PATH = `${TARGET_FOLDER}/TA - ${SAFE_NAME}.md`;

// Write into current file first
const finalText = buildFinalNote(CANON, ALIASES, attributionConfidence, riskLevel, a2);
await app.vault.modify(currentFile, finalText);

// Rename/move the staging note
await app.fileManager.renameFile(currentFile, FINAL_PATH);

// Open final file
const finalFile = app.vault.getAbstractFileByPath(FINAL_PATH);
if (finalFile) await app.workspace.getLeaf(true).openFile(finalFile);

tR = "";
%>
