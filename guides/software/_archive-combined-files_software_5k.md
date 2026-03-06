# ===== START OF FILE _archive-combined-files_software_5k.md =====
# software (4 files, 5,389 tokens)

# 859  _context-commentary_guides-software.md
METADATA
last updated: 2026-02-18 RT
file_name: _context-commentary_guides-software.md
category: guides
subcategory: software
words: 709
tokens: 859


CONTENT

## Context
The software subcategory contains three files documenting the FloodLAMP mobile app and admin web portal — the custom software system FloodLAMP developed to manage its decentralized pooled surveillance testing programs.

FloodLAMP built its app on Appivo, a low-code development platform, with the majority of custom code written in JavaScript. The system had three main interfaces serving different user roles: a participant-facing mobile app for onboarding, consent, and sample collection registration; a staff-facing mobile app view for sample intake, processing, and resulting; and an admin web portal for program management, user administration, and data export.

The files in this subcategory include step-by-step guides for the admin web portal and the staff mobile app workflow, as well as instructions for adding minors to household accounts — a feature specific to FloodLAMP's household pooling model. Together, they document the software's role in managing the end-to-end testing workflow: from participant registration and consent, through sample collection and accessioning, to processing, resulting, and notification. Related operational procedures and test site logistics are covered in the operations and test-site subcategories.


## Commentary
The world of software development has changed fundamentally since we built this system, and it's changing fast. With AI-assisted coding now widely available, how a small company would go about developing custom software today is completely different from what we faced. So I think the primary value of our software work for the archive lies not in the technical implementation, but in the specific features and user flows we designed — particularly those tailored to self-collected household pooling, which was central to FloodLAMP's approach.

The app was a critical part of our overall offering, managing everything from participant onboarding and consent to sample tracking and result notification. That said, at least one site — Davie — ran a substantial screening program of hundreds of samples per week entirely without the app, tracking everything manually. So while the software was important, it was not strictly required to operate the testing model.

Most of the features and user flows are described in the files themselves, but one worth highlighting here is the notes field we added to the collection step. During a collection, the sponsor, the person scanning the sample tube and entering which participants contributed swabs to a pooled tube, could use this field to add someone on the fly who wasn't registered in the program. This obviously introduced potential issues: that person may not have consented, their name might be misspelled, and it brought non-registered individuals into the data. But we thought the flexibility was important, and it was pretty widely used in practice. Ideally, you would pair this with post-processing software that could reconcile any unrecognized names added on the fly.

We learned a lot about software development the hard way. We never had any software engineers on staff, and we were building on Appivo, a low-code platform. The FloodLAMP app grew to be quite complex for the Appivo platform at the time, and there were substantial problems on both sides — our inexperience with software and issues with the platform itself. The interaction effects between our app and the Appivo platform created periods of instability, outages, and downtime during critical operational periods, along with persistent bugs. For FloodLAMP being a small biotech company, the software was a constant source of friction.

One particular challenge worth noting was getting the app approved for the Apple App Store. Because of Apple's heightened scrutiny around health apps and COVID-related apps, we were rejected multiple times through the standard review process. It ultimately required reaching out to a high-level contact at Apple, someone I connected with through a COVID testing group call. Without that personal connection, we may not have been able to get the app approved at all. This is an area where there is room for meaningful progress in pandemic preparedness: platform companies like Apple should have expedited review pathways and dedicated attention for pandemic-related applications, rather than subjecting them to impersonal, blanket denials.

One area of software work we planned but never implemented was integrating the program's initial guidance (customized per site), sign-up, consenting, and registration directly into the app itself, so that the entire onboarding flow could be handled in a single streamlined experience rather than across separate systems.


# 250  Adding Minors In the FloodLAMP App - Instructions.md
METADATA
last updated: 2025-12-14 RT updated metadata after BA fixed inconsistencies
file_name: Adding Minors In the FloodLAMP App - Instructions.md
file_date: 2022-09-01
title: Instructions for Adding Minors In the FloodLAMP App
category: guides
subcategory: software
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1K8CDEafa-U68ia6kPqE3_r6Qd37HyehMN1Ef7BYAzxc
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/guides/software/Adding%20Minors%20In%20the%20FloodLAMP%20App%20-%20Instructions.docx
pdf_gdrive_url: https://drive.google.com/file/d/1Wuje2Az8mBWCFBU2P0cQzJjWITW1Wpbv
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/guides/software/Adding%20Minors%20In%20the%20FloodLAMP%20App%20-%20Instructions.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 250
words: 188
notes: screenshot images omitted from md
summary_short: The “Instructions for Adding Minors In the FloodLAMP App” guide explains how an account holder signs consent in the FloodLAMP App, adds minors to their profile using the minor’s name and birth date, and completes minor consent. It also shows how linked minors appear under the household account in the Collection screen so they can be selected as participants when collecting sample tubes for testing.


