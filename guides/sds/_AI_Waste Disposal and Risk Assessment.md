METADATA
last updated: 2026-02-17 RT initial creation
file_name: _AI_Waste Disposal and Risk Assessment.md
file_date: 2026-02-17
title: FloodLAMP Waste Disposal and Risk Assessment Analysis
category: guides
subcategory: sds
tags: 
source_file_type: md
xfile_type: NA
gfile_url: 
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/guides/sds/Waste%20Disposal%20and%20Risk%20Assessment.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10048
words: 6214
notes: Created by AI during archive preparation. **NOT HUMAN VERIFIED - MAY CONTAIN ERRORS** AI-generated analysis of FloodLAMP reagent waste disposal under federal RCRA and state regulations, review of the 2022 biological risk assessment, and review of the uFMEA (SOP-004-B). Source documents include: Reagent Concentrations reference, SDS files (TCEP, EDTA, Clorox Bleach, IPA 70%, Twist RNA Control), the FloodLAMP biological risk assessment (January 2022), and the uFMEA spreadsheet (SOP-004-B).
summary_short: The FloodLAMP Waste Disposal and Risk Assessment Analysis provides a chemical-by-chemical evaluation of whether FloodLAMP's testing reagents and waste streams constitute hazardous waste under federal RCRA and state regulations (California, Florida, Texas), reviews the 2022 biological risk assessment commissioned by FloodLAMP, and reviews the use-FMEA (uFMEA, SOP-004-B) document. Key findings: working-concentration solutions (1XISS, reaction mixes, PGS) are not hazardous waste; concentrated 100XIS stock may trigger RCRA D002 corrosivity due to NaOH; biological waste classification under state medical waste regulations is the primary regulatory concern.


CONTENT

## Opus 4.6 MAX - Response
### Prompt (Verbatim)
Okay, your task is to do an updated risk assessment and answer some key questions related to this work and the chemicals and reagents used by FloodLAMP during its COVID testing. So, the key question is how should our pilot sites have disposed of the used reagents? So, I had a PhD bioscientist research this multiple times and concluded that based on our concentrations and the chemicals involved including the TCEP, it was not considered hazardous waste and we could dispose of it in the trash. Is that true? We had sites based in California, Florida, and Texas. So, if you need to look up, you know, tell me what regulations bear on making these kinds of decisions. How should, you know, the question being, how should, you know, chemicals used in, yeah, chemicals used in this context be disposed of. And the, there were so there are two primary waste artifacts or waste, you know, physical things. One is the samples, the inactivated samples. The other is the spent reactions, you know, the completed reaction tubes which were, you know, small volumes usually, you know, PCR strip tubes. The samples were usually 1.5 or 5 mil tubes with one to five milliliters of the 1x inactivation saline solution, along with the swabs and the spines. Yeah. So, the other question is how should the unused concentrated reagents be disposed. You know, it's my understanding that like the PGS, the primer, guanidine, saline solution, could just be disposed of in the trash. The primers, the DNA, they're not hazardous. The other chemicals are in very small concentrations. Now the 100x inactivation saline solution, I was a little more concerned that at the higher concentration of TCEP that that should be disposed of other than just thrown in the trash. But I think that too was determined by our PhD scientist again after multiple iterations of research. But all that was pre AI to be to be safe. I don't have a write up of that assessment, unfortunately. But, but additionally, I do have a write up of this risk assessment. So the second component what I want you to do is to review this risk assessment. And I don't want you to reproduce, you know, a new version of it. It, you know, ultimately ended up it ended up not being useful for us. Because it just wasn't specific enough. It didn't make a final kind of assessment or give us any type of numerical quantification of the risk. And that's what I wanted. So we started to look at doing that. And that's what this UFMEA document is. Remind me and describe what UFMEA is, what it stands for, and what's involved with it. Okay, make sure in your response to not include any personally identifiable information, including the name of the person who did the risk assessment or their company name. I want to keep that totally out of your response. Okay, do all this.

**Files included in context window:**
- Reagent Concentrations.md
- uFMEA FloodLAMP.xlsx
- FloodLAMP risk assessment (January 2022).pdf
- project-description.md
- _archive-combined-files_sds.md


### Prompt (Cleaned)
Your task is to do an updated risk assessment and answer key questions related to the chemicals and reagents used by FloodLAMP during its COVID testing.

The key question is: how should our pilot sites have disposed of the used reagents? I had a PhD bioscientist research this multiple times and concluded that based on our concentrations and the chemicals involved, including TCEP, it was not considered hazardous waste and we could dispose of it in the trash. Is that true? We had sites in California, Florida, and Texas. Tell me what regulations bear on making these kinds of decisions.

There are two primary waste streams: (1) the inactivated samples — usually 1.5 or 5 mL tubes with one to five milliliters of the 1X Inactivation Saline Solution, along with the swabs and spines; and (2) the spent reaction tubes — completed reaction tubes which were small volumes, usually PCR strip tubes.

The other question is: how should the unused concentrated reagents be disposed? My understanding is that the PGS (primer-guanidine solution) could just be disposed of in the trash — the primers (DNA) are not hazardous, and the other chemicals are in very small concentrations. The 100X Inactivation Saline Solution concerned me more because of the higher concentration of TCEP. I think that too was determined by our PhD scientist, after multiple iterations of research, to be non-hazardous. But all of that was pre-AI and I don't have a write-up of that assessment.

