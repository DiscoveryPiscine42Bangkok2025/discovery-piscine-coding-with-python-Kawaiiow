import pytest
from conftest import run_module

MODULE = "cell02.ex02.password"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_password_denied(module_result):
    result, _ = module_result
    result = run_module(MODULE, "1234\n")[0]

    assert result.returncode == 0
    assert "ACCESS DENIED" in result.stdout

def test_password_granted(module_result):
    result, _ = module_result
    result = run_module(MODULE, "Python is awesome\n")[0]

    assert result.returncode == 0
    assert "ACCESS GRANTED" in result.stdout