CONTENT

***INTERNAL TITLE:*** Consent and Adding Minors in The FloodLAMP App

After creating your account via [floodlamp.bio/register-household/](https://floodlamp.bio/register-household/), log into the FloodLAMP App and then read and sign the Consent Form.
_3 screenshot images_

Next, navigate to the profile screen, scroll to the bottom, and select the option to add minors to your profile. Enter the minor’s name and birth date into the fields that appear and hit “Sign Consent” to be prompted with the minor consent.
_3 screenshot images_

Repeat these steps to add each minor individually until all household minors are added. At this stage, you’re all set up to participate in the program\!

Once the minor(s) have been linked to your profile, you will be able to add them through the app each time you collect samples for testing. In the Collection screen, they will appear under the name of the account to which they were added. To find them, simply search for ***your name*** and their name will appear underneath yours in the search list.
_3 screenshot images_

Please follow these steps to include each minor as a Participant when collecting your sample tube(s) for testing.


# 1,603  Guide - Admin Web Portal (WIP).md
METADATA
last updated: 2025-12-15 RT updated metadata after BA fixed inconsistencies
file_name: Guide - Admin Web Portal (WIP).md
file_date: 2022-08-31
title: FloodLAMP Guide - Admin Web Portal (WIP)
category: guides
subcategory: software
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/16TH6wjOZtRGVMECh5dU7p88Pb2hLBkOeHCjvSKsdGGY
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/guides/software/Guide%20-%20Admin%20Web%20Portal%20(WIP).docx
pdf_gdrive_url: https://drive.google.com/file/d/1Hv6mrzamP3zl4O4USFQNSjGtElrOGVd0
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/guides/software/Guide%20-%20Admin%20Web%20Portal%20(WIP).pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1603
words: 1207
notes: some portions are WIP
summary_short: The FloodLAMP Guide – Admin Web Portal (WIP) explains how program administrators use the web portal and mobile app roles to manage onboarding, user access, kits/tube tracking, and exports. It includes practical workflows for adding users and roles, monitoring consent and setup progress, reviewing results in Kits/Tubes views, and resolving common intake and collection issues.


CONTENT

***INTERNAL TITLE:*** Admin Web Portal Guide
_Note: Some portion are Work In Progress_
Overview
All Roles - Brief Description
Admin - Main Tasks
- Login
- Adding other Users and Granting Staff or Admin roles
- Adding users with csv "Import Users" function
- Monitoring Onboarding
- Using Kits and Tubes views
- Triggering password reset links
- Exporting csv of results

Admin - Troubleshooting
- Troubleshoot tubes that does not intake ("No such barcode exists" error message)
- Troubleshoot user that can't be added at collection step

Admin - Advanced
- Changing Consent (must get written approval from FloodLAMP)
- Adding a new participant group

## Overview
The FloodLAMP Mobile App and Admin Web Portal are a system that manages pooled surveillance testing, including:
-   participant onboarding, as individuals and households;
-   electronic consent signing;
-   self-directed pooled sample collection and accessioning;
-   tracking, processing, and resulting sample tubes;
-   participation and results monitoring.

There are 3 main roles for users of the system and corresponding views of the app and portal.

**Participants** - people submitting samples for testing.
The Participant View of the FloodLAMP Mobile App is used for:
-   updating profile information such as name, email, and phone number;
-   adding minors under a guardian’s account;
-   registering pooled sample collections by listing the names of who is contributing samples;
-   checking the status of previously collected sample tubes.

All users of the system typically have the privileges of the Participant role (able to be added to a collection) whether or not they actually have the role included.

**Staff** - people processing samples (i.e. running the actual test in the lab)
The Staff View of the FloodLAMP Mobile App is used for:
-   intaking collected tubes by scanning their QR codes;
-   batching tubes together for processing;
-   updating the status tubes at various points of processing (optional);
-   entering test results (positive, negative, inconclusive, invalid).

Users who have been granted the Staff role should also be granted the AccessStaff role as well, and the term “Staff” usually refers to the users with both roles. These Staff can access the Staff View where they process tubes without access to Personal Identifiable Information (PII). Staff will require moderate training.

**Admin** - program managers
The Admin Web Portal is only available via desktop/laptop browser and not through the FloodLAMP Mobile App, though both are accessing the same database of information. It is used for:
-   managing the entire testing program;
-   overseeing the onboarding process;
-   adding users and granting roles;
-   customizing messages and information;
-   viewing the status of tubes and participants;
-   reviewing results and participation history.

The FloodLAMP Mobile App runs on the Appivo Platform and typically, admin privileges should be granted in each. The “Admin” role is granted within the FloodLAMP Mobile App (under “My Apps” in the Appivo Platform) and gives access to the Admin Web Portal. “System Administrator” is granted in the Appivo Platform and enables granting roles both within the App and Appivo Platform (see above [Adding Users and Granting Staff and Admin Roles](#adding-users-and-granting-staff-or-admin-roles)). 

## All Roles - Brief Description
**Participant** can be added to collections, only needed if user has no other roles
**Sponsor** can perform collections with approval (ignore if using SuperSponsor for all)
**SuperSponsor** can perform collections on anyone, i.e. see everyone in their group when adding to collection
**Staff** can use the Staff View to process tubes
**AccessStaff** add together with Staff role, used for “Access Groups” of Staff to link to Groups (participants)
**PI** special role that receives email and text notifications with PII for Positive and Inconclusive results
**Administrator** can view and utilize the Admin Web Portal
**System Administrator** (Appivo platform role) can change user roles from the Appivo User view in top right

## Admin - Main Tasks
### Login 
Log in at [https://apps.appivo.com/](https://apps.appivo.com/) - your account must have been granted the “Admin” role by a System Administrator in order to view the Admin Web Portal.

### Adding Users and Granting Staff or Admin roles
Go to the Appivo User view (in top right corner under the head circle icon)
_screenshot_

-   pencil edit icon edits user profile info
-   this is also where you can trigger a Password Reset to be sent to the user **(Triggering password reset links)**
_screenshot_

-   clicking the user name or anywhere in the line opens up the view to edit their roles
_screenshot_

Example Admin:
_screenshot_

Example Staff:
_screenshot_

To get back to the Admin Web Portal:
1\)  click “My Apps” from top right menu bar
2\)  click the “FloodLAMP” logo on the left side
_screenshot_

### Adding users with csv “Import Users” function
Specify role - typically SuperSponsor which includes Participant role privileges (WIP)

### Monitoring Onboarding
From the Users tab, you can check if folks who have signed up through the form or had their accounts created (import or manual) have actually clicked through to set their password, signed into the app (where they are prompted right away to sign the consent), and have added minors.
_screenshot_

### Using Kits and Tubes views
These tabs are used to check the status or result of a tube or participant who added to a collection.

It’s also used to review tubes collected that day and who is in them.

“Kits” shows a view where each line is an individual QR coded tube - which could contain a single sample from an individual or from several people in a pool.

“Tubes” shows a view where each line is a Participant, but this is sorted by the Tube ID so you will see the people in a pool listed together.

Apologies to the mixed up terminology - these will be changed shortly.

Tubes Tab
The Tubes tab shows the results of a screening session. This can be used or to track down a Participant or their sample tube. Each row of the table on this tab represents a unique collection event (i.e., Tube ID + Participant or Tube ID + Minor). The Tubes tab allows you to:
-   Find Participants & Minors within a positive pool
-   View timestamp of Staff collection and results
-   See notes added by the Sponsor
-   Search by name or Tube ID
-   Export all data or a date-limited set of data
_screenshot_

Kits Tab
_screenshot_

### Exporting csv of results
Available from either the Kits or the Tubes tab. 

## Admin - Troubleshooting
### Troubleshoot tubes that do not intake (“No such barcode exists” error message)
-   This is usually because a participant forgot to complete the collect step (on Participant view of App).
-   Can also be caused by the barcode/QRcode being manually typed in and being incorrect (such as having a trailing whitespace character).

### Troubleshoot user that can’t be added at collection step
-   If Minor, it’s likely because they are not searching the Guardian name first. Minors are nested underneath the Guardian user that added them.
-   May be due to the email for the Participant user being entered incorrectly.
-   May be due to the Participant user not being included in the group.

## Admin - Advanced
### Changing Consent (must get written approval from FloodLAMP)
WIP 

### Adding a new participant group
WIP


# 1,351  Guide - Mobile App (Staff).md
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
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/main/guides/software/Guide%20-%20Mobile%20App%20(Staff).docx
pdf_gdrive_url: https://drive.google.com/file/d/1lMrxJdblUZKo9-9AkB_tIKDt8nxGU7ZV
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive-wip/blob/main/guides/software/Guide%20-%20Mobile%20App%20(Staff).pdf
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

# ===== END OF FILE _archive-combined-files_software_5k.md =====
