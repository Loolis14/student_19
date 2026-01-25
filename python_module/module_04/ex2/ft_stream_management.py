#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES- COMMUNICATION SYSTEM ===\n")
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {id}: {status}", file=sys.stdout)
    print("[ALERT]  System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.")
