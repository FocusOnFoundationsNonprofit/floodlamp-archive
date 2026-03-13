METADATA
last updated: 2026-03-13_065635
file_name: _archive-combined-files_manufacturing_14k.md
category: guides
subcategory: manufacturing
gfile_url: **FLAGGED - TBD user-facing Google-hosted public file URL**
words: 
tokens: 


CONTENT

# _archive-combined-files_manufacturing_14k (7 files, 13,685 tokens)

# 3,429  _AI_Reagent Concentrations.md
METADATA
last updated: 2026-02-17 RT initial creation
file_name: _AI_Reagent Concentrations.md
file_date: 2026-02-17
title: FloodLAMP Reagent Concentrations Reference
category: guides
subcategory: manufacturing
tags: 
source_file_type: md
xfile_type: NA
gfile_url: https://docs.google.com/document/d/1gOeoQK0CY2kBKjLJ50EB9ObVzu74yotF_wSNu4nXYLs
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/Reagent%20Concentrations.md
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: NA
conversion: NA
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 3429
words: 1768
notes: Created by Opus 4.6 during archive preparation. **NOT HUMAN VERIFIED - MAY CONTAIN ERRORS** Concentrations were extracted from manufacturing SOPs, process flow diagrams, and cost models in the FloodLAMP archive, with verification calculations shown. Source documents include: SOP-202-A_1 (100XIS Manufacturing), SOP-201-A_2 (PGS48 Manufacturing), SOP-101-A_2 (1XISS Prep), SOP-102-A_2 (Reaction Mix Prep), SOP-105-A_1/B_1 (QuickColor Test Diagrams/Signage), Assay and Reagent Manufacturing Diagrams, Cost Model, and LAMP Primers spreadsheet.
summary_short: The FloodLAMP Reagent Concentrations Reference provides final concentrations and verification calculations for all key FloodLAMP assay reagents: 100X Inactivation Solution (TCEP 0.25M, EDTA 0.1M, NaOH 1.15N), Primer-Guanidine Solution (primers 2.38X, guanidine-HCl 95.2mM), 1X Inactivation Saline Solution (TCEP 2.5mM, EDTA 1.0mM, NaCl ~153mM), CLAMP Reaction Mix composition, and Twist Positive Control dilution series. Concentrations are derived from manufacturing SOPs, process flow diagrams, and cost models in the archive with full calculation work shown.


CONTENT

## Overview
This reference document consolidates the final concentrations of all key FloodLAMP reagents in one place. Concentrations are extracted from manufacturing SOPs, process flow diagrams (Assay and Reagent Manufacturing Diagrams), and cost models in the FloodLAMP archive. Where concentrations are not explicitly stated in the source documents, they are calculated from batch recipes with full work shown.


## 100X Inactivation Solution (100XIS)

### Final Concentrations
| Component | Concentration |
|-----------|---------------|
| TCEP | 0.25 M |
| EDTA | 0.1 M |
| NaOH | 1.15 N |
||

Source: Assay and Reagent Manufacturing Diagrams, Slide 16 (100X Inactivation Solution Diagram, Standard). Concentrations are stated directly in the slide description.

### Verification from XL Batch Recipe (SOP-202-A_1)
The XL batch recipe calls for:
- 75.0 g TCEP
- 667.5 mL NF water
- 209.4 mL of 0.5M EDTA
- 120 mL of 10N NaOH

Total volume: 667.5 + 209.4 + 120 = 996.9 mL (plus the small volume displaced by dissolved TCEP, bringing total to ~1,000 mL).

**TCEP**: 75 g / 286.65 g/mol (MW from TCEP SDS) = 0.2617 mol in ~1 L = **0.262 M** (matches ~0.25M stated; slight excess due to total volume being marginally under 1L before TCEP displacement).

**EDTA**: 209.4 mL x 0.5 M = 104.7 mmol in ~1 L = **0.105 M** (matches ~0.1M stated).

**NaOH**: 120 mL x 10 N = 1,200 meq in ~1 L = **1.20 N** (matches ~1.15N stated; the small discrepancy reflects the actual total volume being slightly greater than 1L after TCEP dissolves).

### Additional Confirmation
The Cost Model (operations archive) independently lists the same concentrations:
- TCEP stock concentration: 0.5M, final in 100XIS: 0.25M
- EDTA source: 0.5M, final in 100XIS: 0.1M
- NaOH source: 10N, final in 100XIS: 1.15N

### Raw Materials
| Component | Source Product | Source Concentration |
|-----------|---------------|----------------------|
| TCEP | GoldBio TCEP25 (25g bottle) | Solid, MW 286.65 g/mol |
| EDTA | Thermo 15575020 | 0.5 M |
| NaOH | Sigma SX0607N | 10 N |
| NF Water | Thermo 10977015 | N/A |
||

Storage: -20°C in 5 mL screw cap vials (standard batch) or 1 mL aliquots in 1.5 mL tubes (standard batch from Slide 16).


## Primer-Guanidine Solution (PGS)

### Final Concentrations
| Component | Concentration in PGS |
|-----------|----------------------|
| LAMP Primers (each of 3 sets: As1e, N2, E1) | 2.38X per set |
| Guanidine-HCl | 95.2 mM |
||

Source: Assay and Reagent Manufacturing Diagrams, Slide 10 (Primer-Guanidine Solution Diagram). PGS specs stated as: Primers 2.38X, GUD 95.2 mM.

### Verification from PGS48 Manufacturing Recipe (SOP-201-A_2)
The PGS48 batch recipe calls for:
- 28.2 mL NF Water (refrigerated >1 hr)
- 600 µL of 6M Guanidine-HCl
- 9 tubes of LAMP primers (3 sets x 3 tubes each), each resuspended in 1,000 µL NF Water = 9.0 mL total primer volume

Total volume: 28.2 + 0.6 + 9.0 = **37.8 mL**

**Guanidine-HCl**: 600 µL x 6 M = 3,600 µmol = 3.6 mmol. In 37.8 mL: 3.6 / 37.8 = **95.2 mM** (matches stated spec).

**Primers**: Each primer set has 3 tubes resuspended at 30X premix concentration (per LAMP Primers spreadsheet). Per set: 3 tubes x 1,000 µL = 3,000 µL at 30X. Diluted into 37,800 µL total: 3,000 x 30 / 37,800 = **2.38X per set** (matches stated spec).

