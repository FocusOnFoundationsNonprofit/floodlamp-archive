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
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/guides/operations/Cost%20Model%20-%20FloodLAMP.xlsx
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
