METADATA

For every qualifying `.md` file, read the metadata block at the top (between `METADATA` and `


CONTENT` lines) and extract:

- `file_name:` — the canonical filename (ignore the `.md` extension when comparing)
- `gfile_url:` — should point to a Google Doc, Sheet, Slides, or Form
- `pdf_gdrive_url:` — should point to a PDF in Google Drive

---

## STEP 3 — CLASSIFY EACH URL FIELD

For each of the two URL fields, classify as:

| Classification | Meaning | Action |
|---|---|---|
| **HAS_LINK** | Contains a URL starting with `https://` | Proceed to Check A and Check B |
| **NA** | Field value is literally "NA" | Skip — intentional, not an issue |
| **BLANK** | Field exists but has no value after the colon | FLAG for manual review |

---

## STEP 4 — CHECK A: FILENAME MATCH (for all HAS_LINK entries)

Use **WebFetch** to open each URL and extract the filename shown on the page.

- For `gfile_url` (Google Docs/Sheets): the document title is in the page metadata.
- For `pdf_gdrive_url` (Google Drive PDF): the filename is in the page metadata.

**Compare** the base name (stripping extensions like `.md`, `.pdf`, `.docx`) from the URL target against the `file_name:` metadata value.

- ✅ PASS if base names match.
- ❌ FLAG if they don't match — include both the expected and actual names in the report.

> **Tip:** WebFetch works reliably for this without requiring Chrome login. Batch multiple calls in parallel for speed.

---

## STEP 5 — CHECK B: FOLDER LOCATION (for all HAS_LINK entries)

> **⚠️ PREREQUISITE:** This check requires the **Chrome extension to be connected** and the user to be **logged into Google Drive** in Chrome. If Chrome is not available, skip this check and note it in the report.

### Efficient bulk method (recommended):

1. Navigate in Chrome to the target Google Drive folder:
   `Shared drives > FL MAIN > FloodLAMP Archive > Regulatory > [TARGET SUBFOLDER]`
2. Scroll through the entire folder listing to load all files.
3. Use JavaScript to extract all `data-id` attributes from the DOM — these are the file IDs of every file in the folder.
4. Extract the file IDs from all HAS_LINK URLs:
   - `gfile_url`: ID is after `/document/d/` or `/spreadsheets/d/` or `/presentation/d/`
   - `pdf_gdrive_url`: ID is after `/file/d/`
5. Cross-reference: check that every URL's file ID exists in the folder's ID set.

- ✅ PASS if the file ID is found in the target folder.
- ❌ FLAG if the file ID is NOT found — the file is in the wrong location.

> **Fallback (if bulk method fails):** Open individual files and click the move icon (➡️) next to the filename to view "Current location" — then cancel without making changes.

---

## STEP 6 — FLAG BLANK FIELDS

If any URL field is BLANK (not NA, not a URL — just empty after the colon), FLAG it for manual review.

- Do NOT flag fields that contain "NA" — those are intentional.

---

## STEP 7 — COMPILE REPORT

Present results in this format:

```
### ✅ Summary
- Total `.md` files scanned: [N]
- Total URL fields checked: [N] ([N] gfile_url + [N] pdf_gdrive_url)
- Fields classified as NA (skipped): [N]
- Blank fields found: [N]
- Files with no issues: [N]
- Files with issues flagged: [N]

---

### 🚩 Flagged Issues

Number each issue. Format:
[#]. [file_name value] — [short description]

Group under sub-headers:

#### Wrong filename
#### Wrong folder
#### Blank fields (needs manual review)

---

### 📋 Clean Files
List filenames that passed all checks (one per line).
Files that were NA/NA (both fields intentionally empty) should be marked with *(NA/NA)*.
```

---

## RULES — NEVER BREAK THESE

- ❌ Never edit, rename, move, or delete any file
- ❌ Never modify any Google Drive file or folder
- ❌ Never make changes to the markdown metadata
- ❌ Never click "Move" in the Google Drive dialog — always click "Cancel"
- ✅ Read-only access only — your job ends at reporting

---

## TROUBLESHOOTING

| Issue | Solution |
|---|---|
| Chrome extension not connected | Use WebFetch for filename checks (Check A). Skip folder checks (Check B) and note in report. |
| Google Drive login required | Ask user to log into Google Drive in Chrome, then retry. |
| WebFetch can't access a URL | Flag the URL as "inaccessible" in the report — do not skip silently. |
| Folder listing truncated | Scroll to the bottom of the Drive folder before extracting IDs via JavaScript. |
| Move dialog opens accidentally | Always click "Cancel" — never click "Move". |
