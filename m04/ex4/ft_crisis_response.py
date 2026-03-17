#!/usr/bin/python3

def crisis_response() ->None:
    """
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    # lost archive crisis
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open('lost_archive.txt') as file:
            print(file.read())
    except FileNotFoundError:
        print("STATUS: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    # permission crisis
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open('classified_vault.txt') as file:
            file.write('hello')
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")    
    # standar archive
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open('standard_archive.txt') as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("STATUS: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")


FALTA VERIFICAR SI EL DE ARCHIVO SIN PERMISO O CORRUPTO SIRVE Y VERIFICAR SI
PUEDO USAR BLOQUE FINALLY PARA LOS 3 TRY


if __name__ == "__main__":
    crisis_response()