Canonical public web-copy source for the FloodLAMP archive site.
last updated: 3-14 1335

# Overview
- Each top-level heading maps to one Webflow page.
- Shared page metadata fields used on every page: `webflow_page_name`, `webflow_slug`, `nav_label`, `page_title`, `page_type`, `copy_status`, `html_embed_pattern`, and `notes`.
- Shared subcategory fields used on category pages: `anchor`, `label`, `archive_path`, `commentary_file`, and `browse_summary_status`.
- Shared optional media slots that may be noted here without making Webflow canonical for text: `lead_media`, `inline_media`, `callout_media`, and `download_media`.
- Current use: structural source for Milestone 8. Draft copy comes in Milestone 9.
- Current companion outputs: first-pass Webflow embed files now exist in `data/floodlamp/_exclude-from-archive/_code-floodlamp-archive/webcode/`.
- `shared_toc_title`: `On this page`
- `shared_commentary_link_label`: `Open the fuller context and commentary`

# Setup
## FloodLAMP Archive Static Pages Setup
Use these files for the five archive browsing pages:

- `floodlamp_archive_home_archive_embed.html`
- `floodlamp_archive_cat_guides_embed.html`
- `floodlamp_archive_cat_pilots_embed.html`
- `floodlamp_archive_cat_regulatory_embed.html`
- `floodlamp_archive_cat_various_embed.html`

The shared CSS for these pages lives in:

- `floodlamp_archive_site_head.html`


## Recommended Webflow Structure
For each page, keep the structure minimal:

- navbar
- one main section
- one container
- one `HTML Embed`
- footer

Paste the matching page embed file into that page's single `HTML Embed`.


## Shared CSS
The page embeds expect the styles in `floodlamp_archive_site_head.html`.

If that file is already deployed to the site head for the archive item template, replace the site-head code with the current version so the homepage/category-page classes are available too.


## Current Homepage Handling
`Home-Archive` is the working archive homepage page.

Because Webflow's special root homepage remains separate, treat `Home-Archive` as the buildout target first.
Once the archive homepage is ready and approved, either:

- copy the same homepage embed into the special root homepage page, or
- switch the root page over in whatever final way you decide inside Webflow

Do not assume that a duplicated static page automatically becomes `/`.


# Page: home-archive 
## Page Metadata
- `webflow_page_name`: `Home-Archive`
- `webflow_slug`: `home-archive`
- `nav_label`: `Home`
- `page_title`: `FloodLAMP Archive`
- `hero_eyebrow`: `FloodLAMP archive`
- `hero_title`: `The FloodLAMP Archive`
- `page_type`: `homepage`
- `copy_status`: `v2 in companion embed file`
- `html_embed_pattern`: `single HTML embed inside the main page container`
- `notes`: `This is the working archive homepage page. In Webflow, the special root Home page still needs separate handling if floodlamp.bio should land on this content.`


## Content Blocks
### Hero / Page Intro
- `anchor`: `top`
- `purpose`: `Give a short orientation to FloodLAMP, the archive, and what a visitor can do here.`
- `copy_note`: `Keep concise and practical. This is an explanatory landing page, not a startup-style marketing hero.`
- `callout_text`: `This archive of approximately 200 primary files has been prepared in "AI-ready" form. The intention is for the user to download all or portions of the archive and then utilize the zip and combined markdown files with their AI tool of choice.`

FloodLAMP Biotechnologies was a small public-benefit company that developed and deployed decentralized molecular COVID-19 testing during the pandemic.

This page is a guide to the public archive: what it contains, how it is organized, and how to use it effectively.

### What FloodLAMP Is
- `anchor`: `what-floodlamp-is`
- `purpose`: `Briefly explain FloodLAMP as a pandemic-era open-source/public-benefit testing effort.`
- `copy_note`: `Explain the organization at a high level without retelling the full company history.`

FloodLAMP was a pandemic-era effort to build low-cost, decentralized molecular COVID-19 testing based on RT-LAMP and related workflows.

The work spanned assay development, validation documents, pilot deployments, software, operations, regulatory submissions, and broader thinking about open-access diagnostics.

The archive preserves both the technical materials and the surrounding context: what was built, how it was used, what worked in practice, and what broader lessons emerged from the effort.

### What This Archive Is
- `anchor`: `what-this-archive-is`
- `purpose`: `Explain what is in the archive and what the website adds.`
- `copy_note`: `Clarify that the site is a browsing/orientation layer around the archive, not the archive itself.`

