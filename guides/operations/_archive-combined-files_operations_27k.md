METADATA
last updated: 2026-02-16 RT
file_name: _context-commentary_guides-operations.md
category: guides
subcategory: operations
words: 898
tokens: 1145


CONTENT

## Context
The operations subcategory contains three files addressing the organizational and logistical underpinnings of FloodLAMP's testing programs. Unlike the test-site subcategory, which houses the protocols, setup guides, and training materials that front-line test administrators and staff used,  these files capture the higher-level planning: what the economics looked like, what inventory was required, and what primers needed to be ordered.

The Cost Model is a working spreadsheet that modeled cost-of-goods-sold at various production scales. It reflects the iterative process of understanding what decentralized LAMP-based testing would actually cost, tracking the relative weight of each cost driver — from the dominant NEB LAMP master mix down to individual consumables and labor. Multiple versions were produced as the operation evolved; this represents one of the more mature iterations.

The Inventory Dashboard was a practical tracking tool for cataloging everything from pipettes and heat blocks to biohazard bags and collection swabs. It gives a concrete picture of the material complexity involved in running FloodLAMP's pop-up lab model. This involved dozens of distinct items spanning reagents, consumables, equipment, lab supplies, collection materials, and training kits. FloodLAMP also used Airtable and other systems for inventory management; the dashboard here is one view of a broader logistics effort.

The LAMP Primers document specifies the primer sets (derived from the Rabe–Cepko protocol) used for FloodLAMP's SARS-CoV-2 assay, along with ordering and handling specifications. Primer procurement was a key operational step — sourcing HPLC-purified primers at the required quantities and concentrations was not trivial, and this document captures the standardized ordering information that supported that process.

For readers wanting to explore the actual cost breakdowns, inventory details, or primer sequences, the source spreadsheets are included in the archive and are well-suited for AI-assisted exploration.


## Commentary
The operational and supply chain challenges were among the most persistent day-to-day problems we faced. Ideally, we would have contracted with a major distributor — Fisher Scientific, USA Scientific, or similar — to handle the full kitting of our lab supplies. In practice, that was not realistic for FloodLAMP given our volumes and lack of an EUA. No single supplier carried everything we needed, and given our unusual model of deploying pop-up labs in non-laboratory settings with non-laboratory staff, the selection of specific supplies and labware was deliberate. Some items could be substituted without issue, but others would create downstream problems if swapped. We eventually settled on a good set of materials, but the way we managed kitting and distribution was fundamentally not scalable. The scalability problem came from several converging factors: our small organizational size, operational inexperience, lack of established supplier partnerships, and the persistent iteration of kit compositions as the assay and protocols evolved. A more scalable approach would have combined top-down and bottom-up elements — standardized kit specifications and equipment bundles that established suppliers could assemble and ship, paired with clear documentation of acceptable substitutions and flexibility ranges so that smaller labs and pop-up operations could also source and validate their own combinations. 

A good example of this evolution is the tube barcoding process. Early on, we had interns manually applying barcode labels to collection tubes — a tedious, labor-intensive task. We then sourced custom QR-coded tubes from a Chinese manufacturer (Jable), which was a major improvement. However, the minimum order quantity was large and the lead time stretched to several months. During those waiting periods, we still had interns and TaskRabbit workers coming in to manually barcode tubes by hand for days at a time.

The swab and collection tube situation was another significant challenge. Like most testing operations during the pandemic, we had difficulty sourcing swabs. But our specific problem was harder than most: we needed a swab with a breakpoint that would leave the remaining tip and shaft fitting inside a reasonably sized tube, and would accommodate 4 swab tips for pooling. We settled on a 5mL tube as our main collection vessel (the mini system used 1.5mL tubes) and tried many tube-and-swab combinations before finding one that worked. The swab we ultimately adopted was, of all things, a urethral swab. We ended up ordering 100,000 swabs and tubes from Jable. We even hired a consultant to tackle the swab sourcing problem, but that effort didn't produce useful results.

For NEB's colorimetric LAMP master mix — by far our largest single cost item — we arranged for NEB to drop-ship directly to test sites for larger orders, which significantly streamlined logistics.

The core lesson from our operational experience is: simplify relentlessly. Every part you can eliminate reduces cost, training burden, and failure modes. Every standard, off-the-shelf item you can use in place of something custom reduces lead times and sourcing risk. For heating, we found that water baths, dry heat blocks, and even repurposed PCR machines all served as workable heaters — flexibility in equipment selection was critical given our resource-constrained deployments.

On the economics side, the NEB master mix dominated our reagent costs and we had limited leverage on pricing even at higher volumes. This was the key reagent of the test and NEB was a great company overall to work with. The cost model in the archive gives the full picture, and our per-person cost with pooling was competitive for the time. Future effort to bring LAMP-based screening to real scale would need to confront the enzyme cost dependency head-on — whether through alternative sourcing, in-house production, or fundamentally different assay chemistry.


# 11,317  Cost Model - FloodLAMP.md
METADATA
last updated: 2026-02-16 BA after RT initial conversion
file_name: Cost Model - FloodLAMP.md
file_date: 2022-10-29
title: FloodLAMP Cost Model
category: guides
subcategory: operations
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/18F8cJ7T0qBaF9k7fSI5S5kFisnrAayJfrjh1DQRoXuE
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/operations/Cost%20Model%20-%20FloodLAMP.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 11317
words: 5666
notes:
summary_short: The FloodLAMP Cost Model spreadsheet provides detailed cost-of-goods-sold (COGS) analysis for the pooled LAMP-based SARS-CoV-2 screening assay, broken down by reagents (primers, inactivation solution, NEB LAMP master mix), consumables (plastics, tips), collection kits, and labor at various production scales (50K to 1M reactions). It includes supplementary sheets for inactivation/binding solution chemistry costs, primer synthesis pricing, solution preparation recipes, NEB OEM master mix volume pricing, throughput modeling, and example school screening project economics.


CONTENT

## Cost Model
### 0) Details
Pool Size	4
mL per pool	1
450,000	Number of Rxns (Pools)	

### 1) Reagents
|                         |                                                                                                         |            |                          |       |               |             |                 |                  |                 |                                                              |                                                                                             |                                     |  |
|------------------------------------|---------------------------------------------------------------------------------------------------------|------------|--------------------------|-------|---------------|-------------|-----------------|------------------|-----------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------|--|
|                                    |                                                                                                         | Per 1K Rxn |                          |       | Cost / Person | Cost / Pool |                 |                  |                 |                                                              |                                                                                             |                                     |  |
| Saline (6 x 250mL bottles shipped) |                                                                                                         | 1,000      | $9                       | 0.4%  | $0.002        | $0.006      | $2,800          |                  |                 |                                                              |                                                                                             |                                     |  |
| Saline (.9% in 50mL Falcon tubes)  |                                                                                                         | 1,000      | $21                      | 1.4%  | $0.005        | $0.021      | $9,550          |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | mL per tube                                                                                             |            | $0                       | 50    |               |             |                 |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | overage to give                                                                                         |            | $0                       | 50%   |               |             | Cost per Source | Amount in Source | Units           | Amount per Pool                                              | Notes                                                                                       |                                     |  |
|                                    | 5M Saline                                                                                               |            | $0                       | 0%    | $0.000        | $0.000      | $141            | 10               | L               | 0.000031                                                     |                                                                                             |                                     |  |
|                                    | MilliQ Water                                                                                            |            | $0                       | 0%    | $0.000        | $0.000      |                 |                  |                 |                                                              | upfront cost then free                                                                      |                                     |  |
|                                    | 50mL Falcon Tube                                                                                        |            | $0                       | 28%   | $0.002        | $0.006      | $100            | 500              | tubes           | 0.020000                                                     |                                                                                             |                                     |  |
|                                    | Label                                                                                                   |            | $0                       | 1%    | $0.000        | $0.000      | $235            | 40,000           | tubes           | 0.020000                                                     | https://www.amazon.com/gp/product/B07D43PPFR/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1 | not chem one - actually use thermal |  |
|                                    | Labor                                                                                                   |            | $0                       | 71%   | $0.004        | $0.015      | $40             | 80               | tubes per hour  |                                                              | use new dispenser, labels too                                                               |                                     |  |
| Inactivation Soln (100XIS)         |                                                                                                         | 1,000      | $13                      | 0.8%  | $0.003        | $0.013      | $5,662          |                  |                 |                                                              | from 100X Inactiv Soln XL v1.0                                                              |                                     |  |
|                                    | Total volume in batch                                                                                   |            | $0                       | 340   | mL            |             |                 |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | Amount 100XIS per pool                                                                                  |            | $0                       | 0.01  | mL            |             |                 |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | overage to give                                                                                         |            | $0                       | 50%   |               |             | Cost per Batch  | Amount in Batch  | Units           |                                                              |                                                                                             |                                     |  |
|                                    | TCEP                                                                                                    |            | $0                       | 52%   | $0.0016       | $0.0065     | $222            | 25               | g               |                                                              |                                                                                             |                                     |  |
|                                    | EDTA                                                                                                    |            | $0                       | 3%    | $0.0001       | $0.0004     | $13             | 70               | mL              |                                                              |                                                                                             |                                     |  |
|                                    | NF Water                                                                                                |            | $0                       | 1%    | $0.0000       | $0.0001     | $4              | 122.5            | mL              |                                                              |                                                                                             |                                     |  |
|                                    | NaOH                                                                                                    |            | $0                       | 1%    | $0.0000       | $0.0001     | $2              | 40               | mL              |                                                              |                                                                                             |                                     |  |
|                                    | 5mL Screw Cap Tubes                                                                                     |            | $0                       | 6%    | $0.0002       | $0.0008     | $26             | 68               | tubes           |                                                              |                                                                                             |                                     |  |
|                                    | Labels                                                                                                  |            | $0                       | 0%    | $0.0000       | $0.0000     | $1              | 68               | labels          |                                                              | https://www.amazon.com/gp/product/B071LBQ1WT/                                               | Ultraduty Avery .5x1.75             |  |
|                                    | Labor                                                                                                   |            | $0                       | 37%   | $0.0012       | $0.0047     | $40             | 4                | hours per batch |                                                              |                                                                                             |                                     |  |
| Primer Soln (PGS)                  |                                                                                                         | 1,000      | $184                     | 12.0% | $0.046        | $0.184      | $83,006         |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | Num Rxn (Pools) per tube                                                                                | 48         |                          |       |               |             |                 |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | Tubes per Batch                                                                                         | 66         | for 3 x 3 sets = 9 tubes |       |               |             |                 |                  |                 |                                                              |                                                                                             |                                     |  |
|                                    | Primers                                                                                                 |            | $0                       | 92%   | $0.0424       | $0.1697     | $538            | 3168             | rxn             | Updated 9-27-22 RT                                           |                                                                                             |                                     |  |
|                                    | Guanidine                                                                                               |            | $0                       | 1%    | $0.0003       | $0.0011     | $3              | 600              | uL              |                                                              |                                                                                             |                                     |  |
|                                    | NF Water                                                                                                |            | $0                       | 0%    | $0.0001       | $0.0003     | $1              | 28.2             | mL              |                                                              |                                                                                             |                                     |  |
|                                    | 1.5mL Screw Cap Tubes                                                                                   |            | $0                       | 0%    | $0.0001       | $0.0003     | $1              | 66               | tubes           |                                                              |                                                                                             |                                     |  |
|                                    | Labels                                                                                                  |            | $0                       | 0%    | $0.0001       | $0.0004     | $1              | 66               | labels          |                                                              | https://www.amazon.com/gp/product/B071LBQ1WT/                                               | Ultraduty Avery .5x1.75             |  |
|                                    | Labor                                                                                                   |            | $0                       | 7%    | $0.0032       | $0.0126     | $40             | 1                | hours per batch |                                                              |                                                                                             |                                     |  |
| TPC                                | https://docs.google.com/spreadsheets/d/13JTbg_dRq5daE2OKo-OyOo2dmrQh-BpNlDFkkSvXmQs/edit#gid=1494347568 | 24         | $0.17                    | 0.3%  | $0.000        | $0.004      | $1,836          | 112.5            | plates          | $ total seems low but it's 5 tRNA sources and 1 Twist source |                                                                                             |                                     |  |
| CLAMP MM (NEB 1804 LAMP MM)        |                                                                                                         | 960        | $1,277                   | 86.5% | $0.333        | $1.330      | $598,500        |                  |                 |                                                              |                                                                                             |                                     |  |
| TOTAL REAGENTS                     |                                                                                                         |            |                          |       | $0.38         | $1.54       | $691,805        |
||

