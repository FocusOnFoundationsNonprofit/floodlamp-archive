METADATA
last updated: 2026-03-17 RT
file_name: _context-commentary_various-glamp.md
category: various
subcategory: glamp
gfile_url: https://docs.google.com/document/d/1DHfsbDIRjxoKvbxcNJyowvYbBJhaS8dSfmc4A3iJ0hM
words: 1408
tokens: 2003


CONTENT

## Context
### The Global LAMP Consortium (gLAMP)
The Global LAMP Consortium, known as gLAMP, was convened by Chris Mason of Weill Cornell Medicine in April 2020 during the early months of the COVID-19 pandemic. It was an international, pre-competitive forum bringing together scientists, engineers, physicians, educators, government officials, and industry representatives to share protocols, methods, and operational experience related to loop-mediated isothermal amplification (LAMP) for SARS-CoV-2 detection. The consortium grew to over 300 members and met virtually on a weekly basis during the core pandemic period. Its infrastructure included a Google Group mailing list, a Slack workspace, a Zotero reference library, a GitBook documentation hub (docs.lamp.bio), and recurring calls for general discussion, writing coordination, and FDA town hall sessions. gLAMP was explicitly structured as a space for open exchange before commercialization, modeled on how NIST convenes standards groups, and participants shared not only successes but also failures, which were considered critical during a rapidly evolving pandemic. The consortium also maintained connections to related efforts including Just One Giant Lab (JOGL) and the COVID testing XPRIZE. For a fuller survey of gLAMP's public footprint, including citations, media coverage, and infrastructure links, see the companion file `_AI_Global LAMP Consortium (gLAMP) - Public Information Survey`.

### NEB Podcast Interview with Chris Mason (August 2020)
Mason, a researcher at Weill Cornell Medicine, discusses a broader set of LAMP-related activities including head-to-head comparisons of LAMP with RT-PCR and RNA sequencing on clinical samples from the first 735 COVID-positive patients at his hospital. He describes founding the gLAMP consortium, a pre-competitive forum for academic, industry, and nonprofit researchers to share protocols, methods, and failures on a weekly call with a Slack channel and Google group. Mason also discusses saliva-based testing as a more practical alternative to nasopharyngeal swabs for large-scale surveillance ("Saliva Is The Future"), metagenomics sampling of NYC subway stations and hospital surfaces, and the role of pre-print servers in accelerating pandemic science. He mentions Color Genomics scaling a LAMP protocol to over 10,000 samples per day in San Francisco with FDA EUA approval.

### gLAMP Consortium Review Paper (JBT, September 2021)
The major published output of the gLAMP consortium was a comprehensive review article in the *Journal of Biomolecular Techniques*: "Loop-Mediated Isothermal Amplification (LAMP) Detection of SARS-CoV-2 and Myriad Other Applications" (Moore et al., 2021). Led by Keith J. M. Moore of Ateneo de Manila University in the Philippines and co-first-authored with Jeremy Cahill, the paper lists over 50 co-authors representing the breadth of the consortium, including Randy True, founder of FloodLAMP Biotechnologies, Nathan Tanner of New England Biolabs, and Anne Wyllie, founder of SalivaDirect, formerly at the Yale School of Public Health. The review covers the full landscape of LAMP-based testing: pre-analytical sample processing, target amplification and primer design, amplicon detection chemistries, hardware and software for deployment, and the regulatory environment in both the U.S. and EU. It includes first-person case studies from consortium members and concludes with practical recommendations for building fit-for-purpose LAMP tests across a range of settings, from resource-limited environments to high-throughput clinical labs. The paper is openly available through PubMed Central and has been cited in subsequent literature as the comprehensive reference on RT-LAMP alternatives for SARS-CoV-2 detection.
The gLAMP review paper is available in a converted markdown version here in the archive as `gLAMP Global Consortium - JBT Review Paper (Sept 2021)`, along with two PDF versions: an early access pre-typeset version and the final published journal version.

### Archive Files Not Converted to Markdown
`gLAMP Global Consortium - JBT Review Paper (Sept 2021) - Journal version.pdf`
`gLAMP Paper Regulatory section (2021).docx`
`gLAMP Paper Regulatory section (2021).pdf`


## Commentary
See related archive files:
`various/xprize/_AI_Global LAMP Consortium (gLAMP) - pre-competitive vs open-source.md`
`various/xprize/_archive-combined-files_various-xprize.md`

