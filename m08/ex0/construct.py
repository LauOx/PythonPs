#!/bin/usr/env python3

import sys
import os
import site


def detect_environment() -> bool:
    """"""
    if os.getenv('VIRTUAL_ENV'):
        return True
    return False


def env_status() -> None:
    """"""
    if not detect_environment():
        print("\nMATRIX STATUS: You're still plugged in\n")
        print("Current python:", sys.executable)
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment! "
              "\nThe machines can see everything you install.\n")
        print("To enter the construct, run:\n"
              "python3 -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
    else:
        exe = sys.executable
        e_path = os.getenv('VIRTUAL_ENV') or ""
        v_env = os.path.basename(e_path)
        f_pack = site.getsitepackages()
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print("Current python:", exe)
        print("Virtual Environment:", v_env)
        print("Environment Path:", e_path)
        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.")
        print("Package installation path:", f_pack[0])


if __name__ == "__main__":
    env_status()
