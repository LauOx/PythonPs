class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0

    def plant_created(self):
        """
        Este método es solo para mostrar que la plata se ha creado.
        """
        return f"Plant created: {self.name}"
    
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

def main():
    Rose = SecurePlant("Rose", 25, 30)
    print(Rose.plant_created())
    Rose.set_height(25)
    Rose.set_age(30)
    print(f"Current plant: {Rose.name} ({Rose.get_height()}cm, {Rose.get_age()} days)")
    #print(f"Altura de {Rose.name}: {Rose.__age}") # esta escondido, solo se puede llamar con get.

if __name__ == "__main__":
    main()