#!/usr/bin/env python3

"""First exercise."""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file}")
    f = None
    try:
        f = open(file, "r")
        print("Connection established...")
        contenu = f.read()
        print(f"\nRECOVERED DATA:\n{contenu}")
        f.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        if f and f.closed:
            print("\nData recovery complete. Storage unit disconnected.")
