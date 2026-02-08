# tests/test_cell04_ex02.py
import pytest
from conftest import run_module

MODULE = "cell04.ex02.calculator"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_calculator_operations(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "10\n2\n")

    out = result.stdout

    assert "10 + 2 = 12" in out
    assert "10 - 2 = 8" in out
    assert "10 / 2 = 5" in out
    assert "10 * 2 = 20" in out
