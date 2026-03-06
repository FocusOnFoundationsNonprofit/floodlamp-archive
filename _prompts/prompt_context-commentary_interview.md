# Prompt: Context and Commentary Interview

## Author Checklist (not for AI — this is the human author's prep checklist; AI should read for process context only)
[] Review the archive files in this subcategory
In context-commentary file:
[] Voice-dictate raw transcript answers to the generic context questions (will auto-paste)
[] Voice-dictate raw transcript answers to the generic commentary questions (will auto-paste)
[] Drag into AI session: this prompt file, context-commentary file, project-description.md, combined files (all or key files)
[] Optionally drag in _notes_cat-subcategory.md file
[] Run Round 1 AI agent processing
[] Review follow-up questions and scores, decide whether to answer more
[] If answering more: voice-dictate answers, run next round

## Instructions for AI
You are helping the founder and principal scientist of FloodLAMP Biotechnologies develop the Context and Commentary sections of a subcategory context-commentary file for the FloodLAMP archive. Your goal is to process the author's input, distill it into publishable content, and identify gaps where additional input would be valuable.

The user will provide:
- This prompt
- The context-commentary file (already created, with the category and subcategory filled in). This file contains the author's raw transcript notes under the Generic Context Answers and Generic Commentary Answers headings.
- The combined summary entries for the subcategory (as a file)
- The full text of files from the subcategory — either a combined file of all files (for small subcategories) or a combined file of selected key files (for larger subcategories)
- Optionally, the project-description.md file for fuller project background

### Process: Round-Based Refinement

#### Round 1 (Initial Processing)
The author will have already provided raw voice-dictated transcript answers to the generic context and commentary questions in the context-commentary file. Your first task is to process this material and **write the results directly into the context-commentary file**. Do not just display the outputs in chat — you must use your file editing tools to write into the file.

Process the raw transcripts into the following three outputs and write each one into the file:

**Output 1 — Cleaned Transcripts**
Clean up the raw transcripts for both Context and Commentary. Fix dictation artifacts, organize the flow, but preserve the author's voice and all substantive content. Do not add or infer — just clean.
- Write into the `### Generic Context Answers - Cleaned Transcript` section
- Write into the `### Generic Commentary Answers - Cleaned Transcript` section

**Output 2 — Processed Draft Sections**
Distill the cleaned transcripts into publishable draft content for both sections, drawing also on the file summaries and full file text to add specificity and structure:
- **Processed Context**: Clear, factual, explanatory narrative. Third person or neutral voice. Should orient a reader encountering this subcategory for the first time. Write into the `### Processed Context` section.
- **Processed Commentary**: Use either the neutral "we" of FloodLAMP when referring to actions and assessments, or a passive voice as appropriate. Avoid first person singular ("I"). Commentary should be direct, substantive, and not employ marketing language. Provide honest assessments and ideas from the perspective of FloodLAMP closing out its work, not promoting it. Write into the `### Processed Commentary` section.

**Output 3 — Follow-Up Questions**
Generate follow-up questions to address gaps, expand on interesting points, or draw out material the author hasn't covered. Separate into Context and Commentary buckets. For each question:
- State the question
- Score it **1-5** on importance to the overall project goals (1 = nice to have, 5 = significantly important for the archive and downstream work like the scientific paper and vision proposal)
- Brief rationale for the score (one sentence)

Be specific — reference actual files, details, or themes. Present questions sorted by score (highest first) within each bucket. Write into the `### Context Questions` and `### Commentary Questions` sections under `## Follow-Up Questions`.

**IMPORTANT — Write in Round 1:**
After producing all three outputs, you MUST do the following immediately (do not wait for the author to confirm or indicate they are done):
1. **Write all outputs into the context-commentary file** using your file editing tools — cleaned transcripts, processed drafts, and follow-up questions. Every section placeholder in the file should be filled.
2. **Update the `last updated` date** in the file's METADATA section to today's date, keeping the existing author initials (e.g. `RT`). Do NOT change the author initials.

Then present a summary of the follow-up questions in chat so the author can decide whether to answer any of them for a subsequent round.

#### Subsequent Rounds (Optional)
The author will decide whether to answer follow-up questions based on the scores and their own judgment of diminishing returns. If they provide answers (which may again be raw voice-dictated transcript):
1. Clean the new transcript
2. Integrate the new material into updated Processed Draft sections in the file
3. Generate a new set of follow-up questions (if meaningful gaps remain), again scored 1-5, and write them into the file

The author may stop at any point. One round may be sufficient.

### Writing Guidelines (apply to all rounds)
- **Context section**: Clear, factual, explanatory tone. Third person or neutral voice. Informative without being dry. Should orient a first-time reader.
- **Commentary section**: First person (as the author). Direct, substantive, not marketing language. A scientist and founder sharing honest assessments and ideas. The project is a closeout — the author is not promoting FloodLAMP, he is documenting what he learned and what he thinks matters.
- **Length**: Scale to the subcategory. Some will warrant 500-800 words total, others 1500+. Don't pad, don't truncate. Let the substance dictate the length.
- **Cross-references**: When relevant, note connections to other subcategories or collections in the archive (e.g., "The FDA correspondence in fl-fda-correspondence documents the back-and-forth that followed these submissions").


## Project Background
This is the FloodLAMP Archive — an open-source publication of work from FloodLAMP Biotechnologies, a Public Benefit Corporation (2020–2023) focused on decentralized, low-cost molecular testing for COVID-19. The founder is creating this archive as a public good and a grant deliverable. The archive contains ~150 files organized into 4 collections (Guides, Pilots, Regulatory, Various) with multiple subcategories.

The archive is designed to be "AI-ready" — structured so users explore it with their own AI tools. Context and commentary are being added at the subcategory level to provide the narrative layer that the primary source documents alone do not capture.

This is a closeout, not a continuation. The author is not promoting FloodLAMP or pursuing further work in this space. The goal is to make the work openly and honestly available for anyone who may find it relevant — researchers, public health practitioners, regulatory professionals, or historians.

For fuller project background, the user may also include the project-description.md file.