### 2) Consumables
|     |                            |            |         |         |               |             |          |          |  |  |  |  |  |
|-------------------|----------------------------|------------|---------|---------|---------------|-------------|----------|----------|--|--|--|--|--|
|                   |                            | Num per 1K | Cost Ea | Cost 1K | Cost / Person | Cost / Pool |          |          |  |  |  |  |  |
| Plastics          |                            |            |         | $205.75 |               | $0.21       |          |          |  |  |  |  |  |
|                   | 8-Well PCR Strip & Cap     | 125        | $0.67   | $83.75  |               |             |          |          |  |  |  |  |  |
|                   | 96-Well PCR Plate          | 15         | $4.92   | $73.80  |               |             |          |          |  |  |  |  |  |
|                   | Reagent Reservoir          | 20         | $0.96   | $19.20  |               |             |          |          |  |  |  |  |  |
|                   | Foil Plate Seal            | 30         | $0.58   | $17.40  |               |             |          |          |  |  |  |  |  |
|                   | 1.5 mL Snap Cap            | 50         | $0.13   | $6.50   |               |             |          |          |  |  |  |  |  |
|                   | 1.5 mL Screw Cap Tube      | 10         | $0.16   | $1.60   |               |             |          |          |  |  |  |  |  |
|                   | 5mL Transport Tube (blank) | 10         | $0.12   | $1.20   |               |             |          |          |  |  |  |  |  |
|                   | 50 mL Tube                 | 10         | $0.20   | $2.00   |               |             |          |          |  |  |  |  |  |
|                   | 15 mL Tube                 | 2          | $0.15   | $0.30   |               |             |          |          |  |  |  |  |  |
| Tips              |                            |            |         | $119.97 |               | $0.12       |          |          |  |  |  |  |  |
|                   | Tips_Univ_10uL             | 12         | $6.25   | $75.00  |               |             |          |          |  |  |  |  |  |
|                   | Tips_Univ_200uL            | 3          | $6.79   | $20.37  |               |             |          |          |  |  |  |  |  |
|                   | Tips_Univ_1000uL           | 3          | $8.20   | $24.60  |               |             |          |          |  |  |  |  |  |
| TOTAL CONSUMABLES |                            |            |         |         | $0.08         | $0.33       |          | Discount |  |  |  |  |  |
|                   |                            |            |         |         | $0.06         | $0.23       | $102,602 | 70%      |
||

### 3) Collection Kits
|                                      |                              |                    |                |                   |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|--------------------------------------------------------|------------------------------|--------------------|----------------|-------------------|---------------|-------------|---------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------|---------|-------|-------|
|                                                        |                              |                    |                |                   | Cost / Person | Cost / Pool |               |                                   |                                                                                                                                   | Price  | $4      | $5    | $6    |
| Full 4 Person Collection Kit - Sourced in Blister Pack |                              |                    |                |                   | $0.14         | $0.54       | $243,000      |                                   |                                                                                                                                   | Margin | 35%     | 48%   | 57%   |
| Bulk 4 Person Collection Kit - Sourced                 |                              | Num                | Cost Ea        | Cost SubT         | $0.18         | $0.72       |               |                                   | $0.65                                                                                                                             | $2.58  |         |       |       |
|                                                        | 1.5mL Tube                   | 1                  | $0.17          | $0.17             |               |             |               |                                   | Jable QR coded, 100K order                                                                                                        |        |         |       |       |
|                                                        | Swabs                        | 4                  | $0.07          | $0.28             |               |             |               |                                   | Jable UR 200K order, should come down to 2 cents in volume, but may go back up to 10 or more cents each for sterile medical swabs |        |         |       |       |
|                                                        | Biobag                       | 1                  | $0.05          | $0.05             |               |             |               |                                   | new 2x5 biobag price                                                                                                              |        |         |       |       |
|                                                        | Flyer                        | 1                  | $0.10          | $0.10             |               |             |               |                                   | should come way down to 1 cent or less                                                                                            |        |         |       |       |
|                                                        | Outer Zip Seal Bag           | 1                  | $0.12          | $0.12             |               |             |               |                                   | Need to get Uline price                                                                                                           |        |         |       |       |
| Full 4 Person Collection Kit - FL Made                 |                              | Num                | Cost Ea        | Cost SubT         | $0.23         | $0.93       |               |                                   | $0.70                                                                                                                             | $2.80  |         |       |       |
|                                                        | 1.5mL Tube                   | 1                  | $0.16          | $0.16             |               |             |               |                                   | comes down to 10 cents for SSI                                                                                                    |        |         |       |       |
|                                                        | QR Label                     | 1                  | $0.02          | $0.02             |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        | Labor to Apply label         | 1                  | $0.10          | $0.10             |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        | Swabs                        | 4                  | $0.08          | $0.32             |               |             |               |                                   | should come down to 2 cents in volume, but may go back up to 10 or more cents each for sterile medical swabs                      |        |         |       |       |
|                                                        | Baggie                       | 1                  | $0.01          | $0.01             |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        | Labor to put swabs in baggie | 1                  | $0.08          | $0.08             |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        | Biobag                       | 1                  | $0.06          | $0.06             |               |             |               |                                   | should come way down to 1 cent or less                                                                                            |        |         |       |       |
|                                                        | Outer Zip Seal Bag           | 1                  | $0.08          | $0.08             |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        | Labor to make CK             | 1                  | $0.10          | $0.10             |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
| Bulk 4 Person Collection Kit - FL Made                 |                              |                    |                |                   | $0.15         | $0.60       |               |                                   | $0.62                                                                                                                             | $2.46  |         |       |       |
|                                                        |                              |                    |                |                   |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        |                              |                    |                |                   | Cost / Person | Cost / Pool |               |                                   |                                                                                                                                   |        |         |       |       |
| TOTAL COGS                                             | $1,037,406                   | excluding shipping |                |                   | $0.58         | $2.31       | $1,037,406    |                                   |                                                                                                                                   |        |         |       |       |
| Number Rxns (Pools)                                    | 450,000                      | 1,800,000          |                |                   |               |             | $1,037,406.36 |                                   |                                                                                                                                   |        |         |       |       |
| COGS / Rxn (Pool)                                      | $2.31                        | $0.58              |                |                   |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        |                              |                    |                |                   |               |             |               | OLD CALCULATIONS - NEED TO REVIEW |                                                                                                                                   |        |         |       |       |
| Breakdown                                              | per rxn                      | %                  | $ for 450K rxn |                   |               |             |               | Labor to Pick and Ship            | 4                                                                                                                                 | $30.00 | $120.00 | $0.03 | $0.12 |
| Primers Source                                         | $0.17                        | 7.4%               | $76,376        |                   |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
| Other Reagents                                         | $0.04                        | 1.6%               | $16,928        | 100XIS Saline TPC |               |             |               | Price                             | $5.00                                                                                                                             | $6.00  | $7.00   | $8.00 | $9.00 |
| NEB CLAMP MM                                           | $1.33                        | 57.7%              | $598,500       | at least 290K rxn |               |             |               | COGS                              | $2.58                                                                                                                             | $2.80  | $2.80   | $2.80 | $2.80 |
| Lab Consmb (plastics)                                  | $0.23                        | 9.9%               | $102,602       | with 70% discount |               |             |               | Gross Margin                      | 48%                                                                                                                               | 53%    | 60%     | 65%   | 69%   |
| Collection Kit                                         | $0.54                        | 23.4%              | $243,000       |                   |               |             |               |                                   |                                                                                                                                   |        |         |       |       |
|                                                        | $2.31                        | 100.0%             | $1,037,406     |
||

| Number Rxns (Pools)   | 50,000  | 200,000 |               |                   |
|-----------------------|---------|---------|---------------|-------------------|
| COGS / Rxn (Pool)     | $2.64   | $0.66   |               |                   |
|                       |         |         |               |                   |
| Breakdown             | per rxn | %       | $ for 50K rxn |                   |
| Primers Source        | $0.17   | 7.4%    | $8,486        |                   |
| Other Reagents        | $0.04   | 1.6%    | $1,881        | 100XIS Saline TPC |
| NEB CLAMP MM          | $1.57   | 68.1%   | $78,500       | at least 72K rxn  |
| Lab Consmb (plastics) | $0.33   | 14.1%   | $16,286       | no discount       |
| Collection Kit        | $0.54   | 23.4%   | $27,000       |                   |
|                       | $2.64   | 114.6%  | $132,153      |
||

| Breakdown             | 50K   |        | 450K  |       | 1M    |     |
|-----------------------|-------|--------|-------|-------|-------|-----|
| Primers Source        | $0.17 | 100%   | $0.17 | 100%  | $0.17 | 9%  |
| Other Reagents        | $0.04 | 100%   | $0.04 | 100%  | $0.04 | 2%  |
| NEB CLAMP MM          | $1.57 |        | $1.33 |       | $1.13 | 59% |
| Lab Consmb (plastics) | $0.33 | 70%    | $0.23 | 70%   | $0.16 | 8%  |
| Collection Kit        | $0.54 | 100.0% | $0.54 | 80.0% | $0.43 | 22% |
|                       | $2.64 |        | $2.31 |       | $1.93 |
||

## Cost Model OLD
|  | Cost Per Pool | Pool Level | Pools / Day | People / Day | Cost / Sample |
| --- | --- | --- | --- | --- | --- |
| Low Scale | 3.5 | 4 | 2000 | 8000 | 0.875 |
| High Scale | 2.5 | 4 | 8000 | 32000 | 0.625 |
||

