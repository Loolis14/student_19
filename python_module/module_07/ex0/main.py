#!/usr/bin/env python3

from CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    dragon: CreatureCard = CreatureCard('Fire Dragon', 5, 'Legendary', 5, 7)
    print(f'CreatureCard Info: {dragon.get_card_info()}')
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state: dict = {
        'card_played': 'Fire Dragon',
        'mana_used': 5,
        'effect': 'Creature summoned to battlefield'
    }
    print('Play result: ', dragon.play(game_state))
    print('\nFire Dragon attacks Goblin Warrior:')
    print('Attacke result: ', dragon.attack_target("Goblin Warrior"))
    print('\nTesting insufficient mana (3 available):')
    print(f"Playable: {dragon.is_playable(3)}")
    print('\nAbstract pattern successfully demonstrated!')
