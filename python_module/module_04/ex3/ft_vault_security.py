#!/usr/bin/env python3

"""Fourth exercise."""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES- VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    f = None
    try:
        with open("classified_data.txt", "r") as f:
            print("Vault connection established with safe protocols")
            contenu = f.read()
            print("\nSECURE EXTRACTION:")
            print(contenu)
    except FileNotFoundError:
        print("File not Found. 'classified_data.txt' needed")
    else:
        try:
            with open("security_protocols.txt", "w") as f:
                print("\nSECURE PRESERVATION:")
                f.write(contenu)
                print("[CLASSIFIED] New security protocols archived")
                print("Vault automatically sealed upon completion")
        except FileNotFoundError:
            print("File not Found.")

    print("\nAll vault operations completed with maximum security.")
