METADATA
last updated: 2026-02-28 RT initial creation
file_name: _AI_digestion_irb_new-clinical-study-design.md
file_date: 2026-02-28
title: FloodLAMP Integrated Clinical Study Design - Digestion
category: regulatory
subcategory: irb
tags: clinical-study, enrichment, surveillance, EUA, study-design, cascading-cohort
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1kqmFPWjNB7852XZaWs6_SLLt8bdfjE6GSPTmeDcsqBo
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/regulatory/irb/_AI_digestion_irb_new-clinical-study-design_FULL.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 6018
words: 4378
notes: Created by Claude Opus 4.6 Max during archive preparation. **NOT HUMAN VERIFIED - MAY CONTAIN ERRORS** Digestion and analysis of FloodLAMP's integrated clinical study design (~May-August 2022), synthesized from planning notes with whiteboard diagram, associated slide deck/GDoc content, and the original IRB protocol (Protocol 20210401).
summary_short: Digestion of FloodLAMP's integrated clinical study design (~May-August 2022) that merged an active school-based surveillance program with a clinical trial for generating EUA submission data. Covers the enrichment strategy using school exposures and surveillance-detected positives, a cascading cohort structure for maximizing positive specimen yield, comparator testing efficiency, multi-assay validation design, and RNAseP cross-validation, with both internal and external-facing analyses.


CONTENT

## Prompt (Verbatim)
Review the following file and summarize the proposal and try to identify the key reasons for this. This was a new clinical study design that I was trying to figure out and I had an image of it. There, you know, it's not like a single, I don't think it's, I think it's a couple collected kind of associated ideas. But I feel like there's something really important here. I remember thinking this was important and like working on kind of writing it up. I even made a slide deck and it revolved around sort of an integrated, you know, integrating a, like a surveillance program with, doing a clinical study and I think there was like a more comprehensive version of it and a less comprehensive. I'm not really sure. So I want you to kind of summarize, digest, really kind of do a thorough job figuring out what the ideas were, both from the image and from the text and then create a digestion, create the digestion both for me and then also for an external audience, you know, and assume that the external audience is familiar with, you know, diagnostic testing, clinical study designs for testing, etc. So you don't really have to give a background there and just, you know, get to the meat and the key, the key design and ideas behind it. I'm including a project description and a tone here. And you know what? I'm also gonna go ahead and include our IRB. Because that can be some good background info. Okay, do it.

**Files included in context window:**
- _notes_irb_new-clinical-study-design.md
- [hand-drawn whiteboard diagram]
- project-description.md
- tone.md
- IRB - FloodLAMP COVID-19 Biobank and Test Validation Protocol 20210401 v01.md


## Prompt (Cleaned)
Review the following file and summarize the proposal, identifying the key reasons behind it. This was a new clinical study design that I was working on, and I had an image of it. It's not a single idea -- I think it's a collection of associated ideas. I feel like there's something really important here. I remember thinking this was important and working on writing it up. I even made a slide deck, and it revolved around integrating a surveillance program with a clinical study. I think there was a more comprehensive version and a less comprehensive one, but I'm not sure.

Summarize, digest, and do a thorough job figuring out what the ideas were, both from the image and from the text. Create the digestion both for me and for an external audience. Assume the external audience is familiar with diagnostic testing and clinical study designs for testing, so you don't need to provide background -- just get to the key design and ideas behind it.

I'm including a project description and a tone guide. I'm also including our IRB protocol for background context.

**Files included in context window:**
- _notes_irb_new-clinical-study-design.md
- [hand-drawn whiteboard diagram]
- project-description.md
- tone.md
- IRB - FloodLAMP COVID-19 Biobank and Test Validation Protocol 20210401 v01.md


## AI Response - Digestion: FloodLAMP Integrated Clinical Study Design (May 2022)
Done. I created the digestion at `data/floodlamp/regulatory/irb/_digestion_irb_new-clinical-study-design.md` with both an internal and external section.

Here's my read on what was really going on and why it felt important:

**The central idea** was not just a clinical study design but an operational architecture that merged a surveillance program with a clinical trial. Instead of treating these as separate activities (run surveillance over here, run a clinical study over there), the design recognized that a well-structured surveillance program *already contains* most of what you need for a clinical study: consented participants, collection logistics, ongoing testing, and a population with real exposure risk. The study just added the comparator testing, randomization, and formal follow-up protocols on top.

