from subprocess import run
from pathlib import Path
import re
import jugmt

REGEX_PYTHON_SLOC=r"^python:\s+(?P<nlines>\d+)\s+\((?P<percent>\d+\.\d+)%\)$"

def project_sloc_jinja2():
    """Count number of lines in jinja2 templates"""

    sloc = 0
    for path in Path(jugmt.__file__).parent.rglob("*.jinja2"):
        with path.open() as content:
            sloc += sum(1 for line in content)

    return sloc

def project_sloc_python():
    """Count number of lines of Python code, returning (nlines, npercent)"""
    
    path = Path(jugmt.__file__).parent
    
    result = run(
        ["sloccount", f"{path}"],
        capture_output=True,
        text=True,
    )

    nlines = 0
    npercent = 0
    for line in result.stdout.splitlines():
        match = re.match(REGEX_PYTHON_SLOC, line)
        if match:
            nlines = int(match.group("nlines"))
            npercent = float(match.group("percent"))

    return nlines, npercent
            
def test_weight():
    """Test that the jugmt source do not grow too large"""
    
    python_sloc, python_percent = project_sloc_python()
    
    assert python_percent == 100, "This is a Python project; expecting 100% Python code"
    assert python_sloc < 300, "Too much Python code; simplify the code"

    jinja2_sloc = project_sloc_jinja2()
    assert jinja2_sloc < 150, "Too much jinja2 template-code; simplify the code"

    assert jinja2_sloc, "The codebase uses jinja2 templates, so this must be >0"
    assert python_percent, "The codebase is Python; must have percent Python code >0"
    assert python_sloc, "The codebase is Python; must have line of code > 0"