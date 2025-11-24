# core/executor.py

import io
import traceback
from contextlib import redirect_stdout, redirect_stderr
from typing import Dict, Any, Tuple, Optional


def run_snippet(code: str) -> Tuple[bool, str, str, Dict[str, Any], Optional[str], Optional[str]]:
    """
    Run a block of Python code and capture:
      - success (True/False)
      - stdout (printed output)
      - stderr (errors / traceback)
      - variables (final values of user-defined variables)
      - error_type (e.g. 'TypeError')
      - error_message (string message)

    This is the core of your practice lab.
    """
    # Where we'll store variables created by the user's code
    local_env: Dict[str, Any] = {}

    # Buffers to capture printed output and errors
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()

    success = True
    error_type: Optional[str] = None
    error_message: Optional[str] = None

    try:
        # Redirect print() and error output into our buffers
        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            # Execute the code in an empty global env and our local_env
            exec(code, {}, local_env)
    except Exception as e:
        success = False
        error_type = e.__class__.__name__
        error_message = str(e)
        # Capture the full traceback into stderr
        traceback.print_exc(file=stderr_buffer)

    stdout = stdout_buffer.getvalue()
    stderr = stderr_buffer.getvalue()

    # Filter out internal names like __builtins__
    variables = {
        name: value
        for name, value in local_env.items()
        if not name.startswith("__")
    }

    return success, stdout, stderr, variables, error_type, error_message