**The enrichment strategy** was the practical engine. Low prevalence was the killer problem for small companies trying to generate clinical data. Instead of brute-force enrolling thousands of people hoping for 20 positives, the design used school exposure events and surveillance-detected positives as triggers to activate intensive serial testing of households. This is much more efficient and avoids the bias concern of re-testing already-confirmed positives from other tests.

**The cascading cohort structure** was the really clever part. One positive pool in a household cascades into daily paired testing of the whole family, catching new infections at onset. Each new positive restarts the cycle. This multiplied the positive specimen yield from each initial detection event, all with properly paired comparator data.

**The RNAseP angle from the whiteboard** adds another layer: by running both FloodLAMP EasyPCR and the Eurofins comparator across large sample sets, you could cross-validate that FloodLAMP's internal sample adequacy control (RNAseP) was reliable. This would strengthen the home collection usability story (proving people collected their swabs properly) and the overall analytical validation.

**The bottom line**: this was a resource-efficient design for a small company that turned the constraint of limited resources into an advantage by making the surveillance program and the clinical study the same thing, with an enrichment strategy that solved the prevalence problem and a cascading cohort structure that maximized data yield per positive event.


### Internal Summary (For the Author)
#### What This Was
This was a clinical study design developed around May-August 2022 to solve several interrelated problems simultaneously. It represented an evolution from the broad, flexible original IRB protocol (which allowed up to 100,000 specimens across multiple collection modes) into a specific, operationally integrated plan. There was a slide deck and at least one detailed planning document associated with it.

#### The Core Insight
The central idea was to merge an active school-based surveillance testing program with a clinical study, so that the surveillance infrastructure (logistics, population, ongoing testing) would serve double duty as the apparatus for generating clinical performance data for EUA submission. Rather than running a standalone clinical trial that required building recruitment, collection, and testing from scratch, the study would ride on top of existing surveillance operations.

This had two major advantages:
1. It solved the recruitment and logistics problem by using an already-running program.
2. It provided direct value to study participants (testing that helped stop spread in classrooms and families), making this genuinely participant-beneficial rather than purely extractive research.

#### The Enrichment Strategy
Low prevalence was the fundamental obstacle to getting enough positive samples. The design addressed this through two enrichment approaches:

1. **Outbreak chasing**: When a school exposure event occurred, recruit the affected families for serial testing. Send collection kits home with the exposed student the same day if possible; collect swabs the next morning and courier them to the lab within hours.

2. **Surveillance-based enrichment**: Pre-recruit families into the study through the surveillance program. When a routine surveillance test came back positive, those families would be activated into the study's formal protocol arms. This was the more systematic, ongoing version.

Both approaches increased the effective positive rate without introducing the kind of bias that would come from, say, only enrolling people who already tested positive elsewhere (which the notes flagged as a concern: "Could/should we ignore how they tested positive? FDA might ding us for bias").

#### The Cascading Cohort Structure
This is where the design got particularly clever. Rather than a single - timepoint collection, it used a cascading structure that multiplied the data yield:

- **Initial Collection**: Pooled family swabs for FloodLAMP + individual comparator swabs. Run QuickColor immediately.
- **Pool Positive path**: Send individual comparator swabs to CLIA lab. Run EasyPCR. Move the family into the Positive Follow Up Cohort.
- **Positive Follow Up Cohort**: The family collects paired individual swabs daily (FloodLAMP + comparator). Also run rapid antigen tests. The logic: other family members were likely exposed and may be developing infections, so continued testing catches new positives as they emerge.
- **Serial Follow Up Cohort**: Willing participants continue daily paired testing. If a new FloodLAMP positive appears, restart the Positive Follow Up protocol for that person.

The net effect: a single initial positive in a household pool could cascade into multiple confirmed positives across family members, each with paired FloodLAMP/comparator data.

#### Cost Optimization
A key practical feature: the expensive comparator PCR did not need to be run on every negative sample. All FloodLAMP-positive pools needed comparator PCR run (to confirm/disconfirm), but for negatives, only a subset (at least 20) required comparator testing. This meant the surveillance testing could scale broadly while keeping comparator costs manageable. The notes mention this as funding-dependent: "Depending on funding we can run larger negative arms that include the comparator PCR, which give greater statistical power."

#### Diagram of Clinical Study Design Ideas
_made with Claude desktop from hand drawn image_
![Clinical Study Workflow - Sample Processing & Validation Pipeline](_clin-study-diagram.png)

