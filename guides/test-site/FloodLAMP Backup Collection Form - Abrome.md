METADATA
last updated: 2025-12-14 RT
file_name: FloodLAMP Backup Collection Form - Abrome.md
file_date: 2022-08-01
title: FloodLAMP Backup Collection Form - Abrome
category: guides
subcategory: test-site
tags: 
source_file_type: gform
xfile_type: NA
gfile_url: https://docs.google.com/forms/d/14jgRf7MA6dEBkrK8fiPhn5ymCK38ZJqnr9YBAfhIbjc/edit
xfile_github_download_url: NA
pdf_gdrive_url: NA
pdf_github_url: NA
conversion_input_file_type: gform
conversion: ai (chatgpt 5.2 pro)
license: CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
tokens: 597
words: 349
notes:
summary_short: The FloodLAMP Backup Collection Form is a web-based fallback for registering surveillance test samples when the mobile app is unavailable. It ensures sample metadata (tube ID, contributors, sample type) can still be captured and linked to consent, preventing data loss and maintaining chain-of-custody for pooled testing workflows. It was seldom used and introduced due to outages of the FloodLAMP app.


CONTENT

***INTERNAL TITLE:*** FloodLAMP Backup Collection Form - Abrome

## Description
Please use this form to register your collected samples if you do not have the FloodLAMP mobile App or are having problems. By providing a sample you are providing a legal consent for FloodLAMP to perform surveillance testing under the terms listed in [this link](https://drive.google.com/file/d/1we-2GweFKPAfL220x_4GCVqfeSFcozSx/view).

## Form Settings
- Collects respondent email addresses: Yes

## Questions

### Q1. Email
- **Key:** email
- **Prompt:** Email
- **Required:** Yes
- **Widget:** short_answer
- **Answer type / validation:** email (validated)
- **Placeholder:** Valid email

### Q2. Phone Number
- **Key:** phone_number
- **Prompt:** Phone Number (we need to be able to text you in case time sensitive follow up testing is needed)
- **Required:** Yes
- **Widget:** short_answer
- **Answer type / validation:** text (phone number requested; no explicit validation shown)
- **Placeholder:** Short answer text

### Q3. Collection date and time (if different)
- **Key:** collection_date_time
- **Prompt:** Collection date and time if different from when submitting form (leave blank if you are submitting this form shortly after collecting)
- **Required:** No
- **Widget:** short_answer
- **Answer type / validation:** text (date/time requested; no explicit validation shown)
- **Placeholder:** Short answer text

### Q4. Tube ID
- **Key:** tube_id
- **Prompt:** Tube ID (on label next to QR code, for example "FL19823")
- **Required:** Yes
- **Widget:** short_answer
- **Answer type / validation:** text
- **Placeholder:** Short answer text
- **Example:** FL19823

### Q5. Names of people contributing samples to the pool
- **Key:** contributor_names
- **Prompt:** Names of people contributing samples to the pool
- **Required:** Yes
- **Widget:** short_answer
- **Answer type / validation:** text
- **Placeholder:** Short answer text

### Q6. Sample Type
- **Key:** sample_type
- **Prompt:** Sample Type
- **Required:** Yes
- **Widget:** multiple_choice
- **Answer type / validation:** single_select
- **Options:**
  - Nasal swab
  - Throat swab
  - Saliva
  - Other
- **Other option:** Yes — free text

### Q7. Notes
- **Key:** notes
- **Prompt:** Notes
- **Required:** No
- **Widget:** paragraph
- **Answer type / validation:** long_text
- **Placeholder:** Long answer text
