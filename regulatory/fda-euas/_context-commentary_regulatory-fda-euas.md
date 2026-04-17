METADATA
last updated: 2026-03-18 RT
file_name: _context-commentary_regulatory-fda-euas.md
category: regulatory
subcategory: fda-euas
gfile_url: https://docs.google.com/document/d/18JeeeAMKd7JS1pZ8bdDG6vxEt8cr9iaNOMZbTMtlsUU
words: 627
tokens: 1184


CONTENT

## Context
An Emergency Use Authorization (EUA) is a mechanism through which the FDA can authorize the use of unapproved medical products (or unapproved uses of approved products) during a declared public health emergency. During the COVID-19 pandemic, EUAs were the primary pathway by which diagnostic tests reached the market. The EUA process differs from the standard FDA authorization pathways (510(k), PMA, De Novo) in several key respects:

- **Speed**: EUAs are designed for rapid review during emergencies, with intended timelines measured in weeks rather than months or years
- **Evidence threshold**: EUAs require the FDA to determine that the product "may be effective" based on available evidence, a lower bar than the "reasonable assurance of safety and effectiveness" required for standard authorizations
- **Temporary status**: EUAs are valid only for the duration of the declared emergency and can be revised or revoked
- **Conditions of authorization**: EUA-holders must meet ongoing conditions, including labeling requirements, adverse event reporting, and sometimes performance monitoring

Each EUA includes an Instructions for Use (IFU) document that specifies the authorized specimen types, testing procedures, performance characteristics, interpretation criteria, and conditions of authorization. Some EUAs also include an EUA Summary providing the FDA's review of the submission data.

This `regulatory/fda-euas` subcategory contains a selection of EUA documents that were relevant to FloodLAMP's work — not a comprehensive collection of COVID-19 diagnostic EUAs (of which there were hundreds). The files here were included because FloodLAMP reviewed them during development, because they represent comparable technologies (particularly LAMP-based or isothermal assays), or because they illustrate specific aspects of the EUA landscape. The collection includes IFUs and EUA summaries from tests spanning RT-PCR, isothermal amplification, CRISPR-based detection, and home collection kits.

Two files merit specific mention:

- **`DetectaChem - EUA IFU - MobileDetect-BIO BCC19 Test Kit (10-6-2020)`** — This was the EUA most similar to what FloodLAMP was developing: a colorimetric LAMP-based SARS-CoV-2 test designed for point-of-care use. FloodLAMP's assays appeared to achieve significantly higher sensitivity and overall performance than the DetectaChem test based on the published performance data.
- **`2020-10-15_SalivaDirect EUA IFU - Yale School of Public Health SalivaDirect assay EUA Summary`** (available in the `regulatory/open-euas` subcategory) — Notable as the first and essentially only "open" EUA, meaning the protocol was made freely available for other labs to adopt.

- **`2020-12-01_CDC EUA IFU - CDC 2019-Novel Coronavirus (2019-nCoV) Real-Time RT-PCR Diagnostic Panel`** - The CDC's own RT-PCR Diagnostic Panel IFU is also included here. It was the original FDA-authorized COVID-19 test in the United States and provides a baseline example of an EUA IFU at the highest complexity level.

The current FDA page for SARS-CoV-2 molecular diagnostic EUAs is [FDA: In Vitro Diagnostics EUAs – Molecular Diagnostic Tests for SARS-CoV-2](https://www.fda.gov/medical-devices/covid-19-emergency-use-authorizations-medical-devices/in-vitro-diagnostics-euas-molecular-diagnostic-tests-sars-cov-2).
For historical reconstruction of how FDA EUA listings changed over time during the pandemic, useful resources may be:
- 2020 onward: [Wayback Machine archive of the FDA’s earlier IVD EUA page used during the pandemic](https://web.archive.org/web/*/https://www.fda.gov/medical-devices/emergency-situations-medical-devices/emergency-use-authorizations#covid19ivd)
- 2021-3-19 onward: [Wayback Machine archive of the FDA’s later IVD EUA page used during the pandemic](https://web.archive.org/web/*/https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/in-vitro-diagnostics-euas).
An independent COVID-19 EUA repository is the [Center for Complex Interventions - Structured SARS-2 diagnostic data repository (centerofci-archive)](https://github.com/centerofci-archive/SARS-CoV-2-testing-kit-validation-data).

For broader dashboards searchable by regulatory status, see [ASU Testing Commons](https://chs.asu.edu/diagnostics-commons/testing-commons) and [PATH COVID-19 Diagnostics Dashboard](https://www.path.org/who-we-are/programs/diagnostics/covid-dashboard-covid-19-diagnostics-dashboard/).

For broader analysis and commentary on the FDA's EUA process during the pandemic, see the `regulatory/reg-articles-misc` subcategory, which includes articles and reports examining how the process functioned. For FloodLAMP's own FDA submissions and correspondence, see the `regulatory/fl-fda-submissions` and `regulatory/fl-fda-correspondence` subcategories.

Also see the following file, which is an AI-generated report sourcing retrospectives on FDA EUAs during the COVID-19 pandemic.
`regulatory/reg-articles-misc/_AI_fda-eua-covid-retrospectives_post2022_report.md`


## Commentary
See other `regulatory` subcategories for commentary. FloodLAMP's assessments and lessons learned regarding the EUA process are addressed there where they can be grounded in specific documents and experiences.
