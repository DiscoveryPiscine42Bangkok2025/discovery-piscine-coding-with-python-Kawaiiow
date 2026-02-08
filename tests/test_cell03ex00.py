import pytest
from conftest import run_module

MODULE = "cell03.ex00.to25"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_to25_normal_range(module_result):
    result, _ = module_result
    result = run_module(MODULE, "20\n")[0]

    output = result.stdout.strip().splitlines()

    assert result.returncode == 0
    assert output[0].strip() == "Inside the loop, my variable is 20"
    assert output[2].strip() == "Inside the loop, my variable is 22"
    assert output[-1].strip() == "Inside the loop, my variable is 25"

def test_to25_exact_25(module_result):
    result, _ = module_result
    result = run_module(MODULE, "25\n")[0]

    output = result.stdout.strip().splitlines()
    assert len(output) == 1
    assert output[0].strip() == "Inside the loop, my variable is 25"

def test_to25_error_when_above_25(module_result):
    result, _ = module_result
    result = run_module(MODULE, "45\n")[0]

    assert result.returncode == 0
    assert "Error" in result.stdout