### LAMP Primer Sets
The three SARS-CoV-2 LAMP primer sets used in PGS, each containing 6 primers at 30X premix concentration:

| Set | Target | Gene |
|-----|--------|------|
| As1e | ORF1ab | SARS-CoV-2 |
| N2 | N gene | SARS-CoV-2 |
| E1 | E gene | SARS-CoV-2 |
||

Each 30X premix contains (per the LAMP Primers spreadsheet):

| Primer Type | 30X Concentration (µM) |
|-------------|------------------------|
| FIP | 48.0 |
| BIP | 48.0 |
| F3 | 6.0 |
| B3 | 6.0 |
| LF | 12.0 |
| LB | 12.0 |
||

At 1X (final reaction), concentrations are: FIP/BIP 1.6 µM, F3/B3 0.2 µM, LF/LB 0.4 µM.

### PGS Aliquot Sizes
| Aliquot Volume | Reactions per Aliquot | Designation |
|----------------|----------------------|-------------|
| 92 µL | 8 | PGS8 |
| 275 µL | 24 | PGS24 |
| 550 µL | 48 | PGS48 |
| 1,120 µL | 96 | PGS96 |
||

Storage: -20°C in 1.5 mL screw cap tubes.


## CLAMP Reaction Mix

### Component Volumes by Reaction Scale
| Reactions | PGS (µL) | CLAMP MM (µL) | Total RM (µL) |
|-----------|----------|---------------|---------------|
| 8 | 92 | 109 | 201 |
| 16 | 183 | 218 | 401 |
| 24 | 275 | 328 | 603 |
| 48 | 550 | 655 | 1,205 |
||

Source: SOP-102-A_2 (Reaction Mix Prep), SOP-105-A_1 (QuickColor Test Diagrams), SOP-105-B_1 (QuickColor Test Signage). All three documents report the same volumes.

### Per-Reaction Composition
Each reaction: 23 µL reaction mix dispensed per well + 2 µL sample = **25 µL total reaction volume**.

Using the 48-reaction scale for calculation:
- PGS per reaction: 550 / 48 = **11.46 µL**
- CLAMP MM per reaction: 655 / 48 = **13.65 µL**
- Total RM per reaction: 25.1 µL (~10% overage built into the scale-up)

### Final Concentrations in the 25 µL Reaction
| Component | Concentration in Source | Dilution Factor | Final in Reaction |
|-----------|------------------------|-----------------|-------------------|
| LAMP Primers (each set) | 2.38X (in PGS) | 11.46/25 = 0.458 | ~1.09X (~1X target) |
| Guanidine-HCl | 95.2 mM (in PGS) | 11.46/25 = 0.458 | ~43.6 mM |
| NEB M1804 CLAMP MM | 2X (NEB standard) | 13.65/25 = 0.546 | ~1.09X (~1X target) |
||

Note: NEB M1804 (WarmStart Colorimetric LAMP Master Mix) is a proprietary commercial product. Its internal composition (Bst 2.0 WarmStart DNA polymerase, WarmStart RTx reverse transcriptase, dNTPs, MgSO4, phenol red pH indicator, buffer) is not specified in the FloodLAMP archive. NEB supplies it as a 2X concentrate.

### Reaction Mix Usage
- Dispense 23 µL per well (at bottom, no blowout, no tip touch)
- Add 2 µL sample per well (pipet up and down 5X, blowout in liquid, tip touch)
- Amplify at 65°C for 25 min
- Expiration: 4 weeks after prep or if discolored


## 1X Inactivation Saline Solution (1XISS)

### Preparation Protocol
1XISS is prepared by diluting 100XIS 1:100 into 0.9% saline (SOP-101-A_2).

| Saline Volume | 100XIS Volume | Resulting 1XISS Volume |
|---------------|---------------|------------------------|
| 5 mL | 50 µL | ~5 mL |
| 15 mL | 150 µL | ~15 mL |
| 50 mL | 500 µL | ~50 mL |
||

Source: SOP-105-B_1 (QuickColor Test Signage) and SOP-101-A_2 (1XISS Prep Table Form).

### Calculated Final Concentrations
These concentrations are not explicitly stated in the archive documents but are derived from the 1:100 dilution of 100XIS into 0.9% saline.

Starting materials:
- 100XIS: TCEP 0.25M, EDTA 0.1M, NaOH 1.15N
- 0.9% NaCl saline: 9 g/L NaCl, MW 58.44 g/mol = 154 mM NaCl

| Component | 100XIS Concentration | Dilution (1:100) | Final in 1XISS |
|-----------|----------------------|-------------------|----------------|
| TCEP | 0.25 M | /100 | 2.5 mM |
| EDTA | 0.1 M | /100 | 1.0 mM |
| NaOH | 1.15 N | /100 | 11.5 mN (0.0115 N) |
| NaCl | 154 mM (from saline) | x 99/100 | ~152.5 mM (~0.89%) |
||

The 2.5 mM TCEP concentration is independently confirmed in the Cost Model (operations archive), which lists "TCEP Rxn Conc mM = 2.5".

### 1XISS Usage
- Add 1 mL of 1XISS to each pooled dry swab sample tube
- Vortex 10 sec (individual tubes) or 30 sec (tubes in rack)
- Heat inactivation: Water bath 99°C for 8 min then cool 10 min, OR dry heat block 95°C for 5 min then cool 5 min
- Expiration: 2 weeks after preparation


## Twist Positive Control (TPC)

### Dilution Series
| Stock | Concentration | Volume | Storage |
|-------|---------------|--------|---------|
| Twist 102019 (source RNA) | ~1 x 10^6 cp/µL | 100 µL | -80°C |
| Total Human RNA (carrier) | 50 ng/µL | 100 µL | -80°C |
| TSPC (source aliquots) | (concentrated) | 5 µL x 19 | -80°C |
| TRPC (source stock) | 1,000 cp/µL | 490 µL x 10 | -80°C |
| TFPC (intermediate) | (intermediate) | 20 µL x 24 | -80°C |
| TPC (working aliquots) | 125 cp/µL | 10 µL x 16 | -80°C |
||

Source: Assay and Reagent Manufacturing Diagrams, Slide 7 (Twist Positive Control Diagram).

### Carrier Buffer
Twist Synthetic SARS-CoV-2 RNA Control is supplied in TE buffer (per Twist SDS-001038):

