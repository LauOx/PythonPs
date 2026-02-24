class Plant:
    def __init__(self, name: str, height: str, age: str):
        self.name = name
        self.height = height
        self.age = age


def main():
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in garden:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()