Second component: I have a write-up of a biological risk assessment. Review it, but don't reproduce a new version. It ultimately wasn't useful for us because it wasn't specific enough — it didn't make a final assessment or give any numerical quantification of risk. That's what we wanted, so we started a uFMEA. Remind me what uFMEA is, what it stands for, and what's involved.

Do not include any personally identifiable information in your response, including the name of the person who did the risk assessment or their company name.

**Files included in context window:**
- Reagent Concentrations.md
- uFMEA FloodLAMP.xlsx
- FloodLAMP risk assessment (January 2022).pdf
- project-description.md
- _archive-combined-files_sds.md


### Part 1: Waste Disposal Assessment

##### The Two Primary Waste Streams

Based on the reagent concentrations document and the SDSs, FloodLAMP's testing produced two distinct physical waste streams:

**Waste Stream A: Inactivated Sample Tubes**
- 1.5 mL or 5 mL tubes containing 1-5 mL of 1X Inactivation Saline Solution (1XISS) + swabs
- Chemical composition: TCEP 2.5 mM, EDTA 1.0 mM, NaOH 11.5 mN (~0.0115 N), NaCl ~153 mM
- Also contained potentially biohazardous material (nasal swab specimens)

**Waste Stream B: Spent Reaction Tubes**
- PCR strip tubes with ~25 uL per reaction
- Chemical composition: LAMP primers at ~1X (sub-micromolar concentrations), guanidine-HCl ~43.6 mM, NEB colorimetric LAMP master mix components, plus 2 uL of inactivated sample

##### Chemical Hazardous Waste Analysis

The key regulatory framework is the federal **Resource Conservation and Recovery Act (RCRA)**, codified at **40 CFR Part 261**, which defines hazardous waste through two pathways:

1. **Listed wastes** (P-list, U-list, F-list, K-list): Specific chemicals or waste streams explicitly named
2. **Characteristic wastes**: Wastes exhibiting ignitability (D001), corrosivity (D002), reactivity (D003), or toxicity (D004-D043)

Here is the chemical-by-chemical analysis:

**TCEP (tris(2-carboxyethyl)phosphine hydrochloride, CAS 51805-45-9):**
- Not on the RCRA P-list or U-list of listed hazardous wastes
- The SDS classifies it as a corrosive solid (Skin Corr. 1B, Eye Dam. 1) and it ships as UN 3261, Class 8, Packing Group II
- As a neat solid, it is clearly a corrosive hazardous material
- However, the RCRA corrosivity characteristic (D002) for aqueous solutions triggers at pH <= 2.0 or pH >= 12.5
- At 2.5 mM in 1XISS (diluted 1:100 from the stock), this is a very low concentration in a saline solution buffered near neutral pH — it would not trigger the D002 corrosivity characteristic
- Not on the TCLP toxicity characteristic contaminant list (40 CFR 261.24)
- Not a SARA 302 or 313 reportable substance per the SDS

**EDTA (CAS 60-00-4):**
- Not on the RCRA P-list or U-list
- The SDS classifies it only as Category 4 acute inhalation toxicity and Category 2 eye irritation (as a powder)
- At 1.0 mM in aqueous solution, it poses negligible hazard
- Not on the TCLP toxicity characteristic list
- DOT: Not regulated for transport
- CWA reportable quantity is 5,000 lb — far above any volumes involved here

**NaOH:**
- At 1.15 N in the concentrated 100XIS, this could produce a pH above 12.5, potentially triggering D002
- At 11.5 mN (0.0115 N) in the 1XISS working solution, this is far too dilute to produce corrosive pH — the resulting solution would be near neutral
- Not on the TCLP list

**Guanidine-HCl:**
- Not on the RCRA P-list or U-list
- Classified as Category 4 oral and inhalation toxicity (H302, H332), skin irritation (H315), eye irritation (H319)
- At 95.2 mM in PGS stock, and ~43.6 mM in the reaction, these are relatively dilute concentrations
- Not on the TCLP toxicity characteristic contaminant list
- Would not trigger ignitability, corrosivity, or reactivity characteristics in aqueous solution at these concentrations

**LAMP Primers (synthetic oligonucleotides):**
- Synthetic DNA is not classified as hazardous waste under RCRA
- No CAS number listing, not regulated

**NEB Colorimetric LAMP Master Mix:**
- Commercial enzyme/buffer mixture; proprietary but contains standard molecular biology reagents (DNA polymerase, reverse transcriptase, dNTPs, MgSO4, phenol red). None of these are RCRA-listed or characteristic hazardous wastes at working concentrations

**Twist Synthetic RNA Control:**
- Non-hazardous per SDS; synthetic RNA in TE buffer at extremely low concentrations

##### Assessment: Was the PhD Scientist's Determination Correct?

**For the spent reaction tubes and 1XISS sample tubes: Yes, the determination was substantially correct.** At the working concentrations used in FloodLAMP's testing, none of the individual chemical components would trigger RCRA hazardous waste characteristics:

