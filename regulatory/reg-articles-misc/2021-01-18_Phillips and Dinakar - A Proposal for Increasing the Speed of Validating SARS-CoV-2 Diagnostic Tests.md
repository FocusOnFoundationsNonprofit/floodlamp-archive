METADATA
last updated: 2026-02-24 RT initial conversion
file_name: 2021-01-18_Phillips and Dinakar - A Proposal for Increasing the Speed of Validating SARS-CoV-2 Diagnostic Tests.pdf
file_date: 2021-01-18
title: 2021-01-18_Phillips and Dinakar - A Proposal for Increasing the Speed of Validating SARS-CoV-2 Diagnostic Tests
category: regulatory
subcategory: reg-articles-misc
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url:
pdf_gdrive_url: https://drive.google.com/file/d/1JNV1qjtI2poNYGCp89FMRv1oNxOSpuBo
pdf_github_url: 
conversion_input_file_type: pdf
conversion: AI
license: 3rd Party
tokens: 8408
words: 4930
notes:
summary_short: Phillips and Dinakar's proposal paper (v0.1.9, January 2021) recommends three extensions to the FDA's EUA process for accelerating validation of SARS-CoV-2 diagnostic tests: structured (machine-readable) EUA data submissions, distributed FDA-directed CLIA-led validation leveraging existing laboratory expertise, and building an open synthetic patient clinical specimen panel to reduce dependence on limited clinical samples for test validation.


CONTENT

***INTERNAL TITLE:*** A Proposal for Increasing Speed of Validating SARS-CoV-2 Diagnostic Tests

Alexander James Phillips †, Karthik Dinakar ‡
† Center of Complex Interventions, ‡ Massachusetts Institute of Technology
Correspondence to ajp@centerofci.org
v0.1.9 - 2021 Jan 18th

## Summary

Rapid access to diagnostics for emerging high priority pathogens is of great importance from a clinical, public health and economic point of view. Currently in the United States there are several technological, regulatory and organisational improvements that might be adopted for the COVID-19 and future pandemics. In this article, we suggest a proposal for increasing the speed of validating SARS-CoV-2 diagnostic tests, suggestions include: a structured (machine readable) EUA data submission process, distributed FDA directed CLIA led validation, and building an open synthetic patient clinical sample panel. This document is a work in progress, containing some ideas which may be of value to consider and implement. We welcome you to add your name to this proposal or make a contribution of any size and scope. This concept and paradigm will be of utmost importance for pandemics of diseases more prone to the emergence of new mutant strains that evade current diagnostics and vaccines.

## Contents

1 The Opportunity and Goals
- 1.1 Diagnostic tests are powerful tools, we need rapid access to them
- 1.2 We need trustworthy knowledge of diagnostics performance
- 1.3 Emergency Use Authorisation, United States Code

2 The Current Situation
- 2.1 Initial response time
- 2.2 EUA backlog delays tests coming to market
- 2.3 Heterogeneous quality of test performance data
- 2.4 No guarantee of accurate test performance data
- 2.5 Quality control and reference materials

3 Possible Extensions to Current Validation Process
- 3.1 EUA minimum structured data
- 3.2 FDA directed CLIA led validation
- 3.3 Synthetic clinical specimen panel challenge
  - 3.3.1 Current strategy: waiting for infections to get specimens to validate against
  - 3.3.2 New strains are harder to counter
  - 3.3.3 Underpowered validation: Clinical specimen edge cases
  - 3.3.4 Routes to characterised viral material for reproducible validation of diagnostics
  - 3.3.5 Synthetic patient specimen panel
  - 3.3.6 Potential advantages of a synthetic patient specimen panel

4 Request for Comment

5 Revision History

## 1 The Opportunity and Goals

### 1.1 Diagnostic tests are powerful tools, we need rapid access to them

Well characterised diagnostic tests for diseases are powerful tools to help clinicians, public health and policy makers treat patients, and lessen the burden of communicable diseases on communities. In situations of newly emerging serious infectious diseases, rapid access to diagnostics tests is of utmost importance. Diagnostic tests allow clinicians to better treat their patients. Population screening allows public health officials to help trace and break chains of infection and find asymptomatic individuals. In conjunction with policy makers providing support, this allows for test, trace and isolate public health programs to reduce or eliminate community transmission [4].

