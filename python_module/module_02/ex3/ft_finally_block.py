#!/usr/bin/env python3

"""Fourth exercise."""


class Plant():
    """Define a plant."""

    def __init__(self, name: str) -> None:
        """Initialize a plant."""
        super().__init__()
        if name:
            self.name = name
        else:
            raise PlantNameError(str(name))


class PlantNameError(Exception):
    """Define a plant name error"""

    def __init__(self, message):
        """Initialize a plant name error."""
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """Return a custom message."""
        return f"Error: Cannot water {self.message} - invalid plant!"


class WateringSystem:
    """Define the watering system."""

    count_opening = 0
    count_closing = 0

    @classmethod
    def opening_system(cls) -> None:
        """Open the watering system."""
        cls.count_opening += 1

    @classmethod
    def closing_system(cls) -> None:
        """Close the watering system."""
        cls.count_closing += 1
        print("Closing watering system (cleanup)")

    @classmethod
    def get_state(cls) -> str:
        """Get the state of watering system."""
        if cls.count_opening == cls.count_closing:
            return "\nCleanup always happens, even with errors!"
        else:
            return "\nYou failed!"


def water_plants(plant_list: list) -> None:
    """Create and Water each plant in the garden."""
    WateringSystem.opening_system()
    try:
        for plant in plant_list:
            plante = Plant(plant)
            print(f"Watering {plante.name}")
        print("Watering completed successfully!")
    except PlantNameError as e:
        print(e)
    finally:
        WateringSystem.closing_system()


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plant_list: list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    plant_list = ["tomato", None]
    print("\nTesting with error...")
    water_plants(plant_list)
    print(WateringSystem.get_state())
