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


def test_plant_error(plant: str, status: str) -> None:
    """
    Checks the plant status
    """
    if status == "wilting":
        raise PlantError(f"The {plant} plant is {status}!")


def test_water_error(amount: int) -> None:
    """
    Checks amount of water
    """
    if amount < 5:
        raise WaterError("Not enough water in the tank")


def garden_error_demo() -> None:
    """
    Executes the test and checks for errors
    """
    print("=== Custom Garden Errors Demo ===\n")
    # PlantError
    print("Testing PlantError...")
    try:
        test_plant_error("Tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    # WaterError
    print("Testing WaterError...")
    try:
        test_water_error(3)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    # GardenError
    print("Testing catching all garden errors...")
    try:
        test_plant_error("Tomato", "wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        test_water_error(3)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    garden_error_demo()
