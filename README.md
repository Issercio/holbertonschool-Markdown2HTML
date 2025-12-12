# holbertonschool-Markdown2HTML ✅

A small Markdown -> HTML converter written in Python that supports a focused subset of Markdown syntax used for learning and exercises.

This project is intended as an educational implementation and covers the following features:

- Headings (# .. ######)
- Unordered lists (`- item`)
- Ordered lists (`* item`)
- Paragraphs (separated by blank lines; multi-line paragraphs keep line breaks with `<br/>`)
- Inline formatting:
	- Bold: `**text**` -> `<b>text</b>`
	- Emphasis: `__text__` -> `<em>text</em>`
- Custom inline transforms:
	- `((text))` -> remove all `c` and `C` characters from `text`
	- `[[text]]` -> MD5 hash (lowercase hex) of `text`

---

## Requirements 🔧

- Python 3.7 or higher
- The script uses only the Python standard library (no external packages required)

Note: `markdown2html.py` includes a shebang and should be executable. If needed run:

```bash
chmod +x markdown2html.py
```

## Usage

```bash
./markdown2html.py input.md output.html
```

Behavior:
- If you pass fewer than 2 arguments, the script prints to STDERR:
	`Usage: ./markdown2html.py README.md README.html` and exits with code `1`.
- If the input file does not exist, the script prints to STDERR:
	`Missing <filename>` and exits with code `1`.
- On success the script writes the converted HTML to the output file and exits with code `0` (no stdout/stderr).

## Examples

Input (README.md):

```markdown
# My title
- Hello
- Bye

Hello

I'm **a** text
with __2 lines__

((I will live in Caracas))

But it's [[private]]

So cool!
```

Output (README.html):

```html
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm <b>a</b> text
<br/>
with <em>2 lines</em>
</p>
<p>
I will live in araas
</p>
<p>
But it's 2c17c6393771ee3048ae34d6b380c5ec
</p>
<p>
So cool!
</p>
```

Note: spacing and blank lines between tags are not required to match exactly.

## Running tests ✅

This repo includes a set of pytest tests under the `tests/` directory. To run them:

```bash
pytest -q tests/test_markdown2html_*.py
```

If your environment raises an import error related to `pytest_flask` (seen in some global environments), you can disable that plugin when running tests:

```bash
pytest -q -p no:pytest_flask tests/test_markdown2html_*.py
```

Or run the individual test files directly with Python if you prefer to avoid pytest plugin issues.

## Contributing

Contributions, bug reports, and feature requests are welcome. If you'd like to add more Markdown features (links, inline code, nested lists, etc.), open an issue or submit a pull request with tests.

## License

This project currently has no explicit license. Add a `LICENSE` file if you wish to apply one.
