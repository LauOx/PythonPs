def garden_operations(error_str: str) -> None:
    """
    Executes comands to verify errors
    """
    if error_str == "value":
        int("abc")
    elif error_str == "zero":
        1 / 0
    elif error_str == "file":
        open("missing.txt", "r")
    elif error_str == "key":
        dic = {"Oak": 1}
        return dic["rose"]
    

def test_error_types() -> None:
    """
    Test garden operations erros
    """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing\_plant'\n")
    print("Testing KeyError...")
    try:
        garden_operations("key")
        garden_operations("file")# Once "key" executes jumps directly to except.
        garden_operations("value")
    except (KeyError, FileNotFoundError, ValueError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfuly!")


if __name__ == "__main__":
    """
    This is the main function
    """
    test_error_types()