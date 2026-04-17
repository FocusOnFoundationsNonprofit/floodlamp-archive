METADATA
last updated: 2026-03-26 RT
file_name: _AI_FDA_Townhall_Analysis_of_Refusals.md
file_date: 2026-03-26
title: FloodLAMP FDA Town Halls Analysis of Refusals
category: regulatory
subcategory: fda-townhalls
tags: fda, townhalls, refusals, transparency, accountability
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1UTA1dSxr1wnwFT7aMxotDyWF2Mislz_VDkX6I2sMIuA
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 47995
words: 35637
notes: **AI GENERATED - MAY CONTAIN ERRORS** Created during archive preparation using AI-assisted drafting and analysis, then partially revised through human review. Critical analysis in Section 1 is substantively authored by FloodLAMP founder Randy True and was later revised with AI assistance. Sections 2-4 were developed collaboratively with AI support; Section 3 began as heuristic code-based classification and was later partially reviewed, corrected, and expanded through manual comparison against the companion compilation file. This document is not fully audited and may still contain errors, but it is no longer purely unaudited AI output. Current counts reflect 135 identified refusal instances across 90 of 100 files: 88 boilerplate opening disclaimers and 47 scored active refusals. Based on section-titles transcript files. Companion file: _compilation_fda-refusals-to-answer.md.
summary_short: Critical analysis of the FDA's systematic refusal to answer questions during ~100 COVID-19 Diagnostic Virtual Town Hall sessions (2020-2023), covering the "specific submissions" policy's impact on transparency and accountability. Includes an appropriateness rubric, classification and scoring of 135 identified refusal instances, and summary statistics showing an average appropriateness score of 3.1/5 for active refusals, with 32% scoring questionable or worse.


CONTENT

## FDA Town Halls Analysis of Refusals

This document presents a critical analysis of the FDA's refusal to answer questions during
the COVID-19 Diagnostic Virtual Town Hall series (~100 sessions, March 2020 through early 2023),
including an appropriateness rubric, classification and scoring of all identified instances, and a summary of results.

### Methodology Disclaimer — Read Before Citing

**This document is not a fully audited or peer-reviewed analysis. Sections 3 and 4 have received partial human review and revision, but the instance-level classifications and scores should still be treated as provisional and may contain errors.**

