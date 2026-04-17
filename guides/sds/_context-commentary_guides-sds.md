METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-sds.md
category: guides
subcategory: sds
gfile_url: https://docs.google.com/document/d/1f_35t2FdLmr_YW9GzeCFGwbkYhDrwaaQlZh6EvDdUY0
words: 642
tokens: 890


CONTENT

## Context
The `guides/sds` subcategory within the Guides collection contains Safety Data Sheets for the key chemicals used in FloodLAMP's LAMP-based COVID-19 testing workflow, along with an original analysis document addressing waste disposal and risk assessment.

The five SDS files cover the chemicals central to FloodLAMP's reagent system:
- `SDS - TCEP` (tris(2-carboxyethyl)phosphine hydrochloride) — the reducing agent used in the Inactivation Saline Solution for viral inactivation; classified as a corrosive solid
- `SDS - EDTA` (ethylenediaminetetraacetic acid) — the chelating agent also used in the Inactivation Saline Solution; relatively low hazard at working concentrations
- `SDS - Clorox Bleach Regular` (sodium hypochlorite 5–10%) — used for decontamination and cleaning at test sites; corrosive with aquatic toxicity concerns
- `SDS - Isopropyl Alcohol 70 percent` — used for surface disinfection; a Class 3 flammable liquid
- `SDS - Twist Synthetic SARS-CoV-2 RNA Control Rev7 001038v7` — the non-hazardous synthetic RNA positive control used in test verification

These SDS files were maintained as a convenient reference for FloodLAMP personnel and pilot site operators, providing standardized hazard, handling, PPE, and disposal information for the chemicals they encountered during testing operations.

The sixth file in the subcategory, `_AI_Waste Disposal and Risk Assessment` is an original analysis created by AI during archive preparation. It addresses questions that were operationally important during FloodLAMP's active period: whether the used and unused reagents constituted hazardous waste under federal RCRA and state regulations (California, Florida, and Texas), how pilot sites should have disposed of the two primary waste streams (inactivated sample tubes and spent reaction tubes), and what the regulatory landscape looked like for both the chemical and biological components of the waste. The document also reviews a qualitative biological risk assessment that FloodLAMP commissioned in 2022 and a use-FMEA (uFMEA) document (both files omitted from archive due to confidentiality commitments) that FloodLAMP began developing to obtain the numerical risk quantification the narrative assessment lacked. These disposal and risk questions connect to the `guides/manufacturing` subcategory (where the reagent formulations are defined) and to the `guides/qms-sops`subcategory (where the related SOPs reside).


## Commentary
The substantive commentary for this subcategory lives in the "_AI_Waste Disposal and Risk Assessment.md" file, which documents the analysis that we wish we had done more rigorously during FloodLAMP's active period. The core issue was consequential: we needed to better understand how our reagents and testing waste were classified with respect to hazards and risk, and how pilot sites in three different states should dispose of them. We had a PhD bioscientist research the question multiple times, and the conclusion — that the working-concentration solutions were not hazardous waste — turns out to be substantially correct from a chemical standpoint. But the full picture is more nuanced than we appreciated at the time, particularly around the concentrated 100X Inactivation Solution (which likely qualifies as D002 corrosive hazardous waste due to NaOH concentration) and the biological waste classification question, which is governed by state medical waste regulations rather than RCRA.

The lesson to take from this now is about the value of AI-assisted research tools for these kinds of regulatory and technical questions. All of that earlier research was done pre-AI, without a written record of the reasoning. During archive preparation, we were able to use AI to produce the detailed, chemical-by-chemical analysis with specific regulatory citations that we would have liked to have had during FloodLAMP's operation. For any future decentralized testing operation, we recommend a documented waste determination memo for each site — something that maps each waste stream to the applicable federal and state regulations and reaches an explicit disposal recommendation. AI tools make this kind of thorough, multi-jurisdictional regulatory research dramatically more accessible, even for a small company without in-house experts. That is a genuine advancement for the field as the barrier to getting these operational safety and compliance questions properly answered has dropped significantly.
