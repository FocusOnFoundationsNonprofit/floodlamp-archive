import os
from collections import Counter
from primary.llm import *
from primary.fileops import *
from primary.aws import *

OPENAI_MODEL = "gpt-5.4"

### PROMPTS AND TOOLS
REFUSAL_CATEGORY_NAMES = {
    "A": "Boilerplate Opening Disclaimer",
    "B": "Third-Party Confidentiality Protection",
    "C1": "Declined Specifics / Provided Useful General Guidance",
    "C2": "Partial Answer with Redirect",
    "D1": "Timeline/Status Deflection with Redirect",
    "D2": "Timeline/Status Deflection (No Substantive Response)",
    "E": "Deflection to Email (No Substantive Answer)",
    "E2": "Policy/Process Refusal",
    "F1": "Blanket Pre-Filter with Email Redirect",
    "F2": "Blanket Pre-Filter (No Redirect)",
    "UNRESOLVED": "Classification missing"
}
REFUSAL_STRONG_CUE_SUBSTRINGS = [
    "confidential",
    "specific submission",
    "specific submissions",
    "specific company",
    "specific companies",
    "under review",
    "cannot comment",
    "can't comment",
    "can not comment",
    "cannot share",
    "can't share",
    "not able to provide",
    "not able to share",
    "not able to respond",
    "not able to comment",
    "publicly shared",
    "publicly talk about",
    "publicly talk",
    "publicly discuss",
    "public action",
    "reached the limit of what i know i can publicly talk about",
    "don't know what can be publicly shared",
    "do not speak specifically about",
    "we just can't share any of those details",
    "we can't comment about any specific companies",
    "we are not able to provide any information",
    "look internally",
    "internally at the agency",
    "talk with you further",
    "talking offline may be helpful",
    "we can't really get into that on this call",
    "i can't speak to what will be in the template",
    "we're not publishing that right now",
    "i can't answer that over the phone",
    "i'm not able to answer any questions about a specific test",
    "there's a lot of listeners on this call",
    "good bit of transparency that goes on because there's a lot of listeners on this call",
    "stay tuned"
]

