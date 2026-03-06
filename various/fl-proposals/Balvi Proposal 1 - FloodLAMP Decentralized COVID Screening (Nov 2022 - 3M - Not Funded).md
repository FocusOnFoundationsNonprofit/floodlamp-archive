METADATA
last updated: 2025-12-31 RT
file_name: Balvi Proposal 1 - FloodLAMP Decentralized COVID Screening (Nov 2022 - 3M - Not Funded).md
file_date: 2022-11-19
title: Balvi Proposal 1 - FloodLAMP Decentralized COVID Screening (Nov 2022 - 3M - Not Funded)
category: various
subcategory: fl-proposals
tags:
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/10k0xqcAJwCBVtxANZmFkHGydyyYk7hHn-lTjPRecx7E
xfile_github_download_url: 
pdf_gdrive_url: https://drive.google.com/file/d/1tc0rUxp1KJZQjBn4wV-9h14P9dXoeufL/view?usp=drive_link
pdf_github_url:
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 5915
words: 3256
notes: has html table instead of pipe md for deliverables
summary_short: The FloodLAMP Balvi Proposal (Balvi ID B57, Nov. 19, 2022) outlines a plan to build open-source, decentralized infectious disease screening using low-cost extraction-free LAMP testing, self-pooled swab collection, and supporting software, arguing that decentralization, openness, and sub-$5 pricing are essential for pandemic preparedness. It summarizes FloodLAMP’s pilot deployments and partnerships (e.g., NEB and SalivaDirect) and proposes deliverables spanning open program dissemination, publication of pilot data, expanded surveillance deployments, clinical studies and open-protocol FDA submissions, manufacturing scale-up, and legal/governance work. It also provides company background, funding needs and budget, and a growth strategy emphasizing open regulatory pathways, scalable manufacturing, and potential licensing/governance models to sustain public-benefit operations.


CONTENT

***INTERNAL TITLE:*** FloodLAMP: open source decentralized infectious disease screening.
Balvi ID: B57

Balvi Proposal - Nov. 19, 2022
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

