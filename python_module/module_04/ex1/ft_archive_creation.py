#!/usr/bin/env python3

"""Second exercise."""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file = "new_discovery.txt"
    print(f"Initializing new storage unit: {file}")
    f = None
    try:
        f = open(file, "w")
        f.write("[ENTRY 001] quantum algorithm breakthrough !!\n")
        f.write("[ENTRY 002] performance improvement metrics"
                "(347%_ efficiency gain)\n")
        f.write("[ENTRY 003] Archived by mmeurer trainee")
        print("Storage unit created successfully...")
        f.close()
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier: {e}")

    try:
        print("\nInscribing preservation data...")
        f = open(file, "r")
        content = f.read()
        print(content, end="")
        print()
        f.close()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    finally:
        if f and f.closed:
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{file}' ready for long-term preservation.")
