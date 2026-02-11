#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES- VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    with open("classified_data.txt", "r") as f:
        print("Vault connection established with safe protocols")
        contenu = f.read()
        print("\nSECURE EXTRACTION:")
        print(contenu)
    with open("security_protocols.txt", "r") as w:
        print("\nSECURE PRESERVATION:")
        protocol = w.read()
        print(protocol)
        print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")