This archive is a curated public release of documents from FloodLAMP's operating period and its closeout work.

It includes original working files, converted markdown versions, combined commentary files, pilot data materials, regulatory documents, whitepapers, presentations, and related reference material.

The archive is organized into four top-level categories: Guides, Pilots, Regulatory, and Various. Those categories are the main navigation structure for this site.

### How To Use This Archive With AI
- `anchor`: `use-with-ai`
- `purpose`: `Tell users how to use the markdown corpus, combined files, and commentary with AI tools.`
- `copy_note`: `Focus on practical usage patterns rather than AI hype.`

Most of the archive has been prepared in markdown specifically so it can be searched, summarized, compared, and synthesized with AI tools.

A good workflow is to start with one category or subcategory, describe your background and what you want to learn, and then give an AI system the most relevant files or combined markdown bundles.

- Use the category pages on this site to identify the most relevant subcategories.
- Use the linked context/commentary files when you want a curated orientation before reading raw documents.
- Use combined markdown files or zip bundles when you want a larger corpus for AI-assisted synthesis.
- Use the GitHub repository when you want direct access to the underlying archive structure and files.

### Archive Index
- `anchor`: `archive-index`
- `purpose`: `Provide a category and subcategory map with direct links into category-page anchors.`
- `copy_note`: `This is the structural navigation map for the full archive website.`

### System Prompt
- `anchor`: `system-prompt`
- `purpose`: `Provide a direct link to the full archive system prompt for use with AI tools.`
- `placement`: `Inside the hero callout box, above the archive zip download link.`
- `link_href`: `https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/FLOODLAMP_ARCHIVE_SYSTEM_PROMPT.md`
- `link_label`: `Use the full archive system prompt`
- `link_external`: `true`

### Manuscript
- `anchor`: `manuscript`
- `purpose`: `Provide access to the peer-reviewed manuscript that synthesizes the full body of work.`
- `placement`: `Callout box between the hero section and the What FloodLAMP Is section.`
- `manuscript_title`: `Operational outcomes from 11 decentralized RT-LAMP COVID-19 surveillance programs in 6 U.S. states, 2020–2023`
- `archive_path`: `_manuscript/floodlamp-manuscript-with-proposals`

The manuscript synthesizes the full body of work into a single peer-reviewed paper (submitted), including regulatory reform proposals found only in the manuscript.

### Downloads And Bulk Access
- `anchor`: `downloads`
- `purpose`: `Explain how to use combined markdown files, zip bundles, GitHub, and Google-hosted files where relevant.`
- `copy_note`: `Reserve room for bulk-download and machine-readable index links if surfaced later.`

If you want to browse individual materials, the category pages and linked commentary files are the best starting point.

If you want to work with the complete archive, the GitHub repository, combined markdown files, and zip bundles are the better access paths.


## Archive Index Map
### Guides
- `category_page`: `/cat-guides`
- `category_label`: `Guides`
- `card_link_label`: `Open Guides`
- `subcategory_links`: `/cat-guides#manufacturing`, `/cat-guides#operations`, `/cat-guides#qms-sops`, `/cat-guides#sds`, `/cat-guides#software`, `/cat-guides#test-site`, `/cat-guides#test-training`, `/cat-guides#test-validation`

Practical materials for manufacturing, validation, training, site operations, software, safety, and quality systems.

### Pilots
- `category_page`: `/cat-pilots`
- `category_label`: `Pilots`
- `card_link_label`: `Open Pilots`
- `subcategory_links`: `/cat-pilots#pilot-data`, `/cat-pilots#pilot-sites`

Real-world deployment records, pilot data, program comparisons, and case-oriented operational lessons.

### Regulatory
- `category_page`: `/cat-regulatory`
- `category_label`: `Regulatory`
- `card_link_label`: `Open Regulatory`
- `subcategory_links`: `/cat-regulatory#fda-euas`, `/cat-regulatory#fda-policy`, `/cat-regulatory#fda-townhalls`, `/cat-regulatory#fl-fda-submissions`, `/cat-regulatory#fl-fda-correspondence`, `/cat-regulatory#irb`, `/cat-regulatory#ldts`, `/cat-regulatory#open-euas`, `/cat-regulatory#reg-articles-misc`, `/cat-regulatory#surveillance`

