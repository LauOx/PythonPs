class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_bloom = False

    def bloom(self):
        if not self.is_bloom:
            self.is_bloom = True
            return f"{self.name} is blooming beautifully!"
        return f"{self.name} has already bloomed."
    

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color):
        super().__init__(name, height, color)
        self.points = 0

    def prize_points(self):
        """
        las flores con premio, consiguen los puntos cuando crecen
        """
        if self.name == "Sunflower" and self.height > 0:
            self.points = 10

class GardenManager:
    def __init__(self):
        self.garden_list = {}

    def add_garden(self, garden):
        """
        Este método añade jardines al diccionario
        """
        name = garden.owner
        # Guarda el jardín que entre con la clave [name]
        self.garden_list[name] = garden

    def create_garden_network(self, garden_list):
        """
        Este método debería hacer un network de jardines
        """
    
class GardenStats(GardenManager):
    """
    Calcula métricas sobre los jardines gestionados
    """
    

class Garden:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.plants_list = []

    def add_plant(self, plant):
        self.plants_list.append(plant) # append se usa para agregar a la lista de plantas en garden


def main():
    sunflower = PrizeFlower("Sunflower", 51, "yellow")
    AliceGarden = Garden("Alice")
    AliceGarden.add_plant(sunflower)


if __name__ == "__main__":
    main()