Interactive HTML diagram showing the four sample processing paths in the integrated clinical study design: (A) Elute in Saline, where pooled swabs are split, with half sent to Eurofins as comparator and half through 100x inactivation; (B) 1x ISS, where the inactivated half is combined with 1x ISS and run on both FloodLAMP QuickColor LAMP and EasyPCR; (C) Comparator, where multiple individual swabs are sent to Eurofins; and (D) Enrichment, where enriched individual swabs are run directly on FloodLAMP QC and EasyPCR. Both EasyPCR outputs feed into a cross-validation of RNAseP signal over large sample sets. Based on a hand-drawn whiteboard sketch from the original planning sessions.

#### The Whiteboard Sketch
The whiteboard image shows three tiers of the study:

**Top tier (Main pooled arm)**: Multiple swabs pooled in saline (1X ISS), then split. Half goes to Eurofins (external CLIA lab) as comparator. The other half goes through 100X inactivation, then runs on both FLQC (FloodLAMP QuickColor LAMP) and FLEPCR (FloodLAMP EasyPCR). A key annotation: the Eurofins comparator PCR "Validates RNAseP Signal from our PCR," meaning the external reference data could be used to validate FloodLAMP's internal sample adequacy control (RNAseP) across a large population.

**Middle tier (Individual comparator arm)**: Individual swabs sent to Eurofins, with the specific goal to "Compare RNAseP over big sample sets." This appears to be a dedicated arm for building a large dataset correlating FloodLAMP's RNAseP internal control with the external reference, a useful dataset for demonstrating sample collection and processing quality.

**Bottom tier (Enrichment arm)**: Individual swabs from the enrichment strategy run directly on FloodLAMP QC (QuickColor) and EP (EasyPCR). This is the streamlined path for enriched samples where the focus is on FloodLAMP performance data.

#### What It Was Simultaneously Validating
The study was designed to generate clinical data for multiple claims in a single integrated effort:
1. QuickColor (RT-LAMP) performance
2. EasyPCR (RT-qPCR) performance
3. Pooled vs. individual collection performance
4. Home collection kit usability (with and without the FloodLAMP Mobile App)
5. Asymptomatic testing claim (tests run under moderate complexity)

#### The RNAseP Angle
The whiteboard repeatedly emphasizes RNAseP validation. RNAseP is a human housekeeping gene used as an internal control to confirm that a collected swab actually contains sufficient human cellular material (i.e., the swab was properly collected and processed). By running both FloodLAMP EasyPCR (which detects RNAseP) and the Eurofins comparator across large sample sets, FloodLAMP could validate that its RNAseP signal was a reliable indicator of sample adequacy. This matters for both regulatory submissions and for the usability study (the mobile app arm), where RNAseP signal strength could be used to objectively assess whether participants collected their swabs correctly.

#### Practical Status and Constraints
The August 2022 planning notes show this was being scoped to a single Miami site (Embassy or Nova Southeastern), with one operator (FloodLAMP trained staff member who ran Combate program) running FloodLAMP tests and coordinating the PCR comparator. The comparator was the Abbott M2000 system ($85/test, same-day results but no Ct values). There were open questions about whether EasyPCR could be run at the same site or would need a collaborator (James Roach at Cleveland Clinic Ft. Lauderdale or Mayo). The design acknowledged it could expand to 3 sites for 510K requirements.

#### Why This Felt Important
Looking at it in hindsight, the design's significance was in recognizing that for a small company with limited resources, the path to clinical data did not have to be a traditional standalone trial. By structuring a surveillance program so that it inherently generated clinical-grade data, with proper consent, comparator testing, and enrichment, the company could build toward both EUA submission and a much larger publication-quality dataset using essentially the same operational apparatus. The cascading cohort structure was an efficient way to extract maximum clinical data from a low-prevalence environment. And the RNAseP cross-validation was a genuinely useful secondary dataset that could strengthen both the usability claim and the overall analytical validation story.


### External Digestion (For Audience Familiar with Diagnostic Clinical Study Design)
#### Overview
This document describes a clinical study design developed by FloodLAMP Biotechnologies in mid-2022 for generating clinical performance data for multiple molecular COVID-19 assays (an RT-LAMP test called QuickColor and an RT-qPCR test called EasyPCR), a pooled home collection kit, and an associated mobile application. The design aimed to satisfy EUA submission data requirements while simultaneously establishing infrastructure for a larger dataset suitable for publication and 510(k) submission.

