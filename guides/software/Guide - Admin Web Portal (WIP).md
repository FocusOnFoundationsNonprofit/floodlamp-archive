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