PROMPT_REFUSAL_EXTRACTION = """
You are an expert analyst of FDA COVID-19 Diagnostic Virtual Town Hall transcripts.

You will be given the full text of one transcript file. The file is a markdown transcript with line breaks preserved.
Your job is to identify every instance where an FDA speaker refuses, declines, deflects, or pre-filters a question or topic.

Important:
- Return LINE NUMBERS, not quoted text.
- Use 1-based line numbers relative to the exact input text you receive.
- FDA refusal instances should be anchored to an FDA speaker turn. In these transcripts, FDA speakers usually have `FDA` in the speaker label.
- Prioritize explicit refusal behavior by FDA speakers, such as:
  - confidentiality / cannot comment on specific companies or submissions
  - cannot say what can be publicly shared
  - redirect to templates email, reviewer, pre-EUA, pre-submission, or offline follow-up
  - refusal to discuss timeline, status, or case-specific details on the call
  - phrases like "we can't really get into that on this call", "I can't speak to what will be in the template", "we're not publishing that right now", "I can't answer that over the phone", "submit a pre-EUA and we can work with you", or "I'm not able to answer any questions about a specific test"
- Mere process guidance is NOT a refusal. If FDA substantively answers the question and simply says "contact the EUA mailbox" or "work with your lead reviewer" to handle paperwork or follow-up details, do not mark it as a refusal.
- For an active refusal, the FDA response should contain some limiting move such as declining, withholding, redirecting away from the core answer, or explicitly moving the matter off-call.
- Return ranges broad enough to capture the key exchange:
  - usually the caller's question plus the full FDA refusal/deflection response
  - include immediate follow-up lines if needed so the excerpt contains a complete mini exchange
  - do not return only a handoff line, only a speaker label, or only a truncated fragment of the answer
  - for Q&A refusals, start at the relevant question and end after the refusal answer is complete
  - or the moderator/FDA boilerplate disclaimer itself
- Keep each range within a single topical section when the transcript uses markdown headings such as `#### ...`.
- If a new section heading appears, do not let the range spill across it.
- If a moderator handoff appears immediately before a new section heading, prefer the actual question/refusal exchange after the heading.
- Do NOT invent line numbers.
- Do NOT return duplicate or heavily overlapping instances unless they are clearly separate refusals.
- Do NOT mark a passage when FDA simply gives a substantive public answer without actually declining, limiting, or redirecting.
- Do NOT mark passages where the caller says FDA would not answer, but no FDA refusal line appears in the extracted passage.

Include these types:
1. Boilerplate opening disclaimer:
   the standard statement that FDA cannot respond to questions about specific submissions under review.
2. Active refusals during Q&A:
   - declines using "specific submissions" or confidentiality language
   - redirects to templates mailbox, reviewer, pre-EUA, pre-submission, or offline follow-up
   - says question is too detailed, case-specific, or cannot be answered on the call
   - declines timeline/status or specific regulatory decision questions
   - declines to provide template contents, unpublished criteria, or case-specific test guidance on the call
   - pre-filters emailed questions as too detailed or case-specific

For each instance:
- start_line: first relevant line
- end_line: last relevant line
- is_boilerplate: true only for the standard opening disclaimer
- refusal_type: short normalized tag
- brief_description: one sentence summary
- confidence: high, medium, or low

Prefer precision over recall when uncertain. If uncertain, still include the instance but mark confidence as low.
"""
TOOLS_REFUSAL_EXTRACTION = [{
    "type": "function",
    "function": {
        "name": "extract_refusal_instances",
        "description": "Identify FDA refusal or deflection instances in a transcript and return 1-based line number ranges.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "refusal_instances": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "start_line": {
                                "type": "integer",
                                "description": "1-based first line of the refusal passage."
                            },
                            "end_line": {
                                "type": "integer",
                                "description": "1-based last line of the refusal passage."
                            },
                            "is_boilerplate": {
                                "type": "boolean",
                                "description": "True only for the standard opening disclaimer."
                            },
                            "refusal_type": {
                                "type": "string",
                                "description": "Short normalized tag such as boilerplate, email_redirect, timeline_deflection, policy_refusal, prefilter, confidentiality."
                            },
                            "brief_description": {
                                "type": "string",
                                "description": "One-sentence description of what was refused or deflected."
                            },
                            "confidence": {
                                "type": "string",
                                "enum": ["high", "medium", "low"],
                                "description": "Confidence in the extraction."
                            }
                        },
                        "required": [
                            "start_line",
                            "end_line",
                            "is_boilerplate",
                            "refusal_type",
                            "brief_description",
                            "confidence"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            "required": ["refusal_instances"],
            "additionalProperties": False
        }
    }
}]
PROMPT_REFUSAL_CLASSIFICATION = """
You are an expert in FDA regulatory policy, diagnostics EUA process, and transparency/accountability analysis.

You will be given one extracted refusal passage from an FDA COVID-19 Diagnostic Virtual Town Hall transcript, along with file and line metadata.

First decide whether the passage contains a real active refusal by FDA.
- A real active refusal means FDA limits, declines, avoids, or redirects away from answering the core question.
- Mere process guidance is NOT an active refusal. If FDA gives a substantive answer and only mentions the EUA mailbox, templates email, or lead reviewer as a normal implementation path, set `is_active_refusal` to false.
- Category A is only for the standard opening boilerplate disclaimer, not for ordinary Q&A passages.
- Classify the REFUSED CORE QUESTION, not every topic mentioned in the passage.

Classify the refusal using this rubric:

A: Boilerplate Opening Disclaimer — Standard moderator script read at session opening. Score 0.
B: Third-Party Confidentiality Protection — Someone is asking for nonpublic details, review status, or submission-specific information about another company's test or submission. Score 5.
C1: Declined Specifics / Provided Useful General Guidance — Specifics declined, but useful general guidance provided. Score 4.
C2: Partial Answer with Redirect — Some general guidance, but redirected for substantive specifics. Score 3.
D1: Timeline/Status Deflection with Redirect — Status/timeline declined but contact channel offered. Score 3.
D2: Timeline/Status Deflection (No Substantive Response) — Status/timeline declined without useful guidance. Score 2.
E: Deflection to Email (No Substantive Answer) — No meaningful guidance on-call, redirected offline. Score 2.
E2: Policy/Process Refusal — Generalizable policy/process question declined using specific-submission logic. Score 2.
F1: Blanket Pre-Filter with Email Redirect — Emailed question deemed too detailed or case-specific; written or offline response offered. Score 3.
F2: Blanket Pre-Filter (No Redirect) — Emailed question declined as too detailed, no meaningful alternative. Score 2.

Scoring:
5 = Fully Legitimate
4 = Largely Legitimate
3 = Mixed
2 = Questionable
1 = Not Legitimate
0 = Not scored (Category A only)

Important decision rules:
- Distinguish questions about the caller's own submission vs another company's submission.
- Use Category B narrowly. It applies only when the refused core question is about another company's nonpublic submission, review status, or test-specific regulatory details.
- Do NOT use Category B merely because a named company is mentioned.
- If the real question is about FDA policy, market conduct, contracting behavior, fairness, or other generalizable process issues, do not use Category B even if a company name appears in the passage.
- If FDA declines to address a named company's behavior but the caller's real concern is a broader policy or process question, prefer E2, C2, or E depending on how much public guidance FDA gave.
- If FDA could reasonably have generalized the answer publicly, that weighs toward lower legitimacy.
- If FDA provided useful substantive guidance alongside the refusal, that weighs upward.
- Classify the actual refusal behavior in context, not merely the topic of the question.
- Base the classification on the passage itself, not on assumptions about missing surrounding text.
- Do not leave any field blank. If a speaker is not identifiable, return `Unknown`.
- If multiple FDA speakers jointly make the refusal, name both.
- If the passage is not actually an active refusal, set `is_active_refusal` to false and explain that clearly in the rationale. It will be filtered downstream.

Use this precedence order:
1. If not a real active refusal, set `is_active_refusal` to false.
2. If it is the standard opening disclaimer, use A.
3. If the refused core question is about another company's nonpublic submission, review status, authorization timing, or company-specific regulatory details, use B.
4. If FDA is pre-screening or refusing an emailed / previously submitted question as too detailed or case-specific, use F1 or F2.
5. If the refused core question is mainly about timeline or status and is NOT already a B case, use D1 or D2.
6. If the refused core question is a generalizable policy/process/fairness issue and FDA declines to answer it publicly, use E2.
7. If FDA gave substantial generalized guidance before redirecting, use C1.
8. If FDA gave some but not much generalized guidance before redirecting, use C2.
9. If FDA gave no meaningful on-call guidance and moved the matter offline, use E.

Category boundary examples:
- Another company's test approval timing or review status -> B, not D1.
- A named company is mentioned, but the real question is whether FDA allows a broader contracting or fairness practice -> E2, not B.
- A live caller is told to email about a specific case, with no substantive answer -> E, not F1.
- An emailed or pre-submitted question is declined as too detailed, but FDA promises written follow-up -> F1.
- FDA says "I can't say more right now" but still gives actionable generalized guidance that materially answers the underlying issue -> C1, not E2.
- FDA gives only limited generalized context before pushing the real answer offline -> C2, not C1.

Return one best classification only.
"""

