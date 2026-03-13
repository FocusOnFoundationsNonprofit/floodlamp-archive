METADATA
last updated: 2025-12-15 RT after BA fixed inconsistencies
file_name: Resulting Decision Chart v1.2.md
file_date: 2022-12-15
title: Resulting Decision Chart v1.2
category: guides
subcategory: test-site
tags: 
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1hSqrQPAmpFeEcgxNxtFhQyBI904lUhvz1yx7GcAbefo
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/test-site/Resulting%20Decision%20Chart%20v1.2.xlsx
pdf_gdrive_url: https://drive.google.com/file/d/1gozC_wEeATUHnF8WQhn10YK_sbCZtXdn
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/test-site/Resulting%20Decision%20Chart%20v1.2.pdf
conversion_input_file_type: xlsx
conversion: Excel to Markdown extension
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 3410
words: 2431
notes: multiple versions, using Excel to Md conv
summary_short: The Resulting Decision Chart v1.2 is a set of tabular rules for interpreting FloodLAMP test outcomes using single-triplicate and double-triplicate re-run workflows. It maps initial results and subsequent re-run replicate patterns (positive/negative/inconclusive) to a final reportable call—negative, positive, or inconclusive—so test-site staff can apply consistent decision logic across reruns.


CONTENT

***INTERNAL TITLE:*** FloodLAMP Resulting Decision Chart v1.2
**Document Number:** 
**Effective Date:** 
**Version:** 1.2

## Resulting decision chart (double triplicate rerun) Version 1.2

