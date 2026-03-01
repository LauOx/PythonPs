class Plant:
    """
    Class to create plants
    """
    def __init__(self, name):
        self.name = name

def water_plants(plant_list: list) ->None:
    """
    function that activates the watering system
    """
    open = False
    if not open:
        open = True
        print("Opening watering system")
    try:
        for plant in plant_list:
            print(f"Watering {plant.name}")
    except AttributeError:
        print("Error: cannot water None - invalid plant")
    if open:
        open = False
        print("Closing watering system (cleanup)")

def watering_test():
    """
    Function to test the watering system water_plants()
    """
    tomato = Plant("tomato")
    lettuce = Plant("lettuce")
    carrots = Plant("carrots")
    plant_list = [tomato, lettuce, carrots]
    error_plant_list = [tomato, None, lettuce]
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(error_plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    """
    The main function
    """
    watering_test()