TOOLS_REFUSAL_CLASSIFICATION = [{
    "type": "function",
    "function": {
        "name": "classify_refusal",
        "description": "Classify one extracted FDA refusal passage using the legitimacy rubric.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "category_code": {
                    "type": "string",
                    "enum": ["A", "B", "C1", "C2", "D1", "D2", "E", "E2", "F1", "F2"]
                },
                "is_active_refusal": {
                    "type": "boolean",
                    "description": "True only if the passage contains a real active refusal by FDA. False for boilerplate or ordinary substantive guidance that is not actually a refusal."
                },
                "category_name": {
                    "type": "string"
                },
                "legitimacy_score": {
                    "type": "integer",
                    "description": "0 for A; otherwise 1-5."
                },
                "rationale": {
                    "type": "string",
                    "description": "2-4 sentences explaining the classification."
                },
                "key_excerpt": {
                    "type": "string",
                    "description": "Short representative excerpt under 40 words."
                },
                "speaker_refusing": {
                    "type": "string",
                    "description": "Name or role of the FDA speaker making the refusal, if identifiable."
                },
                "speaker_asking": {
                    "type": "string",
                    "description": "Name or role of the questioner, or Moderator / Multiple / Unknown."
                },
                "could_have_generalized": {
                    "type": "boolean"
                },
                "asks_about_third_party_submission": {
                    "type": "boolean"
                }
            },
            "required": [
                "category_code",
                "is_active_refusal",
                "category_name",
                "legitimacy_score",
                "rationale",
                "key_excerpt",
                "speaker_refusing",
                "speaker_asking",
                "could_have_generalized",
                "asks_about_third_party_submission"
            ],
            "additionalProperties": False
        }
    }
}]

### TRANSCRIPT PARSING
def slice_lines(lines, start_line, end_line):
    if start_line < 1 or end_line < start_line:
        raise ValueError(f"Invalid line range: {start_line}-{end_line}")
    if end_line > len(lines):
        raise ValueError(f"Line range exceeds file length: {start_line}-{end_line} > {len(lines)}")
    return "\n".join(lines[start_line - 1:end_line])
def find_nearest_section_heading(lines, start_line):
    """
    Find the nearest preceding markdown heading line, useful for audit context
    in section-titles files.
    """
    for i in range(start_line - 1, -1, -1):
        line = lines[i].strip()
        if line.startswith("#"):
            return {
                "section_heading_line": i + 1,
                "section_heading_text": line
            }
    return {
        "section_heading_line": None,
        "section_heading_text": None
    }
def find_first_topical_section_heading(lines, start_line=1):
    for i in range(max(1, start_line) - 1, len(lines)):
        line = lines[i].strip()
        if line.startswith("#### "):
            return {
                "section_heading_line": i + 1,
                "section_heading_text": line
            }
    return {
        "section_heading_line": None,
        "section_heading_text": None
    }
def is_first_topical_section_heading(section_heading_text):
    if not section_heading_text:
        return False
    return str(section_heading_text).strip().startswith("#### 1.")
def extract_speaker_label(line):
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    if stripped.endswith(":") and len(stripped) <= 120:
        return stripped[:-1].strip()
    return None
def is_fda_speaker_name(speaker_name):
    if not speaker_name:
        return False
    lowered = speaker_name.lower()
    if "fda" in lowered:
        return True
    if "ivd director" in lowered or "assoc director" in lowered:
        return True
    if "cdrh" in lowered and ("director" in lowered or "associate" in lowered):
        return True
    return False
def is_moderator_speaker_name(speaker_name):
    if not speaker_name:
        return False
    lowered = speaker_name.lower()
    return lowered.startswith("coordinator") or "moderator" in lowered
def find_section_bounds(lines, line_number):
    heading_line = None
    for i in range(line_number - 1, -1, -1):
        if lines[i].strip().startswith("#"):
            heading_line = i + 1
            break
    next_heading_line = None
    search_start = heading_line if heading_line else line_number
    for i in range(search_start, len(lines)):
        if lines[i].strip().startswith("#"):
            next_heading_line = i + 1
            break
    section_start = (heading_line + 1) if heading_line else 1
    while section_start <= len(lines) and not lines[section_start - 1].strip():
        section_start += 1
    section_end = (next_heading_line - 1) if next_heading_line else len(lines)
    while section_end >= section_start and not lines[section_end - 1].strip():
        section_end -= 1
    return section_start, section_end
