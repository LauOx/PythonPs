class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes plant object with name, height and age
        """
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self) -> str:
        """
        This method just show a message
        """
        return f"created: {self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    """
    Runs as main function
    Here is where the object is created
    """
    garden = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    num = 0
    print("=== Plant Factory Output ===")
    for plant in garden:
        print(plant.print_plant())
        num += 1
    print(f"\nTotal plants created: {num}")


if __name__ == "__main__":
    main()
