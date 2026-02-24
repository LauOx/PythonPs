class Plant:
    def __init__(self, name: str, height: str, age: str):
        self.name = name
        self.height = height
        self.age = age
    
    def grow(self, days: int):
        self.age += days - 1 
        self.height += days - 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        

def main():
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Day 1 ===")
    day = 1
    start = garden[0].height
    garden[0].get_info()
    print("=== Day 7 ===")
    day = 7
    garden[0].grow(day)
    garden[0].get_info()
    end = garden[0].height
    total = end - start
    print(f"Growth this week: +{total}cm")


if __name__ == "__main__":
    main()