### The Weekly Calls
FloodLAMP connected to the gLAMP consortium early in its development (May 2020), when the company was still a project within a nonprofit. The weekly call quickly became one of the most valuable hours of the week. The information density was consistently high, with presentations covering the latest LAMP research, troubleshooting from the field, and updates on screening program implementation and decentralized testing approaches.

The group was predominantly academic, with researchers in testing and diagnostics from institutions across the globe, but it also included participants from industry, startups, and larger companies. The University of Vienna group behind rtlamp.org was especially active and productive (see also the Kellner et al. references in the `various/papers-lamp` subcategory). JOGL (Just One Giant Lab), an open-science organization, was also a regular presence. There was significant overlap between gLAMP participants and the COVID testing XPRIZE competition (see `various/xprize`).

Through the gLAMP network, FloodLAMP's founder attempted to establish an Open EUA consortium, an effort to collectively develop and share the regulatory submissions needed for FDA authorization of LAMP-based tests. The idea gained some initial interest but did not sustain momentum (see `regulatory/open-euas` for documentation of that effort).

### gLAMP Central and the Review Paper
Beginning roughly in the fall of 2020 and continuing into 2021, a subset of gLAMP participants organized what became known as "gLAMP Central," an effort to distill the group's collective knowledge and best practices into a tangible output. There was early brainstorming about what form this could take. The effort ultimately produced the consortium's major published work: the JBT review paper, "Loop-Mediated Isothermal Amplification (LAMP) Detection of SARS-CoV-2 and Myriad Other Applications" (Moore et al., 2021).

Keith J. M. Moore of Ateneo de Manila University in the Philippines served as the primary coordinator. A core group of roughly five to ten people drove the effort. FloodLAMP's founder, Randy True, contributed to the drafting of the regulatory landscape section (Section 07 of the paper), alongside Anne Wyllie of SalivaDirect, Thomas Kunstman, and several others.

Supporting infrastructure was established through the gLAMP Hub, a GitBook documentation site at docs.lamp.bio with links to shared resources including a Google Drive folder, a Zotero reference library, a Slack workspace, and a Google Group mailing list. In practice, the Hub and its associated infrastructure did not see heavy ongoing use after the initial framework was set up. Details and links are documented in the companion file `_AI_Global LAMP Consortium (gLAMP) - Public Information Survey`.

### Open Protocols vs. the Paper
The review paper was a genuine accomplishment, a comprehensive and practical reference that continues to be cited in the literature. Given that the majority of gLAMP participants were academics, it is understandable that the group's central effort coalesced around a peer-reviewed publication.

That said, FloodLAMP had advocated for gLAMP Central to focus instead on the open development of one or a few consensus LAMP protocols, including the regulatory and FDA submission work needed to make them deployable. The model was something like what SalivaDirect achieved for saliva-based RT-PCR: an open, validated protocol with regulatory authorization that other labs could adopt. Applied to LAMP, such an effort could potentially have produced an open EUA backed by the collective validation data and technical expertise of the consortium's 300+ members.

This did not happen, for several reasons. Academic incentives favor publications, and coordinating a multi-institution regulatory submission is a fundamentally different kind of work than writing a review paper. The Open EUA Consortium effort that FloodLAMP pursued through the same network did not gain sufficient sustained commitment (see `regulatory/open-euas`). FloodLAMP's founder also did not push the consortium approach as hard as he might have, in part because he believed FloodLAMP could obtain its own open-source EUA for colorimetric LAMP — particularly after reviewing the DetectaChem EUA, which seemed to demonstrate a viable path. He did not fully appreciate at the time the challenges of the EUA process: the degree of FDA discretion and shifting prioritization, and especially the mass deprioritization mechanism that would ultimately revoke hundreds of EUAs simultaneously (see `regulatory/fl-fda-submissions` and `regulatory/fl-fda-correspondence`). In hindsight, the better path would have been to go all in on rallying a committed group within gLAMP to pursue an open-source colorimetric LAMP EUA. A consortium-backed submission, drawing on the technical expertise, institutional credibility, and regulatory connections, would have had a far better chance with the FDA than FloodLAMP as a tiny startup trying to do it alone.

Whether the gLAMP consortium represented a missed opportunity for open, collectively developed diagnostic infrastructure, or whether the review paper was the most realistic and valuable product the group could have produced, is a question worth considering. For future pandemic preparedness efforts, the tension between academic output and deployable infrastructure is one of the more consequential choices a consortium faces.