#### Design Rationale
The fundamental challenge was generating sufficient positive clinical specimens during a period of variable and often low SARS-CoV-2 prevalence, using the resources of a small company. The design addressed this by integrating the clinical study into an existing school-based surveillance testing program rather than operating a standalone trial.

#### Integrated Surveillance-Clinical Study Model
The study operated within the framework of an active surveillance program providing serial screening to school populations and their families. This integration served three purposes:

1. **Recruitment pipeline**: Families already participating in surveillance were pre-consented for study participation, eliminating the need for separate recruitment infrastructure.
2. **Enrichment mechanism**: Surveillance testing identified positive individuals and exposure events in real time, enabling targeted activation of clinical study protocols for participants most likely to yield positive specimens.
3. **Participant benefit**: The study provided actionable testing results that helped interrupt transmission within classrooms and households, aligning participant and study interests.

#### Enrichment Strategy
Two enrichment approaches were employed:

- **Exposure-based**: Following a confirmed school exposure event, families of exposed students were recruited for serial testing. Collection kits were distributed same-day when possible, with morning collection and same-day courier to the lab.
- **Surveillance-based**: Families pre-enrolled in the study were activated into the formal clinical protocol when their routine surveillance test returned positive.

Both approaches increased the effective positive specimen rate without selecting for individuals with known positive results from external tests, which would risk introducing ascertainment bias.

#### Cascading Cohort Structure
The study used a multi-stage cohort design that maximized data yield from each positive finding:

1. **Initial Collection**: Participants collected paired specimens: pooled anterior nares swabs for FloodLAMP testing and individual swabs for comparator PCR (high-sensitivity EUA-authorized test at a CLIA lab). Collection order was randomized. QuickColor LAMP was run immediately on the pooled specimen.

2. **Pool Positive Pathway**: If QuickColor detected a positive pool, individual comparator swabs were sent to a CLIA lab (fulfilling the pooled test study arm). FloodLAMP EasyPCR was also run on the same specimen. The family was enrolled in the Positive Follow Up Cohort.

3. **Positive Follow Up Cohort**: All household members collected daily paired individual swabs (FloodLAMP + comparator) plus rapid antigen tests. The rationale: household contacts of newly identified positive individuals were at elevated risk of developing infection, and serial daily testing provided the opportunity to capture new infections at onset, generating additional paired positive specimens with both FloodLAMP and comparator data.

4. **Serial Follow Up Cohort**: Willing participants continued daily paired testing beyond the initial follow-up period. Any new FloodLAMP-positive result restarted the Positive Follow Up protocol for that individual.

This cascading structure meant a single initial positive pool could generate multiple confirmed positive specimens across household members, each with paired investigational and comparator test results.

#### Comparator Testing Efficiency
The design incorporated a cost-optimization: comparator PCR was run on all FloodLAMP-positive specimens but only a defined subset of negatives (minimum 20 for the primary analysis). This allowed surveillance-scale testing volumes without proportional comparator testing costs, while still generating sufficient negative agreement data.

#### Multi-Assay, Multi-Claim Validation
The integrated design simultaneously generated clinical performance data for:
- QuickColor (RT-LAMP) sensitivity and specificity, pooled and individual specimens
- EasyPCR (RT-qPCR) sensitivity and specificity
- Pooled vs. individual collection concordance
- Home collection kit usability (two arms: with and without FloodLAMP Mobile App, assessed via survey, video-recorded collection, and RNAseP-based sample adequacy analysis)
- Asymptomatic screening claim (tests performed under moderate complexity)

#### RNAseP Cross-Validation
A secondary objective involved correlating the RNAseP (human internal control) signal from FloodLAMP EasyPCR against the external comparator across large sample sets. This served dual purposes: validating FloodLAMP's internal sample adequacy metric and providing objective data on self-collection quality, relevant to both the usability study arm and the home collection kit submission.

#### Operational Parameters
The study was planned for a single initial site in the Miami area, with the possibility of expanding to three sites for 510(k) geographic diversity requirements. The comparator assay was the Abbott M2000 real-time PCR system run through a local CLIA lab. The minimum target was 20 prospectively collected positive and 20 negative specimens for the primary EUA analysis, with the surveillance infrastructure positioned to generate a substantially larger dataset over time.

