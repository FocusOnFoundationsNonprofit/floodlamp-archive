METADATA
last updated: 2025-12-15 RT updated metadata after BA fixed inconsistencies
file_name: FloodLAMP Test Validation Guide v1.0.md
file_date: 2021-06-28
title: FloodLAMP Test Validation Guide v1.0
category: guides
subcategory: test-validation
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1WMik-eNoPiJdfQMnzxj9BeptxJUZa_mPFeR--8nbLrI
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/test-validation/FloodLAMP%20Test%20Validation%20Guide%20v1.0.docx
pdf_gdrive_url: https://drive.google.com/file/d/1hhysHVm8TlpmvASuxvPQV5w4SSZmgKdH
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/test-validation/FloodLAMP%20Test%20Validation%20Guide%20v1.0.pdf
conversion_input_file_type: docx
conversion: gdoc markdown
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 5382
words: 3480
notes: 
summary_short: The FloodLAMP Test Validation Guide v1.0 outlines the validation workflow for the QuickColor and EasyPCR COVID-19 assays, including required equipment, kit reagents/supplies, inactivation and amplification procedures, and control/result interpretation criteria. It summarizes key performance metrics (LoD, clinical sensitivity/specificity) and defines two validation runs (controls-only and contrived-positive LoD series) to standardize qualification and troubleshooting across sites.


CONTENT

***INTERNAL TITLE:*** FloodLAMP Test Validation Guide
**EasyPCR(TM) COVID-19 Test**
**QuickColor(TM) COVID-19 Test**

Excerpts from DRAFT Instructions for Use\*

Protocol & Materials for Test Validation

\* Tests have been submitted to the FDA but have not been authorized or approved. 

www.floodlamp.bio
FloodLAMP Biotechnologies, PBC | 930 Brittan Ave. San Carlos, CA 94070 USA

