#!/usr/bin/env python3

def test_error_types(input_str):
    try:
        input_str = int(input_str)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        input_str
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        open("")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        input_str = {}
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    else:
        return a


def garden_operations():
    for input_str, error_testing in data:
        print(f"Testing {error_testing}...")
    
    dictionary = {"key"
                  : "value"}
    test_error_types(dictionary)
    print("All error types tested successfully!")


if __name__ == "__main__":
    data = [
        ("abc", "ValueError"),
        ("0", " ZeroDivisionError"),
        ("", " FileNotFoundError"),
        ("abc", " KeyError"),
        # mutiple error together ?
    ]
    garden_operations(data)
