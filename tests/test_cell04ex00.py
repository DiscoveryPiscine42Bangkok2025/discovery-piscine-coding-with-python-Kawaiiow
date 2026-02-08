"""test upcase_it"""

import pytest
from conftest import run_module

MODULE = "cell04.ex00.upcase_it"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Require file doesn't exist"
    return result
@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Hello\n", "HELLO"),                 # basic
        ("hello world\n", "HELLO WORLD"),     # spaces
        ("hello 123\n", "HELLO 123"),         # digits unchanged
        ("hello, world!\n", "HELLO, WORLD!"), # special characters
        ("hElLo WoRlD\n", "HELLO WORLD"),     # mixed case
        ("42\n", "42"),                       # only numbers
    ],
)
def test_upcase_it(inp, expected):
    result, _ = run_module(MODULE, inp)

    assert result.returncode == 0
    assert expected in result.stdout.strip("\n")