## Overview
FloodLAMP’s QuickColor(TM) and EasyPCR(TM) COVID-19 Tests are streamlined, direct extraction-free molecular assays for the qualitative detection of RNA from the SARS-CoV-2 virus in upper respiratory specimens. They are validated for use with nasal swabs and full EUAs have been submitted to the FDA, including all *in silico*, wet testing, and clinical evaluation data. A summary of the EUA validation data is below. In addition, a pre-EUA for the FloodLAMP Home Collection Kit DTC was submitted on \[5-10-2021\], describing the clinical study design for unsupervised collection of pooled nasal swabs (up to 5). The clinical study also includes usability testing for the FloodLAMP Mobile App. FloodLAMP will conduct the clinical study under an approved IRB Protocol (from WIRB \#20210401) in coordination with a testing program to enrich for asymptomatic positives.

**FloodLAMP EUA Submission Validation Summary**
|  | EasyPCR(TM) COVID-19 Test | QuickColor(TM) COVID-19 Test |
| ----- | :---: | :---: |
| Limit of Detection | 3,100 copies/mL | 12,500 copies/mL |
| Clinical Sensitivity | 97.5% (39/40) | 90.0% (36/40) |
| Clinical Specificity | 100% (40/40) | 100% (40/40) |
||

The FloodLAMP QuickColor(TM) and EasyPCR(TM) COVID-19 Tests use the same inactivated sample, making validation and troubleshooting more straightforward. The inactivation process consists of adding freshly prepared 1X Inactivation Saline Solution, produced by adding 100X Inactivation Solution to 0.9% Saline. 1 mL of 1X Inactivation Saline Solution is used in each tube of up to 5 dry nasal swabs. The tube is vortexed for 30 seconds to elute the specimen from the swab. Next it's heated at a nominal 95°C for minutes and allowed to cool at room temperature for 10 minutes. The inactivated sample is then ready to be added to a prepared amplification reaction mix.

The tests only require a single pipette step and one filter tip per pool and the 1X Inactivation Saline Solution is efficiently dispensed by bottle top dispenser.  Small batch sizes can be run in as little as 45 minutes from sample to result for the QuickColor(TM) test, 1 hour and 40 min for EasyPCR(TM).

A team of 4 newly trained technicians can process approximately 2,500 tubes per 8 hr shift, totaling 10K people screened in pools of 4. Given the low infrastructure needed to run the QuickColor(TM) LAMP test, a distributed network of basic labs or processing sites can be supplied from a single lab that prepares ready to use assay plates and controls in bulk.

 FloodLAMP’s QuickColor(TM) and EasyPCR(TM) COVID-19 tests have very low consumable cost, on a per reaction and per person basis. Additionally, both tests are supply chain robust, using readily available chemicals and supplies.   
_Diagram of FloodLAMP Direct RNA Assays_

## Validation Runs
The FloodLAMP validation process for the EasyPCR(TM) and QuickColor(TM) tests comprises 2 runs:

- **1st Run** -  alternating positive and negative amplification controls and only materials provided in the FloodLAMP Validation Kit. 8 reactions in a single strip tube.
- **2nd Run** - inactivation of a contrived positive sample and preparation of dilution series between 100 and 1 cp/ul. Run consists of a preliminary LoD (full dilution series in triplicate) and a confirmatory LoD of 22 reps at 12.5 cp/µL for LAMP QuickColor(TM) and and 3 cp/µL for EasyPCR(TM).  48 reactions in each PCR plate.

The contrived positive in the 2nd Run is made by spiking a self-collected nasal swab sample with inactivated virus ( provided, gamma-irradiated SARS-CoV-2 virus cell lysate BEI NR-52287). The spiked sample is inactivated along with 3 unspiked samples, which are used together to make a dilution series to be used for the complete preliminary and confirmatory LoD runs (see Dilution Series spreadsheet, LoD plate map, and GCP100 Batch Record below). A positive and negative amplification control is also included in the 2nd Run. 
_Screenshot of Validation Kit Prep: Dilution Series_
_Screenshot of Table for QuickColor and EasyPCR LoD Configuration_
_Screenshot of GCP100 Batch Record v1.3_

## Equipment & Materials for Test Validation
### Equipment Required but not Provided
- Pipettors and filter pipette tips  
- Thermal Cycler or Heat Block - set at 65°C for LAMP Amplification Reaction (do not use heated lid)  
- BioRad CFX96 RT-PCR Instrument (or similar, see EasyPCRTMIFU for instructions on BioRad CFX96, QuantStudio 7 Pro and QuantStudio6 Flex)  
- Water Bath or Heater - set 99.9°C for Inactivation, prepare rack to hold 5ml transport tubes securely (recommend 4-way flipper racks). For heat block, it must hold 16mm tubes properly.  
- Bottletop Dispenser (optional) - typically used for larger runs (\> 100 samples)  
- Vortexer  
- Centrifuge

### Reagents Provided in FloodLAMP Validation Kit (room temp)
| Reagent Name (Label) | Photo | Amount | Conc. | Num Rxns | Purpose |
| ----- | :---: | :---: | :---: | :---: | :---: |
| 0.9% Saline Solution | _photo_ | 50 mL | 0.9% \= 154 mM | 50 at  1 mL/rxn | Making 1X Inactivation Saline Solution |
| 5M NaCl Thermo 24740011 | _photo_ | 15 mL | 5M | 500 | Source for making 0.9% Saline Solution (1 part 5M NaCl to 31.5 water)  and then 1X Inactivation Saline Solution |
| 100X Inactivation Solution (100XIS) | _photo_ | 4 x 1 mL | 100X | 400 | Making 1X Inactivation Saline Solution |
| Nuclease-free Water Thermo 10977015 | _photo_ | 1 mL |  |  |  |
||

### Reagents Provided  in FloodLAMP Validation Kit (dry ice)
| Reagent Name (Label) | Storage | Photo | Amount | Conc. | Num Rxns | Purpose |
| ----- | :---: | :---: | :---: | :---: | :---: | :---: |
| 5X PCR Primers (PCRP) Eurofins 12YS-010YST **(PCRP(Label)** | -20°C | _photo_ | 10 x 105µL | 5X | 10 x 24  \= 240 | EasyPCR(TM) Reaction Mix |
| PCR MM (NLMM) NEB Luna E3006 | -20°C | _photo_ | 737µL |  | \~\<72 | EasyPCR(TM) Reaction Mix |
| PCR RT (NLRT) NEB Luna E3006 | -20°C | _photo_ | 74µL |  | \~\<72 | EasyPCR(TM) Reaction Mix |
| Primer-Guanidine Solution for LAMP  (PGS) FloodLAMP PGS\_210427 | -20°C | _photo_ | 10 x 275µL |  | 10 x 24  \= 240 | Colorimetric LAMP QuickColor(TM) Reaction Mix |
| Colorimetric LAMP MM NEB M1804 | -20°C | _photo_ | 1mL | 2X | 72 | Colorimetric LAMP QuickColor(TM) Reaction Mix |
| Amp Positive Control (TPC) Twist 102019 & Thermo 4307281 | -80°C | _photo_ | 10 x 10µL | \~100 cp/µL | 10 x 4 rxn @ 2ul/rxn | Amplification Positive Control (should give \~32 Ct on EasyPCRTM) |
| Inactivated Virus (GBD) BEI NR-52287 | -80°C | _photo_ | 4 x 100µL | 1K cp/µL | 4  | Contrived Positive Sample creation. In 1ml, final conc. is 100 cp/µL |
||

### Assay Supplies Provided by FloodLAMP
| Item Description | Number | Vendor | Catalog Number |
| ----- | :---: | :---: | :---: |
| 8-Well PCR Strip & Cap | 10 | USA Scientific | 1402-2500 |
| 96-Well PCR Plate | 4 | Eppendorf | 951020303 |
| Optical Plate Seal | 3 | Thermo | 4311971 |
| Foil Plate Seal | 3 | Sigma | Z721549 |
| 1.5 mL Snap Cap | 20 | Eppendorf | 022431021 |
| 1.5 mL Screw Cap Tube | 5 | MTC Bio | C3150-SL |
| 5 mL Transport Tubes | 15 | MTC Bio | C1811 |
| 30 mL Tube | 3 | MTC Bio | C2630 |
||

### Nasal Swabs Provided by FloodLAMP
| Item Description | Number |
| ----- | :---: |
| Micro swab | 20 |
||

## Inactivation Solution
100X Inactivation Solution is provided. Active ingredients are TCEP and EDTA.

## Sample Preparation (wet swabs)
\* For wet swab specimens (swabs in saline or unprocessed swab elution): 

1) If samples are frozen, thaw unless no ice crystals are present and then keep on ice, cold block or at 4°C.   
2) Pulse vortex each sample and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.   
3) Wipe the outside of the sample tube with 70% ethanol.   
   
