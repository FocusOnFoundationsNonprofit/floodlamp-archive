METADATA
last updated: 2026-03-06 by BA
file_name: XPrize FloodLAMP Submission - QS Part 3_ Current Capacity _ Scalability.md
file_date: 2020-09-08
title: FloodLAMP XPRIZE Qualifying Submission - QS Part 3 Current Capacity and Scalability
category: various
subcategory: xprize
tags:
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1sQKsJTu9oNw76n8sHOpnzwf6LHd0j_8q/
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/various/xprize/XPrize%20FloodLAMP%20Submission%20-%20QS%20Part%203_%20Current%20Capacity%20_%20Scalability.pdf
conversion_input_file_type: pdf
conversion: msmid
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1110
words: 833
notes: 
summary_short: FloodLAMP's XPRIZE QS Part 3 (Current Capacity and Scalability) submission details the team's testing throughput (50 tests/day current, 200K/day potential with pooling at 100), 2-hour sample-to-result time, sub-$1 per-test cost, sub-$10K capital expense, and plans for scaling through automation with OpenTrons liquid handling and open-source distribution to other labs.


CONTENT

***INTERNAL TITLE:*** FloodLAMP XPRIZE Qualifying Submission - QS Part 3: Current Capacity and Scalability

### HOW MANY TESTS DO YOU CURRENTLY RUN PER DAY?
Approximately 50. We are still in development, not yet running pilots or production. Last week we ran a batch of 24 diluted samples at the 2mL volume (for 10 pools)—a simulation of a run that would comprise 240 individuals.

### HOW MANY TESTS COULD YOU RUN PER DAY WITH CURRENT SETUP?
200,000, but this is difficult to answer and depends on what is meant by "current setup." Our organization is still doing development but we are growing quickly. The 200,000 number is based on our current leased-lab space at MBC Biolabs, which includes 2 biosafety cabinets, 4 lab bench, and 1 chemical fume hood. It is based on a pooling level of 100, which our LOD supports while still reaching the threshold of infectiousness (~1e6/mL). Likely we will not run many 100 pools immediately and will primarily run 10 pools. The 200,000 number is also based on a 1 hr hands-on time per batch using multichannel pipettes, which is the first configuration we are optimizing in order to spread this screening capability and enable other labs without automation to scale quickly. With a single liquid handling robot, such as an OpenTrons or Bravo (which we intend to bring online in Sept), the hands-on time per batch would go down to minutes and the same personnel could run at least 10X the number of samples/pools.

### HOW LONG DOES IT TAKE TO GO FROM SAMPLE COLLECTION TO RESULTS (MINUTES)?
2 hrs, though again, this is difficult to answer and can be misleading for our program. We are integrating several components of a screening system to achieve mass scale. Our screening system is designed to find unknown new infections among large populations which will be re-screened frequently. Therefore, a 12 hr turnaround for results is sufficient. Through planning or fast-tracking batches, we could reasonably expect 4 hr sample-to-result times.

### WHAT IS THE HANDS-ON TIME (MINUTES)?
1 hr per batch of 45 pooled samples (pool level of 10-100) if using multichannel pipettors. 5-10 minutes if using liquid handling robots.

### HOW MANY TESTS CAN BE RUN PER DAY WITH ONE SETUP?
10K per 24 hr day, assuming no automation, several shifts, and a total of about 10 staff. This scales to 100K+/day with the addition of automation.

### COULD THE TEST BE ADAPTED TO POINT OF CARE?
No

### CAPITAL EXPENSE:
Less than $10K to purchase all the equipment for the baseline lab configuration from scratch. However, most labs will likely already have most of the necessary equipment.

### ESTIMATED COST PER TEST:
<$1, highly dependent on pool level. Current per pool costs are dominated by the NEB LAMP MM (1804) which is $2/rxn in small volumes and approx $0.75 in very large volumes. Consumables cost per pool are currently approximately $5, dropping to <$3 in large volumes. The cost could potentially drop significantly further if the open source LAMP Master Mix using the HIV-1 RT is produced and made available to the LAMP community at a cost less than NEB's product.

### ESTIMATED COST PER RUN:
For the non-automated configuration using multichannel pipettes, a batch size of 45 samples would currently cost approximately $150 in consumables and need 3 hours of labor. At $40/hr labor charge, the batch cost comes to $270. Assuming the standard pool size of 10, that covers 450 people for a primary screen.

### IS THIS TEST CAPABLE OF POOLING SAMPLES?
Yes

### DO YOU CURRENTLY POOL SAMPLES?
Yes

### IF YES, HOW MANY SAMPLES DO YOU CURRENTLY POOL?
We typically pool 2-5 individuals for our development runs, but do so in a total volume of 5mL (assumes 0.5mL per individual in the pool). One of the key concerns for pooling larger numbers of people (even 10) is whether inhibitors or adulterants present in one sample will cause a failure of the pool. We point to China's success at large scale sample pooling at the level of 10 using cheek swabs as evidence for optimism.

### WHAT ARE THE CURRENT LIMITATIONS TO SCALE THIS TEST?
The key limitation of our current configuration is not using automation. However, development of this mode is intentional, as access to liquid handling robots and the resources to feed them would be limiting for many, many labs. With multichannel pipetting and the baseline configuration we are developing, those labs can scale to 10K+ people per day screened. Another limitation is the use of silica rather than magnetic beads. Again, this choice has been intentional due to the availability and cost of magnetic capture beads. This is something we will investigate and consider bringing up in parallel to silica. Practically, we are currently limited in resources—both funding and staffing. We closed our first seed investment last week and expect more funding soon. Recruiting qualified employees is particularly challenging now, but we intend to do further outreach and publicize our efforts very soon.
