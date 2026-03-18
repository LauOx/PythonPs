#!/usr/bin/python3
import sys


def stream_check() -> None:
    """
    checks info output
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    # input check
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    # output check
    print(f"[STANDARD] Archive status from {id}: {status}")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_check()
