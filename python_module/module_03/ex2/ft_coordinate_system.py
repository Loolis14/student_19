#!/usr/bin/env python3

import math
from typing import Tuple, List


def create_position(x: int, y: int, z: int) -> Tuple[int, int, int]:
    """Create a 3D position tuple."""
    position = (x, y, z)
    print(f"Position created: {position}")
    return position


def distance(position: Tuple[int, int, int]) -> None:
    """Print distance from origin to a position."""
    x, y, z = position
    d = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between (0, 0, 0) and {position}: {d:.2f}")


def parse_coordinates(coord_str: str) -> Tuple[int, int, int]:
    """Transform an arg in a tuple of coordinates."""
    coordinates: List = []
    for arg in coord_str.split(","):
        try:
            int(arg)
        except ValueError:
            raise ValueError(
                "Not a valid number of arguments. "
                "Usage: python3 ft_coordinate_system.py \"<x>,<y>,<z>\"")
        else:
            coordinates.append(int(arg))
    if len(coordinates) != 3:
        raise ValueError("Coordinates must have 3 values (x,y,z)")
    return (*coordinates,)


def parse_coordinates_2(coord_str: str) -> Tuple[int, int, int]:
    """Parse a string like '3,4,0' into a tuple of integers."""
    parts = [int(x) for x in coord_str.split(",")]
    if len(parts) != 3:
        raise ValueError("Coordinates must have 3 values (x,y,z)")
    return tuple(parts)


def unpack_coordinates(position: Tuple[int, int, int]) -> None:
    """Demonstrate tuple unpacking."""
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    position = create_position(10, 20, 5)
    distance(position)
    print("\nParsing coordinates: \"3,4,0\"")
    try:
        position_2 = parse_coordinates("3,4,0")
    except ValueError as e:
        print(e)
    distance(position_2)
    print("\nParsing invalid coordinates: \"abc,def,ghi\"")
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError as e:
        print(e)
    print("\nUnpacking demonstration:")
    unpack_coordinates((3, 4, 0))
