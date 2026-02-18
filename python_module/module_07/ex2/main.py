"""Third exercise main."""

from ex0.Card import Card, Rarity
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical
from ex2.Combatable import Combatable


def display_capabilities(obj: EliteCard) -> None:
    """Display methods that Elite card inherits."""
    parents = [Card, Combatable, Magical]

    print("EliteCard capabilities:")

    for parent in parents:
        methods = [method for method in dir(parent)
                   if not method.startswith("__")
                   and method in dir(obj)
                   and not method.startswith("_")]
        print(f"- {parent.__name__}: {methods}")


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")
    print()
    display_capabilities(EliteCard)
    arcane_warrior = EliteCard("Arcane Warrior",
                               5, Rarity.LEGENDARY, 10, 3, 5, 8)
    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    print(f'Attack result: {arcane_warrior.attack("Enemy")}')
    print(f'Defense result: {arcane_warrior.defend(5)}')

    print("\nMagic phase:")
    spell_used = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f'Spell cast: {spell_used}')
    print(f'Mana channel: {arcane_warrior.channel_mana(3)}')
    print("\nMultiple interface implementation successful!")
