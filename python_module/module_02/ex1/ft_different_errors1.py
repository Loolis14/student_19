#!/usr/bin/env python3

def test_error_types(error):
    
    try:
        a = 10 / int(input_str)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        open("")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Caught KeyError: 'missing\_plant'")
    else:
        return a


def garden_operations(data):
    for input_str, error_testing in data:
        print(f"Testing {error_testing}...")
    
    dictionary = {"key": "value"}
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