## Sample Inactivation (wet swabs, previously eluted)
1) Place the inactivation heater (a thermal cycler, water bath, dry heat bath or equivalent) in the BSC, turn on, and **set the temperature to hold at 100°C** .  
2) **Transfer 1 mL** or available volume of each sample to an appropriately labeled 1.5 mL or 5mL tube and securely cap.   
3) **Add 10μL per 1 mL sample volume of 100X Inactivation Solution, or 2μL per 0.1 mL sample volume of 50X Inactivation Solution** to each sample tube.  
4) **Vortex for 30 seconds**.  
5) Place sample tubes into the inactivation **heater for 8 minutes**.  
6) Remove sample tubes from the inactivation heater and let **cool at room temperature for 10 minutes**.  
7) Place sample tubes on ice, in the refrigerator, or on a cold block at **4°C until ready** to perform an amplification reaction. 
Note: Testing of inactivated specimens **must be conducted the same day** inactivation is performed. For long term storage, keep the original specimen at ≤-70°C. 

## Preparing to Run Assay for the First Time
For PCR and Fluorimetric LAMP tests that use RT-PCR Instruments, complete this section of the corresponding IFU prior to continuing. 

## Amplification Reaction Preparation
Common to all assays:
1) Place a 96-well PCR plate or PCR strip tubes onto a **cold block** or ice.  
2) **Thaw frozen reagents** until ice crystals are not present.   
3) Pulse vortex thawed reagents for 3 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
4) Store reagents on ice, in the refrigerator, or on a cold block at 4°C until ready to use.  
5) Prepare 96-well PCR plate or PCR strip tubes with amplification reaction mix

NOTE: For Colorimetric LAMP, optionally seal 96-well PCR plate with foil seal and add sample by piercing seal.

NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

NOTE: Colorimetric LAMP Negative Control must be prepared from 0.9% Saline and 100X Inactivation Solution. 

### Controls and Primers
|  | PCR | Colorimetric LAMP |
| ----- | :---: | :---: |
| Contrived Positive | Gamma BEI - GCP | Gamma BEI - GCP |
| Amp Positive Control | Twist - TFPC | Twist - TFPC |
| Negative Control | nuclease-free water | 0.9% saline with 1X Inactivation Solution |
| Primers  (Tube Label) | PCRP (5X PCR Primer Stock) | PGS (Primer-Guanidine Solution) |
||

