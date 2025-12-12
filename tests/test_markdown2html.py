import os
import subprocess
import sys
import tempfile


SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'markdown2html.py')


def run(*args):
    cmd = [sys.executable, SCRIPT] + list(args)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out.decode(), err.decode()


def test_no_args():
    rc, out, err = run()
    assert rc == 1
    assert out == ''
    assert err.strip() == 'Usage: ./markdown2html.py README.md README.html'


def test_missing_file():
    rc, out, err = run('NON_EXISTENT.md', 'out.html')
    assert rc == 1
    assert out == ''
    assert err.strip() == 'Missing NON_EXISTENT.md'


def test_existing_file(tmp_path):
    inp = tmp_path / 'README.md'
    out = tmp_path / 'README.html'
    inp.write_text('Test')

    rc, sout, serr = run(str(inp), str(out))
    assert rc == 0
    assert sout == ''
    assert serr == ''
    assert out.exists()
