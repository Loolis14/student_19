#!/usr/bin/env python3

import sys
import math


class Position:
    def __init__(self, x, y, z):
        self.position = (x, y, z)
        print(f"Position created: {self.position}")

    @staticmethod
    def distance(position):
        origin = (0, 0, 0)
        x, y, z = position
        d = math.sqrt((x-origin[0])**2 + (y-origin[1])**2 + (z-origin[2])**2)
        return f"Distance between {origin} and {position}: {d:.2f}"

    @staticmethod
    def parse_coordinates(args):
        coordinates = []
        for arg in args.split(","):
            try:
                int(arg)
            except ValueError:
                raise ValueError(
                    "Second argument should be numbers! "
                    "Usage: \"<x>,<y>,<z>\"")
            else:
                coordinates.append(int(arg))
        if len(coordinates) != 3:
            raise ValueError(
                "Not a valid number of arguments. "
                "Usage: python3 ft_coordinate_system.py \"<x>,<y>,<z>\"")
        return (*coordinates,)

    @staticmethod
    def unpack_tuples(coordinate):
        print("Unpacking demonstration:")
        x, y, z = coordinate.split(",")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


def test_to_do(args):
    if args[0] == "create":
        try:
            coordinates = Position.parse_coordinates(args[1])
        except ValueError as e:
            print("Error found. End of try")
            return e
        else:
            Position(*coordinates)
            print(Position.distance(coordinates))
        finally:
            return "\n=== End of test ==="
    elif args[0] == "parse":
        print(f"Parsing coordinates: \"{args[1]}\"")
        try:
            coordinates = Position.parse_coordinates(args[1])
        except ValueError as e:
            return e
        else:
            print(f"Parsed position: \"{coordinates}\"")
            print(Position.distance(coordinates))
        finally:
            return "\n=== End of test ==="
    elif args[0] == "invalid":
        print(f"Parsing invalid coordinates: {args[1]}")
        try:
            coordinates = Position.parse_coordinates(args[1])
        except ValueError as e:
            return e
        else:
            print(f"Parsed position: {coordinates}")
        finally:
            return "\n=== End of test ==="
    elif args[0] == "unpack":
        Position.unpack_tuples(args[1])
    else:
        print(
            "Unknown command. "
            "First argument available: create, parse, invalid or unpack")
    return "\n=== End of test ==="


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) == 1:
        print("No argument given!")
    elif len(sys.argv) > 3:
        print("Too much argument given")
    else:
        print(test_to_do(sys.argv[1:]))
