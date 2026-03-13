METADATA
last updated: 2026-03-02 RT
file_name: _context-commentary_regulatory-fda-townhalls.md
category: regulatory
subcategory: fda-townhalls
words: 3032
tokens: 3898


CONTENT

## Context
This subcategory contains processed transcripts from approximately 100 FDA Virtual Town Hall meetings for COVID-19 diagnostic test developers, spanning from March 2020 through early 2023. The FDA held these meetings approximately every two weeks, with each session typically lasting about an hour. The town halls served as a direct engagement channel between the FDA and the diagnostic test development community during the pandemic, covering topics including Emergency Use Authorization (EUA) submissions, test validation requirements, regulatory updates, and policy changes.

The archive contains two processed file types for each town hall session: `section-titles` files (organized by agenda and topic sections) and `qa-qonly` files (extracted question-and-answer pairs only). The source transcripts were downloaded from the FDA website in PDF format. Processing involved significant variability in cleaning requirements, particularly around standardizing speaker names and formatting across sessions. The question-and-answer extraction represented a substantial separate effort, producing the structured QA pairs that form the foundation of the QRAG knowledge base described below.

#### QRAG Application
QRAG (Question Retrieval Augmented Generation) is a specialized AI retrieval tool that FloodLAMP developed and applied to this corpus of FDA Town Hall transcripts. A live demo is available at:
https://www.focusonfoundations.org/fda-town-halls-qrag-demo

QRAG was developed in late 2023, which is a long time ago in the context of AI development. Current state-of-the-art reasoning systems may achieve comparable results via a system prompt that requests the closest quotations alongside a synthesis from a large corpus of files. However, the QRAG approach may still be faster and more cost-effective for this type of RAG/structured retrieval task.

#### QRAG Explainer
The QRAG system is designed for "serious contexts of use" where authoritative, source-attributed answers are needed. It provides responses by leveraging a pre-processed, curated knowledge base of question-answer (QA) pairs. Key characteristics include:

- **Structured QA Processing**: Utilizes pre-processed QA blocks with metadata for efficient retrieval.
- **Pre-Processed QA Content**: Uses structured QA pairs that can be authority-vetted, enabling high-quality retrieval and responses.
- **Question-Based Vector Search**: Employs embeddings of questions for accurate matching.
- **Intelligent Response Routing**: Routes queries based on question match quality to appropriate LLM prompts.
- **Transparent Source Attribution**: Distinguishes between quoted and AI-generated content.

## Commentary
The FDA's decision to hold regular town halls for diagnostic test developers during the pandemic represented a valuable form of direct engagement with the regulated community. However, the volume and nature of questions from serious test developers across these sessions reveals a persistent information and clarity gap in FDA communication around diagnostic test authorization. Addressing that gap with AI has enormous potential to enable progress in the diagnostics space.

**Why QRAG — the case for authority-quoted retrieval**
The core motivation for the QRAG tool was to avoid full reliance on AI-generated answers for a subject as consequential as FDA diagnostic regulatory policy. Hallucination rates in large language models have decreased substantially since this work began in 2023, but for regulatory questions where precision matters, users benefit from seeing the authority directly quoted — what the FDA actually said — either before or alongside any AI-generated synthesis. This makes the output more reliable and more verifiable. A practical approach for using QRAG is to increase the number of returned chunks (direct quotations) to 20 or even 50, save the results as a markdown file, and then load that file into the user's own AI tool for deeper analysis, particularly if the user has access to extended-reasoning models through a pro-level subscription.

**FDA refusal to answer questions: an unexamined pattern**
One analysis that would be worthwhile but has not been performed is a systematic examination of the FDA's refusal to answer questions during these town halls. The FDA routinely declined to respond to questions about specific submissions, using standard language to that effect. While there is a legitimate basis for this position, many of the questions came from test developers seeking to understand the status or outcome of their own submissions. There are concerns that this standard refusal was also used to avoid addressing questions that touched on areas of potential inconsistency, lack of clarity, or unresolved policy problems. Developers regularly raised straightforward questions, such as why they had not received a review response after months of waiting. There has been important work on both reducing review timelines and increasing transparency around these processes, and the new FDA leadership appears to be moving in that direction.

