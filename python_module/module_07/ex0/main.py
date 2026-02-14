#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity

if __name__ == "__main__":
    game_state: dict = {
            'health': 10,
            'mana': 6,
            'creature': []
        }

    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    dragon: CreatureCard = CreatureCard('Fire Dragon', 5,
                                        Rarity.LEGENDARY, 7, 5)
    print(f'CreatureCard Info: {dragon.get_card_info()}')
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(game_state['mana'])}")
    print('Play result: ', dragon.play(game_state))

    print('\nFire Dragon attacks Goblin Warrior:')
    print('Attacke result: ', dragon.attack_target("Goblin Warrior"))
    print('\nTesting insufficient mana (3 available):')
    print(f"Playable: {dragon.is_playable(game_state['mana'])}")
    print('\nAbstract pattern successfully demonstrated!')