### Our Lab
|  |   |  |
| --- | --- | --- |
| Stations | 2 | 2 |
| Hrs / plate | 0.5 | 0.5 |
| Pools / plate | 94 | 90 |
| Pools / hr | 376 | 360 |
| Pools / 24hrs | 9024 | 8640 |
| Plates / 24hrs | 96 | 96 |
| Samples / pool | 4 | 20 |
| Samples / day | 36096 | 172800 |
| Samples / week | 252672 | 1209600 |
|  |  | $0.50 |
| Cost/Day |  | $86,400 |
||

### 1) Assay Consumable Cost (Plate Process)
|   |     |                      |     |                     |                       |                      |                          |       |             |        |
|-------------------------------------------|-----|----------------------|-----|---------------------|-----------------------|----------------------|--------------------------|-------|-------------|--------|
|                                           |     | High Scale $ / Assay |     | Low Scale $ / Assay | High Production Scale | Low Production Scale | Est. High Scale Discount |       |             |        |
| TCEP cost per primary pool (Inactivation) | 1%  | $0.01                | 1%  | $0.01               | estimate 100 g        | 10 g                 | 80%                      |       |             |        |
| Primers per pool                          | 15% | $0.15                | 7%  | $0.15               | 200K nmoles           | 50K nmoles           |                          |       |             |        |
| NEB 1804 LAMP MM                          | 75% | $0.75                | 86% | $1.93               | $1M                   | $20K                 |                          |       | Number Used | 94     |
| Filter Tips                               | 3%  | $0.03                | 2%  | $0.05               |                       |                      | 60%                      | $5.00 | 1           | $5.00  |
| Well Plates                               | 4%  | $0.04                | 3%  | $0.06               |                       |                      | 60%                      | $6.00 | 1           | $6.00  |
| Sealing Film                              | 1%  | $0.01                | 1%  | $0.01               |                       |                      | 60%                      | $0.68 | 2           | $1.36  |
| Tubes                                     | 0%  | $0.00                | 0%  | $0.00               |                       |                      | 60%                      | $0.20 | 1           | $0.20  |
| Reservoirs                                | 0%  | $0.00                | 0%  | $0.01               |                       |                      | 60%                      | $0.50 | 1           | $0.50  |
|                                           |     | $0.99                |     | $2.23               |                       |                      |                          |       |             | $13.06 |
||

### 2) Collection Consumables Cost
|     |                      |                |                 |  |  |  |  |  |  |  |
|-----------------------------------|----------------------|----------------|-----------------|--|--|--|--|--|--|--|
|                                   |                      | Low Pool Level | High Pool Level |  |  |  |  |  |  |  |
| Per Pool Collection Cost (tube)   | $0.20                | 4              | 20              |  |  |  |  |  |  |  |
|                                   | Coll Consmb / Person | Per Low Pool   | Per High Pool   |  |  |  |  |  |  |  |
| Per Person Collection Cost (swab) | $0.03                | $0.32          | $0.60           |  |  |  |  |  |  |  |
|                                   |                      | Per Person     | Per Person      |  |  |  |  |  |  |  |
|                                   |                      | $0.08          | $0.03           |
||

### 1 + 2) Assay + Collection Consumables
|  |                      |                |                 |                |                 |  |  |  |  |  |
|---------------------------------------|----------------------|----------------|-----------------|----------------|-----------------|--|--|--|--|--|
|                                       |                      | High Scale     |                 | Low Scale      |                 |  |  |  |  |  |
|                                       |                      | Low Pool Level | High Pool Level | Low Pool Level | High Pool Level |  |  |  |  |  |
|                                       |                      | 4              | 20              | 4              | 20              |  |  |  |  |  |
|                                       | Coll Consmb / Person | Per Low Pool   | Per High Pool   | Per Low Pool   | Per High Pool   |  |  |  |  |  |
| Per Person Collection Cost (swab)     | $0.03                | $1.31          | $1.59           | $2.55          | $2.83           |  |  |  |  |  |
|                                       |                      | Per Person     | Per Person      | Per Person     | Per Person      |  |  |  |  |  |
|                                       |                      | $0.33          | $0.08           | $0.64          | $0.14           |
||

### 3) Assay Labor
|                         |        |                     |                 |                      |                 |               |  |  |  |  |
|-----------------------------------------|--------|---------------------|-----------------|----------------------|-----------------|---------------|--|--|--|--|
|                                         | $/hr   | overhead            | $net/hr         | Paid hr/shift        | Assay hrs/shift | Salary / year |  |  |  |  |
| Assay Tech                              | $30    | 20%                 | $36             | 8                    | 6               | $60,000       |  |  |  |  |
|                                         |        |                     |                 |                      |                 |               |  |  |  |  |
| 2 techs 2 shifts / day                  | 4      | PLATE BASED PROCESS |                 |                      |                 |               |  |  |  |  |
| assay hrs / day                         | 24     | Low Pool Level      | High Pool Level |                      |                 |               |  |  |  |  |
| PLATE BASED PROCESS                     |        | 4                   | 20              |                      |                 |               |  |  |  |  |
| High Assay Throughput pools/hr (plates) | 94     |                     |                 |                      |                 |               |  |  |  |  |
| Pools/day                               | 2256   | 9,024               | 45,120          | People / Day         |                 | 24            |  |  |  |  |
| Assay Labor / Day                       | $1,152 |                     |                 |                      |                 |               |  |  |  |  |
| Assay Labor / Pool                      | $0.51  | $0.13               | $0.03           | Assay Labor / Person |
||

### 4) Intake + Inactivation Labor
| 4) Intake + Inactivation Labor |       |                |                 |                        |  |  |  |  |  |  |
|--------------------------------|-------|----------------|-----------------|------------------------|--|--|--|--|--|--|
|                                |       | Low Pool Level | High Pool Level |                        |  |  |  |  |  |  |
|                                |       | 4              | 20              |                        |  |  |  |  |  |  |
| Inactiv Throughput Pools / Hr  | 135   |                |                 |                        |  |  |  |  |  |  |
| Inactiv Labor Cost Per Pool    | $0.36 | $0.09          | $0.02           | Collect Labor / Person |
||

### 3 + 4) Assay + Inactiv Labor
|    |       |                |                 |  |  |  |  |  |  |  |
|--------------------------------|-------|----------------|-----------------|--|--|--|--|--|--|--|
|                                |       | Low Pool Level | High Pool Level |  |  |  |  |  |  |  |
|                                |       | 4              | 20              |  |  |  |  |  |  |  |
| Assay + Inactiv Labor / Pool   | $0.87 |                |                 |  |  |  |  |  |  |  |
| Assay + Inactiv Labor / Person |       | $0.22          | $0.04           |
||

### 1 + 2 + 3 + 4) Assay Consumables & Labor + Collection Consumables + Inactiv Labor
| |                      |                |                 |                |                 |  |  |  |  |  |
|-----------------------------------------------------------------------------------|----------------------|----------------|-----------------|----------------|-----------------|--|--|--|--|--|
|                                                                                   |                      | High Scale     |                 | Low Scale      |                 |  |  |  |  |  |
|                                                                                   |                      | Low Pool Level | High Pool Level | Low Pool Level | High Pool Level |  |  |  |  |  |
|                                                                                   |                      | 4              | 20              | 4              | 20              |  |  |  |  |  |
|                                                                                   |                      |                |                 |                |                 |  |  |  |  |  |
|                                                                                   | Coll Consmb / Person | Per Low Pool   | Per High Pool   | Per Low Pool   | Per High Pool   |  |  |  |  |  |
| Per Person Collection Cost (swab)                                                 | $0.03                | $2.18          | $2.46           | $3.42          | $3.70           |  |  |  |  |  |
|                                                                                   |                      | Per Person     | Per Person      | Per Person     | Per Person      |  |  |  |  |  |
|                                                                                   |                      | $0.54          | $0.12           | $0.85          | $0.18           |
||


|                                    | High Scale | %   | Low Scale | %   |
|------------------------------------|------------|-----|-----------|-----|
| Assay Consumables Cost             | $0.99      | 46% | $2.23     | 65% |
| Collection Consumables (swab tube) | $0.32      | 15% | $0.32     | 9%  |
| Assay Labor / Pool                 | $0.51      | 23% | $0.51     | 15% |
| Inactiv Labor Cost Per Pool        | $0.36      | 16% | $0.36     | 10% |
| **TOTAL**                          | **$2.18**  |     | **$3.42** |     |
||

### THROUGHPUT
|  |  | |
| --- | --- | --- |
| Intake and Inactiv Pools / Hr | 135 | |
| Intake and Inactiv Labor Unit | 1 low complexity tech | Bottle top dispenser, P1000 for PI, Water bath / Sous vide |
||

### INDIV CONFIRMATION WITH PCR
|  |  |
| --- | --- |
| 1 PCR Plate every X Hrs | 2 |
| Average pool size | 3.8 |
| Reps | 1 |
| Conf Pools Per Plate | 24 |
| Positivity | 0.05 |
| Screen Pools Per Hour | 240 |
| Conf Intake & Inactiv Per Hour | 47 |
||

There will be a larger intake time due to locating the bags of individual samples to confirm

## Inactiv BS Cost
|                                |       |           |
|------------------------------------------------|--------|-----------|
| Pool Level                                     | 4      |           |
| TCEP Rxn Conc mM                               | 2.5    |           |
| BS Rxn Conc M                                  | 2      | moles / L |
| BS Vol / Sample Vol                            | 0.5    |           |
|                                                |        |           |
|                                                | SALIVA | SWAB      |
| ml per Person                                  | 0.5    |           |
| ml per Pool                                    | 2      | 1         |
|                                                |        |           |
| CONFIG 1 - Inactiv Entire Pool then BS Aliquot |        |           |
| Inactiv Rxn ml                                 | 2      | 1         |
| TCEP cost / pool                               | $0.013 | $0.0064   |
| TCEP cost / person                             | $0.003 | $0.0016   |
|                                                |        |           |
| BS Rxn Vol ml                                  | 0.5    | 0.5       |
| BS ml / rxn                                    | 0.25   |           |
| NaI g / rxn                                    | 0.225  |           |
| BS cost / pool                                 | $0.042 | $0.021    |
| BS cost / person                               | $0.010 | $0.005    |
| Total cost / pool                              | $0.055 | $0.0273   |
| Total cost / person                            | $0.014 | $0.0068   |
||

| Product | Company | Product Number | Cost | Amount | Units | Cost/Unit | MW |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TCEP | Sigma - Millipore | 580567 | 241 | 5 | g | 48.2 | 287 |
| TCEP | Sigma - Calbiochem | C4706-10G | 380 | 10 | g | 38 | 287 |
| TCEP | Sigma | C4706-50G | 1810 | 50 | g | 36.2 |  |
| TCEP - liq 0.5M | Sigma | 646547-10X1ML | 96 | 10 | ml | 9.6 |  |
| TCEP | GoldBio | TCEP100 | 887 | 100 | g | 8.87 | 287 |
||