## EasyPCR(TM) Amplification Reaction Preparation
1) Prepare the PCR Amplification Reaction by combining the components listed in the table below. 

     *NOTE: Component volumes should be scaled proportionally for the number of reactions.*  
     *NOTE: For 24 reaction scale, the PCR Master Mix and RT should be added to the tube*   
*containing the 5X PCR Primer Stock.*   

2) Vortex the PCR Amplification Reaction Solution for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
3) Add 18 µL of the PCR Amplification Reaction Solution into the wells of the PCR plate or strip tubes.

### EasyPCR(TM) Amplification Reaction Mix
| Component | Volume  (1 reaction) | Volume  (1 x 24 rxn w/ 9% overage) | Volume  (1 x 96 rxn w/ 4% overage) |
| ----- | :---: | :---: | :---: |
| 5X PCR Primer Stock | 4 µL | 105 µL | 400 µL |
| Nuclease-free Water | 3 µL | 79 µL | 300 µL |
| PCR Master Mix | 10 µL | 263 µL | 1000 µL |
| PCR RT | 1 µL | 26.3 µL | 100 µL |
| **SUBTOTAL VOLUME** | **18 µL** | **473 µL** | **1800 µL** |
| Sample | 2 µL | - | - |
| **REACTION VOLUME** | **20 µL** | - | - |
||

## Sample Addition (EasyPCRTM)
NOTE: Ensure that amp positive control and negative control are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Add 2 uL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
2) Mix by pipetting.  
3) If using PCR plate, optical seal (optionally using heat sealer). If using PCR strip tubes, cap strips.  
4) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.

Continue to section “Run the Assay” on pg. 20 of FloodLAMP EasyPCR(TM) PCR COVID-19 Test IFU.

### Thermal cycling and plate read steps for the Bio-Rad CFX96 TouchTM
| Stage | Temperature | Time | Reps |
| :---: | :---: | :---: | :---: |
| 1 | 52° C | 10 min | 1 |
| 2 | 95° C | 2 min | 1 |
| 3 | 95° C | 10 sec | 44 |
| 3 | 55° C \* | 30 sec | 44 |
||

## Test Controls (EasyPCRTM)
All test controls should be examined prior to interpretation of patient specimen results. If the controls are not valid and the expected result, the specimen results cannot be interpreted. Target results for the controls will be interpreted according to the table below.

- The “No Template” (Negative) Control (NTC) should yield a negative “not detected” result for both the N1 and RNaseP targets.  
- The Positive Template Control should yield a positive “detected” result for the N1 target and a negative “not detected” for the RNaseP control.  
- The Internal Process Control should yield a positive "detected" result for RNaseP. Detection of RNaseP is required to report a negative SARS-CoV-2 result. 

In the event of a failure of either the positive or negative control, the lab should discard some or all of the consumables utilized for associated run, including the filter tips, tubes, plates, seals, and aliquots of reagents. Additionally, all pipettes, BSC, and appropriate lab surfaces should be thoroughly cleaned with freshly made 10% bleach solution, 70% ethanol, and (optionally) RNAseZAP(TM) product. In the event of the failure of the positive control, the working aliquot of positive control material should be discarded. Additionally, the lab should review the expiration of the batch of positive control aliquots and verify their integrity by performing qualification reactions of one or more positive control aliquots. If controls continue to fail, labs should not perform additional tests on clinical specimens or report results. Invalid test results should be repeated by performing another amplification reaction.

## Patient Specimen Results Interpretation (EasyPCRTM)
NOTE: Patient specimen results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results. Use the below to assign a result to each sample.  

### EasyPCRTM: Interpretation of Assay Results
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

## QuickColor(TM) Colorimetric LAMP Amplification Reaction
1) Prepare the Colorimetric LAMP Amplification Reaction Mix by adding the Colorimetric LAMP MM to the Primer-Guanidine Solution per the volumes listed in the Table below. 

     *NOTE: Component volumes should be scaled proportionally for the number of reactions.*  
     *NOTE: For 24 reaction scale, the LAMP MM should be added to the tube containing the*   
*Primer-Guanidine Solution.* 