def collect_speaker_turns(lines, start_line, end_line):
    turns = []
    cur_line = start_line
    while cur_line <= end_line:
        speaker = extract_speaker_label(lines[cur_line - 1])
        if not speaker:
            cur_line += 1
            continue
        next_line = cur_line + 1
        while next_line <= end_line and not extract_speaker_label(lines[next_line - 1]):
            next_line += 1
        turn_end = next_line - 1
        while turn_end >= cur_line and not lines[turn_end - 1].strip():
            turn_end -= 1
        text_lines = lines[cur_line:turn_end] if turn_end > cur_line else []
        text = "\n".join(text_lines).strip()
        turns.append({
            "speaker": speaker,
            "start_line": cur_line,
            "end_line": max(cur_line, turn_end),
            "text": text,
            "is_fda": is_fda_speaker_name(speaker),
            "is_moderator": is_moderator_speaker_name(speaker)
        })
        cur_line = next_line
    return turns
def is_transition_line(line):
    stripped = line.strip()
    lowered = stripped.lower()
    if not stripped:
        return True
    if stripped.startswith("#"):
        return True
    if lowered.startswith("our next question"):
        return True
    if lowered.startswith("next question"):
        return True
    if lowered.startswith("coordinator (fda):") or lowered.startswith("coordinator:"):
        return True
    if lowered.startswith("moderator:"):
        return True
    return False
def normalize_instance_range(lines, start_line, end_line):
    heading_lines = [i + 1 for i in range(start_line - 1, end_line) if lines[i].strip().startswith("#")]
    if heading_lines:
        first_heading_line = heading_lines[0]
        leading_segment = lines[start_line - 1:first_heading_line - 1]
        if first_heading_line == start_line or (first_heading_line - start_line <= 6 and all(is_transition_line(line) for line in leading_segment)):
            next_line = first_heading_line + 1
            while next_line <= len(lines):
                if lines[next_line - 1].strip() and not lines[next_line - 1].strip().startswith("#"):
                    start_line = next_line
                    break
                next_line += 1
        for heading_line in heading_lines:
            if heading_line > start_line:
                end_line = min(end_line, heading_line - 1)
                break
    while end_line >= start_line and not lines[end_line - 1].strip():
        end_line -= 1
    if end_line < start_line:
        end_line = start_line
    return start_line, end_line
def expand_refusal_exchange(lines, start_line, end_line):
    section_start, section_end = find_section_bounds(lines, start_line)
    turns = collect_speaker_turns(lines, section_start, section_end)
    if not turns:
        return None
    anchor_indices = []
    for idx, turn in enumerate(turns):
        overlaps_initial_range = not (turn["end_line"] < start_line or turn["start_line"] > end_line)
        near_initial_range = turn["start_line"] <= end_line + 12 and turn["end_line"] >= start_line - 12
        if turn["is_fda"] and not turn["is_moderator"] and any(cue in turn["text"].lower() for cue in REFUSAL_STRONG_CUE_SUBSTRINGS) and (overlaps_initial_range or near_initial_range):
            anchor_indices.append(idx)
    if not anchor_indices:
        return None
    first_anchor = anchor_indices[0]
    last_anchor = anchor_indices[-1]
    asking_speaker = None
    for idx in range(first_anchor - 1, -1, -1):
        turn = turns[idx]
        if turn["is_moderator"]:
            break
        if not turn["is_fda"]:
            asking_speaker = turn["speaker"]
            break
    start_idx = first_anchor
    while start_idx > 0:
        prev_turn = turns[start_idx - 1]
        if prev_turn["is_moderator"]:
            break
        if asking_speaker:
            if prev_turn["speaker"] == asking_speaker or prev_turn["is_fda"]:
                start_idx -= 1
                continue
            break
        if prev_turn["is_fda"]:
            start_idx -= 1
            continue
        break
    end_idx = last_anchor
    while end_idx + 1 < len(turns):
        next_turn = turns[end_idx + 1]
        if next_turn["is_moderator"]:
            break
        if asking_speaker:
            if next_turn["speaker"] == asking_speaker or next_turn["is_fda"]:
                end_idx += 1
                continue
            break
        if next_turn["is_fda"]:
            end_idx += 1
            continue
        break
    expanded_start = turns[start_idx]["start_line"]
    expanded_end = turns[end_idx]["end_line"]
    while expanded_end >= expanded_start and not lines[expanded_end - 1].strip():
        expanded_end -= 1
    return expanded_start, expanded_end

### EXTRACTION NORMALIZATION
def infer_refusal_type_from_text(text):
    lowered = text.lower()
    if "confidential" in lowered or "specific submission" in lowered or "specific company" in lowered:
        return "confidentiality"
    if "under review" in lowered:
        return "under_review"
    if "look internally" in lowered or "internally at the agency" in lowered:
        return "internal_redirect"
    if "offline" in lowered or "talk with you further" in lowered:
        return "offline_redirect"
    if "publicly" in lowered:
        return "public_limit"
    return "refusal"
