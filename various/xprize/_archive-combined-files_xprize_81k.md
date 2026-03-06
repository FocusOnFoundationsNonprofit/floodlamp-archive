# ===== START OF FILE _archive-combined-files_xprize_81k.md =====
# xprize (25 files, 81,247 tokens)

# 5,385  _AI_gLAMP and XPrize - pre-competitive vs open-source.md
METADATA
last updated: 2026-02-24 AI and RT
file_name: _AI_gLAMP and XPrize - pre-competitive vs open-source.md
file_date: 2026-03-03
title: FloodLAMP Global LAMP Consortium (gLAMP) - Pre-Competitive vs Open Source Approaches
category: various
subcategory: glamp
tags: glamp, pre-competitive, open-source, pandemic-testing, public-goods
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1453cKnhM8CnfD95gOKvNS-qosJfenbaqR1sjGr2wvWk
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/glamp/_AI_Global%20LAMP%20Consortium%20%28gLAMP%29%20-%20pre-competitive%20vs%20open-source.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 5385
words: 4123
notes: Created by Opus 4.6 Max (Claude) during archive preparation. **PARTIALLY HUMAN REVIEWED - MAY CONTAIN ERRORS** Multi-part analysis exploring gLAMP's pre-competitive collaboration framework versus an open source alternative, legal risks of open R&D collaboration, market failure evidence for treating pandemic testing as a public good, and stakeholder requirements for open source testing infrastructure. Key source: NEB Podcast Interview with Chris Mason (2020-08-31).
summary_short: Multi-part analysis of the gLAMP consortium's pre-competitive collaboration model compared to an open source approach for pandemic diagnostic testing. Covers the legal framework for open R&D collaboration, argues that market failure evidence supports treating pandemic testing protocols as public goods, proposes a curated portfolio of 5-10 open source testing protocol families, and describes stakeholder roles needed to sustain them.


CONTENT

## 1. Prompt (Cleaned) - Meaning of "Pre-Competitive" Framework
What does this term "pre-competitive" mean, in reference it's use within the National Science Foundation (NSF)?

## 1. AI - Meaning of "Pre-Competitive" Framework
"Pre-competitive" is a specific framework used in government-facilitated R&D collaboration — Mason actually referenced **NIST** (National Institute of Standards and Technology) in the interview, not NSF, though NSF uses similar concepts.

The idea is straightforward: you get competitors — companies, academic labs, government groups — into the same room and declare that space **before the point of competition**. Everyone shares foundational knowledge, protocols, data, and failures openly. The understanding is:

- **What happens in the room is shared commons.** Nobody owns the ideas exchanged there.
- **What you do after you leave is your business.** You can take those shared ideas, optimize them, commercialize them, build products — that's fine.
- **The line is drawn at the foundational/enabling level vs. the product/market level.** Getting LAMP to work reliably on saliva = pre-competitive. Building a $50 point-of-care device that does it and selling it = competitive.

NIST does this routinely for measurement standards and reference materials. They convene industry players who would normally never share anything, because everyone benefits from agreeing on baselines — standard reference materials, calibration methods, interoperability specs. No single company gains an edge from the baseline existing; everyone gains an edge from what they build on top of it.

Mason structured GLAMP the same way: the weekly calls, the Slack, the protocol sharing — all pre-competitive. If Color Genomics took that shared protocol and scaled it on Hamilton robots to get FDA EUA, that's them moving into the competitive space. But the underlying LAMP protocol knowledge that enabled it was freely exchanged. Same for anyone else on those calls who might commercialize a variant.

It's basically a way to say "we're all going to be open here, and nobody is going to get sued for participating" — which is critical during a pandemic when speed matters more than IP protection at the foundational layer.

## 2. Prompt (Cleaned) - Legal Risks of Open Collaboration
Explain the "get sued for participating" part. What do you mean by that? How would that play out? Explain it.

## 2. AI RESPONSE - Legal Risks of Open Collaboration
The concern is **antitrust law**. In the US, when competitors share information with each other — pricing, methods, strategies, technology — it can look like collusion or anticompetitive behavior under the Sherman Act and FTC regulations. If five diagnostic companies all get on a call and share their internal R&D on how to make LAMP work better, a regulator or a competitor who wasn't invited could argue that's a form of coordination that disadvantages others in the market.

There's also the **IP side**. Say you're a company and you share a novel technique on a GLAMP call. Someone else on that call files a patent on it, or on a derivative of it. Now you have a dispute: who invented what, who disclosed what, when? Without a clear framework, sharing openly is legally risky because you might be giving away trade secrets or creating prior art that undermines your own future patent filings — or worse, enabling someone else to patent something you thought was shared.

The "pre-competitive" designation addresses both:

- **Antitrust protection**: When a recognized neutral body (like NIST) convenes the collaboration, and it's explicitly structured as pre-competitive knowledge sharing for public benefit, regulators generally view it as legitimate. It's not companies colluding to fix markets — it's companies contributing to a shared baseline that anyone can access. NIST's involvement essentially gives it a government-sanctioned stamp.

- **IP clarity**: By declaring the space pre-competitive, there's an implicit (and sometimes explicit, via participation agreements) understanding that what's shared in that forum is open. You can't take something someone presented on the weekly call and go patent it as your own. The shared knowledge is treated as commons. Your competitive advantage comes from what you build *on top of* that commons — your implementation, your scale, your product design, your regulatory pathway.

In GLAMP's case it was probably more informal than a full legal framework — Mason basically just started a mailing list and weekly calls. But by invoking the "pre-competitive" label and the NIST model, he was signaling to participants: this is a safe space to share. You're not going to get burned for being open here. That matters because without that signal, a company like Color Genomics or someone from Oxford Nanopore might have their legal team say "absolutely not, you can't get on a call and share protocol details with competitors." The pre-competitive framing gives those companies' legal and business teams a recognizable structure they can say yes to.

## 3. Prompt (Cleaned) - Pre-Competitive vs Open Source Approaches
Compare and contrast this pre-competitive framework and approach to an open source effort. Specifically, describe how gLAMP could have been organized as an open source effort to develop and support a few protocols that could truly scale, and how to avoid the fractured nature (the thousand ships idea), because that assumes that people are going to be competitive after and they just belong to the companies. Whereas if the goal is an open source effort, then that really frames the entire thing differently. Make the case for what gLAMP could have looked like if it was created around an open source approach rather than a pre-competitive one.

## 3. AI RESPONSE - Pre-Competitive vs Open Source Approaches
This is a sharp observation and it gets at a fundamental difference in philosophy.

Pre-competitive says: *"We'll share the starting knowledge, then you go compete."* The end state is proprietary products. The commons is temporary — it's a launchpad, not a destination. Everyone takes the shared knowledge, disappears into their own labs and companies, and builds private things. There's no obligation to contribute back. There's no convergence mechanism. The "thousand ships" metaphor isn't a bug in this model — it's the *feature*. Fragmentation is the expected and accepted outcome.

Open source says: *"We'll build the thing together, and the thing itself stays shared."* The end state is a public good. Contributions flow back into the commons. There's governance, versioning, quality control. You can build commercial services *on top of* the open thing (Red Hat sells support for Linux, not Linux itself), but the core artifact — the protocol, the software, the standard — remains collectively owned and collectively improved.

### What GLAMP Actually Was
Honestly, GLAMP was closer to a mailing list with a weekly standup than either model fully realized. People showed up, shared what they were doing, got ideas, left. The  enrichment trick Mason mentioned is a perfect example — someone drops a gem on a call, everyone says "oh cool," and then 30 different labs go try 30 different implementations of it with no shared tracking of what worked and what didn't. The knowledge was exchanged but never *consolidated*.

The "thousand ships" philosophy sounds inspiring in a crisis, but it has a real cost: massive duplication of effort, no convergence on best practices, no shared validation, and ultimately no single protocol that emerges as the robust, well-tested, globally deployable standard. Each ship sails alone. Most sink quietly. The few that make it (like Color Genomics scaling to 14k tests/day) succeed as proprietary implementations, and their optimizations don't flow back to the community that enabled them.

### What an Open Source GLAMP Could Have Looked Like
Imagine GLAMP organized more like a protocol equivalent of Linux or Apache:

- **A shared repository** (GitHub, GitLab, whatever) with versioned, forkable protocol documents — not just slides on a call, but actual maintained SOPs with revision history. "GLAMP Saliva Protocol v2.3" that anyone can pull, run, and submit improvements to.

- **Maintainers and a steering committee** — maybe 5-7 people from different institutions who triage contributions, review proposed changes, and decide what gets merged into the canonical protocol. Not everyone's pet variation, but the rigorously tested consensus version.

- **Convergence on 2-3 protocols, not 50.** One optimized for saliva. One for NP swabs. One for environmental surfaces. Each with defined reagent lists, equipment specs, expected performance metrics, and known failure modes — all documented in the repo. Instead of launching a thousand ships, you put a thousand people on three ships and make those ships really good.

- **A shared validation benchmark.** Standard reference panels — synthetic RNA at known concentrations, contrived saliva samples, whatever — so that when someone proposes a protocol change, it gets tested against the same yardstick. You'd actually know if enrichment improves sensitivity by 0.5 Ct or 2 Ct, because everyone tests against the same panel.

- **An open license** — something like the Open COVID Pledge, or Creative Commons, or a custom protocol license — that explicitly says: this protocol is free. You can use it, you can build products around it, but you cannot patent the protocol itself or any derivative of it. The core method stays in the commons permanently.

- **Contributions flow back.** This is the big one. When Color Genomics optimizes the protocol for Hamilton robots, that automation workflow goes back into the repo. When someone at a university in Nairobi adapts it for low-resource settings with no cold chain, that adaptation goes back in. Every improvement made anywhere benefits everyone everywhere. That's the open source social contract — you take freely, you give back freely.

- **Defined roles beyond just "participant."** Contributors, reviewers, maintainers, a documentation team, a validation team. Not just a hundred people on a Zoom call — an actual organized development effort with accountability and structure.

### The Fundamental Reframe
The pre-competitive framing accepts a world where the goal is to help companies succeed. The open source framing says the goal is to help *the protocol* succeed — and by extension, anyone who needs it, including the low-resource settings and public health departments that can't afford whatever proprietary product eventually comes out of the competitive phase.

Mason's "thousand ships" metaphor reveals the problem. In open source, you don't launch a thousand ships into an ocean of uncertainty. You launch three ships, crew them heavily, chart a course together, and share navigation updates in real time. The uncertainty doesn't go away, but your response to it is coordinated rather than scattered.

The pre-competitive model essentially subsidized the R&D phase for commercial entities. Everyone pooled knowledge for free, then private companies captured the value. An open source model would have said: the value stays public. You can build a business *delivering* the protocol (kits, automation, consulting, regulatory support), but the protocol itself — the actual intellectual contribution that hundreds of scientists made on those calls — belongs to everyone. Permanently.

Given that GLAMP's participants were mostly academics and government-funded researchers anyway, and given that the entire effort was responding to a public health emergency, the open source framing would have been not just viable but arguably more honest about what was actually happening and who was actually doing the work.

## 4. Prompt (Cleaned) - Case for Open Source Pandemic Testing Infrastructure
Make the case that this open source model is what's needed for testing to be used effectively for pandemic preparedness and response. The private market incentives aren't there to have the technology and products in place for the scale and low cost needed for deploying testing quickly and massively during the early phases of a pandemic. My conclusion is that at some level this needs to be a public goods effort, because the private market incentives aren't there.

A good piece of evidence for that is the evaporation of the market opportunity and the bankruptcy of many of the most innovative companies during the pandemic developing new diagnostic testing technology and innovative screening programs. The bottom fell out of the market and the companies got crushed. It should have been through RADx, the XPRIZE, the CDC, and other organizations to really galvanize this open source, Linux-type approach -- except unlike Linux, it's not a single operating system. This was the case I made to the gLAMP group: it's a handful -- half a dozen protocols and program profiles, software, regulatory support, everything to support them. It's not 20. I don't think it's two or three. I thought it was closer to five to ten.

Make this case and build on the great ideas from the previous responses. Make the case, with all this context, for the open source approach over the pre-competitive approach, and describe what would be needed from the many different stakeholders in order to achieve that.

Additionally, add an RT updated list of pandemic testing/screening scenarios. The AI-generated list needs modification:
- High throughput lab-based molecular: label as "clinical," in the standard clinical diagnostic paradigm where results need to be very high confidence and medical decisions may be made based upon them. It's likely purified to improve sensitivity, but that increases cost and lowers throughput.
- Rapid Antigen Test (not "point of care"): the rapid antigen tests are their own thing. Lateral flow. 10-15 minutes to results. Done anywhere. Low cost, ideally $1-3. Massively accessible.
- Central lab screening: ultra high throughput at low cost. Likely not standard purified PCR.
- Remove the high throughput lab-based isothermal category -- too specific.
- Replace "point of care" with "point of need, instrument-free." DirectLAMP is a good candidate test -- direct meaning no RNA extraction. Visual or simple reader output. Suitable for organizations or small groups willing to put the resources into implementing the setup. Ultra low cost, $1 per person, amenable to pooling.
- Add an at-home device category (e.g., Lucira, Detect). High quality molecular result with high sensitivity, but able to be done anywhere. Not ultra-high sensitivity like purified central lab PCR. Ideally qualified and suitable for pooling. Medium expense, in the $20-50 range.
- Add an instrument plus consumable system category, suitable for organizations or small labs. Higher upfront cost but potentially lower consumable cost than a standalone device.
- Keep the pooled surveillance/environmental and sequencing-based surveillance categories.

## 4. AI RESPONSE - Case for Open Source Pandemic Testing Infrastructure
### The Market Failure is the Evidence
The strongest argument for treating pandemic testing as a public good isn't theoretical — it's empirical. The pandemic itself ran the experiment. Dozens of innovative diagnostic companies raised capital, developed novel testing technologies, built out capacity, pursued EUAs, and then got financially destroyed when demand collapsed. The market opportunity appeared, attracted investment, and then evaporated on a timeline completely misaligned with product development cycles, regulatory timelines, and manufacturing scale-up.

This isn't a market that failed because the technology was bad or the companies were incompetent. It failed because the fundamental economics of pandemic testing are structurally incompatible with private market incentives:

- **Demand is spiky and unpredictable.** You need massive capacity for 12-24 months, then almost nothing. No investor funds a factory for a 18-month revenue window with zero visibility on the back end.
- **The price point needed for public health impact is incompatible with profit margins.** Population-scale screening requires tests at $1-5, not $50-150. The unit economics that make testing epidemiologically useful are the same economics that make companies insolvent.
- **Regulatory timelines don't match pandemic timelines.** By the time an EUA comes through — if it comes through — the window of maximum public health impact may have already closed. Companies spend months and millions pursuing authorization for a market that's already contracting.
- **The most innovative approaches get deprioritized.** Technologies that could fundamentally change the accessibility of testing — like direct LAMP protocols that don't require PCR machines — threaten incumbent platforms and don't fit neatly into existing regulatory frameworks. So they get pushed to the back of the review queue while the FDA processes the 200th RT-PCR kit submission from an established IVD manufacturer.

The bankruptcies and collapses aren't anomalies. They're the predictable outcome of asking the private market to solve a public goods problem. The market optimizes for sustainable revenue streams. Pandemics don't offer those.

---

### What Open Source Gets You That Pre-Competitive Doesn't
The pre-competitive model that gLAMP used was well-intentioned and better than nothing, but it accepted a premise that guaranteed fragmentation: that the endpoint was private competition. Every participant was ultimately building toward their own proprietary implementation. The shared knowledge was a means to an end, not the end itself.

An open source model inverts this. The shared protocols, validation data, regulatory packages, and deployment playbooks *are* the product. They persist across pandemic cycles. They're maintained between pandemics. They're available on day one of the next outbreak, not developed from scratch during the crisis.

Concretely, the difference is:

- **Pre-competitive:** 50 groups each develop their own LAMP variant. Knowledge is shared informally. When the pandemic ends, all that work disperses into company IP portfolios, abandoned grants, and shuttered startups. Next pandemic, everyone starts from scratch.
- **Open source:** 5-10 protocols are developed collaboratively, validated rigorously against shared benchmarks, documented to deployment-ready standards, and maintained in perpetuity. Next pandemic, you pull the playbook off the shelf.

---

### The Portfolio: Not One Protocol, Not a Hundred — A Curated Handful
This isn't Linux. There's no single universal testing protocol because testing contexts are genuinely different. But the number of fundamentally distinct deployment scenarios is finite and small. You probably need something like:

#### RT Updated List of Pandemic Testing/Screening Scenarios
1. **Clinical diagnostic molecular** (RT-qPCR or equivalent) — standard clinical diagnostic paradigm where results must be high-confidence and medical decisions may be made based on them. Likely uses purified RNA extraction to maximize sensitivity, but purification increases cost and lowers throughput. For reference labs, hospitals, centralized clinical processing.
2. **Rapid antigen test** — lateral flow, 10-15 minutes to result, done anywhere. Low cost, ideally $1-3 per test. Massively accessible. Lower sensitivity than molecular methods.
3. **Central lab screening** — ultra-high throughput at low cost. Likely not standard purified PCR. Designed for population-scale screening rather than individual clinical diagnosis.
4. **Point-of-need, instrument-free molecular** — e.g., DirectLAMP (no RNA extraction). Visual or simple reader output. Suitable for organizations or small groups willing to put resources into implementing the setup. Ultra low cost (~$1 per person), amenable to pooling.
5. **At-home molecular device** — e.g., Lucira, Detect. High-quality molecular result with high sensitivity, though not ultra-high sensitivity like purified lab PCR. Standalone, able to be done anywhere. Ideally qualified and suitable for pooling. Medium expense, in the $20-50 range.
6. **Instrument + consumable system** — suitable for organizations or small labs. Higher upfront instrument cost but potentially lower per-test consumable cost than standalone at-home devices.
7. **Pooled surveillance / environmental** — wastewater, pooled saliva, surface sampling. Not individual diagnostics but population-level early warning.
8. **Sequencing-based surveillance** — genomic characterization for variant tracking. Not high-volume diagnostics but essential for situational awareness.

#### AI List of Pandemic Testing/Screening Scenarios
1. **High-throughput lab-based molecular** (RT-qPCR or equivalent) — for reference labs, hospitals, centralized processing. The backbone.
2. **High-throughput lab-based isothermal** (LAMP on liquid handlers) — the Color Genomics model. Faster, simpler equipment, scalable to tens of thousands per day.
3. **Point-of-care molecular without instruments** — direct LAMP, no PCR machine, no RNA extraction. Visual or simple reader output. Critical for clinics, schools, workplaces, low-resource settings.
4. **Point-of-care rapid antigen** — lateral flow, minutes to result, deployable anywhere. Lower sensitivity, but massive accessibility.
5. **Pooled surveillance / environmental** — wastewater, pooled saliva, surface sampling. Not individual diagnostics but population-level early warning.
6. **Sequencing-based surveillance** — genomic characterization for variant tracking. Not high-volume diagnostics but essential for situational awareness.

Each of these needs not just a protocol, but a full open source **stack**: the assay chemistry, the sample collection and handling SOP, the instrumentation specs (or lack thereof), the quality control procedures, the data reporting formats, the regulatory submission template, and the deployment playbook for different settings. Maybe 5-8 protocol families, each with a complete support ecosystem.

---

### What Would Be Needed from Each Stakeholder
#### Federal Agencies (CDC, BARDA, NIH/RADx, FDA)
- Fund the development and maintenance of the open protocol portfolio *between* pandemics, not just during them. This is the equivalent of maintaining the Strategic National Stockpile, except for intellectual infrastructure instead of physical supplies.
- RADx and similar programs should have mandated open protocol deliverables. If public money develops a testing method, the method is public. Period. Not "pre-competitive sharing" that becomes proprietary the moment someone adds a barcode.
- FDA needs a standing regulatory pathway for open source diagnostics — a framework where a community-maintained protocol can hold an EUA or equivalent, with defined processes for protocol updates that don't require re-submission from scratch. Think of it like the FDA monograph system for OTC drugs: a community standard that anyone can manufacture against.
- CDC should maintain and distribute reference panels and validation standards for each protocol family — the shared benchmarks that make protocol improvement measurable.

#### NIST and Standards Bodies
- Define the measurement standards, reference materials, and performance benchmarks for each protocol category. This is already in NIST's wheelhouse — extend it explicitly to pandemic diagnostics.
- Convene and maintain the governance structures (steering committees, technical working groups) that manage the open protocol portfolio.

#### Foundations and Philanthropic Organizations
- XPRIZE, Gates Foundation, Wellcome Trust, Open Philanthropy, and others should fund the *maintenance* layer — the boring but essential work of keeping protocols updated, documentation current, validation data refreshed, and contributor communities active between pandemics.
- This is where the "thousand ships" money went wrong during COVID. It funded a hundred competing efforts for 18 months. Redirect that into sustained support for 5-8 canonical protocols over 10 years.

#### Academic Labs
- Contribute protocol improvements back to the commons, not just to pre-prints that get cited and forgotten. The social contract is: you use the open protocol as your starting point, and your improvements go back into the repo.
- Validation studies run against the shared benchmarks, published with open data, feeding into the evidence base for each protocol.

#### Industry
- This is where the open source analogy to Linux and Red Hat is most relevant. Companies don't need to own the protocol to make money. They make money on **implementation and delivery**: manufacturing test kits to the open spec, building and selling instruments optimized for the open protocols, providing automation and LIMS integration, offering regulatory consulting and quality management services, running high-throughput testing operations.
- The protocol is free. The manufactured kit, the validated instrument, the turnkey lab setup, the regulatory compliance package — those are products. There's a real business model here, and it's more sustainable than trying to own a proprietary assay in a market that evaporates.

#### Global Health Organizations (WHO, FIND, etc.)
- Adopt and endorse the open protocols for international deployment. Translate the deployment playbooks for different regulatory jurisdictions and resource contexts.
- Fund and coordinate validation studies in low- and middle-income countries, feeding results back into the protocol portfolio.

#### The Open Source Governance Layer
- A dedicated organization or consortium — something like the Apache Software Foundation or the Linux Foundation but for diagnostic protocols — that holds the IP (or rather, ensures it stays open), manages the contributor community, maintains the repositories, runs the validation program, and interfaces with regulators.
- This doesn't need to be large. A small permanent staff plus a rotating technical advisory board drawn from academia, industry, and public health. Funded by a combination of government grants and foundation support.

---

### The Bottom Line
The pre-competitive model assumes that public health testing will ultimately be delivered by competing private companies, and that the role of collaboration is to give those companies a head start. The open source model assumes that the core testing infrastructure is a public good — like roads, or GPS, or the internet protocols themselves — and that the role of private enterprise is to build services on top of that shared infrastructure, not to own the infrastructure itself.

The pandemic proved the pre-competitive assumption wrong. The companies that were supposed to carry testing forward after the "pre-competitive phase" ended either went bankrupt, pivoted away, or locked up their improvements as proprietary IP that won't be available next time. The knowledge generated during gLAMP calls, RADx grants, and a thousand individual research efforts is now scattered across abandoned Slack channels, expired pre-prints, and defunct company servers.

An open source approach would have produced a durable, maintained, publicly owned portfolio of testing protocols and deployment playbooks — ready to pull off the shelf the next time a novel pathogen emerges. Not a thousand ships. A small fleet, built to last, crewed by a standing community, and available to anyone on earth who needs them.


# 2,025  _context-commentary_various-xprize.md
METADATA
last updated: 2026-03-03 RT
file_name: _context-commentary_various-xprize.md
category: various
subcategory: xprize
words: 1470
tokens: 2025


CONTENT

## Context
The XPRIZE Rapid Covid Testing competition was a $5 million, seven-month global competition launched on July 28, 2020. Organized by the XPRIZE Foundation, it aimed to incentivize the development of fast, frequent, affordable, and scalable COVID-19 testing solutions. The competition grew out of the broader Open COVID Screen initiative that sought to accelerate diagnostic testing availability during the pandemic.

The competition followed a staged process. Teams registered and submitted qualifying applications by the August 31, 2020 deadline. FloodLAMP Biotechnologies was among the 219 semi-finalist teams selected from 35 countries. Semi-finalists were sent blinded proficiency test kits containing contrived, non-infectious samples (synthetic SARS-CoV-2 RNA and inactivated viral particles in various matrices including saliva, nasal swab material, PBS, and water). Kits were shipped between September 24 and October 2, 2020, and teams had one week from receipt to analyze the samples and upload results, which were scored on sensitivity, specificity, and limit of detection. Finalists were originally scheduled to be announced October 23, 2020, with clinical validation at two independent laboratories to follow. An Open Innovation Track ran in parallel, with finalist announcements in December 2020 and winners in February 2021.

The competition offered $1 million to each of up to five winning teams, divided into installments tied to competition performance and successful deployment at test sites. OpenTrons partnered with XPRIZE to provide liquid handling robots to support teams during the pilot phase.

However, significant delays in the preparation and shipment of the proficiency test panels pushed the competition's overall timeline roughly three to six months behind its original schedule. These delays affected all participants and compounded the broader operational challenges of conducting laboratory work during the pandemic.

FloodLAMP's XPRIZE submission was built around the Rabe Cepko RT-LAMP assay protocol from Harvard Medical School, which used chemical inactivation (TCEP/EDTA), nucleic acid purification with ultra-cheap bulk silica ("glass milk"), and isothermal LAMP amplification with colorimetric readout. The approach targeted the ORF1a and N genes using saliva and nasal swab samples, and was designed for pooled screening of large populations at very low per-sample cost (estimated $0.46 per sample with pooling at 10). FloodLAMP's submission emphasized open-source distribution and enabling other basic labs to adopt the screening protocol, rather than building proprietary closed systems. The complete qualifying submission, with parts covering contact/design, results, capacity/scalability, innovation, targets, reagent costs, equipment, and presentation slides, is documented in the archive files.

FloodLAMP submitted proficiency test results but did not advance to the finalist round. Twenty teams were selected as finalists in December 2020, and five grand prize winners were announced in March 2021: Reliable-LFC (antigen testing), ChromaCode, Mirimus, La Jolla Institute for Immunology, and Alveo Technologies (all RNA testing). FloodLAMP's proficiency test results (`XPrize FloodLAMP Proficiency Test Results.md`) show reasonable performance on the Zepto particle rack (51 of 69 correct, zero false positives, with false negatives concentrated near the limit of detection) but poor sensitivity on the Twist Synthetic RNA rack (13 of 56 SARS-CoV-2 positives detected), where the water-based sample matrix was incompatible with FloodLAMP's TCEP/NaI silica purification protocol. This buffer incompatibility was a concern FloodLAMP had flagged in their original submission.

This subcategory contains files documenting the XPRIZE competition from FloodLAMP's perspective: the multi-part qualifying submission, presentation slides, proficiency test results, legal agreements (competitor agreement, team member release/waiver, registration fee certificate), competition communications (guidelines, PR toolkit, field notes toolkit), proficiency test kit documentation (FAQ, handling instructions), the list of 219 semi-finalist teams, and a separate AI-generated analysis exploring the pre-competitive vs. open-source question (`_AI_gLAMP and XPrize - pre-competitive vs open-source.md`). The gLAMP subcategory under various/ contains related material on the Global LAMP Consortium that provides additional context for the open collaboration themes discussed in the commentary below.


## Commentary
FloodLAMP entered the XPRIZE Rapid Covid Testing competition motivated by the same goals that drove the company's founding: scaling affordable, accessible molecular testing during a pandemic. In hindsight, however, the prize competition model may not have been the most effective use of the resources and goodwill available at the time.

The XPRIZE grew out of the Open COVID Screen initiative, which initially attracted participants with a vision of collaborative, open development of diagnostic tools. Many groups, including FloodLAMP, joined because of that open ethos. As the competition formalized, the dynamic shifted toward a more closed and competitive model. This was reflected in the competition's legal framework: early versions of the participation requirements included open protocol disclosure, but that requirement was later removed. Some teams did publish protocols through platforms like protocols.io, but the overall trajectory moved away from open collaboration and toward proprietary competition. The analysis in `_AI_gLAMP and XPrize - pre-competitive vs open-source.md` in this subcategory explores this tension in detail, comparing the pre-competitive framework used by the gLAMP consortium with what a fully open-source alternative could have looked like.

We believe the prize money and the broader resources channeled through initiatives like the XPRIZE could have been more productively directed toward a coordinated open-source effort. The private market incentives for diagnostic development during a pandemic were already powerful — adding prize competition on top may not have accelerated progress, and the competitive framing may have been counterproductive. It attracted groups that would have contributed to an open commons and instead channeled their energy into closed, competitive tracks. The subsequent collapse of the diagnostic testing market, with many innovative companies going bankrupt once pandemic demand evaporated, provides empirical evidence that the private market alone was not a sustainable vehicle for pandemic testing infrastructure.

FloodLAMP's own XPRIZE submission used a silica-based purification protocol (the "glass milk" approach from the Rabe Cepko assay) that, while functional, was not the protocol the company would ultimately prioritize. The silica protocol required a multi-channel pipette and a plate centrifuge, making it finicky and poorly suited for the low-resource, instrument-minimal settings FloodLAMP was targeting. Labs that already had this equipment could generally afford commercial purification columns, limiting the practical value of the ultra-cheap silica approach for its intended audience. FloodLAMP later moved toward a direct LAMP approach (no RNA extraction) that better aligned with its mission of ultra-accessible screening. The early glass milk protocol is not included in the archive for this reason.

FloodLAMP submitted proficiency test results after running the plates in a final-night-run effort but did not advance to the finalist round. The results, now included in the archive with the answer key, show the assay performed reasonably on the rack containing inactivated viral particles in biological matrices (PBS, saliva, nasal) at 4°C — 51 of 69 correct calls, zero false positives, with an effective limit of detection around 2-5 copies/uL. However, the assay failed almost entirely on the rack containing Twist Synthetic RNA in water stored at -80°C, detecting only 13 of 56 positive samples. This was precisely the buffer incompatibility concern FloodLAMP had raised in their submission: the silica-based nucleic acid binding protocol depended on the TCEP inactivation chemistry and did not work with water-based samples that bypassed that step. Specificity was excellent across both racks — zero false positives and zero cross-reactivity calls against 15 other respiratory viruses. These results represent the early glass milk purification version of the FloodLAMP assay. Shortly after the XPRIZE, at the end of 2020, FloodLAMP switched to a direct LAMP protocol (no RNA extraction) with dry swab collection and a combined elution/inactivation step. The analytical performance of that version is best understood from the March 2021 FDA submissions (see file: `regulatory/fl-fda-submissions/2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md`), and the real-world performance is documented in the pilots data, which showed significantly higher sensitivity than rapid antigen tests, particularly for early and asymptomatic cases (see "Comparison with Antigen Tests" in `pilots/pilot-data/_context-commentary_pilots-pilot-data.md`).

The competition experienced substantial delays. Preparation and shipment of the blinded proficiency test panels put the timeline approximately three to six months behind the original schedule. This was not a failing unique to any single participant or to the XPRIZE organizers. It reflected the broader reality of operating during the pandemic: supply chain disruptions, personnel illness, and the personal toll of lockdowns and family care responsibilities made timelines unreliable across the board.

The deeper question raised by the XPRIZE experience is whether prize competitions are an appropriate mechanism for pandemic diagnostics. The structural economics of pandemic testing — spiky, unpredictable demand at price points incompatible with profit margins, on timelines misaligned with regulatory and product development cycles — suggest that testing infrastructure may be better treated as a public good. The resources spent on incentive prizes and fragmented competitive efforts could have funded a coordinated open-source portfolio of testing protocols, maintained collaboratively, available to deploy immediately at the onset of the next outbreak. This was the argument FloodLAMP made to the gLAMP community during the pandemic, and it remains the assessment in retrospect. The related materials in the gLAMP subcategory (under various/) provide additional context for this perspective.


# 612  XPrize - Guidelines or Resources.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize - Guidelines or Resources.md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - Guidelines and Resources
category: various
subcategory: xprize
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1k8SyKMYW6BS44V1ZaPGZoKV3aMFEXPkiSxWAZ1rBsgs/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20-%20Guidelines%20or%20Resources.docx
pdf_gdrive_url: https://drive.google.com/file/d/1wdQMjL-HXOsiDgdWtENM6Z25oS6DG2tZ/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20-%20Guidelines%20or%20Resources.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 612
words: 339
notes: Image-heavy source document; only text links and descriptions preserved in conversion.
summary_short: The XPRIZE Rapid Covid Testing Guidelines and Resources page provides links to the official competition guidelines, team registration fee, competitor agreement, and the Exhibit E Team Member Release, Waiver and Confidentiality Agreement that all semi-finalist team members were required to complete.


CONTENT

## OPEN INNOVATION TRACK
- Up to 10 Finalist OI Teams announced with 20 Finalist teams on December 8
- Team pitch to Covid Apollo Project and Finalist Judges in early January 2021
- Winner announcement February 9
- Deployment Phase (same as standard track)

## DEPLOYMENT RESOURCES
- Introductions to potential deployment sites - if you want them
- Connections to IRBs to provide regulatory framework for deployment - if you want them
- Connections to consulting services that can help set up protocols and compliance challenges for deployment sites - if you want them

## DEPLOYMENT SITE PROCESS
- Five winners receive $500,000 (half of potential prize) following CV
- Within two months, teams provide a proposal and partnerships for deployment site and are eligible to receive an additional $250,000
- Teams complete deployment site testing
- After completing the deployment site testing, teams will received a final installment of $250,000
- Total prize purse per winning team: $1,000,000

### [Guidelines](https://pop.xprize.org/Prizes/ResourceDetail?codename=xprize_rapid_covid_testing&page=guidelines) (PDF)

These Competition Guidelines describe the objectives that govern XPRIZE Covid Testing.

