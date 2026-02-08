# tests/test_cell04_ex01.py
import pytest
from conftest import run_module

MODULE = "cell04.ex01.age"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_age_calculation(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "15\n")

    assert result.returncode == 0
    out = result.stdout

    assert "You are currently 15" in out
    assert "25 years old" in out
    assert "35 years old" in out
    assert "45 years old" in out
