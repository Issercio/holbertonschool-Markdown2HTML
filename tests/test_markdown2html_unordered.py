import os
import subprocess
import sys


SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'markdown2html.py')


def run(*args):
    cmd = [sys.executable, SCRIPT] + list(args)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out.decode(), err.decode()


def test_unordered_list_conversion(tmp_path):
    inp = tmp_path / 'README.md'
    out = tmp_path / 'README.html'
    inp.write_text('# My title\n- Hello\n- Bye\n')

    rc, sout, serr = run(str(inp), str(out))
    assert rc == 0
    assert sout == ''
    assert serr == ''
    assert out.exists()

    content = out.read_text()
    expected = (
        '<h1>My title</h1>\n'
        '<ul>\n'
        '<li>Hello</li>\n'
        '<li>Bye</li>\n'
        '</ul>\n'
    )
    assert content == expected
