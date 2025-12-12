import os
import subprocess
import sys


SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'markdown2html.py')


def run(*args):
    cmd = [sys.executable, SCRIPT] + list(args)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out.decode(), err.decode()


def test_custom_transforms(tmp_path):
    inp = tmp_path / 'README.md'
    out = tmp_path / 'README.html'
    inp.write_text('# My title\n- He**l**lo\n- Bye\n\nHello\n\nI\'m **a** text\nwith __2 lines__\n\n((I will live in Caracas))\n\nBut it\'s [[private]]\n\nSo cool!\n')

    rc, sout, serr = run(str(inp), str(out))
    assert rc == 0
    assert sout == ''
    assert serr == ''
    assert out.exists()

    content = out.read_text()
    expected = (
        '<h1>My title</h1>\n'
        '<ul>\n'
        '<li>He<b>l</b>lo</li>\n'
        '<li>Bye</li>\n'
        '</ul>\n'
        '<p>\n'
        'Hello\n'
        '</p>\n'
        "<p>\nI'm <b>a</b> text\n<br/>\nwith <em>2 lines</em>\n</p>\n"
        '<p>\n'
        'I will live in araas\n'
        '</p>\n'
        '<p>\n'
        "But it's 2c17c6393771ee3048ae34d6b380c5ec\n"
        '</p>\n'
        '<p>\n'
        'So cool!\n'
        '</p>\n'
    )
    assert content == expected
