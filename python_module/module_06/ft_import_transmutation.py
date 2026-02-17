#!/usr/bin/env python3

from alchemy import healing_potion as heal
from alchemy import elements, potions
from alchemy import create_water


def test_potions():
    print("=== Import Transmutation Mastery ===")

    print("\nMethod 1- Full module import:")
    print(f"alchemy.elements.create_fire(): {elements.create_fire()}")

    print("\nMethod 2- Specific function import:")
    print(f"create_water(): {create_water()}")

    print("\nMethod 3- Aliased import:")
    print(f"heal(): {heal()}")

    print("\nMethod 4- Multiple imports:")
    test = [
        (elements, "create_earth"),
        (elements, "create_fire"),
        (potions, "strength_potion")
    ]
    for module, function in test:
        try:
            func = getattr(module, function)
            print(f"{function}(): {func()}")
        except AttributeError:
            print(f"{function}: AttributeError - not exposed")


if __name__ == "__main__":
    test_potions()
    print("\nAll import transmutation methods mastered!")