FloodLAMP's FDA submissions and correspondence, surveillance framing, FDA policy materials, IRB documents, and related analysis.

### Various
- `category_page`: `/cat-various`
- `category_label`: `Various`
- `card_link_label`: `Open Various`
- `subcategory_links`: `/cat-various#external-programs-reports`, `/cat-various#fl-patent`, `/cat-various#fl-presentations`, `/cat-various#fl-proposals`, `/cat-various#fl-whitepapers`, `/cat-various#glamp`, `/cat-various#lamp-tech`, `/cat-various#papers`, `/cat-various#papers-lamp`, `/cat-various#xprize`

Whitepapers, proposals, presentations, literature, gLAMP, XPRIZE materials, and other adjacent archive context.


## Download Cards
### GitHub Repository
- `title`: `GitHub repository`
- `link_href`: `https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive`
- `link_label`: `Open the repository`
- `link_external`: `true`

Use the public repository for direct file access, archive browsing, and stable links into the markdown corpus.

### Combined Markdown And Zip Bundles
- `title`: `Combined markdown and zip bundles`

These are especially useful when you want to load a larger slice of the archive into an AI tool for synthesis, comparison, or targeted research.

Additional combined-file and bulk-download links can be added here as the homepage is refined.


## Media Notes
- `lead_media`: `Optional FloodLAMP photo, archival image, or simple visual marker if one is actually helpful.`
- `inline_media`: `Optional site diagram or archive-structure graphic near the archive-introduction sections.`
- `callout_media`: `Optional simple visual callout for AI-use guidance or download guidance.`
- `download_media`: `Optional icon-style support media for GitHub, zip, or combined-markdown access cards.`

# Page: cat-guides
## Page Metadata
- `webflow_page_name`: `cat-guides`
- `webflow_slug`: `cat-guides`
- `nav_label`: `Guides`
- `page_title`: `FloodLAMP Archive - Guides`
- `hero_eyebrow`: `FloodLAMP archive category`
- `hero_title`: `Guides`
- `page_type`: `category`
- `copy_status`: `draft v1 in companion embed file`
- `html_embed_pattern`: `single HTML embed inside the main page container`
- `notes`: `Use one lead intro, one in-page table of contents, then one section per subcategory.`


## Content Blocks
### Lead / Category Intro
- `purpose`: `Explain that Guides contains practical operating, training, safety, software, and validation materials.`

The Guides category contains the practical operating materials from FloodLAMP's testing work:

manufacturing documents, validation guides, training materials, site operations documents, software guides, safety references, and quality-system SOPs.

### In-Page Table Of Contents
- `toc_links`: `#manufacturing`, `#operations`, `#qms-sops`, `#sds`, `#software`, `#test-site`, `#test-training`, `#test-validation`

### Subcategory Sections
- `pattern`: `short heading, short web-browsing description, link to fuller context/commentary file`


## Subcategories
### Manufacturing
- `anchor`: `manufacturing`
- `label`: `Manufacturing`
- `archive_path`: `guides/manufacturing`
- `commentary_file`: `data/floodlamp/guides/manufacturing/_context-commentary_guides-manufacturing.md`
- `browse_summary_status`: `draft pending`

SOPs and diagrams for FloodLAMP's most mature reagent-production workflows, especially PGS48 and 100X Inactivation Solution, along with verification procedures for those batches.

### Operations
- `anchor`: `operations`
- `label`: `Operations`
- `archive_path`: `guides/operations`
- `commentary_file`: `data/floodlamp/guides/operations/_context-commentary_guides-operations.md`
- `browse_summary_status`: `draft pending`

Higher-level operating materials on cost modeling, inventory, primer ordering, and the logistical realities of building and supporting a decentralized testing system.

### QMS And SOPs
- `anchor`: `qms-sops`
- `label`: `QMS and SOPs`
- `archive_path`: `guides/qms-sops`
- `commentary_file`: `data/floodlamp/guides/qms-sops/_context-commentary_guides-qms-sops.md`
- `browse_summary_status`: `draft pending`

FloodLAMP's formal quality-system and run-form documents for reagent prep, amplification, shipping, training, and operational traceability at test sites.

### Safety Data Sheets
- `anchor`: `sds`
- `label`: `Safety Data Sheets`
- `archive_path`: `guides/sds`
- `commentary_file`: `data/floodlamp/guides/sds/_context-commentary_guides-sds.md`
- `browse_summary_status`: `draft pending`

