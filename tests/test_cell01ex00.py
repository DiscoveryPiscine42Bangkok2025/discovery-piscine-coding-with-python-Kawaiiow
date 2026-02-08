from conftest import run_module
import pytest

MODULE = "cell01.ex00.name"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_c1_ex00_name(module_result):
    result, _ = module_result
    result, _ = run_module(MODULE)

    assert result.returncode == 0
    assert len(result.stdout.strip()) > 0
