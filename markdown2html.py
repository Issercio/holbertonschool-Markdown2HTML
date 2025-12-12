#!/usr/bin/python3
"""
Minimal markdown2html converter starter per requirements.
"""
import sys
import os


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # According to the task, do nothing else for now
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                f_out.write(line)
    except Exception:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
