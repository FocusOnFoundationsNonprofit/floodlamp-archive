## Task: Audit and Fix Markdown Files

### Scope
- **Folder:** The user will specify which folder to work on when invoking this prompt. If no folder is provided, ask before proceeding.
- **Include:** Only `.md` files in the ROOT of that folder (no subfolders)
- **Exclude:** Any `.md` file whose filename starts with an underscore (`_`)

### Reference
The required metadata and content format is defined in:
`@data/floodlamp/_prompts/prompt_convert-source-to-archive-md.md`

Read that file first before doing anything else. Understand the expected structure fully.

### Checks to Perform (in this order)

**Step 1 — List target files**
List all in-scope `.md` files. For each one, also identify its corresponding source file (same filename but with `.docx`, `.pdf`, or `.xlsx` extension, located in the same folder). Prefer `.docx` over `.pdf` when multiple source formats exist, since docx is easier to parse accurately.

Print the file list with the chosen source file for each before proceeding. Wait for my confirmation.

**Step 2 — For EACH markdown file, do all of the following:**

(a) **Metadata check:** Verify the YAML front matter matches the required format from the reference prompt.

(b) **Content formatting check:** Verify the body content follows the formatting rules from the reference prompt. This includes heading levels, link formatting, list styles, etc.

(c) **Level-1 heading fix:** If there is a `#` heading near the top of the document (first page area), replace it with `***INTERNAL TITLE:***`. Leave any `#` headings appearing later in the document untouched (those need manual review).

(d) **Source file comparison (CRITICAL — do NOT skip this):**
   - Open the chosen source file (e.g., the `.docx` version)
   - Compare it against the markdown content
   - Check and fix: missing sections, missing paragraphs, garbled or truncated text

**Step 3 — Apply fixes**
After completing all checks for a single file:
- Fix every issue found (from metadata, formatting, and source comparison)
- I should be able to do the step where I review your changes after

### Important Reminders
- The source comparison in Step 2d is essential — it catches content errors that format-only checks miss. Always do it.
- When reading source files, pick the most parseable format: `.docx` > `.xlsx` > `.pdf`
- If a source file cannot be found or read for a given markdown, let me know in your summary after checks.