- No components are RCRA-listed wastes (P/U/F/K lists)
- The dilute aqueous solutions would not exhibit corrosivity (pH would be well within the 2.0-12.5 range)
- No ignitability, reactivity, or TCLP toxicity concerns at these concentrations
- The volumes are extremely small (microliters to low milliliters)

**However, there are important caveats:**

1. **Biohazardous waste is a separate question from chemical hazardous waste.** The CDC's November 2020 Lab Advisory explicitly stated that "laboratories and testing sites should treat all waste from suspected or confirmed COVID-19 patient specimens and kit components as biohazardous waste." While FloodLAMP's TCEP-EDTA + heat treatment protocol was designed to inactivate SARS-CoV-2 (and published literature supports its effectiveness), the CDC guidance applied a conservative "out of an abundance of caution" approach. The risk assessment document reviewed here also states that "since the validity of this process cannot be confirmed on every specimen, out of an abundance of caution, all samples should still be considered biohazardous."

2. **State-specific regulations may layer additional requirements:**

   - **California**: Has broader hazardous waste definitions than federal RCRA under Title 22 CCR. California recognizes corrosive solids (RCRA only covers liquids) and has additional "non-RCRA hazardous waste" categories. California DTSC also requires laboratory hazardous waste determinations. However, even under California's stricter criteria, the working dilutions (1XISS at 2.5 mM TCEP, reaction mixes at ~44 mM guanidine-HCl) would not meet the corrosivity pH threshold. The bigger issue in California would be whether the waste is classified as medical waste under the Medical Waste Management Act.

   - **Texas**: The Texas Commission on Environmental Quality (TCEQ) published specific guidance for COVID-19 rapid testing kit disposal from schools, classifying testing waste as regulated medical waste requiring segregation from regular garbage, biohazard containers, and disposal at TCEQ-authorized facilities. This applies to the biological component, not the chemical component.

   - **Florida**: Florida DEP administers RCRA under state authorization. The Florida Department of Health has authority over biomedical waste. COVID testing waste would fall under biomedical waste regulations.

3. **The practical reality**: For small-volume, dilute laboratory waste from point-of-care COVID testing at these concentrations, the chemical component does not constitute RCRA hazardous waste. The biological component (potentially infectious specimens) is where the regulatory burden lies, and that is governed by medical/biomedical waste regulations at the state level, plus CDC and OSHA guidance, not RCRA.

##### The 100X Inactivation Solution (Concentrated Stock)

The instinct to be more cautious about the concentrated 100XIS was well-placed. At stock concentration:

- **TCEP at 0.25 M**: This is a concentrated corrosive substance. The SDS classifies neat TCEP as causing severe skin burns and eye damage.
- **NaOH at 1.15 N**: An aqueous solution at this normality would have a pH well above 12.5, **triggering the D002 corrosivity characteristic**.
- **EDTA at 0.1 M**: Less concerning but still at meaningful concentration.

**The concentrated 100XIS, if disposed of undiluted, would likely qualify as D002 corrosive hazardous waste** due to the NaOH concentration pushing pH above 12.5. This would require disposal as hazardous waste, not regular trash.

However, if only small volumes (a few milliliters in 5 mL vials) were being disposed, this raises the question of generator status. Facilities generating less than 220 pounds (~100 kg) of hazardous waste per month qualify as **Conditionally Exempt Small Quantity Generators (CESQGs)** under federal RCRA, which have reduced regulatory requirements. At FloodLAMP's operational scale, the total volume of concentrated 100XIS being discarded would have been very small.

**For the PGS (Primer-Guanidine Solution)**: At 95.2 mM guanidine-HCl in aqueous solution, this would not trigger corrosivity (neutral pH range) or other RCRA characteristics. The primers are non-hazardous synthetic DNA. Disposal in regular trash is defensible.

##### Summary Table: Disposal Recommendations

| Waste Stream | Chemical Hazard? | Biological Hazard? | Recommended Disposal |
|---|---|---|---|
| Spent reaction tubes (25 uL) | No (too dilute) | Low (post-inactivation) but CDC recommended treating as biohazardous | Biohazardous waste stream per state medical waste regs; chemical component is non-hazardous |
| 1XISS sample tubes (1-5 mL) | No (too dilute) | Moderate (specimens, even if inactivated) | Biohazardous waste stream per state medical waste regs; chemical component is non-hazardous |
| Unused concentrated 100XIS | **Yes** — D002 corrosivity likely due to NaOH pH >12.5 | No | Chemical hazardous waste (but very small quantities; CESQG rules likely apply) |
| Unused PGS stock | No | No | Regular trash acceptable |
|||

##### Relevant Regulations Summary

| Regulation | Jurisdiction | Relevance |
|---|---|---|
| RCRA (40 CFR 261-262) | Federal | Hazardous waste characteristics and generator requirements |
| OSHA Bloodborne Pathogen Standard (29 CFR 1910.1030) | Federal | Handling of potentially infectious materials |
| CDC Lab Advisory (Nov 2020) | Federal guidance | COVID POC testing waste as biohazardous |
| DOT 49 CFR 173.199 | Federal | Transport of Category B infectious substances (UN3373) |
| California Title 22 CCR Div. 4.5 | CA | Broader hazardous waste definitions; Medical Waste Management Act |
| TCEQ Rules, 30 TAC Chapter 326 | TX | Medical waste management |
| Florida Biomedical Waste regulations (Chapter 64E-16 FAC) | FL | Biomedical waste handling and disposal |
|||


