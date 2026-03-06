METADATA
last updated: 2025-12-31 RT
file_name: Balvi Proposal 2 - FloodLAMP Open Source COVID Screening (Dec 2022 - 300K - Funded).md
file_date: 2022-12-06
title: Balvi Proposal 2 - FloodLAMP Open Source COVID Screening (Dec 2022 - 300K - Funded)
category: various
subcategory: fl-proposals
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1Me5Bteul_3m-gBd3auWEXsnicYbmhiJlZ5WBleMDUy0
xfile_github_download_url: 
pdf_gdrive_url: https://drive.google.com/file/d/1Q8PUaqxkrT6i0FXEipH-Cpo0J_FrE9MO
pdf_github_url:
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 5052
words: 2875
notes: has html table instead of pipe md for deliverables
summary_short: The December 6, 2022 Balvi proposal outlines FloodLAMP’s plan to scale open-source, decentralized infectious disease screening built around extraction-free LAMP testing, self-pooled swab collection, and supporting digital tools, emphasizing decentralization, low cost, and open-protocol regulatory pathways. It summarizes 11 pilot programs (including municipal EMS and school deployments) and requests Balvi funding to open source program materials, publish pilot data, and run clinical studies to support future FDA EUA submissions. It also provides company background, partnerships (notably NEB and SalivaDirect), an IP and licensing approach, and a brief Q&A on licensing intentions and expected funding decision timing.


CONTENT

***INTERNAL TITLE:*** FloodLAMP: open source decentralized infectious disease screening.

Balvi Proposal - December 6, 2022
FloodLAMP Biotechnologies, PBC
Randy True randy@floodlamp.bio

We think that the best, and perhaps only, way to have stopped the spread of the SARS-CoV-2 virus was with early, broad based testing. The U.S. and the other countries (with the exception of China) still lack the capability to carry out large scale disease screening. As a result, we remain vulnerable to variants and even more worrying, to new, more deadly pathogens. Mass testing should be a cornerstone of pandemic preparedness and response, but many complex, interconnected problems need to be overcome in order to achieve this important capability.

FloodLAMP Biotechnologies is a Public Benefit Corporation solely focused on solving these problems and helping to deliver universally accessible pandemic response screening. Our assumptions are:

1.  **Decentralization** is needed – the central lab model failed in the U.S. during the COVID-19 pandemic. Anyone or any organization needs to be able to purchase and run testing, with no or very streamlined oversight.

2.  **Isothermal molecular** will win – for mass testing programs over antigen, due to better accuracy and flexibility. Molecular is quicker to adapt to new targets and more efficient for groups running point-of-need testing. Isothermal (LAMP) has revolutionary potential but so far the commercial focus is on expensive, single use/one-at-a-time devices. Further developing LAMP modalities can unlock the entire space.

3.  **Cost** must be low – $5 or less per sample, ideally down to $1 (achievable now with self-pooling).

4.  **Open** is needed – the molecular diagnostics industry’s standard business model is siloed, proprietary technology and 80-90% margins. A new paradigm of “open source protocol” FDA approvals that fully disclose chemistry and primer sequences can have huge impact due to global regulatory harmonization.

5.  **Integrated innovation** is needed – achieving mass scale at low cost will require progress on policy, technology, programs, and business models – all planned and executed to work together.

