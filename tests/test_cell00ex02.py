"""test hello_world.py"""

import pytest
from conftest import run_module

MODULE = "cell00.ex02.hello_world"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result

def test_hello_wolrd(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE)

    assert result.returncode == 0
    assert "Hello World\n" == result.stdout
