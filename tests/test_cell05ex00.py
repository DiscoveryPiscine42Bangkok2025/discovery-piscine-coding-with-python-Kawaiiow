import pytest
from pathlib import Path
from conftest import run_module
import importlib.util
import sys
import io

MODULE = "cell05.ex00.create_array"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result

def test_create_array_behavior(module_result):
    result, _ = module_result
    result = run_module(MODULE)[0]

    assert result.returncode == 0
    output = result.stdout.strip()
    assert output == "[2, 8, 9, 48, 8, 22, -12, 2]"

def test_create_array_actually_uses_array(module_result):

    """Ensure the student actually created an array/list variable"""
    
    _, file_path = module_result
    
    file_path = Path(file_path)
    project_root = Path(__file__).parent.parent
    
    module_path = project_root / "cell05" / "ex00" / "create_array.py"
    
    assert module_path.exists(), f"Module file not found at {module_path}"
    
    spec = importlib.util.spec_from_file_location("student_module", module_path)
    module = importlib.util.module_from_spec(spec)
    
    parent_dir = str(module_path.parent)

    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:

        spec.loader.exec_module(module)
        sys.stdout = old_stdout
        
        has_list = any(isinstance(value, list) for value in module.__dict__.values())
        
        assert has_list, (
            "No list/array variable found in your program. "
            "You must create an array variable, not hardcode the print statement."
        )
        
        student_lists = [value for value in module.__dict__.values() if isinstance(value, list)]
        expected = [2, 8, 9, 48, 8, 22, -12, 2]
        
        assert any(lst == expected for lst in student_lists), (
            f"Found list(s) but none match expected values {expected}. "
            f"Found: {student_lists}"
        )
        
    finally:

        sys.stdout = old_stdout

        if parent_dir in sys.path:
            sys.path.remove(parent_dir)

def test_create_array_not_direct_print(module_result):

    """Ensure the student is not directly printing the string"""
    
    _, file_path = module_result

    source = Path(file_path).read_text()

    forbidden_list = [ 'print("[2, 8, 9, 48, 8, 22, -12, 2]")', 'print([2, 8, 9, 48, 8, 22, -12, 2])' ]

    for forbidden in forbidden_list:
        assert forbidden not in source, (
            "Do not directly print the array string. "
            "Create the array first, then print it."
        )