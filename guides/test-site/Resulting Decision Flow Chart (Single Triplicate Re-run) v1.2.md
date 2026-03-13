METADATA
last updated: 2025-12-15 RT updated metadata after BA fixed
file_name: Resulting Decision Flow Chart (Single Triplicate Re-run) v1.2.md
file_date: 2023-06-16
title: Resulting Decision Flow Chart (Single Triplicate Re-run) v1.2
category: guides
subcategory: test-site
tags: 
source_file_type: pdf
xfile_type: NA
gfile_url: NA
xfile_github_download_url: NA
pdf_gdrive_url: https://drive.google.com/file/d/1Yzxo03RifzDk05rTzOVQn3MM4mpcoIEK
pdf_github_url: https://github.com/FocusOnFoundationsNonprofit/floodlamp-archive/blob/main/guides/test-site/Resulting%20Decision%20Flow%20Chart%20(Single%20Triplicate%20Re-run)%20v1.2.pdf
conversion_input_file_type: pdf
conversion: ai (claude sonnet 3.5)
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 241
words: 82
notes: uses mermaid diagram
summary_short: The Resulting Decision (Single Triplicate Re-run) Flow Chart v1.2 defines how to assign final Negative, Positive, or Inconclusive results based on an initial test outcome followed by a single triplicate re-run when needed. It standardizes interpretation thresholds (e.g., 2+ positives or specific mixed patterns) so staff can make consistent resulting calls across runs.


CONTENT

***INTERNAL TITLE:*** Resulting Decision Flow Chart (Single Triplicate Re-run)  v1.2

```mermaid
flowchart LR
    A["Initial Test"]

    A --> B{"Negative"}
    A --> C{"Inconclusive"}
    A --> D{"Positive"}

    %% Negative path
    B --> NEG1(["Negative"])

    %% Inconclusive path
    C --> E["Re-run<br>(triplicate)"]
    E --> F1{"3<br>Negatives"}
    E --> G1{"2+ Positives"}
    E --> H1{"Other"}

    F1 --> NEG2(["Negative"])
    G1 --> POS1(["Positive"])
    H1 --> INC1(["Inconclusive"])

    %% Positive path
    D --> I["Re-run<br>(triplicate)"]
    I --> F2{"3<br>Negatives"}
    I --> K1{"2+ Positives or<br>1/1/1"}
    I --> H2{"Other"}

    F2 --> NEG3(["Negative"])
    K1 --> POS2(["Positive"])
    H2 --> INC2(["Inconclusive"])
    
```