| Product | Company | Product Number | Cost | Amount | Units | Cost/Unit | MW | g / plate | plates / bottle | $ / plate | $ / rxn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NaI | Sigma | 793558-100G | 68 | 100 | g | 0.68 | 150 |  |  |  |  |
| NaI | Sigma | 793558-1KG | 338 | 1000 | g | 0.338 | 150 |  |  |  |  |
| NaI | Sigma | 217638-2.5KG | 766 | 2500 | g | 0.3064 | 150 | 23 | 108.695652 | 7.0472 | 0.073408 |
| NaI | Sigma | 383112-12KG | 2230 | 12000 | g | 0.185833 | 150 | 23 | 521.73913 | 4.274167 | 0.044523 |
||

## Example School
EXAMPLE SCHOOL SCREENING PROJECT - PIEDMONT
|              |  |
|------------------------------------|--------|
| Total Population Size              | 3,000  |
| Frequency (per week)               | 2      |
| Days per Week do Screening         | 5      |
| Population Pool Level              | 4      |
| Tubes Run per Day                  | 300    |
|                                    |        |
| Samples per Plate                  | 94     |
| Plates per Day                     | 3.2    |
|                                    |        |
| Collection Cost per 4 Pool         | $0.52  |
| Assay Cost per 4 Pool              | $2.23  |
| Consumables Cost per 4 Pool        | $2.75  |
| Consumables Cost per Plate         | $264   |
|                                    |        |
| Consumables Cost per Day           | $843   |
|                                    |        |
| Assay Techs per day                | 2      |
| Assay Tech Labor Cost / Day        | $576   |
|                                    |        |
| Consumables + AT Labor Cost / Day  | $1,419 |
| Consumables + AT Labor Cost / Week | $7,093 |
||

## Soln Prep
- For plate of dried pellets, to setup LAMP reaction:
- Get WGP from -20 freezer. WGP is water guanidine and primers

|          |          |             |            |  |                   |      |
|--------------------------------------------------------------|----------|-------------|------------|--|-------------------|------|
|                                                              |          | 96          | 10%        |  | 24                | 5%   |
|                                                              | ul / rxn | ul / 96 rxn | ul / plate |  | ml / batch plates |      |
| LAMP rxn volume                                              | 25       | 2,400       | 2,640      |  |                   |      |
|                                                              |          |             |            |  |                   |      |
| Water                                                        | 7.5      | 720         | 792        |  | 19.0              | 19.1 |
| Guanidine 10X .4M                                            | 2.5      | 240         | 264        |  | 6.3               | 6.4  |
| Primers 10X                                                  | 2.5      | 240         | 264        |  | 6.3               | 6.4  |
| WGP                                                          | 12.5     | 1,200       | 1,320      |  | 31.7              |      |
|                                                              |          |             |            |  |                   |      |
| LAMP MM                                                      | 12.5     | 1,200       | 1,320      |  |                   |      |
|                                                              |          |             |            |  |                   |      |
| ALL MM                                                       | 25       | 2,400       | 2,640      |  |                   |      |
|                                                              |          |             |            |  |                   |      |
|                                                              |          |             |            |  |                   |      |
|                                                              |          |             |            |  |                   |      |
| Pools / plate                                                | 92       |
||

### INACTIVATION SOLN
| TCEP                              | 25      | g / source bottle |  | Stable for 3 months at -20C |  |
|-----------------------------------|---------|-------------------|--|-----------------------------|--|
| MW                                | 287     | g / mole          |  |                             |  |
| Stock Conc                        | 0.5     | M                 |  |                             |  |
| Ultrapure Water needed            | 174     | ml                |  |                             |  |
| Final Conc in 100X IS             | 0.25    |                   |  |                             |  |
| Vol of 100X Inactiv Soln / source | 348     | ml                |  |                             |  |
| Vol of 100X Inactiv Soln / pool   | 1       | ml                |  |                             |  |
| uL of 100XISS per pool            | 10      | ul                |  |                             |  |
| Pools / source bottle             | 34,843  | pools             |  |                             |  |
| plates / 25g TCEP source bottle   | 378.7   | plates            |  |                             |  |
| Cost / 25g TCEP source bottle     | $225    |                   |  |                             |  |
| Cost / pool                       | $0.0065 |
||

| EDTA source bottle                | 100  | ml |
|-----------------------------------|------|----|
| Source Conc                       | 0.5  | M  |
| Final Conc in 100X IS             | 0.1  | M  |
| Vol of 100X Inactiv Soln / source | 500  | ml |
| Keying off TCEP for Vol 100X      | 348  | ml |
| EDTA source vol needed            | 69.7 | ml |
| Cost / EDTA 0.5M 100ml source     | $18  |
||

| NaOH source                  | 1000 | ml |
|------------------------------|------|----|
| Source Conc                  | 10   | N  |
| Final Conc in 100X IS        | 1.15 | N  |
| Keying off TCEP for Vol 100X | 348  | ml |
| NaOH source vol needed       | 40.1 | ml |
| Cost / NaOH source           | $55  |    |
| Cost NaOH / Batch IS         | $2   |
||

| Ultrapure Water Source        | 500    | ml |
|-------------------------------|--------|----|
| Keying off TCEP for Vol 100X  | 348    | ml |
| Ultrapure Water needed        | 64     | ml |
| Cost / Ultrapure Water Source | $17    |    |
| Cost Ultrapure / Batch IS     | $2     |    |
|                               |        |    |
| TOTAL COST Per Batch          | $247   |    |
| TOTAL COST Per Pool           | $0.007 |
||

### BINDING SOLN
|                |       |        |
|----------------------------|-------|--------|
| NaI 2.5kg                  | 2,500 | g      |
| Stock Conc                 | 7.6   | M      |
| MilliQ Water Needed        | 2,193 | ml     |
| NaI stock needed per plate | 19.75 | ml     |
| Plates / source            | 111.0 | plates |
| 10% Triton / plate         | 5     | ml     |
| Triton X100 - 50ml         | 50    | ml     |
||

- Use new bottle 500ml Ultrapure - pour out 100ml
- Weigh, add Triton X-100 then add additional water to correct weight
- Store in 5ml ED Screw Cap (not DNA LB)
- Store 250ul HCL 1N in tube

| B.S. used per sample | 0.25                            | ml |                             |    |                       |    |                          |  |                                |      |         |
|----------------------|---------------------------------|----|-----------------------------|----|-----------------------|----|--------------------------|--|--------------------------------|------|---------|
|                      |                                 |    |                             |    |                       |    |                          |  |                                |      |         |
| B.S. Component       | volume prep'd per source bottle |    | volume used per pool/sample |    | volume used per plate |    | plates per source bottle |  | source bottle supply duration: | 3    | months  |
| 7.6 M NaI            | 2193                            | ml | 0.1975                      | ml | 18.96                 | ml | 115.7                    |  |                                | 0.00 | bottles |
| 10% Triton           | 500                             | ml | 0.05                        | ml | 4.8                   | ml | 104.2                    |  |                                | 0.00 | bottles |
| 1N HCl               | 250                             | ml | 0.0025                      | ml | 0.24                  | ml | 1041.7                   |  |                                | 0.00 | bottles |
||

### ETHANOL - 80%
|                  |       |    |
|-------------------------------|-------|----|
| Ethanol - 100%                | 2,000 | ml |
|                               | $105  |    |
| Water for 80%                 | 500   | ml |
|                               | $17   |    |
| Total                         | $122  |    |
| Cost 80% EtOH / L             | $49   |    |
| Amount per pool for EtOH wash | 1     | ml |
| Pools / Batch                 | 2,500 |    |
| EtOH cost / pool              | $0.05 |
||

## NEB OEM M1804B
| Volume (mL) | $/mL   | # tubes    | $/tube  | $/rxn | Discount | total $    | total rxn | lead time | Num Rxn | Cost     |     |
|-------------|--------|------------|---------|-------|----------|------------|-----------|-----------|---------|----------|-----|
| 1,000       | 113.88 | 758        | $150    | $1.57 | 32%      | $113,880   | 72,727    | 3 weeks   |         |          | 85% |
| 2,000       | 104.72 | 1,515      | $138    | $1.44 | 38%      | $209,440   | 145,455   | 3 weeks   | 150,000 | $215,985 | 84% |
| 4,000       | 96.42  | 3,030      | $127    | $1.33 | 43%      | $385,680   | 290,909   | 3 weeks   |         |          | 83% |
| 10,000      | 86.42  | 7,576      | $114    | $1.19 | 48%      | $864,200   | 727,273   | 6 weeks   |         |          | 81% |
| 15,000      | 82.25  | 11,364     | $109    | $1.13 | 51%      | $1,233,750 | 1,090,909 | 6 weeks   |         |          | 80% |
|             |        |            |         |       |          |            |           |           |         |          |     |
|             |        | List Price | $221.40 | $2.31 |          |            |           |           |         |          |     |
|             |        |            |         |       |          |            |           |           |         |          |     |
|             |        |            |         |       |          |            |           |           |         |          |     |
|             |        | 300        | $150    | $1.57 |          | $45,096    |           |           |         |          |     |
|             |        | 200        | $150    | $1.57 |          | $30,064    |           |           |         |          |     |
|             |        | 182        | $150    | $1.57 |          | $27,359    |           |           |         |          |     |
|             |        | 100        | $150    | $1.57 |          | $15,032    |           |           |         |          |     |
|             |        | 81         | $150    | $1.57 |          | $12,176    |
||


# 11,671  Inventory Dashboard - FloodLAMP (Updated Aug 2022).md
METADATA
last updated: 2026-03-03 BA after RT initial conversion
file_name: Inventory Dashboard - FloodLAMP (Updated Aug 2022).md
file_date: 2022-08-29
title: FloodLAMP Inventory Dashboard (Updated Aug 2022)
category: guides
subcategory: operations
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1nbUmpJf2iGyJ4u03bYdk83R4k4-YOd9NJHYaG-zFV6k
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/operations/Inventory%20Dashboard%20-%20FloodLAMP%20%28Updated%20Aug%202022%29.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 11671
words: 5300
notes:
summary_short: The FloodLAMP Inventory Dashboard (Updated August 2022) tracks all supplies, reagents, equipment, and collection materials for the FloodLAMP pooled SARS-CoV-2 testing program, with current inventory counts at the Portola site, unit and bundle costs, product IDs, and a master inventory log with dates and notes across categories including lab consumables, reagents, equipment, lab supplies, collection materials, misc supplies, and training kits.


CONTENT

## Inventory and Costs
### Full Costs
| Standard System (with initial 1K consumables) |  |  |  |  |  |  $ 6,323  |
|-----------------------------------------------|--|--|--|--|--|-----------|
| Standard System (only)                        |  |  |  |  |  |  $ 2,882  |
| Mini System (with initial 1K consumables)     |  |  |  |  |  |  $ 4,954  |
| Mini System (only)                            |  |  |  |  |  |  $ 1,609  |
| Model 1K Consumables                          |  |  |  |  |  |  $ 3,498  |
||

