#!/usr/bin/env python3

def arch_reader(filename: str) -> None:
    """
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accesing Storage Vault: {filename}")
    try:
        with open(filename, 'r') as file:
            print("Connection established...")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    arch_reader('archivo.txt')