Safety Data Sheets for key chemicals used in the workflow, plus archive-preparation analysis on waste disposal, hazard questions, and related risk assessment.

### Software
- `anchor`: `software`
- `label`: `Software`
- `archive_path`: `guides/software`
- `commentary_file`: `data/floodlamp/guides/software/_context-commentary_guides-software.md`
- `browse_summary_status`: `draft pending`

Guides to the FloodLAMP mobile app and admin web portal, including the user flows that supported registration, collection, accessioning, and resulting.

### Test Site Operations
- `anchor`: `test-site`
- `label`: `Test Site Operations`
- `archive_path`: `guides/test-site`
- `commentary_file`: `data/floodlamp/guides/test-site/_context-commentary_guides-test-site.md`
- `browse_summary_status`: `draft pending`

Site-facing operational documents covering setup, logistics, collection workflows, resulting logic, communications, and day-to-day deployment practices.

### Test Training
- `anchor`: `test-training`
- `label`: `Test Training`
- `archive_path`: `guides/test-training`
- `commentary_file`: `data/floodlamp/guides/test-training/_context-commentary_guides-test-training.md`
- `browse_summary_status`: `draft pending`

Video-based training materials, transcripts, and certification guidance created to teach the testing workflow to new operators, including non-laboratory staff.

### Test Validation
- `anchor`: `test-validation`
- `label`: `Test Validation`
- `archive_path`: `guides/test-validation`
- `commentary_file`: `data/floodlamp/guides/test-validation/_context-commentary_guides-test-validation.md`
- `browse_summary_status`: `draft pending`

Some of the most formal and self-contained technical documents in the archive, including the validation guides used to transfer the assay into external lab settings.


## Media Notes
- `lead_media`: `Optional single manufacturing, workflow, or testing-site image if it helps orient the page.`
- `inline_media`: `Optional subcategory-specific images such as diagrams or signage references.`
- `callout_media`: `Optional visual cue near training or safety sections if used consistently.`

# Page: cat-pilots
## Page Metadata
- `webflow_page_name`: `cat-pilots`
- `webflow_slug`: `cat-pilots`
- `nav_label`: `Pilots`
- `page_title`: `FloodLAMP Archive - Pilots`
- `hero_eyebrow`: `FloodLAMP archive category`
- `hero_title`: `Pilots`
- `page_type`: `category`
- `copy_status`: `draft v1 in companion embed file`
- `html_embed_pattern`: `single HTML embed inside the main page container`
- `notes`: `Two subcategories: pilot-data for quantitative summaries, pilot-sites for site-level case studies.`


## Content Blocks
### Lead / Category Intro
- `purpose`: `Explain that Pilots contains the real-world deployment record, pilot data, and case-oriented program context.`

The Pilots category documents how FloodLAMP's testing system was actually used in the field:

the deployment record, pilot data, case studies, operational comparisons, and lessons from real-world programs.

### In-Page Table Of Contents
- `toc_links`: `#pilot-data`, `#pilot-sites`

### Subcategory Sections
- `pattern`: `short heading, short web-browsing description, link to fuller context/commentary file`


## Subcategories
### Pilot Programs And Data
- `anchor`: `pilot-data`
- `label`: `Pilot Programs and Data`
- `archive_path`: `pilots/pilot-data`
- `commentary_file`: `data/floodlamp/pilots/pilot-data/_context-commentary_pilots-pilot-data.md`
- `browse_summary_status`: `draft pending`
- `related_context_file`: `data/floodlamp/pilots/pilot-data/_context-commentary_pilot-data_data-processing.md`

This subcategory covers the 11 pilot programs FloodLAMP ran or supported across schools, EMS departments, municipal programs, conferences, and internal/company settings.

It includes aggregated pilot context, program-specific commentary, data-processing notes, and detailed comparisons between FloodLAMP molecular testing and rapid antigen tests.

If you want the clearest picture of what FloodLAMP accomplished in practice, this is one of the most important parts of the archive.

### Pilot Sites
- `anchor`: `pilot-sites`
- `label`: `Pilot Sites`
- `archive_path`: `pilots/pilot-sites`
- `commentary_file`: `data/floodlamp/pilots/pilot-sites/_context-commentary_pilots-pilot-sites.md`
- `browse_summary_status`: `draft pending`

Site-level pilot program descriptions, case studies, and qualitative implementation context for the FloodLAMP deployments, covering the operational and human dimensions of each program.


