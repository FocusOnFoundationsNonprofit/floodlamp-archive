METADATA
last updated: 2026-03-03 AI and RT
file_name: XPrize FloodLAMP Proficiency Test Results.md
file_date: 2021-01-08
title: FloodLAMP XPRIZE Proficiency Test Results — Submitted Results Merged with Answer Key
category: various
subcategory: xprize
tags: xprize, proficiency-test, results, LAMP, performance
source_file_type: gsheet
xfile_type: xlsx
gfile_url: https://docs.google.com/spreadsheets/d/1kBM2uK_QlB8YW2YHPm1bV6q-jtbv5_qH_ckKkVGXg9s
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/various/xprize/XPrize%20FloodLAMP%20Proficiency%20Test%20Results.xlsx
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: xlsx
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 10243
words: 5963
notes: Created by Opus 4.6 Max (Claude) during archive preparation. **PARTIALLY HUMAN REVIEWED - MAY CONTAIN ERRORS** Merged analysis file created by FloodLAMP after receiving the XPRIZE answer key (released Dec 23, 2020, one day after the 20 finalists were announced). Combines FloodLAMP's submitted detection calls (1=detected, 0=not detected) with the unblinded sample compositions. FloodLAMP did not advance to the finalist round. Source xlsx file date is Jan 8, 2021.
summary_short: FloodLAMP's XPRIZE Rapid Covid Testing blinded proficiency test results merged with the competition answer key. Contains 157 samples across two racks: NSP17634 (69 Zepto inactivated viral particle samples in PBS, Saliva, and Nasal matrices at 4°C) and XP60846 (88 Twist Synthetic RNA samples in Water at -80°C, including cross-reactivity controls). FloodLAMP detected 51 of 69 NSP samples correctly with zero false positives but performed poorly on the XP rack (13 of 56 SARS-CoV-2 positives detected), likely due to buffer incompatibility with the silica-based purification protocol.


CONTENT

FloodLAMP's blinded proficiency test results from the XPRIZE Rapid Covid Testing competition, merged with the answer key that XPRIZE released after judging. FloodLAMP submitted results under Team ID 3362. The "Detected" column contains FloodLAMP's submitted calls (1=detected, 0=not detected). The remaining columns show the unblinded sample compositions.

## Performance Summary

### Rack NSP17634 (Zepto particles, PBS/Saliva/Nasal, 4°C)
- 69 samples total
- 51 correct calls, 18 false negatives, 0 false positives
- False negatives concentrated at low concentrations (≤2 copies/uL), consistent with the assay's limit of detection
- All samples ≥5 copies/uL detected correctly except both Saliva 25 copies/uL samples (reagent S7, positions C9 and F1), while 25 copies/uL was detected in PBS (3/3) and Nasal (2/2)

### Rack XP60846 (Twist Synthetic RNA, Water, -80°C)
- 88 samples total (56 SARS-CoV-2 positives, 2 SARS-CoV-2 negatives, 30 cross-reactivity controls)
- 13 of 56 SARS-CoV-2 positive samples detected; detections concentrated at ≥100 copies/uL
- 0 false positives on negative controls or cross-reactivity organisms
- Poor sensitivity likely due to incompatibility between the water-based sample matrix and FloodLAMP's TCEP/NaI silica purification protocol, which was designed for use with the TCEP inactivation step on biological samples

These results represent the early glass milk purification version of the FloodLAMP assay. Shortly after the XPRIZE, at the end of 2020, FloodLAMP switched to a direct LAMP protocol (no RNA extraction) with dry swab collection and a combined elution/inactivation step. The analytical performance of that version is documented in the March 2021 FDA submissions (see file: `regulatory/fl-fda-submissions/2021-03-22_EUA Submission - FloodLAMP QuickColor COVID-19 Test v1.0.md`), and the real-world performance is documented in the pilots data, which showed significantly higher sensitivity than rapid antigen tests, particularly for early and asymptomatic cases (see "Comparison with Antigen Tests" in `pilots/pilot-data/_context-commentary_pilots-pilot-data.md`)

## Sample Order with Comments
157 samples across two racks, grouped by material and sorted by concentration. Rack XP60846 contains Twist Synthetic RNA in Water at -80°C (including SARS-CoV-2 at various concentrations and cross-reactivity controls). Rack NSP17634 contains Zepto inactivated viral particles in PBS, Saliva, and Nasal matrices at 4°C. Detected column: 1=detected, 0=not detected.

| Team ID | Team Name | RackCode | TubePositionNumber | TubePositionText | TubeCode | Matrix | Detected | Organism | Material | Concentration | ConcUnits | Volume | Matrix | Storage | Comments |
|---------|-----------|----------|--------------------|------------------|----------|--------|----------|----------|----------|---------------|-----------|--------|--------|---------|----------|
| 3362 | FloodLAMP | XP60846 | 1 | A1 | 366700409 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0 | copies/ul | 400 | Water | -80 C | |
| 3362 | FloodLAMP | XP60846 | 55 | E7 | 366687548 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 5 | A5 | 366712371 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.01 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 52 | E4 | 366712356 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.01 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 72 | F12 | 366712442 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.01 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 14 | B2 | 366694960 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.02 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 30 | C6 | 366694985 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.02 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 63 | F3 | 366694995 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.02 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 40 | D4 | 366711036 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.05 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 73 | G1 | 366689613 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.05 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 81 | G9 | 366689631 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.05 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 38 | D2 | 366690457 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 56 | E8 | 366709342 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 74 | G2 | 366708039 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 82 | G10 | 366709774 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 84 | G12 | 366708241 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 13 | B1 | 366708116 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 21 | B9 | 366698486 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 32 | C8 | 366717788 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 50 | E2 | 366717561 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 87 | H3 | 366698482 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 0.5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 23 | B11 | 366717619 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 25 | C1 | 366717657 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 39 | D3 | 366708480 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 44 | D8 | 366692591 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 54 | E6 | 366717658 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 1 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 24 | B12 | 366716893 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 2 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 49 | E1 | 366717974 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 2 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 76 | G4 | 366717915 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 2 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 19 | B7 | 367537858 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 3 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 46 | D10 | 367540998 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 3 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 64 | F4 | 367537838 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 3 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 15 | B3 | 366715730 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 4 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 62 | F2 | 366691066 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 4 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 78 | G6 | 366716658 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 4 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 11 | A11 | 366695734 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 33 | C9 | 366715053 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 41 | D5 | 366695712 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 5 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 17 | B5 | 366711757 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 10 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 59 | E11 | 366711821 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 10 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 75 | G3 | 366711755 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 10 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 26 | C2 | 366715055 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 25 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 34 | C10 | 366691100 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 25 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 80 | G8 | 366715070 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 25 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 8 | A8 | 366711552 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 50 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 31 | C7 | 366712660 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 50 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 47 | D11 | 366711173 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 50 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 4 | A4 | 366695473 | Water | 0 | SARS-CoV-2 | Twist Synthetic RNA | 100 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 36 | C12 | 366720128 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 100 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 61 | F1 | 366695856 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 100 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 9 | A9 | 366720642 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 200 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 65 | F5 | 366691660 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 200 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 12 | A12 | 366691008 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 85 | H1 | 366695804 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 43 | D7 | 366695945 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 1000 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 67 | F7 | 366695980 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 1000 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 2 | A2 | 366715002 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 10000 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 57 | E9 | 366713811 | Water | 1 | SARS-CoV-2 | Twist Synthetic RNA | 10000 | copies/ul | 400 | Water | -80 C |  |
| 3362 | FloodLAMP | NSP17634 | 1 | A1 | 366713026 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 400 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 64 | F4 | 366713374 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 400 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 7 | A7 | 376016050 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 21 | B9 | 376016058 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 52 | E4 | 376033074 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 65 | F5 | 376033067 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 10 | A10 | 366697750 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 16 | B4 | 366697734 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 63 | F3 | 366708002 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 13 | B1 | 376021817 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 19 | B7 | 376021825 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 9 | A9 | 376016265 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 11 | A11 | 376016273 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 0.1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 8 | A8 | 366690095 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 35 | C11 | 366711928 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 45 | D9 | 366691359 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 3 | A3 | 376021521 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 32 | C8 | 376021529 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 27 | C3 | 376022129 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 46 | D10 | 376022121 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 0.5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 14 | B2 | 366712026 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 15 | B3 | 366711315 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 54 | E6 | 366696342 | 1x PBS | 0 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 29 | C5 | 376027657 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 43 | D7 | 376027665 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 5 | A5 | 376022035 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 53 | E5 | 376022027 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 1 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 23 | B11 | 366711895 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | 1x PBS | 4 C | Note this is 200ul input not our usual 500ul |
| 3362 | FloodLAMP | NSP17634 | 38 | D2 | 366691369 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 39 | D3 | 366690057 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 22 | B10 | 376004030 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Nasal | 4 C | Looks to me like they have some RNAse activity in Nasal and Saliva |
| 3362 | FloodLAMP | NSP17634 | 34 | C10 | 376022305 | Nasal | 0 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 26 | C2 | 376023473 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 69 | F9 | 376023481 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 2 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 4 | A4 | 376013805 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 28 | C4 | 376013807 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 51 | E3 | 376013806 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 37 | D1 | 376037377 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 60 | E12 | 376037385 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 6 | A6 | 376015191 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 42 | D6 | 376022585 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 5 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 62 | F2 | 376045558 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 66 | F6 | 376045559 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 67 | F7 | 376045557 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 57 | E9 | 376022993 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 59 | E11 | 376022985 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 12 | A12 | 376022681 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 48 | D12 | 376022673 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 10 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 18 | B6 | 376046710 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 55 | E7 | 376046711 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 56 | E8 | 376046709 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 44 | D8 | 376035089 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 47 | D11 | 376035081 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 33 | C9 | 376036601 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 61 | F1 | 376036656 | Saliva | 0 | SARS-CoV-2 | Zepto particles | 25 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 20 | B8 | 376034709 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 31 | C7 | 376034711 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 40 | D4 | 376034710 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 24 | B12 | 376031529 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 30 | C6 | 376031537 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 41 | D5 | 376036393 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 58 | E10 | 376036401 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 50 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 2 | A2 | 376004003 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 36 | C12 | 376023535 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 49 | E1 | 376023543 | 1x PBS | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | 1x PBS | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 17 | B5 | 376035801 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 50 | E2 | 376035793 | Nasal | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Nasal | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 25 | C1 | 376014841 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | NSP17634 | 68 | F8 | 376004822 | Saliva | 1 | SARS-CoV-2 | Zepto particles | 100 | copies/ul | 200 | Saliva | 4 C |  |
| 3362 | FloodLAMP | XP60846 | 37 | D1 | 366719109 | Water | 0 | Twist Human bocavirus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 60 | E12 | 366721496 | Water | 0 | Twist Human bocavirus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 35 | C11 | 366722660 | Water | 0 | Twist Human coronavirus 229E | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 66 | F6 | 366718749 | Water | 0 | Twist Human coronavirus 229E | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 53 | E5 | 366720537 | Water | 0 | Twist Human Coronavirus NL63 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 69 | F9 | 366720553 | Water | 0 | Twist Human Coronavirus NL63 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 18 | B6 | 366718962 | Water | 0 | Twist Human coronavirus OC43 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 27 | C3 | 366721375 | Water | 0 | Twist Human coronavirus OC43 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 7 | A7 | 366721226 | Water | 0 | Twist Human enterovirus 68 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 86 | H2 | 366720181 | Water | 0 | Twist Human enterovirus 68 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 29 | C5 | 366718604 | Water | 0 | Twist Human parainfluenza virus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 45 | D9 | 366718234 | Water | 0 | Twist Human parainfluenza virus 1 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 71 | F11 | 366718621 | Water | 0 | Twist Human parainfluenza virus 4 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 79 | G7 | 366719202 | Water | 0 | Twist Human parainfluenza virus 4 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 3 | A3 | 366721545 | Water | 0 | Twist Human rhinovirus 89 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 58 | E10 | 366720192 | Water | 0 | Twist Human rhinovirus 89 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 22 | B10 | 366718417 | Water | 0 | Twist Influenza A virus H1N1  | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 51 | E3 | 366718921 | Water | 0 | Twist Influenza A virus H1N1  | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 6 | A6 | 366696279 | Water | 0 | Twist Influenza B | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 88 | H4 | 366692526 | Water | 0 | Twist Influenza B | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 28 | C4 | 366713915 | Water | 0 | Twist Influenza H3N2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 70 | F10 | 366718374 | Water | 0 | Twist Influenza H3N2 | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 42 | D6 | 366720411 | Water | 0 | Twist Measles | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 68 | F8 | 366720896 | Water | 0 | Twist Measles | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 48 | D12 | 366713503 | Water | 0 | Twist MERS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 83 | G11 | 366718951 | Water | 0 | Twist MERS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 16 | B4 | 366718269 | Water | 0 | Twist Mumps | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 20 | B8 | 366713397 | Water | 0 | Twist Mumps | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 10 | A10 | 366722643 | Water | 0 | Twist SARS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
| 3362 | FloodLAMP | XP60846 | 77 | G5 | 366718818 | Water | 0 | Twist SARS-coronavirus | Twist Synthetic RNA | 500 | copies/ul | 200 | Water | -80 C |  |
||
