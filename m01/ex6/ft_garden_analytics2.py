class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def validate_height(self) ->bool:
        return self.height > 0


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_bloom = False

    def bloom(self):
        """Makes the FloweringPLant blooms"""
        if not self.is_bloom:
            self.is_bloom = True
            return f"{self.name} is blooming beautifully!"
        return f"{self.name} has already bloomed."
    

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color):
        super().__init__(name, height, color)
        self.points = 0

    def prize_points(self):
        """The FloweringPlant gets points when it grows"""
        if self.name == "Sunflower" and self.height > 0:
            self.points = 10


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plant_list = []

    def add_plant(self, plant):
        """Adds plant to the plant_list (with append)"""
        self.plant_list.append(plant) # append is used to add smt to a list
        print(f"Added {plant.name} to {self.owner}'s garden")

class GardenManager:
    def __init__(self):
        self.my_gardens = {}
        self.general_growth = 0

    def add_garden(self, garden: str) ->None:
        """Adds gardens to the dictionary my_gardens"""
        name = garden.owner # the 'key' word is the name of the garden
                            # that comes from the owner's name
        self.my_gardens[name] = garden # "in the dictionary, with this name, save the garden that entered as parameter"

    def grow_all_plants(self, garden: str, cm: int) ->None:
        """Makes all the plants in all the gardens grow"""
        print(f"{garden.owner} is helping all plants grow...")
        for name in self.my_gardens:
            for plant in self.my_gardens[name].plant_list:
                plant.height += cm
                print(f"{plant.name} grew {cm}cm")
                self.general_growth += 1
    
    @classmethod
    def create_garden_network(cls):
        """creates a manager with gardens added"""
        network = cls() # creates new instance "GardenManager" named
        return network


class GardenStats:
    """This is a GardenManager nested class that helps with statistics
    doesn't need __init__ because no instances are going to be created"""
    @staticmethod
    def total_plants(garden) -> int:
        """Counts total plants in given garden"""
        i = 0
        for plant in garden.plant_list:
            i += 1
        return i
    
    @staticmethod
    def total_growth(garden) ->int:
        """Sums height of all plants in given garden"""
        i = 0
        for plant in garden.plant_list:
            i += plant.height
        return i
    
    @staticmethod
    def plant_types(garden):
        """Gives quantity and type of plants in given garden"""
        counts = {"Plant":0, "FloweringPlant":0, "PrizeFlower":0} #dictionary with exact name of plant types
        for plant in garden.plant_list:
            counts[type(plant).__name__] += 1 #if class name matches dictionary item, adds 1
        return counts #returns the dictionar


def main():
    """runs as main function"""
    print("=== Garden Management System Demo ===\n")
    alice = Garden("Alice")
    bob = Garden("Bob")
    network = GardenManager.create_garden_network()
    network.add_garden(alice)
    network.add_garden(bob)
    rose = FloweringPlant("Rose", 25, "red")
    oak = Plant("Oak Tree", 100)
    Sunflower = PrizeFlower("Sunflower", 50, "yellow")
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(Sunflower)
    print()
    network.grow_all_plants(alice, 1)




if __name__ == "__main__":
    main()
    
                

    
