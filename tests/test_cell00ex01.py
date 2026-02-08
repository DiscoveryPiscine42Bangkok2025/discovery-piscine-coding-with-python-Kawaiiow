"""test 42.py"""

import pytest
from conftest import run_module

MODULE = "cell00.ex01.42"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_print42(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE)

    assert result.returncode == 0
    assert "42" in result.stdout
