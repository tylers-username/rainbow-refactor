"""Module for ensuring our app code is pretty"""

from .process_runner import run_multiple


def main():
    """Installs dependencies then runs pylint"""

    commands = [
        {"message": "Installing dependencies", "command": "poetry install"},
        {
            "message": "Checking if code is pretty",
            "command": "poetry run black . --diff --color --check",
        },
    ]

    run_multiple(commands)
