import pytest
from conftest import run_module

MODULE = "cell03.ex01.multiplication_table"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_table_of_2(module_result):
    result, _ = module_result
    result = run_module(MODULE, "2\n")[0]
    lines = result.stdout.strip().splitlines()

    assert result.returncode == 0
    assert lines[1].strip() == "1 x 2 = 2"
    assert lines[-1].strip() == "9 x 2 = 18"
    assert len(lines) == 10

def test_table_of_0(module_result):
    result, _ = module_result
    result = run_module(MODULE, "0\n")[0]
    lines = result.stdout.strip().splitlines()

    assert all("= 0" in line for line in lines)
    assert len(lines) == 10

def test_table_of_5_contains_expected_value(module_result):
    result, _ = module_result
    result = run_module(MODULE, "5\n")[0]

    output = result.stdout
    assert "4 x 5 = 20" in output
    assert "9 x 5 = 45" in output
