#!/usr/bin/env python3

import os
# from python-dotenv import load_dotenv


def main():
    # 1. Charger le fichier .env s'il existe
    # load_dotenv()
    # si le fichier existe pas : pip install python-dotenv

    print("ORACLE STATUS: Reading the Matrix...")

    # 2. Récupération des variables avec gestion d'erreurs
    # On utilise os.getenv() pour éviter
    # que le script crash si une variable manque
    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT")

    missing = [
        var for var in ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
        if not os.getenv(var)]
    if missing:
        print(f"WARNING: Missing configuration for: {', '.join(missing)}")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(
        f"Database: "
        f"{'Connected to local instance'
           if 'localhost' in (db_url or '')
           else 'Connected to remote instance'}"
           )
    print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_url else 'Offline'}")

    print("\nEnvironment security check:")

    # Vérification simple si .env est dans .gitignore
    gitignore_exists = os.path.exists(".gitignore")
    env_ignored = False
    if gitignore_exists:
        with open(".gitignore", "r") as f:
            if ".env" in f.read():
                env_ignored = True

    print(f"[{'OK' if env_ignored else '!!'}] "
          ".env file properly configured in gitignore")
    print(f"[{'OK' if api_key != 'your_secret_key_here' else '!!'}]"
          "No hardcoded secrets detected")
    print(
        f"[{'OK' if mode == 'production' or os.path.exists('.env') else '??'}]"
        "Production overrides available")


if __name__ == "__main__":
    main()