### Part 2: Review of the Risk Assessment

The risk assessment document (dated January 2022) is a qualitative biological risk assessment focused on worker safety during FloodLAMP's point-of-care surveillance testing. Here is the review:

**What it does well:**
- Properly identifies the three main hazard categories: biological, chemical, and physical
- Correctly structures the analysis around the testing workflow stages (collection, initial processing, NAAT preparation, waste disposal)
- Appropriately references the NIOSH Hierarchy of Controls framework
- Provides a reasonable comparison table of FloodLAMP's test versus other POC diagnostic/screening tests
- Correctly identifies that FloodLAMP's self-collection model eliminates the highest-risk step (direct worker contact with potentially infected individuals)
- References relevant CDC, WHO, and APHL guidance documents

**What it lacks (and why it was found insufficient):**
- **No numerical risk quantification**: It identifies hazards and describes mitigations but never assigns severity scores, probability estimates, or any numerical risk metric
- **No prioritization**: Without quantification, there is no way to rank which risks are most important to address
- **No residual risk assessment**: It does not evaluate whether the mitigations FloodLAMP implemented actually reduced risk to an acceptable level
- **Generic rather than specific**: The mitigations listed are broadly applicable to any COVID POC test, not specifically tailored to FloodLAMP's particular protocol and reagent set
- **No chemical risk quantification**: While it mentions chemical hazards (TCEP, EDTA, guanidine), it does not analyze concentrations, exposure levels, or compare them to regulatory thresholds
- **No waste disposal analysis**: The waste disposal section discusses biological contamination risks but does not analyze the chemical waste disposal question at all
- **Essentially a literature review with a comparison**: It reads more like a biosafety literature review and comparison document than an actionable risk assessment tool

The document's value was as a general biosafety framing document, but it did not meet the need for a specific, quantified risk assessment with actionable conclusions.


### Part 3: The uFMEA Document

##### What is uFMEA?

**uFMEA** stands for **Use Failure Mode and Effects Analysis**. It is a specialized variant of the traditional FMEA methodology adapted specifically for analyzing use-related risks — that is, risks arising from how users interact with a device, product, or system rather than from inherent design or manufacturing defects.

**Traditional FMEA** (sometimes called dFMEA for "design" or pFMEA for "process") has been a staple of quality engineering since the 1940s-1960s (originating with the U.S. military and later adopted extensively by the automotive and aerospace industries). It systematically identifies:
- **Failure modes**: What can go wrong?
- **Effects**: What happens if it goes wrong?
- **Causes**: Why would it go wrong?

**uFMEA** extends this by focusing specifically on the human-device interface — how users might misuse, misunderstand, or make errors when operating a product. It is particularly important for medical devices and in-vitro diagnostics, where the FDA requires human factors analysis as part of the design validation process under:
- **IEC 62366-1** (Application of usability engineering to medical devices)
- **ISO 14971** (Application of risk management to medical devices)
- **FDA Human Factors guidance** for premarket submissions

##### The Scoring System

The uFMEA uses three numerical ratings on a 1-5 scale, as defined in the "Change History" sheet of the document:

1. **Severity (SEV)**: Impact of the failure on the user or patient
   - 5 = Catastrophic (loss of limb, life-threatening)
   - 4 = Critical (severe long-term injury, potential disability)
   - 3 = Serious (short-term injury requiring additional medical intervention)
   - 2 = Minor (slight inconvenience, little effect on performance)
   - 1 = Negligible (no or negligible risk)

2. **Occurrence/Probability (OCC)**: How likely the failure is
   - 5 = Frequent (>= 1 in 100)
   - 4 = Probable (< 1 in 1,000)
   - 3 = Occasional (< 1 in 10,000)
   - 2 = Remote (< 1 in 100,000)
   - 1 = Improbable (< 1 in 1,000,000)

3. **Detection (DET)**: How likely the failure will be detected before it causes harm
   - 5 = Remote chance of detection (very high likelihood failure reaches patient)
   - 4 = Low chance of detection
   - 3 = Moderate chance of detection
   - 2 = High chance of detection
   - 1 = Very high chance of detection

The **Risk Priority Number (RPN)** = Severity x Occurrence x Detection. Higher RPN = higher priority for risk mitigation. After mitigations are applied, a **residual RPN (rRPN)** is calculated.

##### Review of FloodLAMP's uFMEA

The document (SOP-004-B, Version 0, effective 2021-11-23) covers 11 risk categories (U-1 through U-11) spanning the full testing workflow:

| Risk ID | Category | Entries |
|---|---|---|
| U-1 | Preparation | 11 failure modes |
| U-2 | Transport, Storage, and Handling | 8 failure modes |
| U-3 | Transport, Storage, and Handling (Primers) | 1 failure mode |
| U-4 | Reading the IFU | 1 failure mode |
| U-5 | Sample Preparation | 7 failure modes |
| U-6 | Sample Inactivation | 7 failure modes |
| U-7 | CLAMP Reaction Preparation | 7 failure modes |
| U-8 | Sample Addition and Heating | 7 failure modes |
| U-9 | Results Interpretation | 2 failure modes |
| U-10 | Waste Disposal | 3 failure modes |
| U-11 | Maintenance | 1 failure mode |
|||

