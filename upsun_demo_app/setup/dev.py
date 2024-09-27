"""Various dev tasks"""

from .process_runner import run


def cssWatch():
    """Continuously compiles Tailwind to CSS"""
    run(
        "poetry run tailwindcss -i ./upsun_demo_app/static/css/tailwind.css -o ./upsun_demo_app/static/css/main.css --watch",
        "Watching for changes",
    )