#### Relationship to Prior Protocol
This design operationalized a broader IRB-approved protocol (Protocol 20210401, April 2021) that permitted collection of up to 100,000 specimens across multiple collection modalities. The earlier protocol established the regulatory framework; this design specified how that framework would be executed in practice through integration with surveillance operations.


## Slides - FloodLAMP Clinical Study Design - May 2022
https://docs.google.com/presentation/d/1U6NCayI6slDDV36jrq98A4ScT3X0KzNlIy0CIp348KM

### FloodLAMP Integrated Clinical Study
1) Pooled self collection with the FloodLAMP Pooled Home Collection Kit DTC
2) Tests run under moderate complexity for asymptomatic claim
  - QuickColor
  - EasyPCR
  - Pooled and individual test
3) Usability study of the FloodLAMP Mobile App

The goals of this clinical study are both to obtain the minimum necessary clinical data for EUA submission, as well as put in place the apparatus to obtain a much larger clinical data set, both for publication and for 510K. An enrichment strategy utilizes 1) school exposures, and 2) routine surveillance testing. In both, the clinical study offers value to the participants in providing testing to stop spread within classrooms and families.

### Recruitment
Recruit families for serial testing after school exposure.
Distribute collection materials for FL (pooled and indiv) and comp PCR (likely wet AN swab, pref saline).
if possible send collection kits home with student same day
next morning collection, likely send courier same day (within a few hours)
	
Also run surveillance serial screening program, where families are pre-recruited into the study. For this arm, we use an enrichment strategy where we place families into the study if their surveillance test is positive.

### Initial Collection
Have participants collect 2 swabs shortly after notification of exposure
FloodLAMP is pooled AN swabs (our collection kit)
Comparator PCR is individual AN swab (their collection kit, saline/PBS)
Run FloodLAMP QuickColor immediately


## GDoc - Clinical Study Plan May22 - NEEDS REVIEW AND CLEANUP FOR PUB
https://docs.google.com/document/d/1M9jC0gBEOC1kFlfOWMVSeSfbl2J66zeuLksfuI3MkG4
### 8-2-22 
#### Baseline Assumptions:
* Miami only site (Embassy or Nova)  
  * could extend for 510K req of 3 sites  
* ND running FL and coordinating the PCR comparator  
* QuickColor and EasyPCR tests not the   
* 20 positives and negatives (asymptomatic)  
* Indiv samples (not pooled)  
* Enrichment strategy  
  * Options for recruitment  
    * outbreak chase  
    * outreach to positives from testing programs  
      * them if they are asymp  
      * their contacts  
  * For both Pos and Neg  
    * how to do negs? ads in same venue  
* Comparator must be high sensitivity PCR EUA test not non-EUA LDT

#### Questions
How to run EasyPCR also?

1) freeze inactivated samples and batch up to run all at once? still where??  
2) collaborator such as James Roach at Mayo in FTL

Collection: self collection or HCW collected?  
If/how to include antigen tests?  
If/how to include Combate or other surveillance participants?  
Could/should we ignore how they tested positive? FDA might ding us for bias

- exposure testing serially by antigen tests

Can we run at Embassy?  
Do we want to limit it to Florida and ND running?

Abbott M2000 system \- what ND uses ($85 per test, same day by 9:30pm if submitted by 5:30pm) \- Abbott system does not provide Ct values  
United Clinical Laboratories   
Look for other CLIA labs around Ft Lauderdale

#### Info for Plan
Budget  
Timeframe  
Challenges or Roadblocks

#### To Do's for various people
- [ ] get better understanding of ND's schedule  
- [ ] get info on options for the PCR test, what lab, what assay?  
      
### FloodLAMP Integrated Clinical Study for:
1) Pooled self collection with the FloodLAMP Pooled Home Collection Kit DTC  
2) Tests run under moderate complexity for asymptomatic claim  
   1) QuickColor  
   2) EasyPCR
   3) Pooled and individual test  
3) Usability study of the FloodLAMP Mobile App

The goals of this clinical study are both to obtain the minimum necessary clinical data for EUA submission, as well as put in place the apparatus to obtain a much larger clinical data set, both for publication and for 510K. An enrichment strategy utilizes 1\) school exposures, and 2\) routine surveillance testing. In both, the clinical study offers value to the participants in providing testing to stop spread within classrooms and families.

