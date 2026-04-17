## FloodLAMP Archive Item Template Setup
This first-pass template is meant for the main `primary` archive items. It renders the item page as a metadata-and-links hub, with `summary-short` first and the three main actions directly under it:

- `gfile-url`
- `github-markdown-url`
- `github-markdown-download-url`


## Files
Use these files from this folder:

- `floodlamp_archive_item_template.js`
- `floodlamp_archive_item_template_embed.html`


## Recommended Webflow Structure
On the archive item CMS template page, leave your navbar and footer as they are, and add only one middle wrapper:

- Add one `Section`
- Inside it, add one `Container`
- Inside that, add one `HTML Embed`

Paste the contents of `floodlamp_archive_item_template_embed.html` into that embed.

That embed already includes the required root element:

- `#fl-archive-template-root`

The JavaScript will render everything inside that root, so you do not need to build the page layout in the Webflow Designer.


## Bind CMS Fields In The Embed
Replace each `REPLACE_WITH_*` token in the embed with the matching CMS field.

Use this mapping:

| Embed token | Webflow CMS field |
| --- | --- |
| `REPLACE_WITH_TITLE` | `title` |
| `REPLACE_WITH_SUMMARY_SHORT` | `summary-short` |
| `REPLACE_WITH_ARCHIVE_ITEM_TYPE` | `archive-item-type` |
| `REPLACE_WITH_ARCHIVE_SCOPE` | `archive-scope` |
| `REPLACE_WITH_CATEGORY` | `category` |
| `REPLACE_WITH_SUBCATEGORY` | `subcategory` |
| `REPLACE_WITH_SOURCE_FILE_NAME` | `source-file-name` |
| `REPLACE_WITH_SOURCE_REL_PATH` | `source-rel-path` |
| `REPLACE_WITH_FILE_DATE` | `file-date` |
| `REPLACE_WITH_NOTES` | `notes` |
| `REPLACE_WITH_TAGS` | `tags` |
| `REPLACE_WITH_SOURCE_FILE_TYPE` | `source-file-type` |
| `REPLACE_WITH_XFILE_TYPE` | `xfile-type` |
| `REPLACE_WITH_CONVERSION_INPUT_FILE_TYPE` | `conversion-input-file-type` |
| `REPLACE_WITH_CONVERSION` | `conversion` |
| `REPLACE_WITH_LICENSE` | `license` |
| `REPLACE_WITH_WORDS` | `words` |
| `REPLACE_WITH_TOKENS` | `tokens` |
| `REPLACE_WITH_AUDIO_FILE_NAME` | `audio-file-name` |
| `REPLACE_WITH_GFILE_URL` | `gfile-url` |
| `REPLACE_WITH_XFILE_GITHUB_DOWNLOAD_URL` | `xfile-github-download-url` |
| `REPLACE_WITH_PDF_GDRIVE_URL` | `pdf-gdrive-url` |
| `REPLACE_WITH_PDF_GITHUB_URL` | `pdf-github-url` |
| `REPLACE_WITH_GITHUB_MARKDOWN_URL` | `github-markdown-url` |
| `REPLACE_WITH_GITHUB_MARKDOWN_DOWNLOAD_URL` | `github-markdown-download-url` |
| `REPLACE_WITH_WEB_PDF_URL` | `web-pdf-url` |
| `REPLACE_WITH_WEB_SLIDES_URL` | `web-slides-url` |
| `REPLACE_WITH_YOUTUBE_URL` | `youtube-url` |
| `REPLACE_WITH_WEB_URL` | `web-url` |


## Add The JavaScript
Put the contents of `floodlamp_archive_item_template.js` into the archive item template page custom code:

- Webflow page settings
- `Before </body>` custom code
- Wrap it in `<script>...</script>`

Do not put this one in the `<head>`. It is better in the page footer/body custom code so the CMS markup already exists when the script runs.


## Suggested First Test Item
Start with a representative primary item that has all the main links populated, for example:

- `guides-manufacturing-assay-and-reagent-manufacturing-diagrams`

That item should show:

- `summary-short` at the top
- prominent cards for Google file, GitHub markdown view, and markdown download
- lower sections for PDF and original-file access when present
- metadata rows for category, subcategory, file type, date, license, words, tokens, and archive path


## Notes On This First Version
This version is intentionally optimized for your main `primary` archive files.

- It will still render non-primary items.
- It hides missing links instead of leaving dead UI.
- It does not yet try to solve all category-specific or secondary-file edge cases.
- It injects its own CSS, so you do not need to create Webflow classes first.


## Good Next Iterations
After you test the first live item, the next useful refinements are:

- tune the copy and visual emphasis of the three top actions
- add combined-files and related-files logic
- add file-type-specific labels or previews for PDFs, slides, spreadsheets, and special cases
- decide whether to expose notes and tags everywhere or only on some item types
