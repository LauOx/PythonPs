class Plant:
    def __init__(self, name:str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height

class Flower(Plant):
    def __init__(self, name, age, height, color: str):
        super().__init__(name, age, height)
        self.color = color
        self.is_bloom = False

    def bloom(self):
        if not self.is_bloom:
            self.is_bloom = True
            return f"{self.name} is blooming beautifully!"
        return f"{self.name} has already bloomed."
        

class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter: int):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter
        self.shade_produced = 0

    def produce_shade(self):
        shade = round(self.trunk_diameter * 1.56)
        return f"{self.name} provides {shade} square meters of shade"

class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

def main():
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    print("=== Garden Plant Types ===\n")
    print(f"{rose.name} ({type(rose).__name__}), {rose.height}cm, {rose.age} days, "
          f"{rose.color} color")
    print(f"{rose.bloom()}\n")
    print(f"{oak.name} ({type(oak).__name__}), {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    print(f"{oak.produce_shade()}\n")
    print(f"{tomato.name} ({type(tomato).__name__}), {tomato.height}cm, {tomato.age} days, "
          f"{tomato.harvest_season} harvest")
    print(f"Tomato is {tomato.nutritional_value}")

if __name__ == "__main__":
    main()