**Transparency and the case for publishing rejection letters**
FDA Commissioner Marty Makary, in a January 2025 interview on the All-In Podcast, stated:

> "We've got to challenge these deeply held assumptions. And we're doing it. We are doing it with new programs, new priority reviews, new pilots, new forms of transparency. We made our rejection letters public so that if the FDA does not approve a drug, the public deserves to know why. And it creates accountability. And that was not the case before. They talked about it for 30 years and we got it done."

This remark was made in the context of drug approvals, but the principle applies equally to diagnostics. When a diagnostic test developer submits an EUA application, the expectation is that the submission is complete and ready for authorization. The FDA also offers a pre-submission question process (or pre-EUA process) for obtaining feedback on incomplete work. Once the formal submission is made, if the FDA authorizes it, the submission becomes public. There is a strong argument that rejected submissions and the FDA's stated reasons for rejection should also be made public. Given that the submitter has represented the application as ready for authorization, transparency from that point forward could lead to faster processing, greater consistency, higher quality submissions, and greater encouragement of innovation.

**FDA's internal use of AI**
A companion report in this subcategory (`_AI_FDA_Internal_AI_Use_Report.md`) examines the FDA's early adoption of internal generative AI tools, including the "Elsa" platform and the 2025 AI-assisted scientific review pilot. As of that report's date, there has been limited public progress in the direction of the standardization and transparency measures discussed above. The stated capabilities of Elsa (accelerating clinical protocol reviews, shortening scientific evaluations, summarizing adverse events, performing label comparisons) suggest operational efficiency gains, but no center-specific SOPs or workflow changes have been published. These internal AI developments are worth monitoring, as they could eventually affect review workflows, consistency, and processing times for diagnostic submissions.

**Analysis of FDA refusals to answer: an AI-enabled demonstration**
As a demonstration of AI-enabled use of this FDA Townhall set of files, a comprehensive analysis was conducted and is documented in a separate companion file in this subcategory: `_AI_FDA_Townhall_Analysis_of_Refusals_and_Legitimacy.md`.

That document contains:
- A critical analysis of the FDA's standard "we are not able to respond to questions about specific submissions" language, including its effect on transparency, accountability, and the structural silencing of the regulated community.
- A legitimacy rubric with classification categories and a 1–5 scoring system for evaluating whether individual refusal instances were justified.
- Classification and scoring of all 116 identified refusal instances across 84 of the 100 town hall transcript files (51 boilerplate opening disclaimers and 65 active in-session refusals).
- Summary statistics and interpretation of results.

The raw extraction of refusal passages is compiled in a separate file: `_compilation_fda-refusals-to-answer.md`.

