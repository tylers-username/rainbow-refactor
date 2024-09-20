"""Module for cleaning up python environment"""

from .process_runner import run_multiple


def main():
    """Resets Poetry and Python env as well as .env"""

    commands = [
        {"message": "Removing Python env...", "command": "poetry env remove python"},
        {"message": "Removing env/", "command": "rm -rf env/"},
        {"message": "Removing .env", "command": "rm -f .env"},
    ]

    run_multiple(commands)
