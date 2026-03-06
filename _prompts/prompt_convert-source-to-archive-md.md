# Prompt: Convert Source Files to Archive Markdown

## Instructions for AI
You are helping convert source files (docx, pptx, pdf, etc.) into completed archive markdown files for the FloodLAMP archive. You will produce one markdown file per document set, with a standardized METADATA section and a cleaned-up CONTENT section. This prompt works for either a single file or a folder of files.

The user will provide:
- This prompt
- The source files to convert (or a path to a folder containing them)
- One or more example completed markdown files from the archive to use as a template for metadata fields and content formatting

### Step-by-Step Process

#### 1. Identify Source Files and Grouping
- List all files in the target folder
- Group files that belong to the same document (e.g., `SOP-101.docx`, `SOP-101.pdf` are the same document in different formats)
- Each group produces one output `.md` file

#### 2. Choose Conversion Method per File
- **docx available → use pandoc** (`conversion: pandoc`, `conversion_input_file_type: docx`). This is the preferred method — use it whenever a docx is available.
- **pptx available → use msmid** (Microsoft MarkItDown) (`conversion: msmid`, `conversion_input_file_type: pptx`). Good for extracting text from presentations. For image-heavy slides and other visual elements (diagrams, charts, photos), extract the slide or figure title and add a brief 1–2 sentence description as a placeholder in italics, enclosed in single underscores (for example: `_Brief description of the diagram or photo in 1–2 sentences._`).
- **xlsx available → use msmid** (Microsoft MarkItDown) (`conversion: msmid`, `conversion_input_file_type: xlsx`). Converts each sheet into a markdown heading (`## Sheet Name`) followed by a pipe table. Cleanup needed: replace `NaN` with empty cells, rename `Unnamed: N` columns, remove empty rows/columns, and verify table structure against the original spreadsheet.
- **pdf only → use llamaparse or msmid** (`conversion: llamaparse` or `conversion: msmid`, `conversion_input_file_type: pdf`). Use only when no docx, pptx, or xlsx is available.

Run the conversion using the appropriate function from `primary/conversion.py`:
- `convert_file_to_md_pandoc(file_path)` for docx
- `convert_file_to_md_msmid(file_path)` for pptx, xlsx, or pdf
- `convert_llamaparse_pdf_to_md(file_path)` for pdf (alternative)

#### 3. Extract Document Header Info
Even when converting from docx, also run a conversion on the PDF to extract the document header block (Document Number, Effective Date, Version), since these are often lost or mangled in complex table-based layouts. Look for:
- Document Number (e.g., SOP-201-A_2)
- Effective Date (e.g., 02/26/2022)
- Version (e.g., 2)
- Internal Title

#### 4. Clean Up the Raw Conversion Output
This is the manual review step — the most important part:
- Convert leftover HTML tables into clean markdown (headings, lists, pipe tables)
- Fix garbled characters, escaped backticks, stray page numbers
- Reconstruct proper heading hierarchy (`##` for major sections, `###` for subsections)
- Remove all image references — archive markdowns are standalone text files
- Remove pandoc artifacts (empty table rows, excessive whitespace, redundant formatting)
- Verify content against the PDF to ensure nothing was lost or misinterpreted
- For image-heavy documents (diagrams, presentations, charts, photos): remove image references but keep titles/headings and add a brief 1–2 sentence description of each visual element as a placeholder in italics, enclosed in single underscores (for example: `_Brief description of the diagram or photo in 1–2 sentences._`)
- End each pipe table with a line containing double pipe `||` (after the last data row).
- Where the source has hyperlinked text, preserve the link in the converted file using markdown link syntax: `[hyperlinked text](URL)`. Do not drop URLs or leave raw URLs without the descriptive link text.

#### 5. Build the METADATA Section
Create the metadata block using the exact same fields as the example files. Standard fields:

