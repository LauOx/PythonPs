def ft_count_harvest_recursive(i=1, day=None) -> None:
    if day is None:
        day = int(input("Days until harvest: "))
    if i > day:
        print("Harvest time!")
        return
    print(f"Day {i}")
    ft_count_harvest_recursive(i + 1, day)
