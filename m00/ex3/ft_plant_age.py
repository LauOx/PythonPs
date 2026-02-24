def ft_plant_age() -> None:
    limit = 60
    age = int(input("Enter plant age in days: "))
    if age > limit:
        print("Plant is ready to harvest!")
    if age <= limit:
        print("Plant needs more time to grow")
