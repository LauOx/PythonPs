#!/usr/bin/env python3


def arch_reader(filename: str) -> None:
    """
    opens and reads files in the same folder
    """
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accesing Storage Vault: {filename}")
    file = None
    # checks if the file exist
    try:
        file = open(filename, 'r')
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        if file is not None:
            file.close()
        print("\nData recovery complete. Storage unit disconnected")
        # print(file.closed)


if __name__ == "__main__":
    arch_reader('ancient_fragment.txt')
