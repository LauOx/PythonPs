from typing import Dict


class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.last_growth = 0

    def validate_height(self) -> bool:
        return self.height > 0


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_bloom = False

    def bloom(self) -> str:
        """
        Makes the FloweringPLant blooms
        """
        if not self.is_bloom:
            self.is_bloom = True
            return f"{self.name} is blooming beautifully!"
        return f"{self.name} has already bloomed."


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height, color)
        self.points = 0

    def prize_points(self) -> None:
        """
        The FloweringPlant gets points when it blooms
        """
        if self.is_bloom:
            self.points = 10


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plant_list = []
        self.score = 0

    def add_plant(self, plant):
        """
        Adds plant to the plant_list (with append)
        """
        self.plant_list.append(plant)  # append is used to add smt to a list
        self.score = self.sum_points()

    def sum_points(self) -> int:
        total = 0
        for plant in self.plant_list:
            total += plant.height
            total += 10
            if isinstance(plant, PrizeFlower):
                if plant.is_bloom:
                    total += plant.points
        self.score = total  # saves final result in object
        return total        # gives total if needed

    def update_score(self) -> int:
        self.score = self.sum_points()
        return self.score


class GardenManager:
    def __init__(self):
        self.my_gardens = {}
        self.count = 0

    def add_garden(self, garden: str) -> None:
        """
        Adds gardens to the dictionary my_gardens
        """
        name = garden.owner
        self.my_gardens[name] = garden
        self.count += 1

    def grow_all_plants(self, garden: str, cm: int) -> None:
        """
        Makes all the plants in the garden grow
        """
        print(f"{garden.owner} is helping all plants grow...")
        for plant in garden.plant_list:
            plant.height += cm
            plant.last_growth += cm
            print(f"{plant.name} grew {cm}cm")
        garden.update_score()

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        creates a manager with gardens added
        """
        network = cls()
        return network


class GardenStats:
    """
    This is a GardenManager nested class that helps with statistics
    doesn't need __init__ because no instances are going to be created
    """

    @staticmethod
    def total_plants(garden) -> int:
        """
        Counts total plants in given garden
        """
        i = 0
        for plant in garden.plant_list:
            i += 1
        return i

    @staticmethod
    def total_growth(garden) -> int:
        """
        Sums height of all plants in given garden
        """
        i = 0
        for plant in garden.plant_list:
            i += plant.last_growth
        return i

    @staticmethod
    def plant_types(garden) -> Dict[str, int]:
        """
        Gives quantity and type of plants in given garden:
        count = dictionary with exact name of plant types
        if class name matches dictionary item, adds 1
        """
        counts = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
        for plant in garden.plant_list:
            counts[type(plant).__name__] += 1
        return counts

    @staticmethod
    def garden_report(garden) -> None:
        print(f"=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plant_list:
            if isinstance(plant, PrizeFlower):
                bloom_status = "blooming" if plant.is_bloom else "not blooming"
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers ({bloom_status}),"
                      f"Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                bloom_status = "blooming" if plant.is_bloom else "not blooming"
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers ({bloom_status})")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        t_plants = GardenStats.total_plants(garden)
        t_growth = GardenStats.total_growth(garden)
        print(f"\nPlants added: {t_plants}, Total growth: {t_growth}")
        plant_counts = GardenStats.plant_types(garden)
        print(f"Plant types: "
              f"{plant_counts['Plant']} regular, "
              f"{plant_counts['FloweringPlant']} flowering, "
              f"{plant_counts['PrizeFlower']} prize flowers")


def main() -> None:
    """Runs as main function"""
    print("=== Garden Management System Demo ===\n")
    # create gardens
    alice = Garden("Alice")
    bob = Garden("Bob")
    # create network and add gardens to network
    network = GardenManager.create_garden_network()
    network.add_garden(alice)
    network.add_garden(bob)
    # create all flowers
    rose = FloweringPlant("Rose", 25, "red")
    oak = Plant("Oak Tree", 100)
    sunflower = PrizeFlower("Sunflower", 50, "yellow")
    jasmine = FloweringPlant("Jasmine", 26, "white")
    orchid = PrizeFlower("Orchid", 36, "lilac")
    # add and bloom plants to Bob's garden
    orchid.bloom()
    orchid.prize_points()
    bob.add_plant(jasmine)
    bob.add_plant(orchid)
    # add and bloom plants to Alice's garden
    rose.bloom()
    sunflower.bloom()
    sunflower.prize_points()
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    # Print plants added to Alice's garden
    for plant in alice.plant_list:
        print(f"Added {plant.name} to Alice's garden")
    print()
    # grow Alice's plants 1cm each
    network.grow_all_plants(alice, 1)
    print()
    # garden stats and validatios
    GardenStats.garden_report(alice)
    print()
    print(f"Height validation test: {rose.validate_height()}")
    print(f"Garden scores - Alice: {alice.update_score()}, "
          f"Bob: {bob.update_score()}")
    print(f"Total gardens managed: {network.count}")


if __name__ == "__main__":
    main()
