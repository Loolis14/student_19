#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES- DATA RECOVERY SYSTEM ===\n")
    file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file}")
    try:
        f = open(f'../{file}', "r")
        print("Connection established...")
        contenu = f.read()
        print(f"\nRECOVERED DATA:\n{contenu}")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    finally:
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
