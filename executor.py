import subprocess
import sys

def run_python_code(code):
    """Executes python code and returns the output or error."""
    try:
        # We run the code as a separate process for basic isolation
        process = subprocess.Popen(
            [sys.executable, "-c", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(timeout=10) # 10 second safety timeout
        
        if stderr:
            return f"Error:\n{stderr}"
        return stdout
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out (10s limit)."
    except Exception as e:
        return str(e)
