#!/usr/bin/env python3

import functools
import time

def spell_timer(func: callable) -> callable:
    @functools.wraps(func) # pour ne pas perdre les meta
    def wrapper():
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func()
        end_time = time.time()
        time_ = end_time - start_time  
        print(f"Spell completed in {time_} seconds")
        return result
    return func

def power_validator(min_power: int) -> callable:
    pass


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass



def test() -> None:
    test_powers = [28, 5, 16, 8]
    spell_names = ['meteor', 'darkness', 'earthquake', 'tornado']
    mage_names = ['Morgan', 'River', 'Ember', 'Ash', 'Luna', 'Rowan']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']


if __name__ == "__main__":
    test()
