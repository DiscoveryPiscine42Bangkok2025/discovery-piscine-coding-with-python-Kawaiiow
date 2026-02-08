import pytest
from conftest import run_module

MODULE = "cell02.ex03.mult"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_mult_positive(module_result):
    result = run_module(MODULE, "42\n42\n")[0]
    out = result.stdout

    assert result.returncode == 0
    assert "42 x 42 = 1764" in out
    assert "result is positive" in out.lower()

def test_mult_negative(module_result):
    result = run_module(MODULE, "78\n-1\n")[0]
    out = result.stdout

    assert result.returncode == 0
    assert "78 x -1 = -78" in out
    assert "result is negative" in out.lower()

def test_mult_zero(module_result):
    result = run_module(MODULE, "72\n0\n")[0]
    out = result.stdout

    assert result.returncode == 0
    assert "72 x 0 = 0" in out
    assert "positive and negative" in out.lower()
