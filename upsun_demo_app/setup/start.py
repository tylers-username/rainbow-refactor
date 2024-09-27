"""Module for launching app server"""

from .process_runner import run


def main():
    """Launches app server"""
    run("poetry run gunicorn upsun_demo_app.main:app", "Launching app server")
