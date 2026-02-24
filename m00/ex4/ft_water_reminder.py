def ft_water_reminder() -> None:
    limit = 2
    last = int(input("Days since last watering: "))
    if last > limit:
        print("Water the plants!")
    if last <= limit:
        print("Plants are fine")
