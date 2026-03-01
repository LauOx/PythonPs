class GardenError(Exception):
    """
    Basic error for garden problems
    """
    pass

class PlantError(GardenError):
    """
    Error for problems with plants
    """
    pass

class WaterError(GardenError):
    """
    Error for problems with watering
    """
    pass


def garden_error_demo() ->None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")   
    try:
        raise GardenError("The tomato plant is wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise GardenError("Not enough water in the tank")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


if __name__ == "__main__":
    garden_error_demo()