#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent


def main():
    manage = ROOT / "manage.py"
    argv = sys.argv
    cmd = []
    if len(argv) == 1:
        cmd = ["-h"]
    else:
        cmd = argv[1:]
    if cmd[0] == "start":
        subprocess.run(
            ["gunicorn", "cosapp_creator.wsgi:application"] + cmd[1:], cwd=str(ROOT)
        )
    else:
        subprocess.run(["python", manage] + cmd)


if __name__ == "__main__":
    main()