2) Vortex the Colorimetric LAMP Amplification Reaction Solution by for 10 seconds and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
3) Add 23 µL of the Colorimetric LAMP Amplification Reaction Solution into the wells of the PCR plate or PCR strip tubes.

NOTE: Reaction plates/strip tubes comprising the Colorimetric LAMP Amplification Reaction Solution may be prepared in advance, capped/sealed, and stored at -20°C for up to 3 days prior to addition of the sample.

### QuickColor(TM) Colorimetric LAMP Amplification Reaction

| Component | Volume  (1 reaction) | Volume  (1 x 24 rxn w/ 9% overage) | Volume  (1 x 96 rxn w/ 9% overage) |
| ----- | :---: | :---: | :---: |
| Primer-Guanidine Solution | 10.5 µL | 275 µL | 1100 µL |
| Colorimetric LAMP MM | 12.5 µL | 327 µL | 1310 µL |
| **SUBTOTAL VOLUME** | **23 µL** | **602 µL** | **2420 µL** |
| Sample | 2 µL | - | - |
| **REACTION VOLUME** | **25 µL** | - | - |
||

## Sample Addition and Heating (QuickColorTM)
NOTE: Ensure that positive and negative controls are included in each batch run (i.e. in each PCR plate or group of strip tubes that are heated together).

1) Turn on the amplification heater (a thermal cycler, water bath, dry heat bath or equivalent) and set the temperature to hold at 65°C.
NOTE: Amplification heater should be located in a separate, dedicated BSC or area of the lab. Proper cross contamination prevention practices are required, such as glove changes, to prevent amplicon contamination.
2) Add 2 μL of each sample into a separate tube in the amplification reaction PCR plate or strip tubes.   
3) Mix by pipetting.  
4) If using PCR plate, seal with foil seal, optical seal (optionally using heat sealer). If using PCR strip tubes, cap strips.  
5) Pulse vortex and briefly spin down in a centrifuge to collect the liquid at the bottom of the tube.  
6) Place the plate or strip tubes in the heater and set timer for 25 minutes.  
7) Remove the plate or strip tubes from the heater after 25 minutes.  
8) Let cool for 1 minute and then interpret the test results.

Continue to section "Test Controls" on pg. 17 of FloodLAMP QuickColor(TM) COVID-19 Test IFU.

## Patient Specimen Results Interpretation (QuickColorTM)
NOTE: Patient specimen results can only be interpreted if the positive and negative controls in the plate or group of strip tubes have the expected results.

Test results should be read at least 1 minute and no more than 8 hours after plates or tubes have been removed from heat. Test results may be determined directly from visual inspection of the color of the reaction tubes: 

- yellow - result is positive  
- bright pink or red - result is negative  
- any other color - result is invalid. 

Examples are shown below. Edge cases for positive and negative results are shown below. Any color variance stronger than the edge cases should be interpreted as inconclusive. In order to reduce the chance of both false negative and false positive results, this window for color variance is intentionally set to be small.

If the initial test is inconclusive, then one of the following should be performed:  
1) repeat the Colorimetric LAMP Amplification Reaction on the inactivated sample. If the repeat test has a positive result then the final interpretation of the test is positive. If the repeat test has a negative or another inconclusive result, then the final interpretation is inconclusive.  
2) follow-up test the inactivated sample with the FloodLAMP EasyPCR(TM) COVID-19 Test or another high sensitivity EUA authorized test that comprises the same inactivation protocol. The final interpretation is the result of the follow-up test.

If the final interpretation of the test result is inconclusive, then "Inconclusive" should be reported and retesting of the individual is recommended.

_Photo Figure 2 Example of Test Results (Left 2 Negative, Right 2 Positive where Negative are bright red in color, and Positive are bright yellow in color)_
_Photo Figure 3 Edge Case Test Results (Left Negative, Right Positive) where Negative is somewhat pink in color compared to bright red, and Positive is somewhat orange in color compared to bright yellow_

**Figure 2. Example of Test Results (Left 2 Negative, Right 2 Positive)**

**Figure 3. Edge Case Test Results (Left Negative, Right Positive)**

## Validation Kit Photos
_photo showing Room Temperature Box, Inactivation & Assay Box (-dry ice), and PositiveControl Box (dry ice)_

## Contact
email: randy@floodlamp.bio		phone: 415-269-2974

## Notes and Suggestions
