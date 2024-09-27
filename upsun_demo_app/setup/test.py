"""Module for testing app code"""

from .process_runner import run_multiple


def main():
    """Installs dependencies and then runs pip-audit for tests"""

    commands = [
        {"message": "Installing dependencies", "command": "poetry install"},
        {
            "message": "Testing",
            "command": "poetry run pip-audit",
        },
    ]

    run_multiple(commands)