| Initial test | Decision       | First re-run |   |   | Decision           | Second re-run |   |   | Decision           |
|--------------|----------------|--------------|---|---|--------------------|---------------|---|---|--------------------|
| -            | final negative |              |   |   |                    |               |   |   |                    |
| ?            | re-run         | -            | - | - | final negative     |               |   |   |                    |
| ?            | re-run         | +            | + | + | final positive     |               |   |   |                    |
| ?            | re-run         | +            | + | ? | final positive     |               |   |   |                    |
| ?            | re-run         | -            | - | ? | final negative     |               |   |   |                    |
| ?            | re-run         | +            | + | - | re-run             | -             | - | - | final negative     |
| ?            | re-run         | +            | + | - | re-run             | +             | + | + | final positive     |
| ?            | re-run         | +            | + | - | re-run             | +             | + | ? | final positive     |
| ?            | re-run         | +            | + | - | re-run             | +             | + | - | final positive     |
| ?            | re-run         | +            | + | - | re-run             | -             | - | ? | final inconclusive |
| ?            | re-run         | +            | + | - | re-run             | +             | - | - | final inconclusive |
| ?            | re-run         | +            | + | - | re-run             | +             | ? | ? | final positive     |
| ?            | re-run         | +            | + | - | re-run             | -             | ? | ? | final inconclusive |
| ?            | re-run         | +            | + | - | re-run             | +             | - | ? | final inconclusive |
| ?            | re-run         | +            | + | - | re-run             | ?             | ? | ? | final inconclusive |
| ?            | re-run         | +            | - | - | re-run             | -             | - | - | final negative     |
| ?            | re-run         | +            | - | - | re-run             | +             | + | + | final positive     |
| ?            | re-run         | +            | - | - | re-run             | +             | + | ? | final positive     |
| ?            | re-run         | +            | - | - | re-run             | +             | + | - | final positive     |
| ?            | re-run         | +            | - | - | re-run             | -             | - | ? | final negative     |
| ?            | re-run         | +            | - | - | re-run             | +             | - | - | final inconclusive |
| ?            | re-run         | +            | - | - | re-run             | +             | ? | ? | final inconclusive |
| ?            | re-run         | +            | - | - | re-run             | -             | ? | ? | final inconclusive |
| ?            | re-run         | +            | - | - | re-run             | +             | - | ? | final inconclusive |
| ?            | re-run         | +            | - | - | re-run             | ?             | ? | ? | final inconclusive |
| ?            | re-run         | +            | ? | ? | final inconclusive |               |   |   |                    |
| ?            | re-run         | -            | ? | ? | final inconclusive |               |   |   |                    |
| ?            | re-run         | +            | - | ? | final inconclusive |               |   |   |                    |
| ?            | re-run         | ?            | ? | ? | final inconclusive |               |   |   |                    |
| +            | re-run         | -            | - | - | final negative     |               |   |   |                    |
| +            | re-run         | +            | + | + | final positive     |               |   |   |                    |
| +            | re-run         | +            | + | ? | final positive     |               |   |   |                    |
| +            | re-run         | +            | + | - | final positive     |               |   |   |                    |
| +            | re-run         | -            | - | ? | re-run             | -             | - | - | final negative     |
| +            | re-run         | -            | - | ? | re-run             | +             | + | + | final positive     |
| +            | re-run         | -            | - | ? | re-run             | +             | + | ? | final positive     |
| +            | re-run         | -            | - | ? | re-run             | +             | + | - | final positive     |
| +            | re-run         | -            | - | ? | re-run             | -             | - | ? | final negative     |
| +            | re-run         | -            | - | ? | re-run             | +             | - | - | final inconclusive |
| +            | re-run         | -            | - | ? | re-run             | +             | ? | ? | final inconclusive |
| +            | re-run         | -            | - | ? | re-run             | -             | ? | ? | final inconclusive |
| +            | re-run         | -            | - | ? | re-run             | +             | - | ? | final inconclusive |
| +            | re-run         | -            | - | ? | re-run             | ?             | ? | ? | final inconclusive |
| +            | re-run         | +            | - | - | re-run             | -             | - | - | final negative     |
| +            | re-run         | +            | - | - | re-run             | +             | + | + | final positive     |
| +            | re-run         | +            | - | - | re-run             | +             | + | ? | final positive     |
| +            | re-run         | +            | - | - | re-run             | +             | + | - | final positive     |
| +            | re-run         | +            | - | - | re-run             | -             | - | ? | final inconclusive |
| +            | re-run         | +            | - | - | re-run             | +             | - | - | final inconclusive |
| +            | re-run         | +            | - | - | re-run             | +             | ? | ? | final inconclusive |
| +            | re-run         | +            | - | - | re-run             | -             | ? | ? | final inconclusive |
| +            | re-run         | +            | - | - | re-run             | +             | - | ? | final inconclusive |
| +            | re-run         | +            | - | - | re-run             | ?             | ? | ? | final inconclusive |
| +            | re-run         | +            | ? | ? | re-run             | -             | - | - | final negative     |
| +            | re-run         | +            | ? | ? | re-run             | +             | + | + | final positive     |
| +            | re-run         | +            | ? | ? | re-run             | +             | + | ? | final positive     |
| +            | re-run         | +            | ? | ? | re-run             | +             | + | - | final positive     |
| +            | re-run         | +            | ? | ? | re-run             | -             | - | ? | final negative     |
| +            | re-run         | +            | ? | ? | re-run             | +             | - | - | final inconclusive |
| +            | re-run         | +            | ? | ? | re-run             | +             | ? | ? | final positive     |
| +            | re-run         | +            | ? | ? | re-run             | -             | ? | ? | final inconclusive |
| +            | re-run         | +            | ? | ? | re-run             | +             | - | ? | final inconclusive |
| +            | re-run         | +            | ? | ? | re-run             | ?             | ? | ? | final inconclusive |
| +            | re-run         | -            | ? | ? | re-run             | -             | - | - | final negative     |
| +            | re-run         | -            | ? | ? | re-run             | +             | + | + | final positive     |
| +            | re-run         | -            | ? | ? | re-run             | +             | + | ? | final positive     |
| +            | re-run         | -            | ? | ? | re-run             | +             | + | - | final positive     |
| +            | re-run         | -            | ? | ? | re-run             | -             | - | ? | final negative     |
| +            | re-run         | -            | ? | ? | re-run             | +             | - | - | final inconclusive |
| +            | re-run         | -            | ? | ? | re-run             | +             | ? | ? | final inconclusive |
| +            | re-run         | -            | ? | ? | re-run             | -             | ? | ? | final inconclusive |
| +            | re-run         | -            | ? | ? | re-run             | +             | - | ? | final inconclusive |
| +            | re-run         | -            | ? | ? | re-run             | ?             | ? | ? | final inconclusive |
| +            | re-run         | +            | - | ? | re-run             | -             | - | - | final negative     |
| +            | re-run         | +            | - | ? | re-run             | +             | + | + | final positive     |
| +            | re-run         | +            | - | ? | re-run             | +             | + | ? | final positive     |
| +            | re-run         | +            | - | ? | re-run             | +             | + | - | final positive     |
| +            | re-run         | +            | - | ? | re-run             | -             | - | ? | final inconclusive |
| +            | re-run         | +            | - | ? | re-run             | +             | - | - | final inconclusive |
| +            | re-run         | +            | - | ? | re-run             | +             | ? | ? | final inconclusive |
| +            | re-run         | +            | - | ? | re-run             | -             | ? | ? | final inconclusive |
| +            | re-run         | +            | - | ? | re-run             | +             | - | ? | final inconclusive |
| +            | re-run         | +            | - | ? | re-run             | ?             | ? | ? | final inconclusive |
| +            | re-run         | ?            | ? | ? | re-run             | -             | - | - | final negative     |
| +            | re-run         | ?            | ? | ? | re-run             | +             | + | + | final positive     |
| +            | re-run         | ?            | ? | ? | re-run             | +             | + | ? | final positive     |
| +            | re-run         | ?            | ? | ? | re-run             | +             | + | - | final positive     |
| +            | re-run         | ?            | ? | ? | re-run             | -             | - | ? | final inconclusive |
| +            | re-run         | ?            | ? | ? | re-run             | +             | - | - | final inconclusive |
| +            | re-run         | ?            | ? | ? | re-run             | +             | ? | ? | final positive     |
| +            | re-run         | ?            | ? | ? | re-run             | -             | ? | ? | final inconclusive |
| +            | re-run         | ?            | ? | ? | re-run             | +             | - | ? | final inconclusive |
| +            | re-run         | ?            | ? | ? | re-run             | ?             | ? | ? | final inconclusive |
||

