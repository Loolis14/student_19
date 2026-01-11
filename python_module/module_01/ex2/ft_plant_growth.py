#!/usr/bin/env python3

class Plant:
    """
    a class to define plant
    """
    def __init__(self, name, height, day_old):
        self.name = name
        self.height = height
        self.day_old = day_old

    def grow(self, growth, time):
        self.height += growth * time

    def age(self, time):
        self.day_old += time

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.day_old} days old")


def ft_plant_growth(plant, time, growth):
    """
    function to use class and his methods
    """
    plant.grow(growth, time)
    plant.age(time)
    plant.get_info()
    if growth > 0:
        print(f"Growth this week: +{growth * time}cm")


if __name__ == "__main__":
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    ft_plant_growth(rose, 0, 0)
    ft_plant_growth(sunflower, 0, 0)
    ft_plant_growth(cactus, 0, 0)
    time = 7
    print(f"=== Day {time} ===")
    ft_plant_growth(rose, time - 1, 4)
    ft_plant_growth(sunflower, time - 1, 10)
    ft_plant_growth(cactus, time - 1, 1)
