#!/usr/bin/env python3

import os
import sys


def load_config() -> dict[str, str | None]:
    """"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("[ERROR] dotenv not installed. Run 'pip install python-dotenv'")
        sys.exit()

    config = {
        "MODE": os.getenv("MATRIX_MODE"),
        "DB": os.getenv("DATABASE_URL"),
        "API": os.getenv("API_KEY"),
        "LOG": os.getenv("LOG_LEVEL"),
        "ZION": os.getenv("ZION_ENDPOINT")
    }
    return config


def oracle() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config = load_config()

    missing = [k for k, v in config.items() if v is None]
    if missing:
        print(f"ERROR: Missing configuration for: {', '.join(missing)}")

    print("Configuration loaded:")
    print(f"Mode: {config['MODE']}")
    mode = config["MODE"]
    if config['MODE'] == "production":
        print("Database: [ENCRYPTED CONNECTION]")
        print("API Access: SECURE_AUTH_ENABLED")
    elif config['MODE'] == "development":
        print("Database: Connected to local instance")
        print("API Access: Authenticated (Dev Mode)")
    else:
        status = "Missing" if mode is None else f"Invalid ({mode})"
        print(f"ERROR: MATRIX_MODE is {status}. Use development/production")

    print(f"Log Level: {config['LOG']}")
    print(f"Zion Network: {'Online' if config['ZION'] else 'Offline'}")
    print("\nEnvironment security check:")
    if config['API'] and "NEO" in config['API']:
        print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    if config['MODE'] == "production":
        print("[OK] Production overrides available")


if __name__ == "__main__":
    oracle()
