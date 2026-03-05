import sys

def command_quest() -> None:
    """
    
    """
    print("=== Command Quest ===")
    list_len = len(sys.argv)
    i = 1
    if list_len < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    if list_len >= 2:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments recived: {list_len - 1}")
        while i < list_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {list_len}\n")


if __name__ == "__main__":
    command_quest()