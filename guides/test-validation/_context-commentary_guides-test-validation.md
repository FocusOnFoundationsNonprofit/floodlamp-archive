METADATA
last updated: 2026-03-16 RT
file_name: _context-commentary_guides-test-validation.md
category: guides
subcategory: test-validation
gfile_url: https://docs.google.com/document/d/1SAV2Xaj7PxRepMAQGeuBhy7vCf3r_1traljR6saWMcg
words: 921
tokens: 1329


CONTENT

## Context
This `guides/test-validation` subcategory contains two formal protocol documents — the `2021-03-10_Clinical Eval Guide - from FloodLAMP IFU DRAFTS` and the `FloodLAMP Test Validation Guide v1.0` (June 2021) — both derived from FloodLAMP's draft Instructions for Use (IFU) for its COVID-19 molecular assays. They are self-contained, externally-facing technical documents.

Both documents share a common parent: the draft IFUs for FloodLAMP's EasyPCR and QuickColor COVID-19 tests. Large sections of bench procedure — sample preparation, sample inactivation, amplification reaction preparation, and sample addition — are nearly word-for-word identical between them. The core protocol steps (1 mL sample transfer, 100X Inactivation Solution, 30-second vortex, 8 minutes at 100°C, 10-minute cool-down, 2 µL sample addition into prepared reaction mixes) are shared verbatim. Per-reaction volumes are the same: 18 µL reaction mix + 2 µL sample = 20 µL for EasyPCR; 23 µL reaction mix + 2 µL sample = 25 µL for QuickColor (Colorimetric LAMP).

The Clinical Eval Guide was written for a specific clinical evaluation at Stanford University's clinical laboratory in March 2021, for the FDA EUA submissions. It covers three assays — EasyPCR, QuickColor (Colorimetric LAMP), and QuickFluor (Fluorimetric LAMP) — and includes the full recipe for preparing the 100X Inactivation Solution from raw components (TCEP, EDTA, NaOH, nuclease-free water) as well as the Primer-Guanidine Solution from 10X LAMP Primer Mix and Guanidine HCl. The equipment and materials lists are organized simply by what the lab provides versus what FloodLAMP ships.

The Test Validation Guide, dated June 2021, represents a later and more mature version of the protocol. It covers only two assays — EasyPCR and QuickColor — having dropped the Fluorimetric LAMP assay (QuickFluor). The fluorimetric readout was redundant: if a site had a PCR machine, EasyPCR already served that role. FloodLAMP seldom ran the fluorimetric test internally, and none of the pilot sites used it. Importantly, the performance of this test, as we developed it, was considerably worse compared to the PCR and colorimetric LAMP tests (in terms of Limit of Detection). Key differences from the earlier guide include: pre-made 100X Inactivation Solution and pre-mixed Primer-Guanidine Solution (PGS) shipped as part of a formalized validation kit, eliminating the need for sites to prepare these reagents from raw components; detailed kit contents with photos, catalog numbers, exact amounts, concentrations, and number of reactions supported; a structured two-run validation process (Run 1: alternating positive and negative amplification controls in strip tubes; Run 2: contrived positive sample with LoD dilution series in 48-reaction plates); performance data from the EUA submission (LoD of 3,100 cp/mL for EasyPCR and 12,500 cp/mL for QuickColor; clinical sensitivity of 97.5% and 90.0% respectively; 100% specificity for both); Ct-value thresholds and color interpretation criteria for result reporting; thermal cycling parameters for the Bio-Rad CFX96; and 24-reaction scale volumes alongside the 96-reaction scale.

The progression from the Clinical Eval Guide to the Test Validation Guide reflects FloodLAMP's progress over several months — from a bench protocol for generating clinical evaluation data at one specific lab to a more polished, kit-based validation document designed for broader distribution to potential partner labs and organizations.

Connections to other parts of the archive:
- the clinical evaluation data generated using the Clinical Eval Guide formed the core of the March 22, 2021 FDA EUA submissions, which are documented in the `regulatory/fl-fda-submissions` subcategory along with sample sizes, concordance results, and other validation data.
- the manufacturing processes for the reagents referenced here (100X Inactivation Solution, PGS, primer stocks) are detailed in the `guides/manufacturing` subcategory.
- the pilot sites that eventually ran these assays are documented in the `pilots/pilot-sites` subcategory.


## Commentary
These two documents may be of the highest interest/value in the entire archive. They're self-contained, formal, and written for scientists and diagnostic professionals — the kind of documents you could hand to a qualified lab and they could run the test. That's exactly what happened with the Clinical Eval Guide: Stanford's clinical lab ran the test successfully on the first attempt, with no training, using only this guide and the materials we provided. That was a significant validation, not just of the assay performance, but of the documentation itself.

The Clinical Eval Guide dates to March 2021, right before the first round of full FDA EUA submissions. It still required the receiving lab to prepare the 100X Inactivation Solution and Primer-Guanidine Solution from raw components. By the time the Test Validation Guide was written in June 2021, the protocol had matured substantially. We were shipping pre-made reagents — the 100X Inactivation Solution and PGS — as part of a formalized validation kit with catalog numbers, photos, and exact quantities. The fluorimetric LAMP assay (QuickFluor) had been dropped. It was redundant because EasyPCR already covered the PCR-machine use case, and its limit of detection was considerably worse than both other assays. We seldom ran it internally, and none of the pilot sites used it. Of note, none of our pilot sites used EasyPCR either (excluding our own internal staff plus community testing); QuickColor was the assay deployed in all operational surveillance programs.

The Test Validation Guide was not just for our own test sites though. It was created for potential partnerships and external sharing. We did actually share it with one major US healthcare company.

Looking at these two documents together, you can see the evolution from a lab-specific bench protocol to a transferable validation package. The core procedures remained the same, but everything around them — the kit design, the result interpretation criteria, the validation run structure — became more rigorous and more self-sufficient.
