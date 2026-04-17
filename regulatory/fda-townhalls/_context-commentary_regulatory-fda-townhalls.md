METADATA
last updated: 2026-03-22 RT
file_name: _context-commentary_regulatory-fda-townhalls.md
category: regulatory
subcategory: fda-townhalls
gfile_url: https://docs.google.com/document/d/1D3TwdRTkR5UR6oydl7IDwRFOelOVrbSwDaSzmZcMJNs
words: 1709
tokens: 2228


CONTENT

## Context
This subcategory `regulatory/fda-townhalls` contains processed transcripts from approximately 100 FDA Virtual Town Hall meetings for COVID-19 diagnostic test developers, spanning from March 2020 through early 2023. The FDA held these meetings approximately every two weeks, with each session typically lasting about an hour. The town halls served as a direct engagement channel between the FDA and the diagnostic test development community during the pandemic, covering topics including Emergency Use Authorization (EUA) submissions, test validation requirements, regulatory updates, and policy changes.

The archive contains two processed file types for each town hall session: `section-titles` files (organized by agenda and topic sections) and `qa-qonly` files (extracted question-and-answer pairs only). The source transcripts were downloaded from the FDA website in PDF format. Processing involved standardizing the significant variability in these FDA transcripts, particularly speaker names and formatting across sessions. The question-and-answer extraction represented a substantial separate effort, producing the structured QA pairs that form the "QRAG" AI application described below.

### QRAG Application
QRAG (Question Retrieval Augmented Generation) is a specialized AI retrieval tool that FloodLAMP developed and applied to this corpus of FDA Town Hall transcripts. A live demo is available at:
https://www.focusonfoundations.org/fda-town-halls-qrag-demo

QRAG was developed in late 2023, which is a long time ago in the context of AI development. Current state-of-the-art reasoning and agentic AI systems may achieve comparable or superior results; however, the QRAG approach may still be faster and more cost-effective for this type of RAG/structured retrieval task.

### QRAG Explainer
The QRAG system is designed for "serious contexts of use" where authoritative, source-attributed answers are needed. It provides responses by leveraging a pre-processed, curated knowledge base of question-answer (QA) pairs. Key characteristics include:

- **Structured QA Processing**: Utilizes pre-processed QA blocks with metadata for efficient retrieval.
- **Pre-Processed QA Content**: Uses structured QA pairs that can be authority-vetted, enabling high-quality retrieval and responses.
- **Question-Based Vector Search**: Employs embeddings of questions for accurate matching to user queries.
- **Intelligent Response Routing**: Routes queries based on question match quality to appropriate LLM prompts.
- **Transparent Source Attribution**: Distinguishes between quoted and AI-generated content.

## Commentary
The FDA's decision to hold regular town halls for diagnostic test developers during the pandemic represented a valuable form of direct engagement with the regulated community. However, the volume and nature of questions from serious test developers across these sessions reveals a persistent information and clarity gap in FDA communication around diagnostic test authorization. Addressing that gap with AI to improve the efficiency, accuracy, consistency, and objectivity has enormous potential to enable progress in the diagnostics space.

### Why QRAG — the case for authority-quoted retrieval
The core motivation for the QRAG tool was to avoid full reliance on AI-generated answers for a subject as consequential as FDA diagnostic regulatory policy. Hallucination rates in large language models have decreased substantially since this work began in 2023, but for regulatory questions where precision matters, users benefit from seeing the authority directly quoted (i.e. what the FDA actually said) either before or alongside any AI-generated synthesis. This makes the output more reliable and more verifiable. A practical approach for using QRAG is to increase the number of returned chunks (direct quotations) to 20 or even 50, save the results as a markdown file, and then load that file into the user's own AI tool for deeper analysis, particularly if the user has access to extended-reasoning models through a pro-level subscription or other advanced AI tool.

### FDA refusal to answer questions: an example use case
One analysis that may be illuminating and serve as an example use case of our QRAG tool over the FDA Diagnostics Town Halls is a systematic examination of the FDA's refusal to answer questions. The FDA routinely declined to respond to questions about specific submissions, using standard language to that effect. While there is an appropriate basis for not answering in some cases, many of the questions were asked in good faith by test developers seeking to understand the status or outcome of their own submissions, and could have been better served with substantive responses rather than generic refusal. There are concerns that this standard refusal was also used to avoid addressing questions that touched on areas of potential inconsistency, lack of clarity, or unresolved policy problems. Developers regularly raised straightforward questions, such as why they had not received a review response after months of waiting. There has been important work on both reducing review timelines and increasing transparency around these processes, and the new FDA leadership appears to be moving in that direction.

### Analysis of FDA refusals to answer: an AI-enabled demonstration
As a demonstration of AI-enabled use of this FDA Townhall set of files, a comprehensive analysis was conducted and is documented in a separate companion file in this subcategory: `_AI_FDA_Townhall_Analysis_of_Refusals`.