## Media Notes
- `lead_media`: `Optional simple map, program count, or pilot timeline graphic if later useful.`
- `inline_media`: `Optional case-study or pilot-summary image slots if these genuinely improve browsing.`

# Page: cat-regulatory
## Page Metadata
- `webflow_page_name`: `cat-regulatory`
- `webflow_slug`: `cat-regulatory`
- `nav_label`: `Regulatory`
- `page_title`: `FloodLAMP Archive - Regulatory`
- `hero_eyebrow`: `FloodLAMP archive category`
- `hero_title`: `Regulatory`
- `page_type`: `category`
- `copy_status`: `draft v1 in companion embed file`
- `html_embed_pattern`: `single HTML embed inside the main page container`
- `notes`: `This page will likely be one of the densest; keep summaries short and use the commentary links to handle depth.`


## Content Blocks
### Lead / Category Intro
- `purpose`: `Explain that Regulatory contains FDA policy, FloodLAMP's submissions and correspondence, surveillance framing, IRB materials, and related analysis.`

The Regulatory category covers the policy and regulatory environment around COVID-19 testing, including FloodLAMP's own FDA submissions and correspondence, the surveillance framework it operated under, and related commentary on open-access diagnostics and pandemic preparedness.

### In-Page Table Of Contents
- `toc_links`: `#fda-euas`, `#fda-policy`, `#fda-townhalls`, `#fl-fda-submissions`, `#fl-fda-correspondence`, `#irb`, `#ldts`, `#open-euas`, `#reg-articles-misc`, `#surveillance`

### Subcategory Sections
- `pattern`: `short heading, short web-browsing description, link to fuller context/commentary file`


## Subcategories
### Selected FDA EUA Documents
- `anchor`: `fda-euas`
- `label`: `Selected FDA EUA Documents`
- `archive_path`: `regulatory/fda-euas`
- `commentary_file`: `data/floodlamp/regulatory/fda-euas/_context-commentary_regulatory-fda-euas.md`
- `browse_summary_status`: `draft pending`

A reference set of EUA documents FloodLAMP studied during development, including comparable authorized tests and instructive examples of the FDA's authorization model.

### FDA Policy
- `anchor`: `fda-policy`
- `label`: `FDA Policy`
- `archive_path`: `regulatory/fda-policy`
- `commentary_file`: `data/floodlamp/regulatory/fda-policy/_context-commentary_regulatory-fda-policy.md`
- `browse_summary_status`: `draft pending`

The evolving FDA policy framework for COVID-19 testing, including guidance versions, templates, screening policy, pooling policy, and transition-era materials.

### FDA Town Halls
- `anchor`: `fda-townhalls`
- `label`: `FDA Town Halls`
- `archive_path`: `regulatory/fda-townhalls`
- `commentary_file`: `data/floodlamp/regulatory/fda-townhalls/_context-commentary_regulatory-fda-townhalls.md`
- `browse_summary_status`: `draft pending`

Processed transcripts from approximately 100 FDA Virtual Town Hall meetings for COVID-19 diagnostic test developers, spanning 2020 through early 2023, including structured question-and-answer extractions and analysis.

### FloodLAMP FDA Submissions
- `anchor`: `fl-fda-submissions`
- `label`: `FloodLAMP FDA Submissions`
- `archive_path`: `regulatory/fl-fda-submissions`
- `commentary_file`: `data/floodlamp/regulatory/fl-fda-submissions/_context-commentary_regulatory-fl-fda-submissions.md`
- `browse_summary_status`: `draft pending`

FloodLAMP's own EUA submissions and Instructions for Use documents, including for the primary test utilized in FloodLAMP's real-world pilot programs ("QuickColor" extraction-free colorimetric LAMP test) and for a companion "EasyPCR" test run from the same inactivated sample and utilizing the SalivaDirect primers and probes. Also addressed is the broader open-source protocol regulatory strategy.

### FloodLAMP FDA Correspondence
- `anchor`: `fl-fda-correspondence`
- `label`: `FloodLAMP FDA Correspondence`
- `archive_path`: `regulatory/fl-fda-correspondence`
- `commentary_file`: `data/floodlamp/regulatory/fl-fda-correspondence/_context-commentary_regulatory-fl-fda-correspondence.md`
- `browse_summary_status`: `draft pending`

