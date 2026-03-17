#!/usr/bin/python3

def vault_protocol() -> None:
    """
    checks vault security protocol
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_name = "security_protocols.txt"
    print("Initiating secure vault access...")
    try:
        # extraction
        with open(file_name, 'r') as file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            extraction = file.read()
            line = ""
            for c in extraction:
                if c != '\n':
                    line += c
                else:
                    print(f"[CLASSIFIED] {line}")
                    line = ""
            if line != "":
                print(f"[CLASSIFIED] {line}")
        # preservation
        with open(file_name, 'w') as file:
            print("\nSECURE PRESERVATION:")
            preservation = "New security protocols archived"
            file.write(preservation)
            print(f"[CLASSIFIED] {preservation}")
    except FileNotFoundError:
        print(f"ERROR: {file_name} doesn't exist")
    finally: 
        print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_protocol()