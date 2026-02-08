# tests/test_cell04_ex04.py
import pytest
from conftest import run_module

MODULE = "cell04.ex04.round_up"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_round_up_basic(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "41.42\n")
    assert result.stdout.split(" ")[-1].strip("\n") == "42"

def test_round_up_small(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "0.001\n")
    assert result.stdout.split(" ")[-1].strip("\n") == "1"
