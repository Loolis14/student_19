#!/usr/bin/env python3

class Plant:
    """Definie la classe parentale plante"""
    def __init__(self, name, height, day_old):
        self.name = name
        self.height = height
        self.day_old = day_old

    def __str__(self):
        return f"{self.height}cm, {self.day_old} days"


class Flower(Plant):
    """Definie la classe enfant des fleurs"""
    def __init__(self, name, height, day_old, color):
        super().__init__(name, height, day_old)
        self.color = color

    def __str__(self):
        parent_str = super().__str__()
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{parent_str}, {self.color} color"
        )

    def bloom(self):
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    """Definie la classe enfant des arbres"""
    def __init__(self, name, height, day_old, trunk_diameter):
        super().__init__(name, height, day_old)
        self.trunk_diameter = trunk_diameter

    def __str__(self):
        parent = super().__str__()
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{parent}, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self, ares):
        return f"{self.name} provides {ares} square meters of shade"


class Vegetables(Plant):
    """Definie la classe enfant des legumes"""
    def __init__(
        self, name, height, day_old, harvest_season, nutritional_value
    ):
        super().__init__(name, height, day_old)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self):
        parent = super().__str__()
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{parent}, {self.harvest_season} harvest"
        )

    def nutritional(self):
        return f"{self.name} is rich in {self.nutritional_value}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    beautiful = Flower.bloom(rose)
    oak = Tree("Oak", 500, 1825, 50)
    shadow = Tree.produce_shade(oak, 78)
    tomato = Vegetables("Tomato", 80, 90, "summer", "vitamin C")
    provide = Vegetables.nutritional(tomato)
    print(rose)
    print(beautiful)
    print()
    print(oak)
    print(shadow)
    print()
    print(tomato)
    print(provide)
