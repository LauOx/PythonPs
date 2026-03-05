class Plant:
    def __init__(self, name) -> None:
        """
        Inits Plant with name
        """
        self.name = name


def water_plants(plant_list: list) -> None:
    """
    Function that activates the watering system
    """
    open = False
    error = False
    if not open:
        open = True
        print("Opening watering system")
    try:
        for plant in plant_list:
            print(f"Watering {plant.name}")
    except AttributeError:
        error = True
        print("Error: cannot water None - invalid plant!")
    finally:
        if open:
            open = False
        print("Closing watering system (cleanup)")
        if not error:
            print("Watering completed successfully!\n")


def watering_test() -> None:
    """
    Function to test the watering system water_plants()
    """
    print("=== Garden Watering System ===\n")
    tomato = Plant("tomato")
    lettuce = Plant("lettuce")
    carrots = Plant("carrots")
    plant_list = [tomato, lettuce, carrots]
    error_plant_list = [tomato, None, lettuce]
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Testing with error...")
    water_plants(error_plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    """
    The main function
    """
    watering_test()
