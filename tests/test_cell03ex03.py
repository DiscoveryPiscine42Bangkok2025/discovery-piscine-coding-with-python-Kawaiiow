import pytest
from conftest import run_module

MODULE = "cell03.ex03.advanced_mult"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_advanced_mult_no_args(module_result):
    result, _ = module_result
    result = run_module(MODULE)[0]

    lines = [l for l in result.stdout.splitlines() if l.strip()]
    assert result.returncode == 0
    assert len(lines) >= 11   # tables 0–10

def test_advanced_mult_contains_table_0(module_result):
    result, _ = module_result
    result = run_module(MODULE)[0]

    assert "Table de 0" in result.stdout

def test_advanced_mult_contains_table_10(module_result):
    result, _ = module_result
    result = run_module(MODULE)[0]

    assert "Table de 10" in result.stdout
    assert "100" in result.stdout  # 10 x 10 = 100 somewhere in output

def test_advanced_mult_with_argument_gives_none(module_result):
    # some students print "none" when an argument is provided
    result, _ = module_result
    result = run_module(MODULE, "")[0]

    if "none" in result.stdout.lower():
        assert True
    else:
        # alternative acceptable behavior: still prints tables
        assert "Table de 0" in result.stdout
