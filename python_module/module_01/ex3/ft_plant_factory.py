#!/usr/bin/env python3

from typing import List, Tuple


class Plant:
    """
    class for each plant
    """
    def __init__(self, name: str, height: int, day_old: int) -> None:
        """
        Initialize of a plant
        Args: name, height and age
        """
        self.name: str = name
        self.height: int = height
        self.day_old: int = day_old

    def __str__(self) -> str:
        """Returns Plant info"""
        return f"{self.name} ({self.height}cm, {self.day_old} days)"


def ft_plant_factory(data: List[Tuple[str, int, int]]) -> List[Plant]:
    """
    Function to create plant
    """
    plants_created: List = []
    for name, height, age in data:
        seed: Plant = Plant(name, height, age)
        print("Created:", seed)
        plants_created.append(seed)
    return plants_created


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    data: List = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    plants_created: List = ft_plant_factory(data)
    print(f"\nTotal plants created: {len(plants_created)}")
