# test_c1_ex03_whatsyourname.py
import pytest
from conftest import run_module

MODULE = "cell01.ex03.whatsyourname"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_c1_ex03_whatsyourname(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "Wil\n42\n")

    assert result.returncode == 0

    output = result.stdout
    assert "Wil" in output
    assert "42" in output

def test_c1_ex03_whatsyourname_extra(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "Alice\nBob\n")

    assert result.returncode == 0

    output = result.stdout
    assert "Alice" in output
    assert "Bob" in output
