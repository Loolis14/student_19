from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Rarity
from ex1.Deck import Deck

if __name__ == "__main__":
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

"""
Building deck with different card types...
Deck stats: {'total_cards': 3,'creatures': 1,'spells': 1,
'artifacts': 1,'avg_cost': 4.0}
Drawing and playing cards:
Drew: Lightning Bolt (Spell)
Play result: {'card_played': 'Lightning Bolt'
,
'mana_used': 3,
'effect': 'Deal 3 damage to target'}
Drew: Mana Crystal (Artifact)
Play result: {'card_played': 'Mana Crystal'
,
'mana_used': 2,
'effect': 'Permanent: +1 mana per turn'}
Drew: Fire Dragon (Creature)
Play result: {'card_played': 'Fire Dragon'
,
'mana_used': 5,
'effect': 'Creature summoned to battlefield'}
Polymorphism in action: Same interface, different card behaviors!
"""
