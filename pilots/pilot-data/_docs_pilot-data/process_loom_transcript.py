"""
Process Loom SRT transcripts into readable text.

Removes sequence numbers, joins split sentences, and keeps timestamps only every ~1 minute at sentence starts.
"""
import re
import os
from pathlib import Path

### Core processing
def parse_timestamp(ts_str):
    """
    Parse timestamp string to total seconds.

    :param ts_str: str, timestamp in format "HH:MM:SS,mmm".
    :return seconds: float, total seconds.
    """
    match = re.match(r'(\d+):(\d+):(\d+),(\d+)', ts_str)
    if not match:
        return 0.0
    h, m, s, ms = match.groups()
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
def format_timestamp(seconds):
    """
    Format seconds to MM:SS timestamp.

    :param seconds: float, total seconds.
    :return ts_str: str, timestamp in format "MM:SS".
    """
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"
def parse_srt(content):
    """
    Parse SRT content into list of (start_time_seconds, text) tuples.

    :param content: str, raw SRT file content.
    :return entries: list, list of (float, str) tuples with start time and text.
    """
    entries = []
    blocks = re.split(r'\n\n+', content.strip())
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 2:
            continue
        # First line is sequence number (skip it)
        # Second line is timestamp
        # Remaining lines are text
        ts_line = None
        text_lines = []
        for i, line in enumerate(lines):
            if '-->' in line:
                ts_line = line
                text_lines = lines[i+1:]
                break
        if ts_line is None:
            continue
        # Extract start timestamp
        ts_match = re.match(r'(\d+:\d+:\d+,\d+)\s*-->', ts_line)
        if not ts_match:
            continue
        start_ts = ts_match.group(1)
        start_seconds = parse_timestamp(start_ts)
        text = ' '.join(text_lines).strip()
        if text:
            entries.append((start_seconds, text))
    return entries
def is_sentence_start(text):
    """
    Check if text looks like the start of a sentence.

    :param text: str, text to check.
    :return is_start: bool, True if text starts with capital letter or sentence-starting pattern.
    """
    if not text:
        return False
    # Starts with capital letter
    if text[0].isupper():
        return True
    return False
def process_transcript(content, timestamp_interval=60):
    """
    Process SRT transcript into readable text with periodic timestamps.

    :param content: str, raw SRT file content.
    :param timestamp_interval: int, minimum seconds between timestamps.
    :return output: str, processed transcript text.
    """
    entries = parse_srt(content)
    if not entries:
        return ""
    # Join all text, tracking where we might insert timestamps
    output_parts = []
    last_timestamp_seconds = -timestamp_interval  # Ensure first entry gets timestamp if at sentence start
    accumulated_text = ""
    for i, (start_seconds, text) in enumerate(entries):
        # Check if we should insert a timestamp
        time_since_last = start_seconds - last_timestamp_seconds
        should_add_timestamp = time_since_last >= timestamp_interval
        # Check if this is a sentence start (previous text ends with sentence-ending punctuation)
        prev_ends_sentence = False
        if accumulated_text:
            prev_ends_sentence = accumulated_text.rstrip().endswith(('.', '!', '?', '."', '?"', '!"'))
        at_sentence_start = (i == 0) or prev_ends_sentence or is_sentence_start(text)
        if should_add_timestamp and at_sentence_start:
            # Add newline before timestamp if we have accumulated text
            if accumulated_text:
                output_parts.append(accumulated_text.rstrip())
                accumulated_text = ""
            # Add timestamp
            ts_formatted = format_timestamp(start_seconds)
            accumulated_text = f"[{ts_formatted}] {text}"
            last_timestamp_seconds = start_seconds
        else:
            # Continue accumulating text
            if accumulated_text:
                # Check if we need a space
                if accumulated_text.endswith(('.', '!', '?', '."', '?"', '!"')):
                    # New sentence, add space
                    accumulated_text += " " + text
                elif accumulated_text.endswith(' ') or text.startswith(' '):
                    accumulated_text += text
                else:
                    accumulated_text += " " + text
            else:
                accumulated_text = text
    # Don't forget the last accumulated text
    if accumulated_text:
        output_parts.append(accumulated_text.rstrip())
    return '\n\n'.join(output_parts)
def process_srt_file(input_path, output_path=None, timestamp_interval=60):
    """
    Process an SRT file and write the result.

    :param input_path: str, path to input SRT file.
    :param output_path: str, path to output text file (default: same name with .txt extension).
    :param timestamp_interval: int, minimum seconds between timestamps.
    :return output_path: str, path to the output file.
    """
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.with_suffix('.txt')
    else:
        output_path = Path(output_path)
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    result = process_transcript(content, timestamp_interval)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Processed: {input_path}")
    print(f"Output: {output_path}")
    return str(output_path)
def process_directory(directory, timestamp_interval=60):
    """
    Process all SRT files in a directory.

    :param directory: str, path to directory containing SRT files.
    :param timestamp_interval: int, minimum seconds between timestamps.
    :return outputs: list, list of output file paths.
    """
    directory = Path(directory)
    outputs = []
    for srt_file in directory.glob('*.srt'):
        output_path = process_srt_file(srt_file, timestamp_interval=timestamp_interval)
        outputs.append(output_path)
    return outputs

### mrun execution stubs
def mrun_process_single():
    pass
#if __name__ == "__main__":
    srt_path = "data/floodlamp/pilots/pilot-data/_docs_pilot-data/Loom Transcript - Jan26 Data Pipeline Walkthru - part 2.srt"
    process_srt_file(srt_path, timestamp_interval=60)
def mrun_process_directory():
    pass
#if __name__ == "__main__":
    directory = "data/floodlamp/pilots/pilot-data/_docs_pilot-data"
    process_directory(directory, timestamp_interval=60)

if __name__ == "__main__":
    # Process the example file
    import sys
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            if os.path.isdir(path):
                process_directory(path)
            else:
                process_srt_file(path)
    else:
        # Default: process files in the same directory as this script
        script_dir = Path(__file__).parent
        srt_files = list(script_dir.glob('*.srt'))
        if srt_files:
            for srt_file in srt_files:
                process_srt_file(srt_file)
        else:
            print("Usage: python process_loom_transcript.py [file.srt|directory]")