### [Team Registration Fee](https://drive.google.com/file/d/1Zvpb8A2P24dNYF9VqkwroyH07ZGddnX9/view?usp=sharing) (PDF)

### [Competitor Agreement](https://drive.google.com/file/d/1wXkI0XFhfd0omN0UkAaG8ivVRBRyiDbT/view?usp=sharing) (PDF)

A legal and binding document that details the responsibilities of competitors for the prize.

In order to be eligible to advance as a top 200 semifinalist team, the competitor agreement must be completed by the registration deadline. The deadline to register is August 31, 2020 18:59:59 UTC.

### [Competitor Agreement Exhibit E: Team Member Release, Waiver and Confidentiality Agreement](https://pop.xprize.org/Prizes/ResourceDetail?codename=xprize_rapid_covid_testing&page=competitor-agreement-exhibit-e-team-member-release-waiver-and-confidentiality-agreement) (PDF)

In addition to the Competitor Agreement signed by the Team Leader, all Team members are required to acknowledge the terms of the Competitor Agreement by completing the Team Member Release, Waiver and Confidentiality Agreement (Exhibit E).

To complete this activity, each Team Member, including the Team Leader, should complete Exhibit E Team Member Release, Waiver, and Confidentiality Agreement. Please download the corresponding document under the Resources tab, complete all fields, and upload the completed document to this activity.

Whenever possible, individual team member forms should be compiled into one file before being uploaded to POP.


# 1,976  XPrize - List of Semi-Finalist Teams (in alphabetical order).md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize - List of Semi-Finalist Teams (in alphabetical order).md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - List of Semi-Finalist Teams
category: various
subcategory: xprize
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1Tp0hbGabVjm50FpnC3QaUuE2DAskmU6Z6pkDLUwnLRE/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20-%20List%20of%20Semi-Finalist%20Teams%20%28in%20alphabetical%20order%29.docx
pdf_gdrive_url: https://drive.google.com/file/d/1pFYmqP3xaUT8HX01uvdj_UxnxZvubYp_/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20-%20List%20of%20Semi-Finalist%20Teams%20%28in%20alphabetical%20order%29.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1976
words: 1489
notes:
summary_short: Official alphabetical listing of 219 semi-finalist teams from 35 countries competing in the $5M XPRIZE Rapid Covid Testing competition, including FloodLAMP from the United States.


CONTENT

***INTERNAL TITLE:*** List of Semi-Finalist Teams (in alphabetical order)

Total Semi-Finalist Teams: **219**

Total Countries: **35**

| **Team Name** | **Country** |
|----------------------------------------------------|----------------|
| u-Smell-it' - A Rapid Chemosensory Test | United States |
| 19-Xolution | Thailand |
| 1DROP | Switzerland |
| 1tube | United States |
| 3D-Liberty Dx | Australia |
| Aardvark Medical | United States |
| Access Sensor Technologies | United States |
| Accessible Health | United States |
| AEGEA Biotechnologies | United States |
| Allele Biotech COVID | United States |
| ALMAdotcare | Belgium |
| Alveo | United States |
| American Molecular Dx | United States |
| Ampharco | Vietnam |
| ApharSeq | Israel |
| API Pharma LLC | United States |
| API Pharma USA | United States |
| ArcDia mariPOC | Finland |
| Ascella | United States |
| ASSURED | United States |
| Atom Bioworks Inc | United States |
| Avicena Systems 1 | Australia |
| Azar Utah | United States |
| BacterioScan Inc a Delaware corporation | United States |
| Baebies Inc | United States |
| Base Pair Biotechnologies | United States |
| Berking Biotechnology | Chile |
| BGI PATHOGENESIS | China |
| Biocartis US Inc , a Delaware corporation | United States |
| BioGlass | United States |
| Biology Works | United States |
| Biomeme | United States |
| Bioneer | Korea, South |
| BIOPOLYGEN-USA | United States |
| BioSafety Technologies | Israel |
| BLADE Doctors Advanz Testing | United States |
| Boston Biopharma | United States |
| BrewMetrix | United States |
| Buoyant And Magnetic (BAM) Assays | United States |
| Burnet CSC | Australia |
| BVS - Rapid CV-19 With IVDS Technology | United States |
| Canary | United States |
| Cellex | United States |
| ChromaCode | United States |
| CIDx | United States |
| Clip COVID Rapid Antigen Test by Luminostics, Inc | United States |
| Colorimetric RT-LAMP SARS-CoV-2 Research Group | Spain |
| CoronaDetective | Switzerland |
| COVI-SPOT | United States |
| CoviCat | United States |
| COVID 19 Instant Testing & Contact Tracing | United States |
| COVID Bulldogs | United States |
| COVID Continuum | United States |
| COVID No More | Romania |
| CovidNudge | United Kingdom |
| CovidOff | United States |
| COVIDQuickDx | United States |
| COVIDscanDX | United States |
| CovidScope | United States |
| COVIDTell | United Kingdom |
| COVIDXpress | United States |
| COVIRAP(IITKGP) | India |
| CRISP19 | Chile |
| CRISPR-ENHANCE | United States |
| Crystal Diagnostics | United States |
| Dascena | United States |
| Dawatek | United States |
| Diaxxo | Switzerland |
| DISCOPLEX | United States |
| Dr Vida Pocket | Portugal |
| Duke Human Vaccine Institute | United States |
| easyRNA | United States |
| EDNA Dx | United States |
| Electronic Pathogen Detection | United Kingdom |
| Encode Health | United Kingdom |
| Enose-Diagnostics | United States |
| ExosomeDx | United States |
| Extraordinary Innovations LLC | United States |
| FIGHTING COVID 19 | China |
| FloodLAMP | United States |
| Front Line Technologies | United States |
| Galileo - TUNE VID APP | Argentina |
| GenapSys | United States |
| Genesprint-Infrawear | United States |
| GeneSurge | Germany |
| GENOME RESEARCH LIMITED | United Kingdom |
| GoNoGo | United States |
| Grapheal | France |
| Great North Research & Innovation | United Kingdom |
| Happy Lampers | United States |
| Harmony | United States |
| HAYAT | Turkey |
| Hepione | France |
| Highfield Diagnostics | United Kingdom |
| HolographicDiagnostics | United States |
| Hyris | Italy |
| Illucidx | Canada |
| IMT-Detect | Romania |
| Insta-Spot Rapid COVID-19 Point-of-Care Test | United States |
| iSPOT 1 | United States |
| iSPOT 2 | United States |
| KAYA17 | United States |
| Kidod Virion Test | Israel |
| Kinaptic | United States |
| Kunumi | Brazil |
| Lactiga | Canada |
| LAMP-IVD 1 | Australia |
| LAMP-Seq | Germany |
| LessTests | Israel |
| Life Test Ruta N Medellin | Colombia |
| LJI | United States |
| LOMT Pool Testing | Italy |
| LooK SPOT System | Canada |
| Low-Cost Swab to Answer Rapid Covid Test | United States |
| macgyver 1 | Slovakia |
| Medical Diagnostech | South Africa |
| Mikro | Taiwan |
| Mirimus | United States |
| Mmolecular Covid Test | Hong Kong |
| Mobile Xpress Clinics | United States |
| Molecular Mirror | United States |
| Molecular Systems Lab | United States |
| My Rapid Test 1 | Canada |
| My Rapid Test 2 | Canada |
| My Rapid Test 3 | United States |
| my110 | United Kingdom |
| Nabors3D | United States |
| Nanomix | United States |
| Narwhal | United States |
| NDX | United States |
| Neff Lab | United States |
| NEXTGENPCR | Netherlands |
| ni2o inc | United States |
| NowAware | United States |
| NuFaction | United States |
| Oceanit Labs | United States |
| OmniVis | United States |
| Oncophenomics | India |
| OnCovid | India |
| OneRNADx | United States |
| OnsiteGene 1 | United States |
| OnsiteGene 2 | United States |
| OnsiteGene 3 | United States |
| OnsiteGene 4 | United States |
| Ontera | United States |
| Open Science | United States |
| Open-Isothermal-Platforms Dx | Australia |
| PanDemiX | United States |
| PathogenDx | United States |
| PHASE | United States |
| Pinpoint Science | United States |
| Plasmonic PCR | Canada |
| Plenary Research | United States |
| POLAR | United States |
| Poseidon | Singapore |
| PREDICT | United States |
| PreDxion Bio | United States |
| Prime Discoveries | United States |
| Project Lifetime | United States |
| Prompt | United States |
| ProtectLife-AnTaimmu | Taiwan |
| Qanik | Canada |
| Qbiotix | United Kingdom |
| Quaeris | United States |
| Quantification by Design | United States |
| Ram Global | Germany |
| Reliable-LFC, LLC | United States |
| Ricovr Healthcare | United States |
| RNAPath | United States |
| Rosbash | United States |
| SalivaStudyTeam | Germany |
| SANATA | Canada |
| Sante Nano | Canada |
| Scope Fluidics and Curiosity Diagnostics | Poland |
| Scripps Research Institute | United States |
| SensingSelf Mission | Singapore |
| Sensingself Mission 1 | Singapore |
| seqWell | United States |
| SHIELD - University of Illinois, Urbana-Champaign | United States |
| SHINE | United States |
| Simply the Best | Korea, South |
| Single Cycle PCR | United States |
| SiPhox | United States |
| SLINTEC CoronaHunter | Sri Lanka |
| Sol Scientifics | Belgium |
| Sphere | United States |
| Sprightly Health | United States |
| Stanford Microfluidics Lab | United States |
| Steradian Technologies | United States |
| SUREARLY SMART PRO | Korea, South |
| Tapestry | United States |
| Team Genviro | United States |
| Team REVApro | United States |
| Team Spectra | Morocco |
| Team Thylacine-MitoLab | United States |
| TeamPBI | United States |
| Tech4Health | United States |
| Thairanos Rx | Thailand |
| TiMES-Now | United States |
| Tracense systems | Israel |
| UbiDX | United States |
| Ubiquitous Diagnostics | India |
| UCSF COV-ID1 | United States |
| UCSF COV-ID2 | United States |
| UCSF COV-ID3 | United States |
| Unima | Mexico |
| Valetude Primus Healthcare | India |
| VBC-LAMP | Austria |
| VeralizeDevice | United States |
| VERIFAST | United States |
| Veritas PCR Now | United States |
| Viral Testing Inc | Canada |
| ViralAlert | United States |
| WellSIM | United States |
| wePool AI - Intelligent & Efficient Pooled Testing | United States |
| Worlds PROTECT | United States |
| XENOGENE | Spain |
| XING | Australia |
| Zethea | United States |
||


# 2,216  XPrize - Semifinalists and Competition Letter-Shipping.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize - Semifinalists and Competition Letter-Shipping.md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - Semifinalists Competition Letter and Shipping Authorization
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1cI6IPAKNXoI9MOOl6ghgqPJDLSGVkmQK/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20-%20Semifinalists%20and%20Competition%20Letter-Shipping.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 2216
words: 1648
notes: 
summary_short: Official XPRIZE Rapid Testing Competition letter authorizing the shipment of blinded proficiency test kits to 219 semi-finalist teams across 35 countries, documenting that kits contain non-hazardous, non-infectious contrived samples including gamma-irradiated cell line products and synthetic RNA for research use only.


CONTENT

***INTERNAL TITLE:*** XPRIZE Rapid Testing Competition - Shipping Information

This letter serves to provide written documentation, in order to aid in any customs preclearance processes, that the organization/entity (included in list below) is participating as a semifinalist team in the XPRIZE Rapid Testing competition. In order to participate, the listed team has authorization to receive, via FedEx, International and/or Domestic shipping, a blinded proficiency test kit.

This shipment they are receiving contains a test kit for research use only and has no commercial value.

The kit does not contain hazardous chemicals. No infectious agents have been added to any of the samples. Sample targets in the antigen test kit include gamma-irradiated cell line products and purified recombinant proteins. Targets in the RNA test kit include chemically-inactivated cell line products and synthetic RNA.

## Official Semi-Finalist List

- Total Semi-Finalist Teams: 219
- Total Countries: 35

| **Team Name** | **Country** |
|----------------------------------------------------|----------------|
| u-Smell-it' - A Rapid Chemosensory Test | United States |
| 19-Xolution | Thailand |
| 1DROP | Switzerland |
| 1tube | United States |
| 3D-Liberty Dx | Australia |
| Aardvark Medical | United States |
| Access Sensor Technologies | United States |
| Accessible Health | United States |
| AEGEA Biotechnologies | United States |
| Allele Biotech COVID | United States |
| ALMAdotcare | Belgium |
| Alveo | United States |
| American Molecular Dx | United States |
| Ampharco | Vietnam |
| ApharSeq | Israel |
| API Pharma LLC | United States |
| API Pharma USA | United States |
| ArcDia mariPOC | Finland |
| Ascella | United States |
| ASSURED | United States |
| Atom Bioworks Inc | United States |
| Avicena Systems 1 | Australia |
| Azar Utah | United States |
| BacterioScan Inc a Delaware corporation | United States |
| Baebies Inc | United States |
| Base Pair Biotechnologies | United States |
| Berking Biotechnology | Chile |
| BGI PATHOGENESIS | China |
| Biocartis US Inc , a Delaware corporation | United States |
| BioGlass | United States |
| Biology Works | United States |
| Biomeme | United States |
| Bioneer | Korea, South |
| BIOPOLYGEN-USA | United States |
| BioSafety Technologies | Israel |
| BLADE Doctors Advanz Testing | United States |
| Boston Biopharma | United States |
| BrewMetrix | United States |
| Buoyant And Magnetic (BAM) Assays | United States |
| Burnet CSC | Australia |
| BVS - Rapid CV-19 With IVDS Technology | United States |
| Canary | United States |
| Cellex | United States |
| ChromaCode | United States |
| CIDx | United States |
| Clip COVID Rapid Antigen Test by Luminostics, Inc | United States |
| Colorimetric RT-LAMP SARS-CoV-2 Research Group | Spain |
| CoronaDetective | Switzerland |
| COVI-SPOT | United States |
| CoviCat | United States |
| COVID 19 Instant Testing & Contact Tracing | United States |
| COVID Bulldogs | United States |
| COVID Continuum | United States |
| COVID No More | Romania |
| CovidNudge | United Kingdom |
| CovidOff | United States |
| COVIDQuickDx | United States |
| COVIDscanDX | United States |
| CovidScope | United States |
| COVIDTell | United Kingdom |
| COVIDXpress | United States |
| COVIRAP(IITKGP) | India |
| CRISP19 | Chile |
| CRISPR-ENHANCE | United States |
| Crystal Diagnostics | United States |
| Dascena | United States |
| Dawatek | United States |
| Diaxxo | Switzerland |
| DISCOPLEX | United States |
| Dr Vida Pocket | Portugal |
| Duke Human Vaccine Institute | United States |
| easyRNA | United States |
| EDNA Dx | United States |
| Electronic Pathogen Detection | United Kingdom |
| Encode Health | United Kingdom |
| Enose-Diagnostics | United States |
| ExosomeDx | United States |
| Extraordinary Innovations LLC | United States |
| FIGHTING COVID 19 | China |
| FloodLAMP | United States |
| Front Line Technologies | United States |
| Galileo - TUNE VID APP | Argentina |
| GenapSys | United States |
| Genesprint-Infrawear | United States |
| GeneSurge | Germany |
| GENOME RESEARCH LIMITED | United Kingdom |
| GoNoGo | United States |
| Grapheal | France |
| Great North Research & Innovation | United Kingdom |
| Happy Lampers | United States |
| Harmony | United States |
| HAYAT | Turkey |
| Hepione | France |
| Highfield Diagnostics | United Kingdom |
| HolographicDiagnostics | United States |
| Hyris | Italy |
| Illucidx | Canada |
| IMT-Detect | Romania |
| Insta-Spot Rapid COVID-19 Point-of-Care Test | United States |
| iSPOT 1 | United States |
| iSPOT 2 | United States |
| KAYA17 | United States |
| Kidod Virion Test | Israel |
| Kinaptic | United States |
| Kunumi | Brazil |
| Lactiga | Canada |
| LAMP-IVD 1 | Australia |
| LAMP-Seq | Germany |
| LessTests | Israel |
| Life Test Ruta N Medellin | Colombia |
| LJI | United States |
| LOMT Pool Testing | Italy |
| LooK SPOT System | Canada |
| Low-Cost Swab to Answer Rapid Covid Test | United States |
| macgyver 1 | Slovakia |
| Medical Diagnostech | South Africa |
| Mikro | Taiwan |
| Mirimus | United States |
| Mmolecular Covid Test | Hong Kong |
| Mobile Xpress Clinics | United States |
| Molecular Mirror | United States |
| Molecular Systems Lab | United States |
| My Rapid Test 1 | Canada |
| My Rapid Test 2 | Canada |
| My Rapid Test 3 | United States |
| my110 | United Kingdom |
| Nabors3D | United States |
| Nanomix | United States |
| Narwhal | United States |
| NDX | United States |
| Neff Lab | United States |
| NEXTGENPCR | Netherlands |
| ni2o inc | United States |
| NowAware | United States |
| NuFaction | United States |
| Oceanit Labs | United States |
| OmniVis | United States |
| Oncophenomics | India |
| OnCovid | India |
| OneRNADx | United States |
| OnsiteGene 1 | United States |
| OnsiteGene 2 | United States |
| OnsiteGene 3 | United States |
| OnsiteGene 4 | United States |
| Ontera | United States |
| Open Science | United States |
| Open-Isothermal-Platforms Dx | Australia |
| PanDemiX | United States |
| PathogenDx | United States |
| PHASE | United States |
| Pinpoint Science | United States |
| Plasmonic PCR | Canada |
| Plenary Research | United States |
| POLAR | United States |
| Poseidon | Singapore |
| PREDICT | United States |
| PreDxion Bio | United States |
| Prime Discoveries | United States |
| Project Lifetime | United States |
| Prompt | United States |
| ProtectLife-AnTaimmu | Taiwan |
| Qanik | Canada |
| Qbiotix | United Kingdom |
| Quaeris | United States |
| Quantification by Design | United States |
| Ram Global | Germany |
| Reliable-LFC, LLC | United States |
| Ricovr Healthcare | United States |
| RNAPath | United States |
| Rosbash | United States |
| SalivaStudyTeam | Germany |
| SANATA | Canada |
| Sante Nano | Canada |
| Scope Fluidics and Curiosity Diagnostics | Poland |
| Scripps Research Institute | United States |
| SensingSelf Mission | Singapore |
| Sensingself Mission 1 | Singapore |
| seqWell | United States |
| SHIELD - University of Illinois, Urbana-Champaign | United States |
| SHINE | United States |
| Simply the Best | Korea, South |
| Single Cycle PCR | United States |
| SiPhox | United States |
| SLINTEC CoronaHunter | Sri Lanka |
| Sol Scientifics | Belgium |
| Sphere | United States |
| Sprightly Health | United States |
| Stanford Microfluidics Lab | United States |
| Steradian Technologies | United States |
| SUREARLY SMART PRO | Korea, South |
| Tapestry | United States |
| Team Genviro | United States |
| Team REVApro | United States |
| Team Spectra | Morocco |
| Team Thylacine-MitoLab | United States |
| TeamPBI | United States |
| Tech4Health | United States |
| Thairanos Rx | Thailand |
| TiMES-Now | United States |
| Tracense systems | Israel |
| UbiDX | United States |
| Ubiquitous Diagnostics | India |
| UCSF COV-ID1 | United States |
| UCSF COV-ID2 | United States |
| UCSF COV-ID3 | United States |
| Unima | Mexico |
| Valetude Primus Healthcare | India |
| VBC-LAMP | Austria |
| VeralizeDevice | United States |
| VERIFAST | United States |
| Veritas PCR Now | United States |
| Viral Testing Inc | Canada |
| ViralAlert | United States |
| WellSIM | United States |
| wePool AI - Intelligent & Efficient Pooled Testing | United States |
| Worlds PROTECT | United States |
| XENOGENE | Spain |
| XING | Australia |
| Zethea | United States |
||

On Behalf of the XPRIZE Rapid Testing Competition:

Lisa Covington PMP, Prize Lead
XPRIZE Foundation
800 Corporate Pointe, Suite 350
Culver City, CA 90230
U.S.A

Phone: 310-741-4880
Fax: 310-741-4974
https://www.xprize.org


# 628  XPrize - XPRCT Field Notes Comms Toolkit.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize - XPRCT Field Notes Comms Toolkit.md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - Field Notes Communications Toolkit
category: various
subcategory: xprize
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1DFBBbP7CQd8wzN5ZKcMdgrl-qECGjp_pIgu02pJoYzc/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20-%20XPRCT%20Field%20Notes%20Comms%20Toolkit.docx
pdf_gdrive_url: https://drive.google.com/file/d/1JMS9K85AAtlsF3ZVeHx4poXJD0yS2WXw/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20-%20XPRCT%20Field%20Notes%20Comms%20Toolkit.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 628
words: 383
notes:
summary_short: The XPRIZE Rapid Covid Testing Field Notes Communications Toolkit encouraged semi-finalist teams to create 60-second selfie video updates ("Field Notes") documenting their progress, with guidance on content format, suggested social media copy, and promotion of the #RapidTesting campaign across XPRIZE social channels.


CONTENT

***INTERNAL TITLE:*** FIELD NOTES COMMS TOOLKIT

As XPRIZE Rapid Covid Testing semi-finalists receive testing kits to validate their solutions, we want to encourage ongoing filming of prize teams in their quest to help reopen society, safely.

**THE ASK**
Please record yourself and the team in a '60-second selfie video, a 'Field Notes' film, to keep us up-to-date on what is happening. Then, post the video via social channels with #RapidTesting and tag @XPRIZE. Additionally, if you would like a chance to be to have your video produced into an XPRIZE video, please submit your Field Notes to [https://cloud.greenrock.tv/index.php/s/Db1yvXGY2Ku9V9y](https://cloud.greenrock.tv/index.php/s/Db1yvXGY2Ku9V9y)

**WHAT MAKES A GOOD FIELD NOTE?**
This format needn't be bogged down in the context of the overall prize, just a snapshot.

| **What this is** | **What this isn't** |
|------------------------------------|------------------------------------|
| Off the cuff team generated content | Polished content |
| One part of the greater narrative of each prize | All encompassing narrative |
| Snap shot of team activity | Overview of prize |
| Bankable content for raising awareness of prizes | Detailed look at the specifics |
||

**QUESTIONS TO SHAPE THE RECORD**

Who are you and what do you do?

Where are you recording the message from?

What are you working on at the moment?

How will this impact your future work?

Sign off

**WHAT SHOULD I POST ON SOCIAL?**
To help, XPRIZE has drafted a suggested social copy example. Edit where needed to match your channel's tone and voice.

- **Suggested Copy:**
COVID-19 has impacted our lives for too long. We want everything to reopen, but it needs to happen safely. We're one of 219 teams in the $5M XPRIZE Rapid Covid Testing competition trying to solve this problem. Follow along our #RapidTesting journey with @XPRIZE.

**HOW CAN I HELP PROMOTE THIS CAMPAIGN?**
Our goal with the campaign is to let the world know people are working on solutions to help society reopen. Other teams will be posting videos. Click on the hashtag #RapidTesting, and share videos of other competitors. Be sure to mention and tag @XPRIZE in your social media accounts where possible. Here are links to the pages of our most active accounts:

