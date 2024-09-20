"""Module for launching app server"""

from .process_runner import run


def main():
    """Launches app server"""
    run("poetry run gunicorn main:app", "Launching app server")
