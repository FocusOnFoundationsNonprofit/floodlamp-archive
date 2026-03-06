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
