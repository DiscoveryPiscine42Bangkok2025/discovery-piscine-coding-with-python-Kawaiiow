# tests/test_cell04_ex05.py
import pytest
from conftest import run_module

MODULE = "cell04.ex05.up_low"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_up_low_simple(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "Hello World\n")
    assert "hELLO wORLD" in result.stdout

def test_up_low_mixed(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "aaaaAAAA\n")
    assert "AAAAaaaa" in result.stdout

def test_up_low_with_numbers(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "hello 42\n")
    assert "HELLO 42" in result.stdout
