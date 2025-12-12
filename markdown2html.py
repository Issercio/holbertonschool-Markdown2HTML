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

    # Ensure output file exists (empty conversion is acceptable per requirements)
    try:
        with open(output_file, 'w') as f_out:
            # Intentionally leave empty; conversion is out of scope for this task
            pass
    except Exception:
        # If we cannot write the output file, exit with non-zero status
        sys.exit(1)

    # Success: no output and exit 0
    sys.exit(0)


if __name__ == "__main__":
    main()