- [Facebook](https://www.facebook.com/XPRIZE/)
- [Twitter](https://twitter.com/xprize)
- [Instagram](https://www.instagram.com/xprize/)
- [YouTube](https://www.youtube.com/user/xprize)

**QUESTIONS?**
For marketing and media inquiries, contact Caden Kinard, Communications Strategist, at [caden.kinard@xprize.org](mailto:caden.kinard@xprize.org).


# 738  XPrize - XPRCT Team PR Toolkit.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize - XPRCT Team PR Toolkit.md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - PR Toolkit for Semi-Finalist Teams
category: various
subcategory: xprize
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1RK-axKhjF-C3hQcZXBqFpu8653tag6gI7zbFvR1xgyk/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20-%20XPRCT%20Team%20PR%20Toolkit.docx
pdf_gdrive_url: https://drive.google.com/file/d/1un8cgfjBgfuICOqKNFLxDxgifOhNw_OV/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20-%20XPRCT%20Team%20PR%20Toolkit.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 738
words: 476
notes:
summary_short: The XPRIZE Rapid Covid Testing PR Toolkit provided semi-finalist teams with guidelines for press release approval, XPRIZE brand usage requirements, the official XPRIZE boilerplate, and approved competition timeline messaging including details on the semi-final proficiency testing and final clinical validation phases.


CONTENT

***INTERNAL TITLE:*** XPRIZE RAPID COVID TESTING PR TOOLKIT FOR SEMI-FINALIST TEAMS

**Press Releases & Usage of XPRIZE brand**

**Press Release Approval Process:**
Teams are required to submit all media releases to XPRIZE via email (testing@xprize.org) at least three (3) business days prior to publication so that we can approve content, clarify messaging and amplify results as applicable.

**XPRIZE Brand Requirements**
The official name of the competition must always be used (XPRIZE Rapid Covid Testing), no abbreviations are allowed.

When referencing the XPRIZE Rapid Covid Testing or XPRIZE, please note that all instances of "XPRIZE" should be expressed in all capital letters and not broken into two lines, no hyphen, and no foundation.

Both XPRIZE logos and XPRIZE Rapid Covid Testing logos can be found [here.](https://drive.google.com/drive/folders/1UL5vld4VxBMr0Huu_uD7pbVK594LSzPI?usp=sharing) When using the XPRIZE logo, there must be clear space around the logo that is equal to the height of the X. Please refer to [XPRIZE.org/brandguide](http://styleguide.xprize.josephmark.com.au/) when creating materials if there is any confusion.

Please include the latest XPRIZE boilerplate in press releases:

*XPRIZE, a 501(c)(3) nonprofit, is the global leader in designing and implementing innovative competition models to solve the world's grandest challenges. Active competitions include the $20 Million NRG COSIA Carbon XPRIZE, the $10 Million Rainforest XPRIZE, the $10 Million ANA Avatar XPRIZE, the $5 Million IBM Watson AI XPRIZE, $5 Million XPRIZE Rapid Reskilling, XPRIZE NextGen Mask Challenge and $5 Million XPRIZE Rapid COVID Testing. For more information, visit [xprize.org](http://xprize.org).*

**XPRIZE Rapid Covid Testing Competition Timeline Messaging**
Society's most vulnerable citizens and populations are disproportionately affected by Covid-19, with tests being inaccessible, too expensive or too slow. Communities are being forced to shut down. Economies are crippled due to Covid-19.

Launched on July 28, 2020, XPRIZE Rapid Covid Testing is a $5 million, 6-month competition that aims to increase Covid-19 testing capabilities 100-times past our current standard, the level of increase needed to more safely return to everyday activities.

219 teams moved on to the semi-finals after being assigned a "pass" by XPRIZE judges. Semi-finalist teams will be sent a blinded Proficiency Test Kit and be required to accurately identify which samples contain Covid-19. Teams will have one week to submit their results to the XPRIZE Data Collaborative, where their results will be scored on specificity, sensitivity, and limits of detection.

Finalists will be announced October 23, 2020, and from there they will have two weeks to send their testing kits and protocols to two separate laboratories for clinical validation. To ensure a fair competition with comparable results, samples within each lab will be split and tested across multiple tests.

A $1-million grand prize will be awarded to each of the top five teams that develop frequent, fast, cheap and easy Covid-19 screening solutions that help meet the surging demand for tests, and relieve the global supply chain. Final event details will be shared at a later date.


# 10,243  XPrize FloodLAMP Proficiency Test Results.md
METADATA
last updated: 2026-03-03 AI and RT
file_name: XPrize FloodLAMP Proficiency Test Results.md
file_date: 2021-01-08
title: FloodLAMP XPRIZE Proficiency Test Results — Submitted Results Merged with Answer Key
category: various
subcategory: xprize
tags: xprize, proficiency-test, results, LAMP, performance
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1kBM2uK_QlB8YW2YHPm1bV6q-jtbv5_qH_ckKkVGXg9s
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Proficiency%20Test%20Results.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10243
words: 5963
notes: Created by Opus 4.6 Max (Claude) during archive preparation. **PARTIALLY HUMAN REVIEWED - MAY CONTAIN ERRORS** Merged analysis file created by FloodLAMP after receiving the XPRIZE answer key (released Dec 23, 2020, one day after the 20 finalists were announced). Combines FloodLAMP's submitted detection calls (1=detected, 0=not detected) with the unblinded sample compositions. FloodLAMP did not advance to the finalist round. Source xlsx file date is Jan 8, 2021.
summary_short: FloodLAMP's XPRIZE Rapid Covid Testing blinded proficiency test results merged with the competition answer key. Contains 157 samples across two racks: NSP17634 (69 Zepto inactivated viral particle samples in PBS, Saliva, and Nasal matrices at 4°C) and XP60846 (88 Twist Synthetic RNA samples in Water at -80°C, including cross-reactivity controls). FloodLAMP detected 51 of 69 NSP samples correctly with zero false positives but performed poorly on the XP rack (13 of 56 SARS-CoV-2 positives detected), likely due to buffer incompatibility with the silica-based purification protocol.


CONTENT

FloodLAMP's blinded proficiency test results from the XPRIZE Rapid Covid Testing competition, merged with the answer key that XPRIZE released after judging. FloodLAMP submitted results under Team ID 3362. The "Detected" column contains FloodLAMP's submitted calls (1=detected, 0=not detected). The remaining columns show the unblinded sample compositions.

## Performance Summary

### Rack NSP17634 (Zepto particles, PBS/Saliva/Nasal, 4°C)
- 69 samples total
- 51 correct calls, 18 false negatives, 0 false positives
- False negatives concentrated at low concentrations (≤2 copies/uL), consistent with the assay's limit of detection
- All samples ≥5 copies/uL detected correctly except both Saliva 25 copies/uL samples (reagent S7, positions C9 and F1), while 25 copies/uL was detected in PBS (3/3) and Nasal (2/2)

### Rack XP60846 (Twist Synthetic RNA, Water, -80°C)
- 88 samples total (56 SARS-CoV-2 positives, 2 SARS-CoV-2 negatives, 30 cross-reactivity controls)
- 13 of 56 SARS-CoV-2 positive samples detected; detections concentrated at ≥100 copies/uL
- 0 false positives on negative controls or cross-reactivity organisms
- Poor sensitivity likely due to incompatibility between the water-based sample matrix and FloodLAMP's TCEP/NaI silica purification protocol, which was designed for use with the TCEP inactivation step on biological samples

These results represent the early glass milk purification version of the FloodLAMP assay. Shortly after the XPRIZE, at the end of 2020, FloodLAMP switched to a direct LAMP protocol (no RNA extraction) with dry swab collection and a combined elution/inactivation step. The analytical performance of that version is documented in the March 2021 FDA submissions (see file: `regulatory/fl-fda-submissions/2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md`), and the real-world performance is documented in the pilots data, which showed significantly higher sensitivity than rapid antigen tests, particularly for early and asymptomatic cases (see "Comparison with Antigen Tests" in `pilots/pilot-data/_context-commentary_pilots-pilot-data.md`)

## Sample Order with Comments
157 samples across two racks, grouped by material and sorted by concentration. Rack XP60846 contains Twist Synthetic RNA in Water at -80°C (including SARS-CoV-2 at various concentrations and cross-reactivity controls). Rack NSP17634 contains Zepto inactivated viral particles in PBS, Saliva, and Nasal matrices at 4°C. Detected column: 1=detected, 0=not detected.

| Team ID | Team Name | RackCode | TubePositionNumber | TubePositionText | TubeCode | Matrix | Detected | Organism | Material | Concentration | ConcUnits | Volume | Matrix | Storage | Comments |
|---------|-----------|----------|--------------------|------------------|----------|--------|----------|----------|----------|---------------|-----------|--------|--------|---------|----------|
| 3362 | FloodLAMP | XP60846 | 1 | A1 | 366700409 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0 | copies/ul | 400 | Water | -80 C | |
| 3362 | FloodLAMP | XP60846 | 55 | E7 | 366687548 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 5 | A5 | 366712371 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.01 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 52 | E4 | 366712356 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.01 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 72 | F12 | 366712442 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.01 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 14 | B2 | 366694960 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.02 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 30 | C6 | 366694985 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.02 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 63 | F3 | 366694995 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.02 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 40 | D4 | 366711036 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.05 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 73 | G1 | 366689613 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.05 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 81 | G9 | 366689631 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.05 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 38 | D2 | 366690457 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 56 | E8 | 366709342 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 74 | G2 | 366708039 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 82 | G10 | 366709774 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 84 | G12 | 366708241 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 13 | B1 | 366708116 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 21 | B9 | 366698486 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 32 | C8 | 366717788 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 50 | E2 | 366717561 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 87 | H3 | 366698482 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 23 | B11 | 366717619 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 25 | C1 | 366717657 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 39 | D3 | 366708480 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 44 | D8 | 366692591 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 54 | E6 | 366717658 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 24 | B12 | 366716893 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 2 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 49 | E1 | 366717974 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 2 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 76 | G4 | 366717915 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 2 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 19 | B7 | 367537858 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 3 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 46 | D10 | 367540998 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 3 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 64 | F4 | 367537838 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 3 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 15 | B3 | 366715730 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 4 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 62 | F2 | 366691066 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 4 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 78 | G6 | 366716658 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 4 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 11 | A11 | 366695734 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 33 | C9 | 366715053 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 41 | D5 | 366695712 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 17 | B5 | 366711757 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 10 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 59 | E11 | 366711821 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 10 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 75 | G3 | 366711755 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 10 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 26 | C2 | 366715055 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 25 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 34 | C10 | 366691100 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 25 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 80 | G8 | 366715070 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 25 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 8 | A8 | 366711552 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 50 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 31 | C7 | 366712660 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 50 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 47 | D11 | 366711173 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 50 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 4 | A4 | 366695473 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 100 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 36 | C12 | 366720128 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 100 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 61 | F1 | 366695856 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 100 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 9 | A9 | 366720642 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 200 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 65 | F5 | 366691660 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 200 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 12 | A12 | 366691008 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 85 | H1 | 366695804 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 43 | D7 | 366695945 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 1000 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 67 | F7 | 366695980 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 1000 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 2 | A2 | 366715002 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 10000 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 57 | E9 | 366713811 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 10000 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | NSP17634 | 1 | A1 | 366713026 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 400 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 64 | F4 | 366713374 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 400 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 7 | A7 | 376016050 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 21 | B9 | 376016058 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 52 | E4 | 376033074 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 65 | F5 | 376033067 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 10 | A10 | 366697750 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 16 | B4 | 366697734 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 63 | F3 | 366708002 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 13 | B1 | 376021817 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 19 | B7 | 376021825 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 9 | A9 | 376016265 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 11 | A11 | 376016273 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 8 | A8 | 366690095 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 35 | C11 | 366711928 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 45 | D9 | 366691359 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 3 | A3 | 376021521 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 32 | C8 | 376021529 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 27 | C3 | 376022129 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 46 | D10 | 376022121 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 14 | B2 | 366712026 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 15 | B3 | 366711315 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 54 | E6 | 366696342 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 29 | C5 | 376027657 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 43 | D7 | 376027665 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 5 | A5 | 376022035 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 53 | E5 | 376022027 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 23 | B11 | 366711895 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | 1x PBS | 4 C | Note this is 200ul input not our usual 500ul |
| 3362 | FloodLAMP | NSP17634 | 38 | D2 | 366691369 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 39 | D3 | 366690057 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 22 | B10 | 376004030 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Nasal | 4 C | Looks to me like they have some RNAse activity in Nasal and Saliva |
| 3362 | FloodLAMP | NSP17634 | 34 | C10 | 376022305 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 26 | C2 | 376023473 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 69 | F9 | 376023481 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 4 | A4 | 376013805 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 28 | C4 | 376013807 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 51 | E3 | 376013806 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 37 | D1 | 376037377 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 60 | E12 | 376037385 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 6 | A6 | 376015191 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 42 | D6 | 376022585 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 62 | F2 | 376045558 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 66 | F6 | 376045559 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 67 | F7 | 376045557 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 57 | E9 | 376022993 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 59 | E11 | 376022985 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 12 | A12 | 376022681 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 48 | D12 | 376022673 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 18 | B6 | 376046710 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 55 | E7 | 376046711 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 56 | E8 | 376046709 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 44 | D8 | 376035089 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 47 | D11 | 376035081 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 33 | C9 | 376036601 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 61 | F1 | 376036656 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 20 | B8 | 376034709 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 31 | C7 | 376034711 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 40 | D4 | 376034710 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 24 | B12 | 376031529 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 30 | C6 | 376031537 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 41 | D5 | 376036393 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 58 | E10 | 376036401 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 2 | A2 | 376004003 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 36 | C12 | 376023535 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 49 | E1 | 376023543 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 17 | B5 | 376035801 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 50 | E2 | 376035793 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 25 | C1 | 376014841 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 68 | F8 | 376004822 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | XP60846 | 37 | D1 | 366719109 | Water | 0 | Twist Human bocavirus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 60 | E12 | 366721496 | Water | 0 | Twist Human bocavirus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 35 | C11 | 366722660 | Water | 0 | Twist Human coronavirus 229E | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 66 | F6 | 366718749 | Water | 0 | Twist Human coronavirus 229E | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 53 | E5 | 366720537 | Water | 0 | Twist Human Coronavirus NL63 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 69 | F9 | 366720553 | Water | 0 | Twist Human Coronavirus NL63 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 18 | B6 | 366718962 | Water | 0 | Twist Human coronavirus OC43 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 27 | C3 | 366721375 | Water | 0 | Twist Human coronavirus OC43 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 7 | A7 | 366721226 | Water | 0 | Twist Human enterovirus 68 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 86 | H2 | 366720181 | Water | 0 | Twist Human enterovirus 68 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 29 | C5 | 366718604 | Water | 0 | Twist Human parainfluenza virus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 45 | D9 | 366718234 | Water | 0 | Twist Human parainfluenza virus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 71 | F11 | 366718621 | Water | 0 | Twist Human parainfluenza virus 4 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 79 | G7 | 366719202 | Water | 0 | Twist Human parainfluenza virus 4 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 3 | A3 | 366721545 | Water | 0 | Twist Human rhinovirus 89 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 58 | E10 | 366720192 | Water | 0 | Twist Human rhinovirus 89 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 22 | B10 | 366718417 | Water | 0 | Twist Influenza A virus H1N1  | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 51 | E3 | 366718921 | Water | 0 | Twist Influenza A virus H1N1  | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 6 | A6 | 366696279 | Water | 0 | Twist Influenza B | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 88 | H4 | 366692526 | Water | 0 | Twist Influenza B | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 28 | C4 | 366713915 | Water | 0 | Twist Influenza H3N2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 70 | F10 | 366718374 | Water | 0 | Twist Influenza H3N2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 42 | D6 | 366720411 | Water | 0 | Twist Measles | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 68 | F8 | 366720896 | Water | 0 | Twist Measles | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 48 | D12 | 366713503 | Water | 0 | Twist MERS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 83 | G11 | 366718951 | Water | 0 | Twist MERS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 16 | B4 | 366718269 | Water | 0 | Twist Mumps | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 20 | B8 | 366713397 | Water | 0 | Twist Mumps | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 10 | A10 | 366722643 | Water | 0 | Twist SARS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 77 | G5 | 366718818 | Water | 0 | Twist SARS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
||


# 933  XPrize FloodLAMP Submission - Part 10 Reagent or Consumable.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - Part 10 Reagent or Consumable.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Submission - Part 10 Reagent or Consumable
category: various
subcategory: xprize
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1C5zZe9I1dL5b3srfZ2a1XzsXWGqghIXn/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Part%2010%20Reagent%20or%20Consumable.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 933
words: 449
notes:
summary_short: FloodLAMP's XPRIZE submission Part 10 Reagent or Consumable spreadsheet itemizes all reagents and consumables required for the pooled LAMP assay at 0.5mL volume with pool level of 10, including TCEP, NaI, NEB LAMP Master Mix, IDT primers, tubes, and PCR plates, with a total estimated cost of $0.46 per sample and $4.57 per run.


CONTENT

## FloodLAMP Reagent List
**Reagent List (if you have a custom reagent the cost must be what you will sell it for)**
| Reagent or Consumable                                                                                                      | Supplier       | Catalog #    | Cost per item (e.g., cost of a tube of enzyme) | Amount (in relevant units, e.g., ul, ug, U, count) per item (e.g., U per tube of enzyme) | Amount per test sample | Amount per test run | Cost per Sample | Cost per Run |
|----------------------------------------------------------------------------------------------------------------------------|----------------|--------------|------------------------------------------------|------------------------------------------------------------------------------------------|------------------------|---------------------|-----------------|--------------|
| Text                                                                                                                       | Text           | Numeric      | Numeric                                        | Numeric                                                                                  | Numeric                | Numeric             | USD ($)         | USD ($)      |
| assumes we are running at the 0.5ml volume for 10 pools                                                                    |                |              |                                                |                                                                                          |                        |                     |                 |              |
|                                                                                                                            |                |              |                                                | pool level                                                                               | 10                     |                     | -               | -            |
| TCEP                                                                                                                       | Sigma          | C4706-10G    | $380                                           | 10                                                                                       | 0.00004                | 0.00036             | $0.00           | $0.01        |
| NaI                                                                                                                        | Sigma          | 217638-2.5KG | $766                                           | 2500                                                                                     | 0.0225                 | 0.225               | $0.01           | $0.07        |
| LAMP Master Mix                                                                                                            | NEB            | 1804L        | $1.83                                          | 1                                                                                        | 0.2                    | 2                   | $0.37           | $3.66        |
| Primers                                                                                                                    | IDT            | 1umole       | $446                                           | 16100                                                                                    | 0.3                    | 3                   | $0.01           | $0.08        |
| Remaining chemicals and primers are negligible cost, full recipes are listed on protocols.io and our website floodlamp.bio |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     |                 |              |
| 15ml Falcon Tube                                                                                                           | Various        |              | $0.20                                          | 1                                                                                        | 0.1                    | 1                   | $0.02           | $0.20        |
| 5ml Transport Tube                                                                                                         | Various        |              | $0.20                                          | 1                                                                                        |                        | 0                   | $0.00           | $0.00        |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     |                 |              |
| 5ml tube                                                                                                                   | CellTreat      | 229449       | $23                                            | 100                                                                                      | 0.1                    | 1                   | $0.02           | $0.23        |
| 1.5ml tube DNA Low Bind                                                                                                    | Eppendorf      |              | $39                                            | 250                                                                                      | 0.11                   | 1.1                 | $0.02           | $0.17        |
| PCR Strip Tubes                                                                                                            | USA Scientific | 1402-2500    | $81                                            | 125                                                                                      | 0.004                  | 0.044               | $0.00           | $0.03        |
| PCR Plates                                                                                                                 | Eppendorf      | EP951020303  | 130                                            | 25                                                                                       | 0.002                  | 0.022               | $0.01           | $0.12        |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
| Total                                                                                                                      |                |              |                                                |                                                                                          |                        |                     | $0.46           | $4.57        |
||


# 431  XPrize FloodLAMP Submission - Part 11 Equipment Setup.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - Part 11 Equipment Setup.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Submission - Part 11 Equipment Setup
category: various
subcategory: xprize
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1ISK1xG-KtccAZa8MYlH_G7qUnX0bZl5Y/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Part%2011%20Equipment%20Setup.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 431
words: 239
notes:
summary_short: FloodLAMP's XPRIZE submission Part 11 Equipment Setup spreadsheet lists all required equipment organized into three categories: assay equipment (dry block heaters, pipettes, centrifuge, vortexer), inactivation station equipment (heater, hole block, centrifuge, splash guard), and additional infrastructure (biosafety cabinet, PCR enclosure).


CONTENT

## FloodLAMP Equipment
**Equipment List**
| Equipment                | Supplier | Catalog #        | Setup Cost |                                             |
|--------------------------|----------|------------------|------------|---------------------------------------------|
| Text                     | Text     | Text             | USD ($)    |                                             |
| ASSAY                    |          |                  |            |                                             |
| Digital Dry Block Heater | various  |                  | $400       | Need 2 of these, 1 for drying and 1 for amp |
| 96 PCR Block             | various  |                  | $200       | Need 2 of these, 1 for drying and 1 for amp |
| Pipettes (3)             | various  |                  | $1,000     | Vary between $50-400 each                   |
| Multichalle Pipette      | various  |                  | $500       | Vary between $200-1000                      |
| Centrifuge               | various  |                  | $1,200     | Depends on throughput and scale, $300-$10K  |
| Vortexer                 | various  |                  | $130       |                                             |
|                          |          |                  |            |                                             |
| INACTIVATION             |          |                  |            |                                             |
| Digital Dry Block Heater | various  |                  | $400       |                                             |
| 16mm Hole Block          | various  |                  | $100       |                                             |
| Centrifuge               | SpinPlus | VS-TC-SPINPLUS-6 | $276       |                                             |
| Pipettes                 | various  |                  | $200       |                                             |
| Splash Guard             | various  |                  | $50        |                                             |
| Vortexer                 | various  |                  | $130       |                                             |
|                          |          |                  |            |                                             |
| ADDITIONAL               |          |                  |            |                                             |
| Biosafety Cabinet        | various  |                  | $5,000     |                                             |
| PCR Enclosure            | various  |                  | $3,000     |
||


# 585  XPrize FloodLAMP Submission - Part 7 Targets.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - Part 7 Targets.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Submission - Part 7 Targets
category: various
subcategory: xprize
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1K6wkOvyBhdVZBEKIYphTfM18wlJ0xKoG/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Part%207%20Targets.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 585
words: 214
notes:
summary_short: FloodLAMP's XPRIZE submission Part 7 Targets spreadsheet lists the 18 LAMP primer sequences targeting ORF1 (As1e set) and N gene (N2 set), plus 6 RNaseP internal control primers used in the FloodLAMP SARS-CoV-2 assay.


CONTENT

## FloodLAMP Targets
**Primer Sequences OR Antigen target/antibody**
| Target Number | Target Gene | Sequence/Antibody |
| --- | --- | --- |
| Numeric | Text | Text |
| 1 | ORF1 As1e_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| 2 | ORF1 As1e_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| 3 | ORF1 As1_F3 | CGGTGGACAAATTGTCAC |
| 4 | ORF1 As1_B3 | CTTCTCTGGATTTAACACACTT |
| 5 | ORF1 As1_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| 6 | ORF1 As1_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| 7 | N N2-FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| 8 | N N2-BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| 9 | N N2-F3 | ACCAGGAACTAATCAGACAAG |
| 10 | N N2-B3 | GACTTGATCTTTGAAATTTGGATCT |
| 11 | N N2-LF | GGGGGCAAATTGTGCAATTTG |
| 12 | N N2-LB | CTTCGGGAACGTGGTTGACC |
| 13 | RNaseP-F3 | TTGATGAGCTGGAGCCA |
| 14 | RNaseP-B3 | CACCCTCAATGCAGAGTC |
| 15 | RNaseP-FIP | GTGTGACCCTGAAGACTCGGTTTTAGCCACTGACTCGGATC |
| 16 | RNaseP-BIP | CCTCCGTGATATGGCTCTTCGTTTTTTTCTTACATGGCTCTGGTC |
| 17 | RNaseP-LF | ATGTGGATGGCTGAGTTGTT |
| 18 | RNaseP-LB | CATGCTGAGTACTGGACCTC |
||

We are currently using the As1e and N2 combined for maximum sensitivity.

We may move to running them in 2 separate reactions to have independent results for confidence in positives.

RNAseP is standard but we plan to move to an RNA only internal control.


# 2,146  XPrize FloodLAMP Submission - Part 8 Results.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - Part 8 Results.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Submission - Part 8 Results
category: various
subcategory: xprize
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1A7XmTQysodHBUUbLf-cBhAZOQLpkIIGV/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Part%208%20Results.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 2146
words: 1286
notes:
summary_short: FloodLAMP's XPRIZE submission Part 8 Results spreadsheet provides test data from multiple experimental runs including blinded real saliva samples spiked with ZeptoMetrix inactivated virions, Twist RNA limit-of-detection runs at 2mL volume, and real nasal/saliva sample screening, all using As1e and N2 combined primer sets with visual binary readout.


CONTENT

## FloodLAMP Results
**Results**
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Sample #                                                                                                                                                      | Known Value | Sample Type               | Sample Source | Known Value | Known Units  | Result Value | Result Units  | Result Interpretation                         | Notes                        |
| Numeric                                                                                                                                                       | Text        | Text                      | Text          | Numeric     | Text         | Numeric      | Text          | Text                                          | Text                         |
||

Blinded real saliva samples, spiked with zeptometrix inactivated virions into raw sample before any processing
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Run#39-1                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-2                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-3                                                                                                                                                      | Positive    | Real, Raw Zepto Spiked    | Saliva        | 5E+03       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-4                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-5                                                                                                                                                      | Positive    | Real, Raw Zepto Spiked    | Saliva        | 2E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-6                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-7                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-8                                                                                                                                                      | Positive    | Real, Raw Zepto Spiked    | Saliva        | 1E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-9                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-10                                                                                                                                                     | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-NTC                                                                                                                                                    | Negative    | Control                   | PBS           |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-TWC                                                                                                                                                    | Positive    | Contrived                 | Saliva        | 2,500       | copies (est) | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
||

Twist LOD run on 2ml volume of inactivated sample, Twist positive control RNA spiked after sample inactivation before purification, same results in duplicate
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Run#37-8K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 4,000       | copies (est) | Positive     | Visual binary | At or above LOD                               | As1e and N2 Primer Set Combo |
| Run#37-4K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 2,000       | copies (est) | Positive     | Visual binary | At or above LOD                               | As1e and N2 Primer Set Combo |
| Run#37-2K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 1,000       | copies (est) | Positive     | Visual binary | At or above LOD                               | As1e and N2 Primer Set Combo |
| Run#37-1K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 500         | copies (est) | Negative     | Visual binary | Below LOD                                     | As1e and N2 Primer Set Combo |
| Run#37-0                                                                                                                                                      | Negative    | Control                   | Saliva        | 0           |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#37-0                                                                                                                                                      | Positive    | Control (Internal RNAseP) | Saliva        | HIGH        |              | Positive     | Visual binary | Correct                                       | RNAseP Primers               |
| Run#37-NTC                                                                                                                                                    | Negative    | Control                   | PBS           | 0           |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#37-NTC                                                                                                                                                    | Negative    | Control (Internal RNAseP) | PBS           | 0           |              | Negative     | Visual binary | Correct                                       | RNAseP Primers               |
||

Real Sample run on individual for a screen, 2 nasal samples split and 25K zeptos spiked into 2.5ml
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Run#86-1A                                                                                                                                                     | ?           | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-1B                                                                                                                                                     | Positive    | Real, Raw Zepto Spiked    | Nasal         | 1E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#86-2A                                                                                                                                                     | Negative    | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-2B                                                                                                                                                     | Positive    | Real, Raw Zepto Spiked    | Nasal         | 1E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#86-3                                                                                                                                                      | Negative    | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-4                                                                                                                                                      | Negative    | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-5                                                                                                                                                      | ?           | Real                      | Saliva        |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-NTC                                                                                                                                                    | Negative    | Control                   | PBS           |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
||

| Column | Definition | Possible Entries |
| --- | --- | --- |
| Sample # | Unique number for sample | Numeric (1-number of samples tested) |
| Known Value | SAR-CoV-2 sample status | Positive, Negative |
| Known Value | If Clinical sample what is the result from the clinical test; If contrived what amount of virus is used in units of copies per uL | Numeric |
| Known Units | If Clinical sample what is the units from the clinical test; If contrived this must be copies/uL | Text (Ct, copies (of virus in reaction)) |
| Result Value | Sample up to 1 decimal point | Numeric |
| Result Units | Units used for reporting | Text (Ct, fluorescence) |
| Result Interpretation | Based off of this result would you declare this positive or negative | Positive, Negative |
||

These are a few example runs, we have done over 100 runs in the last 2 months, 1000+ LAMP reactions.

Many have been characterization and troubleshooting runs, as we've moved labs 3 times.

We now have great exclusive use lab space at MBC Biolabs with:
- A dedicated room with 2 biosafety cabinets where we will run the silica purification on inactivated samples
- 4 lab benches where we'll install 2 PCR hood for setting up LAMP reactions
- 1 5' chemical fume hood for preparing stock solutions involving acids and bases (Inactivation Solution, Binding Solution and Glass Milk)

We have access to a GloMAX plate reader and ABI QuantStudio7 qPCR machine which we intend to use for comparison and characterization, and perhaps as part of our screening service offering.

We have done many successful runs spiking Zeptometrix virions into raw samples at 1e4/ml level.

The challenge is not getting good results on one run, but setting up a system to run continuously under control, especially eliminating failures due to contamination.

We've moved to single use RNA controls, and aliquoting of many components in specific volumes in preparation for pilot runs.


# 264  XPrize FloodLAMP Submission - Part 9 Results Interpretation.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - Part 9 Results Interpretation.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Submission - Part 9 Results Interpretation
category: various
subcategory: xprize
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1W4o2wfltdjJq0MHjf2qvL7-PI3Z2QICj/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Part%209%20Results%20Interpretation.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 264
words: 201
notes:
summary_short: FloodLAMP's XPRIZE submission Part 9 Results Interpretation spreadsheet defines how assay results are interpreted based on combinations of batch positive/negative controls, SARS-CoV-2 target results, and human internal control (RNaseP) results, including rules for reporting findings of potential clinical significance, invalid samples, and batch failures.


CONTENT

## FloodLAMP Results Interpretation
**Result Interpretation**
| Result | Next Step | Batch Control (+) | Batch Control (-) | SARS Target(s) | Human Internal Control Target |  |
| --- | --- | --- | --- | --- | --- | --- |
| Text | Text |  |  | Numeric | Numeric |
| Finding of Potential Clinical Significance | Report result | Positive | Negative | Positive | Positive |  |
| No Finding of Potential Clinical Significance | Report result | Positive | Negative | Negative | Positive |  |
| Finding of Potential Clinical Significance | Run again | Positive | Negative | Positive | Negative/Inconclusive | EUA's say to report this result as positive even if internal control is negative |
| Sample/Pool Invalid | Run again |  |  | Negative | Negative/Inconclusive |  |
| Batch Invalid | Run again | Negative/Inconclusive | Positive/Inconclusive |  |  |  |
||

For a positive pool, we will run the other aliquot of the pool as a confirmation, and run the individual samples.

**Targets**
Target numbers (1,2,n..) need to correspond to names in "targets" table. Define every possibility of target result and how test result is interpreted.


# 302  XPrize FloodLAMP Submission - QS Part 1_ Contact _ Design.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - QS Part 1_ Contact _ Design.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Qualifying Submission - QS Part 1 Contact and Design
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1anBtyopz0Au-hRg19S1sUtt-J1q98n9A/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20QS%20Part%201_%20Contact%20_%20Design.pdf
conversion_input_file_type: pdf
conversion: msmid (note: msmid produced binary output; content extracted via PDF text reader)
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 302
words: 143
notes: 
summary_short: FloodLAMP's XPRIZE QS Part 1 (Contact and Design) submission form captures the team's contact information (San Carlos, CA), technology overview (isothermal LAMP using ORF1a and N gene targets with colorimetric readout), input volumes (500 or 2000 µL), sample sources (nasal swab and saliva), and intended applications (distributed lab and point of care).


CONTENT

## FloodLAMP XPRIZE Qualifying Submission - QS Part 1: Contact and Design

**EMAIL ADDRESS:**
randy@floodlamp.bio

**WHERE ARE YOU LOCATED? (Country, State, City):**
USA, California, San Carlos

**WHAT ORGANIZATION ARE YOU AFFILIATED WITH?**
FloodLAMP Biotechnologies, Public Benefit Corporation

**WHAT IS YOUR PHONE NUMBER?**
415-269-2974

**WHAT TECHNOLOGY DOES YOUR TEST INVOLVE?**
Isothermal

**IF ISOTHERMAL, TELL US MORE ABOUT YOUR ISOTHERMAL TECHNOLOGY:**
Loop-mediated isothermal amplification (LAMP)

**DOES YOUR TEST DETECT NUCLEIC ACID OR PROTEIN?**
Nucleic Acid

**IF NUCLEIC ACID, HOW MANY SEQUENCES DO YOU TARGET?**
2, ORF1a and N

**IF NUCLEIC ACID, HOW MANY GENES DO YOU TEST FOR?**
2, ORF1a and N

**WHAT READ-OUT TECHNOLOGY DO YOU USE?**
Spectrometric (including Colorimetric)

**WHAT IS YOUR INPUT VOLUME PER TEST?**
500 or 2000 µL per test

**WHAT SAMPLE SOURCES ARE YOU PLANNING TO USE ONCE OPERATIONAL?**
Nasal swab, Saliva

**WHICH APPLICATION BEST DEFINES YOUR TEST?**
Distributed Lab


# 503  XPrize FloodLAMP Submission - QS Part 2_ Results.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - QS Part 2_ Results.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Qualifying Submission - QS Part 2 Results
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1yi2ENCjoLdCUSZPqvt4yTjFfGyJOX9Ol/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20QS%20Part%202_%20Results.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 503
words: 317
notes: 
summary_short: FloodLAMP's XPRIZE QS Part 2 (Results) submission documents the team's estimated limit of detection (1-5 copies/µL), which is based on experiments spiking ZeptoMetrix inactivated virions and Twist RNA into samples. Results are qualitative using contrived saliva samples, with no clinical validation pilots completed at time of submission.


CONTENT

## FloodLAMP XPRIZE Qualifying Submission - QS Part 2: Results

**WHAT IS YOUR LIMIT OF DETECTION? (copies/µL)**
1-5 copies/μL

**WHAT TARGETS IS YOUR LIMIT OF DETECTION BASED ON?**
Our estimated limit of detection is based upon both our experiments (spiking ZeptoMetrix inactivated virions into raw samples and Twist RNA into inactivated samples) and what has been found by Rabe, Cepko, Anahtar et al in running the same assay chemistry. We have yet to do the full 20 replicates at several levels near the LOD to precisely determine it, as we have instead prioritized optimizing various aspects of the workflow (primarily handling the silica pellet prior to amplification). Our goal for the LOD is a real world raw sample level of 1e4/mL, as this gets us to 1e5/mL for a pool of 10. This is a level significantly below what has been cited as the suspected threshold for infectiousness of 1e6/mL (level "Capable to Infect Others"). A viral load of 1e5/ml is the level that the CDC seems to be recommending for new "less sensitive" tests. The viral target which we are detecting is a combination of ORF1a and N genes (using AS1e and N2 primers).

**WHAT SAMPLE TYPES ARE USED FOR YOUR LIMIT OF DETECTION?**
Nasal swab, Saliva

**ARE RESULTS BASED OFF OF CLINICAL OR CONTRIVED SAMPLES?**
Contrived

**WHAT SAMPLE TYPES ARE USED FOR YOUR RESULTS?**
Nasal swab, Saliva

**MEDIAN POSITIVE SAMPLE CONCENTRATION (X LOD):**
NA, have not yet run clinical validation pilots

**WHAT IS YOUR POSITIVE PERCENT AGREEMENT (PPA)? (%)**
NA, have not yet run clinical validation pilots

**HOW MANY POSITIVE SAMPLES WERE USED?**
NA, have not yet run clinical validation pilots

**WHAT IS YOUR NEGATIVE PERCENT AGREEMENT (NPA)? (%)**
NA, have not yet run clinical validation pilots

**HOW MANY NEGATIVE SAMPLES WERE USED?**
NA, have not yet run clinical validation pilots

**ARE YOUR RESULTS QUALITATIVE OR QUANTITATIVE?**
Qualitative

**HAVE YOU CONDUCTED CROSS REACTIVITY EXPERIMENTS?**
No


# 1,120  XPrize FloodLAMP Submission - QS Part 3_ Current Capacity _ Scalability.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - QS Part 3_ Current Capacity _ Scalability.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Qualifying Submission - QS Part 3 Current Capacity and Scalability
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1sQKsJTu9oNw76n8sHOpnzwf6LHd0j_8q/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20QS%20Part%203_%20Current%20Capacity%20_%20Scalability.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1120
words: 819
notes: 
summary_short: FloodLAMP's XPRIZE QS Part 3 (Current Capacity and Scalability) submission details the team's testing throughput (50 tests/day current, 200K/day potential with pooling at 100), 2-hour sample-to-result time, sub-$1 per-test cost, sub-$10K capital expense, and plans for scaling through automation with OpenTrons liquid handling and open-source distribution to other labs.


CONTENT

## FloodLAMP XPRIZE Qualifying Submission - QS Part 3: Current Capacity and Scalability

**HOW MANY TESTS DO YOU CURRENTLY RUN PER DAY?**
Approximately 50. We are still in development, not yet running pilots or production. Last week we ran a batch of 24 diluted samples at the 2mL volume (for 10 pools)—a simulation of a run that would comprise 240 individuals.

**HOW MANY TESTS COULD YOU RUN PER DAY WITH CURRENT SETUP?**
200,000, but this is difficult to answer and depends on what is meant by "current setup." Our organization is still doing development but we are growing quickly. The 200,000 number is based on our current leased-lab space at MBC Biolabs, which includes 2 biosafety cabinets, 4 lab bench, and 1 chemical fume hood. It is based on a pooling level of 100, which our LOD supports while still reaching the threshold of infectiousness (~1e6/mL). Likely we will not run many 100 pools immediately and will primarily run 10 pools. The 200,000 number is also based on a 1 hr hands-on time per batch using multichannel pipettes, which is the first configuration we are optimizing in order to spread this screening capability and enable other labs without automation to scale quickly. With a single liquid handling robot, such as an OpenTrons or Bravo (which we intend to bring online in Sept), the hands-on time per batch would go down to minutes and the same personnel could run at least 10X the number of samples/pools.

**HOW LONG DOES IT TAKE TO GO FROM SAMPLE COLLECTION TO RESULTS (MINUTES)?**
2 hrs, though again, this is difficult to answer and can be misleading for our program. We are integrating several components of a screening system to achieve mass scale. Our screening system is designed to find unknown new infections among large populations which will be re-screened frequently. Therefore, a 12 hr turnaround for results is sufficient. Through planning or fast-tracking batches, we could reasonably expect 4 hr sample-to-result times.

**WHAT IS THE HANDS-ON TIME (MINUTES)?**
1 hr per batch of 45 pooled samples (pool level of 10-100) if using multichannel pipettors. 5-10 minutes if using liquid handling robots.

**HOW MANY TESTS CAN BE RUN PER DAY WITH ONE SETUP?**
10K per 24 hr day, assuming no automation, several shifts, and a total of about 10 staff. This scales to 100K+/day with the addition of automation.

**COULD THE TEST BE ADAPTED TO POINT OF CARE?**
No

**CAPITAL EXPENSE:**
Less than $10K to purchase all the equipment for the baseline lab configuration from scratch. However, most labs will likely already have most of the necessary equipment.

**ESTIMATED COST PER TEST:**
<$1, highly dependent on pool level. Current per pool costs are dominated by the NEB LAMP MM (1804) which is $2/rxn in small volumes and approx $0.75 in very large volumes. Consumables cost per pool are currently approximately $5, dropping to <$3 in large volumes. The cost could potentially drop significantly further if the open source LAMP Master Mix using the HIV-1 RT is produced and made available to the LAMP community at a cost less than NEB's product.

**ESTIMATED COST PER RUN:**
For the non-automated configuration using multichannel pipettes, a batch size of 45 samples would currently cost approximately $150 in consumables and need 3 hours of labor. At $40/hr labor charge, the batch cost comes to $270. Assuming the standard pool size of 10, that covers 450 people for a primary screen.

**IS THIS TEST CAPABLE OF POOLING SAMPLES?**
Yes

**DO YOU CURRENTLY POOL SAMPLES?**
Yes

**IF YES, HOW MANY SAMPLES DO YOU CURRENTLY POOL?**
We typically pool 2-5 individuals for our development runs, but do so in a total volume of 5mL (assumes 0.5mL per individual in the pool). One of the key concerns for pooling larger numbers of people (even 10) is whether inhibitors or adulterants present in one sample will cause a failure of the pool. We point to China's success at large scale sample pooling at the level of 10 using cheek swabs as evidence for optimism.

**WHAT ARE THE CURRENT LIMITATIONS TO SCALE THIS TEST?**
The key limitation of our current configuration is not using automation. However, development of this mode is intentional, as access to liquid handling robots and the resources to feed them would be limiting for many, many labs. With multichannel pipetting and the baseline configuration we are developing, those labs can scale to 10K+ people per day screened. Another limitation is the use of silica rather than magnetic beads. Again, this choice has been intentional due to the availability and cost of magnetic capture beads. This is something we will investigate and consider bringing up in parallel to silica. Practically, we are currently limited in resources—both funding and staffing. We closed our first seed investment last week and expect more funding soon. Recruiting qualified employees is particularly challenging now, but we intend to do further outreach and publicize our efforts very soon.


# 1,548  XPrize FloodLAMP Submission - QS Part 4_ Innovation.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - QS Part 4_ Innovation.md
file_date: 2020-09-09
title: FloodLAMP XPRIZE Qualifying Submission - QS Part 4 Innovation
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1Vc87logYUNc-fLuXBXMkH5StXjA2rBMQ/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20QS%20Part%204_%20Innovation.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1548
words: 1120
notes: 
summary_short: FloodLAMP's XPRIZE QS Part 4 (Innovation) submission covers biosafety protocols, data collection and privacy through the custom Appivo app, innovative sample collection approach with in-app guided self-pooling by households, and the team's core innovation of combining available LAMP technology into an open-source integrated screening platform designed for scalable, affordable deployment by any basic laboratory.


CONTENT

## FloodLAMP XPRIZE Qualifying Submission - QS Part 4: Innovation

**(BIO SAFETY) DO YOU USE STANDARD PPE & BIOHAZARD WASTE PROCEDURES TO ENSURE PERSONNEL & BIOHAZARD SAFETY?**
Yes

**(BIO SAFETY) DO YOU HAVE A UNIQUE OR INNOVATIVE WAY TO ENSURE PERSONNEL OR BIOHAZARD SAFETY?**
No

**(DATA) HOW DO YOU COLLECT & PROCESS RESULTS?**
Automated

**(DATA) DO YOU STORE PATIENT RESULTS?**
Yes

**IF YES, HOW DO YOU ENSURE DATA & RESULT PRIVACY & SAFETY?**
Using industry standard procedures. Personal Identifying Information is carefully protected by assigning non-PII unique identifiers that are utilized to track samples and pools.

**(DATA) HOW DO YOU REPORT RESULTS?**
Other

**IF OTHER, PLEASE SPECIFY**
Through a custom app, with the participants selecting their method of notification. In-app notification is the most secure, however some participants may choose less secure but more convenient direct notification by text or email. Anonymized, aggregated results will also be reported to organizations and participants per specific agreements.

**(DATA) DO YOU HAVE AN INNOVATIVE WAY TO PROCESS DATA AND REPORT RESULTS, SUCH AS AN APP?**
Yes

**IF YES, TELL US ABOUT YOUR INNOVATIVE METHOD:**
Yes, we have developed a custom app with a partner company, Appivo, that has a low-code app development platform. The alpha version of our app is currently under review by Apple. Through the app, participants collect individual samples and self-pooled samples, thus greatly streamlining the overall system. The collection process is initiated and supervised by a "sponsor" who is typically a member of the pool and who has accepted responsibility for understanding and implementing the proper collection process. This is facilitated by in-app instruction (including video links), which take a few minutes. The app has been optimized for a smooth user experience and for repeated screening by pre-populating with previous collection information. Pooled collection including minors with parents/guardians is included.

**IF YES, IS THIS METHOD COMPATIBLE WITH SAMPLE POOLING?**
Yes

**(DATA) CAN YOU INTEGRATE WITH EMPLOYERS/ADMIN FOR TRACKING?**
Yes.

**(DATA) CAN YOU INTEGRATE WITH PUBLIC DOMAIN TRACKERS (I.E. APPLE, GOOGLE)?**
Yes, our app has an API.

**(DATA) DO YOU HAVE A UNIQUE OR INNOVATIVE WAY TO COLLECT SAMPLES?**
Yes

**IF YES, HOW DO YOU ENSURE DATA & RESULT PRIVACY & SAFETY?**
The Appivo platform has built-in industry standard security. Appivo has developed apps that include health data for NGOs, and we are leveraging legal and privacy elements of those apps. The Appivo platform enables separate secure instances to be spun up, siloing separate organizations data. The Appivo platform also enables customization of the app—the branding, the design, and the actual functionality. With the mission to spread mass screening capability, FloodLAMP will license the app to other partner organizations, such as universities, which can customize it to suit any specific needs.

**WHAT MAKES YOUR TEST UNIQUE? WHAT IS YOUR BIGGEST INNOVATION?**
FloodLAMP's innovation is combining currently available technology into a highly efficient, integrated infectious disease screening program that can scale—and doing so in a truly open way. New technologies have enormous potential, but it's not clear if any will be ready in 2020. Both well-funded startups and large diagnostics companies will surely bring online significant additional testing capacity, but most of that will be on closed systems or in closed labs, and will be at the highest price the market will bear. Some new options will have impactful tradeoffs, such as antigen tests with LOD's above the threshold for infectiousness. Incentives have not been properly set to encourage the development of a program that any basic lab can affordably bring up and run at significant scale. FloodLAMP is building upon the foundational work of others to combine a sensitive, super cheap, flexible and molecular assay with streamlined sample collection. We are openly sharing not just our protocols but the wrap around processes for a dedicated screening program that is designed to be accessible for all other labs. At the same time we are soliciting help in best practices, under a structure where that knowledge is shared and disseminated, not just used in a limited, closed offering. In short, we're bringing open source to biotech, helping to create the Linux of infectious disease screening. We're building on the current important open efforts (such as JOGL, gLAMP, shared protocol websites like protocols.io) and implementing an integrated screening program to address the global COVID-19 crisis.

**OPENTRONS IS PARTNERING WITH XPRIZE TO SUPPORT TEAMS WITH LIQUID HANDLING ROBOTS DURING THE PILOT PHASE. PLEASE TELL US WHETHER YOUR TEST CAN BENEFIT FROM LIQUID HANDLING AUTOMATION AND HOW YOU MIGHT USE (OR ARE ALREADY USING) THE OPENTRONS LIQUID HANDLER.**
Yes, we can benefit greatly from liquid handling automation. We plan to develop the next configuration of our assay protocol around the OpenTrons robot. There is one at our shared lab facility (MBC Biolabs in San Carlos) that we would like to gain access to in mid Sept. We have consulted with the automation expert at Denali Pharmaceuticals who planned to automate the Rabe Cepko assay, which primarily involves the silica washing steps. We have extensive experience in automating assay protocols involving silica microparticles, through FloodLAMP founder's previous startup True Materials. Affymetrix acquired True Materials in 2008, and we automated several processes for pilot production of liquid arrays using the True Materials' silica microbarcodes on a Biomek Fx, plate washers, and vacuum aspirators. The OpenTrons system is ideal for our automation development because of the low upfront cost of the system and the open source approach of the company.

**PLEASE TELL US ANY REASONS THE PROFICIENCY OR CLINICAL TESTS MAY NOT ACCURATELY RECAPITULATE HOW WELL YOUR TEST WORKS.**
The buffer that the proficiency samples are in may not be compatible with our nucleic acid binding protocol. At a high level, we are not just developing a test (or assay protocol, that's already been done by Rabe and Cepko and their clinical collaborators, Anahtar et al)—we are developing an integrated screening program. That being said, many parts of the system are plug and play. For example, with a slight modification of our existing protocol (elution from the dried pellet), we can go into qPCR as well. We have done almost all of our development on real human samples, starting with raw saliva and soaked nasal swabs. We inactivate those samples with a chemical reducing agent, TCEP/EDTA per the Rabe Cepko protocol. The next step of the main assay protocol uses a high salt solution (NaI) along with the prepared silica for nucleic acid binding, and that may not work or work as well without the TCEP. For our no template controls, we use 1X PBS with the corresponding amount of the TCEP Inactivation Solution. We have not yet run our assay protocol with VTM or other sample collection buffers, as we will collect and inactivate using our protocol.


# 1,045  XPrize FloodLAMP Submission - Slides.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission - Slides.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Qualifying Submission - Presentation Slides
category: various
subcategory: xprize
tags:
source_file_type: gslide
xfile_type: pptx
gfile_url: https://docs.google.com/presentation/d/1-Dd9oNqmi2FmppZ0Xpw7G6Hh5zIz2bsI044IPjb2x5U/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Slides.pptx
pdf_gdrive_url: https://drive.google.com/file/d/1cJaAi1EGXlDuoViG8LRER1EnwJgVYmcL/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Slides.pdf
conversion_input_file_type: pptx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1045
words: 641
notes: Image-heavy presentation; slide titles and text content preserved, visual elements described in italics.
summary_short: FloodLAMP's 12-slide XPRIZE Qualifying Submission presentation covers the company's mission, the Rabe Cepko RT-LAMP assay technology, unique positioning for scaling community screening at low cost, pooling strategy for infectious detection, user-centered at-home sample collection workflow via custom app, field inactivation station design, and lab facilities at MBC Biolabs.


CONTENT

## Slide 1: FloodLAMP Biotechnologies
a Public Benefit Corporation
_FloodLAMP company logo_

floodlamp.bio

## Slide 2: Our Mission
To deploy mass screening to stop the spread of infectious disease.

## Slide 3: Overview of Technology Involved
Sample Collection
- Coordinated by Custom App
- Self pooling by household

Assay Chemistry - Rabe Cepko Protocol from Harvard Medical School:
- Chemical Inactivation using TCEP/EDTA
- Nucleic Acid Purification Protocol using ultra cheap Silica
- Isothermal LAMP amplification with colorimetric readout

## Slide 4: Rabe Cepko RT-LAMP Assay
_Photos showing the three-step Rabe Cepko RT-LAMP assay process_

Inactivation:
- Chemical (TCEP) + Heat
- Deployable outside a lab

Purification:
- Bulk Silica
- Allows larger volumes
- Ultra cheap

Amplification:
- Colorimetric LAMP
- Isothermal
- Instrument Free

## Slide 5: Unique Positioning
_Chart comparing testing approaches by upfront lab setup cost vs throughput, chart data transformed to table below_

| Throughput     | Upfront Lab Setup Cost | Entity/Method                                      |
|----------------|------------------------|----------------------------------------------------|
| 10-200/day     | $5-10K                 | Community Direct-LAMP                              |
| 1-3K/day       | $5-10K                 | FloodLAMP (non-pooled)                             |
| 10K/day to 50K/day | $5-10K                 | FloodLAMP (non-pooled) — Scaling at our facility while also enabling many other labs to scale through openly sharing protocols and procedures. |
| 1-3K to 10K/day| $1-50M                 | Color, Curative, LetsGetChecked                    |
| 1-3K to 10K/day| $1-50M                 | Medium Thruput Academic Labs: IGI, UCSF, Stanford  |
| 50K/day        | $100-250M              | Summer.bio                                         |
| 50K/day        | $100-250M              | Amazon Broad                                       |
||

## Slide 6: Scaling in Multiple Ways
_Diagrams illustrating three scaling strategies_

1. Increase capacity at our facility with automation
2. Enable distributed network of labs through open protocols
3. IVD EUA to widely distribute full assay kits

## Slide 7: Pooling for Infectious Detection
Threshold for "Capable to Infect Others" ~ 1e6/ml

Pooling uses assay sensitivity to scale up coverage - and detect unknown infectious people in interacting populations.

_Diagram illustrating virus kinetics within an individual over ~25 days post-infection, plotting virus concentration on a logarithmic scale through incubation, transmissible, and post-infectious phases, with curves for live virus and viral RNA copies. There's a red bar that appears between approximately days 3–5 (during early incubation/pre-peak), and a yellow bar spans from roughly day 15 to beyond day 25 (post-transmission period)._
Low sensitivity test false-negative only when taken in red/yellow times
But...Only the red area matters clinically & is a very short window of time!

Yellow time period is after transmission period has ended

## Slide 8: Benefitting Public Health
_Illustrations of public health screening scenarios_

Our open protocol and scaling-friendly set up costs mean low overhead (training, cost, equipment) to better screen the populations that need it most.

## Slide 9: User-centered Screening
_Screenshots of the FloodLAMP custom app interface_

- At-home collection
- Pooling by household or pod
- Custom software for recording samples and tracking results
- Prompts for repeat screens

## Slide 10: Sample Collection Workflow
_Illustrations showing the 6-step sample collection workflow_

1. Register
   - Visit app and register
   - Your info added
   - Your organization (if applicable)
2. Get
   - Receive your kit in the mail
   - Review instructions
3. Learn
   - Watch videos on collection techniques and process
   - Prepare other participants if you're a sponsor
4. Collect
   - Identify who you're collecting for in app
   - Collect individual samples + record in app
   - Pool samples + record in app
5. Drop off
   - Drop samples in secure drop box and record in app OR
   - Drop with staff member who records in system
6. View status
   - See state of your sample (in transit, processing, result, etc)
   - See updates for next collection
   - Sharing options for adoption spread

## Slide 11: Field Inactivation Station
_Photo showing the field inactivation station setup_

## Slide 12: FloodLAMP Facilities at MBC Biolabs
_Photos of FloodLAMP laboratory facilities at MBC Biolabs_


# 10,730  XPrize FloodLAMP Submission.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize FloodLAMP Submission.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Qualifying Submission - Complete Working Document
category: various
subcategory: xprize
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1TedJlyh6UsNWcFVnEV-9aOIdkoOTGm29c7-wcjD9FAc/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission.docx
pdf_gdrive_url: https://drive.google.com/file/d/1xpkId8BJRVRpSSdZXJRI8ubDLo6-5fAJ/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10730
words: 6557
notes: 
summary_short: FloodLAMP's comprehensive XPRIZE Rapid Covid Testing Qualifying Submission working document, covering all parts of the submission including contact and design information (QS Part 1), test results and limit of detection (QS Part 2), current capacity and scalability plans (QS Part 3), innovation highlights including the custom Appivo app and open-source approach (QS Part 4), and references to the presentation, protocols, and spreadsheet submissions (Parts 5-13).


CONTENT

## PART 1: CONTACT & DESIGN
[Our QS1 submission (pdf)](https://drive.google.com/file/d/1wP-f_qg2sX9EZ4Hqp3YN4mwR7YfEsU8j/view?usp=sharing)
[Our QS1 submission (text only)](https://docs.google.com/spreadsheets/d/14remjAC1-H7cidK0EVApdikdE4LF4kTIC_jGoAIljAs/edit?usp=sharing)

EMAIL ADDRESS *
randy@floodlamp.bio
WHERE ARE YOU LOCATED? *
Country, State, City
USA, California, San Carlos
WHAT ORGANIZATION ARE YOU AFFILIATED WITH? *
FloodLAMP Biotechnologies, Public Benefit Corporation
WHAT IS YOUR PHONE NUMBER? *
415-269-2974
WHAT TECHNOLOGY DOES YOUR TEST INVOLVE? *
PCR
Isothermal
NGS
Antigen detection
Hybridization
CRISPR
Other
IF OTHER, PLEASE SPECIFY
IF PCR, TELL US MORE ABOUT YOUR PCR TECHNOLOGY
RT-dPCR
RT-qPCR
Melting point
Other
IF OTHER, PLEASE SPECIFY
IF ISOTHERMAL, TELL US MORE ABOUT YOUR ISOTHERMAL TECHNOLOGY
Loop-mediated isothermal amplification (LAMP)
Recombinase polymerase amplification (RPA)
Nick Enzyme Amplification Reaction (NEAR)
Transcription-mediated amplification (TMA)
Rolling-circle amplification (RCA)
Other
IF OTHER, PLEASE SPECIFY
DOES YOUR TEST DETECT NUCLEIC ACID OR PROTEIN? *
Protein
Nucleic Acid
IF NUCLEIC ACID, HOW MANY SEQUENCES DO YOU TARGET?
2, ORF1a and N
IF PROTEIN, HOW MANY ANTIGENS DO YOU TARGET?
IF NUCLEIC ACID, HOW MANY GENES DO YOU TEST FOR?
2, ORF1a and N
IF PROTEIN, HOW MANY PROTEINS DO YOU TEST FOR?
WHAT READ-OUT TECHNOLOGY DO YOU USE?
Ct
Fluorometric
Spectrometric (including Colorimetric)
Turbidity
Sequencing
Other
IF OTHER, PLEASE SPECIFY
WHAT IS YOUR INPUT VOLUME PER TEST? *
uL per test
500 or 2000
WHAT SAMPLE SOURCES ARE YOU PLANNING TO USE ONCE OPERATIONAL? *
Nasal swab
Saliva
Other
IF OTHER, PLEASE SPECIFY
WHICH APPLICATION BEST DEFINES YOUR TEST? *
At home/personal use
Point of care
Distributed Lab
High Throughput Lab
Other
IF OTHER, PLEASE SPECIFY

## PART 2: RESULTS
[Our QS2 submission (pdf)](https://drive.google.com/file/d/1SfsQ6aNN_ttF331vH_WZtj0Wv0GN6lVj/view?usp=sharing)
[Our QS2 submission (text only, 2nd tab)](https://docs.google.com/spreadsheets/d/14remjAC1-H7cidK0EVApdikdE4LF4kTIC_jGoAIljAs/edit?usp=sharing)

WHAT IS YOUR LIMIT OF DETECTION? *
Limit of Detection (LoD). (copies/uL)
1-5 copies/μL
WHAT TARGETS IS YOUR LIMIT OF DETECTION BASED ON? *
Our estimated limit of detection is based upon both our experiments (spiking ZeptoMetrix inactivated virions into raw samples and Twist RNA into inactivated samples) and what has been found by Rabe, Cepko, Anahtar et al in running the same assay chemistry. We have yet to do the full 20 replicates at several levels near the LOD to precisely determine it, as we have instead prioritized optimizing various aspects of the workflow (primarily handling the silica pellet prior to amplification). Our goal for the LOD is a real world raw sample level of 1e4/mL, as this gets us to 1e5/mL for a pool of 10. This is a level significantly below what has been cited as the suspected threshold for infectiousness of 1e6/mL (level "Capable to Infect Others"). A viral load of 1e5/ml is the level that the CDC seems to be recommending for new "less sensitive" tests. The viral target which we are detecting is a combination of ORF1a and N genes (using AS1e and N2 primers).
WHAT SAMPLE TYPES ARE USED FOR YOUR LIMIT OF DETECTION? *
NP
OP
Nasal swab
Sputum
Saliva
Not applicable
Other
IF OTHER, PLEASE SPECIFY
ARE RESULTS BASED OFF OF CLINICAL OR CONTRIVED SAMPLES? *
Clinical
Contrived
Both
WHAT SAMPLE TYPES ARE USED FOR YOUR RESULTS *
NP
OP
Nasal swab
Sputum
Saliva
Other
IF OTHER, PLEASE SPECIFY
MEDIAN POSITIVE SAMPLE CONCENTRATION (X LOD) *
NA, have not yet run clinical validation pilots
WHAT IS YOUR POSITIVE PERCENT AGREEMENT (PPA)? (%) *
NA, have not yet run clinical validation pilots
HOW MANY POSITIVE SAMPLES WERE USED *
NA, have not yet run clinical validation pilots
WHAT IS YOUR NEGATIVE PERCENT AGREEMENT (NPA)? (%) *
NA, have not yet run clinical validation pilots
HOW MANY NEGATIVE SAMPLES WERE USED *
NA, have not yet run clinical validation pilots
ARE YOUR RESULTS QUALITATIVE OR QUANTITATIVE? *
Qualitative
Quantitative
HAVE YOU CONDUCTED CROSS REACTIVITY EXPERIMENTS? *
Yes
No

## PART 3: CURRENT CAPACITY & SCALABILITY
[Our QS3 submission (pdf)](https://drive.google.com/file/d/1dOuNX6JDfQPF04VqDqpCyXDiYeMnGS5h/view?usp=sharing)
[Our QS3 submission (text only, 3rd tab)](https://docs.google.com/spreadsheets/d/14remjAC1-H7cidK0EVApdikdE4LF4kTIC_jGoAIljAs/edit?usp=sharing)

HOW MANY TESTS DO YOU CURRENTLY RUN PER DAY? *
Approximately 50. We are still in development, not yet running pilots or production. Last week we ran a batch of 24 diluted samples at the 2mL volume (for 10 pools)—a simulation of a run that would comprise 240 individuals.

HOW MANY TESTS COULD YOU RUN PER DAY WITH CURRENT SETUP? *
200,000, but this is difficult to answer and depends on what is meant by "current setup." Our organization is still doing development but we are growing quickly. The 200,000 number is based on our current leased-lab space at MBC Biolabs, which includes 2 biosafety cabinets, 4 lab bench, and 1 chemical fume hood. It is based on a pooling level of 100, which our LOD supports while still reaching the threshold of infectiousness (~1e6/mL). Likely we will not run many 100 pools immediately and will primarily run 10 pools. The 200,000 number is also based on a 1 hr hands-on time per batch using multichannel pipettes, which is the first configuration we are optimizing in order to spread this screening capability and enable other labs without automation to scale quickly. With a single liquid handling robot, such as an OpenTrons or Bravo (which we intend to bring online in Sept), the hands-on time per batch would go down to minutes and the same personnel could run at least 10X the number of samples/pools.

HOW LONG DOES IT TAKE TO GO FROM SAMPLE COLLECTION TO RESULTS (MINUTES)? *
2 hrs, though again, this is difficult to answer and can be misleading for our program. We are integrating several components of a screening system to achieve mass scale. Our screening system is designed to find unknown new infections among large populations which will be re-screened frequently. Therefore, a 12 hr turnaround for results is sufficient. Through planning or fast-tracking batches, we could reasonably expect 4 hr sample-to-result times.

WHAT IS THE HANDS-ON TIME (MINUTES) *
1 hr per batch of 45 pooled samples (pool level of 10-100) if using multichannel pipettors. 5-10 minutes if using liquid handling robots.

HOW MANY TESTS CAN BE RUN PER DAY WITH ONE SETUP? *
10K per 24 hr day, assuming no automation, several shifts, and a total of about 10 staff. This scales to 100K+/day with the addition of automation.

COULD THE TEST BE ADAPTED TO POINT OF CARE? *
Yes
No

CAPITAL EXPENSE *
Less than $10K to purchase all the equipment for the baseline lab configuration from scratch. However, most labs will likely already have most of the necessary equipment.

ESTIMATED COST PER TEST *
<$1, highly dependent on pool level. Current per pool costs are dominated by the NEB LAMP MM (1804) which is $2/rxn is small volumes and approx $0.75 in very large volumes. Consumables cost per pool are currently approximately $5, dropping to <$3 in large volumes. The cost could potentially drop significantly further if the open source LAMP Master Mix using the HIV-1 RT is produced and made available to the LAMP community at a cost less than NEB's product.

ESTIMATED COST PER RUN *
For the non-automated configuration using multichannel pipettes, a batch size of 45 samples would currently cost approximately $150 in consumables and need 3 hours of labor. At $40/hr labor charge, the batch cost comes to $270. Assuming the standard pool size of 10, that covers 450 people for a primary screen.

IS THIS TEST CAPABLE OF POOLING SAMPLES? *
Yes
No

DO YOU CURRENTLY POOL SAMPLES? *
Yes
No

IF YES, HOW MANY SAMPLES DO YOU CURRENTLY POOL?
We typically pool 2-5 individuals for our development runs, but do so in a total volume of 5mL (assumes 0.5mL per individual in the pool). One of the key concerns for pooling larger numbers of people (even 10) is whether inhibitors or adulterants present in one sample will cause a failure of the pool. We point to China's success at large scale sample pooling at the level of 10 using cheek swabs as evidence for optimism.

WHAT ARE THE CURRENT LIMITATIONS TO SCALE THIS TEST? *
The key limitation of our current configuration is not using automation. However, development of this mode is intentional, as access to liquid handling robots and the resources to feed them would be limiting for many, many labs. With multichannel pipetting and the baseline configuration we are developing, those labs can scale to 10K+ people per day screened. Another limitation is the use of silica rather than magnetic beads. Again, this choice has been intentional due to the availability and cost of magnetic capture beads. This is something we will investigate and consider bringing up in parallel to silica. Practically, we are currently limited in resources—both funding and staffing. We closed our first seed investment last week and expect more funding soon. Recruiting qualified employees is particularly challenging now, but we intend to do further outreach and publicize our efforts very soon.

## PART 4: INNOVATION
[Our QS4 submission (pdf)](https://drive.google.com/file/d/1u_qbndJkwJNNYn9X3fSOortUJZMlxYze/view?usp=sharing)
[Our QS4 submission (text only, 4rd tab)](https://docs.google.com/spreadsheets/d/14remjAC1-H7cidK0EVApdikdE4LF4kTIC_jGoAIljAs/edit?usp=sharing)
(BIO SAFETY) DO YOU USE STANDARD PPE & BIOHAZARD WASTE PROCEDURES TO ENSURE PERSONNEL & BIOHAZARD SAFETY? *
Yes
No
(BIO SAFETY) DO YOU HAVE A UNIQUE OR INNOVATIVE WAY TO ENSURE PERSONNEL OR BIOHAZARD SAFETY? *
Yes
No
IF YES, TELL US ABOUT YOUR UNIQUE SAFETY PROTOCOLS.
(DATA) HOW DO YOU COLLECT & PROCESS RESULTS? *
Automated
Manual
Other
IF OTHER, PLEASE SPECIFY
(DATA) DO YOU STORE PATIENT RESULTS? *
Yes
No
IF YES, HOW DO YOU ENSURE DATA & RESULT PRIVACY & SAFETY?
Using industry standard procedures. Personal Identifying Information is carefully protected by assigning non-PII unique identifiers that are utilized to track samples and pools.
(DATA) HOW DO YOU REPORT RESULTS? *
In person at time of test
Through an automated service
Manually call/text/email
Other
IF OTHER, PLEASE SPECIFY
Through a custom app, with the participants selecting their method of notification. In-app notification is the most secure, however some participants may choose less secure but more convenient direct notification by text or email. Anonymized, aggregated results will also be reported to organizations and participants per specific agreements.
(DATA) DO YOU HAVE AN INNOVATIVE WAY TO PROCESS DATA AND REPORT RESULTS, SUCH AS AN APP? *
Yes
No
IF YES, TELL US ABOUT YOUR INNOVATIVE METHOD
Yes, we have developed a custom app with a partner company, Appivo, that has a low-code app development platform. The alpha version of our app is currently under review by Apple. Through the app, participants collect individual samples and self-pooled samples, thus greatly streamlining the overall system. The collection process is initiated and supervised by a "sponsor" who is typically a member of the pool and who has accepted responsibility for understanding and implementing the proper collection process. This is facilitated by in-app instruction (including video links), which take a few minutes. The app has been optimized for a smooth user experience and for repeated screening by pre-populating with previous collection information. Pooled collection including minors with parents/guardians is included.
IF YES, IS THIS METHOD COMPATIBLE WITH SAMPLE POOLING?
Yes
No
(DATA) CAN YOU INTEGRATE WITH EMPLOYERS/ADMIN FOR TRACKING? *
Yes.
(DATA) CAN YOU INTEGRATE WITH PUBLIC DOMAIN TRACKERS (I.E. APPLE, GOOGLE)? *
Yes, our app has an API.
(DATA) DO YOU HAVE A UNIQUE OR INNOVATIVE WAY COLLECT SAMPLES? *
Yes
No
IF YES, HOW DO YOU ENSURE DATA & RESULT PRIVACY & SAFETY?
The Appivo platform has built-in industry standard security. Appivo has developed apps that include health data for NGOs, and we are leveraging legal and privacy elements of those apps. The Appivo platform enables separate secure instances to be spun up, siloing separate organizations data. The Appivo platform also enables customization of the app—the branding, the design, and the actual functionality. With the mission to spread mass screening capability, FloodLAMP will license the app to other partner organizations, such as universities, which can customize it to suit any specific needs.

WHAT MAKES YOUR TEST UNIQUE? WHAT IS YOUR BIGGEST INNOVATION? *
FloodLAMP's innovation is combining currently available technology into a highly efficient, integrated infectious disease screening program that can scale—and doing so in a truly open way. New technologies have enormous potential, but it's not clear if any will be ready in 2020. Both well-funded startups and large diagnostics companies will surely bring online significant additional testing capacity, but most of that will be on closed systems or in closed labs, and will be at the highest price the market will bear. Some new options will have impactful tradeoffs, such as antigen tests with LOD's above the threshold for infectiousness. Incentives have not been properly set to encourage the development of a program that any basic lab can affordably bring up and run at significant scale. FloodLAMP is building upon the foundational work of others to combine a sensitive, super cheap, flexible and molecular assay with streamlined sample collection. We are openly sharing not just our protocols but the wrap around processes for a dedicated screening program that is designed to be accessible for all other labs. At the same time we are soliciting help in best practices, under a structure where that knowledge is shared and disseminated, not just used in a limited, closed offering. In short, we're bringing open source to biotech, helping to create the Linux of infectious disease screening. We're building on the current important open efforts (such as JOGL, gLAMP, shared protocol websites like protocols.io) and implementing an integrated screening program to address the global COVID-19 crisis.

OPENTRONS IS PARTNERING WITH XPRIZE TO SUPPORT TEAMS WITH LIQUID HANDLING ROBOTS DURING THE PILOT PHASE. PLEASE TELL US WHETHER YOUR TEST CAN BENEFIT FROM LIQUID HANDLING AUTOMATION AND HOW YOU MIGHT USE (OR ARE ALREADY USING) THE OPENTRONS LIQUID HANDLER. *
Yes, we can benefit greatly from liquid handling automation. We plan to develop the next configuration of our assay protocol around the OpenTrons robot. There is one at our shared lab facility (MBC Biolabs in San Carlos) that we would like to gain access to in mid Sept. We have consulted with the automation expert at Denali Pharmaceuticals who planned to automate the Rabe Cepko assay, which primarily involves the silica washing steps. We have extensive experience in automating assay protocols involving silica microparticles, through FloodLAMP founder's previous startup True Materials. Affymetrix acquired True Materials in 2008, and we automated several processes for pilot production of liquid arrays using the True Materials' silica microbarcodes on a Biomek Fx, plate washers, and vacuum aspirators. The OpenTrons system is ideal for our automation development because of the low upfront cost of the system and the open source approach of the company.

PLEASE TELL US ANY REASONS THE PROFICIENCY OR CLINICAL TESTS MAY NOT ACCURATELY RECAPITULATE HOW WELL YOUR TEST WORKS. *
The buffer that the proficiency samples are in may not be compatible with our nucleic acid binding protocol. At a high level, we are not just developing a test (or assay protocol, that's already been done by Rabe and Cepko and their clinical collaborators, Anahtar et al)—we are developing an integrated screening program. That being said, many parts of the system are plug and play. For example, with a slight modification of our existing protocol (elution from the dried pellet), we can go into qPCR as well. We have done almost all of our development on real human samples, starting with raw saliva and soaked nasal swabs. We inactivate those samples with a chemical reducing agent, TCEP/EDTA per the Rabe Cepko protocol. The next step of the main assay protocol uses a high salt solution (NaI) along with the prepared silica for nucleic acid binding, and that may not work or work as well without the TCEP. For our no template controls, we use 1X PBS with the corresponding amount of the TCEP Inactivation Solution. We have not yet run our assay protocol with VTM or other sample collection buffers, as we will collect and inactivate using our protocol.

## Part 5: PRESENTATION
Our presentation
Please include a presentation deck addressing the following questions in 15 slides or less:
- Overview of technology involved in testing modality
- Overview of testing protocol
- How is your assay/protocol unique and innovative? What distinguishes you from others in the marketplace?
- What are your critical needs for deployment at scale? (Final teams will need to perform at least 500 tests per week by November 1, 2020)

Please submit a .ppt, .pptx, or PDF file.

## PART 6: OPTIONAL VIDEO
Please include a video demonstration of your technology in use. If you are entering the competition in the Open Innovation category, you must submit a video entry to qualify.

## [PART 7: TARGETS](https://docs.google.com/spreadsheets/d/1StWQ_c_YOOOeHTDvc1lLeUS85wntTLU0Y-BTQzK1u3Q/edit?usp=sharing)

*Fill in all targets used in your test, their associated gene, and the primer sequence or antibody used. The number of rows filled in will be the total number of targets your test uses where the length of unique genes listed will be the total number of unique genes targeted.*

Primer Sequences OR Antigen target/antibody
| Target Number | Target Gene   | Sequence/antibody                                   |
|---------------|---------------|-----------------------------------------------------|
| Numeric       | Text          | Text                                                |
| 1             | ORF1 As1e_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| 2             | ORF1 As1e_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG   |
| 3             | ORF1 As1_F3   | CGGTGGACAAATTGTCAC                                  |
| 4             | ORF1 As1_B3   | CTTCTCTGGATTTAACACACTT                              |
| 5             | ORF1 As1_LF   | TTACAAGCTTAAAGAATGTCTGAACACT                        |
| 6             | ORF1 As1_LB   | TTGAATTTAGGTGAAACATTTGTCACG                         |
| 7             | N N2-FIP      | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC          |
| 8             | N N2-BIP      | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA            |
| 9             | N N2-F3       | ACCAGGAACTAATCAGACAAG                               |
| 10            | N N2-B3       | GACTTGATCTTTGAAATTTGGATCT                           |
| 11            | N N2-LF       | GGGGGCAAATTGTGCAATTTG                               |
| 12            | N N2-LB       | CTTCGGGAACGTGGTTGACC                                |
| 13            | RNaseP-F3     | TTGATGAGCTGGAGCCA                                   |
| 14            | RNaseP-B3     | CACCCTCAATGCAGAGTC                                  |
| 15            | RNaseP-FIP    | GTGTGACCCTGAAGACTCGGTTTTAGCCACTGACTCGGATC           |
| 16            | RNaseP-BIP    | CCTCCGTGATATGGCTCTTCGTTTTTTTCTTACATGGCTCTGGTC       |
| 17            | RNaseP-LF     | ATGTGGATGGCTGAGTTGTT                                |
| 18            | RNaseP-LB     | CATGCTGAGTACTGGACCTC                                |
||

We are currently using the As1e and N2 combined for maximum sensitivity.

We may move to running them in 2 separate reactions to have independent results for confidence in positives.

RNAseP is standard but we plan to move to an RNA only internal control.

## [PART 8: RESULTS](https://docs.google.com/spreadsheets/d/1rl9jx4-rGzI8ukansiwJkvs-liY0aL5-85kYVGQ_p1c/edit?usp=sharing)

*Submit results on samples you have already used to derive your tests performance. The number of unique 'Sample #' which are Positive ('known value') will be used to identify how many positive samples were tested, similarly the number of unique 'Sample #' which are Negative ('known value') will be used to identify how many negative samples were tested. The known units must be total copies in reaction if a contrived 'Sample Type' was used and the total reaction volume (asked previously) will then be used to calculate the copies/uL.*

| Results                                                                                                                                                       |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Sample #                                                                                                                                                      | Known Value | Sample Type               | Sample Source | Known Value | Known Units  | Result Value | Result Units  | Result Interpretation                         | Notes                        |
| Numeric                                                                                                                                                       | Text        | Text                      | Text          | Numeric     | Text         | Numeric      | Text          | Text                                          | Text                         |
||

Blinded real saliva samples, spiked with zeptometrix inactivated virions into raw sample before any processing
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Run#39-1                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-2                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-3                                                                                                                                                      | Positive    | Real, Raw Zepto Spiked    | Saliva        | 5E+03       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-4                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-5                                                                                                                                                      | Positive    | Real, Raw Zepto Spiked    | Saliva        | 2E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-6                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-7                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-8                                                                                                                                                      | Positive    | Real, Raw Zepto Spiked    | Saliva        | 1E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-9                                                                                                                                                      | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-10                                                                                                                                                     | Negative    | Real Unspiked             | Saliva        |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-NTC                                                                                                                                                    | Negative    | Control                   | PBS           |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#39-TWC                                                                                                                                                    | Positive    | Contrived                 | Saliva        | 2,500       | copies (est) | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
||

Twist LOD run on 2ml volume of inactivated sample, Twist positive control RNA spiked after sample inactivation before purification, same results in duplicate
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Run#37-8K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 4,000       | copies (est) | Positive     | Visual binary | At or above LOD                               | As1e and N2 Primer Set Combo |
| Run#37-4K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 2,000       | copies (est) | Positive     | Visual binary | At or above LOD                               | As1e and N2 Primer Set Combo |
| Run#37-2K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 1,000       | copies (est) | Positive     | Visual binary | At or above LOD                               | As1e and N2 Primer Set Combo |
| Run#37-1K                                                                                                                                                     | Positive    | Contrived                 | Saliva        | 500         | copies (est) | Negative     | Visual binary | Below LOD                                     | As1e and N2 Primer Set Combo |
| Run#37-0                                                                                                                                                      | Negative    | Control                   | Saliva        | 0           |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#37-0                                                                                                                                                      | Positive    | Control (Internal RNAseP) | Saliva        | HIGH        |              | Positive     | Visual binary | Correct                                       | RNAseP Primers               |
| Run#37-NTC                                                                                                                                                    | Negative    | Control                   | PBS           | 0           |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#37-NTC                                                                                                                                                    | Negative    | Control (Internal RNAseP) | PBS           | 0           |              | Negative     | Visual binary | Correct                                       | RNAseP Primers               |
||

Real Sample run on individual for a screen, 2 nasal samples split and 25K zeptos spiked into 2.5ml
|                                                                                                                                                        |             |                           |               |             |              |              |               |                                               |                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------|---------------|-------------|--------------|--------------|---------------|-----------------------------------------------|------------------------------|
| Run#86-1A                                                                                                                                                     | ?           | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-1B                                                                                                                                                     | Positive    | Real, Raw Zepto Spiked    | Nasal         | 1E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#86-2A                                                                                                                                                     | Negative    | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-2B                                                                                                                                                     | Positive    | Real, Raw Zepto Spiked    | Nasal         | 1E+04       | virions/ml   | Positive     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
| Run#86-3                                                                                                                                                      | Negative    | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-4                                                                                                                                                      | Negative    | Real                      | Nasal         |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-5                                                                                                                                                      | ?           | Real                      | Saliva        |             |              | Negative     | Visual binary | No Finding of Potential Clinical Significance | As1e and N2 Primer Set Combo |
| Run#86-NTC                                                                                                                                                    | Negative    | Control                   | PBS           |             |              | Negative     | Visual binary | Correct                                       | As1e and N2 Primer Set Combo |
||

These are a few example runs, we have done over 100 runs in the last 2 months, 1000+ LAMP reactions.

Many have been characterization and troubleshooting runs, as we've moved labs 3 times.

We now have great exclusive use lab space at MBC Biolabs with:
- A dedicated room with 2 biosafety cabinets where we will run the silica purification on inactivated samples
- 4 lab benches where we'll install 2 PCR hood for setting up LAMP reactions
- 1 5' chemical fume hood for preparing stock solutions involving acids and bases (Inactivation Solution, Binding Solution and Glass Milk)

We have access to a GloMAX plate reader and ABI QuantStudio7 qPCR machine which we intend to use for comparison and characterization, and perhaps as part of our screening service offering.

We have done many successful runs spiking Zeptometrix virions into raw samples at 1e4/ml level.

The challenge is not getting good results on one run, but setting up a system to run continuously under control, especially eliminating failures due to contamination.

We've moved to single use RNA controls, and aliquoting of many components in specific volumes in preparation for pilot runs.

## [PART 9: RESULTS INTERPRETATION UPLOAD](https://docs.google.com/spreadsheets/d/1fSpC7P8ADUOevr1ufjTCEoyyYzAr-sbGyfUF4Jk17P0/edit?usp=sharing)

*Explain how your results are interpreted using your test. Based on the controls (positive and negative) and each target used in your test, what is the result interpretation (positive, negative, inconclusive, or failed) and what are the next steps for this result. Add or remove columns for targets (starting with the 5th column) as needed. The number of target columns must either be 1 or the same number of rows as in the targets sheet if result interpretation is dependent upon specific target identification. The order of target columns must be the same as the order of target rows in targets sheet.*

| Result | Next Step | Batch Control (+) | Batch Control (-) | SARS Target(s) | Human Internal Control Target |  |
| --- | --- | --- | --- | --- | --- | --- |
| Text | Text |  |  | Numeric | Numeric |
| Finding of Potential Clinical Significance | Report result | Positive | Negative | Positive | Positive |  |
| No Finding of Potential Clinical Significance | Report result | Positive | Negative | Negative | Positive |  |
| Finding of Potential Clinical Significance | Run again | Positive | Negative | Positive | Negative/Inconclusive | EUA's say to report this result as positive even if internal control is negative |
| Sample/Pool Invalid | Run again |  |  | Negative | Negative/Inconclusive |  |
| Batch Invalid | Run again | Negative/Inconclusive | Positive/Inconclusive |  |  |  |
||

For a positive pool, we will run the other aliquot of the pool as a confirmation, and run the individual samples.

## [PART 10: REAGENT OR CONSUMABLE](https://docs.google.com/spreadsheets/d/1dcW-kHoEQRo0jw6J9HFHvqcH4puT1rJqa8nMrZq5uS0/edit?usp=sharing)

*Fill in all required reagents or consumables, their supplier, catalog number, cost per sample, and cost per run. Costs must be in USD ($). If you have a custom made reagent which you will sell with your test then the cost must be the cost you will sell the reagent for. All required reagents and consumables to conduct your analysis for a single run must be listed here and exist within your protocols.io submission. The sum of the cost per run and cost per sample columns will be used for the total cost per run and cost per sample, respectively. If you have multiple variations of a protocol, then each must be uploaded as an individual document.*

Reagent List (if you have a custom reagent the cost must be what you will sell it for)
| Reagent or Consumable                                                                                                      | Supplier       | Catalog #    | Cost per item (e.g., cost of a tube of enzyme) | Amount (in relevant units, e.g., ul, ug, U, count) per item (e.g., U per tube of enzyme) | Amount per test sample | Amount per test run | Cost per Sample | Cost per Run |
|----------------------------------------------------------------------------------------------------------------------------|----------------|--------------|------------------------------------------------|------------------------------------------------------------------------------------------|------------------------|---------------------|-----------------|--------------|
| Text                                                                                                                       | Text           | Numeric      | Numeric                                        | Numeric                                                                                  | Numeric                | Numeric             | USD ($)         | USD ($)      |
| assumes we are running at the 0.5ml volume for 10 pools                                                                    |                |              |                                                |                                                                                          |                        |                     |                 |              |
|                                                                                                                            |                |              |                                                | pool level                                                                               | 10                     |                     | -               | -            |
| TCEP                                                                                                                       | Sigma          | C4706-10G    | $380                                           | 10                                                                                       | 0.00004                | 0.00036             | $0.00           | $0.01        |
| NaI                                                                                                                        | Sigma          | 217638-2.5KG | $766                                           | 2500                                                                                     | 0.0225                 | 0.225               | $0.01           | $0.07        |
| LAMP Master Mix                                                                                                            | NEB            | 1804L        | $1.83                                          | 1                                                                                        | 0.2                    | 2                   | $0.37           | $3.66        |
| Primers                                                                                                                    | IDT            | 1umole       | $446                                           | 16100                                                                                    | 0.3                    | 3                   | $0.01           | $0.08        |
| Remaining chemicals and primers are negligible cost, full recipes are listed on protocols.io and our website floodlamp.bio |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     |                 |              |
| 15ml Falcon Tube                                                                                                           | Various        |              | $0.20                                          | 1                                                                                        | 0.1                    | 1                   | $0.02           | $0.20        |
| 5ml Transport Tube                                                                                                         | Various        |              | $0.20                                          | 1                                                                                        |                        | 0                   | $0.00           | $0.00        |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     |                 |              |
| 5ml tube                                                                                                                   | CellTreat      | 229449       | $23                                            | 100                                                                                      | 0.1                    | 1                   | $0.02           | $0.23        |
| 1.5ml tube DNA Low Bind                                                                                                    | Eppendorf      |              | $39                                            | 250                                                                                      | 0.11                   | 1.1                 | $0.02           | $0.17        |
| PCR Strip Tubes                                                                                                            | USA Scientific | 1402-2500    | $81                                            | 125                                                                                      | 0.004                  | 0.044               | $0.00           | $0.03        |
| PCR Plates                                                                                                                 | Eppendorf      | EP951020303  | 130                                            | 25                                                                                       | 0.002                  | 0.022               | $0.01           | $0.12        |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
|                                                                                                                            |                |              |                                                |                                                                                          |                        |                     | -               | -            |
| Total                                                                                                                      |                |              |                                                |                                                                                          |                        |                     | $0.46           | $4.57        |
||

## [PART 11: EQUIPMENT SETUP](https://docs.google.com/spreadsheets/d/1fP7wOGZFPeDRLWws0fSSTus3jSX-az3DHAJRYN8KIGo/edit?usp=sharing)

Fill in all required equipment, their supplier, catalog number, and setup cost. Costs must be in USD ($). If you have custom made equipment which you will sell with your test then the cost must be the cost you will see the equipment for. All required equipment for a single run must be listed here and exist within your protocols.io submission. If you have multiple variations of a protocol, then each must be uploaded as an individual document.

Equipment List
| Equipment                | Supplier | Catalog #        | Setup Cost |                                             |
|--------------------------|----------|------------------|------------|---------------------------------------------|
| Text                     | Text     | Text             | USD ($)    |                                             |
| ASSAY                    |          |                  |            |                                             |
| Digital Dry Block Heater | various  |                  | $400       | Need 2 of these, 1 for drying and 1 for amp |
| 96 PCR Block             | various  |                  | $200       | Need 2 of these, 1 for drying and 1 for amp |
| Pipettes (3)             | various  |                  | $1,000     | Vary between $50-400 each                   |
| Multichalle Pipette      | various  |                  | $500       | Vary between $200-1000                      |
| Centrifuge               | various  |                  | $1,200     | Depends on throughput and scale, $300-$10K  |
| Vortexer                 | various  |                  | $130       |                                             |
|                          |          |                  |            |                                             |
| INACTIVATION             |          |                  |            |                                             |
| Digital Dry Block Heater | various  |                  | $400       |                                             |
| 16mm Hole Block          | various  |                  | $100       |                                             |
| Centrifuge               | SpinPlus | VS-TC-SPINPLUS-6 | $276       |                                             |
| Pipettes                 | various  |                  | $200       |                                             |
| Splash Guard             | various  |                  | $50        |                                             |
| Vortexer                 | various  |                  | $130       |                                             |
|                          |          |                  |            |                                             |
| ADDITIONAL               |          |                  |            |                                             |
| Biosafety Cabinet        | various  |                  | $5,000     |                                             |
| PCR Enclosure            | various  |                  | $3,000     |
||

## QS PART 12: PROTOCOLS
Protocols.io:

Teams must fill out their protocols on protocols.io. All reagents, consumables, and equipment must be listed here and in the Consumable Reagents (QS Part 10) and Equipment Setup (QS Part 11) tables. If you have multiple variations of a protocol, then each must be uploaded as an individual document. Once complete, please publish your protocol and submit the dx.doi link for your published protocol to this activity.

For protocols.io, we will set the following rules:
1. The protocol workflow must be a "Biology protocol"
2. Teams must use the "Components" to fill out their protocol including:
a. Amount
b. Concentration
c. Temperature
d. Duration
e. Equipment
f. Reagent

## QS PART 13: COMPLETION
Please use this form to indicate that you have completed all relevant portions of the Qualifying Submission, have paid the team registration fee, and have signed the competitor agreement.

## QS Part 5: PRESENTATION
Please include a presentation deck addressing the following questions in 15 slides or less:
- Overview of technology involved in testing modality
Inactivation, purific, LAMP amp

- Overview of testing protocol

- How is your assay/protocol unique and innovative? What distinguishes you from others in the marketplace?

Pooling, most community screening LAMP is direct. Others are prioritizing short sample to answer (while you wait testing) while we're prioritizing scale, screening large interacting populations every other day, with easy sample collection, in field/non-lab necessary inactivation and streamlined lab operations.

Dist - open and scale combo, focus on portability to basic labs

- What are your critical needs for deployment at scale? (Final teams will need to perform at least 500 tests per week by November 1, 2020)

Mention molecular beacons, making LAMP assay robust, instrument free readout

Please submit a .ppt, .pptx, or PDF file.

Personal Identifying Information is carefully protected by assigning non-PII unique identifiers that are utilized to track samples and pools through a custom app, with the participants selecting their method of notification. In-app notification is most secure, however, some participants may choose less secure but more convenient direct notification by text or email. Anonymized, aggregated results will also be reported to organizations and participants per specific agreements.

We have developed a custom app with a partner company, Appivo, that has a low-code app development platform. The alpha version of our app is currently under review by Apple. Through the app, participants collect individual samples and self-pooled samples, thus greatly streamlining the overall system. The collection process is initiated and supervised by a "sponsor" who is typically a member of the pool who has accepted responsibility for understanding and implementing the proper collection process. This is facilitated by in-app instruction, including video links, which take a few minutes. The app has been optimized for a smooth user experience, and for repeated screening, by pre-populating with previous collection information. Pooled collection including minors with parents/guardians is included.

The Appivo platform has built in industry-standard security. Appivo has developed apps that include health data for NGOs, and we are leveraging legal and privacy elements of those apps. The Appivo platform enables separate secure instances to be spun up, siloing separate organizations data. The Appivo platform also enables customization of the app, both the branding, design and actual functionality. With the mission to spread mass screening capability, FloodLAMP will license the app to other partner organizations, such as universities, which can customize it to suit any specific needs.

FloodLAMP's innovation is combining currently available technology into a highly efficient, integrated infectious disease screening program that can scale, and doing so in a truly open way. New technologies have enormous potential, but it's not clear if any will be ready in 2020. Both well funded startups and large diagnostics companies will surely bring online significant additional testing capacity, but most of that will on on closed systems or in closed labs, and will be at the highest price the market will bear. Some new options will have impactful tradeoffs, such as antigen tests with LOD's above the threshold for infectiousness. Incentives have not been properly set to encourage the development of a program that any basic lab can affordably bring up and run at significant scale. FloodLAMP is building upon the foundational work of others to combine a sensitive, super cheap, flexible and molecular assay with streamlined sample collection. We are openly not just our protocols but the wrap around processes for a dedicated screening program that is designed to be accessible for all other labs. At the same time we are soliciting help in best practices, under a structure where that knowledge is shared and disseminated, not just used in a limited, closed offering. In short, we're bringing open source to biotech, helping to create the Linux of infectious disease screening. We're building on the current important open efforts (such as JOGL, gLAMP, shared protocol websites) and taking them to the next level to address the COVID-19 global crisis.

Yes, we can benefit greatly from liquid handling automation. We plan to develop the next configuration of our assay protocol around the OpenTrons robot. There is one at our shared lab facility, at MBC Biolabs in San Carlos, that we would like to gain access to in mid Sept. We have consulted with the automation expert at Denali Pharmaceuticals who planned to automate the Rabe Cepko assay, which primarily involves the silica washing steps. We have extensive experience in automating assay protocols involving silica microparticles, through FloodLAMP founder's previous startup True Materials. Affymetrix acquired True Materials in 2008, and we automated several processes for pilot production of liquid arrays using the True Materials' silica microbarcodes on a Biomek Fx, plate washers, and vacuum aspirators. The OpenTrons system is ideal for our automation development because of the low upfront cost of the system and the open source approach of the company.

The buffer that the proficiency samples are in may not be compatible with our nucleic acid binding protocol. At a high level, we are not just developing a test (or assay protocol, that's already been done by Rabe and Cepko and their clinical collaborators, Anahtar et al). We are developing an integrated screening program. That being said, many parts of the system are plug and play. For example, with a slight modification of our existing protocol (elution from the dried pellet), we can go into qPCR as well. We have done almost all of our development on real human samples, starting with raw saliva and soaked nasal swabs. We inactivate those samples with a chemical reducing agent, TCEP/EDTA per the Rabe Cepko protocol. The next step of the main assay protocol uses a high salt solution (NaI) along with the prepared silica for nucleic acid binding, and that may not work or work as well without the TCEP. For our no template controls, we use 1X PBS with the corresponding amount of the TCEP Inactivation Solution. We have not yet run our assay protocol with VTM or other sample collection buffers, as we will collect and inactivate using our protocol.


# 397  XPrize Kits - FAQ BLINDED PROFICIENCY TEST KITS.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize Kits - FAQ BLINDED PROFICIENCY TEST KITS.md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - FAQ Blinded Proficiency Test Kits
category: various
subcategory: xprize
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1s2OLcJDaSRc5WsaGxCYGtSf8FTM7JOWXaskm3f1OvB0/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20Kits%20-%20FAQ%20BLINDED%20PROFICIENCY%20TEST%20KITS.docx
pdf_gdrive_url: https://drive.google.com/file/d/1gZQia4vjJcbtjWZAjcM5_y4meQUxzwCW/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20Kits%20-%20FAQ%20BLINDED%20PROFICIENCY%20TEST%20KITS.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 397
words: 293
notes:
summary_short: FAQ document for XPRIZE Rapid Covid Testing semi-finalist teams explaining the blinded proficiency test kit contents (150-200 contrived BSL-1 samples), shipping timeline (September 24 - October 2, 2020), one-week testing window, and results submission process via the Prize Operations Platform.


CONTENT

***INTERNAL TITLE:*** FAQ – BLINDED PROFICIENCY TEST KITS

**What will be contained in the blinded proficiency test kits?**

150-200 blinded samples, each containing synthetic SARS-CoV-2 RNA and inactivated viral particles. The samples will be 200-400 μl each.

There will be several base fluids used. We will not reveal the base fluids. Some of them will be VTM/UTM, while others will not.

Kits will be designed for both RNA and Antigen detection tests.

**What biosafety level is required to process the samples?**

The kits will be non-infectious BSL-1. They are all inactivated, contrived samples. No clinical samples will be included. However, please treat all samples as if they were clinical.

**When will the kits be sent?**

The blinded proficiency kits will be shipped between **September 24 – October 2, 2020**.

**How will the kits be shipped?**

The kits will be shipped frozen (on dry ice).

**Will I be notified when my kit ships?**

Yes. We will notify you when a kit has been shipped to you. They will be scheduled to arrive during a business day.

**Will I received tracking information for the shipment?**

Yes. We will send you tracking information as soon as the kit has been shipped.

**How much time do I have to validate the blinded proficiency test?**

Upon receiving a kit, each team will have **one (1) week** to complete the blinded proficiency test and upload their results to POP.

**How do I upload the results to POP?**

In the next few days, we will email you instructions for uploading your results to POP.

**Will I receive my results even if I don't make it to the next round of the competition?**

Yes. All teams will receive performance results, even if they do not make it to the next round.


# 1,001  XPrize Kits - Rapid Testing Proficiency Kit Handling Instructions.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize Kits - Rapid Testing Proficiency Kit Handling Instructions.md
file_date: **FLAGGED - UNKNOWN**
title: XPRIZE Rapid Covid Testing - Proficiency Kit Handling Instructions
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1P05UkYPfngq6hq-8zQUTO8xjbG_6cx8n/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20Kits%20-%20Rapid%20Testing%20Proficiency%20Kit%20Handling%20Instructions.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1001
words: 776
notes:
summary_short: Detailed handling instructions for the XPRIZE Rapid Testing proficiency test kits sent to semi-finalist teams, covering sample format (0.5-1 mL Matrix tubes with barcodes), storage requirements (-80°C for dry ice shipments, 4°C for cold pack shipments), result entry format, and specific guidance for both antigen (gamma-irradiated cell products) and RNA (chemically-inactivated cell products and synthetic RNA) test kits, including notes on albumin precipitation at high temperatures.


CONTENT

***INTERNAL TITLE:***  XPRIZE Rapid Testing Proficiency Kit Instructions

This shipment contains a test kit for semifinalists of the XPRIZE Rapid Testing competition. It is for research use only and has no commercial value.

The kit does not contain hazardous chemicals. No infectious agents have been added to any of the samples. Sample targets in the antigen test kit include gamma-irradiated cell line products and purified recombinant proteins. Targets in the RNA test kit include chemically-inactivated cell line products and synthetic RNA. Some samples contain human saliva or nasal swab materials purchased from a vendor. You should handle these samples under your institution's guidelines for such materials.

Samples are contained in 0.5 or 1 mL Thermo Matrix tubes. Each tube has a unique tube number and corresponding barcode. Tubes are contained in racks (boxes), each with a rack number and corresponding barcode. Each rack contains a negative control at position A1 and a positive control at position A2. Each tube has a minimum sample volume of 200 µL.

By email, you will receive a sample sheet. This sheet will list each of the samples by rack and tube number, as well as their row and column positions (e.g., A1). The sample sheet will also reveal the matrix (i.e., base fluid) for each sample. These include water, phosphate-buffered saline (PBS), saliva, and nasal swab material resuspended in PBS.

The sample sheet has three columns for entry of your results. The first column is required and is for no detection (enter 0), detection (enter 1), or test fail (enter -1). A test fail includes any issue that prevented a positive or negative detection result (e.g., inconclusive result, machine error, human error, etc.). The second and third columns are optional. Here you can enter any test-specific output and their units of measure.

You will have one week starting from your time of receipt to analyze the samples and return the sample sheet with your test results. Return the sheet to XPRIZE by uploading it to the Prize Operations Platform (POP). Here you will also identify the type of material your test is designed to detect. This will allow XPRIZE to score your performance based only on the samples that have materials your test is able to detect.

If your test does not function with a particular matrix fluid, you may dilute the sample in an appropriate buffer that is compatible with your test. You can inform us of this at rapidtesting@xprize.org.

If your test requires knowledge of prevalence (e.g., for pooling strategies), you may choose to individually analyze a portion of each sample and determine this yourself. XPRIZE will not be revealing this information.

## Antigen Test Kit
If you are testing for antigen, your kit consists of one rack shipped on dry ice. The kit ideally should be stored at -80°C until analysis. For short term storage for a week or less, -20°C is sufficient. Additional freeze-thaw cycles should be avoided. While performing your testing protocol, samples still should be kept on ice or as cold as reasonably possible until the moment of analysis.

The positive control has virus material with 10^4 RNA copies/µL. Units here are RNA copies/µL because the material was analyzed by PCR. Rest assured that antigen components are also present.

## RNA Test Kit
If you are testing for RNA, your kit consists of two racks, one shipped on dry ice and one on cold packs. The rack shipped on dry ice should be stored at -80°C until analysis. For short term storage for a week or less, -20°C is sufficient. The rack shipped on cold packs should be stored at 4°C until analysis. While performing your testing protocol, samples still should be kept on ice or as cold as reasonably possible until the moment of analysis.

The dry ice-shipped positive control has 10^4 RNA copies/µL. The cold pack-shipped positive control has 10^2 RNA copies/µL.

Several of the samples (including the positive control) that are shipped on cold packs contain albumin as an inert formulation reagent. We have observed that some precipitation (i.e., cloudiness) may occur upon heating at 95°C for 10 minutes. Incubation at 90°C for 5 minutes reduces this phenomenon and 65°C for 20 minutes reduces it even more. If your test requires heating for inactivation or other reasons, you may consider modifying your protocol if you believe the precipitation may interfere with your analysis. If you cannot modify your protocol and must have a 95°C incubation step, let us know which samples were problematic at rapidtesting@xprize.org. In our own tests, we found that this issue did not interfere with RT-qPCR methods but sometimes (but not always) affected interpretation of colorimetric LAMP methods.


# 2,278  XPrize Legal - Competitor Agreement (certificate summary).md
METADATA
last updated: 2026-02-25 BA
file_name: XPrize Legal - Competitor Agreement (certificate summary).md
file_date: 2020-09-08
title: XPRIZE Competitor Agreement - DocuSign Certificate of Completion (FloodLAMP)
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1vK_P5Fgi_P_YtnUBV4bK3i-s0Mo_INFE/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20Legal%20-%20Competitor%20Agreement%20(certificate%20summary).pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 2278
words: 1640
notes:
summary_short: DocuSign Certificate of Completion for FloodLAMP's XPRIZE Rapid Covid Testing Competitor Agreement, documenting that Randy True (randy@floodlamp.bio) signed the 34-page agreement on September 8, 2020, with the envelope sent to Lisa Covington at XPRIZE for countersignature. Includes the standard Electronic Record and Signature Disclosure.


CONTENT

## Certificate Of Completion
Envelope Id: C865A9DBB0A0488887A93BD3C49899D6
Status: Sent
Subject: Please DocuSign: XPRIZE_Covid Testing_Competitor Agreement_FINAL_2020.08.04.pdf
Source Envelope:
Document Pages: 34
Signatures: 3
Certificate Pages: 4
Initials: 6
AutoNav: Enabled
EnvelopeId Stamping: Enabled
Time Zone: (UTC-08:00) Pacific Time (US & Canada)
Envelope Originator: XPRIZE Foundation, 800 Corporate Pointe, Suite 350, Culver City, CA 90230
skipso.docusign@xprize.org
IP Address: 104.40.24.165

## Record Tracking
Status: Original
9/8/2020 3:15:23 AM
Holder: XPRIZE Foundation, skipso.docusign@xprize.org
Location: DocuSign

## Signer Events
Randy True
randy@floodlamp.bio
Security Level: .Email
ID: c8dabf14-89fb-4dac-8ed3-74b8f63233d7
9/8/2020 3:15:25 AM
Signature: DocuSigned by Randy True (8AEA81FF0C4440E...)
Signature Adoption: Pre-selected Style
Using IP Address: 73.93.172.149
Sent: 9/8/2020 3:15:24 AM
Viewed: 9/8/2020 3:15:30 AM
Signed: 9/8/2020 3:16:30 AM

## Electronic Record and Signature Disclosure:
Accepted: 9/7/2020 2:07:08 PM
ID: d237fe09-1ff3-446e-91be-014488db3be7

Lisa Covington
Lisa.Covington@xprize.org
Security Level: Email, Account Authentication (None)
Sent: 9/8/2020 3:16:31 AM

## Electronic Record and Signature Disclosure:
Not Offered via DocuSign

|  |  |  |
|---|---|---|
| In Person Signer Events | Signature | Timestamp |
| Editor Delivery Events | Status | Timestamp |
| Agent Delivery Events | Status | Timestamp |
| Intermediary Delivery Events | Status | Timestamp |
| Certified Delivery Events | Status | Timestamp |
| Carbon Copy Events | Status | Timestamp |
| Witness Events | Signature | Timestamp |
| Notary Events | Signature | Timestamp |
| Envelope Summary Events | Status | Timestamps |
| Envelope Sent | Hashed/Encrypted | 9/8/2020 3:16:31 AM |
| Payment Events | Status | Timestamps |
| Electronic Record and Signature Disclosure | | |
||

## ELECTRONIC RECORD AND SIGNATURE DISCLOSURE
From time to time, X PRIZE Foundation - Envelope (we, us or Company) may be required by law to provide to you certain written notices or disclosures. Described below are the terms and conditions for providing to you such notices and disclosures electronically through your DocuSign, Inc. (DocuSign) Express user account. Please read the information below carefully and thoroughly, and if you can access this information electronically to your satisfaction and agree to these terms and conditions, please confirm your agreement by clicking the 'I agree' button at the bottom of this document.

### Getting paper copies
At any time, you may request from us a paper copy of any record provided or made available electronically to you by us. For such copies, as long as you are an authorized user of the DocuSign system you will have the ability to download and print any documents we send to you through your DocuSign user account for a limited period of time (usually 30 days) after such documents are first sent to you. After such time, if you wish for us to send you paper copies of any such documents from our office to you, you will be charged a $0.00 per-page fee. You may request delivery of such paper copies from us by following the procedure described below.

### Withdrawing your consent
If you decide to receive notices and disclosures from us electronically, you may at any time change your mind and tell us that thereafter you want to receive required notices and disclosures only in paper format. How you must inform us of your decision to receive future notices and disclosure in paper format and withdraw your consent to receive notices and disclosures electronically is described below.

### Consequences of changing your mind
If you elect to receive required notices and disclosures only in paper format, it will slow the speed at which we can complete certain steps in transactions with you and delivering services to you because we will need first to send the required notices or disclosures to you in paper format, and then wait until we receive back from you your acknowledgment of your receipt of such paper notices or disclosures. To indicate to us that you are changing your mind, you must withdraw your consent using the DocuSign 'Withdraw Consent' form on the signing page of your DocuSign account. This will indicate to us that you have withdrawn your consent to receive required notices and disclosures electronically from us and you will no longer be able to use your DocuSign Express user account to receive required notices and consents electronically from us or to sign electronically documents from us.

### All notices and disclosures will be sent to you electronically
Unless you tell us otherwise in accordance with the procedures described herein, we will provide electronically to you through your DocuSign user account all required notices, disclosures, authorizations, acknowledgements, and other documents that are required to be provided or made available to you during the course of our relationship with you. To reduce the chance of you inadvertently not receiving any notice or disclosure, we prefer to provide all of the required notices and disclosures to you by the same method and to the same address that you have given us. Thus, you can receive all the disclosures and notices electronically or in paper format through the paper mail delivery system. If you do not agree with this process, please let us know as described below. Please also see the paragraph immediately above that describes the consequences of your electing not to receive delivery of the notices and disclosures electronically from us.

Electronic Record and Signature Disclosure created on: 7/13/2015 11:37:56 AM
Parties agreed to: Randy True

### How to contact X PRIZE Foundation - Envelope
You may contact us to let us know of your changes as to how we may contact you electronically, to request paper copies of certain information from us, and to withdraw your prior consent to receive notices and disclosures electronically as follows:

To contact us by email send messages to: ap@xprize.org

### To advise X PRIZE Foundation - Envelope of your new e-mail address
To let us know of a change in your e-mail address where we should send notices and disclosures electronically to you, you must send an email message to us at ap@xprize.org and in the body of such request you must state: your previous e-mail address, your new e-mail address. We do not require any other information from you to change your email address.

In addition, you must notify DocuSign, Inc to arrange for your new email address to be reflected in your DocuSign account by following the process for changing e-mail in DocuSign.

### To request paper copies from X PRIZE Foundation - Envelope
To request delivery from us of paper copies of the notices and disclosures previously provided by us to you electronically, you must send us an e-mail to ap@xprize.org and in the body of such request you must state your e-mail address, full name, US Postal address, and telephone number. We will bill you for any fees at that time, if any.

### To withdraw your consent with X PRIZE Foundation - Envelope
To inform us that you no longer want to receive future notices and disclosures in electronic format you may:

i. decline to sign a document from within your DocuSign account, and on the subsequent page, select the check-box indicating you wish to withdraw your consent, or you may;
ii. send us an e-mail to ap@xprize.org and in the body of such request you must state your e-mail, full name, US Postal Address, telephone number, and account number. We do not need any other information from you to withdraw consent. The consequences of your withdrawing consent for online documents will be that transactions may take a longer time to process.

### Required hardware and software
|  |  |
| --- | --- |
| Operating Systems | Windows 2000 or Windows XP |
| Browsers (for SENDERS) | Internet Explorer 6.0 or above |
| Browsers (for SIGNERS) | Internet Explorer 6.0, Mozilla FireFox 1.0, NetScape 7.2 (or above) |
| Email | Access to a valid email account |
| Screen Resolution | 800 x 600 minimum |
| Enabled Security Settings | Allow per session cookies; Users accessing the internet behind a Proxy Server must enable HTTP 1.1 settings via proxy connection |
||

** These minimum requirements are subject to change. If these requirements change, we will provide you with an email message at the email address we have on file for you at that time providing you with the revised hardware and software requirements, at which time you will have the right to withdraw your consent.

### Acknowledging your access and consent to receive materials electronically
To confirm to us that you can access this information electronically, which will be similar to other electronic notices and disclosures that we will provide to you, please verify that you were able to read this electronic disclosure and that you also were able to print on paper or electronically save this page for your future reference and access or that you were able to e-mail this disclosure and consent to an address where you will be able to print on paper or save it for your future reference and access. Further, if you consent to receiving notices and disclosures exclusively in electronic format on the terms and conditions described above, please let us know by clicking the 'I agree' button below.

By checking the 'I Agree' box, I confirm that:

- I can access and read this Electronic CONSENT TO ELECTRONIC RECEIPT OF ELECTRONIC RECORD AND SIGNATURE DISCLOSURES document; and
- I can print on paper the disclosure or save or send the disclosure to a place where I can print it, for future reference and access; and
- Until or unless I notify X PRIZE Foundation - Envelope as described above, I consent to receive from exclusively through electronic means all notices, disclosures, authorizations, acknowledgements, and other documents that are required to be provided or made available to me by X PRIZE Foundation - Envelope during the course of my relationship with you.


# 19,298  XPrize Legal - Competitor Agreement_FINAL_2020.08.04.md
METADATA
last updated: 2026-02-24 BA
file_name: XPrize Legal - Competitor Agreement_FINAL_2020.08.04.md
file_date: 2020-08-04
title: XPRIZE Rapid Covid Testing - Competitor Agreement (Final, August 4, 2020)
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1wKZGHnesUQ4tVi5bfaZ-AxN0VZhsVua7/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20Legal%20-%20Competitor%20Agreement_FINAL_2020.08.04.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 19298
words: 14396
notes: 
summary_short: The full XPRIZE Rapid Covid Testing Competitor Agreement (dated August 4, 2020) is a comprehensive legal document governing team participation in the $5M competition, covering eligibility requirements, registration, competition judging, intellectual property rights, confidentiality obligations, dispute resolution, team management, and five exhibits (Competition Guidelines, Media Rights Agreement, Insurance Requirements, Team Release and Waiver, and Team Member Release, Waiver and Confidentiality Agreement). FloodLAMP's copy was signed by Randy True (CEO) on September 8, 2020.


CONTENT

***INTERNAL TITLE:*** XPRIZE COMPETITOR AGREEMENT
## 1. PARTIES
### 1.1 XPRIZE Foundation, Inc., a Delaware corporation and 501(c)(3) non-profit foundation ("XPRIZE")

|  |  |
| --- | --- |
| XPRIZE Address | 800 Corporate Pointe, Suite 350, Culver City, California USA 90230 |
| XPRIZE Telephone | 310.741.4880 |
| XPRIZE Email | legal@xprize.org |
| XPRIZE Website | www.xprize.org |
| XPRIZE Signatory<br>Signature and Date: ||
| XPRIZE Signatory<br>Name: ||
|XPRIZE Title: | Prize Lead |
||

### 1.2 [TEAM NAME], a(n) [JURISDICTION] [TYPE OF ENTITY] ("Team")<br> FloodLAMP

|  |  |
| --- | --- |
| Team Address | 930 Brittan Ave<br>(Please include City, State, Zip Code, and Country) |
| Team Telephone | [NUMBER] 415-269-2974 |
| Team Email | [ADDRESS] randy@floodlamp.bio |
| Team Website | [ADDRESS] floodlamp.bio |
| Team Signatory<br>Signature and Date: | DocuSigned by Randy True (8AEA81FF0C4440E...) 9/8/2020 |
| Team Signatory Name: | Randy True |
| Team Signatory Title: | CEO |

### 1.3 Parties to this Agreement

XPRIZE and Team are each, individually, a "Party" and jointly the "Parties" to this Agreement.

## 2. SCOPE OF AGREEMENT
### 2.1 Legal Notice

THIS COMPETITOR AGREEMENT, INCLUDING ANY AND ALL EXHIBITS ("Agreement"), SHALL GOVERN THE XPRIZE Rapid COVID Testing ("Competition") AND WILL SUPERSEDE ANY OTHER AGREEMENT BETWEEN THE PARTIES RELATED TO THE COMPETITION.

### 2.2 Binding Agreement

THE PARTIES, BY VOLUNTARILY ENTERING INTO THIS AGREEMENT, HEREBY AGREE TO BE BOUND BY AND COMPLY WITH THE TERMS AND CONDITIONS OF THIS AGREEMENT. IF TEAM, OR ANY TEAM MEMBER ("Team Member" or "Member"), DOES NOT AGREE TO BE BOUND BY AND COMPLY WITH THIS AGREEMENT, THEN TEAM AND/OR TEAM MEMBER(S) SHOULD NOT ENTER THE COMPETITION OR JOIN THE TEAM. BY SIGNING THIS AGREEMENT, TEAM REPRESENTS AND WARRANTS THAT IT AND ITS PRESENT AND FUTURE TEAM MEMBERS UNDERSTAND AND AGREE TO BE BOUND BY THE TERMS OF THIS AGREEMENT.

### 2.3 Purpose

The $5 Million Dollar XPRIZE Rapid COVID Testing is a seven (7) month global competition to incentivize and accelerate the development of high-quality, affordable COVID-19 testing that can be effectively scaled around the world. The winning team will Develop COVID-19 tests that are radically affordable compared to what is currently available on the market, that are equal to, or better than, commercial offerings at measuring sensitivity, specificity, and limit of detection (LoD), With a maximum turnaround time of 12 hours from sample to result. A successful solution to this challenge will develop novel technologies to accelerate the development of high-quality COVID-19 testing that is fast, frequent, affordable, and easy.

### 2.4 Competition Guidelines

The Parties recognize and acknowledge that the structure, judging criteria, and procedures of the various rounds of the Competition, and details concerning the testing protocols, rules and regulations that will govern the Competition will still be subject to certain changes pursuant to Section 17.1 below.

### 2.5 Limitation on the Team's rights

This Agreement contains important limitations on the Team's rights that are necessary in light of XPRIZE's mission and dedication to the development of technology for the good of society. In light of these limitations, Team is encouraged to consult with legal counsel and ask any questions about its decision to enter into this Agreement and agree to these limitations. By entering into this Agreement, Team represents and warrants that it has had such opportunity to consult with counsel and ask questions about this Agreement.

### 2.6 Prior Status of Team

Prior to entering this Agreement, Team must have been an official registered Team in the Qualifying Round of the Competition and submitted their technical documentation describing their current technology assets, their approach to the Competition, a plan for technology development and integration during the Competition, and their plans for further development after the Competition.

## 3. ELIGIBILITY AND REGISTRATION
### 3.1 Eligible Entity

In order to compete in the Competition and/or receive: (i) any portion of any prize purse; (ii) any other monetary payment; or (iii) any nonmonetary consideration (collectively, "Award") under this Agreement, Team must be either a single individual or organized under a single legal entity. Team must be an "Eligible Entity," defined for the purposes of this Agreement as an entity that is:

3.1.1 A single individual (provided that such individual is the only member of the Team);

3.1.2 A valid existing legal entity (e.g., corporation, LLC, Sole proprietorship, nonprofit etc.) that is duly organized and in good standing in the jurisdiction of its organization;

3.1.3 Organized in a jurisdiction where participation in the Competition is not prohibited;

3.1.4 Organized and operated in such a way that payments in U.S. Dollars may be legally deposited from the United States into a Team bank account. XPRIZE encourages participation by individuals and teams from around the world without regard to race, nationality, politics or ideology. However, United States law prohibits the exchange of services with, or payment of money to, individuals and entities in certain countries. To be eligible, a team must not include any individual or entity organized or with primary residence in Cuba, Iran, North Korea, Sudan, Syria, or where otherwise prohibited by law (See https://www.treasury.gov/resource-center/sanctions/programs/pages/programs.aspx);

3.1.5 Must not be linked, directly or indirectly, to organizations or individuals associated with terrorism;

3.1.6 Must not, and must ensure, that its employees, agents, or representatives do not engage in any dishonesty in obtaining a benefit, or causing a loss, by deception or other means, and includes incidents of attempted, alleged, suspected, or detected fraud ("Fraudulent Activity").

3.1.7 Active in the Competition, meaning that it must not have withdrawn, been terminated, or been disqualified from the Competition; and

3.1.8 In full compliance with the terms and conditions of this Agreement.

3.1.9 If at any time during the Competition, a Team's legal status or make-up changes, Team must provide written notice to XPRIZE within ten (10) business days of change. Failure to notify XPRIZE of changes to a Team's legal status or make-up may result in loss of eligibility.

3.1.10 If Team is not an Eligible Entity at any time, XPRIZE will have the right to reject Team's "Registration" (as defined in Section Error! Reference source not found.) or disqualify Team under Section 3.5 below if it is already registered, and Team will have no right or opportunity to cure.

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE SECTION 3.5 BELOW
TEAM: RT
XPRIZE:

### 3.2 Conflicts of Interest

XPRIZE employees and their immediate families may neither participate in, nor have any financial or other material interest in any Team. XPRIZE and Team acknowledge that certain members of the XPRIZE Board of Trustees (who are not employees of XPRIZE) may promote, fund, or be otherwise involved with one or more Team(s). Such individuals shall have neither input into XPRIZE's decisions with respect to the Competition, nor access to non-public information about the Competition.

Each XPRIZE officer, employee, director, trustee or agent who may have any influence over the acceptance of any Team into the Competition and/or the administration and/or judging of the Competition, including without limitation "Advisors" as defined in Section 5.2 below and "Judges" as defined in Section 5.3 below, and will disclose to XPRIZE any significant past, present, or expected or resulting future relationship with any Team in the Competition. In the event that any relationship results in a conflict of interest, as determined by XPRIZE, in its sole and absolute discretion, the conflicted individual will be denied access to any Team's confidential information and will be recused from any decision(s) concerning the acceptance of any Team into the Competition and the administration and judging of the Competition.

### 3.3 Compliance with Applicable Laws

Generally, where applicable, XPRIZE shall apply for and secure permits from appropriate government agencies, authorities or other regulatory bodies. In particular, where Team specific permits are required, Team is obligated to comply with all applicable laws and acquire all necessary licenses, waivers, and/or permits from the applicable regulatory bodies or other applicable third parties. XPRIZE is not required to advise Team regarding such legal and regulatory compliance.

### 3.4 Team Acquisition or Merger

Subject to Section 6.7 below and the express written approval of XPRIZE, Team may acquire or merge with another Team or acquire another Team's assets at any time during the Competition. Each Team must provide XPRIZE with ten (10) days' prior written notice of any such acquisition or merger.

### 3.5 Disqualification of Team

At any time during the Competition, at the sole and absolute discretion of XPRIZE, XPRIZE shall be entitled to disqualify Team, in whole or in part, upon service of written notice to Team, if:

3.5.1 Team breaches any term of this Agreement;

3.5.2 Team or Team Members become embroiled in internal conflicts or disputes;

3.5.3 A dispute arises concerning the acquisition, combination, collaboration or sharing of technical assets between Teams;

3.5.4 Team or Team Member engages in conduct that is determined by XPRIZE, in its sole discretion: (i) to be immoral, offensive or inappropriate; (ii) to reflect poorly on XPRIZE and/or any Sponsor and other Sponsors of the Competition ("Competition Sponsor"); (iii) to be unsportsmanlike conduct (iv) to be disparaging to XPRIZE or any XPRIZE employee, director, sponsor or agent, or to Sponsor or any Sponsor employee, director, sponsor or agent; or (v) to disrupt or harm, in any manner, the Competition, XPRIZE, Sponsor or any other Competition sponsor;

3.5.5 Team is not an Eligible Entity as defined in Section 3.1 above; and/or

3.5.6 Team fails to actively and productively participate in the Competition.

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE SECTION 3.5 ABOVE
TEAM: RT
XPRIZE:

### 3.6 Return and Reallocation of Awards

If Team is disqualified pursuant to Section 3.5 above after Team has received any Award and the basis of such disqualification is conduct occurring prior to Team receiving the Award that is discovered after Team received the Award, then Team shall return such Award to XPRIZE within five (5) days of request by XPRIZE and XPRIZE shall have sole and absolute discretion to reallocate such Award.

### 3.7 Withdrawal from the Competition

Team may withdraw from the Competition at any time. Team must provide written notice of withdrawal to XPRIZE ten (10) business days prior to its withdrawal. Upon withdrawal, Team will: (i) forfeit Team's Registration Fee; (ii) no longer be eligible to receive any Award; (iii) or return milestone awards that need to be used as a finalist if withdrawing before the final pilot test; (iv) cease use of all XPRIZE materials; and (v) return (or destroy if so instructed in writing by XPRIZE) all media, documents, information, and/or materials provided to Team by XPRIZE or its affiliates or sponsors. Team shall certify in writing that it has complied with this provision within ten (10) business days of Team's withdrawal. Once a Team has withdrawn or is otherwise disqualified from the Competition, Team or Team Members shall not engage in conduct that is determined by XPRIZE: (i) to reflect poorly on XPRIZE and/or any Sponsor and other Competition sponsor; (ii) to be disparaging to XPRIZE or any XPRIZE employee, director, sponsor or agent, or to Sponsor or any Sponsor employee, director, sponsor or agent; or (iii) to disrupt or harm, in any manner, the Competition, XPRIZE, Sponsor or any other Competition sponsor.

## 4. REGISTRATION
### 4.1 Registration Process

To be fully registered to participate in the Main Competition:

4.1.1 Team must have taken part in the qualification round of the Competition by developing a detailed, complete Qualifying Submission;

4.1.2 Team must be qualified by the Competition judging panel based on the merit of the Team Qualifying Submissions;

4.1.3 Team must have an existing account on the Competition Portal;

4.1.4 Team must provide updated information as requested by XPRIZE throughout the competition.

4.1.5 Team must sign this Competitor Agreement, with all Exhibits and Waivers attached hereto, and return a copy of the signed document to XPRIZE as instructed in the Competition Portal;

4.1.6 Team must meet the insurance requirements detailed in Exhibit C of this Agreement; and

4.1.7 XPRIZE must approve Team's Registration, at XPRIZE's sole and absolute discretion.

### 4.2 Registration Fee

Team's Registration Fee, (if applicable), is non-refundable and non-transferable.

### 4.3 Method of Payment

Registration Fee amounts and all references to currency in this Agreement and related documents will be in United States Dollars and shall be paid in accordance with the payment instructions set forth on the Competition Portal.

### 4.4 Registration of Multiple Entries

Team will be allowed to register more than one Entry in the Competition; provided, however, that each Entry registered by Team shall be substantially different than the other Entry or Entries also registered by Team. All Entries by Team will be governed by this Competitor Agreement, but a separate Registration Fee will be required for each Entry. The Registration Fee for each Entry will be determined pursuant to Section 4.2 above according to the date that such Entry is registered and the applicable Registration Fee is paid. If interested, Team should contact XPRIZE for details on how to register one or more additional Entries.

Each Entry must be approved by XPRIZE, at its sole and absolute discretion, prior to being included in the Competition. Team must describe each Entry in sufficient detail to allow XPRIZE to determine whether or not the Entry being registered is substantially different than previous Entries registered by Team. The Team Leader identified on the Competition Portal will receive an email from XPRIZE informing Team whether or not its Registration of each additional Entry has been approved.

Each Entry must be registered, and the Registration Fee must be paid by or prior to the Registration Deadline. No additional Entry Registrations will be accepted or approved after the Registration Deadline.

### 4.5 Compliance Certification

Within thirty (30) days following the announcement of selection of Semifinalist Teams, as set forth in the Competition Guidelines, attached hereto as Exhibit A, all Semifinalist Teams will be required to submit a fully-executed "Compliance Certification Form" in which Team will be required to certify that it is in full compliance with: (i) Sections 3.1, 3.3, and 3.3 above; (ii) Section 11.1 below; and (iii) the Insurance Requirements detailed in Exhibit C to this Agreement, (iv) and has been in compliance through the term listed in Section 4.1.5 (above) as evidenced by the signature of the Team Leader (and in the case of the Insurance Requirements, Teams insurance representative). The deadline for submission of the Compliance Certification Form shall be set forth in the Competition Guidelines, attached hereto as Exhibit A.

In addition to the Registration requirements specified in Section 4.1 above, XPRIZE shall also have the right, at its sole and absolute discretion, to demand that Team submit current proof of legal status, certificate of good standing from the country or state in which the legal entity is registered, and Insurance coverage, at any time during the Term described in Section 6.1 below, within ten (10) business days of the delivery of a written demand from XPRIZE to Team.

## 5. COMPETITION JUDGING - ADVISORS AND JUDGES
### 5.1 Implementation

To Implement the XPRIZE Rapid COVID Testing and support the validity and integrity of the prize process, XPRIZE will convene an Advisory Board, and a Judging Panel.

### 5.2 Independent Advisors and Judges

XPRIZE will form panels of relevant experts ("Advisors") to serve on Advisory Boards and Judging Panels for the Competition. These panels will remain in place throughout the Competition to advise XPRIZE regarding all aspects of the design and implementation of the Competition. Each Advisor will enter into an Agreement with XPRIZE that will: (i) outline Advisor's duties and obligations; (ii) require Advisor to maintain confidentiality of XPRIZE's and Teams' Confidential Information, in accordance with Section 11 of this Agreement; and (iii) require Advisor to acknowledge that he or she shall make no claim to any Team's Intellectual Property.

These panels will be independent of XPRIZE, the Sponsor and all Teams and Team Members. No Advisor, nor any member of Advisor's immediate family, shall participate, nor have any financial or other material interest, in any Team or Team Member. All Advisors shall promptly disclose to XPRIZE any such current or former, or expected future conflict of interest with XPRIZE, the Sponsor or any other Competition sponsor, and/or any Team or Team Member pursuant to Section 3.2 above.

### 5.3 Independent Judges

XPRIZE shall select, at its sole and absolute discretion, a panel of independent subject matter experts (each, individually, a "Judge" and collectively, the "Judging Panel") to judge the Competition. XPRIZE shall enter into an agreement with each Judge obligating the Judge to comply with the terms and conditions of this Agreement, including the Confidentiality provisions in Section 11 below and an acknowledgement that he or shall make no claim to Team's Intellectual Property (as defined in Section 9.1 below).

The Judging Panel will be independent of XPRIZE, Sponsor, and all Teams and Team Members. No Judge, nor any member of Judge's immediate family, shall participate, nor have any financial or other material interest, in any Team or Team Member. All Judges shall promptly disclose to XPRIZE any such current or former, or expected future conflict of interest with XPRIZE or any Team or Team Member.

### 5.4 Judging Panel has Sole Authority to Judge the Competition

Consistent with this Agreement and Guidelines of the Competition, the Judging Panel shall have sole authority to judge the Competition. XPRIZE shall retain authority to make decision on issues expressly left for XPRIZE's discretion in this Agreement. Unless expressly provided otherwise in this Agreement, all determinations, exercises of discretion, decisions and the like made by XPRIZE or the Judging Panel may be made by XPRIZE's and Judging Panel's respective sole discretion, including, without limitation, the awarding of Prizes. All judging decisions and opinions made by the Judging Panel are binding on both Team and XPRIZE, and not subject to review or contest. The Judging Panel retains ultimate discretion to declare a winner of the Competition and otherwise award all Prizes subject to Section 5.6 below. Any such judging decision may not be challenged by Team and Team agrees to abide and refrain from challenging such decision. Notwithstanding the above, XPRIZE retains sole authority to determine the prize purse structure.

### 5.5 Technical Decisions of the Judging Panel are Final

Subject to the express terms of this Agreement, the Judging Panel shall have sole and absolute discretion: (i) to allocate duties among the Judges; (ii) to determine the degree of accuracy and error rate that is acceptable to the Judging Panel for all Competition calculations, measurements, and results, where not specified in the Guidelines; and (iii) to determine the methodology used by the Judging Panel to render its decisions. The technical decisions of the Judging Panel shall be binding on XPRIZE, Team and each Team Member. XPRIZE and Team agree to not dispute any technical decision or ruling of the Judging Panel, including decisions regarding the degree of accuracy or error rate of any Competition calculations, measurements, or results. Team shall have no right to observe other Teams' testing or evaluation, or to be informed of such calculations, measurements or results, unless the information is made publicly available by XPRIZE.

### 5.6 Key Responsibilities of the Judging Panel

The key responsibilities of the Judging Panel include, but are not limited to: (i) working with XPRIZE to interpret the Competition Guidelines and apply such Guidelines to the facts and circumstances of each Team's participation in the Competition; (ii) reviewing Team's final prototype; (iii) usability test; (iv) evaluating additional technical information obtained from the Team; and (v) making Prize award determinations.

### 5.7 Non-Disclosure

The members of the Judging Panel shall be required to sign non-disclosure agreements that they agree to engage in no communication likely to have a material impact on the Competition with any Team or any representative of a Team other than (i) through official channels of communication established by XPRIZE; or (ii) communications within the scope of the Judge's services as a member of the Judging Panel. Judges are also required to notify XPRIZE if any Team or representative of any Team approaches or otherwise communicates with a member of the Judging Panel with regard to any unethical proposition or suggestion that would result in a conflict of interest, as described in Section 5.8 below.

### 5.8 Conflict of Interest

All members of the Judging Panel will be required to disclose any significant current, former, or expected future relationships with any team. To prevent conflicts of interest, or the appearance of said conflicts, Teams may request that a Judging Panel sub-committee be formed to judge the specific issue that is deemed by XPRIZE in its sole and absolute discretion as a perceived or actual conflict of interest. XPRIZE will consider such requests in good faith but has no obligation to grant them. The composition of the Judging Panel sub-committee will not be available to Teams and any request for information will come directly from the managing Judge assigned to Team.

### 5.9 Requirements

The provisions of this Agreement are requirements and Team must fully comply with them to be eligible to win any of the Prizes. XPRIZE may, however, decide in its sole discretion to remove or erase such requirements, provided that it does so for all Teams simultaneously. Notwithstanding the preceding sentences, if no Team in the Competition fulfills all such requirements, but the Judging Panel determines, in its sole discretion, that a Team or Teams has or have substantially fulfilled such requirements, it may award Prize(s) to one or more such Teams in its sole discretion.

### 5.10 Ex-Parte Communications

Teams (including all Teams Members and their representatives) shall not engage in any communications with any member of the Judging Panel about the Competition outside of communication channels and events officially facilitated by XPRIZE.

## 6. TERM, TERMINATION, AMENDMENT AND ASSIGNMENT
### 6.1 Term of Agreement

The "Term" of this Agreement will begin on the date of the last signature on this Agreement ("Effective Date") and will end upon the conclusion of the final Competition Awards Ceremony as defined in the Competition Guidelines, unless extended or terminated earlier by XPRIZE.

### 6.2 Termination of this Agreement by Disqualification of Team

If Team is disqualified pursuant to Section 3.5 above, this Agreement shall be terminated between XPRIZE and Team effective immediately upon the effective date of such disqualification; provided, however, that those Sections and Exhibits specified in Section 17.1 below shall survive such termination.

### 6.3 Cancellation of the Competition

XPRIZE may, in its sole and absolute discretion, cancel the Competition at any time and immediately terminate this Agreement without cause.

### 6.4 Team Notice and Comment prior to Cancellation

XPRIZE will notify Team of any potential cancellation pursuant to Section 6.3 above and will post a public notice of the same on the XPRIZE website, thirty (30) calendar days prior to the cancellation of the Competition.

### 6.5 Effect of Cancellation

If XPRIZE cancels the Competition pursuant to Section 6.3 above, XPRIZE may, in its sole discretion, return all, or a portion of Team's registration fee, but Team will be ineligible to win or receive any Award(s).

### 6.6 Amendment by Mutual Consent

This Agreement may be supplemented, amended or otherwise modified only by the prior written consent of the Parties. Notwithstanding the foregoing, XPRIZE has the right, upon ten (10) business days' written notice, to amend in good faith any and all Exhibits to this Agreement, and the Parties agree that any such amendment made solely by XPRIZE shall be binding on all Parties hereto.

### 6.7 No Assignment by Team

Registration in the Competition is non-transferable. Team shall not assign, delegate or otherwise transfer such Registration or any of Team's rights, interests, duties and/or responsibilities under this Agreement without prior signed, written approval from XPRIZE. Any attempted assignment, delegation or transfer in violation of this Section 6.7 shall be void.

### 6.8 Assignment by XPRIZE

XPRIZE may assign, delegate or transfer any of its rights or interests or duties under this Agreement at its sole and absolute discretion.

## 7. PRIZE PURSES
### 7.1 Total Prize Purse

The total "Prize Purse" for the competition is defined in the Competition Guidelines.

### 7.2 Competition Guidelines

The Competition will be administered and judged and the Prize Purse(s) will be managed and awarded as set forth in the Competition Guidelines, attached as Exhibit A to this Agreement and incorporated into this Agreement pursuant to Section 17 below.

### 7.3 Determinations

All determinations with respect to the satisfaction of Competition Guidelines (Exhibit A) will be made by the Judging Panel subject to Section 5.6 above.

### 7.4 Allocation of Prizes

Any Award allocated to Team will be delivered in its entirety to Team, and only to Team, with applicable fees deducted per Section 7.6 below. Team shall be solely responsible for allocation of the Award funds among Team Members and for any payments to be made to third parties.

### 7.5 Awards Subject to Applicable Law

All Awards shall be made in accordance with United States law and other applicable laws that: (i) may restrict or prohibit payment to Teams organized or domiciled in countries that are subject to United States sanctions; and (ii) may subject Team to United States tax liabilities, even if Team is organized or domiciled outside the United States of America.

### 7.6 Team is responsible for all fees incurred in processing of Prize payment and allocation

Any and all fees and taxes incurred in the processing, transfer, allocation, currency exchange, or delivery of payment of an Award to a Team will be the responsibility of the Team. Should XPRIZE be required to make such payments in order to complete delivery of an Award payment, said payments will be deducted from the Prize Purse.

### 7.7 Prize Purse Conditions

If Sponsor or another major sponsor of the Competition refuses or fails to timely pay XPRIZE the funds that will be used for all or any Award, XPRIZE will not be liable to deliver such Award (or any unpaid portion(s) thereof or to otherwise compensate Team or any Team Member. XPRIZE reserves the right to increase and/or adjust the Prize Purse and/or offer additional Awards at its sole and absolute discretion, but XPRIZE shall have no obligation to do so.

### 7.8 Payments to Team

Team shall only be paid upon winning of an Award and shall not receive payment for preparation or participation in the Competition. XPRIZE reserves the right to withhold or recover any milestone prize payments if Team intends to withdraw or fails to participate throughout the complete duration of the competition. Team and Team Members are solely responsible for all of their own costs. XPRIZE shall make any necessary payment to the bank account specified by Team during Registration. Team bank account information may be updated by written notice to XPRIZE, as per the terms of this Agreement, at least thirty calendar (30) days prior to any expected payment. Compliance with payment instructions provided by Team shall constitute payment of the applicable Award. Team shall be solely responsible for any taxes arising from or relating to the payment of any Award. XPRIZE is not responsible for any division or distribution of any of the Prizes awarded in the Competition among or between Team Members. Instead, distribution or division of any Prize among individual Team Members is the sole responsibility of the participating Team.

## 8. COMPETITION GUIDELINES
### 8.1 Competition Guidelines govern Competition

The Competition will be administered and judged and the Prize Purse(s) will be managed and awarded as set forth in the Competition Guidelines, available through the XPRIZE website and referenced here as Exhibit A and incorporated into this Agreement pursuant to Section 17 below.

### 8.2 Update and Revisions to the Competition Guidelines

Pursuant to Section 6.6 above, the Competition Guidelines may be expanded and updated subject to XPRIZE's sole and absolute discretion at any time during the Term of this Agreement.

## 9. INTELLECTUAL PROPERTY
### 9.1 Definition of "Team Technology"

Inventorship of patentable developments or discoveries conceived and reduced to practice in connection with Team's participation in the Competition during the period of Teams active participation in the Competition ("Team Inventions") will be determined in accordance with U.S. Patent Law. Authorship of copyrighted works, including computer software, created or fixed in a tangible medium of expression by Team or Team Member in connection with Team's participation in the Competition during the period of Teams active participation the Competition ("Team Copyrighted Works") will be determined in accordance with U.S. Copyright Law. "Team Technology" shall include both Team Inventions and Team Copyrighted Works.

### 9.2 Team Will Retain Ownership of Team's Intellectual Property

Team will retain all right, title and other ownership interests in Team Inventions and Team Copyrighted Works. Team will also retain all right, title and other ownership interests in Team's submission and in all inventions, patents, patent applications, designs, copyrights, trademarks, trade secrets, software, source code, object code, processes, formulae, ideas, methods, know-how, techniques, devices, creative works, works of authorship, publications, and/or other intellectual property not included in the definition of Team Technology ("Intellectual Property") developed by Team during the Competition; subject to Section 10.1 below and the media rights granted by Team to XPRIZE pursuant to the Media Rights Agreement, attached as Exhibit B to this Agreement and incorporated into this Agreement pursuant to Section 17 below.

## 10. DATA AND TRADEMARKS
### 10.1 Validation Data

Measurement, scoring, statistical and other data ("Data") collected by XPRIZE during the operation of the Competition is the intellectual property of XPRIZE. XPRIZE retains the right to license such data for academic, research and other purposes.

## 11. CONFIDENTIALITY
### 11.1 "Confidential Information" Defined

"Confidential Information" means all information regarding the business, affairs and technology of XPRIZE, its affiliates, a sponsor or any team participating in the Competition, including, without limitation, business concepts, processes, methods, systems, know-how, devices, formulas, marketing methods, prices, customer information, customer lists, methods of operation, trade secrets, or other information, whether in oral, written, or electronic form, regardless of who discloses the information. Confidential Information also includes inventions, designs, drawings, standards, specifications, modifications, technical information, prototypes, test versions, and models associated with the inventions or solutions conceived or developed by teams. For clarity, Competition results until publicly announced by XPRIZE are the Confidential Information of XPRIZE.

### 11.2 Exclusions from "Confidential Information"

The following information will NOT be considered Confidential Information: (i) information that is publicly available through no fault of the party that was obligated to keep it confidential; (ii) information that was known by a party prior to commencement of discussions regarding the subject matter of this Agreement; (iii) information that was independently developed by a party without reference to the Confidential Information of the other party; and (iv) information rightfully disclosed to a party by a third party without continuing restrictions on its use or disclosure.

### 11.3 Obligation of Confidentiality

Each Party will: (i) hold the other Party's Confidential Information in confidence (using at least the same measures as it does to protect its own Confidential Information of a similar nature) and not disclose the Confidential Information to any third party except to the extent permitted by the terms of this Agreement; and (ii) not remove or permit to be removed from any item any proprietary, confidential, or copyright notices, markings, or legends placed thereon by either Party. This obligation will continue in effect for five (5) years after expiration or termination of the Agreement.

### 11.4 Team's Entry and Submissions

XPRIZE acknowledges that information relating to technical aspects of any Entry developed by Team and submitted to XPRIZE or the Judging Panel as required by this Agreement, will be deemed Confidential Information of Team, regardless of whether or not it is marked as such.

### 11.5 Injunctive Relief

Each Party acknowledges that money damages would not be a sufficient remedy for any breach of this Section 11 above (Confidentiality), and such breach would result in irreparable harm for which there is no adequate remedy at law. Accordingly, in the event of any such breach or threatened breach, each Party, in addition to any other remedies that it may have, will be entitled, without the requirement of proving actual damages or posting a bond or other security (to the extent permitted under Law), to obtain equitable relief, including without limitation injunctive relief and specific performance in any court of competent jurisdiction.

### 11.6 Remedies

The remedies stated in Section 11.5 above are non-exclusive and the exercise of any right a Party may have will not preclude the exercise of any other right under this Agreement, at law, or in equity.

## 12. REPRESENTATIONS AND WARRANTIES
### 12.1 By Team

Team hereby represents and warrants that:

12.1.1 Team is free to enter into this Agreement without the consent of any third party and has the capability to fully perform its obligations hereunder;

12.1.2 Team is not a party to (and it agrees that it shall not become a party to) any agreement, obligation, or understanding that is inconsistent with this Agreement or might limit or impair XPRIZE's rights or Team's obligations under this Agreement;

12.1.3 There is no suit, proceeding, or any other claim pending or threatened against Team, nor does any circumstance exist, to its knowledge, which may be the basis of any such suit, proceeding, or other claim that could limit or impair Team's performance of its obligations pursuant to this Agreement;

12.1.4 Team will not infringe, violate, misappropriate or interfere with the Intellectual Property, contract or other right of any third party in the course of performance of this Agreement or cause XPRIZE or its affiliates to do any of the same;

12.1.5 As of the date that submission of Entries is required, Team owns (or will own) all technologies, methods, resources and Intellectual Property in Team's Entry or Entries and/or has (or will have) all appropriate license rights in any and all third-party technologies, methods, resources and Intellectual Property ("Third-Party Technology") in such Entry or Entries, and that Team's Entry or Entries will be accompanied by and in accordance with all appropriate licenses in such Third-Party Technology.

12.1.6 Any statement made by Team that relates to XPRIZE will: (i) be truthful and (ii) not disparage XPRIZE or any of its affiliates, officers, directors, or board members, any member of the Advisory Board, Judging Panel, or Competition sponsors.

12.1.7 Team will follow principles of good sportsmanship in taking part in the Competition;

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE SECTION 12.1 ABOVE
TEAM: RT
XPRIZE:

### 12.2 By XPRIZE

XPRIZE hereby represents and warrants that:

12.2.1 Subject to Section 7.7 above, XPRIZE expects that it will have sufficient funds to pay the winning Team(s) directly, subject to Team's compliance with the terms of this Agreement; and

12.2.2 XPRIZE will use reasonable efforts to judge all Teams in a non-preferential and equal manner.

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE SECTION 12.2 ABOVE
TEAM: RT
XPRIZE:

## 13. INDEMNIFICATION AND LIMITATION OF LIABILITY
### 13.1 "Losses" Defined

"Losses" means any losses, liabilities, damages (including, without limitation, personal injury, death or property damage), or claims, or any related costs and expenses (including, without limitation, attorneys' and other legal fees and disbursements and costs of investigation, litigation, settlement, judgment, interest, and penalties).

### 13.2 Indemnification By Team

Team agrees to indemnify, defend, and hold harmless XPRIZE and its affiliates, Sponsor and Sponsor's affiliates, and other Competition Sponsors (if applicable) and their affiliates, from and against any and all Losses which they may incur arising from or relating to Team and/or Team's participation in the Competition.

### 13.3 DISCLAIMER OF WARRANTIES

EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, NO PARTY MAKES ANY WARRANTY, EXPRESS OR IMPLIED, REGARDING THE SUBJECT MATTER OF THIS AGREEMENT, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY, RESULTS OF THE COMPETITION, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NON-INFRINGEMENT. EACH PARTY EXPRESSLY DISCLAIMS ALL SUCH WARRANTIES.

### 13.4 EXCLUSION OF DAMAGES

FOR ANY CLAIMS, CAUSES OF ACTION, DISPUTES (AS DEFINED IN SECTION 14.1 BELOW), LOSSES (AS DEFINED IN SECTION 13.1 ABOVE OR DEMANDS ARISING FROM, RELATING TO, OR IN CONNECTION WITH THIS AGREEMENT, INCLUDING BUT NOT LIMITED TO SUCH CLAIMS RESULTING FROM THE BREACH OF ANY TERM OF THIS AGREEMENT AND/OR A PARTY'S NEGLIGENCE OR OTHER TORTIOUS CONDUCT AND/OR ANY DECISION BY XPRIZE TO DISQUALIFY A TEAM AND/OR TERMINATION OF THIS AGREEMENT BY XPRIZE. NO PARTY SHALL BE LIABLE TO ANY OTHER PARTY FOR ANY LOSS OF PROFITS, LOSS OF USE, LOSS OF GOODWILL, OR ANY INDIRECT, SPECIAL, INCIDENTAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES OF ANY KIND, WHETHER OR NOT SUCH PARTY IS ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, AND EVEN IF CIRCUMSTANCES CAUSE AVAILABLE REMEDIES TO FAIL.

### 13.5 LIMITATION OF LIABILITY

THE TOTAL AGGREGATE LIABILITY OF XPRIZE FOR ANY CLAIMS, CAUSES OF ACTION, DISPUTES (AS DEFINED IN SECTION 14.1 BELOW), LOSSES, (AS DEFINED IN SECTION 13.1 ABOVE) OR DEMANDS ARISING FROM, RELATING TO, OR IN CONNECTION WITH THIS AGREEMENT, INCLUDING BUT NOT LIMITED TO SUCH LIABILITY RESULTING FROM XPRIZE'S BREACH OF ANY TERM OF THIS AGREEMENT AND/OR XPRIZE'S NEGLIGENCE OR OTHER TORTIOUS CONDUCT AND/OR ANY DECISION BY XPRIZE TO DISQUALIFY A TEAM AND/OR TERMINATION OF THIS AGREEMENT BY XPRIZE, SHALL BE LIMITED TO THE LESSER OF: (I) THE AMOUNT TEAM PAID TO XPRIZE UNDER THIS AGREEMENT; OR (II) TEAM'S DIRECT DAMAGES NOT TO EXCEED TWENTY FIVE THOUSAND DOLLARS ($25,000.00). NOTWITHSTANDING THE FOREGOING, THIS SECTION 13.5 SHALL NOT ALTER XPRIZE'S OBLIGATION TO PAY PRIZE PURSES IN ACCORDANCE WITH THE TERMS AND CONDITIONS OF THIS AGREEMENT, INCLUDING BUT NOT LIMITED TO SECTION 7 ABOVE AND THE COMPETITION GUIDELINES, ATTACHED AS EXHIBIT A HERETO.

### 13.6 RELIANCE ON SECTION 13 PROVISIONS

EACH PARTY RECOGNIZES AND ACKNOWLEDGES THAT THE OTHER PARTY WOULD NOT HAVE ENTERED INTO THIS AGREEMENT BUT FOR EACH PARTY'S ACCEPTANCE OF ALL PROVISIONS IN THIS SECTION 13.

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE SECTION 13 ABOVE
TEAM: RT
XPRIZE:

## 14. DISPUTE RESOLUTION
### 14.1 Definition of "Dispute"

"Dispute" shall mean any claim, controversy and/or dispute arising out of or related to this Agreement or the making, performance, breach, or interpretation of this Agreement, including, without limitation, any dispute relating to alleged tortious conduct, administrative decisions made by XPRIZE in the operation of the Competition and/or the decisions of the Judging Panel.

### 14.2 Governing Law

This Agreement and all Disputes arising hereunder shall be governed and construed in accordance with the laws of the State of California, United States of America ("Laws"), without regard to its conflict of laws rules.

### 14.3 XPRIZE and Judging Panel Decisions Final

Decisions made by XPRIZE and/or the Judging Panel: (i) are made in the sole and absolute discretion of XPRIZE and/or the Judging Panel; (ii) are final; and (iii) are not subject to review, reconsideration, or contest.

### 14.4 Goal of the Competition

Team and XPRIZE agree that a paramount goal of the Competition is to inspire and educate individuals, attracting new enthusiasm, new investments, and new ideas to the field and increase the connection that individuals around the world feel to the goals of the Competition ("Goals").

### 14.5 Public Disputes Cause Harm to the Competition

Team and XPRIZE agree that Team, XPRIZE, Sponsor and all of the sponsors of the Competition have invested a substantial amount of time, effort, and resources in the Competition. Team and XPRIZE agree that, in light of the Competition's ultimate goal of inspiring and educating individuals, any public dispute regarding any claim or controversy arising out of or related to this Agreement or the making, performance, breach, or interpretation of this Agreement, including, without limitation, any challenge to any decision by the Judging Panel, would detract from the Goals defined in Section 14.4 above and would reflect poorly on Team, XPRIZE, Sponsor, and other sponsors of the Competition. Further, any public dispute regarding any claim or controversy arising out of or related to this Agreement or the making, performance, breach, or interpretation of this Agreement, including, without limitation, any challenge to any decision by the Judging Panel, will result in irreparable harm to XPRIZE, Sponsor, sponsors and prize fulfillment entities of the Competition.

### 14.6 Resolution of Disputes pursuant to Agreement

Any and all Disputes shall be raised and handled solely pursuant to the dispute resolution provisions set forth in this Agreement and in no other manner. Team and XPRIZE agree that the mandatory and exclusive dispute resolution procedures in this Agreement are in the best interests of both Parties.

### 14.7 Condition Precedent / Notice of Dispute / Statute of Limitations

A PARTY MUST SERVE TO THE OTHER PARTY A WRITTEN NOTICE OF DISPUTE SETTING FORTH: (I) THE SUBJECT OF THE DISPUTE; (II) THE DATE(S) OF EVENT(S) GIVING RISE TO THE DISPUTE; AND (III) THE RELIEF REQUESTED ("NOTICE OF DISPUTE") WITHIN TEN (10) CALENDAR DAYS OF THE FIRST INCIDENT GIVING RISE TO THE DISPUTE. SERVICE OF THE NOTICE OF DISPUTE WITHIN SUCH TEN (10)-DAY PERIOD IS A CONDITION PRECEDENT TO PURSUING ANY DISPUTE HEREUNDER AND FAILURE TO DO SO SHALL MEAN THAT ANY RIGHT TO RAISE ANY SUCH CLAIM, CONTROVERSY AND/OR DISPUTE SHALL BE FOREVER FORFEITED AND WAIVED.

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE SECTION 14.7 ABOVE
TEAM: RT
XPRIZE:

### 14.8 Informal Dispute Resolution

If a Party has served a Notice of Dispute in accordance with the provisions of Section 14.7 above, then the Parties agree to first attempt to resolve their dispute informally within sixty (60) days of the date of service of the Notice of Dispute in accordance with the following:

14.8.1 Each Party shall appoint a designated representative whose task it will be to meet for the purpose of endeavoring to resolve such dispute.

14.8.2 The designated representatives shall meet as often as the Parties reasonably deem necessary in order to gather and furnish to the other Party all information with respect to the matter at issue which the Parties believe to be appropriate and germane in connection with its resolution. The representatives shall discuss the problem and attempt to resolve the dispute without the necessity of any formal proceeding.

14.8.3 The specific format for the discussions will be left to the discretion of the designated representatives.

### 14.9 Mediation

The Parties agree that in the event that any Dispute cannot be resolved within sixty (60) days of the date of service of the Notice of Dispute pursuant to the informal dispute resolution process set forth in Section 14.8 above, then no later than ninety (90) days after the date of service of the Notice of Dispute and as a condition precedent to any future demand for arbitration, either Party may commence mediation by providing the other Party a written request for mediation. Upon written request, the Parties will proceed with non-binding mediation before a mediator selected by the Parties to be held in Los Angeles, California. Provided, however, that if one Party maintains that the other Party has failed to comply with the requirements set forth in Section 14.7 above, then such Party shall have the right to refuse to mediate the dispute and proceed directly to arbitration pursuant to Section 14.10 below.

The Parties shall cooperate with one another in selecting a mediator and in scheduling the mediation proceedings. Each Party shall designate at least one (1) person with full settlement authority to attend an in-person mediation in Los Angeles, California. The mediation must take place within thirty (30) days of a Party's written request to engage in mediation, unless agreed otherwise in writing by the Parties.

The Parties covenant that they shall participate in the mediation in good faith, and that they will share equally in the cost of the mediation, including mediator's fees. Further, each Party shall pay all expenses for its own participation therein. All offers, promises, conduct, and statements, whether oral or written, made in the course of the mediation by either of the Parties, their agents, employees, experts, and attorneys, and by the mediator, shall be confidential, privileged under California Evidence Code §§ 1115-1128, and inadmissible for any purpose, including, without limitation, impeachment, in any litigation or other proceeding involving the Parties, provided that evidence that is otherwise admissible or discoverable will not be rendered inadmissible or non-discoverable as a result of its use in the mediation.

### 14.10 Arbitration

Except as provided in Section 11 above (Confidentiality), if the Parties are not able to settle the Dispute in mediation pursuant to Section 14.9 above, Team and XPRIZE agree that: (i) any Dispute; (ii) any issues pertaining to the Dispute; and/or (iii) any claim that this Agreement or any part hereof is invalid, illegal, or otherwise voidable or void, shall be submitted to and finally determined by mandatory and binding arbitration. Arbitration will be conducted in two stages as set forth below. As a condition precedent to arbitration of any Dispute, the Party seeking to arbitrate the Dispute must file a demand for arbitration with JAMS in Los Angeles County, California, as set forth in Section 14.10.4, within one hundred and eighty (180) days of the date of service of the Notice of Dispute. Failure to file the demand to arbitrate with JAMS within such 180-day period shall mean that any right to arbitrate or litigate in any manner such Dispute shall be forever forfeited and waived.

14.10.1 Mandatory and Binding Arbitration: The arbitration and the Parties' agreement therefore will be deemed to be self-executing, and if either Party fails to appear at any properly-noticed arbitration proceeding, an award may be entered against such Party despite said failure to appear and the matter will be dismissed with prejudice. Failure by either Party to pay the fees (or provide a required deposit) of the arbitrators and/or the arbitration administrator in accordance with the rules and policies of the applicable arbitration administrator will result in a forfeiture by the non-paying Party of the right to prosecute or defend the claim which is the subject of the arbitration, but will not otherwise serve to abate, stay, or suspend the arbitration proceedings. The Parties will share equally the arbitrators' fees and expenses, International Chamber of Commerce (ICC) administrative expenses, or other costs incurred by the ICC in the arbitration; provided, however, that each party shall bear its own attorneys' and experts' fees and its own costs incurred in connection with any Dispute hereunder including the arbitration of any Dispute. Further, each Party shall compensate and pay all expenses for its employees and, with respect to Team, all other Team Members for their participation in the arbitration.

14.10.2 Scope of Arbitrators' Authority: The arbitrators will have no power or authority to grant attorneys' fees, punitive or exemplary damages as part of their award. In no event may the provisions of this Agreement, or any ancillary agreement executed in connection with this Agreement, including, without limitation, amendments to this Agreement, be waived, modified, changed, or otherwise equitably excused by the arbitrators at any arbitration hearing. The Parties do not grant the arbitrators the powers of an amiable compositeur and the arbitrators do not have the power to decide ex aequo et bono. The arbitrators will apply California substantive Law to the proceeding. The arbitrators will not have the power to commit errors of Law or legal reasoning, and the award may be vacated or corrected on appeal to a court of competent jurisdiction for any such error. Any arbitration will be conducted in English in Los Angeles, California, USA.

14.10.3 Jurisdiction for Entering Arbitration Awards: The award of the arbitrators will be the exclusive remedy between the Parties regarding any claims, causes of action, counterclaims, issues, or accountings presented or pled to the arbitrators. Any petition, motion, or request to vacate the award shall be filed exclusively in the Los Angeles County Superior Court, and the Parties expressly consent to the exclusive jurisdiction of the Los Angeles County Superior Court over any such petition, motion, or request to vacate the award. The provisions of the California Arbitration Act will apply to any petition, motion, or request to vacate the award pursuant to this Section 14.10.3.

The Parties may confirm or enforce the award in any court of competent jurisdiction; provided, however, that if any party files a petition to confirm the award in the United States of America, such petition will be governed by the provisions of the California Arbitration Act. The Parties may have the judgment domesticated by any court of competent jurisdiction.

14.10.4 Stage 1 Arbitration: The first stage of arbitration shall be conducted before JAMS in Los Angeles County, California, in accordance with the JAMS Optional Expedited Arbitration Procedures by three (3) arbitrators appointed as follows: each Party shall select an arbitrator, and such arbitrators shall select a third; provided, however, that in all events at least two (2) out of the three (3) arbitrators must be active members of the bar of a U.S. State and that each arbitrator must be fluent in English. The matters to be considered and determined by the arbitrators in Stage 1 Arbitration shall include and be limited to the following:

(i) First, the arbitrators shall determine whether or not the Party that served the Notice of Dispute strictly complied with the requirements set forth in Section 14.7 above. If the arbitrators determine that the Party that served the Notice of Dispute failed to strictly comply with the requirements of Section 14.7 above, then the arbitrators shall issue an award dismissing the Dispute with prejudice and ruling that the Party that served the Notice of Dispute shall take nothing thereunder.

(ii) Next, if (a) the arbitrators determine that the Party that served the Notice of Dispute did strictly comply with the requirements of Section 14.7 above, and (b) either Party asserts that the Limitation of Liability provisions set forth in Section 13.5 above are unenforceable in whole or in part, then the arbitrators shall next determine whether or not the Dispute is subject to the Limitation of Liability provisions set forth in Section 13.5 above and issue a ruling of their findings. For purposes of this determination, the Parties agree and represent that the Limitation of Liability Clauses are not contrary to public policy as articulated in Tunkl v. Regents of University of California, 60 Cal. 2d 92 (1963).

(iii) EACH PARTY'S REPRESENTATION IN THIS PARAGRAPH IS A MATERIAL INDUCEMENT FOR THE OTHER PARTY TO ENTER INTO THIS AGREEMENT. IF NEITHER PARTY ASSERTS THAT THE LIMITATION OF LIABILITY PROVISIONS SET FORTH IN SECTION 13.5 ABOVE ARE UNENFORCEABLE IN WHOLE OR IN PART, THEN THE ARBITRATORS SHALL ISSUE A RULING THAT SUCH PROVISIONS ARE FULLY ENFORCEABLE WITH RESPECT TO THE DISPUTE.

INITIAL HERE TO ACCEPT AND ACKNOWLEDGE THIS SECTION 0(iii) ABOVE
TEAM: RT
XPRIZE:

(iv) All awards, decisions and rulings made with regard to the items specified above by the arbitrators in Stage 1 Arbitration shall be binding upon both Parties and upon the arbitrators in Stage 2 Arbitration (if applicable). However, except as required to establish the decisions and rulings of the arbitrators, the records of the proceedings in Stage 1 Arbitration shall not be admissible as evidence in Stage 2 Arbitration proceedings.

14.10.5 Ninety (90)-Day Cooling Off Period: If the arbitrators have not dismissed the Dispute with prejudice when they issue their final rulings pursuant to Section 14.10.4(i) above, then the Parties shall wait for a period of ninety (90) calendar days before proceeding with Stage 2 Arbitration, during which ninety (90)-day period, the Parties agree to negotiate in good faith to resolve the Dispute. This period may be extended by mutual agreement of the Parties.

14.10.6 Stage 2 Arbitration: If necessary, the second stage of arbitration shall be conducted before the International Chamber of Commerce (ICC) in Los Angeles County, California, in accordance with the then-prevailing Rules of Arbitration of the ICC by three (3) arbitrators appointed as follows: each Party shall select an arbitrator, and such arbitrators shall select a third; provided, however, that in all events at least two (2) out of the three (3) arbitrators must be active members of the bar of a U.S. State and that each arbitrator must be fluent in English. Notwithstanding the foregoing, none of the arbitrators used in Stage 1 Arbitration may be selected in Stage 2 Arbitration.

### 14.11 Other Decisions of XPRIZE and the Judging Panel

Nothing in this Section 14 (Dispute Resolution) will limit in any manner: (i) the ability of XPRIZE to eliminate or disqualify Team or cancel the Competition; (ii) the ability of XPRIZE or Team to seek injunctive relief as expressly provided in Section 11.5 above (Confidentiality — Injunctive Relief), and Exhibit B, Paragraph XV (Media Rights Agreement — Injunctive Relief for XPRIZE); or (iii) the sole and exclusive discretion of the Judging Panel, as provided in Section 5.4 above (Judging Panel) and in the Competition Guidelines.

### 14.12 Attorney's Fees

Unless otherwise expressly set forth herein, the Parties shall bear their own attorney's fees, costs, and expenses in connection with the matters set forth in the Agreement.

## 15. TEAM MANAGEMENT
### 15.1 Team Name

The legal entity that is the Team ("Team Entity") and the official name of the Team ("Team Name") shall be set forth in the Team's profile in Section 1 above of this Agreement.

### 15.2 Changes to Team Name

Team shall promptly inform XPRIZE of any intent to change the Team Name and cooperate with XPRIZE to execute the documents and instruments necessary to accomplish such change.

### 15.3 "Team Member" Defined

"Team Member" shall be defined as an individual or corporate entity acting as either an employee, consultant, volunteer, or contractor of Team who makes any contribution to Team's efforts in connection with the Competition, as determined by XPRIZE in its sole and absolute discretion. Team Members include, without limitation: (i) contributors of any pre-existing or developed Intellectual Property to Team; (ii) individuals or entities involved in the design, development, or testing of the Entry; and (iii) any individual or entity having a management, supervisory, or other leadership role within Team. Team Members do not include: (a) investors, donors, and Team Sponsors who make only financial contributions to Team; (b) suppliers of off-the-shelf parts and hardware; or (c) customers of the Team; and (d) third-party holders of any intellectual property licensed to Team for use in its Entry.

### 15.4 Team Member Requirements

Except as provided herein, individual Team Members must either: (i) be of the age of majority (or older) in their jurisdiction of residence; or (ii) obtain the signed written consent of a parent or legal guardian, in order to be eligible to participate in the Competition. If a Team Member is not of the age of majority (or older) in their jurisdiction of residence, then all contracts and waivers required to be signed by Team Members must be signed by such Team Member's parent or legal guardian. All Team Members shall be listed in Team's records on the Competition Portal. Team may add and/or remove Team Members at any time through the Competition Portal. Team agrees to promptly notify XPRIZE through the Competition Portal in the event that Team decides to add and/or remove one or more Team Members.

### 15.5 Team Leader

Each Team shall designate a Team Member to act as "Team Leader" in all communications with XPRIZE. Team Leader will be responsible for receiving communications from and communicating with XPRIZE and the Judging Panel. The Team Leader shall be an individual and shall be at least eighteen (18) years old (or the age of majority in their jurisdiction of residence, if such age of majority is older than eighteen (18) years of age).

### 15.6 Changes in Team Leadership

Team may replace the designated Team Leader at any time through the Competition Portal. Team shall promptly notify XPRIZE through the Competition Portal in the event that Team decides to replace the designated Team Leader. XPRIZE reserves the right to disqualify Team if Team unreasonably and repeatedly appoints a new Team Leader, appoints a Team Leader who is unqualified, or otherwise disrupts the administration of the Competition. For clarity, Team Leaders must perform all obligations required of Team Members, including, without limitation, signing and delivering a Team Member Release, Waiver, and Confidentiality Agreement.

### 15.7 Team Release and Waiver

Concurrent with the execution of the Agreement, Team Leader shall execute the Team Release and Waiver (in the form attached as Exhibit D to the Agreement) on behalf of the Team and the Team Entity. If Team fails to timely provide a Team Release and Waiver, as required pursuant to this Section 15.7, then Team shall be ineligible to participate in the Competition.

### 15.8 Team Member Release and Waiver

TEAM SHALL ENSURE THAT EACH TEAM MEMBER THAT IS NOT AN EMPLOYEE OF THE TEAM ENTITY (INCLUDING TEAM LEADER, IF APPLICABLE) RECEIVES, REVIEWS, SIGNS AND DELIVERS TO XPRIZE A SIGNED COPY OF THE TEAM MEMBER RELEASE, WAIVER AND CONFIDENTIALITY AGREEMENT (IN THE FORM ATTACHED AS EXHIBIT E TO THIS AGREEMENT) ON BEHALF OF SUCH TEAM MEMBER. If Team Member is an entity, then such Team Member's Team Member Release, Waiver and Confidentiality Agreement shall be on behalf of all employees of such Team Member. Team shall deliver to XPRIZE a signed copy of the Team Member Release, Waiver and Confidentiality Agreement for each and every Member of the Team within thirty calendar (30) days of the Effective Date of the Agreement. Team agrees that, prior to admitting any new Team Member(s), Team shall deliver to XPRIZE a copy of the Team Member Release, Waiver and Confidentiality Agreement signed by each new Team Member. If Team fails to timely provide a Team Member Release, Waiver and Confidentiality Agreement for each Team Member, as required pursuant to this Section 15.8, then Team shall be ineligible to participate in the Competition.

### 15.9 Decisions Concerning Team Participation in Competition

To the maximum extent permissible under applicable law, Team Leader and each Team Member agrees to abide by any decision made by XPRIZE to remove, suspend, deem ineligible, or disqualify Team, without contest, legal recourse, or any other action of protest of the decision. Such decisions may be made by XPRIZE for reasons including, but not limited to, ethical transgressions, breach or violation of this Agreement, actions that jeopardize the Competition, or actions that jeopardize sponsorship of the Competition.

## 16. GENERAL LEGAL PROVISIONS
### 16.1 Not Agents, Partners, or in Joint Venture

Parties are not agents or partners of or with one another. Parties are not engaged in any form of joint venture with one another. Parties cannot bind one another by contract.

### 16.2 No Third-Party Beneficiaries

Except as expressly set forth in Section 9 above, Parties agree and acknowledge that there are, and shall be, no third-party beneficiaries to this Agreement, including without limitation, Team Members.

### 16.3 Official Language

The official language of the Competition and of this Agreement shall be English. All communications with XPRIZE will be in English unless Team has received prior written authorization from XPRIZE to submit communications in another language. Additional copies in other languages are welcomed and, if provided on behalf of XPRIZE, are for convenience only but are in no way binding on XPRIZE.

### 16.4 Notices

All notices, requests, claims, demands and other communications between the parties shall be in writing. All notices shall be given (i) by delivery in person (ii) by a nationally recognized next day courier service, (iii) by first class, registered or certified mail, postage prepaid, (iv) by facsimile, or (v) by electronic mail to the address of the party specified in this Agreement or such other address as either party may specify in writing. All notices shall be effective upon (i) receipt by the party to which notice is given, or (ii) on the fifth (5th) calendar day following mailing, whichever occurs first.

### 16.5 Force Majeure

Neither Party hereto will be liable for or suffer any penalty or termination of rights hereunder by reason of any failure or delay in performing any of its obligations hereunder if such failure or delay is occasioned by compliance with governmental regulation or order, or by circumstances beyond the reasonable control of the Party so failing or delaying, including, but not limited to, acts of God, war, civil war, insurrection, acts of terrorism, sabotage, an act of public enemy, travel warnings announced by the United States Department of State, fire, flood, accident, strike or other labor disturbance, equipment failure, or interruption of or delay in transportation caused by forces beyond the parties' control ("Force Majeure Event"). Each Party will promptly notify the other in writing of any such Force Majeure Event, the expected duration thereof, and its anticipated effect on the Party affected. XPRIZE has no obligation to suspend or delay the Competition to accommodate Team if a Force Majeure Event impedes Team's ability to participate in the Competition according to the Competition schedule. XPRIZE may suspend, postpone, or cancel the Competition in the case of a Force Majeure Event.

### 16.6 No Waiver

No failure of either Party to insist upon strict compliance with any covenant, obligation, condition, warranty or agreement contained herein will operate as a waiver of, or estoppel with respect to, any such covenant, obligation, condition, or agreement. Waiver by any Party of any breach of any provision of this Agreement will not be considered as, nor constitute, a continuing waiver or waiver of any other breach of any provision of this Agreement.

### 16.7 Headings

Article, section, subsection and paragraph headings in this Agreement are included for convenience of reference only and will not constitute a part of this Agreement for any other purpose.

### 16.8 Severability

If any provision of this Agreement conflicts with the Law under which this Agreement is construed or that is otherwise applicable to a Team, or if any such provision is held invalid by a competent authority, such provision will be deemed to be restated to reflect as nearly as possible the original intentions of the parties in accordance with Law. If the competent authority holds the provision illegal, invalid, or unenforceable even after restatement, the provision will be limited or eliminated to the minimum extent necessary. The remainder of this Agreement will remain in full force and effect.

### 16.9 No Strict Construction

In the event an ambiguity or question regarding the enforceability, intent or interpretation of any term or condition of this Agreement arises, this Agreement will be construed as if drafted jointly by the parties, and no presumption or burden of proof will arise favoring or disfavoring any Party by virtue of the authorship of any of the provisions of this Agreement. No Agreement from any prior or future XPRIZE competition will be used to construe this Agreement, and this Agreement will not be used to construe any Agreement from any prior or future XPRIZE competition.

### 16.10 Counterparts

This Agreement may be signed in counterparts, and together signed and delivered counterparts will constitute a complete, binding contract. Facsimile or electronic signatures will have the same weight and effect as originals.

### 16.11 Survival

The following Sections of, and Exhibits to, this Agreement will survive the expiration or termination of this Agreement: Sections 2 above (Scope of Agreement); 3.7 above (Return and Reallocation of Awards); 6.5 above (Effect of Cancellation); 7.4 above (Allocation of Prizes); 7.5 above (Awards Subject to Applicable Law); 7.7 above (Prize Purse Conditions); 11 above (Confidentiality); 11 above (Representations and Warranties); 12 above (Indemnification and Limitation of Liability); 13 above (Dispute Resolution); 15 above (General Legal Provisions); and any and all Exhibits and Waivers, etc.

## 17. EXHIBITS AND RELATED FORMS
### 17.1 Exhibits Incorporated into Agreement

THE PARTIES AGREE AND ACKNOWLEDGE THAT THEY SHALL BE BOUND BY THE TERMS AND CONDITIONS OF ALL EXHIBITS TO THIS AGREEMENT. THE FOLLOWING EXHIBITS ARE ATTACHED HERETO AND ARE INCORPORATED INTO THIS AGREEMENT BY THIS REFERENCE:

17.1.1 Exhibit A — Competition Guidelines

17.1.2 Exhibit B — Media Rights Agreement

17.1.3 Exhibit C — Insurance Requirements

17.1.4 Exhibit D — Team Release and Waiver

17.1.5 Exhibit E — Team Member Release, Waiver and Confidentiality Agreement

### 17.2 Forms Incorporated into Agreement

THE PARTIES AGREE AND ACKNOWLEDGE THAT THEY WILL BE BOUND BY THE TERMS AND CONDITIONS OF ANY AND ALL FORMS COMPLETED AS PART OF THE INTENT TO COMPETE FORM; (ii) THE TEAM INFORMATION PROVIDED THROUGH THE COMPETITION PORTAL; AND (iii) THE ENTRY SUBMISSION FORM(S) AND REGISTRATION PROCESS DESCRIBED IN SECTION 4 ABOVE, AND THAT ALL SUCH FORMS ARE HEREBY INCORPORATED INTO THIS AGREEMENT BY THIS REFERENCE, OR SHALL BE INCORPORATED INTO THIS AGREEMENT WHEN SUCH FORMS ARE COMPLETED AND SUBMITTED BY TEAM.

### 17.3 Additional Exhibits

As pursuant to section 6.6 above, XPRIZE may at its sole and absolute discretion add Exhibits to this Agreement for the purpose of further clarifying the rules and regulations governing the Competition.

### 17.4 All Exhibits Subject to Change and Updates

The parties agree and acknowledge that, as pursuant to sections 6.6 above and 8.2 above of this Agreement, and to this Section 17.4, all Exhibits are subject to change and update at XPRIZE's sole and absolute discretion.

## EXHIBIT A — Competition Guidelines

The Competition Guidelines may be accessed through the Competition Website at:

https://www.xprize.org/prizes/covidtesting/guidelines

## EXHIBIT B — Media Rights Agreement

XPRIZE intends to capture audio, video, digital, and photographic material related to the Competition ("XPRIZE Media"). XPRIZE shall retain (on behalf of itself, its Prize Fulfillment Partner and its media partners, including without limitation Discovery Channel) the right to request and obtain preferential (above Team media partners and other media organizations) access to any and all Team facilities or events for the purposes of the capture of XPRIZE Media for later usage; these requests shall not be unreasonably denied or delayed. Team shall use best efforts to provide similar access to facilities of Team contractors, sponsors or partners for the purposes of capture of XPRIZE Media. If such access is not possible, such as for reasons of confidentiality or health and safety, Team shall provide a XPRIZE with a written communication describing with particularity the reasons that such access is not possible. XPRIZE shall consider such communication in good faith and will then determine whether or not (in its sole discretion) to waive this requirement with respect to the particular facility or event. The parties acknowledge and agree that Team's agreement to provide such preferential access constitutes material consideration under this Agreement and XPRIZE's ability to capture and use XPRIZE Media in communications to the general public is a primary purpose for which the Competition is conducted. Accordingly, submission of bad faith requests or other abuse of this provision may, in the sole discretion of XPRIZE, result in Team's disqualification or other adverse consequences to Team.

XPRIZE shall have the right to use, copy, sublicense, modify, transmit, display, distribute, perform, make, sell, assign, license, transfer, import, export, and otherwise dispose of or exploit XPRIZE Media in any manner or medium whatsoever, existing now or in the future, including, without limitation, all motion picture rights of every kind, including, without limitation, theatrical and documentary motion picture rights, television motion picture rights, and home video rights, and all allied, subsidiary, and derivative rights, including, without limitation, sequel, prequel, and remake rights, novelization, comic book, comic strip, newspaper comics, "making of" book, merchandising rights, commercial tie-ups, stage rights, radio rights, webcast rights, internet display rights, and promotional and advertising rights, including, without limitation, the right to broadcast over radio, television, the internet, and all other media, advertisements with respect to any production produced based on the Competition or the story of the Competition. The right to capture and use XPRIZE Media shall include, without limitation, all rights and title in and to any and all audio, video, or photographic material created by, or on the behalf of, XPRIZE or its agent, representatives and assignees. XPRIZE shall not receive any pecuniary consideration in exchange for the license or distribution of XPRIZE Media. Except as necessary for purposes of judging the Competition, XPRIZE will not require Team to disclose their Craft in dissembled form or permit access to discussions with respect to pending patent applications or other Confidential Information of Team. Nevertheless, Team bears ultimate responsibility for ensuring that its Confidential Information is not revealed during the recording of any XPRIZE Media.

If XPRIZE desires to depict any Team Intellectual Property not covered by the grants of rights herein in its production of XPRIZE Media or for advertising or promotional purposes, XPRIZE shall submit a request to Team for permission to use such materials solely for such purposes of producing media content or educational materials related to the Competition. Team agrees not to unreasonably withhold, condition, or delay approval for XPRIZE to depict Team Intellectual Property for production of XPRIZE Media or educational materials related to the Competition, it being understood that such approval would be withheld reasonably if it were to unduly interfere with Team's revenue generation, efforts to file patent applications, agreements with financiers or customers, or trade secrets. Furthermore, Team agrees not to unreasonably withhold permission for advertising or promotional use related to the Competition. Team shall use best efforts to respond to such requests within ten (10) business days. If the content of any XPRIZE Media is subject to 17 U.S.C. 106A or any similar laws, Team hereby irrevocably waives and agrees not to assert all rights under such laws and irrevocably appoints XPRIZE as its agent to assert on Team's behalf, Team's moral rights or any equivalent rights regarding the form or extent of any alteration to the XPRIZE Media (including, without limitation, removal or destruction) or the making of any derivative works based on the XPRIZE Media, including, without limitation, photographs, drawings or other visual reproductions of the work, in any medium, for XPRIZE's purposes.

Team agrees to execute all papers and to perform any acts as XPRIZE may deem necessary to secure for XPRIZE or its designee the rights herein assigned or granted, including, without limitation, any third-party consents that may be necessary to capture and use XPRIZE Media. Further, Team irrevocably appoints XPRIZE as Team's attorney-in-fact to do all of the foregoing, such appointment being coupled with an interest.

XPRIZE will use reasonable efforts to promote the Competition. XPRIZE also anticipates that Team may enter agreements with media partners that are interested in promoting Team's participation in the Competition ("Team Media Partners"). Team shall provide notice to XPRIZE no later than thirty (30) calendar days prior to the execution of any agreement with a Team Media Partner, by completing and submitting the Team Media Partnership Notification Form that will provide XPRIZE with the following information: (i) name of Team Media Partner; (ii) a brief description of the media, marketing, or promotional rights granted to the Team Media Partner; and (iii) a written summary of the business points of any agreement with the Team Media Partner. XPRIZE shall review such agreement terms within ten (10) business days. If such contracts or relationships involve any contractual or implicit commitment to exclusivity, then XPRIZE may impose limitations on or reject the proposed Team Media Partner Agreement as XPRIZE determines to be in the best interests of the Competition. XPRIZE may also reject the proposed Team Media Partner Agreement, if such agreement, in XPRIZE's sole opinion: (i) would cause Team to breach any term of this Agreement; (ii) would require unsuitable advertising including, but not limited to, any advertising that depicts, describes, implies, or promotes obscene or sexually explicit matters, libelous or illegal matters, violence, racial, sexual or other types of legally prohibited discrimination, a particular political view, or may infringe on or otherwise violate any rights of XPRIZE or any third party; (iii) conflicts with the exclusivity of or jeopardizes any sponsorship associated with the Competition; or (iv) undermines the Competition, its underlying goals, or the educational mission of XPRIZE. Team is encouraged to work with XPRIZE well prior to finalizing any agreements with a Team Media Partner to streamline the approval process. If Team has signed agreements with Team Media Partners or other similar relationships prior to the execution of this Agreement, Team shall provide to XPRIZE a detailed written summary of the business points of such agreements and shall amend or terminate such agreements upon request by XPRIZE in accordance with this Exhibit.

## EXHIBIT C — Insurance Requirements
### Liability Insurance

Within thirty (30) days of being selected as a Semifinalist Team, Team shall procure, pay for and thereafter maintain such insurance as will protect against claims for bodily injury or death, or for damage to property, which may arise out of the Team's participation in the challenge or by anyone employed by any of them, or by anyone for whose acts any of them may be liable. Such insurance will include but not be limited to the following minimum coverage and limits of no less than Two Hundred Fifty Thousand Dollars ($250,000) per occurrence and Five Hundred Thousand Dollars ($500,000) aggregate.

Teams that are selected as one of the top five finalists shall procure, pay for and thereafter maintain such insurance as will protect against claims for bodily injury or death, or for damage to property, which may arise out of the Team's participation in the challenge or by anyone employed by any of them, or by anyone for whose acts any of them may be liable. Such insurance will include but not be limited to the following minimum coverage and limits of no less than Five Hundred Thousand Dollars per occurrence [$500,000.00] and One Million Dollars ($1,000,000.00) aggregate.

If Team is non-U.S. owned and operated with principal operations outside the jurisdiction of the government of the United States of America, Team may fulfill these Insurance Requirements by alternate means, such as by obtaining a comparable insurance policy (with appropriate endorsements) issued in the country of origin similar to a commercial General Liability policy (International Standards Organization form).

If Team is non-U.S. based, Team will not require a Waiver of Subrogation endorsement.

If Team is a government or non-profit educational institution, Team may rely on sufficient self-insurance coverage in place of a General Liability policy, or some combination thereof, which complies with the above criteria.

Team shall obtain, from its general liability insurance provider, a certificate of insurance evidencing the above coverage and appropriate endorsements to the policies obtained that name "XPRIZE Foundation, Inc. as an Additional Insured with Waivers of Subrogation.

**If Team does not obtain XPRIZE written approval of all insurance and eligibility requirements, then Team may be ineligible to participate in the Semifinal and/or Final round of this competition.**

### Workers' Compensation — Volunteers Accident Insurance

Team shall maintain Workers' Compensation or comparable insurance as required by any applicable Law, in accordance with the provisions of the Laws of the nation, state, territory or province having jurisdiction over Team's employees with limits sufficient to cover Team's potential liability to its employees in connection with Team's participation in the Competition. If Team has no employees or is otherwise not required by applicable laws to carry such insurance, then Workers Compensation Insurance will not be required. In the event Team is exempt from the requirement to obtain Workers' Compensation insurance pursuant to Law, Team shall insure that all individuals serving as volunteers secure Health Insurance and/or Volunteers Accident Insurance. Team shall be solely responsible for verifying that all volunteers have either form of insurance with sufficient coverage for any and all injuries that may occur during the course of the Competition.

### Automobile Insurance

If Team owns, leases or operates automobiles in connection with its participation in the Competition, Team will maintain an automobile insurance policy with limits sufficient to cover Team's potential liability for bodily injury and property damage to third parties in connection with Team's participation in the Competition. Coverage should include protection for owned automobiles, non-owned automobiles, and hired automobiles, as applicable. An endorsement to the General Liability Policy or self-insurance coverage above covering hired & non-owned automobiles is acceptable.

### Insurance Providers and Coverage Term

All policies and limits should be written with an insurer with an AM Best Rating of A-VII or better, or in the case of workers' compensation, be insured by an acceptable state or government approved program. If the insurer is not rated by AM Best, evidence supporting the insurer's financial strength may be required and be subject to the approval of XPRIZE. The insurance policies required above shall be maintained by Team for such length of time as is necessary to cover all claims arising out of or related to Team's participation in the Competition.

### Compliance Certification Form

Each Team will be required to provide XPRIZE with proof that Team has satisfied the above Insurance Requirements by delivering to XPRIZE a completed Compliance Certification Form (in a form to be provided by XPRIZE), pursuant to which Team will be required (among other requirements as detailed in Section 4.5 of the Agreement) to: (i) clearly outline documentation clearly outlining (in English) how the Team's insurance coverage satisfies the Insurance Requirements set forth above; (ii) certifying, as evidenced by the signature of the Team Leader and Team's insurance agent, broker or representative, that Team is in full compliance with the Insurance Requirements; and (iii) attaching certificates of insurance (in English) evidencing the required coverage, including without limitation, endorsements to the general liability policies naming the XPRIZE Foundation, Inc. as an Additional Insured with Waivers of Subrogation, in a form satisfactory to XPRIZE. A Waiver of Subrogation endorsement is not required for International Teams. The template Compliance Certification Form and the deadline for submission of a completed and signed Compliance Certification Form shall be provided by XPRIZE in the to be attached to the Competition Guidelines.

As specified in Section 4.5 of the Agreement, in addition to the requirements specified above, XPRIZE shall also have the right, at its sole and absolute discretion, to demand that Team submit a Compliance Certification form at any time during the Term, within ten (10) business days of the delivery of a written demand from XPRIZE to Team.

**ATTENTION TEAMS — DO NOT WAIT TO GET INSURANCE COVERAGE**

The delivery of a written demand to submit current proof of insurance coverage is not intended to give you time to get the necessary insurance policies if they are not already in place. If you don't have the required insurance coverage when you are required to submit proof of such insurance, then you will be ineligible to continue to participate in the Competition. This means that you should definitely not delay in getting the required insurance coverage.

## EXHIBIT D — Team Release and Waiver

Team acknowledges and agrees, on behalf of Team and each Team Member, that XPRIZE, Sponsor and any parties affiliated with XPRIZE or Sponsor in connection with the Competition ("Released Parties") will not be liable for any liabilities, damages (including, without limitation, personal injury, death or property damage), or claims, or any related costs and expenses ("Losses") arising from, related to, or connected in any way with any property loss or damage or personal injury, including, without limitation, death, sustained by Team, any Team Member, any partner, sponsor or affiliate of Team, or any person or entity claiming on behalf of Team, arising from, relating to, or connected in any way with Team's participation in the Competition, even in the event of negligence or fault of any of the Released Parties, whether such negligence is present at the execution of the Competitor Agreement ("Agreement") or arises in the future. Team assumes full responsibility for and all risks of any Losses which may occur to Team, any Team Member, any partner, sponsor or affiliate of Team, or any person or entity claiming on behalf of Team, arising from, relating to, or connected in any way with Team's participation in the Competition. Team hereby unconditionally releases and waives all of the Released Parties from any claims alleging Losses, whether existing now or arising in the future, that in any way relate to the Released Parties' execution or duties under this Agreement.

### Waiver of California Civil Code Section 1542

The releases in this Agreement are intended to be, and are, full, complete, unconditional and general releases with respect to all claims, demands, causes of action, defenses, and other matters described above, or any other theory, cause of action, occurrence, matter or thing which might give rise to liability, related to or arising out of any and all acts, omissions, or events occurring prior to the date of this Agreement.

Team and all Team Members acknowledge that he, she, or it is familiar with Section 1542 of the California Civil Code, which reads as follows:

A GENERAL RELEASE DOES NOT EXTEND TO CLAIMS WHICH THE CREDITOR DOES NOT KNOW OR SUSPECT TO EXIST IN HIS OR HER FAVOR AT THE TIME OF EXECUTING THE RELEASE, WHICH IF KNOWN BY HIM OR HER MUST HAVE MATERIALLY AFFECTED HIS OR HER SETTLEMENT WITH THE DEBTOR.

With respect to those claims being released hereunder, each of the Parties acknowledges that he, she, or it is releasing unknown claims and waives all rights he, she, or it has or may have under California Civil Code Section 1542 or any other statute or common law principle of similar effect. Each of the Parties acknowledges that he, she, or it may hereafter discover claims or facts in addition to or different from those now known or believed to exist with respect to the subject matter of the claims being released pursuant hereto, and which, if known or suspected at the time of entering into the Agreement, may have materially affected this Agreement. Nevertheless, each of the Parties hereby waives any right, claim(s), or cause of action that might arise as a result of such different or additional claim(s) or facts. Each of the Parties acknowledges and understands the significance and consequence of such release and such specific waiver of California Civil Code Section 1542.

### No Liability

Team agrees that the Released Parties will not be held liable for any Losses that accrue or may accrue to Team, any Team Member, any partner or affiliate of Team, any Team Sponsor, or any person or entity claiming on behalf of Team, arising in any way from Team's participation in the Competition.

Team Signatory Signature: DocuSigned by Randy True (8AEA81FF0C4440E...)
Date: 9/8/2020
Team Signatory Name: Randy True
Team Signatory Title: CEO

## EXHIBIT E — Team Member Release, Waiver and Confidentiality Agreement

This Team Member Release, Waiver, and Confidentiality Agreement is made pursuant to that certain Competitor Agreement ("Agreement"). I represent and warrant that I have reviewed the Agreement to which this Team Member Release, Waiver and Confidentiality Agreement is attached as Exhibit E, and I hereby agree to be bound by, and comply with, the terms and conditions of the Agreement.

FOR AND IN CONSIDERATION and as a condition of the granting of permission and authority for the undersigned to participate as a Team Member of the Team specified below ("Team") in the Competition, the Team Member specified below ("Team Member"), does hereby release, acquit, and discharge the Released Parties (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) from any and all Losses (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) now accrued or hereafter to accrue on account of Team Member's participation in the Competition.

I Team Member, hereby for myself, my heirs, executors, and administrators:

1. Recognize and acknowledge that, as a Team Member, I am bound by the terms and conditions of Section 11 of the Agreement (Confidentiality) and covenant to comply with the terms and conditions thereof;

2. Understand and acknowledge that my participation in the Competition may be dangerous and could lead to serious injury or death;

3. Voluntarily assume any and all risks associated with participating in the Competition, and understand, acknowledge, and agree that the Released Parties will not be responsible or liable for any Losses that may occur in connection with my participation in the Competition;

4. Unconditionally release and forever discharge the Released Parties from any and all Losses that I may have and for any and all Losses sustained by me and my property arising from my participation in the Competition;

5. Waive any and all right or claim for Losses I may have against the Released Parties for any and all Losses I may suffer in connection with my participation in the Competition;

6. Covenant not to sue the Released Parties, or attach or otherwise encumber any property of any Released Party, for any Losses on account of injury to myself, damage to my personal property, or my death arising from my participation in the Competition, or for any other Losses whatsoever; and

7. Acknowledge and agree to all other terms and conditions in the Team Waiver and Release, including the waiver of Section 1542 of the California Civil Code.

In addition to the general release and waiver provided above, Team Member acknowledges that Team Member may be exposed to certain "Confidential Information" (as defined in Section 11 above of the Agreement) during the course of participating in the Competition. Participant hereby agrees to: (i) hold all Confidential Information in confidence, use it only to perform Team Member's duties under the Agreement, and not disclose the Confidential Information to any third party except to the extent permitted by the terms of the Agreement; and (ii) not remove or permit to be removed from any item any proprietary, confidential, or copyright notices, markings, or legends placed thereon by Team or XPRIZE. Team Member further acknowledges that any breach or violation of these confidentiality provisions will result in irreparable and continued damage to XPRIZE, and its affiliates, Competition sponsors, administrators and Award fulfillment partners for which there may be no adequate remedy at law. Participant hereby agrees that in the event of any such breach or violation, the injured Party will be entitled to both damages and injunctive relief.

Team Member has read and understood the above and foregoing Team Member Release, Waiver and Confidentiality Agreement and hereby voluntarily agrees to be bound by and comply with its terms and conditions and the terms and conditions of the Agreement.

Team Name: FloodLAMP
Team Member Name: Randy True
Team Member Signature: DocuSigned by Randy True (8AEA81FF0C4440E...)
Date of Signature: 9/8/2020


# 2,333  XPrize Legal - Registration Fee (certificate summary).md
METADATA
last updated: 2026-02-25 BA
file_name: XPrize Legal - Registration Fee (certificate summary).md
file_date: 2020-09-08
title: XPRIZE Registration Fee - DocuSign Certificate of Completion (FloodLAMP)
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/12lmH7kzDPyaIqi88xlP8KaXgqdAWJd_F/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20Legal%20-%20Registration%20Fee%20(certificate%20summary).pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 2333
words: 1673
notes:
summary_short: DocuSign Certificate of Completion for FloodLAMP's XPRIZE Rapid Covid Testing registration fee payment, showing that Randy True completed the 1-page document and paid via Stripe credit card on September 8, 2020. Includes the standard Electronic Record and Signature Disclosure.


CONTENT

## Certificate Of Completion
Envelope Id: B60F97D5848B4D0784C0E9A246094676
Status: Completed
Subject: Please DocuSign: XPRIZE Rapid COVID Testing Registration Fee
Source Envelope:
Document Pages: 1
Signatures: 0
Certificate Pages: 4
Initials: 0
AutoNav: Enabled
Payments: 1
EnvelopeId Stamping: Enabled
Time Zone: (UTC-08:00) Pacific Time (US & Canada)
Envelope Originator: XPRIZE Foundation, 800 Corporate Pointe, Suite 350, Culver City, CA 90230
skipso.docusign@xprize.org
IP Address: 104.40.24.165

## Record Tracking
Status: Original
9/8/2020 3:13:59 AM
Holder: XPRIZE Foundation, skipso.docusign@xprize.org
Location: DocuSign

## Signer Events
Randy True
randy@floodlamp.bio
Signature: **Completed**
Security Level: .Email
ID: 8a7f4536-e943-4868-9668-08b52bc7a629
9/8/2020 3:14:00 AM
Using IP Address: 73.93.172.149
Sent: 9/8/2020 3:14:00 AM
Viewed: 9/8/2020 3:14:07 AM
Signed: 9/8/2020 3:15:11 AM

## Electronic Record and Signature Disclosure:
Accepted: 9/7/2020 2:07:08 PM
ID: d237fe09-1ff3-446e-91be-014488db3be7

|  |  |  |
|---|---|---|
| In Person Signer Events | Signature | Timestamp |
| Editor Delivery Events | Status | Timestamp |
| Agent Delivery Events | Status | Timestamp |
| Intermediary Delivery Events | Status | Timestamp |
| Certified Delivery Events | Status | Timestamp |
| Carbon Copy Events | Status | Timestamp |
| Witness Events | Signature | Timestamp |
| Notary Events | Signature | Timestamp |
| Envelope Summary Events | Status | Timestamps |
| Envelope Sent | Hashed/Encrypted | 9/8/2020 3:14:00 AM |
| Certified Delivered | Security Checked | 9/8/2020 3:14:07 AM |
| Signing Complete | Security Checked | 9/8/2020 3:15:11 AM |
| Completed | Security Checked | 9/8/2020 3:15:11 AM |
| Payment Events | Status | Timestamps |
| Randy True, randy@floodlamp.bio, Payment Method: Credit Card, Payment Gateway: Stripe | **PAID**, Using IP Address: 73.93.172.149 | Authorized: 9/8/2020 3:15:11 AM, Paid: 9/8/2020 3:15:11 AM |
| Electronic Record and Signature Disclosure | | |
||

## ELECTRONIC RECORD AND SIGNATURE DISCLOSURE
From time to time, X PRIZE Foundation - Envelope (we, us or Company) may be required by law to provide to you certain written notices or disclosures. Described below are the terms and conditions for providing to you such notices and disclosures electronically through your DocuSign, Inc. (DocuSign) Express user account. Please read the information below carefully and thoroughly, and if you can access this information electronically to your satisfaction and agree to these terms and conditions, please confirm your agreement by clicking the 'I agree' button at the bottom of this document.

### Getting paper copies
At any time, you may request from us a paper copy of any record provided or made available electronically to you by us. For such copies, as long as you are an authorized user of the DocuSign system you will have the ability to download and print any documents we send to you through your DocuSign user account for a limited period of time (usually 30 days) after such documents are first sent to you. After such time, if you wish for us to send you paper copies of any such documents from our office to you, you will be charged a $0.00 per-page fee. You may request delivery of such paper copies from us by following the procedure described below.

### Withdrawing your consent
If you decide to receive notices and disclosures from us electronically, you may at any time change your mind and tell us that thereafter you want to receive required notices and disclosures only in paper format. How you must inform us of your decision to receive future notices and disclosure in paper format and withdraw your consent to receive notices and disclosures electronically is described below.

### Consequences of changing your mind
If you elect to receive required notices and disclosures only in paper format, it will slow the speed at which we can complete certain steps in transactions with you and delivering services to you because we will need first to send the required notices or disclosures to you in paper format, and then wait until we receive back from you your acknowledgment of your receipt of such paper notices or disclosures. To indicate to us that you are changing your mind, you must withdraw your consent using the DocuSign 'Withdraw Consent' form on the signing page of your DocuSign account. This will indicate to us that you have withdrawn your consent to receive required notices and disclosures electronically from us and you will no longer be able to use your DocuSign Express user account to receive required notices and consents electronically from us or to sign electronically documents from us.

### All notices and disclosures will be sent to you electronically
Unless you tell us otherwise in accordance with the procedures described herein, we will provide electronically to you through your DocuSign user account all required notices, disclosures, authorizations, acknowledgements, and other documents that are required to be provided or made available to you during the course of our relationship with you. To reduce the chance of you inadvertently not receiving any notice or disclosure, we prefer to provide all of the required notices and disclosures to you by the same method and to the same address that you have given us. Thus, you can receive all the disclosures and notices electronically or in paper format through the paper mail delivery system. If you do not agree with this process, please let us know as described below. Please also see the paragraph immediately above that describes the consequences of your electing not to receive delivery of the notices and disclosures electronically from us.

Electronic Record and Signature Disclosure created on: 7/13/2015 11:37:56 AM
Parties agreed to: Randy True

### How to contact X PRIZE Foundation - Envelope
You may contact us to let us know of your changes as to how we may contact you electronically, to request paper copies of certain information from us, and to withdraw your prior consent to receive notices and disclosures electronically as follows:

To contact us by email send messages to: ap@xprize.org

### To advise X PRIZE Foundation - Envelope of your new e-mail address
To let us know of a change in your e-mail address where we should send notices and disclosures electronically to you, you must send an email message to us at ap@xprize.org and in the body of such request you must state: your previous e-mail address, your new e-mail address. We do not require any other information from you to change your email address.

In addition, you must notify DocuSign, Inc to arrange for your new email address to be reflected in your DocuSign account by following the process for changing e-mail in DocuSign.

### To request paper copies from X PRIZE Foundation - Envelope
To request delivery from us of paper copies of the notices and disclosures previously provided by us to you electronically, you must send us an e-mail to ap@xprize.org and in the body of such request you must state your e-mail address, full name, US Postal address, and telephone number. We will bill you for any fees at that time, if any.

### To withdraw your consent with X PRIZE Foundation - Envelope
To inform us that you no longer want to receive future notices and disclosures in electronic format you may:

i. decline to sign a document from within your DocuSign account, and on the subsequent page, select the check-box indicating you wish to withdraw your consent, or you may;
ii. send us an e-mail to ap@xprize.org and in the body of such request you must state your e-mail, full name, US Postal Address, telephone number, and account number. We do not need any other information from you to withdraw consent. The consequences of your withdrawing consent for online documents will be that transactions may take a longer time to process.

### Required hardware and software
|  |  |
| --- | --- |
| Operating Systems | Windows 2000 or Windows XP |
| Browsers (for SENDERS) | Internet Explorer 6.0 or above |
| Browsers (for SIGNERS) | Internet Explorer 6.0, Mozilla FireFox 1.0, NetScape 7.2 (or above) |
| Email | Access to a valid email account |
| Screen Resolution | 800 x 600 minimum |
| Enabled Security Settings | Allow per session cookies; Users accessing the internet behind a Proxy Server must enable HTTP 1.1 settings via proxy connection |
||

** These minimum requirements are subject to change. If these requirements change, we will provide you with an email message at the email address we have on file for you at that time providing you with the revised hardware and software requirements, at which time you will have the right to withdraw your consent.

### Acknowledging your access and consent to receive materials electronically
To confirm to us that you can access this information electronically, which will be similar to other electronic notices and disclosures that we will provide to you, please verify that you were able to read this electronic disclosure and that you also were able to print on paper or electronically save this page for your future reference and access or that you were able to e-mail this disclosure and consent to an address where you will be able to print on paper or save it for your future reference and access. Further, if you consent to receiving notices and disclosures exclusively in electronic format on the terms and conditions described above, please let us know by clicking the 'I agree' button below.

By checking the 'I Agree' box, I confirm that:

- I can access and read this Electronic CONSENT TO ELECTRONIC RECEIPT OF ELECTRONIC RECORD AND SIGNATURE DISCLOSURES document; and
- I can print on paper the disclosure or save or send the disclosure to a place where I can print it, for future reference and access; and
- Until or unless I notify X PRIZE Foundation - Envelope as described above, I consent to receive from exclusively through electronic means all notices, disclosures, authorizations, acknowledgements, and other documents that are required to be provided or made available to me by X PRIZE Foundation - Envelope during the course of my relationship with you.


# 3,260  XPrize Legal - Release, Waiver, and Confidentiality Agreement (Team Member).md
METADATA
last updated: 2026-02-25 BA
file_name: XPrize Legal - Release, Waiver, and Confidentiality Agreement (Team Member).md
file_date: 2020-09-08
title: XPRIZE Competitor Agreement Exhibit E - Team Member Release, Waiver and Confidentiality Agreement (FloodLAMP)
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1k4YGkqhOnC8dX3jlh_kqcDtSqmM3owFX/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20Legal%20-%20Release%2C%20Waiver%2C%20and%20Confidentiality%20Agreement%20(Team%20Member).pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 3260
words: 2632
notes: 
summary_short: Exhibit E of the XPRIZE Rapid Covid Testing Competitor Agreement, the Team Member Release, Waiver and Confidentiality Agreement that each FloodLAMP team member was required to sign. The document includes seven key provisions covering confidentiality obligations, risk acknowledgment, unconditional release of XPRIZE and affiliated parties, and waiver of California Civil Code Section 1542. Signed copies include Antanas Sadunas (September 8, 2020).


CONTENT

## EXHIBIT E - Team Member Release, Waiver and Confidentiality Agreement

This Team Member Release, Waiver, and Confidentiality Agreement is made pursuant to that certain Competitor Agreement ("Agreement"). I represent and warrant that I have reviewed the Agreement to which this Team Member Release, Waiver and Confidentiality Agreement is attached as Exhibit E, and I hereby agree to be bound by, and comply with, the terms and conditions of the Agreement.

FOR AND IN CONSIDERATION and as a condition of the granting of permission and authority for the undersigned to participate as a Team Member of the Team specified below ("Team") in the Competition, the Team Member specified below ("Team Member"), does hereby release, acquit, and discharge the Released Parties (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) from any and all Losses (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) now accrued or hereafter to accrue on account of Team Member's participation in the Competition.

I Team Member, hereby for myself, my heirs, executors, and administrators:

1. Recognize and acknowledge that, as a Team Member, I am bound by the terms and conditions of Section 11 of the Agreement (Confidentiality) and covenant to comply with the terms and conditions thereof;

2. Understand and acknowledge that my participation in the Competition may be dangerous and could lead to serious injury or death;

3. Voluntarily assume any and all risks associated with participating in the Competition, and understand, acknowledge, and agree that the Released Parties will not be responsible or liable for any Losses that may occur in connection with my participation in the Competition;

4. Unconditionally release and forever discharge the Released Parties from any and all Losses that I may have and for any and all Losses sustained by me and my property arising from my participation in the Competition;

5. Waive any and all right or claim for Losses I may have against the Released Parties for any and all Losses I may suffer in connection with my participation in the Competition;

6. Covenant not to sue the Released Parties, or attach or otherwise encumber any property of any Released Party, for any Losses on account of injury to myself, damage to my personal property, or my death arising from my participation in the Competition, or for any other Losses whatsoever; and

7. Acknowledge and agree to all other terms and conditions in the Team Waiver and Release, including the waiver of Section 1542 of the California Civil Code.

In addition to the general release and waiver provided above, Team Member acknowledges that Team Member may be exposed to certain "Confidential Information" (as defined in Section 11 above of the Agreement) during the course of participating in the Competition. Participant hereby agrees to: (i) hold all Confidential Information in confidence, use it only to perform Team Member's duties under the Agreement, and not disclose the Confidential Information to any third party except to the extent permitted by the terms of the Agreement; and (ii) not remove or permit to be removed from any item any proprietary, confidential, or copyright notices, markings, or legends placed thereon by Team or XPRIZE. Team Member further acknowledges that any breach or violation of these confidentiality provisions will result in irreparable and continued damage to XPRIZE, and its affiliates, Competition sponsors, administrators and Award fulfillment partners for which there may be no adequate remedy at law. Participant hereby agrees that in the event of any such breach or violation, the injured Party will be entitled to both damages and injunctive relief.

Team Member has read and understood the above and foregoing Team Member Release, Waiver and Confidentiality Agreement and hereby voluntarily agrees to be bound by and comply with its terms and conditions and the terms and conditions of the Agreement.

Team Name: 
Team Member Name: 
Team Member Signature: 
Date of Signature: 

## EXHIBIT E - Team Member Release, Waiver and Confidentiality Agreement

This Team Member Release, Waiver, and Confidentiality Agreement is made pursuant to that certain Competitor Agreement ("Agreement"). I represent and warrant that I have reviewed the Agreement to which this Team Member Release, Waiver and Confidentiality Agreement is attached as Exhibit E, and I hereby agree to be bound by, and comply with, the terms and conditions of the Agreement.

FOR AND IN CONSIDERATION and as a condition of the granting of permission and authority for the undersigned to participate as a Team Member of the Team specified below ("Team") in the Competition, the Team Member specified below ("Team Member"), does hereby release, acquit, and discharge the Released Parties (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) from any and all Losses (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) now accrued or hereafter to accrue on account of Team Member's participation in the Competition.

I Team Member, hereby for myself, my heirs, executors, and administrators:

1. Recognize and acknowledge that, as a Team Member, I am bound by the terms and conditions of Section 11 of the Agreement (Confidentiality) and covenant to comply with the terms and conditions thereof;

2. Understand and acknowledge that my participation in the Competition may be dangerous and could lead to serious injury or death;

3. Voluntarily assume any and all risks associated with participating in the Competition, and understand, acknowledge, and agree that the Released Parties will not be responsible or liable for any Losses that may occur in connection with my participation in the Competition;

4. Unconditionally release and forever discharge the Released Parties from any and all Losses that I may have and for any and all Losses sustained by me and my property arising from my participation in the Competition;

5. Waive any and all right or claim for Losses I may have against the Released Parties for any and all Losses I may suffer in connection with my participation in the Competition;

6. Covenant not to sue the Released Parties, or attach or otherwise encumber any property of any Released Party, for any Losses on account of injury to myself, damage to my personal property, or my death arising from my participation in the Competition, or for any other Losses whatsoever; and

7. Acknowledge and agree to all other terms and conditions in the Team Waiver and Release, including the waiver of Section 1542 of the California Civil Code.

In addition to the general release and waiver provided above, Team Member acknowledges that Team Member may be exposed to certain "Confidential Information" (as defined in Section 11 above of the Agreement) during the course of participating in the Competition. Participant hereby agrees to: (i) hold all Confidential Information in confidence, use it only to perform Team Member's duties under the Agreement, and not disclose the Confidential Information to any third party except to the extent permitted by the terms of the Agreement; and (ii) not remove or permit to be removed from any item any proprietary, confidential, or copyright notices, markings, or legends placed thereon by Team or XPRIZE. Team Member further acknowledges that any breach or violation of these confidentiality provisions will result in irreparable and continued damage to XPRIZE, and its affiliates, Competition sponsors, administrators and Award fulfillment partners for which there may be no adequate remedy at law. Participant hereby agrees that in the event of any such breach or violation, the injured Party will be entitled to both damages and injunctive relief.

Team Member has read and understood the above and foregoing Team Member Release, Waiver and Confidentiality Agreement and hereby voluntarily agrees to be bound by and comply with its terms and conditions and the terms and conditions of the Agreement.

Team Name: FloodLAMP
Team Member Name: Antanas Sadunas
Team Member Signature: _Signature_ Verified by PDFfiller
Date of Signature: 09/08/2020

## EXHIBIT E - Team Member Release, Waiver and Confidentiality Agreement

This Team Member Release, Waiver, and Confidentiality Agreement is made pursuant to that certain Competitor Agreement ("Agreement"). I represent and warrant that I have reviewed the Agreement to which this Team Member Release, Waiver and Confidentiality Agreement is attached as Exhibit E, and I hereby agree to be bound by, and comply with, the terms and conditions of the Agreement.

FOR AND IN CONSIDERATION and as a condition of the granting of permission and authority for the undersigned to participate as a Team Member of the Team specified below ("Team") in the Competition, the Team Member specified below ("Team Member"), does hereby release, acquit, and discharge the Released Parties (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) from any and all Losses (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) now accrued or hereafter to accrue on account of Team Member's participation in the Competition.

I Team Member, hereby for myself, my heirs, executors, and administrators:

1. Recognize and acknowledge that, as a Team Member, I am bound by the terms and conditions of Section 11 of the Agreement (Confidentiality) and covenant to comply with the terms and conditions thereof;

2. Understand and acknowledge that my participation in the Competition may be dangerous and could lead to serious injury or death;

3. Voluntarily assume any and all risks associated with participating in the Competition, and understand, acknowledge, and agree that the Released Parties will not be responsible or liable for any Losses that may occur in connection with my participation in the Competition;

4. Unconditionally release and forever discharge the Released Parties from any and all Losses that I may have and for any and all Losses sustained by me and my property arising from my participation in the Competition;

5. Waive any and all right or claim for Losses I may have against the Released Parties for any and all Losses I may suffer in connection with my participation in the Competition;

6. Covenant not to sue the Released Parties, or attach or otherwise encumber any property of any Released Party, for any Losses on account of injury to myself, damage to my personal property, or my death arising from my participation in the Competition, or for any other Losses whatsoever; and

7. Acknowledge and agree to all other terms and conditions in the Team Waiver and Release, including the waiver of Section 1542 of the California Civil Code.

In addition to the general release and waiver provided above, Team Member acknowledges that Team Member may be exposed to certain "Confidential Information" (as defined in Section 11 above of the Agreement) during the course of participating in the Competition. Participant hereby agrees to: (i) hold all Confidential Information in confidence, use it only to perform Team Member's duties under the Agreement, and not disclose the Confidential Information to any third party except to the extent permitted by the terms of the Agreement; and (ii) not remove or permit to be removed from any item any proprietary, confidential, or copyright notices, markings, or legends placed thereon by Team or XPRIZE. Team Member further acknowledges that any breach or violation of these confidentiality provisions will result in irreparable and continued damage to XPRIZE, and its affiliates, Competition sponsors, administrators and Award fulfillment partners for which there may be no adequate remedy at law. Participant hereby agrees that in the event of any such breach or violation, the injured Party will be entitled to both damages and injunctive relief.

Team Member has read and understood the above and foregoing Team Member Release, Waiver and Confidentiality Agreement and hereby voluntarily agrees to be bound by and comply with its terms and conditions and the terms and conditions of the Agreement.

Team Name: FloodLAMP
Team Member Name: Carey Tan
Team Member Signature: _Signature_
Date of Signature: Sept. 8, 2020

## EXHIBIT E - Team Member Release, Waiver and Confidentiality Agreement

This Team Member Release, Waiver, and Confidentiality Agreement is made pursuant to that certain Competitor Agreement ("Agreement"). I represent and warrant that I have reviewed the Agreement to which this Team Member Release, Waiver and Confidentiality Agreement is attached as Exhibit E, and I hereby agree to be bound by, and comply with, the terms and conditions of the Agreement.

FOR AND IN CONSIDERATION and as a condition of the granting of permission and authority for the undersigned to participate as a Team Member of the Team specified below ("Team") in the Competition, the Team Member specified below ("Team Member"), does hereby release, acquit, and discharge the Released Parties (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) from any and all Losses (as defined in the Team Release and Waiver, attached to the Agreement as Exhibit E) now accrued or hereafter to accrue on account of Team Member's participation in the Competition.

I Team Member, hereby for myself, my heirs, executors, and administrators:

1. Recognize and acknowledge that, as a Team Member, I am bound by the terms and conditions of Section 11 of the Agreement (Confidentiality) and covenant to comply with the terms and conditions thereof;

2. Understand and acknowledge that my participation in the Competition may be dangerous and could lead to serious injury or death;

3. Voluntarily assume any and all risks associated with participating in the Competition, and understand, acknowledge, and agree that the Released Parties will not be responsible or liable for any Losses that may occur in connection with my participation in the Competition;

4. Unconditionally release and forever discharge the Released Parties from any and all Losses that I may have and for any and all Losses sustained by me and my property arising from my participation in the Competition;

5. Waive any and all right or claim for Losses I may have against the Released Parties for any and all Losses I may suffer in connection with my participation in the Competition;

6. Covenant not to sue the Released Parties, or attach or otherwise encumber any property of any Released Party, for any Losses on account of injury to myself, damage to my personal property, or my death arising from my participation in the Competition, or for any other Losses whatsoever; and

7. Acknowledge and agree to all other terms and conditions in the Team Waiver and Release, including the waiver of Section 1542 of the California Civil Code.

In addition to the general release and waiver provided above, Team Member acknowledges that Team Member may be exposed to certain "Confidential Information" (as defined in Section 11 above of the Agreement) during the course of participating in the Competition. Participant hereby agrees to: (i) hold all Confidential Information in confidence, use it only to perform Team Member's duties under the Agreement, and not disclose the Confidential Information to any third party except to the extent permitted by the terms of the Agreement; and (ii) not remove or permit to be removed from any item any proprietary, confidential, or copyright notices, markings, or legends placed thereon by Team or XPRIZE. Team Member further acknowledges that any breach or violation of these confidentiality provisions will result in irreparable and continued damage to XPRIZE, and its affiliates, Competition sponsors, administrators and Award fulfillment partners for which there may be no adequate remedy at law. Participant hereby agrees that in the event of any such breach or violation, the injured Party will be entitled to both damages and injunctive relief.

Team Member has read and understood the above and foregoing Team Member Release, Waiver and Confidentiality Agreement and hereby voluntarily agrees to be bound by and comply with its terms and conditions and the terms and conditions of the Agreement.

Team Name: FloodLAMP
Team Member Name: Samantha Fogelberg
Team Member Signature: _Signature_
Date of Signature: 09-08-2020

# ===== END OF FILE _archive-combined-files_xprize_81k.md =====