Over the last year and a half, we have completed 11 pilot screening programs that are affordable, locally controlled, and can be scaled in a decentralized manner. We have considered not only assay chemistry but also operational configurations, enabling software, and regulatory pathways. The programs use what we consider to be the best current technology stack: isothermal molecular amplification ([<u>LAMP using NEB Master Mix</u>](https://www.neb.com/applications/dna-amplification-pcr-and-qpcr/isothermal-amplification/loop-mediated-isothermal-amplification-lamp)), extraction-free assay chemistry ([<u>Rabe-Cepko protocol</u>](https://www.pnas.org/doi/10.1073/pnas.2011221117)), and self-pooled swabs. In the majority of these pilots, we provided turn-key, in-house programs that included all of the physical materials, digital tools, training and support, with the partner organizations providing the space and staffing. The largest programs were ~1,000 person municipal workforces in two cities in Florida, run by the Emergency Medical Services departments. They scaled to thousands of samples per week during the Omicron surge, screening all first responders regularly. Both cities made our program mandatory despite having access to PCR testing services and practically unlimited antigen tests. We also have deployed successful school pilots that have used our novel at-home self-pooled sample collection, including Abrome in Austin, TX which received Balvi funding.

We are seeking funding from Balvi to publish our work, open source our current programs, and at the same time build the foundation for an enduring entity to help achieve universal access to disease testing, first for all known pandemic-threat pathogens, and then more broadly for improving global health. Key progress on the program and policy fronts can be made, especially with respect to open source FDA approvals and clarity on non-diagnostic testing regulations. On the technical front, our plans include developing a next generation rapid molecular OTC, POC/PON platform (for which we have filed IP and applied for [<u>RADx funding</u>](https://www.poctrn.org/web/radx-tech-high-performance-tests)). There is significant overlap between further developing our current platform and the next gen one, such as bridge assay development work. Please see our [<u>RADx submission</u>](https://docs.google.com/document/d/1FD3-N6AC2PQKKS_WpqtdQ1FnSvZAhJdyZrOcnaXb_AI) for details about this as well as information about our pilots, test performance, regulatory filings, and technology development plans.
_FLOODLAMP ARCHIVE FILE PATH:_ data/floodlamp/various/fl-proposals/RADx 2022 Submitted Proposal - FloodLAMP (Oct 2022 - 3M - Not Funded).md

The following is the set of deliverables we propose. The majority of these have a great deal of groundwork already laid and can proceed in parallel.


## Deliverables
<table style="width:100%;">
<colgroup>
<col style="width: 44%" />
<col style="width: 37%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th><strong>Deliverables</strong></th>
<th><strong>Impact</strong></th>
<th><p><strong>Estimated</strong></p>
<p><strong>Timeline</strong></p></th>
</tr>
<tr>
<th><p><u>1. Open source programs</u></p>
<blockquote>
<p>1A. Website openly disseminating all program information, guides, and supporting docs.</p>
<p>1B. Support for multiple profiles and scales.</p>
</blockquote></th>
<th><ul>
<li><p>Enablement of orgs seeking to bring up locally controlled testing.</p></li>
<li><p>Initiates broad-based feedback.</p></li>
<li><p>Demonstrates new open, cooperative approach.</p></li>
</ul></th>
<th><p>1A. 4-10 weeks</p>
<p>1B. 8 weeks (beta)</p></th>
</tr>
<tr>
<th><p><u>2. Publication</u></p>
<blockquote>
<p>2A. Publish data from 11 pilots programs using LAMP-based COVID surveillance.</p>
<p>2B. Preprint + submission to open access peer reviewed journal.</p>
<p>2C. Website update and outreach when preprint goes live.</p>
</blockquote></th>
<th><ul>
<li><p>Opens avenues to obtain help and further funding from PPR allies.</p></li>
<li><p>Gets attention of U.S. federal agencies (CDC, ASPR, NSC, OSTP).</p></li>
<li><p>Establishes company credibility.</p></li>
<li><p>PR opportunity.</p></li>
<li><p>Stimulates consideration of mass testing for PPR in the U.S.</p></li>
</ul></th>
<th>8 weeks</th>
</tr>
<tr>
<th><p><u>3. Clinical studies and FDA EUA submissions</u></p>
<blockquote>
<p>3A. Clinical studies to gather data needed to support FDA EUA submissions.</p>
</blockquote></th>
<th><ul>
<li><p>Key step to obtaining OS EUA, which</p>
<ul>
<li><p>establishes new OS paradigm for IVD diagnostics at FDA;</p></li>
<li><p>enables global dissemination.</p></li>
</ul></li>
<li><p>Proves out new powerful study design that combines non-dx, organization based screening.</p></li>
</ul></th>
<th>12 weeks</th>
</tr>
</thead>
<tbody>
</tbody>
</table>


## Budget
The budget below is a breakdown of spending to meet the proposed deliverables.

[<u>Balvi Proposal 2 - Budget</u>](https://docs.google.com/spreadsheets/d/1vcN4BmShRpY2CXkC9sAJxAGkqjc9My8eEk-Q5Q7dwZ0/edit?usp=drive_link)

### Budget Table 12-6

| A | B | C | D | E | F | G |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  |  |  |  |  |  |  |
|  | __$130,000__ | __Open Source Platform__ |  |  |  |  |
|  | $ 90,000 | OS Platform - new CYOA website |  |  |  |  |
|  | $ 25,000 | Legal IP - open license w commercial terms (app and test) |  |  |  |  |
|  | $ 15,000 | Comms - Publication, Outreach, Community, PR, Summit, Interview Series |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$100,000__ | __Clinical and Regulatory__ |  |  |  |  |
|  | $ 20,000 | 10K Test Kits for Clinical Studies w Surveillance ($2/kit for NEB MM) |  |  |  |  |
|  | $ 50,000 | Regulatory Consulting (Arete, SalivaDirect partnership) |  |  |  |  |
|  | $ 30,000 | Clinical Studies Site Bring Up & Maintenance |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$ 70,000__ | __Staff__ | 3 | heads |  |  |
|  | $ 60,000 | Employee Salaries  | 20,000 | salaries/mo | 3 | mo |
|  | $ 13,500 | Benefits and Taxes | 0.225 | overhead |  |  |
|  |  |  |  |  |  |  |
|  | ***$300,000*** | ***TOTAL PROPOSAL*** |  |  |  |  |


## FloodLAMP Company Information
FloodLAMP Biotechnologies was incorporated in Delaware on 8/3/2020 as a Public Benefit Corporation. Our charter states “the specific public benefit that the Corporation will promote is the development of open protocols and the implementation of large scale disease screening for infectious disease for the benefit of the public.”

We are currently 4 employees, 2 full time and 2 part time. Please see the last portion of our recent [<u>RADx funding submission</u>](https://docs.google.com/document/d/1dd6XmU5FCCjMfFILdclqgM5yZABerFXfbSB5iPNmSBw/edit?usp=sharing) for profiles of our team members. Here is a more detailed bio for our CEO and founder, Randy: [<u>Randall True Biosketch</u>](https://drive.google.com/file/d/1hgpfBA99cNOszNrRA9Ft4FFdxUyaAkWp/view?usp=share_link). He is a co-author on the [<u>global LAMP consortium review paper</u>](https://drive.google.com/file/d/1822shorursMdugM0lk6Xx4RbZpnQjot0) which appeared in a [<u>special issue of the Journal of Biomolecular Techniques</u>](https://abrf.memberclicks.net/jbt-2021-september-issue).
_FLOODLAMP ARCHIVE FILE PATH:_ various/glamp/gLAMP Global Consortium - JBT Review Paper (Sept 2021).md

Our facility is 2,200 sqft of joint lab and office space in Portola Valley, CA, 10 minutes from Stanford University.

FloodLAMP is majority self-funded, with $975K in SAFE’s ($500K founder, $475K angels) and a $500K founder loan, convertible to a SAFE. Our revenue to date is $234,352.


## Growth
This proposal for funding provides the resources needed to bring much of the work we’ve done during the pandemic to fruition. Many of these are significant accomplishments in their own right, yet they are also steps to building something much bigger and delivering globally impactful solutions in disease detection.

Regarding open EUAs, it should be noted that obtaining the EUAs cited in this proposal will likely require federal agency support due to FDA policy changes in 2021. We think that funding from Balvi, along with publication and outreach, will generate major momentum and galvanize our network, including foundations and NGOs active in pandemic response. We’re hopeful this will lead to support and potential funding from RADx or BARDA. The need for public-private partnerships in COVID/pandemic testing is often highlighted, and we agree. Our goal is to bring many resources to bear on the problem of pandemic testing and help provide efficient avenues to translating funding to actual capability. We are cautiously optimistic as initiatives such as the [<u>White House National Biodefense Plan</u>](https://www.whitehouse.gov/wp-content/uploads/2022/10/National-Biodefense-Strategy-and-Implementation-Plan-Final.pdf) and [<u>World Bank Pandemic Fund</u>](https://www.worldbank.org/en/programs/financial-intermediary-fund-for-pandemic-prevention-preparedness-and-response-ppr-fif) spin up. As was the case during the pandemic, these “plans” are very light on details. We see potential for FloodLAMP to garner attention as we are offering real solutions, both at the level of technology and programs, as well as the systemic/policy level. Publishing our work soon will be key to getting involved with these larger pandemic preparedness and response efforts.

Our IP offers the potential for growth through licensing and partnerships. Our [<u>first patent application</u>](https://drive.google.com/file/d/19qoJLj-dDQs0_ksksWlYg-l-eEssrmyX/view?usp=drive_link) 
_FLOODLAMP ARCHIVE FILE PATH:_ various/fl-patent/FloodLAMP Patent Application - US20240139745A1 - from Google Patents.md
has been published and has broad coverage of inventions related to on-the-fly (outside the lab) pooled sample collection. We filed this patent as a PCT and received a favorable written opinion from the US patent office, which granted us expedited examination for our regular US patent application. We have filed an additional provisional patent application covering other program related inventions and a 161 page provisional on the next generation platform. Given our open source approach and public benefit mission, we have carefully considered options around IP issues. We included as a deliverable the execution of standard licenses to open up access to our IP while maintaining the option to share in profits with better resourced commercial partners. We will consider non-commercial end-use royalty free licenses and open sourcing the code for our new web app. We do think licensing and IP need to be a core competency of the company, as we see a big opportunity to license test IP from universities and offer a commercialization model that maximizes impact while maintaining a modest royalty structure.

Momentum gained from Balvi funding will allow us to fully capitalize on the many relationships we have developed over the course of our work. In particular, we have developed a good relationship with [<u>New England Biolabs</u>](https://www.neb.com/), the largest manufacturer of enzymes for molecular biology in the world. NEB is a critical global supplier for biosecurity and an outlier in the industry, being so large yet still privately held. They were officially certified as a B corp and actively work globally on mission-driven programs and technology transfer. They have donated reagents for several FloodLAMP pilots and collaborations, both in the U.S. and in Colombia and Brazil. NEB is the recognized leader in LAMP, and while we do plan to diversify and validate our test with other LAMP master mixes (several companies such as Thermo and Meridian have commercialized products during the pandemic), NEB has important IP on the inclusion of thermolabile nucleotides into LAMP amplification. This greatly reduces the impact of any amplicon contamination and we believe is a key enabler for the decentralization of LAMP based testing. In addition they acquired the top lyophilization company, Fluorogenics, last year and so have key expertise and technology for OTC/POC LAMP based devices, such as our next generation platform.

FloodLAMP was invited to the NEB campus in Massachusetts in March of this year and gave a talk on FloodLAMP’s work to the company. We have had multiple meetings with senior management and they have expressed a deep interest in our mission and goals. NEB has provided a [<u>letter of support</u>](https://drive.google.com/file/d/1IPgF-HJRjP2sd0NX_MOf1pSXo2bHeUGO/view?usp=share_link) for grant applications to BARDA. Balvi funding will lay the groundwork to progress our relationship with NEB, with future areas of work including technical development, commercialization of inexpensive LAMP test kits, and potentially collaboration on regulatory authorizations through the WHO.

Another key collaborator is [<u>Anne Wyllie</u>](https://ysph.yale.edu/profile/anne-wyllie/), a researcher at the Yale School of Public Health, founder of [<u>SalivaDirect</u>](https://salivadirectinc.org/), and a member of our Scientific Advisory Board. Balvi funding will allow us to work with her and the SalivaDirect team on open source protocol FDA approvals. It was through Anne that we learned about this important regulatory development in the fall of 2020. Anne is a force of nature and deeply committed to openness (see [<u>Anne Wyllie Nomination for FDA Foundation 2022 Innovations in Regulatory Science Awards</u>](https://docs.google.com/document/d/16muU80i9sAFPsCQNosyrK6ZYJqMPxf0gSqZcsudqYZM/edit?usp=drive_link) for more details).
_FLOODLAMP ARCHIVE FILE PATH:_ regulatory/open-euas/Anne Wyllie Nomination for FDA Foundation 2022 Innovations in Regulatory Science Awards.md

She shared her full EUA submission with us as we were working on our EUAs and fielded many questions. Anne also shared legal agreements for labs and states and joined our call with FDA reviewers in October of 2021. Over the last 2 years she has led more than 20 amendments to the SalivaDirect EUA and formed key industry partnerships. Her experience would be tremendously helpful for our regulatory efforts, and formally partnering with SalivaDirect could lead to sustained engagement with the FDA prior to BARDA/RADx funding. We’ve included a line item in our budget for consulting fees for SalivaDirect, which is in the process of spinning out from Yale to form a non-profit. They would be a great organization for Balvi to consider funding.

FloodLAMP was spun out from a 501(c)3 STEM education non-profit. Operating at the intersection of for-profit and non-profit has been challenging, and we are eager to legally codify our public benefit commitments. A potential scenario that looks promising is forming a DAO. FloodLAMP could stay a PBC or transition to a non-profit, and be governed by the DAO. We have no experience in DAOs, blockchain, or web3, though we do have close contacts with experience. A DAO could align the incentives of a range of people and organizations around the focused mission of universal pandemic testing. Some specific aspects of the space and our goals that may make a DOA structure a good fit are:

- enabling the grass roots pull of testing programs into communities or countries by organizing local support and labor, applying specific geographic and technical knowledge, matching with funding, and facilitating the needed physical and digital resources;
- using the Rights of Reference (ROR) sharing mechanisms for regulatory validation data to expedite and lower the costs for test approvals - ROR are very powerful and seldom used - for more info [<u>see Randy’s discussion on the this with the FDA</u>](https://docs.google.com/document/d/1jZzEumjRYUOK31Cz-sUQkfONjqOja1f_YqPcNduwHA8/edit?usp=sharing);
_FLOODLAMP ARCHIVE FILE PATH:_ regulatory/fl-fda-correspondence/2020-12-09_FloodLAMP FDA Townhall Engagement on Open Source FDA IVD EUAs and Generic Molecular Tests.md
- drawing on the expertise of many scientists in making key decisions about what tests to invest in for regulatory approvals and manufacturing scale up – this could create an influential new voice in the space, but notably one that is executing rather than only advocating;
- automatically distributing resources (via smart contracts) when triggering events occur or governing decisions are made, speeding response in an emergency.

Perhaps most important, the transparency in activities and governance of a DAO, could build much needed trust. Most of this could be accomplished within a standard organizational structure as well, however a DAO could potentially be more impactful.

Linked documents and a few others, including our FDA submissions, are in this openly shared google drive folder:

FloodLAMP FDA and Regulatory Documents (link replaced with FloodLAMP Archive Folder[<u>Regulatory</u>](https://drive.google.com/drive/folders/1fI06ZIDsGmi5pdxFSrsMEoSDPEzxNW3x?usp=drive_link)

[<u>FloodLAMP - COVID-19 Tests Summary.pdf</u>](https://drive.google.com/file/d/1Y8Q09VdMMTB1PnBQv2xJuvRAuvq8yv1-/view?usp=drive_link)

[<u>FDA Reagan Udall Foundation - FloodLAMP Presentation (4-21-2022)</u>](https://docs.google.com/presentation/d/1y_Svu_c7pa4QZUijkVRCnFmND6Sy5L7LI0LzldVH4A8/edit?usp=drive_link)

[<u>FloodLAMP Whitepaper - California Preschool Family Pooled Screening Pilot (June 2022)</u>](https://docs.google.com/document/d/1TOnklq-65XUX-v-li018rteK9jeL8NgqbNrtbndgD_o/edit?usp=drive_link)

We look forward to your feedback and questions!


## Q&A
*Tas D.: How would the test be licensed? Would you be willing to open source it within some parameters?*

Randy True: Yes, absolutely. We are intending to open up access to this and our other IP, probably through non-exclusive commercial licenses. We included this as a deliverable (6A). We've done some of the legal groundwork for this with a licensing attorney and the Harvard office of technology licensing, around the Rabe Cepko LAMP test IP. The IP for the next gen platform has a different profile that our current tests (Rabe Cepko) because it's a device rather than a liquid phase test. For liquid phase tests, we have the open source protocol FDA pathway.

*Tas D.: When do you expect a decision about this?*

Hopefully by mid December. I'm planning to reach out to a contact who is a program manager at RADx next week to try and learn more about the process.
