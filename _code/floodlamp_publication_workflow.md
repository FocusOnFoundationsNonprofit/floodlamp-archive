<!-- ===== START OF FILE floodlamp_publication_workflow.md ===== -->
<!-- Purpose: Single-source workflow guide for FloodLAMP archive build, web publication prep, CMS sync, and website-code layers. -->

## Update Checklist
### 1) Update the combined and zips rollups in local private corpus-tools repo
[] run floodlamp_archive_ops.mrun_update_all_archive
  [] review terminal output against expectations
  [] review source control changes against expectations
  [] spot check combined mds in cursor explorer - confirm changes
  [] spot check zips by unzipping from finder - confirm changes
  [] commit and sync repo

### 2) Refresh the embeds, Webflow CMS, and optionally S3 zips
[] run floodlamp_refresh.mrun_run_floodlamp_refresh_changed_only
  [] answer `n` to `Run floodlamp_archive_ops.update_all_archive?` if step 1 already ran
  [] answer `y` or `n` to `Run Amazon S3 zip upload?` (can be run separately later via mrun_run_floodlamp_s3_upload)
  [] answer `y` or `n` to `Run local archive embed refresh?`
  [] review terminal output and `changelogs-refresh/YYYY-MM-DD_TTTTTT_refresh.md` file
in Webflow CMS:
  [] spot check Webflow CMS items that changed (should say 'Queued to publish')
  [] filter by 'Queued to publish', select those, and Publish
