#!/usr/bin/env python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multiply(x: int):
        return (base_spell(x) * multiplier)
    return multiply


def conditional_caster(condition: callable, spell: callable) -> callable:
    def returning_condition(mana: int, spells: str):
        if condition(mana):
            return spell(spells)
        return 'Spell fizzled'
    return returning_condition


def spell_sequence(spells: list[callable]) -> callable:
    def result_spell(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return result_spell


def test() -> None:
    print("Testing spell combiner...")

    def heal(target: str) -> str:
        return f'heals {target}'

    def hit(target: str) -> str:
        return f'hits {target}'

    combined = spell_combiner(hit, heal)
    print('Combined spell result: Fireball', combined('Dragon'))

    print("\nTesting power amplifier...")

    def base_spell(x: int) -> int:
        return x

    multiply = power_amplifier(base_spell, 3)
    print(f'Original: {base_spell(10)}, Amplified: {multiply(10)}')

    print("\nTesting conditional caster...")

    def condition(x: int) -> bool:
        if x > 10:
            return True
        return False

    def spell(spell: str) -> str:
        return spell

    conditionning = conditional_caster(condition, spell)
    print(conditionning(60, 'Fireball'))

    print("\nTesting spell sequence...")
    spell_sequences = spell_sequence([heal, hit, spell])
    print(spell_sequences('Goblin'))


if __name__ == "__main__":
    test()
