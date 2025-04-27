import shutil
import sys

def run_checks():
    missing = []

    if shutil.which("clang-format") is None:
        missing.append("clang-format")
    if shutil.which("cmake-format") is None:
        missing.append("cmake-format")

    if missing:
        print("Missing system requirements:")
        for item in missing:
            print(f"  - {item}")
        sys.exit(1)
    else:
        print("All checks passed.")
