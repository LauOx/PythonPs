class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes plant object with name, height and age
        """
        self.name = name
        self.__height = 0
        self.__age = 0

    def plant_created(self) -> str:
        """
        This method just shows a mesage
        """
        return f"Plant created: {self.name}"

    def set_height(self, new_heigh: int) -> None:
        """
        Sets and checks new plant's height
        """
        if new_heigh < 0:
            print(f"Invalid operation attempted:"
                  f"height {new_heigh}cm [REJECED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_heigh
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """
        Sets and checks new plant's age
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        """
        Secure way to get to plant.height
        """
        return self.__height

    def get_age(self) -> int:
        """
        Secure way to get to plant.age
        """
        return self.__age


def main() -> None:
    """
    Runs as main function
    """
    print("=== Garden Security System ===")
    Rose = SecurePlant("Rose", 25, 30)
    print(Rose.plant_created())
    Rose.set_height(25)
    Rose.set_age(30)
    print()
    Rose.set_height(-5)
    print()
    print(f"Current plant: {Rose.name} ({Rose.get_height()}cm, "
          f"{Rose.get_age()} days)")
    # print(f"Altura de {Rose.name}: {Rose.__age}") is hidden
    # its reacheable with 'get'.


if __name__ == "__main__":
    main()
