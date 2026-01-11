#!/usr/bin/env python3

class Plant:
    """
    class for each plant
    """
    def __init__(self, name, height, day_old):
        self.name = name
        self.height = height
        self.day_old = day_old

    def __str__(self):
        return f"{self.name} ({self.height}cm, {self.day_old} days)"


def ft_plant_factory(data):
    """
    Function to create plant
    """
    plants_created = []
    for name, height, age in data:
        seed = Plant(name, height, age)
        print("Created:", seed)
        plants_created.append(seed)
    return plants_created


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    plants_created = ft_plant_factory(data)
    print(f"\nTotal plants created: {len(plants_created)}")