**Positive aspects:**
- It uses the correct uFMEA framework with SEV/OCC/DET scoring and RPN calculation
- It covers the testing workflow comprehensively from preparation through waste disposal
- It identifies a wide range of realistic user errors (pipetting errors, temperature errors, contamination, etc.)
- It identifies current controls for each failure mode (IFU, training, SOPs, QC checks)
- It properly includes columns for post-mitigation scores and residual RPN

**Issues and limitations:**
- **Incomplete**: The "Actions Taken" and revised score columns (revised SEV, OCC, DET, rRPN) are all empty. This means the document only captures the pre-mitigation risk assessment. Without completed residual risk scores, the uFMEA does not demonstrate that risks have been reduced to acceptable levels.
- **RPN formulas not evaluated**: The RPN column contains Excel PRODUCT formulas rather than calculated values, suggesting this was a working draft.
- **Relatively narrow severity range**: Most failure modes are scored at Severity 2 (Minor) or 4 (Critical), with very few at 3 (Serious) and none at 5 (Catastrophic). For a surveillance test (not a diagnostic), severity 4 may be over-assigned for delayed diagnosis scenarios.
- **Waste disposal section is thin**: Only 3 failure modes for waste disposal (U-10), and they focus on biological contamination risk (opening tubes post-amplification, removing seals), not on chemical waste disposal. There is one entry about "hazardous chemicals/bio-hazardous materials" but it does not break down the specific chemical disposal considerations.
- **No risk acceptability criteria defined in this document**: While the scoring scales are defined, there is no stated threshold for what RPN level is acceptable vs. requires action (e.g., "RPNs above 24 require mitigation").
- **Version 0**: This is explicitly the first version — a starting point that was never completed or iterated on.

The document represents a solid structural foundation for a uFMEA but is essentially an incomplete working draft — consistent with the assessment that it did not meet the need for a specific, quantified risk assessment with actionable conclusions.


### Summary

The PhD scientist's conclusion about the dilute working solutions being non-hazardous waste from a chemical standpoint was well-founded. The concentrated 100XIS stock warranted more caution due to the NaOH-driven corrosivity, though the small volumes involved likely placed sites well within CESQG thresholds. The more operationally significant waste classification question was always the biological side — state-level medical/biomedical waste regulations — not the chemical side. The risk assessment provided a useful qualitative overview but lacked the quantitative teeth needed, and the uFMEA was structurally correct but never completed beyond Version 0.

## ChatGPT 5.2 Pro Extended - Response
Here’s what I’m going to do in this response: (1) answer the “trash vs regulated waste” questions for **used** and **unused** FloodLAMP reagents using the concentrations you provided, (2) cite the **federal + CA/FL/TX** rules that govern those decisions, and (3) review why the older narrative risk assessment wasn’t giving you the quantitative output you wanted and explain **uFMEA**.

### 1) Key disposal question: “Could used FloodLAMP reagents go in the trash?”

#### The short, practical answer

* **Used/inactivated sample tubes + swabs** and **spent reaction tubes** are **very unlikely to be “hazardous waste” under RCRA based on chemical characteristics** at the working concentrations you described (especially compared to corrosivity thresholds).
* But “not RCRA-hazardous chemically” is **not the same thing** as “OK for regular trash.” Whether **regular trash** was acceptable also depends on:

  1. whether the waste is considered **regulated medical/biomedical waste** in that state and setting, and
  2. whether you’re putting **free liquids** into municipal solid waste (often restricted by local landfill rules even when nonhazardous).

So the PhD bioscientist’s conclusion can be **directionally correct for the *used, diluted* waste from a chemical-hazard standpoint**, but it’s **not a complete disposal determination** unless it also covered medical/biomedical waste rules and practical solid-waste restrictions.

---

### 2) The chemical side: when is it “hazardous waste” (RCRA / state hazardous waste)?

#### The controlling concept

Under federal rules, the **generator** must make a hazardous waste determination **at the point of waste generation, before any dilution or mixing**, using knowledge and/or testing. ([Legal Information Institute][1])

A key “gotcha” for FloodLAMP is corrosivity:

* A waste is corrosive (and therefore hazardous, **D002**) if it’s aqueous and **pH ≤ 2 or ≥ 12.5**. ([Legal Information Institute][2])
  California uses the same pH threshold for corrosivity. ([Legal Information Institute][3])

#### Apply that to your actual FloodLAMP compositions

From your concentrations reference:

* **100X Inactivation Solution (100XIS)**: **TCEP 0.25 M, EDTA 0.1 M, NaOH 1.15 N**.
* **1X Inactivation Saline Solution (1XISS)** (from 1:100 dilution): **TCEP 2.5 mM, EDTA 1.0 mM, NaOH 0.0115 N**, plus ~0.9% saline. Primer‑Guanidine Solution)**: **guanidine‑HCl 95.2 mM + primers**.
* **Final reaction**: guanidine‑HCl ~**43.6 miluted into the 25 µL reaction).

##### What that implies (1XISS + swab + specimen)**