### Current Inventory
Last Updated: 2022-08-29
By: Gary W

### Lab Consumables
| Description                    | Supply Type        | Inv_Portola | # in Bundle | Bundles | Cost (each) | Cost/Bundle |
|--------------------------------|--------------------|-------------|-------------|---------|-------------|-------------|
| 1000uL Universal Tip Box       | FL Ship - Standard | 77          | 3           | 25      |  $ 8.37     |  $ 25.11    |
| 200uL Universal Tip Box        | FL Ship - Standard | 108         | 3           | 36      |  $ 6.84     |  $ 20.51    |
| 10uL Universal Tip Box (Long)  | FL Ship - Standard | 121         | 10          | 12      |  $ 9.47     |  $ 94.69    |
| 10uL Universal Tip Box (Short) | FL Ship - Standard | 158         | 10          | 15      |  $ 5.68     |  $ 56.75    |
| 50mL Falcon Tube               | FL Ship - Standard | 500         | 10          | 50      |  $ 0.23     |  $ 2.30     |
| 30mL Chub Tube                 | FL Ship - Standard | 425         | 10          | 42      |  $ 0.29     |  $ 2.88     |
| 5mL Snap Tube                  | FL Ship - Standard | 260         | 20          | 13      |  $ 0.20     |  $ 4.01     |
| 1.5mL Snap Cap Tube            | FL Ship - Standard | 400         | 50          | 8       |  $ 0.06     |  $ 2.90     |
| PCR Strip8 Tubes and Caps      | FL Ship - Standard | 3,200       | 128         | 25      |  $ 0.72     |  $ 92.40    |
| 96-Well PCR Plate              | FL Ship - Standard | 1,020       | 10          | 102     |  $ 3.59     |  $ 35.90    |
| Foil Plate Seal                | FL Ship - Standard | 2,000       | 20          | 100     |  $ 1.12     |  $ 22.36    |
| Reagent Reservoir              | FL Ship - Standard | 950         | 10          | 95      |  $ 0.58     |  $ 5.78     |
|                                |                    |             |             |         |             |  $ 337.45   |
||

| FORMULAS                    |  |      |     |
|-----------------------------|--|------|-----|
| Reagent Reservoir           |  | 950  | 10  |
| 5mL Snap Tube               |  | 260  | 20  |
| 1.5mL Snap Cap Tube         |  | 400  | 50  |
| 30mL Chub Tube              |  | 425  | 10  |
| 50mL Falcon Tube            |  | 500  | 10  |
| 96-Well PCR Plate           |  | 1020 | 10  |
| PCR Strip8 Tubes and Caps   |  | 3200 | 128 |
| Foil Plate Seal             |  | 2000 | 20  |
| 1000uL Universal Tips       |  | 77   | 3   |
| 200uL Universal Tips        |  | 108  | 3   |
| 10uL Universal Tips - Long  |  | 121  | 10  |
| 10uL Universal Tips - Short |  | 158  | 10  |
||

| PRODUCT IDS                   |  |      |     |
|-------------------------------|--|------|-----|
| P_Reservoir_10mL_Oly          |  | 200  | 10  |
| P_Reservoir_5mL_H637          |  | 750  | 10  |
| P_Tube_5mL_snap_MTC           |  | 120  | 20  |
| P_Tube_5mL_snap_ED            |  | 100  | 20  |
| P_Tube_5mL_snap_CL            |  | 40   | 20  |
| P_Tube_1.5mL_EDLB             |  | 400  | 50  |
| P_Tube_30mL_ChubSS            |  | 425  | 10  |
| P_Tube_50mL_FalconOC          |  | 500  | 10  |
| P_PCR_96plate_USA200          |  | 1020 | 10  |
| P_PCRStrips_USA               |  | 3200 | 128 |
| P_FoilSeals_MTC               |  | 2000 | 20  |
| P_Tips_Univ_1000uL_Biotix     |  | 45   | 3   |
| P_Tips_Univ_1000uL_Gilson     |  | 32   | 3   |
| P_Tips_Univ_200uL_Biotix      |  | 108  | 3   |
| P_Tips_Univ_10uL_Biotix_long  |  | 121  | 10  |
| P_Tips_Univ_10uL_Oxf_short    |  | 90   | 10  |
| P_Tips_Univ_10uL_Biotix_short |  | 68   | 10  |
||

### Reagents
| Description                       | Supply Type        | Inv_Portola | # in Bundle | Bundles | Cost (each) | Cost/Bundle  |
|-----------------------------------|--------------------|-------------|-------------|---------|-------------|--------------|
| Primer Solution                   | FL Ship - Prep     | 659         | 22          | 29      |  $ 9.02     |  $ 198.44    |
| 100X Inactivation Solution        | FL Ship - Prep     | 204         | 3           | 68      |  $ 6.50     |  $ 19.50     |
| NEB Colorimetric LAMP Master Mix  |                    | 10          | 11          | 0       |  $ 216.00   |  $ 2,376.00  |
| Amplification Positive Control    | FL Ship - Prep     | 303         | 24          | 12      |  $ 0.17     |  $ 4.06      |
| Saline in Falcon tube 50mL        | FL Ship - Prep     | 65          | 10          | 6       |  $ 2.55     |  $ 25.50     |
| Saline in Bottle 250mL            | FL Ship - Standard | 5           | 1           | 5       |  $ 8.99     |  $ 8.99      |
|                                   |                    |             |             |         |             |  $ 2,632.49  |
||

| PRODUCT IDS         |     |       |
|---------------------|-----|-------|
| PF_PGS-48           | 659 | 31632 |
| PF_100XIS_5mL       | 204 |       |
| PF_Saline_50ml      | 65  |       |
| PF_TPC              | 303 |       |
| P_CLAMPMM_NEB_M1804 | 10  |       |
| P_Saline_NA250      | 5   |       |
| PF_GD50_5mL         |     |       |
| PF_GD50_1.5mL       |
||

### Collection Materials
| Description         | Supply Type        | Inv_Portola | # in Bundle | Bundles | Cost (each) | Cost/Bundle |
|---------------------|--------------------|-------------|-------------|---------|-------------|-------------|
| 1.5mL QR Coded Tube | FL Ship - Prep     | 4,700       | 1000        | 4       | $0.07       | $70.00      |
| 5mL QR Coded Tube   | FL Ship - Prep     | 98,000      | 1000        | 98      | $0.15       | $150.00     |
| Collecton Swab      | FL Ship - Standard | 200,000     | 4000        | 50      | $0.07       | $280.00     |
|                     |                    |             |             |         |             | $500.00     |
||

| PRODUCT IDS                  |        |
|------------------------------|--------|
| P_Tube_1.5mL_MBlueScrew      | 4700   |
| P_Swab_JableUR               | 200000 |
| P_ColTubeQR_5mL_Jable1       | 98000  |
| P_Tube_5mL_Transport_MTC     |        |
| P_Tube_1.5mL_SSI             |        |
| P_Bag_Slider_U6x9            |        |
| PF_CollectionPamphlet_v2_PDC |        |
| P_BioHazBag_D2x5             |
||

### Equipment
| Description                 | Supply Type    | Inv_Portola | # in Bundle | Bundles | Cost (each) | Cost/Bundle |
|-----------------------------|----------------|-------------|-------------|---------|-------------|-------------|
| Mini freezer                | Direct Ship    | 0           | 1           | 0       |  $ 241.50   |  $ 241.50   |
| Mini fridge                 | Direct Ship    | 0           | 1           | 0       |  $ 224.97   |  $ 224.97   |
| Water Bath                  | Direct Ship    | 3           | 1           | 3       |  $ 198.99   |  $ 198.99   |
| Dry Heater for Plate        | FL Ship - Prep | 9           | 1           | 9       |  $ 591.00   |  $ 591.00   |
| Mini Heater                 | FL Ship - Prep | 9           | 2           | 4       |  $ 175.99   |  $ 351.98   |
| Mini centrifuge             | Direct Ship    | 2           | 1           | 2       |  $ 87.99    |  $ 87.99    |
| Vortexer                    | Direct Ship    | 4           | 2           | 2       |  $ 100.00   |  $ 200.00   |
| Electric dispenser          |                | 12          | 1           | 12      |  $ 600.00   |  $ 600.00   |
| Manual dispenser            |                |             |             |         |             |             |
| Pipette 10-100 uL           |                | 6           | 1           | 6       |  $ 56.00    |  $ 56.00    |
| Pipette 100-1000uL          |                | 7           | 1           | 7       |  $ 56.00    |  $ 56.00    |
| Pipette Fixed 2uL           |                | 21          | 1           | 21      |  $ 56.00    |  $ 56.00    |
| Pipette 8-Channel  10-100uL |                | 7           | 1           | 7       |  $ 235.00   |  $ 235.00   |
|                             |                |             |             |         |             |  $ 2,899.43 |
||

| FORMULAS                    |  |    |   |
|-----------------------------|--|----|---|
| Mini freezer                |  | 0  | 1 |
| Mini fridge                 |  | 0  | 1 |
| Water Bath                  |  | 3  | 1 |
| Mini centrifuge             |  | 2  | 1 |
| Vortexer                    |  | 4  | 1 |
| Electric dispenser          |  | 12 | 1 |
| Dry Heater for Plate        |  | 9  | 1 |
| Pipette 10-100 uL           |  | 6  | 1 |
| Pipette 100-1000uL          |  | 7  | 1 |
| Pipette Fixed 2uL           |  | 21 | 1 |
| Pipette 8-Channel  10-100uL |  | 7  | 1 |
| Mini Heater                 |  | 9  | 1 |
||

| PRODUCT IDS               |  |    |   |
|---------------------------|--|----|---|
| P_FreezerMini_Whyn        |  | 0  | 1 |
| P_FridgeMini_hOm          |  | 0  | 1 |
| P_WaterBath_IVYX          |  | 3  | 1 |
| P_CentrifugeMini_4Es      |  | 2  | 1 |
| P_Vortexer_4Es            |  | 4  | 2 |
| P_Dispenser_Elec_Scilgx   |  | 12 | 1 |
| P_Dispenser_10mL_Microlit |  |    |   |
| P_HeatBlocks_96PCR_XX     |  | 3  | 1 |
| P_HeaterDry_96_BnchMB2    |  | 6  | 1 |
| P_Pipette_P100_Microlit   |  | 6  | 1 |
| P_Pipette_P1000_Microlit  |  | 7  | 1 |
| P_Pipette_P2F_Microlit    |  | 21 | 1 |
| P_Pipette8Ch_V100         |  | 7  | 1 |
| P_HeaterDry_96_SWSciXX    |  | 3  | 1 |
| P_HeaterDry_Mini_4Es      |  | 9  | 2 |
| P_HeatBlock_MiniPCR_BTL   |  |    |   |
| P_HeatBlock_MiniPCR_GBI   |  |    |   |
| P_HeatBlock_Mini_1.5mL    |  |    |   |
| P_Air_Purifier_Medify     |  |    |   |
| P_SensorPush_Sensor       |  |    |   |
| P_SensorPush_Gateway      |  |    |   |
| P_Cart_Homz               |  |    |   |
| P_Lightbox_D20            |
||

