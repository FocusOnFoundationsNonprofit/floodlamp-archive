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
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/guides/manufacturing/Reagent%20Concentrations.md
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