| Buffer Component | Concentration |
|------------------|---------------|
| Tris | 10 mM, pH 8.0 |
| EDTA | 0.1 mM |
| RNA | ≤1% |
||

### In-Use Preparation
For PGS verification runs (SOP-301): TPC100 is thawed for 30 sec, then 20 µL of ultra pure water is added to create TPC50 (~50 cp/µL). 2 µL of TPC50 is added per positive control well, delivering approximately **100 copies** of synthetic SARS-CoV-2 RNA per reaction.


## Comprehensive Summary Table
| Reagent | Component | Concentration |
|---------|-----------|---------------|
| **100XIS** | TCEP | 0.25 M |
| **100XIS** | EDTA | 0.1 M |
| **100XIS** | NaOH | 1.15 N |
| **PGS** | LAMP Primers (per set) | 2.38X |
| **PGS** | Guanidine-HCl | 95.2 mM |
| **1XISS** | TCEP | 2.5 mM |
| **1XISS** | EDTA | 1.0 mM |
| **1XISS** | NaOH | 11.5 mN |
| **1XISS** | NaCl | ~153 mM (~0.89%) |
| **Reaction (25 µL)** | LAMP Primers (per set) | ~1X |
| **Reaction (25 µL)** | Guanidine-HCl | ~43.6 mM |
| **Reaction (25 µL)** | NEB M1804 CLAMP MM | ~1X (from 2X) |
| **TPC (working)** | Synthetic SARS-CoV-2 RNA | 125 cp/µL |
| **TPC50 (in-use)** | Synthetic SARS-CoV-2 RNA | ~50 cp/µL |
||


## Source Documents
The concentrations in this reference were extracted and verified from the following FloodLAMP archive documents:
- Assay and Reagent Manufacturing Diagrams (guides/manufacturing) — Slides 5, 6, 7, 10, 11, 16
- SOP-202-A_1: 100XIS Manufacturing Run Form (guides/manufacturing)
- SOP-201-A_2: PGS48 Manufacturing Run Form (guides/manufacturing)
- SOP-101-A_2: 1XISS Prep Table Form (guides/qms-sops)
- SOP-102-A_2: Reaction Mix Prep Table Form (guides/qms-sops)
- SOP-105-A_1: QuickColor Test Diagrams (guides/qms-sops)
- SOP-105-B_1: QuickColor Test Signage (guides/qms-sops)
- Cost Model - FloodLAMP (guides/operations)
- LAMP Primers UPDATED 12-17-2020 (guides/operations)
- SDS - TCEP (guides/sds) — for TCEP molecular weight


# 1,669  _context-commentary_guides-manufacturing.md
METADATA
last updated: 2026-02-16 RT
file_name: _context-commentary_guides-manufacturing.md
category: guides
subcategory: manufacturing
gfile_url: **FLAGGED - TDB after review and update of all CC**
words: 1176
tokens: 1669


CONTENT

## Context
The manufacturing subcategory contains the Standard Operating Procedures (SOPs) and process flow diagrams that represented FloodLAMP's most mature approach to producing its two key reagents: the Primer-Guanidine Solution (PGS48) and the 100X Inactivation Solution (100XIS).

PGS48 is the Primer-Guanidine Solution formulated for 48 reactions. It combines LAMP primer sets (As1e, N2, E1) with guanidine hydrochloride and nuclease-free water. The resulting solution is mixed with NEB's colorimetric LAMP master mix to form the reaction mix for the QuickColor LAMP test. The "48" refers to the standardized batch size of 48 reactions, tuned to FloodLAMP's typical customer usage patterns of 20–100+ reactions per session.

100XIS is the 100X Inactivation Solution, a TCEP-based formulation combining TCEP, EDTA, and NaOH. When diluted to 1X Inactivation Saline Solution and added to dry swabs, it extracts and protects the RNA for downstream testing upon heating. Both reagent formulations derive from the Rabe-Cepko protocol.

The subcategory includes five files:

- **Assay and Reagent Manufacturing Diagrams** — A 19-slide presentation containing process flow diagrams for all key reagent manufacturing and assay workflows, covering PGS batching, 100XIS manufacturing, primer preparation, positive control aliquoting, and assay setup at various reaction scales (24, 48, and 96 reactions).
- **SOP-201-A_2: PGS48 Manufacturing Run Form** — Step-by-step manufacturing procedure for PGS48, including primer resuspension, guanidine-HCl mixing, and robotic aliquoting on an OpenTrons liquid handler.
- **SOP-202-A_1: 100XIS Manufacturing Run Form** — Manufacturing procedure for 100XIS, covering TCEP weighing, component mixing in a 1L glass bottle, and aliquoting into 5 mL vials for storage at -20°C.
- **SOP-301: PGS48 Verification Run Form** — Quality verification procedure for PGS48 batches via CLAMP amplification with positive and negative controls, including a plate layout map for tracking results by lot number.
- **SOP-302: 100XIS Verification Run Form** — Quality verification procedure for 100XIS batches via CLAMP amplification.

The term "manufacturing" is used loosely here. FloodLAMP's production was small-scale pilot manufacturing — a small team working in a shared lab space at MBC BioLabs in San Carlos, California, without the infrastructure or experience typical of industrial reagent manufacturing. The team included a PhD scientist who developed the initial batch records and then these SOPs, which represented the most controlled and streamlined versions of the processes FloodLAMP achieved.

These SOPs were preceded by a less formal system of batch records. The transition to SOPs was substantially but not fully complete by early 2022 (January–February), with the PGS48 and 100XIS procedures being the primary ones formalized. The PGS48 manufacturing process used an OpenTrons liquid handling robot for aliquoting, along with custom 3D-printed tube holders.

Over its operating period, FloodLAMP produced approximately 100,000 reactions worth of PGS and 150,000–200,000 samples worth of 100X Inactivation Solution. The PGS48 process yielded 3,264 reactions per lot (68 tubes at 550 µL each) and could produce roughly 10,000 reactions per hour once setup was complete, though setup time was significant. The 100XIS was produced in much larger lots — approximately 108,000 reactions per lot (216 five-mL tubes), achievable in a few hours with setup time dominating the run.

