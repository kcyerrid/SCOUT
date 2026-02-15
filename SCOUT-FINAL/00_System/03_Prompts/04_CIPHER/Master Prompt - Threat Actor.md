---
type: ai_build
prompt_id: 
source_notes: []
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
status: generated
---

# AI Build — <% tp.file.title %>

## Prompt Used
- Prompt ID: **`<% tp.frontmatter.prompt_id %>`**
- Prompt Note: [[90_AI/Prompts/<% tp.frontmatter.prompt_id %>]]

## Input Context
- Source Notes:
<%*
const sources = tp.frontmatter.source_notes || [];
sources.forEach(s => tR += `- [[${s}]]\n`);
%>

---

## AI Instructions (DO NOT EDIT)

You are executing an **Obsidian-stored master prompt**.

1. Load the prompt content from:
   `90_AI/Prompts/<prompt_id>.md`
2. Treat that note as the **system prompt**
3. Treat the content of the linked source notes as **user input**
4. Generate a **fully Obsidian-compliant document**, including:
   - YAML frontmatter
   - Structured markdown
   - Tasks where appropriate
   - Headings, lists, and links
5. Do NOT mention Smart Connections, ChatGPT, or the execution mechanism
6. Output ONLY the generated document

---

## EXECUTE (Smart Connections)

> **Smart Connections Prompt**
>
> Use the prompt at:
> `[[90_AI/Prompts/<prompt_id>]]`
>
> Apply it to:
> <% tp.frontmatter.source_notes?.map(n => `[[${n}]]`).join(", ") %>
>
> Generate the final Obsidian document below.