### Lab Supplies
| Description                    | Supply Type | Inv_Portola | # in Bundle | Bundles | Cost (each) | Cost/Bundle |
|--------------------------------|-------------|-------------|-------------|---------|-------------|-------------|
| Flipper racks (separate)       |             | 28          | 2           | 14      |  $ 5.67     |  $ 11.33    |
| Flipper rack blocks - 4 zipped |             | 11          | 1           | 11      |  $ 22.75    |  $ 22.75    |
| Light Blue 5mL 50 tube racks   |             | 10          | 2           | 5       |  $ 4.00     |  $ 7.99     |
| 1.5mL tube racks               |             | 4           | 2           | 2       |  $ 3.57     |  $ 7.13     |
| PCR racks                      |             | 26          | 2           | 13      |  $ 5.98     |  $ 11.96    |
| Hinged Box                     |             | 7           | 1           | 7       |  $ 5.04     |  $ 5.04     |
| 500mL Glass bottle             |             | 21          | 1           | 21      |  $ 12.75    |  $ 12.75    |
| Thermometers freezer           |             | 8           | 2           | 4       |  $ 13.58    |  $ 27.16    |
| Timers                         |             | 29          | 2           | 14      |  $ 1.66     |  $ 3.32     |
| PCR Cold Blocks                |             | 12          | 2           | 6       |  $ 31.53    |  $ 63.06    |
| Versi Rack                     |             | 18          | 1           | 18      |  $ 2.00     |  $ 2.00     |
| 3D LookUp racks 5mL x 48 HALF  |             | 12          | 1           | 12      |  $ 2.00     |  $ 2.00     |
| 3D LookUp racks 5mL x 96 FULL  |             | 19          | 2           | 9       |  $ 4.00     |  $ 8.00     |
|                                |             |             |             |         |             |  $ 184.49   |
||

| PRODUCT IDS               |    |
|---------------------------|----|
| P_ColdBlock_PCR_G         | 12 |
| P_GlassBottle_500mL_KAR   | 21 |
| P_Rack_1.5mL_OLY          | 4  |
| P_Rack_50Tubes_5mL_ULA    | 10 |
| P_Rack_Flipper            | 28 |
| PF_Rack_Flipper_4Block    | 11 |
| P_Rack_HingeBox           | 7  |
| P_Rack_PCR                | 26 |
| PF_Versirack              | 18 |
| P_ThermometersFreezer_ETH | 8  |
| P_Timers_LIN              | 29 |
| PF_Rack_LookUp_48Half_5mL | 12 |
| PF_Rack_LookUp_96Full_5mL | 19 |
| P_Baggies_3x4_SNL         |
||

### Misc Supplies
| Description                            | Supply Type | Inv_Portola | # in Bundle | Bundles | Cost (each) | Cost/Bundle |
|----------------------------------------|-------------|-------------|-------------|---------|-------------|-------------|
| Biohazard Baggies Small                |             | 230         | 50          | 4       | $0.40       | $20.00      |
| Biohazard Baggies Stand                |             | 0           | 1           | 0       | $27.07      | $27.07      |
| Calculator                             |             | 7           | 1           | 7       | $10.29      | $10.29      |
| Clipboard                              |             | 8           | 1           | 8       | $2.70       | $2.70       |
| Foil                                   |             | 27          | 2           | 13      | $9.88       | $19.76      |
| Lab Coat                               |             | 13          | 1           | 13      | $23.00      | $23.00      |
| Lightbox                               | Direct Ship | 0           | 1           | 0       | $16.44      | $16.44      |
| Pen (marked clean)                     |             | 15          | 1           | 15      | $1.56       | $1.56       |
| Razor Blades                           |             | 45          | 10          | 4       | $0.10       | $1.00       |
| Sharpie Twin Tip                       |             | 24          | 1           | 24      | $1.41       | $1.41       |
| Spray Bottle Set                       |             | 12          | 1           | 12      | $5.99       | $5.99       |
| Green Tape                             |             | 0           | 1           | 0       | $4.28       | $4.28       |
| Orange Tape                            |             | 0           | 1           | 0       | $4.28       | $4.28       |
| Tip Bucket                             |             | 6           | 2           | 3       | $3.00       | $6.00       |
| Bleach Concentrated 50mL               |             | 0           | 2           | 0       | $0.50       | $1.00       |
| Cryobox Cardboard                      |             | 0           | 1           | 0       | $1.60       | $1.60       |
| Hooks for Coats                        |             | 15          | 2           | 7       | $1.22       | $2.44       |
| Hooks Little                           |             | 15          | 2           | 7       | $0.42       | $0.84       |
| Signage Printouts in Manila Folder (8) |             | 11          | 1           | 11      | $0.10       | $0.10       |
|                                        |             |             |             |         |             | $149.76     |
||

| PRODUCT IDS              |     |
|--------------------------|-----|
| P_BioTrashBag_S          | 230 |
| P_BioTrashBag_Stand      | 0   |
| P_Calculator             | 7   |
| P_Clipboard              | 8   |
| P_Foil_UltraClean        | 27  |
| P_Gloves_Latex_M         | 11  |
| P_LabCoat_RK_L           | 6   |
| P_LabCoat_RK_M           | 5   |
| P_LabCoat_RK_S           | 0   |
| P_LabCoat_RK_XL          | 2   |
| P_LabWipes_L             | 13  |
| P_LabWipes_S             | 15  |
| P_Pen                    | 15  |
| P_RazorBlade_MBC         | 45  |
| P_SharpieTwinTip         | 24  |
| P_SprayBottle_Set        | 12  |
| P_Tape_Green             | 2   |
| P_Tape_Orange_MBC        | 0   |
| P_TipBucket_PVplastic    | 6   |
| P_BleachConc_50mL        | 0   |
| P_Cyrobox_MBC_Gen        | 0   |
| P_Hooks_Coat             | 15  |
| P_Hooks_Lil              | 15  |
| PF_PrintoutStationaryKit | 11  |
||


## Master Inventory (Raw)
### Reagents
| Delivery           | Product ID          | Description                              | Last Inv. Date | Init | Packs | Units/Pack | Qty.  | Inv Date  | Init | Packs | Units/Pack | Qty. | Current Lot |
|--------------------|---------------------|------------------------------------------|----------------|------|-------|------------|-------|-----------|------|-------|------------|------|-------------|
| FL Ship Reagents   | PF_PGS-48           | LAMP Primer Solution 48 rxns             | 9/13/2022      | GW   |       |            | 1,116 |           |      |       |            |      |             |
| FL Ship Reagents   | PF_100XIS_5mL       | 100X Inactivation Solution - 500 samples | 9/13/2022      | GW   |       |            | 165   |           |      |       |            |      |             |
| Direct Shipped NEB | P_CLAMPMM_NEB_M1804 | Colormetric LAMP Master Mix              | 9/13/2022      | GW   |       |            | 40    |           |      |       |            |      |             |
|                    | PF_Saline_5mL       | 5mL Saline in a Snap Cap                 |                |      |       |            |       | 9/25/2023 | BS   |       |            | 8    |             |
| FL Ship Main       | PF_Saline_50ml      | 0.9% Saline in 50mL Tube - 50 samples    | 9/13/2022      | GW   |       |            | 601   | 9/25/2023 | BS   |       |            | 50   |             |
| FL Ship Main       | P_Saline_NA250      | Saline Bottle 250mL                      | 9/15/2022      | GW   |       |            | 6     | 9/25/2023 | BS   |       |            | 6    |             |
|                    | P_Saline_1L         | 1L Saline Bottle                         |                |      |       |            |       | 9/25/2023 | BS   |       |            | 6    |             |
|                    | PF_Saline_Kit       | Portioned Saline Kit                     |                |      |       |            |       | 9/25/2023 | BS   |       |            | 8    |             |
| FL Ship Reagents   | PF_TPC              | Amp Positive Control (20uL in Strips)    | 9/22/2022      | GW   |       |            | 119   |           |      |       |            |      |             |
| FL Ship Reagents   | PF_GD50_5mL         | GD50 Contrived Positive                  |                |      |       |            |       |           |      |       |            |      |             |
| FL Ship Reagents   | PF_GD50_1.5mL       | GD50 Contrived Positive                  |
||

|  | Rxn/tube | Rxn |
|---|---|---|
| Primer Solution (48 rxn) | 48 | 53,568 |
| 100X Inactiv. Sol. (500 samples) | 500 | 82,500 |
| NEB CLAMP Master Mix (96 rxn) | 96 | 3,840 |
||

### Lab Consumables
| Delivery     | Product ID                           | Description                | Last Inv. Date | Init | Packs | Units/Pack | Qty.  | Inv Date  | Init | Packs | Units/Pack | Qty. | Notes                     |
|--------------|--------------------------------------|----------------------------|----------------|------|-------|------------|-------|-----------|------|-------|------------|------|---------------------------|
|              |                                      |                            |                |      |       |            |       |           |      |       |            |      |                           |
| FL Ship Main | P_Tube_5mL_snap_MTC                  | 5mL Snap Cap Tube          | 9/16/2022      | BS   |       |            | 120   | 9/23/2023 | BS   | 6     | 20         | 120  | 6 packs of 20             |
| FL Ship Main | P_Tube_5mL_snap_ED_mixed (pre split) | 5mL Snap Cap Tube          | 9/16/2022      | BS   |       |            | 160   |           |      |       |            |      |                           |
| FL Ship Main | P_Tube_5mL_snap_CL                   | 5mL Snap Cap Tube          | 9/16/2022      | BS   |       |            | 20    | 9/23/2023 | BS   |       |            | 20   |                           |
|              | P_Tube_5mL_snap_ED_310               |                            |                |      |       |            |       | 9/23/2023 | BS   |       |            | 100  |                           |
|              | P_Tube_5mL_snap_ED_460               |                            |                |      |       |            |       | 9/23/2023 | BS   |       |            | 60   |                           |
| FL Ship Main | P_Tube_1.5mL_EDLB                    | 1.5mL Snap Cap Tube        | 9/16/2022      | BS   |       |            | 350   | 9/23/2023 | BS   |       |            | 250  | Box of 81 going to alpine |
| FL Ship Main | P_Tube_1.5mL_Globe                   | 1.5mL Snap Cap Tube        | 9/16/2022      | BS   |       |            | 200   | 9/25/2023 | BS   | 6     | 25         | 150  |                           |
|              | PF_1.5mL_Tube_Kit                    |                            |                |      |       |            |       | 9/23/2023 | BS   | 5     | 50         | 200  | packs of 50               |
| FL Ship Main | P_Tube_30mL_ChubSS                   | 30mL Chub Tube             | 9/16/2022      | BS   |       |            | 450   | 9/25/2023 | BS   |       |            | 370  |                           |
| FL Ship Main | P_Tube_50mL_FalconOC                 | 50mL Falcon Tube           | 9/16/2022      | BS   |       |            | 425   | 9/25/2023 | BS   | 16    | 25         | 400  |                           |
| FL Ship Main | P_Reservoir_10mL_Oly                 | Reagent Reservoir          | 9/12/2022      | GW   |       |            | 200   | 9/25/2023 | BS   | 2     | 100        | 200  |                           |
| FL Ship Main | P_Reservoir_5mL_H637                 | Reagent Reservoir          | 9/12/2022      | GW   |       |            | 697   | 9/25/2023 | BS   |       |            | 730  |                           |
| FL Ship Main | P_PCR_96plate_USA200                 | 96-Well PCR Plate          | 9/12/2022      | GW   |       |            | 1,010 | 9/25/2023 | BS   |       | 100        | 1040 |                           |
| FL Ship Main | P_PCRStrips_USA                      | PCR Strip8 Tubes and Caps  | 9/12/2022      | GW   |       |            | 2,875 | 9/25/2023 | BS   | 20    | 125        | 2500 |                           |
|              | PF_StripTubeKit_USA48                | kits of 48 strips and caps |                |      |       |            |       | 9/23/2023 | BS   |       |            | 5    |                           |
| FL Ship Main | P_FoilSeals_MTC                      | Foil Plate Seal            | 9/12/2022      | GW   |       |            | 1,950 | 9/25/2023 | BS   | 20    | 100        | 2000 |                           |
| FL Ship Main | P_Tips_Univ_1000uL_Biotix            | 1000uL Universal Tips      | 9/12/2022      | GW   |       |            | 27    | 9/26/2023 | BS   |       | 10         | 4    |                           |
| FL Ship Main | P_Tips_Univ_1000uL_Gilson            | 1000uL Universal Tips      | 9/12/2022      | GW   |       |            | 35    | 9/26/2023 | BS   |       | 10         | 46   |                           |
| FL Ship Main | P_Tips_Univ_200uL_Biotix             | 200uL Universal Tips       | 9/12/2022      | GW   |       |            | 110   | 9/26/2023 | BS   |       | 10         | 103  |                           |
| FL Ship Main | P_Tips_Univ_10uL_Biotix_long         | 10uL Universal Tips        | 9/12/2022      | GW   |       |            | 97    | 9/26/2023 | BS   |       | 10         | 77   |                           |
| FL Ship Main | P_Tips_Univ_10uL_Biotix_short        | 10uL Universal Tips        | 9/12/2022      | GW   |       |            | 67    | 9/26/2023 | BS   | 7     | 10         | 70   |
||

