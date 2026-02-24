#!/usr/bin/env python3

from functools import reduce, partial, lru_cache
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
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
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    pass