### 1.2 We need trustworthy knowledge of diagnostics performance

As important as the test itself is clear and trustworthy knowledge of the tests performance characteristics. Although we do need tests "that work", it's important that we know how well tests work, which includes the uncertainty of those metrics describing the test's performance.

One of the objectives of the VITAL Act (Verified Innovative Testing in American Laboratories) of 2020 is to "ensure that laboratory-developed testing procedures are accurate, precise, clinically-relevant" [23, 22d]. In other words, it is necessary for an initial validation to be performed for each new diagnostic test and for that initial validation to be well characterised and consistent to allow comparison between different tests.

### 1.3 Emergency Use Authorisation, United States Code

The United States Food and Drug Administration (FDA) oversees the Emergency Use Authorisation (EUA) process, including that for COVID-19 related medical devices [6]. The criteria for the issuance of EUAs are stated in Act 21 U.S.C. §§ 360bbb-3(c)(1-5) [30]. Included is the legal and binding duty to ensure:

> the known and potential benefits of the product, when used to diagnose, prevent, or treat such disease or condition, outweigh the known and potential risks of the product, taking into consideration the material threat posed

and that

> there is no adequate, approved, and available alternative to the product for diagnosing, preventing, or treating such disease or condition

This thought piece does not disagree with these objectives and criteria; it raises the question of whether and how we might fulfil these requirements but do so more quickly.

## 2 The Current Situation

### 2.1 Initial response time

Crucial to the early access to diagnostics was the timely and accurate publication of the SARS-CoV-2 genome [34]. This enabled high complexity CLIA labs and commercial manufacturers to respond quickly; both in the production of the tests ready for EUA submission and in the quality control material necessary to begin reproducible measurement and validation of test performance.

Many elements of our molecular pathology diagnostic response to this pandemic have been exceptional. The rapid speed at which diagnostics were made ready by molecular pathology laboratories was on par with the 2009 H1N1 pandemic [18, 22b]. However the FDA's EUA process initially significantly slowed efforts to deploy these tests. Without these tests, samples were sent to central public health labs which limited the scale of testing and slowed down the test to result time. Both testing capacity and responsiveness are crucial factors in getting ahead of outbreaks and containing them through public health counter measures. This lack of testing and responsiveness also limited clinicians and policy makers in treating and providing scientific, data driven leadership [17].

The FDA responded to these challenges and updated their guidance to accommodate more risk [5c]. This was a crucial leadership decision that will surely be reflected upon and copied for future infectious disease outbreaks.

### 2.2 EUA backlog delays tests coming to market

Over the following months, almost 1 new diagnostic test was given EUA status per day [15]. The FDA simultaneously grew their diagnostics review team from 25 to 100 (as of mid October [10]) with many more support staff. Despite these admirable efforts there remains a backlog of new diagnostic tests awaiting FDA review for EUA [11b, 10]. This backlog delays companies from bringing their test to market. This delay has a negative effect on our collective ability to leverage all supply chains and technologies as quickly as possible and bring them to bear against this new infectious disease. In hindsight this backlog and associate delay, along with many other shortcomings outside of the FDA's EUA process [8, 21] may be shown to have had a significant negative effect on the ability of the United States to effectively respond to the pandemic.

### 2.3 Heterogeneous quality of test performance data

As previously stated, rapid access to tests with trustworthy evaluation of test performance is a fundamental requirement. Although many tests have now attained EUA, the quality of the documentation and validation of these tests is heterogeneous [28]. This characteristic has persisted since the beginning of the outbreak, is a large source of uncertainty for laboratory staff and managers making decisions about which test to purchase, and increases the burden needed to validate a new diagnostics test. The information heterogeneity shows itself in many forms, the first of which being information in EUAs. Some EUAs are thorough and concise with all the necessary information present. On the other extreme are EUAs that lack crucial information, have errors, or reference data that does not exist. The clearest example of this are primer sequences which although requested by the FDA are only present in 34% of submissions dropping to 5.8% of the most frequently used tests [28]. This is important information given the range of mutations which have been found to negatively impact test performance [13, 32, 2]. Performance degradation might have occurred in other tests and is unlikely to have been detected in all cases. Inclusion of primer / probe sequence information might increase the ability of laboratory, public health and others to be more proactive in the face of new mutant viral strains [29b].

### 2.4 No guarantee of accurate test performance data