The direct written record of FloodLAMP's interactions with the FDA, including pre-EUA contacts, review communications, deficiency letters, and closure of the submission effort.

### IRB And Clinical Study Materials
- `anchor`: `irb`
- `label`: `IRB and Clinical Study Materials`
- `archive_path`: `regulatory/irb`
- `commentary_file`: `data/floodlamp/regulatory/irb/_context-commentary_regulatory-irb.md`
- `browse_summary_status`: `draft pending`

Protocol and consent materials for the clinical-study path FloodLAMP prepared but never carried through, plus commentary on the cost and friction of the process.

### Laboratory-Developed Tests
- `anchor`: `ldts`
- `label`: `Laboratory-Developed Tests`
- `archive_path`: `regulatory/ldts`
- `commentary_file`: `data/floodlamp/regulatory/ldts/_context-commentary_regulatory-ldts.md`
- `browse_summary_status`: `draft pending`

Background on the LDT regulatory pathway and how it intersected with FDA policy, commercial IVDs, and the open-EUA ideas that mattered to FloodLAMP.

### Open EUAs
- `anchor`: `open-euas`
- `label`: `Open EUAs`
- `archive_path`: `regulatory/open-euas`
- `commentary_file`: `data/floodlamp/regulatory/open-euas/_context-commentary_regulatory-open-euas.md`
- `browse_summary_status`: `draft pending`

Materials on the open-EUA concept that sat at the center of FloodLAMP's regulatory strategy: open protocols, open supply chains, and shared access to authorization.

### Regulatory Articles And Reports
- `anchor`: `reg-articles-misc`
- `label`: `Regulatory Articles and Reports`
- `archive_path`: `regulatory/reg-articles-misc`
- `commentary_file`: `data/floodlamp/regulatory/reg-articles-misc/_context-commentary_regulatory-reg-articles-misc.md`
- `browse_summary_status`: `draft pending`

Broader third-party reports, proposals, and retrospective analyses that help place FloodLAMP's regulatory experience in a larger pandemic-policy context.

### Surveillance Testing
- `anchor`: `surveillance`
- `label`: `Surveillance Testing`
- `archive_path`: `regulatory/surveillance`
- `commentary_file`: `data/floodlamp/regulatory/surveillance/_context-commentary_regulatory-surveillance.md`
- `browse_summary_status`: `draft pending`

The regulatory gray-zone framework FloodLAMP ultimately operated under in practice, including how non-diagnostic surveillance was explained, justified, and limited.


## Media Notes
- `lead_media`: `Optional simple regulatory timeline or process visual if it reduces confusion.`
- `inline_media`: `Optional selective document thumbnails only where they help orientation.`
- `callout_media`: `Optional callout visual for the open-EUA idea or surveillance-vs-screening distinction.`

# Page: cat-various
## Page Metadata
- `webflow_page_name`: `cat-various`
- `webflow_slug`: `cat-various`
- `nav_label`: `Various`
- `page_title`: `FloodLAMP Archive - Various`
- `hero_eyebrow`: `FloodLAMP archive category`
- `hero_title`: `Various`
- `page_type`: `category`
- `copy_status`: `draft v1 in companion embed file`
- `html_embed_pattern`: `single HTML embed inside the main page container`
- `notes`: `Use cleaner labels where helpful, but keep the archive paths and anchors stable.`


## Content Blocks
### Lead / Category Intro
- `purpose`: `Explain that Various holds adjacent materials that support the archive: presentations, proposals, papers, external reports, XPRIZE, gLAMP, patent materials, and related context.`

The Various category holds supporting materials that do not fit cleanly into the other top-level groups:

presentations, proposals, whitepapers, scientific literature, gLAMP and XPRIZE materials, external reports, and related contextual documents.

### In-Page Table Of Contents
- `toc_links`: `#external-programs-reports`, `#fl-patent`, `#fl-presentations`, `#fl-proposals`, `#fl-whitepapers`, `#glamp`, `#lamp-tech`, `#papers`, `#papers-lamp`, `#xprize`

### Subcategory Sections
- `pattern`: `short heading, short web-browsing description, link to fuller context/commentary file`


## Subcategories
### External Program Reports
- `anchor`: `external-programs-reports`
- `label`: `External Program Reports`
- `archive_path`: `various/external-programs-reports`
- `commentary_file`: `data/floodlamp/various/external-programs-reports/_context-commentary_various-external-programs-reports.md`
- `browse_summary_status`: `draft pending`