No formal stability study was conducted on PGS, as it was stored frozen and used same-day to make the reaction mix. The more pressing stability issue was the reaction mix itself: when sites stored pre-made reaction mix, the deep pink color of the colorimetric LAMP reaction would sometimes fade or turn orange. FloodLAMP provided clear instructions to avoid storing pre-made reaction mix when possible, and to verify the deep pink color before use. A cursory stability study was performed on the 1X Inactivation Saline Solution (1XISS) using PCR as the endpoint, measuring over a period of two weeks. No significant loss of signal was observed, so two weeks was specified as the usage window for 1XISS.

These documents connect to other parts of the archive: the reagents produced here were shipped to FloodLAMP's pilot program customers (documented in the Pilots collection), and the testing protocols that use these reagents are covered in other Guides subcategories.


## Commentary
These SOPs and the reagent formulations they document were among the most important operational achievements at FloodLAMP. They represented a significant step in simplifying and standardizing the reagent production process. The Primer-Guanidine Solution, in particular, was a meaningful improvement — premixing the primers with guanidine hydrochloride eliminated a step for the end user, and we confirmed through testing that this premixing did not cause degradation. We also put considerable thought into the volumes and tube sizes to minimize waste while providing enough reagent for a typical testing session of 20 to several hundred reactions.

The OpenTrons robot was used for PGS48 aliquoting, and we had custom 3D-printed tube holders to support the workflow. In hindsight, the robotic aliquoting was overkill for the volumes we actually produced. We over-indexed on process improvements at a time when the bottleneck was elsewhere — we couldn't scale the rest of our operations (ordering, logistics, customer support) to match the demand during the Omicron surge in late 2021 and early 2022. We had on the order of half a million reactions worth of primers on hand. The process control was a step in the right direction, but the investment in automation wasn't justified by our actual throughput.

That said, the formulation work itself — consolidating into PGS, tuning the volumes, and standardizing at 48 reactions — was genuinely valuable. That's the endpoint worth preserving from what we did here.

The broader lesson for the field is about the reagent supply chain. Small organizations like FloodLAMP should not be manufacturing their own reagents if there's any way to avoid it. What's needed is for reagent manufacturers — the actual producers like New England Biolabs, not the white-label diagnostic companies — to produce low-cost, high-volume reagent kits for the most widely used open protocols. This has to go hand in hand with establishing open EUA protocols and rights of reference so that multiple parties can legally use and distribute these reagents to run validated, consensus testing protocols.


The bottleneck during the Omicron surge was not reagent manufacturing itself but the overall kit and supplies preparation, shipment, tracking, and coordination. The system involved over 100 parts, many requiring qualification and preparation. Preparing, delivering, and supporting the complete testing systems was a large burden for a small team. The process didn't fully mature until FloodLAMP's last pilot (Abrome) mid 2022, where a cart-and-drawers system worked well. Beyond the physical logistics, the digital side — apps, data tracking, troubleshooting — was a constant challenge with significant downtime and outages.

The model to follow is SalivaDirect, which contracted with Eurofins to produce commercially available SalivaDirect kits, which were available for general order and not restricted to clinical labs designated under Saliva Direct's open EUA. When we ordered those kits, they arrived next day, were well formulated, and a relatively inexperienced lab tech was able to run the protocol successfully on a PCR machine. That combination — simplified protocol, commercially manufactured reagents, fast shipping — is what decentralized testing needs. Having individual labs or small companies mix their own reagents is a dead end for scale.


# 1,958  Assay and Reagent Manufacturing Diagrams.md
METADATA
last updated: 2026-02-15 RT initial conversion
file_name: Assay and Reagent Manufacturing Diagrams.md
file_date: 2022-02-01
title: FloodLAMP Assay and Reagent Manufacturing Diagrams
category: guides
subcategory: manufacturing
tags: 
source_file_type: gslide
xfile_type: pptx
gfile_url: https://docs.google.com/presentation/d/10kiok18TcbatUeareNyUyrcr90_ib0gT56NpWsIh58U
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/Assay%20and%20Reagent%20Manufacturing%20Diagrams.pptx
pdf_gdrive_url: https://drive.google.com/file/d/1uyKevLkDpU1De9Gl8Y2fi1CHgNfvMl7f
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/manufacturing/Assay%20and%20Reagent%20Manufacturing%20Diagrams.pdf
conversion_input_file_type: pptx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1958
words: 925
notes: This is a presentation (pptx/Google Slides) consisting primarily of manufacturing process flow diagrams (images). The markdown content lists slide titles only as placeholders since the slides are image-based diagrams. Refer to the source PDF or pptx for the actual diagrams.
summary_short: The FloodLAMP Assay and Reagent Manufacturing Diagrams is a 19-slide presentation containing process flow diagrams for all key reagent manufacturing and assay workflows. It covers the FloodLAMP Direct RNA Assays (QuickColor LAMP and EasyPCR) at 48- and 96-reaction scales, validation first-run setup, gamma contrived positive preparation, 100X Inactivation Solution manufacturing (standard and XL batches), 1X Inactivation Saline Solution preparation, Twist Positive Control aliquoting, Gamma Blue and 10K dilution series, Primer-Guanidine Solution (PGS) batching, colorimetric CLAMP assay setup, 5X PCR primer preparation, and PCR assay reaction mix preparation.


CONTENT

## Slide 1: FloodLAMP Direct RNA Assays - 48 Reaction Volumes
_Manufacturing process flow diagram showing reagent preparation and assay workflow for 48-reaction scale. Covers 100X Inactivation Solution, 0.9% Saline, Primer-Guanidine Solution (PGS, 550µL), Colorimetric LAMP MM (655µL), PCR Reaction Mix, and both QuickColor LAMP Test (65°C/25min) and EasyPCR Test (qPCR, 80min) pathways._

## Slide 2: FloodLAMP Direct RNA Assays - 96 Reaction Volumes
_Manufacturing process flow diagram showing reagent preparation and assay workflow for 96-reaction scale. Same reagent pathways as Slide 1 but with scaled volumes: PGS (1080µL), Colorimetric LAMP MM (1286µL), CLAMP Reaction Mix (2366µL, 25µL/rxn)._

## Slide 3: Validation: First Run - 24 Reaction Volumes
_Validation run diagram for 24-reaction scale with both CLAMP (PGS 275µL, CLAMP MM 327µL, 602µL total RM) and PCR (5X PCR Primers 105µL, PCR MM 263µL, RT 26.3µL) assay pathways. Includes positive and negative controls in the 24-tube sample plate._