Finally the current EUA process does not ensure the validation results reported are reproducible. In several instances [14, 3b] widely used diagnostic test were assessed and a significant difference was found between the limit of detection (LOD) reported in the EUA and that which the investigators measured using their own reagents and protocol. These are not isolated incidences and the sensitivity of diagnostics given by its LOD is important for effective public health Test Trace Isolate (TTI) programs [1].

As mentioned previously, in several cases the EUA process has not guaranteed disclosure of some essential attributes of diagnostic test characteristics. Similar to the previously cited example where LOD reported in EUAs was not reproducible, several EUAs also report LOD with non SI units of TCID50 ml⁻¹ [28]. This prohibits investigations to reproduce the claimed performance characteristics.

The lack of information or guarantees about the performance of diagnostics tests has transferred the cost of validation to the labs adopting the tests [22c, 20d]. Various open and closed networks of laboratory staff have taken up the role of sharing important test performance information. It would be powerful if there was an open, structured data repository of diagnostic test performance data. Similar to Wikipedia, lab staff could contribute verification / validation data of diagnostic test performance; benefiting other labs, in return benefiting from data submitted by other labs and collectively benefitting the patients they serve. Whilst such a community of lab staff and shared data store would be of great aid to a public health emergency, most labs are primarily driven by commercial pressures and would not be expected to contribute towards such a collective effort despite benefitting from it.

### 2.5 Quality control and reference materials

Viral positive control materials were produced early on and are now widely available. Providers include a range of commercial and government sources [7]. Viral material includes positive clinical specimens, naked RNA, virus like particles, live virus and inactivated virus.

## 3 Possible Extensions to Current Validation Process

These proposals revolve around 3 main themes. Firstly, the merits of defining a minimum set of required data for a diagnostics EUA and doing so in a structured form. Secondly, utilising the validation work already done by some of the high complexity CLIA laboratories around the United States. Thirdly, combining existing quality control materials to provide a representative and extensible panel of synthetic clinical specimen challenges for tests to pass. We hope these suggestions aid further discussion around new models of validating tests, potentially helping bring tests to market sooner, both during this pandemic and any future pandemics.

### 3.1 EUA minimum structured data

The normal submission process for a new diagnostic tests accumulates thousands of pages and takes years [26b]. The EUA process instead requires only tens of pages and should take days to complete. This might enable labs and manufacturers to legally distribute their test within days and meet the urgent need for diagnostics to contain and aid treatment of SARS-CoV-2.

Some tests awaiting review and approval by the FDA have taken over a hundred days and counting. This has largely been due to the volume of testing required which has stimulated a large market response. The correspondingly large volume of submissions has saturated the FDA's capacity to review new submissions in a timely fashion.

As mentioned previously the FDA has been exemplary in their continual adaptation and responsiveness. Expanding their team by many factors [10], reducing and refining the minimum set of information required for EUAs and providing multiple template EUA documents [12]. These templates have aided manufacturers, laboratories and others in their EUA submission process by helping to ensure the minimum information is included. And secondly may have aided the FDA reviewers by providing a more standardised form of EUA submission which makes comprehending and reviewing the EUAs a faster process.

For the same EUA submission type, for example "Molecular Diagnostic Template for Commercial Manufacturers", each EUA submission should contain the same types of data. However despite the templates provided there is still significant heterogeneity in the data [28].

Adopting a tool to enforce structured data upon submission for an EUA might aid both the companies in ensuring all the necessary fields are completed, and the reviewers in checking the data. There are many providers of such tools such as TypeForm, Microsoft Forms, etc. These off the shelf solutions are cheap, secure, fast to configure and reliable. The structured data they take in could then be provided as is or additionally used to automatically populate the templates mentioned earlier. The applications for structured data are many but at a minimum might allow laboratories looking for a new test to more easily compare and search across the available EUA data. The structured data might also aid the FDA's internal processes, allowing for better prioritisation, communication with and tracking of applicants.

**Figure 1:** Locations in the current EUA process where structured data may be employed (solid red boxes) to expedite and enable related processes and workflows (dashed boxes) by ensuring data is present, formatted consistently and easier to parse, prioritise and compare against other EUAs. IFU: Instructions For Use documentation may form part of the package inserts. Adapted from FDA's SHIELDx presentation [25]. SHIELDx (Systemic Harmonization and Interoperability Enhancement for Lab Data) program's stated goal is to "Describe the same test data the same way".

