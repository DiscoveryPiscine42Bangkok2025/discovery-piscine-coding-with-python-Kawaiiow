# tests/test_cell04_ex03.py
import pytest
from conftest import run_module

MODULE = "cell04.ex03.float"

# @pytest.mark.skipif(
#     run_module(MODULE)[0] is None,
#     reason="Required file does not exist"
# )

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_float_integer(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "42\n")
    assert "integer" in result.stdout.lower()

def test_float_decimal(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "42.42\n")
    assert "decimal" in result.stdout.lower()
