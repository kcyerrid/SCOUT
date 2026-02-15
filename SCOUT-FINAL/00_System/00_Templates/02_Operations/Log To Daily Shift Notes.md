<%*
const DAILY_ROOT = "10_Operations/09_Journals/01_Daily";
const MARKER = "<!-- SHIFT_NOTES_LOG -->";
const SHIFT_HEADING = "## 2. Shift Notes (Chronological Log)";

const now = tp.date.now("YYYY-MM-DD");
const dailyFile = tp.file.find_tfile(now);
if (!dailyFile) {
  new Notice("Daily note not found for " + now);
  return;
}

const currentFile = tp.file.find_tfile(tp.file.title);
const currentTitle = currentFile ? currentFile.basename : tp.file.title;
const currentLink = currentFile ? `[[${currentTitle}]]` : currentTitle;

const fm = tp.frontmatter ?? {};
const entityType = fm.entity_type ? String(fm.entity_type) : "";
const status = fm.status ? String(fm.status) : "";
const suffixParts = [];
if (entityType) suffixParts.push(entityType);
if (status) suffixParts.push(`status:${status}`);
const suffix = suffixParts.length ? ` (${suffixParts.join(", ")})` : "";

const logLine = `### ${tp.date.now("HH:mm")} — ${currentLink}${suffix}`;

const content = await app.vault.read(dailyFile);
let updated = content;

if (content.includes(MARKER)) {
  updated = content.replace(MARKER, `${MARKER}\n${logLine}`);
} else if (content.includes(SHIFT_HEADING)) {
  const insertAfter = SHIFT_HEADING;
  const idx = content.indexOf(insertAfter);
  const nextLineIdx = content.indexOf("\n", idx + insertAfter.length);
  const insertPos = nextLineIdx === -1 ? content.length : nextLineIdx + 1;
  updated = content.slice(0, insertPos) + `\n${logLine}\n` + content.slice(insertPos);
} else {
  updated = content + `\n\n${logLine}\n`;
}

await app.vault.modify(dailyFile, updated);
new Notice("Logged to today's Shift Notes.");
%>
