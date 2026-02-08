import pytest
from conftest import run_module

MODULE = "cell03.ex02.i_got_that"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_i_got_that_basic(module_result):
    result, _ = module_result
    inp = "Hello\nSTOP\n"
    result, _ = run_module(MODULE, inp)

    assert result.returncode == 0
    assert "I got that!" in result.stdout