## Resulting decision chart (single triplicate rerun) Version 1.2

| Initial test | Decision       | First re-run |   |   | Decision           |
|--------------|----------------|--------------|---|---|--------------------|
| -            | final negative |              |   |   |                    |
| ?            | re-run         | -            | - | - | final negative     |
| ?            | re-run         | +            | + | + | final positive     |
| ?            | re-run         | +            | + | ? | final positive     |
| ?            | re-run         | -            | - | ? | final inconclusive |
| ?            | re-run         | +            | + | - | final positive     |
| ?            | re-run         | +            | - | - | final inconclusive |
| ?            | re-run         | +            | ? | ? | final positive     |
| ?            | re-run         | -            | ? | ? | final inconclusive |
| ?            | re-run         | +            | - | ? | final inconclusive |
| ?            | re-run         | ?            | ? | ? | final inconclusive |
| +            | re-run         | -            | - | - | final negative     |
| +            | re-run         | +            | + | + | final positive     |
| +            | re-run         | +            | + | ? | final positive     |
| +            | re-run         | +            | + | - | final positive     |
| +            | re-run         | -            | - | ? | final inconclusive |
| +            | re-run         | +            | - | - | final inconclusive |
| +            | re-run         | +            | ? | ? | final positive     |
| +            | re-run         | -            | ? | ? | final inconclusive |
| +            | re-run         | +            | - | ? | final inconclusive |
| +            | re-run         | ?            | ? | ? | final inconclusive |
||

## Key
| Key |              |
|-----|--------------|
| -   | negative     |
| +   | positive     |
| ?   | inconclusive |
||

_Photo Figure 2 Example of Test Results (Left 2 Negative, Right 2 Positive where Negative are bright red in color, and Positive are bright yellow in color)_
_Photo Figure 3 Edge Case Test Results (Left Negative, Right Positive) where Negative is somewhat pink in color compared to bright red, and Positive is somewhat orange in color compared to bright yellow_
