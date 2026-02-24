#!/usr/bin/env python3

"""Fourth exercise."""

from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Use of reduce."""
    match operation:
        case "add":
            return reduce(operator.add, spells)
        case "multiply":
            return reduce(operator.mul, spells)
        case "max":
            return reduce(max, spells)
        case "min":
            return reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Use of partial module."""
    fire_enchant = partial(base_enchantment, power=50, element='fire')
    ice_enchant = partial(base_enchantment, power=50, element='ice')
    lightning_enchant = partial(base_enchantment, power=50, element='light')

    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Use of cache to store data executed."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Use of dispatch with the first argument given."""
    @singledispatch
    def display(value) -> str:
        """Take a type unsported."""
        return "Type not supported"

    @display.register
    def _(value: int) -> str:
        """Take an int type."""
        return f"{value} Damage spell"

    @display.register
    def _(value: str) -> str:
        """Take a str type."""
        return f"Enchantement spell: {value}!"

    @display.register
    def _(value: list) -> str:
        """Take a list type."""
        return f'Multicast spells! {" and ".join(str(v) for v in value)}'

    return display


def test() -> None:
    """Test for the function created."""
    print("\nTesting spell reducer...")
    spell_powers = [47, 23, 34, 29, 24, 43]
    print(f'Sum: {spell_reducer(spell_powers, "add")}')
    print(f'Product: {spell_reducer(spell_powers, "multiply")}')
    print(f'Max: {spell_reducer(spell_powers, "max")}')
    print(f'Min: {spell_reducer(spell_powers, "min")}')

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f'{target} hits with {power} {element} damage!'
    
    base = partial_enchanter(base_enchantment)
    print(base['fire_enchant'](target='Dragon'))
    print(base['ice_enchant'](target='Goblin'))
    print(base['lightning_enchant'](target='Tortle'))

    print("\nTesting memoized fibonacci...")
    fibonacci_tests = [17, 11, 11]
    for n in fibonacci_tests:
        print(f'Fib({n}): {memoized_fibonacci(n)}')

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(30))
    print(dispatch('shrek'))
    print(dispatch([1, 'shrek']))


if __name__ == "__main__":
    test()