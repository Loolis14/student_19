#!/usr/bin/env python3

import functools
import time
from typing import Any


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_ = end_time - start_time
        print(f"Spell completed in {time_} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 2:
            for c in name:
                if c.isalpha() or c.isspace():
                    continue
                else:
                    return False
            return True
        return False

    @power_validator(10)
    @retry_spell(3)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def test() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        return "Result: Fireball cast!"
    print(fireball())

    print("\nTesting MageGuild...")
    print("\nTesting mage name...")
    imardin = MageGuild()
    mage_names = ['Morgan', 'Ember', 'Ash', 'Luna', 'Rowan']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name', 'Shrek!']
    acc = 0
    for name in mage_names:
        if not imardin.validate_mage_name(name):
            acc += 1
    print(f'{"True" if acc == 0 else "False"}')
    acc = 0
    for name in invalid_names:
        if imardin.validate_mage_name(name):
            acc += 1
    print(f'{"False" if acc == 0 else "True"}')

    print("\nTesting cast spell...")
    test_powers = [28, 5, 16, 8]
    spell_names = ['meteor', 'darkness', 'earthquake', 'tornado']
    for i in range(4):
        print(imardin.cast_spell(spell_names[i], test_powers[i]))


if __name__ == "__main__":
    test()