It is important to note that this analysis was produced as a rapid, AI-assisted demonstration. The critical essay in Section 1 of the analysis document was authored through voice-dictated prompts to Claude Opus 4.6 (via Cursor's agentic coding mode), with the author providing the arguments, framing, and specific factual claims, and the model producing the written text. The classification and scoring of the 116 refusal instances was performed by Python code that the model generated and executed — using regex pattern matching and heuristic classification, not through carefully engineered structured-output prompts applied with a frontier reasoning model. As a result, the compilation of raw refusal passages likely has significant problems and errors, but the legitimacy classifications and numerical scores should be treated as merely a placeholder and demonstration of the potential of fully automated AI analysis. The methodology disclaimer in the analysis document itself provides more detail.

This work did not use the QA extraction files or the QRAG retrieval tool — it was performed directly against the `section-titles` transcript files. It demonstrates what is potentially possible with AI and well-cleaned transcripts, even through informal voice-prompted interaction with an agentic model. A more rigorous approach would involve developing a structured-output prompt (with fields for category, score, rationale, and supporting excerpt), tuning and evaluating that prompt against a human-scored sample, running it with a high-quality frontier reasoning model across all identified instances, and performing human evaluation of the results. That level of rigor is achievable with current tools and would produce a substantially more reliable analysis — but the rapid demonstration here is sufficient to illustrate the patterns and motivate the effort.

The python code to implement the rigorous, non-agentic version of this AI-analysis is available in the open-source repo here https://github.com/FocusOnFoundationsNonprofit/public-corpus-tools. This code base was created and partially funded by the Balvi grant received by FloodLAMP to open-source and publish it's work from the pandemic. In particular, 2 python modules fileops.py and llm.py contain code to 1) process text/markdown files, and 2) run llm prompts over them (both normal prompts and function calls/structured output prompts). With the advances in AI coding since this codebase was developed in 2023, these modules could likely get created now in a few minutes or even maybe seconds in one shot with a short voice dictated prompt. The capability offered by these modules is basically a superpower. It means that anyone — a journalist, a researcher, an advocacy group, a congressional staffer — can take a large body of public records like these 100 town hall transcripts, apply a sophisticated and objective analytical framework to the entire corpus, and produce results that would have taken a team of analysts months to compile, for almost nothing in time and cost. And those results can be used to discover and expose problems — from severe structural failures to quiet inefficiencies — in the operation of agencies, institutions, and bureaucracies. And then, crucially, to develop and advocate for specific, actionable reforms. Not vague calls for "more transparency" but concrete proposals grounded in evidence extracted from the institution's own public record. That is what this analysis attempts to demonstrate, and that is what the open-source tools in this repository are designed to enable.


## Follow-Up Questions

### Context Questions
1. **Were there specific town hall sessions or time periods that were particularly information-rich or that marked significant FDA policy shifts?** (Score: 4)
   Highlighting key sessions would help users prioritize their exploration and strengthen the archive's utility as a navigational reference.

2. **What are the known limitations of the processed transcripts — e.g., speaker misattributions, gaps from poor PDF quality, or sessions that could not be fully processed?** (Score: 4)
   Documenting limitations is important for an archive designed to be used with AI tools, where source quality directly affects output quality.

3. **How did the format, content, and attendance of the town halls evolve over the pandemic timeline — e.g., did participation drop off, did topics shift from EUA mechanics to post-pandemic policy?** (Score: 3)
   The evolution of these meetings may reflect broader shifts in the FDA-developer relationship and pandemic response priorities, which would add narrative depth to the context.

4. **How many total QA pairs were extracted across the ~100 town hall transcripts, and what was the distribution over time?** (Score: 3)
   Quantitative details would add specificity to the archive description and help users understand the scale and density of the corpus.

5. **What specific challenges arose during the QA extraction process, and how were edge cases handled (e.g., multi-part questions, questions with no clear FDA response)?** (Score: 2)
   Understanding the extraction methodology would help future users and researchers assess the quality and completeness of the QRAG knowledge base.

### Commentary Questions
1. **Can you provide specific examples of questions that the FDA refused to answer where the refusal seemed to avoid substantive issues rather than protect submission-specific confidentiality?** (Score: 5)
   Concrete examples would significantly strengthen the commentary's central argument about transparency gaps and give future researchers specific threads to follow.
_A: Okay, so I did a big analysis and thread on this and it produced another, the output of that was another document. This is here. Well, I'm going to include it in this in this context window here. Well, actually this is the same thread. I thought I started a new thread, but I didn't. So, well then this should be more straightforward. Yeah, I am going to drag back in the this file though. So what I want you to do is just include it here above. Well, I mean, put it at the end of the process commentary. That's where it should go. And you're going to reference this document and just give a short kind of explainer on what it is. And then what I want you to also do is add a disclaimer to the AI FDA Town Hall Analysis of Refusals and Legitimacy file, because I've only really briefly scanned the classification and I don't have high confidence in them overall. I think some are spot on, but I think some could be really off and just mistakes. And I don't, I'm even confused about the excerpts and how those were pulled and generated. Now, I don't want to redo this whole thing because it's, I'm out of time on dealing with this and I got to move on to the next important area, which is our submissions in the Open EUA concept. So what I think what I'd like to do here is I think really this is, this is look at this as a demonstration of what's potentially possible, you know, with AI and these clean transcripts and note that this was not using the QA extraction or the QRAG tool. And what I want to say is that, you know, how, what would ideally be done here? And this is almost like a technical aside, but I do want to include this because this is pretty important. You know, what would you, what, what I think you would do to do this properly or more thoroughly would be to develop a prompt and it would be a, you know, function call or structured output prompt, you know, with the, you know, the category, the score, the rationale, etc. And then, you know, tune and evaluate that prompt and use that with, you know, one of the high reasoning, high quality, you know, frontier reasoning models, you know, perhaps comparing a few of them and doing, you know, human evaluation of this rubric application and scoring. And then, and then run that in a loop, you know, using code across all of the identified refusals. I think probably the compilation of refusals is pretty good. I'm not sure about that. I did as I scan those, they looked pretty good. But Again, I have a lot less confidence in the legitimacy analysis and kind of numerical scoring and classification there. So it's important to say how this was done. I mean, this was done through very quick voice prompts to Opus 4.6 max within cursor. And so this is the power of the new agentic models is that they should be able to do something like what I described just automatically where they're applying, developing and applying prompts iteratively or sequentially across corpuses or bodies of text, compiling those results, doing these evaluations. And in the end, just delivering you the high quality output that has the consistency that is impossible with single base model calls at all, or even just the reasoning models of a couple of months ago, or just say of 2025. But I'm not sure these systems are actually there yet. I'm not sure that they are doing what I described, which is developing the prompts as structured output prompts iteratively and consistently applying them. I think they are developing and writing code behind the scenes that you don't even see and then running those in a sandbox against the files. And that's all that all seems to be, I mean, that is happening. So again, couch this as an unaudited demo, which very likely contains a significant fraction of errors in the application of the rubric and the legitimacy score for all of these instances. Okay, I think that's enough. That should be good._

2. **How does FloodLAMP's own experience as a test developer submitting to the FDA connect to the patterns observed in these town halls?** (Score: 5)
   FloodLAMP's firsthand experience with the EUA process would add direct credibility and specificity to the commentary. This is the kind of material only the founder can provide, and it connects this subcategory to the fl-fda-correspondence and open-euas subcategories.

3. **What is your assessment of whether the current FDA leadership's transparency reforms (e.g., publishing rejection letters) will meaningfully reach the diagnostics/IVD space, given that the initial focus appears to be on drugs?** (Score: 4)
   The founder's informed opinion on whether drug-side reforms will extend to diagnostics is directly relevant to the archive's regulatory collection and to users in that space.

4. **Are there specific connections between patterns in these town hall Q&As and FloodLAMP's experience documented in other archive subcategories (e.g., fl-fda-correspondence, open-euas, ldts)?** (Score: 4)
   Cross-referencing across subcategories would strengthen the archive as an interconnected resource and help users see how the town halls relate to the broader regulatory story.

5. **Were there specific QRAG queries or use patterns during development that revealed unexpected insights about the town hall corpus?** (Score: 3)
   Discovery stories from building the tool could illustrate its value more concretely than a feature description alone, and could serve as examples for users exploring the QRAG demo.

6. **Has anyone tested a modern reasoning model (e.g., o1, Claude with extended thinking) against the same queries to compare with QRAG's retrieval approach? What is your honest assessment of QRAG's ongoing utility?** (Score: 3)
   An honest comparison would be valuable for the archive's credibility and would help users decide whether to use QRAG or load the transcripts directly into their own AI tool.
