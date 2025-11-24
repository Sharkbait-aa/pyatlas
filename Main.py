# main.py

from core.executor import run_snippet


def main() -> None:
    # For now, we just hardcode a test snippet.
    code = """nums = [5, 2, 9]
s = sorted(nums)
total = sum(s)
print("Total is", total)
"""

    success, stdout, stderr, variables, error_type, error_message = run_snippet(code)

    print("SUCCESS:", success)
    print("STDOUT:")
    print(stdout)
    print("STDERR:")
    print(stderr)
    print("VARIABLES:")
    for name, value in variables.items():
        print(f"  {name} = {value!r} (type: {type(value).__name__})")

    if not success:
        print("ERROR TYPE:", error_type)
        print("ERROR MESSAGE:", error_message)


if __name__ == "__main__":
    main()