That document contains:
- A critical analysis of the FDA's standard "we are not able to respond to questions about specific submissions" language, including its effect on transparency, accountability, and the structural silencing of the regulated community.
- An appropriateness rubric with classification categories and a 1–5 scoring system for evaluating whether individual refusal instances were justified.
- Classification and scoring of all 116 identified refusal instances across 84 of the 100 town hall transcript files (51 boilerplate opening disclaimers and 65 active in-session refusals).
- Summary statistics and interpretation of results.

The raw extraction of refusal passages is compiled in a separate file: `_compilation_fda-refusals-to-answer`.

The critical essay in Section 1 of the analysis document was authored by FloodLAMP founder Randy True and later revised with AI assistance. The initial extraction and classification of refusal instances was produced as a rapid, AI-assisted demonstration using regex pattern matching and heuristic classification generated and executed by the agentic model during that same session.

A more rigorous, non-agentic version was then implemented as a standalone Python module (`refusal_analysis.py`, included in this subcategory). This code runs a two-step structured-output pipeline against the `section-titles` transcript files: first, an LLM-based extraction pass identifies refusal instances by line range using a detailed prompt and function-call schema, supplemented by heuristic keyword matching; second, a classification pass scores each instance against an appropriateness rubric with fields for category code, appropriateness score, rationale, key excerpt, speaker identification, and contextual flags. The extraction and classification prompts, structured-output tool schemas, and the full rubric are defined in the module. The code also generates a markdown report with summary statistics, per-instance detail, and interpretive findings. This approach, structured-output prompts applied with a frontier reasoning model, produces substantially more reliable and auditable results than the initial rapid demonstration.

Additional python code that supports refusal analysis code is available in the open-source repo here https://github.com/FocusOnFoundationsNonprofit/public-corpus-tools. This code base was created and partially funded by the Balvi grant received by FloodLAMP to open-source and publish its work from the pandemic. In particular, 3 python modules fileops.py, llm.py, and rag.py contain code to 1) process text/markdown files, 2) run llm prompts over them (both normal prompts and function calls/structured output prompts), and 3) perform the QRAG retrieval and routed prompt call. With the advances in AI coding since this codebase was developed in 2024, these modules could likely be significantly improved or recreated from scratch.

The capability offered by these modules is powerful, as they enable programmatic file processing and the application of AI to collections of files. Using this code, anyone, a journalist, a researcher, an advocacy group, a government staffer, can take a large body of public records like these 100 town hall transcripts, apply a sophisticated and objective analytical framework to the entire corpus, and produce results that would have taken a team of analysts months to compile, for almost nothing in time and cost. And those results can be used to discover and expose problems, from significant structural failures to meaningful inefficiencies, in the operation of agencies, institutions, and bureaucracies. And then, crucially, to develop and advocate for specific, actionable reforms. Not vague calls for "more transparency" but concrete proposals grounded in evidence extracted from the institution's own public record. That is what this analysis attempts to demonstrate, and that is what the open-source tools in this repository are designed to enable.

### Transparency and the case for publishing rejection letters
FDA Commissioner Marty Makary, in a January 2025 interview on the All-In Podcast, stated:

> "We've got to challenge these deeply held assumptions. And we're doing it. We are doing it with new programs, new priority reviews, new pilots, new forms of transparency. We made our rejection letters public so that if the FDA does not approve a drug, the public deserves to know why. And it creates accountability. And that was not the case before. They talked about it for 30 years and we got it done."

This remark was made in the context of drug approvals, but the principle applies equally to diagnostics. In the context of the pandemic, when a diagnostic test developer submitted an EUA application, the expectation was that the submission was complete and ready for authorization. The FDA also offered a pre-submission question process (or pre-EUA process) for obtaining feedback on incomplete work. Once the formal submission was made, if the FDA authorized the test, the submission (at least a version of it in the form of the IFU) becomes public. There is a strong argument that rejected submissions and the FDA's stated reasons for rejection should both be made public. The submitter has represented the application as ready for authorization and precious resources have been used to review it. Transparency from that point forward could lead to faster processing, greater consistency, higher quality submissions, and greater encouragement of innovation.

### FDA's internal use of AI
A companion report in this subcategory (`_AI_FDA_Internal_AI_Use_Report`) examines the FDA's early adoption of internal generative AI tools, including the "Elsa" platform and the 2025 AI-assisted scientific review pilot. As of that report's date, there has been limited public progress in the direction of the standardization and transparency measures discussed above. The stated capabilities of Elsa (accelerating clinical protocol reviews, shortening scientific evaluations, summarizing adverse events, performing label comparisons) suggest operational efficiency gains, but no center-specific SOPs or workflow changes have been published. These internal AI developments are worth monitoring, as they could eventually affect review workflows, consistency, and processing times for diagnostic submissions.
