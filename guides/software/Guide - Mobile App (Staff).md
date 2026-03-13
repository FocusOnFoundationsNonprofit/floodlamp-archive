METADATA
last updated: 2025-12-15 RT updated metadata after BA
file_name: Guide - Mobile App (Staff).md
file_date: 2022-09-03
title: Mobile App Guide for Test Site Staff
category: guides
subcategory: software
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1gck3ruk1d_Lcp0M5JMt4FT6kzniqxV3-E443ElkEYUQ
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/software/Guide%20-%20Mobile%20App%20(Staff).docx
pdf_gdrive_url: https://drive.google.com/file/d/1lMrxJdblUZKo9-9AkB_tIKDt8nxGU7ZV
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/software/Guide%20-%20Mobile%20App%20(Staff).pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1351
words: 1018
notes: 
summary_short: The Mobile App Guide for Test Site Staff explains how staff use the FloodLAMP mobile app to move sample tubes through Intake, Process, and Results, including creating or adding to batches and updating tube statuses from “Collected” through “AMP.” It also covers how to enter final results (after any reruns), pull non-negative tubes out of a batch for separate resulting, and notify program administrators (with participant notifications noted as globally disabled for surveillance guidance).


CONTENT

## Overview
The app is used to guide the lab workflow, track the status of collected tubes, and notify the program admin and participants of the completion of the test. The basic steps for the workflow are:
1.  **Intake** – log tubes for processing
2.  **Process** – update status of tubes during the run/set to amp
3.  **Result** – update status of tubes and notify program admin and participants

## Staff App Training
### Accessing the Staff Side 
With an account that has staff privileges (“Staff” and “AccessStaff” roles),, one can change to the Staff Role/View by tapping on the hamburger menu ( ☰ ) in the top left corner.
_Two mobile screenshots showing the hamburger menu (☰) in the top-left corner of the app, and the resulting slide-out menu with the option to switch to "Staff" view._

### Intake Tubes
The Intake step changes the status of tubes from “Collected” to “Received”. Only tubes where the Collection step is completed by the Sponsor will be recognized at the Intake step. Intake can happen before inactivation or while waiting for amplification. Staff can intake tubes into Batches that can be progressed through the system together. Batches are automatically assigned a date-based ID, though you can choose any unique name.
1.  Tap the INTAKE Button
2.  Chose batch action option
    -   NO BATCH: Intake tube individually
    -   CREATE BATCH: Create a new Batch
    -   ADD TO BATCH: Add the tube to an existing batch
3.  Select "CREATE BATCH" and name the new batch or approve the default name
_Three mobile screenshots showing the Staff home screen with the INTAKE button, the batch action options (NO BATCH / CREATE BATCH / ADD TO BATCH), and the batch naming dialog with a default date-based ID._

4.  Scan tubes to add to the batch, or enter the barcode manually (tap “Cancel” to exit the scanner)
5.  Click the **<** button at the top left to return to the home screen
_Two mobile screenshots showing the QR code scanner view for scanning tube barcodes into the batch, and the batch detail view listing the scanned tubes._

### Process Tubes 
The Process view allows staff to update the status of batches or tubes in the run.
-   Tap the PROCESS button on the home page
-   Select the batch or tube (tap the circle to the left) and tap the check button at the bottom of the screen
_Three mobile screenshots showing the PROCESS button on the Staff home screen, the Process view listing batches with selection circles on the left, and the check/confirm button at the bottom of the screen._

Update the status of a batch or tube by selecting an option and tapping "Update status"
-   “RECEIVED” is the status after the Intake step
-   “INACTIVE” is the inactivation step
-   “AMP” is the amplification step – selecting this status moves batches and tubes to the "RESULTS" view

If only processing a single batch of tubes, it’s advised to skip updating the batch for the inactivation stage. You may update to AMP as soon as the samples are on the amplification heater. After doing so, you’ll no longer see the batch in the process screen. Tap the (＜) in the top left to return to the main staff view.
_Two mobile screenshots showing the status update screen with selectable options (RECEIVED, INACTIVE, AMP) and an "Update status" button, and the confirmation view after updating a batch to AMP status._

### Resulting Tubes
At this stage, you have completed running the physical test, and you know the result for every pool. The Result you input into the App is the final result, after any reruns if done (i.e. the final “call”). In most batches, all tubes will be negative. In the instances where this is not the case, you must pull the non-negative tubes out of the batch so that they can be resulted separately.

To pull out a tube from a batch: (see video [App Staff - Pulling tube out of batch](https://vimeo.com/745913329/4239dafd1c))
1.  Tap the right arrow icon (➔) on the right end of the row
2.  Search for the tube(s) with the non-negative result(s)
3.  Press the small red “✕” on the right end of the row to remove the tube from the batch
4.  The tube(s) should now appear in the section below the list of batches in the results screen and can be resulted individually
_Three mobile screenshots showing the batch detail view with the right arrow (➔) icon, the expanded tube list with red "✕" buttons to remove individual tubes, and the Results screen with pulled-out tubes listed separately below the batches._

Tubes or batches marked as "AMP" in the Process step are visible in the Results view
1.  Tap RESULTS on home screen
2.  Select the desired tubes or batches to modify and tap UPDATE at the bottom left of the screen
3.  Tap RESULT in the pop-up screen to update the status of the tube or batch. Result options will appear:
    a.  NULL – no value (this is the default)
    b.  INVALID – If the negative or positive controls do not produce negative and positive results, respectively, then the remaining results cannot be interpreted and the run is considered invalid
    c.  INCONCLUSIVE – test result is neither clearly positive or negative, beyond the edge case colors
    d.  NEGATIVE – a negative result
    e.  POSITIVE – a positive result

**Note:** Marking a tube as positive notifies all listed PIs in the tenant of the result.
Select the result and tap “Update Status.”

4.  On the Result screen, select the desired tubes or batches and tap NOTIFY, then OK if you wish to continue.
    a.  This moves the tube to history and changes participant and sponsor tube status to “completed”.
    b.  *Note: Notifications to Participants are currently turned off globally in the FloodLAMP Mobile App to comply with non-diagnostic surveillance testing guidance.*
_Three mobile screenshots showing the Results view with AMP-status batches/tubes and the UPDATE button, the result selection options (NULL / INVALID / INCONCLUSIVE / NEGATIVE / POSITIVE) with "Update Status" button, and the NOTIFY confirmation dialog._
