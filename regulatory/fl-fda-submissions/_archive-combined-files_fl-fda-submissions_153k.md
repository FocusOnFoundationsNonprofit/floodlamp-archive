# ===== START OF FILE _archive-combined-files_fl-fda-submissions_153k.md =====
# fl-fda-submissions (16 files, 152,810 tokens)

# 2,051  _context-commentary_regulatory-fl-fda-submissions.md
METADATA
last updated: 2026-03-02 RT
file_name: _context-commentary_regulatory-fl-fda-submissions.md
category: regulatory
subcategory: fl-fda-submissions
words: 1401
tokens: 2051


CONTENT

## Context
This subcategory contains FloodLAMP's FDA Emergency Use Authorization (EUA) submissions and associated Instructions for Use (IFU) documents for its SARS-CoV-2 diagnostic tests. There are 15 files spanning from November 2020 to October 2021, representing the full arc of FloodLAMP's regulatory submission effort. For background on the EUA framework itself and how it differs from standard 510(k) IVD approvals, see the FDA policy subcategory `regulatory/fda-policy`. For the correspondence with the FDA that accompanied these submissions, see `regulatory/fl-fda-correspondence`.

The subcategory documents four distinct test products and several ancillary submissions. The "QuickColor" test is the main FloodLAMP test, and one that was used for all of FloodLAMP's surveillance pilot programs. When the "FloodLAMP test" is used throughout the files in this archive, the QuickColor test is the one being referred to.

- **FloodLAMP Glass Milk LAMP Test** (Pre-EUA, November 2020): The earliest submission, a colorimetric RT-LAMP assay using silica ("glass milk") purification of nucleic acids from saliva and anterior nares swab specimens (from the Harvard Rabe-Cepko protocol). This was a pre-EUA — a preliminary package submitted to initiate FDA engagement and enter the review queue. It targeted asymptomatic screening with sample pooling at a baseline level of 10. The limit of detection (LoD) was 2 copies/uL (approximately 2,000 copies/mL).

- **FloodLAMP EasyPCR COVID-19 Test** (EUA Submission + IFU, v1.0 March 2021, v1.1 May 2021): An extraction-free, duplex RT-qPCR assay using the CDC N1 and human RNaseP primer-probe sets, with TCEP-based chemical inactivation and heat treatment. It required standard RT-PCR instruments (QuantStudio, Bio-Rad CFX96) but no nucleic acid extraction equipment. The LoD was 3,100 copies/mL. Clinical evaluation at Stanford showed 97.5% positive agreement and 100% negative agreement against a high-sensitivity comparator on 80 specimens.

- **FloodLAMP QuickColor COVID-19 Test** (EUA Submission + IFU, v1.0 March 2021, v1.1 May 2021, v1.2 draft October 2021): An extraction-free, colorimetric RT-LAMP assay with a visual pink-to-yellow readout requiring no specialized instrumentation. It used 18 LAMP primers targeting three SARS-CoV-2 genes (ORF1ab, N, E) and the same TCEP-based inactivation as the EasyPCR test. The LoD was 12,500 copies/mL. Clinical evaluation at Stanford showed 90% positive agreement and 100% negative agreement on 80 specimens. The v1.2 IFU introduced triplicate repeat procedures for inconclusive results.

- **FloodLAMP FLAMP (QuickFluor) COVID-19 Test** (EUA Submission + IFU draft, March 2021, NOT SUBMITTED): A fluorimetric RT-LAMP assay using real-time fluorescence readout on RT-PCR instruments. It used the same primers and inactivation as QuickColor but with fluorescent detection instead of colorimetric. The LoD was 50,000 copies/mL and clinical evaluation showed 80% positive agreement. This test was prepared but never submitted to the FDA.

- **Pooled Swab Collection and Screening Studies** (Pre-EUA submissions, May 2021): Three documents supporting FloodLAMP's pooling and asymptomatic screening strategy — a pre-EUA for a direct-to-consumer pooled swab collection kit (allowing 1–4 self-collected anterior nasal swabs in a single tube), collection kit instructions, and a proposed validation study design for pooling and serial asymptomatic screening aligned to FDA guidance.

Each submission follows the FDA's EUA template structure: purpose, measurand, applicant information, regulatory status, proposed intended use, device description and test principle, controls, interpretation of results, manufacturing and component sourcing, and performance evaluation (LoD, inclusivity, cross-reactivity, interfering substances, clinical evaluation). The IFU documents mirror much of this content in an operational format for laboratory use.

All of FloodLAMP's tests shared a common TCEP-based chemical inactivation step and were designed as "open source protocol" tests — meaning designated CLIA high-complexity laboratories could source all components directly from commercial vendors rather than purchasing proprietary kits. This open-source approach is central to FloodLAMP's strategy, as documented in the `regulatory/open-euas` subcategory. The EasyPCR and QuickColor tests were designed to work as an integrated pair: QuickColor for high-throughput colorimetric screening (45-minute turnaround, no instruments) and EasyPCR for rapid PCR-based confirmation (~1 hour 45 minutes). New England Biolabs supported both tests with their LAMP master mix and Luna RT-qPCR kit, and LGC Biosearch Technologies supplied production-scale LAMP primer sets.

The submissions evolved across versions. The v1.0 submissions (March 2021) proposed intended use for "individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval." The v1.1 submissions (May 2021) reframed the intended use around "routine screening programs" in settings like schools and workplaces. None of these submissions received FDA authorization.


## Commentary
The primary commentary for submissions is combined with the correspondence category — see `regulatory/fl-fda-correspondence/_context-commentary_regulatory-fl-fda-correspondence.md` regarding FloodLAMP's FDA engagement. Here are comments on the more technical aspects of the EUA submission process.

The EUA submission process involves two main types of documents: the submission itself and the Instructions for Use (IFU). The submission is the regulatory document — it follows the FDA's structured template with sections covering purpose, measurand, intended use, device description, performance evaluation, manufacturing, and so on. The IFU is the operational document intended for the laboratories that will run the test. They overlap substantially in content, but serve different audiences and purposes. Both must be prepared and aligned, and both are substantial documents. For FloodLAMP, each test's submission ran 5,000–10,000 words, and each IFU ran 7,000–14,000 words.

A critical concept in understanding these documents is that the FDA authorizes test systems, not tests in isolation. The entire system — reagents from specific vendors, validated instruments, the exact workflow, controls, and interpretation criteria — is what receives authorization. Changing a single component can require revalidation. For open-source protocol tests like FloodLAMP's, this posed an inherent tension: the whole point was to enable broad deployment using commodity components from multiple suppliers, but the regulatory framework required specificity at every level. FloodLAMP addressed this by validating multiple instruments (QuantStudio 6 Flex, QuantStudio 7 Pro, Bio-Rad CFX96) and multiple primer and probe vendors (Eurofins Genomics, IDT, LGC Biosearch) within a single submission.

The bench science for EUA validation can actually move quite fast. In a conversation with another test developer — an academic who started a company during the pandemic and did obtain an EUA — they described doing the core validation work in a weekend. The bottleneck is not the assay work itself but the surrounding logistics and documentation. For FloodLAMP, the single biggest delay was getting registered with BEI Resources to obtain the cross-reactivity reagents. The FDA requires testing against a panel of related pathogens and respiratory flora, and BEI is the primary source for those reference organisms. The registration and shipping process takes weeks, and for a small organization running lean, that waiting period was a significant constraint.

Even with the FDA's templates available, the document preparation is a heavy lift for anyone who has not done it before. FloodLAMP benefited from other groups sharing their actual EUA submission documents — these are not published, and they differ in important ways from the public-facing authorizations and IFUs that appear on the FDA website. Having real examples was helpful for understanding the level of detail and the conventions that the templates alone do not fully convey. If the FDA allowed or facilitated sharing of these submissions, for example, by simply letting developers choose to publish their submissions openly, some likely would, especially academics. This would meaningfully lower the barrier for new entrants.
Even with the FDA's templates available, the document preparation is a heavy lift for anyone who has not done it before. FloodLAMP benefited from other groups sharing their actual EUA submission documents — these are not published, and they differ in important ways from the public-facing authorizations and IFUs that appear on the FDA website. Having real examples was helpful for understanding the level of detail and the conventions that the templates alone do not fully convey. If the FDA allowed or facilitated sharing of these submissions, for example, by simply letting developers choose to publish their submissions openly, some likely would, especially academics. This would meaningfully lower the barrier for new entrants.

The new capabilities of AI could transform the document preparation burden. The EUA submission and IFU are highly structured, repetitive across test types, and draw heavily on standardized language. With progress on standardization and transparency from the FDA — such as machine-readable templates, published example submissions, and clearer guidance on what constitutes acceptable variations — AI tools could handle much of the drafting, cross-referencing, and consistency-checking that currently consumes weeks of a developer's time. The combination of AI and regulatory modernization could significantly reduce the cost and time to bring validated, innovative tests to market.


# 4,273  2020-11-06_Pre-EUA Sub - FloodLAMP Glass Milk LAMP Test.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2020-11-06_Pre-EUA Sub - FloodLAMP Glass Milk LAMP Test.md
file_date: 2020-11-06
title: Pre-EUA Sub - FloodLAMP Glass Milk LAMP Test
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/17NMbkJOYgDgA1mdlawn10Hw3067GZ1wI
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2020-11-06_Pre-EUA%20Sub%20-%20FloodLAMP%20Glass%20Milk%20LAMP%20Test.docx
pdf_gdrive_url: https://drive.google.com/file/d/1pvKMujtiyxrQ7_OwkXEO6Uy4m4ejGY6_
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2020-11-06_Pre-EUA%20Sub%20-%20FloodLAMP%20Glass%20Milk%20LAMP%20Test.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 4273
words: 2263
notes: 
summary_short: The Pre-EUA Sub - FloodLAMP Glass Milk LAMP Test (Nov 6, 2020) is a Molecular Diagnostic Template submission for laboratory use that defines the intended use, measurand, and workflow for a pooled, colorimetric RT-LAMP SARS-CoV-2 test using chemical inactivation plus “glass milk” silica purification for saliva and anterior nares samples in high-complexity CLIA labs. It compiles key regulatory details, validated reagents and prepared solutions, step-by-step procedures, controls, result interpretation criteria, and early performance data (including LoD) to support an EUA pathway for asymptomatic screening and pooling.


CONTENT

***INTERNAL TITLE:*** Molecular Diagnostic Template for Laboratories
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for use of FloodLAMP to be performed for the in vitro qualitative detection of RNA from the SARS-CoV-2 in anterior nares swab specimens and saliva samples from individuals \[suspected of COVID-19 by their healthcare provider\]\[as recommended for testing by public health authority guidelines for screening of asymptomatic individuals\]. FloodLAMP will be performed in CLIA-certified, high-complexity laboratories. Additional testing and confirmation procedures should be performed in consultation with public health and/or other authorities to whom reporting is required. Positive results should also be reported in accordance with local, state, and federal regulations.

## B. MEASURAND
Specific nucleic acid sequences in the ORF1a and nucleocapsid genes of SARS-CoV-2, targeted by the As1e and N2 primer sets.

## C. LABORATORY/SPONSOR 
Randall J. True
Founder and CEO
FloodLAMP Biotechnologies, a DE Public Benefit Corporation
Phone: (415) 269-2974
Email: randy@floodlamp.bio

Mailing Address:
4860 Alpine Rd.
Portola Valley, CA 94028

Laboratory Address:
FloodLAMP.bio at MBC Biolabs
San Carlos, CA 94070

## D. REGULATORY INFORMATION
***Approval/Clearance Status:***

FloodLAMP is not cleared, CLIA-waived, approved, or subject to an approved investigational device exemption.

***Product Code:***

QJR

## E. PROPOSED INTENDED USE
### 1) Intended Use:
The FloodLAMP Glass Milk Test is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) test intended for the qualitative detection of RNA from SARS-CoV-2 in saliva and anterior nares (nasal) swab specimens. Testing is limited to screening of asymptomatic individuals. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories. [Sample pooling is at a baseline level of 10, with on-site and at-home modalities. Pooling of pools to levels greater than 10 will be investigated pending LoD determination and validation studies.]{.mark}

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all positive results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information. FloodLAMP Glass Milk Test is intended to be used on normal and clear saliva that naturally forms in the mouth, not for other lower respiratory tract specimens such as sputum.

The assay is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of real-time PCR and in vitro diagnostic procedures. The assay is only for use under the Food and Drug Administration's Emergency Use Authorization.

Use of the FloodLAMP Glass Milk Test in a general, asymptomatic screening population is intended to be used as part of an infection control plan, that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should be considered presumptive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual's recent exposures, history, presence of clinical signs and symptoms consistent with COVID-19.

### 2) Reagents Used with Test:
The FloodLAMP Glass Milk test is to be used with the following reagents and no specialized instruments. Only ordinary laboratory equipment such as pipettes, centrifuges, and heaters are needed.

#### Table 1: Validated reagents used with Test
|Item|Chemical Composition|Vendor|Catalog number|
|---|---|---|---|
|TCEP|tris(2-carboxyethyl)phosphine hydrochloride|Sigma-Aldrich Millipore Sigma|646547-10X1ML 580567|
|EDTA|Ethylenediaminetetraacetic acid|Thermo Fisher|15575020|
|NaOH|Sodium Hydroxide|Sigma-Aldrich|SX0607N-6|
|Ultrapure Water|Ultrapure Water, DNAse RNAse free|Thermo Fisher|10977015|
|Tris-HCl|TRIS hydrochloride, 1M pH 8.0|Thermo Fisher|AM9855G|
|TE Buffer|TRIS hydrochloride (10mM) and EDTA (1mM)|Sigma-Aldrich|93283|
|1X PBS|monobasic potassium phosphate, sodium chloride, and dibasic sodium phosphate|Thermo Fisher|10010049|
|NaI|Sodium iodide|Sigma-Aldrich|793558|
|HCl|Hydrochloric acid|Sigma-Aldrich|320331|
|Triton X-100|t-Octylphenoxypolyethoxyethanol|Sigma-Aldrich|T8787-50ML|
|Silica|Silicon Dioxide, 325 Mesh|Sigma-Aldrich|SI108|
|Guanidine|Guanidine Hydrochloride|Sigma-Aldrich|SRE0066|
|LAMP MM|Colorimetric LAMP Master Mix|NEB|M1804|
||

### 3) Prepared Solutions Used with Test:
#### Table 2: Inactivation Solution
|Component|Concentration|Volume|
|---|---|---|
|TCEP|0.5 M|10 mL|
|EDTA|0.5 M|4 mL|
|NaOH|10 N|2.3 mL|
|Ultrapure Water| |3.7 mL|
Final Volume 20 mL
||

#### Table 3: Binding Solution
|Component|Concentration|Volume / Mass|
|---|---|---|
|NaI| |45 g|
|Ultrapure Water| |to 48.5 mL|
|HCl|1 N|0.5 mL|
|Triton X-100| |1.0 mL|
Final Volume 50 mL
||

#### Table 4: Glass Milk - Under Development
|Component|Concentration|Volume / Mass|
|---|---|---|
|Silica| |500 g|
|HCl|10%|100 mL|
|dH20| |2400 mL|
|TE Buffer| |500 mL|
|Final Volume 200 mL|
||

#### Table 5: Primers used for FloodLAMP \"AN\" Primer Mix
|Target|Primer|Sequence|
|---|---|---|
|As1e|As1e_FIP|TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG|
| |As1e_BIP|TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG|
| |As1_F3|CGGTGGACAAATTGTCAC|
| |As1_B3|TTACAAGCTTAAAGAATGTCTGAACACT|
| |As1_LF|TTACAAGCTTAAAGAATGTCTGAACACT|
| |As1_LB|TTGAATTTAGGTGAAACATTTGTCACG|
|N2|N2-FIP|TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC|
| |N2-BIP|CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA|
| |N2-F3|ACCAGGAACTAATCAGACAAG|
| |N2-B3|GACTTGATCTTTGAAATTTGGATCT|
| |N2-LF|GGGGGCAAATTGTGCAATTTG|
| |N2-LB|CTTCGGGAACGTGGTTGACC|
||

#### Table 6: 10X Primer Mix
|Primer|Volume (400 reactions)|
|---|---|
|As1e_FIP (100uM)|160 μL|
|As1e_BIP (100uM)|160 μL|
|As1_F3 (100uM)|20 μL|
|As1_B3 (100uM)|20 μL|
|As1_LF (100uM)|40 μL|
|As1_LB (100uM)|40 μL|
|N2-FIP (100uM)|160 μL|
|N2-BIP (100uM)|160 μL|
|N2-F3 (100uM)|20 μL|
|N2-B3 (100uM)|20 μL|
|N2-LF (100uM)|40 μL|
|N2-LB (100uM)|40 μL|
|Add Ultrapure Water|120 μL|
|Final Volume 1000 μL|
||

#### Table 7: Primer Solution
|Component|Volume (1 reaction)|Volume (100 reactions)|
|---|---|---|
|Ultrapure Water|7.5 μL|750 μL|
|Guanidine (400 mM)|2.5 μL|250 μL|
|10X Primer Mix|2.5 μL|250 μL|
|Final Volume 1250 mL|
||

## F. DEVICE DESCRIPTION AND TEST PRINCIPLE
### 1) Product Overview/Test Principle:
The FloodLAMP Glass Milk Test is a method for SARS-CoV-2 detection that comprises 3 steps: 1) sample inactivation and preservation, 2) nucleic acid purification and concentration, and 3) colorimetric RT-LAMP amplification. It can be broadly implemented as it (1) utilizes very low cost, readily available bulk reagents for inactivation and purification, (2) does not require any instrumentation for assay processing or readout, and (3) has high sensitivity enabling sample pooling to be utilized. Thus, the low cost and low barrier to deployment of the FloodLAMP Glass Milk Test means that it can scale quickly to very high levels.

### 2) Description of Test Steps: 
#### Sample Inactivation
Starting with raw saliva or anterior nares swab extract:

1.  100X Inactivation Solution is added to sample.

2.  Sample is vortexed to mix.

3.  Sample is heated in 95°C water bath or dry heat block for 8 minutes.

4.  Sample is placed on ice for at least 4 minutes.

5.  Sample is spun in centrifuge at 5krpm for 4 minutes.

6.  Top 90% of the sample is transferred to a new tube for subsequent processing and/or storage.

7.  Store samples at 2-8°C until sample transport or processing (up to 72 hours) or at -20°C for 2-4 weeks, or at -80°C for longer term storage.

#### Glass Milk Purification
1.  Glass Milk is added to the Binding Solution at a ratio of 1:50.

2.  Glass Milk + Binding Solution is vortexed to mix.

3.  255 µL of Mixture is added to 500 µL of sample, in 1.5 mL microcentrifuge tubes or in wells of a deepwell plate.

4.  Sample is incubated for 10 minutes, with periodic mixing.

5.  Sample is spun down for 1 minute to pellet glass milk.

6.  Supernatant is removed.

7.  80% Ethanol is added and then removed to wash pellet and perform liquid exchange.

8.  100 µL of 80% ethanol is added, pellet resuspended and resuspension transferred to 200 µL PCR tubes (either to strips of 8 PCR tubes or to a PCR plate).

9.  Strips are capped (plates sealed) and spun down.

10. Supernatant is removed.

11. Tubes (plate) with nucleic acid bound silica pellet is placed on a 65°C heat block and heated for 5 minutes or until pellets have dry, chalky appearance.

#### LAMP Amplification
1.  On ice or in cold block, prepare LAMP Reaction Mix by combining 12.5 µL per reaction LAMP Master Mix (NEB 1804) with 12.5 µL of Primer Solution (per reaction: 7.5 µL water, 2.5 µL 400 mM Guanidine Hydrochloride , 2.5 µL 10X Primer Mix).

2.  25 µL of LAMP Reaction Mix is added directly to dried pellet in each PCR tube.

3.  Mix by pipette (avoid bubbles).

4.  Cap strip tubes (seal plate).

5.  Incubate on hot plate with PCR Tube dry block at 65°C for 25 minutes.

6.  Remove strip tubes (plate) and let cool for 2 minutes.

7.  Visually read the result by color of the PCR tube.

### 3) Control Material(s) to be Used:
Controls will be included with every batch of samples run.

#### Table 8: Purpose and frequency of controls to be used with Test
|Control|Purpose|Frequency|
|---|---|---|
|Negative Control|To monitor for contamination during sample processing|Every batch of up to 93 samples|
|Positive Control|To monitor functioning of reagents|Every PCR plate with up to 93 samples or batch of strip tubes|
||

1X Phosphate Buffered Saline + Inactivation Solution is used as a negative control (no template control). 1X Phosphate Buffered Saline + Inactivation Solution + Spike (Zeptometrix Inactivated Virions, BEI Cell Lysate, or Twist synthetic SARS-CoV-2 RNA) is used as positive control (**see Controls in Supporting Data**).

### 4) Assay results and interpretation: 
All test controls should be examined prior to interpretation of patient results. If the controls are not valid, the sample results cannot be interpreted. Results will be interpreted according to **Table 9**.

#### Table 9: Test results and interpretation 
|Outcome|Color|
|---|---|
|Positive|Yellow|
|Negative|Pink|
|Invalid|Orange|
||

#### Table 10: Image of Acceptable Binary Test results**
![][image1]

Invalid test results will be retested by repeating the purification and amplification on the inactivated sample. Results from retested samples will follow the same interpretation as listed in **Table 9**.

## G. PERFORMANCE EVALUATION
### 1) Limit of Detection (LoD) - Analytical Sensitivity:
Specimens from presumed negative participants were collected and spiked with Zeptometrix inactivated virions prior to the inactivation step. This contrived positive sample was diluted in presumed negative inactivated samples to achieve the target concentrations for LoD assay runs (see **Table 10 and Supporting Data**).

#### Table 10: Limit of detection of Test
|Concentration (copies/µL)|Positive Samples Detected|
|---|---|
|4|100% (20/20)|
|2|100% (19/19)|
||

As a part of the Xprize Rapid Test Competition, \"proficiency plates\" consisting of 157 blinded samples were run with the FloodLAMP Glass Milk Test. Purification was performed in deepwell plates and processing was performed with multichannel pipettes. Hands-on time per plate was approximately 1 hour. The Xprize samples were smaller volumes (100-200 µL) than typically used for the FloodLAMP Glass Milk Test (500 µL) and were not inactivated with the same TCEP Inactivation Solution. Notwithstanding these caveats, LoD and cross reactivity determination will be available after the results data is scored.

Below is an image of a completed FloodLAMP Glass Milk Test plate, including 8 alternating positive and negative controls in well positions H5-12.

![][image2]

### 2) Inclusivity (analytical sensitivity): TBD 
In silico inclusivity analysis to be performed by mapping the primers and probes to the complete SARS-CoV-2 genomes that are available in the current GISAID (Global Initiative on Sharing All Influenza Data) database. The rate of mismatches will be calculated and potential for amplification failure analyzed.

### 3) Cross-reactivity (analytical specificity): TBD
In silico cross reactivity analysis to be performed by aligning the primer sequences against sequences of coronaviruses related to SARS-Cov-2, as well as commonrespiratory pathogens. If any organisms show \>80% overall match for the primer sets, wet testing of the following will be performed.

NR-52346 Quantitative PCR (qPCR) Control RNA from Inactivated SARS Coronavirus
NR-44228 Human respiratory syncytial virus , Genomic RNA from Human Respiratory Syncytial Virus, A1998/12-21
NR-45848 Genomic RNA from Influenza B Virus, B/Nevada/03/2011 (Victoria Lineage)
NR-49122 Genomic RNA from Human Metapneumovirus, TN/83-1211
HM-121 Streptococcus salivarius SK126

### 4) Clinical Evaluation:
**Clinical specimens**
The FloodLAMP Glass Milk Test has been performed on a single clinical positive saliva sample, however no concentration or comparator Ct values were available. The nucleic acid bound pellet was split evenly and the standard FloodLAMP Glass Milk Test colorimetric LAMP reaction was run on one set of 8 (duplicates of clinical positive and 6 controls) and the fluorimetric LAMP reaction (NEB E1700) was run on the 2nd set of 8 using an ABI QuantStudio 7 qPCR machine. SARS-CoV-2 was detected for the clinical positive samples in both sets, with expected results from all controls.

![][image3]

*/thanks to collaborators at Montana St Univ, Chang & Keil

## H. UNMET NEED ADDRESSED BY THE PRODUCT 
*This section will be completed by FDA.*

## I. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for the detection of the SARS-CoV-2 have been approved/ cleared by FDA.

## J. BENEFITS AND RISKS
*This section will be completed by FDA.*

## K. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS
Include proposed Fact Sheets for Patients and Healthcare Providers - *see examples for authorized EUA tests on our website and templates will be made available.*

## L. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT
In lieu of a package insert or labeling please include your Laboratory SOP/protocol.

## M. RECORD KEEPING AND REPORTING INFORMATION TO FDA
The laboratory will track adverse events and report to FDA under 21 CFR Part 803. A website is available to report on adverse events, and this website is referenced in the Fact Sheet for Health Care providers. The laboratory will maintain information on the performance of the test, and report to FDA any suspected change in performance of which they become aware. The laboratory will maintain records associated with this EUA and ensure these records are maintained until notified by FDA. Such records will be made available to FDA for inspection upon request.


# 9,057  2021-03-22_EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.0.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-03-22_EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.0.md
file_date: 2021-03-22
title: EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.0
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1xwO9T_T6XRCow_941mS-ylJI9VvL3yCb
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-03-22_EUA%20Submission%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.0.docx
pdf_gdrive_url: https://drive.google.com/file/d/1-2gpnYSgfG6f8OUmL5_OXBBWpXlJ4lB9
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-03-22_EUA%20Submission%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.0.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 9057
words: 5454
notes: 
summary_short: The EUA Submission for the FloodLAMP EasyPCR COVID-19 Test v1.0 details an extraction-free, duplex RT-qPCR assay for qualitative SARS-CoV-2 detection in upper respiratory swab specimens, including proposed intended use for routine weekly screening in asymptomatic individuals. It specifies the CDC N1 and RNaseP targets, validated instruments, sample inactivation workflow, controls and interpretation criteria, and manufacturing/sourcing assumptions for an “open source” CLIA high-complexity lab deployment. It summarizes analytical and clinical performance claims including a 3,100 copies/mL LoD and clinical agreement results from an 80-specimen evaluation.


CONTENT

***INTERNAL TITLE:*** EUA Submission - FloodLAMP EasyPCR(TM) COVID-19 Test
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for distribution and/or use of the **FloodLAMP EasyPCR(TM) COVID-19 Test** for the *in vitro* qualitative detection of RNA from the SARS-CoV-2 in in upper respiratory specimens including oropharyngeal and nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests.** Additional testing and confirmation procedures should be performed in consultation with public health and/or other authorities to whom reporting is required. Test results should be reported in accordance with local, state, and federal regulations.

## B. MEASURAND
Specific nucleic acid sequences from the genome of the SARS-CoV-2, targeted by the previously certified **2019-nCoV\_N1 primers and probe set as part of the CDC qPCR assay**. Primer names and sequences are listed in Table 1.

#### Table 1: Primers and probes
|              |                  |                                           |
|---------------|------------------|----------------------------------------|
| **Target**   | **Primer/Probe** | **Sequence**                              |
| CDC-N1       | 2019-nCoV\_N1-F  | GACCCCAAAATCAGCGAAAT                      |
| CDC-N1       | 2019-nCoV\_N1-R  | TCTGGTTACTGCCAGTTGAATCTG                  |
| CDC-N1       | 2019-nCoV\_N1-P  | **FAM**-ACCCCGCATTACGTTTGGTGGACC-**IBFQ** |
| Human RNAseP | RP-F             | AGATTTGGACCTGCGAGCG                       |
| Human RNAseP | RP-R             | GAGCGGCTGTCTCCACAAGT                      |
| Human RNAseP | RP-P             | **Cy5**-TTCTGACCTGAAGGCTCTGCGCG-**IBRQ**  |
||

## C. APPLICANT
FloodLAMP Biotechnologies, a DE Public Benefit Corporation
| Mailing Address: 4860 Alpine Rd. Portola Valley, CA 94028 | Laboratory Address: 930 Brittan Ave San Carlos, CA 94070	 | Randall J. True, CSO Phone: (415) 269-2974 Email: randy@floodlamp.bio |
| :---- | :---- | :---- |

## D. PROPRIETARY AND ESTABLISHED NAMES
Proprietary Name - **FloodLAMP EasyPCR(TM) COVID-19 Test**
Established Name - **FloodLAMP EasyPCR(TM) COVID-19 Test**
 
## E. REGULATORY INFORMATION
***Approval/Clearance Status:***
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is not cleared, CLIA waived, approved, or subject to an approved investigational device exemption.

***Product Code:***
QJR
 
## F. PROPOSED INTENDED USE
### 1) Intended Use:
**FloodLAMP EasyPCR(TM) COVID-19 Test** is a real-time reverse transcriptase polymerase chain reaction (RT-PCR) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests.** Testing is limited to **laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories.**

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The **FloodLAMP EasyPCR(TM) COVID-19 Test** is intended for use by **qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of in vitro diagnostic procedures**. The **FloodLAMP EasyPCR(TM) COVID-19 Test** is only for use under the Food and Drug Administration’s Emergency Use Authorization.

### 2) Special Conditions for Use Statements:
For Emergency Use Authorization (EUA) only
For prescription use only
For in vitro diagnostic use only

### 3) Special Instrument Requirements:
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is to be used with the RT-PCR instruments listed in Table 2.

#### Table 2. RT-PCR Instruments validated for test
|  |  |
|----------------------|--------------------------------------------------|
| **Manufacturer** | **Instrument** |
| Thermo Fisher Scientific | Applied Biosystems QuantStudio(TM) 6 Flex |
| Thermo Fisher Scientific | Applied Biosystems QuantStudio(TM) 7 Pro |
| Bio-Rad | CFX96 Touch(TM) Real-Time PCR Detection System |
||

Designated laboratories will receive an FDA accepted instrument qualification protocol included as part of the **FloodLAMP EasyPCR(TM) Covid-19 Test** IFU and will be directed to execute the protocol prior to testing clinical samples. Designated laboratories must follow the authorized IFU, which includes the instrument qualification protocol, as per the letter of authorization.

## G. DEVICE DESCRIPTION AND TEST PRINCIPLE
### 1) Product Overview/Test Principle:
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is a RNA extraction-free, duplexed RT-qPCR assay which indicates whether SARS-CoV-2 RNA is present. It can widely and rapidly be scaled because 1) it does not require nucleic acid extraction equipment, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a very straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the **FloodLAMP QuickColor(TM) COVID-19 Test**. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Further, the **FloodLAMP QuickColor(TM) COVID-19 Test** is isothermal, does not require any instrumentation and has a visual readout. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

In the **FloodLAMP EasyPCR(TM) COVID-19 Test,** samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step, and the resulting inactivated sample is directly used as input in the duplexed RT-qPCR test. The test does not use new primers and probes for RT-qPCR testing, but rather uses previously validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC, which are readily available from multiple commercial suppliers. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, reducing the number of tests to 1 assay with 2 targets.

### 2) Description of Test Steps: 
Specimens including **nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs** are collected in **sterile collection tubes.** Swabs are transported and stored dry prior to processing. At the laboratory, an inactivation solution at 1X containing TCEP (2.5 mM), EDTA (1 mM), and NaOH (11 mM) in 0.9% saline (154 mM) is added to the container with the swab, at the volume of 1 ml. Alternatively, for swabs that are collected or eluted in a saline solution or equivalent, the inactivation solution at 100X concentration should be added at 1/100th the sample solution volume.

The container with the specimen and inactivation solution is mixed by vortexing for 30 seconds. Subsequently, the container is heated in a 95°C water bath or dry heat block for 8 minutes. The now inactivated specimen container is allowed to cool at room temperature for 10 minutes and then stored on ice or at 4°C until amplification.

An amplification reaction mix (18 µl) is prepared per manufacturer's specifications, containing the New England Biolabs LunaⓇ PCR Master Mix (New England Biolabs E3006, 10 µl), New England Biolabs LunaⓇ RT (New England Biolabs E3006, 1 µl), a primer solution (4 µl of 5X PCR primer stock w/ N1-F & N1-R at 2 µM, N1-P & RP-P at 1 µM and RP-F & RP-R at 0.75 µM), and nuclease-free water (3 µl).

2µl of the inactivated sample is added to 18µl of the amplification reaction mix. The reaction is then run with the following thermocycler conditions in Table 3:

#### Table 3: Thermal cycling conditions and plate read steps 
|          |                 |          |          |
|----------|-----------------|----------|----------|
| **Step** | **Temperature** | **Time** | **Reps** |
| 1        | 52°C            | 10 min   | 1        |
| 2        | 95°C            | 2 min    | 1        |
| 3        | 95°C            | 10 sec   | 44       |
|     3     | 55°C\*          | 30 sec   |     44     |
||

*\* This step should be the optical read step*

### 3) Control Materials to be Used with FloodLAMP EasyPCR(TM) COVID-19 Test:
**One Positive Template Control and one Negative (No Template) Control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes. An **Internal Process Control** is included in every PCR reaction.

1.  A **“No Template” (Negative) Control (NTC) is needed to assure the absence of cross-contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of nuclease-free water.**

2.  A **Positive Template Control is needed to assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 4 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at -80°C, or at most 1 month at -20°C.

3.  **An Internal Process Control is needed to assure sufficient specimen quantity and quality**. It consists of a primer/probe set targeting the human RNaseP gene that is included in a single PCR amplification reaction. The RNAseP Internal Process Control uses a fluorescent reporter in a separate channel from the SARS-CoV-2 channel (i.e. in duplex).

#### Table 4. Components for Positive Template Control 
|                                |               |                |            |
|--------------------------------|---------------|----------------|------------|
| **Material**                   | **Supplier**  | **Catalog \#** | **Volume** |
| SARS-CoV2 Positive Control RNA | Twist         | 102019         | 5 µL       |
| Total Human RNA                | Thermo Fisher | 4307281        | 100 µL     |
| Nuclease-free Water            | Thermo Fisher | 10977015       | 4,895 µL   |
||
 
## H. INTERPRETATION OF RESULTS
### 1) FloodLAMP EasyPCR(TM) COVID-19 Test Controls 
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to Table 5 below.

1.  The “No Template” (Negative) Control (NTC) should yield a negative “not detected” result for both the N1 and RNaseP targets.

2.  The Positive Template Control should yield a positive “detected” result for the N1 target and a negative “not detected” for the RNaseP control.

3.  The Internal Process Control should yield a positive "detected" result for RNaseP. Detection of RNaseP is required to report a negative SARS-CoV-2 result.

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP(TM) product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### 2) Examination and Interpretation of Patient Specimen Results:
Assessment of clinical patient specimen test results should be performed after the positive, negative, and internal controls have been examined and determined to be valid and acceptable. If the controls are not valid, the patient results cannot be interpreted. Patient specimen results will be interpreted according to Table 5 below.

#### Table 5: Interpretation of Patient Specimen Results
| ABI QuantStudio(TM) 7 Pro |  |  |
| :---: | :---: | :---: |
| **Result** | **Ct Value: N1** | **Ct Value: RP** |
| Positive | \<38.0 | Any Value |
| Negative | ≥38.0 | \<35.0 |
| Invalid | ≥38.0 | ≥35.0 |
| **Bio-Rad CFX96 Touch(TM) ABI QuantStudio(TM) 6 Flex** |  |  |
| **Result** | **Ct Value: N1** | **Ct Value: RP** |
| Positive | \<40.0 | Any Value |
| Negative | ≥40.0 | \<35.0 |
| \*Invalid | ≥40.0 | ≥35.0 |
||

\*Invalid test results will be repeated by rerunning the primary sample if available, otherwise by rerunning the inactivated sample. Results from retested samples will follow the same interpretation as listed in Table 5.

If the final interpretation of the test result is invalid, then "Invalid/Inconclusive" should be reported and retesting of the individual is recommended.

## I. PRODUCT MANUFACTURING
### 1) Overview of Manufacturing and Distribution: 
The **FloodLAMP EasyPCR(TM) COVID-19 Test** utilizes standard chemicals available from multiple vendors, with the exception of the New England Biolabs LunaⓇ Universal Probe One-Step RT-qPCR Kit.

The **FloodLAMP EasyPCR(TM) COVID-19 Test** utilizes the same primer and probes as the EUA authorized SalivaDirect(TM) test, which derive from the CDC primer set. These are available in very large quantities with immediate distribution from multiple vendors including Eurofins Genomics, Integrated DNA Technologies, and LGC Biosearch.

New England Biolabs has expressed strong support for the **FloodLAMP EasyPCR(TM) COVID-19 Test** and FloodLAMP's other open source protocol EUA submissions that incorporate their products. New England Biolabs has very large quantities of the LunaⓇ Universal Probe One-Step RT-qPCR Kit prepared and ready for immediate distribution, typically with 24 hour shipping. Their manufacturing capacity is among the largest in the United States and can surge to meet increased demand.

**\*Under the Emergency Use Authorization (EUA) any of the 21 CFR Part 820 Quality System Regulation (QSR) requirements can be waived for the duration of the EUA but FDA recommends that developers follow comparable practices as much as possible if such requirements are waived. Among other things, FDA may consider previous compliance history when determining whether or not to waive certain QSR requirements for a specific product. Please note adverse events, as per 21 CFR Part 803, have to be reported for authorized devices (see Section P).**

### 2) Components Included with the Test
None. Designated CLIA labs may order components directly from vendors.

### 3) Components Required But Not Included with Test:
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is to be used with the following reagents or equivalents listed in Table 6.

#### Table 6: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | ----- | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-freeWater |  | Ultrapure Water, DNAse RNAse free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| PCR MasterMix \* | - | 2X PCR Master Mix (in LunaⓇ Universal Probe One-Step RT-qPCR Kit) | New England Biolabs | E3006 |
| PCR RT \* | - | Reverse Transcriptase (in LunaⓇ Universal Probe One-Step RT-qPCR Kit) | New England Biolabs | E3006 |
||

\* Item may not be substituted for equivalents. Only the specified vendor and catalog number may be utilized.

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

The 100X Inactivation Solution is prepared by mixing the components in Table 7. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved.

#### Table 7: 100X Inactivation Solution
|  |  |  |  |
|------------------|--------------------|----------------|------------------|
| **Component** | **Source Concentration** | **Volume** | **100X Concentration** |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 8. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 8: 1X Inactivation Saline Solution
|                            |             |
|----------------------------|-------------|
| **Component**              | **Volume**  |
| 0.9% Saline (154 mM NaCl)  | 1000 mL     |
| 100X Inactivation Solution | 10 mL       |
| **TOTAL VOLUME**           | **1010 mL** |
||

The **FloodLAMP EasyPCR(TM) COVID-19 Test** uses the validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, detecting the 2 targets in a single well. This configuration is described in the SalivaDirect(TM) EUA Authorized test ([www.fda.gov/media/141192/download](http://www.fda.gov/media/141192/download)).

The complete set of 6 primers and probes may be purchased from the vendor Eurofins Genomics using the catalog number 12YS-010YST. This product contains primers and probes suspended at 100µM and is enough for 12,500 reactions. The contents can be mixed along with nuclease-free water to create the primer stocks used in the **FloodLAMP EasyPCR(TM) COVID-19 Test**. See Table 9 below for details. A large volume of primer-probe stock can be prepared in advance and stored at 4 oC for one month or -20 oC for up to 1 year. Vendors for the Primer and Probe sets are below in Table 10.

#### Table 9: 5X PCR Primer Stock Preparation from Eurofins Genomics Product
|  |  |  |
|-----------------------------|----------------------|---------------------|
| **Component (final concentration)** | **Volume (1 reaction)** | **Volume (3,125 reactions)** |
| 2019-nCov\_N1-F (10 µM) | 0.4 µl | 1,250 µl |
| 2019-nCov\_N1-R (10 µM) | 0.4 µl | 1,250 µl |
| 2019-nCov\_N1-P (5 µM) | 0.2 µl | 625 µl |
| RP-F (3.75 µM) | 0.15 µl | 469 µl |
| RP-R (3.75 µM) | 0.15 µl | 469 µl |
| RP-P (5 µM) | 0.2 µl | 625 µl |
| Nuclease-free water | 2.5 µl | 7,813 µl |
| **TOTAL VOLUME** | **4 µl** | **12,500 µl** |
||

#### Table 10: Primer and Probe Set Products
| Vendor | Item | Catalog number | Quantity | # Reactions |
|---------|------|----------------|-----------|-------------|
| Order one of the following primer and probe sets |||||
| Eurofins Genomics | SalivaDirect™ complete set of the 6 primers and probes | 12YS-010YST | 50-100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006821 | 50 nmol | 6,2500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006830 | 100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006822 | 50 nmol | 6,250 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006831 | 100 nmol | 12,500 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006831 | 25 nmol | 6,250 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006832 | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006827 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006836 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006828 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006837 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNase P Probe | Custom order (Cy5) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | Custom order (Cy5) | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNase P Probe | 10007061 (ATTO647) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | 10007062 (ATTO647) | 50 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-250 | 250 nmol | 62,500 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-250 | 50 nmol | 12,500 |
||

The final amplification reaction components are listed in Table 11. PCR plates or strip tubes used for the amplification reactions should be maintained on ice or a cold block.

#### Table 11: PCR Amplification Reaction
|  |  |  |
|----------------------------|---------------------|------------------------|
| **Component** | **Volume (1 reaction)** | **Volume (100 reactions)** |
| 5X PCR Primer Stock | 4 µL | 400 µL |
| New England Biolabs PCR MM | 10 µL | 1000 µL |
| New England Biolabs PCR RT | 1 µL | 100 µL |
| Nuclease-Free Water | 3 µL | 300 µL |
| **SUBTOTAL VOLUME** | **18 µL** | **2250 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **20 µL** | - |
||

### 4) Software Validation
The **FloodLAMP EasyPCR(TM) COVID-19 Test** has been validated on the RT-PCR instruments listed in Table 2 using the baseline threshold settings unless otherwise noted in the Instructions for Use. The test does not require any additional software.

### 5) Testing Capabilities 
The **FloodLAMP EasyPCR(TM) COVID-19 Test** has been optimized for a robust, streamlined workflow and for rapid turnaround time on results. The total time to perform the test is dependent upon the following factors: number of lab technicians, batch size of samples, and in advance preparation of reaction mixes. The minimum turnaround time is approximately 1 hour and 45 minutes, of which approximately 1 hour and 20 minutes is the RT-PCR instrument run time. Automation can greatly increase overall throughput.

### 6) Reagent Stability: 
A stability test plan for the components of the **FloodLAMP EasyPCR(TM) COVID-19 Test** will be developed during an interactive review. Briefly, the proposed study includes assessing all prepared solutions including: 100X Inactivation Solution, 1X Inactivation Saline Solution, 5X PCR Primer Stock, and the full PCR Amplification Mix. Prepared solutions will be assessed both for long term storage stability (typically 1-3 months at -20oC) and short term storage stability prior to usage (typically hours to several days at room temperature, 4oC or -20oC).

The proposed study uses a contrived positive sample consisting of gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative specimens at approximately 50,000 copies/mL (4X LoD). The contrived positive stability study samples will be prepared, aliquoted and stored at -80oC to permit repeated testing of the various solutions at the appropriate step of the test protocol.

For test components supplied by vendors, such as New England Biolab’s LunaⓇ Universal Probe One-Step RT-qPCR Kit, the manufacturer's recommended storage conditions and duration will be followed.

### 7) Sample Stability:
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19: https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

Samples can be stored at room temperature for 56 hours after collection prior to inactivation. For longer term storage, samples can be stored at ≤-70oC.


## J. PERFORMANCE EVALUATION
### 1) Limit of Detection (LoD) - Analytical Sensitivity:
The Limit of Detection (LoD) for the **FloodLAMP EasyPCR(TM) COVID-19 Test** was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 6,300, 3,100 and 1,600 copies/mL were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 12. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 3,100 copies/mL.

#### Table 12: Confirmatory LoD Data Results
|  |  |  |  |
|----------------------|----------------|-----------------|------------------|
| **Instrument** | **LoD** | **Positive Replicates** | **Mean Ct Value (SD)** |
| ABI QuantStudio(TM) 7 Pro | 3,100 copies/mL | 95% (20/21) | 36.5 (.8) |
| ABI QuantStudio(TM) 6 Flex | 3,100 copies/mL | 100% (21/21) | 36.9 (1.1) |
| Bio-Rad CFX96 Touch(TM) | 3,100 copies/mL | 95% (20/21) | 37.2 (.9) |
||

### 2) Inclusivity (analytical sensitivity): 
**FloodLAMP EasyPCR(TM) COVID-19 Test** includes a modified RT-qPCR assay by duplexing the previously authorized CDC N1 and human RNase P primer-probe sets. Inclusivity was tested in the original US CDC EUA with all publicly available SARS-CoV-2 genomes as of 1 February 2020. The initial analysis showed 100% homology between the N1 primer-probe set and available genomes, except for one low frequency mismatch with the N1 forward primer. However, this was not expected to affect performance of the primer-probe set due to annealing temperatures of 55°C which tolerate 1-2 mismatches. Indeed, performance of the N1 primer-probe set was shown to be high in the previous comparison of primer-probes sets (<https://www.nature.com/articles/s41564-020-0761-6>). GISAID continuously evaluates mismatches between newly available SARS-CoV-2 genomes and primer-probe sets and confirms a low frequency of nucleotide mismatches (&lt;5%) with the N1 primer-probe set.

### 3) Cross-reactivity (Analytical Specificity): 
The primer and probe sets used in the duplex assay were developed by the US CDC and have been EUA certified. The CDC reported no cross-reactivity with other human coronaviruses (229E, OC43, NL63, and HKU1), MERS-coronavirus, SARS-coronavirus, and 14 additional human respiratory viruses (see <https://www.fda.gov/media/134922/download)>.

**Endogenous Interference Substances Studies:**
Exogenous and endogenous substances were tested for potential interference with the **FloodLAMP EasyPCR(TM) COVID-19 Test*.*** 10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 13 and Supporting Data.

#### Table 13: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

### 4) Clinical Evaluation 
The clinical evaluation of the **FloodLAMP EasyPCR(TM) COVID-19 Test** utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The **FloodLAMP EasyPCR(TM) COVID-19 Tes**t showed a positive agreement of 97.5% and a negative agreement of 100%. The single false negative result was a specimen with a high Ct value as previously measured by the comparator test, indicating very low viral load. A summary of the clinical performance is below in Table 14.

Anterior nares swab specimens were collected from patients in phosphate buffered saline by the Stanford COVID-19 clinical testing program. Specimens were initially tested by the Stanford clinical laboratory using the Hologic Panther Fusion and Aptima SARS-CoV-2 Assays, which serves as the high sensitivity comparator test.

For the **FloodLAMP EasyPCR(TM) COVID-19 Test**, materials and the Instructions For Use were provided to the Stanford clinical laboratory. The materials provided consisted of the validated reagents listed in Table 6, the Eurofins Genomics primers and probes, and an aliquot of the positive control. The Bio-Rad CFX96 instrument was used to perform the RT-PCR. After thawing the frozen specimens, 1 mL of each specimen was transferred to 5mL tubes for the inactivation step. The positive and negative clinical specimens were assigned a new ID in a random order, then transferred to new tubes that were barcoded and labeled with the new ID. Line Item data are provided in the Supporting Data.

#### Table 14: Clinical Evaluation Results
|  |  |  |  |
|------------------------|----------------|----------------|-----------------|
| **FloodLAMP EasyPCR(TM) COVID-19 Test Results** | **Comparator - High Sensitivity EUA Authorized Test** |  |  |
|  | **Positive** | **Negative** | **Total** |
| Positive | 39 | 0 | 39 |
| Negative | 1 | 40 | 41 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 97.5% (39/40) 95% CI: 86.8% to 99.9% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## K. UNMET NEED ADDRESSED BY THE PRODUCT 
This section will be completed by FDA.

## L. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for the detection of the SARS-CoV-2 have been approved/cleared by FDA.

## M. BENEFITS AND RISKS:
This section will be completed by FDA.

## N. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS:
Fact Sheets for Patients and Healthcare Providers attached.

## O. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT:
Instructions for Use attached.

## P. RECORD KEEPING AND REPORTING INFORMATION TO FDA:
Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.

QuantStudio(TM) is a trademark of Thermo Fisher Scientific (NYSE: TMO)

Bio-Rad(TM) and Bio-Rad CFX96 Touch(TM) are trademarks of Bio-Rad Laboratories, Inc. (NYSE: BIO)


# 10,870  2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md
file_date: 2021-03-22
title: EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/19VRwuRtGafiCtB7rHAn264BqKSJgqEjb
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-03-22_EUA%20Submission%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.0.docx
pdf_gdrive_url: https://drive.google.com/file/d/1sS6RlG2aLsXouqmliuSLbQOr4C4eVz2S
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-03-22_EUA%20Submission%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.0.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10870
words: 6496
notes: 
summary_short: The EUA Submission for the FloodLAMP QuickColor COVID-19 Test v1.0 describes an extraction-free, colorimetric RT-LAMP assay for qualitative SARS-CoV-2 detection using a visual pink-to-yellow readout and no specialized instrumentation. It details intended use for weekly screening of symptomatic and asymptomatic individuals, primer design targeting three viral genes, sample inactivation workflow, controls, and interpretation criteria for CLIA high-complexity labs. It reports analytical and clinical performance including a 12,500 copies/mL LoD and 90% positive agreement with 100% negative agreement in an 80-specimen clinical evaluation.


CONTENT

***INTERNAL TITLE:*** EUA Submission - FloodLAMP QuickColor(TM) COVID-19 Test
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for distribution and/or use of the **FloodLAMP QuickColor(TM) COVID-19 Test** for the *in vitro* qualitative detection of RNA from the SARS-CoV-2 in in upper respiratory specimens including oropharyngeal and nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests.** Additional testing and confirmation procedures should be performed in consultation with public health and/or other authorities to whom reporting is required. Test results should be reported in accordance with local, state, and federal regulations.

## B. MEASURAND
Specific nucleic acid sequences from the genome of the SARS-CoV-2, targeted by **primers from the ORF1ab, N and E regions** of the virus. Primer names and sequences are listed in Table 1.

#### Table 1: Primer names and sequences
|  |  |
|----------------------|--------------------------------------------------|
| **Primer Name** | **Sequence (5'-3')** |
| **ORF1ab gene (AS1e)** |  |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |  |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |  |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

## C. APPLICANT
FloodLAMP Biotechnologies, a DE Public Benefit Corporation
| Mailing Address: 4860 Alpine Rd. Portola Valley, CA 94028 | Laboratory Address: 930 Brittan Ave San Carlos, CA 94070	 | Randall J. True, CSO Phone: (415) 269-2974 Email: randy@floodlamp.bio |
| :---- | :---- | :---- |

## D. PROPRIETARY AND ESTABLISHED NAMES
Proprietary Name - **FloodLAMP QuickColor(TM) COVID-19 Test**
Established Name - **FloodLAMP QuickColor(TM) COVID-19 Test**

## E. REGULATORY INFORMATION
***Approval/Clearance Status:***

The **FloodLAMP QuickColor(TM) COVID-19 Test** is not cleared, CLIA waived, approved, or subject to an approved investigational device exemption.

***Product Code:***

QJR

## F. PROPOSED INTENDED USE
### 1) Intended Use:
**FloodLAMP QuickColor(TM) COVID-19 Test** is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests.** Testing is limited to **laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories.**

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The **FloodLAMP QuickColor(TM) COVID-19 Test** is intended for use by **qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures**. The **FloodLAMP QuickColor(TM) COVID-19 Test** is only for use under the Food and Drug Administration's Emergency Use Authorization.

### 2) Special Conditions for Use Statements:
For Emergency Use Authorization (EUA) only
For prescription use only
For *in vitro* diagnostic use only

### 3) Special Instrument Requirements:
The **FloodLAMP QuickColor(TM) COVID-19 Test** does not have special instrument requirements.

## G. DEVICE DESCRIPTION AND TEST PRINCIPLE
### 1) Product Overview/Test Principle:
The **FloodLAMP QuickColor(TM) COVID-19 Test** is a RNA extraction-free reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) molecular assay that indicates the presence of the SARS-CoV-2 viral RNA with a simple visual color change. It can widely and rapidly scale because 1) no special instrumentation of any kind is required, neither nucleic acid extraction equipment nor a RT-PCR instrument, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a very straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the **FloodLAMP EasyPCR(TM) COVID-19 Test**. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories.

The **FloodLAMP QuickColor(TM) COVID-19 Test** uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. It uses Loop Mediated Isothermal Amplification (LAMP), a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. Samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step. The resulting inactivated sample is directly used as input in the LAMP reaction. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. The amplified DNA products lower the pH of the reaction. A phenol red pH indicating dye is included in the amplification reaction mix, thus causing the reaction solution to visibly change from an initial bright pink to a bright yellow when sufficient amplification occurs. Reactions that change color to yellow indicate that SARS-CoV-2 RNA is present.

### 2) Description of Test Steps:
Specimens including **nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs** are collected in **sterile collection tubes.** Swabs are transported and stored dry prior to processing. At the laboratory, an inactivation solution at 1X containing TCEP (2.5 mM), EDTA (1 mM), and NaOH (11 mM) in 0.9% saline (154 mM) is added to the container with the swab, at the volume of 1 mL. Alternatively, for swabs that are collected or eluted in a saline solution or equivalent, the inactivation solution at 100X concentration should be added at 1/100th the sample solution volume.

The container with the specimen and inactivation solution is mixed by vortexing for 30 seconds. Subsequently, the container is heated for 8 minutes in a 95°C water bath or dry heat block. The now inactivated specimen container is allowed to cool at room temperature for 10 minutes and then stored on ice or at 4°C until amplification.

An amplification reaction mix (23 µl) is prepared per manufacturer's specifications, containing the Colorimetric LAMP master mix (NEB M1800, 12.5 µl) and a primer-guanidine solution (10.5 µl) comprising 10X primers mix (2.5 µl of 10X w FIP/BIP at 16 µM, F3/B3 at 2 µM, and LF/BF at 4 µM), guanidine hydrochloride (2.5 µl of 400 mM), and nuclease-free water (5.5 µl). The primer-guanidine solution may be prepared ahead of time and stored at -20°C for up to 1 month.

2 µl of the inactivated sample is added to 23µl of the amplification reaction mix. The reaction is incubated at 65°C for 25 minutes in a thermal cycler, dry heat block, or water bath. After removal from the heat, the reaction solution is allowed to cool at room temperature for 1 minute and then the test result is determined visually based on the color of the reaction solution.

### 3) Control Materials to be Used with test:
**One positive and one negative control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes on each heater:

1.  A "no template" (negative) control (NTC) is needed to **assure the absence of cross contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of 100X Inactivation Solution diluted to 1X in 0.9% saline.** This NTC is the same solution added to dry swabs (see Section I below for the components).

2.  A positive template control is needed to **assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 2 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at -80°C, or at most 1 month at -20°C.

#### Table 2: Components for Positive Template Control
|                                |               |                |            |
|--------------------------------|---------------|----------------|------------|
| **Material**                   | **Supplier**  | **Catalog \#** | **Volume** |
| SARS-CoV2 Positive Control RNA | Twist         | 102019         | 5 µL       |
| Total Human RNA                | Thermo Fisher | 4307281        | 100 µL     |
| Nuclease-free Water            | Thermo Fisher | 10977015       | 4,895 µL   |
||

## H. INTERPRETATION OF RESULTS
### 1) FloodLAMP QuickColor(TM) COVID-19 Test Controls
All test controls should be examined prior to interpretation of specimen results. If the controls are not valid, the specimen results cannot be interpreted. An example of the expected appearance of the negative and positive controls after amplification is shown in Figure 1.

![][image1]

#### Figure 1. Negative control (left) and positive control (right) after amplification.
If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and optionally RNAseZAP product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### 2) Examination and Interpretation of Patient Specimen Results:
Assessment of clinical patient specimen test results should be performed after the positive and negative controls have been examined and determined to be valid and acceptable. If the controls are not valid, the patient results cannot be interpreted.

Test results should be read at least 1 minute and no more than 8 hours after plates or tubes have been removed from heat. Test results may be determined directly from visual inspection of the color of the reaction tubes:

- yellow - result is positive  
- bright pink or red - result is negative  
- any other color - result is inconclusive.

Examples are shown below in Figure 2. Edge cases for positive and negative results are shown below in Figure 3. Any color variance stronger than the edge cases should be interpreted as inconclusive. In order to reduce the chance of both false negative and false positive results, this window for color variance is intentionally set to be small.

If the initial test is inconclusive, then one of the following should be performed:

1) repeat the Colorimetric LAMP Amplification Reaction on the inactivated sample. If the repeat test has a positive result then the final interpretation of the test is positive. If the repeat test has a negative or another inconclusive result, then the final interpretation is inconclusive.

2) follow-up test the inactivated sample with the FloodLAMP EasyPCR(TM) COVID-19 Test or another high sensitivity EUA authorized test that comprises the same inactivation protocol. The final interpretation is the result of the follow-up test.

For serial screening of individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, the initial inconclusive test result may be considered the final interpretation. If the final interpretation of the test result is inconclusive, then "Inconclusive" should be reported and retesting of the individual is recommended.

![][image2]

## I. PRODUCT MANUFACTURING
### 1) Overview of Manufacturing and Distribution:
The **FloodLAMP QuickColor(TM) COVID-19 Test** utilizes standard chemicals available in very large quantities from multiple vendors, with the exception of the LAMP Primers and New England Biolabs Colorimetric LAMP Master Mix.

FloodLAMP has partnered with LGC Biosearch for the LAMP Primers. LGC Biosearch has very large scale oligo production capacity and mature distribution capabilities. The first production scale lot of the LAMP Primers has been completed, with 1.2 million reactions ready for immediate distribution. FloodLAMP has purchased 600K reactions of the LAMP Primers. LGC Biosearch is supplying FloodLAMP for the **FloodLAMP QuickColor(TM) COVID-19 Test** and is also offering the LAMP Primers as a catalog product.

New England Biolabs has expressed strong support for the **FloodLAMP QuickColor(TM) COVID-19 Test** and FloodLAMP's other open source protocol EUA submissions that incorporate their products. New England Biolabs has very large quantities of the Colorimetric LAMP Master Mix product prepared and ready for immediate distribution, typically with 24 hour shipping within the U.S. Their manufacturing capacity is among the largest in the United States and can surge to meet increased demand.

**\*Under the Emergency Use Authorization (EUA) any of the 21 CFR Part 820 Quality System Regulation (QSR) requirements can be waived for the duration of the EUA but FDA recommends that developers follow comparable practices as much as possible if such requirements are waived. Among other things, FDA may consider previous compliance history when determining whether or not to waive certain QSR requirements for a specific product. Please note adverse events, as per 21 CFR Part 803, have to be reported for authorized devices (see Section P).**

### 2) Components Included with the Test
None. Designated CLIA labs may order components directly from vendors.

### 3) Components Required But Not Included with Test:
The **FloodLAMP QuickColor(TM) COVID-19 Test** is to be used with the reagents or equivalents listed in Table 3. No specialized instruments are needed. Only ordinary laboratory equipment such as pipettes, centrifuges, and heaters are needed.

#### Table 3: Validated reagents used with Test
| Item                    | Concentration | Chemical Composition                                 | Vendor                | Catalog No.          |
| :---------------------- | :-----------: | :---------------------------------------------------- | :-------------------- | :-------------------- |
| TCEP                    | .5 M         | tris(2-carboxyethyl)phosphine hydrochloride          | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA                    | .5 M         | Ethylenediaminetetraacetic acid                      | Thermo Fisher         | 15575020             |
| NaOH                    | 10 N         | Sodium Hydroxide                                     | Sigma-Aldrich        | SX0607N-6            |
| Nuclease- free Water    |       -       | Ultrapure Water, nuclease-free                       | Thermo Fisher         | 10977015             |
| NaCl                    | 5 M          | Sodium Chloride                                      | Thermo Fisher         | 24740011             |
| Guanidine               | 6 M          | Guanidine Hydrochloride                              | Sigma-Aldrich        | SRE0066              |
| ColorimetricLAMP MM*    |       -       | Colorimetric LAMP Master Mix                         | New England Biolabs   | M1804                |
||

\* Item may not be substituted for equivalents. Only the specified vendor and catalog number may be utilized.

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 4. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at -20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month.

#### Table 4: 100X Inactivation Solution
| **Component**                 | **Source Concentration**  | **Volume for 100X** | **100X Concentration** |
| ------------------            | --------------------      | ---------------- | ------------------ |
| TCEP                          | 0.5 M                     | 10 mL            | 250 mM            |
| EDTA                          | 0.5 M                     | 4 mL             | 100 mM            |
| NaOH                          | 10 N                      | 2.3 mL           | 1.15 N            |
| Nuclease-free Water           |        -                  | 3.7 mL           |  -                |
| **TOTAL VOLUME**              |              -              | **20 mL**        |        -           |
||


For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 5. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 5: 1X Inactivation Saline Solution
|                                           |             |
|-------------------------------------------|-------------|
| **Component**                             | **Volume**  |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL     |
| 100X Inactivation Solution                | 10 mL       |
| **TOTAL VOLUME**                          | **1010 mL** |
||

The **FloodLAMP QuickColor(TM) COVID-19 Test** uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 1. All 18 primers are mixed together and input into a single amplification reaction.

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered.

The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease-free water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.

Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at -20°C for up to 1 year.

#### Table 6: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | # Reactions |
|--------|------|----------------|-----------|-------------|
| Order one of the following primer sets |||||
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

The primers are mixed with guanidine hydrochloride to form an intermediate Primer-Guanidine Solution prior to combining with the sample and Colorimetric LAMP MM for the full amplification reaction. The components and volumes for the Primer-Guanidine Solution are listed in Table 7 and may be proportionally scaled for batch sizes of different numbers of reactions. The Primer-Guanidine Solution may be prepared in advance and should be stored at -20°C for up to 1 month.

#### Table 7: Primer-Guanidine Solution
| **Component**         | **Volume (1 reaction)** | **Volume (100 reactions)** |
|-----------------------|-------------------------|----------------------------|
| 10X LAMP Primer Mix   | 2.5 µL                 | 250 µL                     |
| Guanidine (400 mM)    | 2.5 µL                 | 250 µL                     |
| Nuclease-free Water   | 5.5 µL                 | 550 µL                     |
| **TOTAL VOLUME**      | **10.5 µL**            | **1050 µL**                |
||

The final Colorimetric LAMP Amplification Reaction components are listed in Table 8. PCR plates or strip tubes used for the amplification reactions should be maintained on ice or a cold block until less than 5 minutes before incubation on the heater. Reaction plates/strip tubes comprising the Colorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at -20°C for up to 1 day prior to addition of the sample. A heated plate sealer is recommended. Alternatively, a manually applied foil or optical seal may be used.

#### Table 8: Colorimetric LAMP Amplification Reaction
| **Component**         | **Volume (1 reaction)** | **Volume (100 reactions)** |
|-----------------------|-------------------------|----------------------------|
| Primer-Guanidine Solution | 10.5 µL             | 1050 µL                    |
| Colorimetric LAMP MM     | 12.5 µL             | 1250 µL                    |
| **SUBTOTAL VOLUME**      | **23 µL**           | **2300 µL**                |
| Sample                   | 2 µL               | -                          |
| **REACTION VOLUME**      | **25 µL**           | -                          |
||

### 4) Software Validation
No software is required for labs to run the **FloodLAMP QuickColor(TM) COVID-19 Test*.***

### 5) Testing Capabilities
The **FloodLAMP QuickColor(TM) COVID-19 Test** has been optimized for a robust, streamlined workflow and rapid turnaround time on results. The total time to perform the test is dependent upon the following factors: number of lab technicians, batch size of samples, and advance preparation of reaction mixes. **The minimum turnaround time is approximately 45 minutes.**

Since the **FloodLAMP QuickColor(TM) COVID-19 Test** does not require specialized instruments, it can be scaled up without the capital investment required for PCR machines or automated extraction. The number of tests capable of being performed per day by a laboratory is not constrained by PCR machines or extraction instruments. One technician can manually process approximately one plate (94 samples) per hour. This includes intake (debagging and barcode scanning), inactivation, and LAMP amplification. Automation can greatly increase throughput.

### 6) Reagent Stability
A stability test plan for the components of the **FloodLAMP QuickColor(TM) COVID-19 Test** will be developed during an interactive review. Briefly, the proposed study includes assessing all prepared solutions including: 100X Inactivation Solution, 1X Inactivation Saline Solution, 30X Primer Stock, 10X Primer Mix, Primer-Guanidine Solution, and the full Colorimetric LAMP Amplification Reaction Mix. Prepared solutions will be assessed both for long term storage stability (typically 1-3 months at -20°C) and short term storage stability prior to usage (typically hours to several days at room temperature, 4°C or -20°C).

The proposed study uses a contrived positive sample consisting of inactivated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative specimens at approximately 50,000 copies/mL (4X LoD). The contrived positive stability study samples will be prepared, aliquoted and stored at -80°C to permit repeated testing of the various solutions at the appropriate step of the test protocol.

For test components supplied by vendors, such as the Colorimetric LAMP Master Mix, the manufacturer's recommended storage conditions and duration will be followed.

### 7) Sample Stability
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19: https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

Samples can be stored at room temperature for 56 hours after collection prior to inactivation. For longer term storage, samples can be stored at ≤-70°C.

## J. PERFORMANCE EVALUATION
### 1) Limit of Detection (LoD) - Analytical Sensitivity:
The Limit of Detection (LoD) for the **FloodLAMP QuickColor(TM) COVID-19 Test** was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 12,500 and 6,250 were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 9. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 12,500 copies/mL.

#### Table 9: LoD Confirmatory Data Results
| **Concentration of Contrived Positive Sample** | **Replicates Detected** |
|-----------------------------------------------|-------------------------|
| 12,500 copies/mL                              | 95% (20/21)            |
| 6,250 copies/mL                               | 52% (11/21)            |
||

### 2) Inclusivity (analytical sensitivity):
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 10 summarizes the results of this in silico inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.

#### Table 10: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total Number of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

#### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs (<https://primer-monitor.neb.com/>), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 11, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 -t 16 -x asm5 -a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having &gt;= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations is not expected to reduce performance of the **FloodLAMP QuickColor(TM) COVID-19 Test** by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 11: Variant Analysis of LAMP Primers
![][image3]  
![][image4]

### 3) Cross-reactivity (Analytical Specificity):
*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the **FloodLAMP QuickColor(TM) COVID-19 Test** against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 12A, 12B, and 12C.

The % identity range (# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with &gt;= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the in silico cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 12A: *In Silico* Cross-Reactivity Analysis for AS1e Primers
![][image5]

#### Table 12B: *In Silico* Cross-Reactivity Analysis for N2 Primers
![][image6]

#### Table 12C: *In Silico* Cross-Reactivity Analysis for E1 Primers
![][image7]

Wet testing was performed to demonstrate that the **FloodLAMP QuickColor(TM) COVID-19 Test** does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen. SARS-CoV, RSV, Flu, Human Metapneumovirus. and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 13 and Supporting Data. 5 µL of each stock of cross-reactivity organism was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked onto the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived positive had 38 µL of 1e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 38,000 copies/mL in the sample input into the amplification reaction.

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 13.

#### Table 13: Wet Testing Cross-Reactivity Results
| **Organism**           | **Description**         | **BEI Number** | **Detected Replicates** |
|------------------------|-------------------------|---------------|-------------------------|
| SARS-CoV               | UV-inactivated virus    | NR-3882       | 0/3                     |
| Human Metapneumovirus  | Genomic RNA            | NR-49122      | 0/3                     |
| RSV                    | Genomic RNA            | NR-43976      | 0/3                     |
| Influenza B            | Genomic RNA            | NR-45848      | 0/3                     |
| Streptococcus salivarius | Bacterial cell culture | HM-121        | 0/3                     |
||

#### Endogenous Interference Substances Studies:
Exogenous and endogenous substances were tested for potential interference with the **FloodLAMP QuickColor(TM) COVID-19 Test.** 10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 14 and Supporting Data.

#### Table 14: Interfering Substances Results
| **Interfering Substance** | **Active Ingredient**                        | **Concentration** | **% Agreement (Positive)** | **% Agreement (Negative)** |
|---------------------------|---------------------------------------------|-------------------|---------------------------|---------------------------|
| Blood                    | N/A                                         | 1% v/v           | 100% (3/3)               | 100% (3/3)               |
| Nasal Congestion Spray   | Acetaminophen,<br>Guaifenesin,<br>Phenylephrine HCI | 20% v/v          | 100% (3/3)               | 100% (3/3)               |
| Nasal Allergy Spray      | Oxymetazoline HCl                           | 15% v/v          | 100% (3/3)               | 100% (3/3)               |
| Lozenges                 | Menthol                                     | 10% w/v          | 100% (3/3)               | 100% (3/3)               |
| Mucin                    | N/A                                         | 0.5% w/v         | 100% (3/3)               | 100% (3/3)               |
||

### 4) Clinical Evaluation
The clinical evaluation of the **FloodLAMP QuickColor(TM) COVID-19 Test** utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The **FloodLAMP QuickColor(TM) COVID-19 Test** showed a positive agreement of 90% and a negative agreement of 100%. The 4 false negative results were specimens with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is below in Table 15.

Anterior nares swab specimens were collected from patients in phosphate buffered saline by the Stanford COVID-19 clinical testing program. Specimens were initially tested by the Stanford clinical laboratory using the Hologic Panther Fusion and Aptima SARS-CoV-2 Assays, which serves as the high sensitivity comparator test.

For the **FloodLAMP QuickColor(TM) COVID-19 Test**, materials and the Instructions For Use were provided to the Stanford clinical laboratory. The materials provided consisted of the validated reagents listed in Table 3, the LGC primers and probes, and an aliquot of the positive control. After thawing the frozen specimens, 1 mL of each specimen was transferred to 5mL tubes for the inactivation step. The positive and negative clinical specimens were assigned a new ID in a random order, then transferred to new tubes that were barcoded and labeled with the new ID. The Bio-Rad C1000 Touch(TM) thermal cycler was used for the heating device to perform the isothermal amplification. Two different technicians independently interpreted the results visually per the Instructions For Use, with identical results. Line Item data are provided in the Supporting Data.

Of the 40 positive specimens, 7 specimens had initial inconclusive results due to color variation beyond the edge case examples. Per Section H2 above, the inactivated samples were follow-up tested with the FloodLAMP EasyPCR(TM) COVID-19 Test, for which all 7 inconclusive results were positive.

#### Table 15: Clinical Evaluation Results
|                                    | **Comparator - High Sensitivity EUA Authorized Test** |     |     |
|------------------------------------|--------------------------------------------------------|-----|-----|
| **FloodLAMP QuickColor(TM) COVID-19 Test Results** | **Positive**                                           | **Negative** | **Total** |
| Positive                           | 36                                                     | 0           | 36        |
| Negative                           | 4                                                      | 40          | 44        |
| Total                              | 40                                                     | 40          | 80        |
| Positive Agreement                 | 90.0% (36/40) 95% CI: 76.3% to 97.2%                   |             |           |
| Negative Agreement                 | 100% (40/40) 95% CI: 91.2% to 100%                     |             |           |
||

## K. UNMET NEED ADDRESSED BY THE PRODUCT
This section will be completed by FDA.

## L. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for the detection of the SARS-CoV-2 have been approved/cleared by FDA.

## M. BENEFITS AND RISKS:
This section will be completed by FDA.

## N. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS:
Fact Sheets for Patients and Healthcare Providers attached.

## O. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT:
Instructions for Use attached.

## P. RECORD KEEPING AND REPORTING INFORMATION TO FDA:
Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.


# 13,973  2021-03-22_Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.0.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-03-22_Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.0.md
file_date: 2021-03-22
title: Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.0
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/19kCNgAQKcM_fpSBXlOyPBOYG1BPIp1Zpv_WpF5WwebY
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-03-22_Instructions%20for%20Use%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.0.docx
pdf_gdrive_url: https://drive.google.com/file/d/1C2VtxuYhMxZ7SyTDB-6te8LNi9ed2J5i
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-03-22_Instructions%20for%20Use%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.0.pdf
conversion_input_file_type: gdoc
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 13973
words: 8770
notes: 
summary_short: The Instructions for Use for the FloodLAMP EasyPCR COVID-19 Test v1.0 provides CLIA high-complexity labs with the full workflow for an extraction-free, duplex RT-qPCR assay using CDC N1 and RNaseP targets after TCEP-based chemical plus heat inactivation. It specifies required reagents and equipment, contamination controls, instrument setup/templates, step-by-step plate and run procedures, and Ct-based result interpretation with control acceptance criteria. It also summarizes stated analytical/clinical performance (including a 3,100 copies/mL LoD and 97.5%/100% agreement in an 80-specimen evaluation) and required reporting/recordkeeping under EUA conditions.


CONTENT

***INTERNAL TITLE:*** FloodLAMP EasyPCR(TM) COVID-19 Test  
Instructions for Use v1.0

IVD

COVID-19 Emergency Use Authorization Only  
For *in vitro* diagnostic (IVD) Use  

[www.floodlamp.bio](http://www.floodlamp.bio)  
FloodLAMP Biotechnologies, PBC | 930 Brittan Ave. San Carlos, CA 94070 USA

## Table of Contents
|  |  |
|---------|------|
| Intended Use | 3 |
| Principles of Procedure | 3 |
| Materials Provided and Storage | 4 |
| Materials Required but Not Provided | 4 |
| • Standard Lab Equipment and Consumables | 5 |
| Warnings and Precautions | 6 |
| • General Precautions | 6 |
| • Contamination Precautions | 7 |
| Limitations | 7 |
| Conditions of Authorization for the Laboratory | 8 |
| Specimen Collection and Storage | 9 |
| Running Tests | 10 |
| • Reagent Preparation | 10 |
| • Controls Preparation | 11 |
| • PCR Primer Stock Preparation | 12 |
| • Sample Preparation | 14 |
| • Sample Inactivation | 14 |
| • Preparing to Run Assay for the First Time | 14 |
| • Create the Plate Layout Map | 16 |
| • PCR Amplification Reaction Preparation | 19 |
| • Sample Addition | 19 |
| • Run the Assay | 20 |
| • Analyzing Data | 22 |
| • Results Interpretation | 23 |
| • • Test Controls | 23 |
| • • Patient Specimen Results Interpretation | 23 |
| Performance Evaluation | 24 |
| • Analytical Sensitivity: Limit of Detection (LoD) | 24 |
| • Analytical Sensitivity: Inclusivity/Cross-Reactivity (in silico) | 24 |
| • Analytical Specificity: Cross-Reactivity | 25 |
| • Analytical Specificity: Interfering Substances | 25 |
| Clinical Evaluation | 26 |
| Support | 26 |
||

FloodLAMP EasyPCR(TM) COVID-19 Test  
For COVID-19 Emergency Use Authorization Only  
Instructions for Use

## Intended Use
FloodLAMP EasyPCR(TM) COVID-19 Test is a reverse transcriptase polymerase chain reaction (RT-PCR) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories.

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The FloodLAMP EasyPCR(TM) COVID-19 Test is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures. The FloodLAMP EasyPCR(TM) COVID-19 Test is only for use under the Food and Drug Administration’s Emergency Use Authorization.

## Principles of Procedure
The FloodLAMP EasyPCR(TM) COVID-19 Test is an RNA-extraction-free, dualplexed RT-qPCR assay which indicates whether SARS-CoV-2 RNA is present. It can widely and rapidly be scaled because 1) it does not require nucleic acid extraction equipment, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a very straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the FloodLAMP QuickColor(TM) test which is isothermal, does not require any instrumentation, and has a visual readout. Together the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories.

In the FloodLAMP EasyPCR(TM) COVID-19 Test samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step, and the resulting inactivated sample is directly used as input in the dualplexed RT-qPCR test. The test does not use new primers and probes for RT-qPCR testing, but rather uses previously validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC, which are readily available from multiple commercial suppliers. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a dualplex assay, reducing the number of tests to 1 assay with 2 sets.

## Materials Provided and Storage
The FloodLAMP EasyPCR(TM) COVID-19 Test utilizes standard chemicals available from multiple vendors, with the exception of the PCR Master Mix. Designated CLIA labs may order components directly from vendors.

## Materials Required but Not Provided
The FloodLAMP EasyPCR(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. The FloodLAMP EasyPCR(TM) COVID-19 Test is to be used with RT-PCR Instruments such as Applied Biosystems QuantStudio(TM) Systems and Bio-Rad CFX(TM) Systems.

#### Table 1: Validated reagents used with Test
| **Item** | **Concentration** | **Chemical Composition** | **Vendor** | **Catalog Number** |
|---|---|---|---|---|
| TCEP | 0.5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich / Millipore Sigma | 646547-10X1ML |
| EDTA | 0.5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-free Water |  | Ultrapure Water, nuclease free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| PCR Kit\* |  | LunaⓇ Universal Probe One-Step RT-qPCR Kit | New England Biolabs | E3006 |
||

\* Item may not be substituted for equivalent.

The FloodLAMP EasyPCR(TM) COVID-19 Test uses the validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a dualplex assay, detecting the 2 targets in a single well. This configuration is described in the SalivaDirect(TM) EUA Authorized test ([www.fda.gov/media/141192/download](http://www.fda.gov/media/141192/download)).

All four primers for both CoV-19 and RNase P detection may be purchased from the vendor Eurofins Genomics using the catalog number 12YS-010YST. This product contains primers and probes suspended at 100μM and is enough for 12,500 reactions. This kit can be mixed along with nuclease-free water to create the primer stock used in the FloodLAMP EasyPCR(TM) COVID-19 Test. See Table 6 below for details. A larger volume of primer-probe stock can be prepared in advance and stored at -20°C for up to 1 year.

#### Table 2: Primers and probes
| **Target**   | **Primer/Probe** | **Sequence**                              |
|---|---|---|
| CDC-N1 | 2019-nCoV\_N1-F | GACCCCAAAATCAGCGAAAT |
| CDC-N1 | 2019-nCoV\_N1-R | TCTGGTTACTGCCAGTTGAATCTG |
| CDC-N1 | 2019-nCoV\_N1-P | **FAM**-ACCCCGCATTACGTTTGGTGGACC-**IBFQ** |
| Human RNAseP | RP-F | AGATTTGGACCTGCGAGCG |
| Human RNAseP | RP-R | GAGCGGCTGTCTCCACAAGT |
| Human RNAseP | RP-P | **Cy5**-TTCTGACCTGAAGGCTCTGCGCG-**IBRQ** |
||
 
### Standard Lab Equipment and Consumables
- 70% ethanol  
- 10% bleach, prepared daily  
- 96-well PCR reaction plates (Applied Biosystems # 4346906, 4366932, 4346907, Eppendorf # 951020303 or equivalent)  
- Optical strip caps (Applied Biosystems # 4323032 or equivalent)  
- Optical plate seal (Applied Biosystems # 4311971 or equivalent)  
- PCR strip tubes and caps (USA Scientific catalog # 1402-2500 or equivalent)  
- 5 mL transport tubes or equivalent (sterile)  
- 1.5 mL microcentrifuge tubes or equivalent (nuclease-free)  
- Aerosol resistant micropipette tips (nuclease-free)  
- Micropipettes (calibrated)  
- Bottle top dispenser for 1 mL volume (optional, calibrated)  
- 96-well cold block  
- Cold blocks for 5 mL and 1.5 mL - 2.0 mL tubes, or ice  
- Vortex mixer  
- 96-well plate centrifuge or equivalent  
- Mini centrifuge for 1.5 mL tubes or equivalent  
- Thermal cycler, water bath, dry heat bath or equivalent (calibrated)  
- Class II Biological Safety Cabinet (BSC)  
- PCR Instrument (choose one)  
  - QuantStudio(TM) 6 Flex  
  - QuantStudio(TM) 7 Pro  
  - Bio-Rad CFX96 Touch(TM)

## Warnings and Precautions
Materials or chemicals required for the use of the FloodLAMP EasyPCR(TM) COVID-19 Test should be closely examined by the user. The user should carefully read all warnings, instructions or Safety Data Sheets provided by the supplier and follow the general safety precautions when handling biohazards, chemicals and other materials.

### General Precautions
- The FloodLAMP EasyPCR(TM) COVID-19 Test is for *in vitro* diagnostic use (IVD) only. Rx Only.  
- For use under COVID-19 Emergency Use Authorization Only.  
- Standard precautions and procedures should be taken when handling and disposing of human samples.  
- This test has not been FDA cleared or approved; the test has been authorized by FDA under an Emergency Use Authorization (EUA) for use by laboratories certified under the Clinical Laboratory Improvement Amendments (CLIA) of 1988, 42 U.S.C. §263a, to perform high complexity tests.  
- This test has been authorized only for the detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens.  
- This test is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of *in vitro* diagnostic tests for detection and/or diagnosis of COVID19 under Section 564(b)(1) of the Act, 21 U.S.C. § 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner.  
- Standard precautions and procedures should be taken when handling and extracting human samples.  
- Standard precautions and procedures should be taken when using laboratory equipment.  
- Standard precautions and procedures should be taken when disposing of waste.  
- Dispose of reagents according to local regulations.  
- Do not use reagents after their recommended stability time frame.  
- Ensure reagents are stored at the recommended temperatures as described below and in the vendor product information and manuals.

### Contamination Precautions
- Avoid contamination by following good laboratory practices, wearing proper personal protective equipment, segregating workflow, and decontaminating workspace appropriately.  
- Ensure that surfaces and equipment used for all test steps have been properly cleaned with 10% bleach and 70% ethanol.  
- Ensure all consumables are DNase and RNase free except for sample collection tubes which may be sterile.  
- Use only calibrated pipettes and filter tips that are sterile and PCR clean.  
- After completion of the test, dispose of the amplification reaction plates or tubes. Do not open tubes or remove the seals on plates after heating amplification reactions.

## Limitations
- The use of this assay as an *in vitro* diagnostic under the FDA COVID-19 Emergency Use Authorization (EUA) is limited to laboratories that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. § 263a, to perform high complexity tests by Rx only.  
- Use of this assay is limited to personnel who are trained in the procedure. Failure to follow these instructions may lead to erroneous results.  
- The performance of the FloodLAMP EasyPCR(TM) COVID-19 Test was established using Nasopharyngeal Swab specimen type collected in saline. Nasal swabs, oropharyngeal swabs, mid-turbinate nasal swabs specimens are also considered acceptable specimen types for use with the test but performance has not been established.  
- Samples must be collected according to recommended protocols and transported and stored as described herein.  
- Samples should not be collected in U(TM) or V(TM) or Liquid Amies transport media.  
- The effect of vaccines, antiviral therapeutics, antibiotics, chemotherapeutic or immunosuppressant drugs have not been evaluated.  
- Detection of SARS-CoV-2 RNA may be affected by sample collection methods, patient factors (e.g., presence of symptoms), and/or stage of infection.  
- False-positive results may arise from various reasons, including, but not limited to the following:  
  - Contamination during specimen collection, handling, or preparation  
  - Contamination during assay preparation  
  - Incorrect sample labeling  
- False-negative results may arise from various reasons, including, but not limited to the following:  
  - Improper sample collection or storage  
  - Degradation of SARS-CoV-2 RNA  
  - Presence of inhibitory substances  
  - Use of extraction reagents or instrumentation not approved with this assay  
  - Incorrect sampling window  
  - Failure to follow instructions for use  
  - Mutations in SARS-CoV-2 target sequences  
- Nucleic acid may persist even after the virus is no longer viable.  
- This test cannot rule out diseases caused by other bacterial or viral pathogens.  
- Performance has not yet been established in asymptomatic individuals and will be established during a post-authorization study.  
- Use of the test in a general, asymptomatic population for serial screening is intended to be used as part of an infection control plan, that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should not be treated as definitive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual’s recent exposures, history, and presence of clinical signs and symptoms consistent with COVID-19.  
- This test should not be used within 30 minutes of administering nasal or throat sprays.  
- Positive results must be reported to appropriate public health authorities, following state and national guidelines.  
- The clinical performance of the test has not been established in all circulating variants, and test performance may vary depending on the prevalence of variants circulating at the time of patient testing.  
- Negative test results do not exclude possibility of exposure to or infection with SARS-CoV-2 virus. Patient handling will be directed by healthcare professionals.

## Conditions of Authorization for the Laboratory
The FloodLAMP EasyPCR(TM) COVID-19 Test Letter of Authorization, along with the authorized Fact Sheet for Healthcare Providers, the authorized Fact Sheet for Patients, and authorized labeling are available on the FDA website: [https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas)

However, to assist clinical laboratories running the FloodLAMP EasyPCR(TM) COVID-19 Test, the relevant Conditions of Authorization are listed below:
- Authorized laboratories1 using the FloodLAMP EasyPCR(TM) COVID-19 Test will include all authorized Fact Sheets with test result reports. Under exigent circumstances, other appropriate methods for disseminating these Fact Sheets may be used, which may include mass media.  
- Authorized laboratories1 using the FloodLAMP EasyPCR(TM) COVID-19 Test will use the FloodLAMP EasyPCR(TM) COVID-19 Test as outlined in the FloodLAMP EasyPCR(TM) COVID-19 Test Instructions for Use. Deviations from the authorized procedures, including the authorized clinical specimen types, authorized control materials, authorized other ancillary reagents and authorized materials required to perform the test are not permitted.  
- Authorized laboratories must notify the relevant public health authorities of their intent to run the test prior to initiating testing.  
- Authorized laboratories using the FloodLAMP EasyPCR(TM) COVID-19 Test will have a process in place for reporting test results to healthcare providers and relevant public health authorities, as appropriate.  
- Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.  
- All laboratory personnel using the test must be appropriately trained in molecular assay techniques and use appropriate laboratory and personal protective equipment when handling these test components, and use the test in accordance with the authorized labeling.  
- FloodLAMP Biotechnologies, PBC authorized distributors, and authorized laboratories using the FloodLAMP EasyPCR(TM) COVID-19 Test will ensure that any records associated with this EUA are maintained until otherwise notified by FDA. Such records will be made available to FDA for inspection upon request.

1 For ease of reference, this will refer to, “Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a certified laboratories with FDA Emergency Use Authorization FDA for performing SARS-CoV-2 testing”

## Specimen Collection and Storage
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19:  
[https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

- Samples can be stored at room temperature for 56 hours after collection prior to inactivation.  
- For longer term storage, samples can be stored at ≤-70°C.

Note: Specimens must be packaged, shipped, and transported according to the current edition of the International Air Transport Association Dangerous Goods Regulation. Follow shipping regulations for UN 3373 Biological Substance, Category B when sending potential 2019-nCoV specimens.

## Running Tests
### Reagent Preparation
The FloodLAMP EasyPCR(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1.

#### Table 1: Validated reagents used with Test
| **Item** | **Concentration** | **Chemical Composition** | **Vendor** | **Catalog Number** |
|---|---|---|---|---|
| TCEP | 0.5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich / Millipore Sigma | 646547-10X1ML |
| EDTA | 0.5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-free Water |  | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| PCR Kit\* |  | LunaⓇ Universal Probe One-Step RT-qPCR Kit | New England Biolabs | E3006 |
||

\* Item may not be substituted for equivalent.

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 3 and vortexing for 30 seconds. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at -20° C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month.

#### Table 3: 100X Inactivation Solution
| **Component** | **Source Concentration** | **Volume** | **100X Concentration** |
|---|---|---|---|
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water |  | 3.7 mL |  |
| **TOTAL VOLUME** |  | **20 mL** |  |
||
 
Swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 4. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 4: 1X Inactivation Saline Solution
| **Component** | **Volume** |
|---|---|
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution                | 10 mL    |
| **TOTAL VOLUME**                          | **1010 mL** |
||
 
### Controls Preparation
One **Positive Template Control** and one **Negative (No Template) Control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes. An **Internal Process Control** is included in every PCR reaction.

1. A **“No Template” (Negative) Control (NTC)** is needed to assure the absence of cross-contamination from positive samples, positive controls, or amplicons and is used to determine if sample results are valid. It consists of nuclease-free water.  
2. A **Positive Template Control** is needed to assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water. Stock and working aliquots of the positive control are produced from the sources listed in Table 5 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at -80°C, or at most 1 month at -20°C.  
3. An **Internal Process Control** is needed to assure sufficient specimen quantity and quality. It consists of a primer/probe set targeting the human RNaseP gene that is included in a single PCR amplification reaction. The RNAseP Internal Process Control uses a fluorescent reporter in a separate channel from the SARS-CoV-2 channel (i.e. in duplex).

#### Table 5. Components for Positive Template Control
| **Material**                   | **Vendor**    | **Catalog \#** | **Volume** |
|---|---|---|---|
| SARS-CoV2 Positive Control RNA | Twist         | 102019         | 5 µl       |
| Total Human RNA                | Thermo Fisher | 4307281        | 100 µl     |
| Nuclease-free Water            | Thermo Fisher | 10977015       | 4,895 µl   |
||
 
### PCR Primer Stock Preparation
The FloodLAMP EasyPCR(TM) COVID-19 Test uses the validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a dualplex assay, detecting the 2 targets in a single well. This configuration is described in the SalivaDirect(TM) EUA Authorized test (www.fda.gov/media/141192/download).

All four primers for both CoV-19 and RNase P detection may be purchased from the vendor Eurofins Genomics using the catalog number 12YS-010YST. This kit contains primers and probes suspended at 100μM and is enough for 12,500 reactions. This kit can be mixed along with nuclease-free water to create the primer stock used in the FloodLAMP EasyPCR(TM) COVID-19 Test. See Table 6 below for details.

#### Table 6: 5X PCR Primer Stock Preparation from Eurofins Genomics Primer and Probe Set
| **Component**          | **5X PCR Primer Stock Concentration** | **Volume (1 reaction)** | **Volume (3,125 reactions)** |
|---|---|---|---|
| 2019-nCov_N1-F         | 2 µM  | 0.4 µl  | 1250 µl  |
| 2019-nCov_N1-R         | 2 µM  | 0.4 µl  | 1250 µl  |
| 2019-nCov_N1-P         | 1 µM  | 0.2 µl  | 625 µl   |
| RP-F                   | 0.75 µM | 0.15 µl | 469 µl   |
| RP-R                   | 0.75 µM | 0.15 µl | 469 µl   |
| RP-P                   | 1 µM  | 0.2 µl  | 625 µl   |
| Nuclease-free water    | - | 2.5 µl | 7813 µl |
| **Total Volume**       | - | **4 µl** | **12500 µl** |
||
 
Alternatively to the Eurofins Genomics Kit, primers may be purchased as individual custom oligos. Table 7 below lists the primer products to be ordered. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at -20°C for up to 1 year.

#### Table 7: PCR Primer Stock Components
| Vendor | Item | Catalog number | Quantity | # Reactions |
|---------|------|----------------|-----------|-------------|
| Order one of the following primer and probe sets |||||
| Eurofins Genomics | SalivaDirect™ complete set of 6 primers and probes | 12YS-010YST | 50-100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006821 | 50 nmol | 6,2500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006830 | 100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006822 | 50 nmol | 6,250 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006831 | 100 nmol | 12,500 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006831 | 25 nmol | 6,250 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006832 | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006827 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006836 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006828 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006837 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNase P Probe | Custom order (cy5) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | Custom order (cy5) | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNase P Probe | 10007061 (ATTO647) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | 10007062 (ATTO647) | 50 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-250 | 250 nmol | 62,500 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-250 | 50 nmol | 12,500 |
||
 
### Sample Preparation
\* For wet swab specimens (swabs in saline or unprocessed swab elution):
1. If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.  
2. Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
3. Wipe the outside of the sample tube with 70% ethanol.

For dry swab specimens:
1. Wipe the outside of the sample tube with 70% ethanol.

### Sample Inactivation
1. Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and set the temperature to hold at 100°C.  
2. \* For wet swab specimens: transfer 1 mL or available volume of each sample to an appropriately labeled 1.5 mL or 5 mL tube and securely cap.  
3. \* For wet swab specimens: add 10µL per 1 mL sample volume of 100X Inactivation Solution to each sample tube.  
4. For dry swab specimens (DO NOT DO FOR WET SWAB SPECIMENS): add 1 mL of 1X Inactivation Solution to each sample tube.  
5. Vortex for 30 seconds.  
6. Place sample tubes into the inactivation heater for 8 minutes.  
7. Remove sample tubes from the inactivation heater and let cool at room temperature for 10 minutes.  
8. Place sample tubes on ice, in the refrigerator, or on a cold block at 4°C until ready to perform amplification reaction.

> Note: Testing of inactivated specimens must be conducted the same day inactivation is performed. For long term storage, keep the original specimen at ≤-70°C.

### Preparing to Run Assay for the First Time
*Note: Any instrument running the FloodLAMP EasyPCR(TM) COVID-19 Test must be calibrated for the following dyes: FAM and Cy5.*

#### Download the Template Run File
The Template Run File contains all the parameters preconfigured to run the FloodLAMP EasyPCR(TM) COVID-19 Test. These parameters can be seen in more detail under “Create the Run File ...” headings below.

To download the Template Run File:
1. Go to [www.floodlamp.bio/ifus](http://www.floodlamp.bio/ifus)  
2. Download the Template Run file(s) for the instrument type and assay to be run.

#### Table 7: RT-PCR Instrument Template Run Files
| **Instrument**            | **Setup Template Filename**                     |
|---|-----------------------------------------------------------|
| ABI QuantStudio(TM) 7 Pro | FloodLAMP_QS7Pro_PCR_template_run.edt       |
| ABI QuantStudio(TM) 6 Flex | FloodLAMP_QS6Flx_PCR_template_run.edt       |
| Bio-Rad CFX96 Touch(TM)   | FloodLAMP_BRCFX_PCR_protocol.prcl            |
|  Bio-Rad CFX96 Touch(TM)                         | FloodLAMP_BRCFX_PCR_template_run.pltd           |
||
 
*Note: Template Run Files only need to be downloaded once upon first use.*

#### Alternatively Create the Template Run File on QuantStudio(TM) 6 Flex or 7 Pro
1. Open the Design and Analysis Software.  
2. Select the “SET UP PLATE” option.  
3. From the sidebar on the screen, select the following properties to filter:  
   - Instrument – choose the appropriate instrument  
   - Block – choose the appropriate block  
   - RunMode – Standard  
   - Analysis options are left blank  
4. From the plate sections present on the screen, select the correct System Template and the system will automatically navigate to the "Run Method" tab.
   - "Presence/Absence" for QuantStudio(TM) 7 Pro  
   - “Presence-Absence Standard Pre PCR Post” for QuantStudio(TM) 6 Flex  
5. Change Run Parameters as shown below:  
   - **Run Method:**  
     - 20μL Rxn Vol.  
     - 105° C Heated Cover Temp  
     - Ramp Rate: 1.6° C/s  

#### Table 8 : Thermal cycling and plate read steps for QuantStudio(TM) Systems for PCR
| **Stage** | **Temperature** | **Time** | **Reps** |
|---|---|---|---|
| 1 | 52° C | 10 min | 1  |
| 2 | 95° C | 2 min  | 1  |
| 3 | 95° C | 10 sec | 44 |
| 3 | 55° C\* | 30 sec | 44 |
| 4 | 55° C\*\* | 30 sec | 1  |
||

\*This step should be the optical read step  
\*\*This step is only required for QuantStudio(TM) 6 Flex

- **Plate Setup**  
  - Targets: FAM (N1) & Cy5 (RP)  
  - Quencher: None  
  - Passive Reference: ROX  

1. Once done setting up the template, go to “Actions” in the top right corner and hit “Save As”:  
   - On Connect: Save to template folder.  
   - Offline: Save to preferred location.

#### Create the Template Run File on Bio-Rad CFX96 Touch(TM)
1. Launch the CFX96 Touch(TM) software package.  
2. In the Startup Wizard pop-up window select the instrument “CFX96” from the drop down menu.  
3. Under “Select Run Type” press the “User-defined” button.  
4. Create a new thermocycler protocol by selecting “Create New” from the Run Setup window.  
5. Under Tools in the top left toolbar select “Run Time Calculator” and check “96 Wells-All Channels”.  
6. Make the following changes to the cycling conditions in the Protocol Editor:  
   - Sample Volume to 20 µL  
   - Lid Setting to 105°C  
   - Change cycles to be as shown below:

#### Table 9 : Thermal cycling and plate read steps for the Bio-Rad CFX96 Touch(TM)
| **Stage** | **Temperature** | **Time** | **Reps** |
|---|---|---|---|
| 1 | 52° C | 10 min | 1  |
| 2 | 95° C | 2 min  | 1  |
| 3 | 95° C | 10 sec | 44 |
| 3 | 55° C\* | 30 sec | 44 |
||

\*This step should be the optical read step

7. Click “OK” to save the protocol as type Protocol File (\*.prcl) and return to the Protocol tab in Run Setup.

### Create the Plate Layout Map
#### QuantStudio(TM) 6 Flex or 7 Pro Option 2: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run.
1. Open template in Design and Analysis app and go to the “Plate Setup” tab.  
2. On the right side of the screen ensure the “Samples” tab is highlighted and press the addition icon to add the number of samples being tested.  
3. Click on the “Sample 1” box to rename the sample.  
   - Repeat this step for all subsequent samples being entered.  
4. Click the well located in the plate map then check the box next to the sample name from the right side bar to associate the name to the well.  
   - There is also the option to highlight the well location in the plate map and click on the “Enter sample” box. Enter the sample ID and press tab to continue to the next well.  
5. Once the sample names have been entered, the wells may be highlighted by left clicking the mouse over the starting well and dragging the mouse across all wells. The targets are then chosen by clicking the check boxes next to each target in the sidebar.  
   - FAM & Cy5 targets should be chosen and named “N1” and “RP” respectively.  
6. Once done setting up the template, go to “Actions” in the top right corner and hit “Save As,” a pop-up window will appear directing the user to title the file according to information pertaining to the sample run.  
   - Connect: Save to the desired folder (only applicable for 7 Pro).  
   - Offline: Save to a USB that is inserted into the computer.  
7. Use your plate layout to load your samples and controls after preparing the amplification reaction mix.

#### QuantStudio(TM) 6 Flex or 7 Pro Option 2: Lookup Based on Well Position
For this option, a single generic sample name is applied to all wells, and subsequently, outside of the instrument software, the results are linked to the actual sample name via a lookup table to the well position.
1. Open the template in the Design and Analysis app and go to the “Plate Setup” tab.  
2. Highlight the entire plate and add 1 sample to all wells, with the same sample name in every well.  
3. Once the sample name has been entered, the targets are chosen by clicking the check boxes next to each target in the sidebar.  
   - FAM & Cy5 targets should be chosen and named “N1” and “RP” respectively.  
4. Go to “Actions” in the top right corner and hit “Save As” and name the Template Run File as desired. The software will automatically save as a .edt file.  
   - Connect: Save to desired location (only applicable for QuantStudio 7 Pro).  
   - Offline: Save to a USB that is inserted into the computer.  
This process only needs to be done once – all subsequent runs can use the same Template Run File.

#### Bio-Rad CFX96 Touch(TM):
1. Launch the CFX96 Touch(TM) software package and open the correct protocol template.  
2. Review the details of the protocol. If correct, click “Next” to proceed to the Plate tab.  
3. On the Plate tab, click “Create New” and the Plate Editor appears.  
4. Use the Plate Editor to create a new plate.  
5. To ensure the correct plate size is selected, go to “Settings > Plate Size” and check that 96-well or 384-well is selected.  
6. To set the plate type, select “Settings > Plate Type” and select “BR Clear” or “BR White” from the drop-down menu.  
7. To set the scan mode, select the “All Channels” scan mode from the Scan Mode drop-down list.  
8. Select the “Select Fluorophores” button on the upper right of the Plate Editor window.  
   - De-select all default fluorophores and select “FAM” and “Cy5” and click OK.  
9. In the Plate Editor window highlight the whole plate and click the checkbox in front of FAM and Cy5.  
10. Select the “Experiment Settings” button in order to define the Targets.  
   - In the lower left of the Experiment Settings window in the New box, type in “N1” and select “Add”.  
   - Repeat and type in “RP”.  
   - Select “OK”.  
11. In the Plate Editor window next to FAM in the drop-down menu under Target Name select “N1” and for Cy5 select “RP”.  
12. Click OK to save changes and close the “Select Fluorophores” dialog box.

#### Bio-Rad CFX96 Touch(TM) Option 1: Sample Name Input
1. Load the appropriate sample type to each well by selecting the well and selecting the appropriate Sample Type (Unknown, NTC, or Positive Control) from the drop-down menu.  
2. Multiple wells can be selected at once to load the sample type.  
   - Note: The EC can be listed as an Unknown sample.  
3. In the “Target Names” section confirm that the necessary fluorophores are assigned to each well.  
4. Name each well by typing in the sample name and pressing “Enter” in the Sample Names dropdown list.  
5. Click OK to save the Plate File (\*.pltd) and return to the Plate tab in Run Setup. When prompted, specify a name for the plate and a save location.

#### Bio-Rad CFX96 Touch(TM) Option 2: Lookup Based on Well Position
1. Name the file as desired and save as type “Plate File (\*.pltd)”.  
2. Select “Save”, click “OK” in the Plate Editor window and exit the software.

This process only needs to be done once – all subsequent runs can use the same Template Plate File.

### PCR Amplification Reaction Preparation
1. Place a 96-well PCR plate or PCR strip tubes onto a cold block or ice.  
2. Thaw frozen reagents until ice crystals are not present.  
3. Pulse vortex thawed reagents for 3 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
4. Store on ice or in the refrigerator or on a cold block at 4°C until ready to use.  
5. Prepare the PCR Amplification Reaction Mix by combining the components listed below in Table 10.
NOTE: Component volumes should be scaled proportionally for the number of reactions.
6. Vortex the PCR Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge.  
7. Add 18 µL of the PCR Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

#### Table 10: PCR Amplification Reaction Mix
| **Component**          | **Volume (1 reaction)** | **Volume (1 reaction x 100)<br>1 x 96-plate w/ 4% overage** |
|---|---|---|
| 5X PCR Primer Stock    | 4 µL   | 400 µL  |
| Nuclease-free Water    | 3 µL   | 300 µL  |
| PCR Master Mix\*       | 10 µL  | 1000 µL |
| PCR RT\*               | 1 µL   | 100 µL  |
| **SUBTOTAL VOLUME**    | **18 µL** | **1800 µL** |
| Sample                 | 2 µL   |     -    |
| **REACTION VOLUME**    | **20 µL** |      -   |
||

\* in LunaⓇ Universal Probe One-Step RT-qPCR Kit

### Sample Addition
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1. Add 2 μL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.  
2. Mix by pipetting.  
3. If using PCR plate, seal with optical film (optionally using heat sealer). If using PCR strip tubes, cap strips.  
4. Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom.  
5. Continue to section “Run the Assay”.

### Run the Assay
Refer to Specific Instrument User Manuals for full system usage and maintenance details.

#### On QuantStudio(TM) 6 Flex
1. To transfer templates from a USB drive, plug a USB drive into the USB port below the touchscreen.  
2. If the instrument is in standby, touch the touchscreen to activate it and then press the green power icon.  
3. In the Main Menu, press “View Templates”.  
4. In the Browse Experiments screen, select the template:  
   - Press the Folder icon, then choose “USB”.  
   - Press the desired template, then press “Save”.  
5. In the Save Experiment As screen, set the name for the file.  
   - Press the “New Template Name” field, then enter a name for the copied file.  
   - Press the “Save to Folder” field, then select the folder to receive the file.  
   - Hit “Save”.  
6. Press the Home icon to return to the Main Menu.  
7. Navigate to the Main Menu screen, then press the red eject icon.  
8. When the side door opens, load the appropriate plate or PCR strips. Ensure that the consumable is properly aligned.  
9. In the Main Menu, press “Browse Experiments”.  
10. In the Experiments screen, choose the desired experiment and then click the Folder icon to choose where to save the experiment.  
11. Then press “Start Run” to start the run immediately.

#### On QuantStudio(TM) 7 Pro
1. Log into user on instrument.  
2. USB: Plug in USB with saved template on it.  
3. From the options on the instrument’s screen press “Load plate file”.  
   - The QuantStudio(TM) 7 is a touchscreen device.  
4. From the “Run Queue” screen,  
   - USB: press “USB drive” on the left side.  
   - Connect: press Cloud icon on the left side.  
5. This will bring up any plate files saved.  
6. Press the plate file associated with the run to be performed.  
7. A new window will appear requesting location of results once the run is complete.  
   - Connect: Press the “Cloud Connect” icon, press again to verify location and then press “Done”.  
   - USB: Press the “USB drive Connected” if not already highlighted and press “Done”.  
8. Press the double-arrow icon at the top right corner of the screen.  
   - The instrument drawer will open from the front.  
9. Place the plate/strips into the plate holder ensuring proper orientation of the plate (A1 well top-left).  
10. Press “Start Run” on the screen of the instrument.  
    - A pop-up window will appear asking the user to confirm the plate has been loaded.  
    - If the plate has been loaded, press “Start Run” again or press “Open Drawer” to place the plate into the block and then press “Start Run”.

#### On Bio-Rad CFX96 Touch(TM)
1. Open the correct .pcrl file and review the protocol details. If correct, click “Next” to proceed to the Plate tab.  
2. When prompted, open the correct .pltd file and review the plate details in the Run Information section.  
3. Select the checkbox for the appropriate block (CFX96 or CFX384) on which to perform the run.  
4. To insert the plate or 8-tube strips into the block, click Open Lid.  
5. Insert the plate or 8-tube strips into the block, ensuring proper orientation.  
6. Click Close Lid.  
7. Click Start Run at the bottom right of the screen.  
8. When prompted, save the data file (.pcrd) to the desired location.

### Analyzing Data
#### Exporting Data from QuantStudio(TM) 6 Flex or 7 Pro
##### Using USB
1. Confirm Quant says “File Transferred - USB”.  
2. Take USB from Quant and plug it into computer.  
3. Export data off of USB onto computer.

##### Using Cloud Connect with QuantStudio(TM) 7 Pro
1. Go to [Cloud Connect](https://apps.thermofisher.com/apps/spa/#/dashboard) and log in.  
2. Go to files and find the data that was just uploaded by the Quant, in the folder chosen previously.  
3. Download .xlsx file.

#### Exporting Data from Bio-Rad CFX96 Touch(TM)
1. After the run has completed, open the data file (.pcrd) by going to Select File > Open > Data File in the Home window and locating the desired data file. Adjust the following settings as described below.  
2. Select Settings > Cq Determination mode and select Single Threshold.  
3. Select Settings > Baseline Setting and select Baseline Subtracted.  
4. Select Settings > Analysis Mode and select analysis by fluorophore.  
5. Select Settings > Cycles to Analyze and confirm that all cycles are analyzed, then click “OK”.  
6. Cq values of each well are displayed in the Quantification Data tab.  
7. Export .xlsx files and select Export > Export all Data Sheets to Excel (Cq values are in "Quantification Plate View Results").

#### Compiling Results Option 1: Lookup Based on Well Position
For this option, outside of the instrument software the results are linked to the actual sample name via a lookup table to the well position. An example spreadsheet to perform this lookup and results compilation is available with instructions at [www.floodlamp.bio/ifus](http://www.floodlamp.bio/ifus).

#### Compiling Results Option 2: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run. Open the results file and continue to “Analyzing Data” section to score results.

### Results Interpretation
#### Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to Table 5 below.

1. The **No Template (Negative) Control (NTC)** should yield a negative “not detected” result for both the N1 and RNaseP targets.  
2. The **Positive Template Control** should yield a positive “detected” result for the N1 target and a negative “not detected” for the RNaseP control.  
3. The **Internal Process Control** should yield a positive "detected" result for RNaseP. Detection of RNaseP is required to report a negative SARS-CoV-2 result.

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP™ product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

#### Patient Specimen Results Interpretation
NOTE: Results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Use Table 11 below to assign a result to each sample.

#### Table 11: Interpretation of Assay Results
| **ABI QuantStudio(TM) 7 Pro** |  |  |
|---|---|---|
| **Result** | **Ct Value: N1** | **Ct Value RP** |
| Positive | <38.0 | Any Value  |
| Negative | ≥38.0 | <35.0      |
| *Invalid  | ≥38.0 | ≥35.0      |
| **Bio-Rad CFX96 Touch(TM)** / **ABI QuantStudio(TM) 6 Flex** |  |  |
| **Result** | **Ct Value: N1** | **Ct Value RP** |
| Positive | <40.0 | Any Value |
| Negative | ≥40.0 | <35.0     |
| *Invalid | ≥40.0 | ≥35.0     |
||

\*Invalid test results should be repeated by rerunning the primary sample if available, otherwise the inactivated sample. Results from retested samples will follow the same interpretation.

If the final interpretation of the test result is invalid, then "Invalid/Inconclusive" should be reported and retesting of the individual is recommended.

## Performance Evaluation
### Analytical Sensitivity: Limit of Detection (LoD)
The Limit of Detection (LoD) for the FloodLAMP EasyPCR(TM) COVID-19 Test was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 3,100 and 1,600 were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 12. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 3,100 copies/mL.

#### Table 12: Confirmatory LoD Data Results
| **Instrument**                  | **LoD**           | **Positive Replicates** |
|---|---|---|
| ABI QuantStudio(TM) 7 Pro | 3,100 copies/mL  | 95% (20/21)             |
| ABI QuantStudio(TM) 6 Flex | 3,100 copies/mL  | 100% (21/21)            |
| Bio-Rad CFX96 Touch(TM)   | 3,100 copies/mL  | 95% (20/21)             |
||
 
### Analytical Sensitivity: Inclusivity
FloodLAMP EasyPCR(TM) COVID-19 Test includes a modified RT-qPCR assay by dualplexing the previously authorized CDC N1 and human RNase P primer-probe sets. Inclusivity was tested in the original US CDC EUA with all publicly available SARS-CoV-2 genomes as of 1 February 2020. The initial analysis showed 100% homology between the N1 primer-probe set and available genomes, except for one low frequency mismatch with the N1 forward primer. However, this was not expected to affect performance of the primer-probe set due to annealing temperatures of 55°C which tolerate 1-2 mismatches. Indeed, performance of the N1 primer-probe set was shown to be high in the previous comparison of primer-probes sets ([https://www.nature.com/articles/s41564-020-0761-6](https://www.nature.com/articles/s41564-020-0761-6)). GISAID continuously evaluates mismatches between newly available SARS-CoV-2 genomes and primer-probe sets and confirms a low frequency of nucleotide mismatches (<5%) with the N1 primer-probe set.

### Analytical Specificity: Cross-Reactivity
The primer and probe sets used in FloodLAMP’s dualplex assay were developed by the US CDC and have been EUA certified. The CDC reported no cross-reactivity with other human coronaviruses (229E, OC43, NL63, and HKU1), MERS-coronavirus, SARS-coronavirus, and 14 additional human respiratory viruses (see [https://www.fda.gov/media/134922/download](https://www.fda.gov/media/134922/download)).

### Analytical Specificity: Interfering Substances
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP EasyPCR(TM) COVID-19 Test. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positive Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 13.

#### Table 13: Interfering Substances Results
| **Interfering Substance** | **Active Ingredient** | **Concentration** | **% Agreement with Expected Results** (Positive Control) | **% Agreement with Expected Results** (Negative Control) |
|---|---|---|---|---|
| Blood                     | N/A                  | 1% v/v            | 100% (3/3)                                             | 100% (3/3)                                             |
| Nasal Congestion Spray    | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray       | Oxymetazoline HCl    | 15% v/v           | 100% (3/3)                                             | 100% (3/3)                                             |
| Lozenges                  | Menthol              | 10% w/v           | 100% (3/3)                                             | 100% (3/3)                                             |
| Mucin                     | N/A                  | 0.5% w/v          | 100% (3/3)                                             | 100% (3/3)                                             |
||
 
## Clinical Evaluation
The clinical evaluation of the FloodLAMP EasyPCR(TM) COVID-19 Test utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The FloodLAMP EasyPCR(TM) COVID-19 Test showed a positive agreement of 97.5% and a negative agreement of 100%. The single false negative result was a specimen with a high Ct value as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is shown in Table 14.

#### Table 14: Clinical Evaluation Results
| **FloodLAMP EasyPCR(TM) COVID-19 Test Results** | **Comparator - High Sensitivity EUA Authorized Test** |  |  |
|---|---|---|---|
|  | **Positive** | **Negative** | **Total** |
| Positive | 39 | 0  | 39 |
| Negative | 1  | 40 | 41 |
| Total    | 40 | 40 | 80 |
| Positive Agreement | 97.5% (39/40) 95% CI: 86.8% to 99.9% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100%   |  |  |
||
 
## Support
FloodLAMP Biotechnologies, PBC support center  
[eua.support@floodlamp.bio](mailto:eua.support@floodlamp.bio)  
650-394-5233  

QuantStudio is a trademark of Thermo Fisher Scientific (NYSE: TMO)  
Bio-Rad and Bio-Rad CFX96 Touch is a trademark of Bio-Rad Laboratories, Inc. (NYSE: BIO)


# 12,087  2021-03-22_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.0.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-03-22_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.0.md
file_date: 2021-03-22
title: Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.0
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/15lzY7exZ6PTja9NeAYTs0zUF05Nyl2J5yD9f3BmEJvM
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-03-22_Instructions%20for%20Use%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.0.docx
pdf_gdrive_url: https://drive.google.com/file/d/1wp_mYfcQBSyl0I5oPwB6QfBHcVuD2AWd
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-03-22_Instructions%20for%20Use%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.0.pdf
conversion_input_file_type: gdoc
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 12087
words: 7494
notes: 
summary_short: The Instructions for Use for the FloodLAMP QuickColor COVID-19 Test v1.0 provides CLIA high-complexity laboratories with the complete protocol for an extraction-free, colorimetric RT-LAMP assay with visual readout after chemical and heat inactivation. It details required reagents and equipment, primer preparation, step-by-step testing workflow, control requirements, result interpretation by color change, and contamination precautions. It also documents analytical and clinical performance claims, including a 12,500 copies/mL LoD and 90% positive agreement with 100% negative agreement in an 80-specimen evaluation.


CONTENT

***INTERNAL TITLE:*** FloodLAMP QuickColor(TM)  COVID-19 Test
Instructions for Use v1.0

IVD
COVID-19 Emergency Use Authorization Only
For *in vitro* diagnostic (IVD) Use  

www.floodlamp.bio
FloodLAMP Biotechnologies, PBC | 930 Brittan Ave. San Carlos, CA 94070 USA

## Table of Contents
|  |  |
|---------|------|
| Intended Use | 3 |
| Principles of Procedure | 3 |
| Materials Provided and Storage | 4 |
| Materials Required but Not Provided | 4 |
| • Standard Lab Equipment and Consumables | 6 |
| Warnings and Precautions | 6 |
| • General Precautions | 6 |
| • Contamination Precautions | 7 |
| Limitations | 7 |
| Conditions of Authorization for the Laboratory | 9 |
| Specimen Collection and Storage | 10 |
| Running Tests | 11 |
| • Reagent Preparation | 11 |
| • Controls Preparation | 12 |
| • 10X LAMP Primer Mix Preparation | 13 |
| • Sample Preparation | 15 |
| • Sample Inactivation | 15 |
| • Colorimetric LAMP Amplification Reaction Preparation | 15 |
| • Sample Addition and Heating | 16 |
| • Test Controls | 17 |
| • Patient Specimen Results Interpretation | 18 |
| Performance Evaluation | 19 |
| • Analytical Sensitivity: Limit of Detection (LoD) | 19 |
| • Analytical Sensitivity: Inclusivity (in silico) | 19 |
| • Evaluation of Impact of Viral Mutations | 20 |
| • Analytical Specificity: Cross-Reactivity (in silico) | 22 |
| • Analytical Specificity: Cross-Reactivity (wet testing) | 26 |
| • Analytical Specificity: Interfering Substances | 26 |
| Clinical Evaluation | 27 |
| Support | 29 |
||

FloodLAMP QuickColor(TM) COVID-19 Test  
For COVID-19 Emergency Use Authorization Only  
Instructions for Use

## Intended Use
FloodLAMP QuickColor(TM) COVID-19 Test is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories. 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The FloodLAMP QuickColor(TM) COVID-19 Test is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures. The FloodLAMP QuickColor(TM) COVID-19 Test is only for use under the Food and Drug Administration’s Emergency Use Authorization.

## Principles of Procedure
The FloodLAMP QuickColor(TM) COVID-19 Test is an RNA-extraction free isothermal RT-LAMP assay that indicates the presence of the SARS-CoV-2 viral RNA with a simple visual color change. It can widely and rapidly be scaled because 1) no special instrumentation of any kind is required, neither nucleic acid extraction equipment nor a RT-PCR instrument, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a very straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the FloodLAMP EasyPCR(TM) Test which is also a supply chain robust, open source protocol test. Together the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

The FloodLAMP QuickColor(TM) COVID-19 Test uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. Loop Mediated Isothermal Amplification (LAMP) is a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. Samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step. The resulting inactivated sample is directly used as input in the LAMP reaction. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. The amplified DNA products lower the pH of the reaction. A phenol red pH indicating dye is included in the amplification reaction mix, thus causing the reaction solution to visibly change from an initial bright pink to a bright yellow when sufficient amplification occurs. Reactions that change color to yellow indicate that SARS-CoV-2 RNA is present.

## Materials Provided and Storage
The FloodLAMP QuickColor(TM) COVID-19 Test utilizes standard chemicals available from multiple vendors, with the exception of the LAMP primers and Colorimetric LAMP master mix. Designated CLIA labs may order components directly from vendors.

## Materials Required but Not Provided
The FloodLAMP QuickColor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. No specialized instruments are needed. Only ordinary laboratory equipment such as pipettes, centrifuges, and heaters are needed.

#### Table 1: Validated reagents used with the Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine HCl | 6 M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| Colorimetric LAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalent. Only the specified vendor and catalog number may be utilized.

The FloodLAMP QuickColor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. All 18 primers are mixed together and are input into a single amplification reaction. Primer names and sequences are listed in Table 2. Primers may be purchased pre-blended from the vendor LGC Biosearch Technologies with the product names LAMP\_S2-As1e, LAMP\_S2-N2, LAMP\_S2-E1. Alternatively, primers may be purchased as individual custom oligos. Appropriate validation of primer mixes from custom oligos is required. See Primer Preparation below for more information. 

#### Table 2: Primer names and sequences
| Primer Name | Sequence (5’-3’) |
| :---- | :---- |
| **ORF1ab gene (AS1e)** |   |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |   |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |   |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

### Standard Lab Equipment and Consumables
* 70% ethanol  
* 10% bleach, prepared daily  
* 96-well PCR reaction plates (Applied Biosystems \# 4346906, 4366932, 4346907, Eppendorf \# 951020303 or equivalent)  
* Optical strip caps (Applied Biosystems \# 4323032 or equivalent)  
* Optical plate seal (Applied Biosystems \# 4311971 or equivalent)  
* PCR strip tubes and caps (USA Scientific catalog \# 1402-2500 or equivalent)   
* 5 mL transport tubes or equivalent (sterile)  
* 1.5 mL microcentrifuge tubes or equivalent (nuclease-free)  
* Aerosol resistant micropipette tips (nuclease-free)  
* Micropipettes (calibrated)  
* Bottle top dispenser for 1 mL volume (optional, calibrated)  
* 96-well cold block  
* Cold blocks for 5 mL and 1.5 mL \- 2.0 mL tubes, or ice  
* Vortex mixer  
* 96-well plate centrifuge or equivalent  
* Mini centrifuge for 1.5 mL tubes or equivalent  
* 2 x Thermal cycler, water bath, dry heat bath or equivalent (calibrated)  
* Class II Biological Safety Cabinet (BSC) 

## Warnings and Precautions
Materials or chemicals required for the use of the FloodLAMP QuickColor(TM) COVID-19 Test should be closely examined by the user. The user should carefully read all warnings, instructions or Safety Data Sheets provided by the supplier and follow the general safety precautions when handling biohazards, chemicals and other materials. 

### General Precautions
* The FloodLAMP QuickColor(TM) COVID-19 Test is for *in vitro* diagnostic use (IVD) only. Rx Only.  
* For use under COVID-19 Emergency Use Authorization Only.  
* Standard precautions and procedures should be taken when handling and disposing of human samples.  
* This test has not been FDA cleared or approved; the test has been authorized by FDA under an Emergency Use Authorization (EUA) for use by laboratories certified under the Clinical Laboratory Improvement Amendments (CLIA) of 1988, 42 U.S.C. §263a, to perform high complexity tests.  
* This test has been authorized only for the detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens.  
* This test is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of *in vitro* diagnostic tests for detection and/or diagnosis of COVID19 under Section 564(b)(1) of the Act, 21 U.S.C. § 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner.  
* Standard precautions and procedures should be taken when handling and extracting human samples.  
* Standard precautions and procedures should be taken when using laboratory equipment.  
* Standard precautions and procedures should be taken when disposing of waste.  
* Dispose of reagents according to local regulations.  
* Do not use reagents after their recommended stability time frame.  
* Ensure reagents are stored at the recommended temperatures as described below and in the vendor product information and manuals.

### Contamination Precautions
* Avoid contamination by following good laboratory practices, wearing proper personal protective equipment, segregating workflow, and decontaminating workspace appropriately.  
* Ensure that surfaces and equipment used for all test steps have been properly cleaned with 10% bleach and 70% ethanol.  
* Ensure all consumables are DNase and RNase free except for sample collection tubes which may be sterile.  
* Use only calibrated pipettes and filter tips that are sterile and PCR clean.  
* After completion of the test, dispose of the amplification reaction plates or tubes. **Do not open tubes** or remove the seals on plates after heating amplification reactions.

## Limitations
* The use of this assay as an *in vitro* diagnostic under the FDA COVID-19 Emergency Use Authorization (EUA) is limited to laboratories that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. § 263a, to perform high complexity tests by Rx only.   
* Use of this assay is limited to personnel who are trained in the procedure. Failure to follow these instructions may lead to erroneous results.   
* The performance of the FloodLAMP QuickColor(TM) COVID-19 Test was established using Nasopharyngeal Swab specimen type collected in saline. Nasal swabs, oropharyngeal swabs, mid-turbinate nasal swabs specimens are also considered acceptable specimen types for use with the test but performance has not been established.   
* Samples must be collected according to recommended protocols and transported and stored as described herein.  
* Samples should not be collected in UTM or VTM or Liquid Amies transport media.  
* The effect of vaccines, antiviral therapeutics, antibiotics, chemotherapeutic or immunosuppressant drugs have not been evaluated.  
* Detection of SARS-CoV-2 RNA may be affected by sample collection methods, patient factors (e.g., presence of symptoms), and/or stage of infection.  
* False-positive results may arise from various reasons, including, but not limited to the following:  
  * Contamination during specimen collection, handling, or preparation  
  * Contamination during assay preparation  
  * Incorrect sample labeling  
* False-negative results may arise from various reasons, including, but not limited to the following:  
  * Improper sample collection or storage  
  * Degradation of SARS-CoV-2 RNA  
  * Presence of inhibitory substances  
  * Use of extraction reagents or instrumentation not approved with this assay   
  * Incorrect sampling window  
  * Failure to follow instructions for use  
  * Mutations In SARS-CoV-2 target sequences  
* Nucleic acid may persist even after the virus is no longer viable.   
* This test cannot rule out diseases caused by other bacterial or viral pathogens.  
* Performance has not yet been established in asymptomatic individuals and will be established during a post-authorization study.   
* Use of the test in a general, asymptomatic population for serial screening is intended to be used as part of an infection control plan, that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should not be treated as definitive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual’s recent exposures, history, and presence of clinical signs and symptoms consistent with COVID-19.  
* This test should not be used within 30 minutes of administering nasal or throat sprays.  
* Positive results must be reported to appropriate public health authorities, following state and national guidelines.   
* The clinical performance of the test has not been established in all circulating variants, and test performance may vary depending on the prevalence of variants circulating at the time of patient testing.   
* Negative test results do not exclude possibility of exposure to or infection with SARS-CoV-2 virus. Patient handling will be directed by healthcare professionals.

## Conditions of Authorization for the Laboratory
The FloodLAMP QuickColor(TM) COVID-19 Test Letter of Authorization, along with the authorized Fact Sheet for Healthcare Providers, the authorized Fact Sheet for Patients, and authorized labeling are available on the FDA website: [https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas)

However, to assist clinical laboratories running the FloodLAMP QuickColor(TM) COVID-19 Test, the relevant Conditions of Authorization are listed below:

* Authorized laboratories1 using the FloodLAMP QuickColor(TM) COVID-19 Test will include all authorized Fact Sheets with test result reports. Under exigent circumstances, other appropriate methods for disseminating these Fact Sheets may be used, which may include mass media.  
* Authorized laboratories1 using the FloodLAMP QuickColor(TM) COVID-19 Test will use the FloodLAMP QuickColor(TM) COVID-19 Test as outlined in the FloodLAMP QuickColor(TM) COVID-19 Test Instructions for Use. Deviations from the authorized procedures, including the authorized clinical specimen types, authorized control materials, authorized other ancillary reagents and authorized materials required to perform the test are not permitted.  
* Authorized laboratories must notify the relevant public health authorities of their intent to run the test prior to initiating testing.  
* Authorized laboratories using the FloodLAMP QuickColor(TM) COVID-19 Test will have a process in place for reporting test results to healthcare providers and relevant public health authorities, as appropriate.  
* Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.  
* All laboratory personnel using the test must be appropriately trained in molecular assay techniques and use appropriate laboratory and personal protective equipment when handling these test components, and use the test in accordance with the authorized labeling.  
* FloodLAMP Biotechnologies, PBC authorized distributors, and authorized laboratories using the FloodLAMP QuickColor(TM) COVID-19 Test will ensure that any records associated with this EUA are maintained until otherwise notified by FDA. Such records will be made available to FDA for inspection upon request. 

1 For ease of reference, this will refer to, “Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a certified laboratories with FDA Emergency Use Authorization FDA for performing SARS-CoV-2 testing

## Specimen Collection and Storage
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19:  
[https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

* Samples can be stored at room temperature for 56 hours after collection prior to inactivation.   
* For longer term storage, samples can be stored at ≤-70oC.

Note: Specimens must be packaged, shipped, and transported according to the current edition of the International Air Transport Association Dangerous Goods Regulation. Follow shipping regulations for UN 3373 Biological Substance, Category B when sending potential 2019-nCoV specimens.

## Running Tests
### Reagent Preparation
The FloodLAMP QuickColor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. 

#### Table 1: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine HCl | 6M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| Colorimetric LAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalent. 

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 3 and vortexing for 30 seconds. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 3: 100X Inactivation Solution
| Component | Source Concentration | Volume | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

Swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 4. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 4: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :---: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

### Controls Preparation
**One positive and one negative control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes on each heater:

1) A “no template” (negative) control (NTC) is needed to **assure the absence of cross contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of 100X Inactivation Solution diluted to 1X in 0.9% saline. This NTC is the same solution added to dry swabs (see Table 3 and Table 4 above for the components).**  
     
2) A positive template control is needed to **assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 5 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.   
   
#### Table 5: Components for Positive Template Control
| Material | Vendor | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µl |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µl |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895 µl |
||

### 10X LAMP Primer Mix Preparation
The FloodLAMP QuickColor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 2. All 18 primers are mixed together and input into a single amplification reaction. 

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered.   
   
The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.  
   
Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at \-20°C for up to 1 year.

#### Table 6: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | # Reactions |
|---------|------|----------------|-----------|-------------|
| Order one of the following primer sets |||||
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

### Sample Preparation
\* For wet swab specimens (swabs in saline or unprocessed swab elution): 

1) If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.   
2) Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.   
3) Wipe the outside of the sample tube with 70% ethanol. 

For dry swab specimens:

1) Wipe the outside of the sample tube with 70% ethanol. 

### Sample Inactivation
1) Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and set the temperature to hold at 100 °C.  
2) \* For wet swab specimens: transfer 1 mL or available volume of each sample to an appropriately labeled 1.5 mL or 5mL tube and securely cap.   
3) \* For wet swab specimens: add 10μL per 1 mL sample volume of 100X Inactivation Solution to each sample tube.  
4) For dry swab specimens (DO NOT DO FOR WET SWAB SPECIMENS): add 1 mL of 1X Inactivation Solution to each sample tube.  
5) Vortex for 30 seconds.  
6) Place sample tubes into the inactivation heater for 8 minutes.  
7) Remove sample tubes from the inactivation heater and let cool at room temperature for 10 minutes.  
8) Place sample tubes on ice, in the refrigerator, or on a cold block at 4°C until ready to perform amplification reaction. 

Note: Testing of inactivated specimens must be conducted the same day inactivation is performed. For long term storage, keep the original specimen at ≤-70°C. 

### Colorimetric LAMP Amplification Reaction Preparation
1) Place a 96-well PCR plate or PCR strip tubes onto a cold block or ice.  
2) Thaw frozen reagents until ice crystals are not present.   
3) Pulse vortex thawed reagents and briefly spin down in a centrifuge.   
4) Store on ice, in the refrigerator, or on a cold block at 4°C until ready to use.  
5) Combine components of Primer-Guanidine Solution per volumes listed in Table 7, or proportionally scaled for the number of reactions to be run. 

      NOTE: Component volumes should be scaled proportionally for the number of reactions.   
      NOTE: The Primer-Guanidine Solution may be prepared in advance and stored at \-20°C    
      for up to 1 month.

6) Pulse vortex and briefly spin down in a centrifuge.   
7) Prepare the Colorimetric LAMP Amplification Reaction Mix by adding the Colorimetric LAMP MM to the Primer-Guanidine Solution per the volumes listed in Table 8.   
8) Vortex the Colorimetric LAMP Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
9) Add 23 µL of the Colorimetric LAMP Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

NOTE: Reaction plates/strip tubes comprising the Colorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at \-20°C for up to 3 days prior to addition of the sample. A heated plate sealer may be used to seal plates. Alternatively, a manually applied foil or optical seal may be used.

#### Table 7: Primer-Guanidine Solution
| Component | Volume (1 reaction) | Volume (1 reaction x 100) 1 x 96-plate w/ 4% overage |
| ----- | :---: | :---: |
| 10X LAMP Primer Mix | 2.5 µL | 250 µL |
| Guanidine HCl (400 mM) | 2.5 µL | - |
| Guanidine HCl (6 M) | - | 16.7 µL |
| Nuclease-free Water | 5.5 µL | 783 µL |
| **TOTAL VOLUME** | **10.5 µL** | **1050 µL** |
||

#### Table 8: Colorimetric LAMP Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| ----- | :---: | :---: |
| Primer-Guanidine Solution | 10.5 µL | 1050 µL |
| Colorimetric LAMP MM | 12.5 µL | 1250 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **2300 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **25 µL** | - |
||

### Sample Addition and Heating
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Turn on the amplification heater (a thermal cycler, water bath, dry heat bath or equivalent) and set the temperature to hold at 65°C.

NOTE: Amplification heater should be located in a separate, dedicated BSC or area of the lab. Proper cross contamination prevention practices are required, such as glove changes, to prevent amplicon contamination.

2) Add 2 μL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
3) Mix by pipetting.  
4) If using PCR plate, seal with foil seal, optical seal (optionally using heat sealer). If using PCR strip tubes, cap strips.  
5) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
6) Place the plate or strip tubes in the heater and set timer for 25 minutes (do not use heated lid).  
7) Remove the plate or strip tubes from the heater after 25 minutes.  
8) Let cool for 1 minute and then interpret the test results.

### Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. An example of the expected appearance of the negative and positive controls after amplification is shown in Figure 1.

**![][image1]![][image2]**

#### Figure 1. Negative control (left) and positive control (right) after amplification.

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and optionally RNAseZAP product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### Patient Specimen Results Interpretation
NOTE: Results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Test results should be read at least 1 minute and no more than 8 hours after plates or tubes have been removed from heat. Test results may be determined directly from visual inspection of the color of the reaction tubes: 

* yellow \- result is positive  
* bright pink or red \- result is negative  
* any other color \- result is invalid. 

Examples are shown below in Figure 2. Edge cases for positive and negative results are shown below in Figure 3. Any color variance stronger than the edge cases should be interpreted as inconclusive. In order to reduce the chance of both false negative and false positive results, this window for color variance is intentionally set to be small.

If the initial test is inconclusive, then one of the following should be performed:  
1) repeat the LAMP Amplification Reaction on the inactivated sample. If the repeat test has a positive result then the final interpretation of the test is positive. If the repeat test has a negative or another inconclusive result, then the final interpretation is inconclusive.  
2) follow up test the inactivated sample with the FloodLAMP EasyPCR(TM) COVID-19 Test or another high sensitivity EUA authorized test that comprises the same inactivation protocol. The final interpretation is the result of the follow up test.

For serial screening of individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, the initial inconclusive test result may be considered the final interpretation.

If the final interpretation of the test result is inconclusive, then "Inconclusive" should be reported and retesting of the individual is recommended. 

| ![][image3] |                  ![][image4]![][image5] |
| :---- | :---- |
| **Figure 2. Example of Test Results  (Left 2 Negative, Right 2 Positive)** |                         **Figure 3. Edge Case Test Results                          (Left Negative, Right Positive)** |

## Performance Evaluation
### Analytical Sensitivity: Limit of Detection (LoD)
The Limit of Detection (LoD) for the FloodLAMP QuickColor(TM) COVID-19 Test was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 12,500 and 6,250 were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 9. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 12,500 copies/mL.

#### Table 9: LoD Confirmatory Data Results
| Concentration of Contrived Positive Sample  | Replicates Detected |
| :---: | :---: |
| 12,500 copies/mL | 95% (20/21) |
| 6,250 copies/mL | 52% (11/21) |
||

### Analytical Sensitivity: Inclusivity (*in silico*)
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 10 summarizes the results of this *in silico* inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.	

#### Table 10: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total \# of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs ([primer-monitor.neb.com](http://primer-monitor.neb.com)), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 11, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 \-t 16 \-x asm5 \-a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having \>= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations are not expected to reduce performance of the FloodLAMP QuickColor(TM) COVID-19 Test by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 11: Variant Analysis of LAMP Primers
![][image6]  
![][image7]

### Analytical Specificity: Cross-Reactivity (*in silico*)
*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the FloodLAMP QuickColor(TM) COVID-19 Test against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 12A, 12B, and 12C. 

The % identity range (\# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with \>= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the *in silico* cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 12A: *In Silico* Cross-Reactivity Analysis for AS1e Primers

![][image8]

#### Table 12B: In Silico Cross-Reactivity Analysis for N2 Primers

![][image9]

#### Table 12C: *In Silico* Cross-Reactivity Analysis for E1 Primers

![][image10]

### Analytical Specificity: Cross-Reactivity (*wet testing*)
Wet testing was performed to demonstrate that the FloodLAMP QuickColor(TM) COVID-19 Test does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen.  SARS-CoV, RSV, Flu, Human Metapneumovirus. and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 13. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 13.

#### Table 13: Wet Testing Cross-Reactivity Results
| Organism | Description | BEI Number | Detected Replicates |
| ----- | ----- | :---: | :---: |
| SARS-CoV | UV-inactivated virus | NR-3882 | 0/3 |
| Human Metapneumovirus | Genomic RNA | NR-49122 | 0/3 |
| RSV | Genomic RNA | NR-43976 | 0/3 |
| Influenza B | Genomic RNA | NR-45848 | 0/3 |
| Streptococcus salivarius | Bacterial cell culture | HM-121 | 0/3 |
||

### Analytical Specificity: Interfering Substances
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP QuickColor(TM) COVID-19 Test. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 14 and Supporting Data.

#### Table 14: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

## Clinical Evaluation
The clinical evaluation of the FloodLAMP QuickColor(TM) COVID-19 Test utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The FloodLAMP QuickColor(TM) COVID-19 Test showed a positive agreement of 90% and a negative agreement of 100%. The 4 false negative results were specimens with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is below in Table 15. 

#### Table 15: Clinical Evaluation Results
| FloodLAMP QuickColor(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 36 | 0 | 36 |
| Negative | 4 | 40 | 44 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 90.0% (36/40) 95% CI: 76.3% to 97.2% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## Support
FloodLAMP Biotechnologies, PBC support center   
eua.support@floodlamp.bio  
650-394-5233


# 10,208  2021-03-26_EUA Submission - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-03-26_EUA Submission - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.md
file_date: 2021-03-26
title: EUA Submission - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1PAAR6WuaB1MjEhA4vN5t6lf5X7nY1Uhw
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-03-26_EUA%20Submission%20-%20FloodLAMP%20FLAMP%20COVID-19%20Test%20NOT%20SUBMITTED.docx
pdf_gdrive_url: https://drive.google.com/file/d/1GkGtknrbFOSlAWkbv3wf5cs2JfuQNd-x
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-03-26_EUA%20Submission%20-%20FloodLAMP%20FLAMP%20COVID-19%20Test%20NOT%20SUBMITTED.pdf
conversion_input_file_type: docx
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10208
words: 6078
notes: 
summary_short: The EUA Submission draft for the FloodLAMP QuickFluor COVID-19 Test (not submitted) describes an extraction-free, fluorimetric RT-LAMP assay using ORF1ab/N/E primer sets and real-time fluorescence readout on validated RT-PCR instruments (e.g., QuantStudio 7 Pro and Bio-Rad CFX96). It specifies the sample inactivation workflow, reaction setup, controls, and result interpretation criteria, along with proposed “open source” component sourcing for CLIA high-complexity labs. It summarizes stated performance claims including a 50,000 copies/mL LoD and clinical agreement results (80% positive agreement, 100% negative agreement) from an 80-specimen evaluation.


CONTENT

***INTERNAL TITLE:*** EUA Submission - FloodLAMP QuickFluor(TM) COVID-19 Test
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for distribution and/or use of the **FloodLAMP QuickFluor(TM) COVID-19 Test** for the *in vitro* qualitative detection of RNA from the SARS-CoV-2 in upper respiratory specimens including oropharyngeal and nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests *.*** Additional testing and confirmation procedures should be performed in consultation with public health and/or other authorities to whom reporting is required. Test results should be reported in accordance with local, state, and federal regulations.

## B. MEASURAND
Specific nucleic acid sequences from the genome of the SARS-CoV-2, targeted by **primers from the ORF1ab, N & E regions** of the virus. Primer names and sequences are listed in Table 1.

#### Table 1: Primer names and sequences
| Primer Name | Sequence (5’-3’) |
| :---- | :---- |
| **ORF1ab gene (AS1e)** |   |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |   |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |   |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

## C. APPLICANT
FloodLAMP Biotechnologies, a DE Public Benefit Corporation  
Mailing Address:  
4860 Alpine Rd.  
Portola Valley, CA 94028

Laboratory Address:  
FloodLAMP at MBC Biolabs  
930 Brittan Ave San Carlos, CA 94070  
San Carlos, CA 94070	

Randall J. True  
Founder and CEO  
Phone: (415) 269-2974  
Email: randy@floodlamp.bio

## D. PROPRIETARY AND ESTABLISHED NAMES
Proprietary Name \- **FloodLAMP QuickFluor(TM) COVID-19 Test**  
Established Name \- **FloodLAMP QuickFluor(TM) COVID-19 Test**

## E. REGULATORY INFORMATION
***Approval/Clearance Status:***

The **FloodLAMP QuickFluor(TM) COVID-19 Test** is not cleared, CLIA waived, approved, or subject to an approved investigational device exemption.

***Product Code:*** 

QJR

## F. PROPOSED INTENDED USE
### 1) Intended Use:
**FloodLAMP QuickFluor(TM) COVID-19 Test** is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests.** Testing is limited to **laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories.** 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis  
for patient management decisions. Negative results must be combined with clinical observations,  
patient history, and epidemiological information.

The **FloodLAMP QuickFluor(TM) COVID-19 Test** is intended for use by **qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures**. The **FloodLAMP QuickFluor(TM) COVID-19 Test** is only for use under the Food and Drug Administration’s Emergency Use Authorization.

### 2) Special Conditions for Use Statements:
For Emergency Use Authorization (EUA) only   
For prescription use only  
For *in vitro* diagnostic use only

### 3) Special Instrument Requirements:
The **FloodLAMP QuickFluor(TM) PCR COVID-19 Test** test is to be used with the RT-PCR instruments listed in Table 2.

#### Table 2. RT-PCR Instruments validated for test
| Manufacturer | Instrument |
| :---: | :---: |
| ThermoFisher Scientific | Applied Biosystems QuantStudio 7 Pro |
| Bio-Rad | CFX96 Touch Real-Time PCR Detection System |
||

Designated laboratories will receive an FDA accepted instrument qualification protocol included as part of the **FloodLAMP QuickFluor(TM) Covid-19 Test** IFU and will be directed to execute the protocol prior to testing clinical samples. Designated laboratories must follow the authorized IFU, which includes the instrument qualification protocol, as per the letter of authorization.

## G. DEVICE DESCRIPTION AND TEST PRINCIPLE
### 1) Product Overview/Test Principle:
The **FloodLAMP QuickFluor(TM) COVID-19 Test** is an RNA-extraction free isothermal RT-LAMP assay which indicates that SARS-CoV-2 RNA is present. FloodLAMP’s test uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. Loop Mediated Isothermal Amplification (LAMP) is a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. An intercalating fluorescent dye is also included in the reaction mix, enabling the real time fluorescence detection of amplicons. A RT-PCR Instrument is utilized for the isothermal amplification incubation and real time fluorescence readout. 

### 2) Description of Test Steps: 
Specimens including **nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs** are collected in **sterile collection tubes.** Swabs are transported and stored dry prior to processing. At the laboratory, an inactivation solution at 1X containing TCEP (2.5 mM), EDTA (1 mM), and NaOH (11 mM) in 0.9% saline (154 mM) is added to the container with the swab, at the volume of 1ml. Alternatively, for swabs that are collected or eluted in a saline solution or equivalent, the inactivation solution at 100X concentration should be added at 1/100th the sample solution volume. 

The container with the specimen and inactivation solution is mixed by vortexing for 30 seconds. Subsequently, the container is heated in a 95°C water bath or dry heat block for 8 minutes. The now inactivated specimen container is allowed to cool at room temperature for 10 minutes and then stored on ice or at 4°C until amplification.

An amplification reaction mix (23 µL) is prepared per manufacturer's specifications, containing the Fluorimetric LAMP master mix (New EB E1700, 12.5 µL), Fluorescent Dye (NEB E1700, .5 µL) a 10X LAMP Primer Mix (2.5 µL of 10X w FIP/BIP at 16 µM, F3/B3 at 2 µM, and LF/BF at 4 µM), and nuclease-free water (7.5 µL). 

2µL of the inactivated sample is added to 23µL of the amplification reaction mix. The reaction is then run with the following thermocycler conditions in Table 3:

#### Table 3. Thermal cycling conditions and plate read steps 
| Stage | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 65 C | 10 sec | 1 |
| 2 | 65 C | 10 sec | 1 |
| 3 | 65 C | 30 sec | 25 |
| 3 | 65\* C | 30 sec | 25 |
||

*\* This step should be the optical read step*

### 3) Control Materials to be Used with FloodLAMP QuickFluor(TM) COVID-19 Test:
**One Positive Template Control and one Negative (No Template) Control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes. 

1) A **“No Template” (Negative) Control (NTC) is needed to assure the absence of cross-contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of nuclease-free water.**  
     
2) A **Positive Template Control is needed to assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 4 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.  

#### Table 4. Components for Positive Template Control 
| Material | Supplier | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µL |
| Total Human RNA | Thermo | 4307281 | 100 µL |
| Nuclease-free Water | Thermo | 10977015 | 4,895 µL |
||

## H. INTERPRETATION OF Results
### 1) FloodLAMP QuickFluor(TM) COVID-19 Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to Table 5 below.

1) The “No Template” (Negative) Control (NTC) should yield a negative “not detected” result for the Sars target.  
     
2) The Positive Template Control should yield a positive “detected” result for the Sars target.

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP(TM) product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### 2) Examination and Interpretation of Patient Specimen Results:
Assessment of clinical specimen test results should be performed after the positive and negative controls have been examined and determined to be valid and acceptable. If the controls are not valid, the patient results cannot be interpreted. Patient specimen results will be interpreted according to Table 5 below.

#### Table 5: Test Results and Interpretation
| ABI QuantStudio(TM) 7 Pro Bio-Rad CFX96 Touch(TM) |  |
| :---: | :---: |
| **Result** | **Ct Value: ORF1ab, N2 & E1** |
| Positive | ≤25.0 |
| Negative | Undetermined |
||

## I. PRODUCT MANUFACTURING
### 1) Overview of Manufacturing and Distribution: 
The **FloodLAMP QuickFluor(TM) COVID-19 Test** utilizes standard chemicals available in very large quantities from multiple vendors, with the exception of the LAMP Primers and New England Biolabs Fluorimetric LAMP Master Mix. 

FloodLAMP has partnered with LGC Biosearch for the LAMP Primers. LGC Biosearch has very large scale oligo production capacity and mature distribution capabilities. The first production scale lot of the LAMP Primers has been completed, with 1.2 million reactions ready for immediate distribution. FloodLAMP has purchased 600K reactions of the LAMP Primers. LGC Biosearch is supplying FloodLAMP for the **FloodLAMP QuickFluor(TM) COVID-19 Test** and is also offering the LAMP Primers as a catalog product. 

New England Biolabs has expressed strong support for the **FloodLAMP QuickFluor(TM) COVID-19 Test** and FloodLAMP's other open source protocol EUA submissions that incorporate their products. New England Biolabs has very large quantities of the Fluorimetric LAMP Master Mix product prepared and ready for immediate distribution, typically with 24 hour shipping within the U.S. Their manufacturing capacity is among the largest in the United States and can surge to meet increased demand.

**\*Under the Emergency Use Authorization (EUA) any of the 21 CFR Part 820 Quality System Regulation (QSR) requirements can be waived for the duration of the EUA but FDA recommends that developers follow comparable practices as much as possible if such requirements are waived. Among other things, FDA may consider previous compliance history when determining whether or not to waive certain QSR requirements for a specific product. Please note adverse events, as per 21 CFR Part 803, have to be reported for authorized devices (see Section P).** 

### 2) Components Included with the Test:
None. Designated CLIA labs may order components directly from vendors.

### 3) Components Required But Not Included with Test:
The **FloodLAMP QuickFluor(TM) COVID-19 Test** is to be used with the reagents or equivalents listed in Table 6. 

#### Table 6: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog No. |
| :---- | ----- | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease free | Thermo | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo | 24740011 |
| Fluorimetric LAMP Kit\* | - | Fluorimetric LAMP Kit | New England Biolabs | E1700 |
||

\* Item may not be substituted for equivalents. Only the specified vendor and catalog number may be utilized.

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 7. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 7: 100X Inactivation Solution
| Component | Source Concentration | Volume for 100X | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 5. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 8: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :---: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

The **FloodLAMP QuickFluor(TM) COVID-19 Test** uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 1. All 18 primers are mixed together and input into a single amplification reaction. 

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered. 

The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease-free water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.

Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at \-20°C for up to 1 year.

#### Table 9: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | # Reactions |
|---------|------|----------------|-----------|-------------|
| Order one of the following primer sets |||||
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orflab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

The final Fluorimetric LAMP Amplification Reaction components are listed in Table 9. PCR plates or strip tubes used for the amplification reactions should be maintained on ice or a cold block until less than 5 minutes before incubation on the heater. Reaction plates/strip tubes comprising the Fluorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at \-20°C for up to 1 day prior to addition of the sample. A heated plate sealer is recommended. Alternatively, a manually applied foil or optical seal may be used.

#### Table 10: Fluorimetric LAMP Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| :---- | :---: | :---: |
| 10X LAMP Primer Mix | 2.5 µL | 250 µL |
| Nuclease Free Water | 7.5 µL | 750 µL |
| Fluorimetric LAMP MM | 12.5 µL | 1250 µL |
| Fluorescent Dye | .5 µL | 50 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **2300 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **25 µL** | - |
||

### 4) Software Validation:
The **FloodLAMP QuickFluor(TM) COVID-19 Test** has been validated on the RT-PCR instruments listed in Table 2 using the baseline threshold settings unless otherwise noted in the Instructions for Use. The test does not require any additional software.

### 5) Testing Capabilities: 
The **FloodLAMP QuickFluor(TM) COVID-19 Test** has been optimized for a streamlined workflow and rapid turnaround time on results. The total time to perform the test is dependent upon the following factors: number of lab technicians, batch size of samples, and in advance preparation of reaction mixes as well as availability of RT-qPCR instruments. The minimum turnaround time is approximately 1 hour, of which approximately 30 minutes is the RT-PCR instrument run time. Automation can greatly increase overall throughput.

### 6) Reagent Stability: 
A stability test plan for the components of the **FloodLAMP QuickFluor(TM) COVID-19 Test** will be developed during an interactive review. Briefly, the proposed study includes assessing all prepared solutions including: 100X Inactivation Solution, 1X Inactivation Saline Solution, 30X Primer Stock, 10X Primer Mix, and the full Fluorimetric LAMP Amplification Reaction Mix. Prepared solutions will be assessed both for long term storage stability (typically 1-3 months at \-20oC) and short term storage stability prior to usage (typically hours to several days at room temperature, 4oC or \-20oC). 

The proposed study uses a contrived positive sample consisting of inactivated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative specimens at approximately 50,000 copies/mL (4X LoD). The contrived positive stability study samples will be prepared, aliquoted and stored at \-80oC to permit repeated testing of the various solutions at the appropriate step of the test protocol.

For test components supplied by vendors, such as the Fluorimetric LAMP Kit, the manufacturer's recommended storage conditions and duration will be followed.

### 7) Sample Stability:
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19: [www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

Samples can be stored at room temperature for 56 hours after collection prior to inactivation. For longer term storage, samples can be stored at ≤-70oC.

## J. PERFORMANCE EVALUATION
### 1) Limit of Detection (LoD) \- Analytical Sensitivity:
The Limit of Detection (LoD) for the **FloodLAMP QuickFluor(TM) COVID-19 Test** was established using gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LOD study. A preliminary LOD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 50,000, 25,000 and 12,500 copies/mL  were selected for confirmatory LOD runs. LOD run details are provided in Supporting Data, with the results summarized below in Table 10. The LOD, defined as the concentration at which at least 95% of the samples are positive, was determined at 50,000 copies/mL.

#### Table 11: Confirmatory LOD Data Results
| Instrument | LOD | Positive Replicates | Mean Ct Value (SD) |
| ----- | :---: | :---: | :---: |
| ABI QuantStudio 7 Pro | 50,000 copies/mL | 95% (20/21) | 11.9 (1.5) |
| Bio-Rad CFX96 | - | - | - |
||

### 2) Inclusivity (analytical sensitivity): 
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 11 summarizes the results of this in silico inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.	

#### Table 12: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total Number of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

#### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs ([primer-monitor.neb.com](https://primer-monitor.neb.com/)), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 12, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 \-t 16 \-x asm5 \-a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having \>= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations are not expected to reduce performance of the **FloodLAMP QuickFluor(TM) COVID-19 Test**  by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 13: Variant Analysis of LAMP Primers
![][image1]  
![][image2]

### 3) Cross-reactivity (Analytical Specificity):  
*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the **FloodLAMP QuickFluor(TM) COVID-19 Test**  against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 14A, 14B, and 14C. 

The % identity range (\# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with \>= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the in silico cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 14A: *In Silico* Cross-Reactivity Analysis for AS1e Primers
![][image3]

#### Table 14B: *In Silico* Cross-Reactivity Analysis for N2 Primers
![][image4]

#### Table 14C: *In Silico* Cross-Reactivity Analysis for E1 Primers
![][image5]

Wet testing was performed to demonstrate that the **FloodLAMP QuickFluor(TM) COVID-19 Test** does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen.  SARS-CoV, RSV, Flu, Human Metapneumovirus, and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 15 and Supporting Data. 5 µL of each stock of cross-reactivity organism was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived positive had 38 µL of 1e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 38,000 copies/mL in the sample input into the amplification reaction.

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 15.

#### Table 15: Wet Testing Cross-Reactivity Results
| Organism | Description | BEI  Number | Detected Replicates |
| ----- | ----- | :---: | :---: |
| SARS-CoV | UV-inactivated virus | NR-3882 | 0/3 |
| Human Metapneumovirus | Genomic RNA | NR-49122 | 0/3 |
| RSV | Genomic RNA | NR-43976 | 0/3 |
| Influenza B | Genomic RNA | NR-45848 | 0/3 |
| Streptococcus salivarius | Bacterial cell culture | HM-121 | 0/3 |
||

#### Endogenous Interference Substances Studies:
Exogenous and endogenous substances were tested for potential interference with the **FloodLAMP QuickFluor(TM) COVID-19 Test*.***10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 16 and Supporting Data.

#### Table 16: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
|| 

### 4) Clinical Evaluation: 
The clinical evaluation of the **FloodLAMP QuickFluor(TM) COVID-19 Test** utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The **FloodLAMP QuickFluor(TM) COVID-19 Test** showed a positive agreement of 80% and a negative agreement of 100%. The 6 false negative results were specimens with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is below in Table 16.

Anterior nares swab specimens were collected from patients in phosphate buffered saline by the Stanford COVID-19 clinical testing program. Specimens were initially tested by the Stanford clinical laboratory using the Hologic Panther Fusion and Aptima SARS-CoV-2 Assays, which serves as the high sensitivity comparator test. 

For the **FloodLAMP QuickFluor(TM) COVID-19 Test**, materials and the Instructions For Use were provided to the Stanford clinical laboratory. The materials provided consisted of the validated reagents listed in Table 3, the LGC primers and probes, and an aliquot of the positive control. After thawing the frozen specimens, 1 mL of each specimen was transferred to 5mL tubes for the inactivation step. The positive and negative clinical specimens were assigned a new ID in a random order, then transferred to new tubes that were barcoded and labeled with the new ID. The Bio-Rad CFX96 instrument was used to perform the isothermal amplification. Line Item data are provided in the Supporting Data. 

#### Table 16: Clinical Evaluation Results
| FloodLAMP QuickFluorr(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 34 | 0 | 34 |
| Negative | 6 | 40 | 46 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 80.0% (34/40) 95% CI: 70.2% to 94.3% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## K. UNMET NEED ADDRESSED BY THE PRODUCT 
This section will be completed by FDA. 

## L. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for the detection of the SARS-CoV-2 have been approved/cleared by FDA.

## M. BENEFITS AND RISKS:
This section will be completed by FDA.

## N. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS:
Fact Sheets for Patients and Healthcare Providers attached.

## O. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT:
Instructions for Use attached.

## P. RECORD KEEPING AND REPORTING INFORMATION TO FDA:
Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.

QuantStudio  is a trademark of Thermo Fisher Scientific (NYSE: TMO)

Bio-Rad and Bio-Rad CFX96 Touch  is a trademark of Bio-Rad Laboratories, Inc. (NYSE: BIO)


# 15,131  2021-03-26_Instructions for Use - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-03-26_Instructions for Use - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED.md
file_date: 2021-03-26
title: Instructions for Use - FloodLAMP FLAMP COVID-19 Test NOT SUBMITTED
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1fsdl_yjBbAV7MnQiwihumJziZApkTa1IJ8RewS4qz-U
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-03-26_Instructions%20for%20Use%20-%20FloodLAMP%20FLAMP%20COVID-19%20Test%20NOT%20SUBMITTED.docx
pdf_gdrive_url: https://drive.google.com/file/d/16kki-qqeTDNdmg-mscq5PByURqvKy3hC
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-03-26_Instructions%20for%20Use%20-%20FloodLAMP%20FLAMP%20COVID-19%20Test%20NOT%20SUBMITTED.pdf
conversion_input_file_type: gdoc
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 15131
words: 9483
notes: 
summary_short: The draft Instructions for Use for the FloodLAMP QuickFluor COVID-19 Test describe an extraction-free, fluorimetric RT-LAMP assay with real-time fluorescence detection on RT-PCR instruments following chemical and heat inactivation. It provides detailed procedures for reagent and primer preparation, instrument setup, workflow execution, controls, and Ct-based result interpretation for CLIA high-complexity laboratories. It also documents proposed analytical and clinical performance, including a 50,000 copies/mL LoD and 80–85% positive agreement with 100% negative agreement in an 80-specimen clinical evaluation, for a test that was not submitted for EUA.


CONTENT

***INTERNAL TITLE:*** FloodLAMP QuickFluor(TM) COVID-19 Test
Instructions for Use v1.0 \*\*DRAFT\*\*

IVD
COVID-19 Emergency Use Authorization Only
For *in vitro* diagnostic (IVD) Use

www.floodlamp.bio
FloodLAMP Biotechnologies, PBC | 930 Brittan Ave. San Carlos, CA 94070 USA

## Table of Contents
|  |  |
|---------|------|
| Intended Use | 3 |
| Principles of Procedure | 3 |
| Materials Provided and Storage | 4 |
| Materials Required but Not Provided | 4 |
| • Standard Lab Equipment and Consumables | 5 |
| Warnings and Precautions | 6 |
| • General Precautions | 6 |
| • Contamination Precautions | 7 |
| Limitations | 7 |
| Conditions of Authorization for the Laboratory | 8 |
| Specimen Collection and Storage | 9 |
| Running Tests | 10 |
| • Reagent Preparation | 10 |
| • Controls Preparation | 11 |
| • 10X LAMP Primer Mix Preparation | 12 |
| • Sample Preparation | 13 |
| • Sample Inactivation | 14 |
| • Preparing to Run Assay for the First Time | 14 |
| • Create the Plate Layout Map | 16 |
| • Fluorimetric LAMP Amplification Reaction Preparation | 18 |
| • Sample Addition | 19 |
| • Run the Assay | 19 |
| • Analyzing Data | 21 |
| • Results Interpretation | 22 |
| • Patient Specimen Results Interpretation | 22 |
| Performance Evaluation | 23 |
| • Analytical Sensitivity: Limit of Detection (LoD) | 23 |
| • Analytical Sensitivity: Inclusivity (*in silico*) | 23 |
| • Evaluation of Impact of Viral Mutations | 24 |
| • Analytical Specificity: Cross-Reactivity (*in silico*) | 26 |
| • Analytical Specificity: Cross-Reactivity (wet testing) | 30 |
| • Analytical Specificity: Interfering Substances | 31 |
| Clinical Evaluation | 32 |
| Support | 32 |
||

FloodLAMP QuickFluor(TM) COVID-19 Test  
For COVID-19 Emergency Use Authorization Only  
Instructions for Use

## Intended Use
FloodLAMP QuickFluor(TM) COVID-19 Test is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories. 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The FloodLAMP QuickFluor(TM) COVID-19 Test is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures. The FloodLAMP QuickFluor(TM) COVID-19 Test is only for use under the Food and Drug Administration’s Emergency Use Authorization.

## Principles of Procedure
The FloodLAMP QuickFluor(TM) COVID-19 Test uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. It uses Loop Mediated Isothermal Amplification (LAMP), a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. Samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step. The resulting inactivated sample is directly used as input in the LAMP reaction. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. An intercalating fluorescent dye is also included in the reaction mix, enabling the real-time fluorescence detection of amplicons. An RT-PCR Instrument is utilized for the isothermal amplification incubation and real-time fluorescence readout.

## Materials Provided and Storage
The FloodLAMP QuickFluor(TM) COVID-19 Test utilizes standard chemicals available from multiple vendors, with the exception of the LAMP primers and Fluorimetric LAMP master mix. Designated CLIA labs may order components directly from vendors.

## Materials Required but Not Provided
The FloodLAMP QuickFluor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. The FloodLAMP QuickFluor(TM) COVID-19 Test is to be used with RT-PCR Instruments such as Applied Biosystems QuantStudio(TM) Systems and Bio-Rad CFX(TM) Systems.

#### Table 1: Validated reagents used with the Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | ----- | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| LAMP Kit\* | - | Fluorimetric LAMP Kit | New England Biolabs | E1700 |
||

\* Item may not be substituted for equivalent. Only the specified vendor and catalog number may be utilized.

The FloodLAMP QuickFluor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. All 18 primers are mixed together and are input into a single amplification reaction. Primer names and sequences are listed in Table 2. Primers may be purchased pre-blended from the vendor LGC Biosearch Technologies with the product names LAMP\_S2-As1e, LAMP\_S2-N2, LAMP\_S2-E1. Alternatively, primers may be purchased as individual custom oligos. Appropriate validation of primer mixes from custom oligos is required. See Primer Preparation below for more information. 

#### Table 2: Primer names and sequences
| Primer Name | Sequence (5’-3’) |
| :---- | :---- |
| **ORF1ab gene (AS1e)** |   |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |   |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |   |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

### Standard Lab Equipment and Consumables
* 70% ethanol  
* 10% bleach, prepared daily  
* 96-well PCR reaction plates (Applied Biosystems \# 4346906, 4366932, 4346907, Eppendorf \# 951020303 or equivalent)  
* Optical strip caps (Applied Biosystems \# 4323032 or equivalent)  
* Optical plate seal (Applied Biosystems \# 4311971 or equivalent)  
* PCR strip tubes and caps (USA Scientific catalog \# 1402-2500 or equivalent)   
* 5 mL transport tubes or equivalent (sterile)  
* 1.5 mL microcentrifuge tubes or equivalent (nuclease-free)  
* Aerosol resistant micropipette tips (nuclease-free)  
* Micropipettes (calibrated)  
* Bottle top dispenser for 1 mL volume (optional, calibrated)  
* 96-well cold block  
* Cold blocks for 5 mL and 1.5 mL \- 2.0 mL tubes, or ice  
* Vortex mixer  
* 96-well plate centrifuge or equivalent  
* Mini centrifuge for 1.5 mL tubes or equivalent  
* Thermal cycler, water bath, dry heat bath or equivalent (calibrated)  
* Class II Biological Safety Cabinet (BSC)   
* PCR Instrument (Choose 1)  
  * QuantStudio(TM) 7 Pro  
  * Bio-Rad CFX96 Touch(TM)

## Warnings and Precautions
Materials or chemicals required for the use of the FloodLAMP QuickFluor(TM) COVID-19 Test should be closely examined by the user. The user should carefully read all warnings, instructions or Safety Data Sheets provided by the supplier and follow the general safety precautions when handling biohazards, chemicals and other materials. 

### General Precautions
* The FloodLAMP QuickFluor(TM) COVID-19 Test is for *in vitro* diagnostic use (IVD) only. Rx Only.  
* For use under COVID-19 Emergency Use Authorization Only.  
* Standard precautions and procedures should be taken when handling and disposing of human samples.  
* This test has not been FDA cleared or approved; the test has been authorized by FDA under an Emergency Use Authorization (EUA) for use by laboratories certified under the Clinical Laboratory Improvement Amendments (CLIA) of 1988, 42 U.S.C. §263a, to perform high complexity tests.  
* This test has been authorized only for the detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens.  
* This test is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of *in vitro* diagnostic tests for detection and/or diagnosis of COVID19 under Section 564(b)(1) of the Act, 21 U.S.C. § 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner.  
* Standard precautions and procedures should be taken when handling and extracting human samples.  
* Standard precautions and procedures should be taken when using laboratory equipment.  
* Standard precautions and procedures should be taken when disposing of waste.  
* Dispose of reagents according to local regulations.  
* Do not use reagents after their recommended stability time frame.  
* Ensure reagents are stored at the recommended temperatures as described below and in the vendor product information and manuals.

### Contamination Precautions
* Avoid contamination by following good laboratory practices, wearing proper personal protective equipment, segregating workflow, and decontaminating workspace appropriately.  
* Ensure that surfaces and equipment used for all test steps have been properly cleaned with 10% bleach and 70% ethanol.  
* Ensure all consumables are DNase and RNase free except for sample collection tubes which may be sterile.  
* Use only calibrated pipettes and filter tips that are sterile and PCR clean.  
* After completion of the test, dispose of the amplification reaction plates or tubes. **Do not open tubes** or remove the seals on plates after heating amplification reactions.

## Limitations
* The use of this assay as an *in vitro* diagnostic under the FDA COVID-19 Emergency Use Authorization (EUA) is limited to laboratories that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. § 263a, to perform high complexity tests by Rx only.   
* Use of this assay is limited to personnel who are trained in the procedure. Failure to follow these instructions may lead to erroneous results.   
* The performance of the FloodLAMP QuickFluor(TM) COVID-19 Test was established using Nasopharyngeal Swab specimen type collected in saline. Nasal swabs, oropharyngeal swabs, mid-turbinate nasal swabs specimens are also considered acceptable specimen types for use with the test but performance has not been established.   
* Samples must be collected according to recommended protocols and transported and stored as described herein.  
* Samples should not be collected in UTM or VTM or Liquid Amies transport media.  
* The effect of vaccines, antiviral therapeutics, antibiotics, chemotherapeutic or immunosuppressant drugs have not been evaluated.  
* Detection of SARS-CoV-2 RNA may be affected by sample collection methods, patient factors (e.g., presence of symptoms), and/or stage of infection.  
* False-positive results may arise from various reasons, including, but not limited to the following:  
  * Contamination during specimen collection, handling, or preparation  
  * Contamination during assay preparation  
  * Incorrect sample labeling  
* False-negative results may arise from various reasons, including, but not limited to the following:  
  * Improper sample collection or storage  
  * Degradation of SARS-CoV-2 RNA  
  * Presence of inhibitory substances  
  * Use of extraction reagents or instrumentation not approved with this assay   
  * Incorrect sampling window  
  * Failure to follow instructions for use  
  * Mutations In SARS-CoV-2 target sequences  
* Nucleic acid may persist even after the virus is no longer viable.   
* This test cannot rule out diseases caused by other bacterial or viral pathogens.  
* Performance has not yet been established in asymptomatic individuals and will be established during a post-authorization study.   
* Use of the test in a general, asymptomatic population for serial screening is intended to be used as part of an infection control plan, that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should not be treated as definitive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual’s recent exposures, history, and presence of clinical signs and symptoms consistent with COVID-19.  
* This test should not be used within 30 minutes of administering nasal or throat sprays.  
* Positive results must be reported to appropriate public health authorities, following state and national guidelines.   
* The clinical performance of the test has not been established in all circulating variants, and test performance may vary depending on the prevalence of variants circulating at the time of patient testing.   
* Negative test results do not exclude possibility of exposure to or infection with SARS-CoV-2 virus. Patient handling will be directed by healthcare professionals.

## Conditions of Authorization for the Laboratory
The FloodLAMP QuickFluor(TM) COVID-19 Test Letter of Authorization, along with the authorized Fact Sheet for Healthcare Providers, the authorized Fact Sheet for Patients, and authorized labeling are available on the FDA website: [https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas)

However, to assist clinical laboratories running the FloodLAMP QuickFluor(TM) COVID-19 Test, the relevant Conditions of Authorization are listed below:

* Authorized laboratories1 using the FloodLAMP QuickFluor(TM) COVID-19 Test will include all authorized Fact Sheets with test result reports. Under exigent circumstances, other appropriate methods for disseminating these Fact Sheets may be used, which may include mass media.  
* Authorized laboratories1 using the FloodLAMP QuickFluor(TM) COVID-19 Test will use the FloodLAMP QuickFluor(TM) COVID-19 Test as outlined in the FloodLAMP QuickFluor(TM) COVID-19 Test Instructions for Use. Deviations from the authorized procedures, including the authorized clinical specimen types, authorized control materials, authorized other ancillary reagents and authorized materials required to perform the  test are not permitted.  
* Authorized laboratories must notify the relevant public health authorities of their intent to run the test prior to initiating testing.  
* Authorized laboratories using the FloodLAMP QuickFluor(TM) COVID-19 Test will have a process in place for reporting test results to healthcare providers and relevant public health authorities, as appropriate.  
* Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.  
* All laboratory personnel using the test must be appropriately trained in molecular assay techniques and use appropriate laboratory and personal protective equipment when handling these test components, and use the test in accordance with the authorized labeling.  
* FloodLAMP Biotechnologies, PBC authorized distributors, and authorized laboratories using the FloodLAMP QuickFluor(TM) COVID-19 Test will ensure that any records associated with this EUA are maintained until otherwise notified by FDA. Such records will be made available to FDA for inspection upon request. 


1 For ease of reference, this will refer to, “Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a certified laboratories with FDA Emergency Use Authorization FDA for performing SARS-CoV-2 testing

## Specimen Collection and Storage
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19:  
[https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

* Samples can be stored at room temperature for 56 hours after collection prior to inactivation.   
* For longer term storage, samples can be stored at ≤-70oC.

Note: Specimens must be packaged, shipped, and transported according to the current edition of the International Air Transport Association Dangerous Goods Regulation. Follow shipping regulations for UN 3373 Biological Substance, Category B when sending potential 2019-nCoV specimens.

## Running Tests
### Reagent Preparation
The FloodLAMP QuickFluor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. 

#### Table 1: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | ----- | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| LAMP Kit\* | - | Fluorimetric LAMP Kit | New England Biolabs | E1700 |
||

\* Item may not be substituted for equivalent. 

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 3 and vortexing for 30 seconds. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 3: 100X Inactivation Solution
| Component | Source Concentration | Volume | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 4. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 4: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :----: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

### Controls Preparation
**One positive and one negative control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes on each heater:

1) A “no template” (negative) control (NTC) is needed to **assure the absence of cross contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of nuclease-free water.**  
     
2) A positive template control is needed to **assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 5 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.   
   
#### Table 5: Components for Positive Template Control
| Material | Vendor | Catalog \# | Volume |
| :---- | :----: | :----: | :----: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µl |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µl |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895 µl |
||

### 10X LAMP Primer Mix Preparation {#10x-lamp-primer-mix-preparation}
The FloodLAMP QuickFluor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 2. All 18 primers are mixed together and input into a single amplification reaction. 

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered.   
   
The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease-free water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.  
   
Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at \-20°C for up to 1 year.

#### Table 6: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | # Reactions |
|--------|------|----------------|-----------|-------------|
| Order one of the following primer sets |||||
| LGC Biosearch Technologies | SARS-CoV-2 LAMP ASIe 6 primer set at 30X (ORF1ab gene) | LAMP_S2-ASIe-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP ASIe 6 primer set at 30X (ORF1ab gene) | LAMP_S2-ASIe-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

### Sample Preparation
\* For wet swab specimens (swabs in saline or unprocessed swab elution): 

1) If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.   
2) Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.   
3) Wipe the outside of the sample tube with 70% ethanol. 

For dry swab specimens:
1) Wipe the outside of the sample tube with 70% ethanol. 

### Sample Inactivation
1) Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and set the temperature to hold at 100°C.  
2) \* For wet swab specimens: transfer 1 mL or available volume of each sample to an appropriately labeled 1.5 mL or 5 mL tube and securely cap.   
3) \* For wet swab specimens: add 10 µL per 1 mL sample volume of 100X Inactivation Solution to each sample tube.  
4) For dry swab specimens (DO NOT DO FOR WET SWAB SPECIMENS): add 1 mL of 1X Inactivation Solution to each sample tube.  
5) Vortex for 30 seconds.  
6) Place sample tubes into the inactivation heater for 8 minutes.  
7) Remove sample tubes from inactivation heater and let cool at room temperature for 10 minutes.  
8) Place sample tubes on ice, in the refrigerator, or on a cold block at 4°C until ready to perform amplification reaction. 

Note: Testing of inactivated specimens must be conducted the same day inactivation is performed. For long term storage, keep the original specimen at ≤-70°C. 

### Preparing to Run Assay for the First Time
*Note: Any instrument running the FloodLAMP QuickFluor(TM) COVID-19 Test must be calibrated for the following dye: FAM*

#### Download the Template Run File
The Template Run File contains all the parameters preconfigured to run the FloodLAMP QuickFluor(TM) COVID-19 Test. These parameters can be seen in more detail under “Create the Run File ...” headings below.

To download the Template Run File:

1) Go to www.floodlamp.bio/euas  
2) Download the Template Run file(s) for the instrument type and assay to be run.

#### Table 7: Fluorescence LAMP Instrument Template Run File
| Instrument | Setup Template Filename |
| ----- | ----- |
| ABI QuantStudio(TM) 7 Pro | FloodLAMP\_QS7Pro\_Fluor\_template\_run.edt |
| Bio-Rad CFX96 Touch(TM) | FloodLAMP\_BRCFX\_Fluor\_protocol.prcl |
| Bio-Rad CFX96 Touch(TM) | FloodLAMP\_BRCFX\_Fluor\_template\_run.pltd |
||

*Note: Template Run Files only need to be downloaded once upon first use.*

#### Alternatively, Create the Template Run File on QuantStudio(TM) 7 Pro
1) Open the Design and Analysis Software  
2) Select the “SET UP PLATE” option  
3) From the sidebar on the screen, select the following properties to filter:  
   1. Instrument – choose the appropriate instrument  
   2. Block – choose the appropriate block  
   3. RunMode – Standard  
   4. Analysis options are left blank  
4. From the plate sections present on the screen, select the correct System Template and the system will automatically navigate to the "Run Method" tab  
   1. "Presence/Absence" for QuantStudio(TM) 7 Pro  
5. Change run template parameters as shown below:

   Run Parameters

- **Run Method:**  
  - 25 µL Rxn Vol.  
  - 95°C Heated Cover Temp  
  - Ramp Rate: 1.6°C/s

#### Table 8: Fluorimetric LAMP Run Parameters
| Stage | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 65°C | 10 sec | 1 |
| 2 | 65°C | 10 sec | 1 |
| 3 | 65°C | 30 sec | 25 |
| 3 | 65°C \* | 30 sec | 25 |
||

*\* This step should be the optical read step*

- **Plate Setup**  
  - Target: FAM (Sars)  
  - Quencher: None  
  - Passive Reference: None

6. Once done editing the template, go to “Actions” in the top right corner, hit “Save As”  
   1. On Connect: Save to template folder  
   2. Offline: Save to preferred location

#### Alternatively, Create the Template Run File on Bio-Rad CFX96 Touch™
1. Launch the CFX96 Touch software package.  
2. In the Startup Wizard pop-up window select the instrument “CFX96” from the drop down menu.  
3. Under “Select Run Type” press the “User-defined” button.  
4. Create a new thermocycler protocol by selecting “Create New” from the Run Setup window.  
5. Under Tools in the top left toolbar select “Run Time Calculator” and check “96 Wells-All Channels”.  
6. Make the following changes to the cycling conditions in the Protocol Editor:   
a. Change the Sample Volume to 25 μL   
b. Change the Lid Setting to 95°C  
c. Change cycles to be as shown below:

#### Table 9: Thermal cycling conditions and plate read steps (BioRad CFX96)
| Stage | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 65 C | 30 sec | 25 |
| 1 | 65\* C | 30 sec | 25 |
||

*\* This step should be the optical read step*

7. Click “OK” to save the protocol as type Protocol File (\*.prcl) and return to the Protocol tab in Run Setup

### Create the Plate Layout Map
#### QuantStudio(TM) 7 Pro Option 1: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run.

1. Open template in Design and Analysis app and go to the “Plate Setup” tab  
2. On the right side of the screen ensure the “Samples” tab is highlighted and press the addition icon to add the number of samples being tested.   
3. Click on the “Sample 1” box to rename the sample  
   1. Repeat this step for all subsequent samples being entered  
4. Click the well located in the plate map then check the box next to the sample name from the right side bar to associate the name to the well  
   1. There is also the option to highlight the well location in the plate map and click on the “Enter sample” box. Enter the sample ID and press tab to continue to the next well in the plate map. This will automatically load the sample name into the sidebar.  
5. Once the sample names have been entered, the wells may be highlighted by left clicking the mouse over the starting well and dragging the mouse across all wells associated in run. The targets are then chosen by clicking the check boxes next to each target in the sidebar  
   1. FAM should be chosen and named “Sars”  
6. Once done setting up the template, go to “Actions” in the top right corner and hit “Save As,” a pop-up window will appear directing the user to title the file according to information pertaining to the sample run  
   1. Connect: save to the desired folder (only applicable for 7 Pro)  
   2. Offline: save to a USB that is inserted into the computer  
7. Use your plate layout to load your samples and controls after preparing the amplification reaction mix.

#### QuantStudio(TM) 7 Pro Option 2: Lookup Based on Well Position
For this option, a single generic sample name is applied to all wells, and subsequently, outside of the instrument software, the results are linked to the actual sample name via a lookup table to the well position. 

1. Open template in Design and Analysis app and go to the “Plate Setup” tab  
2. Highlight the entire plate and add 1 sample to all wells, with the same sample name in every well.  
3. Highlight entire plate and add FAM to all wells  
4. Go to “Actions” in the top right corner and hit “Save As” and name the template as desired.  
   1. Connect: save to desired location   
   2. Offline: save to a USB that is inserted into the computer

This process only needs to be done once – all subsequent runs can use the same Template Run File. 

#### Bio-Rad CFX96 Touch(TM):
1. Launch the CFX96 Touch software package and open the correct protocol template  
2. Review the details of the protocol. If correct, click “Next” to proceed to the Plate tab  
3. On the Plate tab, click “Create New” and the Plate Editor appears.   
4. Use the Plate Editor to create a new plate.   
5. To ensure the correct plate size is selected, go to “Settings \> Plate Size” and check that 96-well or 384-well is selected from the drop-down menu.   
   1. The plate size selected must correspond to the block size of the instrument being used.   
6. To set the plate type, select” Settings \> Plate Type” and select “BR Clear” or “BR White” from the drop-down menu.   
   1. The plate type selected should match the plate type used in the run.   
7. To set the scan mode, select the “All Channels” scan mode from the Scan Mode drop-down list in the Plate Editor toolbar.  
8. Select the “Select Fluorophores” button on the upper right of the Plate Editor window   
   1. De-select all default fluorophores and select “FAM”and click OK  
9. In the Plate Editor window highlight the whole plate and click the checkbox in front of FAM  
10. Select the “Experiment Settings” button in order to define the Targets   
    1. In the lower left of the Experiment Settings window in the New box type in “N1” and select “Add”   
    2. Select “OK”   
11. In the Plate Editor window next to FAM in the drop-down menu under Target Name select “Sars”  
12. Click OK to save changes and close the “Select Fluorophores” dialog box. 

#### Bio-Rad CFX96 Touch(TM) Option 1: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run.

1. Load the appropriate sample type to each well by selecting the well and selecting the appropriate Sample Type (Unknown, NTC, or Positive Control) from the drop-down menu.  
2. Multiple wells can be selected at once to load the sample type  
   1. Note: the EC can be listed as an Unknown sample.   
3. In the “Target Names” section confirm that the necessary fluorophores are assigned to each well.   
4. Name each well as desired by typing in the sample name and pressing “Enter” in the Sample Names dropdown list in the right pane.   
5. Click OK to save the Plate File (\*.pltd)and return to the Plate tab in Run Setup. When prompted, specify a name for the plate and a save location

#### Bio-Rad CFX96 Touch(TM) Option 2: Lookup Based on Well Position
For this option, a single generic sample name is applied to all wells, and subsequently, outside of the instrument software, the results are linked to the actual sample name via a lookup table to the well position. 

1. Name the file as desired and save as type “Plate File (\*.pltd)”  
2. Select “Save”, click “OK” in the Plate Editor window and exit the software

For this method of creating a Plate Layout Map, this process only needs to be repeated once – all subsequent runs can use the same template. 

### Fluorimetric LAMP Amplification Reaction Preparation
1) Place a 96-well PCR plate or PCR strip tubes onto a cold block or ice.  
2) Thaw frozen reagents until ice crystals are not present.   
3) Pulse vortex thawed reagents for 3 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
4) Store on ice, in the refrigerator, or on a cold block at 4°C until ready to use.  
5) Prepare the Fluorimetric LAMP Amplification Reaction Mix by combining the components listed below in Table 10. 

      NOTE: Component volumes should be scaled proportionally for the number of reactions. 

6) Vortex the Fluorimetric LAMP Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
7) Add 23 µL of the Fluorimetric LAMP Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

#### Table 10: Fluorimetric LAMP Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| ----- | :---: | :---: |
| 10X LAMP Primer Mix | 2.5 µL | 250 µL |
| Nuclease-Free Water | 7.5 µL | 750 µL |
| Fluorimetric LAMP MM | 12.5 µL | 1250 µL |
| Fluorescent Dye | .5 µL | 50 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **2300 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **25 µL** | - |
|||

### Sample Addition
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Add 2 µL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
2) Mix by pipetting.  
3) If using PCR plate optical seal (optionally using heat sealer). If using PCR strip tubes, cap strips.  
4) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
5) Continue to section “Run the Assay”

### Run the Assay
Refer to Specific Instrument User Manuals for full system usage and maintenance details.

#### On QuantStudio(TM) 7 Pro
1. Log into user on instrument.  
2. USB: Plug in USB with saved template on it.  
3. From the options on the instrument’s screen press “Load plate file”.  
   1. The QuantStudio(TM) 7 Pro is a touchscreen device.  
4. From the “Run Queue” screen,   
   1. USB: press “USB drive” on the left side.  
   2. Connect: press Cloud icon on the left side.  
5. This will bring up any plate files saved.  
6. Press the plate file associated with the run to be performed.  
7. A new window will appear requesting location of results once the run is complete.  
   1. Connect: Press the “Cloud Connect” icon, press again to verify location the files will be uploaded to and then press “Done”.  
   2. USB: Press the “USB drive Connected” if the icon is not already highlighted and press “Done”.   
8. Press the double-arrow icon located at the top right sided corner of the screen on the instrument.   
   1. The instrument drawer will open from the front.   
9. Place the plate/strips into the plate holder ensuring proper orientation of the plate.   
   1. A1 well should be in the position of the top left corner.  
   2. The plate/strips will appear slightly suspended above the block due to two silicone strips above and below this plate. This is to be expected and the instrument lid will press the plate down once the drawer has closed.   
10. Press “Start Run” on the screen of the instrument.   
    1. A pop-up window will appear asking the user to confirm the plate has been loaded.   
    2. If the plate has been loaded, press “StartRun” again or press “Open Drawer” to place the plate into the block and then press “Start Run”.

#### On Bio-Rad CFX96 Touch(TM)
1) Open the correct .pcrl file and review the protocol details. If correct click “Next” to proceed to the Plate tab.  
2) When prompted, open the correct .pltd file and review the plate details in the Run Information section.  
3) Select the checkbox for the appropriate block (CFX96 or CFX384) on which to perform the run.  
4) To insert the plate or 8-tube strips into the block, click Open Lid.  
5) Insert the plate or 8-tube strips into the block. Ensure the plate or 8-tube strips are properly oriented.  
6) Click Close Lid.  
7) Click Start Run at the bottom right of the screen.  
8) When prompted, save the data file (.pcrd) to the desired location.

### Analyzing Data
#### Exporting Data from QuantStudio(TM) 7 Pro
##### Using USB
1) Confirm Quant says “File Transferred \- USB”  
2) Take USB from Quant and plug it into computer  
3) Export data off of USB onto computer

##### Using Cloud Connect with QuantStudio(TM) 7 Pro
1) Go to [Cloud Connect](https://apps.thermofisher.com/apps/spa/#/dashboard%20%20) and log in.  
2) Go to files and find the data that was just uploaded by the Quant, it will be in the folder chosen previously chosen while running the Quant  
3) Download .xlsx file  

#### Exporting Data from Bio-Rad CFX96 Touch(TM)
1) After the run has completed, open the data file (.pcrd) by going to Select File \> Open \> Data File in the Home window and locating the desired data file. Adjust the following settings as described below.   
2) Select Settings \> Cq Determination mode and select Single Threshold.   
3) Select Settings \> Baseline Setting and select Baseline Subtracted.   
4) Select Settings \> Analysis Mode and select analysis by fluorophore.   
5) Select Settings \> Cycles to Analyze and the Cycles to Analyze dialog box appears. Confirm that all cycles are being analyzed and click “OK”.   
6) Cq values of each well are displayed in the Quantification Data tab.   
7) Export .xlsx files and select Export \> Export all Data Sheets to Excel (Cq values are available in "Quantification Plate View Results").  

#### Compiling Results Option 1: Lookup Based on Well Position
For this option, outside of the instrument software the results are linked to the actual sample name via a lookup table to the well position. An example spreadsheet to perform this lookup and results compilation is available with instructions at [www.floodlamp.bio/euas](http://www.floodlamp.bio/ifus).

#### Compiling Results Option 2: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run. Open the results file and continue to “Analyzing Data” section to score results.

### Results Interpretation
#### Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to Table 11 below.

1) The “No Template” (Negative) Control (NTC) should yield a negative “not detected” result for the SARS target  
     
2) The Positive Template Control should yield a positive “detected” result for the SARS target  
     
3) The Internal Process Control is required to report a negative SARS-CoV-2 result. 

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP(TM) product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### Patient Specimen Results Interpretation
NOTE: Patient specimen results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Use Table 11 below to assign a result to each sample. 

#### Table 11: Interpretation of Assay Results
| ABI QuantStudio(TM) 7 Pro Bio-Rad CFX96 Touch(TM) |  |  |
| :---: | :---: | :---: |
| **Result** | **Ct Value: N1** |  |
| Positive | ≤25.0 |  |
| Negative | Undetermined |  |
|||

## Performance Evaluation
### Analytical Sensitivity: Limit of Detection (LoD)
The Limit of Detection (LoD) for the FloodLAMP QuickFluor(TM) COVID-19 Test was established using gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 50,000, 25,000 and 12,500 copies/mL were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 12. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 50,000 copies/mL.

#### Table 12: LoD Confirmatory Data Results
| Instrument | LoD | Positive Replicates | Mean Ct Value (SD) |
| ----- | ----- | :---: | :---: |
| ABI QuantStudio(TM) 7 Pro | 50,000 copies/mL | 95% (20/21) | 11.9 (1.5) |
| ABI QuantStudio(TM) 7 Pro | 25,000 copies/mL | 76% (16/21) | 13.8 (2.3) |
||

### Analytical Sensitivity: Inclusivity (*in silico*)
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 13 summarizes the results of this *in silico* inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.	

#### Table 13: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total \# of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs ([primer-monitor.neb.com](http://primer-monitor.neb.com)), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 14, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 \-t 16 \-x asm5 \-a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having \>= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations are not expected to reduce performance of the FloodLAMP QuickFluor(TM) COVID-19 Test by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 14: Variant Analysis of LAMP Primers
![][image1]  
![][image2]

### Analytical Specificity: Cross-Reactivity (*in silico*)
*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the FloodLAMP QuickFluor(TM) COVID-19 Test against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 15A, 15B, and 15C. 

The % identity range (\# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with \>= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the *in silico* cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 15A: *In Silico* Cross-Reactivity Analysis for AS1e Primers

![][image3]

#### Table 15B: *In Silico* Cross-Reactivity Analysis for N2 Primers

![][image4]

#### Table 15C: *In Silico* Cross-Reactivity Analysis for E1 Primers

![][image5]

### Analytical Specificity: Cross-Reactivity (*wet testing*)
Wet testing was performed to demonstrate that the FloodLAMP QuickFluor(TM) COVID-19 Test does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen.  SARS-CoV, RSV, Flu, Human Metapneumovirus. and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 16 and Supporting Data. 5 µL of each stock of cross-reactivity organism was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived positive had 38 µL of 1e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 38,000 copies/mL in the sample input into the amplification reaction.

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 16.

#### Table 16: Wet Testing Cross-Reactivity Results
| Organism | Description | BEI Number | Detected Replicates |
| ----- | ----- | :---: | :---: |
| SARS-CoV | UV-inactivated virus | NR-3882 | 0/3 |
| Human Metapneumovirus | Genomic RNA | NR-49122 | 0/3 |
| RSV | Genomic RNA | NR-43976 | 0/3 |
| Influenza B | Genomic RNA | NR-45848 | 0/3 |
| Streptococcus salivarius | Bacterial cell culture | HM-121 | 0/3 |
||

### Analytical Specificity: Interfering Substances
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP QuickFluor(TM) COVID-19 Test. 10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP QuickFluor(TM) COVID-19 Test. 10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 17 and Supporting Data.

#### Table 17: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

## Clinical Evaluation
The clinical evaluation of the FloodLAMP QuickFluor(TM) COVID-19 Test utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The FloodLAMP QuickFluor(TM) COVID-19 Test showed a positive agreement of 80.0% and a negative agreement of 100%. The six false negative results were specimen with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is shown below in Table 18.

#### Table 18: Clinical Evaluation Results
| FloodLAMP QuickFluor(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 34 | 0 | 34 |
| Negative | 6 | 40 | 46 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 85.0% (34/40) 95% CI: 70.2% to 94.3% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## Support

FloodLAMP Biotechnologies, PBC support center   
eua.support@floodlamp.bio  
650-394-5233

QuantStudio(TM)  is a trademark of Thermo Fisher Scientific (NYSE: TMO)

Bio-Rad(TM) and Bio-Rad CFX96 Touch(TM)  are trademarks of Bio-Rad Laboratories, Inc. (NYSE: BIO)


# 8,979  2021-05-18_EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.1.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-05-18_EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.1.md
file_date: 2021-05-18
title: EUA Submission - FloodLAMP EasyPCR COVID-19 Test v1.1
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1doTmCyzTAa4RD88IQ2j8gitAukhfw2nv
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-05-18_EUA%20Submission%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.1.docx
pdf_gdrive_url: https://drive.google.com/file/d/1ANjA5E_pbFelB8mOy3lQyXRcrX3-oix0
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-05-18_EUA%20Submission%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.1.pdf
conversion_input_file_type: docx
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 8979
words: 5489
notes: 
summary_short: The EUA Submission for the FloodLAMP EasyPCR COVID-19 Test v1.1 describes an extraction-free, duplex RT-qPCR assay using CDC N1 and RNaseP targets after chemical plus heat inactivation, designed for CLIA high-complexity labs running routine screening programs (e.g., schools and workplaces) with at least weekly testing. It details intended use, validated instruments, workflow, controls, and component sourcing for an open-protocol deployment. It summarizes performance claims including a 3,100 copies/mL LoD and 97.5% positive agreement with 100% negative agreement in an 80-specimen clinical evaluation.


CONTENT

***INTERNAL TITLE:*** EUA Submission - FloodLAMP EasyPCR(TM) COVID-19 Test
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for distribution and/or use of the **FloodLAMP EasyPCR(TM) COVID-19 Test** for the *in vitro* qualitative detection of RNA from the SARS-CoV-2 in in upper respiratory specimens including oropharyngeal and nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week, such as those implemented by schools, workplaces and community groups**. Additional testing and confirmation procedures should be performed in consultation with public health and/or other authorities to whom reporting is required. Test results should be reported in accordance with local, state, and federal regulations.

## B. MEASURAND
Specific nucleic acid sequences from the genome of the SARS-CoV-2, targeted by the previously certified **2019-nCoV\_N1 primers and probe set as part of the CDC qPCR assay**. Primer names and sequences are listed in Table 1.

#### Table 1: Primers and probes
| Target | Primer/Probe | Sequence |
| :---- | :---- | :---- |
| CDC-N1 |  2019-nCoV\_N1-F | GACCCCAAAATCAGCGAAAT |
| CDC-N1 |  2019-nCoV\_N1-R | TCTGGTTACTGCCAGTTGAATCTG |
| CDC-N1 |  2019-nCoV\_N1-P | **FAM**\-ACCCCGCATTACGTTTGGTGGACC-**IBFQ** |
| Human RNAseP |  RP-F | AGATTTGGACCTGCGAGCG |
| Human RNAseP |  RP-R | GAGCGGCTGTCTCCACAAGT |
| Human RNAseP |  RP-P | **Cy5**\-TTCTGACCTGAAGGCTCTGCGCG-**IBRQ** |
||

## C. APPLICANT
FloodLAMP Biotechnologies, a DE Public Benefit Corporation

| Mailing Address: 4860 Alpine Rd. Portola Valley, CA 94028 | Laboratory Address: 930 Brittan Ave San Carlos, CA 94070	 | Randall J. True, CSO Phone: (415) 269-2974 Email: randy@floodlamp.bio |
| :---- | :---- | :---- |

## D. PROPRIETARY AND ESTABLISHED NAMES
Proprietary Name \- **FloodLAMP EasyPCR(TM) COVID-19 Test**  
Established Name \- **FloodLAMP EasyPCR(TM) COVID-19 Test**

## E. REGULATORY INFORMATION
***Approval/Clearance Status:***
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is not cleared, CLIA waived, approved, or subject to an approved investigational device exemption.

***Product Code:*** 

QJR

## F. PROPOSED INTENDED USE
### 1) Intended Use:
**FloodLAMP EasyPCR(TM) COVID-19 Test** is a real-time reverse transcriptase polymerase chain reaction (RT-qPCR) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week**. Testing is limited to **laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories.** 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis  
for patient management decisions. Negative results must be combined with clinical observations,  
patient history, and epidemiological information.

The **FloodLAMP EasyPCR(TM) COVID-19 Test** is intended for use by **qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of in vitro diagnostic procedures**. The **FloodLAMP EasyPCR(TM) COVID-19 Test** is only for use under the Food and Drug Administration’s Emergency Use Authorization.

### 2) Special Conditions for Use Statements:
For Emergency Use Authorization (EUA) only   
For prescription use only  
For in vitro diagnostic use only

### 3) Special Instrument Requirements:
The **FloodLAMP EasyPCR(TM) COVID-19 Test** test is to be used with the RT-PCR instruments listed in Table 2.

#### Table 2. RT-PCR Instruments validated for test
| Manufacturer | Instrument |
| :---: | :---: |
| Thermo Fisher Scientific | Applied Biosystems QuantStudio(TM) 6 Flex |
| Thermo Fisher Scientific | Applied Biosystems QuantStudio(TM) 7 Pro |
| Bio-Rad | CFX96 Touch(TM) Real-Time PCR Detection System |
||

Designated laboratories will receive an FDA accepted instrument qualification protocol included as part of the **FloodLAMP EasyPCR(TM) Covid-19 Test** IFU and will be directed to execute the protocol prior to testing clinical samples. Designated laboratories must follow the authorized IFU, which includes the instrument qualification protocol, as per the letter of authorization.

## G. DEVICE DESCRIPTION AND TEST PRINCIPLE
### 1) Product Overview/Test Principle:
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is a RNA extraction-free, duplexed RT-qPCR assay which indicates whether SARS-CoV-2 RNA is present. It can widely and rapidly scale because 1) it does not require nucleic acid extraction equipment, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a very straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the **FloodLAMP QuickColor(TM) COVID-19 Test**. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Further, the **FloodLAMP QuickColor(TM) COVID-19 Test** is isothermal, does not require any instrumentation and has a visual readout. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

In the **FloodLAMP EasyPCR(TM) COVID-19 Test,** samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step, and the resulting inactivated sample is directly used as input in the duplexed RT-qPCR test. The test does not use new primers and probes for RT-qPCR testing, but rather uses previously validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC, which are readily available from multiple commercial suppliers. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, reducing the number of tests to 1 assay with 2 sets.

### 2) Description of Test Steps: 
Specimens including **nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs** are collected in **sterile collection tubes.** Swabs are transported and stored dry prior to processing. At the laboratory, an inactivation solution at 1X containing TCEP (2.5 mM), EDTA (1 mM), and NaOH (11 mM) in 0.9% saline (154 mM) is added to the container with the swab, at the volume of 1 ml. Alternatively, for swabs that are collected or eluted in a saline solution or equivalent, the inactivation solution at 100X concentration should be added at 1/100th the sample solution volume. 

The container with the specimen and inactivation solution is mixed by vortexing for 30 seconds. Subsequently, the container is heated in a 95°C water bath or dry heat block for 8 minutes. The now inactivated specimen container is allowed to cool at room temperature for 10 minutes and then stored on ice or at 4°C until amplification.

An amplification reaction mix (18 µl) is prepared per manufacturer's specifications, containing the New England Biolabs LunaⓇ PCR Master Mix (New England Biolabs E3006, 10 µl), New England Biolabs LunaⓇ RT (New England Biolabs E3006, 1 µl), a primer solution (4 µl of 5X PCR primer stock w/ N1-F & N1-R at 2 µM, N1-P & RP-P at 1 µM and RP-F & RP-R at 0.75 µM), and nuclease-free water (3 µl).

2µl of the inactivated sample is added to 18µl of the amplification reaction mix. The reaction is then run with the following thermocycler conditions in Table 3:

#### Table 3: Thermal cycling conditions and plate read steps 
| Step | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 52°C | 10 min | 1 |
| 2 | 95°C | 2 min | 1 |
| 3 | 95°C | 10 sec | 44 |
| 3 | 55°C\* | 30 sec | 44 |
||

*\* This step should be the optical read step*

### 3) Control Materials to be Used with FloodLAMP EasyPCR(TM) COVID-19 Test:
**One Positive Template Control and one Negative (No Template) Control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes. An **Internal Process Control** is included in every PCR reaction. 

1) A **“No Template” (Negative) Control (NTC) is needed to assure the absence of cross-contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of nuclease-free water.**  
     
2) A **Positive Template Control is needed to assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 4 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.    
     
3) **An Internal Process Control is needed to assure sufficient specimen quantity and quality**. It consists of a primer/probe set targeting the human RNaseP gene that is included in a single PCR amplification reaction. The RNAseP Internal Process Control uses a fluorescent reporter in a separate channel from the SARS-CoV-2 channel (i.e. in duplex).

#### Table 4. Components for Positive Template Control 
| Material | Supplier | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µL |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µL |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895 µL |
||

## H. INTERPRETATION OF RESULTS
### 1) FloodLAMP EasyPCR(TM) COVID-19 Test Controls 
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to Table 5 below.

1) The “No Template” (Negative) Control (NTC) should yield a negative “not detected” result for both the N1 and RNaseP targets.  
     
2) The Positive Template Control should yield a positive “detected” result for the N1 target and a negative “not detected” for the RNaseP control.  
     
3) The Internal Process Control should yield a positive "detected" result for RNaseP. Detection of RNaseP is required to report a negative SARS-CoV-2 result. 

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP(TM) product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### 2) Examination and Interpretation of Patient Specimen Results:
Assessment of clinical patient specimen test results should be performed after the positive, negative, and internal controls have been examined and determined to be valid and acceptable. If the controls are not valid, the patient results cannot be interpreted. Patient specimen results will be interpreted according to Table 5 below.

#### Table 5: Interpretation of Patient Specimen Results
| ABI QuantStudio(TM) 7 Pro |  |  |
| :---: | :---: | :---: |
| **Result** | **Ct Value: N1** | **Ct Value: RP** |
| Positive | \<38.0 | Any Value |
| Negative | ≥38.0 | \<35.0 |
| Invalid | ≥38.0 | ≥35.0 |
| **Bio-Rad CFX96 Touch(TM) ABI QuantStudio(TM) 6 Flex** |  |  |
| **Result** | **Ct Value: N1** | **Ct Value: RP** |
| Positive | \<40.0 | Any Value |
| Negative | ≥40.0 | \<35.0 |
| \*Invalid | ≥40.0 | ≥35.0 |
||

\*Invalid test results will be repeated by rerunning the primary sample if available, otherwise by rerunning the inactivated sample. Results from retested samples will follow the same interpretation as listed in Table 5.

If the final interpretation of the test result is invalid, then "Invalid/Inconclusive" should be reported and retesting of the individual is recommended. 

## I. PRODUCT MANUFACTURING
### 1) Overview of Manufacturing and Distribution:
The **FloodLAMP EasyPCR(TM) COVID-19 Test**  utilizes standard chemicals available from multiple vendors, with the exception of the New England Biolabs LunaⓇ Universal Probe One-Step RT-qPCR Kit. 

The **FloodLAMP EasyPCR(TM) COVID-19 Test** utilizes the same primer and probes as the EUA authorized SalivaDirect(TM) test, which derive from the CDC primer set. These are available in very large quantities with immediate distribution from multiple vendors including Eurofins Genomics, Integrated DNA Technologies, and LGC Biosearch.

New England Biolabs has expressed strong support for the **FloodLAMP EasyPCR(TM) COVID-19 Test** and FloodLAMP's other open source protocol EUA submissions that incorporate their products. New England Biolabs has very large quantities of the LunaⓇ Universal Probe One-Step RT-qPCR Kit prepared and ready for immediate distribution, typically with 24 hour shipping. Their manufacturing capacity is among the largest in the United States and can surge to meet increased demand.

**\*Under the Emergency Use Authorization (EUA) any of the 21 CFR Part 820 Quality System Regulation (QSR) requirements can be waived for the duration of the EUA but FDA recommends that developers follow comparable practices as much as possible if such requirements are waived. Among other things, FDA may consider previous compliance history when determining whether or not to waive certain QSR requirements for a specific product. Please note adverse events, as per 21 CFR Part 803, have to be reported for authorized devices (see Section P).** 

### 2) Components Included with the Test
None. Designated CLIA labs may order components directly from vendors.

### 3) Components Required But Not Included with Test:
The **FloodLAMP EasyPCR(TM) COVID-19 Test** is to be used with the following reagents or equivalents listed in Table 6.

#### Table 6: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | ----- | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-freeWater |  | Ultrapure Water, DNAse RNAse free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| PCR MasterMix \* | - | 2X PCR Master Mix (in LunaⓇ Universal Probe One-Step RT-qPCR Kit) | New England Biolabs | E3006 |
| PCR RT \* | - | Reverse Transcriptase (in LunaⓇ Universal Probe One-Step RT-qPCR Kit) | New England Biolabs | E3006 |
||

\* Item may not be substituted for equivalents. Only the specified vendor and catalog number may be utilized.

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

The 100X Inactivation Solution is prepared by mixing the components in Table 7. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved.

#### Table 7: 100X Inactivation Solution
| Component | Source Concentration | Volume | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 8. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 8: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :---: |
| 0.9% Saline (154 mM NaCl) | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

The **FloodLAMP EasyPCR(TM) COVID-19 Test** uses the validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, detecting the 2 targets in a single well. This configuration is described in the SalivaDirect(TM) EUA Authorized test ([www.fda.gov/media/141192/download](http://www.fda.gov/media/141192/download)).

The complete set of 6 primers and probes may be purchased from the vendor Eurofins Genomics using the catalog number 12YS-010YST. This product contains primers and probes suspended at 100µM and is enough for 12,500 reactions. The contents can be mixed along with nuclease-free water to create the primer stocks used in the **FloodLAMP EasyPCR(TM) COVID-19 Test**. See Table 9 below for details. A large volume of primer-probe stock can be prepared in advance and stored at 4oC for one month or \-20oC for up to 1 year. Vendors for the Primer and Probe sets are below in Table 10.

#### Table 9: 5X PCR Primer Stock Preparation from Eurofins Genomics Product
| Component (final concentration) | Volume (1 reaction) | Volume (3,125 reactions) |
| ----- | :---: | :---: |
| 2019-nCov\_N1-F (10 µM) | 0.4 µl | 1,250 µl |
| 2019-nCov\_N1-R (10 µM) | 0.4 µl | 1,250 µl |
| 2019-nCov\_N1-P (5 µM) | 0.2 µl | 625 µl |
| RP-F (3.75 µM) | 0.15 µl | 469 µl |
| RP-R (3.75 µM) | 0.15 µl | 469 µl |
| RP-P (5 µM) | 0.2 µl | 625 µl |
| Nuclease-free water | 2.5 µl | 7,813 µl |
| **TOTAL VOLUME** | **4 µl** | **12,500 µl** |
||

#### Table 10: Primer and Probe Set Products
| Vendor | Item | Catalog number | Quantity | #Reactions |
|---------|------|----------------|-----------|------------|
| Eurofins Genomics | SalivaDirect™ complete set of 6 primers and probes | 12YS-010YST | 50-100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006821 | 50 nmol | 6,2500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006830 | 100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006822 | 50 nmol | 6,250 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006831 | 100 nmol | 12,500 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006831 | 25 nmol | 6,250 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006832 | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006827 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006836 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006828 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006837 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNase P Probe | Custom order (Cy5) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | Custom order (Cy5) | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNase P Probe | 10007061 (ATTO647) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | 10007062 (ATTO647) | 50 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-250 | 250 nmol | 62,500 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-250 | 50 nmol | 12,500 |
||

The final amplification reaction components are listed in Table 11. PCR plates or strip tubes used for the amplification reactions should be maintained on ice or a cold block. 

#### Table 11: PCR Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| :---- | :---: | :---: |
| 5X PCR Primer Stock | 4 µL | 400 µL |
| New England Biolabs PCR MM | 10 µL | 1000 µL |
| New England Biolabs PCR RT | 1 µL | 100 µL |
| Nuclease-Free Water | 3 µL | 300 µL |
| **SUBTOTAL VOLUME** | **18 µL** | **2250 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **20 µL** | - |
||

### 4) Software Validation
The **FloodLAMP EasyPCR(TM) COVID-19 Test** has been validated on the RT-PCR instruments listed in Table 2 using the baseline threshold settings unless otherwise noted in the Instructions for Use. The test does not require any additional software.

### 5) Testing Capabilities 
The **FloodLAMP EasyPCR(TM) COVID-19 Test** has been optimized for a robust, streamlined workflow and for rapid turnaround time on results. The total time to perform the test is dependent upon the following factors: number of lab technicians, batch size of samples, and in advance preparation of reaction mixes. The minimum turnaround time is approximately 1 hour and 45 minutes, of which approximately 1 hour and 20 minutes is the RT-PCR instrument run time. Automation can greatly increase overall throughput.

### 6) Reagent Stability: 
A stability test plan for the components of the **FloodLAMP EasyPCR(TM) COVID-19 Test** will be developed during an interactive review. Briefly, the proposed study includes assessing all prepared solutions including: 100X Inactivation Solution, 1X Inactivation Saline Solution, 5X PCR Primer Stock, and the full PCR Amplification Mix. Prepared solutions will be assessed both for long term storage stability (typically 1-3 months at \-20oC) and short term storage stability prior to usage (typically hours to several days at room temperature, 4oC or \-20oC). 

The proposed study uses a contrived positive sample consisting of gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative specimens at approximately 50,000 copies/mL (4X LoD). The contrived positive stability study samples will be prepared, aliquoted and stored at \-80oC to permit repeated testing of the various solutions at the appropriate step of the test protocol.

For test components supplied by vendors, such as New England Biolab’s LunaⓇ Universal Probe One-Step RT-qPCR Kit, the manufacturer's recommended storage conditions and duration will be followed.

### 7) Sample Stability:
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19: https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

Samples can be stored at room temperature for 56 hours after collection prior to inactivation. For longer term storage, samples can be stored at ≤-70oC.

## J. PERFORMANCE EVALUATION
### 1) Limit of Detection (LoD) - Analytical Sensitivity:
The Limit of Detection (LoD) for the **FloodLAMP EasyPCR(TM) COVID-19 Test** was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 6,300, 3,100 and 1,600 copies/mLwere selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 12. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 3,100 copies/mL. 

#### Table 12: Confirmatory LoD Data Results
| Instrument | LoD | Positive Replicates | Mean Ct Value (SD) |
| ----- | :---: | :---: | :---: |
| ABI QuantStudio(TM) 7 Pro | 3,100 copies/mL | 95% (20/21) | 36.5 (.8) |
| ABI QuantStudio(TM) 6 Flex | 3,100 copies/mL | 100% (21/21) | 36.9 (1.1) |
| Bio-Rad CFX96 Touch(TM) | 3,100 copies/mL | 95% (20/21) | 37.2 (.9) |
||

### 2) Inclusivity (analytical sensitivity): 
**FloodLAMP EasyPCR(TM) COVID-19 Test** includes a modified RT-qPCR assay by duplexing the previously authorized CDC N1 and human RNase P primer-probe sets. Inclusivity was tested in the original US CDC EUA with all publicly available SARS-CoV-2 genomes as of 1 February 2020. The initial analysis showed 100% homology between the N1 primer-probe set and available genomes, except for one low frequency mismatch with the N1 forward primer. However, this was not expected to affect performance of the primer-probe set due to annealing temperatures of 55°C which tolerate 1-2 mismatches. Indeed, performance of the N1 primer-probe set was shown to be high in the previous comparison of primer-probes sets ([https://www.nature.com/articles/s41564-020-0761-6](https://www.nature.com/articles/s41564-020-0761-6)). GISAID continuously evaluates mismatches between newly available SARS-CoV-2 genomes and primer-probe sets and confirms a low frequency of nucleotide mismatches (\<5%) with the N1 primer-probe set.

### 3) Cross-reactivity (Analytical Specificity):
The primer and probe sets used in the duplex assay were developed by the US CDC and have been EUA certified. The CDC reported no cross-reactivity with other human coronaviruses (229E, OC43, NL63, and HKU1), MERS-coronavirus, SARS-coronavirus, and 14 additional human respiratory viruses (see [https://www.fda.gov/media/134922/download](https://www.fda.gov/media/134922/download)). 

#### Endogenous Interference Substances Studies:
Exogenous and endogenous substances were tested for potential interference with the **FloodLAMP EasyPCR(TM) COVID-19 Test*.*** 10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 13 and Supporting Data.

#### Table 13: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

### 4) Clinical Evaluation 
The clinical evaluation of the **FloodLAMP EasyPCR(TM) COVID-19 Test** utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The **FloodLAMP EasyPCR(TM) COVID-19 Tes**t showed a positive agreement of 97.5% and a negative agreement of 100%. The single false negative result was a specimen with a high Ct value as previously measured by the comparator test, indicating very low viral load. A summary of the clinical performance is below in Table 14.

Anterior nares swab specimens were collected from patients in phosphate buffered saline by the Stanford COVID-19 clinical testing program. Specimens were initially tested by the Stanford clinical laboratory using the Hologic Panther Fusion and Aptima SARS-CoV-2 Assays, which serves as the high sensitivity comparator test. 

For the **FloodLAMP EasyPCR(TM) COVID-19 Test**, materials and the Instructions For Use were provided to the Stanford clinical laboratory. The materials provided consisted of the validated reagents listed in Table 6, the Eurofins Genomics primers and probes, and an aliquot of the positive control. The Bio-Rad CFX96 instrument was used to perform the RT-PCR. After thawing the frozen specimens, 1 mL of each specimen was transferred to 5mL tubes for the inactivation step. The positive and negative clinical specimens were assigned a new ID in a random order, then transferred to new tubes that were barcoded and labeled with the new ID. Line Item data are provided in the Supporting Data. 

#### Table 14: Clinical Evaluation Results
| FloodLAMP EasyPCR(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 39 | 0 | 39 |
| Negative | 1 | 40 | 41 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 97.5% (39/40) 95% CI: 86.8% to 99.9% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## K. UNMET NEED ADDRESSED BY THE PRODUCT 
This section will be completed by FDA. 

## L. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for the detection of the SARS-CoV-2 have been approved/cleared by FDA.

## M. BENEFITS AND RISKS:
This section will be completed by FDA.

## N. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS:
Fact Sheets for Patients and Healthcare Providers attached.

## O. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT:
Instructions for Use attached.

## P. RECORD KEEPING AND REPORTING INFORMATION TO FDA:
Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.

QuantStudio  is a trademark of Thermo Fisher Scientific (NYSE: TMO)

Bio-Rad and Bio-Rad CFX96 Touch  is a trademark of Bio-Rad Laboratories, Inc. (NYSE: BIO)


# 10,743  2021-05-18_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.1.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-05-18_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.1.md
file_date: 2021-05-18
title: EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.1
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1TXEZpwcgDREAxPxp4jFblwYVHzHsJ7wl
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-05-18_EUA%20Submission%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.1.docx
pdf_gdrive_url: https://drive.google.com/file/d/1ebCzNHQzoqggWxQuDb9GLieoTHfqLKrU
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-05-18_EUA%20Submission%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.1.pdf
conversion_input_file_type: docx
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10743
words: 6571
notes: 
summary_short: The EUA Submission for the FloodLAMP QuickColor™ COVID-19 Test v1.1 describes an extraction-free RT-LAMP, colorimetric assay for qualitative SARS-CoV-2 RNA detection from upper respiratory swab specimens in both symptomatic individuals and routine serial screening programs. It details intended use, primer targets (ORF1ab, N, E), workflow and controls, manufacturing inputs, and analytical/clinical performance data to support an FDA Emergency Use Authorization request.


CONTENT

***INTERNAL TITLE:*** EUA Submission - FloodLAMP QuickColor(TM) COVID-19 Test
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for distribution and/or use of the **FloodLAMP QuickColor(TM) COVID-19 Test** for the *in vitro* qualitative detection of RNA from the SARS-CoV-2 in in upper respiratory specimens including oropharyngeal and nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week, such as those implemented by schools, workplaces and community groups**. Additional testing and confirmation procedures should be performed in consultation with public health and/or other authorities to whom reporting is required. Test results should be reported in accordance with local, state, and federal regulations.

## B. MEASURAND
Specific nucleic acid sequences from the genome of the SARS-CoV-2, targeted by **primers from the ORF1ab, N and E regions** of the virus. Primer names and sequences are listed in Table 1.

#### Table 1: Primer names and sequences
| Primer Name | Sequence (5’-3’) |
| :---- | :---- |
| **ORF1ab gene (AS1e)** |   |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |   |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |   |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

## C. APPLICANT
FloodLAMP Biotechnologies, a DE Public Benefit Corporation

| Mailing Address: 4860 Alpine Rd. Portola Valley, CA 94028 | Laboratory Address: 930 Brittan Ave San Carlos, CA 94070	 | Randall J. True, CSO Phone: (415) 269-2974 Email: randy@floodlamp.bio |
| :---- | :---- | :---- |

## D. PROPRIETARY AND ESTABLISHED NAMES
Proprietary Name \- **FloodLAMP QuickColor(TM) COVID-19 Test**  
Established Name \- **FloodLAMP QuickColor(TM) COVID-19 Test**

## E. REGULATORY INFORMATION
***Approval/Clearance Status:***

The **FloodLAMP QuickColor(TM) COVID-19 Test** is not cleared, CLIA waived, approved, or subject to an approved investigational device exemption.

***Product Code:*** 

QJR 

## F. PROPOSED INTENDED USE
### 1) Intended Use:
**FloodLAMP QuickColor(TM) COVID-19 Test** is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week**. Testing is limited to **laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories.** 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis  
for patient management decisions. Negative results must be combined with clinical observations,  
patient history, and epidemiological information.

The **FloodLAMP QuickColor(TM) COVID-19 Test** is intended for use by **qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures**. The **FloodLAMP QuickColor(TM) COVID-19 Test** is only for use under the Food and Drug Administration’s Emergency Use Authorization.

### 2) Special Conditions for Use Statements:
For Emergency Use Authorization (EUA) only   
For prescription use only  
For *in vitro* diagnostic use only

### 3) Special Instrument Requirements:
The **FloodLAMP QuickColor(TM) COVID-19 Test** does not have special instrument requirements.

## G. DEVICE DESCRIPTION AND TEST PRINCIPLE
### 1) Product Overview/Test Principle:
The **FloodLAMP QuickColor(TM) COVID-19 Test** is a RNA extraction-free reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) molecular assay that indicates the presence of the SARS-CoV-2 viral RNA with a simple visual color change. It can widely and rapidly scale because 1) no special instrumentation of any kind is required, neither nucleic acid extraction equipment nor a RT-PCR instrument, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the **FloodLAMP EasyPCR(TM) COVID-19 Test**. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

The **FloodLAMP QuickColor(TM) COVID-19 Test** uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. It uses Loop Mediated Isothermal Amplification (LAMP), a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. Samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step. The resulting inactivated sample is directly used as input in the LAMP reaction. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. The amplified DNA products lower the pH of the reaction. A phenol red pH indicating dye is included in the amplification reaction mix, thus causing the reaction solution to visibly change from an initial bright pink to a bright yellow when sufficient amplification occurs. Reactions that change color to yellow indicate that SARS-CoV-2 RNA is present.

### 2) Description of Test Steps:
Specimens including **nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs** are collected in **sterile collection tubes.** Swabs are transported and stored dry prior to processing. At the laboratory, an inactivation solution at 1X containing TCEP (2.5 mM), EDTA (1 mM), and NaOH (11 mM) in 0.9% saline (154 mM) is added to the container with the swab, at the volume of 1 mL. Alternatively, for swabs that are collected or eluted in a saline solution or equivalent, the inactivation solution at 100X concentration should be added at 1/100th the sample solution volume. 

The container with the specimen and inactivation solution is mixed by vortexing for 30 seconds. Subsequently, the container is heated for 8 minutes in a 95°C water bath or dry heat block. The now inactivated specimen container is allowed to cool at room temperature for 10 minutes and then stored on ice or at 4°C until amplification.

An amplification reaction mix (23 µl) is prepared per manufacturer's specifications, containing the Colorimetric LAMP master mix (NEB M1800, 12.5 µl) and a primer-guanidine solution (10.5 µl) comprising 10X primers mix (2.5 µl of 10X w FIP/BIP at 16 µM, F3/B3 at 2 µM, and LF/BF at 4 µM), guanidine hydrochloride (2.5 µl of 400 mM), and nuclease-free water (5.5 µl). The primer-guanidine solution may be prepared ahead of time and stored at \-20°C for up to 1 month.

2 µl of the inactivated sample is added to 23µl of the amplification reaction mix. The reaction is incubated at 65°C for 25 minutes in a thermal cycler, dry heat block, or water bath. After removal from the heat, the reaction solution is allowed to cool at room temperature for 1 minute and then the test result is determined visually based on the color of the reaction solution.

### 3) Control Materials to be Used with test:
**One positive and one negative control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes on each heater:

1) A “no template” (negative) control (NTC) is needed to **assure the absence of cross contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of 100X Inactivation Solution diluted to 1X in 0.9% saline.** This NTC is the same solution added to dry swabs (see Section I below for the components)**.**  
     
2) A positive template control is needed to **assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 2 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.

#### Table 2: Components for Positive Template Control 
| Material | Supplier | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µL |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µL |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895 µL |
||

## H. INTERPRETATION OF RESULTS
### 1) FloodLAMP QuickColor(TM) COVID-19 Test Controls
All test controls should be examined prior to interpretation of specimen results. If the controls are not valid, the specimen results cannot be interpreted. An example of the expected appearance of the negative and positive controls after amplification is shown in Figure 1.

**![][image1]**

#### Figure 1. Negative control (left) and positive control (right) after amplification.
If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and optionally RNAseZAP product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### 2) Examination and Interpretation of Patient Specimen Results:
Assessment of clinical patient specimen test results should be performed after the positive and negative controls have been examined and determined to be valid and acceptable. If the controls are not valid, the patient results cannot be interpreted.

Test results should be read at least 1 minute and no more than 8 hours after plates or tubes have been removed from heat. Test results may be determined directly from visual inspection of the color of the reaction tubes: 

* yellow \- result is positive  
* bright pink or red \- result is negative  
* any other color \- result is inconclusive. 

Examples are shown below in Figure 2. Edge cases for positive and negative results are shown below in Figure 3. Any color variance stronger than the edge cases should be interpreted as inconclusive. In order to reduce the chance of both false negative and false positive results, this window for color variance is intentionally set to be small.

If the initial test is inconclusive, then one of the following should be performed:  
1) repeat the Colorimetric LAMP Amplification Reaction on the inactivated sample. If the repeat test has a positive result then the final interpretation of the test is positive. If the repeat test has a negative or another inconclusive result, then the final interpretation is inconclusive.   
2) follow-up test the inactivated sample with the FloodLAMP EasyPCR(TM) COVID-19 Test or another high sensitivity EUA authorized test that comprises the same inactivation protocol. The final interpretation is the result of the follow-up test.

For serial screening of individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, the initial inconclusive test result may be considered the final interpretation. If the final interpretation of the test result is inconclusive, then "Inconclusive" should be reported and retesting of the individual is recommended. 

![][image2]  

## I. PRODUCT MANUFACTURING
### 1) Overview of Manufacturing and Distribution: 
The **FloodLAMP QuickColor(TM) COVID-19 Test** utilizes standard chemicals available in very large quantities from multiple vendors, with the exception of the LAMP Primers and New England Biolabs Colorimetric LAMP Master Mix. 

FloodLAMP has partnered with LGC Biosearch for the LAMP Primers. LGC Biosearch has very large scale oligo production capacity and mature distribution capabilities. The first production scale lot of the LAMP Primers has been completed, with 1.2 million reactions ready for immediate distribution. FloodLAMP has purchased 600K reactions of the LAMP Primers. LGC Biosearch is supplying FloodLAMP for the **FloodLAMP QuickColor(TM) COVID-19 Test** and is also offering the LAMP Primers as a catalog product. 

New England Biolabs has expressed strong support for the **FloodLAMP QuickColor(TM) COVID-19 Test** and FloodLAMP's other open source protocol EUA submissions that incorporate their products. New England Biolabs has very large quantities of the Colorimetric LAMP Master Mix product prepared and ready for immediate distribution, typically with 24 hour shipping within the U.S. Their manufacturing capacity is among the largest in the United States and can surge to meet increased demand.

**\*Under the Emergency Use Authorization (EUA) any of the 21 CFR Part 820 Quality System Regulation (QSR) requirements can be waived for the duration of the EUA but FDA recommends that developers follow comparable practices as much as possible if such requirements are waived. Among other things, FDA may consider previous compliance history when determining whether or not to waive certain QSR requirements for a specific product. Please note adverse events, as per 21 CFR Part 803, have to be reported for authorized devices (see Section P).** 

### 2) Components Included with the Test
None. Designated CLIA labs may order components directly from vendors.

### 3) Components Required But Not Included with Test:
The **FloodLAMP QuickColor(TM) COVID-19 Test** is to be used with the reagents or equivalents listed in Table 3. No specialized instruments are needed. Only ordinary laboratory equipment such as pipettes, centrifuges, and heaters are needed.

#### Table 3: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog No. |
| :---- | ----- | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine | 6 M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| ColorimetricLAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalents. Only the specified vendor and catalog number may be utilized.

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 4. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 4: 100X Inactivation Solution
| Component | Source Concentration | Volume for 100X | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 5. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 5: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :---: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

The **FloodLAMP QuickColor(TM) COVID-19 Test** uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 1. All 18 primers are mixed together and input into a single amplification reaction. 

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered. 

The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease-free water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.

Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at \-20°C for up to 1 year.

#### Table 6: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | #Reactions |
|---------|------|----------------|-----------|------------|
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

The primers are mixed with guanidine hydrochloride to form an intermediate Primer-Guanidine Solution prior to combining with the sample and Colorimetric LAMP MM for the full amplification reaction. The components and volumes for the Primer-Guanidine Solution are listed in Table 7 and may be proportionally scaled for batch sizes of different numbers of reactions. The Primer-Guanidine Solution may be prepared in advance and should be stored at \-20°C for up to 1 month.

#### Table 7: Primer-Guanidine Solution
| Component | Volume (1 reaction) | Volume (100 reactions) |
| :---- | :---: | :---: |
| 10X LAMP Primer Mix | 2.5 µL | 250 µL |
| Guanidine (400 mM) | 2.5 µL | 250 µL |
| Nuclease-free Water | 5.5 µL | 550 µL |
| **TOTAL VOLUME** | **10.5 µL** | **1050 µL** |
||

The final Colorimetric LAMP Amplification Reaction components are listed in Table 8. PCR plates or strip tubes used for the amplification reactions should be maintained on ice or a cold block until less than 5 minutes before incubation on the heater. Reaction plates/strip tubes comprising the Colorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at \-20°C for up to 1 day prior to addition of the sample. A heated plate sealer is recommended. Alternatively, a manually applied foil or optical seal may be used.

#### Table 8: Colorimetric LAMP Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| :---- | :---: | :---: |
| Primer-Guanidine Solution | 10.5 µL | 1050 µL |
| Colorimetric LAMP MM | 12.5 µL | 1250 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **2300 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **25 µL** | - |
||

### 4) Software Validation
No software is required for labs to run the **FloodLAMP QuickColor(TM) COVID-19 Test*.***

### 5) Testing Capabilities 
The **FloodLAMP QuickColor(TM) COVID-19 Test** has been optimized for a robust, streamlined workflow and rapid turnaround time on results. The total time to perform the test is dependent upon the following factors: number of lab technicians, batch size of samples, and advance preparation of reaction mixes. **The minimum turnaround time is approximately 45 minutes.**

Since the **FloodLAMP QuickColor(TM) COVID-19 Test** does not require specialized instruments, it can be scaled up without the capital investment required for PCR machines or automated extraction. The number of tests capable of being performed per day by a laboratory is not constrained by PCR machines or extraction instruments. One technician can manually process approximately one plate (94 samples) per hour. This includes intake (debagging and barcode scanning), inactivation, and LAMP amplification. Automation can greatly increase throughput.

### 6) Reagent Stability
A stability test plan for the components of the **FloodLAMP QuickColor(TM) COVID-19 Test** will be developed during an interactive review. Briefly, the proposed study includes assessing all prepared solutions including: 100X Inactivation Solution, 1X Inactivation Saline Solution, 30X Primer Stock, 10X Primer Mix, Primer-Guanidine Solution, and the full Colorimetric LAMP Amplification Reaction Mix. Prepared solutions will be assessed both for long term storage stability (typically 1-3 months at \-20oC) and short term storage stability prior to usage (typically hours to several days at room temperature, 4oC or \-20oC). 

The proposed study uses a contrived positive sample consisting of inactivated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative specimens at approximately 50,000 copies/mL (4X LoD). The contrived positive stability study samples will be prepared, aliquoted and stored at \-80oC to permit repeated testing of the various solutions at the appropriate step of the test protocol.

For test components supplied by vendors, such as the Colorimetric LAMP Master Mix, the manufacturer's recommended storage conditions and duration will be followed.

### 7) Sample Stability
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19: https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

Samples can be stored at room temperature for 56 hours after collection prior to inactivation. For longer term storage, samples can be stored at ≤-70oC.

## J. PERFORMANCE EVALUATION
### 1) Limit of Detection (LoD) - Analytical Sensitivity:
The Limit of Detection (LoD) for the **FloodLAMP QuickColor(TM) COVID-19 Test** was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 12,500 and 6,250 were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 9. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 12,500 copies/mL.

#### Table 9: LoD Confirmatory Data Results
| Concentration of Contrived Positive Sample  | Replicates Detected |
| :---: | :---: |
| 12,500 copies/mL | 95% (20/21) |
| 6,250 copies/mL | 52% (11/21) |
||

### 2) Inclusivity (analytical sensitivity):
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 10 summarizes the results of this in silico inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.	

#### Table 10: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total Number of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

#### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs ([primer-monitor.neb.com](https://primer-monitor.neb.com/)), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 11, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 \-t 16 \-x asm5 \-a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having \>= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations is not expected to reduce performance of the **FloodLAMP QuickColor(TM) COVID-19 Test** by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 11: Variant Analysis of LAMP Primers
![][image3]  
![][image4]

### 3) Cross-reactivity (Analytical Specificity):
*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the **FloodLAMP QuickColor(TM) COVID-19 Test** against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 12A, 12B, and 12C. 

The % identity range (\# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with \>= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the in silico cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 12A: *In Silico* Cross-Reactivity Analysis for AS1e Primers
![][image5]

#### Table 12B: *In Silico* Cross-Reactivity Analysis for N2 Primers
![][image6]

#### Table 12C: *In Silico* Cross-Reactivity Analysis for E1 Primers
![][image7]

Wet testing was performed to demonstrate that the **FloodLAMP QuickColor(TM) COVID-19 Test** does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen.  SARS-CoV, RSV, Flu, Human Metapneumovirus. and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 12 and Supporting Data. 5 µL of each stock of cross-reactivity organism was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked onto the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived positive had 38 µL of 1e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 38,000 copies/mL in the sample input into the amplification reaction.

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 13.

#### Table 13: Wet Testing Cross-Reactivity Results
| Organism | Description | BEI Number | Detected Replicates |
| ----- | ----- | :---: | :---: |
| SARS-CoV | UV-inactivated virus | NR-3882 | 0/3 |
| Human Metapneumovirus | Genomic RNA | NR-49122 | 0/3 |
| RSV | Genomic RNA | NR-43976 | 0/3 |
| Influenza B | Genomic RNA | NR-45848 | 0/3 |
| Streptococcus salivarius | Bacterial cell culture | HM-121 | 0/3 |
||

#### Endogenous Interference Substances Studies:
Exogenous and endogenous substances were tested for potential interference with the **FloodLAMP QuickColor(TM) COVID-19 Test.** 10 µL of each stock of interfering substance was spiked on dried AN swab specimens. A contrived positive control was produced by spiking gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) onto dried AN swab specimens. Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. The contrived Positive Control Spiked comprised 20 µL of 8e6 copies/mL irradiated virus stock spiked in, producing after elution of the swab in 1 mL of Inactivation Saline Solution at most a concentration of 160,000 copies/mL in the sample input into the amplification reaction.

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 14 and Supporting Data.

#### Table 14: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

### 4) Clinical Evaluation
The clinical evaluation of the **FloodLAMP QuickColor(TM) COVID-19 Test** utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The **FloodLAMP QuickColor(TM) COVID-19 Test** showed a positive agreement of 90% and a negative agreement of 100%. The 4 false negative results were specimens with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is below in Table 15.

Anterior nares swab specimens were collected from patients in phosphate buffered saline by the Stanford COVID-19 clinical testing program. Specimens were initially tested by the Stanford clinical laboratory using the Hologic Panther Fusion and Aptima SARS-CoV-2 Assays, which serves as the high sensitivity comparator test. 

For the **FloodLAMP QuickColor(TM) COVID-19 Test**, materials and the Instructions For Use were provided to the Stanford clinical laboratory. The materials provided consisted of the validated reagents listed in Table 3, the LGC primers and probes, and an aliquot of the positive control. After thawing the frozen specimens, 1 mL of each specimen was transferred to 5mL tubes for the inactivation step. The positive and negative clinical specimens were assigned a new ID in a random order, then transferred to new tubes that were barcoded and labeled with the new ID. The Bio-Rad C1000 Touch(TM) thermal cycler was used for the heating device to perform the isothermal amplification. Two different technicians independently interpreted the results visually per the Instructions For Use, with identical results. Line Item data are provided in the Supporting Data. 

Of the 40 positive specimens, 7 specimens had initial inconclusive results due to color variation beyond the edge case examples. Per Section H2 above, the inactivated samples were follow-up tested with the FloodLAMP EasyPCR(TM) COVID-19 Test, for which all 7 inconclusive results were positive. 

#### Table 15: Clinical Evaluation Results
| FloodLAMP QuickColor(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 36 | 0 | 36 |
| Negative | 4 | 40 | 44 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 90.0% (36/40) 95% CI: 76.3% to 97.2% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## K. UNMET NEED ADDRESSED BY THE PRODUCT
This section will be completed by FDA. 

## L. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for the detection of the SARS-CoV-2 have been approved/cleared by FDA.

## M. BENEFITS AND RISKS:
This section will be completed by FDA.

## N. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS:
Fact Sheets for Patients and Healthcare Providers attached.

## O. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT:
Instructions for Use attached.

## P. RECORD KEEPING AND REPORTING INFORMATION TO FDA:
Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.


# 14,252  2021-05-18_Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.1.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-05-18_Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.1.md
file_date: 2021-05-18
title: Instructions for Use - FloodLAMP EasyPCR COVID-19 Test v1.1
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1ZeJ4WLC4KXchsf5Lha6SL-JNIaNHX12dtqlFoInGEwE
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-05-18_Instructions%20for%20Use%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.1.docx
pdf_gdrive_url: https://drive.google.com/file/d/1JmITEap5NAd9_dyouusNwFNYAb2-5F7c
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-05-18_Instructions%20for%20Use%20-%20FloodLAMP%20EasyPCR%20COVID-19%20Test%20v1.1.pdf
conversion_input_file_type: gdoc
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 14252
words: 9133
notes: 
summary_short: The Instructions for Use for the FloodLAMP EasyPCR COVID-19 Test v1.1 provides CLIA high-complexity labs with the complete protocol for an extraction-free, duplex RT-qPCR assay (CDC N1 + RNaseP) used in routine screening programs with at least weekly testing. It details required reagents and equipment, inactivation and amplification workflows, instrument template setup, data export/compilation, and Ct-based interpretation with control acceptance criteria. It also summarizes stated analytical and clinical performance, including a 3,100 copies/mL LoD and 97.5% positive agreement with 100% negative agreement in an 80-specimen evaluation.


CONTENT

***INTERNAL TITLE:*** FloodLAMP EasyPCR(TM) COVID-19 Test
Instructions for Use v1.1

IVD
COVID-19 Emergency Use Authorization Only
For *in vitro* diagnostic (IVD) Use

www.floodlamp.bio
FloodLAMP Biotechnologies, PBC | 930 Brittan Ave. San Carlos, CA 94070 USA

## Table of Contents
|  |  |
|---------|------|
| Intended Use | 3 |
| Principles of Procedure | 3 |
| Materials Provided and Storage | 4 |
| Materials Required but Not Provided | 4 |
| • Standard Lab Equipment and Consumables | 5 |
| Warnings and Precautions | 6 |
| • General Precautions | 6 |
| • Contamination Precautions | 7 |
| Limitations | 7 |
| Conditions of Authorization for the Laboratory | 8 |
| Specimen Collection and Storage | 9 |
| Running Tests | 10 |
| • Reagent Preparation | 10 |
| • Controls Preparation | 11 |
| • PCR Primer Stock Preparation | 12 |
| • Sample Preparation | 14 |
| • Sample Inactivation | 14 |
| • Preparing to Run Assay for the First Time | 14 |
| • Create the Plate Layout Map | 16 |
| • PCR Amplification Reaction Preparation | 19 |
| • Sample Addition | 19 |
| • Run the Assay | 20 |
| • Analyzing Data | 22 |
| • Results Interpretation | 23 |
| • Test Controls | 23 |
| • Patient Specimen Results Interpretation | 23 |
| Performance Evaluation | 24 |
| • Analytical Sensitivity: Limit of Detection (LoD) | 24 |
| • Analytical Sensitivity: Inclusivity/Cross-Reactivity (in silico) | 24 |
| • Analytical Specificity: Cross-Reactivity | 25 |
| • Analytical Specificity: Interfering Substances | 25 |
| Clinical Evaluation | 26 |
| Support | 26 |
||

FloodLAMP EasyPCR(TM) COVID-19 Test  
For COVID-19 Emergency Use Authorization Only  
Instructions for Use

## Intended Use
FloodLAMP EasyPCR(TM) COVID-19 Test is a real-time reverse transcriptase polymerase chain reaction (RT-qPCR) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week, such as those implemented by schools, workplaces and community groups. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories. 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The FloodLAMP EasyPCR(TM) COVID-19 Test is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures. The FloodLAMP EasyPCR(TM) COVID-19 Test is only for use under the Food and Drug Administration’s Emergency Use Authorization.

## Principles of Procedure
The FloodLAMP EasyPCR(TM) COVID-19 Test is a RNA extraction-free, duplexed RT-qPCR assay which indicates whether SARS-CoV-2 RNA is present. It can widely and rapidly be scaled because 1) it does not require nucleic acid extraction equipment, 2) it utilizes reagents and supplies readily available in large quantities, and 3) it is a straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the FloodLAMP QuickColor(TM) COVID-19 Test. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Further, the FloodLAMP QuickColor(TM) COVID-19 Test is isothermal, does not require any instrumentation and has a visual readout. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

In the FloodLAMP EasyPCR(TM) COVID-19 Test, samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step, and the resulting inactivated sample is directly used as input in the duplexed RT-qPCR test. The test does not use new primers and probes for RT-qPCR testing, but rather uses previously validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC, which are readily available from multiple commercial suppliers. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, reducing the number of tests to 1 assay with 2 sets.

## Materials Provided and Storage
The FloodLAMP EasyPCR(TM) COVID-19 Test utilizes standard chemicals available from multiple vendors, with the exception of the PCR Kit. Designated CLIA labs may order components directly from vendors.

## Materials Required but Not Provided
The FloodLAMP EasyPCR(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. The FloodLAMP EasyPCR(TM) COVID-19 Test is to be used with RT-PCR Instruments such as Applied Biosystems Quantstudio(TM) Systems and Bio-Rad CFX(TM) Systems.

#### Table 1: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| ----- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-free Water | - | Ultrapure Water, nuclease free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| PCR Kit\* | - | LunaⓇ Universal Probe One-Step RT-qPCR Kit | New England Biolabs | E3006 |
||

\* Item may not be substituted for equivalent. 

The FloodLAMP EasyPCR(TM) COVID-19 Test uses the validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, detecting the 2 targets in a single well. This configuration is described in the SalivaDirect(TM) EUA Authorized test ([www.fda.gov/media/141192/download](http://www.fda.gov/media/141192/download)).  
   
The complete set of 6 primers and probes may be purchased from the vendor Eurofins Genomics using the catalog number 12YS-010YST. This product contains primers and probes suspended at 100µM and is enough for 12,500 reactions. The contents can be mixed along with nuclease-free water to create the primer stocks used in the FloodLAMP EasyPCR(TM) COVID-19 Test. See Table 6 below for details. A larger volume of primer-probe stock can be prepared in advance and stored at \-20oC for up to 1 year.

#### Table 2: Primers and probes
| Target | Primer/Probe | Sequence |
| ----- | ----- | ----- |
| CDC-N1 |  2019-nCoV\_N1-F | GACCCCAAAATCAGCGAAAT |
| CDC-N1 |  2019-nCoV\_N1-R | TCTGGTTACTGCCAGTTGAATCTG |
| CDC-N1 |  2019-nCoV\_N1-P | **FAM**\-ACCCCGCATTACGTTTGGTGGACC-**IBFQ** |
| Human RNAseP |  RP-F | AGATTTGGACCTGCGAGCG |
| Human RNAseP |  RP-R | GAGCGGCTGTCTCCACAAGT |
| Human RNAseP |  RP-P | **Cy5**\-TTCTGACCTGAAGGCTCTGCGCG-**IBRQ** |
||

### Standard Lab Equipment and Consumables
* 70% ethanol  
* 10% bleach, prepared daily  
* 96-well PCR reaction plates (Applied Biosystems \# 4346906, 4366932, 4346907, Eppendorf \# 951020303 or equivalent)  
* Optical strip caps (Applied Biosystems \# 4323032 or equivalent)  
* Optical plate seal (Applied Biosystems \# 4311971 or equivalent)  
* PCR strip tubes and caps (USA Scientific catalog \# 1402-2500 or equivalent)   
* 5 mL transport tubes or equivalent (sterile)  
* 1.5 mL microcentrifuge tubes or equivalent (nuclease-free)  
* Aerosol resistant micropipette tips (nuclease-free)  
* Micropipettes (calibrated)  
* Bottle top dispenser for 1 mL volume (optional, calibrated)  
* 96-well cold block  
* Cold blocks for 5 mL and 1.5 mL \- 2.0 mL tubes, or ice  
* Vortex mixer  
* 96-well plate centrifuge or equivalent  
* Mini centrifuge for 1.5 mL tubes or equivalent  
* Thermal cycler, water bath, dry heat bath or equivalent (calibrated)  
* Class II Biological Safety Cabinet (BSC)   
* PCR Instrument (choose one)  
  * QuantStudio(TM) 6 Flex  
  * QuantStudio(TM) 7 Pro  
  * Bio-Rad CFX96 Touch(TM)

## Warnings and Precautions
Materials or chemicals required for the use of the FloodLAMP EasyPCR(TM) COVID-19 Test should be closely examined by the user. The user should carefully read all warnings, instructions or Safety Data Sheets provided by the supplier and follow the general safety precautions when handling biohazards, chemicals and other materials.

### General Precautions
* The FloodLAMP EasyPCR(TM) COVID-19 Test is for *in vitro* diagnostic use (IVD) only. Rx Only.  
* For use under COVID-19 Emergency Use Authorization Only.  
* Standard precautions and procedures should be taken when handling and disposing of human samples.  
* This test has not been FDA cleared or approved; the test has been authorized by FDA under an Emergency Use Authorization (EUA) for use by laboratories certified under the Clinical Laboratory Improvement Amendments (CLIA) of 1988, 42 U.S.C. §263a, to perform high complexity tests.  
* This test has been authorized only for the detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens.  
* This test is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of *in vitro* diagnostic tests for detection and/or diagnosis of COVID19 under Section 564(b)(1) of the Act, 21 U.S.C. § 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner.  
* Standard precautions and procedures should be taken when handling and extracting human samples.  
* Standard precautions and procedures should be taken when using laboratory equipment.  
* Standard precautions and procedures should be taken when disposing of waste.  
* Dispose of reagents according to local regulations.  
* Do not use reagents after their recommended stability time frame.  
* Ensure reagents are stored at the recommended temperatures as described below and in the vendor product information and manuals.

### Contamination Precautions
* Avoid contamination by following good laboratory practices, wearing proper personal protective equipment, segregating workflow, and decontaminating workspace appropriately.  
* Ensure that surfaces and equipment used for all test steps have been properly cleaned with 10% bleach and 70% ethanol.  
* Ensure all consumables are DNase and RNase free except for sample collection tubes which may be sterile.  
* Use only calibrated pipettes and filter tips that are sterile and PCR clean.  
* After completion of the test, dispose of the amplification reaction plates or tubes. Do not open tubes or remove the seals on plates after heating amplification reactions.

## Limitations
* The use of this assay as an *in vitro* diagnostic under the FDA COVID-19 Emergency Use Authorization (EUA) is limited to laboratories that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. § 263a, to perform high complexity tests by Rx only.   
* Use of this assay is limited to personnel who are trained in the procedure. Failure to follow these instructions may lead to erroneous results.   
* The performance of the FloodLAMP EasyPCR(TM) COVID-19 Test was established using Nasopharyngeal Swab specimen type collected in saline. Nasal swabs, oropharyngeal swabs, mid-turbinate nasal swabs specimens are also considered acceptable specimen types for use with the test but performance has not been established.   
* Samples must be collected according to recommended protocols and transported and stored as described herein.  
* Samples should not be collected in UTM or VTM or Liquid Amies transport media.  
* The effect of vaccines, antiviral therapeutics, antibiotics, chemotherapeutic or immunosuppressant drugs have not been evaluated.  
* Detection of SARS-CoV-2 RNA may be affected by sample collection methods, patient factors (e.g., presence of symptoms), and/or stage of infection.  
* False-positive results may arise from various reasons, including, but not limited to the following:  
  * Contamination during specimen collection, handling, or preparation  
  * Contamination during assay preparation  
  * Incorrect sample labeling  
* False-negative results may arise from various reasons, including, but not limited to the following:  
  * Improper sample collection or storage  
  * Degradation of SARS-CoV-2 RNA  
  * Presence of inhibitory substances  
  * Use of extraction reagents or instrumentation not approved with this assay   
  * Incorrect sampling window  
  * Failure to follow instructions for use  
  * Mutations in SARS-CoV-2 target sequences  
* Nucleic acid may persist even after the virus is no longer viable.   
* This test cannot rule out diseases caused by other bacterial or viral pathogens.  
* Performance has not yet been established in asymptomatic individuals and will be established during a post-authorization study.   
* Use of the test in a general, asymptomatic population for serial screening is intended to be used as part of an infection control plan, that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should not be treated as definitive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual’s recent exposures, history, and presence of clinical signs and symptoms consistent with COVID-19.  
* This test should not be used within 30 minutes of administering nasal or throat sprays.  
* Positive results must be reported to appropriate public health authorities, following state and national guidelines.   
* The clinical performance of the test has not been established in all circulating variants, and test performance may vary depending on the prevalence of variants circulating at the time of patient testing.   
* Negative test results do not exclude possibility of exposure to or infection with SARS-CoV-2 virus. Patient handling will be directed by healthcare professionals.

## Conditions of Authorization for the Laboratory
The FloodLAMP EasyPCR(TM) COVID-19 Test Letter of Authorization, along with the authorized Fact Sheet for Healthcare Providers, the authorized Fact Sheet for Patients, and authorized labeling are available on the FDA website: [https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas)

However, to assist clinical laboratories running the FloodLAMP EasyPCR(TM) COVID-19 Test, the relevant Conditions of Authorization are listed below:

* Authorized laboratories1 using the FloodLAMP EasyPCR(TM) COVID-19 Test will include all authorized Fact Sheets with test result reports. Under exigent circumstances, other appropriate methods for disseminating these Fact Sheets may be used, which may include mass media.  
* Authorized laboratories1 using the FloodLAMP EasyPCR(TM) COVID-19 Test will use the FloodLAMP EasyPCR(TM) COVID-19 Test as outlined in the FloodLAMP EasyPCR(TM) COVID-19 Test Instructions for Use. Deviations from the authorized procedures, including the authorized clinical specimen types, authorized control materials, authorized other ancillary reagents and authorized materials required to perform the test are not permitted.  
* Authorized laboratories must notify the relevant public health authorities of their intent to run the test prior to initiating testing.  
* Authorized laboratories using the FloodLAMP EasyPCR(TM) COVID-19 Test will have a process in place for reporting test results to healthcare providers and relevant public health authorities, as appropriate.  
* Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.  
* All laboratory personnel using the test must be appropriately trained in molecular assay techniques and use appropriate laboratory and personal protective equipment when handling these test components, and use the test in accordance with the authorized labeling.  
* FloodLAMP Biotechnologies, PBC authorized distributors, and authorized laboratories using the FloodLAMP EasyPCR(TM) COVID-19 Test will ensure that any records associated with this EUA are maintained until otherwise notified by FDA. Such records will be made available to FDA for inspection upon request. 

1 For ease of reference, this will refer to, “Clinical Laboratory Improvement Amendments of  
1988 (CLIA), 42 U.S.C. §263a certified laboratories with FDA Emergency Use Authorization  
FDA for performing SARS-CoV-2 testing

## Specimen Collection and Storage
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19:  
[https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

* Samples can be stored at room temperature for 56 hours after collection prior to inactivation.   
* For longer term storage, samples can be stored at ≤-70o C.

Note: Specimens must be packaged, shipped, and transported according to the current edition of the International Air Transport Association Dangerous Goods Regulation. Follow shipping regulations for UN 3373 Biological Substance, Category B when sending potential 2019-nCoV specimens.

## Running Tests
### Reagent Preparation
The FloodLAMP EasyPCR(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. 

#### Table 1: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| ----- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| PCR Kit\* | - | LunaⓇ Universal Probe One-Step RT-qPCR Kit | New England Biolabs | E3006 |
||

\* Item may not be substituted for equivalent. 

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

The 100X Inactivation Solution is prepared by mixing the components in Table 3 and vortexing for 30 seconds. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20° C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 3: 100X Inactivation Solution
| Component | Source Concentration | Volume | 100X Concentration |
| ----- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 4. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 4: 1X Inactivation Saline Solution
| Component | Volume |
| ----- | :---: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

### Controls Preparation
One **Positive Template Control and one Negative (No Template) Control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes. An **Internal Process Control** is included in every PCR reaction. 

1) A **“No Template” (Negative) Control (NTC)** is needed to assure the absence of cross-contamination from positive samples, positive controls, or amplicons and is used to determine if sample results are valid. It consists of nuclease-free water.  
     
2) A **Positive Template Control** is needed to assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water. Stock and working aliquots of the positive control are produced from the sources listed in Table 5 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.    
     
3) An **Internal Process Control** is needed to assure sufficient specimen quantity and quality. It consists of a primer/probe set targeting the human RNaseP gene that is included in a single PCR amplification reaction. The RNAseP Internal Process Control uses a fluorescent reporter in a separate channel from the SARS-CoV-2 channel (i.e. in duplex).  
   
#### Table 5: Components for Positive Template Control
| Material | Vendor | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µL |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µL |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895µL |
||

### PCR Primer Stock Preparation
The FloodLAMP EasyPCR(TM) COVID-19 Test uses the validated primer and probe sets (2019-nCoV\_N1 and RP) developed by the US CDC. The human Ribonuclease P (RP) probe was modified with a different fluorophore so that the primer/probe set could be combined in a duplex assay, detecting the 2 targets in a single well. This configuration is described in the SalivaDirect(TM) EUA Authorized test ([www.fda.gov/media/141192/download](http://www.fda.gov/media/141192/download)).

The complete set of 6 primers and probes may be purchased from the vendor Eurofins Genomics using the catalog number 12YS-010YST. This product contains primers and probes suspended at 100µM and is enough for 12,500 reactions. The contents can be mixed along with nuclease-free water to create the primer stocks used in the FloodLAMP EasyPCR(TM) COVID-19 Test. See Table 6 below for details. A large volume of primer-probe stock can be prepared in advance and stored at 4°C for one month or \-20°C for up to 1 year. Vendors for the Primer and Probe sets are below in Table 7.

#### Table 6: 5X PCR Primer Stock Preparation from Eurofins Genomics Product
| Component  | 5X PCR Primer Stock Concentration | Volume  (1 reaction) | Volume  (3,125 reactions) |
| ----- | :---: | :---: | :---: |
| 2019-nCov\_N1-F | 2 µM | 0.4 µl | 1,250 µl |
| 2019-nCov\_N1-R | 2 µM | 0.4 µl | 1,250 µl |
| 2019-nCov\_N1-P | 1 µM | 0.2 µl | 625 µl |
| RP-F | 0.75 µM | 0.15 µl | 469 µl |
| RP-R | 0.75 µM | 0.15 µl | 469 µl |
| RP-P | 1 µM | 0.2 µl | 625 µl |
| Nuclease-free water | - | 2.5 µl | 7,813 µl |
| **Total Volume** | - | **4 µl** | **12,500 µl** |
|| 

#### Table 7: PCR Primer Stock Components
| Vendor | Item | Catalog number | Quantity | #Reactions |
|---------|------|----------------|-----------|------------|
| Eurofins Genomics | SalivaDirect™ complete set of 6 primers and probes | 12YS-010YST | 50-100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006821 | 50 nmol | 6,2500 |
| Integrated DNA Technologies | nCoV_N1 Forward Primer Aliquot | 10006830 | 100 nmol | 12,500 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006822 | 50 nmol | 6,250 |
| Integrated DNA Technologies | nCoV_N1 Reverse Primer Aliquot | 10006831 | 100 nmol | 12,500 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006831 | 25 nmol | 6,250 |
| Integrated DNA Technologies | NCoV_N1 Probe Aliquot | 10006832 | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006827 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Forward Primer Aliquot | 10006836 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006828 | 50 nmol | 16,600 |
| Integrated DNA Technologies | RNaseP Reverse Primer Aliquot | 10006837 | 100 nmol | 33,300 |
| Integrated DNA Technologies | RNase P Probe | Custom order (Cy5) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | Custom order (Cy5) | 50 nmol | 12,500 |
| Integrated DNA Technologies | RNase P Probe | 10007061 (ATTO647) | 25 nmol | 6,250 |
| Integrated DNA Technologies | RNase P Probe | 10007062 (ATTO647) | 50 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Forward Primer | nCoV-N1-F-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-100 | 100 nmol | 12,500 |
| LGC Biosearch Technologies | nCoV_N1 Reverse Primer | nCoV-N1-R-1000 | 1000 nmol | 125,000 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | NCoV_N1 Probe | nCoV-N1-P-250 | 250 nmol | 62,500 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Forward Primer | RNP-F-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-20 | 20 nmol | 6,660 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-100 | 100 nmol | 33,300 |
| LGC Biosearch Technologies | RNaseP Reverse Primer | RNP-R-1000 | 1000 nmol | 333,300 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-25 | 25 nmol | 6,250 |
| LGC Biosearch Technologies | RNase P Probe | RNP-PQ670-250 | 50 nmol | 12,500 |
||

### Sample Preparation
\* For wet swab specimens (swabs in saline or unprocessed swab elution): 

1) If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.   
2) Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.   
3) Wipe the outside of the sample tube with 70% ethanol. 

For dry swab specimens:
1) Wipe the outside of the sample tube with 70% ethanol. 

### Sample Inactivation
1) Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and set the temperature to hold at 100°C.  
2) \* For wet swab specimens: transfer 1 mL or available volume of each sample to an appropriately labeled 1.5 mL or 5mL tube and securely cap.   
3) \* For wet swab specimens: add 10µL per 1 mL sample volume of 100X Inactivation Solution to each sample tube.  
4) For dry swab specimens (DO NOT DO FOR WET SWAB SPECIMENS): add 1 mL of 1X Inactivation Solution to each sample tube.  
5) Vortex for 30 seconds.  
6) Place sample tubes into the inactivation heater for 8 minutes.  
7) Remove sample tubes from the inactivation heater and let cool at room temperature for 10 minutes.  
8) Place sample tubes on ice, in the refrigerator, or on a cold block at 4°C until ready to perform amplification reaction. 

Note: Testing of inactivated specimens must be conducted the same day inactivation is performed. For long term storage, keep the original specimen at ≤-70°C. 

### Preparing to Run Assay for the First Time
*Note: Any instrument running the FloodLAMP EasyPCR(TM) COVID-19 Test must be calibrated for the following dyes: FAM and Cy5.*

#### Download the Template Run File
The Template Run File contains all the parameters preconfigured to run the FloodLAMP EasyPCR(TM) COVID-19 Test. These parameters can be seen in more detail under “Create the Run File ...” headings below.

To download the Template Run File:
1) Go to www.floodlamp.bio/euas  
2) Download the Template Run file(s) for the instrument type and assay to be run.

#### Table 7: RT-PCR Instrument Template Run Files
| Instrument | Setup Template Filename |
| ----- | ----- |
| ABI QuantStudio(TM) 7 Pro | FloodLAMP\_QS7Pro\_PCR\_template\_run.edt |
| ABI QuantStudio(TM) 6 Flex | FloodLAMP\_QS6Flx\_PCR\_template\_run.edt |
| Bio-Rad CFX96 Touch(TM) | FloodLAMP\_BRCFX\_PCR\_protocol.prcl |
| Bio-Rad CFX96 Touch(TM) | FloodLAMP\_BRCFX\_PCR\_template\_run.pltd |
||

*Note: Template Run Files only need to be downloaded once upon first use.*

#### Alternatively Create the Template Run File on QuantStudio(TM) 6 Flex or 7 Pro
1) Open the Design and Analysis Software.  
2) Select the “SET UP PLATE” option.  
3) From the sidebar on the screen, select the following properties to filter:  
   1) Instrument – choose the appropriate instrument  
   2) Block – choose the appropriate block  
   3) RunMode – Standard  
   4) Analysis options are left blank  
4) From the plate sections present on the screen, select the correct System Template and the system will automatically navigate to the "Run Method" tab.  
   1) "Presence/Absence" for QuantStudio(TM) 7 Pro  
   2) “Presence-Absence Standard Pre PCR Post” for QuantStudio(TM) 6 Flex  
5) Change Run Parameters as shown below:  
- **Run Method:**  
  - 20μL Rxn Vol.  
  - 105° C Heated Cover Temp  
  - Ramp Rate: 1.6° C/s

#### Table 8 : Thermal cycling and plate read steps for QuantStudio(TM) Systems for PCR
| Stage | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 52° C | 10 min | 1 |
| 2 | 95° C | 2 min | 1 |
| 3 | 95° C | 10 sec | 44 |
| 3 | 55° C \* | 30 sec | 44 |
| 4 | 55° C \*\* | 30 sec | 1 |
||

\* *This step should be the optical read step*  
*\*\* This step is only required for QuantStudio(TM) 6 Flex*

- **Plate Setup**  
  - Targets: FAM (N1) & Cy5 (RP)  
  - Quencher: None  
  - Passive Reference: ROX

6) Once done setting up the template, go to “Actions” in the top right corner and hit “Save As”:  
   1. On Connect: Save to template folder.  
   2. Offline: Save to preferred location.

#### Create the Template Run File on Bio-Rad CFX96 Touch(TM)
1) Launch the CFX96 Touch(TM) software package.  
2) In the Startup Wizard pop-up window select the instrument “CFX96” from the drop down menu.  
3) Under “Select Run Type” press the “User-defined” button.  
4) Create a new thermocycler protocol by selecting “Create New” from the Run Setup window.  
5) Under Tools in the top left toolbar select “Run Time Calculator” and check “96 Wells-All Channels”.  
6) Make the following changes to the cycling conditions in the Protocol Editor:   
   - Sample Volume to 20 µL  
   - Lid Setting to 105°C  
   - Change cycles to be as shown below:  
     

#### Table 9 : Thermal cycling and plate read steps for the Bio-Rad CFX96 Touch(TM)
| Stage | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 52° C | 10 min | 1 |
| 2 | 95° C | 2 min | 1 |
| 3 | 95° C | 10 sec | 44 |
| 3 | 55° C \* | 30 sec | 44 |
||

*\* This step should be the optical read step*

 7. Click “OK” to save the protocol as type Protocol File (\*.prcl) and return to the Protocol tab in Run Setup.

### Create the Plate Layout Map
#### QuantStudio(TM) 6 Flex or 7 Pro Option 1: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run.

1) Open template in Design and Analysis app and go to the “Plate Setup” tab.  
2) On the right side of the screen ensure the “Samples” tab is highlighted and press the addition icon to add the number of samples being tested.   
3) Click on the “Sample 1” box to rename the sample.  
   1) Repeat this step for all subsequent samples being entered.  
4) Click the well located in the plate map then check the box next to the sample name from the right side bar to associate the name to the well.  
   1) There is also the option to highlight the well location in the plate map and click on the “Enter sample” box. Enter the sample ID and press tab to continue to the next well in the plate map. This will automatically load the sample name into the sidebar.  
5) Once the sample names have been entered, the wells may be highlighted by left clicking the mouse over the starting well and dragging the mouse across all wells associated in run. The targets are then chosen by clicking the check boxes next to each target in the sidebar.  
   1) FAM & Cy5 targets should be chosen and named “N1” and “RP” respectively.  
6) Once done setting up the template, go to “Actions” in the top right corner and hit “Save As,” a pop-up window will appear directing the user to title the file according to information pertaining to the sample run.  
   1) Connect: Save to the desired folder (only applicable for 7 Pro).  
   2) Offline: Save to a USB that is inserted into the computer.  
7) Use your plate layout to load your samples and controls after preparing the amplification reaction mix.

#### QuantStudio(TM) 6 Flex or 7 Pro Option 2: Lookup Based on Well Position
For this option, a single generic sample name is applied to all wells, and subsequently, outside of the instrument software, the results are linked to the actual sample name via a lookup table to the well position. 

1) Open the template in the Design and Analysis app and go to the “Plate Setup” tab.  
2) Highlight the entire plate and add 1 sample to all wells, with the same sample name in every well.  
3) Once the sample name has been entered, the targets are chosen by clicking the check boxes next to each target in the sidebar.  
   1) FAM & Cy5 targets should be chosen and named “N1” and “RP” respectively.  
4) Go to “Actions” in the top right corner and hit “Save As” and name the Template Run File as desired and the software will automatically save as a .edt file.  
   1) Connect: Save to desired location (only applicable for QuantStudio 7 Pro).  
   2) Offline: Save to a USB that is inserted into the computer.

This process only needs to be done once – all subsequent runs can use the same Template Run File. 

#### Bio-Rad CFX96 Touch(TM):
1) Launch the CFX96 Touch(TM) software package and open the correct protocol template.  
2) Review the details of the protocol. If correct, click “Next” to proceed to the Plate tab.  
3) On the Plate tab, click “Create New” and the Plate Editor appears.   
4) Use the Plate Editor to create a new plate.  
5) To ensure the correct plate size is selected, go to “Settings \> Plate Size” and check that 96-well or 384-well is selected from the drop-down menu.  
   1) The plate size selected must correspond to the block size of the instrument being used.   
6) To set the plate type, select” Settings \> Plate Type” and select “BR Clear” or “BR White” from the drop-down menu.  
   1) The plate type selected should match the plate type used in the run.  
7) To set the scan mode, select the “All Channels” scan mode from the Scan Mode drop-down list in the Plate Editor toolbar.  
8) Select the “Select Fluorophores” button on the upper right of the Plate Editor window   
   1) De-select all default fluorophores and select “FAM” and “Cy5” and click OK.  
9) In the Plate Editor window highlight the whole plate and click the checkbox in front of FAM and Cy5.  
10) Select the “Experiment Settings” button in order to define the Targets.  
    1) In the lower left of the Experiment Settings window in the New box type in “N1” and select “Add”.  
    2) Repeat this step and type in “RP”.  
    3) Select “OK”.  
11) In the Plate Editor window next to FAM in the drop-down menu under Target Name select “N1” and for Cy5 select “RP”.  
12) Click OK to save changes and close the “Select Fluorophores” dialog box. 

#### Bio-Rad CFX96 Touch(TM) Option 1: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run.

1) Load the appropriate sample type to each well by selecting the well and selecting the appropriate Sample Type (Unknown, NTC, or Positive Control) from the drop-down menu.  
2) Multiple wells can be selected at once to load the sample type.  
   1) Note: The EC can be listed as an Unknown sample.   
3) In the “Target Names” section confirm that the necessary fluorophores are assigned to each well.   
4) Name each well by typing in the sample name and pressing “Enter” in the Sample Names dropdown list in the right pane.   
5) Click OK to save the Plate File (\*.pltd)and return to the Plate tab in Run Setup. When prompted, specify a name for the plate and a save location.

#### Bio-Rad CFX96 Touch(TM) Option 2: Lookup Based on Well Position
For this option, a single generic sample name is applied to all wells, and subsequently, outside of the instrument software, the results are linked to the actual sample name via a lookup table to the well position. 

1. Name the file as desired and save as type “Plate File (\*.pltd)”  
2. Select “Save”, click “OK” in the Plate Editor window and exit the software.

This process only needs to be done once – all subsequent runs can use the same Template Plate File. 

### PCR Amplification Reaction Preparation
1) Place a 96-well PCR plate or PCR strip tubes onto a cold block or ice.  
2) Thaw frozen reagents until ice crystals are not present.   
3) Pulse vortex thawed reagents for 3 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
4) Store on ice or in the refrigerator or on a cold block at 4°C until ready to use.  
5) Prepare the PCR Amplification Reaction Mix by combining the components listed below in Table 10. 

      NOTE: Component volumes should be scaled proportionally for the number of reactions. 

6) Vortex the PCR Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
7) Add 18 µL of the PCR Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

#### Table 10: PCR Amplification Reaction Mix
| Component | Volume (1 reaction) | Volume (1 reaction x 100) 1 x 96-plate w/ 4% overage |
| ----- | :---: | :---: |
| 5X PCR Primer Stock | 4 µL | 400 µL |
| Nuclease-free Water | 3 µL | 300 µL |
| PCR Master Mix\* | 10 µL | 1000 µL |
| PCR RT\* | 1 µL | 100 µL |
| **SUBTOTAL VOLUME** | **18 µL** | **1800 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **20 µL** | - |
||

\* in LunaⓇ Universal Probe One-Step RT-qPCR Kit

### Sample Addition
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Add 2 μL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
2) Mix by pipetting.  
3) If using PCR plate, seal with optical film (optionally using heat sealer). If using PCR strip tubes, cap strips.  
4) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
5) Continue to section “Run the Assay”.

### Run the Assay
Refer to Specific Instrument User Manuals for full system usage and maintenance details.

#### On QuantStudio(TM) 6 Flex
1) To transfer templates from a USB drive plug a USB drive into the USB port below the touchscreen.   
2) If the instrument is in standby, touch the touchscreen to activate it and then press the green power icon.  
3) In the Main Menu, press “View Templates”.   
4) In the Browse Experiments screen, select the template:   
   1) Press the Folder icon, then choose “USB”.   
   2) Press the desired template, then press “Save”.  
5) In the Save Experiment As screen, set the name for the file.  
   1) Press the “New Template Name” field, then enter a name for the copied file.   
   2) Press the “Save to Folder” field, then select the folder to receive the file   
   3) Hit “Save”.   
6) Press the Home icon to return to the Main Menu.  
7) Navigate to the Main Menu screen, then press the red eject icon.   
8) When the side door opens, load the appropriate plate or PCR strips. Ensure that the consumable is properly aligned in the holder.   
9) In the Main Menu, press “Browse Experiments”.   
10) In the Experiments screen, choose the desired experiment and then click the Folder icon to choose where to save the experiment.  
11) Then press “Start Run” to start the run immediately.

#### On QuantStudio(TM) 7 Pro
1) Log into user on instrument.  
2) USB: Plug in USB with saved template on it.  
3) From the options on the instrument’s screen press “Load plate file”.  
   1) The QuantStudio(TM) 7 is a touchscreen device.  
4) From the “Run Queue” screen,   
   1) USB: press “USB drive” on the left side.  
   2) Connect: press Cloud icon on the left side.  
5) This will bring up any plate files saved.  
6) Press the plate file associated with the run to be performed.  
7) A new window will appear requesting location of results once the run is complete.  
   1) Connect: Press the “Cloud Connect” icon, press again to verify location the files will be uploaded to and then press “Done”.  
   2) USB: Press the “USB drive Connected” if the icon is not already highlighted and press “Done”.   
8) Press the double-arrow icon located at the top right sided corner of the screen on the instrument.   
   1) The instrument drawer will open from the front.   
9) Place the plate/strips into the plate holder ensuring proper orientation of the plate.   
   1) A1 well should be in the position of the top left corner.  
   2) The plate/strips will appear slightly suspended above the block due to two silicone strips above and below this plate. This is to be expected and the instrument lid will press the plate down once the drawer has closed.   
10) Press “Start Run” on the screen of the instrument.   
    1) A pop-up window will appear asking the user to confirm the plate has been loaded.   
    2) If the plate has been loaded, press “Start Run” again or press “Open Drawer” to place the plate into the block and then press “Start Run”.

#### On Bio-Rad CFX96 Touch(TM)
1) Open the correct .pcrl file and review the protocol details. If correct click “Next” to proceed to the Plate tab.  
2) When prompted, open the correct .pltd file and review the plate details in the Run Information section.  
3) Select the checkbox for the appropriate block (CFX96 or CFX384) on which to perform the run.  
4) To insert the plate or 8-tube strips into the block, click Open Lid.  
5) Insert the plate or 8-tube strips into the block. Ensure the plate or 8-tube strips are properly oriented.  
6) Click Close Lid.  
7) Click Start Run at the bottom right of the screen.  
8) When prompted, save the data file (.pcrd) to the desired location.

### Analyzing Data
#### Exporting Data from QuantStudio(TM) 6 Flex or 7 Pro
##### Using USB
1) Confirm Quant says “File Transferred \- USB”.  
2) Take USB from Quant and plug it into computer.  
3) Export data off of USB onto computer.

##### Using Cloud Connect with QuantStudio(TM) 7 Pro
1) Go to [Cloud Connect](https://apps.thermofisher.com/apps/spa/#/dashboard%20%20) and log in.  
2) Go to files and find the data that was just uploaded by the Quant, it will be in the folder chosen previously chosen while running the Quant.  
3) Download .xlsx file.

#### Exporting Data from Bio-Rad CFX96 Touch(TM)
1) After the run has completed, open the data file (.pcrd) by going to Select File \> Open \> Data File in the Home window and locating the desired data file. Adjust the following settings as described below.   
2) Select Settings \> Cq Determination mode and select Single Threshold.   
3) Select Settings \> Baseline Setting and select Baseline Subtracted.   
4) Select Settings \> Analysis Mode and select analysis by fluorophore.   
5) Select Settings \> Cycles to Analyze and the Cycles to Analyze dialog box appears. Confirm that all cycles are being analyzed and click “OK”.   
6) Cq values of each well are displayed in the Quantification Data tab.   
7) Export .xlsx files and select Export \> Export all Data Sheets to Excel (Cq values are available in "Quantification Plate View Results").

#### Compiling Results Option 1: Lookup Based on Well Position
For this option, outside of the instrument software the results are linked to the actual sample name via a lookup table to the well position.  An example spreadsheet to perform this lookup and results compilation is available with instructions at [www.floodlamp.bio/euas](http://www.floodlamp.bio/ifus).

#### Compiling Results Option 2: Sample Name Input
For this option, sample names (i.e. specimen IDs) are directly input into the instrument software prior to starting the run.  Open the results file and continue to “Analyzing Data” section to score results.

### Results Interpretation
#### Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to Table 5 below.

1) The “No Template” (Negative) Control (NTC) should yield a negative “not detected” result for both the N1 and RNaseP targets.  
     
2) The Positive Template Control should yield a positive “detected” result for the N1 target and a negative “not detected” for the RNaseP control.  
     
3) The Internal Process Control should yield a positive "detected" result for RNaseP. Detection of RNaseP is required to report a negative SARS-CoV-2 result. 

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP(TM) product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

#### Patient Specimen Results Interpretation
NOTE: Patient specimen results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Use Table 11 below to assign a result to each sample.  

#### Table 11: Interpretation of Assay Results
| ABI QuantStudio(TM) 7 Pro |  |  |
| :---: | :---: | :---: |
| **Result** | **Ct Value: N1** | **Ct Value RP** |
| Positive | \<38.0 | Any Value |
| Negative | ≥38.0 | \<35.0 |
| \*Invalid | ≥38.0 | ≥35.0 |
| **Bio-Rad CFX96 Touch(TM) ABI QuantStudio(TM) 6 Flex** |  |  |
| **Result** | **Ct Value: N1** | **Ct Value RP** |
| Positive | \<40.0 | Any Value |
| Negative | ≥40.0 | \<35.0 |
| \*Invalid | ≥40.0 | ≥35.0 |
||

\*Invalid test results should be repeated by rerunning the primary sample if available, otherwise the inactivated sample. Results from retested samples will follow the same interpretation as listed in Table 11.

If the final interpretation of the test result is invalid, then "Invalid/Inconclusive" should be reported and retesting of the individual is recommended. 

## Performance Evaluation
### Analytical Sensitivity: Limit of Detection (LoD)
The Limit of Detection (LoD) for the FloodLAMP EasyPCR(TM) COVID-19 Test was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 6,300, 3,100 and 1,600 copies/mL were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 12. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 3,100 copies/mL.

#### Table 12: Confirmatory LoD Data Results
| Instrument | LoD | Positive Replicates |
| ----- | :---: | :---: |
| ABI QuantStudio(TM) 7 Pro | 3,100 copies/mL | 95% (20/21) |
| ABI QuantStudio(TM) 6 Flex | 3,100 copies/mL | 100% (21/21) |
| Bio-Rad CFX96 Touch(TM) | 3,100 copies/mL | 95% (20/21) |
||

### Analytical Sensitivity: Inclusivity
FloodLAMP EasyPCR(TM) COVID-19 Test includes a modified RT-qPCR assay by duplexing the previously authorized CDC N1 and human RNase P primer-probe sets. Inclusivity was tested in the original US CDC EUA with all publicly available SARS-CoV-2 genomes as of 1 February 2020. The initial analysis showed 100% homology between the N1 primer-probe set and available genomes, except for one low frequency mismatch with the N1 forward primer. However, this was not expected to affect performance of the primer-probe set due to annealing temperatures of 55°C which tolerate 1-2 mismatches. Indeed, performance of the N1 primer-probe set was shown to be high in the previous comparison of primer-probes sets ([https://www.nature.com/articles/s41564-020-0761-6](https://www.nature.com/articles/s41564-020-0761-6)). GISAID continuously evaluates mismatches between newly available SARS-CoV-2 genomes and primer-probe sets and confirms a low frequency of nucleotide mismatches (\<5%) with the N1 primer-probe set.

### Analytical Specificity: Cross-Reactivity
The primer and probe sets used in FloodLAMP’s duplex assay were developed by the US CDC and have been EUA certified. The CDC reported no cross-reactivity with other human coronaviruses (229E, OC43, NL63, and HKU1), MERS-coronavirus, SARS-coronavirus, and 14 additional human respiratory viruses (see [https://www.fda.gov/media/134922/download](https://www.fda.gov/media/134922/download)). 

### Analytical Specificity: Interfering Substances
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP EasyPCR(TM) COVID-19 Test. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 13.

#### Table 13: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

## Clinical Evaluation
The clinical evaluation of the FloodLAMP EasyPCR(TM) COVID-19 Test utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The FloodLAMP EasyPCR(TM) COVID-19 Test showed a positive agreement of 97.5% and a negative agreement of 100%. The single false negative result was a specimen with a high Ct value as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is shown below in Table 14.

#### Table 14: Clinical Evaluation Results
| FloodLAMP EasyPCR(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 39 | 0 | 39 |
| Negative | 1 | 40 | 41 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 97.5% (39/40) 95% CI: 86.8% to 99.9% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## Support
FloodLAMP Biotechnologies, PBC support center   
eua.support@floodlamp.bio  
650-394-5233

QuantStudio(TM)  is a trademark of Thermo Fisher Scientific (NYSE: TMO)

Bio-Rad(TM) and Bio-Rad CFX96 Touch(TM)  are trademarks of Bio-Rad Laboratories, Inc. (NYSE: BIO)


# 12,132  2021-05-18_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.1.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-05-18_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.1.md
file_date: 2021-05-18
title: Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.1
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/19yTV3UUkOQrfbqOPcL5hhBw9eJyc_5ra5Uz_tKQcs24
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-05-18_Instructions%20for%20Use%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.1.docx
pdf_gdrive_url: https://drive.google.com/file/d/1sX1THefQLIJxrQHUx0_NxRtgRGYfbvwc
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-05-18_Instructions%20for%20Use%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.1.pdf
conversion_input_file_type: gdoc
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 12132
words: 7518
notes: 
summary_short: The Instructions for Use for the FloodLAMP QuickColor COVID-19 Test v1.1 provides CLIA high-complexity laboratories with the complete workflow for an extraction-free, colorimetric RT-LAMP assay with visual result interpretation after chemical and heat inactivation. It details required reagents, primer preparation, step-by-step testing procedures, control requirements, and criteria for interpreting positive, negative, and inconclusive results without specialized instrumentation. It also summarizes analytical and clinical performance, including a 12,500 copies/mL LoD and 90% positive agreement with 100% negative agreement in an 80-specimen clinical evaluation.


CONTENT

***INTERNAL TITLE:*** FloodLAMP QuickColor(TM) COVID-19 Test
Instructions for Use v1.1

IVD
COVID-19 Emergency Use Authorization Only
For *in vitro* diagnostic (IVD) Use

www.floodlamp.bio
FloodLAMP Biotechnologies, PBC | 930 Brittan Ave. San Carlos, CA 94070 USA

## Table of Contents
|  |  |
|---------|------|
| Intended Use | 3 |
| Principles of Procedure | 3 |
| Materials Provided and Storage | 4 |
| Materials Required but Not Provided | 4 |
| • Standard Lab Equipment and Consumables | 6 |
| Warnings and Precautions | 6 |
| • General Precautions | 6 |
| • Contamination Precautions | 7 |
| Limitations | 7 |
| Conditions of Authorization for the Laboratory | 9 |
| Specimen Collection and Storage | 10 |
| Running Tests | 11 |
| • Reagent Preparation | 11 |
| • Controls Preparation | 12 |
| • 10X LAMP Primer Mix Preparation | 13 |
| • Sample Preparation | 15 |
| • Sample Inactivation | 15 |
| • Colorimetric LAMP Amplification Reaction Preparation | 15 |
| • Sample Addition and Heating | 16 |
| • Test Controls | 17 |
| • Patient Specimen Results Interpretation | 18 |
| Performance Evaluation | 19 |
| • Analytical Sensitivity: Limit of Detection (LoD) | 19 |
| • Analytical Sensitivity: Inclusivity (*in silico*) | 19 |
| • Evaluation of Impact of Viral Mutations | 20 |
| • Analytical Specificity: Cross-Reactivity (*in silico*) | 22 |
| • Analytical Specificity: Cross-Reactivity (wet testing) | 26 |
| • Analytical Specificity: Interfering Substances | 26 |
| Clinical Evaluation | 27 |
| Support | 27 |
||

FloodLAMP QuickColor(TM) COVID-19 Test  
For COVID-19 Emergency Use Authorization Only  
Instructions for Use

## Intended Use
FloodLAMP QuickColor(TM) COVID-19 Test is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week, such as those implemented by schools, workplaces and community groups. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories. 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The FloodLAMP QuickColor(TM) COVID-19 Test is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures. The FloodLAMP QuickColor(TM) COVID-19 Test is only for use under the Food and Drug Administration’s Emergency Use Authorization.

## Principles of Procedure
The FloodLAMP QuickColor(TM) COVID-19 Test is a RNA extraction-free reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) molecular assay that indicates the presence of the SARS-CoV-2 viral RNA with a simple visual color change. It can widely and rapidly be scale because 1) no special instrumentation of any kind is required, neither nucleic acid extraction equipment nor a RT-PCR instrument, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the FloodLAMP EasyPCR(TM) Test. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

The FloodLAMP QuickColor(TM) COVID-19 Test uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. It uses Loop Mediated Isothermal Amplification (LAMP), a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. Samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step. The resulting inactivated sample is directly used as input in the LAMP reaction. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. The amplified DNA products lower the pH of the reaction. A phenol red pH indicating dye is included in the amplification reaction mix, thus causing the reaction solution to visibly change from an initial bright pink to a bright yellow when sufficient amplification occurs. Reactions that change color to yellow indicate that SARS-CoV-2 RNA is present.

## Materials Provided and Storage
The FloodLAMP QuickColor(TM) COVID-19 Test utilizes standard chemicals available from multiple vendors, with the exception of the LAMP primers and Colorimetric LAMP master mix. Designated CLIA labs may order components directly from vendors.

## Materials Required but Not Provided
The FloodLAMP QuickColor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. No specialized instruments are needed. Only ordinary laboratory equipment such as pipettes, centrifuges, and heaters are needed.

#### Table 1: Validated reagents used with the Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine HCl | 6 M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| Colorimetric LAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalent. Only the specified vendor and catalog number may be utilized.

The FloodLAMP QuickColor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. All 18 primers are mixed together and are input into a single amplification reaction. Primer names and sequences are listed in Table 2. Primers may be purchased pre-blended from the vendor LGC Biosearch Technologies with the product names LAMP\_S2-As1e, LAMP\_S2-N2, LAMP\_S2-E1. Alternatively, primers may be purchased as individual custom oligos. Appropriate validation of primer mixes from custom oligos is required. See Primer Preparation below for more information. 

#### Table 2: Primer names and sequences
| Primer Name | Sequence (5’-3’) |
| :---- | :---- |
| **ORF1ab gene (AS1e)** |   |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |   |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |   |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

### Standard Lab Equipment and Consumables
* 70% ethanol  
* 10% bleach, prepared daily  
* 96-well PCR reaction plates (Applied Biosystems \# 4346906, 4366932, 4346907, Eppendorf \# 951020303 or equivalent)  
* Optical strip caps (Applied Biosystems \# 4323032 or equivalent)  
* Optical plate seal (Applied Biosystems \# 4311971 or equivalent)  
* PCR strip tubes and caps (USA Scientific catalog \# 1402-2500 or equivalent)   
* 5 mL transport tubes or equivalent (sterile)  
* 1.5 mL microcentrifuge tubes or equivalent (nuclease-free)  
* Aerosol resistant micropipette tips (nuclease-free)  
* Micropipettes (calibrated)  
* Bottle top dispenser for 1 mL volume (optional, calibrated)  
* 96-well cold block  
* Cold blocks for 5 mL and 1.5 mL \- 2.0 mL tubes, or ice  
* Vortex mixer  
* 96-well plate centrifuge or equivalent  
* Mini centrifuge for 1.5 mL tubes or equivalent  
* 2 x Thermal cycler, water bath, dry heat bath or equivalent (calibrated)  
* Class II Biological Safety Cabinet (BSC) 

## Warnings and Precautions
Materials or chemicals required for the use of the FloodLAMP QuickColor(TM) COVID-19 Test should be closely examined by the user. The user should carefully read all warnings, instructions or Safety Data Sheets provided by the supplier and follow the general safety precautions when handling biohazards, chemicals and other materials. 

### General Precautions
* The FloodLAMP QuickColor(TM) COVID-19 Test is for *in vitro* diagnostic use (IVD) only. Rx Only.  
* For use under COVID-19 Emergency Use Authorization Only.  
* Standard precautions and procedures should be taken when handling and disposing of human samples.  
* This test has not been FDA cleared or approved; the test has been authorized by FDA under an Emergency Use Authorization (EUA) for use by laboratories certified under the Clinical Laboratory Improvement Amendments (CLIA) of 1988, 42 U.S.C. §263a, to perform high complexity tests.  
* This test has been authorized only for the detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens.  
* This test is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of *in vitro* diagnostic tests for detection and/or diagnosis of COVID19 under Section 564(b)(1) of the Act, 21 U.S.C. § 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner.  
* Standard precautions and procedures should be taken when handling and extracting human samples.  
* Standard precautions and procedures should be taken when using laboratory equipment.  
* Standard precautions and procedures should be taken when disposing of waste.  
* Dispose of reagents according to local regulations.  
* Do not use reagents after their recommended stability time frame.  
* Ensure reagents are stored at the recommended temperatures as described below and in the vendor product information and manuals.

### Contamination Precautions
* Avoid contamination by following good laboratory practices, wearing proper personal protective equipment, segregating workflow, and decontaminating workspace appropriately.  
* Ensure that surfaces and equipment used for all test steps have been properly cleaned with 10% bleach and 70% ethanol.  
* Ensure all consumables are DNase and RNase free except for sample collection tubes which may be sterile.  
* Use only calibrated pipettes and filter tips that are sterile and PCR clean.  
* After completion of the test, dispose of the amplification reaction plates or tubes. **Do not open tubes** or remove the seals on plates after heating amplification reactions.

## Limitations
* The use of this assay as an *in vitro* diagnostic under the FDA COVID-19 Emergency Use Authorization (EUA) is limited to laboratories that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. § 263a, to perform high complexity tests by Rx only.   
* Use of this assay is limited to personnel who are trained in the procedure. Failure to follow these instructions may lead to erroneous results.   
* The performance of the FloodLAMP QuickColor(TM) COVID-19 Test was established using Nasopharyngeal Swab specimen type collected in saline. Nasal swabs, oropharyngeal swabs, mid-turbinate nasal swabs specimens are also considered acceptable specimen types for use with the test but performance has not been established.   
* Samples must be collected according to recommended protocols and transported and stored as described herein.  
* Samples should not be collected in UTM or VTM or Liquid Amies transport media.  
* The effect of vaccines, antiviral therapeutics, antibiotics, chemotherapeutic or immunosuppressant drugs have not been evaluated.  
* Detection of SARS-CoV-2 RNA may be affected by sample collection methods, patient factors (e.g., presence of symptoms), and/or stage of infection.  
* False-positive results may arise from various reasons, including, but not limited to the following:  
  * Contamination during specimen collection, handling, or preparation  
  * Contamination during assay preparation  
  * Incorrect sample labeling  
* False-negative results may arise from various reasons, including, but not limited to the following:  
  * Improper sample collection or storage  
  * Degradation of SARS-CoV-2 RNA  
  * Presence of inhibitory substances  
  * Use of extraction reagents or instrumentation not approved with this assay   
  * Incorrect sampling window  
  * Failure to follow instructions for use  
  * Mutations in SARS-CoV-2 target sequences  
* Nucleic acid may persist even after the virus is no longer viable.   
* This test cannot rule out diseases caused by other bacterial or viral pathogens.  
* Performance has not yet been established in asymptomatic individuals and will be established during a post-authorization study.   
* Use of the test in a general, asymptomatic population for serial screening is intended to be used as part of an infection control plan that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should not be treated as definitive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual’s recent exposures, history, and presence of clinical signs and symptoms consistent with COVID-19.  
* This test should not be used within 30 minutes of administering nasal or throat sprays.  
* Positive results must be reported to appropriate public health authorities, following state and national guidelines.   
* The clinical performance of the test has not been established in all circulating variants, and test performance may vary depending on the prevalence of variants circulating at the time of patient testing.   
* Negative test results do not exclude possibility of exposure to or infection with SARS-CoV-2 virus. Patient handling will be directed by healthcare professionals.

## Conditions of Authorization for the Laboratory
The FloodLAMP QuickColor(TM) COVID-19 Test Letter of Authorization, along with the authorized Fact Sheet for Healthcare Providers, the authorized Fact Sheet for Patients, and authorized labeling are available on the FDA website: [https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas)

However, to assist clinical laboratories running the FloodLAMP QuickColor(TM) COVID-19 Test, the relevant Conditions of Authorization are listed below:

* Authorized laboratories1 using the FloodLAMP QuickColor(TM) COVID-19 Test will include all authorized Fact Sheets with test result reports. Under exigent circumstances, other appropriate methods for disseminating these Fact Sheets may be used, which may include mass media.  
* Authorized laboratories1 using the FloodLAMP QuickColor(TM) COVID-19 Test will use the FloodLAMP QuickColor(TM) COVID-19 Test as outlined in the FloodLAMP QuickColor(TM) COVID-19 Test Instructions for Use. Deviations from the authorized procedures, including the authorized clinical specimen types, authorized control materials, authorized other ancillary reagents and authorized materials required to perform the test are not permitted.  
* Authorized laboratories must notify the relevant public health authorities of their intent to run the test prior to initiating testing.  
* Authorized laboratories using the FloodLAMP QuickColor(TM) COVID-19 Test will have a process in place for reporting test results to healthcare providers and relevant public health authorities, as appropriate.  
* Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.  
* All laboratory personnel using the test must be appropriately trained in molecular assay techniques and use appropriate laboratory and personal protective equipment when handling these test components, and use the test in accordance with the authorized labeling.  
* FloodLAMP Biotechnologies, PBC authorized distributors, and authorized laboratories using the FloodLAMP QuickColor(TM) COVID-19 Test will ensure that any records associated with this EUA are maintained until otherwise notified by FDA. Such records will be made available to FDA for inspection upon request. 


1 For ease of reference, this will refer to, “Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a certified laboratories with FDA Emergency Use Authorization FDA for performing SARS-CoV-2 testing

## Specimen Collection and Storage
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19:  
[https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

* Samples can be stored at room temperature for 56 hours after collection prior to inactivation.   
* For longer term storage, samples can be stored at ≤-70oC.

Note: Specimens must be packaged, shipped, and transported according to the current edition of the International Air Transport Association Dangerous Goods Regulation. Follow shipping regulations for UN 3373 Biological Substance, Category B when sending potential 2019-nCoV specimens.

## Running Tests
### Reagent Preparation
The FloodLAMP QuickColor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. 

#### Table 1: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine HCl | 6M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| Colorimetric LAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalent. 

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 3 and vortexing for 30 seconds. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 3: 100X Inactivation Solution
| Component | Source Concentration | Volume | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |
||

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 4. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 4: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :---: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

### Controls Preparation
**One positive and one negative control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes on each heater:

1) A “no template” (negative) control (NTC) is needed to **assure the absence of cross contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of 100X Inactivation Solution diluted to 1X in 0.9% saline. This NTC is the same solution added to dry swabs (see Table 3 and Table 4 above for the components).**  
     
2) A positive template control is needed to **assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 5 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.   
   
#### Table 5: Components for Positive Template Control
| Material | Vendor | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µL |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µL |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895 µL |
||

### 10X LAMP Primer Mix Preparation
The FloodLAMP QuickColor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 2. All 18 primers are mixed together and input into a single amplification reaction. 

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered.   
   
The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease-free water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.  
   
Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at \-20°C for up to 1 year.

#### Table 6: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | #Reactions |
|---------|------|----------------|-----------|------------|
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP AS1e 6 primer set at 30X (ORF1ab gene) | LAMP_S2-AS1e-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

### Sample Preparation
\* For wet swab specimens (swabs in saline or unprocessed swab elution): 

1) If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.   
2) Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.   
3) Wipe the outside of the sample tube with 70% ethanol. 

For dry swab specimens:

1) Wipe the outside of the sample tube with 70% ethanol. 

### Sample Inactivation
1) Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and set the temperature to hold at 100 °C.  
2) \* For wet swab specimens: transfer 1 mL or available volume of each sample to an appropriately labeled 1.5 mL or 5mL tube and securely cap.   
3) \* For wet swab specimens: add 10μL per 1 mL sample volume of 100X Inactivation Solution to each sample tube.  
4) For dry swab specimens (DO NOT DO FOR WET SWAB SPECIMENS): add 1 mL of 1X Inactivation Solution to each sample tube.  
5) Vortex for 30 seconds.  
6) Place sample tubes into the inactivation heater for 8 minutes.  
7) Remove sample tubes from the inactivation heater and let cool at room temperature for 10 minutes.  
8) Place sample tubes on ice, in the refrigerator, or on a cold block at 4°C until ready to perform amplification reaction. 

Note: Testing of inactivated specimens must be conducted the same day inactivation is performed. For long term storage, keep the original specimen at ≤-70°C. 

### Colorimetric LAMP Amplification Reaction Preparation
1) Place a 96-well PCR plate or PCR strip tubes onto a cold block or ice.  
2) Thaw frozen reagents until ice crystals are not present.   
3) Pulse vortex thawed reagents and briefly spin down in a centrifuge.   
4) Store on ice, in the refrigerator, or on a cold block at 4°C until ready to use.  
5) Combine components of Primer-Guanidine Solution per volumes listed in Table 7, or proportionally scaled for the number of reactions to be run. 

      NOTE: Component volumes should be scaled proportionally for the number of reactions.   
      NOTE: The Primer-Guanidine Solution may be prepared in advance and stored at \-20°C    
      for up to 1 month.

6) Pulse vortex and briefly spin down in a centrifuge.   
7) Prepare the Colorimetric LAMP Amplification Reaction Mix by adding the Colorimetric LAMP MM to the Primer-Guanidine Solution per the volumes listed in Table 8.   
8) Vortex the Colorimetric LAMP Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
9) Add 23 µL of the Colorimetric LAMP Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

   NOTE: Reaction plates/strip tubes comprising the Colorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at \-20°C for up to 3 days prior to addition of the sample. A heated plate sealer may be used to seal plates. Alternatively, a manually applied foil or optical seal may be used.

#### Table 7: Primer-Guanidine Solution
| Component | Volume (1 reaction) | Volume (1 reaction x 100) 1 x 96-plate w/ 4% overage |
| ----- | :---: | :---: |
| 10X LAMP Primer Mix | 2.5 µL | 250 µL |
| Guanidine HCl (400 mM) | 2.5 µL | - |
| Guanidine HCl (6 M) | - | 16.7 µL |
| Nuclease-free Water | 5.5 µL | 783 µL |
| **TOTAL VOLUME** | **10.5 µL** | **1050 µL** |
||

#### Table 8: Colorimetric LAMP Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| ----- | :---: | :---: |
| Primer-Guanidine Solution | 10.5 µL | 1050 µL |
| Colorimetric LAMP MM | 12.5 µL | 1250 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **2300 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **25 µL** | - |
||

### Sample Addition and Heating
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Turn on the amplification heater (a thermal cycler, water bath, dry heat bath or equivalent) and set the temperature to hold at 65°C.

   NOTE: Amplification heater should be located in a separate, dedicated BSC or area of the lab. Proper cross contamination prevention practices are required, such as glove changes, to prevent amplicon contamination.

2) Add 2 μL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
3) Mix by pipetting.  
4) If using PCR plate, seal with foil seal, optical seal (optionally using heat sealer). If using PCR strip tubes, cap strips.  
5) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
6) Place the plate or strip tubes in the heater and set timer for 25 minutes (do not use heated lid).  
7) Remove the plate or strip tubes from the heater after 25 minutes.  
8) Let cool for 1 minute and then interpret the test results.

### Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. An example of the expected appearance of the negative and positive controls after amplification is shown in Figure 1.

**![][image1]![][image2]**

#### Figure 1: Negative control (left) and positive control (right) after amplification.
If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and optionally RNAseZAP product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### Patient Specimen Results Interpretation
NOTE: Patient specimen results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Test results should be read at least 1 minute and no more than 8 hours after plates or tubes have been removed from heat. Test results may be determined directly from visual inspection of the color of the reaction tubes: 

* yellow \- result is positive  
* bright pink or red \- result is negative  
* any other color \- result is invalid. 

Examples are shown below in Figure 2. Edge cases for positive and negative results are shown below in Figure 3. Any color variance stronger than the edge cases should be interpreted as inconclusive. In order to reduce the chance of both false negative and false positive results, this window for color variance is intentionally set to be small.

If the initial test is inconclusive, then one of the following should be performed:  
1) repeat the Colorimetric LAMP Amplification Reaction on the inactivated sample. If the repeat test has a positive result then the final interpretation of the test is positive. If the repeat test has a negative or another inconclusive result, then the final interpretation is inconclusive.  
2) follow-up test the inactivated sample with the FloodLAMP EasyPCR(TM) COVID-19 Test or another high sensitivity EUA authorized test that comprises the same inactivation protocol. The final interpretation is the result of the follow-up test.

For serial screening of individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, the initial inconclusive test result may be considered the final interpretation.

If the final interpretation of the test result is inconclusive, then "Inconclusive" should be reported and retesting of the individual is recommended. 

| ![][image3] |                  ![][image4]![][image5] |
| :---- | :---- |
| **Figure 2. Example of Test Results  (Left 2 Negative, Right 2 Positive)** |                         **Figure 3. Edge Case Test Results                          (Left Negative, Right Positive)** |

## Performance Evaluation
### Analytical Sensitivity: Limit of Detection (LoD)
The Limit of Detection (LoD) for the FloodLAMP QuickColor(TM) COVID-19 Test was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 12,500 and 6,250 were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 9. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 12,500 copies/mL.

#### Table 9: LoD Confirmatory Data Results
| Concentration of Contrived Positive Sample  | Replicates Detected |
| :---: | :---: |
| 12,500 copies/mL | 95% (20/21) |
| 6,250 copies/mL | 52% (11/21) |
||

### Analytical Sensitivity: Inclusivity (*in silico*)
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 10 summarizes the results of this *in silico* inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.	

#### Table 10: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total \# of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs ([primer-monitor.neb.com](http://primer-monitor.neb.com)), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 11, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 \-t 16 \-x asm5 \-a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having \>= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations is not expected to reduce performance of the FloodLAMP QuickColor(TM) COVID-19 Test by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 11: Variant Analysis of LAMP Primers
![][image6]  
![][image7]

### Analytical Specificity: Cross-Reactivity (*in silico*)
*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the FloodLAMP QuickColor(TM) COVID-19 Test against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 12A, 12B, and 12C. 

The % identity range (\# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with \>= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the *in silico* cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 12A: *In Silico* Cross-Reactivity Analysis for AS1e Primers
![][image8]

#### Table 12B: In Silico Cross-Reactivity Analysis for N2 Primers
![][image9]

#### Table 12C: *In Silico* Cross-Reactivity Analysis for E1 Primers
![][image10]

### Analytical Specificity: Cross-Reactivity (*wet testing*)
Wet testing was performed to demonstrate that the FloodLAMP QuickColor(TM) COVID-19 Test does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen.  SARS-CoV, RSV, Flu, Human Metapneumovirus. and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 13. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 13.

#### Table 13: Wet Testing Cross-Reactivity Results
| Organism | Description | BEI Number | Detected Replicates |
| ----- | ----- | :---: | :---: |
| SARS-CoV | UV-inactivated virus | NR-3882 | 0/3 |
| Human Metapneumovirus | Genomic RNA | NR-49122 | 0/3 |
| RSV | Genomic RNA | NR-43976 | 0/3 |
| Influenza B | Genomic RNA | NR-45848 | 0/3 |
| Streptococcus salivarius | Bacterial cell culture | HM-121 | 0/3 |
||

### Analytical Specificity: Interfering Substances
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP QuickColor(TM) COVID-19 Test. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 14 and Supporting Data.

#### Table 14: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

## Clinical Evaluation
The clinical evaluation of the FloodLAMP QuickColor(TM) COVID-19 Test utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The FloodLAMP QuickColor(TM) COVID-19 Test showed a positive agreement of 90% and a negative agreement of 100%. The 4 false negative results were specimens with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is below in Table 15. 

#### Table 15: Clinical Evaluation Results
| FloodLAMP QuickColor(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 36 | 0 | 36 |
| Negative | 4 | 40 | 44 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 90.0% (36/40) 95% CI: 76.3% to 97.2% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |
||

## Support
FloodLAMP Biotechnologies, PBC support center   
eua.support@floodlamp.bio  
650-394-5233


# 5,822  2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection DTC.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection DTC.md
file_date: 2021-05-18
title: Pre-EUA Sub - FloodLAMP Pooled Swab Collection DTC
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: docx
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1SixDbR0YTTz5b1xIA92TCH0dt6Yul5hG
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-05-18_Pre-EUA%20Sub%20-%20FloodLAMP%20Pooled%20Swab%20Collection%20DTC.docx
pdf_gdrive_url: https://drive.google.com/file/d/1xyDz50WSzjhaVNuEXPk5GfsRWQojUJRP
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-05-18_Pre-EUA%20Sub%20-%20FloodLAMP%20Pooled%20Swab%20Collection%20DTC.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 5822
words: 4092
notes: 
summary_short: The Pre-EUA submission for the FloodLAMP Pooled Swab Collection Kit DTC outlines an unsupervised, direct-to-consumer system for pooling 1–4 dry anterior nasal swabs for SARS-CoV-2 testing at designated CLIA high-complexity laboratories. It describes the kit components, ordering/registration and accessioning workflows (including optional use of the FloodLAMP Mobile App for pooling, identity, and results delivery), and planned usability and stability/rehydration validation for use with authorized molecular tests. It frames intended use for asymptomatic screening programs and specifies reporting, labeling, manufacturing, and recordkeeping expectations for an EUA pathway.


CONTENT

***INTERNAL TITLE:*** Home Specimen Collection Molecular Diagnostic Template
## A. PURPOSE FOR SUBMISSION
Emergency Use Authorization (EUA) request for distribution and/or use of the **FloodLAMP Pooled Swab Collection Kit DTC** for the **unsupervised collection** of **1 to 4 pooled nasal swabs** in a **dry tube** to transport viral SARS-CoV-2 RNA, from **any individual, including individuals without symptoms or other reasons to suspect COVID-19**. The collection kit is for use in conjunction with molecular diagnostic testing performed at a clinical laboratory using an in vitro diagnostic (IVD) test for the detection of SARS-CoV-2 that is authorized for use with the **FloodLAMP Pooled Swab Collection Kit DTC**.

Testing is limited to laboratories designated by **FloodLAMP Biotechnologies, PBC** that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, and meet requirements to perform high complexity tests.

Test results may be delivered to the user via the **FloodLAMP Mobile App or Web Portal**. Individuals with positive or inconclusive will be referred to a healthcare provider. The direct to consumer home collection system is intended to enable individuals and organizations to access information about their COVID-19 infection status that could aid with determining if self-isolation or quarantine is appropriate and to assist with healthcare decisions after discussion with a healthcare provider.

The **FloodLAMP Pooled Swab Collection Kit DTC** is for use by unsupervised adults 18 years and older, to self-collect dry anterior nasal swab specimens, including for use by such individuals without symptoms or other reasons to suspect COVID-19. Collection for minors under the age of 18 may be assisted by pre-authorized individuals, including by a parent, guardian or other responsible person who is contributing a nasal swabs specimen to the same pool as the minor.

The **FloodLAMP Pooled Swab Collection Kit DTC** is not a substitute for visits to a healthcare provider. The information provided by this kit when combined with an authorized test should not be used to start, stop, or change any course of treatment unless advised by your healthcare provider.

## B. APPLICANT
FloodLAMP Biotechnologies, a DE Public Benefit Corporation
| Mailing Address: 4860 Alpine Rd. Portola Valley, CA 94028 | Laboratory Address: 930 Brittan Ave San Carlos, CA 94070	 | Randall J. True, CSO Phone: (415) 269-2974 Email: randy@floodlamp.bio |
| :---- | :---- | :---- |

## C. PROPRIETARY AND ESTABLISHED NAMES
Proprietary Name - **FloodLAMP Pooled Swab Collection Kit DTC**
Established Name - **FloodLAMP Pooled Swab Collection Kit DTC**

## D. REGULATORY INFORMATION
### Approval/Clearance Status:
The **FloodLAMP Pooled Swab Collection Kit DTC and FloodLAMP Mobile App** are not cleared, approved, or subject to an approved investigational device exemption.

### Product Code: 
*QJR*

## E. PROPOSED INTENDED USE
### 1) Intended Use:
***The proposed IU will be finalized based on, among other things, the data and recommendations from Public Health authorities at the time of authorization – example text is provided below.***

***Example text for a home collection kit where the manufacturer does not hold the COVID-19 NAAT test EUA:***

The **FloodLAMP Pooled Swab Collection Kit DTC** is a direct to consumer (DTC) product for **self-collecting pooled anterior nasal swabs in a dry tube** at home (which includes a community based setting), **including individuals without symptoms or other reasons to suspect COVID-19**. Specimens collected using the **FloodLAMP Pooled Swab Collection Kit DTC** are transported at ambient temperature for testing at a laboratory. SARS-CoV-2 RNA from the **nasal swabs** is maintained in the specimen packaging and is suitable for use in molecular diagnostic testing performed using an in vitro diagnostic (IVD) test for the detection of SARS-CoV-2 that has been issued an EUA for use with Home Collection Kits, that includes the **FloodLAMP Pooled Swab Collection Kit DTC**.

Testing is limited to laboratories designated by **FloodLAMP Biotechnologies** and certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests. Testing is also limited to molecular diagnostic tests that are authorized for use with Home Collection Kits for collection of nasal swab specimens, including the **FloodLAMP Pooled Swab Collection Kit DTC**.

The **FloodLAMP Pooled Swab Collection Kit DTC** is only for use under the Food and Drug Administration’s Emergency Use Authorization.

***Example text for a home collection kit where the manufacturer also holds the COVID-19 NAAT test EUA (e.g., an already issued EUA is being revised to authorize home specimen collection as an option):***

The **FloodLAMP QuickColor(TM) COVID-19 Test** is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay that indicates the presence of the SARS-CoV-2 viral RNA with a simple visual color change. The **FloodLAMP EasyPCR(TM) COVID-19 Test** is a real-time reverse transcriptase polymerase chain reaction (RT-qPCR) assay that utilizes a RT-PCR instrument. These tests are RNA extraction-free tests intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs **from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when tested at a weekly interval with no more than 9 days between tests.**

These tests are also for use with the **FloodLAMP Pooled Swab Collection Kit DTC** for **self-collecting pooled anterior nasal swabs in a dry tube** at home (which includes a community based setting), **including individuals without symptoms or other reasons to suspect COVID-19**. Specimens collected using the **FloodLAMP Pooled Swab Collection Kit DTC** are transported at ambient temperature for testing at a laboratory.

Testing is limited to \[***specify laboratory/laboratories***\] certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests.

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in **upper respiratory specimens** during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all positive results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The **FloodLAMP QuickColor(TM) and EasyPCR(TM) COVID-19 Tests** are intended for use by **qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of in vitro diagnostic procedures**. The **FloodLAMP QuickColor(TM) and EasyPCR(TM) COVID-19 Tests** are only for use under the Food and Drug Administration’s Emergency Use Authorization.

### 2) Special Conditions for Use Statements:
For Emergency Use Authorization (EUA) only.

**For prescription use and over-the-counter use**.

For in vitro diagnostic use only.

For use **unsupervised** by people 18 years of age or older.

For use by **minors under the age of 18 with assistance by individuals pre-authorized by a parent or guardian.**

The **FloodLAMP Pooled Swab Collection Kit DTC** is only authorized for use in conjunction with an in vitro diagnostic (IVD) test for the detection of SARS-CoV-2 that has been issued an EUA and is authorized for use with this collection device.

## F. DEVICE DESCRIPTION 
### 1) Device Description:
The **FloodLAMP Pooled Swab Collection Kit DTC** consists of **nasal swabs, barcoded transport tube, zip-seal biohazard safety bag, and instructions**. Some kit configurations include multiple transport tubes and biohazard safety bags for multiple collections. Additionally, the kit may include other tubes for simultaneous collection of individual (non-pooled) swabs, along with a barcode label and additional zip-seal bag.

### 2) Home Collection Kit Ordering and Processing:
The **FloodLAMP Pooled Swab Collection Kit DTC** is available direct to consumer (DTC) without a prescription for any individual 18 years and older. Individuals may receive kits by purchasing through an authorized distributor or as a part of a screening program. Instructions included with the kit guide users on how to properly collect the anterior nasal swab specimens. After collection of all swabs in the pool, the transport tube is capped and placed inside the biohazard bag, which is then sealed. The biohazard bag with specimens is returned to a designated location and placed inside a secure receptacle or given to responsible program staff. The biohazard bag may also be couriered or placed inside an appropriate labeled mailer for shipping to a designated location for processing. The time from collection to receipt for processing is not to exceed 48 hours.

If using the **FloodLAMP Mobile App**, the following steps are performed to complete a pooled collection event:

-   all participants sign up for an account on a computer or mobile device, confirm their identity via email or text message, set a password, login to the app, and digitally sign a consent;

-   a single individual (the "pool sponsor"), who may be a participant in the pool, initiates a collection event and oversees the proper collection of specimens by all participants in the pool;

-   participants are instructed to swab both nostrils per the printed instructions which are reproduced in the app;

-   next, the pool sponsor scans the barcode of the transport tube used for collection of the swab specimens for the collection event;

-   next, the pool sponsor enters the names, emails, or phone numbers of the other participants contributing specimens to the pool;

-   if this collection event is the first time the pool sponsor is including a participant in the pool, the participant is required to provide authorization via the app;

-   after all participants are added, the pool sponsor completes a collection confirmation consisting of questions that are required to be checked.

If not using the **FloodLAMP Mobile App**, the registration of which individuals contribute specimens to the pools may be accomplished through secure lookup tables containing barcodes and PII in a process managed by administrators of the serial screening program.

Barcoded specimen tubes are received at the clinical laboratory for testing and undergo the following accessioning prior to acceptance for testing:

-   biohazard bags are opened and barcoded transport tubes removed;

-   transport tubes are inspected and if cap is missing, tube is improperly capped, or tube is cracked or otherwise damaged, then the tube is intake scanned for intake and rejected for testing;

-   participants with specimens in rejected tubes are notified, and if appropriate, requested to provide another specimen;

-   tubes that are not rejected are placed into a queue for processing.

Clinical laboratories may use an existing LIS or use the lightweight LIS provided in the **FloodLAMP Mobile App**. The app LIS is accessed by switching to "staff mode" which is only available to permitted users. Staff users can place intake scanned tubes into batches both physically and digitally, for example in batches of 94 to run in an amplification plate. The status and results for individual tubes or batches of tubes is set by staff users. After completion of the test (amplification reaction), results (positive, negative, inconclusive/invalid) can be entered by scanning tube barcodes or imported from a file (for example the output file from a RT-PCR instrument). All data is protected by secure login to the **FloodLAMP Mobile App**.

Test results are communicated back to individuals that used the **FloodLAMP Pooled Swab Collection Kit DTC** via the **FloodLAMP Mobile App.** Users set their notification preference as email or text message. When a new result is available, they receive a short message to check the app for that new result. From the home screen in the app, users select "Results" to see their test results. Additionally, administrators receive an email with information on a positive pool including the participants names and contact information.

### 3) Specimen Collection Control:
Though it may also be used for individual specimen collection, the primary use case for the **FloodLAMP Pooled Swab Collection Kit DTC** is for pooled collection as part of a serial screening program. The pool sponsor who registers the collection event in the **FloodLAMP Mobile App** is instructed to observe all participants contributing specimens to the pool to control for proper nasal swabbing technique. This oversight provides a baseline level of specimen collection control.

The **FloodLAMP EasyPCR(TM) COVID-19 Test** which is intended for use with the **FloodLAMP Pooled Swab Collection Kit DTC** has an internal process control to assure sufficient specimen quantity and quality. It consists of a primer/probe set targeting the human RNaseP gene that is included in a single PCR amplification reaction. The RNAseP Internal Process Control uses a fluorescent reporter in a separate channel from the SARS-CoV-2 channel (i.e. in duplex).

### 4) Partnering Laboratories:
| Laboratory  | EUA Assay  | Lab Testing Capacity (per day or week) |
| :---- | :---- | :---- |
| **Lab Name** Address Phone:  CLIA \#: | Assay Name **Identify if Commercial Assay or LDT**  |  |
||

### 5) Test Result Reporting:
All test results will be reported to healthcare providers and relevant public health authorities in accordance with local, state, and federal requirements, using appropriate LOINC and SNOMED codes, as defined by the [Laboratory In Vitro Diagnostics (LIVD) Test Code Mapping for SARS-CoV-2 Tests](https://www.cdc.gov/csels/dls/sars-cov-2-livd-codes.html) provided by CDC. 

Public health reporting will be supported by the **FloodLAMP Mobile App**, through an API or a results export file. Alternatively, reporting may be done through the CDC's SimpleReport application ([https://simplereport.gov/](https://simplereport.gov/)). For pooled results, the reporting occurs during deconvolution testing of individual samples, according to local public health requirements.

### 6) Mobile Applications and Software:
The **FloodLAMP Mobile App** requires 4 MB of device memory and an internet connection. The **FloodLAMP Mobile App** is supported in IOS, Android and mobile web browsers.

IOS is supported from versions 12 through 14. Android is supported from version 5.1 through version 1. Mobile browser testing occurs on safari and chrome using the most recent stable release.

End-to-end testing and validation occurs on the oldest and most recent supported devices for all platform changes. FloodLAMP tests each user stage (onboarding and account creation, sample collection, pooling and deposit, and results) during server and platform updates. All permutations of required and non-required fields are tested for corresponding error codes and successful database entries.

Records are not stored on user devices and are stored on a secure cloud based database.

## G. PRODUCT MANUFACTURING
The**FloodLAMP Pooled Swab Collection Kit DTC \[**has been\] validated using only the components referenced in this submission.

### 1) Overview of Manufacturing and Distribution: 

The product will be manufactured at **Eralab Scientific Instrument (HK) Co., Limited by Ningbo Dasky Life Science** personnel consistent with practices for the production of **diagnostic collection kits** based on **CE standards**. Material manufactured by **Ningbo Dasky Life Science** may be bottled and kitted by **FloodLAMP Biotechnologies** at their manufacturing facility.

The current manufacturing capabilities include the ability to manufacture approximately **50,000 products per week**. In the event of a surge in demand, this could be increased to **4.9 million products per week within a two week timeframe**.

The product will be distributed by **FloodLAMP Biotechnologies and its distribution partners**.

### 2) Components Included with the Home Collection Kit
Components manufactured by **Eralab Scientific Instrument (HK) Co., Limited** and supplied with the home collection kit include:

#### Kit components 
|  |  |  |  |
|--------------------|------------------------|-----------|-----------------|
| **Name** | **Description** | **Quantity** | **Material Supplier** |
| Biohazard safety bag | Zip-seal biohazard safety bag | 1 | Various |
| Sterile Collection Tube | Sterile collection tube with QR code | 1 | Various |
| Nasal Swab | Foam or spun polyester swab | 4 | Various |
| Instructions for self collection | Printed card with graphical instructions for self collection | 1 | Printed |
| Fact sheet for individuals | Contains information on risks and benefits | 1 | Printed |
| Return shipping mailer (optional) | Postage paid return mailer | 1 | Various |
||

### 3) Collection Device Stability: 
No collection reagents are used in the **FloodLAMP Pooled Swab Collection Kit DTC**.

## H. PERFORMANCE EVALUATION
### 1) Home Collection Sample Stability Study:
Shipping stability of foam and dry spun polyester swabs has been demonstrated by Quantigen Biosciences with support from The Gates Foundation and UnitedHealth Group. The Quantigen study demonstrated 56-hour stability for dry anterior nasal foam and spun polyester swabs when subjected to both summer and winter thermal excursions. Quantigen Biosciences has granted a right of reference to the stability data to any sponsor, such as FloodLAMP Biotechnologies, PBC pursuing an EUA for which a claimed specimen type is foam or dry spun polyester swabs. Therefore, the stability of anterior nasal samples collected using foam or dry spun polyester swabs were not evaluated in the sample stability study.

**Dry Swab Rehydration Validation:**
The rehydration protocol for dry swabs collected with the **FloodLAMP Pooled Swab Collection Kit DTC** varies depending upon the downstream test chemistry of the COVID-19 NAAT test EUA. Principally, it comprises addition of between 1 mL and 3 mL of solution/media to the tube of pooled dry swabs, with less than 1 mL potentially for individual swabs. The solution/media may contain an inactivation/lysis chemical or it may be VTM or saline solution. After addition of the solution/media, the tube is agitated to facilitate extraction of the specimen from the swab. Typically, 30 seconds of vortexing is recommended. The specific volume, composition of solution/media, and agitation protocol must be validated for all COVID-19 NAAT test EUAs using the **FloodLAMP Pooled Swab Collection Kit DTC**.

For the **FloodLAMP QuickColor(TM) and EasyPCR(TM) COVID-19 Tests**, the rehydration protocol for pools of up to 4 dry swabs collected with the **FloodLAMP Pooled Swab Collection Kit DTC** comprises:

1.  addition of \[1\] mL of 1X Inactivation Saline Solution;

2.  vortex for 30s at 3-5,000 rpm.

Following are the steps of heat inactivation, cooling of samples, and amplification. Please see the test IFUs for the complete SOP.

For validation of the dry swab rehydration protocol for the **FloodLAMP QuickColor(TM) and EasyPCR(TM) COVID-19 Tests** for pools of up to 4 dry swabs collected with the **FloodLAMP Pooled Swab Collection Kit DTC**, contrived positives specimens at 20,000 copies/swab were prepared by

### 2) General Acceptance Criteria:
\* Please see acceptance criteria in section F-2 above and reference to the dry swab stability study in H-1.

### 3) Human Usability Study: Pooled Self-Collection Validation
PROPOSED USABILITY STUDY

-   Testing will include a minimum of 30 participants in each arm and will take place in an actual or simulated home environment.

-   Study Arm 1 will provide only printed IFU instructions with the collection kit and include barcoded collection tubes that have been pre-registered to the participant. This arm assesses usability of a workflow for a serial screening program that uses pre-registration of collection kits.

-   Study Arm 2 will provide printed IFU instructions with the collection kit and require the participant to register the kit using the **FloodLAMP Mobile App**.

-   The entire workflow will be performed by each individual participant using the collection kit, including kit registration, sample collection, packaging of the sample, and return of the sample (by mail or dropoff depending upon the study arm).

-   The participants will be observed either in person or by recorded video conference during sample collection and all difficulties will be noted.

-   Participants will collect pooled samples of between 1 and 4 swab specimens.

-   After the entire process is completed, the user will be given the attached 12 question survey assessing the ease of use of the kit and sample collection as well as understanding of the consequences if steps are not performed correctly. The participant will be able to provide comments if needed.

-   The laboratory personnel will inspect the packaging and specimens upon delivery and note all packaging errors and acceptability of the sample for testing.

-   The samples collected during the study will be tested for specimen adequacy using the **FloodLAMP EasyPCR(TM) COVID-19 Test** which includes an internal human sample control (RNaseP). The RNaseP Ct value will be used to determine if sufficient sample was collected by the user. \[To CDRH Reviewers: Is it acceptable to utilize the FloodLAMP EasyPCR(TM) COVID-19 Test for determining the pass/fail of specimen adequacy? It is not yet an EUA authorized test but a full EUA submission is included along with this pre-EUA for review. The test uses the CDC primers from the EUA authorized SalivaDirect(TM) Test. In the clinical evaluation performed by the Stanford University Clinical Lab, the test showed a 98% sensitivity. The LoD was determined at 3,100 copies/mL.\]

-   Participants will include individuals representing varying education levels and ages. Participants with prior medical or laboratory training will be excluded. <s>Participants who have prior experience with self-collection should be excluded.</s> \[To CDRH Reviewers: Is it acceptable to strike this exclusion since self-collection has become much more widespread?\]

-   The study will have pre-defined acceptance criteria and errors identified in the study will be mitigated by modifying the instructions.

#### Inclusion and Exclusion Criteria for Usability Study (both arms)
|  |  |
|------------------------------------|------------------------------------|
| **Inclusion Criteria** | **Exclusion Criteria** |
| Participant is 18 years or older. | Participant has participated in a prior COVID-19 collection kit usability study. |
| Participant resides in the United States. | Participant is suspected of COVID-19. |
| Participant speaks English. | Participant is experiencing symptoms of COVID-19. |
| Participant is willing to read the study information and informed consent. | Participant has received a positive COVID-19 test result. |
| Participant is willing to sign the informed consent. | Participant has prior medical or laboratory training. |
| Participant is willing to complete the survey. | Participant regularly uses home use diagnostic tests, such as glucose meters. |
| Participant is willing to have the interview recorded. | Participant does not speak English. |
||

#### Inclusion and Exclusion Criteria for Usability Study (additional for arm 2)
|  |  |
|------------------------------------|------------------------------------|
| **Inclusion Criteria** | **Exclusion Criteria** |
| Participant has a valid email address. | Participant is a professional software developer or UX/UI designer. |
| Participant has access to an iOS or Android mobile device. | - |
| Participant has access to a stable internet connection. | - |
||

### 4) User Labeling:
**You should submit for review your packaging and directions for your specimen collection kit. FDA will review these documents for their ease of use and clarity of instructions. We recommend all directions be written at a 7th grade reading level or below.**

The print version of the Instructions for Use for the **FloodLAMP Pooled Swab Collection Kit DTC** are included as a pdf document with this submission.

## I. UNMET NEED ADDRESSED BY THE PRODUCT 
**This section will be completed by FDA.**

## J. APPROVED/CLEARED ALTERNATIVE PRODUCTS
Currently no methods for specimen self-collection in conjunction with a laboratory-based molecular in vitro diagnostic EUA test for the detection of the SARS-CoV-2 have been approved/cleared by FDA.

## K. BENEFITS AND RISKS:
**This section will be completed by FDA.**
## L. FACT SHEET FOR HEALTHCARE PROVIDERS AND PATIENTS:

**As set forth in the EUAs, Fact Sheets for Patients and Healthcare Providers generally are to be provided with the assays that will be used with the home collection kit *- see examples for authorized EUA tests on our website and templates will be made available.***

## M. INSTRUCTIONS FOR USE/ PROPOSED LABELING/PACKAGE INSERT:
**Include Instructions for Use, Box Labels, Vial Labels and any other proposed labeling for the test and/or home collection kit. You should also include copies of any questionnaires used to determine eligibility of the patient to receive the home collection kit.**

## N. RECORD KEEPING AND REPORTING INFORMATION TO FDA:
If authorized, conditions would likely be included in the EUA to require the following -

**FloodLAMP Biotechnologies** will track adverse events and report to FDA under 21 CFR Part 803. A website is available to report adverse events, and this website is referenced through the **FloodLAMP Biotechnologies** Product Support website: **floodlamp.bio/support**. Each report of an adverse event will be processed according to **FloodLAMP Biotechnologies**’s Non-Conformance Reporting Requirements, and Medical Device Reports will be filed with the FDA as required. Through a process of inventory control, **FloodLAMP Biotechnologies** will also maintain records of device usage/purchase. **FloodLAMP Biotechnologies** will collect information on the performance of the test, and report to FDA any suspected occurrence of false positive or false negative results of which **FloodLAMP Biotechnologies** becomes aware. **FloodLAMP Biotechnologies** will maintain records associated with this EUA and ensure these records are maintained until notified by FDA. Such records will be made available to FDA for inspection upon request.


# 1,498  2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection Kit DTC.md
METADATA
last updated: 2025-12-18 by BA
file_name: 2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection Kit DTC.md
file_date: 2021-05-18
title: 2021-05-18_Pre-EUA Sub - FloodLAMP Pooled Swab Collection Kit DTC
category: regulatory
subcategory: fl-fda-submissions
tags: collection
source_file_type: sketch
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/13ghhBwFK9nAfA2htGq7mQ_5_JXSgTixt
pdf_github_url: 
conversion_input_file_type: pdf
conversion: megaparse-u
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1498
words: 1085
notes: 
summary_short: The FloodLAMP Pooled Swab Collection Kit DTC instructions describe how up to four people can self-collect anterior nasal swabs into a single barcoded/QR-coded tube, with step-by-step workflows for both a mobile app–guided and non-app version. It explains kit contents, hygiene and swabbing steps, participant association and tube scanning in the app, and how to package and return specimens via collection point or prepaid mailer. It includes EUA-required limitations stating the product is authorized only for home collection/maintenance of anterior nasal swabs for SARS-CoV-2 nucleic acid detection during the active emergency declaration.


CONTENT

**FloodLAMP Biotechnologies**
A Public Benefit Corporation
FloodLAMP Pooled Swab Collection Kit DTC
For IVD Use. For use under emergency use authorization only.

## Mobile App Version
For use with the FloodLAMP Mobile App

### Your kit includes:

_Diagram of swabs_
Swabs

_Diagram of QR coded tube_
QR coded tube

_Diagram of Biohazard bag_
Biohazard bag

_Diagram of Fact sheet_
Fact sheet

_Diagram of Return shipping mailer_
Return shipping mailer (optional)

### Getting started
- Ensure you and everyone contributing samples washes their hands!
- Inspect contents of kit and ensure you have enough swabs and tubes for the collection.
- Follow the instructions inside this sheet

### Returning your kit
- Contact your program coordinator for kit return details

1. Get the app
Download the FloodLAMP app and register for an account, then login to the app. First time users will need to sign the FloodLAMP consent form. You can associate minors with your account proﬁle.

2. Begin collection
Tap the “Collect” button from the app home screen. Follow the swabbing instructions, which are listed here in steps 3-8.

3. Sanitize
Wash your hands thoroughly for 20 seconds and dry them completely before collecting your sample.

4. Open the kit
Open your kit and distribute swabs to each participant who will be adding samples to the tube.

5. Open swab packs
Each participant should open their swab pack. Be careful not to touch the absorbent end with your hands.

6. Swab the first nostril
Each participant should insert the swab tip into their ﬁrst nostril until the absorbent end is no longer visible. Swab the sides of the nostril in a circular motion 4 times. Make sure to twist the swab as you go.

7. Swab the other nostril
Each participant should repeat the previous steps with the same swab in the second nostril.

8. Put swabs in tube
Each participant should place their swab in the barcoded tube and snap off the end of the swab at the break point.

9. Cap tube
Once each participant has added their swab, securely tighten the cap onto the tube.

10. Scan and add participants
Complete the Collect work ﬂow in the app. You can add up to 4 swabs in each tube, and associate the partipants using their FloodLAMP registered email addresses. Minors will be registered under their guardian’s account.

11. Put the tube in the biohazard bag
Securely close the zippered bag, then thoroughly wash or sanitize your hands.

12. Return the biohazard bag
By collection point: If your kit does not include a return mailer, bring your biohazard bag to the collection point designated by your program administrator.

By mail: If your kit includes a return mailer, seal the biohazard bag in the return mailer. This packaging is specially designed for carrying samples suspected of carrying infectious substances. Do NOT replace it.
Note: Your return shipping has already been paid.

### Need help?
Contact support@ﬂoodlamp.bio or select “Support” from the FloodLAMP app menu.

FloodLAMP.bio

This product has not been FDA cleared or approved, but has been authorized for emergency use by FDA under an EUA;

This product has been authorized only for the home collection and maintenance of anterior nasal swab specimens as an aid in detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens; and,

The emergency use of this product is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of medical devices under Section 564(b)(1) of the Federal Food, Drug and Cosmetic Act, 21 U.S.C. §360bbb-3(b)(1), unless the declaration is terminated or authorization is revoked sooner.

## Non-Mobile App Version
### Your kit includes:
_Diagram of swabs_
Swabs

_Diagram of QR coded tube_
QR coded tube

_Diagram of Biohazard bag_
Biohazard bag

_Diagram of Fact sheet_
Fact sheet

_Diagram of Return shipping mailer_
Return shipping mailer (optional)

### Getting started
- Ensure you and everyone contributing samples washes their hands!
- Inspect contents of kit and ensure you have enough swabs and tubes for the collection.
- Follow the instructions inside this sheet

### Returning your kit
- Contact your program coordinator for kit return details

1. Sanitize
Wash your hands thoroughly for 20 seconds and dry them completely before collecting your sample.

2. Open the kit
Open your kit and distribute swabs to each participant who will be adding samples to the tube.

3. Open swab packs
Each participant should open their swab pack. Be careful not to touch the absorbent end with your hands.

4. Swab the first nostril
Each participant should insert the swab tip into their ﬁrst nostril until the absorbent end is no longer visible. Swab the sides of the nostril in a circular motion 4 times. Make sure to twist the swab as you go.

5. Swab the other nostril
Each participant should repeat the previous steps with the same swab in the second nostril.

6. Put swabs in tube
Each participant should place their swab in the barcoded tube and snap off the end of the swab at the lower break point. You can add up to 4 swabs in each tube.

7. Cap tube
Once each participant has added their swab, securely tighten the cap onto the tube.

8. Put the tube in the biohazard bag
Securely close the zippered bag, then thoroughly wash or sanitize your hands.

9. Return the biohazard bag
By collection point: If your kit does not include a return mailer, bring your biohazard bag to the collection point designated by your program administrator.

By mail: If your kit includes a return mailer, seal the biohazard bag in the return mailer. This packaging is specially designed for carrying samples suspected of carrying infectious substances. Do NOT replace it.
Note: Your return shipping has already been paid.

### Need help?
Contact support@ﬂoodlamp.bio or select “Support” from the FloodLAMP app menu.

FloodLAMP.bio

This product has not been FDA cleared or approved, but has been authorized for emergency use by FDA under an EUA;

This product has been authorized only for the home collection and maintenance of anterior nasal swab specimens as an aid in detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens; and,

The emergency use of this product is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of medical devices under Section 564(b)(1) of the Federal Food, Drug and Cosmetic Act, 21 U.S.C. §360bbb-3(b)(1), unless the declaration is terminated or authorization is revoked sooner.


# 1,318  2021-05-18_Pre-EUA Sub - FloodLAMP Proposed Pooling and Asymptomatic Screening Study.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-05-18_Pre-EUA Sub - FloodLAMP Proposed Pooling and Asymptomatic Screening Study.md
file_date: 2021-05-18
title: Pre-EUA Sub - FloodLAMP Proposed Pooling and Asymptomatic Screening Study
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1l70VyK_wS6DkCVj6G61OaJGPSSHxU7tF4RrfckS0YPA
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-05-18_Pre-EUA%20Sub%20-%20FloodLAMP%20Proposed%20Pooling%20and%20Asymptomatic%20Screening%20Study.docx
pdf_gdrive_url: https://drive.google.com/file/d/1o_BdhSMocE3XsQoZQcS96IuA748hoyCG
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-05-18_Pre-EUA%20Sub%20-%20FloodLAMP%20Proposed%20Pooling%20and%20Asymptomatic%20Screening%20Study.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1318
words: 889
notes: 
summary_short: The Pre-EUA document outlines proposed validation studies to support swab pooling (up to four swabs) and serial asymptomatic screening claims for the FloodLAMP EasyPCR and QuickColor COVID-19 tests, aligned to FDA pooling/serial testing guidance. It specifies LoD and high-viral-load pooling experiments with replicate counts, acceptance criteria (e.g., ≥95% detection, Ct shift limits, invalid-rate thresholds), and use of inactivated virus controls. It also describes an IRB-approved asymptomatic screening study design using self-collected duplicate anterior nares swabs with a comparator EUA PCR test and app-based consent/kit logistics.


CONTENT

## Proposed Pooling Study
From FDA Guidance Document "Pooling and Serial Testing Amendment Letter" (4-20-2021) - Appendix B: Swab pooling up to n=5

“Validation of Expected Limit of Detection (LoD)” and “Validation of High Viral Concentrations”. As part of the notification to FDA, summary data must be submitted, including the percent of positive pools detected, the Ct score difference, and the line data including the Ct score for each pool and individual sample tested.

### 1) Validation of Expected Limit of Detection (LoD)
-   Use inactivated virus of a known quantity represented as copies/mL

    -   Zeptometrix NATSARS(COV2)-ST at 1e6 copies/mL OR

    -   BEI gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287).

-   Prepare negative swabs by collecting from healthy individuals.

-   Sample volumes for 4 swab pools of 2 mL of 1X Inactivation Saline Solution.

-   Prepare positive swabs by spiking a known amount of inactivated virus onto the swab prior to immersion in the 1X Inactivation Saline Solution.

-   Add remaining 4 negative swabs.

-   The final concentration of inactivated virus in the 1X Inactivation Saline Solution is approximately 3x the LoD of the assay.

    -   **FloodLAMP EasyPCR(TM) COVID-19 Test**: 10,000 copies/mL (~3 x 3,100)

    -   **FloodLAMP QuickColor(TM) COVID-19 Test**: 40,000 copies/mL (~3 x 12,500)

-   Test 20 independent extraction replicates of individual positive swabs in 1 mL of 1X Inactivation Saline Solution (same volume used in the LoD study as described in single swab protocol in EUA submission and IFU).

-   Test 20 replicates of 4 swab pools each containing a single positive swab and 3 negative swabs in 2 mL of 1X Inactivation Saline Solution.

-   Results criteria:

    -   ≥95% of pooled replicates are detected as positive using the swab pooling protocol;

    -   The Ct score difference for **FloodLAMP EasyPCR(TM) COVID-19 Test** between the pooled and single swab protocols does not exceed 1.7 Ct;

    -   The invalid rate in the swab pooling protocol does not exceed 5%.

### 2) Validation of High Viral Concentrations
-   Prepare 3 positive swabs simulating high viral concentrations by spiking to a final concentration of 1e6 copies/mL of inactivated virus in 1X Inactivation Saline Solution.

-   Prepare 2 negative swabs by collecting from healthy individuals.

-   Combine 4 swabs into high viral concentration 4 swab pool and add 2 mL of 1X Inactivation Saline Solution.

-   Test 10 replicates of inactivated high viral concentration sample.

-   Results criteria:

    -   All 10 replicates are detected as positive;

    -   The invalid rate does not exceed 5%.

## Proposed Asymptomatic Screening Study
The following clinical study is proposed as a condition of authorization for the serial screening indication of **FloodLAMP EasyPCR(TM) and QuickColor(TM) COVID-19 Tests** which specifies anterior nasal respiratory specimens from individuals without known or suspected COVID-19 when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week, such as those implemented by schools, workplaces and community groups. A point-in-time asymptomatic claim will be requested provided the performance evaluation data from the study supports such a claim.

FloodLAMP has obtained IRB approval to conduct the following clinical study from WCG IRB ("FloodLAMP COVID-19 Test Validation Protocol" 20210401, Study Number 1306140). The IRB Protocol includes several variations in sample collection sites and methods.

### Inclusion and Exclusion Criteria for Asymptomatic Screening Study
| **Inclusion Criteria** | **Exclusion Criteria** |
|------------------------------------|------------------------------------|
| The specimen is an anterior nasal swab using the swab and QR code labeled tubes, nasal swabs included with the FloodLAMP Pooled Swab Collection Kit DTC. | The specimen was not properly collected, identified, transported, processed, or stored according to the instructions provided by the sponsor. |
| The swab specimen can be tested within 56 hours or less after collection. If frozen, specimens are to be stored at &lt;-70℃ until tested. | The specimen was not collected under informed consent. |
| The subject is suspected of COVID, whether or not symptomatic. |  |
| The subject is not experiencing symptoms and/or has not notified a physician that they suspect they have COVID . |  |
| The subject has had a positive COVID test within the last 10 days. |  |
| The specimen is from a consenting male or female (including pregnant women) subject. |  |
| The specimen is from a subject ages 2 to 13 and has been collected by a parent or guardian OR age 14 and above and has been self-collected. |  |
||

The study will utilize an enrichment strategy to obtain specimens from 20 positive and 20 negative subjects. Subject recruitment will be conducted via internet advertisements seeking participation by individuals who are asymptomatic and have recently received a COVID-19 test result. An eligibility questionnaire will select for subjects to meet the 20 positives and 20 negatives. The questionnaire will include symptom screening questions.

Eligible subjects will register using the **FloodLAMP Mobile App**, sign the Research Subject Information and Consent Form, then be mailed a version of the FloodLAMP Home Collection Kit for self-collection and sample return.

Duplicate anterior nares swabs will be self-collected with the order being randomized and at least 10 but no more than 30 minutes between collection of the two swabs. One swab will be used to run the comparator test (EUA purified PCR test) and the other will be used to run the **FloodLAMP EasyPCR(TM) and QuickColor(TM) COVID-19 Tests**.


# 12,223  2021-10-01_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.2.md
METADATA
last updated: 2025-12-16 BA updated metadata after BA fixed inconsistencies
file_name: 2021-10-01_Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.2.md
file_date: 2021-10-01
title: Instructions for Use - FloodLAMP QuickColor COVID-19 Test v1.2
category: regulatory
subcategory: fl-fda-submissions
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/11mBfGYxQ3JLl5seHycFXzzLki5Qaxcp0EiIDuP48GzQ
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/regulatory/fl-fda-subs/2021-10-01_Instructions%20for%20Use%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.2.docx
pdf_gdrive_url: https://drive.google.com/file/d/1iG8vgTipdezsobTOea6URDaP7DWEti31
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/regulatory/fl-fda-subs/2021-10-01_Instructions%20for%20Use%20-%20FloodLAMP%20QuickColor%20COVID-19%20Test%20v1.2.pdf
conversion_input_file_type: gdoc
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 12223
words: 7571
notes: 
summary_short: The FloodLAMP QuickColor COVID-19 Test Instructions for Use v1.2 (draft) provides updated procedures for an extraction-free, colorimetric RT-LAMP assay with visual interpretation (including photo-based review) for routine weekly screening in CLIA high-complexity labs. It details reagents, primer preparation, inactivation and amplification steps, controls, and revised guidance for handling inconclusive results using a triplicate repeat and defined result-mapping rules. It also summarizes analytical and clinical performance claims consistent with prior versions, including a 12,500 copies/mL LoD and 90% positive agreement with 100% negative agreement in an 80-specimen evaluation.


CONTENT

***INTERNAL TITLE:*** FloodLAMP QuickColor(TM) COVID-19 Test
Instructions for Use v1.2 \- DRAFT

IVD
COVID-19 Emergency Use Authorization Only
For *in vitro* diagnostic (IVD) Use

www.floodlamp.bio
FloodLAMP Biotechnologies, PBC | 4860 Alpine Rd. Portola Valley, CA USA 

## Table of Contents
|  |  |
|---------|------|
| Intended Use | 3 |
| Principles of Procedure | 3 |
| Materials Provided and Storage | 4 |
| Materials Required but Not Provided | 4 |
| • Standard Lab Equipment and Consumables | 6 |
| Warnings and Precautions | 6 |
| • General Precautions | 6 |
| • Contamination Precautions | 7 |
| Limitations | 7 |
| Conditions of Authorization for the Laboratory | 9 |
| Specimen Collection and Storage | 10 |
| Running Tests | 11 |
| • Reagent Preparation | 11 |
| • Controls Preparation | 12 |
| • 10X LAMP Primer Mix Preparation | 13 |
| • Sample Preparation | 15 |
| • Sample Inactivation | 15 |
| • Colorimetric LAMP Amplification Reaction Preparation | 15 |
| • Sample Addition and Heating | 16 |
| • Test Controls | 17 |
| • Patient Specimen Results Interpretation | 18 |
| Performance Evaluation | 19 |
| • Analytical Sensitivity: Limit of Detection (LoD) | 19 |
| • Analytical Sensitivity: Inclusivity (*in silico*) | 19 |
| • Evaluation of Impact of Viral Mutations | 20 |
| • Analytical Specificity: Cross-Reactivity (*in silico*) | 22 |
| • Analytical Specificity: Cross-Reactivity (wet testing) | 26 |
| • Analytical Specificity: Interfering Substances | 26 |
| Clinical Evaluation | 27 |
| Support | 27 |
||

FloodLAMP QuickColor(TM) COVID-19 Test  
For COVID-19 Emergency Use Authorization Only  
Instructions for Use

## Intended Use
FloodLAMP QuickColor(TM) COVID-19 Test is a reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) assay intended for the qualitative detection of RNA from SARS-CoV-2 in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs from individuals suspected of COVID-19 by their healthcare provider and from individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, when such individuals are tested as part of a testing program that includes testing at regular intervals, at least once per week, such as those implemented by schools, workplaces and community groups. Testing is limited to laboratories certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a, to perform high complexity tests, or by similarly qualified non-U.S. laboratories. 

Results are for the identification of SARS-CoV-2 RNA. The SARS-CoV-2 RNA is generally detectable in upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs during the acute phase of infection. Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease. Laboratories within the United States and its territories are required to report all test results to the appropriate public health authorities.

Negative results do not preclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.

The FloodLAMP QuickColor(TM) COVID-19 Test is intended for use by qualified and trained clinical laboratory personnel specifically instructed and trained in the techniques of *in vitro* diagnostic procedures. The FloodLAMP QuickColor(TM) COVID-19 Test is only for use under the Food and Drug Administration’s Emergency Use Authorization.

## Principles of Procedure
The FloodLAMP QuickColor(TM) COVID-19 Test is a RNA extraction-free reverse transcriptase loop-mediated isothermal amplification (RT-LAMP) molecular assay that indicates the presence of the SARS-CoV-2 viral RNA with a simple visual color change. It can widely and rapidly be scale because 1) no special instrumentation of any kind is required, neither nucleic acid extraction equipment nor a RT-PCR instrument, 2) it utilizes reagents and supplies readily available in large quantities, and 3) is a straightforward protocol with minimal steps that can be executed quickly and reliably. It also utilizes the same streamlined sample preparation as the FloodLAMP EasyPCR(TM) Test. Both are supply chain robust, "open source" protocol tests, meaning designated laboratories may obtain the test components directly from vendors. Together, the two tests can be used in an integrated program for screening and rapid confirmation in large populations by a broad range of laboratories. 

The FloodLAMP QuickColor(TM) COVID-19 Test uses a set of specific primers that target ORF1ab, N and E genes for the detection of SARS-CoV-2 RNA. It uses Loop Mediated Isothermal Amplification (LAMP), a nucleic acid amplification technique wherein DNA amplification is carried out at a constant temperature of approximately 65°C. Samples are first treated with a TCEP-based Inactivation Solution followed by a heat inactivation step. The resulting inactivated sample is directly used as input in the LAMP reaction. The amplification reaction mix includes a reverse transcriptase (RT) polymerase to create complementary cDNA from RNA. The cDNA is subsequently amplified by a high strand displacement DNA polymerase. The amplified DNA products lower the pH of the reaction. A phenol red pH indicating dye is included in the amplification reaction mix, thus causing the reaction solution to visibly change from an initial bright pink to a bright yellow when sufficient amplification occurs. Reactions that change color to yellow indicate that SARS-CoV-2 RNA is present.

## Materials Provided and Storage
The FloodLAMP QuickColor(TM) COVID-19 Test utilizes standard chemicals available from multiple vendors, with the exception of the LAMP primers and Colorimetric LAMP master mix. Designated CLIA labs may order components directly from vendors.

## Materials Required but Not Provided
The FloodLAMP QuickColor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. No specialized instruments are needed. Only ordinary laboratory equipment such as pipettes, centrifuges, and heaters are needed.

#### Table 1: Validated reagents used with the Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease-free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5 M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine HCl | 6 M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| Colorimetric LAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalent. Only the specified vendor and catalog number may be utilized.

The FloodLAMP QuickColor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. All 18 primers are mixed together and are input into a single amplification reaction. Primer names and sequences are listed in Table 2. Primers may be purchased pre-blended from the vendor LGC Biosearch Technologies with the product names LAMP\_S2-As1e, LAMP\_S2-N2, LAMP\_S2-E1. Alternatively, primers may be purchased as individual custom oligos. Appropriate validation of primer mixes from custom oligos is required. See Primer Preparation below for more information. 

#### Table 2: Primer names and sequences
| Primer Name | Sequence (5’-3’) |
| :---- | :---- |
| **ORF1ab gene (AS1e)** |   |
| Orf1ab\_FIP | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG |
| Orf1ab\_BIP | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG |
| Orf1ab\_F3 | CGGTGGACAAATTGTCAC |
| Orf1ab\_B3 | CTTCTCTGGATTTAACACACTT |
| Orf1ab\_LF | TTACAAGCTTAAAGAATGTCTGAACACT |
| Orf1ab\_LB | TTGAATTTAGGTGAAACATTTGTCACG |
| **N Gene (N2)** |   |
| N2\_FIP | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC |
| N2\_BIP | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA |
| N2\_F3 | ACCAGGAACTAATCAGACAAG |
| N2\_B3 | GACTTGATCTTTGAAATTTGGATCT |
| N2\_LF | GGGGGCAAATTGTGCAATTTG |
| N2\_LB | CTTCGGGAACGTGGTTGACC |
| **E Gene (E1)** |   |
| E1\_FIP | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG |
| E1\_BIP | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT |
| E1\_F3 | TGAGTACGAACTTATGTACTCAT |
| E1\_B3 | TTCAGATTTTTAACACGAGAGT |
| E1\_LF | CGCTATTAACTATTAACG |
| E1\_LB | GCGCTTCGATTGTGTGCGT |
||

### Standard Lab Equipment and Consumables
* 70% ethanol  
* 10% bleach, prepared daily  
* 96-well PCR reaction plates (Applied Biosystems \# 4346906, 4366932, 4346907, Eppendorf \# 951020303 or equivalent)  
* Optical strip caps (Applied Biosystems \# 4323032 or equivalent)  
* Optical plate seal (Applied Biosystems \# 4311971 or equivalent)  
* PCR strip tubes and caps (USA Scientific catalog \# 1402-2500 or equivalent)   
* 5 mL transport tubes or equivalent (sterile)  
* 1.5 mL microcentrifuge tubes or equivalent (nuclease-free)  
* Aerosol resistant micropipette tips (nuclease-free)  
* Micropipettes (calibrated)  
* Bottle top dispenser for 1 mL volume (optional, calibrated)  
* 96-well cold block  
* Cold blocks for 5 mL and 1.5 mL \- 2.0 mL tubes, or ice  
* Vortex mixer  
* 96-well plate centrifuge or equivalent  
* Mini centrifuge for 1.5 mL tubes or equivalent  
* 2 x Thermal cycler, water bath, dry heat bath or equivalent (calibrated)  
* Class II Biological Safety Cabinet (BSC) 

## Warnings and Precautions
Materials or chemicals required for the use of the FloodLAMP QuickColor(TM) COVID-19 Test should be closely examined by the user. The user should carefully read all warnings, instructions or Safety Data Sheets provided by the supplier and follow the general safety precautions when handling biohazards, chemicals and other materials. 

### General Precautions
* The FloodLAMP QuickColor(TM) COVID-19 Test is for *in vitro* diagnostic use (IVD) only. Rx Only.  
* For use under COVID-19 Emergency Use Authorization Only.  
* Standard precautions and procedures should be taken when handling and disposing of human samples.  
* This test has not been FDA cleared or approved; the test has been authorized by FDA under an Emergency Use Authorization (EUA) for use by laboratories certified under the Clinical Laboratory Improvement Amendments (CLIA) of 1988, 42 U.S.C. §263a, to perform high complexity tests.  
* This test has been authorized only for the detection of nucleic acid from SARS-CoV-2, not for any other viruses or pathogens.  
* This test is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of *in vitro* diagnostic tests for detection and/or diagnosis of COVID19 under Section 564(b)(1) of the Act, 21 U.S.C. § 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner.  
* Standard precautions and procedures should be taken when handling and extracting human samples.  
* Standard precautions and procedures should be taken when using laboratory equipment.  
* Standard precautions and procedures should be taken when disposing of waste.  
* Dispose of reagents according to local regulations.  
* Do not use reagents after their recommended stability time frame.  
* Ensure reagents are stored at the recommended temperatures as described below and in the vendor product information and manuals.

### Contamination Precautions
* Avoid contamination by following good laboratory practices, wearing proper personal protective equipment, segregating workflow, and decontaminating workspace appropriately.  
* Ensure that surfaces and equipment used for all test steps have been properly cleaned with 10% bleach and 70% ethanol.  
* Ensure all consumables are DNase and RNase free except for sample collection tubes which may be sterile.  
* Use only calibrated pipettes and filter tips that are sterile and PCR clean.  
* After completion of the test, dispose of the amplification reaction plates or tubes. **Do not open tubes** or remove the seals on plates after heating amplification reactions.

## Limitations
* The use of this assay as an *in vitro* diagnostic under the FDA COVID-19 Emergency Use Authorization (EUA) is limited to laboratories that are certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. § 263a, to perform high complexity tests by Rx only.   
* Use of this assay is limited to personnel who are trained in the procedure. Failure to follow these instructions may lead to erroneous results.   
* The performance of the FloodLAMP QuickColor(TM) COVID-19 Test was established using Nasopharyngeal Swab specimen type collected in saline. Nasal swabs, oropharyngeal swabs, mid-turbinate nasal swabs specimens are also considered acceptable specimen types for use with the test but performance has not been established.   
* Samples must be collected according to recommended protocols and transported and stored as described herein.  
* Samples should not be collected in UTM or VTM or Liquid Amies transport media.  
* The effect of vaccines, antiviral therapeutics, antibiotics, chemotherapeutic or immunosuppressant drugs have not been evaluated.  
* Detection of SARS-CoV-2 RNA may be affected by sample collection methods, patient factors (e.g., presence of symptoms), and/or stage of infection.  
* False-positive results may arise from various reasons, including, but not limited to the following:  
  * Contamination during specimen collection, handling, or preparation  
  * Contamination during assay preparation  
  * Incorrect sample labeling  
* False-negative results may arise from various reasons, including, but not limited to the following:  
  * Improper sample collection or storage  
  * Degradation of SARS-CoV-2 RNA  
  * Presence of inhibitory substances  
  * Use of extraction reagents or instrumentation not approved with this assay   
  * Incorrect sampling window  
  * Failure to follow instructions for use  
  * Mutations in SARS-CoV-2 target sequences  
* Nucleic acid may persist even after the virus is no longer viable.   
* This test cannot rule out diseases caused by other bacterial or viral pathogens.  
* Performance has not yet been established in asymptomatic individuals and will be established during a post-authorization study.   
* Use of the test in a general, asymptomatic population for serial screening is intended to be used as part of an infection control plan that may include additional preventative measures, such as a predefined serial testing plan or directed testing of high-risk individuals. Negative results should not be treated as definitive and do not preclude current or future infection obtained through community transmission or other exposures. Negative results must be considered in the context of an individual’s recent exposures, history, and presence of clinical signs and symptoms consistent with COVID-19.  
* This test should not be used within 30 minutes of administering nasal or throat sprays.  
* Positive results must be reported to appropriate public health authorities, following state and national guidelines.   
* The clinical performance of the test has not been established in all circulating variants, and test performance may vary depending on the prevalence of variants circulating at the time of patient testing.   
* Negative test results do not exclude possibility of exposure to or infection with SARS-CoV-2 virus. Patient handling will be directed by healthcare professionals.

## Conditions of Authorization for the Laboratory
The FloodLAMP QuickColor(TM) COVID-19 Test Letter of Authorization, along with the authorized Fact Sheet for Healthcare Providers, the authorized Fact Sheet for Patients, and authorized labeling are available on the FDA website: [https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas)

However, to assist clinical laboratories running the FloodLAMP QuickColor(TM) COVID-19 Test, the relevant Conditions of Authorization are listed below:

* Authorized laboratories1 using the FloodLAMP QuickColor(TM) COVID-19 Test will include all authorized Fact Sheets with test result reports. Under exigent circumstances, other appropriate methods for disseminating these Fact Sheets may be used, which may include mass media.  
* Authorized laboratories1 using the FloodLAMP QuickColor(TM) COVID-19 Test will use the FloodLAMP QuickColor(TM) COVID-19 Test as outlined in the FloodLAMP QuickColor(TM) COVID-19 Test Instructions for Use. Deviations from the authorized procedures, including the authorized clinical specimen types, authorized control materials, authorized other ancillary reagents and authorized materials required to perform the test are not permitted.  
* Authorized laboratories must notify the relevant public health authorities of their intent to run the test prior to initiating testing.  
* Authorized laboratories using the FloodLAMP QuickColor(TM) COVID-19 Test will have a process in place for reporting test results to healthcare providers and relevant public health authorities, as appropriate.  
* Authorized laboratories will collect information on the performance of the test and report to DMD/OHT7-OIR/OPEQ/CDRH (via email: CDRH-EUA-Reporting@fda.hhs.gov) and FloodLAMP Biotechnologies, PBC support center (via email: eua.support@floodlamp.bio) any suspected occurrence of false positive or false negative results and significant deviations from the established performance characteristics of the test of which they become aware.  
* All laboratory personnel using the test must be appropriately trained in molecular assay techniques and use appropriate laboratory and personal protective equipment when handling these test components, and use the test in accordance with the authorized labeling.  
* FloodLAMP Biotechnologies, PBC authorized distributors, and authorized laboratories using the FloodLAMP QuickColor(TM) COVID-19 Test will ensure that any records associated with this EUA are maintained until otherwise notified by FDA. Such records will be made available to FDA for inspection upon request. 


1 For ease of reference, this will refer to, “Clinical Laboratory Improvement Amendments of 1988 (CLIA), 42 U.S.C. §263a certified laboratories with FDA Emergency Use Authorization FDA for performing SARS-CoV-2 testing

## Specimen Collection and Storage
Upper respiratory specimens including nasopharyngeal swabs, anterior nasal and mid-turbinate nasal swabs should be collected using standard procedures and recommendations. Swab specimens should be collected in 0.9% saline, PBS, or dry tubes. Specimens should not be collected in UTM, VTM, or Liquid Amies.

Please refer to Interim Guidelines for Collecting, Handling, and Testing Clinical Specimens for COVID-19:  
[https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html](https://www.cdc.gov/coronavirus/2019-ncov/lab/guidelines-clinical-specimens.html)

The stability study of the nasal swab sample transported in saline has been conducted by Quantigen Biosciences, with support from The Gates Foundation and UnitedHealth Group. Quantigen Biosciences has granted a right of reference to any sponsor wishing to pursue an EUA to leverage their COVID-19 swab stability data as part of that sponsor’s EUA request.

* Samples can be stored at room temperature for 56 hours after collection prior to inactivation.   
* For longer term storage, samples can be stored at ≤-70oC.

Note: Specimens must be packaged, shipped, and transported according to the current edition of the International Air Transport Association Dangerous Goods Regulation. Follow shipping regulations for UN 3373 Biological Substance, Category B when sending potential 2019-nCoV specimens.

## Running Tests
### Reagent Preparation
The FloodLAMP QuickColor(TM) COVID-19 Test is to be used with the reagents or equivalents listed in Table 1. 

#### Table 1: Validated reagents used with Test
| Item | Concentration | Chemical Composition | Vendor | Catalog Number |
| :---- | :---: | :---- | :---- | :---- |
| TCEP | .5 M | tris(2-carboxyethyl)phosphine hydrochloride | Sigma-Aldrich Millipore Sigma | 646547-10X1ML |
| EDTA | .5 M | Ethylenediaminetetraacetic acid | Thermo Fisher | 15575020 |
| NaOH | 10 N | Sodium Hydroxide | Sigma-Aldrich | SX0607N-6 |
| Nuclease- free Water | - | Ultrapure Water, nuclease-free | Thermo Fisher | 10977015 |
| NaCl | 5M | Sodium Chloride | Thermo Fisher | 24740011 |
| Guanidine HCl | 6M | Guanidine Hydrochloride | Sigma-Aldrich | SRE0066 |
| Colorimetric LAMP MM\* | - | Colorimetric LAMP Master Mix | New England Biolabs | M1804 |
||

\* Item may not be substituted for equivalent. 

Stocks of TCEP, EDTA, NaOH, and NaCl may be prepared from powder form at the specified concentration using nuclease-free, MilliQ or equivalent molecular biology grade water.

0.9% Saline (154 mM) may be prepared by diluting 15.4 mL of 5 M NaCl in MilliQ or equivalent molecular biology grade water to a final volume of 500 mL. Equivalent preparations or commercial saline products may be utilized, with appropriate validation.

A 100X Inactivation Solution is prepared by mixing the components in Table 3 and vortexing for 30 seconds. Equivalent preparations utilizing components with different source concentrations may be used such that the final 100X Concentration is achieved. Aliquots of 100X Inactivation Solution should be stored in the dark at \-20°C for up to 3 months. Upon thaw, working aliquots of 100X Inactivation Solution should be stored in the dark at room temperature for up to 1 month. 

#### Table 3: 100X Inactivation Solution
| Component | Source Concentration | Volume | 100X Concentration |
| :---- | :---: | :---: | :---: |
| TCEP | 0.5 M | 10 mL | 250 mM |
| EDTA | 0.5 M | 4 mL | 100 mM |
| NaOH | 10 N | 2.3 mL | 1.15 N |
| Nuclease-free Water | - | 3.7 mL | - |
| **TOTAL VOLUME** | - | **20 mL** | - |

For swabs that are collected or eluted in 0.9% saline solution or equivalent, the 100X Inactivation Solution should be added at 1/100th the sample solution volume.

For dry swabs, a preparation of 1X Inactivation Saline Solution should be prepared per Table 4. 1X Inactivation Saline Solution should be kept at room temperature and used within 24 hours of preparation from components or 100X Inactivation Solution.

#### Table 4: 1X Inactivation Saline Solution
| Component | Volume |
| :---- | :---: |
| 0.9% Saline (154 mM NaCl) in MilliQ Water | 1000 mL |
| 100X Inactivation Solution | 10 mL |
| **TOTAL VOLUME** | **1010 mL** |
||

### Controls Preparation
**One positive and one negative control** will be included on every 96-well plate with up to 94 samples, or with every batch of strip tubes on each heater:

1) A “no template” (negative) control (NTC) is needed to **assure the absence of cross contamination from positive samples, positive controls, or amplicons** and is used **to determine if sample results are valid.** **It consists of 100X Inactivation Solution diluted to 1X in 0.9% saline. This NTC is the same solution added to dry swabs (see Table 3 and Table 4 above for the components).**  
     
2) A positive template control is needed to **assure proper functioning of reagents and the absence of significant RNAse contamination. It consists of synthetic viral RNA at a concentration of approximately 100,000 cp/mL diluted in total human RNA and nuclease-free water.** Stock and working aliquots of the positive control are produced from the sources listed in Table 5 or equivalents. Working aliquots should be diluted prior to use to 100,000 cp/mL. Positive control aliquots should be stored for at most 3 months at \-80°C, or at most 1 month at \-20°C.   
   
#### Table 5: Components for Positive Template Control
| Material | Vendor | Catalog \# | Volume |
| ----- | :---: | :---: | :---: |
| SARS-CoV2 Positive Control RNA | Twist | 102019 | 5 µL |
| Total Human RNA | Thermo Fisher | 4307281 | 100 µL |
| Nuclease-free Water | Thermo Fisher | 10977015 | 4,895 µL |
||

### 10X LAMP Primer Mix Preparation
The FloodLAMP QuickColor(TM) COVID-19 Test uses 18 LAMP primers targeted for 3 different SARS-CoV-2 genes, with 6 primers for each target. Primer names and sequences are shown above in Table 2. All 18 primers are mixed together and input into a single amplification reaction. 

Primers may be purchased from the vendor LGC Biosearch Technologies as 3 pre-blended sets, or the primers may be purchased as 18 individual custom oligos. Table 6 below lists the primer products to be ordered.   
   
The LGC Biosearch primer products are provided already blended for each target (6 primers per tube) and dried such that upon resuspension with 1 mL of nuclease-free water, the primers for each target are at 30X concentration. One resuspended tube for each of the 3 targets (i.e. primer blends) are mixed together to yield a 3 mL total volume that contains all individual primers at 10X concentration. This 3 mL of 10X LAMP Primer Mix provides for 1,200 reactions at 2.5 µL per reaction.  
   
Alternatively to the pre-blended LGC Biosearch products, primers may be purchased as individual custom oligos. Custom oligos may be blended to form 30X Primer Set Mixes as intermediates or all mixed together for the 10X LAMP Primer Mix. The FIP and BIP primers for each target require purification by HPLC or an equivalent process. Appropriate validation of primer mixes from custom oligos is required. Primers may be stored at 4°C for up to one month, or at \-20°C for up to 1 year.

#### Table 6: 10X LAMP Primer Mix Components
| Vendor | Item | Catalog number | Quantity | # Reactions |
|--------|------|----------------|-----------|-------------|
| Order one of the following primer sets |||||
| LGC Biosearch Technologies | SARS-CoV-2 LAMP ASIe 6 primer set at 30X (ORF1ab gene) | LAMP_S2-ASIe-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP ASIe 6 primer set at 30X (ORF1ab gene) | LAMP_S2-ASIe-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP N2 6 primer set at 30X (N gene) | LAMP_S2-N2-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-48 | 6-48 nmol | 1,200 |
| LGC Biosearch Technologies | SARS-CoV-2 LAMP E1 6 primer set at 30X (E gene) | LAMP_S2-E1-480 | 60-480 nmol | 12,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | Orf1ab_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | N2_LB | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_FIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_BIP | Custom Order | 1,000 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_F3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_B3 | Custom Order | 125 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LF | Custom Order | 250 nmol | 25,000 |
| LGC Biosearch Technologies, Eurofins Genomics, Integrated DNA Technologies, Sigma | E1_LB | Custom Order | 250 nmol | 25,000 |
||

### Sample Preparation
\* For wet swab specimens (swabs in saline or unprocessed swab elution): 

1) If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.   
2) Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.   
3) Wipe the outside of the sample tube with 70% ethanol. 

For dry swab specimens:
1) Wipe the outside of the sample tube with 70% ethanol. 

### Sample Inactivation
1) Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and set the temperature to hold at 100 °C.  
2) \* For wet swab specimens: transfer 1 mL or available volume of each sample to an appropriately labeled 1.5 mL or 5mL tube and securely cap.   
3) \* For wet swab specimens: add 10μL per 1 mL sample volume of 100X Inactivation Solution to each sample tube.  
4) For dry swab specimens (DO NOT DO FOR WET SWAB SPECIMENS): add 1 mL of 1X Inactivation Solution to each sample tube.  
5) Vortex for 30 seconds.  
6) Place sample tubes into the inactivation heater for 8 minutes.  
7) Remove sample tubes from the inactivation heater and let cool at room temperature for 10 minutes.  
8) Place sample tubes on ice, in the refrigerator, or on a cold block at 4°C until ready to perform amplification reaction. 

Note: Testing of inactivated specimens must be conducted the same day inactivation is performed. For long term storage, keep the original specimen at ≤-70°C. 

### Colorimetric LAMP Amplification Reaction Preparation
1) Place a 96-well PCR plate or PCR strip tubes onto a cold block or ice.  
2) Thaw frozen reagents until ice crystals are not present.   
3) Pulse vortex thawed reagents and briefly spin down in a centrifuge.   
4) Store on ice, in the refrigerator, or on a cold block at 4°C until ready to use.  
5) Combine components of Primer-Guanidine Solution per volumes listed in Table 7, or proportionally scaled for the number of reactions to be run. 

      NOTE: Component volumes should be scaled proportionally for the number of reactions.   
      NOTE: The Primer-Guanidine Solution may be prepared in advance and stored at \-20°C    
      for up to 1 month.

6) Pulse vortex and briefly spin down in a centrifuge.   
7) Prepare the Colorimetric LAMP Amplification Reaction Mix by adding the Colorimetric LAMP MM to the Primer-Guanidine Solution per the volumes listed in Table 8.   
8) Vortex the Colorimetric LAMP Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
9) Add 23 µL of the Colorimetric LAMP Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

NOTE: Reaction plates/strip tubes comprising the Colorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at \-20°C for up to 3 days prior to addition of the sample. A heated plate sealer may be used to seal plates. Alternatively, a manually applied foil or optical seal may be used.

#### Table 7: Primer-Guanidine Solution
| Component | Volume (1 reaction) | Volume (1 reaction x 100) 1 x 96-plate w/ 4% overage |
| ----- | :---: | :---: |
| 10X LAMP Primer Mix | 2.5 µL | 250 µL |
| Guanidine HCl (400 mM) | 2.5 µL | - |
| Guanidine HCl (6 M) | - | 16.7 µL |
| Nuclease-free Water | 5.5 µL | 783 µL |
| **TOTAL VOLUME** | **10.5 µL** | **1050 µL** |
||

#### Table 8: Colorimetric LAMP Amplification Reaction
| Component | Volume (1 reaction) | Volume (100 reactions) |
| ----- | :---: | :---: |
| Primer-Guanidine Solution | 10.5 µL | 1050 µL |
| Colorimetric LAMP MM | 12.5 µL | 1250 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **2300 µL** |
| Sample | 2 µL | - |
| **REACTION VOLUME** | **25 µL** | - |
||

### Sample Addition and Heating
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Turn on the amplification heater (a thermal cycler, water bath, dry heat bath or equivalent) and set the temperature to hold at 65°C.

NOTE: Amplification heater should be located in a separate, dedicated BSC or area of the lab. Proper cross contamination prevention practices are required, such as glove changes, to prevent amplicon contamination.

2) Add 2 μL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
3) Mix by pipetting.  
4) If using PCR plate, seal with foil seal, optical seal (optionally using heat sealer). If using PCR strip tubes, cap strips.  
5) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
6) Place the plate or strip tubes in the heater and set timer for 25 minutes (do not use heated lid).  
7) Remove the plate or strip tubes from the heater after 25 minutes.  
8) Let cool for 1 minute and then interpret the test results.

### Test Controls
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. An example of the expected appearance of the negative and positive controls after amplification is shown in Figure 1.

**![][image1]![][image2]**

#### Figure 1. Negative control (left) and positive control (right) after amplification.

If the negative and positive controls do not appear as expected, the specimen results of the corresponding plate or batch should be considered invalid. In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and optionally RNAseZAP product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

### Patient Specimen Results Interpretation
NOTE: Patient specimen results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Test results should be read at least 1 minute and no more than 8 hours after plates or tubes have been removed from heat. Test results may be determined directly from visual inspection of the color of the reaction tubes or from photographs: 

* yellow \- result is positive  
* bright pink or red \- result is negative  
* any other color \- result is inconclusive. 

Examples are shown below in Figure 2. Edge cases for positive and negative results are shown below in Figure 3. Any color variance stronger than the edge cases should be interpreted as inconclusive. In order to reduce the chance of both false negative and false positive results, this window for color variance is intentionally set to be small.

If the initial test is inconclusive, then one of the following should be performed:  
1) repeat the Colorimetric LAMP Amplification Reaction on the inactivated samplein triplicate. Results of the repeat tests are to be interpreted according to Table 9 below.

#### Table 9: Initial Inconclusive Repeat Results Interpretation
| Repeat Triplicate Results | Final Sample Result Reported |
| :---: | :---: |
| 3 Positive | Positive |
| 2 Positive, 1 Inconclusive | Positive |
| 1 Positive, 2 Inconclusive | Inconclusive |
| 3 Negative | Negative |
| Any other results | Inconclusive |
||

2) follow-up test the inactivated sample with the FloodLAMP EasyPCR(TM) COVID-19 Test or another high sensitivity EUA authorized test that comprises the same inactivation protocol. The final interpretation is the result of the follow-up test.

For serial screening of individuals without symptoms or other epidemiological reasons to suspect COVID-19 infection, the initial inconclusive test result may be considered the final interpretation.

If the final interpretation of the test result is inconclusive, then "Inconclusive" should be reported and retesting of the individual is recommended. 

| ![][image3] |                  ![][image4]![][image5] |
| :---- | :---- |
| **Figure 2. Example of Test Results  (Left 2 Negative, Right 2 Positive)** |                         **Figure 3. Edge Case Test Results                          (Left Negative, Right Positive)** |

## Performance Evaluation
### Analytical Sensitivity: Limit of Detection (LoD)
The Limit of Detection (LoD) for the FloodLAMP QuickColor(TM) COVID-19 Test was established using gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) spiked into negative real specimens. The negative specimens were confirmed by PCR using the CDC primers. The gamma-irradiated virus was spiked into the specimen prior to the heat inactivation step, and carried through the entire assay. The concentration of spike was such that the contrived positive sample was at 100,000 copies/mL after the inactivation step. The stock contrived positive was diluted into inactivated negative sample matrix to produce the concentrations for the LoD study. A preliminary LoD run was performed using the concentrations ranging from 100,000 copies/mL to 3,100 copies/mL. Concentrations of 12,500 and 6,250 were selected for confirmatory LoD runs. LoD run details are provided in Supporting Data, with the results summarized below in Table 10. The LoD, defined as the concentration at which at least 95% of the samples are positive, was determined at 12,500 copies/mL.

#### Table 10: LoD Confirmatory Data Results
| Concentration of Contrived Positive Sample  | Replicates Detected |
| :---: | :---: |
| 12,500 copies/mL | 95% (20/21) |
| 6,250 copies/mL | 52% (11/21) |
||

### Analytical Sensitivity: Inclusivity (*in silico*)
An inclusivity study was conducted for the ORF1ab, N2, and E1 primer sets against all complete, high coverage SARS-CoV-2 sequences deposited at GISAID as of February 27, 2021. Table 11 summarizes the results of this *in silico* inclusivity analysis. A total of 498,224 sequences were considered. There are 10 sequence isolates that have 1mm to both As1e and E1 and had N2 excluded due to greater than 15 N's, with the other 498,214 sequence isolates all have at least 1 target region that is a complete match.

Each primer set matched at 100% similarity against the SARS-CoV-2 RefSeq reference genome (Wuhan-Hu-1; NC\_045512.1). All three primer sets differed by one or fewer mutations for 99.7% of GISAID sequences, indicating nominal primer hybridization for all SARS-CoV-2 variants under consideration.	

#### Table 11: *In Silico* Inclusivity Analysis for LAMP Primers
| Primer | AS1e  (ORF1ab gene) |  | N2  (N gene) |  | E1  (E gene) |  |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Total Primer Length** | 195 |  | 169 |  | 168 |  |
| **Total \# of Strains Evaluated** | 498,224 |  | 498,224 |  | 498,224 |  |
| **100% Match** | 474,717 | 95.3% | 479,548 | 96.3% | 462,538 | 92.8% |
| **1 Mismatch** | 19,301 | 3.9% | 15,698 | 3.2% | 30,626 | 6.1% |
| **2 Mismatches** | 338 | 0.1% | 161 | 0.0% | 1,455 | 0.3% |
| **3 Mismatches** | 9 | 0.0% | 5 | 0.0% | 103 | 0.0% |
| **\> 3 Mismatches** | 0 | 0.0% | 0 | 0.0% | 1 | 0.0% |
| **Total Strains Removed** | 3,859 | 0.8% | 2,812 | 0.6% | 3,501 | 0.7% |
||

### Evaluation of Impact of Viral Mutations
The As1e, E1 and N2 primer regions of all SARS-CoV-2 genomes present in GISAID as of 2/26/2021 were evaluated to assess the potential impact of genomic variants on LAMP primer binding. This analysis was performed with the Primer Monitoring Tool from New England Biolabs ([primer-monitor.neb.com](http://primer-monitor.neb.com)), which continually monitors registered primer sets for overlapping variants in sequences from GISAID. Results are summarized by region and locus below in Table 12, including the 30 countries with most sequences in GISAID. Sequences were aligned to the SARS-CoV-2 reference sequence (NC\_045512.2) using minimap2 (minimap2 \-t 16 \-x asm5 \-a). Variant sites (excluding Ns) were identified using samtools mpileup and summarized by region and genome position. Genomic positions having \>= 40 global variant observations are shown (column labels). When present, box labels indicate the fraction of variants observed at a given locus.

The aggregate of current published mutations is not expected to reduce performance of the FloodLAMP QuickColor(TM) COVID-19 Test by more than 5% from that established by the performance evaluation in this EUA submission. Further, the use of 3 primer sets targeting different regions in the SARS-CoV-2 genome should make the test robust to new genetic variants.

#### Table 12: Variant Analysis of LAMP Primers
![][image6]  
![][image7]

## Analytical Specificity: Cross-Reactivity (*in silico*) {#analytical-specificity:-cross-reactivity-(in-silico)}

*In silico* cross-reactivity analysis was performed by aligning the primer sequences of the FloodLAMP QuickColor(TM) COVID-19 Test against sequences of other coronaviruses and common respiratory flora using the BLASTn alignment tool from NCBI. Results of this analysis are presented in Tables 13A, 13B, and 13C. 

The % identity range (\# identical bases/ \# primer bases) is shown for each primer and organism. Darker font indicates % identity greater than 80%. Organisms with \>= 50% identity primer hits are shown. This analysis is not intended to predict amplification. Near perfect homology across B3, F3, FIP and BIP is necessary to support successful amplification. With the exception of SARS-CoV, simultaneous homologies do not occur between any of the primers and microorganisms screened. With respect to clinical relevance of the *in silico* cross-reactivity analysis, there are no known circulating strains of SARS-CoV circulating in humans, thus the overall probability for the test to produce a cross-reactive signal is negligible.

#### Table 13A: *In Silico* Cross-Reactivity Analysis for AS1e Primers

![][image8]

#### Table 13B: In Silico Cross-Reactivity Analysis for N2 Primers

![][image9]

#### Table 13C: *In Silico* Cross-Reactivity Analysis for E1 Primers

![][image10]

### Analytical Specificity: Cross-Reactivity (*wet testing*)
Wet testing was performed to demonstrate that the FloodLAMP QuickColor(TM) COVID-19 Test does not react with related pathogens, high prevalence disease agents and normal or pathogenic flora that are reasonably likely to be encountered in a clinical specimen.  SARS-CoV, RSV, Flu, Human Metapneumovirus. and Streptococcus Salivarius were tested for potential cross-reactivity, as shown in Table 14. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and cross-reactivity organisms were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All wet testing showed no cross-reactivity with the viral pathogens and common respiratory flora, as shown in Table 14.

#### Table 14: Wet Testing Cross-Reactivity Results
| Organism | Description | BEI Number | Detected Replicates |
| ----- | ----- | :---: | :---: |
| SARS-CoV | UV-inactivated virus | NR-3882 | 0/3 |
| Human Metapneumovirus | Genomic RNA | NR-49122 | 0/3 |
| RSV | Genomic RNA | NR-43976 | 0/3 |
| Influenza B | Genomic RNA | NR-45848 | 0/3 |
| Streptococcus salivarius | Bacterial cell culture | HM-121 | 0/3 |
||

### Analytical Specificity: Interfering Substances
Exogenous and endogenous substances were tested for potential interference with the FloodLAMP QuickColor(TM) COVID-19 Test. Gamma-irradiated SARS-CoV-2 virus cell lysate (BEI NR-52287) was spiked onto dried AN swab specimens to produce contrived Positve Controls. Negative Control dried swabs obtained simultaneously were confirmed to be SARS-CoV-2 negative by PCR using the CDC primers. The gamma-irradiated SARS-CoV-2 virus and interfering substances were spiked into the dried swabs prior to the heat inactivation step, and carried through the full test protocol. 

All interfering substance testing showed no disagreement with expected positive and negative results, as shown in Table 15 and Supporting Data.

#### Table 15: Interfering Substances Results
| Interfering Substance | Active Ingredient | Concentration | % Agreement with Expected Results |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  | **Positive Control Spiked** | **Negative Control Unspiked** |
| Blood | N/A | 1% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Congestion Spray | Acetaminophen, Guaifenesin, Phenylephrine HCI | 20% v/v | 100% (3/3) | 100% (3/3) |
| Nasal Allergy Spray | Oxymetazoline HCl | 15% v/v | 100% (3/3) | 100% (3/3) |
| Lozenges | Menthol | 10% w/v | 100% (3/3) | 100% (3/3) |
| Mucin | N/A | 0.5% w/v | 100% (3/3) | 100% (3/3) |
||

## Clinical Evaluation
The clinical evaluation of the FloodLAMP QuickColor(TM) COVID-19 Test utilized confirmed clinical anterior nares swab specimens. 40 positive and 40 negative clinical specimens were evaluated and compared to a high sensitivity EUA authorized test run on the original fresh samples. The FloodLAMP QuickColor(TM) COVID-19 Test showed a positive agreement of 90% and a negative agreement of 100%. The 4 false negative results were specimens with high Ct values as previously measured by the comparator test, indicating low viral load. A summary of the clinical performance is below in Table 16. 

#### Table 16: Clinical Evaluation Results
| FloodLAMP QuickColor(TM) COVID-19 Test Results | Comparator \- High Sensitivity EUA Authorized Test |  |  |
| :---: | :---: | :---: | :---: |
|  | **Positive** | **Negative** | **Total** |
| Positive | 36 | 0 | 36 |
| Negative | 4 | 40 | 44 |
| Total | 40 | 40 | 80 |
| Positive Agreement | 90.0% (36/40) 95% CI: 76.3% to 97.2% |  |  |
| Negative Agreement | 100% (40/40) 95% CI: 91.2% to 100% |  |  |

## Support
FloodLAMP Biotechnologies, PBC support center   
eua.support@floodlamp.bio  
650-394-5233

# ===== END OF FILE _archive-combined-files_fl-fda-submissions_153k.md =====
