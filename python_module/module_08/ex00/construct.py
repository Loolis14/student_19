#!/usr/bin/env python3

"""First exercise."""

import sys
import os
import site


def venv_not_activated() -> None:
    """Run scripts if no venv is activate."""
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate     # On Windows")
    print("\nThen run this program again.")


def venv_activated() -> None:
    """Run scripts if a venv is activated."""
    venv_root = sys.prefix
    venv_name = os.path.basename(venv_root)
    site_packages = site.getsitepackages()[0]

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_root}")
    print("\nSUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting the global system.\n")
    print(f"Package installation path:\n {site_packages}")


def is_venv() -> bool:
    """Check if the program runs on a venv."""
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    if is_venv():
        venv_activated()
    else:
        venv_not_activated()
