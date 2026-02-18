"""Concrete factory fantasy cards."""

from ex0 import Card, CreatureCard, Rarity
from ex1 import ArtifactCard, SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Create fantasy cards."""

    def __init__(self) -> None:
        """Keep all the cards created."""
        self.cards: list[Card] = []

    def create_creature(self, name_or_power) -> Card:
        """Create creature cards."""
        if name_or_power == 'dragon':
            dragon = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY, 7, 5)
            self.cards.append(dragon)
            return dragon
        elif name_or_power == 'goblin':
            goblin = CreatureCard('Goblin Warior', 2, Rarity.COMMON, 5, 1)
            self.cards.append(goblin)
            return goblin
        else:
            peon = CreatureCard('Peon', 1, Rarity.COMMON, 1, 2)
            self.cards.append(peon)
            return peon

    def create_spell(self, name_or_power) -> Card:
        """Create spell cards."""
        if name_or_power == 'lightning':
            lightning = SpellCard('Lightning Bolt', 3,
                                  Rarity.LEGENDARY, '+3 damage')
            self.cards.append(lightning)
            return lightning
        elif name_or_power == 'fireball':
            fireball = SpellCard('Fireball', 2, Rarity.COMMON, 'damage')
            self.cards.append(fireball)
            return fireball
        else:
            ice = SpellCard('Ice arrow', 4, Rarity.COMMON, 'damage')
            self.cards.append(ice)
            return ice

    def create_artifact(self, name_or_power) -> Card:
        """Create artifact cards."""
        if name_or_power == 'mana_ring':
            ring = ArtifactCard('Mana_ring', 4, Rarity.LEGENDARY, 4, 'damage')
            self.cards.append(ring)
            return ring
        healing = ArtifactCard('Healing Beam', 1, Rarity.COMMON, 4, 'heal')
        self.cards.append(healing)
        return healing

    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck."""
        pass

    def get_supported_types(self) -> dict:
        """Return the types supported."""
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball', 'lightning'],
            'artifacts': ['mana_ring']
            }