This analysis was produced through a rapid interaction with Claude Opus 4.6 (Anthropic's agentic reasoning model) within Cursor, an AI-assisted IDE. The process worked as follows:

- **Section 1 (Critical Analysis):** The arguments, factual claims, framing, and many specific examples were provided by the author (Randy True, FloodLAMP founder and CEO during the pandemic) through drafting and revision. AI assisted with drafting and restructuring the prose.
- **Section 2 (Rubric):** The rubric categories and scoring definitions were developed collaboratively between the author and the model.
- **Section 3 (Classification and Scoring):** The classification process began with AI-written Python code using regex pattern matching and heuristic rules to extract and classify candidate refusal instances. That output was then partially reviewed and revised manually, including removal of some weak or misattributed boilerplate entries, review of selected active-refusal classifications, and addition of some refusal passages identified in the companion compilation file.
- **Section 4 (Summary):** The summary statistics reflect the current Section 3 contents after those revisions. They are more reliable than the original heuristic-only output, but still should be treated as provisional rather than fully audited.
- **The compilation of raw refusal passages** (in the companion file `_compilation_fda-refusals-to-answer.md`) was assembled separately and appears to have been used as a secondary review source for identifying omissions and checking recall.

**What this analysis does well:** The critical essay in Section 1 reflects the author's direct experience as a diagnostic test developer during the pandemic and is substantively authored content. The rubric in Section 2 is a reasonable framework for evaluating refusal appropriateness. The overall patterns identified in Section 4 are more reliable than in the original heuristic-only version and are likely directionally useful, especially after partial human review of boilerplate counts and selected active-refusal entries.

**What this analysis does not do well:** The instance-level classification in Section 3 still began as heuristic code rather than a fully prompt-tuned, instance-by-instance model evaluation, and the document has not been fully audited. Some classifications are still likely wrong or debatable — the heuristics and later revisions may misread the tone or substance of an exchange, misclassify a partial answer as a deflection, or fail to detect that a useful general answer was provided alongside a refusal.

**How this should ideally be done:** A more rigorous approach would involve:
1. Developing a structured-output prompt with defined fields (category, score, rationale, key excerpt, speaker) for each refusal instance.
2. Tuning and evaluating that prompt against a human-scored sample of 20–30 instances.
3. Running the prompt with a high-quality frontier reasoning model (e.g., Claude Opus, GPT-4o, Gemini 2.5 Pro) across all identified instances, potentially comparing results across models.
4. Performing human evaluation of a random sample of the model's output to measure agreement and identify systematic errors.
5. Iterating on the prompt based on error analysis.

This level of rigor is achievable with current tools and would produce a substantially more reliable analysis. The current version goes beyond the original rapid demonstration because it includes partial human review and revision, but it still should not be cited as if every individual instance-level score has been fully validated.

**What this demonstrates about AI capability:** This analysis — including extraction from roughly 100 transcript files, development of an appropriateness rubric, generation of an initial code-based classification pass, construction of a long-form analytical document, and later rounds of targeted human review and revision — shows that current agentic AI tools can substantially accelerate complex archival analysis. This work was performed directly against the `section-titles` transcript files and did not use the QA extraction files or the QRAG retrieval tool. Current models can help develop code, execute it in sandboxed environments, read and process large file sets, and produce analytical documents of this scope, but they still benefit from explicit human direction and selective audit when instance-level judgments matter. The gap between rapid AI-assisted first pass and fully validated human-audited analysis remains important.

---

## 1. Critical Analysis: "We Are Not Able to Respond to Questions About Specific Submissions"

### The Standard Language
Across nearly every one of the ~100 FDA Virtual Town Halls for COVID-19 diagnostic test developers, the moderator opened with a variation of:

> "Please remember that during this Town Hall, we are not able to respond to questions about specific submissions that might be under review."

This language became the default framing for all engagement. It was not presented as a circumstantial limitation but as a blanket policy. And it shaped the entire dynamic of these calls: developers learned quickly that any question touching on their own submission would be deflected, regardless of the nature of the question or the willingness of the developer to waive any confidentiality concerns.

### What Does the FDA Actually Mean?
The stated justification for this policy was confidentiality — that submission details are proprietary and the FDA cannot disclose them on a public call. But this framing obscures what is actually happening in the majority of cases. Consider the participants:

- Almost everyone calling in is either preparing to submit, has submitted, or is actively engaged with the FDA on a COVID-19 diagnostic test EUA.
- When a developer asks a question about their *own* submission on a public call, they are voluntarily disclosing whatever details they choose. There is no third-party confidentiality to protect.
- The FDA's concern about confidentiality is therefore not about protecting the *caller* — it is about protecting the FDA's own discretion over what it says, when, and to whom.

If we strip away the confidentiality framing, the most charitable interpretation of what the FDA is actually saying is:

> "We cannot look up your submission in our systems during this live call, review the details, and give you a case-specific answer on the spot. We can only answer from general knowledge and established policy."

That is a *reasonable operational limitation*. It would be unreasonable to expect Tim Stenzel or Toby Lowe to pull up a submission file during a live town hall and conduct an ad hoc review. No one disputes that.

### The Problem: Refusal Instead of Generalization
The critical failure is not the limitation itself — it is what the FDA chose to do with it. When a developer asked a specific question, the FDA had two options:

1. **Generalize and answer**: Reframe the question as a general policy or process question and provide the closest applicable answer. This is what subject matter experts do in every other public-facing context (or _should_ do).
2. **Refuse and deflect**: Invoke the "specific submissions" language, provide no substantive guidance, and redirect the caller to a private email or the pre-EUA process where they are not publicly accountable for their response..

The FDA chose option 2 far more often than necessary. In many instances, the Director of the Office of In Vitro Diagnostics — one of the most qualified people in the world to answer these questions — was sitting on the call, understood the general policy perfectly well, and could have provided a useful general answer. Instead, the caller was told to "reach out to the templates email address" and wait days or weeks for a response that might or might not come.

It is important to recognize who these callers were and why they were calling in to a public forum. These were diagnostic test developers — scientists, regulatory affairs professionals, and company leaders who understood the FDA's processes and knew that they could submit questions in writing through pre-EUA submissions, Q-subs (question submissions), or the templates email address. They chose to ask on a public call for reasons that the "send it in writing" redirect systematically undermined:

- **Timeliness.** Written submissions to the FDA could take weeks or months to receive a response. During a pandemic where delays cost lives, waiting weeks for guidance on a validation question was not a neutral outcome. A developer on the call could get an answer in real time — if the FDA chose to give one.
- **Public accountability.** A question asked and answered on a recorded call with hundreds of listeners becomes part of the public record. Other developers with similar questions benefit from the answer. And the FDA is accountable for the consistency of its answer because anyone can compare it to what was said on previous calls. A private email response has none of these properties.
- **Signal of importance.** Calling in to a live town hall, identifying yourself, and asking a question publicly was a signal that the issue mattered and that the developer wanted the broader community to hear the FDA's position.

There is an appropriate use for the email redirect: when a question genuinely requires case-specific review that cannot be done live, directing the developer to a channel where that review can happen is reasonable — provided the FDA actually follows through in a timely manner. But the transcripts show that the redirect was used routinely for questions that did not require case-specific review, as a blanket deflection that moved questions out of the public forum and into private, unaccountable channels. The later town halls formalized this further, pre-screening emailed questions before the call and declining to address any deemed "too detailed or case-specific" — a category that appeared to expand over time.

### The Effect on Transparency and Accountability
The "specific submissions" policy had several compounding effects:

- **Public accountability was removed.** When a question is answered on a recorded public call, the answer is on the record. When it is redirected to a private email exchange, there is no public record, no consistency check, and no accountability.
- **Inconsistency was hidden.** If the FDA's answer to Developer A differs from its answer to Developer B on the same policy question, the public call format would expose that. The email redirect ensures it never comes to light.
- **Developers were trained not to ask.** Over 100 sessions, developers internalized the refusal pattern. The quality and specificity of questions declined over time, not because developers had fewer questions, but because they learned there was no point in asking.
- **The appearance of engagement substituted for actual engagement.** The town halls allowed the FDA to claim it was holding regular, open sessions with the developer community. But if the most pressing questions are systematically deflected, the engagement is performative.

### The Chilling Effect: Retaliation Risk and Structural Silencing
There is a deeper dimension to this pattern that the transcripts cannot directly show, but that anyone who operated in the COVID-19 diagnostics space understood: **the people best positioned to criticize the FDA's process were the people most vulnerable to retaliation by the FDA.**

The diagnostics industry is entirely dependent on FDA authorization. A company cannot sell a test without it. A CEO who publicly criticized the FDA's review process, questioned the consistency of its decisions, or challenged a refusal on one of these town halls was not engaging in normal public discourse — they were risking their company's relationship with the one entity that controlled whether their product could exist in the market. The consequences were not hypothetical:

- The FDA had complete discretion over review timelines. A submission could be prioritized or deprioritized with no public justification.
- The FDA had complete discretion over the depth of review. A submission could receive one round of questions or five, with no external check on whether the additional scrutiny was warranted.
- The FDA had discretion over informal guidance. A developer who maintained a cooperative relationship might receive a helpful pre-EUA call; one who had been publicly critical might receive a form response pointing to the templates.
- The consequences extended beyond any single company. A CEO perceived as antagonistic to the FDA could find their professional reputation in the field damaged — not through any formal action, but through the informal networks that connect regulators, reviewers, and the companies that depend on them. In a field this specialized, being blackballed by the FDA is not a setback — it is a career-ending event.
- For smaller companies, even a delay — not a rejection, just a delay — could be existential. Diagnostic startups burning cash on R&D and manufacturing scale-up cannot survive indefinitely without revenue, and revenue requires authorization. The case of Lucira Health illustrates this starkly: Lucira developed the first at-home combination COVID-19 and flu test, anticipated FDA authorization by August 2022, and spent through its reserves waiting. The FDA finally issued the EUA on February 27, 2023 — five days after Lucira filed for Chapter 11 bankruptcy protection. The company that built one of the most innovative diagnostic products of the pandemic was destroyed not by the market but by the timeline of regulatory authorization. (Sources: FDA CDRH Statement on EUA of Lucira Health's COVID-19 & Flu Home Test, Feb. 2023; GlobeNewsWire, Lucira Health press releases, Feb. 22 and Feb. 27, 2023.)

None of this is provable in individual cases, and that is precisely the point. The system was structured so that inconsistency, favoritism, and retaliation were *impossible to detect from the outside*. Review decisions were made behind closed doors. Rejection reasoning was not published. Comparative timelines across similar submissions were not available. And the one public forum where these issues might surface — the town halls — systematically deflected the questions that would expose them.

The result was a structural silencing of the FDA's most knowledgeable constituency. The developers, scientists, and CEOs who understood the FDA's review process well enough to identify its flaws were the same people who could not afford to say so publicly. The field is so technically specialized that outside observers — journalists, legislators, the general public — lack the expertise to evaluate whether the FDA's review decisions were consistent, timely, or well-reasoned. Only the regulated community had that knowledge, and the regulated community was effectively muzzled by its dependence on the regulator's goodwill.

This dynamic is worth noting in the context of the town hall transcripts specifically: listen to how callers framed their questions. They were deferential, grateful, and careful not to imply criticism. Even when a developer had waited months for a response, or when the FDA's guidance contradicted its own templates, the questions were phrased as requests for clarification rather than challenges. This was not politeness — it was self-preservation. The power asymmetry between the FDA and its regulated community was so complete that even on a public call with hundreds of listeners, no one could afford to say what many of them were thinking.

### The Consistency Problem: No Mechanism for Accountability
It is worth pausing on the specific nature of the consistency concern. Tim Stenzel, the Director of the Office of In Vitro Diagnostics who led these town halls, came to the FDA from industry — he had previously served as head of diagnostics at Quidel, one of the largest diagnostic test manufacturers in the United States. Quidel received several early and notable authorizations during the pandemic, including early point-of-care and screening claims. This is not presented as evidence of impropriety — Quidel is a major company with significant technical capabilities, and early authorizations for large manufacturers may be entirely justified. But it illustrates the structural problem: **there was no mechanism by which anyone could assess whether review decisions were consistent across applicants.**

When a small company waited months for a response while a large company received rapid authorization, there was no public data to determine whether the difference was explained by submission quality, technical merit, review staffing, or something else. The FDA's answer to this concern — as evidenced throughout these transcripts — was to decline to discuss specific submissions. The effect was to make the consistency question permanently unanswerable. And because the people who would have the standing to raise this concern were the same people who depended on the FDA for their livelihood, the question was rarely raised at all.

The performance data problem compounds this. Throughout the EUA process, companies self-reported their own analytical performance data — including their Limit of Detection (LoD), which is the key measure of test sensitivity. Because different developers used different viral materials, sample matrices, and protocols to establish their LoDs, these self-reported figures were not directly comparable across tests. The FDA recognized this and developed its own SARS-CoV-2 Reference Panel: a standardized set of materials sent to all EUA-authorized molecular test developers, with results to be posted publicly. This was the one attempt at independent, standardized, comparative performance evaluation.

The results were revealing. When tests were evaluated against the same reference material, many showed LoDs dramatically different than what appeared in their EUA labeling. The discrepancies were not marginal — some tests showed reference panel LoDs 10x, 100x, or even 1000x worse than their self-reported EUA LoDs. (See: `FDA SARS-CoV-2 Reference Panel Comparative Data`, compiled by Matt McFarlane, archived in this repository.) The response from industry was not to address the discrepancies but to challenge the panel itself. A law firm representing unidentified EUA holders filed a formal complaint under the Information Quality Act in December 2020, demanding that the FDA remove the comparative data from its website, claiming it was "inaccurate and misleading" and that their clients had suffered "direct harm" from having their tests "inaccurately presented as having a low sensitivity." (See: `2023-09-23_FDA Response Letter - To Compliant regarding FDA Reference Panel from Dec 2020`, archived in this repository.)

The FDA's response letter, dated September 29, 2023 — nearly three years later — defended the scientific validity of the reference panel and protocol. But it also noted that the FDA had stopped distributing the panel when the materials expired and had removed the comparative data from its website "as part of its regular review and updating of COVID-related information because that data has become outdated." The one mechanism that existed for independent comparative assessment of test performance was allowed to expire, the data was taken down, and the practice of self-reported, non-comparable performance claims was effectively restored.

This episode is directly relevant to the refusal-to-answer pattern documented in these transcripts. When the FDA says it "cannot discuss specific submissions," one of the things it is not discussing is whether the performance claims in those submissions are consistent with independent evaluation. The reference panel data suggested they often were not. And the constituency that objected loudest to the publication of that data was not the public — it was the regulated industry, which preferred the opacity of self-reported figures to the accountability of standardized comparison. [RT - don't agree with this paragraph]

### The Broader Context: Discretion Without Accountability
This refusal pattern is one small but telling manifestation of a larger structural problem: the FDA operated during the pandemic with enormous discretion over diagnostic test authorization and very little public transparency about how that discretion was exercised. Submissions were reviewed behind closed doors. Rejection reasons were not published. Timeline expectations were vague. And when developers tried to ask about these things on the one public channel available to them, they were told the FDA could not discuss it.

The cost of this opacity was not abstract. Delayed authorizations meant delayed testing. Delayed testing meant undetected infections. Undetected infections meant preventable transmission and preventable deaths. The FDA's role as the sole gatekeeper for diagnostic tests during a pandemic gave it extraordinary power, and the absence of transparency around how that power was exercised was not a minor procedural shortcoming — it was a structural failure with direct public health consequences.

And the constituency that understood this best — the diagnostics developers, the lab directors, the scientists building the tests — could not say so without jeopardizing their own ability to get tests authorized. The retaliation risk described above meant that the FDA's opacity was self-reinforcing: the less transparent the process, the more dependent developers were on maintaining a good relationship with the agency, and the less likely anyone was to demand transparency. It was a closed loop, and it operated largely unchallenged for the duration of the pandemic.

FDA Commissioner Marty Makary's recent decision to publish drug rejection letters reflects an understanding that transparency about *why* a regulatory agency says no is essential to accountability. The same logic applies to diagnostics — arguably more so, given that during a pandemic the stakes of delayed or inconsistent test authorization are measured directly in lives. The principle should extend to every stage of the regulatory process, including the informal, public-facing engagement that these town halls were supposed to provide.

### What Should Have Happened
A more appropriate version of the "specific submissions" policy would have:

1. **Stated the actual limitation honestly**: "We cannot look up your submission during this call, so we will answer from general policy."
2. **Required generalization, not refusal**: FDA staff should have been directed to reframe specific questions as general ones and provide the best available public answer.
3. **Committed to public follow-up**: Questions redirected to email should have been answered in a public FAQ update, not buried in private correspondence.
4. **Distinguished between confidentiality and convenience**: Protecting a third party's submission details is appropriate. Declining to answer a caller's question about their own submission, on a call they chose to join, is not confidentiality — it is discretion.
5. **Published comparative review metrics**: Aggregate data on review timelines, rounds of questions, and outcomes by submission type would allow the developer community and the public to assess whether the FDA's discretion was exercised consistently. Without this data, concerns about favoritism and retaliation are permanently unanswerable — which benefits the FDA and no one else.
6. **Established structural protections against retaliation**: When the regulated community cannot criticize the regulator without risking its livelihood, accountability depends entirely on the regulator's self-discipline. That is not a system — it is an honor code, and it failed during the pandemic.
7. **Created a non-confidential submission pathway**: The FDA has no mechanism by which a developer can elect to make their submission, and the FDA's review correspondence, public. During a global pandemic, many developers — particularly academic laboratories, university research groups, and public health institutions — would have willingly open-sourced their submissions and invited public scrutiny of the review process if such an option existed. This would have allowed independent assessment of review consistency, surfaced best practices across developers, and demonstrated the FDA's reasoning in real time. The absence of this option was not an oversight — it reflected a system designed around the assumption that all regulatory interactions must be confidential, even when the regulated party would prefer transparency.

### Anticipating the Defense
It is important to engage honestly with the strongest version of the FDA's position before concluding that it was inadequate. The best defense of the FDA's conduct during these town halls would include the following arguments:

**"The FDA was operating under unprecedented resource constraints."** This is true. Tim Stenzel himself stated on multiple calls that his virology branch saw a 60-fold increase in workload. Staff were working around the clock. The surge in submissions was genuinely overwhelming, and the FDA added review staff and reorganized teams to address it. Under these conditions, asking reviewers to also prepare public answers to specific questions on live calls would have been an additional burden.

**Response:** Resource constraints explain slow timelines. They do not explain the choice to refuse rather than generalize. Saying "we cannot look up your submission right now, but here is the general policy on that question" requires no additional staff, no database access, and no case-specific review. It requires only a directive to FDA staff that generalization is the expected response to specific questions. The senior FDA officials on these calls — Stenzel, Lowe, and others — had deep enough command of their own policies and templates to do this routinely. They occasionally did (Category C1 instances in the scoring), proving it was possible. The choice not to do it consistently was a policy decision, not a resource constraint.

**"Changing the system mid-pandemic would have caused further delays."** The argument here is that introducing new transparency mechanisms — published review metrics, non-confidential submission pathways, public follow-up to redirected questions — would have required process development, legal review, and IT infrastructure, all of which would have diverted resources from the core mission of reviewing submissions.

**Response:** Some of the reforms described above would indeed require process development. But the most impactful changes were not process changes — they were posture changes. Directing staff to generalize instead of refuse, committing to post redirected questions as FAQs, and publishing aggregate review timeline data are not infrastructure projects. They are leadership decisions that could have been made in a single directive. The FDA did, in fact, update its FAQ page almost weekly based on town hall questions — this infrastructure already existed. The question is why the answers to redirected questions were not added to it.

**"The confidentiality framework exists for good reasons and cannot be selectively applied."** The FDA would argue that treating all submission information as confidential — even when the submitter would waive confidentiality — is necessary to maintain a consistent legal framework. If the FDA began discussing some submissions publicly while keeping others confidential, it might create pressure on developers to waive confidentiality in order to receive more favorable or faster treatment, which could disadvantage companies with valid trade-secret concerns.

**Response:** This is the strongest argument, and it has some merit. However, it proves too much. The solution is not to maintain blanket confidentiality at the cost of all accountability — it is to create opt-in mechanisms that give developers the choice. A non-confidential submission pathway, where a developer affirmatively elects public review, preserves the default of confidentiality for those who want it while enabling transparency for those who prefer it. During the pandemic, many academic labs, public health institutions, and mission-driven companies would have enthusiastically opted in. The COVID-19 pandemic prompted an extraordinary outpouring of public-spirited scientific work — researchers publishing preprints at unprecedented speed, sharing protocols openly, collaborating across institutions. A non-confidential submission pathway would have channeled that same energy into the regulatory process, and it would have given the FDA access to something it badly needed: external validation that its review decisions were consistent and well-reasoned.

**"The town halls were never intended to be a review forum."** The FDA would point out that the town halls were designed to provide general updates and address general questions, not to serve as an alternative review channel. Developers who needed case-specific guidance had dedicated pathways: pre-EUA submissions, assigned reviewers, and the templates email.

**Response:** This is correct in its framing and misleading in its implication. No one expected the town halls to replace the formal review process. But the town halls were the only public forum in which the FDA's diagnostic review process was subject to external questioning. They were the closest thing to public accountability that existed for the hundreds of life-and-death authorization decisions being made behind closed doors. To argue that they were "not intended" for substantive questioning is to admit that no public forum for substantive questioning was ever intended — which is the core of the transparency problem.

### The Choice of the Term "Town Hall"
It is worth pausing on the name itself. A town hall — in American civic tradition — is a meeting where constituents confront their representatives, ask hard questions, and expect direct answers. The power dynamic is supposed to flow upward: the officials serve the public and are accountable to it. Elected officials who refuse to answer at a town hall pay a political price. The format exists specifically because accountability requires a forum where the powerful cannot control the terms of engagement.

The FDA's "Virtual Town Hall Meetings" for COVID-19 diagnostic test developers bore the name but inverted the dynamic. Consider what these sessions actually were:

- The FDA controlled the agenda, the opening remarks, the order of questions, and the length of the call.
- The moderator opened every session with a preemptive disclaimer that the FDA would not answer the most substantive category of questions.
- Callers identified themselves by name and affiliation, making themselves visible to the regulator they depended on for authorization.
- In the later sessions, the FDA pre-screened emailed questions before the call, declining to address any it deemed "too detailed or case-specific." The questions that made it to the call were, in effect, curated by the FDA.
- When a caller asked something that touched on their submission, the response was some variation of "we are not able to discuss that." The caller had no recourse — no follow-up, no appeal, no mechanism to compel a public answer.

There are ways in which these sessions did resemble a town hall: they were open to the public, they were recorded and transcribed (though often with multi-week delay), and FDA leadership did show up regularly and provide substantive technical updates. Tim Stenzel and Toby Lowe did provide their time and expertise. The opening remarks on each call contained useful policy updates, and some of the Q&A exchanges — particularly in the earlier sessions — were substantively helpful.

But the core function of a town hall — the part where constituents hold officials accountable by asking questions the officials cannot deflect (or may pay a price for doing so) — was systematically disabled. The "specific submissions" policy, the email redirect, the pre-screening of questions, and the power asymmetry between a regulator and its regulated community all combined to produce something that looked like a town hall and functioned like a press briefing. The FDA spoke; the audience listened; questions were taken at the FDA's discretion and answered at the FDA's discretion; and the most important questions were deferred to private channels where the answers would never be publicly visible.

The choice to call these sessions "town halls" was not accidental. It projected openness, accessibility, and accountability — qualities that the FDA has strong institutional reasons to project, whether or not the underlying reality supports them. In his book *Reputation and Power: Organizational Image and Pharmaceutical Regulation at the FDA* (Princeton University Press, 2010), political scientist Daniel Carpenter argues that the FDA became the world's most powerful regulatory agency not primarily through its legal authority but through the cultivation and maintenance of an *organizational reputation* for competence and vigilance. That reputation — carefully maintained across relationships with Congress, industry, advocacy groups, media, and foreign governments — is both the source of the FDA's extraordinary power and the mechanism by which it insulates itself from challenge. Calling a controlled briefing a "town hall" is a small example of reputation management in action: it frames the interaction on the FDA's terms while borrowing the appropriateness of a format that implies accountability.

This matters beyond the town halls themselves. The FDA regulates approximately 20% of the U.S. economy by some estimates, including food, drugs, biologics, and medical devices. Its decisions on diagnostics alone — the subject of these transcripts — directly determined how many COVID-19 tests were available, how fast they reached the market, and whether innovative approaches were authorized or left to die in review queues. And through a process known as regulatory harmonization, the FDA's standards and decisions propagate globally: other nations' regulatory agencies look to the FDA as the benchmark, adopt its frameworks, and defer to its judgments. A decision made in Silver Spring, Maryland about whether to authorize a diagnostic test does not stay in Silver Spring — it shapes what tests are available to patients worldwide.

Balaji Srinivasan — a Stanford-trained engineer (BS, MS, PhD), co-founder and former CTO of Counsyl (a genomics company that at its peak screened approximately 4% of all U.S. births), former general partner at Andreessen Horowitz, and former CTO of Coinbase — has described regulatory harmonization as "perhaps the single worst thing in the world," referring to the mechanism by which U.S. regulators effectively impose their regulatory framework on the entire global market. ([Source: "FDA is broken: How to fix it," Balaji Srinivasan in conversation with Lex Fridman, YouTube.](https://www.youtube.com/watch?v=awIRM3-9JNc)) This characterization is obviously debatable, but it captures a structural reality that is often invisible to those outside the regulated industries: the FDA's decisions have a monopoly-like reach that extends far beyond its formal jurisdiction. Srinivasan was himself considered for the position of FDA Commissioner in 2017, and his trajectory — from biotech CEO to broader technology leadership — has placed him in a position to be candidly critical of the FDA in a way that most current industry participants cannot afford to be, for exactly the reasons described throughout this analysis.

And that is the closing observation. Look at how the FDA ran its "town hall meetings" for diagnostic test developers during the worst public health crisis in a century. An agency with total discretion over authorization timelines, blanket refusal to answer substantive questions on a public call, no published review metrics, no mechanism for developers to opt into transparent review, and a regulated constituency of scientists and entrepreneurs who stepped up to build — alongside vaccines — the single most important intervention available during the pandemic: testing and screening. Look at the gap between how these sessions were presented and what they actually were. Look at the gap between the accountability the term "town hall" implies and the discretion the FDA actually exercised.

Then consider that this agency's decisions propagate to every country that harmonizes with U.S. regulatory standards. The transparency deficit documented in these 100 transcripts is not a local problem — it is a structural feature of the institution that sets the global standard for how drugs, medical devices, and diagnostic tests (basically all important aspects of healthcare) reach patients.

But this is not a counsel of despair. The reforms are not radical and they are not expensive. EUA and diagnostic test submissions — which by definition must contain sufficient data to support authorization — could be made public by default when they are submitted, with a narrow carve-out for genuinely proprietary information (trade secrets, manufacturing processes) that can be identified and redacted systematically. The FDA's review correspondence, questions, and reasoning could be published alongside each authorization decision, as current reform-minded FDA Commissioner Marty Makary has begun doing for drug rejection letters. Aggregate review metrics — timelines, rounds of review, outcomes by submission type and applicant size — could be openly published. A non-confidential submission pathway could be created for developers who choose full transparency. And AI tools, which the FDA itself is beginning to adopt internally, could be applied to minimize the role of individual discretion in review: flagging inconsistencies across reviewers, standardizing the depth and rigor of review, and making the review process auditable in ways that were not technically feasible even a few years ago.

Transparency, consistency, and accountability are achievable. The technology exists, And with AI, is now at our fingertips. The precedents are being set in other parts of the FDA. What is required is the recognition that the current system — in which the world's most consequential regulatory decisions are made behind closed doors, with no public record of reasoning, no comparative metrics, and a regulated constituency that cannot afford to demand better — is not adequate to the stakes. The pandemic made this visible. The question is whether we act on what it revealed.

---

## 2. Appropriateness Rubric

Each identified refusal instance is classified into one of the following categories and assigned an appropriateness score.

### Classification Categories

| Code | Category | Description |
| --- | --- | --- |
| A | Boilerplate Opening Disclaimer | Standard moderator script read at the opening of nearly every session. Not scored (not an active refusal). |
| B | Third-Party Confidentiality Protection | Someone asking about another company's submission. FDA appropriately cannot disclose. |
| C1 | Declined Specifics / Provided Useful General Guidance | FDA declined the specific question but provided substantive general guidance that partially addresses the underlying issue. |
| C2 | Partial Answer with Redirect | FDA provided some general guidance but redirected the substantive question to email or pre-EUA. |
| D1 | Timeline/Status Deflection with Redirect | Developer asks about submission status or timeline; FDA declines specifics but offers a contact channel. |
| D2 | Timeline/Status Deflection (No Substantive Response) | Developer asks about submission status or timeline; FDA declines with no substantive guidance. |
| E | Deflection to Email (No Substantive Answer) | FDA provides no on-call guidance and redirects entirely to offline channels. |
| E2 | Policy/Process Refusal | FDA declines to engage on a generalizable policy or process question using 'specific submission' language. |
| F1 | Blanket Pre-Filter with Email Redirect | FDA pre-screens emailed questions as 'too detailed or case-specific' and promises written response. |
| F2 | Blanket Pre-Filter (No Redirect) | FDA declines emailed question as 'too detailed' without clear alternative. |
|||

### Appropriateness Scoring (1-5)

| Score | Label | Description |
| --- | --- | --- |
| 5 | Fully Appropriate | True third-party confidentiality protection. FDA cannot and should not disclose. |
| 4 | Largely Appropriate | Question genuinely requires case-specific review; FDA provides useful general guidance as substitute. |
| 3 | Mixed | Question is partially answerable in general terms; FDA provides some guidance but also deflects substantively. Alternatively, FDA pre-filters with a promise of written follow-up. |
| 2 | Questionable | Question is generalizable and touches on policy/process that should be publicly answerable; refusal appears to protect discretion rather than confidentiality. |
| 1 | Not Appropriate | Refusal is used to avoid a question the FDA could and should answer publicly. No substantive alternative is offered. |
|||

---

## 3. Classification and Scoring of All Identified Instances

**Total instances identified:** 135
**Boilerplate opening disclaimers (Category A):** 88
**Active refusals (Scored):** 47

### 3a. Boilerplate Instances (Category A — Not Scored)

The following instances are the standard moderator disclaimer read at the opening of each session. They are catalogued but not scored, as they represent institutional policy rather than active refusals.

| # | File | Section |
| --- | --- | --- |
| 1 | 2020-03-02_Virtual Town Hall 0_section-titles.md | #### 1. FDA Guidance on COVID-19 Diagnostic Testing Policy |
| 2 | 2020-04-15_Virtual Town Hall 4_section-titles.md | #### 1. FDA Updates on Testing, Safety, and Collaboration Strategies |
| 3 | 2020-05-27_Virtual Town Hall 10_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Policies and FAQs |
| 4 | 2020-06-03_Virtual Town Hall 11_section-titles.md | #### 1. FDA Updates on Diagnostic Tests and Safety Issues |
| 5 | 2020-06-10_Virtual Town Hall 12_section-titles.md | #### 1. FDA Updates on COVID-19 Testing Procedures |
| 6 | 2020-06-17_Virtual Town Hall 13_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and EUA Processes |
| 7 | 2020-06-24_Virtual Town Hall 14_section-titles.md | #### 1. FDA Guidance on COVID-19 Testing Updates |
| 8 | 2020-07-01_Virtual Town Hall 15_section-titles.md | #### 1. FDA Updates and Guidance on SARS-CoV-2 Testing |
| 9 | 2020-07-08_Virtual Town Hall 16_section-titles.md | #### 1. Updates on COVID-19 Testing and Device Authorization |
| 10 | 2020-07-15_Virtual Town Hall 17_section-titles.md | #### 1. FDA Updates and Q&A on SARS-CoV-2 Testing |
| 11 | 2020-07-22_Virtual Town Hall 18_section-titles.md | #### 1. FDA Updates on COVID-19 Testing Policies and Guidance |
| 12 | 2020-07-29_Virtual Town Hall 19_section-titles.md | #### 1. FDA Updates on Testing Templates and Validation Strategies |
| 13 | 2020-08-05_Virtual Town Hall 20_section-titles.md | #### 1. FDA Updates on EUA Applications and Pooling Strategies |
| 14 | 2020-08-12_Virtual Town Hall 21_section-titles.md | #### 1. FDA Updates on COVID-19 Testing and FAQs |
| 15 | 2020-08-19_Virtual Town Hall 22_section-titles.md | #### 1. Updates on FDA Testing Guidelines and Authorizations |
| 16 | 2020-08-26_Virtual Town Hall 23_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Guidelines and Templates |
| 17 | 2020-09-02_Virtual Town Hall 24_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Development Guidance |
| 18 | 2020-09-09_Virtual Town Hall 25_section-titles.md | #### 1. FDA Updates on COVID-19 Test Development Progress |
| 19 | 2020-09-16_Virtual Town Hall 26_section-titles.md | #### 1. False Positives and Testing Accuracy in SARS-CoV-2 Diagnostics |
| 20 | 2020-09-23_Virtual Town Hall 27_section-titles.md | #### 1. FDA Virtual Town Hall: SARS-CoV-2 Testing Updates |
| 21 | 2020-09-30_Virtual Town Hall 28_section-titles.md | #### 1. Improving Quality and Efficiency of EUA Submissions |
| 22 | 2020-10-07_Virtual Town Hall 29_section-titles.md | #### 1. Positive Predictive Value Challenges in Low-Prevalence Populations |
| 23 | 2020-10-14_Virtual Town Hall 30_section-titles.md | #### 1. FDA Updates on SARS CoV-2 Testing Guidance |
| 24 | 2020-10-21_Virtual Town Hall 31_section-titles.md | #### 1. Addressing False Positives in COVID-19 Testing Strategies |
| 25 | 2020-10-28_Virtual Town Hall 32_section-titles.md | #### 1. FDA Virtual Town Hall: SARS-CoV-2 Test Updates |
| 26 | 2020-11-04_Virtual Town Hall 33_section-titles.md | #### 1. False Positive Risks in Antigen Test Reporting |
| 27 | 2020-11-18_Virtual Town Hall 34_section-titles.md | #### 1. FDA Updates on COVID-19 Testing Authorization |
| 28 | 2020-12-02_Virtual Town Hall 35_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Developments and Priorities |
| 29 | 2020-12-09_Virtual Town Hall 36_section-titles.md | #### 1. Updates on COVID-19 Testing Developments and Priorities |
| 30 | 2020-12-16_Virtual Town Hall 37_section-titles.md | #### 1. FDA Updates on COVID-19 Testing and Authorization Guidelines |
| 31 | 2021-01-06_Virtual Town Hall 38_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Variant Impact |
| 32 | 2021-01-13_Virtual Town Hall 39_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Variants |
| 33 | 2021-01-27_Virtual Town Hall 40_section-titles.md | #### 1. Developing and Validating COVID-19 Tests Amid Mutations |
| 34 | 2021-02-03_Virtual Town Hall 41_section-titles.md | #### 1. FDA Updates and Guidance on SARS-CoV-2 Test Validation |
| 35 | 2021-02-10_Virtual Town Hall 42_section-titles.md | #### 1. FDA Updates and Q&A on SARS-CoV-2 Diagnostics |
| 36 | 2021-02-17_Virtual Town Hall 43_section-titles.md | #### 1. Updates and Guidance on COVID-19 Test Development |
| 37 | 2021-02-24_Virtual Town Hall 44_section-titles.md | #### 1. FDA Updates on COVID-19 Test Guidance and Monitoring |
| 38 | 2021-03-03_Virtual Town Hall 45_section-titles.md | #### 1. FDA Town Hall: SARS-CoV-2 Test Development Updates |
| 39 | 2021-03-10_Virtual Town Hall 46_section-titles.md | #### 1. FDA Updates on At-Home SARS-CoV-2 Test Authorizations |
| 40 | 2021-03-17_Virtual Town Hall 47_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Development and Screening Policies |
| 41 | 2021-03-24_Virtual Town Hall 48_section-titles.md | #### 1. FDA Guidance on SARS-CoV-2 Testing and Validation. |
| 42 | 2021-03-31_Virtual Town Hall 49_section-titles.md | #### 1. Updates on SARS-CoV-2 Test Validations and Mutations |
| 43 | 2021-04-07_Virtual Town Hall 50_section-titles.md | #### 1. FDA Update on COVID-19 Test Authorizations and Validation Guidance |
| 44 | 2021-04-14_Virtual Town Hall 51_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Authorizations |
| 45 | 2021-04-21_Virtual Town Hall 52_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing Guidance and Authorizations |
| 46 | 2021-04-28_Virtual Town Hall 53_section-titles.md | #### 1. FDA Webinar on COVID-19 Test Guidance Updates |
| 47 | 2021-05-05_Virtual Town Hall 54_section-titles.md | #### 1. Updates on FDA COVID-19 Test Submissions and Recommendations |
| 48 | 2021-05-12_Virtual Town Hall 55_section-titles.md | #### 1. FDA Updates on COVID-19 Testing and Submissions Priorities |
| 49 | 2021-05-19_Virtual Town Hall 56_section-titles.md | #### 1. FDA Virtual Town Hall: SARS-CoV-2 Testing Updates and Questions |
| 50 | 2021-05-26_Virtual Town Hall 57_section-titles.md | #### 1. Guidance on Validation and Study Design for SARS-CoV-2 Tests |
| 51 | 2021-06-02_Virtual Town Hall 58_section-titles.md | #### 1. Updates on SARS-CoV-2 Test Development and Safety Concerns |
| 52 | 2021-06-09_Virtual Town Hall 59_section-titles.md | #### 1. Updates on SARS-CoV-2 Testing and Mutations Impact |
| 53 | 2021-06-16_Virtual Town Hall 60_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Prioritization |
| 54 | 2021-06-23_Virtual Town Hall 61_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Testing and Innovations |
| 55 | 2021-06-30_Virtual Town Hall 62_section-titles.md | #### 1. Developing and Validating SARS-CoV-2 Diagnostic Tests: Updates and Guidance |
| 56 | 2021-07-14_Virtual Town Hall 63_section-titles.md | #### 1. Updates on SARS-CoV-2 Testing Development Challenges |
| 57 | 2021-07-28_Virtual Town Hall 64_section-titles.md | #### 1. FDA Updates on SARS-CoV-2 Test Validation Efforts |
| 58 | 2021-08-04_Virtual Town Hall 65_section-titles.md | #### 1. FDA Updates on EUA Tests and Prioritization Policies |
| 59 | 2021-08-11_Virtual Town Hall 66_section-titles.md | #### 1. Expanding Access to High-Volume COVID-19 Diagnostic Testing |
| 60 | 2021-08-18_Virtual Town Hall 67_section-titles.md | #### 1. FDA Priorities for SARS-CoV-2 Test Development |
| 61 | 2021-08-25_Virtual Town Hall 68_section-titles.md | #### 1. SARS-CoV-2 Test Development and Validation Updates |
| 62 | 2021-09-08_Virtual Town Hall 69_section-titles.md | #### 1. COVID-19 Test Development and Authorization Guidelines Presentation |
| 63 | 2021-09-22_Virtual Town Hall 70_section-titles.md | #### 1. Updates on SARS-CoV-2 Testing and EUA Reviews |
| 64 | 2021-10-06_Virtual Town Hall 71_section-titles.md | #### 1. COVID-19 Test Updates and EUA Prioritization Changes |
| 65 | 2021-10-21_Virtual Town Hall 72_section-titles.md | #### 1. Updates on COVID Test Development and Prioritization Strategies |
| 66 | 2021-11-17_Virtual Town Hall 73_section-titles.md | #### 1. Updates on COVID-19 Test Guidance and Priorities |
| 67 | 2021-12-01_Virtual Town Hall 74_section-titles.md | #### 1. COVID-19 Test Guidance Amid Omicron Variant Concerns |
| 68 | 2021-12-15_Virtual Town Hall 75_section-titles.md | #### 1. SARS-CoV-2 Diagnostic Challenges and Omicron Variant Updates |
| 69 | 2022-01-12_Virtual Town Hall 76_section-titles.md | #### 1. FDA Guidance on Laboratory Modifications to Authorized COVID-19 Tests |
| 70 | 2022-01-26_Virtual Town Hall 77_section-titles.md | #### 1. FDA Updates on COVID-19 Test Development Guidance |
| 71 | 2022-02-09_Virtual Town Hall 78_section-titles.md | #### 1. FDA's Transition Plan for COVID-19 Diagnostic Test EUAs |
| 72 | 2022-02-23_Virtual Town Hall 79_section-titles.md | #### 1. COVID-19 IVD Town Hall Updates and FAQs |
| 73 | 2022-03-09_Virtual Town Hall 80_section-titles.md | #### 2. FDA Warns Against Unauthorized COVID-19 Diagnostic Tests |
| 74 | 2022-03-09_Virtual Town Hall 80_section-titles.md | #### 7. Guidance on Enrichment Approaches for COVID-19 Test Evaluation |
| 75 | 2022-03-23_Virtual Town Hall 81_section-titles.md | #### 9. Live Q&A Guidelines and Participant Instructions |
| 76 | 2022-04-06_Virtual Town Hall 82_section-titles.md | #### 1. SARS-CoV-2 Testing Updates and FDA Transition Guidance |
| 77 | 2022-04-20_Virtual Town Hall 83_section-titles.md | #### 1. FDA Updates and Guidance on COVID-19 Test Development |
| 78 | 2022-05-04_Virtual Town Hall 84_section-titles.md | #### 1. SARS-CoV-2 Test Updates and Counterfeit Concerns |
| 79 | 2022-05-18_Virtual Town Hall 85_section-titles.md | #### 6. Challenges in Flu Test Validation and FDA Recommendations |
| 80 | 2022-06-29_Virtual Town Hall 88_section-titles.md | #### 1. FDA Updates on Monkeypox and COVID-19 Testing |
| 81 | 2022-06-29_Virtual Town Hall 88_section-titles.md | #### 7. EUA Requirements for OTC SARS-CoV-2 Antigen Tests |
| 82 | 2022-07-27_Virtual Town Hall 89_section-titles.md | #### 1. FDA Updates on COVID-19 and Monkeypox Testing |
| 83 | 2022-10-26_Virtual Town Hall 96_section-titles.md | #### 1. Updates and Guidance on Monkeypox and COVID-19 Testing |
| 84 | 2022-11-30_Virtual Town Hall 98_section-titles.md | #### 1. Monkeypox and COVID-19 Testing Updates and EUA Plans |
| 85 | 2022-12-14_Virtual Town Hall 99_section-titles.md | #### 1. Mpox and COVID-19 Diagnostic Test Updates and Guidance |
| 86 | 2023-01-11_Virtual Town Hall 100_section-titles.md | #### 1. 100th Virtual Town Hall: Updates on Mpox and COVID-19 Testing |
| 87 | 2023-02-15_Virtual Town Hall 101_section-titles.md | #### 1. Updates on EUA Processes for Mpox and COVID-19 |
| 88 | 2023-04-26_Virtual Town Hall 103_section-titles.md | #### 1. Guidance for Transitioning SARS-CoV-2 Test EUAs |
||

**Total boilerplate instances:** 88

### 3b. Active Refusals (Scored)

#### Instance 1: 2020-03-02_Virtual Town Hall 0_section-titles.md
**Line range:** 295-302
**Section:** #### 13. Approved IDT Lots and Clinical Testing Requirements
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** FDA gave a substantive general answer to part of the question: if the lot was qualified by CDC under its EUA, the lab does not need to submit its own EUA. But FDA declined the specific request for which IDT lots are approved and where to find that list, saying it was still working on how to make that information public and directing the caller to stay tuned and contact IDT. This is an active refusal because the core public-information request was not answered on-call, though some useful guidance was provided.
**Speaker refusing:** Tim Stenzel
**Speaker asking:** B.J. Dacall

**Excerpt:**
B.J. Dacall:
Hello. We have a question about the IDT lots. Which ones are approved and where do we find that list of approved lots of IDT? And can you elaborate around that EUA that you authorized if we're buying an approved lot from IDT? We're good to start clinical testing without validation.

Tim Stenzel (FDA IVD Director):
So if it's a lot that's been qualified by the CDC under their EUA authorization you do not need to submit your own EUA. We are still working on how we're going to make that information public. So stay tuned and stay in touch with IDT. At this moment that's what I recommend. They were expecting that they might receive some inquiries about this. And as of now we only have one kit left to announce but again stay tuned.

B.J. Dacall:
Thank you.

---

#### Instance 2: 2020-03-06_Virtual Town Hall 00_section-titles.md
**Line range:** 330-337
**Section:** #### 15. CDC N Gene Selection and FDA EUA Review
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** This is a real but limited refusal: FDA declines to answer the specific question of why CDC selected the N gene and redirects that portion to CDC. However, FDA does provide useful generalized guidance by noting alternative designs can proceed under the issued guidance policy and by explaining that CDC's assay targeted multiple regions within the N gene, including novel-specific and pan-SARS targets. Substantive context is provided alongside the deflection.
**Speaker refusing:** UnknownSpeaker (FDA)
**Speaker asking:** Inca Wachaski

**Excerpt:**
Inca Wachaski:
Yes, I just had a question regarding why the CDC decided to go with the N gene while, for example, the WHO decided to go with other gene targets and other kind of unintelligible using other targets.

UnknownSpeaker (FDA):
Sure, we are working with developers around the world to bring on additional manufacture kits that are of different design. And certainly an LAK provider that wants to develop their own task base, based on an alternate design that you read about. You have that pathway through the guidance policy. The Guidance policy that we issued last Saturday. But, you know, stay tuned as far as additional manufacturers. As to why the CDC chose just the N gene, I would direct those questions to the CDC. I'll just say that our review of their EUA package was excellent. We had no issues with the design. They did target two different unintelligible of the N gene. So a three different targets, two are specific for the novel and then one was for a more pan SARS region.

Inca Wachaski:
Thank you very much.

---

#### Instance 3: 2020-04-15_Virtual Town Hall 4_section-titles.md
**Line range:** 153-157
**Section:** #### 8. Process for Interagency Review of Rapid Serological Tests
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This is an active refusal because FDA declines to answer the public-disclosure part of the question, saying it has not yet decided how the results will be made public and that it will work with individual developers on that. FDA does provide some useful general guidance about the program's purpose, target tests, and that FDA will handle the regulatory review of resulting data, but the specifics of public availability and pathway details are deferred. The refused core question is a generalizable process question, not a third-party submission issue, and FDA could likely have generalized more if a policy had been set.
**Speaker refusing:** Tim Stenzel
**Speaker asking:** Hanna Fish

**Excerpt:**
Hanna Fish:
Hi. Thank you. I think this might have been addressed in an earlier question but I just wanted to get clarification with regard to the voluntary program with the NR agency review of the serologic test unintelligible. Can you now elaborate on what that review process is and how that information is going to be made available to the public and what we can expect as far as review of complexity of those tests?

Tim Stenzel (FDA IVD Director):
Sure. This is primarily intended for rapid serological tests. It is an interagency program that's designed to do testing with actual patient samples. Voluntary program, we have yet to decide on how this - the result of this may be formally made public. We will, you know, situations work with individual developers on that. The sort of regulatory review of any data that may come out of this is going to reside with the FDA. So if a sponsor would like to - test developer would like for the test results from this interagency collaboration to be used for a formal submission to the FDA that is going to be entirely possible and we'll work with - the FDA will work with those individual developers to determine how that would happen. We are working on further announcing how that potential pathway so stay tuned that should be forthcoming in the not too distant future.

---

#### Instance 4: 2020-04-15_Virtual Town Hall 4_section-titles.md
**Line range:** 282-286
**Section:** #### 16. FDA Guidance on 3D Printed Nasopharyngeal Swabs Pending
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** FDA does not refuse the topic entirely; it explains that public-facing guidance for 3D-printed nasopharyngeal swab design/manufacturing is still being developed and gives substantive general context about the different design and manufacturing scenarios and responsibilities. The active limitation is that FDA cannot yet provide published standards or finalized recommendations because they are still under scientific, policy, regulatory, and legal review. Useful generalized guidance is provided, and the caller is invited to follow up for updates.
**Speaker refusing:** Sara Brenner (FDA)
**Speaker asking:** Jane Aya

**Excerpt:**
Jane Aya:
Hi. Thank you so much. My question is for Dr. Brenner again related to the 3D printed Nasopharyngeal swabs. I'm wondering if there are any published FDA guidance or standards documents that are relevant specifically to the design and manufacturing of Nasopharyngeal swabs.

Sara Brenner (FDA):
Yes. That's a great question and that's sort of what we are working on now. We are doing sort of a scientific structuring of what our recommendations would look like and the different to consider that will then go through policy, regulatory and legal review. So in terms of guidelines we do not have any that are public-facing yet at this point and we are aware that there are several different scenarios by which a 3D printed Nasopharyngeal swab, for example, might be created including the entities who are involved in the designing of more of the software side, those who are actually in the manufacturing world either in a small way for local distribution or distribution with another institution. And then potentially commercial entities who would be producing at high volumes and distributing. So each of those entities will have some responsibility. But on the design side that you asked about we are trying to figure out what the role of us and our collaborators and partners for example through the MOU with NIH and VA and American Mates would be with regards to helping to vet the designs themselves. So stay tuned for information forthcoming on that. And if you would like to email me directly please do and we can keep you looped in as that conversation evolves.

---

#### Instance 5: 2020-04-29_Virtual Town Hall 6_section-titles.md
**Line range:** 126-145
**Section:** #### 6. Path Forward for Point-of-Care Serology Test Authorization
**Category:** B — Third-Party Confidentiality Protection
**Appropriateness Score:** 5/5
**Rationale:** This passage contains a real but limited refusal on the second part of the question: FDA declines to provide public updates on in-progress or rejected serology submissions because those details are often proprietary and confidential. That refused core question is about other companies' nonpublic submission status and denial information, which squarely fits third-party confidentiality protection. FDA did, however, provide substantive answers on the first part about point-of-care policy, so the refusal is narrow and appropriate.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Daniel

**Excerpt:**
Daniel:
All right. Thanks Tim. I appreciate the weekly public information sharing session that you guys are doing. It's kind of a two-part question. Do you envision - what do you envision as the path forward indirect for unintelligible serology test kits. Currently it's only acceptable to use at high-complexity labs. Some developed countries have gone as far as making these available for home use, if I understand correctly. When do you see FDA policy changing to allow utilization of these tests at, at least point of care level? That concerns me from a commercial standpoint, in my opinion could reduce the RNG effort in development or investment activity for these test kits. So that's part one. The part two is, we've seen so many unverifiable claims by suppliers of serological tests, companies claiming their unintelligible application or unintelligible distribution notification has been submitted or is in progress, unintelligible transparency, could FDA maybe consider publishing the status of developers that have unintelligible? Of course, we can see you approved one, but more, I guess related to in progress or that have been rejected, so that we know which manufacturers or suppliers to focus on or consider unintelligible?

Tim Stenzel (FDA IVD Director):
Okay, so the two questions are, I think, point of care, the need for that, and FDA status of submissions of serology tests. So, we do make the serology tests that have been authorized clear - that have notified us but haven't been authorized clear. We also have now made clear both the authorized and the notifications pathway what clinic or what clinical environment they can be tested in, whether it's high complexity or moderate complexity or point of care -- or what we call waved, with a W. So, H, M or W. It is more challenging to provide updates other than that because that is oftentimes considered proprietary, confidential information. If a test is denied, authorization, if under the NCI umbrella pathway, that I mentioned earlier, if you do not meet the performance bar, they will be removed from the unintelligible and potential other further actions may be taken. So those tests that may have been denied may be removed from the unintelligible list, and that will be out - that will be one way that we make this information public as soon as we make that decision. I hope that answered your question.

Daniel:
That did. And I guess maybe about the first part of the question, what the path forward may be.

Tim Stenzel (FDA IVD Director):
Yes. So, the pathway - if you come to us through our EUA template address, what the path forward may be. Yes, so the pathway, if you come to us through our EUA templates and ask what is required for a point-of-care validation, we will provide that to you. We are in the final stages of drafting the serology template, which will lay out these things a little bit more clearly for all to see, and will be posted publicly when they are signed off. FDA

Daniel:
Okay, thanks.

Tim Stenzel (FDA IVD Director):
Our policy is that we will authorize point-of-care serology, and other point-of-care tests, if they meet the expectations in working with our reviewers for those applications. So, there is no prohibition about this - there is also no prohibition about home collections or home testing. It's just that in the home collection, home testing situation, those require EUA authorizations. They require specific accuracy tests to be done, so that we know in those environments accurate results can be obtained -- and the same goes for the point-of-care setting. So it is policy that we will authorize these if the correct studies are performed and the accuracy is there that we can authorize them.

Daniel:
Thank you sir. Thank you.

---

#### Instance 6: 2020-04-29_Virtual Town Hall 6_section-titles.md
**Line range:** 240-256
**Section:** #### 11. FDA Guidance on 3-D Printed Nasopharyngeal Swabs
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This passage contains a limited active refusal on two fronts: FDA declines to give a firm release timeline for the forthcoming swab guidance and says it does not yet have a definitive answer on the registration/listing question. However, FDA does provide meaningful general context about the guidance being prepared, the internal clearance process, and an upcoming public discussion forum, so the response is not a total non-answer.
**Speaker refusing:** Sara Brenner (FDA)
**Speaker asking:** Ted Riff

**Excerpt:**
Ted Riff:
Hi, yes, thank you. Good afternoon. My question is for Dr. Brenner if she is still available, or, Tim, if you could answer. At a town hall...

Tim Stenzel (FDA IVD Director):
She's probably better answering almost anything.

Ted Riff:
At a town hall two weeks ago it was mentioned that an FDA recommendation pertaining to 3-D printing of nasopharyngeal swabs. I was wondering whether we will be seeing that document soon or if it's still in progress? And specifically during this public health emergency, will FDA expect the hospital to register a list of unintelligible as a manufacturer if it prints the swab only for the internal hospital use of its own patients?

Tim Stenzel (FDA IVD Director):
Go ahead Sara. FDA

Sara Brenner (FDA):
So those are great questions and I know we have discussed the issue of 3-D printed nasopharyngeal swabs and other types of swabs on this town hall call for many weeks now, so I thank everyone for their patience. What I can share at this point is we most certainly are preparing formal information or guidance. I don't want to be too prescriptive of what form it will take, but we are working on, what I believe the community will find to be very informative based on the questions that have come in so far. And then there's a process that we go through internally to have that verbiage cleared, it will probably be out of our office this week and moving up through the necessary channels with posting hopefully as early as next week. I'm not making that promise but we certainly have been striving to get all of this information together and presented to the public as quickly as we can, because I know there are many, many questions and many people trying to address shortages through these very creative manufacturing means. So that's one thing I'll say. The two other points on that. One is that we do intend to have an open discussion, a town hall- like forum, where folks who are interested in a dialogue with FDA and other federal partners can join in sort of an open-dialogue and those of you who have reached out by email following this town halls would certainly be welcome and any others would be welcome as well. So we're shooting to get that conversation set up and broadcast to the appropriate parties at some point next week. Again, thanks for your patience and stay tuned. The last piece on this and related to that is our internal team, which includes subject matter experts, policy folks, regulatory experts, legal folks, the whole gamut, we've been following the literature closely, including data that has been FDA submitted to us for analysis and data that's been submitted to federal partners, including NIH and VA, too as, I believe most folks know we have an interagency partnership with -- on 3-D printing and additive manufacturing. And so there are many experts across FDA our agency partners who are trying to stay ahead of the curve with regards to what's being manufactured and advertised and marketed and used out in the field. So, in coordinating with those folks and stakeholders that have reached out to FDA and other parts of the government, we're looking for a sort of harmonized way that we can all work together safely and get products out there that are going to be effective and safe, and then also where that fits into our regulatory framework given that these traditionally have been class 1 exempt devices. To your question about registration enlisting, I'm not sure that we have a definitive answer on that yet, but it is something that will go into the guidance or information that we put out. We definitely are aware of that issue and that question.

Ted Riff:
Thank you for your answer and I really appreciate all the work you and everyone at FDA have been doing -- and for these town halls. Thank you so much.

---

#### Instance 7: 2020-05-20_Virtual Town Hall 9_section-titles.md
**Line range:** 90-151
**Section:** #### 5. Status of Serology Test Approvals and Review Process
**Category:** B — Third-Party Confidentiality Protection
**Appropriateness Score:** 5/5
**Rationale:** This is an active refusal because the caller asks about the approval timing and status of specific named companies' serology tests, and FDA declines to provide submission-specific information on the call. Stenzel gives some general context about the updated serology review process and says decisions will become public soon, but for the specific tests he redirects the caller to email and notes any shareable information may be confidential. The refused core question concerns nonpublic details and status of other companies' submissions.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** William Lamparder

**Excerpt:**
William Lamparder:
Yes. I have a question in regards to certain test kits being approved. It's been a few months since they submitted application for the Zhejiang Orient Gene Biotech company from AYTU bioscience and I was wondering why or when that will be approved and also, they have another test kit, Biolitics. They're both over 95 percent accuracy and they're also approved by the FDA in other countries as well. I'm just wondering what's the hold up?

Tim Stenzel (FDA IVD Director):
Are these serology tests?

William Lamparder:
Yes.

Tim Stenzel (FDA IVD Director):
Okay.

William Lamparder:
Sorry.

Tim Stenzel (FDA IVD Director):
So, we've obviously updated our guidance on serology tests recently and…

William Lamparder:
Yes. I… FDA Townhall

Tim Stenzel (FDA IVD Director):
…put into place processes and procedures. So, you should expect that in the very near future that decisions will be rolling off and that we'll make those decisions public. You know, the original, let's see, March 16th guidance allowed tests of this sort if they met the criteria that was set forth in the guidance to notify us.

William Lamparder:
Yes.

Tim Stenzel (FDA IVD Director):
We would post that notification and to be legally marketed. We're meeting the public health need at that time.

William Lamparder:
Okay.

Tim Stenzel (FDA IVD Director):
And now the update is for us to review those applications and make decisions. So, we're now focused on that. So, you should see a lot of progress in the near future.

William Lamparder:
Okay. Because I know they did a review by a private party, I believe it was, and to meet your guidelines and everything and they proved that it was almost 100 percent accurate with the Zhejiang Orient test.

Tim Stenzel (FDA IVD Director):
Okay.

William Lamparder:
And then these other tests from Biolitics in Singapore are excellent as well. Yes. I just know a lot of people are wondering what's going on?

Tim Stenzel (FDA IVD Director):
Yes. No. I can understand that. Like I said, you will be getting to see a lot of decisions going forward… FDA Townhall

William Lamparder:
How long do you think it will take for them to - I mean, it's been, what, a month or two now.

Tim Stenzel (FDA IVD Director):
So, if it's a specific test or tests, if you send us an email with the templates email address, we will try to give you as much information we can. If it's considered confidential information that may be…

William Lamparder:
Oh, I'm sorry. I almost forgot one other thing. The AYTU Bioscience, they're working with Sire Cyanide and Sterling Medical on the Helight. I don't know if you heard of that, the Helight Products where it kills the virus inside your body. They submitted for a patent and FDA approval. I don't know if you can even say anything about that or have any info on that?

Tim Stenzel (FDA IVD Director):
Yes. That would not be in our office. Not be in the IVD Office. So, again, if you send an email to the templates email address, we can potentially direct you to somebody that might be able to answer some questions about that. Thank you.

William Lamparder:
Great. Thank you so much for your time. Take care.

---

#### Instance 8: 2020-05-20_Virtual Town Hall 9_section-titles.md
**Line range:** 186-232
**Section:** #### 7. Validation of Dry Swabs for At-Home COVID-19 Testing
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** FDA does limit what it will say publicly, stating it has reached the limit of what can be publicly shared about dry-swab home-collection validation. However, the agency also provides some substantive generalized guidance: existing FAQ material, possible use of stability data, likely focus on resuspension validation, and that actual patient positives may not be needed. FDA partially answers the technical question but redirects the specifics to direct email follow-up.
**Speaker refusing:** Tim Stenzel (FDA IVD Director) and Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Eric Konick

**Excerpt:**
Eric Konick:
All right. Tim, Toby, thank you for hosting us, and thank you for everything you're doing during this pandemic. My question is related to unobserved at- home collection for RT-PCR assays and specifically related to dry swabs and how to obtain positive samples. So, I think as you're probably aware, at least in the Seattle area, we're seeing a huge decrease in the number of positive patients, so actually getting positive samples is challenging, especially for, you know, at-home collection, so would the agency accept dry swabs that have been collected from negative – SARS-Co-V-2 negative participants that are spiked VTM or UTM as a positive sample?

Tim Stenzel (FDA IVD Director):
So are you an IVD kit developer or a lab?

Eric Konick:
Oh, I'm sorry. University of Washington.

Tim Stenzel (FDA IVD Director):
Oh.

Eric Konick:
So academic medical center.

Tim Stenzel (FDA IVD Director):
Yeah, so I understand, and it's nice to hear that the prevalence of acute COVID-19 is relatively low in the Seattle, Washington area. Below 2 percent was the last numbers I saw, so I can certainly understand the challenges of that. There are some innovative things that we can do that might be able to help you in those areas where incidence is lower. I'm not sure what I can say publicly right now, but we are working to address that very topic. So, again, your name is – is this Alex, or who is this? FDA Townhall

Eric Konick:
This is Eric Konick.

Tim Stenzel (FDA IVD Director):
Eric. I'm sorry I didn't catch your name.

Eric Konick:
Oh, no worries.

Tim Stenzel (FDA IVD Director):
And we know each other, so you're welcome to email me directly or email our template's email address and ask about this, but I have some thoughts that could help you and potentially others, and we want to make that – I just don't know what can be publicly shared at this time. The dry swabs and home collection of dry swabs is very interesting, and we are working in collaboration with others to make this available, and Toby may know a little bit more about what we can share right now publicly, and Toby – I'm not sure. I've reached the limit of what I know I can publicly talk about, but, Toby, do you have anything to add.

Toby Lowe (FDA IVD Assoc Director):
Yeah, we'd love to talk to you about the specific that you're looking to do and see if we can take at that and see what we can work out with you. We do have some information on the FAQ about validation material, but it will really be dependent on your specific situation and, you know, what you're looking to validate, whether you're validating your assay as a whole or if you're validating home collection, and we may have some – you know, we do have some stability study data that you can leverage for home collection, and then we would need to see, you know, what other data you already have and how that can all be used.

Tim Stenzel (FDA IVD Director):
I believe – and this is ringing a bell now. I believe what is the – sort of the only piece that might be missing from this is validation of resuspension of a FDA Townhall dry swab with your particular assay or assays that you want to use with this, but much of the rest of the work has already been accomplished, and rights are allowed to the previous data that Toby mentioned about stability. So I think there's a pretty clear pathway that is least burdensome here and pretty efficient. I think, if I remember correctly, we just want to make sure from the dry swab you have a good method of resuspending and it performs well in your hands, and at that point, coming off the swab in that situation, I don't believe actual patient positives – individual, you know, positive patients aren't needed for that, but let's double-check on that, okay?

Eric Konick:
Great. Thank you for your help.

Toby Lowe (FDA IVD Assoc Director):
And you can email either of us directly, or if you have a lead reviewer that you're working with, we can work with you on that.

Eric Konick:
Great. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Yes.

---

#### Instance 9: 2020-05-20_Virtual Town Hall 9_section-titles.md
**Line range:** 288-343
**Section:** #### 9. Concerns About Small Diagnostics Companies and Test Approvals
**Category:** B — Third-Party Confidentiality Protection
**Appropriateness Score:** 5/5
**Rationale:** This is a real active refusal: FDA repeatedly declines to discuss whether a named company has submitted, the status of its review, or movement on its specific saliva test. The refused core question is about a third party company's nonpublic submission and authorization-related details, which squarely fits confidentiality protection. FDA does provide a little general reassurance that confidentiality is not delaying reviews and that innovative developers are welcomed, but the main refusal is still an appropriate bar on discussing another company's specific EUA matters.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director); Tim Stenzel (FDA IVD Director)
**Speaker asking:** Larry Lines

**Excerpt:**
Larry Lines:
Hey there. I just had a question – I'm no professional or anything, but I've been following along with a local USA company in Utah called Co- Diagnostics, and they were talking about having a dual serology and PCR test, and those tests really interest me because, like I said, I'm no professional, but I've been reading up a lot. FDA Townhall And most of the tests seem to be having some of their false results due to the primer dimers in the RT PCR chain reaction process, and that is a big part – they have, you know, intellectual property on their co-primers which eliminates that. They also are working with an oil lab DNA with their co- primers to try to work for a saliva test, which I haven't heard much about. They submitted that mid-April. I'm just really curious. That's a local company. It's a little small. I'm worried they may be overlooked because of small, but from the research I've done, their intellectual property and could really help, so I would just love to hear back from that.

Tim Stenzel (FDA IVD Director):
So, yeah, there is information that might be considered confidential. The…

Larry Lines:
That's what I worried about. You know, I'm local. I'm right by Utah, and I know dozens of people who can't get tests, and, you know, I'm with no media, and I just worry about my friends and family where these good tests may be being held up, you know, the spit tests which have these co-primers which would reduce a lot of these primer dimers which is a very predominant cause of these false positives in these RT PCR chain reaction. And I'm just worried that some of this whole business confidentiality is really overtaking the safety of these tests. As long as – you know, they've been bragging this new test could be serology and RT PCR and that could be the gold standard for our company.

Toby Lowe (FDA IVD Assoc Director):
I think… Crosstalk

Tim Stenzel (FDA IVD Director):
So yeah… FDA Townhall

Toby Lowe (FDA IVD Assoc Director):
Go ahead, Tim.

Tim Stenzel (FDA IVD Director):
No. No. You go ahead.

Toby Lowe (FDA IVD Assoc Director):
So the confidentiality that Tim's mentioning is not holding up any reviews. We just are not able to provide any information about any specific companies that may or may not be seeking EUA until that is public, so we just can't share any of those details on these calls, but we are definitely open to any new technologies or improvements on existing technologies, and we encourage all of those companies to come talk to us.

Larry Lines:
Is there any movement on their oil DNA lab saliva test using co-primer technology to reduce false positives?

Toby Lowe (FDA IVD Assoc Director):
Again, we can't comment about any specific companies or…

Larry Lines:
You comment on AYGU a second ago which is confusing to me.

Toby Lowe (FDA IVD Assoc Director):
No, I don't think we commented anything specific to that company or test driver.

Larry Lines:
I understand. You know, I don't want to take up any more time. I feel like you guys won't answer my question specifically. Thank you very much.

Coordinator (FDA):
Thank you very much.

Tim Stenzel (FDA IVD Director):
Let me just – hold on. Let me just complete the loop on this. Toby was right. We welcome all developers. If - we do not speak specifically about any FDA Townhall developers that haven't given us permission to speak or we haven't taken public action. However, we do work with those developers, and we are working very closely, and if there's any innovative technologies that will assist us, we've authorized now over 100 tests, and that represents tens of millions of testing opportunities…

Larry Lines:
May I say one thing?

Tim Stenzel (FDA IVD Director):
Yeah.

Larry Lines:
Over those hundreds of tests, I do believe it's about 40 or 50 percent coming from the same four or five companies, and that's just what worries me. You know, seeing such a pandemic and you have a small company that has the potential to grow, I just do worry it may be overshadowed. For the good of the community just based off of, you know, large corporate greed and – that is my main point. You know, I do believe in their technology very soundly. You can speak to the stock price, which I have no interest into it as well. I just want to get good tests, you know, made in America out to my friends and family, and, you know, I just worry. I have a lot of elderly family, but, again, thank you for your time. I understand if you can't get any more into detail. I do not want to take up one more minute of your time. Thank you.

Tim Stenzel (FDA IVD Director):
Okay. Let's move to the next question please.

---

#### Instance 10: 2020-05-20_Virtual Town Hall 9_section-titles.md
**Line range:** 429-439
**Section:** #### 13. FDA Guidance on VTM and Fair Developer Practices
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This is a real active refusal because the caller asks a generalizable policy/process question—how a manufacturer without a 510(k) can get VTM to market quickly—and FDA declines to provide the anticipated specifics on-call. Stenzel gives limited useful context that FDA recognizes the unmet need, is handling inquiries through the templates email, and is considering a broader approach, but then explicitly says he 'can't say anything else at this point' and tells listeners to stay tuned. The question is not about a third party's nonpublic submission, and FDA could likely have generalized more public guidance.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Sara Clark

**Excerpt:**
Sara Clark:
Hi, Tim. Thank you for taking my last question. It's my understanding that FDA will be issuing some guidance on VTM in the near future but currently FDA Townhall doesn't have anything out. I was wondering how a manufacturer who does not have a 510-K can get the product on the market as soon as possible.

Tim Stenzel (FDA IVD Director):
Yeah. This is clearly an unmet need, providing VTM, and we've been taking inquiries at the template's email address and addressing them as quickly as possible, and we are considering ways in which we can make this more broadly applicable, and I really can't say anything else at this point, other than to stay tuned, because this is a hot topic, and we hope to provide additional information in the not-to-distant future.

Sara Clark:
Okay. Thank you. I appreciate your time.

Tim Stenzel (FDA IVD Director):
You're welcome. All right. That was the last question, I think. I want to follow up on a conversation that happened earlier on this call, and that is I do want to emphasize that we do work with all developers and all developers are treated fairly and equally, and we make decisions as fast as we can. Our decisions are sometimes complicated, and they're all aimed at providing products that consumers and clinicians and health-care systems can rely on, and we're very open to new ideas. I think as clearly expressed today and all previous Townhalls and some of the innovative approaches we have taken in this pandemic from looking at ways to really expand authorization for home collection and being open to home testing and open to over-the-counter, and so I just want to emphasize that. There was a caller who mentioned a specific company, and it's publicly known that we have authorized tests already on April 3rd from Co- Diagnostics, and everybody gets a fair shake with us. That's absolutely how we roll. So with that, Irene, I turn it over to you. FDA Townhall

---

#### Instance 11: 2020-06-10_Virtual Town Hall 12_section-titles.md
**Line range:** 201-262
**Section:** #### 11. Antigen Test Availability and Contractual Restrictions Concerns
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** This is a real active refusal because the caller asks a broader, generalizable policy/fairness question: whether FDA allows an EUA holder to use contractual terms to lock out future competing antigen tests. FDA does not answer that public policy/process question on the call, instead saying the Agency will look into it internally and talk offline, while only offering the general point that FDA wants more antigen tests authorized. The concern could reasonably have been generalized without discussing confidential submission details.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Ken Kim

**Excerpt:**
Ken Kim:
Hi. I'm a physician and actually quite involved in the clinical trial space. My NWX-FDA OC question revolves around antigen. I want to know how many companies that you - the FDA is aware of that is developing antigens that already applied for EUA for antigen. And I'm aware of the Quidel EUA antigen approval. The reason why I ask that is I wanted to get antigen to actually use that as a diagnostic tool of Quidel, but then they wanted - they're mandating their contract that we have to exclusively use Quidel and cannot replace it for the next three years unless there's a double-blind randomized trial showing this other agent head-to-head is better. And I said, number one, most things are going to be EUA-approved. Number two, no one's going to do a head-to-head to the initial trial and three years is ridiculous. So basically, wanted to create a monopoly to lock in people and it's very frustrating and I'm actually a little worried that a Quidel person that's on this phone will also retaliate because now they will not even - they won't sell me kits because I won't sign that if we supply. I was wondering is the FDA allowing that to happen and is there any way you can actually lock other people out with that kind of language?

Tim Stenzel (FDA IVD Director):
Let me just make sure that I understand your question. You want to obtain antibodies or antigens?

Ken Kim:
Antigens for...

Tim Stenzel (FDA IVD Director):
Antigens?

Ken Kim:
... for a serology test. No, antigen, not serology. Antigen is different from NWX-FDA OC serology, right?

Tim Stenzel (FDA IVD Director):
So the antigen… Crosstalk

Toby Lowe (FDA IVD Assoc Director):
You're looking to use the actual antigen test? You're not looking to source the antigen ; is that correct?

Ken Kim:
Correct. When we want to use the antigen test for diagnostic purposes and there's only one FDA EUA-approved antigen, to me as a physician, I've been doing clinical trials of one over 700 clinical trials, antigen is going to be a very good screen test that could actually replace TCR for screening, but we need more antigen tests. I think we need more antigen tests, not antibody tests. So I've requested Cordel...

Tim Stenzel (FDA IVD Director):
Okay. Okay.

Ken Kim:
... to use this. Yes. So...

Tim Stenzel (FDA IVD Director):
Okay.

Ken Kim:
... I have two questions… Crosstalk

Tim Stenzel (FDA IVD Director):
So you're having trouble acquiring those Cordel tests?

Ken Kim:
Yes. Well, because they're refusing because they want me to sign a contract that NWX-FDA OC says that I would not go to a different antigen test if something comes up for three years unless there's a double-blind randomized trial head-to-head against their antigens, which to me is not - to me, I think, is not right in this emergency environment. So they are using their EUA to actually, you know - I'm at a standstill because I would like to buy their - I'd like to buy lots of their kits, but they won't sell them to me because I won't sign that.

Tim Stenzel (FDA IVD Director):
Okay. I understand better. Thanks for explaining that.

Ken Kim:
Yes. So that's the problem. It's really frustrating because, you know, on the fields we definitely want to use this as a point of care test. It's great. But I don't know whether this is legal for them to take an EUA and actually create a market lock that anyone who starts using these we're locked in with them for three years. We can't use another antigen test when another one gets approved. You see what the problem is?

Tim Stenzel (FDA IVD Director):
Yes. Yes, no, I see. Let me note this and we'll look internally at this unintelligible...

Ken Kim:
I can talk offline.

Tim Stenzel (FDA IVD Director):
Yes, talking offline may be helpful too.

Ken Kim:
Yes. I - you know, I think - I typed it up in the email. So if you email me, I could set up a call, we could talk about it and I could send you the language, but I think it's a problem because that shouldn't - that - we're trying to actually do good things for the country in terms of diagnosing disease and you can't get situations where someone is going to lock you into something that, you know, NWX-FDA OC isn't really credible. Three months from now there will be another antigen that might be better and we can't - we wouldn't be able to switch to it legally.

Tim Stenzel (FDA IVD Director):
Okay. I certainly hear what you're saying and understand what you're saying and, you know, it's probably best if internally at the Agency we look into this and talk with you further. There's a lot of listeners on this call and, you know, there's obviously a good bit of transparency that goes on because there's a lot of listeners on this call. So - and we make ourselves available right now week in, week out here on this call. So I appreciate your calling. I would just add that we're very interested in additional antigen tests to be authorized. There seems to be a real shortage of developers in this space. So I would encourage anyone who wants to develop an antigen test, that's - they come talk to us and let's see what we can do because we are very interested in adding to the number of antigen tests.

---

#### Instance 12: 2020-07-08_Virtual Town Hall 16_section-titles.md
**Line range:** 78-88
**Section:** #### 3. Updates on At-Home Testing Availability and Timelines
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This is a real active refusal because FDA declines to provide the requested timeline for release of the at-home testing template. FDA does give some substantive context—that home testing is a priority and they are working on home collection and molecular at-home testing—and offers a contact path for feedback, but the core timeline question is not answered.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director); Tim Stenzel (FDA IVD Director)
**Speaker asking:** Mark Heckman

**Excerpt:**
Mark Heckman:
Yes good morning Tim and Toby. How are you today? I'm just following up on my question that I asked a couple weeks ago. You may have answered it last week's call. I was not on it but just wondering when the template for full at-home testing is going to be released? We still have a lot of people out there that need to be tested quickly and right now the way that the big-box tests are going and things like that with there's logistic issues getting swabs, reagents and things like that we feel a full at-home test right now is ready to go. So I just have to hear you input on that. And if you answered it last week just say that answered it last week and I'll hang up.

Tim Stenzel (FDA IVD Director):
Well it is a priority and we're very interested in home testing. And we are still working on the home testing home collection for serology but we can provide feedback to folks who contact us, same for molecular at home testing. Toby can you give any other more specific updates than I did? NWX-FDA OC US

Toby Lowe (FDA IVD Assoc Director):
No unfortunately we can't share specific timelines but we are working to get that out as quickly as possible.

Mark Heckman:
Thanks very much.

---

#### Instance 13: 2020-09-02_Virtual Town Hall 24_section-titles.md
**Line range:** 306-340
**Section:** #### 12. FDA Policy on LDT Enforcement and Safety Communications
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** This is a real active refusal because the caller asks a generalizable policy/process question about FDA/OIVD enforcement authority and practices for LDTs after the HHS statement, and FDA explicitly says it will not comment specifically on that statement. FDA offers only high-level generic remarks about communicating safety information and then declines to provide any timeline for further information. The issue is broader policy, and FDA could reasonably have generalized its answer publicly.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Alexander

**Excerpt:**
Alexander:
Hi, thanks. I had a question regarding some of the prior enforcement actions that have been taken by your office. And I'm specifically thinking Page 24 back to one that happened on I believe, July where FDA indicated that there were certain laboratory tests that had been reviewed by the FDA and FDA, according to statements, determined that there were significant problems and warn the public against their use, I believe is Chemisys and Mayo Clinic Arizona. My question though, relates to kind of backward enforcement and forward enforcement as relates to LDTs under the new HHS policy. Is your office kind of one, as relates to prior enforcement actions, does your office believe that it can still kind of warn folks against the use of particular test and two on a kind of ongoing or prospective basis. What does enforcement look like from OIVD against certain COVID tests that FDA believes may not be effective or safe or adequate for use?

Tim Stenzel (FDA IVD Director):
Yes, no, that's a great question. I think Toby is going to respond.

Toby Lowe (FDA IVD Assoc Director):
Yes, so you're basically asking, you know, sort of what our processes for when we determine what to communicate in terms of the sorts of safety issues, is that correct? Page 25

Alexander:
Yes, or even more basic, you know, what are the new rules of the road for enforcement for that decision?

Toby Lowe (FDA IVD Assoc Director):
When you say, for that decision, what are you referring to?

Alexander:
Sorry for the HHS communication I suppose two weeks ago now that FDA had limited authority over LDTs to open some, perhaps.

Toby Lowe (FDA IVD Assoc Director):
Right. So I think, you know, Tim mentioned last week on the call, that we weren't necessarily commenting on that statement on that call last week. And I think that, unfortunately, we're still not going to be commenting specifically on that statement today. In sort of more general terms, when we are determining what to communicate about a specific test, we look at what the safety implications are, the public health implications, based on the information that we have on hand and then we put out information that is available to be publicly distributed. And we put out that information that we think is necessary for Page 26 healthcare providers or laboratories or patients, the appropriate audience to be aware in a specific situation.

Alexander:
And one quick follow up if I may. Is there an expected timeline as to when your office believes that it may provide more information on the reactions of statement weeks, months?

Toby Lowe (FDA IVD Assoc Director):
I'm not able to provide that at the moment.

Alexander:
Okay, thank you.

Toby Lowe (FDA IVD Assoc Director):
Yes.

Operator (FDA):
Thank you. Next question comes from Kaumudi. Your line is open, sir.

---

#### Instance 14: 2020-10-07_Virtual Town Hall 29_section-titles.md
**Line range:** 99-118
**Section:** #### 5. Saliva Sensitivity and Antibody Immunity Testing Challenges
**Category:** B — Third-Party Confidentiality Protection
**Appropriateness Score:** 5/5
**Rationale:** This is a real active refusal because FDA explicitly declines to share data it has seen, citing company-confidentiality. The refused core question is whether FDA can make available data from named developers about saliva antigen testing, which is nonpublic company-specific information. FDA does provide some general technical guidance about saliva antigen workflow and considerations, but the central refusal is still a confidentiality-based decline regarding third-party data.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Wendy Strongen

**Excerpt:**
Wendy Strongen:
Thank you. In a prior call you said that experts have concerns about whether saliva would be sufficiently sensitive for antigen testing. Was that based on any data that they had actually collected or that FDA has seen? Or was that just a general concern?

Tim Stenzel (FDA IVD Director):
So we have seen data to this effect. And it does, you know, obviously alert us to a potential issue. There was also a recent press report about two different developers who reported they have decided and rapid antigen tests could not - have decided not to pursue saliva as a sample type. So the FDA remains open to it. But we want to see the data to support its use.

Wendy Strongen:
Yes. I know the press report you're familiar - that you're referring to. But it doesn't say anything about what was tried or what the method was. Does the FDA have any data that you can make available to manufacturers who are interested in this?

Tim Stenzel (FDA IVD Director):
We cannot share any confidential - any company confidential information with the public. Those companies are welcome to share that. So, you know, the companies were named in that press report so you're free to approach them and ask them for anything that they might have that might help you. But typically, you know, a rapid antigen test, the sample type, you know, whether it's, you know, nasal swab or nasopharyngeal swab, it would go directly into some sort of lysis buffer, you know, and then onto the device. And you can imagine the similar workflow for saliva. I mean that would just be where I would start. FDA Virtual TH But, you know, picking the right antigen target might be important in saliva and also, how you might process that saliva sample in that first buffer might be important in order to free up and preserve those protein antigens you're targeting.

Wendy Strongen:
Great. Thank you. I have one additional question about antibody testing. The CDC says on its Web site that if someone has antibodies they likely have some degree of immunity to SARS-CoV-2. Would you allow a home test to have a claim of some degree of immunity conferred by antibodies without the manufacturer actually going out and doing studies, which would obviously be very, you know, difficult and time consuming to actually prove immunity?

Tim Stenzel (FDA IVD Director):
Yes, that's a different - a difficult situation to prove. First of all, if you just do one serology test in a low percent positive population the likelihood of a false positive result is not insignificant and should be reckoned with. And we've talked long ago on this meeting, on this call, about the potential to do not just one but a second serology, different serology test to try to, you know, firm up that exposure history. And then the question about - even about - well, you know, about immunity is obviously an important one but very difficult to prove. And in order to make claims about that in which somebody might rely on that information and - in going about their life, and potentially putting them at risk of being let's say reinfected, let's just assume they've had a prior infection but we've already had reports of reinfection. And until we firm up that understanding that's something that we're not going to be able to authorize at this time unless the data's supported.

Wendy Strongen:
Thank you. FDA Virtual TH

---

#### Instance 15: 2020-10-28_Virtual Town Hall 32_section-titles.md
**Line range:** 135-160
**Section:** #### 5. Equipment and Software Requirements for Reference Panel Validation
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** FDA answers the general reference-panel question by explaining that the panel should be run in line with the authorized instructions for use. However, when the caller asks about the pending amendment adding other equipment, FDA declines to address the specifics of that test and redirects those questions to the review team. Useful generalized guidance is provided alongside a narrow refusal of case-specific details.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Gustavo Heteray

**Excerpt:**
Gustavo Heteray:
Hi. Good afternoon. My name is Gustavo Heteray and my question is in reference to using a real-time PCR equipment to do the reference final validation. So we're trying to help a Chinese company called Enshare Biotech comply with the required reference panel. As such we have a question regarding the devices that may be used to perform the test. We have at our disposal an ABIs 7500 Fast Dx REAL-Time PCR instrument and a SLAN-96 P REAL-Time PCR system. However the IFU in the EUA mentions an ABIs 7500 REAL-Time PCR system. Is it possible to perform the reference panel using the ABIs 7500 Fast Dx REAL-Time PCR system or the SLAN-96 REAL-Time PCR system as we do not have access to the one mentioned in the IFU?

Toby Lowe (FDA IVD Assoc Director):
So if you're referring to performing the reference panel as a condition of the authorization which is typically what the - how the reference panel is currently being used then the performance of the reference panel does need to be in line with the instructions for use in - of the authorized test so that the - so that it does - it is reflective of the test that was authorized.

Gustavo Heteray:
Oh okay. They have introduced an amendment including the equipment that I have mentioned. But the amendment has not been reviewed. I guess maybe pending the reference panel results?

Toby Lowe (FDA IVD Assoc Director):
So I'm not able to answer any questions about a specific test. Generally we do expect the reference panel to be performed using the authorized test. If there is any specific questions about any, you know, an amendment or any authorizations there those should go directly to the review team.

Gustavo Heteray:
Okay then we'll find an equipment as mentioned in the IFU. And in regards to the software does the software have to be the exact same software or could be - could it be a more updated software on the equipment?

Toby Lowe (FDA IVD Assoc Director):
It should be the test as authorized.

Gustavo Heteray:
Okay all right well thanks a lot. That answers my question.

Toby Lowe (FDA IVD Assoc Director):
Great.

Coordinator (FDA):
Our next question comes from Arvita Tripati. Your line is open.

---

#### Instance 16: 2020-11-18_Virtual Town Hall 34_section-titles.md
**Line range:** 75-103
**Section:** #### 4. Progress and Challenges in COVID-19 Test Authorizations
**Category:** B — Third-Party Confidentiality Protection
**Appropriateness Score:** 5/5
**Rationale:** This is a real active refusal because FDA explicitly declines to identify which rapid antigen test sponsors were denied authorization. The refused core question concerns nonpublic company-specific regulatory outcomes of other firms' submissions, which fits third-party confidentiality protection. FDA does provide some general explanation about authorization pace and review factors, but the specific refusal is to disclose other companies' denied submissions.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Lewis Perlmutter

**Excerpt:**
Lewis Perlmutter:
Yes, again, I iterate the same thing that you talked about the home testing. Can you elaborate? Can you say which company is producing that? And I think you said it was a molecular test, correct?

Tim Stenzel (FDA IVD Director):
Yes, it was a molecular test. It was a real time loop mediated amplification reaction. So it runs in about 30 minutes.

Lewis Perlmutter:
Okay and can you mention the company or I guess I missed that.

Tim Stenzel (FDA IVD Director):
It was Lucira. L-U-C-I-R-A. Lewis Perlmutter Yes and then I have some comments about the rapid antigen test. It's been a while since we've had, or something that's come on the market for rapid antigen test. It just seems that it takes so long to get these tests approval. It is because of the negative or the false negatives and false positives that's inhibiting these tests to get marketed or what is the problem?

Tim Stenzel (FDA IVD Director):
So rapid antigen tests are a priority in the office. And we've authorized, I believe, seven to date. I'll say that we have denied authorizations to some. I'm not going to mention names. Confidential information. The scale of authorization and the rate of authorization really depends on, you know, the applications we receive. Are they complete? Is the test accurate? And can they authorize it without asking the sponsors for additional work? The antigen team, I think, has done a pretty good job when something is able to be authorized to move it through quickly and get it authorize.

Lewis Perlmutter:
Tim, where can I find the seven that have been approved?

Tim Stenzel (FDA IVD Director):
So we have an EUA, IVD, FDA page that lists for all of the test types, not just the antigen tests, but the molecular and serology tests as well. And shortly after authorization, we post a new test. So that - I don't know if the Lucira test of yet public there, but we, in this case with the FDA, did issue a press release to announce that.

Lewis Perlmutter:
Just a thought. I'm just wondering, hopefully with the new task force coming through in a month or so, that they develop a national testing policy, because that's really badly needed. Because there doesn't seem to be standardized very much. And I just wondering what your thoughts are on that?

Tim Stenzel (FDA IVD Director):
Yes, no, I'm a good soldier. So I've been asked to speed access to accurate testing through the authorization process. And end of the day, we've authorized almost 300 tests of all now different shapes and types. And, you know, I think it's upwards of 600 through additional notification pathways. So almost 1000 tests to date, which is my role and the federal government, so it's the others in the task force, perhaps, who could better address that question.

Lewis Perlmutter:
I appreciate that Tim. Anyway, thanks very much.

---

#### Instance 17: 2020-11-18_Virtual Town Hall 34_section-titles.md
**Line range:** 228-253
**Section:** #### 11. FDA Guidance on Antigen Tests and Validation Requirements
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** This is a real but limited refusal: FDA says it may not be able to share details about the first home test authorization due to proprietary confidentiality reasons. However, Tim Stenzel then gives substantial generalized guidance on the actual policy question—authorization depends on data, adults may swab children in studies and at home if supported by data, and new specimen types like buccal swabs require validation. The refusal is narrow and accompanied by useful public guidance.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Franco Calderon

**Excerpt:**
Franco Calderon:
Thank you for taking my call. So my question is going to have a couple of parts. So the first part has to do with the institution that I am teaming up to do my clinical validation. It's an academic institution here in Texas. And they are performing the clinical part quite well. It's going kind of slow because of the low incidence. But they have a question regarding the cross reactivity information that we need to report. Does FDA provide any resources, perhaps panel, for the cross reactivity information part of the test? So that's one. The other question is if we're going to be making a claim for OTC use, I noticed that on the last test, or the first home test that FDA approved, the youngest age is, I think, 14 years old. So does that mean that we need to show that if we're going to be making that age claim, does that mean that younger children cannot perform a, let's say, a nasal swab by themselves if they're being coached? How does that work? Further to the specimen question, if we want to show that the test works with nasal swabs, let's say buccal swabs, do we have to submit the information for those too? I'm guessing that we do so.

Tim Stenzel (FDA IVD Director):
So, a couple of questions. You're developing a kit and it sounds like it's for a molecular? Is that correct?

Franco Calderon:
No, I'm sorry. This is an antigen. It's a pure, naked paper strip.

Tim Stenzel (FDA IVD Director):
Okay, until you asked about the buccal swab, I was thinking molecular and then I was thinking antigen to molecular and so the buccal swab would obviously be a new sample type and would need to be validated by you and performance acceptable for us to authorize for an antigen test. And the same thing goes for a molecular. But I was curious. As far as - I will need to dig into some of the details about the first home test authorization. But I may not be able to share, due the proprietary confidentiality reasons. But I'll say in general - and I don't know of anything that's not acceptable about this first home test, but in general, we make decisions based on data, of course, if not in all cases. So we definitely have allowed children to be tested. And we allow an adult present to swab in clinical studies and to support an authorization. I will say, though, you know, if a developer has not shown that an adult in the home can adequately swab a child in the home, then we wouldn't have data to make an assessment about whether or not that can be authorized because there is an age and this is, you know, we have pediatrician on our staff. There's an age at which we're just not sure if somebody can accurately self- collect and run a test uniquely so. But as far as the collection part of the home test, if a developer comes in with data that shows an adult can swab a child, then we'll - and the data looked good, obviously, then we will authorize that as well, whether it's OTC or prescription, it doesn't really matter. And as far as cross reactivity goes for antigen test, I think I would - if you could, and Toby may know, but my recommendation is to send something to our template's email box about that. I don't know if we have a list of providers, we can share that, make samples available or not. We are sometimes hesitant if we can't vouch for the quality of those panels from the FDA perspective and - but there may be resources out there that we can point you to as a possibility. But of course, with molecular tests, you know, we have allowed in silico analysis. It's much harder to do that sort of thing, obviously, with antigen tests. Toby, do you have anything to add about any of those questions and my answers?

Toby Lowe (FDA IVD Assoc Director):
No, I think just what you said, there's information in the template about performing those studies and if you need assistance, finding where to get, you know, where to buy organisms to test for cluster activity, you can send it to the mailbox and we'll see if we have anyone that we can point you to.

Franco Calderon:
Okay. Thank you. Just to that to that last comment. I do have an assigned reviewer. So would it make sense for me to just communicate with that person?

Tim Stenzel (FDA IVD Director):
Yes.

Toby Lowe (FDA IVD Assoc Director):
Yes.

Franco Calderon:
Okay. Great. Thank you.

---

#### Instance 18: 2020-12-16_Virtual Town Hall 37_section-titles.md
**Line range:** 105-109
**Section:** #### 6. Access to Approved EUA Submissions for Test Developers
**Category:** B — Third-Party Confidentiality Protection
**Appropriateness Score:** 5/5
**Rationale:** This is a real active refusal: FDA directly says it has no plan to post approved EUA submissions and explains that those files contain proprietary information that is unlikely to be made public. The refused core question is whether developers can access other sponsors' approved submissions, which squarely concerns third-party nonpublic application contents. FDA does provide alternative public sources like decision summaries, IFUs, and authorization letters, but the core refusal is a confidentiality-based denial of access to other companies' submissions.
**Speaker refusing:** Tim Stenzel
**Speaker asking:** Piero Holitecio

**Excerpt:**
Piero Holitecio:
Thank you for taking my call. I would like to ask if the actual submission of the tests that have been approved, are available to us to read and preen information off of? I think it would be very valuable for us as developers - it would cut through a lot of our red tape to - trial and error, to send in our pre- EUAs. And it would dot the I's and take care of our development timeframe if those EUA actual submissions that have been approved already, not the ones that are pending approval, are available to developers. Thank you.

Tim Stenzel (FDA IVD Director):
Yes. I'm not an expert on this particular topic. I'll just say that we don't have any plan of posting that information. In almost all cases, if not all cases, there is proprietary information in those applications. That is not - that is unlikely to ever be made public. And sponsors, test developers appreciate that. You understand that in order for us to make the very best assessments, we ask for this kind of - some of this kind of information. And that would be a proprietary formulation so that we can understand. I'll also say that this maybe the first time that I'm mentioning this on the town hall call, so we do ask for all developers to provide us as much detail about their test design and designs. And so we do ask for say for molecular assays, primary and probe designs. Our office, on a monthly basis, is looking at the database of mutations, at least that are linked to the US. We are - since we have those primary and probe sequences, our bio-pharmaticians are scanning the mutation data and flagging anything that could be of concern. We have already initiated reaching out to some developers. And we are, you know, in dialog with them. If there is something that is existent that would potentially lower the performance of the test we will work with those developers in every situation and make that information public as soon as possible. We probably are looking at communicating this program more formally in the not too distant future. So we are doing this as a service. It's not something that we normally do. But in this pandemic we feel it's important. We would encourage all developers, of course when a molecular developer say comes in with primary probe sequences, we are asking for both inclusivity testing even if in only in silico as well as cross-reactivity testing at least in silico for some things. But we do really want that test developer's post authorization to be surveying. We would encourage them and recommend to them that they survey indication standards and for any prevalent mutations that might exist in the population at least for the US, that might affect the performance in their assay. So more to come on that later. We, in our office, have traditionally even from before the pandemic, have made decision summaries available for all of the authorized tests, whether at the PMA, whether at the 510k or de novo. We do this after it's been scrubbed for confidential information from the developers, to provide just the sort of information that you're asking about that's most relevant. And we believe in our - in the IFUs and the letters of authorization and some of them post-market commitments, that we are providing this same sort of clarity to the development community. And if you have questions about designing something or something about your test that - even after you've reviewed previous authorizations, you're always welcome to come into our templates email box and ask those questions. And we'll be as forthcoming about, you know, answering your question as we can. Again, we treat others - a significant amount of company confidential information that we guard and we protect because that's part of our duties and it's also the law. All right. Thank you. And I think we can go to the next question.

---

#### Instance 19: 2021-01-27_Virtual Town Hall 40_section-titles.md
**Line range:** 327-352
**Section:** #### 9. Developing Variant Testing Strategies for Antigen and Serology Assays
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** This is a real active refusal because FDA explicitly says it is 'not ready to give recommendations right now' on variant testing for antigen and serology submissions. However, Tim Stenzel provides substantial generalized guidance: FDA is actively developing an approach, may update templates and authorization letters, is considering in silico and limited wet testing, and expects developers to raise their thoughts and likely engage in post-market monitoring. The refused core question is a general policy/process question, and FDA gave meaningful public context instead of simply pushing the matter offline.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Misha Lee

**Excerpt:**
Misha Lee:
Yes, hi. Thank you for taking my question. Following up on the topic of mutation testing, I know it was indicated on the last town hall that FDA is proactively reaching out to already authorized molecular developers to conduct additional testing. My question is for manufacturers that will be submitting their new like point of care nuclear protein based antigen EUA, is there any additional variant testing required as part of the initial EUA submission?

Tim Stenzel (FDA IVD Director):
So let me, you know, ask the question of you, because I am going to reach out to all of the EUA authorized antigen test developers. You know, can you use say even activated antigen or virus and/or a radiated virus from BEI, because this - if we can - if antigen tests can - those antigen tests that can use this and of course a lot of this is going to be comparing to the original strain that was deposited at BEI and we typically think of that as anything comparing to that. But if an antigen test is amenable for use of inactivated virus that makes all of our lives a lot easier as far as testing reactivity and inclusivity. And it's my understanding that the UK variants have been deposited BEI and I'm just going to be double checking with them that they are planning to inactivate that. So we haven't figured that all out yet. We just know that at least for key variants we're going to start wanting to know, you know, if there's any loss of sensitivity with those variants. And we're trying to figure out the very best way to do this and using live virus in a lab is not ideal. But if inactivated virus can be used then potentially panels can be distributed to developers and to tests that are already on the market.

Misha Lee:
Thank you very much.

Tim Stenzel (FDA IVD Director):
But stay tuned is the bottom line. But obviously, the mutation - variants of interest right now to keep up with health importance, are the UK variant, the South African variant and now what's called the Brazilian variant. Okay?

Misha Lee:
Okay. So in terms of testing the type of variants, are those the only two that we should be testing or what is the best way to keep current on the type of variant?

Tim Stenzel (FDA IVD Director):
So we are working through this process. So in all likelihood we'll be updating template; in all likelihood we'll be updating letters of authorization of these going forward; in how best to do this. So, and we're just at the beginning stages of thinking through this. It would be ideal if we can be using in silico analysis to some degree. We use it of course for molecular. But if we could start using it for antigen and serology tests. So we are going to start beginning to ask developers how they think they can monitor variants for variants of concern. And obviously I've mentioned three variants - South African, UK and Brazilian. But there could be - and those are important because they appear to be more infectious and could have potential impact on the vaccine efficacy. So - but there could be one or more variants out there that in accumulation, could start to depress the sensitivity of assays. There's even some cases we're thinking in serology examples, typically for neutralizing antibodies, where there could potentially be false positives. Right? So you have neutralizing antibodies to, you know, a prior infection but not to, you know, some of the variants. So all I can say right now is this is one of our top priorities if not the top priority right now, for our office and our center and the ability of the agency as well, to try to figure out how to best do this. So certainly we have been having lots of conversations. So in all likelihood as I said, we're going to be asking - doing a template update, asking developers, you know, what are their thoughts for how they can monitor for impact of variants and work with us essentially, to figure this out. And whether modeling for antigen and serology tests can be used, is too early for me to say how useful that is to figure out if a variant could have an impact. And then if there is a potential impact, for molecular tests already we have been asking the last developers to do blood testing to make sure that the variants don't mess with the sensitivity of the assay. And we want to keep that kind of wet testing to a minimum if possible, because there are just so many variants obviously.

Misha Lee:
Okay. Thank you very much. Sorry. You had mentioned that there's - that you guys are working on updating the template. So before that update do you suggest that we reach out to the EUA, you know, just to obtain specific guidance on variant testing?

Tim Stenzel (FDA IVD Director):
You can, but I don't think we're ready to give recommendations right now. We're focused on, you know, we're doing it for molecular. And all molecular developers do this in the process of submitting their application. They survey the landscape. I just - since we don't have a solution that's really workable yet, for antigen and serology, I don't want to be making recommendations about that. But other than to - we want to know what your thoughts are about these. And as we develop our knowledge base and information base and as we discover ways to do this better, we may update those recommendations. But certainly, if you want to bring it up I'm not holding you back. I mean I think it's a sign of a good developer that brings up these issues. I just don't want to hold back authorization until we can figure out how to do this right. We are likely to, in addition to template asking, for what your thoughts are on how to monitor the impacted variants we are probably going to put that into a commitment for post-market monitoring. And if you discover something, to contact us and we'll figure out the next steps. And the other thing is - these are just thoughts, nothing's settled, nothing's determined yet. But I think it is an important topic and it doesn't hurt to bring this topic up as we try to work through it.

Misha Lee:
Thank you very much Dr. Stenzel.

---

#### Instance 20: 2021-02-03_Virtual Town Hall 41_section-titles.md
**Line range:** 297-346
**Section:** #### 12. Reporting and Risk Mitigation for At-Home Antigen Testing
**Category:** E — Deflection to Email (No Substantive Answer)
**Appropriateness Score:** 2/5
**Rationale:** FDA acknowledged the importance of the at-home reporting question but said it was still 'struggling' with implementation and did not provide concrete public guidance on what personal data, reporting elements, or confidentiality approach would be required. Instead, Tim Stenzel redirected the caller to email the templates mailbox and Dr. Sara Brenner for further help. Although he later gave some substantive discussion on prevalence as a possible mitigation, the refused core question in this passage is the reporting requirements for at-home antigen tests, which were not meaningfully answered on-call.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Gloria

**Excerpt:**
Gloria:
Hello. Yes, I have a question on the reporting. So we are developing and antigen test and we are willing to provide it with in a mobile app for guiding the users through the test and for reporting the result could also be an option if we're reading the HHS specifications for COVID-19 data reporting it's really oriented to point of care testing. So we are wondering if there is some guidance in case of reporting for an at home test what would be needed on personal data and on data of the user? And also do we have to encounter a mechanism to yes predict and to say something about the prevalence in the region the consumer is behaving so you could give an indication on the, yes the PPV and the NPV so it's a more yes, just trusting the results?

Tim Stenzel (FDA IVD Director):
I did - I'm not sure I caught the last part of your question. The first part I caught was you're developing an app to guide the person through the testing and to report the results that you aren't using the smart phone to actually read the result but maybe you are?

Gloria:
No it's readouts on the reader. Yes.

Tim Stenzel (FDA IVD Director):
The reporting is guiding and reading - guiding them through and reporting the results.

Gloria:
Yes.

Tim Stenzel (FDA IVD Director):
And then you want to know what are the point of care or home recommendations for reporting and how you do it and how you insure confidentiality…

Gloria:
Yes.

Tim Stenzel (FDA IVD Director):
…and mindful of HIPAA requirements. And those are all really important questions. And the, you know, the facts are that we are still struggling with how to do that reporting well. Even if you have an app to report to connecting it to the database and getting authorizations from all of the states, you know, and the federal government to be able to do that and connect it all up report results that is a mission in process. And…

Gloria:
Yes.

Tim Stenzel (FDA IVD Director):
…we're fortunate to have our office, the office I lead is a chief medical officer who is an expert in this, Dr. Sara Brenner who's actually on loan right now to HHS to work primarily on this reporting question. And it's - I know that there's Web sites and there's documents that are available but I don't have them at my fingertips, Sara would. It's probably something Toby and Irene that we want to add to our slide deck that we provide at the town hall, some materials around our reporting and since we've had a number of questions about reporting and those links to important documents that can guide developers. But we're very interested in working with you. So if you send us an email to the templates email address and you ask for that to be forward into Dr. Sara Brenner, B-R-E-N-N-E-R, Sara will get back to you with as much as she can tell you about the process now.

Gloria:
Okay. And my second then on the prevalence could it be maybe it was already discussed earlier that Rx the prescription and the mitigation of risk does FDA also considers a prediction of the prevalence of COVID-19 in the region where the app is installed and a user is doing the test as a mitigation of risk? So yes if it is low prevalence region then already results might be less supportive that are and that kind of mitigation, is that's open for discussion?

Tim Stenzel (FDA IVD Director):
It's an interesting question. Certainly in a low prevalence population your risk - your PPV is going to go down, your Positive Predictive Value's…

Gloria:
Yes.

Tim Stenzel (FDA IVD Director):
…going to go down but your NPV is going to go up. But we've heard that false positives with antigen tests especially in point-of-care congregant settings where then they move a patient based on their test results into a COVID ward can expose someone who doesn't really have COVID to SARS and developing COVID. So it's a complex thing. The other thing is and obviously if you're prevalence is higher then it's kind of the reverse. But, you know, one of the challenges with that is you'd have to have - first of all you'd have to have, you know, even to consider it you'd have to have really good prevalence data and up to the minute prevalence data which we don't have. And then you'd have to have an adaptable system that had some geo-locator that says well you're in this ZIP Code and this is the prevalence and so this is the number to use, you know, for your mitigation. So it's an interesting idea and I don't want to give you any more definitive - I don't want to give you any definitive answer on it. We're always open to new ideas.

Gloria:
Okay.

Tim Stenzel (FDA IVD Director):
So if you want to propose this in a pre-EUA or an EUA as the mitigation please do. I can't guarantee the results. But like I said, you know, this town hall is to help educate folks about our current thinking. But we learn just as much from developers, you know, as you do from us. So, you know, thanks for asking a creative question.

Gloria:
Okay. Thank you.

---

#### Instance 21: 2021-02-10_Virtual Town Hall 42_section-titles.md
**Line range:** 375-382
**Section:** #### 19. Sample Size Requirements for Antibody Test Kit Approvals
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** The caller asks a generalizable policy question about the sample-size expectations for the forthcoming home-use antibody template. FDA declines to say what will be in the template and offers mailbox follow-up instead of a public answer. The refused core question is public policy/process guidance.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Shannon Clark

**Excerpt:**
Shannon Clark:
Hello, again. Shannon Clark with UserWise Consulting. Question about - I'm really looking forward to this template coming out for this home-use test kits for antibody testing. Do you expect that it's going to require a sample size of 30 participants for prescription-only; then 150 participants, or 100 sessions with some pairs for over-the-counter? Because I've received conflicting emails from the FDA implying that perhaps OTC could be achieved with a sample size as low as 30.

Toby Lowe (FDA IVD Assoc Director):
I don't - I can't speak to what exactly will be in that template. Hopefully, we will be able to get it out soon so that we will be able to speak to it more definitively. But if you do have specific questions as you're planning your approach now, you can send them to the mailbox. And if you're having difficulty getting a FDA Townhall uniform answer, you can flag the question for Tim and me, and we'll take a look into it.

Coordinator (FDA):
Your next question is from Jackie Chin. Your line is open.

---

#### Instance 22: 2021-02-24_Virtual Town Hall 44_section-titles.md
**Line range:** 498-505
**Section:** #### 18. Clarification on Sample Requirements for Submission and Clinical Data
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** FDA declined to comment on a specific recently published IFU because the exact test was not identified, which is a limited refusal on the specific example raised. However, Toby Lowe did provide substantive general guidance on the underlying sample requirement: FDA wants a complete data set of 30 specimens, with any additional fresh samples on top of the 30 and the remainder of 30 fresh to be collected post-authorization. The core question was largely answered with useful generalized guidance.
**Speaker refusing:** Toby Lowe
**Speaker asking:** Sue Hart

**Excerpt:**
Sue Hart:
Hi Toby. Thanks for taking my question. I think part of this was already answered and don't want to belabor this. It was around the antigen performance and the five prospective samples. I just want to know if you could clarify so the samples could be collected retrospectively or prospectively but then in addition the submission would need to include those five prospective samples without transport media and then while you're continuing to get the 30 positives throughout. And then I am just looking at a recent IFU that was just published I think this week where it's intended for fresh samples but the clinical performance is all on banked samples, all unfrozen samples so I was just curious if you could talk a little bit about that?

Toby Lowe (FDA IVD Assoc Director):
Right so we would want to see a complete data set of 30 specimens. Without knowing exactly which test you're referring to I can't comment on the ISU but we would want to see, you know, complete data set of 30. And then if you have additional fresh that would be on top of the 30 and we would ask for the rest of the 30 fresh to be in the post authorization. NWX-FDA OC

Sue Hart:
Okay. Okay great. Thank you.

---

#### Instance 23: 2021-03-10_Virtual Town Hall 46_section-titles.md
**Line range:** 75-100
**Section:** #### 3. Updating FDA Website with Molecular Test Data
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** The caller asks when molecular test data and a January-authorized test's panel results will be posted on FDA's website. FDA does not provide a concrete answer or criteria, saying only that the next update is being worked on, no target date has been formalized, and to 'stay tuned.'
**Speaker refusing:** Tim Stenzel
**Speaker asking:** Chris Benson

**Excerpt:**
Chris Benson:
Hi, Tim. I was wondering, we have not seen any recent postings of the FDA standard for molecular tests on the website. I was wondering, that has not been updated since I think October, and I had a client who got an EUA authorization in January, and they were wondering when they might see that data posted on the website.

Tim Stenzel (FDA IVD Director):
So we are working on the next update, and it hasn't been - a target date hasn't been formalized yet. So all I can say is, stay tuned. We want to update it again as soon as we can.

Chris Benson:
All right. Thank you.

Toby Lowe (FDA IVD Assoc Director):
Can you also clarify, did you say that you're asking about a test that was authorized in January, but you're not seeing that test posted on our website?

Chris Benson:
No. I'm sending the results from the FDA panel.

Toby Lowe (FDA IVD Assoc Director):
Ah, okay. Thank you. FDA Virtual TH

Chris Benson:
It was not posted yet, but it's in the IFQ, of course, which we appreciate, but we were wondering about the posting. That was all. All right.

Toby Lowe (FDA IVD Assoc Director):
Thank you for clarifying

Chris Benson:
Perfect.

---

#### Instance 24: 2021-03-31_Virtual Town Hall 49_section-titles.md
**Line range:** 96-97
**Section:** #### 9. Guidance on At-Home Serology Test Development
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** FDA declines to say when or whether an at-home serology template will be published, which withholds a public policy/process answer developers could use broadly. The response gives fallback process guidance through the mailbox and review team, but the core public guidance question remains unanswered.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Multiple

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
Our next question is regarding the development of rapid tests for antigen and antibody. Basically a few questions about at-home serology tests and whether there's a template available. We have not yet published a template for at- home serology tests and we're not able to speak to when or whether there will be one that is published. However, we know that some test developers have received some draft feedback from the review team and that is a good starting point. If you have specific questions about your own validation or study design, you can reach out through the mailbox or to your review team if you already have one. There's additionally a question about a test, a serology test that has already received an EUA to the point of care and what additional performance data is needed. So we would expect to see validation in an at-home setting if you are looking to have an at-home claim.

---

#### Instance 25: 2021-04-07_Virtual Town Hall 50_section-titles.md
**Line range:** 33-37
**Section:** #### 2. BioFire De Novo Updates and Submission Guidance
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** FDA confirms that the BioFire decision summary will be posted but declines to comment on the timing. The response does provide some practical substitute guidance by noting that the granting letter is already posted and can be used in the meantime, along with the special controls for study design.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Multiple

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
Thanks, Kris. That's a really good point that all of that information is available on our website and it's very helpful for the test developer. So moving along, we have a couple of questions about the BioFire de novo. We do have a question about whether the decision summary for the BioFire will be posted and it will be. We unfortunately are not able to comment on the timeline. We are working on getting that out. I'm sure everyone is aware FDA Webinar that decision summaries for de novo sometimes takes some time to get posted. But we are working to expedite that one. We also briefly discussed just a little bit last week but there's a question about the BioFire being challenging to have access to as a predicate since it's the only de novo currently in the - the only predicate for a future 510K for a SARS-CoV-2 test. And we did talk last week that you can use an EUA authorized test as a comparator for your clinical studies even though BioFire would e your predicate for the submission itself. The question also was asking about whether there are other options such as testing to the reference panel to support a 510K. And while we do consider another EUA authorized comparator to the acceptable we do really want to see the perspective clinical study in your 510K submission. You can also include reference panel results and the clinicals that are from your authorized EUA if you have one and leverage those but they would not be, generally they would not be considered to be sufficient on their own to support a 510K clearance. Kris, anything to add on that one?

Kris Roth (FDA):
Sure, I think, you know, in this time between while we're waiting for that decision to maybe be posted, you know, the granting letter is posted and it does have the special controls noted for these types of tests and you can take a look at those special controls and design your studies to mee those requirements as well.

---

#### Instance 26: 2021-04-07_Virtual Town Hall 50_section-titles.md
**Line range:** 42-43
**Section:** #### 3. Asymptomatic Screening and Over-the-Counter Test Authorization Guidelines
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** FDA provides substantial generalized guidance on asymptomatic serial screening and over-the-counter expansion, but declines to get into the statistical-plan details on the call because they are specific to each test. The core limitation is a partial public answer with the details deferred to case-by-case review.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Multiple

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
Great, thanks. So moving on, we have some questions about asymptomatic screening. And particularly related to the supplemental template that we put out and asking about the post-authorization validation studies. Generally we would want to see your proposal for a serial testing plan and the post- FDA Webinar authorization study in your EUA request. And we would discuss that with you during the review particularly the statistical plan which is what this question is focused on. We would want to go through that with you in detail. So we can't really get into too many details on the specific book on this call because it will be specific to each individual test and each approach that you're looking to take as a test developer to validate your test. And then along the same lines with serial screening using that supplemental template, we have some questions about the additional data that we would expect to see. And so, you know, the way that supplemental template is laid out is that it is there as an approach sot that if you have symptomatic validation data and you've been authorized for testing symptomatic individuals, that template allows you to expand your or to request expanding your claims to asymptomatic serial screening without doing that additional asymptomatic validation ahead of time. That would be the post-authorization condition. So generally, you know, for most cases as long as nothing else is changing, so you're not changing your patient population such as point of care to at home or other changes that might impact the usability. We would not expect to see additional validation clinical or usability as long as nothing is changing except for going from symptomatic to serial screening. And we could discuss that on a case-by-case basis if there are things that are changing whether there is additional data that we would need to see. And then there is another question along the same lines asking about removing the prescription requirement when going from prescription to over- the-counter. We do have recommendations in the template for OTC use that's in the non-laboratory use template for molecular and antigen tests. The supplemental template that we've been talking about also can support this FDA Webinar move from prescription to over-the-counter because one of the requirements for over-the-counter is that there is an asymptomatic claim. We generally would not authorize a test for over-the-counter use if it does not have that broad asymptomatic screening claim since that's how we would expect it to be used over the counter. And so if you are able to use the supplemental template to get that asymptomatic claim, as long as everything else about your test is appropriate for over-the-counter use and has appropriate labeling, usability user comprehension for a lay user then we would be able to do that over-the-counter labeling for you as well in that same EUA request.

---

#### Instance 27: 2021-04-14_Virtual Town Hall 51_section-titles.md
**Line range:** 36-37
**Section:** #### 3. Transition Plan for EUA Devices and Regulatory Pathways
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This is a real but limited refusal: FDA explicitly declines to provide a specific timeline for discontinuing EUAs or requiring traditional pathways. However, the speaker gives substantial generalized guidance, including that a transition plan is on the FY21 guidance priority list, that EUAs generally remain effective until the public health emergency is terminated unless revoked, that termination is not typically accelerated, and that the BioFire De Novo opened a 510(k) pathway without affecting other EUAs.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Unknown

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
Next we have a question about the process and timing to discontinue EUAs and require 510k's or Denovos. And we have discussed this a little bit previously on calls. And we've mentioned before that I can't comment on a timeline specifically but we are working on a transition plan for devices that are offered under EUA. And this is included as a guidance document on the center's guidance priority list for FY21. If you take a look there you'll see the transition plan for medical devices distributed under enforcement policies or emergency's authorization during the COVID-19 public health emergency. Additionally it's important to recognize that generally unless they're revoked an EUA is in effect until the public health emergency is terminated. And the termination of a public health emergency does not typically happen on a particularly accelerated timeline. You can see that there are previous public health emergencies, like, Zika and Ebola that still have not been terminated. Now we have authorized the first test for marketing beyond the public health emergency with the BioFire Denovo. And that does open up the 510k pathway for other molecular diagnostic SARS-CoV-2 tests both individual or a single analyte SARS-CoV-2 test as well as multi-analyte panels which the Bio Fire test is. But that Denovo does not impact any other EUAs other than the BioFire EUA for that same identical test which was revoked concurrent to granting the Denovo. BioFire's other EUAs and other developer's EUAs were not impacted. So we can't anticipate when the public health emergency would end but we are working on that transition plan and we are committed to, you know,  ensuring that the public has access to a wide variety of test options for COVID-19 and we have no intention at the moment of stopping review for EUAs or revoking based solely on timeline or anything, like, that.

---

#### Instance 28: 2021-05-12_Virtual Town Hall 55_section-titles.md
**Line range:** 318-334
**Section:** #### 13. Defining High Throughput and Testing Prioritization Criteria
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** The caller asks a generalizable priority-policy question about how FDA defines high throughput. FDA explains the broad priority buckets but declines to publish the operative criterion and tells developers to check through the pre-EUA process instead. The withheld answer concerns unpublished policy criteria.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Jackie Chin

**Excerpt:**
Jackie Chin:
Just following-up on the previous question on priority. In particular if a developer has got multiple tests like the unmet needs such as the - a neutralizing antibody test or other type of technology they - it's not on the high throughput platform that so it is not - so it cannot test at least 150 tests at once but it can still test multiple tests at once. Is this of a lower priority than other POC tests or the bigger platform test?

Tim Stenzel (FDA IVD Director):
Yes so again we're looking at access. And so it does - it's home, it's point- of-care or it's high throughput. It really needs to pass those bars right now first, those thresholds. Having a great neutralizing antibody assay that can't really help that many people is not going to address the country's needs right now. So we are, you know, this is - you know, these priorities are out there for clear reasons. One is to inform developers of what we're not prioritizing. And it also is to hopefully stimulate developers to develop the tests that are really needed at this stage of the pandemic. Okay?

Jackie Chin:
Okay. Can you define high throughput? Is it at least 150 at one?

Tim Stenzel (FDA IVD Director):
So, yes as we said before if you want to check and see if your test will meet current priorities, you know, do send in a pre-EUA with relevant information for us to assess that. You don't have to fill out a full pre-EUA if you're going to use the templates as in the template recommendations as intended. You can simply say our one question is do we need the high throughput at all? That is something that we're not publishing right now because as we go through the pandemic that may - they may elevate and if the needs change. So it's best just to check with our staff through the pre-EUA process to see if your test would currently match our priorities.

Jackie Chin:
Thank you.

Coordinator (FDA):
Thank you. Our next question is from Dana Hummel. Your line is open.

---

#### Instance 29: 2021-05-19_Virtual Town Hall 56_section-titles.md
**Line range:** 48-49
**Section:** #### 5. Validation and Approval for Home Use Antibody Tests
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** FDA declines to provide specific validation study recommendations for home-use serology self-testing because no template has been finalized yet. Although it identifies procedural options such as pre-EUA, pre-submission, de novo, or 510(k), the core request is a generalizable policy/process question about what validation FDA expects, and that public guidance is withheld.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Unknown

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
The next question that we have is about home use antibody tests and asking specific questions about the validation and prioritization. So, unfortunately since we have not yet finalized a template for COVID-19 serology home use self-testing, we're not able to comment further at this time on specific validation study recommendations. And we would recommend that you reach out through a pre-EUA or if you would like to pursue a de novo or 510k through a pre-submission to further discuss your approach.

---

#### Instance 30: 2021-06-02_Virtual Town Hall 58_section-titles.md
**Line range:** 411-445
**Section:** #### 14. Addressing Sample Bias in Antigen Test Validation Methods
**Category:** E — Deflection to Email (No Substantive Answer)
**Appropriateness Score:** 2/5
**Rationale:** This is a real active refusal: FDA stops the caller from continuing because the question seeks highly specific advice about the caller's own validation approach and says that is not something they typically do on the call. FDA gives only limited general context that bias assessment depends on more protocol detail and review of the study design, but does not provide a concrete public answer.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Franco Calderon

**Excerpt:**
Franco Calderon:
Thank you for giving me the opportunity to ask a couple of more questions since there's a light audience today. The first one is regarding a sensitive control step that we have been doing at our own discretion, really because we have been generating the sensitivity of the antigen test. So since the Abbott BinaxNOW, the Quidel QuickVue, and a couple of others can actually be bought now directly from pharmacies, we actually got our hands on a couple of Abbott BinaxNOW and, I believe, the care test from Axis Bio. And we used the most positive control with the specimens that we purchased, which were in CDC VTM. And I wanted to also provide a little additional detail about how we obtained those. So basically, and this would address the issue of the bias, perhaps. So basically, we hired a lab that has been doing a lot of testing through the pandemic. And they use a high sensitivity PCR test with an extraction step. So we knew that from the get-go. So basically what we did for those 30 samples was we said, hey when you get a positive, let us know. We like to test that person to see, you know, how our test performs. And that's, in effect, how we ended up getting those 30 specimens. So would that be a biased way? So that's what is related to my first comments regarding - are you aware...

Tim Stenzel (FDA IVD Director):
Yes. So...

Franco Calderon:
...about the - sorry. May I continue?

Tim Stenzel (FDA IVD Director):
Yes. But hold on a second, though, because this is getting very specific advice for your specific submission.

Franco Calderon:
Okay.

Tim Stenzel (FDA IVD Director):
And it's not it's not something that we typically do on the call.

Franco Calderon:
I apologize.

Tim Stenzel (FDA IVD Director):
So the best way, though, to get - because in all likelihood, I'd need more detail than you're giving me right now to address bias. And so the usual way for us to do this is actually see the study protocol.

Franco Calderon:
Okay.

Tim Stenzel (FDA IVD Director):
How are you acquiring samples in the context of your specific assay and use case? So those are all important to assess, you know, the acceptability of what you propose and takes a little bit more time to assess than we can on this call.

Franco Calderon:
Sure. I apologize. Thank you.

Tim Stenzel (FDA IVD Director):
No reason to apologize.

---

#### Instance 31: 2021-06-09_Virtual Town Hall 59_section-titles.md
**Line range:** 51-58
**Section:** #### 5. FDA Policies on COVID-19 EUA Submissions and Transition Plans
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This passage contains a real but limited refusal in the final exchange about quantitative viral load molecular tests: FDA says it cannot provide specific answers because there are too many possible intended uses and settings. FDA does provide useful generalized guidance by explaining that an international standard now makes meaningful quantitative tests possible, that intended use and validation must be discussed in context, and that sponsors should submit a pre-EUA to discuss options.
**Speaker refusing:** Kris Roth (FDA)
**Speaker asking:** Toby Lowe (reading prepared question)

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
Great. Thanks, Chris. The next question that we have is along the lines of questions that we've had on previous town halls. This is about FDA's policy on SARS-CoV-2 EUA submissions and, you know, sort of the timeline for the public health emergency. So they're asking when FDA will stop accepting new EUA applications; when FDA will stop accepting amendments to existing EUA products, when the current EUAs will expire; how long EUA products can be distributed after the EUA expires; and will there be a grace period for EUAs transitioning to 510ks? So, you know, we have talked about this a bit before. We are still accepting EUA requests both for original EUAs and supplemental EUA requests for amendments to previously authorized tests. We don't have a timeline that we can comment on for a transition plan, but we have previously announced that we are - the center is working on a transition plan for devices offered under EUA. And that's a guidance document that's included on the center's guidance priority list for FY '21. That's - the title on that priority list is the Transition Plan for Medical Devices Distributed Under Enforcement Policies or Emergency Use Authorization during the COVID-19 public health emergency. And generally, unless it's revoked, an EUA is in effect until the public health emergency is terminated. And that is a, you know, specific termination by the Secretary of HHS that goes along, you know, sort of the end of the declaration that the Secretary makes at the beginning of the public health emergency, to allow FDA to start using the EUA authority. And so the, you know, at some point in the future the Secretary then terminates that emergency. But that is not something that we would expect to happen for quite a while. You can see that there are previous public health emergencies that still have not been terminated, looking at Zika and Ebola as examples there. So, you know, while we can't anticipate when the public health emergency will end, we, you know, we can make clear that we're committing to helping to ensure that the public has access to a wide variety of test options for COVID- 19. And we do continue to review EUAs and we plan to continue to do so as long as there is a public health need for that to be done. Regarding conversion to 510ks, we have mentioned the last few times on town halls as well as in previous town halls, that anyone looking to submit a 510k submit a pre-submission for - so that we can discuss your proposed validation approach to make that process go as smoothly as possible. The next question we have is let's see, about a molecular point of care COVID device for an EUA. This company intends to submit an EUA request and is asking about a notification letter for the manufacturer to commercialize the device while the EUA is under review. So just to clarify, there are - this question appears to be referring to the notification policies that are included in the guidance document, the policy for Coronavirus Disease 2019 Test during the public health emergency. And that policy guidance document does include the notification policies that, you know, puts together a process for a manufacturer following completion of their assay validation to notify FDA that their assay has been validated and that they intend to begin distribution or use of the test. Generally, FDA would acknowledge receipt of the notification and add the name of the test developer and the test to our Web site listing. We do have a list of all notified tests on the FAQ pages. And, you know, in the guidance document it outlined a process for the test developer to submit a completed EUA request within 15 business days of the notification to FDA that the assay has been successfully validated. And if that's not done we generally removed the test from the Web site and may take additional action as appropriate. There are a couple of important things to note here. One is that submission of an EUA request is not the same as notifying under the policies in the guidance. A test developer that intends to use the notification policy must specifically notify per the process outlined in the guidance and should not assume that they're considered to be notified simply because they submitted an EUA request. And then another thing that I want to note is that this question specifically mentioned the point of care device. And the notification policy is specific to tests being used in high complexity CLIA-certified laboratories. Tests that are not yet authorized are - under CLIA, are limited to use in high complexity CLIA-certified laboratories. So that would generally not apply to point of care devices unless that point of care setting is - falls under a CLIA-certified laboratory - a high complexity CLIA-certified laboratory certificate. All right. The next question we have is about quantitative viral load molecular tests for COVID-19. And this would be a test that would measure viral count per milliliter, not a test that would just report the CT count. The question is asking for FDA's viewpoint on the medical importance or usefulness of such a test, whether we would support or encourage the development of such a test; whether it be used for screening similar to other tests for other patient populations that we would recommend it being for, as well as the review priority that, you know, we're - that this would fall under. So generally now that an international standard is available, it is possible for a meaningful quantitative test to be developed. And we are glad to engage in discussions about validation of such a test. There are limited guidelines for use of this type of information. So we would want to engage in a discussion of the appropriate intended use and we would, you know, that discussion would need to be in the context of the specific test setting and technology being proposed. So we would encourage you to submit a pre-EUA so that we can discuss those options with you. And Chris, do you want to add anything on that one?

Kris Roth (FDA):
Yes, thanks. I think there's just a lot of different options in this - for this type of intended use. And so unfortunately I don't think we can really provide some specific answers to these questions. There's just too many different ways to go. But certainly having the international standard will help tremendously. And I think we're ready to engage. Thanks.

Toby Lowe (FDA IVD Assoc Director):
Great. Thanks, Chris. And that is all the prepared Q&A that we have. So we can open up the lines for live questions.

---

#### Instance 32: 2021-08-04_Virtual Town Hall 65_section-titles.md
**Line range:** 33-34
**Section:** #### 3. Prioritization of Multi-Analyte Tests and Resubmission Considerations
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** FDA does refuse to discuss specific submissions on the call, which is an active limitation. However, the speaker then provides useful generalized guidance on why a prior EUA may have been deprioritized and explains the conditions under which a resubmitted request would be considered and prioritized. The core question still receives a meaningful general answer.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Unknown

**Excerpt:**
Toby Lowe (FDA IVD Assoc Director):
The next question that we received is similar to previous questions that have been asked regarding whether the US is prioritizing multi-analyte tests and specifically asking whether we would permit a company that had a previous EUA for a respiratory panel deprioritized to resubmit the same EUA. And so to reiterate what we've previously said, multi-analyte tests that have sufficient manufacturing and testing capacity are included in our priorities and will continue to be prioritized. While we can't discuss specific submissions on this call as we've mentioned, we can generally share that if an EUA request was deprioritized previously, it was likely because the test either had low manufacturing or testing capacity or that the submission was deficient in some way. If such an EUA request was resubmitted and addressed any outstanding issues, then it would be considered and prioritized as appropriate based on the information in the EUA request.

---

#### Instance 33: 2021-08-04_Virtual Town Hall 65_section-titles.md
**Line range:** 126-163
**Section:** #### 9. Clarifying EUA Approval Timelines for OTC Test Kits
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Appropriateness Score:** 2/5
**Rationale:** FDA provides general context about prioritization and completeness of submissions, but explicitly declines to provide a specific timeline or average wait time for OTC EUA review. The refused core question is a timing/status question, no concrete estimate is given, and the follow-up mailbox offer does not materially answer the public timeline question.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Tianyang Liu

**Excerpt:**
Tianyang Liu:
Hi. Could you hear me?

Toby Lowe (FDA IVD Assoc Director):
Yes.

Tianyang Liu:
OK, thank you. So my question is that our company has submitted the EUA for our antigen home tester kit months ago. But we just took our feedback from FDA that said it gets started and at a very early stage. Although FDA claimed the OTC home used test kit is a priority, but it seems not going that fast. We are eager to get it approved, since we all see the Delta virus is currently spreading fast and more and more people are being infected. OTC tester kit can play a greater role against the Delta virus, because they can easily and rapidly detect the virus. Could you please let me know how much this priority bill for OTC study will speed up in the process? And how long we are supposed to wait? Is there any kind of rough estimation for those type of EUA approval? And what kind of resources does the FDA put on the priority to speed up the OTC product? Thank you.

Toby Lowe (FDA IVD Assoc Director):
Sure. So obviously, we can't speak to specific tests. And I don't know off-hand the specific situation with yours. If you do have concerns about your file, you can send an email to the Templates mailbox and ask that it be sent to me, and I can take a look at it. But generally, OTC and home use tests are a priority. We do have a large number of submissions in the house, and we are prioritizing those reviews as much as possible and moving through them as quickly as possible. In addition to prioritizing the home use tests, we also do look at the content of the submission. So it does make a difference if the submission is complete and followed the recommendations in the template and looks promising at first glance, if you will. And those aspects are all factored in when we have to prioritize reviews with so many submissions in-house.

Tianyang Liu:
Oh. I see, I see. Thank you, Megan. And is your average-- I mean, average days or months that you already OTC EUA has been approved? I know that right now, we have five OTC products approved by the FDA right now.

Toby Lowe (FDA IVD Assoc Director):
So sorry, I'm not sure I caught that question.

Tianyang Liu:
I mean, is there an average months or days that-­

Toby Lowe (FDA IVD Assoc Director):
Oh. No, I can't necessarily specify a specific timeline or an average. It really does depend on the submission, the quality of the submission. And if you follow the recommendations in the template, that definitely helps to speed things up.

Tianyang Liu:
OK. OK, thank you very much sir-- thank you very much, madam. And in this case, you said that we can send it to you. Is there an email address that we could refer to?

Toby Lowe (FDA IVD Assoc Director):
So if you send an email to the CDRH EUA Templates mailbox, it should be showing on the screen, and you can ask that it be sent to Toby to take a look and get back to you.

Tianyang Liu:
OK. Thank you very much.

Toby Lowe (FDA IVD Assoc Director):
No problem.

Anike Freeman (FDA)
OK. Our next question is from Michael D'Armiento.

---

#### Instance 34: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Line range:** 39-40
**Section:** #### 4. FDA Plans for Transitioning COVID-19 Test EUAs
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Appropriateness Score:** 2/5
**Rationale:** FDA gives substantial context about the broader transition framework, but explicitly refuses to comment on the timeline for the transition plan. The refused core question is a timeline/status question, no concrete timing is provided, and the surrounding public guidance does not resolve the requested schedule.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Unknown

**Excerpt:**
Tim Stenzel (FDA IVD Director):
Next question. Does the FDA plan to end the EUA pathway for any SARS-CoV-2 related test diagnostics, serology, et cetera, prior to the official end of the public health emergency? The short answer is no. If so, what would be the criteria for ending the EUA pathway? The FDA is actually not the one that would declare an end to the emergency. That's the brief answer. I'll go into a longer answer here shortly. Also, would tests previously granted EUA be allowed to remain on market if the EUA pathway is ended? And the answer is there is a short answer, is yes. Let me go into more detail on this. We have covered this before on this call, but we'll go over it again. While we can't comment on the timeline, we're working on a transition plan for devices offered under EUA. But we still are encouraging full authorization submissions to the FDA soon as you want. We are accepting Q-Subs, Pre-Subs for those. And we're accepting full authorization applications. For molecular, that mostly would be 510k submissions now, since we've already granted one submission. And then for serology and antigen, it would be-- the first one would be a de novo application. And then subsequent to that, most of the antigen and serology tests would be 510k submission. So the transition plan guidance is on the Center's, CDRH's FY '21 priority list. And additionally, revoked EUAs are in effect until the public health emergency is terminated. This does not typically happen for quite a while, and as can be seen from previous public health emergencies that still have not been terminated, like Zika and Ebola. So there are still non SARS-CoV-2 tests that are able to be sold and used under EUA authorities. We cannot anticipate when the public health emergency will end. However, the FDA is committed to helping ensure the public has access to a wide variety of test options for COVID. And we'll continue to review the EUAs to address public health needs.

---

#### Instance 35: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Line range:** 80-81
**Section:** #### 11. FDA Guidance on EUA to 510k Transitions
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** The passage contains a real but limited refusal when FDA says it cannot comment on the timeline for a transition plan from QSR to ISO 13485. However, FDA does provide useful general guidance by stating that the EUA pathway for critical assays is not expected to end in the near future, which partially addresses the practical concern.
**Speaker refusing:** Tim Stenzel
**Speaker asking:** Unknown

**Excerpt:**
Tim Stenzel (FDA IVD Director):
Next question. For an EUA over-the-counter nonprescription COVID-19 rapid lateral flow assay with a serial testing claim that will eventually provide FDA with acceptable asymptomatic serial study data, is it a correct assumption that, for the transition from EUA to 510k, no new asymptomatic testing would be necessary for the 510k? Meaning that only the acceptable asymptomatic serial study data is required to support the asymptomatic claim. So currently, the serial testing program is only applicable to EUA tests. However, we will want to incorporate as much of the EUA data as is possible. And that's possible if the device does not change in any material way that can impact performance. So but as far as the minimum recommendations for the number of samples, et cetera, you'll want to validate that according to FDA recommendations. And you can go ahead and submit a Pre-Sub or a Q- Sub with your proposed studies on specific questions. So depending on the size of that asymptomatic study, it may or may not meet the expectations for full authorization. Second question from this person, for an at-home test by prescription multi-analyte COVID-19 and influenza EB lateral flow test intended for symptomatic individuals, presuming EUA authorization and eventual 510k clearance, is it correct that no testing of asymptomatic individuals would be required, either single or serial testing? If you're proposing a claim for a symptomatic population, which is the likely population, when you have a multi-analyte test other than SARS, we simply don't know what's going on with other viruses, respiratory viruses, in an asymptomatic population, you would not need to test asymptomatic individuals. Next question from this individual, in general, when the performance of an assay isn't expected to exceed 90% PPA or sensitivity, does a test developer need to include symptomatic and asymptomatic serial testing in a clinical study to support 510k clearance for COVID-19 rapid lateral flow assay for over the counter? So again, depending on what claims you want to make, we recommend you submit a Pre-Sub to get more information. And the final question from this person notes that in an August 12 article, in Agency IQ by Laura DiAngelo on the FDA transition from QSR to ISO 13485, that there are questions about the impact on EUA authorizations. So yes, we are in the process of converting from QSR to ISO 13485. However, and we can't comment on the timeline for a transition plan. But again, we do not see an end anywhere in the near future to the EUA pathway for review of critical assays by the FDA.

---

#### Instance 36: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Line range:** 101-147
**Section:** #### 13. FDA Review Process for OTC Home Test Applications
**Category:** D1 — Timeline/Status Deflection with Redirect
**Appropriateness Score:** 3/5
**Rationale:** The caller asks for expected timing and then for the status implication of having heard only that the first OTC home-test submission is 'under review' after seven weeks. FDA gives some general process information about initial completeness review and prioritization, but declines to provide a concrete timeline or substantive status interpretation for this specific submission, instead saying the submitter should contact the assigned reviewer or the templates mailbox for periodic status updates. That is a mixed case: some useful general guidance was provided, but the core status/timeline question was redirected offline.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Tianyang Liu

**Excerpt:**
Tianyang Liu:
Thank you. Oh, hi, Tim. My question is, if we formally submitted our materials to FDA of our OTC home test kit, and it has no major deficiency, how long should we expect the first feedback from FDA?

Tim Stenzel (FDA IVD Director):
So if we take a look at the assay, we do an initial review to make sure that the application is complete. If the application is not complete, we would, within a few days, I think up to 10 days, we would return comments with the fact that the assay, the application is incomplete.

Tianyang Liu:
I see. Yeah, but--

Tim Stenzel (FDA IVD Director):
If you are beyond that period, then we take a deeper dive into the application. And those applications that have essentially no substantial questions get prioritized ahead of others. And that's because we can move those applications along more quickly. So it's important to submit a good application. Because if we've got questions, it will move an application down in priority. So and it's probably evident to all on the call that the authorized another home OTC test, the BD Veritor. And that was late last night. And so that, obviously, was something that could move along the process relatively quickly. So then we move to those that are next on the list. And it is our goal to get through that list as quickly as possible. And I meet regularly with the team, and we discuss all the applications. And we discuss priority within even the home OTC applications what are the top priority.

Tianyang Liu:
I see. So --

Tim Stenzel (FDA IVD Director):
Hopefully that addresses the question.

Tianyang Liu:
Thank you, Tim. So in this case, if we submitted our OTC home test kit which is a priority two months ago, I mean, seven weeks ago, and we never received any feedback except that your application is under review. So in this case, you mean that--

Tim Stenzel (FDA IVD Director):
So yeah.

Tianyang Liu:
We are --

Tim Stenzel (FDA IVD Director):
If we issued a-- oh, go ahead. I'm sorry. Go ahead.

Tianyang Liu:
So in this case, you mean that so our application is under a deep dive look. And in this case, we should wait. Right?

Tim Stenzel (FDA IVD Director):
It depends on what feedback. You said, resubmission. So if an assay is resubmitted--

Tianyang Liu:
No. It is the first submission. It's a first.

Tim Stenzel (FDA IVD Director):
Oh, a first submission. Oh, OK. Yes. It is under review, and it -- you should have already been assigned a reviewer and have somebody to contact. If not, you can send an email to the templates email box. And they can, on a periodic basis, give you an update on the status.

Tianyang Liu:
OK. Thank you. Thank you. Got it.

Anike Freeman (FDA)
Our next question is from Richard Montagna.

---

#### Instance 37: 2021-08-25_Virtual Town Hall 68_section-titles.md
**Line range:** 368-384
**Section:** #### 20. Transition from EUA to Full 820 Compliance
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** This is a real but limited refusal: the caller asks about the transition path from EUA-era 820 flexibility to full 820 compliance and possible future ISO transition, and FDA says it 'really can't comment on the guidance.' However, Tim Stenzel provides substantial generalized guidance by explaining there is no immediate change, FDA is accepting and reviewing Pre-Subs/Q-Subs for full authorization, firms should begin preparing full authorizations now, and updated templates will likely carry specific recommendations.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Laura D'Angelo

**Excerpt:**
Laura D'Angelo:
Hi there. I would like to follow up on myself on the 820 question. I think the last time we talked about 820 at these town halls was in February, when the plan was the transition guidance will address kind of the things that were waved out under EUA and the transition into a fully compliant 820 system. And then forward looking, and the answer might just literally be we can't comment on the timeline. But my question was, if we're transitioning from EUA with some parts waived out in 820, to full 820, is there going to be another plan for? Or is this just we'll take as it comes for the transition to ISO, which I know is kind of in the hopper?

Tim Stenzel (FDA IVD Director):
So I don't I don't see any immediate change to how we have EUA and how we have full authorization in the near future. We are accepting Q-Subs and Pre-Subs for full authorization. We are reviewing those. We are getting back to folks as soon as possible. And all our areas antigen, molecular, and serology have ideas. Of course, molecular, we've already done it. So we have very clear recommendations. We are going to work on templates, updates on what those full authorization recommendations are. I am recommending that, those that want to stay on the market long term, that they do start working on their full authorizations and submit Pre-Subs for us to review if needed. I mean, you can look at things in the molecular. You can look at what we've already reauthorized. You may not have any questions, and you can just go forward. And so I really can't comment on the guidance. That's really not within my control anymore. It's going through the process to be able to be made public. That document will not specify for IVDs the recommendations for conversions in all likelihood. It'll just be outlying things like timelines and general high level expectations. But our plan is to update the templates with specific recommendations for those.

Laura D'Angelo:
OK. Very cool. Thank you.

Anike Freeman (FDA)
All right. I think we have time for one more?

Tim Stenzel (FDA IVD Director):
We have time for one more.

Anike Freeman (FDA)
Yep. And that will be from Diane B.

---

#### Instance 38: 2021-09-22_Virtual Town Hall 70_section-titles.md
**Line range:** 120-142
**Section:** #### 8. Clarification on Confirmed Positives and FDA Communication Response Time
**Category:** E — Deflection to Email (No Substantive Answer)
**Appropriateness Score:** 2/5
**Rationale:** The caller asks a case-specific methodological question, and FDA says the question is too detailed or test-specific to address on the call. Rather than giving a meaningful public answer, FDA sends the caller to the templates mailbox or assigned reviewer. There is no substantive on-call guidance on the question itself, and the matter is moved offline.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Julio Herrera

**Excerpt:**
Julio Herrera:
Yes, can you hear me?

Joseph Tartal (FDA):
Yes.

Julio Herrera:
All right, so I submitted this via email. And I guess it got missed or maybe it's for next week. So we're working on an at-home collection for serology assays. And so we're doing the clinical agreement section, which is the 30 unvaccinated and the 30 vaccinated confirmed infections. My question is actually twofold. One is, for confirming positives, can we use an FDA EUA antigen or rapid test, such as the BinaxNOW, as a positive confirmatory test to basically include that as our positives? The second question is related, but we've also had a number of individuals that we've collected that were vaccinated individuals and let's say are four to six months past their last dose of the vaccine that basically are now sending us a confirmatory positive result. Would those individuals be eligible as confirmed positives for this clinical agreement or for the usability?

Tim Stenzel (FDA IVD Director):
So I neglected to read a disclaimer at the beginning of the question that we went over that were received prior to the call. And this is true for every week. So we do receive some questions that are a little too detailed or test- or case-specific that we will not address on the call. And so I forgot to do that. So that was the case for your question. So I do recommend that you reach out to FDA staff through the CDRH EUA Templates email address. Or if you already have a reviewer assigned, to reach out to them to engage them in this conversation. I'm not going to be able to go over that question today.

Julio Herrera:
OK, all right. How long does it take them to respond? Because I sent in a question to them through that site several weeks ago and I haven't heard back from them yet.

Tim Stenzel (FDA IVD Director):
If it's been more than a couple of weeks, you can go ahead and send an another email to the Templates email address and ask them, in this case, to contact Toby.

Julio Herrera:
All right, all right, thank you.

Joseph Tartal (FDA):
Thank you. We'll go on to our next question. Tianyang Liu. I'm opening up your microphone so that you can unmute and ask your question.

---

#### Instance 39: 2021-10-21_Virtual Town Hall 72_section-titles.md
**Line range:** 213-244
**Section:** #### 14. Pre-EUA Requirements and Time Frame Clarifications
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Appropriateness Score:** 2/5
**Rationale:** FDA substantively answered the pre-EUA requirement question, but when asked for the time frame for receiving a response to a pre-EUA, it declined to provide any estimate. The only additional information was a general reference to FAQs on prioritization and review times, which did not answer the specific timeline question or offer a concrete contact path. This is therefore an active refusal focused on timeline information, with minimal useful guidance.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Homer Wu

**Excerpt:**
Homer Wu:
OK, you guys can hear?

Joseph Tartal (FDA):
Yes, we can hear.

Homer Wu:
OK, thanks for taking my call. My quick question is, according to the templates if we apply for serial testing for home use antigen we have to supplement the pre-EUA. Is that right or we can go ahead without the pre-EUA?

Toby Lowe (FDA IVD Assoc Director):
So if you're following the template then you could do that without a pre-EUA. You can just submit your EUA request. There is discussion of serial testing in the supplemental template as well as in the antigen template directly or the home use template rather. If there are questions that you have or approaches that you want to take that are different than what is in the template then we would suggest that you come in and discuss that with us.

Homer Wu:
OK, so it's not required, right?

Toby Lowe (FDA IVD Assoc Director):
A pre-EUA is never required. It's just an option if there are questions that you need to get answered prior to submission of your EUA request.

Homer Wu:
OK, follow up question. If we do apply for the pre-EUA, what's the time frame not to have a response?

Toby Lowe (FDA IVD Assoc Director):
We are not able to provide a time frame at this point. We do have some information on our FAQs about our prioritization and about the time for reviews but we're not able to provide an estimate right now.

Homer Wu:
OK. All right, thank you guys.

Toby Lowe (FDA IVD Assoc Director):
Sure.

Joseph Tartal (FDA):
OK, next question. Laura Ferguson. I'm muting you right now. Please unmute yourself and ask your question.

---

#### Instance 40: 2022-02-09_Virtual Town Hall 78_section-titles.md
**Line range:** 72-82
**Section:** #### 7. Delays in EUA Amendment Review Process
**Category:** D1 — Timeline/Status Deflection with Redirect
**Appropriateness Score:** 3/5
**Rationale:** The caller asks whether an amendment may have been missed or whether the long silence is expected. FDA does not answer that submission-status question on the call, but it does offer a concrete follow-up path by asking the caller to send the details to the templates mailbox with Tim and Toby copied so the agency can investigate.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Richard Montagna

**Excerpt:**
Richard Montagna:
Thank you for taking the call. This is Richard Montagna from Rheonix. I know that the FDA is not able to respond to specific questions about a specific submission, so I'll try to frame this in a very general way. We submitted an amendment to our PCR EUA back in September. It was intended to validate the assay as a moderate complexity rather than the originally authorized high complexity. We were notified that it was in the triage, it would be evaluated, but for the past five months, we've got nothing but the biweekly updates. I'm wondering, is this what we should expect, or is it possible it's fallen through the cracks? Because it's also impacting another amendment we want to send in that will reduce the time of the assay. And we don't know whether we should run that with the software that would be used for high complexity or whether we should run it with the moderate complexity, because we don't know where we stand on that. I guess the question is, is it possible that it fell through the cracks, or is this what we should expect? So thanks for any guidance.

Tim Stenzel (FDA IVD Director):
Sorry for that experience. If you just follow up later today with an email to our templates email inbox and relay this information and ask for Tim and Toby to be copied, I'll go ahead and figure out what's going on and get a response back to you.

Richard Montagna:
OK, thank you very much. I really appreciate it.

Joseph Tartal (FDA):
OK, thank you our next question, Karl. Karl, I'm unmuting you. Please unmute yourself and ask your question.

---

#### Instance 41: 2022-03-09_Virtual Town Hall 80_section-titles.md
**Line range:** 48-52
**Section:** #### 4. FDA Guidance on Serology Test Marketing Authorization
**Category:** E2 — Policy/Process Refusal
**Appropriateness Score:** 2/5
**Rationale:** This is a real active refusal: FDA declines to answer a generalizable policy/process question about whether guidance for serology full marketing authorization will be issued before EUA terminations. The response does not turn on a specific submission or third-party confidentiality issue, and FDA could reasonably have provided public process-level guidance if available. FDA offers only a general statement that it cannot comment on future guidance and redirects developers to the Pre-Submission process, so this fits a policy/process refusal.
**Speaker refusing:** Kris Roth (FDA)
**Speaker asking:** Commander Kimberly Piermatteo (FDA)

**Excerpt:**
Commander Kimberly Piermatteo (FDA):
OK. Thank you. Our next question is, can FDA clarify whether a de novo or 510k guidance document for serology tests will be issued prior to the announcement of EUA terminations?

Kris Roth (FDA):
Yeah, we can't comment on any future guidance or policy documents that may be in the works at this time or in draft, being drafted, however we will provide further details as additional information becomes available. Test developers interested in pursuing full marketing authorization for a serology test are encouraged to submit Pre-Submission to discuss your approach.

---

#### Instance 42: 2022-03-09_Virtual Town Hall 80_section-titles.md
**Line range:** 57-61
**Section:** #### 5. FDA Guidance on De Novo Serology Test Submissions
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** FDA expressly declined to comment on whether any de novo serology submissions were under review, which is an active refusal of the specific status question. However, FDA then provided useful generalized guidance for similarly situated developers by recommending a Pre-Submission with study protocols to obtain feedback on a de novo pathway. The refused core question is not about another company's identified submission.
**Speaker refusing:** Kris Roth (FDA)
**Speaker asking:** Commander Kimberly Piermatteo (FDA)

**Excerpt:**
Commander Kimberly Piermatteo (FDA):
Thank you, alright. The next question, is FDA currently reviewing any de novo submissions for serology tests? If so, would it be possible to share recommendations provided to developers at this time?

Kris Roth (FDA):
So again, we're not going to comment on any submissions that may be under review, however if you intend to pursue a de novo regulatory pathway for your serology test, we recommend that you submit a Pre-Submission with your study protocols, in order for FDA to provide appropriate feedback.

---

#### Instance 43: 2022-05-18_Virtual Town Hall 85_section-titles.md
**Line range:** 36-40
**Section:** #### 3. Average Timeline for EUA COVID Test Submissions
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Appropriateness Score:** 2/5
**Rationale:** FDA does not provide the requested average timeline and instead points to a general FAQ stating only that reviews are handled as quickly as possible. The response explains that timing varies by submission quality and priority, but gives no concrete average or actionable estimate, so it functions as a deflection on a general timeline question. This is not a third-party confidentiality case and no meaningful substantive timeline guidance is provided beyond variability factors.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Commander Kimberly Piermatteo (FDA)

**Excerpt:**
Commander Kimberly Piermatteo (FDA):
Thank you, Toby. Our next question is, what is the average timeline for manufacturers who submit EUA or COVID‐only or COVID‐flu combo tests?

Toby Lowe (FDA IVD Assoc Director):
So we do have an FAQ that addresses this a little bit. And that FAQ is posted on our website. It's titled "I submitted a pre‐EUA or EUA request for a COVID‐19 test. How long will the review take?" And in that FAQ, we are clear that we try to review pre‐EUA and EUA requests as quickly as we can. And we do communicate with each sponsor regarding their pre‐EUA or EUA request as soon as possible. The timeline for a specific submission, however, is dependent on many different factors, including the priority of that submission, and the quality of the submission and the data provided.

---

#### Instance 44: 2022-08-24_Virtual Town Hall 90_section-titles.md
**Line range:** 120-145
**Section:** #### 9. Optimizing Clinical Trial Design for Dual Testing Kits
**Category:** C2 — Partial Answer with Redirect
**Appropriateness Score:** 3/5
**Rationale:** FDA gives meaningful generalized study-design guidance, including suggestions for backup sampling plans and bias mitigation. However, when the caller asks whether the same extraction buffer can be used for both kits in the same clinical trial, FDA explicitly declines to approve that approach on the phone and redirects the sponsor to pre-EUA review. The core answer is only partial, and the decisive guidance is deferred offline.
**Speaker refusing:** Kris Roth (FDA)
**Speaker asking:** Seungjin Ha Gina

**Excerpt:**
Seungjin Ha Gina:
Hi, how are you? This is Gina from Seungjin. And our company is developing the influenza A and B with COVID‐19 detection antigen testing kits under the FDA EUA process. And the other one, we are also developing for the influenza A and B, also antigen testing kits under the FDA 510k process. But we are trying to conduct a clinical trial with those two testing kits under the same procedure at the same time by the IRB operable with the clinical trial protocol. So I would like to know, if we collect one swab sample from our patients and it will be added into the reagent tube and containing the extraction of buffer. And also, we will use this one swab and one extraction buffer to the two kits at the same time. So we would like to know if it is possible for clinical trial with these two kits at the same time under the IRB approval. Do you think it is available or acceptable by your side?

Kris Roth (FDA):
Yeah, thanks for that. It's a little bit of a challenge because you are using the test kind of off label or not with the instructions that folks will have if it's either the COVID/flu combo or the flu alone. That being said, we do want to try to make efficiencies available to developers where it's appropriate. And so I think probably you're going to want to submit this as a pre‐EUA and let us know what the volumes are, what the challenges are, what happens if they run out of volume on the second test or something of that nature. And then I would also maybe think about a backup plan as well. So propose a sampling plan of, we'll do the standard care first, then we'll do the flu/COVID next, then the flu alone, and some sort of randomization scheme. So I would just plan for both instances or provide us a plan, I guess, in both instances, one, using the same abstraction buffer and two, provide a sampling plan that minimizes bias for the two candidate tests.

Seungjin Ha Gina:
So you recommend we have to get through the pre‐EUA for those submissions?

Kris Roth (FDA):
Yeah, I wouldn't be able to comment. I can't say on the phone, yes, it's fine to use the same abstraction buffer. One, it's off‐label use to use against the instructions for use. And number two, we'd be concerned about running out of buffer.

Seungjin Ha Gina:
OK. I got it. So before we are going to conduct the clinical trials with these at the same time, clinical trials, we have to get through the pre‐EUA and FDA should have reviewed our clinical trial first before removing every bias for conducting this clinical study. Am I correct?

Kris Roth (FDA):
That would lower your risk. Of course, if we know what you're going to do prior to you doing it, then you've got buy in from us, and you can be confident that your sampling plan is kind of agreed upon. Of course, that's not a requirement. You can go off and do your study, and then we can review it after it's done. But that's a little bit more risk on your end.

Seungjin Ha Gina:
Yeah, I understand. OK, thanks.

Kris Roth (FDA):
Thank you.

Commander Kimberly Piermatteo (FDA):
Thank you Gina and Kris. At this time, I'm going to ask if anyone has any questions to please raise your hand. OK we have a question from Kay. Kay, I have unmuted your line. Please unmute yourself and ask your question.

---

#### Instance 45: 2022-10-26_Virtual Town Hall 96_section-titles.md
**Line range:** 69-76
**Section:** #### 5. FDA Transition Plans for COVID-19 Device Policies
**Category:** D2 — Timeline/Status Deflection (No Substantive Response)
**Appropriateness Score:** 2/5
**Rationale:** This is a real active refusal because the core question asks whether FDA will implement the transition plan soon and requests an estimated implementation date, and FDA expressly says it is not able to comment on estimated finalization dates. FDA does provide background on the scope of the two draft transition guidances, but that does not substantively answer the requested timing. The response redirects listeners to monitor FDA's website instead of giving any concrete timeline or status detail.
**Speaker refusing:** Toby Lowe (FDA IVD Assoc Director)
**Speaker asking:** Commander Kimberly Piermatteo (FDA)

**Excerpt:**
Commander Kimberly Piermatteo (FDA):
Thanks again, Toby. So our last previously submitted question today is, with the implementation of new COVID‐19 test policy, is FDA also planning to implement the transition plan for medical devices that fall within enforcement policies issued during the coronavirus disease 2019, COVID­ 19, public health emergency soon? If so, can FDA provide an estimated implementation date?

Toby Lowe (FDA IVD Assoc Director):
Thanks, Kim. So we have discussed the transition plan draft guidance documents on previous town halls. And as discussed, we are working to finalize those draft guidance documents. The drafts were issued late last year. And it's important to note that those two draft guidance documents are not test specific. They're for all medical devices that fall within enforcement policies or were issued EUAs during the COVID‐19 public health emergency. And they do address different situations than the newly updated COVID‐19 test policy guidance. So the draft guidance document titled “Transition Plan for Medical Devices that Fall within Enforcement Policies Issued During the COVID‐19 Public Health Emergency” provides FDA's recommendations and expectations for devices under COVID‐19 related enforcement policies to transition back‐to‐normal operations when the public health emergency expires. And it is very important to note that the COVID­ 19 test policy guidance is outside of the scope of that transition guidance. And then COVID‐19 tests that were issued EUAs are within the scope of the draft guidance document titled “Transition Plan for Medical Devices Issued Emergency Use Authorizations During the COVID‐19 Public Health Emergency,” which addresses the transition back‐to‐normal operations when the emergency use declarations that allowed for FDA to issue EUAs are no longer in effect. However, we're not able to comment on estimated finalization dates for draft guidances, so we do recommend that you keep an eye on FDA's website for any updates there.

Commander Kimberly Piermatteo (FDA):
Thanks again, Toby, for all of your responses. And thank you to those stakeholders who submitted those questions. That wraps up the previously emailed questions for both monkeypox and COVID‐19 test development. We will now take your live questions. As a reminder, to ask a live question, please select the Raise Hand icon at the bottom of your Zoom screen. When you are called on, please follow the prompt in Zoom and select the blue button to unmute your line. Then identify yourself, and ask your question, indicate whether the question is related to monkeypox or COVID‐19, and please, remember to limit yourself to asking one question only. If you have an additional question, you may raise your hand again to get back into the queue. And I will call on you as time permits. So our first live question is coming from Dr. Farhan Khan. I have unmuted your line. Please unmute yourself and ask your question.

---

#### Instance 46: 2022-11-30_Virtual Town Hall 98_section-titles.md
**Line range:** 249-289
**Section:** #### 11. Challenges with Antigen Testing Using Banked Flu B Samples
**Category:** C1 — Declined Specifics / Provided Useful General Guidance
**Appropriateness Score:** 4/5
**Rationale:** This is a real but limited refusal: FDA declines to answer the caller's follow-on question because it concerns the details and status of the caller's specific pre-EUA submission. Before that refusal, however, FDA provided substantial generalized guidance on the underlying scientific and regulatory issue, including challenges with banked flu B samples for antigen tests, openness to dry swabs and some banked samples with transport media, and the need to discuss enrichment strategies with FDA in advance. The core refused question is submission-specific, and useful public guidance was given.
**Speaker refusing:** Tim Stenzel (FDA IVD Director)
**Speaker asking:** Homer Wu

**Excerpt:**
Homer Wu:
Hi, this is Homer Wu from Hopkins MedTech Compliance. I'm just following the question from, I guess, Kathy from BD about the multi‐analyte antigen tests for COVID plus flu A and flu B, either OTC or POC. Does the FDA still allow us to do the flu B with a sample, banked sample or retrospective samples?

Tim Stenzel (FDA IVD Director):
Is this a molecular test or an antigen test?

Homer Wu:
Antigen test.

Tim Stenzel (FDA IVD Director):
So bank samples with antigen tests are really challenging. We have been open to dry swabs. So that is a very specific question. I think we're‐‐ as Toby covered, the multi‐analyte with COVID, flu A/B and/or RSV or other analytes about how we would handle those. So we would ask you to come in with a Pre‐Submission and make sure that we would prioritize your product for review. And then, if so, we can really get into the details about how you might do that. But it's really‐‐ right now, there's significant flu A, but there's almost no flu B, and so that's a real challenge to test that. They really do require direct swab to be able to evaluate them. Kris, anything else to add?

Kris Roth (FDA):
No. And I think if your test uses a transport media, they generally we're more open to banked samples. If the test doesn't have a transport media, just saline or VTM then it's going to be a lot more challenging.

Tim Stenzel (FDA IVD Director):
And we don't necessarily encourage the use of VTM for antigen tests because we have seen significant issues in the COVID pandemic with VTM, and most of the antigen tests have really moved away from allowing transparent media because of those false positive issues.

Homer Wu:
Right. If we can find flu B patients, can we call them back?

Tim Stenzel (FDA IVD Director):
So you're really talking about an enrichment strategy, and we've recommended for any sort of enrichment strategy that you check with the FDA first on your plan to make sure that any potential biases are mitigated to the extent they can be and that the FDA is fine with your study plan. We're open to enrichment, but we want to make sure that it's a good plan, one that we can support an authorization with.

Homer Wu:
OK, thanks. We do have a Pre‐Sub for this before, but was closed, and we still can't follow‐ on, pre‐EUA.

Tim Stenzel (FDA IVD Director):
You have a pre‐EUA, and what's the status? You got responses back?

Homer Wu:
We got response, and we‐‐ I guess like this follow‐on question, can we still use that case?

Tim Stenzel (FDA IVD Director):
So I don't know the details. You're asking about details of a specific submission. So I would go back to whoever responded to you and ask whatever questions you have about the status.

Homer Wu:
OK, alright. Thank you.

Commander Kimberly Piermatteo (FDA):
Thank you, Homer, and thank you, Tim. Alright, our next question. We're circling back to Ashfaaq. You have another question. I have unmuted your line. Please unmute yourself and ask your question.

---

#### Instance 47: 2023-04-26_Virtual Town Hall 103_section-titles.md
**Line range:** 27-43
**Section:** #### 2. COVID-19 Test Regulations Post-Public Health Emergency
**Category:** F1 — Blanket Pre-Filter with Email Redirect
**Appropriateness Score:** 3/5
**Rationale:** This passage contains an active refusal because the moderator explicitly says some previously emailed questions are too detailed or test-case specific and will not be addressed on the call. He also narrows the session to transition-related questions and offers written follow-up and the COVID19dx mailbox as the alternative path. It is a pre-screening refusal of emailed questions with a promised written response.
**Speaker refusing:** Joseph Tartal (FDA)
**Speaker asking:** Multiple

**Excerpt:**
Joseph Tartal (FDA):
Yep, thank you, Toby, for that valuable information. Great presentation. We'll now answer your previously emailed questions about COVID-19 test development validation and the final emergency use authorization transition guidance documents. As always, we have received some questions that are a little too detailed or test case specific that we will not address on today's call. Further, we are focusing primarily on the transition for today's town hall, and some questions we received are not related to the transition and the transition guidances. For those questions that we don't address on today's call, we will try to send a response in writing within a few days. If you have submitted a question and do not hear it addressed, please look for a written response. If you do not receive one within a few days, please feel free to reach back out to the COVID19dx@fda.hhs.gov mailbox. So our first question, we have received several questions about submissions following May 11th, and the transition period for both COVID-19 transition guidances. And I'll try to group a few of these together here to respond to them all together so that we don't have overlap. So there's four parts of this. What is the FDA's plan regarding devices that are currently under EUA submission review post May 11th? During the transition period for the EUA transition guidances will supplements/amendments be allowed for modifications to the emergency use authorization devices? How do the COVID-19 transition guidances impact manufacturers with ongoing clinical studies for future EUA submissions? And in light of FDA's COVID transition guidances, does the FDA prioritize pre-market submissions? So Toby, I'll be looking to you to respond to this first four-part question.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. And yeah, we grouped those together since they sort of share a lot of aspects of the response. So as we discussed, the public health emergency under 319 will expire on May 11th and will not be renewed. The 319 and 564 declarations are independent. The 319 public health emergency expiration does not impact the 564 declarations. The EUA declarations related to COVID-19 under Section 564 of the FD&C Act will continue until the Secretary of HHS ends them. Additionally, as we've discussed and is in the transition plan guidance, we expect 180 day notice before the 564 EUA declarations are terminated. So while the 564 declaration for COVID-19 IVDs is in place, manufacturers may submit EUA requests, including supplemental EUA requests, and FDA will continue to consider them based on our previously communicated prioritization and considering the public health needs. Once the 564 declaration is terminated, we will no longer be authorized to issue EUAs, and therefore we will not continue review of any EUA requests that are under review at that time. As we've talked about, we don't have a date for the 564 declaration being terminated, and we do expect 180 days notice prior to the termination. At this point, however, rather than pursuing an EUA or a modification to an EUA, the FDA is encouraging all manufacturers to submit traditional marketing submissions, such as 510ks, de novos, and possibly PMAs, in some cases. If you have an ongoing clinical study or you're otherwise planning for a future EUA request for a COVID-19 test, we recommend that you consider how your clinical study and other validation efforts may also support a traditional marketing submission, since we are encouraging all manufacturers to pursue traditional marketing submissions. That said, marketing submissions, including 510ks and de novos, are not prioritized in the same way that EUA requests have been. We do aim to review marketing submissions according to the timelines established under the Medical Device User Fee Amendment or MDUFA program. Generally 510k applicants can expect submission acceptance review decisions within 15 calendar days, substantive review decisions within 60 days, and final decisions within 90 days. And those days are calculated as what we refer to as FDA days, so days under FDA review, not including any days where the submission might be placed on hold due to a request for additional information from the applicant.

Joseph Tartal (FDA):
OK. Thank you, Toby, for that information and clarify and ordering out a lot of good information in a nice logical order. So with that, we'll get to our next question, which is, how does the public health emergency termination on May 11th impact LDTs, laboratory developed tests? Can I offer my LDT point of care COVID-19 test after May 11th in alignment with the general enforcement discretion policy for LDTs outside of an EUA declaration? Toby, I'm going to send this question to you.

Toby Lowe (FDA IVD Assoc Director):
Thanks, Joe. I'm not sure why we had point of care in that question. I'll just clarify that most LDTs are not point of care. But for LDTs in general, FDA has generally exercised enforcement discretion, as we've talked about, meaning that we don't exercise our authority to enforce regulatory requirements for LDTs, although we do have that authority. We don't apply the general enforcement discretion approach to certain LDTs, as I mentioned in the slides, including those used for declared emergencies under 564. As we've mentioned, the 319 and 564 are independent. The EUA declaration under 564 is continuing, and we expect that 180-day notice before it is terminated. Therefore, even after the PHE, the Public Health Emergency, termination on May 11th, the EUA declaration for COVID-19 IVDs is still in effect, including the EUA requirements for COVID-19 tests, and that does apply for LDTs. This will continue to help assure that COVID-19 tests remain appropriately accurate and reliable, including in the setting of new variants and sub-variants that we continue to see with COVID-19. Following termination of the EUA declaration, that's the 564 declaration, which we don't have a date yet for that termination, so that 564 declaration for COVID-19 IVDs, once that is terminated, we do intend to have the same enforcement approach for COVID-19 LDTs as we do for other LDTs.

Joseph Tartal (FDA):
OK, thank you for that comprehensive response. With that, we'll go to our next question. Due to a high prevalence of low positive samples in the clinical study cohort for EUA requests for COVID- 19 antigen tests, many sponsors have used a control low positive analysis, where the analysis is stratified the positive percent agreement, PPA, of the investigational device by different percentages of low positive samples, such as 10% and 20%, in the sponsor's clinical study cohort. Can a low positive analysis such as this be used to support a traditional marketing submission such as a 510k. Kris, I'm going to turn that question over to you.

Kris Roth (FDA):
OK, great. Thank you, Joe. So our recommendations to support a traditional marketing submission are different from our recommendations to support an EUA. And at this time, we don't intend to use this type of low positive analysis to support traditional marketing authorizations. Generally, we would expect robust overall performance observed in a prospective clinical study for COVID-19 antigen tests seeking traditional marketing authorization, with a minimum PPA of 80% and a lower bounds of the 95%, confidence interval of 70%. The special controls that such tests must meet are outlined in the FDA's recently granted de novo, and that's de novo number DEN220039. And this de novo was from the Quidel Corporation for the Sofia 2 SARS Antigen plus FIA. The low positive analysis used during the EUA authorization for some tests was based on a variety of factors that were kind of unique to the pandemic. This included high prevalence of reported COVID-19 cases, the viral load of the circulating variants at that time, and the frequent use of serial testing or otherwise repeated regular testing, such as workplace or school testing programs. This all led to a determination that the benefits of wide availability of OTC COVID-19 tests outweighed the potential risks of lower sensitivity. As these factors have now largely shifted with lower prevalence of reported COVID-19 cases, as well as reduced testing, FDA's recommendations for traditional marketing authorization do not include the use of a low positive analysis.

---

## 4. Summary of Results

### Overall Distribution

| Metric | Count |
| --- | --- |
| Total refusal instances identified | 135 |
| Boilerplate opening disclaimers (not scored) | 88 |
| Active refusals (scored) | 47 |
| Files with at least one refusal | 90 of 100 |
||

### Distribution by Category (Active Refusals Only)

| Code | Category | Count | Avg Score |
| --- | --- | --- | --- |
| B | Third-Party Confidentiality Protection | 6 | 5.0 |
| C1 | Declined Specifics / Provided Useful General Guidance | 9 | 4.0 |
| C2 | Partial Answer with Redirect | 14 | 3.0 |
| D1 | Timeline/Status Deflection with Redirect | 2 | 3.0 |
| D2 | Timeline/Status Deflection (No Substantive Response) | 5 | 2.0 |
| E | Deflection to Email (No Substantive Answer) | 3 | 2.0 |
| E2 | Policy/Process Refusal | 7 | 2.0 |
| F1 | Blanket Pre-Filter with Email Redirect | 1 | 3.0 |
| F2 | Blanket Pre-Filter (No Redirect) | 0 | - |
||

### Distribution by Appropriateness Score (Scored Active Refusals Only)

| Score | Label | Count | % of Active Refusals |
| --- | --- | --- | --- |
| 5 | Fully Appropriate | 6 | 13% |
| 4 | Largely Appropriate | 9 | 19% |
| 3 | Mixed / Could Have Done Better | 17 | 36% |
| 2 | Questionable | 15 | 32% |
| 1 | Not Appropriate | 0 | 0% |
||

### Key Findings

- **Average appropriateness score across active refusals: 3.1/5**
- **15 of 47 active refusals (32%) scored 2 or below.**
- **15 of 47 active refusals (32%) scored 4 or above.**
- **31 of 47 active refusals (66%) could plausibly have been generalized publicly.**
- **Most common active refusal category: C2 (14 instances).**

### Interpretation

The data supports the following conclusions:

1. **The balance of refusals in this file leans toward partial answer with redirect.** The most common scored category was C2, which suggests the dominant refusal pattern in this exchange set was not pure non-response so much as partial public guidance paired with off-call deflection.

2. **The overall appropriateness level is mixed.** With an average appropriateness score of 3.1/5, the FDA's refusal behavior in this file was a mix of partial guidance and questionable deflection.

3. **A substantial share of these refusals could still have been generalized publicly.** 31 of 47 scored refusals were marked as potentially generalizable, which indicates that confidentiality was not always the only available response.

4. **The boilerplate disclaimer framed the session before Q&A even began.** The file contains 88 boilerplate instances, reinforcing the expectation that some lines of questioning would be treated as off-limits from the start.
