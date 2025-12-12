import os
import subprocess
import sys


SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'markdown2html.py')


def run(*args):
    cmd = [sys.executable, SCRIPT] + list(args)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out.decode(), err.decode()


def test_headings_conversion(tmp_path):
    inp = tmp_path / 'README.md'
    out = tmp_path / 'README.html'
    inp.write_text('# My title\n## My title2\n# My title3\n#### My title4\n### My title5\n')

    rc, sout, serr = run(str(inp), str(out))
    assert rc == 0
    assert sout == ''
    assert serr == ''
    assert out.exists()

    content = out.read_text()
    expected = (
        '<h1>My title</h1>\n'
        '<h2>My title2</h2>\n'
        '<h1>My title3</h1>\n'
        '<h4>My title4</h4>\n'
        '<h3>My title5</h3>\n'
    )
    assert content == expected