* Chemically: the NaOH is **orders of magnitude lower than the 100X l pH testing shows ≥12.5, it’s **unlikely to be D002 corrosive**. The conservative way to remove doubt is to **measure pH of a representative “worst-case” waste sample** (freshly made 1XISS + typical specimen load). The corrosivity threshold is the regulatory line. ([Legal Information Institute][2])
* So, **chemically**: often **non‑hazardous**.

**B) Used reaction tubes (spent amplification strips)**

* Chemically: ~43.6 mM guanidine-HCl and buffers/enzymes, tiny volumes.
* This is **not a listed RCRA waste**, and typically doesn’t meet RCRA characteristics (ignitable/corrosive/reactive/toxic) at those concentrations. (RCRA toxicity is a specific list of contaminan’t one of the classic D‑list metals/organics.) ([Legal Information Institute][1])

**C) Unused concentrates (this is where the conclusion often flips)**
This is the biggest regulatory trap in what you described:

* If you discard **unused 100XIS** (TCEP 0.25 M + **NaOH 1.15 N**), you must classify it **as discarded**, **before** diluting it. ([Legal Information Institute][1])
* A solution containing ~1 N NaOH is **very likely pH ≥ 12.5** → corrosive characteristic (**D002**) under federal rules, and the same pH threshold exists in CA. ([Legal Information Institute][2])

**Bottom line (chemical regulatory view):**

* **Used 1XISS/specimen waste + spent reactions**: *likely* **not RCRA hazardous** chemically (but verify pH if you want high confidence).
* **Unused 100XIS**: *likely* **hazardous waste (corrosive, D002)** → **not** appropriate for regular trash.

---

### 3) The biomedical/medical waste side (often the real “trash vs not trash” determinant)

Even if a waste is **not** chemically hazardous, it may still be regulated as **medical/biomedical waste** depending on state definitions and what kind of facility is generating it.

#### California (Medical Waste Management Act)

Two key points from the statute:

* **Saliva, sputum, nasal secretions** (and similar) are **generally not medical waste unless visibly contaminated with blood**. ([California Department of Public Health][4])
* If waste *is* “medical waste,” California requires it to be **treated** by specified methods (incineration, steam sterilization/autoclave, or approved alternatives) **prior to disposal as solid waste**. ([California Department of Public Health][4])

Implication for your CA pilot sites:

* If your waste was **nasal/saliva material without visible blood**, CA law provides a pathway where it may **not** be regulated medical waste. ([California Department of Public Health][4])
* But if your program (or a local enforcing agency) treats these as laboratory/diagnostic wastes associated with a communicable disease, they may require a regulated stream anyway (this is where local interpretation and the site’s classification matter).

#### Florida (Chapter 64E‑16)

Florida’s definitions mirror CA in a surprising way:

* “Body excretions… and secretions such as **nasal discharges, saliva, sputum** … **shall not be considered biomedical waste unless visibly contaminated with blood**.” ([Florida Department of Health][5])
* But “biomedical waste” also includes “**laboratory… wastes which contain human disease-causing agents**,” plus sharps, etc. ([Florida Department of Health][5])
  If it is biomedical waste, Florida has detailed **containment/labeling/treatment** requirements (e.g., red bags, sealed packages, treatment prior to disposal, etc.). ([Florida Department of Health][5])

A particularly relevant rule: **biomedical waste mixed with hazardous waste must be managed as hazardous waste**. ([Florida Department of Health][5])
That’s a strong reason to keep **unused 100XIS** out of any biomedical-waste stream.

#### Texas (TCEQ / TAC framework)

Texas defines “medical waste” more narrowly as special waste from health care-related facilities comprised of categories like:

* **bulk human blood/body fluids**, microbiological waste, pathological waste, sharps, etc. ([TCEQ][6])

Texas guidance also emphasizes that **treated medical waste** can be managed as municipal solid waste under specified conditions, and Texas rules include “thermal inactivation” as a recognized treatment method in their health-services rules. ([TCEQ][7])

Implication:

* Small-volume swab tubes (1–5 mL) may or may not be treated as “bulk body fluids” depending on definitions and accumulation practices, and facility classification matters. ([TCEQ][6])

---

### 4) So—how *should* your pilot sites have disposed of the two primary waste streams?

I’ll give you a **best-practice, compliance-robust** answer first, then note where the statutes create flexibility.

#### Waste stream A: inactivated specimen tubes (swab + 1–5 mL of 1XISS)

**Most compliance‑robust approach across CA/FL/TX:**

1. Keep tubes **closed** and place in a **leak‑resistant secondary container** (zip bag or rigid biohazard container), with absorbent if there’s meaningful free liquid risk.
2. Manage as **biomedical/medical waste** (or at least as “potentially infectious diagnostic waste”) via the site’s medical-waste program or a contracted hauler—especially if the site is operating in a “laboratory” posture or under CLIA-like governance.

**Why this is conservative:** even though CA and FL exclude saliva/nasal secretions unless visibly bloody ([California Department of Public Health][4]), the broader “laboratory waste/human disease-causing agents” language can pull diagnostic testing operations into biomedical waste rules depending on interpretation. ([Florida Department of Health][5])

**Where “regular trash” can be defensible:**

