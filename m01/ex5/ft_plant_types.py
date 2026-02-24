class Plant:
    def __init__(self, name:str, age: int, height: int) ->None
        self.name = name
        self.__age = 0
        self.__height = 0

    def set_height(self, new_heigh):
        if new_heigh < 0:
            print(f"Invalid operation attempted: height {new_heigh}cm [REJECED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_heigh
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

class Flower(Plant):
    def __init__(self, name, age, height, color: str):
        super().__init(name, age, height)
        self.color = color

    def bloom(self, bloom):
        bloom = false

class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter: int):
        super().__init(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(slef, trunk_diameter, shade):
        self.shade = trunk_diameter * 1.56

class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season):
        super().__init(name, age, height)
        self.harvest_season = harvest_season

    def nutritional_value(self, nutritional_value):
        self.nutritional_value = nutritional_value

def main():
    Rose = Flower("Rose", 25, 30, "red")
    Oak = Tree("Oak", 500, 1825, 50)
    Tomato = Vegetable("Tomato", 80, 90, "summer harvest")
    Rose.bloom = true
    Tomato.nutritional_value = "rich in vitamin C"