#!/usr/bin/env python3

class Plant:
    """Base class for all plants in the garden."""
    def __init__(self, name: str, height: int, day_old: int) -> None:
        """
        Initialize of a Plant
        Args: name, height and age
        """
        self.name: str = name
        self.height: int = height
        self.day_old: int = day_old

    def __str__(self) -> str:
        """Returns Plant info as a string"""
        return f"{self.height}cm, {self.day_old} days"


class Flower(Plant):
    """Represents a flower with a color and ability to bloom."""
    def __init__(self, name: str, height: int,
                 day_old: int, color: str) -> None:
        """
        Initialize of a Plant
        Args: name, height, age and color
        """
        super().__init__(name, height, day_old)
        self.color: str = color

    def __str__(self) -> str:
        """Returns Plant info"""
        parent_str: str = super().__str__()
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{parent_str}, {self.color} color"
        )

    def bloom(self) -> str:
        """Returns Plant blooming"""
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    """Definie child class Tree"""
    def __init__(self, name: str, height: int,
                 day_old: int, trunk_diameter: int) -> None:
        """
        Initialize of a Plant
        Args: name, height, age and trunk diamater
        """
        super().__init__(name, height, day_old)
        self.trunk_diameter: int = trunk_diameter

    def __str__(self) -> str:
        """Returns Tree info"""
        parent: str = super().__str__()
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{parent}, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self, ares: int) -> str:
        """Returns how much shade Tree provides"""
        return f"{self.name} provides {ares} square meters of shade"


class Vegetable(Plant):
    """Represents a vegetable with harvest season and nutritional value."""
    def __init__(
        self, name: str, height: int, day_old: int,
        harvest_season: str, nutritional_value: str
    ) -> None:
        """
        Initialize of a Plant
        Args: name, height, age, harvest season and nutritional value
        """
        super().__init__(name, height, day_old)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def __str__(self) -> str:
        """Returns Vegetable info"""
        parent: str = super().__str__()
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{parent}, {self.harvest_season} harvest"
        )

    def nutritional(self) -> str:
        """Return the nutritional information of the vegetable."""
        return f"{self.name} is rich in {self.nutritional_value}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose: Flower = Flower("Rose", 25, 30, "red")
    oak: Tree = Tree("Oak", 500, 1825, 50)
    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(rose)
    print(rose.bloom())
    print()
    print(oak)
    print(oak.produce_shade(78))
    print()
    print(tomato)
    print(tomato.nutritional())
