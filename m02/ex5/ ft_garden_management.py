class GardenError(Exception):
    """General garden error"""
    pass


class WaterError(GardenError):
    """Basic water error"""
    pass


class SunlightError(GardenError):
    """Basic sunlight error"""
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        """
        Initializes a Plant object
        """
        self.name = name
        self.water_level = water
        self.sun_hours = sun

    def photosynthesis(self, hr: int) -> None:
        """
        Exposes plant to sun
        """
        self.sun_hours += hr


class Garden:
    def __init__(self, name: str) -> None:
        """
        Initializes garden with name
        """
        self.name = name
        self.plant_list = []
        self.tank_level = 0

    def add_plant(self, plant: Plant) -> None:
        """
        adds plant to garden
        """
        if not plant.name:
            raise GardenError("Plant name cannot be empty!")
        else:
            self.plant_list.append(plant)
        print(f"Added {plant.name} successfully")

    def add_water_tank(self, lt: int) -> None:
        """
        checks and adds water to the garden tank
        """
        total = self.tank_level + lt
        if total > 50:
            print(f"Error: Adding {lt}lts to tank would exced the tank limit")
        if total < 50:
            self.tank_level += total


class GardenManager:

    @staticmethod
    def water_plants(garden: Garden, lt: int) -> None:
        """
        Waters all plants in the garden
        """
        is_open = False
        if not is_open:
            is_open = True
            if garden.tank_level > lt:
                print("Opening watering system")
                for plant in garden.plant_list:
                    plant.water_level += lt
                    print(f"Watering {plant.name} - success")
                    garden.tank_level -= lt
            else:
                raise GardenError("Not enought water in the tank")
        if is_open:
            is_open = False

    @staticmethod
    def photosynthesis(plant_list: list, hr: int) -> int:
        """
        Make plants take sunbaths (one at day)
        """
        for plant in plant_list:
            plant.sun_hours += hr

    @staticmethod
    def check_plant_health(plant: Plant) -> None:
        """
        Checks data on plant and Raises errors
        """
        if plant.water_level > 10:
            raise WaterError(f"Water level {plant.water_level} "
                             "is too high (max 10)")
        elif plant.water_level < 1:
            raise WaterError(f"Water level {plant.water_level} "
                             "is too low (min 1)")
        elif plant.sun_hours > 12:
            raise SunlightError(f"Sunlight hours {plant.sunlight_hours} "
                                " is too high (max 12)")
        elif plant.sun_hours < 2:
            raise SunlightError(f"Sunlight hours {plant.sunlight_hours} "
                                " is too low (2 min)")
        else:
            print(f"{plant.name} healthy "
                  f"(water: {plant.water_level}, sun {plant.sun_hours})")


def test_garden_manager() -> None:
    """
    Test the function of the Garden and plants
    """
    print("=== Garden Management System ===\n")
    my_garden = Garden("My garden")
    tomato = Plant("tomato", 2, 5)
    lettuce = Plant("lettuce", 12, 5)
    other = Plant("", 0, 0)
    # Adding plants to garden
    print("Adding plants to garden...")
    try:
        my_garden.add_plant(tomato)
        my_garden.add_plant(lettuce)
        my_garden.add_plant(other)
    except GardenError as e:
        print(f"Error adding plant: {e}\n")
    # Watering plants
    print("Watering plants...")
    my_garden.tank_level = 20
    try:
        GardenManager.water_plants(my_garden, 3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("Closing watering system (cleanup)")
    # doing photosynthesis
    GardenManager.photosynthesis(my_garden.plant_list, 3)
    # doing photosynthesis
    print()
    # Check plants health
    print("Checking plant health...")
    try:
        for plant in my_garden.plant_list:
            GardenManager.check_plant_health(plant)
    except GardenError as e:
        print(f"Error checking {plant.name}: {e}\n")
    # Testing error not enought water in the tank
    print("Testing error recovery...")
    my_garden.tank_level = 2
    try:
        GardenManager.water_plants(my_garden, 3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    """
    main function
    """
    test_garden_manager()
