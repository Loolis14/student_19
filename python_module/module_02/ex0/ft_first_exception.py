#!/usr/bin/env python3

"""First exercise."""


def check_temperature(temp_str: str) -> int | None:
    """Test if the temperature is a number and between 0 and 40."""
    print(f"\nTesting temperature: {temp_str}")
    try:
        tmp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    else:
        if tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
            return None
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {tmp}°C is perfect for plants!")
            return tmp


def test_temperature_input() -> None:
    """Test the check temperature function."""
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