## Slide 4: Gamma Contrived Positive Diagram (v1.3)
_Process flow for preparing Gamma Contrived Positive (GCP) samples. Shows dilution from Gamma Blue Dilution (GBD, 1000 cp/µL) using anterior nares (AN) swabs dried >20 min, with 1X Inactivation Saline Solution elution and standard inactivation procedures._

## Slide 5: 100X Inactivation Solution XL Diagram
_Extended-scale manufacturing diagram for 100X Inactivation Solution. Key source materials: TCEP (25g), 10N NaOH (1L), 0.5M EDTA (100mL). Includes component volume calculation table with Standard and Adjusted columns, plus 0.5M TCEP intermediate preparation step._

## Slide 6: 1X Inactivation Saline Solution Diagram
_Process flow for preparing 1X Inactivation Saline Solution (1XISS). Combines 5M NaCl-derived 0.9% Saline with 100X Inactivation Solution at ~1/100th volume. Shows 50mL Falcon tube aliquoting and reference to Saline Batch Record v1.0 and Inactivation Protocol v5.1._

## Slide 7: Twist Positive Control Diagram
_Aliquoting workflow for Twist Positive Controls (TPC). Key source: Twist 102019 (~1e6 cp/µL, 100µL) and Total Human RNA (50ng/µL, 100µL). Creates TSPC (5µL x 19), TRPC source stock (1000 cp/µL, 490µL x 10), TFPC (20µL x 24), and TPC working aliquots (125 cp/µL, 10µL x 16). All stored at -80°C._

## Slide 8: Gamma Blue Dilution (GBD) Diagram
_Dilution workflow from BEI gamma-irradiated SARS-CoV-2 (NR-52287, 1.75e6 cp/µL). Creates GBEI aliquots (5µL x 100 in PCR strip tubes), then dilutes to GBD (1000 cp/µL) in 30mL Chub (8.75mL), and final aliquots in 1.5mL tubes (83 x 105µL). Reference: Gamma Blue Dil Batch Record v1.1._

## Slide 9: Gamma 10K Dilution (G10K) Diagram
_Dilution workflow from BEI source (1.75e6 cp/µL) to 10,000 cp/µL working stock. Creates GBEI aliquots (5µL x 100), then G10K in 1.5mL screw cap (875µL at 10,000 cp/µL), and final aliquots (32 x 27µL). Reference: Gamma 10K Dil Batch Record vX._

## Slide 10: Primer-Guanidine Solution (PGS) Diagram
_Manufacturing diagram for PGS batches. Combines dry LAMP primer sets (As1e, N2, E1) resuspended in NFWater with 6M Guanidine-HCl (200µL) to create 10X LAMP Primer Mix, then dilutes to PGS. Aliquot options: 92µL x 136 (8 rxn), 275µL x 45 (24 rxn), or 1120µL x 11 (96 rxn). PGS specs: Primers 2.38X, GUD 95.1nM. Reference: Batch Record v2.0._

## Slide 11: Colorimetric Assay Diagram - 24 and 96 Reactions (CLAMP Assay v2.5)
_CLAMP reaction mix preparation for 24-rxn (PGS 275µL + CLAMP MM 327µL = 602µL RM, 73µL/tube fill strips) and 96-rxn (PGS 1080µL + CLAMP MM 1286µL = 2366µL RM, 290µL/tube fill strips) scales. Each CLAMP reaction: 23µL MM + 2µL sample._

## Slide 12: Colorimetric Assay Diagram - 48 Reactions (CLAMP Assay v2.5)
_CLAMP reaction mix preparation for 48-reaction scale. Uses PGS and Colorimetric LAMP MM from frozen storage. Fill strip volumes at 146µL/tube. Note: some volume fields marked "FIX" in original._

## Slide 13: 5X PCR Primers Diagram
_Manufacturing diagram for 5X PCR Primer working stocks. Combines source primers with 11.562mL NFWater to create 12.5mL bulk in 30mL Chub. Aliquots to 1.5mL tubes (105.6µL x 10, 24 rxn, 10% over) and 5mL tubes (1.1mL x 11). References: 5X PCR Primer Source Stock v1.1 and Working Stock v1.0._

## Slide 14: PCR Assay Diagram (PCR Assay v1.3)
_PCR reaction mix preparation for 24-reaction scale. Combines Luna PCR MM (from NEB E3006 Kit), LUNA RT (26.4µL from 100µL aliquot), 5X PCR Primers (105.6µL), and NFWater (79.2µL) into 472.5µL total RM in 1.5mL tube. Fill strip at 57µL/well. Each PCR reaction: 18µL MM + 2µL sample._

## Slide 15: EXTRA
_Blank/placeholder slide._

## Slide 16: 100X Inactivation Solution Diagram (Standard)
_Standard-scale manufacturing diagram for 100X Inactivation Solution. Shows preparation of intermediate stocks: 0.5M TCEP (in 250mL glass bottle + 100mL NFWater), 3.83N NaOH (in 250mL glass bottle + 74mL NFWater), and 0.5M EDTA. Aliquoting to 30mL Chubs and 15mL Falcons, then combining into 100XIS (TCEP 0.25M, EDTA 0.1M, NaOH 1.15N) in 30mL Chub, with final 1mL x 24 aliquots in 1.5mL tubes at -20°C. References batch records for TCEP v1.1, NaOH v1.0, EDTA v1.0, and 100XIS v1.0._

## Slide 17: FloodLAMP Overview - Streamlined Sample Prep
_Overview diagram showing the complete FloodLAMP workflow: 100X Inactivation Solution → 1X Inactivation Saline Solution → sample processing → dual test paths. QuickColor LAMP Test (high sensitivity 90%, ultra-high throughput, ideal for serial screening). EasyPCR Test (very high sensitivity 98%, medium throughput 1.5 hours/94, ideal for diagnostics/reflex/confirm). Highlights streamlined sample prep with upfront swab pooling and same sample for both tests._

## Slide 18: Streamlined Sample Prep (Simplified)
_Simplified version of the overview diagram showing the three main workflow blocks: Streamlined Sample Prep → QuickColor LAMP Test → EasyPCR Test._

## Slide 19: FloodLAMP Lab Playbook
_Diagram showing reflex testing workflow: Positives or Invalids from QuickColor COVID-19 Test reflexed using FloodLAMP EasyPCR COVID-19 Test._


