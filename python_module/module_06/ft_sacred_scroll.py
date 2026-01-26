#!/usr/bin/env python3

import alchemy


def test_elements():
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(alchemy.elements.create_fire())
    print(alchemy.elements.create_water())
    print(alchemy.elements.create_earth())
    print(alchemy.elements.create_air())
    print("\nTesting package-level access (controlled by __init__.py):")

    for spell in ["create_fire", "create_water", "create_earth", "create_air"]:
        try:
            func = getattr(alchemy, spell)
            print(func())
        except AttributeError:
            print(f"{spell}: AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    test_elements()