_Flowchart diagram showing the EUA process from test manufacturers through FDA review to approval and publication of EUAs/IFUs. Solid red boxes indicate where structured data could be employed at the submission, initial review, and laboratory use stages. Dashed boxes indicate downstream processes and workflows—such as prioritisation, clarification requests, and cross-EUA comparison—that may be aided by the presence of structured data._

### 3.2 FDA directed CLIA led validation

The requirement of an EUA for a Laboratory Developed Test (LDT) has recently been lifted by the FDA [16b]. Whilst there may have been a component of political pressure, this in part is due to the depth of expertise of the directors and staff in the nation's ~2,500 high complexity CLIA laboratories subspecialising in virology (~127,000 high complexity CLIA laboratories as of 2011 [33b] of which 2% subspecialise in virology [33c]). The LDT EUA rescission has allowed many hundreds of laboratories to legally begin immediate use of their LDTs for diagnosis. In conjunction with the LDTs they have developed and validated, many laboratories have and will continue to increase their testing capacity by evaluating and purchasing commercial test manufacturers equipment and reagents.

It has already been highlighted that expert validation work of newly purchased diagnostic tests is being conducted by the purchasing labs [22c], as is required by CLIA regulations [27b]. Taken together this validation work may collectively be being conducted with a much broader range of acceptable sample types. This is important as it has the potential to contain a sufficient number of specimens to be representative of the population of specimens and avoid being a statistically underpowered validation of a diagnostic test. Secondly this work is inherently aligned to the interests of patients, society, laboratories, regulators and test manufacturers by avoiding the potential unconscious bias of diagnostic manufacturers as they validate their own test. As previously suggested [20b], there is an obvious opportunity to leverage this expert validation work being conducted by CLIA labs. What follows is a potential model the FDA could design, implement and coordinate in this and future pandemics:

1. A prospective supplier seeking an EUA sends a number of copies of the machine (a minimum of 3, preferably more) and sufficient reagents (e.g. for 1000+ tests each) to the FDA along with their submission of structured data describing the test, its performance characteristics as assessed by the manufacturer, claimed capabilities, etc.
2. Separately, for free or a fee, laboratories make themselves available to the FDA to review the EUA and validate machines. This is a task all have already had to do during this pandemic and seems prudent to harness this significant capacity of distributed talented work
3. The FDA can conduct their own evaluation of the machine whilst also sending the draft EUA, a machine, and reagents to a random subset of available laboratories. Optionally a reference panel (see "Synthetic clinical specimen panel challenge" below) can be sent as well. Amongst other potential benefits a reference panel would enable harmonising results between laboratories
4. The initial standard sets of validation data, including positive viral materials used, comparator test, etc. are uploaded to a centralised database
5. Any significant discrepancy between laboratory validation results are resolved
6. The company is authorised for a particular set of EUA performance characteristics
7. Only then can the submitting company know which labs are in possession of their test machine and may offer them to buy it

This is one potential model for the distributed initial validation of diagnostics for emerging, high priority pathogens. It is coordinated by the FDA and uses the existing legislation but leverages the latent, capable and eager talent of our molecular pathology laboratories.

**Figure 2:** Potential model leveraging validation work being performed in CLIA laboratories to maximise speed, volume and accuracy of authorising emergency diagnostics. IFU: Instructions For Use.

_Flowchart diagram showing test manufacturers submitting EUAs along with machines and reagents to the FDA, which then distributes them to randomly selected available CLIA laboratories for independent validation. The laboratories conduct CLIA-led validation and report results back to the FDA for review, leading to approval and publication of EUAs/IFUs._

### 3.3 Synthetic clinical specimen panel challenge

#### 3.3.1 Current strategy: waiting for infections to get specimens to validate against

When a new pathogen emerges the availability of clinical samples to test with is very limited. This limitation slowed down the effective development and validation of much needed new diagnostics for COVID-19 pandemic. (todo: find and cite paper reiterating benefits of international sharing of specimens) Our current strategy is to wait for sufficient new infections to get sufficient samples needed for multiple labs, commercial manufacturers and government agencies to all develop and validate their diagnostics tests. If not addressed, this strategy will slow down the response to the next pathogen or strain that emerges.