* If the specimens are **saliva/nasal secretions without visible blood** and you have a documented basis that they are not regulated medical/biomedical waste under that state’s definition (CA and FL explicitly carve these out). ([California Department of Public Health][4])
* And the waste is not chemically hazardous (e.g., not corrosive by pH). ([Legal Information Institute][2])
* And you prevent leakage/free liquids.

#### Waste stream B: spent reaction tubes (PCR strips, ~25 µL, post‑amplification)

Chemically, these are extremely small-volume aqueous mixes with guanidine-HCl at ~43.6 mM and master mix components.

**Best practice** is to dispose them in the same controlled waste stream as sample tubes (sealed, leak-resistant), because they:

* contained human specimen aliquots, and
* contain amplified nucleic acid (contamination control reasons).

Whether they legally must be regulated medical waste depends on the same state-specific definitions above; but operationally, treating them as controlled lab waste is cleaner.

---

### 5) The separate question: “How should unused concentrated reagents be disposed?”

### Unused 100X Inactivation Solution (100XIS)

This is the one I would *not* be comfortable calling “trash safe.”

* Composition includes **NaOH 1.15 N**.
* Hazardous waste determinations must be made **before** dilution/mixing. ([Legal Information Institute][1])
* If the pH is ≥12.5, it is **corrosive hazardous waste (D002)**. ([Legal Information Institute][2])

**Recommended disposal posture:**

* Treat unused 100XIS as **hazardous chemical waste (corrosive)** unless you have actual pH testing demonstrating otherwise.
* Do **not** put it in regular trash.
* Do **not** dump to drain unless your site has an EHS-approved neutralization/sewer-discharge procedure and the local sewer authority permits it.

### Unused PGS (guanidine‑HCl ~95.2 mM + primers)

* PGS is **not obviously RCRA-hazardous** at that concentration based on typical characteristics (not ignitable, not likely corrosive, not a D-list toxicant).
* But: it’s still a chemical solution. The “right” answer is often **drain disposal with plenowed by local sewer rules*, or collecting as **nonhazardous lab chemical waste**.

If PGS is contaminated with human specimens, then handle it under your biomedical waste logic.

### Primers / DNA

As you noted, primers/DNA themselves are generally not hazardous. The disposal question is usually about the **matrix** they’re in (buffer, salts, any hazardous additives).

---

### 6) What regulations bear on these decisions (the “decision tree” inputs)

### Federal hazardous waste (RCRA)

* Generator must make a hazardous waste determination **at the point of generation, before dilution/mixing**, and keep supporting records. ([Legal Information Institute][1])
* Corrosivity chered by **pH ≤2 or ≥12.5** (D002). ([Legal Information Institute][2])

### California

* California hazardous waste corrosivity threshold mirrors federal (pH ≤2 or ≥12.5). ([Legal Information Institute][3])
* California Medical Waste Management Act contains both:

  * the explicit exclusion for saliva/nasal secretions unless visibly bloody ([California Department of Public Health][4]), and
  * treatment requirements if something is medical waste. ([California Department of Public Health][4])

### Florida

* Florida biomedical waste definitions (including the nasal/saliva exclusion unless blood) ([Florida Department of Health][5])
* Packaging/containment/treatment requirements if waste is biomedical waste ([Florida Department of Health][5])
* Mixing biomedical waste with hazardous waste → manage as hazardous waste ([Florida Department of Health][5])

### Texas

