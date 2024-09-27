"""Module for copying .env.sample to .env"""

from .process_runner import run


def main():
    """Copies .env.sample to .env."""
    run("cp .env.sample .env", "Copying .env.sample to .env")
    run(
        "poetry run download-tailwind --version 3.4.12",
        "Downloading tailwind if needed",
    )
    run(
        "poetry run tailwindcss -i ./upsun_demo_app/static/css/tailwind.css -o ./upsun_demo_app/static/css/main.css --minify",
        "Building production CSS",
    )
