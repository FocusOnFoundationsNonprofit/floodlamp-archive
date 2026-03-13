METADATA
last updated: 2026-02-24 AI and RT
file_name: _AI_gLAMP and XPrize - pre-competitive vs open-source.md
file_date: 2026-03-03
title: FloodLAMP Global LAMP Consortium (gLAMP) - Pre-Competitive vs Open Source Approaches
category: various
subcategory: xprize
tags: glamp, pre-competitive, open-source, pandemic-testing, public-goods
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1453cKnhM8CnfD95gOKvNS-qosJfenbaqR1sjGr2wvWk
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/various/glamp/_AI_Global%20LAMP%20Consortium%20%28gLAMP%29%20-%20pre-competitive%20vs%20open-source.md
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
