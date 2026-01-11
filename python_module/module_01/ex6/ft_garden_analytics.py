#!/usr/bin/env python3

class GardenManager:
    # partager par toutes les instances
    all_gardens = []

    def __init__(self, owner, plants=None):
        self._owner = owner
        self.plants = plants or list()
        self.stats = self.GardenStats(self)
        self.all_gardens.append(self)

    def __str__(self):
        return f"{self._owner}'s garden"

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant} to {self}")
        self.stats.append()

    @classmethod
    def create_garden_network(cls):
        pass

    @staticmethod
    def utility():
        pass

    class GardenStats():
        def __init__(self, garden):
            self.garden = garden

        def how_many_gardens(self):
            return len(self.garden.all_gardens)
        """  def calculate_analytics(plant, growth, types_plants):
            plant_added = 0
            types_plants = 0 """


class Plant:
    def __init__(self, name, height=0):
        self.name = name
        self.height = height

    def grow(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_type(self):
        return "regular"

    def __str__(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    pass


class PrizeFlower(FloweringPlant):
    pass


def create_manager():
    alice = GardenManager("Alice", None)
    bob = GardenManager("Bob", None)
    return (alice, bob)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    create_manager()
    print(GardenManager.GardenStats.how_many_gardens())
