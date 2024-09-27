"""Module for linting our app code"""

from .process_runner import run_multiple


def main():
    """Installs dependencies then runs pylint"""
    commands = [
        {"message": "Installing dependencies", "command": "poetry install"},
        {"message": "Linting code", "command": "poetry run pylint **/*.py"},
    ]

    run_multiple(commands)