* Texas definition of medical waste (categories; includes bulk blood/body fluids, microbiological wa([TCEQ][6])
* Texas rules/guidance on treatment options including thermal inactivation and on disposal as municipal solid waste when treated and documented ([Legal Information Institute][8])

---

### 7) Review of the older narrative risk assessment you shared (why it didn’t meet your need)

Without repeating any identifying names, here’s what the document does well and why it didn’t give you the “final numeric answer” you wanted:

#### What it does well

* It’s a solid **hazard identification** document for a point-of-care molecular workflow: it calls out the higher-risk steps (specimen handling, pipetting, potential aerosols/splashes, heat steps, disinfectants) and groups mitigations under the **Hierarchy of Controls** framework (elimination → engineering → administrative → PPE).
* It explicitly recognizes that “inactivation” steps can fail and recommends conservative handling assumptions.

#### Why it wasn’t operationally useful for your “so what do we do?” questions

* It’s primarily **qualitative**, not quantitative. It doesn’t produce:

  * a severity/occurrence/detectability scoring model,
  * an overall residual-risk rating, or
  * a prioritized list of “top risks” with numeric justification.
* It stays relatively **high level** on some operational questions (like waste handling/disposal), describing the hazard category but not making a specific classification decision (e.g., “this is regulated medical waste in CA/FL/TX” vs “this can be disposed as solid waste if X and Y are met”).
* It mixes **biosafety** and **chemical safety** concerns, but doesn’t do a concentration-driven waste determination (e.g., the difference between discarding **100X** vs **1X** solutions).

---

### 8) What uFMEA is (what it stands for and what’s involved)

**uFMEA** most commonly means **Use Failure Modes and Effects Analysis** (often also described as **User FMEA**). It’s an FMEA variant focused on **use-related hazards**—what can go wrong when real users perform tasks in real environments. ([Emergo by UL][9])

#### What’s involved in a uFMEA

A uFMEA typically follows this structure:

1. **Define the use process / user tasks**

   * Break the workflow into steps a user performs (collect sample, add reagent, cap tube, heat, load strip, interpret result, dispose waste, etc.).

2. **Identify potential failure modes (“use errors” / “task failures”)**

   * Examples: wrong volume, wrong tube, skipped step, opened tube at the wrong time, mislabeled sample, incorrect disposal, etc.

3. **Identify the effects and harms**

   * Not just “test fails,” but the **harm**: false negative → infected person not isolated; chemical burn; exposure; cross-contamination; etc.

4. **Score risk**

   * Classic FMEA uses ordinal ratings for:

     * **Severity (S)**
     * **Occurrence (O)** (or probability)
     * **Detection (D)** (how likely the failure is caught before harm)
   * Then computes a **Risk Priority Number (RPN = S × O × D)** to prioritize mitigations. ([ASQ][10])

5. **List current controls**

   * Training, labeling, physical constraints, packaging, SOPs, engineered guards, timers, etc.

6. **Define and implement additional actions**

   * And then re-score **residual risk** after controls.

#### Why uFMEA would have been the right move for your complaint

Your complaint about the narrative risk assessment was essentially: “I need **numerical prioritization and a residual risk statement**.” That’s exactly what an FMEA/uFMEA is designed to produce: a prioritized list of failure modes with **quantified (ordinal) risk scores** and a clear “before vs after controls” view.

One important caveat: RPNs are great for **prioritization**, but they are not a perfect measure of absolute risk (the scoring scales and definitions really matter). Many teams pair uFMEA with an explicit **risk acceptability matrix** (e.g., severity × probability) so you can say “acceptable vs not acceptable” rather than only ranking.

---

### A clean “answer” to your original claim

If I translate your PhD scientist’s conclusion into two separate claims:

1. **“Used FloodLAMP tubes are not hazardous waste (chemical).”**
   That is **plausibly true** for the *used, diluted* waste streams (1XISS + specimen, and spent reactions), because they’re unlikely to meet RCRA characteristics like corrosivity at working strength. The way to make this high-confidence is to document the determination basis under the generator rules and (if needed) verify pH. ([Legal Information Institute][1])

2. **“Therefore we can dispose in regular trash.”**
   That is **not automatically true**, because it also depends on (a) state biomedical/medical waste definitions and facility context, and (b) practical solid-waste rules about free liquids. CA and FL explicitly exclude saliva/nasal secretions unless visibly bloody ([California Department of Public Health][4]), which can support a “trash is allowed” pathway in some circumstances, but it’s still a site- and program-specific determination.

And separately:

3. **“Unused 100X inactivation solution can go in trash.”**
   This is the one that is **very likely false**: the **NaOH 1.15 N** stock is likely corrosive and hazardous (D002), and the hazardous waste determination must be made before dilution.  ([Legal Information Institute][1])

If you want, I can also turn this into a one-page “waste determination memo” template (no names, no company identifiers) that a pilot site could have kept on file: waste streams, compositions, hazard characteristics check, state medical waste decision, and final disposal route.



[1]: https://www.law.cornell.edu/cfr/text/40/262.11 "https://www.law.cornell.edu/cfr/text/40/262.11"
[2]: https://www.law.cornell.edu/cfr/text/40/261.22 "https://www.law.cornell.edu/cfr/text/40/261.22"
[3]: https://www.law.cornell.edu/regulations/california/22-CCR-66261.22 "Cal. Code Regs. Tit. 22, § 66261.22 - Characteristic of Corrosivity | State Regulations | US Law | LII / Legal Information Institute"
[4]: https://www.cdph.ca.gov/programs/ceh/drsem/cdph%20document%20library/emb/medicalwaste/medicalwastemanagementact.pdf "https://www.cdph.ca.gov/programs/ceh/drsem/cdph%20document%20library/emb/medicalwaste/medicalwastemanagementact.pdf"
[5]: https://www.floridahealth.gov/wp-content/uploads/2025/08/64E-16.pdf "https://www.floridahealth.gov/wp-content/uploads/2025/08/64E-16.pdf"
[6]: https://www.tceq.texas.gov/permitting/waste_permits/msw_permits/medwaste/medwaste-def?utm_source=chatgpt.com "What is Medical Waste?"
[7]: https://www.tceq.texas.gov/permitting/waste_permits/msw_permits/medwaste/medwaste-disposal "https://www.tceq.texas.gov/permitting/waste_permits/msw_permits/medwaste/medwaste-disposal"
[8]: https://www.law.cornell.edu/regulations/texas/25-Tex-Admin-Code-SS-1-136 "https://www.law.cornell.edu/regulations/texas/25-Tex-Admin-Code-SS-1-136"
[9]: https://www.emergobyul.com/news/10-steps-conducting-use-related-risk-analysis-part-your-human-factors-engineering-process?utm_source=chatgpt.com "10 Steps to Conducting a Use-related Risk Analysis as Part ..."
[10]: https://asq.org/quality-resources/fmea?srsltid=AfmBOoqAZuOIRT8VEXsOfhlGgyJ15ikmCL9wrAVhTKbve4bnzhE93IuP&utm_source=chatgpt.com "What is FMEA? Failure Mode & Effects Analysis"