### Equipment
| Delivery              | Product ID                 | Description                 | Last Inv. Date | Init | Packs | Units/Pack | Qty. | Inv Date | Init | Packs | Units/Pack | Qty. | Notes                           |
|-----------------------|----------------------------|-----------------------------|----------------|------|-------|------------|------|----------|------|-------|------------|------|---------------------------------|
| FL Ship Main          | P_Dispenser_Elec_Scilgx    | Electric dispenser          | 9/14/2022      | GW   |       |            | 14   |          |      |       |            |      |                                 |
| FL Ship Main          | P_Dispenser_2.5mL_Microlit | Manual dispenser            | 9/12/2022      | GW   |       |            | 1    |          |      |       |            |      |                                 |
| FL Ship Main          | P_Pipette_P100_Microlit    | Pipette 10-100 uL           | 9/12/2022      | GW   |       |            | 10   |          |      |       |            |      | 3 need calibration              |
| FL Ship Main          | P_Pipette_P1000_Microlit   | Pipette 100-1000uL          | 9/12/2022      | GW   |       |            | 8    |          |      |       |            |      |                                 |
| FL Ship Main          | P_Pipette_PF2_Microlit     | Pipette Fixed 2uL           | 9/12/2022      | GW   |       |            | 20   |          |      |       |            |      |                                 |
| FL Ship Main          | P_Pipette8Ch_V100          | Pipette 8-Channel  10-100uL | 9/12/2022      | GW   |       |            | 7    |          |      |       |            |      |                                 |
| FL Ship Main          | P_HeaterDry_Mini_4Es       | Mini Heater                 | 9/12/2022      | GW   |       |            | 7    |          |      |       |            |      |                                 |
| FL Ship Main          | P_HeaterDry_96_SWSci       | Dry Heater for Plate        | 9/12/2022      | GW   |       |            | 3    |          |      |       |            |      |                                 |
| FL Ship Main          | P_HeaterDry_96_BnchMB2     | Dry Heater for Plate        | 9/12/2022      | GW   |       |            | 6    |          |      |       |            |      |                                 |
| FL Ship Main          | P_HeatBlock_MiniPCR_BTL    | Mini PCR Heat Block         | 9/12/2022      | GW   |       |            | 11   |          |      |       |            |      |                                 |
| FL Ship Main          | P_HeatBlock_MiniPCR_GBI    | Mini PCR Heat Block         | 9/12/2022      | GW   |       |            | 0    |          |      |       |            |      |                                 |
| FL Ship Main          | P_HeatBlock_Mini_1.5mL     | Mini 1.5mL Heat Block       | 9/16/2022      | BS   |       |            | 7    |          |      |       |            |      |                                 |
| Direct Ship Immediate | P_WaterBath_IVYX           | Water Bath                  | 9/12/2022      | GW   |       |            | 1    |          |      |       |            |      | +2 active (1 Alpine, 1 Portola) |
| Direct Ship Immediate | P_CentrifugeMini_4Es       | Mini centrifuge             | 9/12/2022      | GW   |       |            | 4    |          |      |       |            |      |                                 |
| Direct Ship Immediate | P_Vortexer_4Es             | Vortexer                    | 9/12/2022      | GW   |       |            | 4    |
||

### Lab Supplies
| Delivery              | Product ID                | Description                    | Last Inv. Date | Init | Packs | Units/Pack | Qty. | Inv Date | Init | Packs | Units/Pack | Qty. | Notes           |
|-----------------------|---------------------------|--------------------------------|----------------|------|-------|------------|------|----------|------|-------|------------|------|-----------------|
| FL Ship Main          | P_ColdBlock_PCR_G         | PCR Cold Blocks                | 9/12/2022      | GW   |       |            | 11   |          |      |       |            |      | 3 need cleaning |
| FL Ship Main          | P_GlassBottle_250mL_KAR   | 500mL Glass bottle             | 9/16/2022      | BS   |       |            | 21   |          |      |       |            |      |                 |
| FL Ship Main          | P_Rack_1.5mL_OLY          | 1.5mL tube racks               | 9/16/2022      | BS   |       |            | 2    |          |      |       |            |      |                 |
| FL Ship Main          | P_Rack_50Tubes_5mL_ULA    | Light Blue 5mL 50 tube racks   | 9/16/2022      | BS   |       |            | 8    |          |      |       |            |      |                 |
| FL Ship Main          | P_Rack_Flipper            | Flipper racks (separate)       | 9/16/2022      | BS   |       |            | 27   |          |      |       |            |      |                 |
| FL Ship Main          | PF_Rack_Flipper_4Block    | Flipper rack blocks - 4 zipped | 9/12/2022      | GW   |       |            | 8    |          |      |       |            |      |                 |
| FL Ship Main          | P_Rack_HingeBox           | Hinged Box                     | 9/16/2022      | BS   |       |            | 6    |          |      |       |            |      |                 |
| FL Ship Main          | P_Rack_PCR                | PCR racks                      | 9/16/2022      | BS   |       |            | 60   |          |      |       |            |      |                 |
| FL Ship Main          | PF_Versirack              | Versi Rack                     | 9/16/2022      | BS   |       |            | 17   |          |      |       |            |      |                 |
| FL Ship Main          | P_ThermometersFreezer_ETH | Thermometers freezer           | 9/16/2022      | BS   |       |            | 20   |          |      |       |            |      |                 |
| FL Ship Main          | P_Timers_LIN              | Timers                         | 9/16/2022      | BS   |       |            | 27   |          |      |       |            |      |                 |
| FL Ship Main          | PF_Rack_LookUp_48Half_5mL | 3D LookUp racks 5mL x 48 HALF  | 9/16/2022      | BS   |       |            | 20   |          |      |       |            |      |                 |
| FL Ship Main          | PF_Rack_LookUp_96Full_5mL | 3D LookUp racks 5mL x 96 FULL  | 9/12/2022      | BS   |       |            | 23   |          |      |       |            |      |                 |
| FL Ship Main          | P_Baggies_3x4_SNL         | Baggie 3x4                     | 9/16/2022      | BS   |       |            | 950  |          |      |       |            |      |                 |
| Direct Ship Immediate | P_Eyewash_Station         | Eyewash Station                | 9/16/2022      | BS   |       |            | 1    |
||

### Collection Materials
| Delivery     | Product ID                   | Description                                | Last Inv. Date | Init | Packs | Units/Pack | Qty.    | Inv Date | Init | Packs | Units/Pack | Qty. | Notes |
|--------------|------------------------------|--------------------------------------------|----------------|------|-------|------------|---------|----------|------|-------|------------|------|-------|
| FL Ship Main | P_Swab_JableUR               | Jable UR Swabs                             | 9/12/2022      | GW   |       |            | 172,900 |          |      |       |            |      |       |
| FL Ship Main | P_ColTubeQR_5mL_Jable1       | 5mL collection tubes (Jable blue cap)      | 9/12/2022      | GW   |       |            | 89,500  |          |      |       |            |      |       |
| FL Ship Main | PF_ColTubeQR_5mL_M1          | 5mL collection tubes (MTC Bio w our label) | 9/13/2022      | GW   |       |            | 3,000   |          |      |       |            |      |       |
| FL Ship Main | PF_ColTubeQR_1.5mL_BSC1      | 1.5m collection tubes (MTC Blue Screw cap) | 9/12/2022      | GW   |       |            | 500     |          |      |       |            |      |       |
| FL Ship Main | P_Bag_Slider_U6x9            | Collection Kit Outer Bag                   | 9/16/2022      | BS   |       |            | 770     |          |      |       |            |      |       |
| FL Ship Main | PF_CollectionPamphlet_v2_PDC | Pamplet Collection Instructions            | 9/16/2022      | BS   |       |            | 800     |          |      |       |            |      |       |
| FL Ship Main | P_BioHazBag_D2x5             | Biohazard Bags for Collection              | 9/16/2022      | BS   |       |            | 3,200   |
||

