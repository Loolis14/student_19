#!/usr/bin/env python3

class Plant:
    """
    a class to define plant
    """
    def __init__(self, name: str, height: int, day_old: int) -> None:
        """
        Initialize of a plant
        Args: name, height and age
        """
        self.name = name
        self.height = height
        self.day_old = day_old

    def grow(self, growth: int, time: int) -> None:
        """
        add a height for the time given

        Args:
            growth (int): height taken per day
            time (int): number of days
        """
        self.height += growth * time

    def age(self, time: int) -> None:
        """
        add the number of day that passed

        Args:
            time (int): number of days
        """
        self.day_old += time

    def get_info(self) -> None:
        """Print info of the plant"""
        print(f"{self.name}: {self.height}cm, {self.day_old} days old")


def ft_plant_growth(plant, time: int, growth: int) -> None:
    """
    function to use class and his methods

    Args:
        plant (Plant): instance of plant
        time (int): time passed
        growth (int): height taken per days
    """
    plant.grow(growth, time)
    plant.age(time)
    plant.get_info()
    if growth > 0:
        print(f"Growth this week: +{growth * time}cm")


if __name__ == "__main__":
    print("=== Day 1 ===")
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    ft_plant_growth(rose, 0, 0)
    ft_plant_growth(sunflower, 0, 0)
    ft_plant_growth(cactus, 0, 0)
    time: int = 7
    print(f"=== Day {time} ===")
    ft_plant_growth(rose, time - 1, 4)
    ft_plant_growth(sunflower, time - 1, 10)
    ft_plant_growth(cactus, time - 1, 1)
