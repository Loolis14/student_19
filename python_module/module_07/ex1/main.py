"""Second exercise main."""

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Rarity
from ex1.Deck import Deck

if __name__ == "__main__":
    game_state = {
        'health': 30,
        'mana': 20,
        'active_effect': [],
        'creature': []
    }
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 5, 7)
    spell = SpellCard("Lightning Bolt", 3, Rarity.COMMON,
                      'Deal 3 damage to target')
    artificats: ArtifactCard = ArtifactCard("Mana Crystal", 2,
                                            Rarity.LEGENDARY, 10,
                                            "Permanent: +1 mana per turn")
    morgane_deck: Deck = Deck()
    morgane_deck.add_card(creature)
    morgane_deck.add_card(spell)
    morgane_deck.add_card(artificats)

    print(f'Deck stats: {morgane_deck.get_deck_stats()}')
    print("\nDrawing and playing cards:")
    card = morgane_deck.draw_card()
    print(f'\nDrew: {card.name}')
    print(f'Play result: {card.play(game_state)}')
    morgane_deck.remove_card(card.name)
    card = morgane_deck.draw_card()
    print(f'\nDrew: {card.name}')
    print(f'Play result: {card.play(game_state)}')
    morgane_deck.remove_card(card.name)
    card = morgane_deck.draw_card()
    print(f'\nDrew: {card.name}')
    print(f'Play result: {card.play(game_state)}')
    morgane_deck.remove_card(card.name)

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")
