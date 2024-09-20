# packages/tailwind/tailwind/cli.py

import platform
import urllib.request
import os
import sys
import shutil
import stat
import subprocess

ASSET_MAP = {
    ('Linux', 'x86_64'): 'tailwindcss-linux-x64',
    ('Linux', 'arm64'): 'tailwindcss-linux-arm64',
    ('Linux', 'armv7l'): 'tailwindcss-linux-armv7',
    ('Darwin', 'x86_64'): 'tailwindcss-macos-x64',
    ('Darwin', 'arm64'): 'tailwindcss-macos-arm64',
    ('Windows', 'x86_64'): 'tailwindcss-windows-x64.exe',
    ('Windows', 'arm64'): 'tailwindcss-windows-arm64.exe',
}

def get_asset_filename():
    system = platform.system()
    machine = platform.machine().lower()

    key = (system, machine)
    filename = ASSET_MAP.get(key)

    if not filename:
        # Handle common aliases
        if system == 'Darwin' and machine.startswith('arm'):
            filename = 'tailwindcss-macos-arm64'
        elif system == 'Linux' and machine.startswith('arm'):
            filename = 'tailwindcss-linux-arm64'
        elif system == 'Windows' and machine.startswith('arm'):
            filename = 'tailwindcss-windows-arm64.exe'
        else:
            raise ValueError(f'Unsupported platform: {system} {machine}')

    return filename

def download_tailwind(filename, destination='tailwindcss'):
    url = f'https://github.com/tailwindlabs/tailwindcss/releases/latest/download/{filename}'
    print(f'Downloading {filename} from {url}...')

    with urllib.request.urlopen(url) as response, open(destination, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    if not filename.endswith('.exe'):
        # Make the binary executable
        st = os.stat(destination)
        os.chmod(destination, st.st_mode | stat.S_IEXEC)

    print(f'Downloaded and saved as {destination}')

def main():
    try:
        filename = get_asset_filename()
        destination = 'tailwindcss.exe' if filename.endswith('.exe') else 'tailwindcss'
        download_tailwind(filename, destination)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

def run_tailwind(*args):
    """
    Runs the Tailwind CSS binary from the current working directory if it exists.
    If the binary is not found, advises the user to download it.

    Args:
        *args: Arguments to pass to the Tailwind CSS binary.
    """
    # Determine the binary name based on the operating system
    binary = 'tailwindcss.exe' if os.name == 'nt' else 'tailwindcss'
    binary_path = os.path.join(os.getcwd(), binary)

    if os.path.isfile(binary_path):
        try:
            # Execute the Tailwind CSS binary with the provided arguments
            subprocess.run([binary_path] + list(args), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Tailwind CSS: {e}", file=sys.stderr)
            sys.exit(e.returncode)
    else:
        print(
            "Tailwind CSS binary not found in the current directory.\n"
            "Please download it by running:\n"
            "    poetry run download-tailwind"
        )
        sys.exit(1)
