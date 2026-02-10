#!/usr/bin/env python3

"""Third Exercise."""


class GardenError(Exception):
    """Alerte on garden error."""
    pass


class PlantError(GardenError):
    """Alerte on plant error."""
    pass


class WaterError(GardenError):
    """Alerte on water error."""
    pass


def check_plant_error() -> None:
    """Test if the plant name error works."""
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def check_water_error() -> None:
    """Test if the water name error works."""
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    check_plant_error()
    print()
    check_water_error()
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error {e}")
    print("\nAll custom error types work correctly!")