[] switch to Webflow Design and publish to staging site
[] if not changing web design/copy, skip step 3 (embeds are verified in sync during refresh and won't change unless web-copy was edited)

### 3) If changing web design/copy
[] update .../webcode/floodlamp-archive-web-copy.md and maybe floodlamp_archive_md_to_embed.py and/or floodlamp_archive_item_template.js
[] run floodlamp_archive_md_to_embed.mrun_update_floodlamp_embeds_then_prompt_and_compare
[] if changed, copy and paste local embeds and `_template.js` to Webflow pages
[] publish to staging site
[] review live staging site for changes

### 4) Mirror to public repo 'floodlamp-archive'
[] check that public repo has clean working directory (in source control view)
[] in corpus-tools (private repo) run public-repo-mirror/mirror_to_repo.py
[] review changed files in source control in public repo
[] review terminal output and mirror_log.md
[] bring up GitHub md file that you expect to change and confirm old version
[] commit and sync public repo
[] refresh page and confirm change is now there
[] OPTIONAL: run nuke_history.sh in floodlamp-archive (public repo)

### 5) S3 zip upload (after staging check)
[] run floodlamp_refresh.mrun_run_floodlamp_s3_upload

### 6) Update GDrive Files
[] Get list of files that need to be updated
[] Manually update them

## FloodLAMP Publication Workflow
This document is the current single-source guide for how the FloodLAMP archive build, web publication prep, CMS sync, and website-code layers fit together.

It is meant to serve two audiences:
- Operator mode: what Randy needs to know right now to run the correct code with maximum clarity and minimum redundancy.
- Orientation mode: what a new person needs in order to understand how the modules relate to each other.

This document is intentionally pragmatic rather than idealized.
- The goal is not to redesign this codebase into a clean public framework before finishing the FloodLAMP publication work.
- The goal is to make the current code reliable enough, understandable enough, and controllable enough to finish this archive and web publication workflow without avoidable confusion.
- Some legacy structure, overlap, and technical debt are acceptable as long as the behavior is explicit and operator trust stays high.
- This document should therefore describe the code as it actually works now, including awkward boundaries and current limitations, rather than pretending the system is cleaner than it is.


## Operator Quick Read
- `floodlamp_archive_ops.py` is the trusted local archive build layer.
- `update_all_archive()` is the main local rebuild entry point for archive rollups.
- Archive rollups means: subcategory combined markdown files, subcategory zip files, category combined files, category context-commentary files, category zip files, and root-level archive outputs.
- `floodlamp_webflow_cms.py` is the lower-level CMS utility layer.
- `create_and_import_floodlamp_cms()` builds a CMS CSV from the current local archive state and pushes it to Webflow as create/update only.
- `create_and_import_floodlamp_cms()` does not delete stale Webflow items.
- `floodlamp_refresh.py` is the orchestration layer for web publication prep, not the primary archive-rollup build layer.
- `run_floodlamp_refresh_changed_only()` is now the main changed-only refresh entry point.
- `run_floodlamp_refresh_changed_only()` begins by asking `Run floodlamp_archive_ops.update_all_archive?`
- `run_floodlamp_refresh_changed_only()` then asks separately whether to do the Amazon S3 zip upload and local archive embed refresh stage.
- If you answer `yes`, it calls `update_all_archive()` directly rather than decomposing the local archive rebuild into narrower refresh helpers.
- If you answer `no`, it runs a fast trust check that verifies the expected archive rollup files exist, but it does not do a full temp-copy content comparison.
- After the archive-rollup decision, `run_floodlamp_refresh_changed_only()` handles the downstream refresh steps: S3 upload, embed sync, integrated archive view update, and CMS live sync.
- Backward-compatible alias: `run_floodlamp_update_changed_only()` now calls `run_floodlamp_refresh_changed_only()`.
- CMS update/import payloads now include blank mapped field values so stale live Webflow values can be cleared when the current expected local value is empty.
- A core part of operator verification is the Cursor/VS Code source-control view.
- The preferred behavior is that meaningful local file changes should show up there whenever possible, because that is part of the incremental verification workflow.
- Important wrinkle: full-content zip files with names matching `_zip_*.zip` are git-ignored in this repo, so changes to those files will not show up in the source-control view.
- Because of that, any workflow that updates full-content zip files needs explicit terminal/status visibility, not just reliance on source control.


## Operator Assumptions
- Randy is the primary operator and already knows the archive content and local verification process well.
- The local archive-rollup build in `floodlamp_archive_ops.py` is the most trusted part of the workflow because it has been exercised repeatedly with manual on-disk checking.
- Source control is part of the operating surface, not just a background tool.
- Seeing changed combined markdown files and changed markdown-only zip-adjacent outputs in the source-control view is useful for trust and verification.
- The code should avoid silently changing important operator-facing files without making that obvious either through source control or explicit terminal/status reporting.
- This system does not need to be generalized yet for broad public reuse; finishing this archive publication reliably is more important than architectural purity.


## Recommended Terms
Use these terms consistently when talking about the system.

| Term | Meaning | Primary code |
| --- | --- | --- |
| Archive source files | The actual FloodLAMP archive markdown and related source files under `data/floodlamp`, excluding generated outputs and excluded folders. | `floodlamp_archive_ops.py` and source files themselves |
| Archive rollups | Generated archive outputs on disk such as combined markdown files, zips, root metadata/list files, and related rollups. | `floodlamp_archive_ops.py` |
| Full-content zips | Zip files named like `_zip_floodlamp-archive-{scope}.zip` that include all intended files for that scope, not just markdown files. These exist at subcategory, category, and full-archive/root scope. | `floodlamp_archive_ops.py` |
| Markdown-only zips | Zip files named like `_zip-md_floodlamp-archive-{scope}.zip` that contain markdown-only subsets for that scope. These also exist at subcategory, category, and full-archive/root scope. | `floodlamp_archive_ops.py` |
| Web publication prep | Steps that prepare the archive for web publication: zip upload, embed sync, integrated archive view updates, CMS snapshot generation, and CMS live sync. | `floodlamp_refresh.py` and `floodlamp_webflow_cms.py` |
| Website presentation | Actual website-facing code, copy, embeds, templates, JS, HTML, and static page helpers. | `webcode/*` |

The key distinction is:
- `floodlamp_archive_ops.py` mainly handles archive source files plus archive rollups.
- `floodlamp_refresh.py` mainly handles web publication prep.
- `webcode/*` mainly handles website presentation.


## Verification Model
- The preferred verification model is layered:
- first trust the local archive-rollup build output in `floodlamp_archive_ops.py`,
- then use source control and direct file inspection to confirm expected changes,
- then run downstream web publication prep steps with explicit awareness of which steps touch live systems.
- Combined markdown files and many other generated markdown outputs are visible in source control when they change, and that visibility is important.
- Full-content zip files are a special case because the repo `.gitignore` contains `**/_zip_*.zip`.
- That means the full-content zips are intentionally hidden from normal source-control change review even when they are updated on disk.
- Markdown-only zips do not match that exact ignore rule and can remain visible depending on repo state and path, so do not assume the same visibility behavior for `_zip-md_*.zip` and `_zip_*.zip`.
- Operator takeaway: do not rely on the source-control view alone to detect changes to full-content zips.
- For full-content zips, rely on terminal output, explicit status markers, file timestamps/sizes if needed, and downstream artifact checks.


## Status Marker Convention
The current `floodlamp_archive_ops.py` status-marker convention should be preserved because it is useful for rapid operator review.

Current meanings:
- `✅ retained existing` means the generated artifact was checked and the existing file already matched the newly generated content.
- `⬆️ updated` means the generated artifact existed and was rewritten because the generated content changed.
- `⬆️ created new` means the generated artifact did not exist and was created.

This convention is implemented in the archive build layer and should remain the standard operator-facing signal for generated artifact writes.
- It is especially important for full-content zip files because those updates may not be visible in source control due to git-ignore behavior.
- It is also useful for keeping confidence high while doing repeated incremental runs and manual verification.


## Module Map
| Module | Role | Main operator-facing entry points |
| --- | --- | --- |
| `floodlamp_archive_ops.py` | Local archive build and rollups. | `update_all_archive()`, `update_category()`, `update_subcategory()`, `update_root_archive_files()` |
| `floodlamp_webflow_cms.py` | Build CMS rows/CSV and push to Webflow. | `create_floodlamp_cms_csv()`, `create_and_import_floodlamp_cms()` |
| `floodlamp_refresh.py` | Orchestrate status checks, archive-rollup trust/rebuild decisions, S3 upload, embed sync, integrated view update, and CMS live sync. | `run_floodlamp_refresh_status()`, `run_floodlamp_refresh_changed_only()`, `run_floodlamp_rebuild_everything()` |
| `floodlamp_publish_rules.py` | Shared publication rules, inclusion/exclusion logic, naming/path helpers. | Helper module, not mainly an operator entry point |
| `webcode/*` | Website content, template JS, embeds, and site presentation helpers. | Depends on file; not one central operator entry point |


## Current Workflow Layers
### Layer 1: Archive build and rollups
This layer is what Randy has been using and checking on disk.

Primary function:
- `update_all_archive()`

What it does:
- Validates category/subcategory metadata consistency.
- Runs `update_category()` for every category.
- `update_category()` runs `update_subcategory()` for each subcategory.
- Regenerates root-level archive outputs.

What this layer updates on disk:
- Source-file metadata fields that are refreshed by archive update logic.
- Subcategory combined markdown files.
- Subcategory full-content zip files.
- Subcategory markdown-only zip files.
- Category combined markdown files.
- Category context-commentary combined markdown files.
- Category full-content zip files.
- Category markdown-only zip files.
- Root-level metadata/list/summary files.
- Root-level full-content archive zip files.
- Root-level markdown-only full archive zip files.

What this layer does not do:
- S3 zip upload.
- Embed sync.
- Webflow CMS live sync.
- Change-log orchestration in the refresh update-record style.


## Files Touched By `update_all_archive()`
These are the important local file groups touched by the archive-rollup build layer.

Directly touched or regenerated on disk:
- CMS-eligible and non-CMS archive source markdown files whose metadata fields are refreshed by `update_metadata_words_tokens()`.
- Subcategory combined markdown files: `data/floodlamp/<category>/<subcategory>/_archive-combined-files_<subcategory>_*.md`
- Subcategory full-content zips: `data/floodlamp/<category>/<subcategory>/_zip_floodlamp-archive-<category>-<subcategory>.zip`
- Subcategory markdown-only zips: `data/floodlamp/<category>/<subcategory>/_zip-md_floodlamp-archive-<category>-<subcategory>.zip`
- Category combined markdown files: `data/floodlamp/<category>/_archive-combined-files_<category>_*.md`
- Category context-commentary combined markdown files: `data/floodlamp/<category>/_archive-combined-context-commentary_<category>*.md`
- Category full-content zips: `data/floodlamp/<category>/_zip_floodlamp-archive-<category>.zip`
- Category markdown-only zips: `data/floodlamp/<category>/_zip-md_floodlamp-archive-<category>.zip`
- Root metadata extract: `data/floodlamp/_exclude-from-archive/_metadata-extract.csv`
- Root file counts: `data/floodlamp/_exclude-from-archive/_file-counts.csv`
- Root archive file list: `data/floodlamp/_archive-file-list.md`
- Root archive file list headings-only: `data/floodlamp/_archive-file-list-headings-only.md`
- Root combined metadata summary: `data/floodlamp/_archive-combined-metadata_summary_short.md`
- Root full-content archive zip: `data/floodlamp/_zip_floodlamp-archive-all.zip`
- Root markdown-only full archive zip: `data/floodlamp/_zip-md_floodlamp-archive-all.zip`
- Root-level included folders in archive zips (defined in `ZIP_INCLUDE_ROOT_FOLDERS`): `_manuscript/` and `_prompts/`. All files from these folders are included in the full-content zip; only `.md` files are included in the markdown-only zip.
- FDA Town Halls special full-content zips when applicable: `data/floodlamp/regulatory/fda-townhalls/_zip_floodlamp-archive-regulatory-fda-townhalls-qa.zip` and `data/floodlamp/regulatory/fda-townhalls/_zip_floodlamp-archive-regulatory-fda-townhalls-transcripts.zip`

Operator note:
- Most of these files are exactly the files Randy has been manually checking and trusting on disk.
- Full-content zip changes will not appear in the source-control view because of the repo git-ignore rule for `_zip_*.zip`.


## Layer 2: CMS utility layer
This layer translates the local archive into CMS rows and can push those rows into Webflow.

Primary function:
- `create_and_import_floodlamp_cms()`

What it does:
- Scans CMS-eligible markdown files from the local archive.
- Builds one CMS row per CMS-eligible markdown file.
- Writes a CSV export.
- Imports that CSV into Webflow by slug.

What this layer does not do:
- It does not compare against archive rollup artifacts.
- It does not upload zips to S3.
- It does not sync embed files.
- It does not update the integrated archive view.
- It does not delete stale Webflow CMS items.

Best short description:
- CMS-only create/update sync from the current local archive state.


## Layer 3: Web publication prep orchestration
This layer is implemented in `floodlamp_refresh.py`.

It is trying to do all of the following in one workflow:
- Detect whether local archive rollup outputs are already up to date.
- Rebuild only the affected local rollup outputs if needed.
- Upload current zip artifacts to S3.
- Refresh local generated archive embed files from canonical web copy.
- Build local CMS snapshots and compare them against live Webflow CMS.
- Apply Webflow CMS deletes, creates, and updates.
- Update the integrated archive view.
- Write update-record logs.

This means `floodlamp_refresh.py` is not just "CMS refresh."
It is really the web publication prep orchestration layer.


## Files Touched By Refresh / Web Publication Prep
These are the important file groups touched by the refresh/web-prep layer after the archive-rollup decision has been made.

Always or commonly touched locally:
- Refresh-record folder under `data/floodlamp/_exclude-from-archive/changelogs-refresh/`
- Refresh-record top-level markdown log
- Refresh-record `source_manifest.csv`
- Refresh-record `cms_expected_full.csv`
- Refresh-record `cms_live_before_refresh.csv`
- Refresh-record `cms_operations_manifest.csv`
- Refresh-record `cms_delta_refresh.csv`
- Refresh-record `cms_delete_manifest.csv`
- Refresh-record `cms_live_current.csv` when CMS updates are applied
- Refresh-record artifact listing markdown files
- Integrated archive view: `data/floodlamp/_archive-integrated-view.md`
- Legacy compatibility file: `data/floodlamp/_propagation-ref.md`

Local website-prep files that may be rewritten during embed sync:
- `data/floodlamp/_exclude-from-archive/_code-floodlamp-archive/webcode/floodlamp_archive_*_embed.html`
- In current practice, this means the generated homepage/category embed HTML files in `webcode/`

Live/external targets touched by refresh:
- S3 zip objects under the FloodLAMP archive publish folder
- Live Webflow CMS items when CMS updates are approved

Conditional local overlap with archive-rollup build:
- If you answer `yes` to `Run floodlamp_archive_ops.update_all_archive?`, it also touches the archive-rollup files listed in the `update_all_archive()` section above.
- If you answer `no` to that prompt, it should leave those archive-rollup files alone and proceed by trusting the current local rollup state after a quick existence check.


## As-Built Entry Points
### `update_all_archive()`
Best current description:
- Full local archive rollup rebuild.

Use it when:
- You want to regenerate archive rollups on disk.
- You want to inspect combined files and zips directly.
- You want to trust the archive build layer before doing any web-facing work.


## `create_and_import_floodlamp_cms()`
Best current description:
- CMS-only create/update push to Webflow from current local state.

Use it when:
- You want a standalone CMS sync.
- You do not need stale-item deletes.
- You do not need S3 upload, embed sync, or integrated-view updates as part of the same run.


## `run_floodlamp_refresh_status()`
Best current description:
- Temp-copy comparison check for publication-target outputs and local CMS snapshots.

Use it when:
- You want to see whether current local rollup outputs differ from what a fresh rebuild would produce.
- You want a status/check report without applying local refresh stages.

Important note:
- This rebuild happens in a temp copy for comparison purposes.
- It does not change the real archive on disk.


## `run_floodlamp_refresh_changed_only()`
Best current description:
- Changed-only refresh workflow with an explicit archive-rollup decision prompt.

What it does:
- Prompts: `Run floodlamp_archive_ops.update_all_archive?`
- If you answer `yes`, it runs `update_all_archive()` directly.
- If you answer `no`, it runs a quick trust check that verifies the expected archive-rollup files exist.
- Prompts separately whether to do Amazon S3 zip uploads.
- Prompt text: `Run Amazon S3 zip upload?`
- If approved, uploads current full-content and markdown-only zip artifacts to S3.
- Prompts separately whether to refresh local archive embeds.
- Prompt text: `Run local archive embed refresh?`
- If approved, refreshes local generated archive embeds from canonical web copy.
- Builds the expected CMS snapshot from current local state.
- Compares that snapshot to live Webflow CMS.
- Applies Webflow CMS deletes/create/update.
- Updates the integrated archive view.
- Writes an update log.

Important limit of the `no` / trust-current-rollups path:
- The quick trust check is intentionally fast.
- It checks that the expected archive-rollup files are present.
- It does not compare current file contents against a temp rebuilt expected state.

Backward-compatible alias:
- `run_floodlamp_update_changed_only()` now delegates to `run_floodlamp_refresh_changed_only()`


## `run_floodlamp_rebuild_everything()`
Best current description:
- Full rebuild plus downstream web publication prep.

What it does:
- Rebuilds the full local archive publication outputs.
- Uploads zips to S3.
- Syncs embeds.
- Builds the CMS delta against live Webflow.
- Updates the integrated archive view.
- Applies CMS updates if you approve them.

This is the closest current top-level function to:
- "do the local rebuild and then do the downstream web prep in one run."


## Embed Update And Manual Webflow Handoff
When the website-facing archive embeds or archive item template JS change, there is an important distinction between local regeneration and manual Webflow publication.

- `floodlamp_archive_item_template.js` is a direct website-presentation file and must be pasted into the archive item template page custom code manually when it changes.
- The homepage/category embed HTML files are generated from `webcode/floodlamp_archive_md_to_embed.py`.
- For a local-only embed regeneration pass without a manual pause, it is acceptable to call `update_local_embeds_from_web_copy()` directly from Python import context.
- That direct local-regeneration path is what was used for the 2026-03-27 homepage/category zip-link move and layout tweak.
- `update_floodlamp_embeds_then_prompt_and_compare()` is the guided operator flow when you want all three stages in one run: regenerate local embed files, pause for manual Webflow paste/publish, then compare local embed content against the live public pages.
- `update_local_embeds_from_web_copy()` is now the single non-interactive local rewrite helper for generated archive embeds.
- `floodlamp_refresh.py` now imports the embed module and calls `update_local_embeds_from_web_copy()` directly during its downstream local-embed refresh stage.

After local embed generation is complete, the manual Webflow side is:
- paste the updated `floodlamp_archive_item_template.js` into the archive item template page custom code when that JS file changed
- paste the refreshed embed HTML into the `Home` page and the four category pages when those generated embed files changed
- publish in Webflow
- if you used the guided compare flow, let `update_floodlamp_embeds_then_prompt_and_compare()` continue into its final local-vs-live comparison step after publishing


## Current As-Built Behavior
The main 2026-03-27 design change is:
- `run_floodlamp_refresh_changed_only()` no longer relies on the old temp-copy status gate before the downstream refresh steps.
- Instead, it makes the archive-rollup decision explicit with a prompt.
- This removes the earlier problem where the changed-only refresh could stop early after a prior `update_all_archive()` run.

Current operator model:
- If the archive rollups need to be refreshed, answer `yes` and let refresh call `update_all_archive()` directly.
- If the archive rollups are already trusted and checked, answer `no` and let refresh proceed after the quick existence check.


## What Is Preserved After `update_all_archive()`
If you have already run `update_all_archive()` successfully and checked the files on disk, then these local results are already in place:
- Refreshed subcategory outputs.
- Refreshed category outputs.
- Refreshed root-level archive outputs.
- Current local combined files and zips that you have manually verified.

What the new refresh flow does with that:
- `run_floodlamp_refresh_changed_only()` can now be used as the downstream continuation workflow.
- Answer `no` to `Run floodlamp_archive_ops.update_all_archive?` if you want to trust the current verified rollups and continue into S3 upload, embed sync, integrated view update, and CMS live sync.
- The quick trust check is intentionally only a fast existence check, not a semantic content comparison.


## Current Operator-Safe Conclusion
As of now, the workflows divide like this:
- Use `update_all_archive()` when the job is local archive rollups.
- Use `create_and_import_floodlamp_cms()` when the job is CMS-only create/update.
- Use `run_floodlamp_refresh_changed_only()` when the job is downstream refresh/web publication prep, with the option to either run `update_all_archive()` first or decline it and trust the current verified rollups after a quick existence check.
- Use `run_floodlamp_rebuild_everything()` when the job is a more explicit full rebuild plus downstream web publication prep in one flow.
- Keep using source control as a core verification tool for markdown-visible changes, but remember that full-content zip changes are intentionally hidden from that view by git-ignore rules.


## Suggested Future Naming
These names are not yet implemented in code. They are terminology suggestions for clarity.

Possible high-level vocabulary:
- Archive build / rollups.
- Web publication prep.
- Website presentation.

Current naming choice adopted on 2026-03-27:
- Keep `update_all_archive()` as the archive-rollup rebuild name.
- Rename the main refresh workflow to `run_floodlamp_refresh_changed_only()`.
- Keep `run_floodlamp_update_changed_only()` as a backward-compatible alias while transition notes and docs catch up.

The goal of the naming should be:
- make it obvious which functions rebuild local archive rollups,
- which functions prepare downstream web publication,
- and which functions touch live Webflow or website-facing assets.


## New-Person Orientation
If someone new joins this work, the clean mental model is:
- The archive source files are the core product.
- The archive rollups are convenience/generated artifacts for AI use and download.
- The CMS layer turns selected archive markdown files into structured rows for Webflow.
- The refresh/orchestration layer tries to connect the archive outputs to the published web-facing state.
- The website layer uses CMS data, embed files, and custom front-end code to present the archive on the site.

So the flow is broadly:
- source files -> archive rollups -> web publication prep -> website presentation

But the current codebase mixes some of those boundaries:
- `floodlamp_refresh.py` spans both local-output checking and downstream web publication prep.
- `floodlamp_archive_ops.py` remains the cleanest place for archive build logic.


## Notes For Runbook Deprecation
The older `floodlamp_refresh_runbook.md` should remain as a historical/testing runbook for now, but this document should become the primary reference for:
- terminology,
- workflow boundaries,
- module relationships,
- and operator decision-making.
<!-- ===== END OF FILE floodlamp_publication_workflow.md ===== -->