### Misc Supplies
| Delivery     | Product ID                   | Description                     | Last Inv. Date | Init | Packs | Units/Pack | Qty. | Inv Date  | Init | Packs | Units/Pack | Qty. | Notes |
|--------------|------------------------------|---------------------------------|----------------|------|-------|------------|------|-----------|------|-------|------------|------|-------|
| FL Ship Main | P_Calculator                 | Calculator                      | 9/16/2022      | BS   |       |            | 6    |           |      |       |            |      |       |
| FL Ship Main | P_Clipboard                  | Clipboard                       | 9/16/2022      | BS   |       |            | 8    |           |      |       |            |      |       |
| FL Ship Main | P_Foil_UltraClean            | Foil                            | 9/16/2022      | BS   |       |            | 23   | 9/25/2023 | BS   | 22    | 1          | 22   |       |
| FL Ship Main | P_Gloves_Latex_S_GenX        | Latex Gloves S                  | 9/16/2022      | BS   |       |            | 0    |           |      |       |            |      |       |
| FL Ship Main | P_Gloves_Latex_M_GenX        | Latex Gloves M                  | 9/16/2022      | BS   |       |            | 5    |           |      |       |            |      |       |
| FL Ship Main | P_Gloves_Latex_L_GenX        | Latex Gloves L                  | 9/16/2022      | BS   |       |            | 0    |           |      |       |            |      |       |
| FL Ship Main | P_LabCoat_RK_S               | Lab Coat                        | 9/16/2022      | BS   |       |            | 1    |           |      |       |            |      |       |
| FL Ship Main | P_LabCoat_RK_M               | Lab Coat                        | 9/16/2022      | BS   |       |            | 0    |           |      |       |            |      |       |
| FL Ship Main | P_LabCoat_RK_L               | Lab Coat                        | 9/16/2022      | BS   |       |            | 4    |           |      |       |            |      |       |
| FL Ship Main | P_LabCoat_RK_XL              | Lab Coat                        | 9/16/2022      | BS   |       |            | 6    |           |      |       |            |      |       |
| FL Ship Main | P_LabWipes_S_VWRLD           | Science Precision wipes         | 9/16/2022      | BS   |       |            | 2    |           |      |       |            |      |       |
| FL Ship Main | P_LabWipes_L_KimGreen        | Science Precision wipes         | 9/16/2022      | BS   |       |            | 14   |           |      |       |            |      |       |
| FL Ship Main | P_Pen                        | Pen                             | 9/16/2022      | BS   |       |            | 8    |           |      |       |            |      |       |
| FL Ship Main | P_RazorBlade_Uline           | Razor Blades                    | 9/16/2022      | BS   |       |            | 11   |           |      |       |            |      |       |
| FL Ship Main | P_SharpieTwinTip             | Sharpie Twin Tip                | 9/16/2022      | BS   |       |            | 70   |           |      |       |            |      |       |
| FL Ship Main | P_SprayBottle_Set            | Spray Bottles                   | 9/16/2022      | BS   |       |            | 34   |           |      |       |            |      |       |
| FL Ship Main | P_Tape_Orange_VWR            | Orange Tape                     | 9/16/2022      | BS   |       |            | 10   |           |      |       |            |      |       |
| FL Ship Main | P_TipBucket_PVplastic        | Tip Bucket                      | 9/16/2022      | BS   |       |            | 4    |           |      |       |            |      |       |
| FL Ship Main | P_BleachConc_50mL            | Bleach Concentrated 50mL        | 9/16/2022      | BS   |       |            | 0    |           |      |       |            |      |       |
| FL Ship Main | P_Cyrobox_Gen                | Cryobox Cardboard               | 9/16/2022      | BS   |       |            | 0    | 9/25/2023 | BS   |       |            | 44   |       |
| FL Ship Main | P_Hooks_Coat                 | Hooks for Coats                 | 9/16/2022      | BS   |       |            | 41   |           |      |       |            |      |       |
| FL Ship Main | P_Hooks_Wire                 | Small Wire Hooks                | 9/16/2022      | BS   |       |            | 17   |           |      |       |            |      |       |
|              | P_BottleShipper_500mL_Orange | Orange shipper for 500mL bottle |                |      |       |            |      | 9/25/2023 | BS   |       |            | 9    |
||

### Training Kit
| Delivery     | Product ID | Description              | Last Inv. Date | Init | Packs | Units/Pack | Qty. | Inv Date | Init | Packs | Units/Pack | Qty. | Notes |
|--------------|------------|--------------------------|----------------|------|-------|------------|------|----------|------|-------|------------|------|-------|
| FL Ship Main |            | Training 1.5mL Tubes     |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Training 30mL Chub Tubes |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Training 5mL Snap Tubes  |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Mock PGS                 |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Mock CLAMPMM             |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Mock 100XIS              |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Mock 50mL Saline         |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Mock TPC                 |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Combo Protocol           |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Protocol Log             |                |      |       |            |      |          |      |       |            |      |       |
| FL Ship Main |            | Run Worksheet            |
||


# 1,630  LAMP Primers UPDATED 12-17-2020.md
METADATA
last updated: 2026-01-21 RT
file_name: LAMP Primers UPDATED 12-17-2020.xlsx
file_date: 2020-12-17
title: LAMP Primers UPDATED 12-17-2020
category: guides
subcategory: operations
tags:
source_file_type: xlsx
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1yrgBbJJtmFw3edxbjYx7XaO3ecsXNemaOtbrY2RnuoY
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/operations/LAMP%20Primers%20UPDATED%2012-17-2020.xlsx.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: pandas
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1630
words: 520
notes: Unsure about license
summary_short: The FloodLAMP LAMP Primers list (updated 12/17/2020) specifies SARS-CoV-2 and human internal control primer sets derived from the Rabe–Cepko protocol, including sequences, mix concentrations, and ordering/handling notes (HPLC purification, resuspension, packaging, and minimum order quantities). It provides premix targets for 30X stock solutions for ORF1ab (AS1e), E gene (E1), N gene (N2), and human controls (RNaseP and ACTB) to support standardized assay preparation and procurement.


CONTENT

***INTERNAL TITLE:*** LAMP Primers UPDATED 12-17-2020

- FloodLAMP Contact Randy True   randy@floodlamp.bio
- from Rabe Cepko | [Proc Natl Acad Sci 2020 Sep 29;117(39):24450-24458. doi: 10.1073/pnas.2011221117. Epub 2020 Sep 8.](https://pubmed.ncbi.nlm.nih.gov/32900935/)
- Harvard University IP


- All oligos 5' to 3'
- 6 Primer per set to be premixed at 30X concentration
- All primers HPLC purified
- Resuspended in DNAse RNAse free water, shipped on cold packs
- Supplied in 1ml tubes
- MOQ 25 x 1ml tubes (10K rxns at 2.5ul per reaction of 10X)

| **As1e - ORF1ab (SARS-CoV-2)**   |                                           |   | 30X μM   | ml   | total nmoles   |
|------------------------------|-----------------------------------------------------|--------------|----------|------|----------------|
| As1e_FIP                     | TCAGCACACAAAGCCAAAAATTTATTTTTCTGTGCAAAGGAAATTAAGGAG | 51.0         | 48.0     | 25.0 | 1200.0         |
| As1e_BIP                     | TATTGGTGGAGCTAAACTTAAAGCCTTTTCTGTACAATCCCTTTGAGTG   | 49.0         | 48.0     |      | 1200.0         |
| As1_F3                       | CGGTGGACAAATTGTCAC                                  | 18.0         | 6.0      |      | 150.0          |
| As1_B3                       | CTTCTCTGGATTTAACACACTT                              | 22.0         | 6.0      |      | 150.0          |
| As1_LF                       | TTACAAGCTTAAAGAATGTCTGAACACT                        | 28.0         | 12.0     |      | 300.0          |
| As1_LB                       | TTGAATTTAGGTGAAACATTTGTCACG                         | 27.0         | 12.0     |      | 300.0          |
|                              |                                                     |              |          |      |                |
|                              |                                                     |              |          |      |                |
| **E1 - E Gene (SARS-CoV-2)**     |                                                     |              |          |      |                |
| E1-FIP                       | ACCACGAAAGCAAGAAAAAGAAGTTCGTTTCGGAAGAGACAG          | 42.0         | 48.0     |      |                |
| E1-BIP                       | TTGCTAGTTACACTAGCCATCCTTAGGTTTTACAAGACTCACGT        | 44.0         | 48.0     |      |                |
| E1-F3                        | TGAGTACGAACTTATGTACTCAT                             | 23.0         | 6.0      |      |                |
| E1-B3                        | TTCAGATTTTTAACACGAGAGT                              | 22.0         | 6.0      |      |                |
| E1-LF                        | CGCTATTAACTATTAACG                                  | 18.0         | 12.0     |      |                |
| E1-LB                        | GCGCTTCGATTGTGTGCGT                                 | 19.0         | 12.0     |      |                |
|                              |                                                     |              |          |      |                |
| **N2 - N Gene (SARS-CoV-2)**     |                                                     |              |          |      |                |
| N2-FIP                       | TTCCGAAGAACGCTGAAGCGGAACTGATTACAAACATTGGCC          | 42.0         | 48.0     |      |                |
| N2-BIP                       | CGCATTGGCATGGAAGTCACAATTTGATGGCACCTGTGTA            | 40.0         | 48.0     |      |                |
| N2-F3                        | ACCAGGAACTAATCAGACAAG                               | 21.0         | 6.0      |      |                |
| N2-B3                        | GACTTGATCTTTGAAATTTGGATCT                           | 25.0         | 6.0      |      |                |
| N2-LF                        | GGGGGCAAATTGTGCAATTTG                               | 21.0         | 12.0     |      |                |
| N2-LB                        | CTTCGGGAACGTGGTTGACC                                | 20.0         | 12.0     |      |                |
|                              |                                                     |              |          |      |                |
| **RNAseP (Human IC)**            |                                                     |              |          |      |                |
| RNP-FIP                      | GTGTGACCCTGAAGACTCGGTTTTAGCCACTGACTCGGATC           | 41.0         | 48.0     |      |                |
| RNP-BIP                      | CCTCCGTGATATGGCTCTTCGTTTTTTTCTTACATGGCTCTGGTC       | 45.0         | 48.0     |      |                |
| RNP-F3                       | TTGATGAGCTGGAGCCA                                   | 17.0         | 6.0      |      |                |
| RNP-B3                       | CACCCTCAATGCAGAGTC                                  | 18.0         | 6.0      |      |                |
| RNP-LF                       | ATGTGGATGGCTGAGTTGTT                                | 20.0         | 12.0     |      |                |
| RNP-LB                       | CATGCTGAGTACTGGACCTC                                | 20.0         | 12.0     |      |                |
|                              |                                                     |              |          |      |                |
| **ActinB (Human IC)**            |                                                     |              |          |      |                |
| ACTB-FIP                     | GAGCCACACGCAGCTCATTGTATCACCAACTGGGACGACA            | 40.0         | 48.0     |      |                |
| ACTB-BIP                     | CTGAACCCCAAGGCCAACCGGCTGGGGTGTTGAAGGTC              | 38.0         | 48.0     |      |                |
| ACTB-F3                      | AGTACCCCATCGAGCACG                                  | 18.0         | 6.0      |      |                |
| ACTB-B3                      | AGCCTGGATAGCAACGTACA                                | 20.0         | 6.0      |      |                |
| ACTB-LF                      | TGTGGTGCCAGATTTTCTCCA                               | 21.0         | 12.0     |      |                |
| ACTB-B                       | CGAGAAGATGACCCAGATCATGT                             | 23.0         | 12.0     |      |                |
||

# ===== END OF FILE _archive-combined-files_operations_27k.md =====
