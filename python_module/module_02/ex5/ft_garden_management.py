#!/usr/bin/env python3

"""Fifth exercise."""

from typing import List


class GardenError(Exception):
    """Except a garden error."""

    pass


class PlantError(GardenError):
    """Except a plant error."""

    pass


class WaterLvlError(GardenError):
    """Except an error in the water level."""

    pass


class SunError(GardenError):
    """Except a sun error."""

    pass


class TankError(GardenError):
    """Except a tank error."""

    pass


class Plant:
    """Define a class for the plant."""

    def __init__(self, name: str | None, water: int, sun: int) -> None:
        """Initialize a plant."""
        if not name:
            raise PlantError("Error: Plant name cannot be empty!")
        self.name = name
        self.water = water
        self.sun = sun

    def check_healthy(self) -> str:
        """Check the health of the plant."""
        if self.water < 1:
            raise WaterLvlError(
                f"Error: Water level {self.water} is too low (min 1)")
        elif self.water > 10:
            raise WaterLvlError(
                f"Error: Water level {self.water} is too high (max 10)")
        if self.sun < 2:
            raise SunError(
                f"Error: sun hours {self.sun} is too low (min 2)")
        elif self.sun > 12:
            raise SunError(
                f"Error: sun hours {self.sun} is too high (max 12)")
        return f"{self.name}: healthy (water: {self.water}, sun: {self.sun})"


class GardenManager:
    """Define a manager for the gardener."""

    def __init__(self) -> None:
        """Initialize the garden with all the plant."""
        self.plants: List[Plant] = []

    def add_plants(self, plant_name: str | None, water: int, sun: int) -> None:
        """Add plant to a garden."""
        try:
            plant = Plant(plant_name, water, sun)
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, tank: "TankSystem") -> None:
        """Water all plant in the garden."""
        WateringSystem.opening_system()
        try:
            for plant in self.plants:
                try:
                    TankSystem.use(tank, 1)
                except TankError as e:
                    print(e)
                plant.water += 1
                print(f"Watering {plant.name} - success")
            print("Watering completed successfully!")
        finally:
            WateringSystem.closing_system()

    def check_healthy(self) -> None:
        """Check if the plant is healthy."""
        for plant in self.plants:
            try:
                print(plant.check_healthy())
            except (WaterLvlError, SunError) as e:
                print(e)


class WateringSystem:
    """Define a class to control the watering system."""

    count_opening = 0
    count_closing = 0

    @classmethod
    def opening_system(cls) -> None:
        """Open the watering system."""
        print("Opening watering system")
        WateringSystem.count_opening += 1

    @classmethod
    def closing_system(cls) -> None:
        """Close the watering system."""
        cls.count_closing += 1
        print("Closing watering system (cleanup)")

    @classmethod
    def get_state(cls) -> str:
        """Get the status of the watering system."""
        if cls.count_opening == cls.count_closing:
            return "\nCleanup always happens, even with errors!"
        else:
            return "\nYou failed!"


class TankSystem:
    """Define a class for the tank."""

    def __init__(self, water: int) -> None:
        """Initiliaze the tank system."""
        self.water = water

    def refill(self, quantity: int) -> None:
        """Refill the water on the tank."""
        self.water += quantity
        print("System recovered and continuing...")

    def use(self, quantity: int) -> None:
        """Use water on the tank."""
        if self.water - quantity < 0:
            raise TankError("Caught GardenError: Not enough water in tank")
        else:
            self.water -= quantity


def add_plant(bob: GardenManager) -> None:
    """Add plant to a garden."""
    print("\nAdding plants to garden...")
    bob.add_plants("tomato", 4, 8)
    bob.add_plants("lettuce", 10, 6)
    bob.add_plants(None, 2, 6)


def watering(bob: GardenManager, tank: TankSystem) -> None:
    """Water the plant on a garden."""
    print("\nWatering plants...")
    try:
        bob.water_plants(tank)
    except TankError as e:
        print(e)


def checking_plant_health(bob: GardenManager) -> None:
    """Check the health on a garden."""
    print("\nChecking plant health...")
    for plant in bob.plants:
        try:
            plant.check_healthy()
        except (WaterLvlError, SunError) as e:
            print(e)


def recovery_tank(bob: GardenManager, tank: TankSystem) -> None:
    """Use and refill the tank water."""
    print("\nTesting error recovery...")
    try:
        tank.use(3)
    except TankError as e:
        print(e)
        tank.refill(10)


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    bob: GardenManager = GardenManager()
    tank: TankSystem = TankSystem(2)
    add_plant(bob)
    watering(bob, tank)
    print("\nChecking plant health...")
    bob.check_healthy()
    recovery_tank(bob, tank)
    print("\nGarden management system test complete!")
