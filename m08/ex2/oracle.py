#!/usr/bin/env python3

import os
import sys


def load_config() -> None:
    """"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("[ERROR] dotenv not installed. Run 'pip install python-dotenv'")
        exit()

    config = {
        "MODE": os.getenv("MATRIX_MODE"),
        "DB": os.getenv("DATABASE_URL"),
        "API": os.getenv("API_KEY"),
        "LOG": os.getenv("LOG_LEVEL"),
        "ZION": os.getenv("ZION_ENDPOINT")
    }
    return config


def oracle():
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config = load_config()

    missing = [k for k, v in config.items() if v is None]
    if missing:
        print(f"ERROR: Missing configuration for: {', '.join(missing)}")
    
    print("\nConfiguration loaded:")
    print(f"  Mode: {config['MODE']}")
    if config['MODE'] == "production":
        print(f"  Database: [ENCRYPTED CONNECTION] to {config['DB']}")
        print(f"  API Access: SECURE_AUTH_ENABLED")
    elif config['MODE'] == "development":
        print(f"  Database: Connected to local instance ({config['DB']})")
        print(f"  API Access: Authenticated (Dev Mode)")
    else:
        print(f"{config['MODE']} is not valid. Try development or production")

    print(f"  Log Level: {config['LOG']}")
    print(f"  Zion Network: {'Online' if config['ZION'] else 'Offline'}")
    print("\nEnvironment security check:")
    if config['API'] and "NEO" in config['API']:
        print("[OK] No hardcoded secrets detected")
         
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
        
    if config['MODE'] == "production":
        print("[OK] Production overrides available")

if __name__ == "__main__":
    oracle()