```
METADATA
last updated: [YYYY-MM-DD] [initials] initial conversion
file_name: [filename].md
file_date: [effective date from document, YYYY-MM-DD format]
title: FloodLAMP [QMS or other prefix] [Document Number] [Title]
category: [category]
subcategory: [subcategory]
tags: 
source_file_type: [gdoc, gslides, gsheet, etc. — the original Google Workspace type]
xfile_type: [docx, pptx, xlsx, pdf — the exported file type]
gfile_url: [Google Doc/Slides/Sheet URL — flag if unknown]
xfile_github_download_url: [construct programmatically — see URL construction rules below]
pdf_gdrive_url: [Google Drive URL for the PDF — flag if unknown]
pdf_github_url: [construct programmatically — see URL construction rules below, or "na" if no PDF exists]
conversion_input_file_type: [docx, pptx, pdf — which file was actually fed to the converter]
conversion: [pandoc, msmid, llamaparse, etc.]
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: [to be calculated]
words: [to be calculated]
notes: [any relevant notes about the conversion or document]
summary_short: [1-3 sentence description]
```

**URL Construction Rules for `xfile_github_download_url` and `pdf_github_url`:**
These two fields are constructed programmatically from the file's metadata — they do not need to be looked up. The formula is:

- `xfile_github_download_url`: `https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/{category}/{subcategory}/{url_encoded_filename}.{xfile_type}`
- `pdf_github_url`: `https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/{category}/{subcategory}/{url_encoded_filename}.pdf`

Where:
- `{category}` and `{subcategory}` come from the metadata fields
- `{url_encoded_filename}` is the `file_name` field minus the `.md` extension, with spaces URL-encoded as `%20` and other special characters percent-encoded
- `{xfile_type}` is the exported file extension from the `xfile_type` metadata field (e.g., `docx`, `pptx`, `xlsx`)
- If no PDF exists for the document, set `pdf_github_url` to `na`

There is also a function `add_and_validate_github_urls()` in `primary/floodlamp_archive.py` that can construct and validate these URLs across a folder. It reads the metadata fields (`file_name`, `category`, `subcategory`, `xfile_type`) and fills in empty URL fields automatically. You can run this after creating the files to auto-populate or validate the URLs.

#### 6. Build the CONTENT Section
Start with the standard document header block (matching the example files), then the cleaned content:

```
CONTENT

***INTERNAL TITLE:*** [title as it appears in the actual doc, if present, omit if no internal document title]

[cleaned content with proper markdown headings and formatting]
```

For non-SOP documents (presentations, spreadsheets, etc.), adapt the header block as appropriate or omit SOP-specific fields.

#### 7. Write the summary_short
Compose a 1-3 sentence description of the document's purpose and key contents. Style:
- Start with the artifact directly (e.g., "The FloodLAMP QMS SOP-201-A_2 is a manufacturing run form for...")
- Be concise and specific
- Do not write "This document..." as the opener

#### 8. Calculate tokens and words
Run `update_metadata_words_tokens()` from `primary/floodlamp_archive.py` on the target folder to populate the `tokens` and `words` fields using the project's actual tokenizer. Set the folder path in the `mrun_update_metadata_words_tokens` stub and run it.

#### 9. Flag Unknown Fields
For any metadata values that cannot be determined from the source files, insert `**FLAGGED - UNKNOWN**` (or a more specific flag like `**FLAGGED - day not specified in original**`). This makes unknowns searchable so the human author can find and fill them in later. Common fields that may need flagging:
- `gfile_url` (Google source URLs — not in the exported files)
- `pdf_gdrive_url` (Google Drive PDF URLs)
- `file_date` (when the document doesn't contain an explicit effective date)
- `source_file_type` (when uncertain whether the original was gdoc, gslides, etc.)

#### 10. Clean Up
- Delete intermediate conversion files (`_pandoc.md`, `_msmid.md`, `_llamaparse.md`)
- Delete any extracted media folders created by pandoc (`media/`)
- Re-comment the `if __name__` stub back to `#if __name__`

### Quality Checklist
- [ ] Content matches the PDF — nothing lost or fabricated
- [ ] No image references remain in the markdown
- [ ] No leftover HTML in the content
- [ ] Hyperlinks preserved as `[text](URL)` where the source had links
- [ ] Pipe tables end with a line containing `||`
- [ ] Heading hierarchy is clean and consistent
- [ ] Metadata fields match the example files exactly (same field names, same order)
- [ ] Unknown fields are flagged (bold, searchable)
- [ ] tokens and words populated by the actual tokenizer
- [ ] Intermediate files cleaned up
- [ ] summary_short is accurate and follows style conventions
