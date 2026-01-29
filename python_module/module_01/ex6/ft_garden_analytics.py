#!/usr/bin/env python3

from typing import List, Dict


class GardenManager:
    """Handle multiple gardens"""
    gardens: Dict = {}

    def __init__(self, owner: str) -> None:
        """
        Initialize a garden for
        Args:
        - a owner (str)
        - and the plants (list or none) he owns
        """
        self._owner: str = owner
        self.plants: List["Plant"] = []
        self.score: int = 0
        self.stats = self.GardenStats(self)
        GardenManager.gardens[owner] = self

    def __str__(self) -> str:
        """Returns garden info"""
        return f"{self._owner}'s garden"

    def add_plant(self, plant: "Plant"):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self}")

    def help_grow(self, growth: int) -> None:
        print(f"{self._owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(growth)
            self.stats.total_growth += growth

    @classmethod
    def create_garden_network(cls) -> Dict:
        alice.score = 218
        bob.score = 92
        score: Dict = {}
        for owner, garden in cls.gardens.items():
            score[owner] = garden.score
        return score

    @classmethod
    def total_garden(cls) -> int:
        return len(cls.gardens)

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    class GardenStats():
        """Calculates statistics"""

        def __init__(self, garden: "GardenManager") -> None:
            self.garden = garden
            self.total_growth: int = 0

        def report(self) -> None:
            print(f"\n=== {self.garden._owner} Report ===")
            print("Plants in garden:")
            for plant in self.garden.plants:
                print(f"- {plant}")

        def count_plants(self) -> int:
            return len(self.garden.plants)

        def types_plant(self) -> str:
            types: Dict = {'prize_flowers': 0, 'flowering': 0, 'regular': 0}
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    types["prize_flowers"] += 1
                elif isinstance(plant, FloweringPlant):
                    types["flowering"] += 1
                elif isinstance(plant, Plant):
                    types["regular"] += 1
            return (f"Plant types: {types['regular']} regular, "
                    f"{types['flowering']} flowering, "
                    f"{types['prize_flowers']} prize flowers")


class Plant:
    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def __str__(self):
        return f"{self.name}: {self.height}cm"

    def grow(self, amount: int) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_type(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    """Represents a plant with ability to bloom."""

    def __init__(self, name, height, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color

    def __str__(self):
        parent: str = super().__str__()
        return f"{parent}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Represents a flower with a prize"""

    def __init__(self, name, height, color, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize: int = prize

    def __str__(self):
        parent: str = super().__str__()
        return f"{parent}, Prize points: {self.prize}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    # Garden create
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    # add plants in garden
    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print()
    alice.help_grow(1)
    alice.stats.report()

    print()
    print(f"Plants added: {alice.stats.total_growth}, "
          f"Total growth: {alice.stats.count_plants()}cm")
    print(alice.stats.types_plant())

    print()
    print("Height validation test:", alice.validate_height(10))
    print("Garden scores - ", GardenManager.create_garden_network())
    print("Total gardens managed:", GardenManager.total_garden())
