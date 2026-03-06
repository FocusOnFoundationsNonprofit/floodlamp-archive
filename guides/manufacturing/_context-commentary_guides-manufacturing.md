METADATA
last updated: 2026-02-16 RT
file_name: _context-commentary_guides-manufacturing.md
category: guides
subcategory: manufacturing
words: 1176
tokens: 1669


CONTENT

## Context
The manufacturing subcategory contains the Standard Operating Procedures (SOPs) and process flow diagrams that represented FloodLAMP's most mature approach to producing its two key reagents: the Primer-Guanidine Solution (PGS48) and the 100X Inactivation Solution (100XIS).

PGS48 is the Primer-Guanidine Solution formulated for 48 reactions. It combines LAMP primer sets (As1e, N2, E1) with guanidine hydrochloride and nuclease-free water. The resulting solution is mixed with NEB's colorimetric LAMP master mix to form the reaction mix for the QuickColor LAMP test. The "48" refers to the standardized batch size of 48 reactions, tuned to FloodLAMP's typical customer usage patterns of 20–100+ reactions per session.

100XIS is the 100X Inactivation Solution, a TCEP-based formulation combining TCEP, EDTA, and NaOH. When diluted to 1X Inactivation Saline Solution and added to dry swabs, it extracts and protects the RNA for downstream testing upon heating. Both reagent formulations derive from the Rabe-Cepko protocol.

The subcategory includes five files:

- **Assay and Reagent Manufacturing Diagrams** — A 19-slide presentation containing process flow diagrams for all key reagent manufacturing and assay workflows, covering PGS batching, 100XIS manufacturing, primer preparation, positive control aliquoting, and assay setup at various reaction scales (24, 48, and 96 reactions).
- **SOP-201-A_2: PGS48 Manufacturing Run Form** — Step-by-step manufacturing procedure for PGS48, including primer resuspension, guanidine-HCl mixing, and robotic aliquoting on an OpenTrons liquid handler.
- **SOP-202-A_1: 100XIS Manufacturing Run Form** — Manufacturing procedure for 100XIS, covering TCEP weighing, component mixing in a 1L glass bottle, and aliquoting into 5 mL vials for storage at -20°C.
- **SOP-301: PGS48 Verification Run Form** — Quality verification procedure for PGS48 batches via CLAMP amplification with positive and negative controls, including a plate layout map for tracking results by lot number.
- **SOP-302: 100XIS Verification Run Form** — Quality verification procedure for 100XIS batches via CLAMP amplification.

The term "manufacturing" is used loosely here. FloodLAMP's production was small-scale pilot manufacturing — a small team working in a shared lab space at MBC BioLabs in San Carlos, California, without the infrastructure or experience typical of industrial reagent manufacturing. The team included a PhD scientist who developed the initial batch records and then these SOPs, which represented the most controlled and streamlined versions of the processes FloodLAMP achieved.

These SOPs were preceded by a less formal system of batch records. The transition to SOPs was substantially but not fully complete by early 2022 (January–February), with the PGS48 and 100XIS procedures being the primary ones formalized. The PGS48 manufacturing process used an OpenTrons liquid handling robot for aliquoting, along with custom 3D-printed tube holders.

Over its operating period, FloodLAMP produced approximately 100,000 reactions worth of PGS and 150,000–200,000 samples worth of 100X Inactivation Solution. The PGS48 process yielded 3,264 reactions per lot (68 tubes at 550 µL each) and could produce roughly 10,000 reactions per hour once setup was complete, though setup time was significant. The 100XIS was produced in much larger lots — approximately 108,000 reactions per lot (216 five-mL tubes), achievable in a few hours with setup time dominating the run.

No formal stability study was conducted on PGS, as it was stored frozen and used same-day to make the reaction mix. The more pressing stability issue was the reaction mix itself: when sites stored pre-made reaction mix, the deep pink color of the colorimetric LAMP reaction would sometimes fade or turn orange. FloodLAMP provided clear instructions to avoid storing pre-made reaction mix when possible, and to verify the deep pink color before use. A cursory stability study was performed on the 1X Inactivation Saline Solution (1XISS) using PCR as the endpoint, measuring over a period of two weeks. No significant loss of signal was observed, so two weeks was specified as the usage window for 1XISS.

These documents connect to other parts of the archive: the reagents produced here were shipped to FloodLAMP's pilot program customers (documented in the Pilots collection), and the testing protocols that use these reagents are covered in other Guides subcategories.


## Commentary
These SOPs and the reagent formulations they document were among the most important operational achievements at FloodLAMP. They represented a significant step in simplifying and standardizing the reagent production process. The Primer-Guanidine Solution, in particular, was a meaningful improvement — premixing the primers with guanidine hydrochloride eliminated a step for the end user, and we confirmed through testing that this premixing did not cause degradation. We also put considerable thought into the volumes and tube sizes to minimize waste while providing enough reagent for a typical testing session of 20 to several hundred reactions.

The OpenTrons robot was used for PGS48 aliquoting, and we had custom 3D-printed tube holders to support the workflow. In hindsight, the robotic aliquoting was overkill for the volumes we actually produced. We over-indexed on process improvements at a time when the bottleneck was elsewhere — we couldn't scale the rest of our operations (ordering, logistics, customer support) to match the demand during the Omicron surge in late 2021 and early 2022. We had on the order of half a million reactions worth of primers on hand. The process control was a step in the right direction, but the investment in automation wasn't justified by our actual throughput.

That said, the formulation work itself — consolidating into PGS, tuning the volumes, and standardizing at 48 reactions — was genuinely valuable. That's the endpoint worth preserving from what we did here.

The broader lesson for the field is about the reagent supply chain. Small organizations like FloodLAMP should not be manufacturing their own reagents if there's any way to avoid it. What's needed is for reagent manufacturers — the actual producers like New England Biolabs, not the white-label diagnostic companies — to produce low-cost, high-volume reagent kits for the most widely used open protocols. This has to go hand in hand with establishing open EUA protocols and rights of reference so that multiple parties can legally use and distribute these reagents to run validated, consensus testing protocols.


The bottleneck during the Omicron surge was not reagent manufacturing itself but the overall kit and supplies preparation, shipment, tracking, and coordination. The system involved over 100 parts, many requiring qualification and preparation. Preparing, delivering, and supporting the complete testing systems was a large burden for a small team. The process didn't fully mature until FloodLAMP's last pilot (Abrome) mid 2022, where a cart-and-drawers system worked well. Beyond the physical logistics, the digital side — apps, data tracking, troubleshooting — was a constant challenge with significant downtime and outages.

The model to follow is SalivaDirect, which contracted with Eurofins to produce commercially available SalivaDirect kits, which were available for general order and not restricted to clinical labs designated under Saliva Direct's open EUA. When we ordered those kits, they arrived next day, were well formulated, and a relatively inexperienced lab tech was able to run the protocol successfully on a PCR machine. That combination — simplified protocol, commercially manufactured reagents, fast shipping — is what decentralized testing needs. Having individual labs or small companies mix their own reagents is a dead end for scale.
