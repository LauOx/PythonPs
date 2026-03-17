#!/usr/bin/env python3


def create_file(data: list) -> None:
    """
    creates a new file and writes items in data
    divided by '\n'
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    new_file = "new_discovery.txt"
    error = False
    print(f"Initializing new storage unit: {new_file}")
    try:
        open(new_file, 'x')
        print("storage unit created successfully...\n")
        with open(new_file, 'w') as file:
            print("Inscribing preservation data...")
            i = 1
            for line in data:
                file.write(f"{line}\n")
                print(f"[ENTRY {i:03d}] {line}")
                i += 1
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        error = False
    except FileExistsError:
        print(f"\nERROR: The file {new_file} already exist.")
        error = True     
    if not error:
        print(f"Archive '{new_file}' ready for long-term preservation.")
    elif error:
        print(f"An error occurred while creating the file {new_file}")


if __name__ == "__main__":
    data = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]
    create_file(data)