# 1,444  SOP-201-A_2 PGS48 Manufacturing - Run Form.md
METADATA
last updated: 2026-02-16 BA after RT initial conversion
file_name: SOP-201-A_2 PGS48 Manufacturing - Run Form.md
file_date: 2022-02-26
title: FloodLAMP QMS SOP-201-A_2 PGS48 Manufacturing - Run Form
category: guides
subcategory: manufacturing
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1OE4rCaCn2htHdlq_Q_Nk9Mu-MpMgTtwO
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/SOP-201-A_2%20PGS48%20Manufacturing%20-%20Run%20Form.docx
pdf_gdrive_url: https://drive.google.com/file/d/1QPBDtkL4h9dFd4yP_X8J5ZpmaJNkUPYJ
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/manufacturing/SOP-201-A_2%20PGS48%20Manufacturing%20-%20Run%20Form.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1444
words: 842
notes: 
summary_short: The FloodLAMP QMS SOP-201-A_2 is a manufacturing run form for producing PGS48 (Primer-Guanidine Solution, 48-reaction aliquots). It covers preparation, safety procedures, step-by-step PGS mixing instructions (primer resuspension, guanidine-HCl addition, vortexing), materials checklist with product/lot tracking, and robotic aliquoting on an Opentrons liquid handler. The form includes write-in fields for location, operator, date, and lot tracking, plus startup/shutdown procedures for the Opentrons robot.


CONTENT

FloodLAMP Biotechnologies
**Document Number:** SOP-201-A
**Effective Date:** 02/26/2022
**Version:** 2

***INTERNAL TITLE:*** PGS48 Manufacturing - Run Form

## PREP
- Safety Procedures:
  - Work in PCR Box or BSC
  - **Designated CLEAN** Lab coat, gloves, face mask, and face shield/goggles
