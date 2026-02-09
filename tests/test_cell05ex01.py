import pytest
from pathlib import Path
from conftest import run_module
import importlib.util
import sys
import io

MODULE = "cell05.ex01.play_with_arrays"

@pytest.fixture
def module_result():
    result = run_module(MODULE)
    assert result[0] is not None, "Required file doesn't exist"
    return result


def test_play_with_arrays_behavior(module_result):
    """Test that the program runs and produces correct output format"""
    result, _ = module_result
    result = run_module(MODULE)[0]

    assert result.returncode == 0, "Program should execute without errors"
    
    output = result.stdout.strip()
    lines = output.split('\n')
    
    assert len(lines) == 2, "Output should have exactly 2 lines"
    assert lines[0].startswith("Original array:"), "First line should start with 'Original array:'"
    assert lines[1].startswith("New array:"), "Second line should start with 'New array:'"


def test_play_with_arrays_correct_output(module_result):
    """Test that the program produces the expected output with example array"""
    result, _ = module_result
    result = run_module(MODULE)[0]

    assert result.returncode == 0
    
    output = result.stdout.strip()
    
    # Check if it contains the expected arrays (accounting for possible variations)
    # The expected output should show original and new array with +2 to each element
    assert "Original array:" in output
    assert "New array:" in output


def test_play_with_arrays_uses_actual_arrays(module_result):
    """Ensure the student actually created array variables, not hardcoded prints"""
    _, file_path = module_result
    
    # Convert to Path object
    file_path = Path(file_path)
    
    # Get the project root
    project_root = Path(__file__).parent.parent
    
    # Construct the full path to the module
    module_path = project_root / "cell05" / "ex01" / "play_with_arrays.py"
    
    # Fallback to using the provided file_path if it exists
    if not module_path.exists() and file_path.exists():
        module_path = file_path
    
    assert module_path.exists(), f"Module file not found at {module_path}"
    
    # Load the module dynamically
    spec = importlib.util.spec_from_file_location("student_module", module_path)
    module = importlib.util.module_from_spec(spec)
    
    # Temporarily add the parent directory to sys.path
    parent_dir = str(module_path.parent)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    # Capture stdout to prevent print statements during import
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        spec.loader.exec_module(module)
        sys.stdout = old_stdout
        
        # Find all list variables in the module
        student_lists = [value for value in module.__dict__.values() if isinstance(value, list)]
        
        assert len(student_lists) >= 2, (
            f"Expected at least 2 list/array variables (original and new), "
            f"but found {len(student_lists)}. "
            "You must create both the original array and the new array as variables."
        )
        
        # Check that we have at least one pair where second = first + 2 for each element
        found_valid_pair = False
        for i, arr1 in enumerate(student_lists):
            for j, arr2 in enumerate(student_lists):
                if i != j and len(arr1) == len(arr2):
                    # Check if arr2 is arr1 with each element +2
                    if all(arr2[k] == arr1[k] + 2 for k in range(len(arr1))):
                        found_valid_pair = True
                        break
            if found_valid_pair:
                break
            
        assert found_valid_pair, (
            "Could not find two arrays where the second array is the first array "
            "with 2 added to each element. Make sure you're correctly iterating "
            "and building the new array by adding 2 to each value."
        )
        
    finally:
        sys.stdout = old_stdout
        # Clean up sys.path
        if parent_dir in sys.path:
            sys.path.remove(parent_dir)


def test_play_with_arrays_not_hardcoded(module_result):
    """Ensure the student didn't hardcode the output strings"""
    _, file_path = module_result
    
    source = Path(file_path).read_text()
    
    # Check for common hardcoded patterns
    forbidden_patterns = [
        'print("Original array: [2, 8, 9, 48, 8, 22, -12, 2]")',
        'print("New array: [4, 10, 11, 50, 10, 24, -10, 4]")',
        "print('Original array: [2, 8, 9, 48, 8, 22, -12, 2]')",
        "print('New array: [4, 10, 11, 50, 10, 24, -10, 4]')",
    ]
    
    for pattern in forbidden_patterns:
        assert pattern not in source, (
            "Do not hardcode the complete output string. "
            "Create the arrays as variables and print them dynamically."
        )


def test_play_with_arrays_has_iteration(module_result):
    """Check that the student used some form of iteration"""
    _, file_path = module_result
    
    source = Path(file_path).read_text()
    
    # Look for common iteration patterns
    has_for_loop = 'for ' in source
    has_while_loop = 'while ' in source
    has_list_comprehension = '[' in source and 'for' in source and 'in' in source
    has_map = 'map(' in source
    
    assert (has_for_loop or has_while_loop or has_list_comprehension or has_map), (
        "Your code should iterate over the original array. "
        "Use a for loop, while loop, list comprehension, or map() function."
    )


def test_play_with_arrays_preserves_original(module_result):
    """Ensure both arrays exist and original is not modified"""
    _, file_path = module_result
    
    # Convert to Path object
    file_path = Path(file_path)
    
    # Get the project root
    project_root = Path(__file__).parent.parent
    
    # Construct the full path to the module
    module_path = project_root / "cell05" / "ex01" / "play_with_arrays.py"
    
    # Fallback to using the provided file_path if it exists
    if not module_path.exists() and file_path.exists():
        module_path = file_path
    
    assert module_path.exists(), f"Module file not found at {module_path}"
    
    # Load the module dynamically
    spec = importlib.util.spec_from_file_location("student_module", module_path)
    module = importlib.util.module_from_spec(spec)
    
    # Temporarily add the parent directory to sys.path
    parent_dir = str(module_path.parent)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        spec.loader.exec_module(module)
        sys.stdout = old_stdout
        
        # Find all list variables
        student_lists = [value for value in module.__dict__.values() if isinstance(value, list)]
        
        # Check that we have at least 2 distinct arrays
        assert len(student_lists) >= 2, "Should have at least 2 array variables"
        
        # Ensure arrays are different (not the same object)
        unique_lists = []
        for lst in student_lists:
            if not any(lst is existing for existing in unique_lists):
                unique_lists.append(lst)
        
        assert len(unique_lists) >= 2, (
            "You should have two separate arrays. "
            "Don't modify the original array; create a new one."
        )
        
    finally:
        sys.stdout = old_stdout
        if parent_dir in sys.path:
            sys.path.remove(parent_dir)
