#!/usr/bin/env python3
"""
Interpreter for rabbi_ighfir_332837_times.txt

Streams the file without loading the ~641 MB source into memory.
Usage:
    python3 rabbi_ighfir_interpreter.py rabbi_ighfir_332837_times.txt
    python3 rabbi_ighfir_interpreter.py rabbi_ighfir_332837_times.txt --verify
    python3 rabbi_ighfir_interpreter.py rabbi_ighfir_332837_times.txt --count
"""

import argparse
import hashlib
from pathlib import Path

TARGET = "رَبِّ اغْفِرْ وَارْحَمْ وَأَنْتَ خَيْرُ الرَّاحِمِينَ"
FILLER = "خير"

def interpret(path: Path, verify=False, count_only=False):
    repetitions = 0
    filler_count = 0
    nonempty_lines = 0
    sha256 = hashlib.sha256()

    with path.open("r", encoding="utf-8", newline="") as f:
        for raw in f:
            sha256.update(raw.encode("utf-8"))
            line = raw.rstrip("\r\n")

            # A filler line represents the requested replacement for a blank space.
            if line == FILLER:
                filler_count += 1
                continue

            if line == "":
                continue

            nonempty_lines += 1

            # Each source repetition is represented by the exact supplied block.
            # Count the occurrences of the complete requested prayer within the line.
            repetitions += line.count(TARGET)

    print(f"File: {path}")
    print(f"Prayer occurrences: {repetitions:,}")
    print(f'Filler "{FILLER}" lines: {filler_count:,}')
    print(f"Non-empty lines: {nonempty_lines:,}")

    if verify:
        expected = 332_837
        if repetitions == expected:
            print("Verification: PASS — expected prayer occurrence count found.")
        else:
            print(f"Verification: FAIL — expected {expected:,}, found {repetitions:,}.")

    print(f"SHA-256: {sha256.hexdigest()}")

def main():
    parser = argparse.ArgumentParser(description="Streaming interpreter/verifier for the generated Arabic repetition file.")
    parser.add_argument("file", nargs="?", default="rabbi_ighfir_332837_times.txt")
    parser.add_argument("--verify", action="store_true", help="verify the expected 332,837 prayer occurrences")
    parser.add_argument("--count", action="store_true", help="count and report occurrences (default behavior)")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")

    interpret(path, verify=args.verify, count_only=args.count)

if __name__ == "__main__":
    main()
