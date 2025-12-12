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

    # Read input and convert heading lines to HTML
    try:
        with open(input_file, 'r') as f_in:
            lines = f_in.readlines()
    except Exception:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    out_lines = []
    list_type = None  # None, 'ul' or 'ol'
    for line in lines:
        s = line.rstrip('\n')
        # Heading has priority. If a heading appears while in a list, close the list.
        if s.startswith('#'):
            if list_type is not None:
                out_lines.append(f"</{list_type}>\n")
                list_type = None
            # Count leading '#' until first space
            parts = s.split(' ', 1)
            if len(parts) == 2 and parts[0].count('#') == len(parts[0]) and 1 <= len(parts[0]) <= 6:
                level = len(parts[0])
                text = parts[1]
                out_lines.append(f"<h{level}>{text}</h{level}>\n")
                continue

        # Unordered list item: lines starting with '- ' (strict syntax)
        if s.startswith('- '):
            if list_type is None:
                out_lines.append('<ul>\n')
                list_type = 'ul'
            elif list_type != 'ul':
                # close previous list and open ul
                out_lines.append(f"</{list_type}>\n")
                out_lines.append('<ul>\n')
                list_type = 'ul'
            text = s[2:]
            out_lines.append(f"<li>{text}</li>\n")
            continue

        # Ordered list item: lines starting with '* ' (strict syntax)
        if s.startswith('* '):
            if list_type is None:
                out_lines.append('<ol>\n')
                list_type = 'ol'
            elif list_type != 'ol':
                out_lines.append(f"</{list_type}>\n")
                out_lines.append('<ol>\n')
                list_type = 'ol'
            text = s[2:]
            out_lines.append(f"<li>{text}</li>\n")
            continue

        # Non-heading, non-list lines: if we are in a list, close it first
        if list_type is not None:
            out_lines.append(f"</{list_type}>\n")
            list_type = None

        if s == '':
            out_lines.append('\n')
        else:
            out_lines.append(s + '\n')

    # Close any open list at EOF
    if list_type is not None:
        out_lines.append(f"</{list_type}>\n")

    try:
        with open(output_file, 'w') as f_out:
            f_out.writelines(out_lines)
    except Exception:
        # If we cannot write the output file, exit with non-zero status
        sys.exit(1)

    # Success: no output and exit 0
    sys.exit(0)


if __name__ == "__main__":
    main()
