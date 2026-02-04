def ft_water_reminder() -> None:
    n: int = int(input("Days since last watering: "))
    if n > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
