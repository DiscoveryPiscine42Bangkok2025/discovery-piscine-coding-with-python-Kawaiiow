import pytest
from pathlib import Path
from conftest import run_module
import importlib.util
import sys
import io

MODULE = "cell05.ex02.play_with_arrays"

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


def test_play_with_arrays_example_output(module_result):
    """Test that the program produces expected output with the example array"""
    result, _ = module_result
    result = run_module(MODULE)[0]

    assert result.returncode == 0
    
    output = result.stdout.strip()
    lines = output.split('\n')
    
    # The example shows:
    # Line 1: [2, 8, 9, 48, 8, 22, -12, 2]
    # Line 2: [10, 11, 50, 10, 24]  (only values > 5, with +2 added)
    
    # Check that both lines contain array-like output
    assert lines[0].startswith('[') and lines[0].endswith(']'), "First line should be an array"
    assert lines[1].startswith('[') and lines[1].endswith(']'), "Second line should be an array"


def test_play_with_arrays_uses_actual_arrays(module_result):
    """Ensure the student created array variables and applied filtering logic"""
    _, file_path = module_result
    
    # Convert to Path object
    file_path = Path(file_path)
    
    # Get the project root
    project_root = Path(__file__).parent.parent
    
    # Construct the full path to the module
    module_path = project_root / "cell05" / "ex02" / "play_with_arrays.py"
    
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
            f"Expected at least 2 list/array variables (original and filtered), "
            f"but found {len(student_lists)}. "
            "You must create both the original array and the new filtered array as variables."
        )
        
        # Check that we have arrays where filtering was applied correctly
        found_valid_pair = False
        for i, original in enumerate(student_lists):
            for j, filtered in enumerate(student_lists):
                if i != j and len(original) > 0:  # Original must have elements, filtered can be empty
                    # Check if filtered array contains only values from original that are > 5, with +2 added
                    # For each element in filtered, it should be original_element + 2 where original_element > 5
                    
                    # Get elements from original that are > 5
                    values_greater_than_5 = [x for x in original if x > 5]
                    expected_filtered = [x + 2 for x in values_greater_than_5]
                    
                    # The filtered array should match expected (can be empty if no values > 5)
                    if filtered == expected_filtered:
                        found_valid_pair = True
                        break
            if found_valid_pair:
                break
        
        assert found_valid_pair, (
            "Could not find two arrays where the second array contains only values > 5 "
            "from the first array, with 2 added to each. Make sure you're:\n"
            "1. Filtering values greater than 5\n"
            "2. Adding 2 to those filtered values\n"
            "3. Building a new array with the results\n"
            "Note: If no values are > 5, the result array should be empty []"
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
        'print("[2, 8, 9, 48, 8, 22, -12, 2]")',
        'print("[10, 11, 50, 10, 24]")',
        "print('[2, 8, 9, 48, 8, 22, -12, 2]')",
        "print('[10, 11, 50, 10, 24]')",
    ]
    
    for pattern in forbidden_patterns:
        assert pattern not in source, (
            "Do not hardcode the complete output string. "
            "Create the arrays as variables and print them dynamically."
        )


def test_play_with_arrays_has_filtering_logic(module_result):
    """Check that the student used conditional filtering"""
    _, file_path = module_result
    
    source = Path(file_path).read_text()
    
    # Look for conditional expressions that might indicate filtering
    has_if_statement = 'if ' in source
    has_comparison = '>' in source or '>=' in source
    has_filter_function = 'filter(' in source
    has_list_comprehension_with_if = '[' in source and 'for' in source and 'if' in source
    
    has_filtering_logic = (
        (has_if_statement and has_comparison) or 
        has_filter_function or 
        has_list_comprehension_with_if
    )
    
    assert has_filtering_logic, (
        "Your code should filter values from the array. "
        "Use a conditional (if > 5), filter() function, or list comprehension with condition."
    )


def test_play_with_arrays_correct_filtering(module_result):
    """Verify the filtering condition is > 5"""
    _, file_path = module_result
    
    # Convert to Path object
    file_path = Path(file_path)
    
    # Get the project root
    project_root = Path(__file__).parent.parent
    
    # Construct the full path to the module
    module_path = project_root / "cell05" / "ex02" / "play_with_arrays.py"
    
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
        
        # Try to find the original and filtered arrays
        # Original should have values <= 5 that don't appear in filtered
        # Filtered should only have values that were > 5 in original
        
        found_correct_filtering = False
        for original in student_lists:
            for filtered in student_lists:
                if original is not filtered and len(original) > 0:  # Filtered can be empty
                    # Check if filtered contains transformed values from original where original > 5
                    values_gt_5_from_original = [x for x in original if x > 5]
                    expected = [x + 2 for x in values_gt_5_from_original]
                    
                    if filtered == expected:
                        # If there are values <= 5, verify they're NOT in the filtered array
                        values_lte_5 = [x for x in original if x <= 5]
                        if len(values_lte_5) > 0 and len(filtered) > 0:
                            filtered_minus_2 = [x - 2 for x in filtered]  # Reverse the +2 operation
                            # None of the values <= 5 should appear in the reversed filtered array
                            no_small_values_included = all(v not in filtered_minus_2 for v in values_lte_5)
                            if no_small_values_included:
                                found_correct_filtering = True
                                break
                        else:
                            # Either no small values exist, or filtered is empty (both valid)
                            found_correct_filtering = True
                            break
            if found_correct_filtering:
                break
        
        assert found_correct_filtering, (
            "The filtering logic doesn't seem correct. Make sure you're only including "
            "values that are GREATER THAN 5 (not >= 5) from the original array. "
            "If no values are > 5, the result should be an empty array []."
        )
        
    finally:
        sys.stdout = old_stdout
        if parent_dir in sys.path:
            sys.path.remove(parent_dir)


def test_play_with_arrays_preserves_original(module_result):
    """Ensure original array is not modified"""
    _, file_path = module_result
    
    # Convert to Path object
    file_path = Path(file_path)
    
    # Get the project root
    project_root = Path(__file__).parent.parent
    
    # Construct the full path to the module
    module_path = project_root / "cell05" / "ex02" / "play_with_arrays.py"
    
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
        
        # Ensure arrays are different objects
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