"""Module for copying .env.sample to .env"""

from .process_runner import run


def main():
    """Copies .env.sample to .env."""
    run("cp .env.sample .env", "Copying .env.sample to .env")
