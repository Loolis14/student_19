#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES- PRESERVATION SYSTEM ===\n")
    file = "new_discovery.txt"
    print(f"Initializing new storage unit: {file}")
    try:
        f = open(file, "w")
        f.write("quantum algorithm breakthrough !!\n")
        f.write("performance improvement metrics (347%_ efficiency gain)\n")
        f.write("Archived by mmeurer trainee")
        print("Storage unit created successfully...")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier: {e}")
    try:
        f = open(file, "r")
        contenu = f.readlines()
        print("\nInscribing preservation data...")
        entry = 1
        for line in contenu:
            line = line.rstrip("\n")
            print(f"[ENTRY 00{entry}] {line}")
            entry += 1
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    finally:
        f.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file}' ready for long-term preservation.")
