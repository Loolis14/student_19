#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as f:
            f.read()
    except (PermissionError, FileNotFoundError):
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")

    try:
        print(
            "\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("../standard_archive.txt", "r") as f:
            f.read()
            print("SUCCESS: Archive recovered")
    except Exception:
        print("You failed!")
    finally:
        print("STATUS: Normal operations resumed")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
