# ===== START OF FILE primary/floodlamp_pilot_context.py =====
# Functions for extracting pilot data stats and populating context-commentary files.

import os
import re

PILOT_DATA_DIR = "data/floodlamp/pilots/pilot-data"

SITE_CODES = ["ABRM", "BEND", "COMB", "COSP", "CRLN", "DAVI", "FLMP", "FLSP", "FTFC", "KENT", "NDHM", "ROSA"]

FIELDS_TO_EXTRACT = [
    ("Dates", "Start Run Date"),
    ("Dates", "End Run Date"),
    ("Overall", "Number of Tubes Tested (initial only - no re-runs)"),
    ("Overall", "Number of Participant Results"),
    ("Positives", "Number of Tubes with Final Result Positive"),
    ("People", "Number of Unique Individuals Tested"),
    ("Info", "Test Operator"),
    ("Info", "Test Processing Site"),
    ("Info", "Population Tested"),
    ("Info", "Configuration"),
    ("Info", "Collection Type"),
    ("Info", "Self or HCW Collected"),
    ("Info", "App Used?"),
    ("Info", "Bring-up Type"),
    ("Info", "Program Name"),
    ("Info", "Site"),
    ("Info", "Site Type"),
    ("Info", "Location"),
]

### Helpers
def _parse_stats_table(md_text):
    """
    Parse the stats key-values markdown table from a pilot data summary file.

    :param md_text: str, full text of the summary markdown file.
    :return stats: dict, mapping (section, metric) tuples to value strings.
    """
    stats = {}
    lines = md_text.split('\n')
    in_stats = False
    past_separator = False
    for line in lines:
        stripped = line.strip()
        if '### Stats key-values' in stripped:
            in_stats = True
            past_separator = False
            continue
        if in_stats and stripped.startswith('###'):
            break
        if not in_stats:
            continue
        if not stripped.startswith('|'):
            continue
        if '---' in stripped:
            past_separator = True
            continue
        if not past_separator:
            continue
        cells = [c.strip() for c in stripped.split('|')]
        # pipe split gives empty strings at positions 0 and last
        if len(cells) >= 4:
            section = cells[1]
            metric = cells[2]
            value = cells[3]
            stats[(section, metric)] = value
    return stats
def _format_comma_number(value_str):
    """
    Ensure an integer value string has comma separators at thousands places.

    :param value_str: str, the raw value string from the table.
    :return formatted: str, value with commas if it is an integer >= 1000.
    """
    cleaned = value_str.replace(',', '')
    if cleaned.isdigit():
        return f"{int(cleaned):,}"
    return value_str
def _build_site_block(stats):
    """
    Build the text block for a site from its parsed stats dictionary.

    :param stats: dict, mapping (section, metric) to value string.
    :return block: str, formatted multi-line text block (no leading/trailing blank lines).
    """
    comma_fields = {
        "Number of Tubes Tested (initial only - no re-runs)",
        "Number of Participant Results",
    }
    lines = []
    for section, metric in FIELDS_TO_EXTRACT:
        value = stats.get((section, metric), "")
        if not value:
            continue
        if metric in comma_fields:
            value = _format_comma_number(value)
        lines.append(f"{metric}: {value}")
    return '\n'.join(lines)

### Main function
def populate_context_commentary(pilot_data_dir=PILOT_DATA_DIR):
    """
    Read pilot data summaries and populate the context-commentary file with extracted stats.

    :param pilot_data_dir: str, path to the pilot-data directory.
    :return None: writes the updated context-commentary file in place.
    """
    context_file = os.path.join(pilot_data_dir, "_context-commentary_pilots-pilot-data_INITIAL.md")
    with open(context_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Build stats for each site
    site_blocks = {}
    for code in SITE_CODES:
        summary_path = os.path.join(pilot_data_dir, f"{code}_pilot-data", f"{code}_pilot-data_summary.md")
        if not os.path.exists(summary_path):
            print(f"WARNING: summary not found for {code}: {summary_path}")
            continue
        with open(summary_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        stats = _parse_stats_table(md_text)
        block = _build_site_block(stats)
        if block:
            site_blocks[code] = block
            print(f"  {code}: extracted {len(block.splitlines())} fields")
        else:
            print(f"  {code}: no fields extracted")
    # Build stats for aggregate
    agg_summary_path = os.path.join(pilot_data_dir, "aggregate_pilot-data", "aggregate_pilot-data_summary.md")
    if os.path.exists(agg_summary_path):
        with open(agg_summary_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        stats = _parse_stats_table(md_text)
        block = _build_site_block(stats)
        if block:
            site_blocks["AGGREGATE"] = block
            print(f"  AGGREGATE: extracted {len(block.splitlines())} fields")
    # Now update the context file - only in the "Generic Context Answers - Raw Transcript" section
    lines = content.split('\n')
    context_start = None
    context_end = None
    for i, line in enumerate(lines):
        if '### Generic Context Answers - Raw Transcript' in line:
            context_start = i
        if context_start is not None and i > context_start and line.startswith('### '):
            context_end = i
            break
    if context_start is None or context_end is None:
        print("ERROR: could not find Context Answers section boundaries")
        return
    # Find all h4 headings within the context section and their positions
    headings = []
    for i in range(context_start, context_end):
        if lines[i].startswith('#### '):
            headings.append(i)
    # Build new content for the context section
    new_section_lines = lines[context_start:headings[0]] if headings else lines[context_start:context_end]
    for idx, heading_line_num in enumerate(headings):
        heading_text = lines[heading_line_num]
        new_section_lines.append(heading_text)
        # Determine which site this heading belongs to
        block_text = None
        if 'Aggregate' in heading_text:
            block_text = site_blocks.get("AGGREGATE")
        else:
            for code in SITE_CODES:
                if heading_text.startswith(f'#### {code}'):
                    block_text = site_blocks.get(code)
                    break
        if block_text:
            new_section_lines.append('')
            new_section_lines.extend(block_text.split('\n'))
        new_section_lines.append('')
    # Reconstruct the full file
    result_lines = lines[:context_start] + new_section_lines + ['\n'] + lines[context_end:]
    result = '\n'.join(result_lines)
    # Clean up any triple+ blank lines to double
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    with open(context_file, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"\nUpdated: {context_file}")

### MRUN
def mrun_populate_pilot_context():
    pass
#if __name__ == "__main__":
    populate_context_commentary(PILOT_DATA_DIR)

# ===== END OF FILE primary/floodlamp_pilot_context.py =====
