import pytest
from conftest import run_module

MODULE = "cell02.ex01.isneg"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_isneg_positive(module_result):
    result, _ = module_result
    result = run_module(MODULE, "42\n")[0]

    assert result.returncode == 0
    assert "positive" in result.stdout.lower()
    assert "both" not in result.stdout.lower()

def test_isneg_negative(module_result):
    result = run_module(MODULE, "-42\n")[0]

    assert result.returncode == 0
    assert "negative" in result.stdout.lower()
    assert "both" not in result.stdout.lower()

def test_isneg_zero(module_result):
    result = run_module(MODULE, "0\n")[0]

    assert result.returncode == 0
    assert "both positive and negative" in result.stdout.lower()
