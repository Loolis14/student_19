#!/usr/bin/env python3


def mage_counter() -> callable:
    i = 0

    def count_time() -> int:
        nonlocal i
        i += 1
        return i

    return count_time


def spell_accumulator(initial_power: int) -> callable:
    i = initial_power

    def count_power() -> int:
        nonlocal i
        i += initial_power
        return i

    return count_power


def enchantment_factory(enchantment_type: str) -> callable:
    def create_enchant(item: str) -> str:
        return f'{enchantment_type} {item}'
    return create_enchant


def memory_vault() -> dict[str, callable]:
    storage = {}

    def store(key: str, value: str) -> None:
        storage[key] = value

    def recall(key: str) -> None:
        return storage.get(key, 'Memory not found')

    return {
        'store': store,
        'recall': recall
    }


def test() -> None:
    print("Testing mage counter...")
    count_mage = mage_counter()
    for i in range(1, 4):
        print(f'Call {i}: {count_mage()}')

    print("\nTesting spell accumulator...")
    count_spell = spell_accumulator(5)
    for i in range(1, 4):
        print(f'Call {i}: {count_spell()} power')

    print("\nTesting enchantment factory...")
    flaming_factory = enchantment_factory('Flaming')
    frozen_factory = enchantment_factory('Frozen')
    print(flaming_factory('Sword'))
    print(frozen_factory('Shield'))

    print("\nTesting memory vault...")
    memory_function = memory_vault()
    memory_function['store']('shrek', 'marais')
    print(memory_function['recall']('shrek'))


if __name__ == "__main__":
    test()