We are seeking funding from Balvi to publish our work, expand upon our current programs, and at the same time build the foundation for an enduring entity to help achieve universal access to disease testing, first for all known pandemic-threat pathogens, and then more broadly for improving global health. Key progress on the program and policy fronts can be made, especially with respect to open source FDA approvals and clarity on non-diagnostic testing regulations. On the technical front, our plans include developing a next generation rapid molecular OTC, POC/PON platform (for which we have filed IP and applied for [<u>RADx funding</u>](https://www.poctrn.org/web/radx-tech-high-performance-tests)). There is significant overlap between further developing our current platform and the next gen one, such as bridge assay development work. Please see our [<u>RADx submission</u>](https://docs.google.com/document/d/1dd6XmU5FCCjMfFILdclqgM5yZABerFXfbSB5iPNmSBw/edit?usp=sharing) for details about this as well as information about our pilots, test performance, regulatory filings, and technology development plans.

The following is the set of deliverables we propose. The majority of these have a great deal of groundwork already laid and can proceed in parallel. The timing on several (#3 Expand surveillance programs, \#5 Manufacturing scale up) depend upon the trajectory of the pandemic this winter, and subsequent demand/need for COVID screening. Interest and funding from federal agencies, such as RADx, would also have an impact on priorities and timing.


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
<p>1C. Web app version of mobile app.</p>
</blockquote></th>
<th><ul>
<li><p>Enablement of orgs seeking to bring up locally controlled testing.</p></li>
<li><p>Initiates broad-based feedback.</p></li>
<li><p>Demonstrates new open, cooperative approach.</p></li>
</ul></th>
<th><p>1A. 4-10 weeks</p>
<p>1B. 8 weeks (beta)</p>
<p>1C. 16 weeks</p></th>
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
<li><p>Stimulates consideration of mass testing for PPR in U.S.</p></li>
</ul></th>
<th>4 weeks</th>
</tr>
<tr>
<th><p><u>3. Expand surveillance programs</u></p>
<blockquote>
<p>3A. 20+ additional deployments in prioritized populations (EMS, Schools)</p>
<p>3B. Consider commercial operations for high profit programs (Entertainment)</p>
<p>3C. Additional targets (influenza, RSV)</p>
</blockquote></th>
<th><ul>
<li><p>Reduces disease burden in target populations.</p></li>
<li><p>Progress on legal and procedures for non-diagnostic testing.</p></li>
<li><p>Pushes on FDA/CMS boundaries to legitimize public health emergency/pandemic testing.</p></li>
</ul></th>
<th>30 weeks</th>
</tr>
<tr>
<th><p><u>4. Clinical studies and FDA EUA submissions</u></p>
<blockquote>
<p>4A. Clinical studies to gather data needed to support FDA EUA submissions.</p>
<p>4B. EUA submissions as open source protocol tests.</p>
<p>4C. Multi-site studies to support 510K.</p>
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
<tr>
<th><p><u>5. Manufacturing scale up</u></p>
<blockquote>
<p>5A. Manufacture reagents for 450K test kits.</p>
<p>5B. Purchase consumables &amp; collection kits.</p>
<p>5C. Engagement with contract manufacturers.</p>
</blockquote></th>
<th><ul>
<li><p>Derisks continued operations.</p></li>
<li><p>Gives internal capacity for scaling programs in different configurations.</p></li>
<li><p>Sets stage for growth of manufacturing capabilities.</p></li>
</ul></th>
<th>8 weeks</th>
</tr>
<tr>
<th><p><u>6. Legal agreements and plan for growth</u></p>
<blockquote>
<p>6A. Standard licenses</p>
<p>6B. Corporate structure changes, to establish FloodLAMP’s creation of public goods and simultaneously support growth</p>
</blockquote></th>
<th><ul>
<li><p>Provides foundation for the next stage of the company/new entity.</p></li>
<li><p>Serves as an example of implementation of key governance, commercial, and IP issues for public goods focused entities.</p></li>
</ul></th>
<th>6 weeks</th>
</tr>
</thead>
<tbody>
</tbody>
</table>


## Budget
The budget below is a breakdown of spending to meet the proposed deliverables. A second budget for a set of supplementals includes areas for which we are also seeking funding from RADx. We included a placeholder line item for commercial operations, which we can discuss in the context of the main proposal and Balvi priorities.

[<u>Balvi Proposal 1 - Budget</u>](https://docs.google.com/spreadsheets/d/1QUWxjItRY1k-QHd1DmSPnTbUJQ8SyT5Qfxmqh3FHFjg)

### Budget Table 11-17

| A | B | C | D | E | F | G |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  |  |  |  |  |  |  |
|  | __$730,000__ | __Open Source Platform__ |  |  |  |  |
|  | $250,000 | OS Platform - new CYOA website |  |  |  |  |
|  |  | $200,000  Web agency - design and dev |  |  |  |  |
|  |  |   $ 50,000   Studio & Video production |  |  |  |  |
|  | $ 80,000 | Legal IP - open license w commercial terms (app and test) |  |  |  |  |
|  | $200,000 | Comms - Publication, Outreach, Community, PR, graphic design and more? |  |  |  |  |
|  | $200,000 | Web App w open license Non-Comm, Non-govt |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$450,000__ | __Clinical and Regulatory__ |  |  |  |  |
|  | $200,000 | 50K Test Kits for Clinical Studies w Surveillance & registry study |  |  |  |  |
|  | $100,000 | Regulatory Consulting (Arete, SalivaDirect partner) |  |  |  |  |
|  | $150,000 | Clinical Studies Site Bring Up & Maintenance (IRB, consumables, etc) |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$590,000__ | __Manufacturing Scale Up__ |  |  |  |  |
|  | $200,000 | Bulk reagents, 50K kits, ops |  |  |  |  |
|  | $300,00 | Manufacturing team |  |  |  |  |
|  | $ 90,000 | Equipment |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$132,0000__ | __Staff__ | 8 | heads | 0.8 | ramp |
|  | $788,800 | Employee Salaries  | 116000 | salaries/mo | 7 | mo |
|  | $177,480 | Benefits and Taxes  | 0.225 | overhead |  |  |
|  | $350,000 | Contractor Fees | 50000 | fees/mo | 7 | mo |
|  |  |  |  |  |  |  |
|  | __$ 60,000__ | __Equipment (Internal)__ |  |  |  |  |
|  | 60000 | PCR Machines | (1x96 and 3x16) |  |  |  |
|  |  |  |  |  |  |  |
|  | ***$3,150,000*** | ***TOTAL PROPOSAL*** |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$1,210,000__ | __Next Gen Platform R&D__ |  |  |  |  |
|  | $200,000 | Device Prototype Fabrication |  |  |  |  |
|  | $350,000 | Instrument Prototype |  |  |  |  |
|  | $660,000 | Next Gen Staff: 3 FTE for 6 mo, 4 contractors |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$120,000__ | __Marketing/Access__ |  |  |  |  |
|  | $120,000 | Outreach and dissemination and publication |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$80,000__ | __Open source commercial - legal__ |  |  |  |  |
|  | $ 80,000 | licenses etc |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$100,000__ | __Consumables__ |  |  |  |  |
|  | $ 80,000 | Cartridges and microfluidics |  |  |  |  |
|  | $ 20,000 | Droppers |  |  |  |  |
|  |  |  |  |  |  |  |
|  | __$100,000__ | __Commercial Team Seed Funds__ |  |  |  |  |
|  |  |  |  |  |  |  |
|  | ***$1,530,000*** | ***TOTAL SUPPLEMENTALS*** |  |  |  |  |


## FloodLAMP Company Information
FloodLAMP Biotechnologies was incorporated in Delaware on 8/3/2020 as a Public Benefit Corporation. Our charter states “the specific public benefit that the Corporation will promote is the development of open protocols and the implementation of large scale disease screening for infectious disease for the benefit of the public.”

We are currently 4 employees, 2 full time and 2 part time. Please see the last portion of our recent [<u>RADx funding submission</u>](https://docs.google.com/document/d/1dd6XmU5FCCjMfFILdclqgM5yZABerFXfbSB5iPNmSBw/edit?usp=sharing) for profiles of our team members. Here is a more detailed bio for our CEO and founder, Randy: [<u>Randall True Biosketch</u>](https://drive.google.com/file/d/1hgpfBA99cNOszNrRA9Ft4FFdxUyaAkWp/view?usp=share_link). He is a co-author on the [<u>global LAMP consortium review paper</u>](http://bit.ly/gLAMP-review) which appeared in a [<u>special issue of the Journal of Biomolecular Techniques</u>](https://abrf.memberclicks.net/jbt-2021-september-issue).

Our facility is 2,200 sqft of joint lab and office space in Portola Valley, CA, 10 minutes from Stanford University.

FloodLAMP is majority self-funded, with $975K in SAFE’s ($500K founder, $475K angels) and a $500K founder loan, convertible to a SAFE. Our revenue to date is $234,352.

## Growth
This proposal for funding provides the resources needed to bring much of the work we’ve done during the pandemic to fruition. Many of these are significant accomplishments in their own right, yet they are also steps to building something much bigger and delivering globally impactful solutions in disease detection.

Regarding open EUAs, it should be noted that obtaining the EUAs cited in this proposal will likely require federal agency support due to FDA policy changes in 2021. We think that funding from Balvi, along with publication and outreach, will generate major momentum and galvanize our network, including foundations and NGOs active in pandemic response. We’re hopeful this will lead to support and potential funding from RADx or BARDA. The need for public-private partnerships in COVID/pandemic testing is often highlighted, and we agree. Our goal is to bring many resources to bear on the problem of pandemic testing and help provide efficient avenues to translating funding to actual capability. We are cautiously optimistic as initiatives such as the [<u>White House National Biodefense Plan</u>](https://www.whitehouse.gov/wp-content/uploads/2022/10/National-Biodefense-Strategy-and-Implementation-Plan-Final.pdf) and [<u>World Bank Pandemic Fund</u>](https://www.worldbank.org/en/programs/financial-intermediary-fund-for-pandemic-prevention-preparedness-and-response-ppr-fif) spin up. As was the case during the pandemic, these “plans” are very light on details. We see potential for FloodLAMP to garner attention as we are offering real solutions, both at the level of technology and programs, as well as the systemic/policy level. Publishing our work soon will be key to getting involved with these larger pandemic preparedness and response efforts.

Our IP offers the potential for growth through licensing and partnerships. Our [<u>first patent application</u>](https://drive.google.com/file/d/1QRwe6OzAOEfTtnd8rpgYurZL7dRxpsl-/view?usp=share_link) has been published and has broad coverage of inventions related to on-the-fly (outside the lab) pooled sample collection. We filed this patent as a PCT and received a favorable written opinion from the US patent office, which granted us expedited examination for our regular US patent application. We have filed an additional provisional patent application covering other program related inventions and a 161 page provisional on the next generation platform. Given our open source approach and public benefit mission, we have carefully considered options around IP issues. We included as a deliverable the execution of standard licenses to open up access to our IP while maintaining the option to share in profits with better resourced commercial partners. We will consider non-commercial end-use royalty free licenses and open sourcing the code for our new web app. We do think licensing and IP need to be a core competency of the company, as we see a big opportunity to license test IP from universities and offer a commercialization model that maximizes impact while maintaining a modest royalty structure.

Momentum gained from Balvi funding will allow us to fully capitalize on the many relationships we have developed over the course of our work. In particular, we have developed a good relationship with [<u>New England Biolabs</u>](https://www.neb.com/), the largest manufacturer of enzymes for molecular biology in the world. NEB is a critical global supplier for biosecurity and an outlier in the industry, being so large yet still privately held. They were officially certified as a B corp and actively work globally on mission-driven programs and technology transfer. They have donated reagents for several FloodLAMP pilots and collaborations, both in the U.S. and in Colombia and Brazil. NEB is the recognized leader in LAMP, and while we do plan to diversify and validate our test with other LAMP master mixes (several companies such as Thermo and Meridian have commercialized products during the pandemic), NEB has important IP on the inclusion of thermolabile nucleotides into LAMP amplification. This greatly reduces the impact of any amplicon contamination and we believe is a key enabler for the decentralization of LAMP based testing. In addition they acquired the top lyophilization company, Fluorogenics, last year and so have key expertise and technology for OTC/POC LAMP based devices, such as our next generation platform.

FloodLAMP was invited to the NEB campus in Massachusetts in March of this year and gave a talk on FloodLAMP’s work to the company. We have had multiple meetings with senior management and they have expressed a deep interest in our mission and goals. NEB has provided a [<u>letter of support</u>](https://drive.google.com/file/d/1IPgF-HJRjP2sd0NX_MOf1pSXo2bHeUGO/view?usp=share_link) for grant applications to BARDA. Balvi funding will allow us to collaborate with them on both technical development and commercialization of inexpensive LAMP test kits, and also on regulatory authorizations through the WHO.

Another key collaborator is [<u>Anne Wyllie</u>](https://ysph.yale.edu/profile/anne-wyllie/), a researcher at the Yale School of Public Health, founder of [<u>SalivaDirect</u>](https://ysph.yale.edu/salivadirect/), and a member of our Scientific Advisory Board. Balvi funding will allow us to work with her and the SalivaDirect team on open source protocol FDA approvals. It was through Anne that we learned about this important regulatory development in the fall of 2020. Anne is a force of nature and deeply committed to openness (see [<u>link</u>](https://docs.google.com/document/d/1GKlS-Ln69ZiPpXdfgpHLHMXGCsbkIsIufwRrbJ1WCIg/edit?usp=sharing) for more details). She shared her full EUA submission with us as we were working on our EUAs and fielded many questions. Anne also shared legal agreements for labs and states and joined our call with FDA reviewers in October of 2021. Over the last 2 years she has led more than 20 amendments to the SalivaDirect EUA and formed key industry partnerships. Her experience would be tremendously helpful for our regulatory efforts, and formally partnering with SalivaDirect could lead to sustained engagement with the FDA prior to BARDA/RADx funding. We’ve included a line item in our budget for consulting fees for SalivaDirect, which is in the process of spinning out from Yale to form a non-profit. They would be a great organization for Balvi to consider funding.

FloodLAMP was spun out from a 501(c)3 STEM education non-profit. Operating at the intersection of for-profit and non-profit has been challenging, and we are eager to legally codify our public benefit commitments. A potential scenario that looks promising is forming a DAO. FloodLAMP could stay a PBC or transition to a non-profit, and be governed by the DAO. We have no experience in DAOs, blockchain, or web3, though we do have close contacts with experience. A DAO could align the incentives of a range of people and organizations around the focused mission of universal pandemic testing. Some specific aspects of the space and our goals that may make a DOA structure a good fit are:

- enabling the grass roots pull of testing programs into communities or countries by organizing local support and labor, applying specific geographic and technical knowledge, matching with funding, and facilitating the needed physical and digital resources;
- using the Rights of Reference (ROR) sharing mechanisms for regulatory validation data to expedite and lower the costs for test approvals - ROR are very powerful and seldom used (for more info [<u>see Randy’s discussion on the this with the FDA</u>](https://docs.google.com/document/d/1mU4CYHEAUiRaP3gugs2NxJkAl9yAUxi-hxGZ_o276dg/edit?usp=share_link));
- drawing on the expertise of many scientists in making key decisions about what tests to invest in for regulatory approvals and manufacturing scale up – this could create an influential new voice in the space, but notably one that is executing rather than only advocating;
- automatically distributing resources (via smart contracts) when triggering events occur or governing decisions are made, speeding response in an emergency.

Perhaps most important, the transparency in activities and governance of a DAO, could build much needed trust. Most of this could be accomplished within a standard organizational structure as well, however a DAO could potentially be more impactful.

Linked documents and a few others, including our FDA submissions, are in this openly shared google drive folder:

<!-- FLAG -->
[<u>Balvi &lt;&gt; FloodLAMP Shared Folder</u>](https://drive.google.com/drive/folders/1Myhwp0Hl18SzGkUGTHkSKfeSzOQTX8kR?usp=share_link).

[<u>FloodLAMP FDA and Regulatory Documents</u>](https://drive.google.com/drive/folders/1Q6lMi3OvjMRYTlGmzRxVLFxe61Y17Nhr?usp=share_link)

[<u>FloodLAMP - COVID-19 Tests Summary.pdf</u>](https://drive.google.com/file/d/1dvyU-HwsN_aRpsMkBTSFVx6Dt82jh5nc/view?usp=share_link)

[<u>FloodLAMP - FDA Foundation Presentation.pdf</u>](https://drive.google.com/file/d/1y0Bb-8Knjqaps2er5MMsg1uimw22bMPP/view?usp=share_link)

[<u>FloodLAMP Preschool Program Description.pdf</u>](https://drive.google.com/file/d/16szPDXq_8QL9epOubYITPbUNepFSUZYN/view?usp=share_link)

We look forward to your feedback and questions!
