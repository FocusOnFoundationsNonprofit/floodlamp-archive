METADATA
last updated: 2026-02-16 RT
file_name: _context-commentary_guides-operations.md
category: guides
subcategory: operations
words: 898
tokens: 1145


CONTENT

## Context
The operations subcategory contains three files addressing the organizational and logistical underpinnings of FloodLAMP's testing programs. Unlike the test-site subcategory, which houses the protocols, setup guides, and training materials that front-line test administrators and staff used,  these files capture the higher-level planning: what the economics looked like, what inventory was required, and what primers needed to be ordered.

The Cost Model is a working spreadsheet that modeled cost-of-goods-sold at various production scales. It reflects the iterative process of understanding what decentralized LAMP-based testing would actually cost, tracking the relative weight of each cost driver — from the dominant NEB LAMP master mix down to individual consumables and labor. Multiple versions were produced as the operation evolved; this represents one of the more mature iterations.

The Inventory Dashboard was a practical tracking tool for cataloging everything from pipettes and heat blocks to biohazard bags and collection swabs. It gives a concrete picture of the material complexity involved in running FloodLAMP's pop-up lab model. This involved dozens of distinct items spanning reagents, consumables, equipment, lab supplies, collection materials, and training kits. FloodLAMP also used Airtable and other systems for inventory management; the dashboard here is one view of a broader logistics effort.

The LAMP Primers document specifies the primer sets (derived from the Rabe–Cepko protocol) used for FloodLAMP's SARS-CoV-2 assay, along with ordering and handling specifications. Primer procurement was a key operational step — sourcing HPLC-purified primers at the required quantities and concentrations was not trivial, and this document captures the standardized ordering information that supported that process.

For readers wanting to explore the actual cost breakdowns, inventory details, or primer sequences, the source spreadsheets are included in the archive and are well-suited for AI-assisted exploration.


## Commentary
The operational and supply chain challenges were among the most persistent day-to-day problems we faced. Ideally, we would have contracted with a major distributor — Fisher Scientific, USA Scientific, or similar — to handle the full kitting of our lab supplies. In practice, that was not realistic for FloodLAMP given our volumes and lack of an EUA. No single supplier carried everything we needed, and given our unusual model of deploying pop-up labs in non-laboratory settings with non-laboratory staff, the selection of specific supplies and labware was deliberate. Some items could be substituted without issue, but others would create downstream problems if swapped. We eventually settled on a good set of materials, but the way we managed kitting and distribution was fundamentally not scalable. The scalability problem came from several converging factors: our small organizational size, operational inexperience, lack of established supplier partnerships, and the persistent iteration of kit compositions as the assay and protocols evolved. A more scalable approach would have combined top-down and bottom-up elements — standardized kit specifications and equipment bundles that established suppliers could assemble and ship, paired with clear documentation of acceptable substitutions and flexibility ranges so that smaller labs and pop-up operations could also source and validate their own combinations. 

A good example of this evolution is the tube barcoding process. Early on, we had interns manually applying barcode labels to collection tubes — a tedious, labor-intensive task. We then sourced custom QR-coded tubes from a Chinese manufacturer (Jable), which was a major improvement. However, the minimum order quantity was large and the lead time stretched to several months. During those waiting periods, we still had interns and TaskRabbit workers coming in to manually barcode tubes by hand for days at a time.

The swab and collection tube situation was another significant challenge. Like most testing operations during the pandemic, we had difficulty sourcing swabs. But our specific problem was harder than most: we needed a swab with a breakpoint that would leave the remaining tip and shaft fitting inside a reasonably sized tube, and would accommodate 4 swab tips for pooling. We settled on a 5mL tube as our main collection vessel (the mini system used 1.5mL tubes) and tried many tube-and-swab combinations before finding one that worked. The swab we ultimately adopted was, of all things, a urethral swab. We ended up ordering 100,000 swabs and tubes from Jable. We even hired a consultant to tackle the swab sourcing problem, but that effort didn't produce useful results.

For NEB's colorimetric LAMP master mix — by far our largest single cost item — we arranged for NEB to drop-ship directly to test sites for larger orders, which significantly streamlined logistics.

The core lesson from our operational experience is: simplify relentlessly. Every part you can eliminate reduces cost, training burden, and failure modes. Every standard, off-the-shelf item you can use in place of something custom reduces lead times and sourcing risk. For heating, we found that water baths, dry heat blocks, and even repurposed PCR machines all served as workable heaters — flexibility in equipment selection was critical given our resource-constrained deployments.

On the economics side, the NEB master mix dominated our reagent costs and we had limited leverage on pricing even at higher volumes. This was the key reagent of the test and NEB was a great company overall to work with. The cost model in the archive gives the full picture, and our per-person cost with pooling was competitive for the time. Future effort to bring LAMP-based screening to real scale would need to confront the enzyme cost dependency head-on — whether through alternative sourcing, in-house production, or fundamentally different assay chemistry.
