"""Runs shell commands and exits if a non-zero code is provided."""

import subprocess
import sys


def run(command, message=None, exit_on_fail=True):
    """
    Print a message and execute a shell command.
    Exit the script if the command fails and exit_on_fail is True.

    :param command: The shell command to execute.
    :param message: Optional message to display before running the command.
                    Defaults to "Running: {command}" if not provided.
    :param exit_on_fail: Whether to exit the script if the command fails.
    """

    if message is None:
        message = f"Running: {command}"

    print(message)

    try:
        result = subprocess.run(command, shell=True, check=False)
    except: # pylint: disable=bare-except
        sys.exit(1)

    if result.returncode != 0:
        if exit_on_fail:
            sys.exit(result.returncode)


def run_multiple(commands):
    """
    Iterate over a list of command dictionaries and execute each command.

    :param commands: List of dictionaries with keys:
         - "command" (str): The shell command to execute.
         - "message" (str, optional): Message to display before running the command.
         - "exit_on_fail" (bool, optional): Whether to exit if the command fails.
    """

    for cmd in commands:
        command = cmd.get("command")
        if not command:
            print("Error: Command not specified in:", cmd)
            sys.exit(1)

        message = cmd.get("message")
        exit_on_fail = cmd.get("exit_on_fail", True)

        run(command, message, exit_on_fail)