def build_heuristic_refusal_instances(lines):
    turns = collect_speaker_turns(lines, 1, len(lines))
    instances = []
    seen_ranges = set()
    for turn in turns:
        if not turn["is_fda"] or turn["is_moderator"]:
            continue
        if not any(cue in turn["text"].lower() for cue in REFUSAL_STRONG_CUE_SUBSTRINGS):
            continue
        expanded_range = expand_refusal_exchange(lines, turn["start_line"], turn["end_line"])
        if not expanded_range:
            continue
        if expanded_range in seen_ranges:
            continue
        seen_ranges.add(expanded_range)
        instances.append({
            "start_line": expanded_range[0],
            "end_line": expanded_range[1],
            "is_boilerplate": False,
            "refusal_type": infer_refusal_type_from_text(turn["text"]),
            "brief_description": "Heuristic refusal candidate anchored to explicit FDA limiting language.",
            "confidence": "medium"
        })
    return instances
def infer_speakers_from_passage(passage):
    speaker_labels = []
    for raw_line in passage.splitlines():
        speaker = extract_speaker_label(raw_line)
        if speaker:
            speaker_labels.append(speaker)
    unique_labels = list(dict.fromkeys(speaker_labels))
    fda_labels = [
        label for label in unique_labels
        if is_fda_speaker_name(label)
    ]
    asking_labels = [
        label for label in unique_labels
        if label not in fda_labels and not is_moderator_speaker_name(label)
    ]
    speaker_refusing = " and ".join(fda_labels) if fda_labels else "Unknown"
    speaker_asking = asking_labels[0] if asking_labels else "Unknown"
    return {
        "speaker_refusing": speaker_refusing,
        "speaker_asking": speaker_asking
    }

### CLASSIFICATION NORMALIZATION
def normalize_classification_result(classification, inst):
    normalized = classification or {}
    fallback_speakers = infer_speakers_from_passage(inst.get("passage", ""))
    legitimacy_score = normalized.get("legitimacy_score")
    if isinstance(legitimacy_score, str) and legitimacy_score.strip().isdigit():
        legitimacy_score = int(legitimacy_score.strip())
    if not isinstance(legitimacy_score, int):
        legitimacy_score = None
    category_code = str(normalized.get("category_code", "")).strip()
    category_name = str(normalized.get("category_name", "")).strip()
    if "is_active_refusal" in normalized:
        is_active_refusal = bool(normalized.get("is_active_refusal"))
    else:
        is_active_refusal = False if inst.get("is_boilerplate") else any(cue in inst.get("passage", "").lower() for cue in REFUSAL_STRONG_CUE_SUBSTRINGS)
    if inst.get("is_boilerplate"):
        if not category_code:
            category_code = "A"
        if legitimacy_score is None:
            legitimacy_score = 0
        is_active_refusal = False
    elif not category_code:
        category_code = "UNRESOLVED"
    if not category_name:
        category_name = REFUSAL_CATEGORY_NAMES.get(category_code, "Classification missing")
    rationale = str(normalized.get("rationale", "")).strip() or "No classification rationale returned."
    key_excerpt = str(normalized.get("key_excerpt", "")).strip()
    if not key_excerpt:
        for line in inst.get("passage", "").splitlines():
            stripped = line.strip()
            if stripped:
                key_excerpt = stripped[:200]
                break
    speaker_refusing = str(normalized.get("speaker_refusing", "")).strip() or fallback_speakers["speaker_refusing"]
    speaker_asking = str(normalized.get("speaker_asking", "")).strip() or fallback_speakers["speaker_asking"]
    return {
        "category_code": category_code,
        "is_active_refusal": is_active_refusal,
        "category_name": category_name,
        "legitimacy_score": legitimacy_score,
        "rationale": rationale,
        "key_excerpt": key_excerpt,
        "speaker_refusing": speaker_refusing,
        "speaker_asking": speaker_asking,
        "could_have_generalized": bool(normalized.get("could_have_generalized", False)),
        "asks_about_third_party_submission": bool(normalized.get("asks_about_third_party_submission", False))
    }
def report_value(value, fallback="Unknown"):
    if value is None:
        return fallback
    value = str(value).strip()
    return value if value else fallback
def format_legitimacy_score(value):
    if isinstance(value, int):
        if value == 0:
            return "0 (not scored)"
        return f"{value}/5"
    return "n/a"