### Consider including:
* POC for 1XISS in dispenser and reaction mix provided  
* arm for asym people with positive result  
* arm with just our test on repeat swabs and arm with their swab/tube and our test  
* get ND involved when we need another site \- James Roach at Ft. L Cleveland Clinic


### Key Outstanding Questions
- [ ] Do we need a clinical lab to run our QuickColor LAMP test? Or can we run that ourselves in a research lab?

### Recruitment
Recruit families for serial testing after school exposure  
Distribute collection materials for FL (pooled and indiv) and comp PCR (likely wet AN swab, pref saline)

* if possible send home with student same day  
* next morning collection, likely send courier same day (within a few hours)

	  
Also run surveillance serial screening program, where families are pre-recruited into the study. For this arm, we use an enrichment strategy where we place families into the study if their surveillance test is positive.

### Initial Collection
Have participants collect 2 swabs shortly after notification of exposure  
Randomize which swab is done first

- [ ] How to randomize?  
- [ ] Should we consider FloodLAMP first, then 2nd swab for comparator?  
- [ ] Do we need to specify at least 10min and no more than 30min as in our Pre-EUA

FloodLAMP is pooled AN swabs (our collection kit)

- [ ] Is QuickColor & EasyPCR assayed only using pooled AN swabs, or are there multiple arms \- pooled and individual swabs?    
- [ ] Are we comparing pooled AN swabs vs all individual swab comparators in the pool?    
- [ ] In the case of enriched positive samples in the pooled case, are we controlling it so that there is only one positive swab per pool?  If so, how are we sampling the negative swabs? 

Comparator PCR is individual AN swab (their collection kit, saline/PBS)  
Run FloodLAMP QuickColor immediately

#### Pool Positive

If FloodLAMP QuickColor is positive:

* Send indiv comparator PCR swabs to CLIA lab to run. These fulfill the **Pooled Test Study Arm**.  
  * If possible, get frozen aliquot of saline eluted swab (fresh would be difficult, maybe friendly lab).  
* Run fresh FloodLAMP EasyPCR  
* Add family to **Positive Follow Up Cohort** (looking to catch other exposed family members at onset of infection).  
  * Individual swabs for follow up cohort?    
  * QuickColor and EasyPCR?  
  * Comparator swab collected & randomized in the same way?

#### Pool Negative

Select 20 negative pools:

* Send indiv comparator PCR swabs to CLIA lab to run  
* Run fresh FloodLAMP EasyPCR 

If any individual comparator PCR results are positive, move family to Positive Follow Up Cohort

#### Positive Follow Up Cohort

Same day as detecting the positive pool \- have the family collect pairs of individual swabs for FloodLAMP tests and comparator PCR.  
Testing follows the same protocol as initial collection except FloodLAMP swabs are individual instead of pooled.  
Family also collect and each run antigen tests at least 10min after other swabs (document results with photo and time of collection).  
All FloodLAMP QuickColor negatives do not have to be run for the comparator PCR, only a subset (at least 20). Depending on funding we can run larger negative arms that include the comparator PCR, which give greater statistical power to the sensitivity and specificity.

#### Serial Follow Up Cohort

For willing study participants from the Positive Follow Up Cohort, offer to continue serial testing daily per the paired individual swab protocol. The rationale here is that some or all of the family may have been exposed to the likely infected family member(s). By continuing to test them daily in the study, there's the opportunity to pick up a new infection early. Again, the collected PCR swabs only need to be run with the associated cost, if the FloodLAMP QuickColor LAMP test is positive (restart the Positive Follow Up Cohort).  Also running rapid antigen daily as above?  
	

#### Collection Kit Usability Study

See Pre-EUA submitted 5-18-2021, Section H.3  
Includes:

* 12 question survey  
* video recording collection  
* incoming inspection  
* sample adequacy analysis

2 arms, Arm1 without FloodLAMP Mobile App, and Arm2 with the FloodLAMP Mobile App.  
Since all collections for the entire study will be done with the FloodLAMP Mobile App excluding this Arm1, all participants in the study can be given the survey, and their inactivated samples frozen and run on FloodLAMP EasyPCR where the RNAseP signal can be used to assess the sample adequacy. The FDA replied that they did not approve of this but it appears they misunderstood.

### Need to Do/Find
- [ ] Symptom tracker \- maybe rolled into overall daily survey/form, include vaccination/booster status, infection history

### Ideas
- [ ] Get feedback from Dave and others