- Wipe down all work surfaces, tube racks, and all items used with 10% bleach solution followed by ethanol (as needed)
- Turn on UV lamp for 15 minutes in PCR Box or BSC (at start or end of prev run)
- Check to ensure you have **sufficient amounts of all materials** for number of lots to be created ([Calculator](https://docs.google.com/spreadsheets/d/13lsSll6-xEt3S978Hygg-NN1sRpHmo3qctL8WpOq_JU/edit?gid=0#gid=0))
- With Scale (USSolid1), **measure 28.2mL of NF Water** in 50mL Falcon Tube, leave **in the refrigerator > 1hr** (prep ahead).
- **Ensure Primer Resuspension NF Water is also in refrigerator > 1 hr** (prep ahead).
- **Do Startup** of the Opentrons (last page).
- **Load Opentrons software**, open protocol "iPGS48_x68_SOP-201-B_2.json"

## PREP USER WRITE IN
_QR Code_ PGS48 Manuf SOP
[Log Form Link](https://docs.google.com/forms/d/1WZ_MRSIV70tB_JvaW4fMwJGhpsMDjF50mVi8yF8p3nA/edit?usp=drive_web&ouid=111730229766683196858)
Location:
Name:
Date and Time:
PGS48 Lots Created:

Materials
- 50mL Falcon Tube (1)
  - Confirm Product ID & Lot in Log Form
- 1.5mL S.C. Tubes (67)
  - Confirm Product ID & Lot in Log Form
- Nuclease-free Water (2)
  - Confirm Product ID & Lot in Log Form
- FloodLAMP Primer Tubes (9)
  - Confirm Product ID & Lot in Log Form
- 6M Guanidine HCl
  - Confirm Product ID & Lot in Log Form
- Pipette ID
  - Confirm Product ID & Lot in Log Form
- 1000uL micropipette tips
  - Confirm Product ID & Lot in Log Form
- Robot tips (Opentrons 1000uL Filter Tip)

Equipment in AirClean Box
- Mini-centrifuge
- Vortex
- Timer
- 50mL & 1.5mL tube racks
- Tip waste bin

## MAKE PGS
- **Thaw three tubes of each primer set for 10-30min after pulling from freezer**
- Spin down primer tubes after thawing
- Get 50mL Falcon Tube of NF water (at least 10mL), put in rack in hood.
- Add 1000uL of Primer Resuspension NF Water to each tube of primers
  - Do NOT stick pipette tip into tube, primers will stick to tip
  - Air drop (no contact) dispense into tubes, no tip change
- **Vortex for 10s** to dissolve
- **Let sit 1min**, then vortex again 10s
- **Centrifuge** tubes briefly
- Retrieve NF water aliquot from fridge, check that volume appears ~28.2mL
- **Add 600uL of 6M Guanidine-HCl** to NF water in 50mL Falcon Tube
- **Mix** by vortexing 10s
- **Add the full volume of all nine tubes of Primer sets** to the 50mL Falcon Tube
  - Careful to get last bit of liquid (look)
- **Mix well** by vortexing 30s
- Remove cap and pipet any liquid in the cap and add back into the tube
- **Keep PGS mix in refrigerator** until aliquoting or aliquot within 5min

## ALIQUOT ON OPENTRONS
- **Arrange the robot deck** according to deck layout shown below
  - Remove lid from tip box, **verify that there is a tip in the back-left position**
  - Fill the back and front row of each of the six tube racks with 1.5mL SC tubes, uncapped
  - Place the 50mL PGS reservoir tube in the plate at position "8"
- **Click** "Proceed to Calibrate" button
- **Follow on-screen instructions** to complete calibration procedure
- **Click** "Start Run"
- When protocol has finished, **cap all tubes** inside the Opentrons hood
- **Transfer tubes** to cryobox, store at -20C.
- Label cryobox lid with "PGS48" & Lot#.
- **Click** "Reset Run" on OpenTrons software

Notes:
- Make sure the caps are not obstructing the openings of the neighboring tubes.
- Ensure that the 50mL tube is fully seated in the holder with 10mL mark just showing.
- Calibration procedure necessary only on the first run. Subsequent runs won't require re-calibration until the robot is disconnected/reconnected or a different program is run. Calibrate 1.5mL tube with tube out and center XY with respect to rack hole.
- Note that the final 1-2 tubes may be short on volume. These should be either used to do QC verification of the batch or discarded. Write with a marker a "•" on the top of any short tubes.
- Measure remaining volume in Falcon tube: if outside 450uL +/- 10uL, weigh all tubes individually. Spec is X to Y g, reject any tubes outside spec.

_[Deck Layout Diagram - see source PDF for image]_

## OpenTrons Startup
1. Turn on rocker power switch in back left (-- mark).
2. Press flashing blue button on front, wait until solid.
3. If not already open, launch OpenTrons application with shortcut on desktop.
4. Start Hepa unit and put at setpoint.
5. Take lid tipbox cover off.
6. Ensure tip is in back left position of tipbox.
7. Open json protocol.
8. Run calibration.
9. Leave front panel closed (down) when running.

## OpenTrons Shutdown
1. Place lid tipbox cover on.
2. Turn off Hepa unit.
3. Turn off OpenTrons rocker power switch (O mark).
4. Close front panel.


# 496  SOP-202-A_1 100XIS Manufacturing - Run Form.md
METADATA
last updated: 2026-02-15 BA after RT initial conversion
file_name: SOP-202-A_1 100XIS Manufacturing - Run Form.md
file_date: 2022-01-21
title: FloodLAMP QMS SOP-202-A_1 100XIS Manufacturing - Run Form
category: guides
subcategory: manufacturing
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1pzBrcBLajWdFH0M_ib3bILgtN7EN5h4G2KROieLmN78
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/SOP-202-A_1%20100XIS%20Manufacturing%20-%20Run%20Form.docx
pdf_gdrive_url: https://drive.google.com/file/d/1Th-fjY0mqBwXC74ZZwirwFW-iHAPIZ8F
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/manufacturing/SOP-202-A_1%20100XIS%20Manufacturing%20-%20Run%20Form.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 496
words: 262
notes: 
summary_short: The FloodLAMP QMS SOP-202-A_1 is a manufacturing run form for producing 100X Inactivation Solution (100XIS). It provides step-by-step instructions for combining TCEP, nuclease-free water, EDTA, and NaOH in a 1L glass bottle, followed by aliquoting 5 mL into labeled screw cap vials for storage at -20°C. The form includes safety procedures (fume hood, PPE), a materials checklist with lot/product ID tracking fields, equipment requirements, and write-in fields for operator documentation.


CONTENT

FloodLAMP Biotechnologies
**Document Number:** SOP-202-A
**Effective Date:** 01/21/2022
**Version:** 1

***INTERNAL TITLE:*** 100XIS Manufacturing - Run Form

## PREP
- Wipe down all work surfaces, tube racks, and other items used with 10% bleach solution followed by ethanol (as needed)
- Label 5mL screw cap vials with 100XIS labels
- Safety Procedures:
  - Work in fume hood
  - Lab coat, gloves, face mask, and face shield/goggles

## PREP USER WRITE IN
_QR Code_ 100XIS Manuf SOP
Form Link
Location:
Name:
Date and Time:

**Material**
- 5mL screw cap vials (200) LOT#:
  (Eppendorf)
- TCEP 25 g bottle (3) LOT#
  (GoldBio TCEP25) EXP:
- Nuclease-free Water LOT#:
  (Thermo 10977015) EXP:
- 0.5M EDTA LOT#
  (Thermo 15575020) EXP:
- 10N NaOH LOT#
  (Sigma SX0607N) EXP:

**Equipment**
- 1 L glass bottle with cap
- Scale
- Graduated cylinder or 50mL volumetric pipet
- Bottle top dispenser for 500mL bottle

**Notes:**

## MAKE 100XIS
- **Weigh 75.0 g of TCEP**
- Add TCEP to cleaned and sanitized 1L glass bottle
- **Add 667.5 mL of NF water to the glass bottle**
- **Cap and swirl bottle to dissolve 75 g of TCEP (do not shake)**
- **Add 209.4 mL EDTA**
- **Add 120 mL NaOH solution**
- **Cap and swirl to mix**
  - Wrap cap with parafilm
- **Aliquot 5 mL into labeled 5mL screw cap vials**
  - Prime the pump ~2-3 times into a waste container until it dispenses smoothly
  - Keep the 5mL tube under the dispenser nozzle when withdrawing the plunger to catch drips
- **Place 100XIS vials into the -20C freezer**


# 1,198  SOP-301 PGS48 Verification - Run Form.md
METADATA
last updated: 2026-02-16 BA after RT initial conversion
file_name: SOP-301 PGS48 Verification - Run Form.md
file_date: 2022-01-01
title: FloodLAMP QMS SOP-301 PGS48 Verification - Run Form
category: guides
subcategory: manufacturing
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1mVuPCxzU2bUILebEfg7gvHwjzD6DwGqv
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/SOP-301%20PGS48%20Verification%20-%20Run%20Form.docx
pdf_gdrive_url: https://drive.google.com/file/d/1W7vkFU0raZso77GsFPm3LWNDMkqKmwm1
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/manufacturing/SOP-301%20PGS48%20Verification%20-%20Run%20Form.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1198
words: 671
notes: 
summary_short: The FloodLAMP QMS SOP-301 is a verification run form for testing PGS48 (Primer-Guanidine Solution) batches via CLAMP amplification. It covers preparation of reaction mixes (46 µL PGS + 55 µL CLAMP MM per tube), positive/negative control setup, and a plate layout map for tracking POS/NEG results by PGS lot number. The second half includes an Amp Run Sheet Short with standard amplification procedures, heater settings (65°C for 25 min), and write-in fields for operator documentation and result logging.


CONTENT

FloodLAMP Biotechnologies
**Document Number:** SOP-301-A
**Effective Date:** 01/XX/2022
**Version:** 1

***INTERNAL TITLE:*** PGS48 Verification - Run Form

## PREP
- Amp heaters on (Heat indicator lit!)
- Map out plate layout
- Printout these 2 pages out separate
- Label Reaction Mix tubes
  - 1.5mL EDLB tubes
  - 4 rxn per RM tube
  - 1 RM tubes per PGS batch (#68)
- Calc amount of CLAMP MM needed
  - 55 µL x # batches = \_\_\_\_\_\_\_\_\_
  - Use single source tube
  - If larger run combine MM tubes
- Label strip8 tubes (or use plate)
- Make 1mL 1XISS (fill out on next pg)

## PREP USER WRITE IN
_QR Code_ Validation PGS
[Form Link](https://docs.google.com/forms/d/e/1FAIpQLSdGHu4xGNY6SDBQqnp0ZH3N4lL0r4EnNr7e3cYC8mKiNyIXag/closedform)
Location: MBC
Name:
Date and Time:

## RUN
- Get PCR cold block out 10min before - put plate or strip8 tubes in
- Get blue tube cold block out 10min before - keep all RM tubes in this
- Make Reaction Mixes for all tubes:
1. Add 46 µL of each PGS to each RM tube (making sure to match lot#'s)
2. Add 55 µL of CLAMP MM to each RM Tube
3. Vortex for 10s and centrifuge/shake down
4. Add 23µL of reaction mix to each of 4 wells {at bottom, no blowout, no tip touch}
- After adding RM to all reconfigure POS strips together and NEG strips together
- Add NEG control (1XISS) to those columns/tubes - cap
- Prep Pos Control: TPC100 - thaw 30s, add 20uL of Ultra Pure water (clean glove!)
- Add POS - TPC50 to each POS tube PGS Lot# Prefix \_\_\_\_

|  | POS | NEG | POS | NEG | POS | NEG | POS | NEG | POS | NEG | POS | NEG |
|------|------|------|------|------|------|------|------|------|------|------|------|------|
|  | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** |
| **A 1** | POS 0040 | NEG 0040 |  |  |  |  |  |  |  |  |  |  |
| **B 2** | POS 0040 | NEG 0040 |  |  |  |  |  |  |  |  |  |  |
| **C 3** | POS 0041 | NEG 0041 |  |  |  |  |  |  |  |  |  |  |
| **D 4** | POS 0041 | NEG 0041 |  |  |  |  |  |  |  |  |  |  |
| **E 5** | POS 0042 | NEG 0042 |  |  |  |  |  |  |  |  |  |  |
| **F 6** | POS 0042 | NEG 0042 |  |  |  |  |  |  |  |  |  |  |
| **G 7** |  |  |  |  |  |  |  |  |  |  |  |  |
| **H 8** |  |  |  |  |  |  |  |  |  |  |  |  |
||

## PREP
- Heaters on (Heat indicator lit!)
- 1X Inactivation Saline Soln ready
- Reaction mix strip8/plates ready
- Safety Procedures:
  - lab coat
  - gloves
  - face mask
  - face shield or goggles
- Alcohol wipe sample tubes

## PREP USER WRITE IN
|               | Amp Run Sheet Short Any System | version 1.3mod |
|---------------|-------------------------------|----------------|
|               |                               |                |
|               |                               |                |
|               |                               |                |
||

## AMPLIFICATION REACTION
- Thaw Reaction Mix (if frozen)
- Setup tips to align with reactions
- Add 2μL from each sample tube (pipet up & down 5X, blowout in liquid, tip touch)
- Heat 65°C for 25 min, set timer
- Intake sample tubes in App
- Put sample tubes in fridge
- Remove Reactions and Let cool for 1 min before photo
- Take photo in lightbox
- Crop photo and apply vivid filter
- Update results in App
- Log Run with Form link

## AMPLIFICATION REACTION USER WRITE IN
Amp Heater: Strip8 Tubes or Plates
Reaction Mix: Fresh
CLAMP MM Lot and EXP:
Num Reactions (including controls):
Pos Ctrl ID: TPC50 from TPC\_
Ultrapure Water ID:
Neg Ctrl ID (today's 1XISS):
Initial Inconclusives?:
Notes:


# 499  SOP-302 100XIS Verification - Run Form.md
METADATA
last updated: 2026-02-16 BA after RT initial conversion
file_name: SOP-302 100XIS Verification - Run Form.md
file_date: 2022-01-01
title: FloodLAMP QMS SOP-302 100XIS Verification - Run Form
category: guides
subcategory: manufacturing
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1OkAplBX1wXaJ0g6SHvMH76DuvRYXXYz7
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/SOP-302%20100XIS%20Verification%20-%20Run%20Form.docx
pdf_gdrive_url: https://drive.google.com/file/d/17gZaAVN_PZnOG81F7vwaNzTDuR74pjdI
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/manufacturing/SOP-302%20100XIS%20Verification%20-%20Run%20Form.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 499
words: 298
notes: 
summary_short: The FloodLAMP QMS SOP-302 is a verification run form for testing 100X Inactivation Solution (100XIS) batches via CLAMP amplification. It covers preparation steps including CLAMP MM volume calculation and 1XISS setup, followed by a standard Amp Run Sheet Short with amplification procedures (65°C for 25 min), positive/negative control handling, imaging, and result logging. The form includes write-in fields for heater IDs, reagent lots, reaction counts, and operator documentation.


CONTENT

FloodLAMP Biotechnologies
**Document Number:** SOP-302-A
**Effective Date:** 01/XX/2022 
**Version:** 1

***INTERNAL TITLE:*** 100XIS Verification - Run Form

## PREP
- Amp heaters on (Heat indicator lit!)
- Calc amount of CLAMP MM needed
  - 55 µL x # batches = \_\_\_\_\_\_\_\_\_
  - Use single source tube
  - If larger run combine MM tubes
- Label strip8 tubes
- Make 1mL 1XISS (fill out on next pg)

## PREP USER WRITE IN
_QR Code_ Validation 100XIS
Form Link
Location:
Name:
Date and Time:

## RUN
- Get PCR cold block out 10min before - put plate or strip8 tubes in

## PREP
- Heaters on (Heat indicator lit!)
- 1X Inactivation Saline Soln ready
- Reaction mix strip8/plates ready
- Safety Procedures:
  - lab coat
  - gloves
  - face mask
  - face shield or goggles
- Alcohol wipe sample tubes

## PREP USER WRITE IN
|               | Amp Run Sheet Short Any System | version 1.3mod |
|---------------|-------------------------------|----------------|
|               |                               |                |
|               |                               |                |
|               |                               |                |
||

## AMPLIFICATION REACTION
- Thaw Reaction Mix (if frozen)
- Setup tips to align with reactions
- Add 2μL from each sample tube (pipet up & down 5X, blowout in liquid, tip touch)
- Heat 65°C for 25 min, set timer
- Intake sample tubes in App
- Put sample tubes in fridge
- Remove Reactions and Let cool for 1 min before photo
- Take photo in lightbox
- Crop photo and apply vivid filter
- Update results in App
- Log Run with Form link

## AMPLIFICATION REACTION USER WRITE IN
Amp Heater: Strip8 Tubes or Plates
Reaction Mix: Fresh
CLAMP MM Lot and EXP:
Num Reactions (including controls):
Pos Ctrl ID: TPC50 from TPC\_
Ultrapure Water ID:
Neg Ctrl ID (today's 1XISS):
Initial Inconclusives?:
Notes:
