##### Commentary on DAVI Referral-Antigen Comparison Data (AI Generated - Opus 4.6)
The Davie site produced the archive's most detailed head-to-head comparison between FloodLAMP and BinaxNOW rapid antigen testing, tracking 51 employee cases through three evolving testing protocols during the Delta and Omicron waves. Across cases where both tests were administered on the same day, FloodLAMP and BinaxNOW agreed 90% of the time. In the remaining 10% of cases -- four employees -- FloodLAMP detected the infection while BinaxNOW did not. Three of those four were asymptomatic. There were no cases where antigen detected a positive that FloodLAMP missed. During the intensive dual-testing phase (Group 2, Dec 24 -- Jan 9), when both tests were used for daily follow-up through return to work, the two tests tracked closely, typically clearing on the same day. This pattern suggests that the practical sensitivity difference between FloodLAMP and antigen testing was concentrated at the onset of infection, particularly in asymptomatic or low-viral-load individuals -- precisely the detection gap that molecular screening is designed to address. The Davie data, combined with the anecdotal reports from Coral Springs where 21 of 22 FloodLAMP positives in a single plate were antigen-negative but subsequently confirmed, reinforced a consistent finding across the pilot programs: BinaxNOW rapid antigen tests lagged FloodLAMP molecular detection at infection onset, especially in asymptomatic individuals.

##### Analysis of DAVI Referral-Antigen Comparison Data (AI Generated - Opus 4.6)
The file tracks 51 employee COVID cases at the Davie Fire and Rescue site across three protocol phases during the Delta and Omicron waves (Sept 2021 -- Feb 2022), each with a different approach to using FloodLAMP (FL) and BinaxNOW rapid antigen (B) together:

- **Group 1** (15 employees, Sep 15 -- Dec 23): FL as primary test; BinaxNOW used sometimes at home on Day 0. Only 8 of 15 had same-day antigen comparison data.
- **Group 2** (22 employees, Dec 24 -- Jan 9): Both FL and BinaxNOW used throughout until return-to-work clearance. This is the most informative group for head-to-head comparison.
- **Group 3** (14 employees, Jan 10 -- Feb 7): FL for initial detection/diagnosis; BinaxNOW for return-to-work clearance. FL was not used for ongoing follow-up.

###### Key findings

1. **Same-day concordance on Day 0**: Of ~42 cases with same-day FL and antigen results, 38 (90.5%) agreed (both positive) and 4 (9.5%) disagreed -- all 4 being FL-positive / antigen-negative. There were zero cases of antigen catching a positive that FloodLAMP missed.

2. **Sensitivity advantage in asymptomatic cases**: Of the 4 FL+/B- discordant cases, 3 (75%) were asymptomatic. By contrast, only 31.6% of the concordant FL+/B+ cases were asymptomatic. This suggests FloodLAMP's molecular sensitivity was most valuable in exactly the population with lower viral loads where antigen tests are known to underperform.

3. **Group 2 tracking data**: When both tests were run side by side over the course of illness, they generally agreed on a day-to-day basis and cleared on the same day. The average time to negative was approximately 9 days (range 5--14). This close tracking indicates that when viral load was high enough for antigen detection, the two tests gave consistent results -- the divergence arose at low viral loads near detection onset.

4. **Zero false positives**: Across the full DAVI program, the stats file reports 0 false positives and 0 suspected false negatives for FloodLAMP, with 97.7% of FL positives confirmed by referral or correspondence.

###### Inconsistency - (CAN REMOVE; ERROR HAS BEEN CORRECTED)
The inconsistency is in the original xlsx spreadsheet, not in the md processing. The md file faithfully reproduced what was in the spreadsheet.
Here's what's happening:
The correct numbers come from the "Same Day" summary table (columns AB--AD, rows 2--6), which uses proper COUNTIFS formulas scanning the structured data columns. These correctly compute FL+/B+ = 38 and FL+/B- = 4 (total 42 same-day comparisons).

The incorrect "11 (73.3%)" numbers come from cells K7--K8 and L8 in the legend/header area, which use a broken formula chain:
Cell K7 = 4 (hard-coded) -- the total FL+/B- count. This number is correct.
Cell E11 = SUM(E14:E80) = 15 -- this counts column E, which is a flag marking asymptomatic employees who had same-day antigen testing (15 of the 18 total asymptomatic cases; the 3 without the flag -- emps 4, 11, 12 -- had no antigen test).

Cell K8 = E11 - K7 = 15 - 4 = 11 -- labeled "FL+ and B+" but actually computing "asymptomatic-with-antigen minus total FL+/B-," which is a nonsensical subtraction of two unrelated quantities.
Cell L8 = K8/(K7+K8) = 11/15 = 0.7333 (73.3%)

The most likely explanation is that these cells K7/K8/L8 were written at an early stage -- possibly when only Group 1 (15 employees) existed and column E may have been used differently (e.g., as a general count). When Groups 2 and 3 were added along with the proper structured columns (X--AH) and the correct COUNTIFS summary table (AB--AD rows 2--6), the old K7/K8 formulas were never updated. They now point at a cell (E11) whose meaning shifted, producing a spurious result.

Bottom line: The "Same Day" summary table (FL+/B+ = 38, FL+/B- = 4) is the authoritative data. The "11 (73.3%)" line is a stale, broken formula artifact in the original spreadsheet. The md processing was faithful -- it just reproduced both the correct and incorrect values from the source.

## Human Verification Checklist

Instructions: Verify each claim below against the source data file `DAVI_pilot-data_referral-antigen-comparison.md` and the stats file `DAVI_pilot-data_summary.md`. The claims are quoted from the AI-generated commentary and analysis above. Multiple checkboxes may appear under a single claim; each is a distinct item to verify.


### Commentary Paragraph Checks

> "tracking 51 employee cases" - CONFIRMED

[] Count employee rows in Group 1 "As Reported" table. Expected: 15 (employees 1--15).
[] Count employee rows in Group 2 "As Reported" table. Expected: 22 (employees 16--37).
[] Count employee rows in Group 3 "As Reported" table. Expected: 14 (employees 38--51).
[] Confirm 15 + 22 + 14 = 51.

> "three evolving testing protocols during the Delta and Omicron waves" - CONFIRMED

[] Confirm three distinct groups exist in the source file with three different testing protocols.
[] Group 1 dates (Sep 15 -- Dec 23, 2021) overlap with the Delta wave in the US.
[] Group 2/3 dates (Dec 24 onward) overlap with the Omicron wave in the US.

> "FloodLAMP and BinaxNOW agreed 90% of the time" - CONFIRMED

[] Locate the summary table at the top of the source file under "Summary: Same Day Test Comparison."
[] Confirm FL+, B+ total = 38.
[] Confirm FL+, B- total = 4.
[] Compute: 38 / (38 + 4) = 38 / 42 = 0.9048 ≈ 90.5%. Confirm "90%" is a fair rounding.

> "four employees -- FloodLAMP detected the infection while BinaxNOW did not" - CONFIRMED

[] Identify the 4 FL+/B- employees by scanning Day 0 results in all three "As Reported" tables. They should be:
[] Employee 14 (Group 1): Day 0 = "FL +, B -, ASY"
[] Employee 18 (Group 2): Day 0 = "FL +, B -, ASY"
[] Employee 41 (Group 3): Day 0 = "FL +, B -, SYM"
[] Employee 45 (Group 3): Day 0 = "FL +, B -, ASY"
[] Confirm no other employees in any group have FL+, B- on Day 0.

> "Three of those four were asymptomatic" - CONFIRMED

[] Of the 4 FL+/B- employees identified above, confirm 3 have ASY in Day 0 (emps 14, 18, 45) and 1 has SYM (emp 41).
[] Cross-check against the summary table: FL+, B- row shows Asymptomatic = 3, Symptomatic = 1.

> "There were no cases where antigen detected a positive that FloodLAMP missed" - CONFIRMED

[] Scan all Day 0 results in all three "As Reported" tables for any case of "FL -, B +" or "B +, FL -" or "B +" without FL+. Expected: none.
[] Note employee 21 (Group 2) Day 0 is "B + SYM" without FL. In the Structured table, Day 0 FL is blank and "Same Day Antigen" = False. Confirm this case is excluded from the same-day comparison (not counted in the 42) and therefore does not represent a FL miss.
[] Note employee 43 (Group 3) Day 0 is "SYM" without any test result. Confirm this is also excluded ("Same Day Antigen" = False).

> "Group 2, Dec 24 -- Jan 9" - CONFIRMED

[] Confirm Group 2 header in source file says "Testing between Dec 24th and Jan 9th."
[] Confirm Group 2 Structured table dates show 2021-12-24 and 2022-01-09.

> "the two tests tracked closely, typically clearing on the same day" - CONFIRMED

[] In Group 2 Structured table, for every row where both "Day # FloodLAMP Neg" and "Day # Antigen Neg" have values, compare the two numbers. Expected: all 18 such pairs are identical (same day).
[] Specifically verify these pairs (employee: FL neg day, B neg day):
[] Emp 16: 6, 6
[] Emp 21: 12, 12
[] Emp 22: 6, 6
[] Emp 23: 8, 8
[] Emp 24: 8, 8
[] Emp 25: 9, 9
[] Emp 26: 8, 8
[] Emp 27: 10, 10
[] Emp 28: 9, 9
[] Emp 29: 14, 14
[] Emp 30: 12, 12
[] Emp 31: 10, 10
[] Emp 32: 11, 11
[] Emp 33: 8, 8
[] Emp 34: 10, 10
[] Emp 35: 5, 5
[] Emp 36: 8, 8
[] Emp 37: 10, 10
[] Confirm 4 rows (emps 17, 18, 19, 20) have blank FL neg day and only antigen neg day. These are excluded from the "same day clearing" comparison.

> "21 of 22 FloodLAMP positives in a single plate were antigen-negative but subsequently confirmed" (Coral Springs reference) - CONFIRMED

[] This claim is NOT from the DAVI data. It references Coral Springs (COSP) program.
[] Verify against `_context-commentary_pilots-pilot-data_INITIAL.md`, COSP commentary section. The text there says: "the highest number of positives they had in a single plate, which was 22...only one of the 22 were antigen positive (BinaXNow)."
[] Confirm 22 - 1 = 21 antigen-negative is the correct derivation.


### Analysis Section Checks

> Group 1: "15 employees, Sep 15 -- Dec 23" - CONFIRMED

[] Count rows in Group 1 "As Reported" table: expected 15 (employees 1--15).
[] Count rows in Group 1 "Structured" table: expected 15.
[] Confirm source header says "Testing between Sept 15th and Dec 23rd."

> "Only 8 of 15 had same-day antigen comparison data" - CONFIRMED

[] In Group 1 Structured table, count rows where "FloodLAMP Test with Same Day Antigen" = True. Expected: 8.
[] Identify the 8 True rows: employees 1, 2, 3, 7, 8, 9, 10, 14 (match to Structured table row order).
[] Count remaining False rows: expected 7 (employees 4, 5, 6, 11, 12, 13, 15).

> Group 2: "22 employees, Dec 24 -- Jan 9" - CONFIRMED

[] Count rows in Group 2 "As Reported" table: expected 22 (employees 16--37).
[] Count rows in Group 2 "Structured" table: expected 22.
[] Confirm source header says "Testing between Dec 24th and Jan 9th."

> Group 3: "14 employees, Jan 10 -- Feb 7" - CONFIRMED

[] Count rows in Group 3 "As Reported" table: expected 14 (employees 38--51).
[] Count rows in Group 3 "Structured" table: expected 14.
[] Confirm source header says "Testing between Jan 10th and Feb 7th."

> "Of ~42 cases with same-day FL and antigen results, 38 (90.5%) agreed and 4 (9.5%) disagreed" - CONFIRMED

[] Count all "True" entries in "FloodLAMP Test with Same Day Antigen" column across all three Structured tables. Expected: 8 + 21 + 13 = 42.
[] Group 2: Count True entries. Expected: 21 (emp 21 is the one False, with blank FL result Day 0).
[] Group 3: Count True entries. Expected: 13 (emp 43 is the one False, with no Day 0 test results).
[] Confirm 38 / 42 = 0.9048 = 90.5%.
[] Confirm 4 / 42 = 0.0952 = 9.5%.
[] Cross-check these totals against the summary table at top of source file: FL+, B- = 4, FL+, B+ = 38, total = 42.

> "Of the 4 FL+/B- discordant cases, 3 (75%) were asymptomatic" - CONFIRMED

[] Confirm 3/4 = 0.75 = 75%.
[] Cross-check against summary table: "% Asymp" row under FL+, B- column = 0.75.

> "only 31.6% of the concordant FL+/B+ cases were asymptomatic" - CONFIRMED

[] From the summary table, FL+, B+ column: Asymptomatic = 12, Total = 38.
[] Compute 12 / 38 = 0.3158 = 31.6%. Confirm.
[] Cross-check against summary table: "% Asymp" row under FL+, B+ column = 31.6%.

> "The average time to negative was approximately 9 days (range 5--14)" - CONFIRMED

[] Using Group 2 Structured table only, list all "Day # FloodLAMP Neg" values that are not blank: 6, 12, 6, 8, 8, 9, 8, 10, 9, 14, 12, 10, 11, 8, 10, 5, 8, 10. Expected count: 18.
[] Compute sum: 6+12+6+8+8+9+8+10+9+14+12+10+11+8+10+5+8+10 = 164.
[] Compute average: 164 / 18 = 9.11. Confirm "approximately 9" is fair.
[] Confirm minimum value = 5 and maximum value = 14 (range 5--14).
[] Alternatively, using "Day # Antigen Neg" for all 22 Group 2 rows: sum = 6+12+14+9+9+12+6+8+8+9+8+10+9+14+12+10+11+8+10+5+8+10 = 208. Average = 208/22 = 9.45. Also approximately 9. Range also 5--14.

> "the stats file reports 0 false positives and 0 suspected false negatives" - CONFIRMED

[] In `DAVI_pilot-data_summary.md`, locate "False Positives Final Results" row. Expected value: 0.
[] In `DAVI_pilot-data_summary.md`, locate "False Negative Final Results (Suspected)" row. Expected value: 0.

> "97.7% of FL positives confirmed by referral or correspondence" - CONFIRMED

[] In `DAVI_pilot-data_summary.md`, locate "% FloodLAMP Positive or Inconclusive with Referral / Correspondence Positive" row. Expected value: 97.7%.
[] Note the comments column for that row explains the one unconfirmed case: antigen negative same day, no follow-up antigen, but FL positive 4 more times and person became symptomatic.


### Internal Consistency Check (Summary Table vs. Raw Data)

These checks verify that the summary table at the top of the source file is itself consistent with the row-level data.

> Summary table: FL+, B+ Asymptomatic = 12 - CONFIRMED

[] Count all employees across all three groups where Day 0 shows both FL+ and B+ AND ASY. List them and confirm total = 12.
[] Expected: Emps 1, 16, 17, 23, 31, 36, 38, 39, 40, 44, 46, 47 (verify each).

> Summary table: FL+, B+ Symptomatic = 26 - CONFIRMED

[] Count all employees across all three groups where Day 0 shows both FL+ and B+ AND SYM. Confirm total = 26.

> Summary table: FL+, B- Asymptomatic = 3 - CONFIRMED

[] Confirm: Emps 14 (ASY), 18 (ASY), 45 (ASY). Total = 3.

> Summary table: FL+, B- Symptomatic = 1 - CONFIRMED

[] Confirm: Emp 41 (SYM). Total = 1.

> Source file line: "+ on FloodLAMP and + on BinaxNOW: 11 (73.3%)" - CONFIRMED ERROR AND CORRECTED

[] This line appears to be inconsistent with the summary table (which says 38). Determine if "11" refers to a subset (possibly Group 1 only, or a different counting method). Flag for author review.
[] Note: If this is Group 1 only, count FL+, B+ in Group 1 "As Reported": Emps 1, 2, 3, 7, 8, 9, 10 = 7, not 11. The number 11 does not obviously correspond to any subset. The "73.3%" also does not match 7/15 (46.7%) or 38/51 (74.5%). This likely needs author clarification.


### End of Checklist