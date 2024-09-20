import platform
import urllib.request
import os
import sys
import shutil
import stat
import subprocess
import argparse
import re

ASSET_MAP = {
    ("Linux", "x86_64"): "tailwindcss-linux-x64",
    ("Linux", "arm64"): "tailwindcss-linux-arm64",
    ("Linux", "armv7l"): "tailwindcss-linux-armv7",
    ("Darwin", "x86_64"): "tailwindcss-macos-x64",
    ("Darwin", "arm64"): "tailwindcss-macos-arm64",
    ("Windows", "x86_64"): "tailwindcss-windows-x64.exe",
    ("Windows", "arm64"): "tailwindcss-windows-arm64.exe",
}

VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")

DEFAULT_VERSION = "latest"  # Use "latest" by default


def get_asset_filename():
    system = platform.system()
    machine = platform.machine().lower()

    key = (system, machine)
    filename = ASSET_MAP.get(key)

    if not filename:
        # Handle common aliases
        if system == "Darwin" and machine.startswith("arm"):
            filename = "tailwindcss-macos-arm64"
        elif system == "Linux" and machine.startswith("arm"):
            filename = "tailwindcss-linux-arm64"
        elif system == "Windows" and machine.startswith("arm"):
            filename = "tailwindcss-windows-arm64.exe"
        else:
            raise ValueError(f"Unsupported platform: {system} {machine}")

    return filename


def download_tailwind(filename, version, destination="tailwindcss", force=False):
    """
    Downloads the specified version of Tailwind CSS.

    Args:
        filename (str): The Tailwind CSS binary filename.
        version (str): The version of Tailwind CSS to download ("latest" or specific version).
        destination (str): The destination filename for the downloaded binary.
        force (bool): If True, force download even if the file exists.
    """
    if os.path.exists(destination) and not force:
        print(
            f"Tailwind CSS binary already exists as '{destination}'. Skipping download. Use --force to override. Or --help for more options."
        )
        return

    if version.lower() == "latest":
        version_path = "latest"
        url = f"https://github.com/tailwindlabs/tailwindcss/releases/{version_path}/download/{filename}"
    else:
        version_path = f"v{version}"
        url = f"https://github.com/tailwindlabs/tailwindcss/releases/download/{version_path}/{filename}"

    print(f'Downloading Tailwind CSS version "{version_path}" from {url}...')

    try:
        with urllib.request.urlopen(url) as response, open(
            destination, "wb"
        ) as out_file:
            shutil.copyfileobj(response, out_file)
    except urllib.error.HTTPError as e:
        print(f"Failed to download Tailwind CSS: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"URL Error while downloading Tailwind CSS: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while downloading Tailwind CSS: {e}", file=sys.stderr)
        sys.exit(1)

    if not filename.endswith(".exe"):
        # Make the binary executable
        try:
            st = os.stat(destination)
            os.chmod(destination, st.st_mode | stat.S_IEXEC)
        except Exception as e:
            print(f"Failed to make the binary executable: {e}", file=sys.stderr)
            sys.exit(1)

    print(
        f'Downloaded Tailwind CSS version "{version_path}" and saved as "{destination}"'
    )


def main():
    parser = argparse.ArgumentParser(description="Download Tailwind CSS binary.")
    parser.add_argument(
        "--version",
        type=str,
        default=DEFAULT_VERSION,
        help="Specify the Tailwind CSS version to download (e.g., '3.3.2'). Defaults to 'latest'.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force download even if the binary already exists.",
    )
    args = parser.parse_args()

    version = args.version
    force = args.force

    if version.lower() != "latest" and not VERSION_PATTERN.match(version):
        print(
            "Error: Invalid version format. Please use 'X.Y.Z' format, e.g., '3.3.2'.",
            file=sys.stderr,
        )
        sys.exit(1)

    filename = get_asset_filename()
    destination = "tailwindcss.exe" if filename.endswith(".exe") else "tailwindcss"

    download_tailwind(filename, version, destination, force=force)


def run_tailwind(*args):
    """
    Runs the Tailwind CSS binary from the current working directory if it exists.
    If the binary is not found, advises the user to download it.

    Args:
        *args: Arguments to pass to the Tailwind CSS binary.
    """
    # Determine the binary name based on the operating system
    binary = "tailwindcss.exe" if os.name == "nt" else "tailwindcss"
    binary_path = os.path.join(os.getcwd(), binary)

    if os.path.isfile(binary_path):
        try:
            # Execute the Tailwind CSS binary with the provided arguments
            subprocess.run([binary_path] + list(args), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Tailwind CSS: {e}", file=sys.stderr)
            sys.exit(e.returncode)
        except Exception as e:
            print(
                f"An unexpected error occurred while running Tailwind CSS: {e}",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        print(
            "Tailwind CSS binary not found in the current directory.\n"
            "Please download it by running:\n"
            "    poetry run download-tailwind [--version <desired-version>] [--force]"
        )
        sys.exit(1)
