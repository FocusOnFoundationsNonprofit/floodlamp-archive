METADATA
last updated: 2026-02-16 BA after RT initial conversion
file_name: SOP-201-A_2 PGS48 Manufacturing - Run Form.md
file_date: 2022-02-26
title: FloodLAMP QMS SOP-201-A_2 PGS48 Manufacturing - Run Form
category: guides
subcategory: manufacturing
tags: 
source_file_type: gdoc
xfile_type: docx
gfile_url: https://docs.google.com/document/d/1OE4rCaCn2htHdlq_Q_Nk9Mu-MpMgTtwO
xfile_github_download_url: https://raw.githubusercontent.com/FocusOnFoundationsNonprofit/floodlamp-archive/main/guides/manufacturing/SOP-201-A_2%20PGS48%20Manufacturing%20-%20Run%20Form.docx
pdf_gdrive_url: https://drive.google.com/file/d/1QPBDtkL4h9dFd4yP_X8J5ZpmaJNkUPYJ
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/manufacturing/SOP-201-A_2%20PGS48%20Manufacturing%20-%20Run%20Form.pdf
conversion_input_file_type: docx
conversion: pandoc
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 1444
words: 842
notes: 
summary_short: The FloodLAMP QMS SOP-201-A_2 is a manufacturing run form for producing PGS48 (Primer-Guanidine Solution, 48-reaction aliquots). It covers preparation, safety procedures, step-by-step PGS mixing instructions (primer resuspension, guanidine-HCl addition, vortexing), materials checklist with product/lot tracking, and robotic aliquoting on an Opentrons liquid handler. The form includes write-in fields for location, operator, date, and lot tracking, plus startup/shutdown procedures for the Opentrons robot.


CONTENT

FloodLAMP Biotechnologies
**Document Number:** SOP-201-A
**Effective Date:** 02/26/2022
**Version:** 2

***INTERNAL TITLE:*** PGS48 Manufacturing - Run Form

## PREP
- Safety Procedures:
  - Work in PCR Box or BSC
  - **Designated CLEAN** Lab coat, gloves, face mask, and face shield/goggles
- Wipe down all work surfaces, tube racks, and all items used with 10% bleach solution followed by ethanol (as needed)
- Turn on UV lamp for 15 minutes in PCR Box or BSC (at start or end of prev run)
- Check to ensure you have **sufficient amounts of all materials** for number of lots to be created ([Calculator](https://docs.google.com/spreadsheets/d/13lsSll6-xEt3S978Hygg-NN1sRpHmo3qctL8WpOq_JU/edit?gid=0#gid=0))
- With Scale (USSolid1), **measure 28.2mL of NF Water** in 50mL Falcon Tube, leave **in the refrigerator > 1hr** (prep ahead).
- **Ensure Primer Resuspension NF Water is also in refrigerator > 1 hr** (prep ahead).
- **Do Startup** of the Opentrons (last page).
- **Load Opentrons software**, open protocol "iPGS48_x68_SOP-201-B_2.json"

## PREP USER WRITE IN
_QR Code_ PGS48 Manuf SOP
[Log Form Link](https://docs.google.com/forms/d/1WZ_MRSIV70tB_JvaW4fMwJGhpsMDjF50mVi8yF8p3nA/edit?usp=drive_web&ouid=111730229766683196858)
Location:
Name:
Date and Time:
PGS48 Lots Created:

Materials
- 50mL Falcon Tube (1)
  - Confirm Product ID & Lot in Log Form
- 1.5mL S.C. Tubes (67)
  - Confirm Product ID & Lot in Log Form
- Nuclease-free Water (2)
  - Confirm Product ID & Lot in Log Form
- FloodLAMP Primer Tubes (9)
  - Confirm Product ID & Lot in Log Form
- 6M Guanidine HCl
  - Confirm Product ID & Lot in Log Form
- Pipette ID
  - Confirm Product ID & Lot in Log Form
- 1000uL micropipette tips
  - Confirm Product ID & Lot in Log Form
- Robot tips (Opentrons 1000uL Filter Tip)

Equipment in AirClean Box
- Mini-centrifuge
- Vortex
- Timer
- 50mL & 1.5mL tube racks
- Tip waste bin

## MAKE PGS
- **Thaw three tubes of each primer set for 10-30min after pulling from freezer**
- Spin down primer tubes after thawing
- Get 50mL Falcon Tube of NF water (at least 10mL), put in rack in hood.
- Add 1000uL of Primer Resuspension NF Water to each tube of primers
  - Do NOT stick pipette tip into tube, primers will stick to tip
  - Air drop (no contact) dispense into tubes, no tip change
- **Vortex for 10s** to dissolve
- **Let sit 1min**, then vortex again 10s
- **Centrifuge** tubes briefly
- Retrieve NF water aliquot from fridge, check that volume appears ~28.2mL
- **Add 600uL of 6M Guanidine-HCl** to NF water in 50mL Falcon Tube
- **Mix** by vortexing 10s
- **Add the full volume of all nine tubes of Primer sets** to the 50mL Falcon Tube
  - Careful to get last bit of liquid (look)
- **Mix well** by vortexing 30s
- Remove cap and pipet any liquid in the cap and add back into the tube
- **Keep PGS mix in refrigerator** until aliquoting or aliquot within 5min

## ALIQUOT ON OPENTRONS
- **Arrange the robot deck** according to deck layout shown below
  - Remove lid from tip box, **verify that there is a tip in the back-left position**
  - Fill the back and front row of each of the six tube racks with 1.5mL SC tubes, uncapped
  - Place the 50mL PGS reservoir tube in the plate at position "8"
- **Click** "Proceed to Calibrate" button
- **Follow on-screen instructions** to complete calibration procedure
- **Click** "Start Run"
- When protocol has finished, **cap all tubes** inside the Opentrons hood
- **Transfer tubes** to cryobox, store at -20C.
- Label cryobox lid with "PGS48" & Lot#.
- **Click** "Reset Run" on OpenTrons software

Notes:
- Make sure the caps are not obstructing the openings of the neighboring tubes.
- Ensure that the 50mL tube is fully seated in the holder with 10mL mark just showing.
- Calibration procedure necessary only on the first run. Subsequent runs won't require re-calibration until the robot is disconnected/reconnected or a different program is run. Calibrate 1.5mL tube with tube out and center XY with respect to rack hole.
- Note that the final 1-2 tubes may be short on volume. These should be either used to do QC verification of the batch or discarded. Write with a marker a "•" on the top of any short tubes.
- Measure remaining volume in Falcon tube: if outside 450uL +/- 10uL, weigh all tubes individually. Spec is X to Y g, reject any tubes outside spec.

_[Deck Layout Diagram - see source PDF for image]_

## OpenTrons Startup
1. Turn on rocker power switch in back left (-- mark).
2. Press flashing blue button on front, wait until solid.
3. If not already open, launch OpenTrons application with shortcut on desktop.
4. Start Hepa unit and put at setpoint.
5. Take lid tipbox cover off.
6. Ensure tip is in back left position of tipbox.
7. Open json protocol.
8. Run calibration.
9. Leave front panel closed (down) when running.

## OpenTrons Shutdown
1. Place lid tipbox cover on.
2. Turn off Hepa unit.
3. Turn off OpenTrons rocker power switch (O mark).
4. Close front panel.
