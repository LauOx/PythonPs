class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self.__age = age
    
    def set_height(self, new_heigh):
        if new_heigh < 0:
            print(f"Invalid operation attempted: height {new_heigh}cm [REJECED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_heigh
            print(f"Plant created: {self.name}")
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Plant created: {self.name}")
            print(f"Age updated: {self._age} days [OK]")

def main():
    Rose = SecurePlant("Rose", 25, 30)
    Oak = SecurePlant("Oak", 200, 365)
    Cactus = SecurePlant("Cactus", 5, 90)
    Sunflower = SecurePlant("Sunflower", 80, 45)
    Fern = SecurePlant("Fern", 15, 120)
    garden = [Rose, Oak, Cactus, Sunflower, Fern]
    Rose.set_height(6)
    Rose.set_age(6)


if __name__ == "__main__":
    main()

    #### hay que hacer la suma de los datos antes y despues?