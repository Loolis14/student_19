#!/usr/bin/env python3

def check_temperature(temp_str):
    """
    Function to test if the temperature is a number and between 0 and 40
    """
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp_str = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    else:
        if temp_str > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            return None
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
            return temp_str


def test_temperature_input():
    """
    Give examples to test a function
    """
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
