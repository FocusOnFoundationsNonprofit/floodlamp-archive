# Prompt: Save AI Response to Archive Markdown

## Instructions for AI
You are helping convert a previous AI response from this conversation into a completed archive markdown file for the FloodLAMP archive. The user has already received an AI-generated analysis or write-up in a prior message, and now wants it saved as a properly formatted archive file with standardized metadata.

The user will provide:
- This prompt
- The target folder where the file should be saved (as a path like `data/floodlamp/guides/sds` or by naming the subcategory)

Use `data/floodlamp/various/fl-whitepapers/_AI_Comparable Programs Survey - Household Pooled COVID-19 Testing.md` as the example template for metadata fields and formatting. Read this file to see the exact field names, field order, and style conventions.

### Step-by-Step Process

#### 1. Identify the Response to Archive
- Look back in the conversation for the AI-generated response that should be saved
- Identify the user's original prompt that produced that response
- Identify all files that were included in the context window for that prompt

#### 2. Build the METADATA Section
Create the metadata block using the exact same fields and field order as the example template (`data/floodlamp/various/fl-whitepapers/_AI_Comparable Programs Survey - Household Pooled COVID-19 Testing.md`). Standard fields for AI-generated content:

```
METADATA
last updated: [YYYY-MM-DD] RT initial creation
file_name: _AI_[filename].md
file_date: [YYYY-MM-DD, today's date]
title: FloodLAMP [Descriptive Title]
category: [category from target folder path]
subcategory: [subcategory from target folder path]
tags: 
source_file_type: md
xfile_type: NA
gfile_url: **FLAGGED - FILL IN AFTER INSERTING INTO GDRIVE**
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/{category}/{subcategory}/_AI_{url_encoded_filename}.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 0
words: 0
notes: Created by [model name] during archive preparation. **NOT HUMAN VERIFIED - MAY CONTAIN ERRORS** [Brief description of what was analyzed and key source documents used.]
summary_short: [1-3 sentence description following archive style — start with the artifact name, be concise and specific, do not open with "This document..."]
```

Key metadata notes:
- `gfile_url`: Leave blank (no Google Doc source for AI-generated content)
- `source_file_type` through `conversion`: All NA since this is AI-generated, not converted from a source file
- `tokens` and `words`: Set to 0 initially; will be populated by the tokenizer in a later step
- `notes`: Must include the AI model name and the **NOT HUMAN VERIFIED** caveat. Also describe the analysis and list key source documents.
- For `xfile_github_download_url`: URL-encode spaces as `%20` in the filename portion

#### 3. Build the Prompt Section
At the top of the CONTENT section (before the response body), include two versions of the original prompt as H2 headings:

**## Prompt (Verbatim)**
The exact text of the user's original prompt, unedited. If the prompt was voice-dictated, include it as-is with all speech artifacts.

Below the verbatim prompt, add:
```
**Files included in context window:**
- [filename1]
- [filename2]
- ...
```
List only filenames (no paths, no other text). If any filenames contain personally identifiable information, sanitize them.

**## Prompt (Cleaned)**
A lightly cleaned version of the same prompt: remove filler words ("you know", "yeah", "like"), fix grammar, consolidate repeated phrasing, and organize into clear paragraphs. Preserve the original meaning and all specific details.

Below the cleaned prompt, add the same file list.

#### 4. Build the CONTENT Section
After the prompt sections, include the full AI response with proper markdown formatting:
- Use `##` for major sections, `###` for subsections
- End every pipe table with a row containing `|||`
- Use proper markdown: headings (not bold-only pseudo-headings), hyphen bullets, pipe tables with leading/trailing pipes and single-space cell padding
- Replace special Unicode characters (em dashes, curly quotes, etc.) with ASCII equivalents where appropriate for archive consistency
- Do not include any personally identifiable information if the user requested PII exclusion

#### 5. Write the File
Save to the target folder with the `_AI_` prefix followed by a descriptive filename (e.g., `_AI_Waste Disposal and Risk Assessment.md`). All AI-generated archive files must start with the `_AI_` prefix to distinguish them from human-authored or converted source documents.

#### 6. Calculate Tokens and Words
Run `update_metadata_words_tokens()` from `primary/floodlamp_archive.py` on the target folder by calling the function directly with the target folder path:

```
.venv/bin/python -c "from primary.floodlamp_archive import update_metadata_words_tokens; update_metadata_words_tokens('TARGET_FOLDER', suffix_pattern='.md', include_subfolders=False)"
```

Replace `TARGET_FOLDER` with the actual target folder path (e.g., `data/floodlamp/guides/sds`).

#### 7. Verify
- Confirm the tokens and words fields were populated in the file
- Check for any formatting issues

### Quality Checklist
- [ ] Metadata fields match the example file exactly (same field names, same order)
- [ ] `notes` field includes AI model name and **NOT HUMAN VERIFIED** caveat
- [ ] Prompt (Verbatim) section includes exact original prompt text
- [ ] Prompt (Cleaned) section is a readable, lightly edited version
- [ ] Both prompt sections include the file reference list
- [ ] No PII if exclusion was requested
- [ ] Full AI response is included with proper markdown formatting
- [ ] All pipe tables end with `|||`
- [ ] Tokens and words populated by the actual tokenizer
