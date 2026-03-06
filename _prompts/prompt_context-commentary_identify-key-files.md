# Prompt: Identify Key Files for Context and Commentary

## Instructions for AI
You are helping the founder and principal scientist of FloodLAMP Biotechnologies identify which files in a subcategory of the FloodLAMP archive warrant file-level context or commentary as metadata additions. Most files do not need this — the subcategory-level context and commentary file will cover the group. File-level additions should be reserved for files where extra annotation adds significant value.

The user will provide the combined summary entries for one subcategory as a file. Review the entries and identify files that meet one or more of the criteria below.

**Note:** For small subcategories where the total token count is manageable, the user may skip this step entirely and simply combine all files in the subcategory for the interview. This prompt is most useful for larger subcategories where selecting a subset of key files to load as full text is necessary.

### Criteria for File-Level Context
- The summary alone does not convey the file's significance or role within the subcategory
- There is likely backstory that matters — e.g., why something was drafted but not submitted, what happened after a correspondence, what led to a particular decision
- The file documents a turning point, a key decision, or a notable outcome
- The file is a primary or anchor document for the subcategory (the one a reader should start with)
- The file captures something that connects importantly to other parts of the archive (other subcategories or collections)

### Criteria for File-Level Commentary
- The file is likely to prompt strong opinions or assessments from the author
- The file represents a missed opportunity, a lesson learned, or a "what I'd do differently" moment
- The file contains technical or strategic choices that deserve explanation of rationale
- The file is one where the author's interpretation would materially change how a reader understands it

### Output Format

#### 1. Flagged Files with Rationale
For each file you flag, provide:
- The file name
- Which criteria it meets (brief)
- Suggested questions to ask the author — 2-4 specific questions that would draw out useful context or commentary for that file

#### 2. Key Files List
A clean bullet-point list of just the recommended file names:
- filename1.md
- filename2.md
- filename3.md

#### 3. Python Code to Generate Combined Key Files
Provide a ready-to-run mrun function call using `combine_files_to_markdown` that will combine the selected key files into a single markdown file. Use the file paths from the subcategory. The output file should go in the subcategory folder with the name `_archive-combined-files_SUBCATEGORY-key-files.md`. Format:
```python
def mrun_combine_key_files_SUBCATEGORY():
    pass
#if __name__ == "__main__":
    custom_files = ["data/floodlamp/CATEGORY/SUBCATEGORY/filename1.md", "data/floodlamp/CATEGORY/SUBCATEGORY/filename2.md", "data/floodlamp/CATEGORY/SUBCATEGORY/filename3.md"]
    output = "data/floodlamp/CATEGORY/SUBCATEGORY/_archive-combined-files_SUBCATEGORY-key-files.md"
    combine_files_to_markdown(custom_files, output, output_name="SUBCATEGORY key files")
```

#### 4. Summary
How many files you recommend for file-level additions out of the total in the subcategory, and a brief note on whether this subcategory seems like one where file-level context/commentary is particularly valuable or whether the subcategory-level file will largely suffice.


## Project Background
This is the FloodLAMP Archive — an open-source publication of work from FloodLAMP Biotechnologies, a Public Benefit Corporation (2020–2023) focused on decentralized, low-cost molecular testing for COVID-19. The founder is creating this archive as a public good and a grant deliverable. The archive contains ~150 files organized into 4 collections (Guides, Pilots, Regulatory, Various) with multiple subcategories. Each file has a short summary in the combined summary document.

The archive is designed to be "AI-ready" — structured so users explore it with their own AI tools. Context and commentary are being added at the subcategory level (and selectively at the file level) to provide the narrative layer that the primary source documents alone do not capture: why things happened, what they reveal, lessons learned, and the author's ideas and opinions.

### Definitions
- **Context**: Additional factual information, description, and explanation. Less subjective. Answers: what was happening, why this exists, how things relate.
- **Commentary**: The author's ideas, views, opinions, assessments. More subjective. Answers: what I think about this, what I learned, what the field should take from this.
