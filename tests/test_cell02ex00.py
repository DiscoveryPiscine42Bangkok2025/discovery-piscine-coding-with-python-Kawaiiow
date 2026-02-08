# test_c2_ex00_iszero.py
import pytest
from conftest import run_module

MODULE = "cell02.ex00.iszero"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_c2_ex00_iszero_nonzero(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "42\n")

    assert result.returncode == 0
    assert "different from zero" in result.stdout.lower()

def test_c2_ex00_iszero_zero(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE, "0\n")

    assert result.returncode == 0
    assert "equal to zero" in result.stdout.lower()