### CLEANUP HELPERS
def dedupe_boilerplate_results(results):
    deduped = []
    seen = set()
    for result in results:
        key = (
            report_value(result.get("file")),
            report_value(result.get("section_heading_text"))
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(result)
    return deduped
def normalize_and_validate_instances(raw_instances, total_lines, lines):
    """
    Sort, validate, and lightly de-duplicate extracted line ranges.
    """
    cleaned = []
    seen = set()

    for inst in raw_instances:
        start_line = int(inst["start_line"])
        end_line = int(inst["end_line"])

        if start_line < 1:
            start_line = 1
        if end_line > total_lines:
            end_line = total_lines
        if end_line < start_line:
            continue
        start_line, end_line = normalize_instance_range(lines, start_line, end_line)
        if not bool(inst["is_boilerplate"]):
            expanded_range = expand_refusal_exchange(lines, start_line, end_line)
            if not expanded_range:
                continue
            start_line, end_line = expanded_range

        key = (
            start_line,
            end_line,
            bool(inst["is_boilerplate"])
        )
        if key in seen:
            continue
        seen.add(key)

        cleaned.append({
            "start_line": start_line,
            "end_line": end_line,
            "is_boilerplate": bool(inst["is_boilerplate"]),
            "refusal_type": inst["refusal_type"].strip(),
            "brief_description": inst["brief_description"].strip(),
            "confidence": inst["confidence"]
        })

    cleaned.sort(key=lambda x: (x["start_line"], x["end_line"]))
    return cleaned

### MAIN REFUSAL ANALYSIS FUNCTIONS
def refusal_extract_from_file(file_path, prompt, tools, model=OPENAI_MODEL, verbose=False):
    """
    Step 1: extract refusal instances by line range, then extract the actual text in Python.

    :param file_path: string path to one transcript file
    :param prompt: string system prompt for extraction
    :param tools: list of structured-output tool definitions
    :param model: string model name
    :param verbose: bool for debug printing
    :return: list of extracted instance dicts
    """
    raw_text = read_complete_text(file_path)
    lines = raw_text.splitlines()
    fname = os.path.basename(file_path)

    response = openai_function_call(
        prompt=prompt,
        content=raw_text,
        tools=tools,
        model=model,
        verbose=verbose
    )
    arguments = parse_function_call_response(response, "openai")
    if not arguments:
        print(f"WARNING: No extraction response for {fname}")
        return []

    extracted = normalize_and_validate_instances(
        arguments.get("refusal_instances", []) + build_heuristic_refusal_instances(lines),
        total_lines=len(lines),
        lines=lines
    )

    instances = []
    for inst in extracted:
        passage = slice_lines(lines, inst["start_line"], inst["end_line"])
        heading_meta = find_nearest_section_heading(lines, inst["start_line"])
        if inst["is_boilerplate"] and not report_value(heading_meta.get("section_heading_text"), "").startswith("#### "):
            heading_meta = find_first_topical_section_heading(lines, inst["start_line"])
        is_boilerplate = bool(inst["is_boilerplate"]) or is_first_topical_section_heading(heading_meta.get("section_heading_text"))

        instances.append({
            "file": fname,
            "source_file_path": file_path,
            "total_files_checked": 1,
            "start_line": inst["start_line"],
            "end_line": inst["end_line"],
            "is_boilerplate": is_boilerplate,
            "refusal_type": inst["refusal_type"],
            "brief_description": inst["brief_description"],
            "confidence": inst["confidence"],
            "section_heading_line": heading_meta["section_heading_line"],
            "section_heading_text": heading_meta["section_heading_text"],
            "passage": passage
        })

    return instances
def refusal_extract_from_folder(folder_path, suffix, prompt, tools, model, output_path=None, verbose=False):
    """
    Run step 1 across all matching files in a folder and save JSON.

    :param folder_path: folder containing transcript files
    :param suffix: suffix filter, e.g. '_section-titles.md'
    :param prompt: extraction prompt
    :param tools: extraction structured-output tool schema
    :param model: model name
    :param output_path: output JSON path or None to skip writing
    :param verbose: bool for debug printing
    :return: list of extracted instances
    """
    files = sorted(get_files_in_folder(folder_path, suffixpat_include=suffix))
    print(f"Found {len(files)} files matching suffix '{suffix}'")

    all_instances = []
    for i, fpath in enumerate(files, 1):
        fname = os.path.basename(fpath)
        print(f"[{i}/{len(files)}] {fname}")
        instances = refusal_extract_from_file(fpath, prompt, tools, model=model, verbose=verbose)
        for inst in instances:
            inst["total_files_checked"] = len(files)
        print(f"  Found {len(instances)} instances")
        all_instances.extend(instances)

    if output_path:
        write_json_file_from_json_data(all_instances, output_path, overwrite="yes")
        print(f"Saved step 1 extraction JSON to: {output_path}")
    return all_instances
def refusal_classify(instances_path, prompt, tools, model, output_path=None, verbose=False):
    """
    Step 2: classify extracted instances with rubric-based structured outputs.

    :param instances_path: path to extraction JSON or list of extracted instances
    :param prompt: classification prompt
    :param tools: classification structured-output tool schema
    :param model: model name
    :param output_path: output JSON path or None to skip writing
    :param verbose: bool for debug printing
    :return: list of classification results
    """
    if isinstance(instances_path, str):
        instances = get_json_data_from_json_file(instances_path)
    else:
        instances = instances_path
    results = []

    for i, inst in enumerate(instances, 1):
        print(f"[{i}/{len(instances)}] {inst['file']} lines {inst['start_line']}-{inst['end_line']}")

        context_prefix = (
            f"FILE: {inst['file']}\n"
            f"LINE RANGE: {inst['start_line']}-{inst['end_line']}\n"
            f"SECTION: {inst.get('section_heading_text')}\n"
            f"EXTRACTION NOTE: {inst.get('brief_description')}\n"
            f"EXTRACTED TYPE: {inst.get('refusal_type')}\n"
        )
        full_prompt = prompt + "\n\n" + context_prefix

        response = openai_function_call(
            prompt=full_prompt,
            content=inst["passage"],
            tools=tools,
            model=model,
            verbose=verbose,
            temperature=0
        )
        classification = parse_function_call_response(response, "openai")
        if not classification:
            print("  WARNING: Classification failed")
            classification = {}

        result = {
            **inst,
            **normalize_classification_result(classification, inst)
        }
        if not result["is_boilerplate"] and result.get("category_code") == "UNRESOLVED":
            print("  -> filtered out (classification unresolved)")
            continue
        if not result["is_boilerplate"] and not result.get("is_active_refusal", False):
            print("  -> filtered out (not an active refusal)")
            continue
        results.append(result)

        print(f"  -> {result['category_code']} ({result['legitimacy_score'] if result['legitimacy_score'] is not None else 'n/a'})")

    if output_path:
        write_json_file_from_json_data(results, output_path, overwrite="yes")
        print(f"Saved step 2 classification JSON to: {output_path}")
    return results
def refusal_generate_report(step2_path, output_md_path):
    """
    Generate markdown report with valid tables and line-range references.

    :param step2_path: path to classified JSON or list of classified instances
    :param output_md_path: path for markdown report
    :return: output_md_path
    """
    if isinstance(step2_path, str):
        results = get_json_data_from_json_file(step2_path)
    else:
        results = step2_path

    boilerplate = dedupe_boilerplate_results([r for r in results if r.get("is_boilerplate")])
    active = [r for r in results if not r.get("is_boilerplate")]
    scored = [r for r in active if isinstance(r.get("legitimacy_score"), int) and r["legitimacy_score"] > 0]
    total_identified = len(boilerplate) + len(active)
    total_files_checked = max((int(r.get("total_files_checked", 1)) for r in results), default=1)
    files_with_refusals = len(set(report_value(r.get("file")) for r in boilerplate + active))

    cat_counts = Counter(r.get("category_code") or "UNRESOLVED" for r in scored)
    score_counts = Counter(r.get("legitimacy_score") for r in scored)

    lines = []
    lines.append("## 3. Classification and Scoring of All Identified Instances")
    lines.append("")
    lines.append(f"**Total instances identified:** {total_identified}")
    lines.append(f"**Boilerplate opening disclaimers (Category A):** {len(boilerplate)}")
    lines.append(f"**Active refusals (Scored):** {len(active)}")
    lines.append("")

    lines.append("### 3a. Boilerplate Instances (Category A — Not Scored)")
    lines.append("")
    lines.append("The following instances are the standard moderator disclaimer read at the opening of each session. They are catalogued but not scored, as they represent institutional policy rather than active refusals.")
    lines.append("")
    lines.append("| # | File | Section |")
    lines.append("| --- | --- | --- |")
    for i, r in enumerate(boilerplate, 1):
        lines.append(f"| {i} | {report_value(r.get('file'))} | {report_value(r.get('section_heading_text'))} |")
    lines.append("||")
    lines.append("")
    lines.append(f"**Total boilerplate instances:** {len(boilerplate)}")
    lines.append("")

    lines.append("### 3b. Active Refusals (Scored)")
    lines.append("")
    for i, r in enumerate(active, 1):
        lines.append(f"#### Instance {i}: {report_value(r.get('file'))}")
        lines.append(f"**Line range:** {r['start_line']}-{r['end_line']}")
        lines.append(f"**Section:** {report_value(r.get('section_heading_text'))}")
        lines.append(f"**Category:** {report_value(r.get('category_code'))} — {report_value(r.get('category_name'))}")
        lines.append(f"**Legitimacy Score:** {format_legitimacy_score(r.get('legitimacy_score'))}")
        lines.append(f"**Rationale:** {report_value(r.get('rationale'), 'No rationale returned.')}")
        lines.append(f"**Speaker refusing:** {report_value(r.get('speaker_refusing'))}")
        lines.append(f"**Speaker asking:** {report_value(r.get('speaker_asking'))}")
        lines.append("")
        lines.append("**Excerpt:**")
        for passage_line in (report_value(r.get("passage"), "").split("\n") if r.get("passage") else ["[no excerpt available]"]):
            lines.append(passage_line)
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## 4. Summary of Results")
    lines.append("")
    lines.append("### Overall Distribution")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("| --- | --- |")
    lines.append(f"| Total refusal instances identified | {total_identified} |")
    lines.append(f"| Boilerplate opening disclaimers (not scored) | {len(boilerplate)} |")
    lines.append(f"| Active refusals (scored) | {len(active)} |")
    lines.append(f"| Files with at least one refusal | {files_with_refusals} of {total_files_checked} |")
    lines.append("||")
    lines.append("")

    lines.append("### Distribution by Category (Active Refusals Only)")
    lines.append("")
    lines.append("| Code | Category | Count | Avg Score |")
    lines.append("| --- | --- | --- | --- |")
    for code, count in sorted(cat_counts.items()):
        cat_items = [r for r in scored if r.get("category_code") == code]
        scores = [r["legitimacy_score"] for r in cat_items if isinstance(r.get("legitimacy_score"), int) and r["legitimacy_score"] >= 0]
        avg_score_display = f"{sum(scores) / len(scores):.1f}" if scores else "n/a"
        cat_name = cat_items[0].get("category_name", "") if cat_items else REFUSAL_CATEGORY_NAMES.get(code, "Unknown")
        lines.append(f"| {code} | {report_value(cat_name)} | {count} | {avg_score_display} |")
    lines.append("||")
    lines.append("")

    lines.append("### Distribution by Legitimacy Score (Scored Active Refusals Only)")
    lines.append("")
    score_labels = {
        5: "Fully Legitimate",
        4: "Largely Legitimate",
        3: "Mixed / Could Have Done Better",
        2: "Questionable",
        1: "Not Legitimate"
    }
    lines.append("| Score | Label | Count | % of Active Refusals |")
    lines.append("| --- | --- | --- | --- |")
    for score in [5, 4, 3, 2, 1]:
        count = score_counts.get(score, 0)
        pct = (count / len(scored) * 100) if scored else 0
        lines.append(f"| {score} | {score_labels[score]} | {count} | {pct:.0f}% |")
    lines.append("||")
    lines.append("")

    if scored:
        avg = sum(r["legitimacy_score"] for r in scored) / len(scored)
        could_generalize = sum(1 for r in scored if r.get("could_have_generalized"))
        questionable = sum(1 for r in scored if r["legitimacy_score"] <= 2)
        strong = sum(1 for r in scored if r["legitimacy_score"] >= 4)
        lines.append("### Key Findings")
        lines.append("")
        lines.append(f"- **Average legitimacy score across active refusals: {avg:.1f}/5**")
        lines.append(f"- **{questionable} of {len(scored)} active refusals ({questionable/len(scored)*100:.0f}%) scored 2 or below.**")
        lines.append(f"- **{strong} of {len(scored)} active refusals ({strong/len(scored)*100:.0f}%) scored 4 or above.**")
        lines.append(f"- **{could_generalize} of {len(scored)} active refusals ({could_generalize/len(scored)*100:.0f}%) could plausibly have been generalized publicly.**")
        if cat_counts:
            most_common_code, most_common_count = cat_counts.most_common(1)[0]
            lines.append(f"- **Most common active refusal category: {most_common_code} ({most_common_count} instances).**")
        lines.append("")
        lines.append("### Interpretation")
        lines.append("")
        lines.append("The data supports the following conclusions:")
        lines.append("")
        top_category_code = cat_counts.most_common(1)[0][0] if cat_counts else None
        top_category_name = REFUSAL_CATEGORY_NAMES.get(top_category_code, "Unknown pattern") if top_category_code else "Unknown pattern"
        lines.append(f"1. **The balance of refusals in this file leans toward {top_category_name.lower()}.** The most common scored category was {top_category_code}, which suggests the dominant refusal pattern in this exchange set was not random but structurally repeated.")
        lines.append("")
        lines.append(f"2. **The overall legitimacy level is {'relatively high' if avg >= 3.5 else 'mixed' if avg >= 2.5 else 'relatively low'}.** With an average legitimacy score of {avg:.1f}/5, the FDA's refusal behavior in this file was {'often paired with meaningful general guidance' if avg >= 3.5 else 'a mix of partial guidance and questionable deflection' if avg >= 2.5 else 'more often characterized by deflection than transparent public guidance'}.")
        lines.append("")
        lines.append(f"3. **A substantial share of these refusals could still have been generalized publicly.** {could_generalize} of {len(scored)} scored refusals were marked as potentially generalizable, which indicates that confidentiality was not always the only available response.")
        lines.append("")
        lines.append(f"4. **The boilerplate disclaimer framed the session before Q&A even began.** The file contains {len(boilerplate)} boilerplate instance{'s' if len(boilerplate) != 1 else ''}, reinforcing the expectation that some lines of questioning would be treated as off-limits from the start.")

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Report written to: {output_md_path}")
    return output_md_path

### EXECUTION CODE
# SETTINGS
    TRANSCRIPT_DIR = "data/floodlamp/regulatory/fda-townhalls/_exclude-from-archive/_sample-test-group"
    INTERMEDIATE_DIR = "data/floodlamp/regulatory/fda-townhalls/_exclude-from-archive/_refusal-analysis-intermediate-files"
    FILE_SUFFIX = "_section-titles.md"
    MODEL = "gpt-5.4"
    REPORT_OUTPUT = f"{INTERMEDIATE_DIR}/_sample-test-group-report.md"

    os.makedirs(INTERMEDIATE_DIR, exist_ok=True)

# ---- SINGLE FILE TEST RUN
    # TEST_FILE = "data/floodlamp/regulatory/fda-townhalls/fda-townhalls-transcripts-qa/2020-06-10_Virtual Town Hall 12_section-titles.md" 
    # test_report = f"{INTERMEDIATE_DIR}/test17_report.md"
    # test_instances = refusal_extract_from_file(
    #     TEST_FILE,
    #     PROMPT_REFUSAL_EXTRACTION,
    #     TOOLS_REFUSAL_EXTRACTION,
    #     model=MODEL
    # )
    # test_results = refusal_classify(
    #     test_instances,
    #     PROMPT_REFUSAL_CLASSIFICATION,
    #     TOOLS_REFUSAL_CLASSIFICATION,
    #     MODEL
    # )
    # refusal_generate_report(test_results, test_report)

# ---- RUN ON FOLDER
    full_instances = refusal_extract_from_folder(
        TRANSCRIPT_DIR,
        FILE_SUFFIX,
        PROMPT_REFUSAL_EXTRACTION,
        TOOLS_REFUSAL_EXTRACTION,
        MODEL
    )
    full_results = refusal_classify(
        full_instances,
        PROMPT_REFUSAL_CLASSIFICATION,
        TOOLS_REFUSAL_CLASSIFICATION,
        MODEL
    )
    refusal_generate_report(full_results, REPORT_OUTPUT)
