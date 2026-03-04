class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes plant object with name, height and age
        """
        self.name = name
        self.age = age
        self.height = height

    def info(self) -> str:
        """
        Gests info from plant
        """
        str = (
            f"{self.name} ({type(self).__name__}), {self.height}cm, "
            f"{self.age} days"
            )
        return str


class Flower(Plant):
    def __init__(self, name: str, age: int, height: int, color: str) -> None:
        """
        Initializes flower object with data inherited from Plant
        plus color
        """
        super().__init__(name, age, height)
        self.color = color
        self.is_bloom = False

    def bloom(self) -> str:
        """
        Changes is_bloom status
        """
        if not self.is_bloom:
            self.is_bloom = True
            return f"{self.name} is blooming beautifully!"
        return f"{self.name} has already bloomed."

    def info(self) -> str:
        """
        Gests info from flower
        """
        str = f"{super().info()} {self.color} color\n{self.bloom()}"
        return str


class Tree(Plant):
    def __init__(self, name: str, age: int,
                 height: int, trunk_diameter: int) -> None:
        """
        Initializes Tree object with data inherited from Plant
        plus trunk_diameter
        """
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter
        self.shade_produced = 0

    def produce_shade(self) -> str:
        """
        Calculates shade produced by the tree
        """
        shade = round(self.trunk_diameter * 1.56)
        return f"{self.name} provides {shade} square meters of shade"

    def info(self) -> str:
        """
        Gests info from tree
        """
        str = (f"{super().info()} {self.trunk_diameter}"
        f"\n{self.produce_shade()}")
        return str


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initializes vegetable object with data inherited from Plant
        plus harvest_season and nutritional_value
        """
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> str:
        """
        Gests info from vegetable
        """
        str = (
            f"{super().info()} {self.harvest_season}\n"
            f"{self.name} is {self.nutritional_value}"
            )
        return str


def main() -> None:
    """
    Runs as main function
    """
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    print("=== Garden Plant Types ===\n")
    print(f"{rose.info()}\n")
    # print(f"{rose.name} ({type(rose).__name__}), {rose.height}cm, "
    #       f"{rose.age} days, {rose.color} color")
    # print(f"{rose.bloom()}\n")
    print(f"{oak.info()}\n")
    # print(f"{oak.name} ({type(oak).__name__}), {oak.height}cm, "
    #       f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    # print(f"{oak.produce_shade()}\n")
    print(f"{tomato.info()}")
    # print(f"{tomato.name} ({type(tomato).__name__}), {tomato.height}cm, "
    #       f"{tomato.age} days, {tomato.harvest_season} harvest")
    # print(f"Tomato is {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
