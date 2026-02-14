#!/usr/bin/env python3

"""Fifth exercise."""


if __name__ == "__main__":
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===\n")
    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as f:
            f.read()
            print("SUCCESS: Archive recovered")
    except Exception as e:
        print(f"You failed! {e}")
    finally:
        print("STATUS: Normal operations resumed")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
