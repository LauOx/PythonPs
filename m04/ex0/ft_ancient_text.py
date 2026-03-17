#!/usr/bin/env python3


def arch_reader(filename: str) -> None:
    """
    opens and reads files in the same folder
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accesing Storage Vault: {filename}")
    # checks if the file exist
    try:
        archive = open(filename, 'r')
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(archive.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        archive.close()
        print("Data recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    arch_reader('ancient_fragment.txt')
