#!/usr/bin/env python3

"""Fourth Exercise."""


class PlantError(Exception):
    """Except a plant error."""

    pass


class WaterLvlError(Exception):
    """Except an error in the water level."""

    pass


class SunError(Exception):
    """Except a sun error."""

    pass


def check_plant_health(plant_name: str | None, water_level: int,
                       sunlight_hours: int) -> str:
    """Check if the plant is healthy."""
    if not plant_name:
        raise PlantError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise WaterLvlError(
            f"Error: Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise WaterLvlError(
            f"Error: Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise SunError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise SunError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test the check plant function."""
    print("\nTesting with good values")
    try:
        print(check_plant_health("tomato", 5, 9))
    except (PlantError, WaterLvlError, SunError) as e:
        print(e)
    print("\nTesting with bad plant name")
    try:
        print(check_plant_health(None, 5, 9))
    except (PlantError, WaterLvlError, SunError) as e:
        print(e)
    print("\nTesting with bad water level")
    try:
        print(check_plant_health("tomato", -2, 9))
    except (PlantError, WaterLvlError, SunError) as e:
        print(e)
    print("\nTesting with bad sunlight hours")
    try:
        print(check_plant_health("tomato", 5, 50))
    except (PlantError, WaterLvlError, SunError) as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
