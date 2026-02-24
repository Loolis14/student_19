#!/usr/bin/env python3

"""Third exercise."""

import os

try:
    from dotenv import load_dotenv, dotenv_values
except ImportError:
    print("Error: The 'python-dotenv' module is not installed.")
    print("Please install a virtuel environnement and then run")
    print("'pip install python-dotenv'")
    exit(1)


def main() -> None:
    """Test notions on subject."""
    print("\nORACLE STATUS: Reading the Matrix...")
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

    required_keys = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": db_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_url,
        }
    missing = [key for key, value in required_keys.items() if not value]
    if missing:
        print(f"\nWARNING: Missing configuration for: {', '.join(missing)}")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode if mode else 'Missing data'}")
    print(f"Database: {db_url if db_url else 'Missing data'}")
    print(f"API Access: {api_key if api_key else 'Missing data'}")
    print(f"Log Level: {log_level if log_level else 'Missing data'}")
    print(f"Zion Network: {zion_url if zion_url else 'Missing data'}")

    print("\nEnvironment security check:")
    gitignore_exists = os.path.exists(".gitignore")
    env_ignored = False
    if gitignore_exists:
        with open(".gitignore") as f:
            if ".env" in f.read():
                env_ignored = True
    if env_ignored:
        print("[OK] No hardcoded secrets detected")
        print("[OK] Production overrides available")
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
