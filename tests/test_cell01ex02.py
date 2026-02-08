import pytest
from conftest import run_module

MODULE = "cell01.ex02.age"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_c1_ex02_age(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE)

    assert result.returncode == 0

    output = result.stdout.strip()
    # Output should be a number
    assert output.isdigit()