Secondly the threshold for which diagnostics tests must overcome to show clinical efficacy was 20 and is now set at 30 positive patient samples. During the early stages of a pandemic, when testing is most important to control spread, there are insufficient samples which makes this barrier insurmountable.

#### 3.3.2 New strains are harder to counter

In later stages of a pandemic that is under control there will also be insufficient samples. If there are many new infections, such as the United States and other countries like the United Kingdom are experiencing coming into the winter of 2020, there is a different problem, namely the increased infections, increases the chance of mutations rendering existing diagnostics less effective [13, 32, 2]. This is an identical, if not harder, scenario to contend with than at the outset of a pandemic. It is harder because there will be many infections from existing strains which makes identifying appropriate samples for testing against more challenging. Simultaneously, in the early phase of a new strain spreading, there will be a very low absolute and relative number of specimens for which to validate tests against.

#### 3.3.3 Underpowered validation: Clinical specimen edge cases

Finally, the validation of new diagnostic tests is conducted using a random but small set of samples from clinical specimens. This is likely to be statistically underpowered whilst also likely not including many or any of the significant edge cases a diagnostic test would preferably be able to correctly deal with. Edge cases such as a concurrent infection with pus, elevated mucin levels, blood, or for saliva samples, the presence of food, or acidity from orange juice etc. Some EUAs, often submitted during periods of relatively low disease prevalence, used contrived samples based on repeating tests on the same clinical sample, further limiting the range of samples the test is validated for. Other EUAs have been given based on samples of RNA in solutions of stabilizing buffer RNA Diluent P which although likely justifiable given the circumstances, would seem to have significant room for improvement to meet US Federal Regulations calling for samples used (in proficiency testing) to "mimic actual patient specimens when possible" [31].

#### 3.3.4 Routes to characterised viral material for reproducible validation of diagnostics

In the absence of a national or international standard of SARS-CoV-2 material the FDA has made available a reference panel of samples [9]. This material is an important step and one called for previously to enable the standardisation of diagnostic test sensitivity [20c]. In the context of the current pandemic, wider and early access to such a control material would enable a more robust characterisation of diagnostic tests between different laboratories, machines, and batches of reagents and consumables.

As this material is still restricted to the diagnostics tests which have received EUA an alternative approach is the use of commercially available control materials [7]. As these are not yet benchmarked a harmonisation study being prototyped by JIMB is underway [19]. The results from this important work should allow the use of commercial control materials to yield commutable results of diagnostics test sensitivity. This study is predicated on the quality control material being homogenous and consistent with one batch.

#### 3.3.5 Synthetic patient specimen panel

With the FDA reference panel, or an open source panel constructed from harmonised commercial viral material it would then be possible for multiple testing labs, and or by the FDA or another organisation like FINDDX [24]. to conduct independent and comparable validation of diagnostic sensitivity.

If an open source list of ingredients for each of the reference panel specimens were made available, then over time it could be improved to more closely represent clinical specimens and extended to cover more edge cases. For example the inclusion of blood, mucin, a simulated concurrent bacterial infection and other interfering components and pharmaceuticals could be included in an extended reference panel.

**Figure 3:** How the use of a pre made clinically relevant synthetic patient specimen panel spiked with inactivated viral material may allow more rapid validation of diagnostics. Based on the assumptions that rapid access to diagnostics aids public health test, trace and isolate interventions to curtail community transmission and secondly that limited clinical samples delayed validation of new diagnostics.

_Timeline comparison diagram showing two parallel processes. The current process proceeds from pathogen isolation through sequencing, test development, waiting for community prevalence to rise, collecting sufficient clinical specimens, conducting test validations, and finally granting EUAs for widespread deployment. The proposed process using a synthetic specimen panel bypasses the need to wait for clinical specimens by spiking a pre-made panel with inactivated viral material, enabling earlier test validation and EUA granting. The diagram indicates that the time saved would result in avoided community infections._

#### 3.3.6 Potential advantages of a synthetic patient specimen panel

Confronted with a new pathogen, or a mutant of an existing pandemic pathogen, it might be much faster to spike new synthetic or inactivated viral material into such a reference panel than wait for sufficient patient specimens to validate a diagnostic test. Such a panel would also offer the opportunity to include all the edge cases such a test should be able to handle. And finally with these consistent and characterised synthetic specimens a more consistent and reproducible validation of diagnostic tests may be conducted allowing the performance characteristics to be compared to each other. This would help lab staff make informed decisions about which diagnostic system to purchase or implement, this aids patient care, supports public health initiatives and provides a crucial piece of information to make the diagnostics market more competitive and efficient.

