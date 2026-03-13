METADATA
last updated: 2026-03-06 by BA
file_name: XPrize FloodLAMP Submission - Part 9 Results Interpretation.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Submission - Part 9 Results Interpretation
category: various
subcategory: xprize
tags:
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1W4o2wfltdjJq0MHjf2qvL7-PI3Z2QICj/
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20Part%209%20Results%20Interpretation.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 302
words: 193
notes:
summary_short: FloodLAMP's XPRIZE submission Part 9 Results Interpretation spreadsheet defines how assay results are interpreted based on combinations of batch positive/negative controls, SARS-CoV-2 target results, and human internal control (RNaseP) results, including rules for reporting findings of potential clinical significance, invalid samples, and batch failures.


CONTENT

## FloodLAMP Results Interpretation
### Result Interpretation
| Result                                        | Next Step     | Batch Control (+)     | Batch Control (-)     | SARS Target(s) | Human Internal Control Target |                                                                                  |
|-----------------------------------------------|---------------|-----------------------|-----------------------|----------------|-------------------------------|----------------------------------------------------------------------------------|
| Text                                          | Text          |                       |                       | Numeric        | Numeric                       |                                                                                  |
| Finding of Potential Clinical Significance    | Report result | Positive              | Negative              | Positive       | Positive                      |                                                                                  |
| No Finding of Potential Clinical Significance | Report result | Positive              | Negative              | Negative       | Positive                      |                                                                                  |
| Finding of Potential Clinical Significance    | Run again     | Positive              | Negative              | Positive       | Negative/Inconclusive         | EUA's say to report this result as positive even if internal control is negative |
| Sample/Pool Invalid                           | Run again     | NA                    | NA                    | Negative       | Negative/Inconclusive         |                                                                                  |
| Batch Invalid                                 | Run again     | Negative/Inconclusive | Positive/Inconclusive | NA             | NA                            |
||

For a positive pool, we will run the other aliquot of the pool as a confirmation, and run the individual samples.

### Targets
Target numbers (1,2,n..) need to correspond to names in "targets" table. Define every possibility of target result and how test result is interpreted.
