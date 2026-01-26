#!/usr/bin/env python3

import alchemy.grimoire as gr


def test():
    print("\nTesting ingredient validation:")
    print(f'validate_ingredients("fire air"): '
          f'{gr.validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{gr.validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{gr.record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{gr.record_spell("Dark Magic", "shadow")}')

    print("\nTesting late import technique:")
    print(f'record_spell("Lightning", "air"): '
          f'{gr.record_spell("Lightning", "air")}')

    print("\nCircular dependency curse avoided using late imports!")


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")
    test()
    print("All spells processed safely!")