## 4 Request for Comment

This is a work in progress and any contributors who would like to join the draft with any size and scope of change are welcome. We look forward to receiving your thoughts and integrating them in this or a subsequent document. Please contact ajp@centerofci.org.

## References

[1] Ramy Arnaout et al. "SARS-CoV2 Testing: The Limit of Detection Matters". (June 2020). doi: 10.1101/2020.06.02.131144. [link](https://doi.org/10.1101/2020.06.02.131144).

[2] Maria Artesi et al. "A Recurrent Mutation at Position 26340 of SARS-CoV-2 Is Associated with Failure of the E Gene Quantitative Reverse Transcription-PCR Utilized in a Commercial Dual-Target Diagnostic Assay". In: *Journal of Clinical Microbiology* 58.10 (July 2020). Ed. by Angela M. Caliendo. doi: 10.1128/jcm.01598-20. [link](https://doi.org/10.1128/jcm.01598-20).

[3] (a) Atreyee Basu et al. "Performance of Abbott ID Now COVID-19 Rapid Nucleic Acid Amplification Test Using Nasopharyngeal Swabs Transported in Viral Transport Media and Dry Nasal Swabs in a New York City Academic Institution". In: *Journal of Clinical Microbiology* 58.8 (2020). Ed. by Alexander J. McAdam. doi: 10.1128/JCM.01136-20. [link](https://jcm.asm.org/content/58/8/e01136-20); (b) [annotation](https://hyp.is/Jyk67B4yEeu8g6-KL---0Q/jcm.asm.org/content/58/8/e01136-20).

[4] Aleksandra Bliszczyk. "How doughnuts became Australia's symbol of Covid hope". Nov. 2020. [link](https://www.theguardian.com/lifeandstyle/2020/nov/05/how-doughnuts-became-australias-symbol-of-covid-hope).

[5] (a) "Coronavirus (COVID-19) Update: FDA Issues New Policy to Help Expedite Availability of Diagnostics". Feb. 2020. [link](https://www.fda.gov/news-events/press-announcements/coronavirus-covid-19-update-fda-issues-new-policy-help-expedite-availability-diagnostics); (b) "Policy for Diagnostics Testing in Laboratories Certified to Perform High Complexity Testing under CLIA prior to Emergency Use Authorization for Coronavirus Disease-2019 during the Public Health Emergency Immediately in Effect Guidance for Clinical Laboratories and Food and Drug Administration Staff". Feb. 2020. [link](https://www.regulations.gov/document?D=FDA-2020-D-0987-0007); (c) [annotation](https://anot8.org/r/1772.2/1163?h=0).

[6] "Coronavirus Disease 2019 (COVID-19) Emergency Use Authorizations for Medical Devices". [link](https://www.fda.gov/medical-devices/emergency-use-authorizations-medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices).

[7] "Database of SARS-CoV2-relevant control materials: Specs, Vendors, and more". [link](https://poeli.gitlab.io/collated_vendor_info/).

[8] "Dying in a Leadership Vacuum". In: *New England Journal of Medicine* 383.15 (Oct. 2020), pp. 1479–1480. doi: 10.1056/nejme2029812. [link](https://doi.org/10.1056/nejme2029812).

[9] Center for Devices FDA and Radiological Health. "SARS-CoV-2 Reference Panel Comparative Data". 2020. [link](https://www.fda.gov/medical-devices/coronavirus-covid-19-and-medical-devices/sars-cov-2-reference-panel-comparative-data).

[10] "FDA Virtual Town Hall Series - Immediately in Effect Guidance on Coronavirus (COVID-19) Diagnostic Tests". Oct. 2020.

[11] (a) "FDA Virtual Town Hall Series - Immediately in Effect Guidance on Coronavirus (COVID-19) Diagnostic Tests". June 2020; (b) [annotation](https://hyp.is/e4JUzh6cEeueFN8b2wv2sg/www.fda.gov/media/139618/download).

[12] Food, Center for Devices Drug Administration, and Radiological Health. "In Vitro Diagnostics EUAs". 2020. [link](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas).

[13] Allison J. Greaney et al. "Complete mapping of mutations to the SARS-CoV-2 spike receptor-binding domain that escape antibody recognition". (Sept. 2020). doi: 10.1101/2020.09.10.292078. [link](https://doi.org/10.1101/2020.09.10.292078).

[14] Amanda Harrington et al. "Comparison of Abbott ID Now and Abbott m2000 Methods for the Detection of SARS-CoV-2 from Nasopharyngeal and Nasal Swabs from Symptomatic Patients". In: *Journal of Clinical Microbiology* 58.8 (Apr. 2020). Ed. by Alexander J. McAdam. doi: 10.1128/jcm.00798-20. [link](https://doi.org/10.1128/jcm.00798-20).

[15] Resilience Health. "Resilience Health: Tests". 2020. [link](https://www.resiliencehealth.com/tests.html).

[16] (a) FDA HHS. "Rescission of Guidances and Other Informal Issuances". Aug. 2020. [link](https://www.hhs.gov/coronavirus/testing/recission-guidances-informal-issuances-premarket-review-lab-tests/index.html); (b) [annotation](https://hyp.is/T60DACeHEeukcedxY7hb2g/www.hhs.gov/coronavirus/testing/recission-guidances-informal-issuances-premarket-review-lab-tests/index.html).

[17] Julia Ioffe. "The Infuriating Story of How the Government Stalled Coronavirus Testing". 2020. [link](https://www.gq.com/story/inside-americas-coronavirus-testing-crisis).

[18] D. B. Jernigan et al. "Detecting 2009 Pandemic Influenza A (H1N1) Virus Infection: Availability of Diagnostic Testing Led to Rapid Pandemic Response". In: *Clinical Infectious Diseases* 52.suppl 1 (Jan. 2011), S36–S43. doi: 10.1093/cid/ciq020. [link](https://doi.org/10.1093/cid/ciq020).

[19] "JIMB CoViD-19 Standards working group". [link](https://jimb.stanford.edu/covid-19-standards).

[20] (a) Karen L. Kaul. "Laboratories and Pandemic Preparedness". In: *The Journal of Molecular Diagnostics* 22.7 (July 2020), pp. 841–843. doi: 10.1016/j.jmoldx.2020.05.002. [link](https://doi.org/10.1016/j.jmoldx.2020.05.002); (b) [annotation](https://hyp.is/zOQYVhkREeuspBd-tOlK8A/www.jmdjournal.org/article/S1525-1578(20)30326-3/pdf); (c) [annotation](https://hyp.is/anQ13BkdEeusbiMhG2DGew/www.jmdjournal.org/article/S1525-1578(20)30326-3/pdf); (d) [annotation](https://hyp.is/oFe9Oii-Eeuc4S_dbyDFNw/www.jmdjournal.org/article/S1525-1578(20)30326-3/pdf).

[21] Amy Maxmen. "Scientists baffled by decision to stop a pioneering coronavirus testing project". In: *Nature* (May 2020). doi: 10.1038/d41586-020-01543-x. [link](https://doi.org/10.1038/d41586-020-01543-x).

[22] (a) Frederick S. Nolte et al. "Responding to the Challenges of Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2)". In: *The Journal of Molecular Diagnostics* 22.8 (Aug. 2020), pp. 968–974. doi: 10.1016/j.jmoldx.2020.06.003. [link](https://doi.org/10.1016/j.jmoldx.2020.06.003); (b) [annotation](https://hyp.is/94iqCB9_EeuQCNcJXiV1IA/www.jmdjournal.org/article/S1525-1578(20)30360-3/fulltext); (c) [annotation](https://hyp.is/gTHBhB6_EeudDw8HxXC_sg/www.jmdjournal.org/article/S1525-1578(20)30360-3/fulltext); (d) [annotation](https://hyp.is/0rG_vCgrEeuRumtNauILPw/www.jmdjournal.org/article/S1525-1578(20)30360-3/fulltext).

[23] Rand Paul. "VITAL (Verified Innovative Testing in American Laboratories) Act of 2020". Mar. 2020. [link](https://www.congress.gov/bill/116th-congress/senate-bill/3512/text).

[24] "SARS-COV-2 diagnostic performance data". [link](https://finddx.shinyapps.io/COVID19DxData/).

[25] "SHIELDx - Harmonizing Standards Application to Accelerate Innovation". [link](https://mdic.org/wp-content/uploads/2020/02/SHIELD-Harmonizing-Standards-Application-to-Accelerate-Innovation.pdf).

[26] (a) Jeffrey Shuren and Timothy Stenzel. "Covid-19 Molecular Diagnostic Testing — Lessons Learned". In: *New England Journal of Medicine* 383.17 (Oct. 2020), e97. doi: 10.1056/nejmp2023830. [link](https://doi.org/10.1056/nejmp2023830); (b) [Traditional vs EUA annotation](https://hyp.is/WHCaiigbEeudVUcdtkaPAw/www.nejm.org/doi/10.1056/NEJMp2023830).

[27] (a) "State operations manual, Appendix C. Survey procedures and interpretive guidelines for laboratories and laboratory services, §493.1253". 2017. [link](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/som107ap_c_lab.pdf); (b) [New test annotation](https://hyp.is/V6fXvinMEeur7c_bYPXtXQ/www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/som107ap_c_lab.pdf).

[28] "Structured SARS-2 diagnostic data". [link](https://interventions.centerofci.org/pub/structured-sars-2-diagnostic-data).

[29] (a) "The SARS-CoV-2 genome: variation, implication and application". Aug. 2020. [link](https://royalsociety.org/-/media/policy/projects/set-c/set-c-genome-analysis.pdf); (b) [annotation](https://hyp.is/9tlYGB6uEeuYWEOCIUY17Q/royalsociety.org/-/media/policy/projects/set-c/set-c-genome-analysis.pdf).

[30] "Title 21-FOOD AND DRUGS, CHAPTER 9-FEDERAL FOOD, DRUG, AND COSMETIC ACT, SUBCHAPTER V-DRUGS AND DEVICES, Part E-General Provisions Relating to Drugs and Devices, §360bbb–3. Authorization for medical products for use in emergencies". [link](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title21-section360bbb-3&num=0&edition=prelim).

[31] "Title 42 Public Health, Chapter IV Centers for Medicare & Medicaid Services, Department of Health and Human Services, Subchapter G Standards and Certification, PART 493 - LABORATORY REQUIREMENTS, Subpart I - Proficiency Testing Programs for Nonwaived Testing, 493.901 Approval of proficiency testing programs, (b)(1)(ii)". [link](https://hyp.is/b1cQHCKUEeuRMnertWVt-w/ecfr.federalregister.gov/current/title-42/chapter-IV/subchapter-G/part-493).

[32] Manu Vanaerschot et al. "Identification of a polymorphism in the N gene of SARS-CoV-2 that adversely impacts detection by a widely-used RT-PCR assay". (Aug. 2020). doi: 10.1101/2020.08.25.265074. [link](https://doi.org/10.1101/2020.08.25.265074).

[33] (a) Jr. Wians Frank H. and Gary W. Gill. "Clinical and Anatomic Pathology Test Volume by Specialty and Subspecialty Among High-Complexity CLIA-Certified Laboratories in 2011". In: *Laboratory Medicine* 44.2 (May 2013), pp. 163–167. doi: 10.1309/LMPGOCRS216SVDZH. [link](https://doi.org/10.1309/LMPGOCRS216SVDZH); (b) [Claimed approximate number of CLIA-certified high-complexity laboratories in the US](https://hyp.is/GRQ0PFsGEeuZRYtChYD_7w/academic.oup.com/labmed/article/44/2/163/2657801); (c) [Percentage of labs with subspecialty in virology](https://hyp.is/Yha9RFsGEeurKYsSWIH69g/academic.oup.com/labmed/article/44/2/163/2657801).

[34] Y.-Z. Zhang et al. "Wuhan seafood market pneumonia virus isolate Wuhan-Hu-1, complete genome". 2020. [link](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1).

## 5 Revision History

- v0.1.9 - 2021 Jan 18th - Integrate feedback, gratefully received from Dr Alex Greninger, University of Washington School of Medicine.
- v0.1.8 - 2020 Nov 25th - Add 3 figures
- v0.1.7 - 2020 Nov 23rd - Typesetting polishing and readability
- v0.1.6 - 2020 Nov 19th - Typesetting polishing
- v0.1.5 - 2020 Nov 19th - Author affiliations
- v0.1.4 - 2020 Nov 19th - Add summary
- v0.1.0 - 2020 Nov 17th - First public version
