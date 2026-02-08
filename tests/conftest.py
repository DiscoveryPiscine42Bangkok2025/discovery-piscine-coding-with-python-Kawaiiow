from pathlib import Path
import subprocess
import sys

def run_module(module: str, input_text: str = ""):
    file_path = Path(f"{module.replace('.', '/')}.py")

    if not file_path.exists():
        return None, file_path

    result = subprocess.run(
        [sys.executable, "-m", module],
        input=input_text,
        text=True,
        capture_output=True,
    )
    return result, file_path
