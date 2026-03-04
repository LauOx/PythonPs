def check_plant_health(name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Checks data on plant and Raises errors
    """
    if not name:
        raise ValueError("Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level}"
                         "is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} "
                         "is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         " is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         " is too low (2 min)")
    else:
        print(f"Plant '{name}' is healthy!")


def test_plant_checks() -> None:
    """
    Test the check_plant_health function
    """
    print("=== Garden Plant Health Checker ===\n")
    # Testing with all correct values
    print("Testing good values...")
    check_plant_health("tomato", 5, 5)
    print()
    # Testing with name error
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}\n")
    # Testing with bad water level
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}\n")
    # Testing with bad sunlight hours
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}\n")
    print("All error tests completed!")


if __name__ == "__main__":
    """
    The main function
    """
    test_plant_checks()