A curated set of outside reports and reference materials on pandemic testing programs, especially K-12 school screening and related operational models.

### FloodLAMP Patent
- `anchor`: `fl-patent`
- `label`: `FloodLAMP Patent`
- `archive_path`: `various/fl-patent`
- `commentary_file`: `data/floodlamp/various/fl-patent/_context-commentary_various-fl-patent.md`
- `browse_summary_status`: `draft pending`

The abandoned FloodLAMP patent application on decentralized testing hardware, preserved as a public-domain exploration of the design space rather than a finalized product blueprint.

### FloodLAMP Presentations
- `anchor`: `fl-presentations`
- `label`: `FloodLAMP Presentations`
- `archive_path`: `various/fl-presentations`
- `commentary_file`: `data/floodlamp/various/fl-presentations/_context-commentary_various-fl-presentations.md`
- `browse_summary_status`: `draft pending`

Slide decks and summary materials used to explain FloodLAMP to audiences including BARDA, NEB, EMS leaders, and FDA-adjacent groups.

### FloodLAMP Proposals
- `anchor`: `fl-proposals`
- `label`: `FloodLAMP Proposals`
- `archive_path`: `various/fl-proposals`
- `commentary_file`: `data/floodlamp/various/fl-proposals/_context-commentary_various-fl-proposals.md`
- `browse_summary_status`: `draft pending`

Funding and partnership proposals spanning RADx, Balvi, and Florida EMS expansion, showing how FloodLAMP's strategy evolved over time.

### FloodLAMP Whitepapers
- `anchor`: `fl-whitepapers`
- `label`: `FloodLAMP Whitepapers`
- `archive_path`: `various/fl-whitepapers`
- `commentary_file`: `data/floodlamp/various/fl-whitepapers/_context-commentary_various-fl-whitepapers.md`
- `browse_summary_status`: `draft pending`

FloodLAMP's whitepaper-style program writeups, especially the California preschool family pooled-screening document and the unfinished EMS draft.

### gLAMP
- `anchor`: `glamp`
- `label`: `gLAMP`
- `archive_path`: `various/glamp`
- `commentary_file`: `data/floodlamp/various/glamp/_context-commentary_various-glamp.md`
- `browse_summary_status`: `draft pending`

Materials related to the Global LAMP Consortium, the pre-competitive community around open sharing of LAMP methods, diagnostics experience, and pandemic testing ideas.

### LAMP Technology
- `anchor`: `lamp-tech`
- `label`: `LAMP Technology`
- `archive_path`: `various/lamp-tech`
- `commentary_file`: `data/floodlamp/various/lamp-tech/_context-commentary_various-lamp-tech.md`
- `browse_summary_status`: `draft pending`

Practical background material on the underlying LAMP assay technology FloodLAMP built on, distinct from the broader scientific literature section.

### Papers
- `anchor`: `papers`
- `label`: `Papers`
- `archive_path`: `various/papers`
- `commentary_file`: `data/floodlamp/various/papers/_context-commentary_various-papers.md`
- `browse_summary_status`: `draft pending`

A broader collection of pandemic-testing literature that informed or contextualized FloodLAMP's work, beyond the specifically LAMP-focused papers.

### LAMP Papers
- `anchor`: `papers-lamp`
- `label`: `LAMP Papers`
- `archive_path`: `various/papers-lamp`
- `commentary_file`: `data/floodlamp/various/papers-lamp/_context-commentary_various-papers-lamp.md`
- `browse_summary_status`: `draft pending`

A curated selection of RT-LAMP papers directly relevant to the scientific and technical background of FloodLAMP's assay work.

### XPRIZE
- `anchor`: `xprize`
- `label`: `XPRIZE`
- `archive_path`: `various/xprize`
- `commentary_file`: `data/floodlamp/various/xprize/_context-commentary_various-xprize.md`
- `browse_summary_status`: `draft pending`

FloodLAMP's materials from the XPRIZE Rapid Covid Testing competition, along with commentary on the competition model and its relationship to open-source testing efforts.


## Media Notes
- `lead_media`: `Optional one-image or one-graphic treatment only if it helps unify this broad category.`
- `inline_media`: `Optional thumbnails for presentations, whitepapers, or patent material if later useful.`
- `callout_media`: `Optional visual treatment for especially browsable subcategories such as whitepapers or XPRIZE.`
