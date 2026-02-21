#!/usr/bin/env python3
"""
Install a virtuel environnement and execute:
'pip install python-dotenv'
• Demonstrates different configuration for development : pour faire des tests
/production : deploie l'appli et tout est suppose etre sur
• Shows how to keep secrets secure
"""
import os
from dotenv import load_dotenv, dotenv_values


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    if not load_dotenv():
        print(
            "Missing .env file.\n\nExample of a configuration:\n"
            "MATRIX_MODE='development' or 'production'\n"
            "DATABASE_URL= <insert your database url>\n"
            "API_KEY= <enter your API key>\n"
            "LOG_LEVEL= <log level print>\n"
            "ZION_ENDPOINT= <zion adress>\n"
            )
        return

    config = dotenv_values()
    mode = os.getenv("MATRIX_MODE") or config.get("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL") or config.get("DATABASE_URL")
    api_key = os.getenv("API_KEY") or config.get("API_KEY")
    log_level = os.getenv("LOG_LEVEL") or config.get("LOG_LEVEL")
    zion_url = os.getenv("ZION_ENDPOINT") or config.get("ZION_ENDPOINT")

    required_keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    missing = [key for key in required_keys if not config.get(key) or config.get(key).strip() == ""]
    if missing:
        print(f"WARNING: Missing configuration for: {', '.join(missing)}")
    
    print("\nConfiguration loaded:")
    print(f"Mode: {mode if mode else 'Missing data'}")
    print(f"Database: {db_url if db_url else 'Missing data'}")
    print(f"API Access: {api_key if api_key else 'Missing data'}")
    print(f"Log Level: {log_level if log_level else 'Missing data'}")
    print(f"Zion Network: {zion_url if zion_url else 'Missing data'}")

    print("\nEnvironment security check:")

    # Vérification simple si .env est dans .gitignore
    gitignore_exists = os.path.exists(".gitignore")
    env_ignored = False
    if gitignore_exists:
        with open(".gitignore") as f:
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

"""
Configuration loaded:
Mode: development
Database: Connected to local instance
API Access: Authenticated
Log Level: DEBUG
Zion Network: Online
Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available
The Oracle sees all configurations.
"""
